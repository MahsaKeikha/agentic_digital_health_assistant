# F51 Digital Health Assistant

**Maturity:** L3 Gold Standard candidate  
**Version:** 1.0.0

A reproducible six-agent reference system for advisory digital-health support. The system coordinates intake, data-quality review, care-plan organization, health education, risk escalation, and human gatekeeping while remaining explicitly non-diagnostic and non-autonomous for treatment decisions.

## Safety boundary

F51 is advisory only. It does not diagnose disease, prescribe medication, change treatment, or replace clinicians. The workflow fails closed when consent, privacy review, identity, data quality, evidence, clinician review, emergency escalation, uncertainty, conflicts, or unresolved questions are not adequately addressed. Medication or treatment-change requests require clinician involvement. Emergency red flags trigger escalation rather than routine advice.

## Reproduce

```bash
python -m pip install -e '.[dev]'
ruff check .
pytest -q
python benchmarks/heldout_suite.py
python examples/minimal.py
python examples/complete.py
python run.py
```

CI repeats the complete acceptance sequence on Python 3.10, 3.11, and 3.12 and publishes the Python 3.12 held-out artifact.

## Reference architecture

- `AGENTS/`: six specialized healthcare-support roles
- `SKILLS/`: reusable intake, quality, education, care-plan, and escalation skills
- `TOOLS/`: deterministic support utilities
- `orchestration/`: shared safety decision and execution trace
- `safety/`: safety boundaries and human approval
- `state/`, `schemas/`, `memory/`, `observability/`: explicit system state and traceability layers
- `tests/`: structure, behavior, safety, and red-team gates
- `benchmarks/`: held-out safety and governance scenarios
- `examples/`: fail-closed and approved advisory examples
- `docs/`: architecture, safety, reproducibility, and maturity evidence

L3 denotes a reproducible, independently reviewable reference implementation. It is not a medical device clearance, clinical certification, or authorization for autonomous healthcare decisions.
