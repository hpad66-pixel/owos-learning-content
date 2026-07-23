# RDF Comparison and Simulation Pack

## Purpose

This pack supplies the practical core for Modules 10 and 11 of `Meaning Before Models: RDF and
Knowledge Graphs for Utilities`. It compares familiar data and business-intelligence work with
retrieval-augmented generation (RAG), graph-grounded retrieval, formal reasoning, and an agentic
application.

Module 01 may preview the distinction in one sentence. The complete comparison and simulations
belong in the later application modules so the opening primer can stay focused.

## The accurate distinction

The course must not use “deterministic versus indeterministic” as a shortcut for “tables versus
graphs.”

- A Structured Query Language (SQL) query over a fixed data snapshot with fixed logic is normally
  repeatable.
- A Power BI semantic model can encode explicit table relationships, measures, and filter
  propagation. Those are real semantics, but they are usually local to that model.
- An RDF graph can also return repeatable results when the graph, query, inference rules, and
  software versions are fixed.
- RAG combines retrieval with language generation. Retrieval may change when the index, ranking,
  query, filters, or corpus changes. Generated wording and unsupported hypotheses may vary when
  probabilistic decoding is used.
- A graph-grounded agent can keep facts, relationship paths, rules, and validation deterministic
  while still using a language model to explain the result. The explanation may vary even when the
  evidence path does not.
- An agentic application adds tools, state, permissions, and actions. It needs explicit stop
  conditions and human authority regardless of the knowledge source.

The useful comparison is therefore:

> Which parts are fixed and inspectable, which parts are retrieved or inferred, which parts are
> generated, and which actions require human approval?

## Course comparison table

| Dimension | Joined tables and Power BI | Document RAG | RDF graph-grounded agent |
| --- | --- | --- | --- |
| Primary representation | Rows, columns, keys, measures, and a report model | Document chunks, embeddings, metadata, and a vector index | Named entities, predicates, objects, vocabularies, rules, constraints, and provenance |
| How relationships are expressed | Foreign keys and model relationships selected for a known report | Similarity between a question and passages, plus metadata filters | Explicit triples with stable identifiers and named predicates |
| Typical question | “Show vibration alarms by pump and month.” | “What do our documents say about recurring vibration?” | “Which alarm, work order, condition, location, and operator note are connected to Pump P-104?” |
| Query mechanism | SQL, Data Analysis Expressions (DAX), and report filters | Vector or hybrid retrieval followed by a language-model prompt | SPARQL graph patterns, optional inference, and language generation over the selected evidence |
| Repeatability | High when data, model, measures, and filters are fixed | Retrieval and wording may vary with index, ranking, query rewriting, and model decoding | Graph query and formal rules can be repeatable; generated explanation may still vary |
| Meaning boundary | Meaning is often embedded in table names, column definitions, measures, and report logic | Meaning is carried in prose and inferred by the retriever and model | Meaning is represented through identifiers, classes, predicates, and controlled vocabularies |
| New relationship | Usually requires a new join, model change, transformation, or measure | May be found in text without a schema change, but may be ambiguous | Add a governed triple or mapping, then query it with other relationships |
| Reasoning | Calculations and business rules explicitly written into queries or measures | Language-model interpretation over retrieved text | RDF Schema or OWL entailment when declared, plus explicit application rules |
| Validation | Data types, constraints, pipeline tests, reconciliation, and report-model checks | Chunk quality, retrieval evaluation, citation checks, and answer evaluation | SHACL shapes, identity checks, graph tests, query tests, and source-boundary checks |
| Provenance | Report lineage and source-system lineage when configured | Retrieved passages and citations when retained correctly | Relationship-level provenance can connect a statement to its source, activity, agent, and version |
| Anomaly detection | Statistical rule or model produces a score shown in a report | Retrieved documents help explain or contextualize the anomaly | Anomaly node connects to asset, observation, threshold, work, place, source, rule, and decision |
| Best fit | Stable metrics, aggregation, trends, and repeatable reporting | Searching and summarizing large document collections | Cross-system relationship questions, explainable paths, rules, provenance, and controlled action context |
| Common failure | The needed relationship was never modeled, or a measure hides its assumptions | The wrong passages are retrieved, evidence conflicts, or fluent text exceeds the evidence | Identity mappings are wrong, predicates are poorly governed, rules are overclaimed, or stale graph data is treated as current |
| Agentic connection | Agent calls a report or query as one tool | Agent retrieves passages and drafts an answer | Agent queries relationships, checks constraints and authority, proposes an action, waits for approval, then records provenance |

## Running scenario: Pump P-104

All names and values below are fictional instructional data.

### Source records

| Source | Record |
| --- | --- |
| Telemetry historian | Alarm A-77 observed on Pump P-104 at 02:14; vibration value 9.2 millimeters per second |
| Asset registry | Pump P-104 is located at Lift Station 7 |
| Work system | Work Order 4821 concerns Pump P-104 and reports a seal leak |
| Hydraulic model | Pump P-104 serves Pressure Zone 3 |
| Customer system | Customer Account 882 is located in Pressure Zone 3 |
| Operator knowledge note | Note 19 describes Pump P-104 and says seal leakage has previously increased after heavy rain |
| Procedure library | Procedure M-12 requires vibration verification before a maintenance recommendation |

### RDF-style triples

```text
Alarm_A77 -> observed_on -> Pump_P104
Alarm_A77 -> observed_at -> 2026-07-23T02:14
Alarm_A77 -> has_metric -> Vibration
Alarm_A77 -> has_value -> 9.2_mm_per_s
Pump_P104 -> located_at -> Lift_Station_7
Pump_P104 -> serves -> Pressure_Zone_3
Pressure_Zone_3 -> contains -> Customer_Account_882
Work_Order_4821 -> concerns -> Pump_P104
Work_Order_4821 -> reports_condition -> Seal_Leak
Note_19 -> describes -> Pump_P104
Note_19 -> authored_by -> Operator_Maya
Note_19 -> reports_pattern -> Rain_Associated_Seal_Leak
Procedure_M12 -> applies_to -> High_Vibration_Alarm
Procedure_M12 -> requires_check -> Verify_Vibration
```

### Provenance triples

```text
Statement_301 -> was_derived_from -> Historian_Record_A77
Statement_301 -> was_generated_by -> Historian_Import_Run_44
Historian_Import_Run_44 -> was_associated_with -> Telemetry_Connector
Statement_309 -> was_derived_from -> Operator_Note_19
Operator_Note_19 -> was_attributed_to -> Operator_Maya
```

The provenance relationships follow the general Entity, Activity, and Agent pattern supported by
the W3C PROV Ontology. The lesson can translate those terms into source, process, and accountable
person for leaders.

## Simulation 1: Same question, three architectures

### Learner question

> What do we know about Pump P-104, and what should happen next?

### Joined-table and Power BI result

With fixed tables, joins, filters, and measures:

```text
Pump: P-104
Latest vibration: 9.2 mm/s
Open work order: 4821
Reported condition: seal leak
```

This is repeatable and useful. It answers the fields that were modeled. It does not automatically
follow operator knowledge, procedure applicability, customer impact, or provenance unless those
relationships were added to the model.

### Illustrative document-RAG runs

These are static teaching examples of possible variation, not recorded outputs from a live model.

Run 1 retrieves the alarm summary and a generic maintenance guide:

```text
Pump P-104 has high vibration. Bearing wear or misalignment may be responsible. Inspect the pump.
```

Run 2 retrieves the work order and Operator Note 19:

```text
Pump P-104 has a seal leak, and a prior operator note associates seal leakage with heavy rain.
Prioritize a seal inspection.
```

Run 3 retrieves the alarm, work order, and procedure:

```text
Pump P-104 has a high-vibration alarm and an open seal-leak work order. Verify the vibration under
Procedure M-12 before recommending maintenance.
```

The answers differ because different passages were selected and because the generator composes an
answer rather than returning a fixed row set. The first answer also introduces possible causes not
supported by the fictional utility records. RAG can be useful and still needs retrieval evaluation,
source display, and answer boundaries.

### Graph-grounded agent result

The graph query returns a stable evidence path:

```text
Alarm_A77 -> observed_on -> Pump_P104
Work_Order_4821 -> concerns -> Pump_P104
Work_Order_4821 -> reports_condition -> Seal_Leak
Procedure_M12 -> applies_to -> High_Vibration_Alarm
Procedure_M12 -> requires_check -> Verify_Vibration
```

The agent may explain the path in different words, but it must preserve these facts:

```text
Pump P-104 has Alarm A-77 and Work Order 4821. The work order reports a seal leak. Procedure M-12
requires vibration verification before a maintenance recommendation. Draft the verification task
for operator review. Do not state a root cause from the available evidence.
```

This is not “the graph makes artificial intelligence deterministic.” The controlled result comes
from fixing the graph snapshot, query, rules, validation, output boundary, and approval path.

## Simulation 2: Watch a small graph form

### Step 1: One statement

```text
Pump_P104 -> serves -> Pressure_Zone_3
```

### Step 2: Reuse the object as a new subject

```text
Pressure_Zone_3 -> contains -> Customer_Account_882
```

Now the application can follow a path from pump to customer account.

### Step 3: Connect an operational event

```text
Alarm_A77 -> observed_on -> Pump_P104
```

Now the application can ask which customer area is associated with the alarmed pump.

### Step 4: Connect work and evidence

```text
Work_Order_4821 -> concerns -> Pump_P104
Work_Order_4821 -> reports_condition -> Seal_Leak
```

Now the graph connects the alarmed asset to known work evidence without claiming that the seal leak
caused the alarm.

### Step 5: Connect procedure and authority

```text
Procedure_M12 -> applies_to -> High_Vibration_Alarm
Procedure_M12 -> requires_check -> Verify_Vibration
Operator_Maya -> authorized_for -> Verify_Vibration
```

Now an application can propose a bounded next step and identify an authorized role. Human approval
still controls the action.

## Simulation 3: Query, infer, validate, act

| Stage | Mechanism | Pump P-104 example | Deterministic boundary |
| --- | --- | --- | --- |
| Query | SPARQL matches explicit graph patterns | Find alarms, work orders, procedures, and authorized roles connected to P-104 | Repeatable for a fixed graph and query engine |
| Infer | Declared RDF Schema or OWL rules make implicit facts explicit | If every `HighVibrationAlarm` is a `MechanicalAlarm`, infer that A-77 is a `MechanicalAlarm` | Repeatable for fixed axioms, profile, reasoner, and data |
| Validate | SHACL checks required graph structure | A maintenance-task proposal must have an asset, evidence, procedure, owner, and approval state | Repeatable for fixed shapes, graph, and validator |
| Generate | Language model explains the evidence | Summarize the path in plain English | Wording may vary unless templated or otherwise constrained |
| Act | Agent calls an approved tool | Draft, but do not submit, a vibration-verification task | Permission, state, and human approval control the action |
| Record | Provenance is written back | Record the query, graph version, sources, proposed task, reviewer, and decision | Stable identifiers and append-only evidence support reconstruction |

## Agentic application flow

```text
Question
-> identify asset and requested decision
-> query the RDF graph
-> apply declared inference
-> run SHACL validation
-> retrieve supporting documents when needed
-> generate an explanation bounded by the graph path
-> propose an authorized tool action
-> wait for human approval
-> execute or stop
-> write the outcome and provenance back to the graph
```

The graph does not replace documents, telemetry, Power BI, or source applications. It supplies a
shared relationship and provenance layer that an agent can query before it explains or acts.

## Simulation 4: Capturing enterprise and individual knowledge

### Spoken expert knowledge

An operator says:

> When P-104 vibration rises after heavy rain, check the seal area before assuming bearing failure.

Do not publish this as an unquestioned rule. Capture it as a candidate knowledge object:

```text
Candidate_Claim_44 -> describes -> Pump_P104
Candidate_Claim_44 -> proposes_check -> Inspect_Seal_Area
Candidate_Claim_44 -> applies_when -> Heavy_Rain_And_High_Vibration
Candidate_Claim_44 -> was_attributed_to -> Operator_Maya
Candidate_Claim_44 -> was_derived_from -> Interview_2026_07_23
Candidate_Claim_44 -> has_review_status -> Pending_Engineering_Review
```

After review, the approved relationship or rule receives its own identifier and effective date. The
original claim remains linked as provenance.

### Enterprise policy knowledge

```text
Procedure_M12 -> requires_check -> Verify_Vibration
Procedure_M12 -> approved_by -> Maintenance_Manager
Procedure_M12 -> effective_on -> 2026_01_15
Procedure_M12 -> supersedes -> Procedure_M10
```

### Company operating knowledge

```text
Lift_Station_7 -> owned_by -> Riverbend_Utility
Pump_P104 -> maintained_by -> Mechanical_Team_East
Mechanical_Team_East -> reports_to -> Maintenance_Division
Maintenance_Division -> accountable_for -> Pump_Reliability
```

The graph can connect individual knowledge, approved procedures, organizational responsibility, and
physical assets while preserving their different authority levels.

## Water, wastewater, and stormwater triple bank

### Water

```text
Pump_P104 -> serves -> Pressure_Zone_3
Valve_V22 -> isolates -> Main_Segment_M18
Sample_S55 -> collected_at -> Entry_Point_EP2
Entry_Point_EP2 -> supplies -> Pressure_Zone_3
Customer_Account_882 -> located_in -> Pressure_Zone_3
Work_Order_4821 -> concerns -> Pump_P104
```

### Wastewater

```text
Lift_Station_L7 -> flows_to -> Interceptor_I4
Interceptor_I4 -> flows_to -> Treatment_Plant_T2
Overflow_Event_O9 -> occurred_at -> Manhole_MH44
Manhole_MH44 -> downstream_of -> Lift_Station_L7
Rain_Gauge_R3 -> observed -> Rain_Event_RE8
Overflow_Event_O9 -> occurred_during -> Rain_Event_RE8
```

### Stormwater

```text
Outfall_OF12 -> drains -> Catchment_C5
Catchment_C5 -> contains -> Inlet_IN88
Inspection_I31 -> inspected -> Outfall_OF12
Inspection_I31 -> observed_condition -> Debris_Blockage
Permit_P9 -> applies_to -> Outfall_OF12
Maintenance_Task_MT6 -> addresses -> Debris_Blockage
```

### People, work, and decisions

```text
Operator_Maya -> performed -> Inspection_I31
Engineer_Lee -> reviewed -> Candidate_Claim_44
Manager_Rosa -> approved -> Procedure_M12
Decision_D18 -> used_evidence -> Alarm_A77
Decision_D18 -> selected_action -> Verify_Vibration
Decision_D18 -> authorized_by -> Manager_Rosa
```

## Final learner conclusion

The learner should be able to say:

> A table joins values for a modeled analytical job. RAG retrieves passages and generates language.
> RDF states explicit relationships that can be queried, inferred over, validated, traced to sources,
> and used by an agent under controlled authority. These approaches can work together.
