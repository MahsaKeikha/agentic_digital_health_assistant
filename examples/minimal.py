from orchestration.orchestrator import run_workflow

result = run_workflow({})
assert result["status"] == "clinical_review_or_escalation_required"
print(result["status"], result["blockers"][:3])
