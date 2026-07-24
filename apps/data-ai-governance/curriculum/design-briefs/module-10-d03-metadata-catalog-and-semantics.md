# OWOS Module Design Brief

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-master-data-governance-001`, `dga001:10` |
| Working title | A field name is not a meaning |
| Learner roles | Utility staff, data stewards, system owners, analysts, leaders |
| Competencies | Reconstruct meaning, map terms to fields, control semantic change |
| Controlled sources | Data Ready Before AI Ready v2.3 D03; W3C DCAT 3, SKOS, and PROV-O |
| Evidence boundary | Instructional Riverbend facts. No catalog certification, legal conclusion, or semantic-model approval. |

## Learning job

| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | An analyst wants to count inactive pumps from an undefined `status = 0` field. |
| What must the learner decide before teaching begins? | Whether to use the field or stop and reconstruct its meaning. |
| What professional consequence makes this matter? | A wrong interpretation changes reliability reporting and downstream decisions. |
| What should the learner be able to do afterward? | Connect a business concept to an authoritative field, owner, time rule, use, and change evidence. |
| What usable work product will the learner create? | Metadata and semantics record. |
| What evidence is required for completion? | Opening decision, catalog reconstruction, matching check, saved record, and applied defense. |

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| Similar field names can carry different meanings | Evidence comparison | `comparison-table` | Inspect candidate fields | Authority and decision fitness become visible | `matching` |
| Governed metadata adds meaning, use, and change control | Before and after | `before-after-slider` | Compare two catalog states | Missing connections become visible | Applied defense |
| A field implements a concept only for a stated use | Case reconstruction | Worked Riverbend evidence desk | Reconstruct the mapping | The pump count changes because interpretation changes | Matching |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | metadata-forensics |
| Signature mechanism | reconstruct-meaning-owner-source-and-use-from-catalog-evidence |
| Course visual language applied here | Evidence desk and catalog case file |
| Intended learner feeling | Healthy suspicion, then clarity |
| Narrative architecture | Disputed field, evidence reconstruction, controlled mapping, change review |
| Mental model | Meaning = definition + identity + authority + time + use + change |
| Purposeful interaction 1 | Catalog evidence reconstruction |
| Purposeful interaction 2 | Before and after semantic change review |
| Explanatory visuals, normally two to five | `comparison-table`, `before-after-slider` |
| Visual pacing plan and any prose exception | Visual or worked example follows each major teaching block |
| Original editorial illustration, when appropriate | Not used. The forensic table better fits the idea. |
| Assessment sequence and cognitive jobs | Opening judgment, relationship matching, applied defense |
| Distributed assessment locations | Opening, after case-file teaching, inside work-product studio |
| Final applied work-product check | Defend meaning, authority, use, and change evidence |
| Role-sensitive treatment | Foundation, practitioner, and leader views |
| Professional work product | Metadata and semantics record |
| Same-page Knowledge Graph behavior | Right drawer, focus return |
| Header Graph, Community, and Start actions | Present in course bar and hero |
| Bottom connected-learning section | Present before navigation |
| Explicit bottom `#owos-course-community` anchor before navigation | Present |
| Drawer focus return and mobile behavior | Shared course runtime; full-width drawer on phone |
| Module-specific FAQ location and disclosure behavior | Six semantic and catalog questions before evidence boundary |
| Animation and teaching purpose | Slider reveals the additional evidence connections |
| Reduced-motion equivalent | Immediate state change without transition |
| Mobile transformation | Single-column lesson and artifact fields |
| Persistence and learner events | Browser-only working artifact; release events disabled |

## Instructor explanation plan

| Major component | What the learner sees | What the learner does | What to notice | Utility meaning | Debrief needed |
| --- | --- | --- | --- | --- | --- |
| Metadata case table | Four candidate status fields | Inspect each row | Labels do not establish authority or fit | A decision needs governed meaning | Yes |
| Before and after view | Field-only and decision-aware catalog states | Move the divider | Meaning adds relationships and change evidence | Catalog depth matters more than raw coverage | Yes |
| Matching check | Utility objects and required metadata | Match pairs | Metadata follows the object’s decision job | The same profile does not fit every record | Immediate feedback |
| Work product | A structured semantic record | Write and save | Every claim needs an owner and boundary | The result can seed a governed catalog entry | Applied check |

## Written-first review

- Approximate conversational teaching words: more than 1,300.
- Worked utility example and marker: Riverbend pump-availability count, marked with `data-worked-example`.
- Misconception addressed: a familiar field name or recent timestamp is enough.
- Boundary or non-example: a field-only catalog does not establish semantic fitness.
- Component debriefs: visible after both major mechanisms.
- What remains if every video and animation is removed: the complete explanation, example, comparison, assessment, artifact, FAQ, and evidence boundary.

## Visual pacing review

- Longest run of consecutive full prose blocks: two.
- Visual, interaction, worked example, or callout used to break each dense section: evidence desk, worked example, table, slider, role row, artifact.
- Any uninterrupted prose exception and reason: none.
- Editorial illustration reading guide and learner conclusion, when used: not applicable.
- Dark-surface contrast plan: shared hero and drawer rules explicitly use white text.

## Explanatory graphic plan

| Teaching idea | Visual shape | Arsenal pattern | Learner conclusion | How the instructor explains it | Accessible and mobile treatment |
| --- | --- | --- | --- | --- | --- |
| Candidate field fitness | Comparison | `comparison-table` | Meaning and authority determine use | Read across from field to decision fit | Horizontally scrollable governed table |
| Metadata maturity | State comparison | `before-after-slider` | Governed meaning adds connected evidence | Compare syntax with decision context | Stacks and remains operable by touch |

## Learner FAQ plan

| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
| Must we buy a large catalog first? | Tool and governance are often confused | Start around material decisions | Pump availability fields | Case file | No product endorsement |
| Dictionary or glossary? | Both contain descriptions | Technical fields differ from business concepts | `OPS.available_flag` | Comparison | Local practice varies |
| Does ontology replace catalog? | Both manage meaning | They connect but do different jobs | Concept to field mapping | Relationship explanation | No architecture approval |
| Who approves definitions? | Steward and owner are confused | Steward maintains, owner approves material meaning | Availability definition | Role view | Authority is utility-specific |
| What if departments disagree? | Consensus can hide authority | Preserve proposals and escalate with consequence | Competing status definitions | Worked sequence | No legal conclusion |
| How is catalog quality measured? | Field counts look persuasive | Measure decision coverage and evidence | Regulatory critical fields | Comparison | Criteria require review |

## Recording script

| Field | Decision |
| --- | --- |
| Script path | Not planned |
| Intended recording length | Not applicable |
| Spoken opening | Written lesson is authoritative |
| Utility example | Riverbend pump availability |
| Visual directions | Included on-page |
| Learner action and work product | Metadata and semantics record |
| Transition to next lesson | From governed meaning to reproducible lineage |

## Diversity check

- Adjacent module reviewed: Chapter 09 authority simulation and Chapter 11 lineage reconstruction.
- Course Experience Brief reviewed: yes.
- Lesson archetype differs from adjacent modules: yes.
- Signature mechanism is unique to this lesson: yes.
- Opening pattern intentionally different: undefined field decision.
- Dominant visual intentionally different: forensic comparison.
- Interaction pair intentionally different: table inspection plus before and after.
- Quiz sequence intentionally different: opening judgment, matching, applied defense.
- Work-product format intentionally different: metadata case record.
- Any justified repetition: shared navigation, drawers, accessibility, and completion semantics only.
- Course-level distinctiveness result: blocked by unfinished Chapters 11 through 24, not by Chapter 10.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | pending | | | Source-owner review remains |
| Learning design | conditional | Codex working review | 2026-07-23 | Automated conformance targeted |
| Utility practice | pending | | | Practitioner review remains |
| Golden lesson benchmark, when applicable | not applicable | | | Chapter 09 remains capability benchmark |
