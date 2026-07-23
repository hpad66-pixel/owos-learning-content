# Instructional Views

## Principle

The course does not split learners into “people who can understand this” and “people who cannot.”
Every learner receives the same core model. Views change vocabulary density, implementation depth,
and decision emphasis.

## View comparison

| View | Primary need | What the learner sees first | Optional depth | Required exit capability |
| --- | --- | --- | --- | --- |
| Foundation | Understand the idea without technical prerequisites | plain sentence, labeled visual, utility example, pronunciation | readable Turtle or query reveal | explain the concept accurately in ordinary language |
| Practitioner | Build, connect, test, or govern the model | identifiers, triples, query, rule, shape, data lineage | profiles, syntax, implementation notes | produce and inspect a small technical artifact |
| Leader | Decide value, ownership, risk, and sequencing | operational question, consequence, evidence path, control point | architecture and investment detail | make a bounded pilot or governance decision |

## Example: RDF

- Foundation: “RDF represents information as small statements. Each statement names one thing, one
  relationship, and the thing or value on the other side.”
- Practitioner: inspect IRIs, literals, datatypes, Turtle, graph boundaries, and source mappings.
- Leader: decide which relationships must be reusable across applications and who owns their
  meaning.

## Example: SPARQL

- Foundation: “SPARQL, pronounced ‘sparkle,’ asks for patterns of relationships.”
- Practitioner: assemble `PREFIX`, `SELECT`, `WHERE`, triple patterns, filters, optional patterns,
  and property paths.
- Leader: compare a governed competency question with the current manual evidence path.

## Example: OWL

- Foundation: “OWL lets software derive a new statement when declared logic and existing statements
  support it.”
- Practitioner: inspect axioms, entailment traces, profile choices, consistency, and reasoner
  configuration.
- Leader: approve which inferences may affect decisions and which require human review.

## Example: SHACL

- Foundation: “SHACL, pronounced ‘shackle,’ checks whether graph data meets declared structural
  rules.”
- Practitioner: author targets, property shapes, cardinalities, datatypes, controlled values,
  severities, and validation reports.
- Leader: distinguish validation from truth and assign owners for violations and exceptions.

## Example: provenance and authority

- Foundation: “The graph should show who or what supplied a statement and when it applied.”
- Practitioner: model source records, named graphs, PROV-O relationships, effective time, record
  time, version, and supersession.
- Leader: set authority levels and determine which sources can support which decisions.

## Example: data model, ontology, semantic layer, and AI context

- Foundation: use four labeled cards. Structure tells a system where information goes. Ontology
  defines shared meaning. The semantic layer connects that meaning to actual records. AI context
  carries what the model needs for this task.
- Practitioner: inspect schemas, identifiers, mappings, query services, source policies, retrieval,
  context contracts, and logs.
- Leader: decide which meanings must be shared, which source is authoritative, what may be
  virtualized or materialized, and what the agent may know or do.

## Example: Knowledge Spine

- Foundation: follow one customer-exposure question from data sources through shared meaning into a
  task-specific evidence packet.
- Practitioner: inspect ontology releases, mappings, graph services, federation, extraction,
  validation, reasoning, access, and observability.
- Leader: assign ownership, choose the pilot boundary, approve the data-placement decision, and set
  measurable operational outcomes.

## View-switch behavior

- Preserve learner progress and simulation state.
- Keep the same utility question visible across views.
- Never remove provenance, uncertainty, permission, or safety warnings.
- Define a term before using its acronym in Foundation view.
- Offer pronunciation once, then use the formal spelling.
- Use expandable code, never code-only explanation.
- Provide a “show me the evidence” control in all views.

## Accessibility and device behavior

- Every graph has an equivalent ordered relationship-path list.
- Color never carries status by itself.
- Animation has pause, replay, step, and reduced-motion behavior.
- Phone layouts replace pan-and-zoom dependency with focus cards and next-relationship controls.
- Keyboard and touch interactions have the same outcomes.
- Screen-reader text states whether a statement is asserted, inferred, invalid, approved, or
  generated.
