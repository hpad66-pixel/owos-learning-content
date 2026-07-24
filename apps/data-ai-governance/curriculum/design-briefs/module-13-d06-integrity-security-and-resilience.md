# OWOS Module Design Brief

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-master-data-governance-001`, `dga001:13` |
| Working title | The screen is green. Can you trust it? |
| Learner roles | Operators, OT, IT, cyber, emergency, engineering, leaders |
| Competencies | Separate integrity, availability, safe response, and tested recovery |
| Controlled sources | Method v2.3 D06; NIST SP 800-82, CSF; CISA water resources |
| Evidence boundary | No operational procedure, assessment, or security-sensitive detail. |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | Chemical-feed setpoint and evidence cannot be trusted. |
| What must the learner decide before teaching begins? | Continue automation, reboot, or use safe-state verification. |
| What professional consequence makes this matter? | Unsafe treatment and loss of trusted operational evidence. |
| What should the learner be able to do afterward? | Design layered controls and return-to-service evidence. |
| What usable work product will the learner create? | Integrity and resilience control plan. |
| What evidence is required for completion? | Decision, failure injections, evidence check, plan, defense. |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| Trust crosses boundaries | Network | `network-diagram` | Follow process to decision | Available screen can hide upstream failure | `multi-select` |
| Failures have different consequences | Cause chain | `failure-chain` | Inject three failures | Integrity, availability, recovery diverge | Multi-select |
| Controls need depth | Stack | `layered-stack` | Read independent layers | Recovery and learning remain visible | Applied defense |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | resilience-challenge |
| Signature mechanism | inject-integrity-availability-and-recovery-failures |
| Course visual language applied here | Control-room path, failure chain, control stack |
| Intended learner feeling | Tension, disciplined containment, confidence |
| Narrative architecture | Incident call, physical verification, failure injection, layered recovery |
| Mental model | Prevent, detect, respond, recover, learn |
| Purposeful interaction 1 | Failure injection console |
| Purposeful interaction 2 | Return-to-service evidence challenge |
| Explanatory visuals, normally two to five | `network-diagram`, `failure-chain`, `layered-stack` |
| Visual pacing plan and any prose exception | Control-room scene alternates with diagrams |
| Original editorial illustration, when appropriate | Network path teaches the scene without protected detail |
| Assessment sequence and cognitive jobs | Opening containment judgment, `multi-select`, applied plan defense |
| Distributed assessment locations | Incident opening, return evidence, artifact |
| Final applied work-product check | Layered resilience defense |
| Role-sensitive treatment | Foundation, practitioner, leader |
| Professional work product | Integrity and resilience plan |
| Same-page Knowledge Graph behavior | Physical state to authority path |
| Header Graph, Community, and Start actions | Present |
| Bottom connected-learning section | Present |
| Explicit bottom `#owos-course-community` anchor before navigation | Present |
| Drawer focus return and mobile behavior | Shared runtime |
| Module-specific FAQ location and disclosure behavior | Six operational questions |
| Animation and teaching purpose | Scenario state changes cause path failures |
| Reduced-motion equivalent | Immediate static path update |
| Mobile transformation | Scrollable control paths |
| Persistence and learner events | Browser-only plan |

## Instructor explanation plan

| Major component | What the learner sees | What the learner does | What to notice | Utility meaning | Debrief needed |
| --- | --- | --- | --- | --- | --- |
| Trust path | Five boundaries | Follow path | Later display can hide earlier failure | Verify end to end | Yes |
| Failure console | Three incident modes | Inject failure | Response differs by condition | Safe state and evidence drive action | Yes |
| Control stack | Five layers | Read depth | Backup is not recovery | Exercise the whole service | Yes |

## Written-first review

- Approximate conversational teaching words: more than 1,200.
- Worked utility example and marker: chemical-feed control incident.
- Misconception addressed: uptime proves trustworthy state.
- Boundary or non-example: green dashboard or backup-job result.
- Component debriefs: visible.
- What remains if every video and animation is removed: full control reasoning and incident sequence.

## Visual pacing review

- Longest run of consecutive full prose blocks: two.
- Visual, interaction, worked example, or callout used to break each dense section: yes.
- Any uninterrupted prose exception and reason: none.
- Editorial illustration reading guide and learner conclusion, when used: trust path includes scene meaning.
- Dark-surface contrast plan: white text on control-room surfaces.

## Explanatory graphic plan

| Teaching idea | Visual shape | Arsenal pattern | Learner conclusion | How the instructor explains it | Accessible and mobile treatment |
| --- | --- | --- | --- | --- | --- |
| End-to-end trust | Network | Network diagram | Screen availability is downstream evidence only | Read physical to decision | Labeled scroll strip |
| Failure consequence | Chain | Failure-propagation chain | Failure class changes action | Inject one condition | Button and live output |
| Defense depth | Stack | Layered stack | Independent layers preserve service | Read prevention to learning | Responsive cards |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| Cyber only an IT job? | Technical ownership dominates | Service roles share distinct jobs | Chemical control | Role map | No procedure |
| Backup or recovery? | Terms are conflated | Recovery is tested restoration | Controller baseline | Stack | Local objectives |
| Every anomaly cyber? | Causes overlap | Preserve evidence and classify carefully | Sensor fault | Failure chain | No attribution |
| Anomaly proves integrity? | Detection sounds conclusive | It is one signal | Setpoint change | Network | No assurance |
| First move for small utility? | Program may feel large | Protect key decisions and exercise restore | Safe state | Sequence | Proportionate |

## Recording script

| Field | Decision |
| --- | --- |
| Script path | Not planned |
| Intended recording length | Not applicable |
| Spoken opening | Written incident |
| Utility example | Chemical-feed control |
| Visual directions | On-page |
| Learner action and work product | Resilience plan |
| Transition to next lesson | From system trust to people’s rights |

## Diversity check

- Adjacent module reviewed: quality clinic and rights panel.
- Course Experience Brief reviewed: yes.
- Lesson archetype differs from adjacent modules: yes.
- Signature mechanism is unique to this lesson: yes.
- Opening pattern intentionally different: live control-room incident.
- Dominant visual intentionally different: failure propagation.
- Interaction pair intentionally different: scenario injection plus evidence selection.
- Quiz sequence intentionally different: containment, multi-select, defense.
- Work-product format intentionally different: control and exercise plan.
- Any justified repetition: shared course controls only.
- Course-level distinctiveness result: later shells still block.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | pending | | | OT security review |
| Learning design | conditional | Codex | 2026-07-23 | Automated gate targeted |
| Utility practice | pending | | | Operator review |
| Golden lesson benchmark, when applicable | not applicable | | | |
