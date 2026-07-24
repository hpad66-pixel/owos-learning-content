# Module Design Brief: Chapter 06 Advanced scheduling

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-master-project-delivery-001` / `pm-06-advanced-scheduling` |
| Working title | Advanced scheduling |
| Learner roles | Utility project staff, technical leads, operations, finance or commercial staff, sponsor |
| Competencies | Use PERT, resource leveling, compression choices, buffers, and simulation to make a risk-aware schedule commitment. |
| Controlled sources | GAO Schedule Assessment Guide; NASA Systems Engineering Handbook; PMI standards |
| Evidence boundary | Millpond is instructional. Current law, contract, adopted policy, approved technical records, funding conditions, and delegated authority govern live work. |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | Choose a commitment date after testing duration uncertainty, resource limits, and schedule risk. |
| What must the learner decide before teaching begins? | Complete the `duration-range-decision` opening interaction and record the first judgment. |
| What professional consequence makes this matter? | A single deterministic date can hide resource impossibility and expose the utility to missed outages, funding deadlines, and public commitments. |
| What should the learner be able to do afterward? | Use PERT, resource leveling, compression choices, buffers, and simulation to make a risk-aware schedule commitment. |
| What usable work product will the learner create? | Schedule risk commitment note. |
| What evidence is required for completion? | Opening decision, two distributed checks, drafted work product, and deterministic final applied check. |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| resource-load-grid | Relationship or change mechanism | `heat-grid` | Operate the existing reslevel component | A schedule that requires unavailable crews is not an executable plan. | Guided interpretation |
| schedule-risk-distribution | Relationship or change mechanism | `line-s-curve` | Operate the existing montecarlo component | A commitment date should match the consequence of being late and the evidence in the model. | Guided interpretation |
| Professional judgment | Reviewable decision record | Schedule risk commitment note builder | Draft and test the record | Implicit assumptions and missing evidence become visible | Final applied check |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | Schedule uncertainty laboratory |
| Signature mechanism | Existing `pert` opening mechanism plus chapter-specific professional record |
| Course visual language applied here | Field-delivery controls, working calculations, reviewable utility decisions |
| Intended learner feeling | Able to explain the mechanism and defend the decision without hiding uncertainty |
| Narrative architecture | Consequential decision, plain-language teaching, simulation, distributed checks, work product, evidence boundary |
| Mental model | Evidence and authority connect a technical result to an accountable decision |
| Purposeful interaction 1 | `duration-range-decision` |
| Purposeful interaction 2 | Existing chapter simulations and the applied work-product check |
| Explanatory visuals, normally two to five | `heat-grid`; `line-s-curve` |
| Visual pacing plan and any prose exception | Existing sections alternate explanation, utility example, and interactive mechanisms. The retrofit adds no long prose run. |
| Original editorial illustration, when appropriate | Not added. Existing operational calculators and diagrams teach the mechanisms more directly. |
| Assessment sequence and cognitive jobs | `classification`, `true-false`, work-product check |
| Distributed assessment locations | Existing checks remain beside the concepts they assess; final check follows the professional record. |
| Final applied work-product check | Deterministic selection tied to `schedule-risk-note` |
| Role-sensitive treatment | Foundation, practitioner, and leader views appear near the opening |
| Professional work product | Schedule risk commitment note |
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
| resource-load-grid | Existing interactive reslevel mechanism with reading guide | Operate and compare states | Compare weekly demand with the actual resource cap before and after leveling. | A schedule that requires unavailable crews is not an executable plan. | Visible learner conclusion |
| schedule-risk-distribution | Existing interactive montecarlo mechanism with reading guide | Operate and compare states | Run enough trials to see the difference between the deterministic date, the median, and the safer P80 commitment. | A commitment date should match the consequence of being late and the evidence in the model. | Visible learner conclusion |
| Schedule risk commitment note | Structured draft and evidence standard | Write and test the record | Whether another reviewer can reconstruct the basis | Professional decisions require retained evidence | Immediate feedback |

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
| resource-load-grid | heat-grid | `heat-grid` | A schedule that requires unavailable crews is not an executable plan. | The grid makes over-allocation visible instead of leaving it buried in activity assignments. | Text reading guide and conclusion remain visible; controls reflow on mobile |
| schedule-risk-distribution | line-s-curve | `line-s-curve` | A commitment date should match the consequence of being late and the evidence in the model. | The distribution shows uncertainty as a range of possible finishes instead of a false single date. | Text reading guide and conclusion remain visible; controls reflow on mobile |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| Is P80 a guarantee? | The lesson can be misapplied without the boundary | No. It is a modeled percentile based on the ranges, dependencies, and assumptions supplied. Poor inputs can still produce a misleading result. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| What is the difference between leveling and smoothing? | The lesson can be misapplied without the boundary | Leveling may extend the finish to respect resource limits. Smoothing rearranges work within available float so the finish does not move. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| When should I crash a schedule? | The lesson can be misapplied without the boundary | Only after confirming the target activity is on the controlling path and that added resources can shorten it without unacceptable cost, safety, or quality consequences. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| Why is fast-tracking risky? | The lesson can be misapplied without the boundary | It overlaps work that was planned sequentially, so downstream work may start before upstream information is stable and may need rework. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| Who chooses the commitment percentile? | The lesson can be misapplied without the boundary | The accountable decision maker should choose it with project, operational, financial, and risk advice based on the consequence of missing the date. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |

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

- Adjacent module reviewed: Chapters 05 and 07.
- Course Experience Brief reviewed: Yes.
- Lesson archetype differs from adjacent modules: Yes.
- Signature mechanism is unique to this lesson: Yes.
- Opening pattern intentionally different: duration-range-decision.
- Dominant visual intentionally different: resource-load-grid and schedule-risk-distribution.
- Interaction pair intentionally different: Existing chapter-specific simulations are preserved.
- Quiz sequence intentionally different: `classification`, `true-false`.
- Work-product format intentionally different: Schedule risk commitment note.
- Any justified repetition: Millpond case continuity and shared navigation controls are intentional.
- Course-level distinctiveness result: Passed, 21 lessons and 21 archetypes.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | conditional | Codex working review | 2026-07-23 | Official source boundary added; independent factual review remains. |
| Learning design | conditional | Codex working review | 2026-07-23 | Static and deterministic checks planned; human walkthrough remains. |
| Utility practice | pending | | | Qualified practitioner review remains. |
| Golden lesson benchmark, when applicable | not applicable | | | Evidence retrofit, not benchmark selection. |
