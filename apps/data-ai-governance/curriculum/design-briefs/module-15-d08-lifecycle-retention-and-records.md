# OWOS Module Design Brief

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-master-data-governance-001`, `dga001:15` |
| Working title | The old plan is still making decisions |
| Learner roles | Operations, engineering, records, legal, technology, leaders |
| Competencies | Separate current use, retention, hold, and disposition |
| Controlled sources | Method v2.3 D08; NARA scheduling guidance; ISO 15489-1 |
| Evidence boundary | No schedule, hold, public-records, or disposition authority. |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | A superseded isolation plan remains on crew tablets during a hold. |
| What must the learner decide before teaching begins? | Delete, leave available, or separate use from preservation. |
| What professional consequence makes this matter? | Unsafe field work or destruction of evidence. |
| What should the learner be able to do afterward? | Apply lifecycle events and write a schedule record. |
| What usable work product will the learner create? | Lifecycle and retention schedule record. |
| What evidence is required for completion? | Decision, timeline, judgment check, saved record, defense. |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| Events change allowed action | Timeline | `timeline-roadmap` | Select lifecycle event | Use and preservation states separate | `multiple-choice` |
| Related evidence has different classes | Hierarchy | `tree-wbs` | Read record families | One incident spans several schedules | Multiple choice |
| Disposition is gated | Process | `phase-gate` | Step through review | Eligibility can stop at each gate | Applied defense |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | records-lifecycle-timeline |
| Signature mechanism | apply-retention-disposition-hold-and-supersession-decisions |
| Course visual language applied here | Version timeline, record tree, disposition gate |
| Intended learner feeling | Urgency, distinction, controlled closure |
| Narrative architecture | Field conflict, reconciliation, event timeline, series classification, disposition |
| Mental model | Class + trigger + period + exception + authority + proof |
| Purposeful interaction 1 | Lifecycle event console |
| Purposeful interaction 2 | Records judgment |
| Explanatory visuals, normally two to five | `timeline-roadmap`, `tree-wbs`, `phase-gate` |
| Visual pacing plan and any prose exception | Each lifecycle distinction is followed by a representation |
| Original editorial illustration, when appropriate | Field conflict taught in worked sequence |
| Assessment sequence and cognitive jobs | Opening judgment, `multiple-choice`, applied schedule defense |
| Distributed assessment locations | Field opening, after disposition, artifact |
| Final applied work-product check | Schedule and authority defense |
| Role-sensitive treatment | Three lenses |
| Professional work product | Lifecycle and retention schedule record |
| Same-page Knowledge Graph behavior | Series, version, trigger, hold, disposition |
| Header Graph, Community, and Start actions | Present |
| Bottom connected-learning section | Present |
| Explicit bottom `#owos-course-community` anchor before navigation | Present |
| Drawer focus return and mobile behavior | Shared runtime |
| Module-specific FAQ location and disclosure behavior | Six records questions |
| Animation and teaching purpose | Event selection changes allowed action |
| Reduced-motion equivalent | Immediate timeline update |
| Mobile transformation | Horizontal labeled timeline and stacked form |
| Persistence and learner events | Browser-only schedule draft |

## Instructor explanation plan

| Major component | What the learner sees | What the learner does | What to notice | Utility meaning | Debrief needed |
| --- | --- | --- | --- | --- | --- |
| Lifecycle console | Six stages and four events | Select event | Superseded and held are distinct | Use and preservation separate | Yes |
| Record tree | Evidence families | Follow branches | One decision links several series | Classification is functional | Yes |
| Disposition gate | Six stages | Step through | Eligibility is not automatic deletion | Authority and proof remain | Yes |

## Written-first review

- Approximate conversational teaching words: more than 1,200.
- Worked utility example and marker: valve-plan reconciliation.
- Misconception addressed: obsolete means deletable or held means current.
- Boundary or non-example: filename warning as records control.
- Component debriefs: visible.
- What remains if every video and animation is removed: complete lifecycle and disposition teaching.

## Visual pacing review

- Longest run of consecutive full prose blocks: two.
- Visual, interaction, worked example, or callout used to break each dense section: yes.
- Any uninterrupted prose exception and reason: none.
- Editorial illustration reading guide and learner conclusion, when used: not applicable.
- Dark-surface contrast plan: explicit shared rules.

## Explanatory graphic plan

| Teaching idea | Visual shape | Arsenal pattern | Learner conclusion | How the instructor explains it | Accessible and mobile treatment |
| --- | --- | --- | --- | --- | --- |
| Lifecycle state | Timeline | Roadmap | Events change allowed action | Compare same series over time | Scrollable cards |
| Record families | Hierarchy | Tree/WBS | Related evidence can follow different rules | Read from decision down | Semantic list |
| Disposition | Gated process | Phase gate | Every gate can stop action | Step authority to proof | Responsive stepper |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| Is all data a record? | Format bias | Function and authority determine status | Sensor event | Tree | Local law |
| Keep forever? | Preservation seems safer | Over-retention creates risk | Old plans | Timeline | No schedule |
| Hold permanent? | Hold pauses action | Return to schedule after release | Revision 5 | Timeline | Legal review |
| Backups? | Copies are hidden | Define schedule and hold treatment | Restored obsolete file | Gate | Architecture-specific |
| AI decision record? | New formats confuse | Retain reconstruction evidence | Model action | Sequence | Use-specific |

## Recording script

| Field | Decision |
| --- | --- |
| Script path | Not planned |
| Intended recording length | Not applicable |
| Spoken opening | Written field conflict |
| Utility example | Valve plan |
| Visual directions | On-page |
| Learner action and work product | Schedule record |
| Transition to next lesson | From internal lifecycle to external sharing |

## Diversity check

- Adjacent module reviewed: rights panel and sharing boundary.
- Course Experience Brief reviewed: yes.
- Lesson archetype differs from adjacent modules: yes.
- Signature mechanism is unique to this lesson: yes.
- Opening pattern intentionally different: old record in current field use.
- Dominant visual intentionally different: lifecycle timeline.
- Interaction pair intentionally different: event selector and judgment.
- Quiz sequence intentionally different: field decision, multiple choice, defense.
- Work-product format intentionally different: schedule record.
- Any justified repetition: shared controls only.
- Course-level distinctiveness result: later shells still block.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | pending | | | Records and legal review |
| Learning design | conditional | Codex | 2026-07-23 | Automated gate targeted |
| Utility practice | pending | | | Operations review |
| Golden lesson benchmark, when applicable | not applicable | | | |
