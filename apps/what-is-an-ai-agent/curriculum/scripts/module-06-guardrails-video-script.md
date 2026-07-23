# Module 6 Video Script: Guardrails Are Part of the Design

Intended length: 7 to 9 minutes

Status: working recording draft

## Spoken words

A guardrail is a control that blocks, pauses, redirects, limits, or escalates behavior. It is not one warning placed around a model. Useful control comes from several layers working together.

[Show the guardrail layers.]

Identity tells the system who is acting. Permissions define what that identity may do. Source rules limit which records may support the task. Validation checks the result. Retry limits stop repeated failure. Logging creates an activity record. Monitoring helps people detect unusual behavior. Human authority keeps consequential decisions with named people.

The lesson also introduces prompt injection. Prompt injection is an instruction hidden in untrusted content that tries to redirect the system. For example, a document could contain text telling an agent to ignore its approved task. The system should treat the document as evidence to inspect, not as new authority.

[Show the operational-technology boundary.]

Operational technology includes systems that monitor or control physical processes. A beginner pilot should not quietly gain authority to change a pump setting, chemical dose, gate position, or other physical control. Those actions carry different safety, cyber, operating, and regulatory consequences.

Your work product is a guardrail and human-authority plan. Name allowed actions, prohibited actions, approval points, retry limits, monitoring, and escalation. Write each control so that another person can test it.

The takeaway is that guardrails belong in the system design from the beginning. In the next lesson, we will compare possible utility applications using value, readiness, and consequence.
