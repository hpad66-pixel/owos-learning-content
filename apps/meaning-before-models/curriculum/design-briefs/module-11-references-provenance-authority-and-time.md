# Module 11 Design Brief: References, Provenance, Authority, and Time

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-course-semantic-data-ai-001`, `mbm001:11` |
| Working title | References, Provenance, Authority, and Time |
| Learner roles | All utility staff, evidence stewards, document owners, data practitioners, leaders |
| Competencies | Distinguish reference, provenance, authority, version, supersession, and four time questions |
| Controlled sources | W3C PROV-O, PROV Overview, RDF 1.2, OWL-Time |
| Evidence boundary | Instructional pressure limits do not establish local operating authority |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | Historian, old procedure, approved procedure, and operator note conflict about P-104. |
| What must the learner decide before teaching begins? | Which statement controls the operating-limit question at 9:15 a.m. |
| What professional consequence makes this matter? | “Newest” or “most confident” can select the wrong type of evidence. |
| What should the learner be able to do afterward? | Trace derivation, classify source role, select the relevant clock, and document escalation. |
| What usable work product will the learner create? | Authority and Time Ledger |
| What evidence is required for completion? | Authority ruling, docket classification, four-clock review, ledger, applied review |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| Controlling authority | Evidence hearing | Source docket | Select controlling statement | Scope and effective status defeat “newest” | `authority-ranking` |
| Provenance chain | Entity-activity-agent network | `provenance-network` | Classify source roles | Transformations and derivations remain visible | `conflict-resolution` |
| Four clocks | Time comparison and lens | `comparison-table`, `interactive-process` | Inspect all clocks and resolve applicability | Relevant clock changes with question | `timeline-reconstruction` |
| Transfer | Ledger | Professional artifact | Record claim governance | Conflict resolution becomes reproducible | `applied-assessment` |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | Evidence hearing |
| Signature mechanism | Four-clock evidence docket |
| Course visual language applied here | Hearing room, docket cards, authority chair, clocks |
| Intended learner feeling | “I know why this source controls this question at this time.” |
| Narrative architecture | Hearing, vocabulary, provenance docket, clock review, ledger |
| Mental model | Claim plus provenance plus authority plus applicable time |
| Purposeful interaction 1 | `provenance-docket-classifier` |
| Purposeful interaction 2 | `four-clock-question-lens` |
| Explanatory visuals, normally two to five | `provenance-network`, `comparison-table`, `interactive-process` |
| Visual pacing plan and any prose exception | Source cards, network, table, and clock lens alternate with explanation |
| Original editorial illustration, when appropriate | Evidence hearing room and authority chair |
| Assessment sequence and cognitive jobs | `authority-ranking`, `conflict-resolution`, `timeline-reconstruction`, `applied-assessment` |
| Distributed assessment locations | Opening, provenance, time, transfer |
| Final applied work-product check | Ledger completeness review |
| Role-sensitive treatment | Foundation, practitioner, leader authority lenses |
| Professional work product | Authority and Time Ledger |
| Same-page Knowledge Graph behavior | Traces entity, activity, agent, derivation, role |
| Header Graph, Community, and Start actions | Present |
| Bottom connected-learning section | Evidence chain and source conflict discussion |
| Explicit bottom `#owos-course-community` anchor before navigation | Present |
| Drawer focus return and mobile behavior | Shared fieldbook; hearing and clocks stack |
| Module-specific FAQ location and disclosure behavior | Six source/time questions before evidence boundary |
| Animation and teaching purpose | Question-triggered clock explanation only |
| Reduced-motion equivalent | Immediate textual outputs |
| Mobile transformation | Docket, network, clocks, ledger become one column |
| Persistence and learner events | Local completion and artifact storage |

## Instructor explanation plan

| Major component | What the learner sees | What the learner does | What to notice | Utility meaning | Debrief needed |
| --- | --- | --- | --- | --- | --- |
| Hearing | Four conflicting sources | Choose controlling evidence | Newest is not authority | Decision governance | Yes |
| Provenance network | Source-to-answer chain | Classify roles | Extraction and mapping are activities | Reproducibility | Yes |
| Four clocks | Table and lens | Inspect and select | Time means different things | Historical and effective truth | Yes |
| Ledger | Structured review form | Document one claim | Supersession and escalation are explicit | Audit-ready handoff | Yes |

## Written-first review

- Approximate conversational teaching words: 2,100
- Worked utility example and marker: P-104 pressure-limit hearing; `data-worked-example`
- Misconception addressed: Latest timestamp or extraction confidence equals authority.
- Boundary or non-example: OCR confidence cannot revive a superseded procedure.
- Component debriefs: Docket, provenance network, time comparison, clock lens.
- What remains if every video and animation is removed: Full source logic, four-clock explanation, exercises, ledger, FAQs, sources.

## Visual pacing review

- Longest run of consecutive full prose blocks: Two paragraphs.
- Visual, interaction, worked example, or callout used to break each dense section: Hearing, network, docket, clock table, lens.
- Any uninterrupted prose exception and reason: Vocabulary is grouped to compare terms.
- Editorial illustration reading guide and learner conclusion, when used: Hearing is explained before source ruling.
- Dark-surface contrast plan: Authority chair and drawers use explicit light text.

## Explanatory graphic plan

| Teaching idea | Visual shape | Arsenal pattern | Learner conclusion | How the instructor explains it | Accessible and mobile treatment |
| --- | --- | --- | --- | --- | --- |
| Derivation chain | Five-node flow | `provenance-network` | Answer can be reproduced | Follow source to extraction to graph | Text nodes stack |
| Time distinctions | Table | `comparison-table` | Select clock by question | Read one time job per row | Scrollable |
| Question-driven time | Clock deck | `interactive-process` | Governing rule uses effective time | Trigger all four | Text outputs |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| Newest equals authority? | Time columns dominate | No | Historian versus procedure | Hearing | Local policy applies |
| Citation equals provenance? | Both point backward | No | Clause and extraction | Network | Capture transformation |
| Can notes be authoritative? | Personhood mistaken for scope | Within defined scope | Field condition | Docket | Approval policy required |
| OCR confidence? | Numeric confidence looks objective | It applies to extraction | Old procedure | Network | Review low confidence |
| Preserve superseded data? | Old seems useless | Yes, for history and audit | 2018 procedure | Hearing | Mark time and scope |
| Provenance makes generation deterministic? | Grounding overpromised | No | Agent summary | Clock lens | Generative wording may vary |

## Recording script

| Field | Decision |
| --- | --- |
| Script path | `curriculum/scripts/module-11-references-provenance-authority-and-time-video-script.md` |
| Intended recording length | 14 to 17 minutes if recorded |
| Spoken opening | “Four sources say four different things. Which one controls?” |
| Utility example | P-104 105 psi procedure |
| Visual directions | Convene hearing, trace derivation, rotate through four clocks |
| Learner action and work product | Classify docket and complete ledger |
| Transition to next lesson | Put meaning, sources, controls, and consumers into a running spine |

## Diversity check

- Adjacent module reviewed: SHACL inspection station and knowledge-spine operations bridge.
- Course Experience Brief reviewed: Yes.
- Lesson archetype differs from adjacent modules: Yes.
- Signature mechanism is unique to this lesson: Yes.
- Opening pattern intentionally different: Conflicting-source hearing.
- Dominant visual intentionally different: Evidence docket and clock deck.
- Interaction pair intentionally different: Source-role classification and time-question lens.
- Quiz sequence intentionally different: `authority-ranking` → `conflict-resolution` → `timeline-reconstruction` → `applied-assessment`.
- Work-product format intentionally different: Authority and Time Ledger.
- Any justified repetition: Shared platform controls only.
- Course-level distinctiveness result: Diagnostic required.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | conditional | Codex working review | 2026-07-23 | W3C provenance sources used; local authority review pending |
| Learning design | passed | Codex working review | 2026-07-23 | Distinct evidence-hearing architecture |
| Utility practice | pending |  |  | Practitioner review required |
| Golden lesson benchmark, when applicable | not applicable |  |  |  |
