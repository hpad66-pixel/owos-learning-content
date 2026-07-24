# Module 02 Design Brief: The Anatomy of a Triple

Status: approved for production under standing owner authorization
Build state: authorized on 2026-07-24

## Identity

| Field | Decision |
| --- | --- |
| Course and module ID | `owos-course-semantic-data-ai-001`, `mbm001:02` |
| Primary learner | Utility professional or leader without assumed RDF syntax experience |
| Secondary learner | Data, GIS, IT, OT, analytics, governance, and AI practitioner |
| Curriculum role | Formal statement foundation between Module 01 recognition and Module 03 identity adjudication |
| Learning job | Repair ambiguous or malformed triples and explain identifiers, resources, literal values, datatypes, labels, and direction |
| Controlled evidence | `SRC-001`; claims `CLM-001`, `CLM-012` |
| Boundary | The common route does not require memorizing Turtle, RDF-star, blank-node design, or advanced serialization features. |

## Opening situation

A laboratory result reaches an overflow-response dashboard as:

`Outfall 12 | has result | 7.2`

The statement looks complete. It is not. The team cannot tell whether Outfall 12 is the monitored
asset or the sampling location, whether 7.2 is pH, dissolved oxygen, turbidity, or another measure,
which unit applies, when the value was observed, or whether the phrase "Outfall 12" is an identifier
or only a display label.

The learner must choose the first corrected statement before the terms IRI, resource, literal,
datatype, and label are introduced.

## One learning job

The learner answers:

> What exactly belongs in each position of an RDF statement, and what evidence is lost when we put
> the wrong kind of thing there?

This lesson teaches precision inside statements. It does not repeat Module 01's graph recognition,
perform Module 03's identity adjudication, or teach production ontology modeling.

## Cognitive design

| Field | Decision |
| --- | --- |
| Prior knowledge | A triple has a subject, predicate, object, and direction. |
| Misconception | A triple is merely a three-column row whose values can be any convenient text. |
| Worked example | A wastewater sample observation linked to Outfall 12 and a typed pH value. |
| Guided practice | Repair reversed, overloaded, free-text, and incorrectly typed statements. |
| Independent transfer | Convert a stormwater inspection result and water work-order statement into precise triples. |
| Feedback model | Every repair explains the information preserved, the ambiguity removed, and the strongest tempting alternative. |
| Professional artifact | Reviewed Triple Deck with identifier, label, resource, literal, datatype, source, and review notes. |

## Narrative architecture

1. A plausible three-cell result fails professional review.
2. The learner opens the Triple Evidence Bench.
3. The instructor separates stable identity from human-readable labels.
4. The learner follows the object fork: another resource or a literal value.
5. The instructor shows why datatype and unit are not decoration.
6. The learner repairs four distinct defects.
7. The same statements appear in plain language, a graph view, and a small Turtle excerpt.
8. The learner produces and defends a Reviewed Triple Deck.

## Concept-to-experience plan

| Teaching idea | Natural shape | Planned visual | Learner action | Intended realization |
| --- | --- | --- | --- | --- |
| A plausible statement can discard measurement meaning | Annotated laboratory evidence scene | Sample-to-statement forensic strip | Inspect what the three-cell result omits | Three positions do not guarantee precision |
| Identifier and label perform different jobs | Specimen comparison | Identifier and label evidence cards | Decide which value survives a rename or language change | Identity should not depend on display text |
| An object may be another resource or a literal | Branching decision map | Resource-or-literal object fork | Route examples through the correct branch | The object position has two fundamentally different forms |
| Literal values need explicit type and often a unit relationship | Measurement anatomy | Typed-literal instrument panel | Repair number, date, boolean, and text examples | `"7.2"` and typed `7.2` are not equivalent evidence |
| Serialization changes notation, not the underlying graph | Translation strip | Plain language to graph to Turtle | Align the same statement across three views | Turtle is one readable notation, not the meaning itself |

## Signature mechanism

### Triple Evidence Bench

The learner receives four defective utility statements:

- a subject and object reversed;
- a display label used as permanent identity;
- a measurement packed into one free-text object;
- a numeric value stored without a datatype or unit relationship.

The learner inspects each position, replaces only the defective part, and sees the repaired statement
in plain language, graph form, and Turtle. A repair cannot pass until the learner explains what
evidence the change preserves.

## Visual and interaction distinction

Module 01 constructs and chains relationships. Module 02 behaves like a forensic syntax workbench:
specimen trays, value-type forks, measurement instruments, and side-by-side statement translations.
Module 03 will use an identity evidence board. Module 02 will not use Module 05's evidence desk,
five-job comparison, context packet, failure laboratory, or decision-room palette.

## Assessment sequence

| Location | Assessment job |
| --- | --- |
| Opening | Choose the statement that preserves the measurement claim |
| Identifier specimen | Distinguish identifier, label, and literal |
| Object fork | Route a resource object versus a literal object |
| Evidence Bench | Diagnose and repair four malformed triples |
| Serialization strip | Identify which notation change preserves the graph |
| Transfer | Repair a stormwater inspection statement |
| Final | Defend the Reviewed Triple Deck against transparent criteria |

## Reviewed Triple Deck

The artifact contains five reviewed statements, not ten repetitive form rows. Together they must
include:

- one resource-to-resource relationship;
- one typed number;
- one date or time;
- one human-readable label separated from identity;
- one source and reviewer note;
- one explicit boundary stating what the deck does not prove.

## Written-first and accessibility requirements

- Technical vocabulary follows the ordinary-language job.
- Every visual has a reading guide, complete text alternative, and conclusion.
- Repair controls work through selection and buttons, not drag alone.
- The complete lesson works without animation or video.
- Phone layout preserves the three statement positions and translation order without shrinking text.
- Reduced motion uses direct state changes.
- No more than two prose blocks appear without a visual, worked example, learner action, or debrief.

## Approval

| Gate | Status | Reviewer | Note |
| --- | --- | --- | --- |
| Lesson contract | approved for design | Hardeep Anand | Progressive production authorized |
| Narrative and storyboard | approved for production | Hardeep Anand | Standing progressive-production authorization |
| Visual and interaction plan | approved for production | Hardeep Anand | Syntax-workbench experience authorized |
| Evidence | conditional | Course production | Independent RDF review remains required |
| Release | blocked | Hardeep Anand | Separate approval required |
