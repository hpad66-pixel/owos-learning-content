# Module 13 Design Brief: Map Meaning to Data

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-course-semantic-data-ai-001`, `mbm001:13` |
| Working title | Map Meaning to Data |
| Learner roles | Non-technical domain staff, integration teams, data engineers, semantic modelers, leaders |
| Competencies | Distinguish joins and mappings; specify identity, triples, transformations, provenance, and tests |
| Controlled sources | W3C R2RML, Direct Mapping, RDF 1.2 Concepts, PROV-O |
| Evidence boundary | Source dictionaries and actual mappings require local review |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | Three systems expose a field named STATUS with three different meanings. |
| What must the learner decide before teaching begins? | Whether to collapse the fields or map lifecycle, run, and work status separately. |
| What professional consequence makes this matter? | A bad mapping creates confident semantic error for every dashboard, graph query, and agent. |
| What should the learner be able to do afterward? | Define stable identity, map source fields to concepts, preserve units and provenance, and specify tests. |
| What usable work product will the learner create? | Semantic Mapping Specification |
| What evidence is required for completion? | False-equivalence ruling, wiring bench, unit normalizer, specification, applied review |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| Same label, different meaning | Source wall | Editorial source boards | Reject false equivalence | Three status concepts separate | `mapping-classification` |
| Cross-system identity | Bridge | `identity-bridge` | Inspect reconciliation | Local records stay traceable | `identity-join` |
| Join, map, transform, infer | Comparison | `comparison-table` | Compare operations | Jobs and boundaries become explicit | Embedded check |
| Mapping lifecycle | Five-stage flow and bench | `interactive-process` | Wire fields to concepts | Expected triples appear | `identity-join` |
| Unit normalization | Conversion machine | Measured-value simulation | Preserve original and derived values | Provenance appears | `unit-normalization` |
| Transfer | Specification | Professional artifact | Write expected triples and tests | Mapping becomes reviewable | `applied-assessment` |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | Semantic wiring workshop |
| Signature mechanism | Source-to-concept wiring bench |
| Course visual language applied here | Workshop wall, bridge, wiring bench, conversion gear |
| Intended learner feeling | “I can explain exactly how this field becomes that graph statement.” |
| Narrative architecture | Source wall, vocabulary, identity bridge, wiring bench, normalization, specification |
| Mental model | Source contract plus mapping rules produces testable RDF statements |
| Purposeful interaction 1 | `source-to-concept-wiring-bench` |
| Purposeful interaction 2 | `unit-and-provenance-normalizer` |
| Explanatory visuals, normally two to five | `identity-bridge`, `comparison-table`, `interactive-process` |
| Visual pacing plan and any prose exception | Source boards and workshop mechanisms alternate with explanation |
| Original editorial illustration, when appropriate | Same-label source wall |
| Assessment sequence and cognitive jobs | `mapping-classification`, `identity-join`, `unit-normalization`, `applied-assessment` |
| Distributed assessment locations | Opening, mapping implementation, value normalization, transfer |
| Final applied work-product check | Mapping-specification completeness check |
| Role-sensitive treatment | Foundation, practitioner, leader mapping lenses |
| Professional work product | Semantic Mapping Specification |
| Same-page Knowledge Graph behavior | Traces source, triples map, property, role, competency |
| Header Graph, Community, and Start actions | Present |
| Bottom connected-learning section | Mapping graph and field-name discussion |
| Explicit bottom `#owos-course-community` anchor before navigation | Present |
| Drawer focus return and mobile behavior | Shared behavior; workshop stacks |
| Module-specific FAQ location and disclosure behavior | Six mapping questions before evidence boundary |
| Animation and teaching purpose | Mapping preview and unit derivation appear on valid learner choices |
| Reduced-motion equivalent | Immediate text updates |
| Mobile transformation | Wall, bridge, bench, and converter become one column |
| Persistence and learner events | Local state and specification storage |

## Instructor explanation plan

| Major component | What the learner sees | What the learner does | What to notice | Utility meaning | Debrief needed |
| --- | --- | --- | --- | --- | --- |
| Source wall | Three STATUS fields | Reject collapse | Labels are not semantics | Prevent false equivalence | Yes |
| Identity bridge | Three local keys | Trace reconciliation | Graph identity is governed | Entity resolution | Yes |
| Comparison | Four operations | Compare boundaries | Join is not mapping | Architecture clarity | Yes |
| Wiring bench | Source row and target graph | Configure mapping | Expected triples are testable | Mapping contract | Yes |
| Unit machine | Original and derived values | Choose preservation | Conversion creates derived evidence | Measurement integrity | Yes |

## Written-first review

- Approximate conversational teaching words: 2,200
- Worked utility example and marker: P-104 asset row; `data-worked-example`
- Misconception addressed: Semantic mapping is column renaming or an ordinary join.
- Boundary or non-example: Matching STATUS labels do not imply matching concepts.
- Component debriefs: Identity bridge, operation table, mapping flow, wiring bench, unit normalizer.
- What remains if every video and animation is removed: Full mapping explanation, expected triples, exercises, specification, FAQs, sources.

## Visual pacing review

- Longest run of consecutive full prose blocks: Two paragraphs.
- Visual, interaction, worked example, or callout used to break each dense section: Source wall, bridge, table, flow, bench, converter.
- Any uninterrupted prose exception and reason: Vocabulary grouped before the workshop.
- Editorial illustration reading guide and learner conclusion, when used: Source wall interpreted by opening choice.
- Dark-surface contrast plan: Mapping preview and drawers use explicit light text.

## Explanatory graphic plan

| Teaching idea | Visual shape | Arsenal pattern | Learner conclusion | How the instructor explains it | Accessible and mobile treatment |
| --- | --- | --- | --- | --- | --- |
| Identity | Bridge | `identity-bridge` | Matching is governed, not magical | Keep source links | Stacks |
| Operation boundaries | Table | `comparison-table` | Join, transform, map, infer differ | Read one operation per row | Scroll |
| Mapping lifecycle | Five-stage flow | `interactive-process` | Review meaning before code | Profile to release | Ordered cards |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| Just rename columns? | Mapping looks textual | No | STATUS properties | Table | Source dictionary required |
| Same RDF resource? | Identity feels technical | Yes, with governed rules | P-104 keys | Bridge | Reconciliation review |
| Map every column? | Completeness mistaken for value | No | Technical fields | Flow | Use-case boundary |
| Map documents? | R2RML is relational | Extract selected claims with provenance | Procedure clause | FAQ sequence | Authority review |
| Who approves code mapping? | Engineer may implement alone | Domain and source owners | Code A | Wiring bench | Governance required |
| Virtual or materialized? | Mapping confused with storage | Either, per workload | CMMS view | Spine transition | Architecture review |

## Recording script

| Field | Decision |
| --- | --- |
| Script path | `curriculum/scripts/module-13-map-meaning-to-data-video-script.md` |
| Intended recording length | 15 to 18 minutes if recorded |
| Spoken opening | “Three fields have the same label and three different meanings.” |
| Utility example | P-104 asset row and pressure conversion |
| Visual directions | Compare source wall, cross identity bridge, wire fields, derive unit |
| Learner action and work product | Run wiring bench and write Mapping Specification |
| Transition to next lesson | Choose whether each mapped path is virtualized, indexed, cached, or materialized |

## Diversity check

- Adjacent module reviewed: Knowledge-spine operations bridge and access-pattern decision lesson.
- Course Experience Brief reviewed: Yes.
- Lesson archetype differs from adjacent modules: Yes.
- Signature mechanism is unique to this lesson: Yes.
- Opening pattern intentionally different: Same-label false equivalence.
- Dominant visual intentionally different: Workshop wall and wiring bench.
- Interaction pair intentionally different: Mapping configuration and unit provenance.
- Quiz sequence intentionally different: `mapping-classification` → `identity-join` → `unit-normalization` → `applied-assessment`.
- Work-product format intentionally different: Semantic Mapping Specification.
- Any justified repetition: Shared platform controls only.
- Course-level distinctiveness result: Diagnostic required.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | conditional | Codex working review | 2026-07-23 | W3C mapping sources used; local source review pending |
| Learning design | passed | Codex working review | 2026-07-23 | Distinct workshop architecture |
| Utility practice | pending |  |  | Practitioner review required |
| Golden lesson benchmark, when applicable | not applicable |  |  |  |
