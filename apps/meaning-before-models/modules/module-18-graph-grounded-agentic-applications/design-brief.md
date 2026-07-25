# Module 18 Design Brief: Graph-Grounded Agentic Applications

Status: approved for production under standing owner authorization

## Learning decision

The learner must separate a well-grounded answer from permission to change the world. Given an
agent proposal, the learner decides whether the system may act, must ask a human, must refresh or
clarify evidence, or must stop.

## Experience architecture

This lesson is an agent authorization control room, not another answer-pipeline comparison. A
wastewater agent proposes creating a corrective work order after detecting a likely upstream
contributor to Overflow 21. The relationship path is credible, but the last inspection is stale,
the operator has draft-only authority, and the requested priority would commit staff and money.

The learner follows the proposal through two independent keys:

1. knowledge fitness, including identity, evidence, provenance, freshness, validation, and
   unresolved conflict; and
2. action authority, including authenticated actor, policy, delegated role, tool scope, approval,
   safe execution, verification, and audit.

The emotional rhythm is confidence, interruption, disciplined restraint, controlled action, and
accountable proof.

## Visual Arsenal selection

| Teaching idea | Visual class | Selected visual | Learner conclusion |
| --- | --- | --- | --- |
| Grounding and authority are independent | paired-control comparison | Two-Key Action Console | A grounded proposal still cannot act without authority |
| Safe action is a branching lifecycle | state-transition diagram | Proposal-to-Record State Machine | Ask and stop are successful controlled outcomes |
| Execution needs a bounded contract | exploded-view anatomy | Action Envelope | Evidence, policy, tool, and recovery controls travel together |
| Accountability continues after the tool call | audit timeline | Action Flight Recorder | A completed action needs a verifiable receipt and owner |

## Narrative arc

1. Open on a correct answer that is not authorized to act.
2. Separate epistemic confidence from operational authority.
3. Walk the proposal through validate, authorize, approve, execute, verify, and record.
4. Resolve allowed, denied, stale, ambiguous, and approval-required cases.
5. Rehearse uncertain tool outcomes, duplicate prevention, and recovery.
6. Write and defend an Agent Action Contract.

## Foundation, Practitioner, and Leader views

- Foundation: ask three plain questions: Do we know enough? May this actor do this? Can we prove
  what happened?
- Practitioner: define tool schemas, preconditions, freshness, idempotency keys, retry rules,
  receipts, reconciliation, and immutable audit events.
- Leader: set delegated authority, mandatory approval thresholds, separation of duties,
  accountability, review cadence, and prohibited actions.

## Signature mechanisms

### Agent Action Control Room

The learner resolves five proposals using ACT, ASK, REFRESH, CLARIFY, or STOP. Each case exposes
the evidence and declared control before revealing the correct disposition.

### Safe Retry and Receipt Simulator

The learner handles five uncertain execution states: pre-call timeout, acknowledged success,
unknown outcome, rejected duplicate, and failed verification. The mechanism teaches that retry is
not a synonym for repeating a side effect.

## Assessment rhythm

- Opening multiple-choice check rejects the idea that answer confidence is permission.
- A matching check pairs action states with their operating meaning.
- The control-room simulation assesses stop and escalation judgment in context.
- A multi-select check diagnoses the minimum executable action envelope.
- The retry simulator assesses idempotency and external-state recovery.
- Flip cards rehearse audit questions before the final artifact.
- The applied work product requires a defensible Agent Action Contract.

## Professional work product

The Agent Action Contract records bounded use, proposed action, identity and evidence prerequisites,
freshness, validation, policy, authenticated role, delegated authority, allowed tool and parameters,
prohibited actions, approval, act/ask/stop states, idempotency, retry and reconciliation, verification,
audit receipt, owners, tests, and correction procedure.

## Evidence boundary

Resource Description Framework relationships can ground identity and evidence. Shapes Constraint
Language can test declared graph constraints. Provenance can describe sources and activities. None
of those standards supplies authentication, authorization, orchestration, safe tool execution,
cybersecurity controls, or human accountability by itself.

## Accessibility and responsive treatment

- Every state is named in text and never conveyed by color alone.
- Decision controls are native buttons with immediate live-region feedback and retry.
- Static diagrams preserve all meaning when motion is reduced.
- Mobile layouts stack gates, states, envelope layers, and audit events in reading order.
- Tool outcomes and receipts remain readable at 200 percent zoom without horizontal scrolling.
- The action control room teaches before it tests and provides a textual explanation for every case.

## Adjacent-module distinctiveness

- Module 17 compares BI, document retrieval, graph retrieval, and context-engine answer paths. Its
  work product is an Answer Repeatability Map. Module 18 begins only after a proposal exists and
  governs whether that proposal may change external state.
- Module 19 is a capstone investment and pilot-defense experience. Module 18 does not ask the
  learner to design architecture, value, or a ninety-day pilot.
- This lesson's dominant grammar is an authorization console, branching state machine, executable
  envelope, and flight recorder. It does not reuse synchronized lanes or a pilot canvas.

## Release-review additions

- A complete LS-7 graph-to-action trace exposes six explicit triples and the separate graph,
  validation, authorization, approval, execution, verification, and audit decisions.
- Dates, priority labels, role names, freshness limits, and approval thresholds are identified as
  illustrative utility policy assumptions.
- The Agent Action Contract uses a twenty-point rubric, a sixteen-point handoff threshold, a
  completed exemplar, weak-versus-strong comparison, final defense, and export.
- National Institute of Standards and Technology guidance strengthens the operational-technology,
  least-privilege, authorization, and artificial-intelligence risk boundaries.
- Every graphic offers a full-size view and structured text equivalent; mobile keeps the graphic
  inspectable inside its own controlled viewport.
- Module 19 must consume a contract scoring at least sixteen points and map every control to an
  architecture component, owner, and acceptance test.
