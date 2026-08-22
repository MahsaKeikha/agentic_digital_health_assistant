from orchestration.orchestrator import run_workflow

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
    "evidence_sources": ["validated patient-reported data"],
    "unresolved_conflicts": [],
    "unresolved_questions": [],
    "human_approval": True,
}
result = run_workflow(case)
assert result["status"] == "approved_for_advisory_support"
print(result["status"], result["scope"])
