# Module Design Brief: Chapter 04 Scope and requirements

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-master-project-delivery-001` / `pm-04-scope-and-requirements` |
| Working title | Scope and requirements |
| Learner roles | Utility project staff, technical leads, operations, finance or commercial staff, sponsor |
| Competencies | Turn stakeholder needs into testable requirements and trace them through scope, work packages, and acceptance. |
| Controlled sources | NASA Systems Engineering Handbook; PMI standards; GAO Schedule Assessment Guide |
| Evidence boundary | Millpond is instructional. Current law, contract, adopted policy, approved technical records, funding conditions, and delegated authority govern live work. |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | Decide whether the stated requirement is testable enough to enter the Millpond scope baseline. |
| What must the learner decide before teaching begins? | Complete the `requirement-type-decision` opening interaction and record the first judgment. |
| What professional consequence makes this matter? | Ambiguous requirements become bid assumptions, change orders, failed acceptance, and assets that operations cannot use. |
| What should the learner be able to do afterward? | Turn stakeholder needs into testable requirements and trace them through scope, work packages, and acceptance. |
| What usable work product will the learner create? | Requirements traceability record. |
| What evidence is required for completion? | Opening decision, two distributed checks, drafted work product, and deterministic final applied check. |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| wbs-tree | Relationship or change mechanism | `network-diagram` | Operate the existing tree component | A WBS controls scope by making the whole deliverable visible and assignable. | Guided interpretation |
| traceability-rollup | Relationship or change mechanism | `phase-gate` | Operate the existing rollup component | A requirement is controlled only when its acceptance evidence can be traced. | Guided interpretation |
| Professional judgment | Reviewable decision record | Requirements traceability record builder | Draft and test the record | Implicit assumptions and missing evidence become visible | Final applied check |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | Requirement traceability studio |
| Signature mechanism | Existing `classify` opening mechanism plus chapter-specific professional record |
| Course visual language applied here | Field-delivery controls, working calculations, reviewable utility decisions |
| Intended learner feeling | Able to explain the mechanism and defend the decision without hiding uncertainty |
| Narrative architecture | Consequential decision, plain-language teaching, simulation, distributed checks, work product, evidence boundary |
| Mental model | Evidence and authority connect a technical result to an accountable decision |
| Purposeful interaction 1 | `requirement-type-decision` |
| Purposeful interaction 2 | Existing chapter simulations and the applied work-product check |
| Explanatory visuals, normally two to five | `network-diagram`; `phase-gate` |
| Visual pacing plan and any prose exception | Existing sections alternate explanation, utility example, and interactive mechanisms. The retrofit adds no long prose run. |
| Original editorial illustration, when appropriate | Not added. Existing operational calculators and diagrams teach the mechanisms more directly. |
| Assessment sequence and cognitive jobs | `classification`, `true-false`, work-product check |
| Distributed assessment locations | Existing checks remain beside the concepts they assess; final check follows the professional record. |
| Final applied work-product check | Deterministic selection tied to `requirements-trace-record` |
| Role-sensitive treatment | Foundation, practitioner, and leader views appear near the opening |
| Professional work product | Requirements traceability record |
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
| wbs-tree | Existing interactive tree mechanism with reading guide | Operate and compare states | Read from the project deliverable down to work packages. Each branch should describe complete work, not a department or an activity list without an output. | A WBS controls scope by making the whole deliverable visible and assignable. | Visible learner conclusion |
| traceability-rollup | Existing interactive rollup mechanism with reading guide | Operate and compare states | Follow one requirement from need to design, work package, test, and acceptance evidence. | A requirement is controlled only when its acceptance evidence can be traced. | Visible learner conclusion |
| Requirements traceability record | Structured draft and evidence standard | Write and test the record | Whether another reviewer can reconstruct the basis | Professional decisions require retained evidence | Immediate feedback |

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
| wbs-tree | network-diagram | `network-diagram` | A WBS controls scope by making the whole deliverable visible and assignable. | The tree shows how scope becomes manageable work without losing the parent deliverable. | Text reading guide and conclusion remain visible; controls reflow on mobile |
| traceability-rollup | phase-gate | `phase-gate` | A requirement is controlled only when its acceptance evidence can be traced. | The rollup reveals where a requirement can be lost between conversation and handover. | Text reading guide and conclusion remain visible; controls reflow on mobile |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| What makes a requirement testable? | The lesson can be misapplied without the boundary | It states a measurable condition, operating context, acceptance method, and responsible source without relying on words such as adequate or user-friendly. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| Is the WBS the same as the schedule? | The lesson can be misapplied without the boundary | No. The WBS defines all deliverable-oriented scope. The schedule arranges the activities needed to produce that scope in time. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| Can operations add a requirement during construction? | The lesson can be misapplied without the boundary | They can identify a need, but the team must evaluate and authorize it through change control before treating it as committed scope. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| How much traceability is enough? | The lesson can be misapplied without the boundary | Use enough to connect material needs to design, procurement, construction, testing, and acceptance. The depth should follow consequence and complexity. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |
| Why record the source of a requirement? | The lesson can be misapplied without the boundary | The source shows who can clarify intent, whether the requirement is mandatory, and which evidence has authority when interpretations conflict. | Millpond or utility delivery context | Direct comparison or worked interpretation | Controlled local evidence governs |

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

- Adjacent module reviewed: Chapters 03 and 05.
- Course Experience Brief reviewed: Yes.
- Lesson archetype differs from adjacent modules: Yes.
- Signature mechanism is unique to this lesson: Yes.
- Opening pattern intentionally different: requirement-type-decision.
- Dominant visual intentionally different: wbs-tree and traceability-rollup.
- Interaction pair intentionally different: Existing chapter-specific simulations are preserved.
- Quiz sequence intentionally different: `classification`, `true-false`.
- Work-product format intentionally different: Requirements traceability record.
- Any justified repetition: Millpond case continuity and shared navigation controls are intentional.
- Course-level distinctiveness result: Passed, 21 lessons and 21 archetypes.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | conditional | Codex working review | 2026-07-23 | Official source boundary added; independent factual review remains. |
| Learning design | conditional | Codex working review | 2026-07-23 | Static and deterministic checks planned; human walkthrough remains. |
| Utility practice | pending | | | Qualified practitioner review remains. |
| Golden lesson benchmark, when applicable | not applicable | | | Evidence retrofit, not benchmark selection. |
