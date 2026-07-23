# Hardeep Anand direction: Knowledge Spine and AI context master class

Captured: 2026-07-23

## Supplied teaching content

Hardeep supplied a detailed distinction among four terms:

> Data model: How is information structured?
>
> Ontology: What does the information mean?
>
> Semantic layer: How is meaning connected to enterprise data?
>
> AI context: What does the model need for this task?

He supplied this relationship:

> Data models + ontology + semantic layer + policies + runtime state -> context engine -> AI context
> -> model

He clarified that a context engine is not the context itself. It retrieves, filters, validates, and
assembles the task-specific package.

The supplied example concerned an artificial intelligence agent evaluating customer exposure. The
data model supplies structure. The ontology supplies meaning. The semantic layer connects meaning to
authoritative data. Runtime context supplies the customer, date, jurisdiction, policy, permissions,
workflow state, and permitted actions.

The source argues that an ontology cannot remain a diagram, glossary, presentation, or modeling file
that applications never query. It introduces “Knowledge Spine” as an operational pattern in which
the ontology is instantiated, queryable, versioned, governed, and connected to real data at query
time.

The illustrative architecture uses Stardog and Databricks. The ontology runs in a semantic platform,
structured data stays in the lakehouse, virtual graphs map it into the semantic model, and agents
query the connected layer. Hardeep explicitly directed the course to teach the architecture as
vendor-agnostic.

The source also argues for a move-less-data-first strategy:

- use knowledge graphs where relationships carry the value;
- virtualize before replicating;
- materialize hot paths when latency, availability, or cost justifies it;
- keep structured data governed where it lives when practical;
- index and retrieve unstructured material with suitable search methods;
- connect structured and unstructured evidence through shared meaning, identity, policy, and
  provenance.

## Direct course direction

Hardeep withdrew the original whole-course fifteen-minute boundary and confirmed this course as a
master class. He directed the course to connect all of the following in depth:

- ontology;
- taxonomy;
- data structure;
- structured and unstructured data;
- semantics;
- references;
- inference;
- knowledge graphs;
- semantic layers;
- artificial intelligence context;
- context engines;
- data federation and virtualization;
- materialization decisions;
- governed agentic applications; and
- the One Water Operating System knowledge-graph foundation.

The course must include extensive teaching graphics, simulations, methods, process frameworks,
quizzes, module-specific frequently asked questions, and practical utility examples.

## Supplied graphic

Attachment:
`codex-clipboard-51086484-b453-44f8-9ee9-8dbb2aeed6dc.png`

Observed dimensions: 1280 by 719 pixels.

SHA-256:
`f0bf46683c308afbf439db9ad9bf9def815b464c619d19f6f971be5f466a5bf5`

The visible diagram shows a Knowledge Spine between source systems and a consumption plane. The
spine contains an Ontology and Governance Core, Semantic Platform, and Connection Fabric. Source
categories include lakehouse or warehouse, domain knowledge graphs, and unstructured sources.
Consumers include business intelligence and analytics, applications, language models and agents,
and data stewards. The diagram states that meaning is resolved at query time with no data copied and
shows a stewardship feedback loop.

The graphic is treated as attributed research input. Ownership and reuse permission are not
established. Released OWOS artwork must be original unless permission is documented.
