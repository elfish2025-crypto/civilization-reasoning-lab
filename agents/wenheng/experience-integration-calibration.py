#!/usr/bin/env python3
"""Deterministic instrument calibration, not an LLM or Agent experiment.

Only the controller sees phase and expected protocol. Each policy sees a
default, a selected memory value, and feedback from its own previous action.
The full audit trace is inaccessible to policies. Run with --plan and --output.
"""

import argparse
import hashlib
import itertools
import json
import platform
from datetime import datetime, timezone
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def opposite(value):
    return {"q": "r", "r": "q"}[value]


def propose(policy, memory, default, readable=True):
    # No expected protocol, phase, trial ID, clock, or audit trace is an input.
    if policy == "record_only":
        return default, {"path": "unused", "value": None}
    if not readable:
        return default, {"path": "blocked", "value": None}
    return (memory if memory is not None else default), {
        "path": "read", "value": memory
    }


def update(policy, memory, action, success):
    # Binary, noiseless task: either outcome identifies the correct protocol.
    inferred = action if success else opposite(action)
    if policy == "freeze_first" and memory is not None:
        return memory
    return inferred


def trajectory(policy, first, default, trials_per_phase):
    memory = None
    trace = []
    checkpoints = []
    phases = [first, opposite(first), first]
    for phase, required in enumerate(phases):
        for trial in range(trials_per_phase):
            before = memory
            action, read = propose(policy, memory, default)
            success = action == required
            memory = update(policy, memory, action, success)
            trace.append({
                "event": len(trace) + 1,
                "controller_only": {"phase": phase, "trial": trial,
                                    "required": required},
                "memory_before": before,
                "planner_read": read,
                "proposal": action,
                "feedback": {"success": success},
                "memory_after": memory,
                "changed": before != memory,
            })
        checkpoints.append({"phase": phase, "event": len(trace),
                            "memory": memory})

    # Isolated decision-only probes at the end of phase 1 (zero-based).
    # No returned probe feedback or memory writes; not independent learning runs.
    latest = checkpoints[1]["memory"]
    old = checkpoints[0]["memory"]
    probes = []
    for condition, selected, readable in [
        ("latest", latest, True),
        ("blocked", latest, False),
        ("old", old, True),
    ]:
        action, read = propose(policy, selected, default, readable)
        probes.append({
            "condition": condition,
            "source_event": checkpoints[0 if condition == "old" else 1]["event"],
            "selected_memory": selected,
            "planner_read": read,
            "proposal": action,
            "controller_only_required": phases[1],
            "correct_proposal": action == phases[1],
            "feedback_delivered": False,
            "memory_updated": False,
        })

    eligible = [e for e in trace if e["controller_only"]["phase"] > 0
                and e["controller_only"]["trial"] > 0]
    return {
        "policy": policy, "initial_protocol": first, "default": default,
        "phase_protocols": phases, "trace": trace, "checkpoints": checkpoints,
        "probes": probes,
        "continuous": {
            "successes": sum(e["feedback"]["success"] for e in trace),
            "actions": len(trace),
            "post_change_after_first_feedback_successes": sum(
                e["feedback"]["success"] for e in eligible),
            "post_change_after_first_feedback_actions": len(eligible),
        },
    }


def summarize(runs, policies):
    summary = {}
    for policy in policies:
        selected = [r for r in runs if r["policy"] == policy]
        row = {"constructed_cases": len(selected),
               "continuous_successes": 0, "continuous_actions": 0,
               "post_feedback_successes": 0, "post_feedback_actions": 0,
               "probe_correct": {c: 0 for c in ["latest", "blocked", "old"]},
               "latest_vs_old_changed": 0,
               "latest_vs_blocked_changed": 0,
               "latest_better_than_blocked": 0,
               "latest_worse_than_blocked": 0}
        for run in selected:
            continuous = run["continuous"]
            row["continuous_successes"] += continuous["successes"]
            row["continuous_actions"] += continuous["actions"]
            row["post_feedback_successes"] += continuous[
                "post_change_after_first_feedback_successes"]
            row["post_feedback_actions"] += continuous[
                "post_change_after_first_feedback_actions"]
            probes = {p["condition"]: p for p in run["probes"]}
            for condition, probe in probes.items():
                row["probe_correct"][condition] += probe["correct_proposal"]
            row["latest_vs_old_changed"] += (
                probes["latest"]["proposal"] != probes["old"]["proposal"])
            row["latest_vs_blocked_changed"] += (
                probes["latest"]["proposal"] != probes["blocked"]["proposal"])
            delta = (int(probes["latest"]["correct_proposal"])
                     - int(probes["blocked"]["correct_proposal"]))
            row["latest_better_than_blocked"] += delta > 0
            row["latest_worse_than_blocked"] += delta < 0
        summary[policy] = row
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Refusing to overwrite an existing result")
    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    started = datetime.now(timezone.utc).isoformat()
    if datetime.fromisoformat(plan["fixed_at_utc"]) >= datetime.fromisoformat(started):
        raise ValueError("Plan timestamp must precede execution")
    assert plan["protocols"] == ["q", "r"]
    assert plan["defaults"] == ["q", "r"]
    assert plan["policies"] == ["last_feedback", "record_only", "freeze_first"]
    assert plan["trials_per_phase"] == 3
    runs = [trajectory(policy, first, default, plan["trials_per_phase"])
            for policy, first, default in itertools.product(
                plan["policies"], plan["protocols"], plan["defaults"])]
    result = {
        "schema": "wenheng-experience-calibration-result-v1",
        "kind": "self_authored_deterministic_calibration",
        "runtime": {"python": platform.python_version(),
                    "system": platform.system(), "machine": platform.machine()},
        "started_at_utc": started,
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": digest(Path(__file__)),
        "plan_sha256": digest(args.plan),
        "plan": plan,
        "summary": summarize(runs, plan["policies"]),
        "runs": runs,
        "limits": ["No LLM or real Agent", "No governance or responsibility probe",
                   "No OS process replacement or durable-storage test",
                   "No human or independent review", "Not independent statistical samples",
                   "Not a validation of strong experience, P1, or P2"],
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8")
    print(json.dumps({"summary": result["summary"],
                      "result_sha256": digest(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
