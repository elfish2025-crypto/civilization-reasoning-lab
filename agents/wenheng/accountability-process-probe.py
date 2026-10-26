#!/usr/bin/env python3
"""Constructed serial ledger experiment; no LLM, Agent, network or real tools.

Run in a fresh output directory. The controller is trusted and assigns identity
to a private child-process pipe. This is not an authentication security test.
Only worker processes restart; the gate and SQLite connection remain alive.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import selectors
import sqlite3
import subprocess
import sys
import time
import uuid


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def send(stream, obj):
    stream.write(json.dumps(obj, sort_keys=True) + "\n")
    stream.flush()


def child(role, receipt_path):
    send(sys.stdout, {"pid": os.getpid(), "role": role})
    for line in sys.stdin:
        request = json.loads(line)
        if role == "worker":
            # Stateless relay: no identity, ledger, outcome or feedback input.
            if set(request) != {"request_id", "item"}:
                raise ValueError("Unexpected worker input")
            send(sys.stdout, request)
        else:
            record = {**request, "tool_pid": os.getpid(),
                      "received_at": now(), "executed": True,
                      "effect": "append_dummy_receipt"}
            with open(receipt_path, "a", encoding="utf-8") as out:
                out.write(json.dumps(record, sort_keys=True) + "\n")
                out.flush()
                os.fsync(out.fileno())
            send(sys.stdout, record)


class Process:
    def __init__(self, role, cwd, events, timeout, receipt_path=None, subject=None):
        self.events, self.timeout = events, timeout
        self.role, self.subject = role, subject
        self.instance = str(uuid.uuid4())
        args = [sys.executable, str(Path(__file__).resolve()), "--child", role]
        if receipt_path is not None:
            args += ["--receipt-path", str(receipt_path)]
        self.proc = subprocess.Popen(args, stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE, text=True,
                                     cwd=cwd, close_fds=True)
        self.selector = selectors.DefaultSelector()
        self.selector.register(self.proc.stdout, selectors.EVENT_READ)
        greeting = self.read()
        if greeting != {"pid": self.proc.pid, "role": role}:
            raise ValueError("Child handshake mismatch")
        events.append({"kind": "start", "at": now(),
                       "monotonic_ns": time.monotonic_ns(),
                       "role": role, "instance": self.instance,
                       "pid": self.proc.pid, "bound_subject": subject,
                       "binding_basis": "controller_owned_private_pipe"})

    def read(self):
        if not self.selector.select(self.timeout):
            raise TimeoutError("Child response timed out")
        line = self.proc.stdout.readline()
        if not line:
            raise RuntimeError("Child ended before response")
        return json.loads(line)

    def call(self, payload):
        send(self.proc.stdin, payload)
        return self.read()

    def stop(self):
        self.proc.stdin.close()
        forced = False
        try:
            code = self.proc.wait(timeout=self.timeout)
        except subprocess.TimeoutExpired:
            forced = True
            self.proc.kill()
            code = self.proc.wait()
        self.events.append({"kind": "stop", "at": now(),
                            "monotonic_ns": time.monotonic_ns(),
                            "role": self.role, "instance": self.instance,
                            "pid": self.proc.pid, "returncode": code,
                            "forced_kill": forced})
        self.selector.close()
        self.proc.stdout.close()
        if forced or code:
            raise RuntimeError("Child did not exit cleanly")


class Gate:
    def __init__(self, path, sticky):
        self.db = sqlite3.connect(path)
        self.db.execute("CREATE TABLE events (seq INTEGER PRIMARY KEY, body TEXT NOT NULL)")
        self.sticky, self.denied = sticky, set()
        self.instance = str(uuid.uuid4())

    def append(self, event):
        self.db.execute("INSERT INTO events(body) VALUES (?)",
                        (json.dumps(event, sort_keys=True),))
        self.db.commit()

    def history(self):
        return [{"seq": seq, **json.loads(body)} for seq, body in
                self.db.execute("SELECT seq,body FROM events ORDER BY seq")]

    def decide(self, subject, item):
        pair = (subject, item)
        if self.sticky and pair in self.denied:
            return "deny", "stale_deny_cache", False
        actions, opened = {}, {}
        for event in self.history():
            if event["kind"] == "action":
                actions[event["id"]] = (event["subject"], event["item"])
            elif event["kind"] == "open":
                owner = (event["subject"], event["item"])
                if actions[event["source_event"]] != owner:
                    raise ValueError("Obligation origin mismatch")
                opened[event["id"]] = owner
            elif event["kind"] == "close":
                if event["authority"] != "test_controller":
                    raise ValueError("Invalid fixture settlement authority")
                del opened[event["obligation"]]
            else:
                raise ValueError("Unknown ledger event")
        if pair in opened.values():
            if self.sticky:
                self.denied.add(pair)
            return "deny", "open_obligation", True
        return "allow", "no_open_obligation", True


def receipts(path):
    return [json.loads(line) for line in path.read_text().splitlines()]


def run_trace(plan, mode, trace, root):
    trace_dir = root / (mode + "-" + trace)
    trace_dir.mkdir()
    receipt_path = trace_dir / "tool-receipts.jsonl"
    receipt_path.touch(exist_ok=False)
    database_path = trace_dir / "ledger.sqlite"
    gate = Gate(database_path, sticky=(mode == "sticky_deny_cache"))
    life, workers, all_processes, observations = [], {}, [], []
    fixture = plan["identities"]
    items = plan["items"]
    tool = Process("tool", trace_dir, life, plan["timeout_seconds"], receipt_path)
    all_processes.append(tool)
    snapshots, transitions, worker_inputs = [], [], []
    try:
        for step in plan["traces"][trace]:
            if "fixture" in step:
                action = step["fixture"]
                subject = fixture[step["subject"]]
                if action == "open":
                    gate.append({"id": "origin", "kind": "action",
                                 "subject": subject, "item": items["x"],
                                 "evidence_kind": "controller_injected_fixture"})
                    gate.append({"id": "obligation", "kind": "open",
                                 "subject": subject, "item": items["x"],
                                 "source_event": "origin"})
                elif action == "close":
                    gate.append({"id": "settlement", "kind": "close",
                                 "obligation": "obligation",
                                 "authority": "test_controller",
                                 "basis": "predeclared_fixture_correction_complete"})
                else:
                    raise ValueError("Unknown fixture operation")
                snapshots.append({"after_fixture": action, "at": now(),
                                  "events": gate.history()})
                continue
            subject = fixture[step["subject"]]
            if step.get("restart"):
                previous = workers.pop(subject)
                before = gate.history()
                previous.stop()
                current = Process("worker", trace_dir, life,
                                  plan["timeout_seconds"], subject=subject)
                workers[subject] = current
                all_processes.append(current)
                transitions.append({"before_case": step["case"],
                                    "old_instance": previous.instance,
                                    "new_instance": current.instance,
                                    "old_pid": previous.proc.pid,
                                    "new_pid": current.proc.pid,
                                    "old_exit_confirmed_before_spawn": True,
                                    "same_gate_instance": gate.instance,
                                    "ledger_equal_before_after": before == gate.history()})
            if subject not in workers:
                workers[subject] = Process("worker", trace_dir, life,
                                           plan["timeout_seconds"], subject=subject)
                all_processes.append(workers[subject])
            worker = workers[subject]
            request = {"request_id": mode + ":" + trace + ":" + step["case"],
                       "item": items[step["item"]]}
            proposal = worker.call(request)
            if proposal != request:
                raise ValueError("Unexpected proposal")
            worker_inputs.append({"instance": worker.instance, "input": request,
                                  "output": proposal})
            # Bind to the process object controlled by the parent, not any
            # asserted identity in the worker's proposal. No expected result
            # or case name is passed into the policy decision.
            decision, basis, read = gate.decide(worker.subject, proposal["item"])
            before_receipts = receipts(receipt_path)
            ack = None
            if decision == "allow":
                ack = tool.call({**proposal, "subject": worker.subject})
            after_receipts = receipts(receipt_path)
            new_receipts = after_receipts[len(before_receipts):]
            dispatch_ok = (new_receipts == [ack] if decision == "allow"
                           else not new_receipts)
            expected_count = 1 if step["expected"] == "allow" else 0
            observations.append({**step, "at": now(),
                                 "actual_subject": worker.subject,
                                 "request": request, "worker_instance": worker.instance,
                                 "worker_pid": worker.proc.pid, "gate_instance": gate.instance,
                                 "ledger": gate.history(), "ledger_read": read,
                                 "actual_decision": decision, "decision_basis": basis,
                                 "deny_cache": sorted(gate.denied),
                                 "tool_receipts_before": len(before_receipts),
                                 "tool_receipts_after": len(after_receipts),
                                 "new_tool_receipts": new_receipts,
                                 "dispatch_matches_decision": dispatch_ok,
                                 "decision_matches_plan": decision == step["expected"],
                                 "effect_matches_plan": len(new_receipts) == expected_count})
    finally:
        for process in reversed(all_processes):
            if not process.proc.stdin.closed:
                process.stop()
        final_ledger = gate.history()
        gate.db.close()
    return {"mode": mode, "trace": trace, "gate_instance": gate.instance,
            "process_lifecycle": life, "worker_restarts": transitions,
            "worker_io": worker_inputs, "fixture_snapshots": snapshots,
            "observations": observations, "final_ledger": final_ledger,
            "tool_receipts": receipts(receipt_path),
            "database_sha256": sha(database_path.read_bytes()),
            "tool_receipts_sha256": sha(receipt_path.read_bytes())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--child", choices=["worker", "tool"])
    parser.add_argument("--receipt-path", type=Path)
    parser.add_argument("--plan", type=Path)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    if args.child:
        child(args.child, args.receipt_path)
        return
    if not args.plan or not args.output_dir:
        parser.error("--plan and --output-dir are required")
    plan_bytes = args.plan.read_bytes()
    plan = json.loads(plan_bytes)
    script_sha = sha(Path(__file__).read_bytes())
    if plan["script_sha256"] != script_sha:
        raise ValueError("Script differs from pre-run plan")
    args.output_dir.mkdir(exist_ok=False)
    result = {"kind": "constructed_process_ledger_probe", "started_at": now(),
              "script_sha256": script_sha, "plan_sha256": sha(plan_bytes),
              "python": platform.python_version(), "sqlite": sqlite3.sqlite_version,
              "platform": platform.platform(), "controller_pid": os.getpid(),
              "plan": plan, "runs": []}
    try:
        for mode in plan["modes"]:
            for trace in plan["traces"]:
                result["runs"].append(run_trace(plan, mode, trace, args.output_dir))
        result["summary"] = []
        for mode in plan["modes"]:
            relevant = [r for r in result["runs"] if r["mode"] == mode]
            rows = [row for r in relevant for row in r["observations"]]
            mismatches = [row["case"] for row in rows if not row["decision_matches_plan"]]
            result["summary"].append({"mode": mode, "decisions": len(rows),
                                      "matching_decisions": sum(r["decision_matches_plan"] for r in rows),
                                      "mismatched_cases": mismatches,
                                      "matching_effects": sum(r["effect_matches_plan"] for r in rows),
                                      "dispatch_consistent": all(r["dispatch_matches_decision"] for r in rows),
                                      "tool_executions": sum(len(r["tool_receipts"]) for r in relevant),
                                      "matches_predeclared_fault_pattern": mismatches == plan["expected_mismatches"][mode]})
        result["status"] = "completed"
    except Exception as exc:
        result["status"] = "execution_error"
        result["error"] = {"type": type(exc).__name__, "message": str(exc)}
        raise
    finally:
        result["ended_at"] = now()
        with (args.output_dir / "result.json").open("x", encoding="utf-8") as out:
            json.dump(result, out, ensure_ascii=False, indent=2)
            out.write("\n")
    print(json.dumps(result["summary"], ensure_ascii=False))


if __name__ == "__main__":
    main()
