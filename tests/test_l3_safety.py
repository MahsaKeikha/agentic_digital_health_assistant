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
        "evidence_sources": ["validated patient-reported data"],
        "unresolved_conflicts": [],
        "unresolved_questions": [],
        "human_approval": True,
    }
    case.update(updates)
    return case


def test_healthy_advisory_case_can_be_approved():
    result = run_workflow(healthy())
    assert result["status"] == "approved_for_advisory_support"
    assert result["scope"] == "advisory_only_no_diagnosis_or_autonomous_treatment"
    assert len(result["analyses"]) == 6


def test_human_approval_is_required():
    assert run_workflow(healthy(human_approval=False))["status"] == "awaiting_human_approval"


def test_emergency_red_flags_fail_closed():
    result = run_workflow(healthy(emergency_red_flags=["possible emergency"]))
    assert result["status"] == "clinical_review_or_escalation_required"
    assert "emergency_escalation_required" in result["blockers"]


def test_medication_and_treatment_changes_are_not_autonomous():
    result = run_workflow(healthy(medication_change_requested=True, treatment_change_requested=True))
    assert "medication_change_requires_clinician" in result["blockers"]
    assert "treatment_change_requires_clinician" in result["blockers"]


def test_diagnosis_request_is_out_of_scope():
    result = run_workflow(healthy(diagnosis_requested=True))
    assert "diagnosis_out_of_scope" in result["blockers"]


def test_privacy_consent_identity_and_evidence_are_required():
    result = run_workflow(healthy(consent_confirmed=False, privacy_review_complete=False, identity_verified=False, evidence_sources=[]))
    assert {"consent_missing", "privacy_review_incomplete", "identity_not_verified", "evidence_missing"}.issubset(result["blockers"])


def test_required_clinician_review_must_be_complete():
    result = run_workflow(healthy(clinician_review_required=True, clinician_review_complete=False))
    assert "clinician_review_incomplete" in result["blockers"]


def test_high_uncertainty_and_unresolved_issues_fail_closed():
    result = run_workflow(healthy(uncertainty_high=True, unresolved_conflicts=["conflicting values"], unresolved_questions=["missing context"]))
    assert "high_uncertainty_requires_review" in result["blockers"]
    assert "unresolved_conflict" in result["blockers"]
    assert "unresolved_question" in result["blockers"]
