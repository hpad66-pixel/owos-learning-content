# Research Assessment: What Is an AI Agent?

Updated: 2026-07-22  
Status: ready for Hardeep's review, not a locked curriculum

## Research conclusion

The McKinsey paper is a useful executive explainer but should not become the course outline. It mixes several levels of analysis: individual agents, multi-agent systems, workflow platforms, enterprise architecture, and operating models. The course needs a cleaner conceptual spine supported by primary technical sources and grounded in utility decisions.

## Recommended foundational distinction

### Model

The model interprets information and produces predictions, reasoning, or language. A model alone does not have permission, tools, or a durable job.

### Chatbot

A chatbot provides a conversational interface. It may answer from a model or retrieved information. It is not automatically an agent because conversation alone does not mean it controls and completes a workflow.

### Retrieval-augmented generation

Retrieval-augmented generation supplies selected external context to a model before it answers. It can improve grounding and citations. Retrieval alone does not plan, select actions, or complete a workflow, so it is not an agent by itself.

### Deterministic workflow

A deterministic workflow follows code-defined steps and branches. A model may perform one step, but the software controls the route.

### Agent

An agent is a bounded software system that uses a model to direct parts of its own process, select approved tools, observe results, adjust, and work toward a user-defined goal. It operates under instructions, permissions, stop conditions, and human oversight.

### Agentic system

Agentic system is the broader architecture. It may contain fixed workflows, one dynamic agent, several specialized agents, memory, tools, evaluation, and human checkpoints. The adjective agentic describes goal-directed, adaptive behavior. It is better treated as a spectrum than as a binary label.

### Multi-agent system

A multi-agent system coordinates several agents with distinct responsibilities. Handoffs, shared state, conflict resolution, evaluation, and accountability become part of the design problem.

## What should precede the agent

Learners need a short conceptual runway:

1. data and governed sources;
2. model and prompt;
3. chatbot and conversational interface;
4. retrieval and grounding;
5. tools and application programming interfaces;
6. deterministic automation;
7. memory and state; and
8. permissions, identity, and human authority.

These concepts should be introduced only far enough to explain agents. Separate courses can address retrieval, chatbots, models, and data architecture in depth.

## Utility teaching boundary

The course should focus on administrative, analytical, knowledge, and coordination patterns before operational control. Credible examples include:

- assembling a cited regulatory research packet;
- triaging work-order information and preparing a crew brief;
- checking a capital-project submission for missing evidence;
- coordinating storm-event information across approved sources;
- comparing inspection records and escalating conflicts;
- drafting customer-service responses from approved policy; and
- preparing an asset-risk review for human decision.

The course must not imply that a generative agent should independently control treatment, pumping, chemical dosing, safety systems, emergency response, permit certification, procurement approval, or financial authorization.

## Proposed aha moments

1. The same utility question passes through five systems: chatbot, retrieval-supported answer, fixed workflow, single agent, and multi-agent system. Learners see what changes at each step.
2. A live loop shows goal, plan, tool selection, action, observation, evaluation, adjustment, and stop or escalation.
3. A streaming workbench reveals intermediate events without presenting hidden model reasoning as fact.
4. An orchestration simulation passes a stormwater evidence task among planner, source librarian, analyst, critic, and human approver.
5. A handoff lab deliberately drops context, authority, or provenance so the learner sees why shared state and contracts matter.
6. A guardrail console changes permissions from read to recommend to draft to write, showing which actions require approval.
7. A failure lab introduces stale data, unavailable tools, conflicting records, prompt injection, unsupported claims, and retry limits.
8. A utility agent canvas lets the learner define a bounded use case, sources, tools, actions, guardrails, evaluation, owner, and escalation path.

## Additional evidence needed before course lock

- Primary source for retrieval-augmented generation fundamentals
- Primary source for secure tool use and prompt-injection controls
- Current guidance on agent evaluation and observability
- Utility-specific cybersecurity and operational-technology boundaries
- Utility practitioner review of proposed use cases
- Decision on whether McKinsey figures and company examples will be excluded or traced to their original studies
