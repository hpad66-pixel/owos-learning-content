# Module 19 Phase 0 Reconciliation

## Governing identity

- Course: Meaning Before Models
- Module: 19 of 19
- Approved title: Design the One Water Knowledge Spine
- Role: Capstone design and defense
- Central question: What is the smallest governed semantic pilot worth building?
- Required prior learning: Modules 1 through 18 and the accumulated learner fieldbook
- Phase state: Reconciled and ready for owner design review
- Implementation state: Not started

## Correction to the historical record

An older curriculum note described Design the One Water Knowledge Spine as Module 18 and used a P-104 exposure scenario. That note predates the approved nineteen-module sequence and is not authoritative.

The approved sequence is:

1. Module 17: Operationalize and Scale
2. Module 18: Graph-Grounded Agentic Applications
3. Module 19: Design the One Water Knowledge Spine

Module 19 consumes the completed Module 18 Agent Action Contract. It does not repeat Module 18's authorization console, action-state machine, or operational-controls lesson.

## Prerequisite chain from Modules 1 through 18

| Module | Prior capability or artifact | How Module 19 uses it |
|---|---|---|
| 1 | Explain a subject-predicate-object relationship | Reject pilot concepts that cannot identify a meaningful relationship |
| 2 | Build and inspect utility triples | Specify candidate statements and identify weak predicates |
| 3 | Resolve identity across systems | Define durable identities for assets, events, documents, customers, and organizations |
| 4 | Traverse a small graph | State the bounded relationship question the pilot must answer |
| 5 | Distinguish the five meaning layers | Assign each design concern to its correct layer |
| 6 | Design a governed vocabulary | Identify controlled terms, synonyms, classifications, and stewardship |
| 7 | Model an ontology | Define the smallest classes, properties, and semantic rules needed |
| 8 | Write SPARQL patterns | Define competency questions and proof queries |
| 9 | Bound OWL inference | Declare permitted, explainable, and prohibited inferences |
| 10 | Define SHACL validation | Specify structural contracts and failure handling |
| 11 | Carry provenance and authority | Define source, time, jurisdiction, confidence, and authority controls |
| 12 | Compare semantic architectures | Select a fit-for-purpose architecture without defaulting to a copied enterprise graph |
| 13 | Map data in place | Identify virtual mappings, materialized hot paths, and synchronization risks |
| 14 | Govern unstructured evidence | Define extraction, citation, retrieval, and evidence-status controls |
| 15 | Test grounded answers | Establish answer-quality, freshness, abstention, and evidence measures |
| 16 | Assemble runtime context | Define the context package required for the pilot decision |
| 17 | Operationalize and scale | Assign owners, change controls, release controls, and repeatability measures |
| 18 | Govern graph-grounded actions | Supply a scored Agent Action Contract and its approval, retry, verification, and audit controls |

## Module 18 handoff contract

Module 19 accepts the Module 18 work product only when:

1. The Agent Action Contract scores at least 16 of 20.
2. It names one bounded action: create a draft inspection work order.
3. It distinguishes grounded evidence from permission to act.
4. It defines stale, ambiguous, denied, timeout, duplicate, failed-verification, and correction paths.
5. It preserves human approval before execution.
6. It defines idempotency, retry, post-action verification, and audit recording.
7. It does not authorize dispatch, priority assignment, closure, operational changes, credentials, graph publication, or autonomous control.

Module 19 maps every accepted Module 18 control to an architecture component, accountable owner, acceptance test, release or stop condition, and audit record.

## Capstone utility scenario

The design exercise uses a fictional ninety-day wastewater overflow-response pilot centered on Lift Station LS-7 and Overflow Event 21.

The bounded operational question is:

> When Overflow Event 21 occurs, which upstream assets and current evidence should a wastewater supervisor review before approving one draft inspection work order?

The pilot may assemble a decision package and, after explicit approval, create a draft inspection work order. It may not dispatch a crew, change operations, set work priority, close work, publish a graph, or exercise autonomous control.

All asset identifiers, dates, thresholds, conditions, performance figures, and operating details are instructional assumptions unless separately cited.

## Capstone decision

The learner must recommend one of three decisions:

- Build the bounded ninety-day pilot.
- Revise the pilot before investment.
- Do not build a knowledge-graph pilot for this question.

The recommendation requires a passed Graph Fit Test, explicit baseline and target, evidence and identity readiness, bounded semantics, validation and inference controls, access and authority controls, named owners, a ninety-day test plan, and stop and scale criteria.

## Evidence boundaries

- RDF, RDFS, OWL, SPARQL, and SHACL claims remain within authoritative W3C evidence.
- Knowledge Spine is a course architecture term, not a W3C standard.
- A context engine is an architectural capability, not the runtime context itself.
- SHACL conformance does not prove factual truth.
- OWL inference does not replace operator judgment or policy.
- A grounded answer does not create authorization to act.
- A knowledge graph is not automatically the right solution.
- Pilot metrics and thresholds require owner approval before real utility use.
- Cybersecurity and industrial-control decisions require qualified human review.

## Adjacent-module distinctiveness

| Module | Dominant experience | What Module 19 must not repeat |
|---|---|---|
| 17 | Operating model, ownership, and repeatability | A generic scale-up roadmap or lane diagram |
| 18 | Authorization control room and action-state transitions | An authorization console, action simulator, or state machine |
| 19 | Cross-functional pilot design and investment defense | A lesson that treats architecture or controls as the final decision |

## Phase 0 exit test

Phase 0 is complete because the approved sequence is preserved, each prerequisite has a capstone use, Module 18 has a testable handoff, the scenario and decision are bounded, evidence and authority limits are explicit, and no implementation work has begun.

