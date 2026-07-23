# Module 3 Design Brief: What an Agent Needs to Work

Status: approved curriculum direction, design draft for review

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-course-ai-agents-001`, Module 03 |
| Working title | What an Agent Needs to Work |
| Learner roles | Operators, maintenance leaders, utility managers, regulatory professionals, data leaders, capital-program managers, consultants, and emerging leaders |
| Competencies | Explain agent anatomy, diagnose readiness, set permissions, identify missing controls, and connect technical parts to accountable utility work |
| Controlled sources | Claims AG-002 through AG-012 plus approved utility scenarios |
| Evidence boundary | Functional teaching model, not a claim that every implementation has separate products for every part |

## Learning job

| Question | Answer |
| --- | --- |
| What situation opens the lesson? | A capable model is asked to prepare a lift-station maintenance packet but has incomplete records, no write permission, and no named decision owner. |
| What must the learner decide first? | Is the model failing because it is not intelligent enough, or because the surrounding agent system is incomplete? |
| Why does this matter? | Utilities can buy a capable model and still create an unreliable system when data, tools, permissions, evaluation, and accountability are missing. |
| What can the learner do afterward? | Open an agent, explain each functional part, diagnose a missing part, and define the minimum readiness for a bounded use case. |
| What work product is created? | Agent Dependency and Readiness Map, which becomes part of the capstone. |
| What evidence completes the lesson? | Anatomy lab completed, two failure repairs completed, knowledge checks passed, and readiness map saved. |

## Interactive anatomy experience

The main visual is an interactive cutaway of an agent system. It contains twelve functional parts:

1. Goal
2. Instructions
3. Model
4. Sources
5. Retrieval
6. Tools
7. Memory and state
8. Permissions
9. Evaluation
10. Guardrails
11. Human owner
12. Stop and escalation conditions

Selecting a part reveals four plain-English questions:

- What is this?
- Why does the agent need it?
- What can go wrong?
- What does this look like in a utility?

The learner can remove or weaken a part and run the same task again. The operating loop then exposes a visible consequence. Examples include lost context, unsupported evidence, blocked tool access, unauthorized action, endless retry, and an accountability gap.

The lab never displays hidden model reasoning. It displays the task plan, selected tool, source locator, permission decision, action status, evaluation result, retry count, handoff, and escalation status.

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| Agent anatomy | Parts of a working system | Interactive cutaway and layered stack | Open, remove, and restore parts | Dependencies and failure consequences | Matching |
| Data, retrieval, and sources | Connected evidence system | Provenance network | Change source quality and retrieval | Citation coverage, conflict, and confidence boundary | Multi-select |
| Tools and permissions | Controlled action | Permission ladder | Move from read to write | Required approval and consequence level | Scenario choice |
| Memory and state | Change over a task | Stateful timeline | Remove shared state before handoff | Lost context and duplicated work | Ordering |
| Evaluation and guardrails | Cause and effect | Defense layers and failure tree | Add checks and retry limits | Block, retry, escalate, or pass | Reflection |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Narrative architecture | Diagnostic repair lab |
| Mental model | A capable model surrounded by the functional system it needs to complete accountable work |
| Purposeful interaction 1 | Remove-and-repair agent anatomy lab |
| Purposeful interaction 2 | Tool-permission and consequence console |
| Additional interaction | Source and retrieval conflict test |
| Visual types | Cutaway, layered stack, provenance network, permission ladder, state timeline, failure tree |
| Quiz sequence | Matching, multi-select, ordering, scenario choice, reflection |
| Role-sensitive treatment | Operator sees task usefulness; manager sees authority; data leader sees sources and permissions; executive sees consequence and ownership |
| Professional work product | Agent Dependency and Readiness Map |
| Same-page Knowledge Graph behavior | Selecting an anatomy part highlights its related sources, tools, controls, roles, competencies, and failure modes in a side drawer |
| Animation purpose | Show information and control moving through the agent; reveal where a missing part interrupts the loop |
| Reduced-motion equivalent | Step controls and persistent state labels replace automatic movement |
| Mobile transformation | Anatomy becomes a selectable component list above a focused detail and test panel |
| Persistence and learner events | Selected repairs, knowledge checks, and readiness-map fields persist as draft evidence |

## Tooltip behavior

- Explain every technical term in the teaching sentence first.
- Apply a dotted term treatment to the first use and important later uses.
- Use one shared tooltip element for the page.
- Open tooltips on hover, keyboard focus, or touch.
- Keep definitions short, concrete, and readable without another technical term.
- Never place essential instructions only inside a tooltip.

## Diversity check

- Module 2 uses a step-through operating loop; Module 3 uses a diagnostic cutaway and repair lab.
- Module 3 does not reuse Module 2's cycle as its dominant visual.
- The primary learner action changes from sequencing events to removing, testing, and restoring system parts.
- The work product changes from an event trace to a readiness map.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Curriculum direction | approved | Hardeep Anand | 2026-07-22 | Anatomy, plain English, and tooltips explicitly requested. |
| Evidence and claims | in review | | | Additional retrieval and security sources required. |
| Learning design | proposed | | | Requires Hardeep design review before HTML. |
| Utility practice | pending | | | Practitioner scenario review required. |
