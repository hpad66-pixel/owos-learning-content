# Knowledge Spine and AI Context Teaching Pack

## The distinction learners must retain

| Concept | Plain question | What it contains | What it does not do alone |
| --- | --- | --- | --- |
| Data model | How is information structured here? | entities, attributes, keys, relationships, cardinalities, constraints | establish one shared enterprise meaning |
| Taxonomy | How are terms grouped? | controlled categories and hierarchies | express every relationship or rule |
| Ontology | What do these concepts and relationships mean? | shared concepts, properties, classifications, selected semantic rules | connect itself to every source record |
| Semantic layer | How does meaning resolve to enterprise data? | mappings, metric rules, identifiers, source policies, query services | package every task's runtime instructions and permissions |
| AI context | What does the model or agent need now? | evidence, definitions, entities, time, jurisdiction, policy, state, permissions, limits | remain permanently correct after the task changes |
| Context engine | How is that package assembled and checked? | retrieval, identity, filtering, validation, policy, authorization, formatting, logging | become the ontology or source of truth |

## Utility scenario: customer exposure during a pressure event

The question is:

> Which active customers may be exposed to a pressure-loss event affecting Pressure Zone 3, under
> the current advisory policy, and what action may the agent propose?

### What the data models contribute

The Customer Information System contains:

```text
ACCOUNT_ID
PREMISE_ID
SERVICE_STATUS
CUSTOMER_CLASS
START_DATE
END_DATE
```

The Geographic Information System contains:

```text
PREMISE_FEATURE_ID
SERVICE_LINE_ID
MAIN_SEGMENT_ID
PRESSURE_ZONE_CODE
```

The Supervisory Control and Data Acquisition system contains:

```text
TAG_ID
ASSET_ID
OBSERVATION_TIME
PRESSURE_VALUE
UNIT
QUALITY_CODE
```

Each model structures its own records. None of the three alone defines exactly what “active
customer exposed to the event” means.

### What the taxonomy contributes

The taxonomy classifies:

```text
Customer
  ResidentialCustomer
  CommercialCustomer
  CriticalFacilityCustomer

PressureEvent
  LowPressureEvent
  PressureLossEvent
  SuspectedSensorEvent
```

This creates consistent grouping. It does not yet define the cross-system path from event to zone to
premise to account.

### What the ontology contributes

Illustrative triples:

```text
Pressure_Event_771 -> affects -> Pressure_Zone_3
Premise_22018 -> located_in -> Pressure_Zone_3
Service_Account_882 -> serves -> Premise_22018
Service_Account_882 -> has_status -> Active
Service_Account_882 -> has_customer_class -> Critical_Facility
Advisory_Policy_12 -> applies_to -> Pressure_Loss_Event
```

Illustrative meaning:

- a service account is active during a period;
- an account serves a premise;
- a premise is located in a pressure zone;
- a pressure event affects a zone;
- an advisory policy applies in a jurisdiction and effective period;
- a critical facility is a customer classification with an escalation route.

The ontology makes the relationships and categories reusable. It does not automatically know which
source fields contain the current account status or pressure reading.

### What the semantic layer contributes

Illustrative mappings:

| Shared meaning | Source resolution |
| --- | --- |
| `ServiceAccount` | CIS `ACCOUNT_ID` |
| `serves` | CIS relationship from `ACCOUNT_ID` to `PREMISE_ID` |
| `Premise` | canonical identity mapped from CIS `PREMISE_ID` and GIS `PREMISE_FEATURE_ID` |
| `locatedInPressureZone` | GIS premise-to-zone topology |
| `hasStatus Active` | CIS `SERVICE_STATUS = 'A'`, subject to effective-date rule |
| `PressureEvent` | event derived from approved SCADA quality and threshold logic |
| `appliesPolicy` | approved policy registry by event type, jurisdiction, and effective time |

The layer also names authoritative sources, owners, freshness, tests, and conflict behavior.

### What the context engine does

For one request, the engine:

1. Identifies the user and intended task.
2. Resolves `Pressure_Event_771` and `Pressure_Zone_3`.
3. Checks whether the user may access customer and critical-facility information.
4. Queries approved mappings across SCADA, GIS, and CIS.
5. Retrieves the current policy for the event time and jurisdiction.
6. Detects stale GIS topology for one premise and records the conflict.
7. Validates required identifiers, units, timestamps, policy version, and evidence references.
8. Builds a bounded context packet.
9. Excludes fields that the task does not need.
10. Supplies permitted tool and action boundaries.
11. Logs the ontology, mapping, policy, source snapshots, query, and context contract versions.

### What the AI context contains

```text
Task:
  Prepare a customer-exposure review for Pressure_Event_771.

Resolved entities:
  Event: Pressure_Event_771
  Zone: Pressure_Zone_3
  Jurisdiction: Utility_Service_Area

Evidence:
  Pressure observation and quality code
  Event-to-zone relationship
  Zone-to-premise relationships
  Premise-to-active-account relationships
  Current approved advisory policy

Definitions:
  Active account
  Exposure candidate
  Critical facility

Time:
  Event observation time
  Account effective time
  Policy effective time
  Evidence freshness limits

Permissions:
  User may view aggregate customer counts.
  User may view identified critical facilities.
  User may not export the complete customer list.

Workflow state:
  Exposure review is draft.
  Operations confirmation is pending.

Permitted actions:
  Draft an exposure summary.
  Propose a review queue.
  Do not issue an advisory.
  Do not change operational controls.

Known conflict:
  Premise_22018 has stale zone topology and requires GIS steward review.

Output:
  Evidence-backed summary, counts, exceptions, citations, and proposed next step.
```

The language model receives this package. It does not receive permission to invent a missing
relationship or convert the draft into an issued advisory.

## From paper ontology to running capability

| Stage | Paper-only state | Operational state |
| --- | --- | --- |
| Definition | “Active customer” appears in a glossary | definition has an identifier, owner, version, and effective scope |
| Structure | entity boxes appear in a diagram | classes and properties are machine-readable |
| Data connection | arrows point vaguely to systems | mappings resolve concepts to fields, APIs, graph terms, and documents |
| Instances | examples are typed in slides | identified accounts, premises, zones, policies, and events are queryable |
| Validation | reviewers say the model looks complete | shapes test required identifiers, dates, units, roles, and values |
| Query | expected questions appear in notes | competency questions run as repeatable graph patterns |
| Reasoning | rules are written in prose | selected semantics or rules produce visible proof traces |
| Governance | a workshop approves the slide | ontology, mappings, shapes, and tests are versioned and released |
| Use | the model is referenced occasionally | BI, applications, agents, and stewards use governed services |
| Feedback | errors stay in downstream reports | usage and corrections become stewarded model changes |

## The One Water Knowledge Spine

### Ontology and Governance Core

Contains:

- identified concepts and relationships;
- definitions, labels, classifications, and selected axioms;
- SHACL shapes and validation severities;
- source and authority policies;
- model ownership and stewardship;
- version, release, deprecation, and supersession records;
- competency questions and tests.

### Semantic Platform

Provides:

- stored and virtual graph access;
- SPARQL and application APIs;
- approved reasoning profiles;
- SHACL validation;
- query planning and federation;
- named graph and access controls;
- provenance and observability;
- model and mapping release management.

### Connection Fabric

Connects:

- lakehouse and warehouse tables;
- GIS, SCADA, CMMS or EAM, LIMS, CIS, and document systems;
- domain knowledge graphs;
- event streams and APIs;
- document indexes and extraction pipelines;
- governed caches and selected materialized graphs.

### Consumption Plane

Serves:

- BI and analytics;
- operational and enterprise applications;
- search and retrieval;
- context engines;
- language models and agents;
- data steward and ontology change workflows.

## Virtualize before materialize, with a decision gate

### Scenario A: customer status

The CIS is current, supports selective queries, and remains authoritative. Virtual mapping may be a
good starting point.

### Scenario B: emergency exposure path

The answer must return during a CIS outage within seconds. A governed, frequently refreshed hot-path
materialization may be justified.

### Scenario C: high-frequency telemetry

Do not convert every raw sensor reading into permanent RDF merely because RDF is available. Keep the
time series in its suited platform. Represent the sensor, observed property, quality, event, and
selected evidence links in the graph.

### Scenario D: procedures and permits

Preserve originals in the document system. Build a governed search index, extract candidate clauses
and entities, and connect approved claims to exact passages, versions, effective dates, and
jurisdictions.

### Scenario E: repeated analytical aggregate

If every query recomputes the same expensive cross-source aggregate, an approved materialized view
may be simpler and cheaper.

## Structured and unstructured evidence are different

| Method | Useful for | Does not establish by itself |
| --- | --- | --- |
| Keyword search | exact terms, identifiers, clauses | semantic equivalence |
| Vector similarity | conceptually related passages | explicit relationship or authority |
| Entity extraction | candidate assets, people, places, events, clauses | approved identity or truth |
| RDF assertion | explicit identified relationship | source authority or completeness |
| Ontology inference | declared logical consequence | observation, approval, or prediction |
| SHACL validation | structural conformance | real-world truth |
| Human review | purpose-specific approval | permanent correctness after data or policy changes |

## Failure simulations

### Missing ontology

The model treats “active contract” as “a row with no closed date.” The business actually requires an
approved status plus an effective date range and jurisdiction. The answer includes inactive
customers.

### Ontology without mappings

The definition is correct, but no runtime service knows that CIS code `A` and the effective-date rule
instantiate `ActiveServiceAccount`. The application cannot answer the question.

### Mapping without change control

The CIS team renames a status column and changes a code. The virtual query still runs but maps the
wrong field. Contract tests should fail before the answer reaches a learner or agent.

### Context without effective time

The engine retrieves the newest policy document by upload date, not the policy effective at the
event time. The model cites the wrong procedure.

### Retrieval without authority

Vector search ranks an outdated draft above the approved procedure because the wording is more
similar to the question.

### Graph without permissions

The evidence path is correct, but the requesting role is not authorized to view customer-level
details. The correct application result is denial or an aggregate response.

### Correct answer without action authority

The agent identifies likely exposure correctly. It may draft a review packet but may not issue the
advisory or change control settings.

## What this architecture improves

When governed well, the pattern can improve:

- consistency of definitions across applications;
- reuse of identity and relationships;
- traceability from answer to evidence;
- handling of source authority and effective time;
- query across structured and unstructured evidence;
- visible validation and inference boundaries;
- controlled context assembly;
- separation between recommendation and permission to act.

It does not guarantee accurate sources, complete graphs, correct mappings, safe policies, available
systems, perfect retrieval, deterministic generation, or authorized action.
