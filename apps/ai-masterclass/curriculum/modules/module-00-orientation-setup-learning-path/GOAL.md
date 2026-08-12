# GOAL: Module M00, Orientation, Setup, and Your Learning Path

| Field | Value |
| --- | --- |
| Module ID | `legacy:M00` |
| Course | AI Master Class, One Water AI Executive Fellowship |
| Work stage | research draft |
| Approval state | proposed, no owner decision recorded |
| Authority | `MODULE-GUIDANCE.json`, `STAFF-DIRECTION.md`, the M00 design brief, `CONTENT-PLACEMENT-REGISTER.json`, `COURSE-BRIEF.md`, `EVIDENCE-BOUNDARIES.md` |
| Governs | what M00 is for and how it will be judged. It does not approve facts, claims, placements, assessments, or release. |

---

## 1. Module purpose

M00 is the contract between the Academy and the learner.

A professional arrives holding a real problem and facing a 64 module curriculum. Their risk is not
that the material is too hard. Their risk is that they wander through it as a collection of
interesting topics, never attach it to work they actually own, and finish with nothing they can
show anyone.

M00 removes that risk by refusing to teach artificial intelligence at all. It orients the learner to
the program, establishes what the program does and does not authorize, captures a readiness baseline
that routes support rather than ranking people, sets the evidence and privacy rules for safe
participation, and requires the learner to name one real One Water problem and one work product
before the curriculum begins.

The module is judged on one thing. Did the learner leave with a completed One Water AI Learning
Charter.

## 2. Learner outcomes and their completion evidence

Backward design starts here. Every outcome names the evidence that proves it. An outcome with no
evidence does not survive into the blueprint, and the package validator fails the build if one
appears.

| ID | The learner can | Completion evidence |
| --- | --- | --- |
| M00.O01 | Explain in plain English what One Water AI teaches, what it does not authorize, and why a named person remains accountable | Orientation acknowledgement plus a scenario question on authority and recommendation |
| M00.O02 | Identify one real drinking water, wastewater, stormwater, reuse, administrative, financial, technical, or public service problem that will anchor their learning | Anchor problem field in the saved Learning Charter, non generic and role connected |
| M00.O03 | Complete and interpret a readiness baseline across role, AI fluency, data and evidence, governance, technical confidence, and organizational support | Completed readiness diagnostic plus a learner written interpretation of one support need |
| M00.O04 | Select the shared core and the role lens most relevant to the decisions they influence, while recognizing the curriculum remains connected | Pathway selection event plus a scenario multiple choice on pathway reasoning |
| M00.O05 | Classify information as approved, restricted, uncertain, or needing approval before it enters an AI system | Information boundary sorter passed, with classify and retry feedback |
| M00.O06 | Create a One Water AI Learning Charter naming a target work product, support needs, success evidence, and a first accountable action | Saved charter with every required field populated |
| M00.O07 | Locate optional technical preparation without treating programming skill as an entry requirement | Question confirming that the shared core requires no terminal, credential file, or code editor |

Verbs are observable by design. The words know, learn, understand, appreciate, and be aware are
rejected at validation, so `Getting set up` never becomes an outcome.

## 3. Curriculum and professional outcomes

**Curriculum.** Establish one participation, evidence, privacy, and human authority contract that
every later module inherits. Capture a baseline that later modules can revisit. Create the first
Fieldbook artifact. Route technical preparation out of the front door and into the modules where it
is actually used.

**Professional.** The learner can tell a supervisor why they are in the program and what they intend
to produce. The learner begins with a named organizational problem instead of general interest in
AI. The program team can see, before week two, who needs technical preparation, evidence support, or
accessibility support.

**Internal marketing.** Staff may describe clarity, a personal starting point, pathway selection, a
readiness baseline, and the Learning Charter. Staff may not promise promotion, salary change, cost
savings, regulatory compliance, certification, implementation success, or mastery.

## 4. Learning Charter completion evidence

The module is not complete unless the learner saves a charter containing all eight fields:

1. role and the decisions they influence
2. one real anchor problem
3. selected role lens and the reason for choosing it
4. readiness baseline and any support needed
5. the source, privacy, evidence, and human authority rules they agree to follow
6. the professional work product they intend to create or improve
7. the evidence that would show useful progress
8. the first accountable action, its owner, and its date

Passing requires all of: required teaching viewed, required interactions completed, information
boundary check passed, and charter saved with every field populated. Scrolling, time on page,
self reported confidence, and diagnostic score are explicitly not completion.

## 5. Evidence boundary

M00 carries almost no external factual load. Nearly everything it teaches is an internal curriculum
decision about how this program operates, and it must be labeled that way rather than dressed up as
established fact.

**M00 makes no determination about** law, privacy law, records retention law, cybersecurity
practice, employment practice, credentialing, product capability, pricing, or utility performance.

**Registered design rationale, not learner facing fact.** Cornell Center for Teaching Innovation on
learning outcomes and course design. University of Illinois Chicago on backward design and Bloom's
taxonomy. CAST Universal Design for Learning Guidelines 3.0. These justify the instructional
approach. They are not cited to the learner as authority for water claims.

**Contributor input is not authority.** `INT-002`, Shreya's contributions `STF-002`, `STF-007`, and
`STF-008`, are expert curriculum planning input. They shape placement. They do not establish
technical fact.

**Every claim carries a class**, recorded in the claims register, one of: sourced fact, internal
curriculum decision, Hardeep Anand position, instructional scenario, expert interpretation, or
unresolved question. The class lives in the register only, never duplicated inline.

**Any claim marked VERIFY** may appear at research draft or blueprint candidate stage and is blocked
at manuscript candidate and beyond. This is enforced mechanically.

## 6. Quality gates

**Automated, enforced by `validate_learnworlds_package.py`, build fails on any failure.**

| Gate | Rule |
| --- | --- |
| Backward design | every outcome names evidence that resolves to a real activity, question, or interaction ID |
| Observable verbs | vague verbs rejected |
| No deleted content | every placement record dispositioned retain, refine, or consolidate into M00 is referenced by an activity |
| Claim discipline | every cited claim declared and present in the register; VERIFY claims blocked past blueprint |
| Assessment integrity | every question attached to an assessment activity, carrying an outcome and both feedback paths |
| Design minimums | four visual types, two interactions, three question types |
| Charter builder | M00 must contain a `builder` interaction |
| Accessibility | alt text present and within 250 characters on every visual |
| Seat time | activity minutes within ten percent of declared |
| Writing standard | no em dash, no en dash, no banned marketing vocabulary |
| Approval language | the words approved, production ready, public, complete, certified, released blocked without a committed record |
| Reviewers | all four review roles must be named before production candidate status |

**Human, cannot be automated.**

| Gate | Accountable role | Current status |
| --- | --- | --- |
| Source authority and locator accuracy | source verification reviewer | unassigned |
| Claim truth and applicability | owner, Hardeep Anand | pending |
| Utility practice realism of every example | qualified utility practitioner | unassigned |
| Plain English, acronym on first use, reading level | novice learner reviewer | unassigned |
| Keyboard, touch, phone, reduced motion, contrast, focus order | accessibility reviewer | unassigned |
| Placement approval | owner | proposed only |
| Release | owner | not authorized |

**Rejection conditions, taken directly from staff direction.** The module is rejected if required
orientation depends on terminal or code editor use, the learner cannot state the program boundary in
plain English, an outcome uses a vague verb, a required activity has no feedback, role tracks read as
separate curricula, the diagnostic reads as a performance rating, the charter is missing a field, a
content block moved without preserving its history, marketing copy makes an unsupported claim,
accessibility is deferred, or any gate is unresolved.

## 7. Unresolved decisions requiring owner approval

Work stops here per the governed sequence. Six decisions are material and are yours, not the
authoring model's.

**D1. Three of four review roles are unassigned.** `production-status.md` shows utility practitioner,
novice learner, and accessibility review with no reviewer. This is the binding constraint on M00, not
drafting capacity. M00 cannot pass production candidate without names.

**D2. A placement inconsistency in the register.** `M00.P04` is dispositioned `consolidate` with
`destinationModuleId: legacy:M00`, but `consolidateUnder: M00.P02`, and `M00.P02` is dispositioned
`cross-reference` to `legacy:M25`. So the consolidated record points at M00 while its parent points
at M25. One of the two needs to change. Recommendation, set `M00.P04` destination to `legacy:M25`
with a preserved M00 origin reference, which keeps the history and puts the merged proposal where its
parent lives. This is a placement decision, so I am not making it.

**D3. Readiness diagnostic data handling.** The design says support routing, not performance rating.
Once stored per learner in the platform it becomes an employment adjacent record. Needed: who can see
individual results, how long they are kept, whether staff see aggregate only, and whether the learner
can delete theirs. M00 should state the answer to the learner in plain English.

**D4. Where the Learning Charter physically lives.** LearnWorlds offers a Form activity and a
Reflection Journal activity. Neither produces a versioned, learner owned, exportable record that
later modules and the capstone can read. Options: build it as an HTML5 or SCORM activity with export,
or hold it in the Fieldbook with the platform capturing only a completion event. This decision
changes the module build, so it is needed before the manuscript.

**D5. Module to section mapping.** Confirm that one governed module becomes one LearnWorlds section
containing multiple learning activities, rather than one graded SCORM package as a single activity.
The import contract assumes the former.

**D6. Glossary scope.** `M00.07 Glossary` is dispositioned `retain`. Open question, does M00 carry a
module glossary or a course wide glossary surfaced in M00. A course wide glossary changes the work
from writing entries to establishing the term registry that all 64 modules draw from.

---

## What this document is

A research draft prepared for owner review. It is not a blueprint lock, not a manuscript, not a
production candidate, and not approved. No claim in M00 has been source verified. No placement has
been committed. No release is authorized.
