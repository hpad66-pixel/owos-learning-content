# Module Design Brief: Chapter 05 Scheduling and the Critical Path

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-master-project-delivery-001` / `pm-05-scheduling-critical-path` |
| Working title | Scheduling and the Critical Path |
| Learner roles | Utility project staff, technical leads, operations, finance or commercial staff, sponsor |
| Competencies | Build a logic-based schedule, calculate critical path and float, and interpret a cost-loaded S-curve. |
| Controlled sources | GAO Schedule Assessment Guide; PMI standards; GAO Cost Estimating and Assessment Guide |
| Evidence boundary | Millpond is instructional. Current law, contract, adopted policy, approved technical records, funding conditions, and delegated authority govern live work. |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | Identify the activity chain that actually controls the Millpond finish date before promising recovery. |
| What must the learner decide before teaching begins? | Complete the `schedule-logic-read` opening interaction and record the first judgment. |
| What professional consequence makes this matter? | Accelerating noncritical work consumes money without moving the finish and can create a new bottleneck elsewhere. |
| What should the learner be able to do afterward? | Build a logic-based schedule, calculate critical path and float, and interpret a cost-loaded S-curve. |
| What usable work product will the learner create? | Schedule basis memo. |
| What evidence is required for completion? | Opening decision, two distributed checks, drafted work product, and deterministic final applied check. |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| editable-gantt-network | Relationship or change mechanism | `network-diagram` | Operate the existing ganttedit component | A schedule is credible because of its logic, not because the bars are neatly drawn. | Guided interpretation |
| cost-loaded-s-curve | Relationship or change mechanism | `line-s-curve` | Operate the existing scurve component | A cost-loaded schedule makes the timing of financial exposure visible. | Guided interpretation |
| Professional judgment | Reviewable decision record | Schedule basis memo builder | Draft and test the record | Implicit assumptions and missing evidence become visible | Final applied check |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | Critical-path control room |
| Signature mechanism | Existing `gantt` opening mechanism plus chapter-specific professional record |
| Course visual language applied here | Field-delivery controls, working calculations, reviewable utility decisions |
| Intended learner feeling | Able to explain the mechanism and defend the decision without hiding uncertainty |
| Narrative architecture | Consequential decision, plain-language teaching, simulation, distributed checks, work product, evidence boundary |
| Mental model | Evidence and authority connect a technical result to an accountable decision |
| Purposeful interaction 1 | `schedule-logic-read` |
| Purposeful interaction 2 | Existing chapter simulations and the applied work-product check |
| Explanatory visuals, normally two to five | `network-diagram`; `line-s-curve` |
| Visual pacing plan and any prose exception | Existing sections alternate explanation, utility example, and interactive mechanisms. The retrofit adds no long prose run. |
| Original editorial illustration, when appropriate | Not added. Existing operational calculators and diagrams teach the mechanisms more directly. |
| Assessment sequence and cognitive jobs | `classification`, `numeric-estimate`, work-product check |
| Distributed assessment locations | Existing checks remain beside the concepts they assess; final check follows the professional record. |
| Final applied work-product check | Deterministic selection tied to `schedule-basis-memo` |
| Role-sensitive treatment | Foundation, practitioner, and leader views appear near the opening |
| Professional work product | Schedule basis memo |
| Same-page Knowledge Graph behavior | Accessible right drawer with concept, source, role, competency, and relationship context |
| Header Graph, Community, and Start actions | Compact controls in the existing course navigation |
| Bottom connected-learning section | Chapter-specific prompt immediately before navigation |
| Explicit bottom `#owos-course-community` anchor before navigation | Implemented |
| Drawer focus return and mobile behavior | Close and Escape return focus; drawer becomes full width on small screens |
| Module-specific FAQ location and disclosure behavior | Five disclosures before the evidence boundary |
| Animation and teaching purpose | Existing components reveal dependency, change, calculation, or consequence |
| Reduced-motion equivalent | Values, text conclusions, and controls remain available without transitions |
| Mobile transformation | Role views stack; drawers and form controls use full width |
| Persistence and learner events | Work product remains local to the page; completion stays disabled until draft and final standard are present |

## Instructor explanation plan

| Major component | What the learner sees | What the learner does | What to notice | Utility meaning | Debrief needed |
| --- | --- | --- | --- | --- | --- |
| editable-gantt-network | Existing interactive ganttedit mechanism with reading guide | Operate and compare states | Trace every predecessor before changing a duration. Watch whether the controlling chain and finish date move together. | A schedule is credible because of its logic, not because the bars are neatly drawn. | Visible learner conclusion |
| cost-loaded-s-curve | Existing interactive scurve mechanism with reading guide | Operate and compare states | Read planned cumulative spending over time and compare the steepest section with the period of greatest field demand. | A cost-loaded schedule makes the timing of financial exposure visible. | Visible learner conclusion |
| Schedule basis memo | Structured draft and evidence standard | Write and test the record | Whether another reviewer can reconstruct the basis | Professional decisions require retained evidence | Immediate feedback |

## Written-first review

- Approximate conversational teaching words: Existing full lesson exceeds the current minimum floor.
- Worked utility example and marker: Millpond case teaching is retained throughout.
- Misconception addressed: A tool output or preferred answer is not enough without assumptions, authority, and evidence.
- Boundary or non-example: The instructional model does not replace current local controls.
- Component debriefs: Existing component cues plus governed reading guides and learner conclusions.
- What remains if every video and animation is removed: Full prose teaching, calculations, examples, questions, work product, FAQ, and evidence boundary.

## Visual pacing review

- Longest run of consecutive full prose blocks: Existing lesson rhythm generally limits the run to two.
- Visual, interaction, worked example, or callout used to break each dense section: Existing chapter-specific academy components.
- Any uninterrupted prose exception and reason: None introduced.
- Editorial illustration reading guide and learner conclusion, when used: Not applicable.
- Dark-surface contrast plan: Drawer header explicitly uses white text on dark blue.

## Explanatory graphic plan

| Teaching idea | Visual shape | Arsenal pattern | Learner conclusion | How the instructor explains it | Accessible and mobile treatment |
| --- | --- | --- | --- | --- | --- |
| editable-gantt-network | network-diagram | `network-diagram` | A schedule is credible because of its logic, not because the bars are neatly drawn. | The editable Gantt exposes the logic behind bars that otherwise look like a calendar picture. | Text reading guide and conclusion remain visible; controls reflow on mobile |
| cost-loaded-s-curve | line-s-curve | `line-s-curve` | A cost-loaded schedule makes the timing of financial exposure visible. | The curve connects schedule timing to cash flow and management attention. | Text reading guide and conclusion remain visible; controls reflow on mobile |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| Is every zero-float activity equally important? | The lesson can be misapplied without the boundary | Every critical activity can affect the finish, but risk also depends on uncertainty, remaining duration, interfaces, and the credibility of the logic. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| Can the critical path change? | The lesson can be misapplied without the boundary | Yes. Progress, delays, resequencing, and duration changes can move the controlling path. Recalculate it after meaningful updates. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| Why can shortening a task fail to shorten the project? | The lesson can be misapplied without the boundary | The task may have float or another parallel path may still control the finish. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| What does lag represent? | The lesson can be misapplied without the boundary | Lag is intentional waiting between linked activities, such as cure time. It should be explicit and justified rather than hidden inside a task duration. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| Is an S-curve proof that the schedule is realistic? | The lesson can be misapplied without the boundary | No. It visualizes planned or actual cumulative value, but it inherits every weakness in the underlying scope, logic, durations, and cost loading. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |

## Recording script

| Field | Decision |
| --- | --- |
| Script path | None. Written-first module. |
| Intended recording length | Not applicable |
| Spoken opening | Not applicable |
| Utility example | Complete in the written lesson |
| Visual directions | Complete in reading guides and component cues |
| Learner action and work product | Complete in the written lesson |
| Transition to next lesson | Existing bottom navigation |

## Diversity check

- Adjacent module reviewed: Chapters 04 and 06.
- Course Experience Brief reviewed: Yes.
- Lesson archetype differs from adjacent modules: Yes.
- Signature mechanism is unique to this lesson: Yes.
- Opening pattern intentionally different: schedule-logic-read.
- Dominant visual intentionally different: editable-gantt-network and cost-loaded-s-curve.
- Interaction pair intentionally different: Existing chapter-specific simulations are preserved.
- Quiz sequence intentionally different: `classification`, `numeric-estimate`.
- Work-product format intentionally different: Schedule basis memo.
- Any justified repetition: Millpond case continuity and shared navigation controls are intentional.
- Course-level distinctiveness result: Passed, 21 lessons and 21 archetypes.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | conditional | Codex working review | 2026-07-23 | Official source boundary added; independent factual review remains. |
| Learning design | conditional | Codex working review | 2026-07-23 | Static and deterministic checks planned; human walkthrough remains. |
| Utility practice | pending | | | Qualified practitioner review remains. |
| Golden lesson benchmark, when applicable | not applicable | | | Evidence retrofit, not benchmark selection. |
