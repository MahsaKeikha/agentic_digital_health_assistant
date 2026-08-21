from orchestration.orchestrator import run_workflow

if __name__ == "__main__":
    print(run_workflow({"intake": {}, "care_plan": {}, "education_topics": [], "risk_flags": [], "human_approved": False}))
