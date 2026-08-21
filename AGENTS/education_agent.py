class EducationAgent:
    name = "education"

    def run(self, context: dict) -> dict:
        return {"education_topics": context.get("education_topics", []), "review_required": True}
