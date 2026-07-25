# Module 08 Design Brief: Ask the Graph with SPARQL

Status: approved for production under standing owner authorization

## Learning decision

The learner must translate one utility question into a readable SPARQL graph pattern, run it, and
trace returned bindings to visible source statements.

## Experience architecture

This is a query laboratory. A dashboard can display source records but cannot follow the changing
relationship path behind an affected-customer question. The learner places a query stencil over the
graph, assembles clauses in order, observes variable bindings, changes one filter, and defends the
evidence behind a result row.

## Visual Arsenal selection

| Idea | Shape | Visual | Conclusion |
| --- | --- | --- | --- |
| Dashboard and graph question differ | split console | Dashboard dead-end | A relationship question needs a graph pattern |
| Variables match unknown nodes | stencil | Variable stencil | Variables are placeholders bound by matching statements |
| Clauses reveal paths | synchronized overlay | Query-to-path overlay | Query text and graph edges express the same pattern |
| Results need evidence | lineage table | Binding provenance table | A result row is defensible when its statements are traceable |

## Signature mechanism

The SPARQL Query Laboratory assembles SELECT, WHERE triple patterns, FILTER, OPTIONAL, and LIMIT in
order. Each clause states what becomes visible in the graph and result set.

## Work product

The Question-to-Query Sheet records the question, variables, graph pattern, filter, optional data,
expected bindings, evidence path, source groups, and limitations.

## Evidence boundary

SPARQL queries RDF graph patterns. It is not OWL reasoning or SHACL validation. Federation is
possible through configured endpoints and permissions, not automatic access to every source.
