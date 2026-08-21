class RiskEscalationAgent:
    name = "risk_escalation"

    def run(self, context: dict) -> dict:
        return {"flags": context.get("risk_flags", []), "escalate_to_human": bool(context.get("risk_flags"))}
