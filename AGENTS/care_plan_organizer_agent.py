class CarePlanOrganizerAgent:
    name = "care_plan_organizer"

    def run(self, context: dict) -> dict:
        return {"care_plan": context.get("care_plan", {}), "status": "organized"}
