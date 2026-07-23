# Module 2 Video Script: Inside the Agent Loop

Intended length: 6 to 8 minutes

Status: working recording draft

## Spoken words

An agent is easier to understand when you stop looking only at the final answer. In this lesson, we will watch the work happen one step at a time.

The loop starts with a goal. The goal describes the result the user wants. The system then plans the next part of the work. It chooses an approved tool, takes an action, and observes what happened. Evaluation checks the result against the goal and the evidence. The system may adjust and try again, stop because the goal has been met, or escalate because a person needs to decide.

[Show the animated loop. Pause on each stage.]

Our utility example is a maintenance information request. The agent must find the correct asset, open approved work records, compare recent observations, identify missing information, and prepare a recommendation for review. The event stream on the page records each action in order. It is the system's activity log for this task.

When you step through the simulation, watch the difference between an action and an observation. Searching a work system is an action. The returned records are an observation. Drafting a recommendation is an action. A source-coverage check is an evaluation.

Your work product is an agent-loop trace. Record the goal, each tool call, each observation, each check, and the final stop or escalation. If a later reviewer cannot reconstruct the path, the final answer is not enough.

The takeaway is that an agent needs a controlled loop, not endless activity. In the next lesson, we will inspect the parts that make this loop possible.
