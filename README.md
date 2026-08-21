# Agentic Digital Health Assistant

F51 in the Agentic AI Library.

This repository implements a multi-agent digital health workflow support system with explicit specialist agents, tools, skills, orchestration, memory, state, schemas, prompts, configuration, safety controls, observability, evaluation, benchmarks, examples, tests, and CI.

This system does not diagnose, prescribe, authorize treatment, or replace qualified clinical judgment or emergency processes.

## Core agents

- [`intake_coordinator_agent.py`](AGENTS/intake_coordinator_agent.py)
- [`data_quality_agent.py`](AGENTS/data_quality_agent.py)
- [`care_plan_organizer_agent.py`](AGENTS/care_plan_organizer_agent.py)
- [`education_agent.py`](AGENTS/education_agent.py)
- [`risk_escalation_agent.py`](AGENTS/risk_escalation_agent.py)
- [`human_gatekeeper_agent.py`](AGENTS/human_gatekeeper_agent.py)

## Core architecture

- [`TOOLS/`](TOOLS/)
- [`SKILLS/`](SKILLS/)
- [`orchestration/`](orchestration/)
- [`memory/`](memory/)
- [`state/`](state/)
- [`schemas/`](schemas/)
- [`prompts/`](prompts/)
- [`config/`](config/)
- [`safety/`](safety/)
- [`observability/`](observability/)
- [`evals/`](evals/)
- [`benchmarks/`](benchmarks/)
- [`examples/`](examples/)
- [`tests/`](tests/)
- [`docs/`](docs/)

## Run

```bash
python run.py
```

Human review is required before patient-specific or consequential use.
