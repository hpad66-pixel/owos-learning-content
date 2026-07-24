# OWOS Module Design Brief

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-master-data-governance-001`, `dga001:17` |
| Working title | The screen is not the plant |
| Learner roles | Operators, asset stewards, OT engineers, model owners, leaders |
| Competencies | Separate physical, observed, model, and authority states; define twin action limits |
| Controlled sources | D10 course research; NIST CSF; CISA ICS; ISO 55000 overview |
| Evidence boundary | No command, safety case, cyber architecture, or twin certification |

## Learning job

The learner must block an unsafe recommendation when a twin conflicts with a verified isolation, reconstruct the state path, and define a governed control boundary.

## Concept-to-experience plan

| Teaching idea | Natural shape | Selected visual | Learner action | What becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
| One asset has several valid states | Layered evidence | `layered-stack` | Compare four states | Model confidence and operating authority are different | `operating-authority-sequencing` |
| Asset properties come from different systems | Relationship network | `network-diagram` | Trace identity and authority | No universal source answers every property | Applied defense |
| Twin use changes under degraded evidence | Instrument panel | `gauge-dial` | Triage incidents | Stop, degrade, or proceed decisions | Sequence check |

## Module design fingerprint

| Element | Selection |
| --- | --- |
| Lesson archetype | operational-twin-control-room |
| Signature mechanism | separate-asset-state-model-state-and-operating-authority |
| Narrative architecture | Plant conflict, four-state reconstruction, identity network, disagreement console |
| Intended learner feeling | Operational clarity and respect for field authority |
| Purposeful interaction | Twin disagreement triage |
| Explanatory visuals | `layered-stack`, `network-diagram`, `gauge-dial` |
| Assessment sequence | Command decision, incident triage, operating-authority sequencing, applied defense |
| Professional work product | OT and digital-twin control map |
| Role-sensitive treatment | Foundation, practitioner, leader |
| Graph and Community | Same-page drawers plus bottom connection |
| Persistence | Browser-only working artifact; no command or release event |

## Instructor explanation plan

| Component | Instructor job | Debrief |
| --- | --- | --- |
| Four-state stack | Keep physical, observed, model, and authority state distinct | Conflict is evidence |
| Asset identity network | Name source authority by property and time | Text similarity is not identity governance |
| Disagreement console | Explain stop, degrade, and approved operation | Confidence alone never grants authority |

## Visual pacing review

- A dark control-room rail anchors the lesson's mental model.
- Three different visual forms follow the three major teaching jobs.
- The worked reconstruction is placed before identity and telemetry detail.
- Mobile presentation stacks state panels and console outputs; reduced motion removes transitions.

## Explanatory graphic plan

| Idea | Visual shape | Arsenal pattern | Learner conclusion | Accessible treatment |
| --- | --- | --- | --- | --- |
| Four concurrent states | Stack | `layered-stack` | A digital description is not physical truth or permission | Text labels for every layer |
| Multi-system identity | Network | `network-diagram` | Authority varies by property | Relationship list remains readable |
| Degraded use | Dial console | `gauge-dial` | A twin can remain advisory after control is blocked | Buttons and aria-live advice |

## Learner FAQ plan

Six questions distinguish dashboard and twin, authority by property, direct control, missing telemetry, replacement identity, and shared ownership.

## Recording script

| Field | Decision |
| --- | --- |
| Script path | Not planned |
| Intended recording length | Not applicable |
| Spoken opening | Written lesson is authoritative |
| Visual directions | Included on page |
| Learner action | Save an OT and twin control map |

## Diversity check

- Chapter 16 is a commercial boundary negotiation; Chapter 18 is an AI release runway.
- This lesson uses a persistent control-room rail, three operational state visualizations, and an authority sequence.
- Quiz and interaction signatures are unique in the five-chapter batch.
- Shared navigation, drawers, persistence, and completion semantics are infrastructure.

## Approval

| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | pending | | | Operator, safety, OT, cyber, and source-owner review |
| Learning design | conditional | Codex working review | 2026-07-23 | Automated conformance required |
| Utility practice | pending | | | Independent plant practitioner review |
| Release | blocked | | | Not requested |
