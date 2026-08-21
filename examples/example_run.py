from orchestration.orchestrator import run_workflow

EXAMPLE = {"intake": {"source": "example"}, "care_plan": {}, "education_topics": ["general education"], "risk_flags": [], "human_approved": False}

if __name__ == "__main__":
    print(run_workflow(EXAMPLE))
