# Module 4 Golden-Lesson Design Brief: The Handoff

Status: approved for golden-lesson production by Hardeep Anand on 2026-07-22

## Consequential situation

A stormwater program must prepare an evidence packet for a pending review. Inspection records, geographic information, maintenance activity, rainfall data, photographs, and prior correspondence disagree. The deadline is close, but speed does not remove the need for provenance and human authority.

## First learner decision

Should one general agent handle the entire task, should a fixed workflow route it, or should specialized agents coordinate under an accountable human owner?

## Specialized roles

| Role | Plain-English job | Boundary |
| --- | --- | --- |
| Orchestrator | Routes work, tracks status, and enforces handoff requirements | Does not approve regulatory conclusions |
| Planner | Breaks the goal into reviewable tasks | Does not invent missing evidence |
| Source librarian | Finds approved records and preserves locators | Does not decide which conflict is acceptable |
| Analyst | Compares records and identifies conflicts | Does not certify the result |
| Critic | Tests coverage, consistency, and unsupported claims | Does not become the accountable owner |
| Human approver | Accepts, rejects, or returns the packet | Retains named authority and accountability |

## Learner experience

1. Choose an architecture for the task.
2. Play the handoff across the six roles.
3. Inspect the live event stream and shared-state ledger.
4. Open the provenance network for every material statement.
5. Introduce one broken handoff: missing locator, lost context, unauthorized action, conflicting record, or no approver.
6. Repair the handoff contract.
7. Set read, recommend, draft, write, and execute permissions.
8. Run critic and deterministic checks.
9. Decide whether the packet is ready for human review.
10. Save the orchestration and handoff contract.

## Design fingerprint

| Element | Design |
| --- | --- |
| Narrative | Multi-voice orchestration room |
| Mental model | Work plus context plus evidence plus authority must cross every handoff |
| Visuals | Handoff packet anatomy, failure-propagation cause map, swimlane, provenance network, shared-state ledger, status heat grid, permission ladder, evidence funnel |
| Interaction 1 | Orchestration playback with Back, Step, Play, Pause, and Reset |
| Interaction 2 | Broken-handoff diagnosis and repair |
| Interaction 3 | Permission and approval console |
| Quiz mix | Multi-select, ordering, multiple choice, reflection |
| Work product | Orchestration and Handoff Contract |
| Capstone | Name roles, shared state, handoffs, evidence, and human approval |
| Graph | Side drawer follows the active agent, source, event, control, role, and competency |
| Mobile | Role rail becomes horizontal; active work, ledger, and evidence become tabs |

## Golden-lesson capabilities

- Plain-English teaching and tooltips
- Consequential utility scenario
- Multiple professional viewpoints
- Purposeful instructional animation
- Stateful simulation and visible progress
- Deterministic checks with explanatory feedback
- Original utility visuals
- Professional work-product builder
- Same-page Knowledge Graph
- Keyboard, touch, mobile, contrast, and reduced-motion behavior
- Completion based on evidence rather than scrolling
- Source map and explicit instructional boundary

## Completion evidence

Architecture decision, full handoff playback, one repaired failure, permission plan, critic check, knowledge check, and saved handoff contract.

## Production review still required

Hardeep review of the working learner-facing lesson, practitioner review of the stormwater scenario, and separate approval before this lesson becomes the production benchmark for the remaining modules.

## Visual selection record

| Teaching idea | Shape | Selected visual | Learner action | Check type |
| --- | --- | --- | --- | --- |
| Work moving among specialists | Process and responsibility | Interactive swimlane | Step, play, pause, and inspect each handoff | Put in order |
| Shared context and evidence | Relationship and hidden dependency | Provenance network | Select a claim and trace its source, transformation, reviewer, and authority | Multi-select |
| Handoff health | Status across roles | Status heat grid | Compare complete, missing, stale, and unauthorized handoffs | Classification |
| Action authority | Position and consequence | Permission ladder | Set read, recommend, draft, write, and execute limits | Multiple choice |
| Many records becoming a review packet | Filtering and narrowing | Evidence funnel | Inspect which records survive evidence gates | Reflection |
| Repairing a broken handoff | Cause and effect | Handoff repair laboratory | Diagnose a failure, select a repair, and rerun the transfer | Deterministic repair check |
| What must cross a handoff | Parts and relationship | Layered handoff packet anatomy | Trace six required layers from the current role to the receiving role | Explain the packet in plain English |
| Why one missing source travels | Cause and effect | Interactive failure-propagation chain | Compare a complete packet with a missing locator and follow the downstream effect | Explain the repair point |

The handoff packet, cause chain, swimlane, provenance network, heat grid, permission ladder, and evidence funnel are deliberately different visual shapes. Motion teaches sequence and the effect of missing context. Reduced-motion mode presents the same states through direct stepping and visible text changes.
