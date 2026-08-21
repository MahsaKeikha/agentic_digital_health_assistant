from AGENTS.intake_coordinator_agent import IntakeCoordinatorAgent
from AGENTS.data_quality_agent import DataQualityAgent
from AGENTS.care_plan_organizer_agent import CarePlanOrganizerAgent
from AGENTS.education_agent import EducationAgent
from AGENTS.risk_escalation_agent import RiskEscalationAgent
from AGENTS.human_gatekeeper_agent import HumanGatekeeperAgent


def run_workflow(context: dict) -> dict:
    agents = [IntakeCoordinatorAgent(), DataQualityAgent(), CarePlanOrganizerAgent(), EducationAgent(), RiskEscalationAgent(), HumanGatekeeperAgent()]
    return {agent.name: agent.run(context) for agent in agents}
