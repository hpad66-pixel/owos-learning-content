# Course Overview Video Script

Working title: Meet the Agent: How AI Gets Work Done in Water Utilities

Intended length: 10 to 14 minutes

Audience: utility professionals who are new to AI agents

Status: working recording draft

## Opening

**Visual direction:** Show Hardeep on camera. Then show a water utility control room, a field inspection, a maintenance planner, and a stormwater map.

**Spoken words:**

Welcome. This course is for people who understand utility work but may not yet understand what an AI agent is. You do not need a technical background. We will start with familiar water, wastewater, and stormwater situations. Then we will use those situations to explain what the technology is doing.

An AI agent is a system that can work toward a goal, use approved information and tools, observe what happened, and decide what to do next within defined limits. That is different from a chatbot that only responds in a conversation. It is also different from a fixed workflow that follows the same steps every time.

The purpose of this course is not to make every utility process agentic. The purpose is to help you recognize the differences, see how the parts work, understand where people remain accountable, and design one bounded application that can be evaluated before anyone treats it as real utility infrastructure.

## Lesson 1: Before the Agent

**Visual direction:** Show five cards labeled model, chatbot, retrieval-supported answer, fixed workflow, and agent.

**Spoken words:**

Lesson one gives you a practical vocabulary. You will take one utility question and watch it move through five different kinds of systems. A model produces an answer. A chatbot provides a conversational interface. Retrieval brings approved source material into the current task. A fixed workflow follows predetermined steps. An agent can select among approved next steps while working toward a goal.

You will classify examples and create an AI terms field card. The point is to stop calling every AI feature an agent. By the end of the lesson, you should be able to explain the differences to a coworker without using sales language or technical shorthand.

## Lesson 2: Inside the Agent Loop

**Visual direction:** Animate goal, plan, tool, action, observation, evaluation, adjustment, and stop.

**Spoken words:**

Lesson two opens the agent and lets you watch the operating loop. A goal tells the system what result is requested. A plan organizes the work. A tool lets the system search, calculate, draft, or perform another approved function. An observation records what happened after the action. Evaluation checks whether the result is supported and whether the goal has been met.

You will step through a maintenance information task and read an event stream, which is simply a time-ordered record of what the system did. You will build an agent-loop trace so that a later reviewer can see the path from request to result.

## Lesson 3: What an Agent Needs to Work

**Visual direction:** Show an agent cutaway with goal, instructions, model, sources, retrieval, tools, state, identity, permissions, evaluation, guardrails, human owner, and stop conditions.

**Spoken words:**

Lesson three explains the anatomy of an agent. Anatomy means the working parts and responsibilities that make the system function. You will remove or weaken one part and see what changes.

If the goal is vague, the system may complete the wrong job. If the sources are stale, a polished answer can still be wrong. If identity and permissions are missing, the system may not know whose authority it is using. If there is no stop condition, the agent can continue retrying after it should have asked for help.

Your work product is a dependency and readiness map. It shows what your proposed application would need before it could be tested responsibly.

## Lesson 4: The Handoff

**Visual direction:** Show the Harbor County stormwater evidence scenario and six roles passing work.

**Spoken words:**

Lesson four is about orchestration and handoffs. Orchestration is the coordination of specialized roles. A handoff is the controlled transfer of work, evidence, status, limitations, and authority from one role to the next.

You will watch a stormwater evidence packet move through an orchestrator, source librarian, analyst, critic, drafter, and human approver. You will see a shared-state ledger, which is the approved task record that tells each role what happened before. Then you will break a handoff, watch the problem travel downstream, and repair the original cause.

You will first read a six-part handoff packet graphic. It shows the goal, status, evidence, limitations, identity, authority, and escalation information that must travel with the work. A cause map then shows why one missing source locator can block several later roles.

You will also set the least authority each role needs and create an orchestration and handoff contract. This lesson shows why adding more agents is not automatically better. Every additional boundary needs evidence, accountability, and a way to stop.

## Lesson 5: Agent, Agentic, or Automated?

**Visual direction:** Show an autonomy spectrum next to a consequence matrix.

**Spoken words:**

Lesson five separates three ideas that are often mixed together. Automated means the system follows defined rules or steps. An agent can choose among approved actions while working toward a goal. Agentic describes how much delegated decision-making appears in the process. A system can be mildly agentic and still require frequent human approval.

You will compare possible utility applications and select the least complicated architecture that can perform each job. You will create an autonomy and consequence decision record. The lesson teaches a practical discipline: do not add open-ended decision-making when a rule, checklist, calculation, or fixed workflow can do the job more clearly.

## Lesson 6: Guardrails Are Part of the Design

**Visual direction:** Show permissions, source rules, evaluation checks, retry limits, escalation, and human approval surrounding an agent.

**Spoken words:**

Lesson six explains guardrails. A guardrail is a control that blocks, pauses, redirects, limits, or escalates behavior. It is not one filter placed at the end. Useful controls can include identity, permissions, approved sources, validation rules, retry limits, logging, monitoring, and named human authority.

You will test failure conditions and decide what the system may read, recommend, draft, write, or execute. You will also mark operational technology boundaries. Operational technology includes systems that monitor or control physical processes. The course does not treat autonomous control of those systems as a beginner exercise.

Your work product is a guardrail and human-authority plan.

## Lesson 7: Where Utilities May Become Agentic

**Visual direction:** Show application cards for maintenance, customer service, capital programs, water quality, stormwater, data stewardship, and regulatory evidence.

**Spoken words:**

Lesson seven moves from mechanism to application. You will examine utility opportunities across roles and departments. For each one, you will compare value, consequence, source readiness, cost, measurement, and the simplest suitable architecture.

The lesson also requires you to reject at least one idea. That matters because good technology judgment includes knowing when not to build. Your work product is a utility opportunity portfolio that distinguishes promising pilots from ideas that need better data, tighter boundaries, or a different solution.

## Lesson 8: Design Your First Utility Agent

**Visual direction:** Assemble the Utility Agent Canvas and 90-Day Pilot Brief.

**Spoken words:**

Lesson eight brings the course together. You will assemble the Utility Agent Canvas that you have been building one part at a time. The canvas records the problem, user, goal, sources, tools, actions, owner, permissions, guardrails, evidence, measures, stop conditions, and escalation path.

Then you will challenge your own design. You will ask what could fail, what would be hard to notice, what action has too much consequence, and what evidence a reviewer would need. Finally, you will produce a 90-Day Pilot Brief with a narrow scope, named owners, evaluation measures, and clear stop conditions.

## Closing

**Visual direction:** Return to Hardeep on camera. Show the eight lesson cards connected to the final pilot brief.

**Spoken words:**

At the end of this course, you should not leave with a vague statement that agents are the future. You should leave with a way to examine them. You should be able to name the parts, read the activity, inspect the evidence, question the handoffs, set the authority, and choose a simpler option when it is better.

Most of all, you should be able to connect the technology to real utility responsibilities. The goal is not to remove professional judgment. The goal is to make the work, evidence, limits, and accountability more visible before a system is trusted with greater responsibility.
