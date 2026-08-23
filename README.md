# F51 Digital Health Assistant

**Maturity:** L3 Gold Standard candidate  
**Version:** 1.0.0

A reproducible six-agent reference architecture for advisory digital-health support across intake, data-quality review, care-plan organization, health education, risk escalation, and human gatekeeping.

F51 is designed for engineers, researchers, digital-health teams, and students who want to study how a healthcare-support workflow can be decomposed into specialized agents while keeping consent, privacy, evidence quality, uncertainty, clinician involvement, escalation, and human authority explicit.

The system is advisory only. It does not diagnose disease, prescribe medication, change treatment, authorize clinical actions, or replace qualified clinicians. It is not a cleared medical device and should not be represented as one.

## Why this architecture exists

Digital-health systems often combine information from users, caregivers, sensors, records, questionnaires, and educational resources. The engineering challenge is not only producing a helpful response. The system must know whether the data are trustworthy, whether the user has consented to the workflow, whether a request exceeds the system's authority, whether a clinician must be involved, and whether a red flag requires escalation instead of ordinary advice.

F51 therefore separates these responsibilities into six roles:

```text
user / caregiver / health-support request
              |
              v
   Intake Coordinator Agent
              |
              v
      Data Quality Agent
              |
              v
 Care Plan Organizer Agent
              |
              v
       Education Agent
              |
              v
    Risk Escalation Agent
              |
              v
 Human Gatekeeper Agent
              |
              v
 advisory output or escalation
```

A later agent does not erase a blocker created earlier. Poor data quality, missing consent, unresolved uncertainty, or a safety concern remains visible through the workflow.

## Six-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Intake Coordinator Agent | Structure the user's request, context, identity, consent, and goals | Do we have the minimum information and permission required to proceed? |
| Data Quality Agent | Review completeness, provenance, recency, consistency, and uncertainty | Is the available information trustworthy enough for this advisory task? |
| Care Plan Organizer Agent | Organize existing clinician-approved plans, routines, goals, and follow-up items | Can the information be structured without creating or changing treatment? |
| Education Agent | Provide bounded health education from approved sources | What general information can be explained safely without diagnosing or prescribing? |
| Risk Escalation Agent | Detect red flags, high-risk ambiguity, and requests requiring professional review | Does this case need emergency, urgent, clinician, or specialist escalation? |
| Human Gatekeeper Agent | Enforce final advisory boundaries and clinician/human review requirements | Is this response eligible to be delivered, or must a qualified human intervene? |

The architecture is intentionally conservative. Healthcare uncertainty should result in visible limits or escalation rather than confident invention.

## Repository structure

```text
AGENTS/
├── intake_coordinator_agent.py
├── data_quality_agent.py
├── care_plan_organizer_agent.py
├── education_agent.py
├── risk_escalation_agent.py
└── human_gatekeeper_agent.py

SKILLS/
├── intake_structuring.py
├── data_quality_review.py
├── care_plan_organization.py
├── health_education.py
└── risk_escalation.py

TOOLS/
├── intake_normalizer.py
├── data_quality_checker.py
├── care_plan_formatter.py
├── education_resource_index.py
└── escalation_router.py

benchmarks/
├── benchmark.py
├── heldout_suite.py
└── RESULTS.md

config/
docs/
evals/
examples/
memory/
observability/
safety/
schemas/
state/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
CITATION.cff
LICENSE
README.md
```

The repository separates agent roles, reusable skills, deterministic support tools, shared state, schemas, memory, observability, safety logic, testing, and evaluation.

## Advisory scope

F51 can support activities such as:

- structuring a health-related intake
- organizing an existing care plan
- summarizing clinician-provided instructions
- identifying missing information
- explaining general health concepts
- helping prepare questions for a clinician
- organizing symptom or routine logs
- surfacing uncertainty
- routing requests to an appropriate human reviewer
- identifying situations that should not be handled as routine advisory support

It must not independently:

- diagnose a condition
- rule out a serious condition
- prescribe medication
- start or stop medication
- change dose or timing
- replace clinician review
- authorize treatment
- interpret an emergency as routine
- make definitive clinical claims from incomplete evidence

## Intake and consent

The Intake Coordinator Agent establishes the minimum context needed for the workflow.

Useful intake fields can include:

```text
case_id
request_type
user_role
subject_identity_status
consent_status
care_context
known_conditions
current_clinician_involvement
current_care_plan_reference
data_sources
user_goal
urgency_signal
```

Production implementations should collect only information needed for the stated purpose.

### Consent

Consent should be treated as an explicit state rather than assumed from message presence.

A production system should define:

- what information will be processed
- why it is needed
- who can access it
- whether it will be stored
- retention period
- whether external services receive it
- how consent is recorded
- how consent can be withdrawn

Missing required consent should fail closed.

## Identity and role clarity

Healthcare information can involve the user, a dependent, a caregiver, a clinician, or another authorized representative.

The workflow should distinguish:

- who is asking
- who the health information concerns
- whether the requester is authorized to act for that person
- whether the system is providing education, organization, or escalation support

Identity and authorization requirements depend on the deployment environment and applicable law and policy.

## Data quality

The Data Quality Agent treats health information as evidence with uncertainty rather than as unquestioned truth.

A review can consider:

- source
- timestamp
- recency
- completeness
- missing values
- contradictory information
- measurement context
- unit consistency
- device quality
- whether information is self-reported
- whether a clinician confirmed it
- whether a sensor result is within its intended use

Useful evidence states include:

```text
VERIFIED
SELF_REPORTED
DEVICE_REPORTED
CLINICIAN_PROVIDED
STALE
INCOMPLETE
CONFLICTING
UNVERIFIED
```

The system should not convert weak evidence into a definitive clinical conclusion.

## Sensor and wearable data

Digital-health systems often receive data from wearables, home sensors, questionnaires, or connected devices.

Before using such data, production systems should understand:

- device intended use
- sampling method
- measurement error
- missingness
- synchronization
- firmware or algorithm version
- calibration requirements
- artifact sensitivity
- whether the metric has clinical validity for the intended interpretation

A consumer wearable measurement should not automatically be treated as a clinical diagnostic result.

## Care-plan organization

The Care Plan Organizer Agent structures existing plans rather than creating treatment.

It can organize:

- clinician-provided instructions
- appointments
- medication lists as reported
- rehabilitation tasks
- daily routines
- monitoring schedules
- caregiver tasks
- questions for follow-up
- unresolved items

A structured plan might include:

```text
goal
existing instruction
source
responsible person
schedule
completion status
follow_up_date
open_question
clinician_review_required
```

If the user asks to alter a treatment plan, the workflow should route that request to an appropriate clinician rather than generating an autonomous change.

## Medication boundary

Medication-related requests require especially clear authority boundaries.

F51 should not independently recommend:

- starting medication
- stopping medication
- changing dosage
- changing frequency
- combining medications
- substituting one medication for another
- changing prescription timing based on symptoms

The system may help organize a reported medication list or formulate questions for a pharmacist or clinician. Treatment changes require qualified professional review.

## Health education

The Education Agent provides general explanatory information rather than diagnosis.

Good educational output should:

- distinguish general information from personal medical advice
- use appropriate evidence sources
- state important uncertainty
- avoid overstating causality
- avoid claiming a condition is present or absent
- explain when professional evaluation is appropriate

`TOOLS/education_resource_index.py` provides the reference abstraction for approved educational resources.

Production systems should version and govern their educational corpus rather than allowing arbitrary unverified sources to become clinical authority.

## Evidence and provenance

Health-related claims should remain traceable to their source.

Useful provenance fields include:

```text
source_id
source_type
source_date
publisher_or_provider
version
retrieval_date
claim_supported
confidence
limitations
```

The system should distinguish:

1. reported facts
2. measured data
3. clinician-provided information
4. general educational evidence
5. system interpretation
6. unresolved uncertainty

These categories should not be silently merged.

## Risk escalation

The Risk Escalation Agent determines when ordinary advisory support is no longer appropriate.

Potential escalation categories include:

```text
ROUTINE
CLINICIAN REVIEW
URGENT REVIEW
EMERGENCY ESCALATION
SPECIALIST REVIEW
INSUFFICIENT INFORMATION
```

Production escalation logic must be defined with qualified clinical and safety professionals for the intended population and use case.

### Emergency boundary

If the system identifies signs that may represent an emergency or immediate danger, it should not continue as though the case were routine health education.

The reference architecture is designed to transition into an escalation state and require appropriate human/emergency handling according to the deployment's approved protocol.

## Uncertainty handling

Uncertainty is a first-class safety state.

The system should explicitly represent situations such as:

```text
DATA INSUFFICIENT
SOURCES CONFLICT
MEASUREMENT UNCERTAIN
CLINICAL INTERPRETATION REQUIRED
REQUEST OUTSIDE SCOPE
```

A useful system knows when it does not have enough evidence to answer safely.

## Human gatekeeping

The Human Gatekeeper Agent is the final authority boundary inside the reference workflow.

It verifies that required automated safety conditions are satisfied before advisory output is released.

Examples of blockers include:

- required consent missing
- identity or authorization unresolved
- material data-quality failure
- source provenance missing
- treatment-change request
- diagnostic request beyond scope
- emergency or urgent risk signal
- clinician review required
- conflicting evidence unresolved
- uncertainty above allowed threshold
- privacy requirement unresolved
- critical question unanswered

Human review does not mean an unqualified reviewer can override clinical or safety requirements. The reviewer must have the authority required by the actual deployment.

## Privacy and data minimization

Health information is highly sensitive. Production deployments should apply strict privacy-by-design controls.

Relevant controls can include:

- minimum necessary collection
- purpose limitation
- access control
- encryption
- data separation
- audit logging
- retention limits
- deletion workflows
- consent records
- role-based access
- de-identification or pseudonymization where appropriate
- environment separation
- secure secrets management

Agents should receive only the information required for their role.

## Shared state and schemas

The `state/` and `schemas/` layers keep evidence structured across the six-agent workflow.

Useful state can include:

- consent state
- identity state
- intake record
- evidence sources
- data-quality findings
- care-plan items
- educational references
- escalation state
- uncertainty state
- clinician-review requirement
- human-gate decision

Structured state supports testing and auditability more reliably than one long free-form conversation.

## Memory

The `memory/` layer can retain workflow evidence across stages.

Production memory should be scoped by case, user authorization, data source, purpose, and retention policy. Sensitive information should not be retained merely because it may be useful later.

Superseded data should remain traceable where audit requirements demand it, but retention should still comply with applicable privacy rules and organizational policy.

## Observability

The observability layer should make the advisory workflow inspectable without unnecessarily exposing sensitive information.

Useful trace fields include:

- case ID
- agent execution order
- schema version
- evidence references
- tool calls
- data-quality state
- escalation state
- gate results
- unresolved questions
- human review event

Production logging should avoid placing protected or sensitive health information into unrestricted logs.

## Fail-closed safety behavior

F51 fails closed when required evidence or authority is missing.

Useful failure states include:

```text
CONSENT REQUIRED
IDENTITY UNRESOLVED
AUTHORIZATION UNRESOLVED
DATA QUALITY INSUFFICIENT
SOURCE PROVENANCE MISSING
CLINICIAN REVIEW REQUIRED
MEDICATION CHANGE NOT AUTHORIZED
TREATMENT CHANGE NOT AUTHORIZED
DIAGNOSTIC REQUEST OUT OF SCOPE
EMERGENCY ESCALATION REQUIRED
PRIVACY REVIEW REQUIRED
CONFLICTING EVIDENCE
INSUFFICIENT INFORMATION
HUMAN REVIEW REQUIRED
```

The system should never fabricate a clinician review, consent record, measurement result, diagnosis, treatment approval, or emergency assessment to complete the workflow.

## End-to-end workflow

A typical reference run follows this sequence:

1. Receive the advisory health-support request.
2. Identify the user role and subject of the information.
3. Confirm required consent and authorization state.
4. Normalize the intake information.
5. Identify the data sources being relied upon.
6. Run data-quality and provenance review.
7. Organize existing care-plan information where appropriate.
8. Retrieve or structure approved educational information.
9. Review for red flags, uncertainty, and escalation requirements.
10. Determine whether clinician review is required.
11. Apply human gatekeeping and fail-closed safety rules.
12. Deliver bounded advisory support or escalate to the appropriate human process.

## Reproduce the reference implementation

Install the project with development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run static checks and tests:

```bash
ruff check .
pytest -q
```

Run the held-out safety suite:

```bash
python benchmarks/heldout_suite.py
```

Run the examples:

```bash
python examples/minimal.py
python examples/complete.py
```

Run the main entry point:

```bash
python run.py
```

CI repeats the acceptance sequence on Python 3.10, 3.11, and 3.12 and publishes the Python 3.12 held-out artifact.

## Benchmarks and evaluation

The repository includes:

```text
benchmarks/benchmark.py
benchmarks/heldout_suite.py
benchmarks/RESULTS.md
evals/evaluator.py
```

Evaluation should test safety and workflow behavior rather than only whether the response sounds helpful.

Useful dimensions include:

- consent enforcement
- identity/authorization handling
- data-quality detection
- provenance preservation
- unsupported-claim rate
- medication-boundary enforcement
- treatment-change refusal
- diagnostic-boundary enforcement
- emergency escalation
- clinician-review routing
- uncertainty disclosure
- privacy-gate enforcement
- conflict detection
- human-gate enforcement

Strong held-out scenarios should include missing consent, stale data, contradictory sources, requests to change medication, emergency red flags, attempts to bypass clinician review, and incomplete evidence.

## Red-team considerations

Healthcare-support systems should be tested against attempts to override their boundaries.

Examples include requests to:

- ignore a red flag
- provide a diagnosis anyway
- change medication without clinician review
- treat an unverified sensor reading as definitive
- conceal uncertainty
- bypass privacy requirements
- claim a clinician approved something when no approval exists

The correct behavior is to preserve the safety boundary, not to comply with the attempted bypass.

## CI and reproducibility

The GitHub Actions workflow under `.github/workflows/ci.yml` validates the reference architecture across supported Python versions.

Production systems should additionally test:

- schema compatibility
- privacy controls
- authentication and authorization
- clinical content governance
- escalation routing
- audit logging
- data-retention behavior
- source-version changes
- integration with sandbox clinical systems
- representative user and caregiver workflows

Version prompts, policies, schemas, educational sources, tools, escalation rules, and benchmark sets so behavior can be reproduced.

## L3 Gold Standard candidate

The repository includes `docs/L3_AUDIT.md` and is labeled an **L3 Gold Standard candidate** based on its reproducible multi-agent architecture, explicit state and safety layers, fail-closed human gating, held-out safety evaluation, CI, and independently reviewable evidence path.

This maturity designation applies to the repository as a reference implementation. It is not FDA clearance, clinical certification, validation for a specific patient population, proof of diagnostic accuracy, or authorization for autonomous medical decisions.

## Extending F51

Common extensions include:

- EHR integration
- FHIR-based data exchange
- patient-reported outcomes
- wearable data ingestion
- caregiver portals
- appointment preparation
- medication-list reconciliation support
- clinician messaging workflows
- rehabilitation adherence tracking
- remote-monitoring dashboards
- educational content governance
- multilingual health education
- consent management
- privacy-preserving analytics
- clinical escalation workflows

Every extension should preserve minimum necessary data access, source provenance, uncertainty, professional review requirements, and the non-autonomous treatment boundary.

## Example applications

F51 can serve as a reference architecture for:

- patient education assistants
- caregiver support systems
- chronic-care organization tools
- remote-monitoring workflow support
- appointment preparation
- rehabilitation support
- wellness coaching with clear medical boundaries
- health-data quality review
- care coordination support
- research prototypes for human-supervised digital health

Any real clinical deployment requires use-case-specific clinical validation, risk management, privacy/security review, regulatory assessment, usability testing, and qualified human oversight.

## Design principles

1. Keep the system advisory rather than diagnostic or prescriptive.
2. Confirm consent and authorization before processing sensitive workflows.
3. Treat health data as evidence with provenance and uncertainty.
4. Separate care-plan organization from treatment creation.
5. Separate health education from personalized diagnosis.
6. Escalate red flags instead of normalizing them into routine advice.
7. Require clinician involvement for medication and treatment changes.
8. Apply minimum necessary data access and privacy-by-design.
9. Fail closed when safety evidence or authority is incomplete.
10. Keep consequential clinical decisions with qualified humans.

## Documentation

Additional documentation is available in:

- `docs/ARCHITECTURE.md`
- `docs/REPRODUCIBILITY_AND_SAFETY.md`
- `docs/L3_AUDIT.md`

## Citation and reuse

The repository includes `CITATION.cff` for academic and technical citation and is distributed under the MIT license. It can be studied, referenced, adapted, and extended subject to the license terms.

## Responsible use

Use F51 as a digital-health workflow and multi-agent architecture reference. Validate the intended use, clinical boundaries, data quality, source evidence, privacy controls, escalation pathways, clinician review requirements, and human gatekeeping against the actual deployment environment. Final diagnosis, treatment, medication, emergency, and other clinical decisions remain with qualified healthcare professionals and authorized human systems.