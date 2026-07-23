# Meet the Agent: How AI Gets Work Done in Water Utilities

Status: proposed blueprint for Hardeep's review

Estimated learning time: 2 hours 15 minutes plus capstone refinement
Level: foundation with practitioner and leader lenses

## Course promise

See an agent work from goal to action, understand the parts and handoffs, and design one bounded utility application that keeps people in control.

## Intended learners

- Utility managers
- Operators and maintenance leaders
- Water-quality and regulatory professionals
- Stormwater and wastewater professionals
- Data and technology leaders
- Consultants and vendors serving utilities
- Emerging utility leaders

## Learning outcomes

By the end of the course, learners will be able to:

1. Distinguish a model, chatbot, retrieval-supported system, deterministic workflow, agent, and multi-agent system.
2. Explain the goal, plan, tool, action, observation, evaluation, adjustment, and stop or escalation loop.
3. Identify common agent roles without treating one vendor's taxonomy as universal.
4. Explain how orchestration, handoffs, shared state, and streaming events affect reliability.
5. Set permissions, guardrails, evaluation, and human checkpoints according to consequence.
6. Recognize utility work that may suit an agent and work that should remain deterministic or human-controlled.
7. Produce a bounded Utility Agent Canvas with purpose, sources, tools, actions, owner, evidence, and escalation.

## How this course teaches a novice

Every module follows a consistent learning rhythm without repeating the same visual design:

1. Start with a recognizable utility situation.
2. Ask the learner to make an initial decision.
3. Explain the idea in ordinary language.
4. Let the learner open, move, compare, or repair the system.
5. Show what changes because of the learner's action.
6. Connect the result to the learner's role.
7. Add one part to the capstone.
8. End with a plain-English recap and the next practical action.

Technical terms are never left unexplained. The first use includes the full term and a plain-English definition. The rendered course uses one accessible tooltip system per page. A tooltip supports the explanation but never replaces it.

## The twelve learning dimensions

| Dimension | What the learner should understand | How the course teaches it |
| --- | --- | --- |
| Recognition | What is and is not an agent | Scenario classifier comparing chat, retrieval, workflows, agents, and multi-agent systems |
| Mechanism | How an agent moves from a goal to a result | Animated operating loop and event-stream inspector |
| Agent anatomy | What parts an agent needs and why | Interactive cutaway with removable parts and failure consequences |
| Utility relevance | Where the idea touches real utility work | Role-filtered water, wastewater, and stormwater situations |
| Agenticness and autonomy | How delegated control varies | Autonomy spectrum combined with a consequence matrix |
| Data and knowledge readiness | Why the agent depends on governed information | Diagnostic lab with stale, missing, conflicting, and unattributed evidence |
| Orchestration and handoffs | How specialized agents and people coordinate | Multi-agent handoff simulation and shared-state repair |
| Guardrails and human authority | What the system may do and who remains accountable | Permission console and approval design exercise |
| Failure literacy | How agents fail and how people detect it | Safe failure laboratory with observable symptoms and recovery choices |
| Value and feasibility | When an agent earns its added cost and complexity | Simplest-solution recommender and value-risk comparison |
| Workforce implications | How tasks, skills, and responsibilities change | Role perspectives and responsibility mapping |
| Personal application | How the learner applies the course to one real problem | Progressive Utility Agent Canvas and pilot brief |

## Agent anatomy, explained simply

The anatomy experience presents an agent as a small working system:

| Part | Plain-English explanation | What the learner can test |
| --- | --- | --- |
| Goal | The result the user wants | Make the goal vague or measurable and compare the behavior |
| Instructions | The operating rules and expected method | Remove an edge-case instruction and observe the failure |
| Model | The part that interprets context and chooses among possible next steps | Compare a simple and a more capable model on the same bounded task |
| Sources | The approved information the agent can use | Introduce stale or conflicting evidence |
| Retrieval | The process that finds relevant information for the current task | Change the retrieved records and inspect the answer's support |
| Tools | The approved functions and systems the agent can use | Enable or disable read, search, calculate, draft, and write tools |
| Memory and state | What the system retains about the task and its progress | Remove shared state and watch a handoff lose context |
| Permissions | The actions the current identity is allowed to take | Move from read to recommend to write and see approval requirements change |
| Evaluation | The checks used to judge the result | Add a critic, rule check, or source-coverage test |
| Guardrails | Boundaries that block, pause, redirect, or escalate unsafe behavior | Trigger a privacy, relevance, authorization, or consequence boundary |
| Human owner | The named person accountable for the decision and system | Remove the owner and expose the accountability gap |
| Stop conditions | The rules for completion, retry limits, failure, and escalation | Create an endless retry and then repair it |

The anatomy will not imply that these parts are always separate software products. They are functional responsibilities that may be implemented in different ways.

## Proposed curriculum

### Module 1: Before the Agent

Start with a utility question and run it through a model response, chatbot, retrieval-supported answer, fixed workflow, and agent. Learners classify each system and see why conversation is not the same as agency.

Work product: AI terms field card.

Capstone step: state the utility problem and classify the current process.

### Module 2: Inside the Agent Loop

Follow a maintenance-information task through goal, plan, tool selection, action, observation, evaluation, adjustment, and stop or escalation. A step-through animation and live event stream show what the system is doing and which evidence it used.

Work product: agent-loop trace.

Capstone step: draw the proposed goal-to-result loop.

### Module 3: What an Agent Needs to Work

Explore models, instructions, tools, governed data, retrieval, memory, state, identity, permissions, and evaluation. Learners repair an agent that has a capable model but missing authority and unreliable context.

Work product: dependency and readiness map.

Capstone step: identify required sources, tools, memory, identity, and readiness gaps.

### Module 4: The Handoff

Proposed golden lesson. A stormwater evidence task moves among an orchestrator, planner, source librarian, analyst, critic, and human approver. Learners watch streamed events, inspect shared state, repair a broken handoff, and decide when work must return to a person.

Work product: orchestration and handoff contract.

Capstone step: name agent roles, human roles, shared state, and handoff evidence.

### Module 5: Agent, Agentic, or Automated?

Use an autonomy spectrum and scenario sorter to compare deterministic workflows, model-assisted workflows, single agents, and multi-agent systems. Learners decide when flexibility earns its cost and risk.

Work product: autonomy and consequence decision record.

Capstone step: select the least complicated architecture that can perform the job and justify the autonomy level.

### Module 6: Guardrails Are Part of the Design

Operate a permission console across read, retrieve, recommend, draft, write, and execute levels. A failure lab introduces stale data, tool failure, conflicting records, unsupported claims, prompt injection, retry limits, and escalation.

Work product: guardrail and human-authority plan.

Capstone step: define allowed actions, prohibited actions, approvals, retry limits, and escalation.

### Module 7: Where Utilities May Become Agentic

Explore bounded patterns in regulatory research, work-order preparation, capital submissions, storm-event coordination, inspection reconciliation, customer service, and asset-risk review. Learners separate plausible value from unsafe autonomy.

Work product: utility opportunity portfolio.

Capstone step: compare value, consequence, readiness, cost, and measurement options.

### Module 8: Design Your First Utility Agent

Create and challenge a Utility Agent Canvas. Define the goal, trigger, sources, tools, allowed actions, prohibited actions, owner, evidence, evaluation, cost, stop conditions, and human escalation. A peer or instructor review checks whether a deterministic workflow would be better.

Capstone: approved Utility Agent Canvas and 90-day pilot brief.

Capstone step: assemble, challenge, revise, and defend the complete pilot.

## Agent roles introduced

- Orchestrator or router
- Planner
- Source librarian or retrieval specialist
- Analyst
- Tool-use or execution specialist
- Memory and state service
- Critic or evaluator
- Guardrail or policy check
- Human approver and accountable owner

These are reusable architectural roles, not a claim that every agent system needs nine separate agents.

## Evidence and safety boundary

The course teaches advisory, analytical, knowledge, and coordination applications. It does not authorize autonomous operational control, permit certification, emergency decisions, procurement approval, or financial authorization.

## Capstone completion standard

The final Utility Agent Canvas and 90-Day Pilot Brief must identify:

1. Utility problem and current process
2. Intended result and measurable value
3. Users, affected people, and accountable owner
4. Approved sources and known data limitations
5. Tools and systems
6. Agent and human roles
7. Allowed and prohibited actions
8. Handoffs and shared state
9. Guardrails and approval points
10. Evaluation cases and success measures
11. Cost, usage, and retry limits
12. Stop and escalation conditions
13. Reason an agent is preferable to a deterministic workflow
14. Ninety-day pilot boundary and review schedule

The capstone does not require programming. It requires professional judgment, clear boundaries, and a testable design.

## Thirty-day application challenge

After the course, learners are encouraged to:

1. Identify one repetitive but irritating task.
2. Map how it is completed today.
3. Name the sources, systems, and accountable person.
4. Decide whether rules, retrieval, or an agent is the simplest answer.
5. Test the idea against historical cases.
6. Begin with read-only or recommendation-only permissions.
7. Record every failure and unexpected cost.
8. Measure accuracy, time, rework, cost, and human-review effort.
9. Expand the pilot only when evidence supports the change.

## Course completion

Completion requires the assigned simulations, explanatory knowledge checks, progressive capstone sections, final Utility Agent Canvas, pilot brief, and learner explanation of why the proposed system should or should not be agentic.

## Approval needed

- Working title and learner promise
- Final working title
- Module 4 golden lesson design brief
- Utility-practitioner reviewers
- Final credential name and release standard
