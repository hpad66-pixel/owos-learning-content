# Module 09 Design Brief: Reasoning and Inference with OWL

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-course-semantic-data-ai-001`, `mbm001:09` |
| Working title | Reasoning and Inference with OWL |
| Learner roles | Non-technical staff, operators, ontology stewards, data and AI practitioners, utility leaders |
| Competencies | Distinguish assertion, inference, prediction, and authority; reconstruct and bound an OWL proof path |
| Controlled sources | W3C OWL 2 Overview, Primer, Profiles; W3C RDF Semantics |
| Evidence boundary | Instructional utility cases demonstrate logic patterns, not operating facts, causation, or permission to act |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | A graph classifies Pump P-104 as a critical service asset before a morning coordination call. |
| What must the learner decide before teaching begins? | Whether the displayed facts entail the classification or only make it sound plausible. |
| What professional consequence makes this matter? | An unsupported inference can be mistaken for observation, diagnosis, or operating authority. |
| What should the learner be able to do afterward? | Inspect premises and axioms, explain an entailment, find the first unsupported leap, and define a human stop condition. |
| What usable work product will the learner create? | Inference Case File |
| What evidence is required for completion? | Opening verdict, rule switchboard, proof challenge, saved case file, applied review |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| Assertion, axiom, inference | Evidence lanes | `network-diagram` | Read source, rule, and result separately | Provenance of the conclusion remains visible | `inference-verdict` |
| Subclass, inverse, and property-chain reasoning | Rule switchboard | Interactive proof sheet | Activate all three rules | Premises and conclusions change beside the active axiom | `rule-path` |
| Inference versus causal or action overclaim | Escalating chain | `failure-propagation-chain` | Find unsupported steps | The exact logical boundary becomes visible | `counterexample-check` |
| Transfer to work | Case file | Review artifact | Document a utility inference | Evidence, proof, and authority boundary become inspectable | `applied-assessment` |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | Inference courtroom |
| Signature mechanism | OWL rule switchboard with visible proof path |
| Course visual language applied here | Paper case file, evidence lanes, courtroom cross-examination |
| Intended learner feeling | “I can see exactly why this follows, and exactly where it stops.” |
| Narrative architecture | Contested claim, doctrine, demonstration, cross-examination, case filing |
| Mental model | Premises plus applicable axiom produce an entailment, not authority |
| Purposeful interaction 1 | `owl-rule-switchboard` |
| Purposeful interaction 2 | `counterexample-cross-examination` |
| Explanatory visuals, normally two to five | `network-diagram`, `failure-propagation-chain`, contextual evidence lanes |
| Visual pacing plan and any prose exception | Every major doctrine segment is followed by a visible proof, chain, or decision |
| Original editorial illustration, when appropriate | Circular contested-claim seal and case docket composition |
| Assessment sequence and cognitive jobs | `inference-verdict`, `rule-path`, `counterexample-check`, `applied-assessment` |
| Distributed assessment locations | Opening, rule demonstration, boundary challenge, professional transfer |
| Final applied work-product check | Deterministic completeness check against the Inference Case File |
| Role-sensitive treatment | Foundation, practitioner, and leader lenses plus operator, steward, and sponsor cards |
| Professional work product | Inference Case File |
| Same-page Knowledge Graph behavior | Drawer exposes concept, source, relationship, role, competency |
| Header Graph, Community, and Start actions | Present and keyboard reachable |
| Bottom connected-learning section | Case vocabulary and peer cross-examination prompts |
| Explicit bottom `#owos-course-community` anchor before navigation | Present |
| Drawer focus return and mobile behavior | Shared fieldbook behavior; one-column mobile courtroom |
| Module-specific FAQ location and disclosure behavior | Six OWL questions before the evidence boundary |
| Animation and teaching purpose | State changes are learner-triggered; no decorative autoplay |
| Reduced-motion equivalent | All proof changes appear immediately as text |
| Mobile transformation | Courtroom, lanes, and rule switchboard collapse to one column |
| Persistence and learner events | Local completion and artifact state through shared fieldbook |

## Instructor explanation plan

| Major component | What the learner sees | What the learner does | What to notice | Utility meaning | Debrief needed |
| --- | --- | --- | --- | --- | --- |
| Opening claim | Critical-asset classification | Issue preliminary verdict | Plausibility is not entailment | Do not let labels become proof | Yes |
| Rule switchboard | Three proof paths | Activate and compare rules | Axiom name stays beside result | Reproducible reasoning | Yes |
| Cross-examination | Relationship-to-action chain | Select unsupported claims | Causation and authority exceed the path | Safety boundary | Yes |
| Case file | Review form and preview | Document one inference | Assertions and inferences remain separate | Governed handoff | Yes |

## Written-first review

- Approximate conversational teaching words: 2,000
- Worked utility example and marker: Pump P-104, Zone 3, Hospital H-7; `data-worked-example`
- Misconception addressed: OWL reasoning is a machine guess or an action authorization.
- Boundary or non-example: Property-chain support does not prove causation.
- Component debriefs: Visible after rule and failure-chain sections.
- What remains if every video and animation is removed: Full explanation, proof paths, boundary examples, assessment, work product, FAQs, and sources.

## Visual pacing review

- Longest run of consecutive full prose blocks: Two paragraphs.
- Visual, interaction, worked example, or callout used to break each dense section: Case banner, network, switchboard, failure chain, role court.
- Any uninterrupted prose exception and reason: OWL vocabulary section remains compact so terms can be read together.
- Editorial illustration reading guide and learner conclusion, when used: Contested-claim seal is interpreted by the opening instructor text.
- Dark-surface contrast plan: Shared drawer rule and proof surfaces use explicit light text.

## Explanatory graphic plan

| Teaching idea | Visual shape | Arsenal pattern | Learner conclusion | How the instructor explains it | Accessible and mobile treatment |
| --- | --- | --- | --- | --- | --- |
| Source, rule, result | Three evidence lanes | `network-diagram` | Inferred is not asserted | Read color and labels, not color alone | Text labels; stacks on mobile |
| Unsupported escalation | Five-stage chain | `failure-propagation-chain` | Relationship, causation, and action differ | Stop at first unsupported claim | Ordered text boxes |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| Is an inference true in the real world? | Logic and evidence fitness are conflated | It follows from supplied facts and axioms; sources can still be wrong | P-104 class mapping | Proof path | Local facts require review |
| Is this prediction? | Both create new statements | OWL entails; ML estimates | Critical asset versus failure probability | Comparison in prose | Model behavior varies |
| Why is missing not false? | Database habits | Open world preserves unknown | Backup pump not recorded | Doctrine section | Explicit negatives need policy |
| Can OWL operate equipment? | Correctness is mistaken for authority | No | Pump shutdown | Failure chain | Human authority required |
| Do we need full OWL? | More expressivity sounds better | Select the profile for the reasoning job | Large utility asset graph | Rule switchboard | Performance requires testing |
| How are inferences stored? | Materialization choices vary | Query or materialize with provenance and version | Cached criticality | Case file | Cache invalidation required |

## Recording script

| Field | Decision |
| --- | --- |
| Script path | `curriculum/scripts/module-09-reasoning-and-inference-with-owl-video-script.md` |
| Intended recording length | 12 to 15 minutes if recorded |
| Spoken opening | “The claim sounds sensible. Show me the rule.” |
| Utility example | P-104, Zone 3, H-7 |
| Visual directions | Reveal asserted, axiom, inferred; then expose unsupported causal and action steps |
| Learner action and work product | Run proof paths and complete Inference Case File |
| Transition to next lesson | Reasoning can derive; SHACL checks required graph content |

## Diversity check

- Adjacent module reviewed: Module 08 SPARQL query experience and Module 10 inspection station.
- Course Experience Brief reviewed: Yes.
- Lesson archetype differs from adjacent modules: Yes, inference courtroom.
- Signature mechanism is unique to this lesson: Yes.
- Opening pattern intentionally different: Contested classification.
- Dominant visual intentionally different: Proof lanes and courtroom case.
- Interaction pair intentionally different: Rule activation and cross-examination.
- Quiz sequence intentionally different: `inference-verdict` → `rule-path` → `counterexample-check` → `applied-assessment`.
- Work-product format intentionally different: Inference Case File.
- Any justified repetition: Shared navigation, drawers, completion, and evidence controls only.
- Course-level distinctiveness result: Diagnostic required after full-course retrofit.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | conditional | Codex working review | 2026-07-23 | W3C sources used; factual review still human-controlled |
| Learning design | passed | Codex working review | 2026-07-23 | Distinct courtroom architecture implemented |
| Utility practice | pending |  |  | Practitioner review required |
| Golden lesson benchmark, when applicable | not applicable |  |  | Not the approved golden lesson |
