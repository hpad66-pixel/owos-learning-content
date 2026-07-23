# Plain-Language Glossary

Each entry includes the shortest useful definition, a utility example, and a boundary that prevents
a common misunderstanding.

## Core RDF terms

### RDF

Pronounced: “are-dee-eff.” Resource Description Framework is a W3C graph data model for representing
information as triples. Example: `Pump_P104 serves Pressure_Zone_3`. RDF is not a file format,
database product, or artificial intelligence model.

### Triple

One RDF statement made of subject, predicate, and object. Example:
`Pump_P104 hasStatus Available`. A row with three cells is not automatically an RDF triple. RDF
terms have defined roles and identifiers.

### Subject

The resource the statement is about. In `Pump_P104 serves Pressure_Zone_3`, `Pump_P104` is the
subject.

### Predicate

The named relationship from subject to object. In `Pump_P104 serves Pressure_Zone_3`, `serves` is
the predicate. Direction matters.

### Object

The resource or literal value on the other side of the relationship. In
`Pump_P104 serves Pressure_Zone_3`, the pressure zone is the object.

### RDF graph

A set of RDF triples. Shared subjects and objects connect statements into a directed, labeled graph.
The diagram is a view of the graph, not the graph's only form.

### Resource

Something that can be identified and described, such as a pump, location, procedure, role, event, or
concept.

### IRI

Pronounced by its letters. An Internationalized Resource Identifier gives a resource or property a
globally usable name. A short label such as `P-104` may be displayed to people while the IRI keeps
the machine identity unambiguous.

### URI

Uniform Resource Identifier. URI is an older, familiar identifier term contained within the broader
IRI concept. A URL is one kind of URI. An RDF identifier does not have to open a web page.

### Literal

A value such as text, a number, a date, or a Boolean. Example:
`Observation_88 hasValue "7.2"^^xsd:decimal`. A literal is not used as the subject of an ordinary RDF
triple.

### Datatype

The declared kind of a literal value, such as decimal, integer, dateTime, or Boolean. The unit is a
separate concern and should not be guessed from the number.

### Language tag

A marker indicating the natural language of text, such as `@en` for English. It supports
multilingual labels and definitions.

### Blank node

An RDF node without a named IRI. It can be useful for local structures, but it is a poor choice when
an enterprise must identify and reconcile the same thing across systems.

### Turtle

Pronounced like the animal. A compact, human-readable syntax for writing RDF. Turtle is one way to
serialize RDF, not a different data model.

### JSON-LD

JSON for Linked Data. A JSON-based way to serialize linked data using shared context and
identifiers. JSON-LD is not the only way to represent RDF.

### Named graph

A set of triples given its own name so an application can discuss its source, scope, access, or
provenance. A named graph can help separate imported records, approved statements, and generated
material.

### Triplestore

A database designed to store and query RDF triples. RDF can also be processed without one
particular storage product.

## Graph and identity terms

### Node

A resource or literal shown as a point in a graph view. In RDF, subjects and resource objects appear
as nodes.

### Edge

A directed, labeled relationship between nodes. In RDF, the predicate supplies the edge label.

### Path

A sequence of connected relationships. Example:
`Pump_P104 serves Zone_3`, then `Zone_3 contains Account_882`.

### Knowledge graph

A graph-based knowledge representation that connects identified things, relationships, types, and
often provenance or rules. Not every graph database is automatically a governed knowledge graph.

### Semantic layer

A reusable layer that expresses shared meaning across source systems and applications. It
complements systems of record rather than automatically replacing them.

### Semantic mapping

A governed connection between a source field, table, API response, graph term, document extraction,
or metric and the corresponding concept or property in a shared model.

### Knowledge Spine

The course's name for an operational pattern that keeps shared meaning queryable, governed,
versioned, and connected to enterprise data. It includes more than an ontology file and should not
be treated as one mandatory vendor product.

### Ontology instantiation

The use of ontology classes and properties with actual or representative identified things and
statements. Defining `Pump` is modeling. Stating that Pump P-104 is a Pump and serves Zone 3 is
instantiation.

### Canonical identifier

The governed identifier used to refer to one thing across contexts. It may be mapped to several
source-system identifiers.

### Identity resolution

The process of deciding whether records refer to the same real or conceptual thing. Matching a
label is evidence, not proof.

### Crosswalk

A governed mapping between source-system identifiers and a canonical identity.

### Same-as assertion

A strong claim that two identifiers denote the same thing. Such claims require careful evidence,
because a wrong equivalence can spread errors across a graph.

## Shared meaning terms

### Data model

A description of how information is structured for a database, application, report, API, or
analytical use. It commonly defines entities, attributes, keys, relationships, cardinalities, and
constraints. A data model can carry meaning, but it is often bounded to a particular system or use.

### Vocabulary

A defined set of terms and relationships used by a community or system.

### Ontology

A formal model of concepts, relationships, and logical statements in a domain. In this course,
“shared meaning model” is used before “ontology” when plain language is clearer.

### Taxonomy

A controlled classification, usually arranged as categories and subcategories. A pump taxonomy may
classify booster, raw-water, and high-service pumps. A taxonomy is useful shared structure but
usually expresses less relationship and logic than an ontology.

### RDFS

Pronounced “are-dee-eff schema.” RDF Schema provides vocabulary for describing classes, properties,
subclasses, domains, ranges, labels, and related modeling concepts. It is not a form-validation
language.

### Class

A category of things, such as `Pump`, `PressureZone`, or `Inspection`.

### Instance

An individual member of a class, such as Pump P-104 as an instance of `Pump`.

### Property

A reusable relationship or attribute used in statements, such as `serves`, `locatedIn`, or
`hasStatus`.

### Subclass

A class whose members are also members of a broader class. Every `BoosterPump` may be a `Pump`, for
example.

### Domain

An RDFS statement indicating the class of resources that normally use a property as subject. It can
support inference and should not be casually mistaken for an input-screen restriction.

### Range

An RDFS statement indicating the class or datatype of values used as a property's object. Like
domain, it participates in semantics and is not the same as SHACL validation.

## Query terms

### SPARQL

Pronounced “sparkle.” SPARQL is the query language for RDF graphs. It asks for graph patterns, such
as a pump that serves a zone containing an affected customer. SPARQL does not itself guarantee
correct data or safe decisions.

### Graph pattern

A set of triple-shaped patterns containing variables. Matching the pattern binds variables to graph
terms.

### Variable

A placeholder in a query, often written with `?`, such as `?pump` or `?customer`.

### Competency question

A plain-language question the semantic model must be able to answer. It keeps modeling connected to
operational value.

### Property path

SPARQL syntax for matching a sequence or alternative of relationships. Property paths are useful
for traversal, but they do not add new facts to the graph.

## Reasoning terms

### OWL

Pronounced “owl.” Web Ontology Language expresses formal semantics that can support inference and
consistency checking. OWL does not mean that a machine understands like a person.

### Axiom

A formal statement used as part of an ontology's logic, such as an inverse relationship or class
restriction.

### Reasoner

Software that computes logical consequences under a declared semantics or checks aspects of
consistency.

### Inference

A conclusion derived from existing statements and declared rules or semantics.

### Entailment

The formal relationship in which a conclusion follows under a specified semantics.

### Asserted statement

A statement explicitly supplied to the graph rather than derived by a reasoner.

### Inferred statement

A statement derived from asserted statements under declared semantics. It should remain traceable to
its inputs and reasoning configuration.

### Open-world assumption

The principle that missing information does not normally make a statement false. If the graph does
not say Valve V-12 is open, its state may be unknown.

### Closed-world assumption

The assumption that what is not present may be treated as false or absent for a bounded application.
Some operational checks need this behavior, but it must be declared rather than smuggled into RDF
semantics.

### Unknown

A state in which the available evidence does not establish true or false. Unknown is often the
safest result for incomplete utility data.

### Consistency

Freedom from specified logical contradictions under a chosen semantics. Logical consistency does
not prove that every real-world statement is accurate.

## Validation terms

### SHACL

Pronounced “shackle.” Shapes Constraint Language describes and validates RDF graphs against declared
conditions. Passing SHACL does not prove a statement is true.

### Shape

An RDF description of constraints that selected graph nodes should satisfy.

### Data graph

The RDF graph being validated.

### Shapes graph

The RDF graph containing SHACL shapes and constraints.

### Target

The nodes to which a SHACL shape applies, such as every instance of `Pump`.

### Constraint

A declared condition, such as exactly one asset identifier or a required observation unit.

### Cardinality

A constraint on how many values a property may or must have.

### Validation report

The machine-readable result of SHACL validation, including conformance and any reported results.

### Conformance

The state in which the data graph satisfies the declared shapes for that validation run. Conformance
is narrower than truth, safety, quality, or completeness.

## Evidence, governance, and time

### Provenance

Information about where a statement or artifact came from, how it was produced, and who or what was
involved.

### Lineage

The path through sources and transformations that produced data or an output. Lineage is part of
provenance but does not by itself establish authority.

### PROV-O

Pronounced “prov-oh.” The W3C PROV Ontology provides RDF terms for provenance involving entities,
activities, and agents.

### Authority

The recognized right of a source, role, or process to make or approve a statement for a defined
purpose. Confidence and authority are not the same.

### Confidence

An assessment of certainty or match strength. A high-confidence assertion can still lack authority.

### Observation time

When a condition was observed.

### Record time

When a system stored or received the statement.

### Effective time

When a statement, procedure, rule, or status applies in the operational world.

### Version

A distinguishable state of a model, procedure, rule, dataset, or application.

### Supersedes

A relationship indicating that a newer statement or version replaces an older one for a defined
scope. The older item may remain important for history.

### Source system

The system from which a record was obtained. Source does not automatically mean authoritative for
every field or decision.

## Analytics and artificial intelligence

### AI context

The task-specific package supplied to a model or agent at runtime. It may include instructions,
intent, resolved entities, evidence, definitions, policy, jurisdiction, time, permissions, workflow
state, tool boundaries, uncertainty, and output constraints.

### Context engine

Software and control logic that retrieves, filters, validates, and assembles AI context. The engine
is the assembler. The context is the package it produces for a particular task.

### Context contract

A declared specification of what context must, may, and must not be supplied for a task, including
freshness, authority, permission, and output requirements.

### Context window

The bounded amount of input and prior generated content a language model can process in one run. A
context window is not an enterprise memory, ontology, or knowledge graph.

### BI

Business intelligence. BI tools model, aggregate, filter, calculate, and visualize data for
analysis. They can contain substantial semantics and should not be portrayed as “just charts.”

### Table join

An operation that combines rows using a relationship between fields. Joins are valuable and may be
the simplest correct solution.

### Anomaly detection

A method for identifying observations that differ from an expected pattern. An anomaly is a signal,
not automatically a fault, cause, or required action.

### RAG

Retrieval-augmented generation. A system retrieves external material and gives it to a generative
model as context. Output may vary with source content, retrieval, ranking, prompt, model, tools, and
generation settings.

### Embedding

A numeric representation used to compare similarity. Similarity can help retrieval, but it is not
the same as an explicit semantic relationship.

### Vector index

A structure used to retrieve items with similar embeddings. It complements rather than replaces
explicit identity, authority, and relationships.

### Entity extraction

The process of identifying candidate people, organizations, assets, places, events, clauses, or
other concepts in unstructured content. An extracted candidate is not automatically an approved
graph assertion.

### Deterministic

Producing the same result from the same defined inputs and configuration. Determinism is a property
of the complete pipeline and operating conditions.

### Probabilistic

Using probabilities or statistical estimates. Probabilistic does not mean random, incorrect, or
uncontrolled.

### Generated statement

Text or structured content produced by a model or software process. It is not automatically an
approved enterprise assertion.

### Grounding

Connecting an answer or action to selected evidence. Grounding can improve traceability but does not
guarantee that the evidence is correct, current, sufficient, or authorized.

## Connection and data-placement terms

### Federation

Querying or combining information across separately managed sources through governed connections.
Federation does not eliminate network, access, performance, availability, or consistency concerns.

### Virtual graph

A graph view produced from mappings over data held in another source, often at query time. A virtual
graph can expose relational or other data as RDF without first storing every resulting triple in the
graph platform.

### Query pushdown

Translating part of a query into the source system's native language so the source performs eligible
filtering, joins, or aggregation.

### Materialization

Storing a computed, mapped, indexed, or copied representation so it can be reused. Materialization
may improve latency and availability but creates freshness, governance, lineage, and lifecycle work.

### Cache

A temporary or managed copy used to reduce response time or source load. A cache still needs
freshness, invalidation, security, and audit rules.

### Search index

A structure built to retrieve content efficiently. Keyword and vector indexes serve different
retrieval patterns and are not substitutes for source authority or explicit graph meaning.

### Data in place

An access pattern in which authoritative source data remains in its existing managed system while
another service queries it through governed interfaces or mappings. Some metadata, indexes, caches,
or results may still be stored elsewhere.

### Agent

An application that can pursue a goal through models, tools, data, and control logic. The word does
not imply unrestricted autonomy.

### Tool

A capability an agent can call, such as a graph query, work-management API, notification service,
or hydraulic model.

### Human in the loop

A control in which a person reviews, approves, corrects, or stops part of a process. The role,
evidence, timing, and consequence of the review must be explicit.

## Common utility systems

### SCADA

Supervisory Control and Data Acquisition. SCADA monitors and controls operational processes. Access
to SCADA data does not imply permission to issue control commands.

### GIS

Geographic information system. GIS manages spatial features and relationships. Spatial topology can
be part of a semantic model without replacing GIS.

### CMMS or EAM

Computerized Maintenance Management System or Enterprise Asset Management system. These systems
manage assets, work, maintenance, materials, and related records.

### LIMS

Laboratory Information Management System. A LIMS manages samples, methods, results, quality control,
and laboratory workflows.
