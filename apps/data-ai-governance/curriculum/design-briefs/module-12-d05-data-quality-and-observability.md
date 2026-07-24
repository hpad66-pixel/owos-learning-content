# OWOS Module Design Brief

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-master-data-governance-001`, `dga001:12` |
| Working title | “Good data” for which decision? |
| Learner roles | Operators, stormwater staff, data stewards, analysts, leaders |
| Competencies | Define quality requirements by use and operate issue closure |
| Controlled sources | Method v2.3 D05; ISO 8000 concepts; NIST and EPA quality anchors |
| Evidence boundary | Instructional thresholds. No alert, engineering, or quality certification. |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | A delayed and uneven rainfall feed is proposed for automated alerts. |
| What must the learner decide before teaching begins? | Whether a 93 percent average supports automation. |
| What professional consequence makes this matter? | Missed or late flood warning. |
| What should the learner be able to do afterward? | Write use-specific requirements, responses, and closure evidence. |
| What usable work product will the learner create? | Quality-by-use contract. |
| What evidence is required for completion? | Decision, model, closure loop, estimate, contract, defense. |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| Requirements move with use | Threshold model | `quality-by-use` | Change use and evidence | Critical gates move | `estimate` |
| Averages hide location and condition | Matrix | `heat-grid` | Inspect cells | Segment failure appears | Applied defense |
| Alerts need owned closure | Loop | `cycle-loop` | Step through response | Decision correction extends beyond pipeline repair | Estimate |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | quality-by-use-clinic |
| Signature mechanism | change-intended-use-and-watch-quality-requirements-change |
| Course visual language applied here | Quality clinic, threshold rows, condition grid |
| Intended learner feeling | Surprise at moving thresholds, then control |
| Narrative architecture | Intake, diagnosis, threshold experiment, observability, closure |
| Mental model | Stated use + critical requirement + evidence + response |
| Purposeful interaction 1 | Quality-by-use model |
| Purposeful interaction 2 | Quality issue closure loop |
| Explanatory visuals, normally two to five | `quality-by-use`, `heat-grid`, `cycle-loop` |
| Visual pacing plan and any prose exception | Every major section ends in a visual or worked example |
| Original editorial illustration, when appropriate | Not selected; grid and threshold model fit better |
| Assessment sequence and cognitive jobs | Opening judgment, `estimate`, applied contract defense |
| Distributed assessment locations | Intake, coverage teaching, artifact |
| Final applied work-product check | Quality contract defense |
| Role-sensitive treatment | Three role lenses |
| Professional work product | Quality-by-use contract |
| Same-page Knowledge Graph behavior | Use, requirement, evidence, issue relationships |
| Header Graph, Community, and Start actions | Present |
| Bottom connected-learning section | Present |
| Explicit bottom `#owos-course-community` anchor before navigation | Present |
| Drawer focus return and mobile behavior | Shared runtime |
| Module-specific FAQ location and disclosure behavior | Five clinic questions |
| Animation and teaching purpose | Sliders reveal threshold consequence |
| Reduced-motion equivalent | Values and verdict remain visible |
| Mobile transformation | Scrollable quality cells and stacked forms |
| Persistence and learner events | Browser artifact only |

## Instructor explanation plan

| Major component | What the learner sees | What the learner does | What to notice | Utility meaning | Debrief needed |
| --- | --- | --- | --- | --- | --- |
| Quality model | Thresholds by use | Change use and sliders | Same evidence changes verdict | Use defines requirements | Yes |
| Heat grid | Place and condition cells | Compare segments | Average hides red and unknown | Coverage is material | Yes |
| Closure loop | Five controlled stages | Step through | Recovery differs from decision correction | Issues close with retest | Yes |

## Written-first review

- Approximate conversational teaching words: more than 1,150.
- Worked utility example and marker: rainfall feed across three uses.
- Misconception addressed: one quality percentage is transferable.
- Boundary or non-example: disclaimer cannot make unsafe automation fit.
- Component debriefs: visible.
- What remains if every video and animation is removed: full lesson and threshold explanation.

## Visual pacing review

- Longest run of consecutive full prose blocks: two.
- Visual, interaction, worked example, or callout used to break each dense section: yes.
- Any uninterrupted prose exception and reason: none.
- Editorial illustration reading guide and learner conclusion, when used: not applicable.
- Dark-surface contrast plan: explicit shared rules.

## Explanatory graphic plan

| Teaching idea | Visual shape | Arsenal pattern | Learner conclusion | How the instructor explains it | Accessible and mobile treatment |
| --- | --- | --- | --- | --- | --- |
| Fitness by use | Threshold comparison | Quality-by-use model | Requirements change with consequence | Change use first | Keyboard ranges and live verdict |
| Coverage | Matrix | Heat grid | Do not average critical gaps away | Read by place and condition | Scrollable labeled cells |
| Issue operation | Loop | Cycle | Close cause and affected decisions | Step from signal to retest | Stacked on mobile |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| Must data be perfect? | Fitness can sound absolute | No, match requirements to use | Rainfall feed | Three-use comparison | No approval |
| Who sets thresholds? | Tool teams often do | Accountable owner with required advice | Flood alert | Role view | Local authority |
| Validation or observability? | Both test data | Observability adds changing condition and diagnosis | Gauge feed | Loop | No product claim |
| Is one score useful? | Dashboards favor totals | Only with visible gates and coverage | Heat grid | Matrix | No certification |
| Consumer found issue? | Monitoring can miss it | Treat report as evidence and correct monitoring | Late alert | Sequence | Protect identities |

## Recording script

| Field | Decision |
| --- | --- |
| Script path | Not planned |
| Intended recording length | Not applicable |
| Spoken opening | Written lesson |
| Utility example | Rainfall feed |
| Visual directions | On-page |
| Learner action and work product | Quality contract |
| Transition to next lesson | From quality failure to resilience |

## Diversity check

- Adjacent module reviewed: lineage reconstruction and resilience challenge.
- Course Experience Brief reviewed: yes.
- Lesson archetype differs from adjacent modules: yes.
- Signature mechanism is unique to this lesson: yes.
- Opening pattern intentionally different: same data, higher-consequence use.
- Dominant visual intentionally different: moving threshold model.
- Interaction pair intentionally different: sliders plus closure stepper.
- Quiz sequence intentionally different: judgment, estimate, defense.
- Work-product format intentionally different: threshold contract.
- Any justified repetition: shared shell controls only.
- Course-level distinctiveness result: batch distinct; later shells block.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | pending | | | Technical review |
| Learning design | conditional | Codex | 2026-07-23 | Automated gate targeted |
| Utility practice | pending | | | Stormwater practitioner review |
| Golden lesson benchmark, when applicable | not applicable | | | |
