# Meaning Before Models: RDF and Knowledge Graphs for Utilities

## Course promise

Understand knowledge graphs from the first triple through a running utility Knowledge Spine. Learn
how structure, shared meaning, enterprise data, documents, policies, runtime context, and controlled
agents connect without pretending they are the same thing.

## Intended learners

Primary learners are utility professionals and leaders who use data and make or govern decisions
but do not begin with semantic-technology or programming experience. This includes operators,
maintainers, engineers, laboratory staff, planners, customer-service staff, managers, executives,
board members, and emerging leaders.

Secondary learners include data, Geographic Information System, operational-technology,
information-technology, cybersecurity, analytics, artificial-intelligence, and governance
practitioners. They receive optional implementation depth while sharing the common language and
decision model.

## Format

- Twenty-module foundational master class in five parts
- Estimated eighteen guided hours plus a six-hour capstone, pending pilot
- Module 01 remains a complete fifteen-minute standalone primer
- Foundation, Practitioner, and Leader instructional views
- Original diagrams, utility simulations, process frameworks, frequent checks, module-specific
  frequently asked questions, and saved work products
- Responsive on computer, tablet, and phone

## Mastery standard

Given one bounded utility question, a learner demonstrates mastery by identifying the important
entities and relationships, distinguishing asserted from inferred or validated statements, tracing
an answer to evidence, choosing an appropriate semantic access pattern, defining the context and
controls required before an application or agent may use or act on the result, and defending a
reviewable Utility Knowledge Spine Pilot Canvas.

# Part I: See the relationships

## Module 01: RDF in 15 Minutes

Begin with three simple questions from water, wastewater, and stormwater. Build one
subject-predicate-object statement, connect several statements, and reveal the graph.

Simulation: triple builder and one relationship-path query.

Work product: relationship card.

FAQ focus: Is RDF a database? Is an RDF graph the same as a diagram? Why not use a spreadsheet?

## Module 02: The Anatomy of a Triple

Distinguish resources from literal values, identifiers from labels, and direction from visual
proximity. Translate ordinary utility statements into readable Turtle.

Core concepts: subject, predicate, object, Internationalized Resource Identifier, literal, datatype,
language tag, blank node, direction, serialization, RDF dataset, and named graph.

Simulation: repair reversed, ambiguous, overloaded, and free-text triples.

Work product: reviewed ten-triple deck.

FAQ focus: Can the object be a number? Can a triple have more than three parts? Why are identifiers
long?

## Module 03: Which Pump Do You Mean?

Follow Pump P-104 through SCADA, GIS, CMMS or EAM, drawings, work orders, and staff language.
Matching labels are treated as candidates, not proof of identity.

Simulation: accept, reject, or escalate identity matches, then observe how one wrong equivalence
changes downstream answers.

Work product: identity crosswalk and conflict queue.

FAQ focus: Why not use the asset tag? What if systems disagree? Who approves the canonical identity?

## Module 04: From Triples to a Utility Knowledge Graph

Connect assets, locations, observations, work, people, procedures, permits, customers, and risks.
Separate the machine-readable graph from its node-link visualization.

Simulation: grow a thirty-triple graph from source records and answer three cross-domain questions.

Work product: utility mini-graph with named source groups.

FAQ focus: Does every relationship belong in one graph? Is a graph database automatically a
knowledge graph? How large can a graph become?

# Part II: Build shared meaning

## Module 05: Data Model, Taxonomy, Ontology, Semantic Layer, and AI Context

Use one customer-exposure scenario to separate five terms:

| Concept | Question it answers | Utility example |
| --- | --- | --- |
| Data model | How is information structured for this system or use? | customer, service account, premise, fields, keys, and cardinalities |
| Taxonomy | How are terms classified or arranged? | customer classes and service categories |
| Ontology | What do the concepts and relationships mean across systems? | customer, served location, active service agreement, exposure, and affected zone |
| Semantic layer | How does shared meaning connect to actual enterprise data and metrics? | map `ActiveCustomer` to approved CIS fields, GIS relationships, and calculation rules |
| AI context | What does the model or agent need for this task now? | customer, date, jurisdiction, evidence, policy, permissions, workflow state, and output limits |

Teach that a context engine assembles context. It is not the context itself.

Simulation: sort 25 artifacts into the five concepts, then repair a mixed architecture.

Work product: Five-Layer Meaning Map.

FAQ focus: Is a semantic layer an ontology? Is a prompt AI context? Is a taxonomy enough?

## Module 06: Taxonomies, Vocabularies, and RDFS

Start with terms utility staff already classify: pump types, inspection types, overflow categories,
customer classes, and permit conditions. Move from lists and hierarchies into shared classes and
properties.

Core concepts: controlled vocabulary, taxonomy, class, instance, property, subclass, subproperty,
domain, range, label, definition, and RDF Schema.

Simulation: reconcile four competing meanings of “asset,” then test the effect of a bad hierarchy.

Work product: governed vocabulary and taxonomy sheet.

FAQ focus: Can one thing belong to several classes? Who owns definitions? Does RDFS validate data?

## Module 07: Ontology Engineering in Plain Language

Turn competency questions into an ontology. Discover terms, define boundaries, identify
relationships, choose identifiers, formalize selected semantics, test against examples, review with
domain experts, version, and release.

Teach upper ontology, domain ontology, application profile, modularity, reuse, alignment, and change
control without requiring philosophy or advanced logic.

Simulation: conduct a utility modeling session for “active customer exposed to a pressure event.”

Work product: ontology decision record with competency questions and excluded meanings.

FAQ focus: Can an ontology be wrong? How much should we model? Should we reuse an industry ontology?

## Module 08: Ask the Graph with SPARQL

Pronounce SPARQL as “sparkle” once. Connect each query clause to a visible graph pattern. Begin with
`SELECT`, variables, and triple patterns, then add filters, optional information, federation, and
paths only when the question requires them.

Simulation: assemble queries for affected customers, upstream wastewater assets, and overdue outfall
inspections.

Work product: question-to-query sheet with expected evidence.

FAQ focus: Is SPARQL harder than SQL? Does SPARQL infer facts? Can it query data that stays in another
system?

# Part III: Trust the graph

## Module 09: Reasoning and Inference with OWL

Distinguish explicit assertions from conclusions derived under declared logic. Teach inverse,
transitive, equivalent, and class-membership examples with visible proof traces.

Teach the open-world principle: missing information normally means unknown, not false.

Simulation: reveal the exact assertions and axiom behind every inference, then reject an unsupported
leap.

Work product: inference boundary card.

FAQ focus: Is inference prediction? Does the graph invent facts? When should a utility avoid an
equivalence assertion?

## Module 10: Validation with SHACL

Pronounce SHACL as “shackle” once. Treat a shape as a declared structural contract and separate
conformance from truth, quality, safety, and completeness.

Simulation: validate Pump, Sample, Work Order, Customer Exposure, and Outfall records. Correct
missing identifiers, units, dates, roles, and controlled values.

Work product: utility SHACL contract and remediation route.

FAQ focus: Why can valid data still be wrong? Is SHACL a database constraint? Who handles a warning
versus a violation?

## Module 11: References, Provenance, Authority, and Time

Model observed, recorded, asserted, extracted, inferred, generated, reviewed, and approved
statements. Attach source, responsible role, confidence, observation time, record time, effective
time, version, supersession, and access boundary.

Simulation: reconcile a SCADA observation, CMMS record, approved engineering rule, retired
procedure, extracted contract clause, and language-model summary.

Work product: authority, provenance, and time ledger.

FAQ focus: Is source the same as authority? Can two conflicting statements both be preserved? What
does the agent use when a rule has been superseded?

# Part IV: Operate the Knowledge Spine

## Module 12: From an Ontology File to a Running Knowledge Spine

Show why an ontology in a presentation or modeling file does not change runtime behavior. Build a
vendor-agnostic operating architecture:

1. Ontology and Governance Core: shared model, shapes, rules, policy links, ownership, versions, and
   releases.
2. Semantic Platform: instantiated graph, query, reasoning, validation, security, and observability.
3. Connection Fabric: mappings, federation, extraction, indexing, APIs, and selected materialization.
4. Consumption Plane: BI, applications, agents, data stewards, and governed feedback.

Simulation: move a customer-exposure concept from paper definition to queryable operational
knowledge.

Work product: Utility Knowledge Spine Architecture.

FAQ focus: Is the spine one product? Where does the ontology run? Does all source data become RDF?

## Module 13: Map Meaning to Data

Connect ontology concepts and properties to fields, tables, APIs, event streams, graph nodes, and
document extractions. Explain mapping, transformation, direct mapping, R2RML, source pushdown, and
semantic contracts.

Simulation: map `ActiveCustomer`, `servedBy`, `affectedBy`, and `effectivePolicy` across CIS, GIS,
SCADA, and policy records. Break one mapping and observe the wrong answer.

Work product: semantic mapping record with owner, source, transformation, validation, and test query.

FAQ focus: Is mapping the same as copying? What happens when a column changes? Where do mapping rules
live?

## Module 14: Virtualize, Cache, Index, or Materialize?

Teach a move-less-data-first decision, not a no-copy promise. Compare query-in-place, federated
query, cache, search index, extracted entity store, materialized graph, and replicated analytical
table.

Decision factors: source authority, query capability, latency, freshness, availability, cost,
security, workload volume, transformation need, and recovery.

Simulation: choose an access pattern for telemetry, customer records, work history, permits,
procedures, and hot emergency-response paths. Change latency and freshness requirements and watch
the answer change.

Work product: Virtualize-or-Materialize Decision Record.

FAQ focus: Is duplication always bad? What if the source is unavailable? Do embeddings count as a
copy?

## Module 15: Structured and Unstructured Knowledge

Connect rows, time series, spatial features, documents, emails, calls, images, contracts, reports,
and procedures. Separate metadata, keyword search, vector similarity, entity extraction, explicit
graph statements, and approved knowledge.

Simulation: ask one overflow-response question. Compare document search, vector retrieval, extracted
entities, graph connections, and hybrid retrieval. Reveal what each method preserves and loses.

Work product: Structured-Unstructured Evidence Plan.

FAQ focus: Does an embedding contain meaning? Should every sentence become a triple? How are document
passages connected to graph claims?

## Module 16: Context Engines and Runtime AI Context

Use this operating relationship:

```text
data models + ontology + semantic layer + policies + runtime state
-> context engine
-> task-specific AI context
-> model or agent
```

The context package may contain instructions, user intent, identified entities, retrieved evidence,
definitions, current policy, jurisdiction, time, permissions, workflow state, tool boundaries,
output schema, and unresolved conflicts.

Simulation: assemble context for a customer-exposure decision. Omit one item at a time and show the
resulting ambiguity, denial, stale answer, or unsafe action proposal.

Work product: AI Context Contract with required, optional, prohibited, and freshness-controlled
elements.

FAQ focus: Is a long prompt good context? Does the context window store knowledge? Can good context
make a generative model deterministic?

# Part V: Apply the backbone

## Module 17: BI, RAG, Graph Retrieval, and Context Engines

Ask the same Pump P-104 question through joined tables and Power BI, document RAG, RDF graph
retrieval, and a context engine.

Identify what may remain fixed and what may vary: source snapshot, mapping, query, graph, inference
regime, validation shapes, retrieval, ranking, context assembly, prompt, model, decoding, tools, and
external state.

Carry the result through identify, query, retrieve, infer, validate, assemble context, and explain.

Simulation: rerun four answer paths and diagnose whether a changed source, mapping, query, retrieval,
context, generation setting, or external state changed the evidence or wording.

Work product: Answer Repeatability Map.

FAQ focus: Does the graph replace RAG? Why can wording vary when evidence does not? What must be
recorded for a defensible rerun?

## Module 18: Graph-Grounded Agentic Applications

Begin after the system has produced a grounded proposal. Carry it through evidence fitness,
validation, authentication, authorization, approval, execution, verification, and recording.

Separate two independent questions: Is the proposal grounded well enough to consider, and may this
actor perform this action now? Treat ACT, ASK, REFRESH, CLARIFY, and STOP as explicit controlled
states.

Simulation: govern five wastewater work-order cases, then recover tool timeouts and uncertain
external state without creating duplicate side effects.

Work product: Agent Action Contract.

FAQ focus: Can a correct answer authorize action? What is idempotency? When should an agent stop?
Who owns correction when an agent acts incorrectly?

## Module 19: Design the One Water Knowledge Spine

Choose a bounded operational question, not “build the enterprise graph.” Identify concepts,
identities, sources, documents, mappings, graph patterns, validation shapes, inference boundaries,
provenance, context requirements, access, ownership, metrics, integration points, and agent controls.

Apply the Graph Fit Test:

- Do the same entities cross several systems?
- Are relationships central to the question?
- Must meaning be reused across applications?
- Do provenance, distributed ownership, or inference matter?
- Can the organization govern identifiers, definitions, mappings, and change?
- Is the expected operational value worth the added layer?

Capstone: One Water Knowledge Spine Pilot Canvas and decision briefing.

FAQ focus: Where should a utility start? How much graph is enough? What should the first 90 days
produce? When should the team stop?

## Module 20: One Water Knowledge Spine Lab

Operate a full-screen HTML laboratory that carries one realistic utility question through identity,
triples, graph construction, SPARQL traversal, SHACL validation, inference boundaries, governed
evidence, runtime context, authorization, simulated action, verification, and audit.

Begin with the Lift Station LS-7 and Overflow Event 21 wastewater scenario. Then switch to water,
stormwater, or a guided learner-supplied use case. Build the pattern, introduce realistic failures,
repair them, replay the result, and export a portable use-case configuration.

Simulation: the entire module is a build, run, break, repair, and adapt laboratory.

Work product: Portable One Water Knowledge Spine Use-Case Configuration contained within the HTML
experience.

FAQ focus: Is this connected to real utility systems? What parts can be reused? Why can a correct
query still lead to a stopped action? How do we adapt the pattern safely?

## Completion rule

```text
20 module checks passed
+ required Utility Semantic Starter Pack artifacts saved
+ final transfer scenario passed
+ One Water Knowledge Spine Pilot Canvas submitted
+ Portable One Water Knowledge Spine Use-Case Configuration completed
= course complete
```

## Approval note

The twenty-module curriculum and lesson contracts are approved for design. Existing live-review
modules remain governed by their recorded release states. Graph publication,
credential claims, and final release remain behind their separate approval gates.
