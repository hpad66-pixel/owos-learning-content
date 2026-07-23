# Hardeep's Direction

Use this file for approved course intent, utility examples, personal positions, stories, teaching instructions, and questions requiring further research.

Nothing in this file becomes public or enters the shared graph without explicit approval.

## Direction captured 2026-07-22

Hardeep's starting reframe is that the smallest unit of machine-readable understanding is one
semantic relationship: how A relates to B.

The course should address the architecture problem exposed when an artificial intelligence
initiative reaches an established data estate and the organization discovers that access to data
does not mean the machine understands identity, relationships, rules, or provenance.

Teach RDF as part of the answer. Build from triples into the surrounding standards stack, semantic
governance, a knowledge graph layer above the lakehouse, and metadata that carries lineage alongside
meaning.

The course should help platform teams focus on the feed into artificial intelligence and decide
whether semantic requirements have been designed into the platform.

The complete original wording is preserved in
`conversations/2026-07-22-semantic-data-architecture-course-direction.md`.

## Direction captured 2026-07-22: course shape

This is a fifteen-minute standalone course for leaders. It will connect to the existing `Data Before
AI` course later.

The lesson should create a moment of recognition by asking simple relationship questions in water,
wastewater, and stormwater. It should make the learner see that connected meaning can be broken into
subject, predicate, and object, then built back into a graph.

The learner should encounter many everyday and utility examples until the triple becomes natural.
The visual experience should grow from one triple to a graph, then through RDF, RDFS, SPARQL, OWL,
and SHACL. Animations must work on computer, tablet, and phone and show how references, semantics,
queries, inferences, and validation differ.

The learner must leave understanding:

- the three parts of a triple;
- why shared triples form a graph;
- the different jobs of RDF, RDFS, SPARQL, OWL, and SHACL; and
- how the same relationship pattern appears in real life, water, wastewater, and stormwater.

The complete original wording is preserved in
`conversations/2026-07-22-fifteen-minute-rdf-course-direction.md`.

## Direction captured 2026-07-23: BI, RAG, graphs, and agents

Compare familiar table joins, Power BI, anomaly detection, and reporting with RAG, explicit
semantics, graph reasoning, and agentic applications.

Use a clear comparison table and small simulations. Ask the same question against the same fictional
utility data, show several RAG responses, explain why retrieved evidence and generated wording can
change, and contrast that with a stable RDF evidence path.

Build a small real graph from subject, predicate, and object triples. Use many utility examples and
show how enterprise knowledge, individual expert knowledge, organizational responsibility,
procedures, provenance, and physical assets can connect without pretending that every captured
statement has equal authority.

Carry the graph into an agentic application. Show query, inference, validation, explanation,
proposed action, human approval, execution or stop, and provenance writeback.

The complete original wording and the technical interpretation boundary are preserved in
`conversations/2026-07-23-bi-rag-graph-and-agentic-comparison-direction.md`.

## Direction captured 2026-07-23: comprehensive foundation

Expand the short primer into a substantial foundational course because semantic meaning is the
backbone for the larger data and artificial intelligence curriculum.

The course must work for technical and nontechnical utility staff. It must define and pronounce the
important terms, including RDF, SPARQL as “sparkle,” and SHACL as “shackle,” while preserving the
formal spelling. It must provide a glossary, instructional views, extensive practical examples, and
enough repetition for learners to internalize triples and the different jobs in the standards
stack.

Bring in identity collisions, authority, provenance, time and version, the distinction between
unknown and false, cases where RDF is not the right solution, measurable operational value, and a
substantial Utility Semantic Starter Pack.

The complete original wording is preserved in
`conversations/2026-07-23-expand-to-comprehensive-semantic-backbone-course.md`.

## Direction captured 2026-07-23: Knowledge Spine and AI context

Teach the difference among a data model, ontology, semantic layer, artificial intelligence context,
and context engine. Use the relationship:

```text
data models + ontology + semantic layer + policies + runtime state
-> context engine
-> task-specific AI context
-> model or agent
```

Show why an ontology that exists only in a presentation, glossary, or modeling tool does not change
runtime behavior. Teach the “Knowledge Spine” as an operational pattern in which shared meaning is
instantiated, queryable, governed, versioned, and connected to authoritative data.

Teach a move-less-data-first architecture without turning it into dogma. Virtualize when governed
query-in-place is suitable. Materialize when latency, availability, transformation, cost, or workload
requirements justify it. Treat Stardog and Databricks as one illustrative combination, not the
architecture itself.

Connect structured data, unstructured documents, extracted entities, vector retrieval, explicit
relationships, provenance, policy, runtime state, and agent permissions. Build original
utility-specific diagrams, simulations, methods, quizzes, work products, and module-specific
frequently asked questions.

The complete direction and supplied-diagram inventory are preserved in
`conversations/2026-07-23-knowledge-spine-ai-context-master-class-direction.md`.
