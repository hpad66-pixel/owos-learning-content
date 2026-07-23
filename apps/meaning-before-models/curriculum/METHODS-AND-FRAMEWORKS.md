# Methods and Frameworks

## 1. Five-Layer Meaning Test

Use this test whenever a team uses several semantic terms as if they were interchangeable.

| Layer | Governing question | Typical artifact | Failure when missing |
| --- | --- | --- | --- |
| Data model | How is information structured for this use? | schema, entity relationship model, API contract | fields and joins are unclear |
| Taxonomy | How are terms grouped or classified? | controlled list or hierarchy | inconsistent categories |
| Ontology | What do the concepts and relationships mean? | classes, properties, axioms, definitions | systems use the same words differently |
| Semantic layer | How does shared meaning resolve to enterprise data? | mappings, metrics, query services, source policies | definitions remain disconnected from records |
| AI context | What must the model or agent know and obey now? | task-specific evidence and control package | ambiguous, stale, unauthorized, or unsupported output |

Method:

1. Name the operational question.
2. Put each existing artifact into one layer.
3. Mark artifacts that claim to do several jobs.
4. Identify the missing handoff between layers.
5. Test one real utility question from source to runtime answer.

## 2. Ontology-to-Operations Lifecycle

```text
discover
-> define
-> formalize
-> instantiate
-> map
-> validate
-> query
-> observe use
-> correct
-> version and release
```

The lifecycle closes the gap between a modeling workshop and a running capability.

1. Discover language from staff, systems, standards, records, and decisions.
2. Define concepts, relationships, boundaries, synonyms, and exclusions.
3. Formalize only the semantics needed for the competency questions.
4. Instantiate representative assets, people, events, policies, and evidence.
5. Map source fields, APIs, streams, and extractions to the shared model.
6. Validate declared structural contracts.
7. Query the graph against expected results.
8. Observe usage, failures, corrections, and unanswered questions.
9. Route corrections through accountable stewards and domain owners.
10. Version and release the ontology, mappings, shapes, and dependent tests together.

## 3. Knowledge Spine Operating Model

| Layer | Owns | Does not own by itself |
| --- | --- | --- |
| Ontology and Governance Core | definitions, classes, properties, shapes, selected axioms, policy links, ownership, versions | operational source records |
| Semantic Platform | graph storage or virtual views, query, reasoning, validation, security, observability | every source system's business process |
| Connection Fabric | mappings, federation, extraction, indexes, APIs, synchronization, selected materialization | final meaning without the core model |
| Consumption Plane | BI, applications, agents, search, stewardship workflows | authority to redefine enterprise meaning silently |

The feedback loop is part of the operating model. Queries, failures, corrections, and new use cases
become governed change requests, not invisible model drift.

## 4. Virtualize-or-Materialize Decision Gate

Score each factor for the intended workload. The result is a review prompt, not an automatic
architecture decision.

| Factor | Virtual access is favored when | Materialization is favored when |
| --- | --- | --- |
| Freshness | source must be current at query time | a controlled snapshot is acceptable |
| Latency | source can meet the response target | repeated remote queries miss the target |
| Availability | source availability is sufficient | service must continue during source outage |
| Volume | queries are selective | workloads repeatedly scan large remote sets |
| Transformation | mapping is light | expensive transformation must be reused |
| Security | governed remote access is permitted | isolation or approved derived data is required |
| Cost | remote compute and network cost are acceptable | repeated remote access costs more |
| Source capability | source supports pushdown and concurrency | source cannot support the workload |
| Audit | source-time results are reproducible | a retained evidence snapshot is required |

Decision outcomes:

- virtual query;
- federated query;
- governed cache;
- search or vector index;
- extracted entity store;
- materialized RDF graph;
- replicated analytical table;
- hybrid pattern by question.

## 5. Structured-Unstructured Evidence Bridge

1. Preserve the original document, media item, or message.
2. Record identity, source, access, version, and effective time.
3. Segment or index the content for retrieval.
4. Extract candidate entities, relationships, events, and clauses.
5. Link each candidate to the exact source passage or region.
6. Map approved concepts to the ontology.
7. Validate required structure and controlled values.
8. Distinguish extracted, inferred, generated, reviewed, and approved statements.
9. Retain the passage for grounded explanation.
10. Route corrections back to the extraction, mapping, or ontology owner.

## 6. Context Assembly Method

The context engine performs a controlled assembly:

```text
understand request
-> resolve identity
-> determine task and jurisdiction
-> retrieve authorized evidence
-> apply semantic mappings
-> evaluate freshness and conflicts
-> include current policy and workflow state
-> apply permission and tool boundaries
-> validate the context contract
-> package for the model or agent
-> log what was supplied
```

Every context contract specifies:

- purpose and intended decision;
- required entities and identifiers;
- required evidence types;
- source authority;
- freshness and effective-time rules;
- definitions and ontology version;
- policy and jurisdiction;
- user and agent permissions;
- current workflow state;
- allowed tools and actions;
- unresolved conflicts and uncertainty;
- output schema and citation requirements;
- retention and audit behavior.

## 7. Knowledge Claim Lifecycle

```text
observed or received
-> recorded
-> extracted or mapped
-> asserted as candidate
-> validated structurally
-> reviewed for authority
-> approved for a purpose
-> used or inferred
-> monitored
-> corrected or superseded
```

No arrow is automatic. A valid extraction does not become approved enterprise knowledge without the
defined review.

## 8. Graph Fit Test

Use RDF or a knowledge graph when most answers are yes:

1. Do identified entities recur across several systems?
2. Are multi-step relationships central to the question?
3. Must shared meaning outlive one report or application?
4. Must statements retain provenance, authority, and time?
5. Will several teams own parts of the meaning?
6. Will graph-pattern query, inference, or shapes add real value?
7. Can the organization govern identities, definitions, mappings, and versions?
8. Is there a measurable operational question?

Prefer a simpler pattern when the need is local, stable, shallow, and already answered well by a
table, GIS query, time-series store, document search, API, or existing semantic model.
