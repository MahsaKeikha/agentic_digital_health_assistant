# Agentic Digital Health Assistant

F51 in the Agentic AI Library.

A standalone multi-agent digital health workflow support system with explicit specialist agents, tools, skills, orchestration, memory, state, schemas, prompts, configuration, safety, observability, evaluation, benchmarks, examples, tests, and CI.

This system does not diagnose, prescribe, authorize treatment, or replace qualified clinical judgment or emergency processes.

## Agents

- [`intake_coordinator_agent.py`](AGENTS/intake_coordinator_agent.py)
- [`data_quality_agent.py`](AGENTS/data_quality_agent.py)
- [`care_plan_organizer_agent.py`](AGENTS/care_plan_organizer_agent.py)
- [`education_agent.py`](AGENTS/education_agent.py)
- [`risk_escalation_agent.py`](AGENTS/risk_escalation_agent.py)
- [`human_gatekeeper_agent.py`](AGENTS/human_gatekeeper_agent.py)

## Tools

- [`intake_normalizer.py`](TOOLS/intake_normalizer.py)
- [`data_quality_checker.py`](TOOLS/data_quality_checker.py)
- [`care_plan_formatter.py`](TOOLS/care_plan_formatter.py)
- [`education_resource_index.py`](TOOLS/education_resource_index.py)
- [`escalation_router.py`](TOOLS/escalation_router.py)

## Skills

- [`intake_structuring.py`](SKILLS/intake_structuring.py)
- [`data_quality_review.py`](SKILLS/data_quality_review.py)
- [`care_plan_organization.py`](SKILLS/care_plan_organization.py)
- [`health_education.py`](SKILLS/health_education.py)
- [`risk_escalation.py`](SKILLS/risk_escalation.py)

## Supporting architecture

[`orchestration/`](orchestration/) | [`memory/`](memory/) | [`state/`](state/) | [`schemas/`](schemas/) | [`prompts/`](prompts/) | [`config/`](config/) | [`safety/`](safety/) | [`observability/`](observability/) | [`evals/`](evals/) | [`benchmarks/`](benchmarks/) | [`examples/`](examples/) | [`tests/`](tests/) | [`docs/`](docs/)

## Run

```bash
python run.py
```

Human review is required before patient-specific or consequential use.
