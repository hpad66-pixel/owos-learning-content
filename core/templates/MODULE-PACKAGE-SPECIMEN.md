---
schema: owos-learnworlds-module/v1
courseId: ai-masterclass
moduleId: legacy:M00
moduleCode: M00
title: Orientation, Setup, and Your Learning Path
sectionTitle: Start Here, Orientation and Your Learning Path
status: research-draft
approvalState: proposed
approvalRecord: none
workProduct: One Water AI Learning Charter
seatTimeMinutes: 50
readingLevelTarget: grade-10
accessibilityTarget: WCAG-2.2-AA
registers:
  claims: research/CLAIMS-REGISTER.md
  sources: research/SOURCE-REGISTER.md
  evidenceBoundaries: research/EVIDENCE-BOUNDARIES.md
  placement: curriculum/modules/module-00-orientation-setup-learning-path/CONTENT-PLACEMENT-REGISTER.json
reviewers:
  utilityPractitioner: unassigned
  noviceLearner: unassigned
  accessibility: unassigned
  sourceVerification: unassigned
outcomes:
  - id: M00.O01
    verb: explain
    statement: Explain what One Water AI teaches, what it does not authorize, and where a named person remains accountable.
    evidence: [M00.A02, M00.Q01]
  - id: M00.O02
    verb: identify
    statement: Identify one real One Water problem or professional opportunity that will anchor the learning.
    evidence: [M00.A05, M00.X01]
  - id: M00.O03
    verb: complete
    statement: Complete and interpret a readiness baseline across role, fluency, evidence, governance, technical confidence, and organizational support.
    evidence: [M00.A04, M00.X02]
  - id: M00.O04
    verb: classify
    statement: Classify learning information as approved, restricted, uncertain, or requiring human approval before use.
    evidence: [M00.A06, M00.Q02]
  - id: M00.O05
    verb: produce
    statement: Produce a One Water AI Learning Charter naming a target work product, support needs, success evidence, and a first accountable action.
    evidence: [M00.A08, M00.X01]
  - id: M00.O06
    verb: locate
    statement: Locate optional technical preparation without treating programming skill as an entry requirement.
    evidence: [M00.A03, M00.Q03]
claims:
  - CLM-M00-001
  - CLM-M00-002
  - CLM-M00-003
  - CLM-M00-004
---

# Orientation, Setup, and Your Learning Path

## Where you are standing right now

```owos-activity
id: M00.A01
type: ebook
title: Where you are standing right now
placementRefs: [M00.01]
outcomeRefs: [M00.O01]
estimatedMinutes: 5
```

Somewhere in your organization there is a decision waiting on better information. It might be which
pump station to rehabilitate first. It might be whether a consent order response will hold up. It
might be why the same customer complaint keeps arriving from the same six blocks after every storm.

You did not come here to learn a technology. You came here because a decision like that one is
yours to make, or yours to inform, and the information you have is not good enough yet.

This program is built on one idea. Artificial intelligence, meaning a set of computational methods
that produce predictions, classifications, or generated text from data, produces recommendations
rather than decisions. [CLM-M00-001] A named person still owns the decision.

```owos-visual
id: M00.V01
type: role-network
title: Who touches a single One Water decision
altText: A network diagram with a pump station replacement decision at the center, connected to an operator, a maintenance planner, an engineer, a finance analyst, a regulatory contact, and a customer service representative.
sourceRefs: [SRC-M00-001]
placementRefs: [M00.01]
```

## What this program does and does not authorize

```owos-activity
id: M00.A02
type: ebook
title: What this program does and does not authorize
placementRefs: [M00.02, M00.05]
outcomeRefs: [M00.O01]
estimatedMinutes: 6
```

This program teaches judgment. It does not grant authority.

Finishing this program does not authorize you to release a model into operations, to change a
permit submission, to alter a rate study, or to act on a recommendation your organization has not
reviewed. Every module keeps a visible line between what a system suggests and what a person
decides. [CLM-M00-002]

The curriculum is shared. Everyone takes the same core. A role lens changes the examples you see
first, not the standard you are held to. [CLM-M00-003]

```owos-visual
id: M00.V02
type: comparison
title: Recommendation compared with decision
altText: A two column comparison. The left column lists what a model produces, including rankings, classifications, and drafts. The right column lists what a person owns, including approval, release, communication, and accountability.
sourceRefs: [SRC-M00-002]
placementRefs: [M00.02]
```

## Getting set up without becoming a programmer

```owos-activity
id: M00.A03
type: ebook
title: Getting set up without becoming a programmer
placementRefs: [M00.03]
outcomeRefs: [M00.O06]
estimatedMinutes: 5
```

Required setup is short. You need account access, a supported browser, a way to reach support, any
accessibility accommodation you use, and an approved place to store your own work.

You do not need a terminal. You do not need an application programming interface key, which is a
credential that lets one software system call another. You do not need a code editor. Those topics
are preserved in this program as optional preparation, and they are taught where they are actually
used rather than at the front door.

```owos-visual
id: M00.V03
type: flow
title: Required setup compared with optional preparation
altText: A flow diagram with two lanes. The required lane shows account access, browser, support contact, accessibility needs, and approved storage. The optional lane branches to later modules covering command line tools, credentials, and code editors.
sourceRefs: [SRC-M00-003]
placementRefs: [M00.03]
```

## Your readiness baseline

```owos-activity
id: M00.A04
type: self-assessment
title: Your readiness baseline
placementRefs: [M00.04]
outcomeRefs: [M00.O03]
estimatedMinutes: 8
```

The next set of questions produces a baseline, not a score. It routes you to support. It is not
used for advancement, employment, aptitude, or performance evaluation, and no supervisor receives
it. [CLM-M00-004]

```owos-interaction
id: M00.X02
type: self-diagnostic
title: Six dimension readiness baseline
dimensions: [role, ai-fluency, data-and-evidence, governance, technical-confidence, organizational-support]
routing: support-only
retention: learner-visible, instructor-aggregate-only
placementRefs: [M00.04]
```

```owos-question
id: M00.Q03
activity: M00.A04
type: true-false
outcomeRef: M00.O06
claimRefs: [CLM-M00-003]
stem: Programming skill is required to complete this program.
options:
  - True
  - False
correct: 2
feedbackCorrect: Correct. Programming is optional preparation. The shared core is completed without writing code.
feedbackIncorrect: Not correct. Programming is offered as optional preparation and is taught where it is used. The shared core does not require it.
```

## Choosing a role lens without leaving the shared curriculum

```owos-activity
id: M00.A05
type: ebook
title: Choosing a role lens without leaving the shared curriculum
placementRefs: [M00.06]
outcomeRefs: [M00.O02]
estimatedMinutes: 5
```

A role lens is a starting angle. An operations lens opens with a lift station. A finance lens opens
with a rate case. A stormwater lens opens with a drainage complaint after a rain event. A reuse
lens opens with a permit condition. The underlying material is the same for all of them.

```owos-visual
id: M00.V04
type: matrix
title: Role lens compared with anchor problem
altText: A grid with role lenses down the left side, including operations, engineering, finance, regulatory, and customer service, and example anchor problems across the top drawn from drinking water, wastewater, stormwater, and reuse.
sourceRefs: [SRC-M00-004]
placementRefs: [M00.06]
```

## What you may bring into this program and what you may not

```owos-activity
id: M00.A06
type: ebook
title: What you may bring into this program and what you may not
placementRefs: [M00.07]
outcomeRefs: [M00.O04]
estimatedMinutes: 6
```

You will work on a real problem, so you will be tempted to bring real records. Sort every piece of
information into one of four boxes before it enters your coursework. Approved means your
organization has cleared it for this use. Restricted means it is sealed, private, personally
identifying, or security sensitive, and it stays out. Uncertain means you do not know yet, so treat
it as restricted until you do. Needs approval means a named person has to say yes first.

## Orientation check

```owos-activity
id: M00.A07
type: exam
title: Orientation check
placementRefs: [M00.08]
outcomeRefs: [M00.O01, M00.O04]
estimatedMinutes: 5
```

```owos-question
id: M00.Q01
activity: M00.A07
type: multiple-choice
outcomeRef: M00.O01
claimRefs: [CLM-M00-001, CLM-M00-002]
stem: A vendor tells your utility that its model will decide which pumps to replace next year. Under this program's accountability rule, what is the correct reading of that statement?
options:
  - The model decides and staff carry out the decision.
  - The model produces a ranked recommendation and a named person remains accountable for the decision.
  - The decision is automated, so accountability transfers to the vendor.
  - Accountability is shared equally between the model and the utility.
correct: 2
feedbackCorrect: Correct. The program teaches recommendation, not authority. A named person stays accountable for the capital decision.
feedbackIncorrect: Not correct. A model can rank and recommend. Accountability for a capital decision stays with a named person and does not transfer to a vendor.
```

```owos-question
id: M00.Q02
activity: M00.A07
type: ordering
outcomeRef: M00.O04
claimRefs: [CLM-M00-004]
stem: Place these steps in the order you should follow before bringing a utility record into your coursework.
options:
  - Identify what the record contains and where it came from.
  - Classify it as approved, restricted, uncertain, or needing approval.
  - Obtain a named approval if one is required.
  - Use only the approved portion in your coursework.
correct: [1, 2, 3, 4]
feedbackCorrect: Correct. Identify, classify, obtain approval, then use only what was cleared.
feedbackIncorrect: Not correct. Classification comes before approval, and approval comes before use. Review the four boxes and try again.
```

## Your One Water AI Learning Charter

```owos-activity
id: M00.A08
type: form
title: Your One Water AI Learning Charter
placementRefs: [M00.09, M00.P04, M00.P04a, M00.P04b, M00.P04c, M00.P04d, M00.P04e]
outcomeRefs: [M00.O02, M00.O05]
estimatedMinutes: 8
```

```owos-interaction
id: M00.X01
type: builder
title: One Water AI Learning Charter builder
fields: [role, anchor-problem, role-lens, readiness-needs, support-needs, evidence-boundary, target-work-product, success-evidence, first-accountable-action]
output: learner-owned artifact, saved to the Fieldbook
placementRefs: [M00.09]
```

Your charter is the contract you write with yourself. It names one problem, one lens, one work
product you intend to produce, the evidence that would tell you it worked, and one action you will
take within the next two weeks that someone else can see.

## Module FAQ and where M01 picks up

```owos-activity
id: M00.A09
type: ebook
title: Module FAQ and where M01 picks up
placementRefs: [M00.01]
outcomeRefs: [M00.O01]
estimatedMinutes: 2
```

Module one begins with the question this module has been circling. What actually changes in utility
work when these systems arrive, what does not change, and who remains accountable when they do.
