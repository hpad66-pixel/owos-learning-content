# Module 14 Design Brief: Virtualize, Cache, Index, or Materialize?

Status: approved for production under standing owner authorization

## Learning decision

The learner must choose and defend an access pattern under explicit latency, freshness,
availability, authority, security, volume, transformation, recovery, and cost constraints.

## Experience architecture

This is a constraint stress test. An emergency wastewater question must be answered in two seconds
while one source is intermittently unavailable. The learner changes the workload constraints,
selects source-specific patterns, exposes every copy, and rehearses stale-data failure.

## Visual Arsenal selection

| Idea | Shape | Visual | Conclusion |
| --- | --- | --- | --- |
| Four patterns solve different problems | decision surface | Access-pattern field | No pattern wins universally |
| Copies exist in several forms | physical estate | Data-placement map | Cache and index are still governed copies |
| Constraint changes alter design | stress response | Scenario pivot board | Architecture follows measurable needs |
| Staleness travels to decisions | cause chain | Stale-copy propagation trace | Every copy needs freshness and fallback controls |

## Signature mechanisms

The Access-Pattern Stress Board selects virtualize, cache, index, materialize, or a governed hybrid
for five workloads. The Stale-Copy Failure Rehearsal identifies the earliest effective control when
freshness, availability, authority, or recovery breaks.

## Work product

The Virtualize-or-Materialize Decision Record captures each source, selected pattern, assumptions,
latency, freshness, copy location, authority, security, cost, fallback, recovery, owner, and review
trigger.

## Evidence boundary

Move less data first is a decision prompt, not an absolute rule. Local engineering measurements and
risk review determine the production design.
