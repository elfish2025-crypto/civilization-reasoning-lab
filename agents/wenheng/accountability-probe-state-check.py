#!/usr/bin/env python3
"""Constructed state-model check of probe design, not an Agent experiment.

Only Python's standard library is used. No network, model calls, process
restarts, real identity service or real gateway are involved. Worker generation
numbers are model labels; gateway state is an in-memory Python object.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def history(subject, closed=False):
    obligation = f"obligation-{subject}-x"
    events = [
        {"id": f"action-{subject}", "kind": "action", "subject": subject,
         "item": "x"},
        {"id": obligation, "kind": "open", "subject": subject, "item": "x",
         "source_event": f"action-{subject}"},
    ]
    if closed:
        events.append({"id": f"settlement-{subject}", "kind": "close",
                       "obligation": obligation,
                       "basis": "controller_injected_valid_settlement"})
    return events


SNAPSHOTS = {"empty": [], "A-open": history("A"),
             "A-closed": history("A", closed=True), "B-open": history("B")}
# Expected decisions are the 2026-09-19 design table, not outputs of a gate.
PLAN = [
    ("main", "baseline", "empty", "A", "x", 0, "allow"),
    ("main", "obligation_open", "A-open", "A", "x", 0, "deny"),
    ("main", "worker_rebound", "A-open", "A", "x", 1, "deny"),
    ("main", "identity_isolation", "A-open", "B", "x", 0, "allow"),
    ("main", "item_isolation", "A-open", "A", "y", 1, "allow"),
    ("main", "settled", "A-closed", "A", "x", 1, "allow"),
    ("main", "worker_rebound_after_settlement", "A-closed", "A", "x", 2,
     "allow"),
    ("swapped", "swapped_obligated", "B-open", "B", "x", 1, "deny"),
    ("swapped", "swapped_unobligated", "B-open", "A", "x", 0, "allow"),
]
FIELDS = ("trace", "case", "snapshot", "subject", "item",
          "worker_generation_label", "expected_decision")


def blocked_pairs(events):
    """Reduce the declared event history; reject malformed fixture histories."""
    actions, outstanding = {}, {}
    for event in events:
        if event["kind"] == "action":
            actions[event["id"]] = (event["subject"], event["item"])
        elif event["kind"] == "open":
            pair = (event["subject"], event["item"])
            if actions.get(event["source_event"]) != pair:
                raise ValueError("Obligation source does not match its owner/item")
            outstanding[event["id"]] = pair
        elif event["kind"] == "close":
            del outstanding[event["obligation"]]
        else:
            raise ValueError("Unknown fixture event")
    return set(outstanding.values())


class Gate:
    def __init__(self, sticky_deny):
        self.sticky_deny = sticky_deny
        self.deny_cache = set()

    def decide(self, subject, item, events):
        pair = (subject, item)
        before = sorted(self.deny_cache)
        if self.sticky_deny and pair in self.deny_cache:
            return "deny", False, before, sorted(self.deny_cache)
        decision = "deny" if pair in blocked_pairs(events) else "allow"
        # Deliberate defect: denies are cached without settlement invalidation.
        if self.sticky_deny and decision == "deny":
            self.deny_cache.add(pair)
        return decision, True, before, sorted(self.deny_cache)


def run(sticky_deny, isolated):
    observations = []
    gate, current_trace, generation = None, None, 0
    for values in PLAN:
        step = dict(zip(FIELDS, values))
        reset = isolated or gate is None or step["trace"] != current_trace
        if reset:
            gate = Gate(sticky_deny)
            generation += 1
        current_trace = step["trace"]
        decision, read, before, after = gate.decide(
            step["subject"], step["item"], SNAPSHOTS[step["snapshot"]]
        )
        observations.append({
            "case": step["case"], "actual_decision": decision,
            "matches_expected": decision == step["expected_decision"],
            "gateway_generation": generation, "gateway_reset_before": reset,
            "ledger_read_this_decision": read,
            "deny_cache_before": before, "deny_cache_after": after,
        })
    failures = [o["case"] for o in observations if not o["matches_expected"]]
    return {
        "gate_model": "sticky_deny_cache" if sticky_deny else "current_ledger",
        "execution_mode": "isolated_snapshots" if isolated else "continuous_gate",
        "decision_count": len(observations),
        "matching_decisions": len(observations) - len(failures),
        "mismatched_cases": failures,
        "observations": observations,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    plan = {"snapshots": SNAPSHOTS, "steps": [dict(zip(FIELDS, p)) for p in PLAN]}
    result = {
        "format_version": "1",
        "evidence_scope": "constructed_state_model_probe_design_check",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "research_agent": "WenHeng / 问衡",
        "maintenance_agent": "ZhiHeng / 知衡",
        "authoring_model": {"provider": "OpenAI", "name": "GPT-6",
                            "exact_version": "unknown"},
        "independent_review": False, "human_reviewer": None,
        "source_baseline_commit": "0faa4360a5635dec6daa37eb03d0e2bf0b6d6a0c",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "plan_sha256": digest(plan), "python_version": platform.python_version(),
        "randomness": "none", "repetitions_per_configuration": 1,
        "agent_experiment": False, "real_gateway_test": False,
        "process_restarts_performed": False, "tool_execution_observed": False,
        "plan": plan,
        "runs": [run(sticky, isolated) for sticky in (False, True)
                 for isolated in (True, False)],
    }
    # Refuse to overwrite a prior run record; use another output path to repeat.
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(result, out, ensure_ascii=False, indent=2)
        out.write("\n")
    print(json.dumps([{k: row[k] for k in ("gate_model", "execution_mode",
        "matching_decisions", "decision_count", "mismatched_cases")}
        for row in result["runs"]], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
