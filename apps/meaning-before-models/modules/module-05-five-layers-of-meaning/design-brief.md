# Module 05 Design Brief: Five Layers of Meaning

Status: approved for golden-lesson implementation
Storyboard: `storyboard.yaml`, version 0.2.0
Build state: authorized on 2026-07-24

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-course-semantic-data-ai-001`, `mbm001:05` |
| Working title | Five Layers of Meaning |
| Primary learner | An intelligent utility professional or leader who uses data and makes or governs decisions without assumed semantic-technology or programming experience |
| Secondary learner | Data, GIS, IT, OT, analytics, governance, and AI practitioners using optional implementation depth |
| Curriculum role | Architecture distinction map between a usable graph and the deeper vocabulary, ontology, mapping, and context lessons |
| Competency | Distinguish five commonly mixed meaning jobs and route each utility artifact or responsibility to its proper job |
| Controlled evidence | `DIR-005`, `SRC-001`, `SRC-005`; claims `CLM-028`, `CLM-029`, `CLM-030` |
| Evidence boundary | The five-job distinction is an OWOS teaching framework. Product language varies. Good context can reduce ambiguity and unsupported generation, but it does not make a generative model perfectly deterministic. |

## The one learning job

The learner must answer one practical question:

> Which meaning job is this artifact, rule, mapping, or runtime control actually performing?

This lesson is not the ontology mastery lesson, the semantic mapping implementation lesson, or the
AI Context Contract lesson. Modules 06, 07, 13, and 16 carry those jobs. Module 05 gives learners
the distinction map they need before entering them.

## Opening situation

At 2:10 a.m., a pressure event affects Zone 3. The duty manager asks:

> Which active critical-facility customers may be exposed, what evidence supports the list, and
> which procedure applies tonight?

The team has data. CIS has accounts. GIS has premises and zones. SCADA has the event. The document
system has procedures. A dashboard joins several tables. A prompt asks an AI assistant for the
answer. Yet the team still disagrees about what "active," "critical facility," "exposed," and
"current procedure" mean.

Before teaching begins, the learner chooses which artifact should control the meaning of
"active customer exposed to this event." The debrief reveals why no single database table, report,
taxonomy, ontology, mapping, or prompt performs every job.

## Consequence

When the jobs are mixed, teams solve the wrong problem at the wrong boundary:

- they change a table when a shared definition is missing;
- they add a category when a relationship rule is missing;
- they rewrite a prompt when an enterprise mapping is wrong;
- they retrieve more records when task permissions or time are missing;
- they blame the model when the organization never assigned semantic ownership.

The professional consequence is an answer that may look polished but cannot be defended.

## Five distinctions, in ordinary language

| Job | Plain-English question | Utility example | What it does not do by itself |
| --- | --- | --- | --- |
| Data model | How is information structured in this system or product? | CIS tables for account status, start date, end date, and service address | Establish one shared enterprise meaning for "active customer" |
| Taxonomy | How do we classify and organize terms? | Critical facility categories such as hospital, dialysis center, and nursing facility | Express all domain relationships, rules, or runtime permissions |
| Ontology | What do our shared concepts and relationships mean? | An active service account serves a premise; a premise lies in a pressure zone; an event affects a zone | Identify the current source row or package tonight's task context |
| Semantic layer | How does shared meaning resolve to authoritative enterprise data? | Map `ActiveServiceAccount` to governed CIS status and effective-date fields, and `PressureZone` to GIS identifiers | Decide the user's purpose, permission, time, or permitted action |
| AI context | What does the model or agent need for this task now? | The customer, event, effective time, evidence, definitions, current policy, permissions, conflicts, and output limits | Become a permanent enterprise ontology or a source system |

A context engine is the governed mechanism that retrieves, filters, validates, and assembles AI
context. It is not the context package itself.

## Cognitive design

| Field | Decision |
| --- | --- |
| Prior knowledge activated | Module 04 showed that shared nodes and named relationships form answerable graph paths. |
| Misconception to change | Structure, classification, shared meaning, enterprise mapping, and runtime context are interchangeable words for one technical layer. |
| Worked example | Zone 3 critical-facility exposure, read from operational event through human-reviewed answer. |
| Guided practice | Classify twelve familiar artifacts with visible reasoning and correction. |
| Independent practice | Diagnose the primary missing job in a wastewater overflow scenario. |
| Retrieval opportunities | Opening decision, five-job contrast, artifact classification, missing-job diagnosis, and final defense. |
| Transfer task | Determine why a stormwater outfall inspection assistant uses the wrong permit condition despite retrieving the correct document. |
| Feedback model | Immediate explanation names the artifact's primary job in the bounded scenario and explains why the strongest alternative is tempting but wrong. Retry changes no hidden state. |
| Load removed | No standards syntax, vendor screen, stack diagram, ontology editor, or large architecture inventory is required on the common route. |

## Narrative architecture

The lesson is a decision room, not a catalog of definitions.

1. A pressure event exposes disagreement despite abundant data.
2. The learner makes a consequential opening decision.
3. The instructor separates the five questions before naming the five terms.
4. The learner classifies real utility artifacts at an evidence desk.
5. The instructor connects the five jobs into one answer path without turning them into a mandatory stack.
6. The learner removes one job and watches the failure change shape downstream.
7. The scenario transfers to wastewater and stormwater.
8. The learner produces and defends one Five-Layer Meaning Map.

## Concept-to-experience plan

| Teaching idea | Natural visual shape | Planned visual ID | Learner action | Learner realization | Assessment job |
| --- | --- | --- | --- | --- | --- |
| Data can be plentiful while meaning and authority remain unresolved | Annotated editorial utility scene | `mbm05-pressure-room` | Inspect the Zone 3 evidence desk and make the opening decision | Source records contribute evidence, but no single source performs every meaning job | Choose and explain |
| Five related terms answer five different questions | Governed comparison table with one scenario threaded across rows | `mbm05-five-job-comparison` | Compare question, artifact, owner, and failure for each job | Similar vocabulary does not make the jobs interchangeable | Match question to job |
| Meaning must resolve to real enterprise records | Concept-to-source connection map | `mbm05-semantic-bridge` | Trace `ActiveServiceAccount` from concept to fields and current records | Ontology meaning and semantic mapping cooperate but do different work | Locate the broken boundary |
| Runtime context is a bounded package, not all available data | Exploded context packet | `mbm05-context-packet` | Add only task-relevant evidence, policy, permission, time, and output limits | More context is not automatically better context | Detect omission and excess |
| A missing job creates a distinct downstream failure | Executable failure propagation map | `mbm05-failure-trace` | Remove one job and follow the consequence to the answer | Repair should begin at the first broken boundary | Diagnose and repair |

## Signature mechanism

### The Meaning Triage Desk

The learner receives twelve utility artifacts from the Zone 3 event:

1. CIS account-status table
2. critical-facility category list
3. definition of an active service account
4. `servesPremise` relationship rule
5. mapping from the shared concept to CIS fields
6. GIS zone identifier crosswalk
7. current pressure-event record
8. effective-time rule
9. current response procedure
10. operator permission
11. unresolved source conflict
12. output and action limit

The learner routes each artifact to its primary meaning job. The desk then reorganizes those
artifacts into a governed answer path. This transformation is the lesson's "wow" moment: the same
pieces stop looking like a pile of data and begin looking like distinct responsibilities.

The interaction does not pretend that every artifact has only one possible use. Feedback explains
that classification is based on the artifact's primary job in this bounded decision.

## Purposeful interactions

| Interaction | Purpose | Required behavior | Why it belongs here |
| --- | --- | --- | --- |
| Meaning Triage Desk | Classify twelve utility artifacts by primary job | Keyboard and touch operation, immediate explanatory feedback, retry, progress preserved locally | Makes the five distinctions concrete through ordinary enterprise artifacts |
| Missing-Job Failure Trace | Remove a job and inspect where the answer fails | Five selectable failure states, visible source-to-answer propagation, reset, static reduced-motion equivalent | Demonstrates that different architecture failures require different repairs |
| Five-Layer Meaning Map Builder | Create the professional work product | Scenario-specific entries, live preview, deterministic completeness check, local save and export | Transfers vocabulary into a reviewable architecture decision |

## Assessment sequence

Assessment is distributed where the thinking occurs. It is not a repeated quiz inventory.

| Location | Assessment type | Cognitive job |
| --- | --- | --- |
| Opening | Consequential forced choice with explanation | Expose the learner's current mental model |
| After the five-job comparison | Relationship matching | Distinguish each question from its strongest distractor |
| Inside the Meaning Triage Desk | Controlled classification | Apply distinctions to real utility artifacts |
| After the semantic bridge | Hotspot or boundary selection | Identify whether meaning or mapping is broken |
| Inside the failure trace | Diagnose and repair | Select the first broken job and responsible owner |
| Final | Applied decision defense | Defend the Five-Layer Meaning Map against six transparent criteria |

The final check requires:

1. one bounded utility question;
2. one named source structure;
3. one classification artifact;
4. one shared concept and relationship;
5. one concept-to-source mapping;
6. one task-specific context need, plus one explicit limit.

The learner must also name the first unresolved gap and the person or role responsible for resolving
it. Passing this check does not approve an operational implementation.

## Professional work product

The sole work product is the **Five-Layer Meaning Map**. It becomes the architecture-distinction
section of the Utility Knowledge Spine Fieldbook.

It contains:

- the bounded utility question;
- one concrete artifact or responsibility for each of the five jobs;
- the accountable owner for each job;
- one unresolved gap;
- one boundary explaining what the map does not authorize.

Module 16 will create the full AI Context Contract. Module 05 includes only enough runtime context
to distinguish its job from the other four.

## Instructor explanation plan

| Major component | What the learner sees | What the learner does | What to notice | Utility meaning | Debrief |
| --- | --- | --- | --- | --- | --- |
| Pressure room | A physical event, four source systems, disputed terms, and a human decision | Make the opening choice and inspect the evidence | Data availability is not the same as shared meaning or authority | A dashboard can display an answer whose definition is still contested | Name the missing responsibility, not a favored tool |
| Five-job comparison | The same Zone 3 question shown through five distinct questions | Read across question, artifact, owner, and failure | The rows cooperate but do not collapse into one another | Architecture improves when each job has a named owner | Product labels vary, so govern the job and boundary |
| Meaning Triage Desk | Twelve realistic records, definitions, mappings, and controls | Classify, receive feedback, retry | File format does not reveal semantic job | A spreadsheet may hold a taxonomy, mapping, or runtime evidence | Use primary purpose in this scenario |
| Semantic bridge | A shared concept resolving to governed fields and current records | Trace and identify the broken boundary | Meaning is reusable; mappings connect that meaning to changing systems | A correct ontology can still return the wrong record if a mapping drifts | Test meanings and mappings separately |
| Context packet | A bounded task package around a model or agent | Add relevant items and reject excess | Time, permission, conflict, and output limits are part of context | Retrieving everything can increase risk and confusion | Better context improves grounding, not perfect determinism |
| Failure trace | One missing job changing into a downstream consequence | Remove a job and choose the repair point | The symptom appears late, while the cause begins earlier | Fix the first broken responsibility | Prompt changes cannot repair every upstream defect |
| Meaning Map | A reviewable one-page architecture decision | Complete, evaluate, revise, and defend | Named owners and limits make the map actionable | Teams can use it before selecting a platform | Local completion is not production approval |

## Explanatory visual plan

| Visual ID | Asset class | Teaching idea | Learner conclusion | Reading guide | Mobile and reduced-motion treatment |
| --- | --- | --- | --- | --- | --- |
| `mbm05-pressure-room` | Original editorial utility scene | A pressure event crosses physical assets, records, definitions, mappings, and authority | The answer needs several governed jobs, not one more table join | Begin at the pressure signal, move through the evidence desk, then stop at the named human decision | Recompose as three vertical scenes. All meaning remains in labels and static callouts. |
| `mbm05-five-job-comparison` | Governed comparison | Five terms answer five different questions | Distinguish by job, not vendor label | Read each row from question to failure, then compare owners | Cards replace columns on phone while preserving identical row order. |
| `mbm05-semantic-bridge` | Connection map | Shared meaning resolves to authoritative data through tested mappings | Ontology and semantic layer cooperate without being interchangeable | Start with the concept, cross the mapping bridge, inspect source fields, then check the current record | Vertical bridge on phone. No motion is needed to preserve meaning. |
| `mbm05-context-packet` | Packet anatomy | AI context is task-specific and bounded | Context includes evidence and controls, but excludes irrelevant or unauthorized material | Read the task envelope first, then evidence, definitions, policy, time, permission, conflicts, and limits | Accordion groups on phone. Static expanded alternative under reduced motion. |
| `mbm05-failure-trace` | Executable cause map | Each missing job produces a different failure and owner | Repair starts at the first broken boundary | Select a missing job, follow the highlighted consequence, and read the repair note | Selectable text sequence mirrors every path. Transitions are disabled under reduced motion. |

All five visuals are planned original OWOS assets or governed executable components. A card grid,
colored container, icon row, or generic node cloud will not count as any of these visuals.

## Written-first review

- Target conversational teaching text: 4,500 to 6,000 words.
- The complete explanation must remain understandable with every animation paused and every video
  removed.
- Technical terms appear only after the learner understands the ordinary-language job.
- Every major mechanism receives an introduction, reading guide, learner instruction, and debrief.
- The lesson uses water for the worked example, wastewater for guided transfer, and stormwater for
  independent transfer.
- No more than two full prose blocks appear consecutively without a visual, worked example,
  learner action, comparison, or instructor callout.

## Depth treatment

### Common route

The five questions, ordinary utility artifacts, failure modes, owners, and Five-Layer Meaning Map.

### Practitioner depth

Optional drawers show representative identifiers, fields, mapping tests, evidence references, and a
small RDF statement. No coding is required to complete the lesson.

### Leader decisions

Leaders assign accountable ownership, approve boundaries, fund the first broken capability, and
decide what evidence or review is required before operational use.

The three views share one narrative and one set of claims. They do not become three parallel pages.

## Accessibility and responsive behavior

- Every interaction works with keyboard, touch, and visible focus.
- Classification never relies on drag alone. Select-then-place and move controls are required.
- Every visual has a reading guide, full text alternative, and learner conclusion.
- Color is never the only signal for a job or result.
- Phone layouts preserve teaching order and do not shrink diagrams into unreadable thumbnails.
- Reduced motion preserves every state and consequence without autoplay.
- Graph and Community use responsive side drawers with focus return.
- The lesson includes an explicit `#owos-course-community` anchor before bottom navigation.
- Dark surfaces use verified light text.

## Module-specific FAQ plan

1. Is a semantic layer the same as an ontology?
2. Is a taxonomy enough for shared meaning?
3. Can a data model contain business definitions?
4. Is a prompt the same thing as AI context?
5. Does better context make an AI answer deterministic?
6. Does a knowledge graph replace the warehouse or lakehouse?
7. When is a governed table enough?

Each answer will use the Zone 3 example or one transfer case and will state where product terminology
or implementation choices may vary.

## Diversity check

- Module 04 is a relationship-discovery lab dominated by graph construction and path tracing.
- Module 05 is a decision room dominated by artifact triage, comparison, and failure diagnosis.
- Module 06 is a classification studio dominated by hierarchy repair and class-instance decisions.
- Module 05 will not use graph growth as its main visual, a taxonomy tree as its main interaction, or
  a repeated multiple-choice, matching, multi-select quiz sequence.
- Its professional artifact is an architecture distinction map, not a triple deck, mini-graph,
  vocabulary sheet, or full context contract.

## Approval gates

| Gate | Status | Reviewer | Note |
| --- | --- | --- | --- |
| Lesson contract | approved for design | Hardeep Anand | Approval recorded from the user's instruction to proceed |
| Evidence and claims | conditional | Course production | Independent semantic-architecture and utility review remain required |
| Narrative and storyboard | approved for golden build | Hardeep Anand | Explicit direction: "Approve module five. Go ahead!" |
| Visual plan | approved for golden build | Hardeep Anand | Original assets and executable failure trace authorized |
| Interactions and assessments | approved for golden build | Hardeep Anand | Meaning Triage Desk, failure trace, distributed checks, and Meaning Map authorized |
| Golden benchmark | approved at capability level | Hardeep Anand | Quality and instructional discipline govern production; composition reuse is prohibited |
| Release | blocked | Hardeep Anand | Separate release approval required |
