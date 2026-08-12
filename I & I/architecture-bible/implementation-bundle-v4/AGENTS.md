# Version 4 Implementation Bundle Instructions

These instructions govern every file and subfolder inside this Version 4 implementation bundle.

## Mission

Implement the first PumpOS and I&I Intelligence operational slice:

> One basin, one rainfall event, one receiving pump station, one frozen input snapshot, one
> deterministic calculation chain, optional model comparison, one traceable dashboard result set,
> and one human-reviewed decision packet.

Do not expand the mission without written owner direction recorded in `intake.yaml`.

## Authority order

When instructions conflict, use this order:

1. explicit current owner direction;
2. this `AGENTS.md`;
3. machine-readable contracts in this folder;
4. `implementation-edition.md`;
5. Version 3 of the Architecture Bible;
6. prior source papers.

Never use an agent-generated summary to override a machine-readable contract.

## Required working sequence

1. Read `COPY-PASTE-AGENT-HANDOFF.md`.
2. Read `implementation-edition.md`.
3. Read `work-packages.yaml` and select one ready work package.
4. Verify every dependency is complete.
5. Read every contract named by the work package.
6. Write or update the tests named in its acceptance criteria.
7. Implement only the declared outputs.
8. Run the bundle validator and relevant implementation tests.
9. Update evidence, limitations, and unresolved work.
10. Stop at the declared human-approval boundary.

## Non-negotiable calculation boundary

- The deterministic calculation engine computes.
- SWMM and EPANET adapters execute declared models.
- The reconciliation service compares results.
- The agent explains, composes, and prepares review material.
- A human accepts, rejects, revises, or authorizes consequential action.

The agent must never generate an unregistered formula and present it as a governed calculation.

## Evidence classes

Every numerical value must be classified as exactly one of:

- `observed`
- `calculated`
- `modeled`
- `reconciled`
- `interpreted`

Do not remove or collapse these labels.

## Fail-closed rules

Return a structured data gap or blocked result when:

- the basin, event, station, or meter boundary is unresolved;
- source identity or effective time is unresolved;
- required units cannot be resolved;
- timestamps cannot be aligned;
- a required formula contract is absent or inactive;
- the pump configuration is unknown;
- the model version or model-file hash is missing;
- the result would require an unapproved jurisdiction rule;
- a requested action exceeds the caller's authority.

Do not fill missing engineering data with a silent default.

## Data rules

- Preserve raw records.
- Normalize through recorded transformations.
- Freeze every accepted input snapshot.
- Never mutate an old snapshot.
- Store units with values.
- Store source identifiers and effective timestamps.
- Use synthetic data only in examples and tests.
- Clearly label every synthetic value.

## Model rules

- SWMM represents declared rainfall, gravity-sewer, storage, surcharge, and overflow scenarios.
- EPANET represents declared pressurized-network scenarios.
- Model output never silently replaces observed or deterministic output.
- Every run records engine version, model hash, input hash, settings, start time, completion state,
  continuity or convergence findings, calibration state, validation state, and approved use.
- An uncalibrated model cannot be promoted to a calibrated or validated state by an agent.

## Agent rules

The agent may:

- retrieve governed context;
- identify missing data;
- invoke approved calculations and models;
- compare governed results;
- explain lineage;
- draft findings and investigation plans;
- request approval.

The agent may not:

- write to SCADA or pump controls;
- approve its own calculation or model;
- make a compliance determination;
- issue a work order;
- alter a model without a new version;
- modify a formula contract without formula governance;
- hide disagreement or uncertainty.

## Engineering and software quality

- Use decimal-safe or quantity-safe arithmetic where the contract requires it.
- Reject incompatible units.
- Make time zone and daylight-saving behavior explicit.
- Make every state transition testable.
- Keep APIs idempotent where declared.
- Pin external solver and library versions.
- Run uploaded models in isolated workers.
- Preserve complete audit records.
- Add tests before declaring a work package complete.

## Completion language

Use:

- `implemented candidate`
- `mechanically validated`
- `pending engineering review`
- `pending field validation`

Do not use:

- `100 percent accurate`
- `production ready`
- `certified`
- `compliant`

unless the corresponding approval record explicitly supports that statement.
