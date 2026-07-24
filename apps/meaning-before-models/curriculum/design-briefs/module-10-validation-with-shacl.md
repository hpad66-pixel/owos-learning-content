# Module 10 Design Brief: Validation with SHACL

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-course-semantic-data-ai-001`, `mbm001:10` |
| Working title | Validation with SHACL |
| Learner roles | Utility staff, data stewards, operations owners, semantic practitioners, leaders |
| Competencies | Explain SHACL, configure a small shape, interpret a result, and route remediation |
| Controlled sources | W3C SHACL, SHACL 1.2 Core, RDF 1.2 Concepts, OWL 2 Overview |
| Evidence boundary | Shape conformance does not prove source truth or confer operating authority |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | An agent cannot complete a shutdown brief because a pump graph node lacks governed identity, status, and date values. |
| What must the learner decide before teaching begins? | Which control should run before the agent relies on the node. |
| What professional consequence makes this matter? | Hidden graph defects spread into entity resolution, context packages, and operational handoffs. |
| What should the learner be able to do afterward? | Distinguish data and shapes graphs, interpret validation results, and connect severity to a governed workflow consequence. |
| What usable work product will the learner create? | SHACL Constraint Card |
| What evidence is required for completion? | Triage, shape console, result router, card, applied review |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| Validation result anatomy | Repair ticket | `packet-anatomy` | Inspect focus node, path, constraint, message | Precise remediation target | `defect-triage` |
| Shape configuration | Inspection console | Interactive simulator | Configure and run three constraints | Report changes to three named findings | `shape-configuration` |
| OWL versus SHACL | Side-by-side matrix | `comparison-table` | Compare questions and outputs | Reasoning and validation separate | Embedded check |
| Defect propagation and routing | Chain plus board | `failure-propagation-chain` | Route three findings | Workflow consequence becomes explicit | `severity-routing` |
| Transfer | Contract card | Review artifact | Specify one utility constraint | Technical and business controls join | `applied-assessment` |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | Graph inspection station |
| Signature mechanism | Live shape console and remediation board |
| Course visual language applied here | Inspection tickets, result columns, warning bands |
| Intended learner feeling | “I know what failed, where, why, and who should respond.” |
| Narrative architecture | Failed intake, inspection language, console, remediation floor, constraint card |
| Mental model | Data graph plus shapes graph produces a validation report |
| Purposeful interaction 1 | `shacl-shape-console` |
| Purposeful interaction 2 | `validation-result-routing-board` |
| Explanatory visuals, normally two to five | `packet-anatomy`, `comparison-table`, `failure-propagation-chain` |
| Visual pacing plan and any prose exception | Every terminology block is followed by an inspection object or console |
| Original editorial illustration, when appropriate | Failed-handoff count and inspection strip |
| Assessment sequence and cognitive jobs | `defect-triage`, `shape-configuration`, `severity-routing`, `applied-assessment` |
| Distributed assessment locations | Intake, constraint design, remediation, transfer |
| Final applied work-product check | Completeness check against the SHACL Constraint Card |
| Role-sensitive treatment | Foundation, practitioner, leader lenses |
| Professional work product | SHACL Constraint Card |
| Same-page Knowledge Graph behavior | Connects target, shape, constraint, result, and steward |
| Header Graph, Community, and Start actions | Present |
| Bottom connected-learning section | Constraint graph and practice comparison |
| Explicit bottom `#owos-course-community` anchor before navigation | Present |
| Drawer focus return and mobile behavior | Shared fieldbook behavior; board and console stack |
| Module-specific FAQ location and disclosure behavior | Six SHACL questions before evidence boundary |
| Animation and teaching purpose | Console and routing react only to learner input |
| Reduced-motion equivalent | Text result report appears without motion dependency |
| Mobile transformation | Inspection surfaces stack; tables scroll |
| Persistence and learner events | Local state and artifact persistence |

## Instructor explanation plan

| Major component | What the learner sees | What the learner does | What to notice | Utility meaning | Debrief needed |
| --- | --- | --- | --- | --- | --- |
| Failed handoff | Three findings | Choose SHACL | Prompt rewriting does not validate graph | Gate agent context | Yes |
| Result packet | Focus/path/constraint/message | Read in order | Result is actionable | Steward workflow | Yes |
| Shape console | Shape and source record | Configure constraints | Data graph remains separate | Testable contract | Yes |
| Router | Three severities | Assign consequences | Severity is not risk authority | Governance mapping | Yes |

## Written-first review

- Approximate conversational teaching words: 2,000
- Worked utility example and marker: P-104 handoff; `data-worked-example`
- Misconception addressed: SHACL cleans data or proves real-world truth.
- Boundary or non-example: Valid datatype can still contain the wrong fact.
- Component debriefs: Result packet, comparison, propagation chain, router.
- What remains if every video and animation is removed: Full inspection logic, console text, routing, artifact, FAQs, sources.

## Visual pacing review

- Longest run of consecutive full prose blocks: Two paragraphs.
- Visual, interaction, worked example, or callout used to break each dense section: Intake strip, packet, console, table, chain, router.
- Any uninterrupted prose exception and reason: Vocabulary kept together for coherent first explanation.
- Editorial illustration reading guide and learner conclusion, when used: Intake strip is interpreted in opening prompt.
- Dark-surface contrast plan: Shape console uses explicit white text and shared drawer contrast.

## Explanatory graphic plan

| Teaching idea | Visual shape | Arsenal pattern | Learner conclusion | How the instructor explains it | Accessible and mobile treatment |
| --- | --- | --- | --- | --- | --- |
| Validation result fields | Packet | `packet-anatomy` | Steward can locate defect | Read focus to message | Text cards |
| OWL versus SHACL | Table | `comparison-table` | Logic and validation differ | Compare one row at a time | Horizontal scroll |
| Downstream cost | Chain | `failure-propagation-chain` | Early validation prevents amplification | Follow missing ID | Ordered cards |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| Does SHACL clean data? | Validation and remediation conflated | No, it reports | P-104 ID | Router | Repairs require authority |
| Does conforming mean true? | Syntax mistaken for fact | No | Correctly typed wrong date | Packet | Source review required |
| One giant shape? | Centralization seems easier | Use workflow-focused versions | Handoff versus public map | Console | Local design needed |
| Severity equals risk? | Similar labels | Utility maps technical result to consequence | Missing ID | Router | Policy required |
| Can it validate paths? | Seen as field validation | Yes | Outfall to receiving water | Table | Shape testing required |
| Where should it run? | Many control points | Where it catches defects before costly use | Agent handoff | Failure chain | Latency and ownership vary |

## Recording script

| Field | Decision |
| --- | --- |
| Script path | `curriculum/scripts/module-10-validation-with-shacl-video-script.md` |
| Intended recording length | 12 to 15 minutes if recorded |
| Spoken opening | “The node looks readable, but the handoff still fails.” |
| Utility example | P-104 identity, status, installation date |
| Visual directions | Reveal report packet, run shape, route results |
| Learner action and work product | Configure console and create Constraint Card |
| Transition to next lesson | A valid statement still needs provenance, authority, and time |

## Diversity check

- Adjacent module reviewed: OWL inference courtroom and provenance evidence hearing.
- Course Experience Brief reviewed: Yes.
- Lesson archetype differs from adjacent modules: Yes.
- Signature mechanism is unique to this lesson: Yes.
- Opening pattern intentionally different: Failed agent handoff.
- Dominant visual intentionally different: Inspection packet and console.
- Interaction pair intentionally different: Shape configuration and remediation routing.
- Quiz sequence intentionally different: `defect-triage` → `shape-configuration` → `severity-routing` → `applied-assessment`.
- Work-product format intentionally different: Constraint Card.
- Any justified repetition: Shared shell and governed controls only.
- Course-level distinctiveness result: Diagnostic required after whole-course retrofit.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | conditional | Codex working review | 2026-07-23 | W3C sources used; factual review pending |
| Learning design | passed | Codex working review | 2026-07-23 | Distinct inspection architecture |
| Utility practice | pending |  |  | Practitioner review required |
| Golden lesson benchmark, when applicable | not applicable |  |  |  |
