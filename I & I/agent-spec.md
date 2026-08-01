# Agentic I&I Application Technical Contract

Status: architecture draft, implementation prohibited  
Version: 0.1.0  

## Purpose

The application will analyze infiltration and inflow for United States sanitary sewer systems. It
will combine monitored data, asset records, rainfall, groundwater, operations, field investigation,
models, costs, and jurisdiction-specific rules without confusing one type of evidence with another.

The agent may calculate, compare, flag, explain, and assemble a review package. It may not certify
capacity, approve a design, declare compliance, select a rehabilitation project, or control a
facility without the separately required professional and organizational approvals.

## Core architecture

```text
Source and data intake
-> identity, units, time, geography, and ownership validation
-> data quality and missingness classification
-> system and basin boundary resolver
-> dry-weather baseline engine
-> wet-weather event engine
-> formula registry and unit engine
-> RDII and RTK engine
-> hydraulic context engine
-> investigation and defect evidence layer
-> rehabilitation verification engine
-> economics and prioritization engine
-> jurisdiction rule-pack evaluator
-> uncertainty and sensitivity engine
-> provenance-rich result and review dossier
```

## Calculation classes

The method-selection layer is mandatory. EPA's 2008 RDII methods review found that no single
prediction method is universally applicable. The application therefore treats universality as a
common data, evidence, validation, and result contract across multiple approved methods.

### Universal identities

These include exact unit conversions, time integration, ratios, mass balance, present value, and
other mathematics that do not change by jurisdiction. They still require declared units, time
bases, boundaries, and numerical policies.

### Engineering methods

These include dry-weather baseline methods, groundwater infiltration estimates, event separation,
RTK hydrographs, regression, hydraulic calculations, cost-effectiveness, and before-and-after
verification. They are portable methods, not universally interchangeable answers. The agent must
select them only when their assumptions and data requirements pass.

### Screening metrics

Peak ratios, gallons per day per inch-diameter-mile, gallons per linear foot, and other normalized
metrics help compare records. They do not locate a defect, prove causation, certify capacity, or
establish a national pass or fail value.

### Jurisdiction rules

Federal, state, local, permit, consent-decree, and utility rules are versioned separately from the
mathematical engine. A rule pack must include authority, exact locator, effective date, geography,
regulated entity, metric definition, units, calculation method, exceptions, and review date.

## Required result envelope

Every calculation result must return:

- result value and unit;
- formula identifier and version;
- source or derivation identifiers;
- input values, units, timestamps, lineage, and quality flags;
- basin, system, event, and jurisdiction boundary;
- assumptions and method selection reason;
- applicability checks and their pass or fail state;
- uncertainty interval or a specific reason it cannot be estimated;
- sensitivity results where material;
- warnings and excluded conclusions;
- validation-suite version;
- jurisdiction rule-pack version, when used;
- reviewer and approval state; and
- a deterministic calculation trace suitable for reproduction.

## Fail-closed conditions

The agent must refuse a numerical or decision conclusion when:

- a material unit, time basis, or system boundary is missing;
- a local threshold is requested without a current applicable rule pack;
- flow and rainfall timestamps cannot be aligned;
- a dry-weather baseline is not defensible;
- the event recession is materially truncated;
- meter behavior under surcharge, backwater, fouling, or low depth is unresolved;
- tributary area or asset inventory does not match the numerator;
- an RTK parameter set is used outside its calibrated conditions without a stated transfer method;
- uncertainty is material but unavailable;
- a screening metric is being used as a design or compliance result;
- a formula has not reached production status; or
- the requested decision requires licensed professional judgment or facility authority.

## No silent defaults

The application may offer a candidate default with its source and consequence, but it cannot apply
that default until the user or an approved configuration selects it. This applies to rainfall
windows, dry-day definitions, base-flow methods, meter gap limits, RTK initial abstraction,
tributary area, pipe inventory, roughness, discount rate, asset life, cost escalation, comparison
storm, confidence level, and every regulatory or program threshold.

## Separation of evidence

The result must label each statement as measured, calculated, modeled, inferred, reported by an
external party, regulatory, or unresolved. A repaired defect is measured work. A modeled gallon
reduction is a model result. A lower post-repair hydrograph is an observation. A causal
rehabilitation benefit requires a defensible comparison. The agent must never collapse those into
one unsupported claim.

## Production condition

Implementation may begin against candidate formulas, but no output may be used for an engineering,
capital, operating, or compliance decision until the applicable formulas, rule packs, and model
paths pass `verification-plan.yaml` and receive qualified approval.
