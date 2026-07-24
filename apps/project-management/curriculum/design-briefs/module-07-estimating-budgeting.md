# Module Design Brief: Chapter 07 Estimating and budgeting

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-master-project-delivery-001` / `pm-07-estimating-budgeting` |
| Working title | Estimating and budgeting |
| Learner roles | Utility project staff, technical leads, operations, finance or commercial staff, sponsor |
| Competencies | Interpret estimate maturity, build a cost baseline, distinguish capital from O&M, and connect a CIP choice to funding and customer impact. |
| Controlled sources | GAO Cost Estimating and Assessment Guide; EPA WIFIA Program; PMI standards |
| Evidence boundary | Millpond is instructional. Current law, contract, adopted policy, approved technical records, funding conditions, and delegated authority govern live work. |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | Set an honest estimate range and funding path before placing the project into the capital plan. |
| What must the learner decide before teaching begins? | Complete the `estimate-range-decision` opening interaction and record the first judgment. |
| What professional consequence makes this matter? | False precision, omitted lifecycle cost, or an unaffordable funding stack becomes rate shock, deferred work, and loss of public trust. |
| What should the learner be able to do afterward? | Interpret estimate maturity, build a cost baseline, distinguish capital from O&M, and connect a CIP choice to funding and customer impact. |
| What usable work product will the learner create? | Estimate and funding basis note. |
| What evidence is required for completion? | Opening decision, two distributed checks, drafted work product, and deterministic final applied check. |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| cip-funding-gates | Relationship or change mechanism | `phase-gate` | Operate the existing cipplan component | A funded year is credible only when scope, estimate maturity, financing, and rate impact align. | Guided interpretation |
| rate-impact-curve | Relationship or change mechanism | `line-s-curve` | Operate the existing rateimpact component | Affordability belongs in project selection, not only in the final rate hearing. | Guided interpretation |
| Professional judgment | Reviewable decision record | Estimate and funding basis note builder | Draft and test the record | Implicit assumptions and missing evidence become visible | Final applied check |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | Capital funding portfolio room |
| Signature mechanism | Existing `estrange` opening mechanism plus chapter-specific professional record |
| Course visual language applied here | Field-delivery controls, working calculations, reviewable utility decisions |
| Intended learner feeling | Able to explain the mechanism and defend the decision without hiding uncertainty |
| Narrative architecture | Consequential decision, plain-language teaching, simulation, distributed checks, work product, evidence boundary |
| Mental model | Evidence and authority connect a technical result to an accountable decision |
| Purposeful interaction 1 | `estimate-range-decision` |
| Purposeful interaction 2 | Existing chapter simulations and the applied work-product check |
| Explanatory visuals, normally two to five | `phase-gate`; `line-s-curve` |
| Visual pacing plan and any prose exception | Existing sections alternate explanation, utility example, and interactive mechanisms. The retrofit adds no long prose run. |
| Original editorial illustration, when appropriate | Not added. Existing operational calculators and diagrams teach the mechanisms more directly. |
| Assessment sequence and cognitive jobs | `classification`, `true-false`, work-product check |
| Distributed assessment locations | Existing checks remain beside the concepts they assess; final check follows the professional record. |
| Final applied work-product check | Deterministic selection tied to `estimate-funding-note` |
| Role-sensitive treatment | Foundation, practitioner, and leader views appear near the opening |
| Professional work product | Estimate and funding basis note |
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
| cip-funding-gates | Existing interactive cipplan mechanism with reading guide | Operate and compare states | Move through prioritization, affordability, funding, authorization, and annual revalidation before treating a project as committed. | A funded year is credible only when scope, estimate maturity, financing, and rate impact align. | Visible learner conclusion |
| rate-impact-curve | Existing interactive rateimpact mechanism with reading guide | Operate and compare states | Change project cost, financing terms, and customer count, then watch the monthly bill consequence move. | Affordability belongs in project selection, not only in the final rate hearing. | Visible learner conclusion |
| Estimate and funding basis note | Structured draft and evidence standard | Write and test the record | Whether another reviewer can reconstruct the basis | Professional decisions require retained evidence | Immediate feedback |

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
| cip-funding-gates | phase-gate | `phase-gate` | A funded year is credible only when scope, estimate maturity, financing, and rate impact align. | The gates show that a capital plan is a sequence of decisions, not a wish list. | Text reading guide and conclusion remain visible; controls reflow on mobile |
| rate-impact-curve | line-s-curve | `line-s-curve` | Affordability belongs in project selection, not only in the final rate hearing. | The curve translates a capital decision into the customer scale leaders must explain. | Text reading guide and conclusion remain visible; controls reflow on mobile |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| Is contingency the same as padding? | The lesson can be misapplied without the boundary | No. Controlled contingency addresses identified and residual uncertainty with a stated basis and authority. Padding is hidden and cannot be governed. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| Why show an estimate range instead of one number? | The lesson can be misapplied without the boundary | The range communicates uncertainty appropriate to design maturity. A single number can imply precision the evidence does not support. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| Does a grant make a project free? | The lesson can be misapplied without the boundary | No. Grants may require match, compliance, administration, schedule, and long-term operating commitments. The utility still owns the asset consequences. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| What belongs in lifecycle cost? | The lesson can be misapplied without the boundary | Include capital delivery plus material operating, maintenance, renewal, financing, and disposal consequences over the decision horizon. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| How should rate impact be communicated? | The lesson can be misapplied without the boundary | State assumptions, customer classes, timing, financing, existing revenue needs, and the difference between this project's incremental effect and the total rate plan. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |

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

- Adjacent module reviewed: Chapters 06 and 08.
- Course Experience Brief reviewed: Yes.
- Lesson archetype differs from adjacent modules: Yes.
- Signature mechanism is unique to this lesson: Yes.
- Opening pattern intentionally different: estimate-range-decision.
- Dominant visual intentionally different: cip-funding-gates and rate-impact-curve.
- Interaction pair intentionally different: Existing chapter-specific simulations are preserved.
- Quiz sequence intentionally different: `classification`, `true-false`.
- Work-product format intentionally different: Estimate and funding basis note.
- Any justified repetition: Millpond case continuity and shared navigation controls are intentional.
- Course-level distinctiveness result: Passed, 21 lessons and 21 archetypes.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | conditional | Codex working review | 2026-07-23 | Official source boundary added; independent factual review remains. |
| Learning design | conditional | Codex working review | 2026-07-23 | Static and deterministic checks planned; human walkthrough remains. |
| Utility practice | pending | | | Qualified practitioner review remains. |
| Golden lesson benchmark, when applicable | not applicable | | | Evidence retrofit, not benchmark selection. |
