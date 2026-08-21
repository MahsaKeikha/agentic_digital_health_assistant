class IntakeCoordinatorAgent:
    name = "intake_coordinator"

    def run(self, context: dict) -> dict:
        return {"intake": context.get("intake", {}), "missing": context.get("missing", [])}
