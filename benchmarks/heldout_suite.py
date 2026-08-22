import json
from pathlib import Path

from orchestration.orchestrator import run_workflow


def healthy(**updates):
    case = {
        "consent_confirmed": True,
        "privacy_review_complete": True,
        "identity_verified": True,
        "data_quality_acceptable": True,
        "clinician_review_required": False,
        "clinician_review_complete": False,
        "emergency_red_flags": [],
        "medication_change_requested": False,
        "diagnosis_requested": False,
        "treatment_change_requested": False,
        "uncertainty_high": False,
        "evidence_sources": ["validated source"],
        "unresolved_conflicts": [],
        "unresolved_questions": [],
        "human_approval": True,
    }
    case.update(updates)
    return case


SCENARIOS = [
    ("healthy_advisory", healthy(), "approved_for_advisory_support"),
    ("awaiting_human", healthy(human_approval=False), "awaiting_human_approval"),
    ("emergency_red_flag", healthy(emergency_red_flags=["red flag"]), "clinical_review_or_escalation_required"),
    ("diagnosis_request", healthy(diagnosis_requested=True), "clinical_review_or_escalation_required"),
    ("medication_change", healthy(medication_change_requested=True), "clinical_review_or_escalation_required"),
    ("privacy_consent_gap", healthy(consent_confirmed=False, privacy_review_complete=False), "clinical_review_or_escalation_required"),
    ("high_uncertainty", healthy(uncertainty_high=True), "clinical_review_or_escalation_required"),
    ("clinician_review_incomplete", healthy(clinician_review_required=True), "clinical_review_or_escalation_required"),
]


def main():
    rows = []
    for name, payload, expected in SCENARIOS:
        actual = run_workflow(payload)["status"]
        rows.append({"scenario": name, "expected": expected, "actual": actual, "passed": actual == expected})
    passed = sum(row["passed"] for row in rows)
    result = {
        "system_id": "F51",
        "version": "1.0.0",
        "scenario_count": len(rows),
        "passed": passed,
        "pass_rate": passed / len(rows),
        "scenarios": rows,
    }
    Path("benchmarks/heldout_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if result["pass_rate"] != 1.0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
