# Module Design Brief: Chapter 08 Earned Value and forecasting

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-master-project-delivery-001` / `pm-08-earned-value` |
| Working title | Earned Value and forecasting |
| Learner roles | Utility project staff, technical leads, operations, finance or commercial staff, sponsor |
| Competencies | Interpret PV, EV, AC, CPI, SPI, EAC, and TCPI as a connected performance story. |
| Controlled sources | DOE EVMS Gold Card; GAO Cost Estimating and Assessment Guide; PMI standards |
| Evidence boundary | Millpond is instructional. Current law, contract, adopted policy, approved technical records, funding conditions, and delegated authority govern live work. |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | Forecast Millpond's likely finish cost from actual performance instead of reporting only percent spent. |
| What must the learner decide before teaching begins? | Complete the `evm-status-decision` opening interaction and record the first judgment. |
| What professional consequence makes this matter? | Late or optimistic forecasting removes the time leaders need to correct performance, secure authority, or communicate a credible variance. |
| What should the learner be able to do afterward? | Interpret PV, EV, AC, CPI, SPI, EAC, and TCPI as a connected performance story. |
| What usable work product will the learner create? | EVM forecast note. |
| What evidence is required for completion? | Opening decision, two distributed checks, drafted work product, and deterministic final applied check. |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| evm-performance-curve | Relationship or change mechanism | `line-s-curve` | Operate the existing evm component | A forecast is useful when the underlying progress measurement is trustworthy and the response is explicit. | Guided interpretation |
| evm-signal-table | Relationship or change mechanism | `comparison-table` | Operate the existing classify component | CPI, SPI, EAC, and TCPI answer different management questions and should not be substituted for one another. | Guided interpretation |
| Professional judgment | Reviewable decision record | EVM forecast note builder | Draft and test the record | Implicit assumptions and missing evidence become visible | Final applied check |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | Performance forecasting lab |
| Signature mechanism | Existing `evm` opening mechanism plus chapter-specific professional record |
| Course visual language applied here | Field-delivery controls, working calculations, reviewable utility decisions |
| Intended learner feeling | Able to explain the mechanism and defend the decision without hiding uncertainty |
| Narrative architecture | Consequential decision, plain-language teaching, simulation, distributed checks, work product, evidence boundary |
| Mental model | Evidence and authority connect a technical result to an accountable decision |
| Purposeful interaction 1 | `evm-status-decision` |
| Purposeful interaction 2 | Existing chapter simulations and the applied work-product check |
| Explanatory visuals, normally two to five | `line-s-curve`; `comparison-table` |
| Visual pacing plan and any prose exception | Existing sections alternate explanation, utility example, and interactive mechanisms. The retrofit adds no long prose run. |
| Original editorial illustration, when appropriate | Not added. Existing operational calculators and diagrams teach the mechanisms more directly. |
| Assessment sequence and cognitive jobs | `true-false`, `multiple-choice`, work-product check |
| Distributed assessment locations | Existing checks remain beside the concepts they assess; final check follows the professional record. |
| Final applied work-product check | Deterministic selection tied to `evm-forecast-note` |
| Role-sensitive treatment | Foundation, practitioner, and leader views appear near the opening |
| Professional work product | EVM forecast note |
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
| evm-performance-curve | Existing interactive evm mechanism with reading guide | Operate and compare states | Compare planned value, earned value, and actual cost at the same data date before reading CPI, SPI, and EAC. | A forecast is useful when the underlying progress measurement is trustworthy and the response is explicit. | Visible learner conclusion |
| evm-signal-table | Existing interactive classify mechanism with reading guide | Operate and compare states | Sort each signal by whether it describes cost efficiency, schedule performance, or required future efficiency. | CPI, SPI, EAC, and TCPI answer different management questions and should not be substituted for one another. | Visible learner conclusion |
| EVM forecast note | Structured draft and evidence standard | Write and test the record | Whether another reviewer can reconstruct the basis | Professional decisions require retained evidence | Immediate feedback |

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
| evm-performance-curve | line-s-curve | `line-s-curve` | A forecast is useful when the underlying progress measurement is trustworthy and the response is explicit. | The curve separates work accomplished from money spent, which ordinary budget reporting cannot do. | Text reading guide and conclusion remain visible; controls reflow on mobile |
| evm-signal-table | comparison-table | `comparison-table` | CPI, SPI, EAC, and TCPI answer different management questions and should not be substituted for one another. | The comparison prevents the EVM abbreviations from becoming disconnected formulas. | Text reading guide and conclusion remain visible; controls reflow on mobile |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| Can EVM be used on every project? | The lesson can be misapplied without the boundary | The ideas can help widely, but formal EVM requires a credible scope baseline, schedule, budget, progress rules, and disciplined updates. Scale the method to the decision. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| Why is percent spent not percent complete? | The lesson can be misapplied without the boundary | Spending measures cost outflow. Earned value measures budgeted value for completed work. They can differ substantially. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| What if CPI and SPI disagree? | The lesson can be misapplied without the boundary | That is normal. One describes cost efficiency and the other schedule performance. Explain both and trace the causes. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| Which EAC formula should I use? | The lesson can be misapplied without the boundary | Use the method that matches the expected future conditions, document the rationale, and compare it with an independent bottom-up forecast when consequence is high. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| Does a good CPI prove the project is healthy? | The lesson can be misapplied without the boundary | No. Progress measurement may be weak, critical work may be late, quality may be failing, or future risk may be unpriced. EVM is one evidence stream. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |

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

- Adjacent module reviewed: Chapters 07 and 09.
- Course Experience Brief reviewed: Yes.
- Lesson archetype differs from adjacent modules: Yes.
- Signature mechanism is unique to this lesson: Yes.
- Opening pattern intentionally different: evm-status-decision.
- Dominant visual intentionally different: evm-performance-curve and evm-signal-table.
- Interaction pair intentionally different: Existing chapter-specific simulations are preserved.
- Quiz sequence intentionally different: `true-false`, `multiple-choice`.
- Work-product format intentionally different: EVM forecast note.
- Any justified repetition: Millpond case continuity and shared navigation controls are intentional.
- Course-level distinctiveness result: Passed, 21 lessons and 21 archetypes.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | conditional | Codex working review | 2026-07-23 | Official source boundary added; independent factual review remains. |
| Learning design | conditional | Codex working review | 2026-07-23 | Static and deterministic checks planned; human walkthrough remains. |
| Utility practice | pending | | | Qualified practitioner review remains. |
| Golden lesson benchmark, when applicable | not applicable | | | Evidence retrofit, not benchmark selection. |
