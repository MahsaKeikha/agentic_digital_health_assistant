def format_plan(plan: dict) -> dict:
    return {"goals": plan.get("goals", []), "tasks": plan.get("tasks", []), "notes": plan.get("notes", [])}
