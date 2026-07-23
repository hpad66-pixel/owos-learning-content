# Module 3 Video Script: What an Agent Needs to Work

Intended length: 7 to 9 minutes

Status: working recording draft

## Spoken words

This lesson explains the anatomy of an agent. Anatomy means the parts and responsibilities that allow the system to work. These parts do not have to be separate products. They are jobs that the design must perform.

[Show the agent cutaway.]

The goal states the requested result. Instructions describe the method and boundaries. The model interprets context and chooses among possible next steps. Sources provide approved information. Retrieval finds the information needed for the current task. Tools let the system search, calculate, draft, or perform another approved function.

State is the current task record. It tells the system what has already happened. Identity tells the system who is asking and whose authority applies. Permissions define what that identity may do. Evaluation checks the result. Guardrails block, pause, redirect, limit, or escalate behavior. A human owner remains accountable for consequential decisions. Stop conditions tell the system when it is complete, when it has failed, and when it must ask for help.

In the interactive anatomy, remove or weaken one part. If you remove state, the system may repeat work or forget an open conflict. If you weaken permissions, the system may be able to change a record that it should only read. If you remove the owner, the accountability gap becomes visible.

Your work product is a dependency and readiness map. For your utility use case, name the sources, tools, identity, permissions, checks, owner, and stop conditions that must exist before a pilot begins.

The takeaway is that a capable model is only one part of an agent. In the next lesson, we will watch several roles pass work across controlled handoffs.
