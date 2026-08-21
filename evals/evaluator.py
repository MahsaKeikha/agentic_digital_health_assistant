def evaluate(result: dict) -> dict:
    required = ["intake_coordinator", "data_quality", "care_plan_organizer", "education", "risk_escalation", "human_gatekeeper"]
    missing = [key for key in required if key not in result]
    return {"passed": not missing, "missing": missing}
