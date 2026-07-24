# OWOS Module Design Brief

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-master-data-governance-001`, `dga001:11` |
| Working title | Can you rebuild the number? |
| Learner roles | Billing, customer service, data, technology, assurance, leaders |
| Competencies | Reconstruct run-level lineage and trace impacts forward |
| Controlled sources | Method v2.3 D04; W3C PROV-O and PROV-DM; NIST SP 800-53 |
| Evidence boundary | Instructional bill. No billing proof, compliance, or assurance conclusion. |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | A disputed bill cannot be reproduced. |
| What must the learner decide before teaching begins? | Whether current data or the bill PDF is sufficient proof. |
| What professional consequence makes this matter? | An unsupported charge may be defended or corrected incorrectly. |
| What should the learner be able to do afterward? | Rebuild the exact historical run and trace effects forward. |
| What usable work product will the learner create? | Lineage and provenance pack. |
| What evidence is required for completion? | Decision, replay, handoff, ordering check, saved pack, final defense. |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| Run-level proof | Network | `provenance-network` | Step through entities, activities, and agents | Missing manual activity becomes visible | `ordering` |
| Evidence must survive transfer | Process | `handoff-simulator` | Compare fragmented and governed packets | Reproducibility changes | Applied defense |
| Designed route differs from historical run | Evidence sequence | Worked reconstruction strip | Trace from bill to outcome | Exact versions and authority appear | Opening judgment |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | lineage-reconstruction |
| Signature mechanism | rebuild-broken-decision-lineage-from-provenance-events |
| Course visual language applied here | Investigation wall and replay network |
| Intended learner feeling | Forensic curiosity followed by evidentiary confidence |
| Narrative architecture | Dispute, backward trace, manual-event discovery, replay, forward impact |
| Mental model | Entity + activity + agent + version + decision + outcome |
| Purposeful interaction 1 | Broken lineage replay |
| Purposeful interaction 2 | Evidence packet handoff |
| Explanatory visuals, normally two to five | `provenance-network`, `handoff-simulator`, evidence strip |
| Visual pacing plan and any prose exception | Reconstruction visual follows each teaching block |
| Original editorial illustration, when appropriate | Evidence strip replaces a scene illustration |
| Assessment sequence and cognitive jobs | Opening judgment, `ordering`, applied reconstruction defense |
| Distributed assessment locations | Incident opening, replay teaching, pack close |
| Final applied work-product check | Historical-run and forward-impact defense |
| Role-sensitive treatment | Foundation, practitioner, leader |
| Professional work product | Lineage and provenance pack |
| Same-page Knowledge Graph behavior | Drawer with entity, activity, agent relationships |
| Header Graph, Community, and Start actions | Present |
| Bottom connected-learning section | Present |
| Explicit bottom `#owos-course-community` anchor before navigation | Present |
| Drawer focus return and mobile behavior | Shared accessible runtime |
| Module-specific FAQ location and disclosure behavior | Six investigation questions before evidence boundary |
| Animation and teaching purpose | Step replay reveals proof in sequence |
| Reduced-motion equivalent | Manual Step control and immediate states |
| Mobile transformation | Single-column reconstruction and scrollable evidence strip |
| Persistence and learner events | Browser-only pack; release events disabled |

## Instructor explanation plan

| Major component | What the learner sees | What the learner does | What to notice | Utility meaning | Debrief needed |
| --- | --- | --- | --- | --- | --- |
| Provenance network | Records, activities, agents | Step through replay | Manual change closes the trace | Historical proof needs exact events | Yes |
| Handoff simulator | Three-role evidence transfer | Compare modes | Context survives governed transfer | Answers must carry proof | Yes |
| Ordering check | Investigation steps | Reorder | Current pipeline is not the starting point | Exact output anchors replay | Immediate feedback |

## Written-first review

- Approximate conversational teaching words: more than 1,200.
- Worked utility example and marker: Riverbend bill 770184.
- Misconception addressed: current architecture or output PDF is historical proof.
- Boundary or non-example: present-day rerun.
- Component debriefs: after both mechanisms.
- What remains if every video and animation is removed: complete reconstruction teaching and evidence sequence.

## Visual pacing review

- Longest run of consecutive full prose blocks: two.
- Visual, interaction, worked example, or callout used to break each dense section: all used.
- Any uninterrupted prose exception and reason: none.
- Editorial illustration reading guide and learner conclusion, when used: not applicable.
- Dark-surface contrast plan: explicit shared light text.

## Explanatory graphic plan

| Teaching idea | Visual shape | Arsenal pattern | Learner conclusion | How the instructor explains it | Accessible and mobile treatment |
| --- | --- | --- | --- | --- | --- |
| Historical run | Relationship network | Provenance network | Exact versions and agents matter | Step from output backward and forward | SVG label and controls |
| Controlled transfer | Process chain | Handoff simulator | Proof travels with answer | Compare two modes | Stacked mobile mode |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| Lineage or audit log? | Both show history | Logs are inputs to connected lineage | Billing run | Network | No assurance |
| How much detail? | Detail can be expensive | Match consequence | Disputed bill | Comparison | Proportionate |
| What about spreadsheets? | Manual work is overlooked | Include file and activity evidence | Exception file | Sequence | Protected data |
| Reconstruct later? | Evidence may be gone | Preserve gaps and correct control | Missing run | Worked case | No false certainty |
| Who owns it? | Several teams contribute | Assign jobs by authority | Billing replay | Role view | Local authority |

## Recording script

| Field | Decision |
| --- | --- |
| Script path | Not planned |
| Intended recording length | Not applicable |
| Spoken opening | Written lesson only |
| Utility example | Disputed bill |
| Visual directions | On-page |
| Learner action and work product | Reconstruction pack |
| Transition to next lesson | From reproducibility to fitness for use |

## Diversity check

- Adjacent module reviewed: metadata forensics and quality clinic.
- Course Experience Brief reviewed: yes.
- Lesson archetype differs from adjacent modules: yes.
- Signature mechanism is unique to this lesson: yes.
- Opening pattern intentionally different: disputed historical output.
- Dominant visual intentionally different: provenance replay.
- Interaction pair intentionally different: replay plus handoff.
- Quiz sequence intentionally different: judgment, ordering, defense.
- Work-product format intentionally different: evidence-index reconstruction.
- Any justified repetition: shared navigation and accessibility only.
- Course-level distinctiveness result: batch lessons distinct; later shells still block course.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | pending | | | Source-owner review required |
| Learning design | conditional | Codex | 2026-07-23 | Automated working gate targeted |
| Utility practice | pending | | | Billing practitioner review required |
| Golden lesson benchmark, when applicable | not applicable | | | |
