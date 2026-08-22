from __future__ import annotations

from copy import deepcopy
from typing import Any

from AGENTS.care_plan_organizer_agent import CarePlanOrganizerAgent
from AGENTS.data_quality_agent import DataQualityAgent
from AGENTS.education_agent import EducationAgent
from AGENTS.human_gatekeeper_agent import HumanGatekeeperAgent
from AGENTS.intake_coordinator_agent import IntakeCoordinatorAgent
from AGENTS.risk_escalation_agent import RiskEscalationAgent


AGENTS = [
    IntakeCoordinatorAgent(),
    DataQualityAgent(),
    CarePlanOrganizerAgent(),
    EducationAgent(),
    RiskEscalationAgent(),
    HumanGatekeeperAgent(),
]


def _normalize(context: dict[str, Any]) -> dict[str, Any]:
    state = deepcopy(context)
    defaults = {
        "consent_confirmed": False,
        "privacy_review_complete": False,
        "identity_verified": False,
        "data_quality_acceptable": False,
        "clinician_review_required": False,
        "clinician_review_complete": False,
        "emergency_red_flags": [],
        "medication_change_requested": False,
        "diagnosis_requested": False,
        "treatment_change_requested": False,
        "uncertainty_high": False,
        "evidence_sources": [],
        "unresolved_conflicts": [],
        "unresolved_questions": [],
        "human_approval": False,
    }
    for key, value in defaults.items():
        state.setdefault(key, value)
    return state


def _blockers(state: dict[str, Any]) -> list[str]:
    blockers: list[str] = []
    checks = {
        "consent_missing": not state["consent_confirmed"],
        "privacy_review_incomplete": not state["privacy_review_complete"],
        "identity_not_verified": not state["identity_verified"],
        "data_quality_inadequate": not state["data_quality_acceptable"],
        "evidence_missing": not state["evidence_sources"],
        "emergency_escalation_required": bool(state["emergency_red_flags"]),
        "medication_change_requires_clinician": state["medication_change_requested"],
        "diagnosis_out_of_scope": state["diagnosis_requested"],
        "treatment_change_requires_clinician": state["treatment_change_requested"],
        "high_uncertainty_requires_review": state["uncertainty_high"],
        "unresolved_conflict": bool(state["unresolved_conflicts"]),
        "unresolved_question": bool(state["unresolved_questions"]),
    }
    for name, failed in checks.items():
        if failed:
            blockers.append(name)
    if state["clinician_review_required"] and not state["clinician_review_complete"]:
        blockers.append("clinician_review_incomplete")
    return blockers


def run_workflow(context: dict[str, Any]) -> dict[str, Any]:
    """Run F51 as an advisory, fail-closed digital-health workflow."""
    state = _normalize(context)
    analyses: dict[str, Any] = {}
    trace: list[dict[str, Any]] = []
    for step, agent in enumerate(AGENTS, 1):
        analyses[agent.name] = agent.run(state)
        trace.append({"step": step, "actor": agent.name, "event": "completed"})

    blockers = _blockers(state)
    if blockers:
        status = "clinical_review_or_escalation_required"
    elif state["human_approval"]:
        status = "approved_for_advisory_support"
    else:
        status = "awaiting_human_approval"

    trace.append({
        "step": len(trace) + 1,
        "actor": "digital_health_safety_gate",
        "event": status,
        "blockers": blockers,
    })
    return {
        "system_id": "F51",
        "system_name": "Digital Health Assistant",
        "version": "1.0.0",
        "maturity": "L3 Gold Standard",
        "scope": "advisory_only_no_diagnosis_or_autonomous_treatment",
        "state": state,
        "analyses": analyses,
        "blockers": blockers,
        "status": status,
        "trace": trace,
    }
