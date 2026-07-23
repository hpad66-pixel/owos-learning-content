# Module 05 Recording Script: Five Layers of Meaning

Status: golden-lesson recording candidate

Estimated recording length: 30 to 35 minutes

## Scene 1: Pressure event

### Spoken words

It is 2:10 in the morning. A pressure event affects Zone 3.

The question sounds simple. Which active customers may be exposed, which policy applies at this
time, and what may the agent propose?

The customer system knows accounts. GIS knows premises and pressure zones. SCADA knows the pressure
event. The policy system knows approved procedures. None of those systems, by itself, defines the
whole question.

### Visual direction

[Show the evidence desk with SCADA, GIS, CIS, policy, and agent records. Keep disagreement visible.]

## Scene 2: Five questions

### Spoken words

Here is the easiest way to separate five terms that are often blended.

A data model answers: how is information structured here?

A taxonomy answers: how are terms classified?

An ontology answers: what do the concepts and relationships mean across systems?

A semantic layer answers: how does that shared meaning resolve to enterprise data and metrics?

AI context answers: what does the model or agent need for this task now?

A context engine assembles the context. It is not the context itself.

### Visual direction

[Reveal the five columns one at a time. Keep the governing question above every column.]

## Scene 3: Classify by job

### Spoken words

Now classify the artifacts by their primary job.

The account table is a data model artifact. The customer-class hierarchy is a taxonomy. The
statement that an account serves a premise belongs to the shared ontology. The mapping from CIS
status code A and the effective-date rule belongs to the semantic layer. The packet containing the
event, current policy, permission, and output limits is runtime AI context.

One artifact may participate in several layers. What matters here is the job it performs.

### Visual direction

[Demonstrate the first sorter item, then let the learner complete the remaining items.]

## Scene 4: Follow one customer

### Spoken words

Follow Account 882.

The source models provide the fields and keys. The taxonomy classifies the account as a critical
facility. The ontology states that the account serves a premise, the premise is in a zone, and the
event affects the zone.

The semantic layer resolves those concepts to approved CIS, GIS, SCADA, and policy records.

The context engine checks identity, time, source authority, policy, permissions, conflicts, and
output limits. It supplies the model with a bounded task package.

The model may draft the review. It may not issue the advisory.

### Visual direction

[Step through the source-to-context flow. End at named human authority.]

## Scene 5: Break the architecture

### Spoken words

Remove the ontology and “active customer” becomes a local guess.

Keep the ontology but remove the semantic mappings, and the definition remains trapped in a file.

Remove runtime context, and the model may use the wrong policy, ignore the event time, expose
restricted information, or propose an unauthorized action.

Every job must be performed somewhere. That does not mean every job belongs in one product.

### Visual direction

[Use the failure lab. Reveal one consequence and repair at a time.]

## Scene 6: Assemble context

### Spoken words

Good context is not every record you can find.

For this task, include the resolved event and zone, event time, freshness rules, active-account
definition, approved mappings, current policy, user permission, known conflicts, and output limits.

Do not include unrelated billing notes. Do not give the model permission to issue the advisory.

Good context can reduce ambiguity and unsupported generation. It cannot guarantee that a generative
model will always be correct or perfectly repeatable.

### Visual direction

[Build the context packet. Show required, prohibited, and unresolved items.]

## Scene 7: Work product and close

### Spoken words

Choose one bounded utility question and complete the Five-Layer Meaning Map.

Name the source structure. Name the categories. Name the shared concepts and relationships. Name the
mappings and authoritative sources. Then state what the runtime context must contain and who reviews
each decision.

The map is not production approval. It is a reviewable statement of what your architecture must do.

Module Six takes the next step and builds shared vocabulary, taxonomy, and RDF Schema.

### Visual direction

[Show the completed customer-exposure map, then transition to the learner's builder.]
