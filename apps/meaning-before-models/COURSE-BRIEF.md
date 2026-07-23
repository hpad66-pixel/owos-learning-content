# Course Brief

## Working title

Meaning Before Models: RDF and Knowledge Graphs for Utilities

## Subtitle

How relationships, rules, and evidence become machine-readable knowledge

## Course promise

Give every utility learner, including nontechnical staff, a durable mental model for semantic data.
The learner starts with one plain relationship, builds it into a graph, and learns how RDF, RDFS,
SPARQL, OWL, SHACL, provenance, and agentic applications perform different jobs.

Module 01 preserves the original fifteen-minute course as a complete primer. The remaining modules
turn recognition into practical competence without requiring prior coding or data-modeling
experience.

## Utility connection

The lesson begins with three plain questions:

1. Water: Which customers are served by the pressure zone affected by this pump?
2. Wastewater: Which upstream lift stations could contribute to this overflow?
3. Stormwater: Which outfalls drain the catchments where an inspection found debris?

The records may exist in several systems. The missing piece is a consistent way to state what each
thing is and how it relates to the next thing.

## Working reframe

Data becomes more useful when its relationships carry meaning. RDF starts with one statement that
is small enough to say out loud:

```text
subject -> predicate -> object
```

Then the lesson repeats the pattern until it becomes familiar:

```text
Pump_P104 -> serves -> Pressure_Zone_3
Lift_Station_7 -> flows_to -> Treatment_Plant_2
Outfall_12 -> drains -> Catchment_5
```

Once several triples share the same things, the learner can see a graph forming:

```text
Pump_P104 -> serves -> Pressure_Zone_3
Pressure_Zone_3 -> contains -> Customer_Account_882
Pump_P104 -> has_work_order -> Work_Order_4821
Work_Order_4821 -> reports -> Seal_Leak
```

The “wow” moment is that the machine does not receive understanding as one giant document. It can
follow many small, explicit relationships.

## Course architecture

| Part | Learner question | Capability built |
| --- | --- | --- |
| I. See the relationships | What does this data mean, and which thing is which? | Read triples, trace graphs, and resolve identity. |
| II. Build shared meaning | How do structure, taxonomy, ontology, and semantics differ? | Model shared concepts and query graph patterns. |
| III. Trust the graph | What may be inferred, what must be present, and who said what when? | Separate reasoning, validation, provenance, authority, and time. |
| IV. Operate the Knowledge Spine | How does shared meaning connect to data and documents without unnecessary copying? | Instantiate, map, federate, materialize selectively, and assemble context. |
| V. Apply the backbone | How does this improve BI, RAG, agents, and utility decisions? | Compare architectures, control agent actions, and design a pilot. |

## Module 01: the fifteen-minute learner experience

| Time | Learner experience | Intended realization |
| --- | --- | --- |
| 0:00 to 2:00 | Answer three deceptively simple utility questions | The data may exist while the relationships remain implicit. |
| 2:00 to 5:00 | Build and correct subject, predicate, and object triples | An RDF statement is one named relationship. |
| 5:00 to 8:00 | Watch triples from everyday life and utility work connect into a graph | Connected meaning grows from repeated small statements. |
| 8:00 to 12:00 | Explore RDF, RDFS, SPARQL, OWL, and SHACL by the job each performs | Model, describe, query, infer, and validate are different jobs. |
| 12:00 to 15:00 | Ask one graph question, then write one useful utility triple | Connected meaning can be queried and reused. |

## Program outcomes

By the end of the course, learners can:

1. Read and write subject-predicate-object triples.
2. Explain how identifiers, literals, classes, properties, and shared nodes form an RDF graph.
3. Resolve a real asset identity across SCADA, GIS, CMMS or EAM, laboratory, document, and staff
   vocabularies.
4. Distinguish RDF, RDFS, SPARQL, OWL, and SHACL by the job each performs.
5. Read and modify a small SPARQL query without treating the course as a programming class.
6. Explain the difference between an asserted fact, an inferred statement, a validation result, and
   an approved operational claim.
7. Apply the open-world principle: absent data is usually unknown, not automatically false.
8. Attach source, authority, effective time, version, and supersession to important statements.
9. Compare table joins and BI, document RAG, RDF graph retrieval, and graph-grounded agents without
   making false deterministic-versus-probabilistic claims.
10. Distinguish a data model, taxonomy, ontology, semantic layer, context engine, and runtime
    artificial intelligence context.
11. Explain how a paper ontology becomes instantiated, queryable, governed operational knowledge.
12. Choose among virtualization, indexing, caching, and materialization based on workload,
    governance, latency, and cost.
13. Connect structured records and unstructured evidence without pretending that embeddings,
    extracted entities, and explicit graph relationships are the same.
14. Design a small utility semantic-backbone pilot with a measurable operational question, named
    sources, validation rules, access controls, and human approval boundaries.

## Required example bank

The lesson should rotate quickly through familiar relationships before returning to utility work:

- a person lives at an address;
- a child attends a school;
- a medication treats a condition;
- a vehicle is registered to an owner;
- a purchase belongs to a customer;
- a pump serves a pressure zone;
- a valve isolates a main segment;
- a sample was collected at a location;
- a work order concerns an asset;
- a lift station flows to a treatment plant;
- a sewer segment is upstream of an overflow location;
- an outfall drains a catchment;
- a catchment received an inspection;
- a permit applies to a discharge point.

Every example must clearly identify the subject, predicate, and object. Several examples must chain
into a graph, because isolated triples alone do not create the intended recognition.

## Content and safety boundaries

- Keep the common path accessible to nontechnical staff. Practitioner views may expose syntax and
  implementation detail, but no learner must become a programmer to understand the course.
- Teach “RDF” as singular. Explain that RDF data consists of many triples.
- Explain the difference among subject, predicate, and object.
- Explain the difference among RDF, RDFS, SPARQL, OWL, and SHACL by their jobs.
- Teach SPARQL through readable graph patterns, query assembly, and utility questions. Keep advanced
  syntax optional.
- Preview inference, validation, references, semantics, and provenance without compressing them into
  one vague idea.
- Keep existing databases, geographic systems, telemetry platforms, and lakehouses in their proper
  roles. The relationship layer sits above and across them.
- Distinguish the ontology from its operational instantiation, mappings, data, query services, and
  runtime context.
- Do not use “Knowledge Spine” as a new name for every database, integration, or graph.
- Teach that virtualization still requires connections, mappings, credentials, query planning,
  performance controls, and source availability.
- Teach that unstructured documents become usable through several methods, including metadata,
  extraction, search, embeddings, and explicit graph connections. No single method captures all
  meaning.
- Do not claim that a knowledge graph guarantees a correct artificial intelligence answer.
- Do not teach that tables are deterministic, RAG is always indeterministic, or graph applications
  are automatically deterministic. Identify the fixed and variable parts of each complete pipeline.
- Teach that SHACL validation checks declared constraints, not real-world truth.
- Teach that OWL inference derives statements under declared semantics, not human judgment.
- Teach that missing data is not automatically false.
- Treat expert statements as candidate knowledge until source, authority, review, and effective time
  are recorded.
- Include cases where RDF is unnecessary or disproportionate.
- Do not use the supplied third-party diagram as released artwork without permission.

## Depth model

Each module has three instructional views:

- Foundation: plain language, visual examples, pronunciation, and one practical decision.
- Practitioner: identifiers, triples, query or rule detail, data contracts, and implementation
  considerations.
- Leader: value, risk, governance, accountability, and the next investment decision.

The views share the same core claims. They change the level of detail, not the truth presented.

## Work-product progression

The learner builds a Utility Semantic Starter Pack: a relationship card, four-concept distinction
map, identity crosswalk, small graph, taxonomy and ontology sheet, SPARQL question, inference
boundary, SHACL contract, authority and provenance ledger, Knowledge Spine architecture, mapping
record, virtualize-or-materialize decision, context contract, architecture comparison, agent action
contract, and final pilot canvas.

## Relationship to existing OWOS courses

This is a standalone foundational course that connects to `Data Before AI: Data and Artificial
Intelligence Governance for Utilities`.

`Data Before AI` explains why governed data matters. This course shows how shared identity,
relationships, constraints, provenance, and reasoning can be represented. Module 01 can still be
used independently as the short concept primer.

## Current boundary

The comprehensive course scope and connection to `Data Before AI` are approved direction. The
detailed eighteen-module blueprint, original visual treatment, golden lesson, and release still
require their normal reviews.
