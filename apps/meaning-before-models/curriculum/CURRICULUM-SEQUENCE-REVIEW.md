# Meaning Before Models Curriculum Sequence Review

Status: Step 2 approved by Hardeep Anand
Date: 2026-07-24

## Sequence test

Every proposed module was tested against five questions:

1. Does it contribute directly to the approved graduation capability?
2. Is its prerequisite taught before the learner needs it?
3. Does it perform one clear learning job rather than several unrelated jobs?
4. Does it contribute evidence to the final Utility Knowledge Spine Pilot Canvas?
5. Is its common route understandable without programming or platform configuration?

## Recommended intellectual sequence

```text
recognize one relationship
-> construct a precise statement
-> establish identity
-> connect statements into answerable paths
-> distinguish the layers of enterprise meaning
-> govern vocabulary and ontology
-> query, infer, validate, and trace authority
-> instantiate and connect a running Knowledge Spine
-> combine structured and unstructured evidence
-> assemble task-specific context
-> compare answer-producing architectures
-> control agent action
-> design and defend a bounded pilot
```

## Module-by-module decision

| Proposed module | Learning job on the common route | Practitioner depth | Prerequisite | Curriculum decision |
| --- | --- | --- | --- | --- |
| 01. RDF in 15 Minutes | Recognize that machine-readable meaning begins with explicit, directed relationships | Inspect the generated triples | none | Retain as orientation and standalone primer. It previews later jobs but does not establish mastery. |
| 02. The Anatomy of a Triple | Construct precise subjects, predicates, objects, identifiers, and literal values | Read and edit small Turtle examples | Module 01 | Retain. This is the formal statement foundation. |
| 03. Which Pump Do You Mean? | Decide when records do or do not identify the same real utility thing | Identity matching evidence and canonical identifier controls | Module 02 | Retain. Shared identity must precede graph connection. |
| 04. From Triples to a Utility Knowledge Graph | Connect statements and trace an answerable relationship path | Named graphs and source grouping | Modules 02 and 03 | Retain. This completes the first usable graph mental model. |
| 05. Five Layers of Meaning | Distinguish data model, taxonomy, ontology, semantic layer, and runtime artificial-intelligence context | Map each layer to enterprise artifacts | Module 04 | Retain and narrow. It is a comparison and architecture-orientation lesson, not the ontology or context mastery lesson. |
| 06. Taxonomies, Vocabularies, and RDF Schema | Govern terms, classes, properties, and hierarchies without confusing description with validation | Domain, range, subclass, and subproperty behavior | Modules 04 and 05 | Retain. It supplies vocabulary and schema concepts needed by ontology work. |
| 07. Ontology Engineering in Plain Language | Turn bounded competency questions into shared concepts, relationships, and decisions | Modularity, reuse, alignment, versioning, and selected formal semantics | Module 06 | Retain. Keep production ontology engineering optional. |
| 08. Ask the Graph with SPARQL | Translate a utility question into a readable graph pattern and interpret the returned evidence | Filters, optional patterns, federation, and paths | Modules 04, 06, and 07 | Retain. Query construction is required for evidence tracing. |
| 09. Reasoning and Inference with OWL | Separate explicit assertions from conclusions derived under declared logic | Selected axiom types and visible proof traces | Modules 06 through 08 | Retain. Keep advanced profiles and reasoner configuration optional. |
| 10. Validation with SHACL | Test declared graph constraints and repair nonconforming data without equating conformance with truth | Shape design, severity, and remediation routing | Modules 06 through 08 | Retain. Validation is a separate job from inference. |
| 11. References, Provenance, Authority, and Time | Decide which statement may support a decision, who asserted it, and when it applies | PROV-O mappings, versions, supersession, and access boundaries | Modules 04, 09, and 10 | Retain. This closes the trust foundation. |
| 12. From an Ontology File to a Running Knowledge Spine | Explain how governed meaning becomes queryable and connected to runtime systems | Semantic-platform services and operating model | Modules 05 through 11 | Retain. This is the architecture transition from representation to operation. |
| 13. Map Meaning to Data | Connect approved concepts to fields, tables, application programming interfaces, events, and graph statements | Relational-to-RDF mapping, pushdown, tests, and change control | Module 12 | Retain. Mapping must precede access-pattern decisions. |
| 14. Virtualize, Cache, Index, or Materialize? | Choose how an application reaches governed data under latency, freshness, authority, availability, security, and cost constraints | Federation, caching, indexing, and materialization implementation considerations | Modules 12 and 13 | Retain. This establishes a decision method rather than a no-copy slogan. |
| 15. Structured and Unstructured Knowledge | Distinguish retrieval, similarity, extraction, explicit graph assertion, review, and approved knowledge | Hybrid retrieval and document-to-claim provenance | Modules 11 through 14 | Retain. Keep this focused on evidence state, not application comparison. |
| 16. Context Engines and Runtime AI Context | Assemble the task-specific evidence, definitions, policy, time, permissions, and workflow state needed now | Context retrieval, filtering, validation, freshness, and output contracts | Modules 11 through 15 | Retain. This completes the transition from stored knowledge to task use. |
| 17. BI, RAG, Graph Retrieval, and Context Engines | Compare how the same utility question is answered, what remains fixed, what may vary, and how evidence is traced | Pipeline configuration, evaluation, and repeatability controls | Modules 08 and 12 through 16 | Retain but remove agent authorization and action from this module. |
| 18. Graph-Grounded Agentic Applications | Carry a grounded answer through propose, validate, authorize, act or stop, and record | Tool contracts, policy enforcement, human approval, idempotency, and audit | Modules 11, 16, and 17 | Create by splitting the second learning job out of the current Module 17. |
| 19. Design the One Water Knowledge Spine | Scope, design, measure, and defend one bounded semantic-backbone pilot | Technical implementation roadmap and review panel | Modules 01 through 18 | Retain the current capstone as Module 19. |

## Why the proposed sequence grows from eighteen to nineteen modules

The current Module 17 performs two different professional jobs:

1. compare how Business Intelligence, Retrieval-Augmented Generation, graph retrieval, and context
   assembly produce answers; and
2. govern whether an agent may act.

Answer production and action authorization are related, but they are not the same decision. Keeping
them together produces two mental models, two signature mechanisms, two work products, and too much
responsibility in one lesson. Splitting them gives the learner a clear boundary:

```text
a well-supported answer
does not automatically create
permission to act
```

## Depth rule for all modules

Every module will use:

- one common route that satisfies the approved nontechnical graduation capability;
- optional Practitioner depth for syntax, standards detail, mappings, configuration, or
  implementation; and
- Leader decisions only where ownership, investment, risk, authority, or approval changes.

The three views share one truth and one evidence boundary. They do not become three separate lessons.

## Step 2 approval

Hardeep Anand approved the nineteen-module sequence and the split of the current Module 17 on
2026-07-24. Lesson contracts and the revised golden lesson remain behind later approval gates.
