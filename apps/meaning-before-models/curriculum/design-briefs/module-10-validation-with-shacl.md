# OWOS Module Design Brief: Validation with SHACL

## Identity
| Field | Decision |
| --- | --- |
| Course and module ID | `owos-course-semantic-data-ai-001`, `mbm001:10` |
| Working title | Validation with SHACL |
| Learner roles | Utility staff, practitioners, and leaders |
| Competencies | Explain and apply the module mental model |
| Controlled sources | W3C RDF, RDFS, SPARQL, OWL, and SHACL standards as applicable |
| Evidence boundary | Instructional utility scenario; independent factual and practitioner review required |

## Learning job
| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | A pump record passes through the graph with no asset identifier, a sample has no unit, and an outfall inspection has no inspector role. |
| What must the learner decide before teaching begins? | What does a SHACL validation result establish? |
| What professional consequence makes this matter? | An implicit or unowned boundary can produce an indefensible utility answer. |
| What should the learner be able to do afterward? | Shapes Constraint Language expresses structural contracts and produces violations, warnings, and information for governed remediation. |
| What usable work product will the learner create? | Utility SHACL Contract |
| What evidence is required for completion? | Opening, mechanism lab, matching, boundary check, saved artifact, and applied assessment |

## Concept-to-experience plan
| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| Select a target | relationship or process | `shape-anatomy` | Inspect the utility example | A governed boundary becomes visible | multiple-choice |
| Apply constraints | relationship or process | `validation-report` | Inspect the utility example | A governed boundary becomes visible | multiple-choice |
| Read the report | relationship or process | `severity-matrix` | Inspect the utility example | A governed boundary becomes visible | multiple-choice |
| Route remediation | relationship or process | `remediation-swimlane` | Inspect the utility example | A governed boundary becomes visible | multiple-choice |

## Module design fingerprint
| Element | Selection |
| --- | --- |
| Narrative architecture | A pump record passes through the graph with no asset identifier, a sample has no unit, and an outfall inspection has no inspector role. |
| Mental model | Shapes Constraint Language expresses structural contracts and produces violations, warnings, and information for governed remediation. |
| Purposeful interaction 1 | Four-step mechanism laboratory |
| Purposeful interaction 2 | Governed artifact builder |
| Visual types, minimum four | `shape-anatomy`, `validation-report`, `severity-matrix`, `remediation-swimlane` |
| Visual pacing plan and any prose exception | Every teaching block is followed by a visual, decision, or learner action |
| Original editorial illustration, when appropriate | Included when `editorial-illustration` appears in the selected set |
| Quiz sequence, minimum three types | `matching`, `multi-select`, `ordering` plus `flip-cards` retrieval practice and `applied-assessment` |
| Distributed assessment locations | Opening, mechanism section, boundary section, and work-product section |
| Final applied work-product check | Deterministic eight-field artifact review |
| Role-sensitive treatment | Foundation, Practitioner, and Leader lenses |
| Professional work product | Utility SHACL Contract |
| Same-page Knowledge Graph behavior | `network-diagram` with source, concept, relationship, role, and competency nodes |
| Header Graph, Community, and Start actions | Required compact header controls |
| Bottom connected-learning section | Graph and Community cards before navigation |
| Explicit bottom `#owos-course-community` anchor before navigation | Required |
| Drawer focus return and mobile behavior | Focus return and full-width mobile drawers |
| Module-specific FAQ location and disclosure behavior | Five questions before evidence boundary |
| Animation and teaching purpose | Step selection reveals controlled sequence |
| Reduced-motion equivalent | Every state is available by direct selection |
| Mobile transformation | Grids stack and wide comparisons scroll |
| Persistence and learner events | Local draft and completion cache; production events disabled |

## Instructor explanation plan
| Major component | What the learner sees | What the learner does | What to notice | Utility meaning | Debrief needed |
| --- | --- | --- | --- | --- | --- |
| Opening decision | Utility scenario | Choose and retry | Explicit evidence boundary | Decisions need reviewable meaning | Yes |
| Visual set | Four visual shapes | Read and compare | Different controls perform different jobs | Architecture follows the question | Yes |
| Mechanism lab | Four steps | Select all steps | Each step adds evidence or control | Missing steps propagate failure | Yes |
| Work product | Eight fields | Save and evaluate | Specificity and authority | Artifact supports cross-team review | Yes |

## Visual pacing review
- Longest run of consecutive full prose blocks: two.
- Visual, interaction, worked example, or callout used to break each dense section: yes.
- Any uninterrupted prose exception and reason: none.
- Editorial illustration reading guide and learner conclusion, when used: required.
- Dark-surface contrast plan: explicit white or light text.

## Explanatory graphic plan
| Teaching idea | Visual shape | Arsenal pattern | Learner conclusion | How the instructor explains it | Accessible and mobile treatment |
| --- | --- | --- | --- | --- | --- |
| Select a target | shape-anatomy | Shared component gallery | Shapes Constraint Language expresses structural contracts and produces violations, warnings, and information for governed remediation. | Read from the first boundary to the controlled result | Text guide, conclusion, responsive layout |
| Apply constraints | validation-report | Shared component gallery | Shapes Constraint Language expresses structural contracts and produces violations, warnings, and information for governed remediation. | Read from the first boundary to the controlled result | Text guide, conclusion, responsive layout |
| Read the report | severity-matrix | Shared component gallery | Shapes Constraint Language expresses structural contracts and produces violations, warnings, and information for governed remediation. | Read from the first boundary to the controlled result | Text guide, conclusion, responsive layout |
| Route remediation | remediation-swimlane | Shared component gallery | Shapes Constraint Language expresses structural contracts and produces violations, warnings, and information for governed remediation. | Read from the first boundary to the controlled result | Text guide, conclusion, responsive layout |

## Learner FAQ plan
| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| How does SHACL apply? | New term | It performs one named job in the module mental model. | A pump record passes through the graph with no asset identifier, a sample has no unit, and an outfall inspection has no inspector role. | Selected module visuals | Instructional scenario |
| How does shape apply? | New term | It performs one named job in the module mental model. | A pump record passes through the graph with no asset identifier, a sample has no unit, and an outfall inspection has no inspector role. | Selected module visuals | Instructional scenario |
| How does target apply? | New term | It performs one named job in the module mental model. | A pump record passes through the graph with no asset identifier, a sample has no unit, and an outfall inspection has no inspector role. | Selected module visuals | Instructional scenario |
| How does constraint apply? | New term | It performs one named job in the module mental model. | A pump record passes through the graph with no asset identifier, a sample has no unit, and an outfall inspection has no inspector role. | Selected module visuals | Instructional scenario |
| How does severity apply? | New term | It performs one named job in the module mental model. | A pump record passes through the graph with no asset identifier, a sample has no unit, and an outfall inspection has no inspector role. | Selected module visuals | Instructional scenario |

## Recording script
| Field | Decision |
| --- | --- |
| Script path | `curriculum/scripts/module-10-validation-with-shacl-video-script.md` |
| Intended recording length | 25 to 35 minutes |
| Spoken opening | A pump record passes through the graph with no asset identifier, a sample has no unit, and an outfall inspection has no inspector role. |
| Utility example | Module scenario and work product |
| Visual directions | Follow the four selected visual patterns |
| Learner action and work product | Complete Utility SHACL Contract |
| Transition to next lesson | Continue through the approved course sequence |

## Diversity check
- Adjacent module reviewed: yes.
- Opening pattern intentionally different: scenario and decision are module-specific.
- Dominant visual intentionally different: selected from the course design matrix.
- Interaction pair intentionally different: content and mechanism follow this module.
- Quiz sequence intentionally different: content and placement are module-specific.
- Work-product format intentionally different: Utility SHACL Contract.
- Any justified repetition: shared Graph, Community, accessibility, and completion controls.

## Approval
| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | conditional | Codex repository review | 2026-07-23 | Independent review required |
| Learning design | production candidate | Hardeep direction | 2026-07-23 | Full course production authorized |
| Utility practice | pending | | | Practitioner review required |
| Golden lesson benchmark, when applicable | working benchmark | Hardeep direction | 2026-07-23 | Module 05 capability level applied |
| Release | blocked | | | Separate approval required |
