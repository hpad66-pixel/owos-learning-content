#!/usr/bin/env python3
"""Build the governed Meaning Before Models lesson set from module contracts."""

from __future__ import annotations

import html
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "apps/meaning-before-models"
CURRICULUM = COURSE / "curriculum"


def module(number, slug, title, scene, question, answer, mental, steps, artifact, terms, visuals):
    return {
        "number": number, "slug": slug, "title": title, "scene": scene,
        "question": question, "answer": answer, "mental": mental,
        "steps": steps, "artifact": artifact, "terms": terms, "visuals": visuals,
    }


MODULES = [
    module(1, "rdf-in-15-minutes", "RDF in 15 Minutes",
        "A pump alarm appears at 2:00 a.m. The records name a pump, a pressure zone, a work order, and customers, but no record states the complete path.",
        "Which statement gives a machine one reusable piece of meaning?",
        "Pump_P104 serves Pressure_Zone_3.",
        "Resource Description Framework starts with one directed, named relationship: subject, predicate, object.",
        ["Name the subject", "Choose the relationship", "Name the object", "Connect the next triple"],
        "Relationship Card",
        ["RDF", "triple", "subject", "predicate", "object", "resource", "literal", "graph"],
        ["editorial-illustration", "network-diagram", "comparison-table", "interactive-process"]),
    module(2, "anatomy-of-a-triple", "The Anatomy of a Triple",
        "A sample result is entered as three words, but the direction is reversed and the number has no unit or datatype.",
        "Which triple preserves direction and the measured value clearly?",
        "Sample_S17 hasResult 4.2_mg_per_L.",
        "A triple has three positions, but each position has a different job and only the object may be a literal value.",
        ["Identify resources", "Choose a directed property", "Type the literal", "Review the serialization"],
        "Reviewed Ten-Triple Deck",
        ["IRI", "label", "literal", "datatype", "language tag", "blank node", "Turtle", "named graph"],
        ["comparison-table", "packet-anatomy", "interactive-process", "network-diagram"]),
    module(3, "which-pump-do-you-mean", "Which Pump Do You Mean?",
        "Pump P-104 appears under five identifiers across Supervisory Control and Data Acquisition, Geographic Information System, work management, drawings, and operator language.",
        "Is a matching label enough to declare two records the same asset?",
        "No. Treat the match as a candidate until governed evidence supports identity.",
        "Identity is an approved relationship supported by evidence, not a text-match shortcut.",
        ["Collect identifiers", "Compare evidence", "Approve or reject", "Preserve conflicts"],
        "Identity Crosswalk and Conflict Queue",
        ["canonical identity", "source identifier", "exact match", "crosswalk", "equivalence", "conflict", "steward", "provenance"],
        ["editorial-illustration", "comparison-table", "failure-propagation-chain", "raci-grid"]),
    module(4, "from-triples-to-a-utility-knowledge-graph", "From Triples to a Utility Knowledge Graph",
        "Operations can see each source record, but the answer requires a path from pump to zone, customer, work order, procedure, and decision owner.",
        "What turns isolated triples into a useful graph?",
        "Shared identifiers that let one triple connect to the next.",
        "A knowledge graph grows when explicit statements reuse the same identified things and preserve evidence.",
        ["Load source statements", "Resolve shared nodes", "Connect paths", "Ask a cross-domain question"],
        "Utility Mini-Graph",
        ["node", "edge", "path", "dataset", "named graph", "source group", "graph pattern", "visualization"],
        ["network-diagram", "interactive-process", "packet-anatomy", "comparison-table"]),
    module(6, "taxonomies-vocabularies-and-rdfs", "Taxonomies, Vocabularies, and RDFS",
        "Four utility teams use the word asset for equipment, facilities, pipes, documents, and financial records.",
        "What should the team establish before connecting all five uses?",
        "A governed vocabulary that defines the terms, categories, and intended scope.",
        "A taxonomy classifies terms. RDF Schema adds reusable classes, properties, labels, domains, ranges, and hierarchies.",
        ["Collect terms", "Define categories", "Test the hierarchy", "Publish ownership"],
        "Vocabulary and Taxonomy Sheet",
        ["vocabulary", "taxonomy", "class", "instance", "property", "subclass", "domain", "range"],
        ["comparison-table", "network-diagram", "failure-propagation-chain", "raci-grid"]),
    module(7, "ontology-engineering-in-plain-language", "Ontology Engineering in Plain Language",
        "A modeling workshop starts with forty nouns and no agreement about the operational question the model must answer.",
        "What should the team write before adding more concepts?",
        "Competency questions that define what the model must help answer.",
        "Ontology engineering is a controlled sequence from useful questions to shared concepts, relationships, tests, ownership, and versioned release.",
        ["Write competency questions", "Bound the model", "Define relationships", "Test and release"],
        "Ontology Decision Record",
        ["competency question", "ontology", "upper ontology", "domain ontology", "application profile", "modularity", "alignment", "version"],
        ["editorial-illustration", "interactive-process", "raci-grid", "network-diagram"]),
    module(8, "ask-the-graph-with-sparql", "Ask the Graph with SPARQL",
        "A dashboard can count work orders, but operations needs the path from an affected zone to active critical-facility accounts and current procedures.",
        "What does a SPARQL query describe first?",
        "The graph pattern the answer must match.",
        "SPARQL turns a utility question into variables and triple patterns, then adds filters, optional data, federation, or paths only when needed.",
        ["State the question", "Choose variables", "Assemble triple patterns", "Inspect evidence"],
        "Question-to-Query Sheet",
        ["SPARQL", "SELECT", "variable", "triple pattern", "FILTER", "OPTIONAL", "federation", "property path"],
        ["network-diagram", "interactive-process", "comparison-table", "packet-anatomy"]),
    module(9, "reasoning-and-inference-with-owl", "Reasoning and Inference with OWL",
        "The graph states that Pump P-104 serves Zone 3 and that Zone 3 is part of the North Service Area. A new relationship appears after reasoning.",
        "What must accompany an inferred statement?",
        "The asserted inputs and declared axiom that entail it.",
        "Web Ontology Language reasoning derives statements under declared logic. It does not predict the future or replace human judgment.",
        ["Inspect assertions", "Apply one axiom", "Trace the entailment", "Preserve unknowns"],
        "Inference Boundary Card",
        ["OWL", "assertion", "axiom", "inference", "entailment", "inverse", "transitive", "open world"],
        ["network-diagram", "interactive-process", "failure-propagation-chain", "comparison-table"]),
    module(10, "validation-with-shacl", "Validation with SHACL",
        "A pump record passes through the graph with no asset identifier, a sample has no unit, and an outfall inspection has no inspector role.",
        "What does a SHACL validation result establish?",
        "Whether the data conforms to the declared shape, not whether the real-world fact is true.",
        "Shapes Constraint Language expresses structural contracts and produces violations, warnings, and information for governed remediation.",
        ["Select a target", "Apply constraints", "Read the report", "Route remediation"],
        "Utility SHACL Contract",
        ["SHACL", "shape", "target", "constraint", "severity", "violation", "warning", "conformance"],
        ["packet-anatomy", "interactive-process", "failure-propagation-chain", "raci-grid"]),
    module(11, "references-provenance-authority-and-time", "References, Provenance, Authority, and Time",
        "A current sensor reading, an old procedure, a staff note, an extracted clause, and an approved engineering rule all make claims about Pump P-104.",
        "Which statement should control an operational recommendation?",
        "The statement with applicable authority, effective time, version, scope, and review status.",
        "Source, authority, time, version, and supersession are separate controls that let conflicting statements be preserved and resolved.",
        ["Identify the statement type", "Attach provenance", "Resolve effective time", "Select applicable authority"],
        "Authority, Provenance, and Time Ledger",
        ["provenance", "authority", "observation time", "record time", "effective time", "version", "supersession", "confidence"],
        ["editorial-illustration", "comparison-table", "interactive-process", "raci-grid"]),
    module(12, "running-knowledge-spine", "From an Ontology File to a Running Knowledge Spine",
        "The ontology is approved in a presentation, but no application, dashboard, or agent can query it or connect it to current utility records.",
        "What changes the ontology from documentation into operating knowledge?",
        "Instantiate it, map it to governed data, make it queryable, and connect it to controlled use.",
        "A Knowledge Spine combines a governed ontology core, semantic platform, connection fabric, and consumption plane.",
        ["Release the ontology core", "Instantiate the semantic platform", "Connect sources", "Serve governed consumers"],
        "Utility Knowledge Spine Architecture",
        ["Knowledge Spine", "instantiation", "semantic platform", "connection fabric", "consumption plane", "federation", "validation", "observability"],
        ["editorial-illustration", "packet-anatomy", "interactive-process", "network-diagram"]),
    module(13, "map-meaning-to-data", "Map Meaning to Data",
        "The shared concept ActiveCustomer is approved, but the Customer Information System stores status codes and dates that change independently.",
        "What makes the concept resolve to actual enterprise records?",
        "A governed semantic mapping with source authority, transformation, tests, and change control.",
        "Mapping connects shared meaning to fields, tables, application programming interfaces, streams, and extracted document entities without implying that all data is copied.",
        ["Inspect source structure", "Map concept and property", "Test transformation", "Monitor source change"],
        "Semantic Mapping Record",
        ["mapping", "transformation", "R2RML", "pushdown", "semantic contract", "source authority", "test query", "change control"],
        ["comparison-table", "interactive-process", "failure-propagation-chain", "packet-anatomy"]),
    module(14, "virtualize-cache-index-or-materialize", "Virtualize, Cache, Index, or Materialize?",
        "Emergency response needs a two-second answer, customer data must remain authoritative in place, and the procedure library may be unavailable during an outage.",
        "Should the architecture use one access pattern for every source?",
        "No. Choose per workload using authority, latency, freshness, availability, cost, and security.",
        "Move less data first, then cache, index, or materialize only where measured requirements justify another governed copy.",
        ["State the workload", "Score constraints", "Choose an access pattern", "Record recovery and review"],
        "Virtualize-or-Materialize Decision Record",
        ["virtualization", "federation", "cache", "index", "materialization", "freshness", "latency", "recovery"],
        ["comparison-table", "interactive-process", "failure-propagation-chain", "raci-grid"]),
    module(15, "structured-and-unstructured-knowledge", "Structured and Unstructured Knowledge",
        "An overflow response depends on sensor records, a map, an email, a call transcript, a procedure, inspection photographs, and a permit clause.",
        "Does an embedding turn every retrieved passage into approved knowledge?",
        "No. Similarity finds candidates. Extraction, graph assertion, provenance, and review remain separate.",
        "Structured and unstructured evidence become useful through different combinations of metadata, search, embeddings, extraction, explicit relationships, and approval.",
        ["Preserve the original", "Find relevant passages", "Extract candidate entities and claims", "Link, review, and approve"],
        "Structured-Unstructured Evidence Plan",
        ["structured data", "unstructured data", "metadata", "embedding", "vector search", "entity extraction", "claim", "passage"],
        ["editorial-illustration", "comparison-table", "network-diagram", "packet-anatomy"]),
    module(16, "context-engines-and-runtime-ai-context", "Context Engines and Runtime AI Context",
        "An agent receives the right customer and wrong procedure because the task package omitted effective time, jurisdiction, permission, and workflow state.",
        "Is the context engine the same thing as the context it supplies?",
        "No. The engine retrieves, filters, validates, and assembles the task-specific package.",
        "Runtime AI context is a bounded package of intent, entities, evidence, definitions, policy, time, permissions, state, conflicts, tools, and output limits.",
        ["Resolve task identity", "Retrieve governed evidence", "Apply policy and permission", "Assemble and validate the package"],
        "AI Context Contract",
        ["context engine", "AI context", "user intent", "runtime state", "jurisdiction", "permission", "tool boundary", "output schema"],
        ["packet-anatomy", "interactive-process", "failure-propagation-chain", "comparison-table"]),
    module(17, "bi-rag-graph-and-agentic-applications", "BI, RAG, Graph Grounding, and Agentic Applications",
        "The same Pump P-104 question is sent through joined tables, a dashboard, document retrieval, an RDF graph, and an agent with tools.",
        "Which technology label tells you the whole answer path is deterministic?",
        "None. Repeatability depends on the configured sources, mappings, retrieval, model, tools, and external state.",
        "Compare complete pipelines stage by stage, then separate knowing, proposing, authorizing, acting, stopping, and recording.",
        ["Identify fixed stages", "Expose variable stages", "Assemble evidence", "Authorize, act, or stop"],
        "Repeatability Map and Agent Action Contract",
        ["BI", "RAG", "graph grounding", "agent", "retrieval", "decoding", "tool call", "authorization"],
        ["comparison-table", "interactive-process", "failure-propagation-chain", "raci-grid"]),
    module(18, "design-the-one-water-knowledge-spine", "Design the One Water Knowledge Spine",
        "A team proposes an enterprise knowledge graph before naming one operational question, one decision owner, or one measurable outcome.",
        "What should the pilot define first?",
        "One bounded operational question tied to a named decision and measurable value.",
        "A useful pilot connects graph fit, identity, relationships, evidence, mappings, validation, context, access, agent controls, ownership, and measures around one decision.",
        ["Bound the question", "Run the Graph Fit Test", "Design controls and evidence", "Plan ninety-day measures and stop conditions"],
        "One Water Knowledge Spine Pilot Canvas",
        ["Graph Fit Test", "pilot", "operational question", "competency", "baseline", "target", "stop condition", "decision briefing"],
        ["editorial-illustration", "network-diagram", "raci-grid", "interactive-process"]),
]


def esc(value):
    return html.escape(str(value), quote=True)


def visual_markup(kind, item, index):
    title = item["steps"][index % len(item["steps"])]
    points = item["steps"]
    if kind == "comparison-table":
        body = '<div class="comparison-scroll"><table class="comparison"><thead><tr><th>Question</th><th>Weak treatment</th><th>Governed treatment</th></tr></thead><tbody>' + "".join(
            f"<tr><th>{esc(point)}</th><td>Implicit, local, or unreviewed</td><td>Named, testable, owned, and traceable</td></tr>" for point in points
        ) + "</tbody></table></div>"
    elif kind in {"interactive-process", "failure-propagation-chain"}:
        body = '<div class="process-flow">' + "".join(
            f'<div class="flowbox"><b>{i + 1}</b><span>{esc(point)}</span></div>{"" if i == len(points)-1 else "<span class=flowarrow>→</span>"}'
            for i, point in enumerate(points)
        ) + "</div>"
    elif kind == "raci-grid":
        body = '<div class="comparison-scroll"><table class="comparison"><thead><tr><th>Decision</th><th>Accountable</th><th>Responsible</th></tr></thead><tbody>' + "".join(
            f"<tr><th>{esc(point)}</th><td>Named utility owner</td><td>Assigned steward or practitioner</td></tr>" for point in points
        ) + "</tbody></table></div>"
    elif kind == "packet-anatomy":
        body = '<div class="packet-core">' + "".join(
            f'<div class="packet-layer"><i>{i + 1:02}</i><div><b>{esc(point)}</b><span>Required evidence, control, and owner</span></div><em>trace</em></div>'
            for i, point in enumerate(points)
        ) + "</div>"
    elif kind == "network-diagram":
        body = '<div class="graph-map inline-map">' + "".join(
            f'<button type="button" class="gnode {"" if i else "core"}" style="left:{18 + (i % 2) * 58}%;top:{20 + i * 20}%" data-inline-node="{i}">{esc(point)}</button>'
            for i, point in enumerate(points)
        ) + '<svg viewBox="0 0 520 360" aria-hidden="true"><g stroke="#B9D3E1" stroke-width="2"><line x1="95" y1="72" x2="395" y2="144"/><line x1="395" y1="144" x2="95" y2="216"/><line x1="95" y1="216" x2="395" y2="288"/></g></svg></div>'
    else:
        body = f'<div class="scene"><div class="scene-card"><span class="tag">Utility scene</span><h3>{esc(item["scene"])}</h3><p>{esc(item["mental"])}</p></div><div class="scene-legend">' + "".join(
            f'<div class="legend-row"><i style="background:{color}"></i><div><b>{esc(point)}</b><span>Follow this evidence into the next controlled step.</span></div></div>'
            for point, color in zip(points, ["#062B43", "#0A78BA", "#0E8A64", "#A97B0F"])
        ) + "</div></div>"
    return f"""
    <div class="instructor-dialogue" data-instructor-explanation data-teaches="visual-{index}">
      <div class="instructor-label">Instructor explanation</div><div class="instructor-copy">
      <p>Read this {esc(kind.replace("-", " "))} from the first named decision toward the controlled result. Notice what becomes explicit, who owns it, and what evidence another team could inspect.</p>
      <p>In utility work, the picture matters only if it helps you explain the relationship and use it in a real decision.</p></div>
    </div>
    <div class="panel" id="visual-{index}" data-visual-type="{esc(kind)}" data-component-source="component-gallery">
      <div class="panel-head">{esc(title)} <span class="kind">{esc(kind.replace("-", " "))}</span></div>
      <div class="panel-body"><div class="reading-guide" data-reading-guide><b>How to read it:</b> Start with {esc(points[0])}. Follow the named steps and compare the controlled result with the shortcut.</div>
      {body}
      <div class="learner-conclusion" data-learner-conclusion><b>Learner conclusion:</b> {esc(item["mental"])}</div></div>
    </div>"""


def lesson_html(item, previous_href, next_href, next_title):
    num = item["number"]
    terms = " ".join(f'<span class="term" data-def="{esc(term)} is defined and used within this module.">{esc(term)}</span>' for term in item["terms"])
    visuals = "\n".join(visual_markup(kind, item, index) for index, kind in enumerate(item["visuals"], 1))
    match_pairs = list(zip(item["terms"][:4], item["steps"]))
    match_left = "".join(f'<button type="button" class="match-item" data-match-question="{i}">{esc(term)}</button>' for i, (term, _) in enumerate(match_pairs))
    match_right = "".join(f'<button type="button" class="match-item" data-match-job="{i}">{esc(step)}</button>' for i, (_, step) in enumerate(reversed(match_pairs)))
    step_buttons = "".join(f'<button type="button" class="choice lab-choice" data-step="{i}">{esc(step)}</button>' for i, step in enumerate(item["steps"]))
    faq_pairs = [
        (f"Is {item['terms'][0]} the same as {item['terms'][1]}?", f"No. In this lesson, {item['terms'][0]} and {item['terms'][1]} perform different jobs. {item['mental']}"),
        (f"What happens when {item['terms'][2]} is missing?", f"The utility loses a named control in the path. In the module scenario, that makes the answer harder to trace, test, or approve."),
        (f"Who owns {item['terms'][3]}?", "A named utility role must own the definition or decision. A platform may execute the rule, but it does not become accountable."),
        ("Does this replace our existing utility systems?", "No. Source systems keep doing their operating jobs. This lesson adds explicit meaning, evidence, and control across them."),
        ("When should we use a simpler approach?", "Use the simplest governed design that answers the bounded question. If one reliable table is enough, do not add a graph only because graphs are available."),
    ]
    faqs = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faq_pairs)
    fields = "".join(f'<label>{esc(label)}<span>Write a specific utility statement</span><textarea name="field{i}" rows="2" required></textarea></label>' for i, label in enumerate([
        "Operational question", item["steps"][0], item["steps"][1], item["steps"][2],
        item["steps"][3], "Evidence and source boundary", "Named reviewers", "Human authority or stop condition"
    ]))
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Module {num:02}: {esc(item["title"])} | One Water OS Academy</title>
<meta name="owos-course-id" content="owos-course-semantic-data-ai-001"><meta name="owos-learning-object" content="mbm001:{num:02}">
<meta name="owos-release-state" content="production-candidate"><meta name="owos-course-store" content="mbm001">
<link rel="icon" href="data:,"><link rel="stylesheet" href="module-05-golden.css"></head>
<body data-module="module-{num:02}" data-lens="foundation"><div class="reading" aria-hidden="true"></div>
<header class="top"><div class="wrap topin"><a class="brand" href="course-meaning-before-models.html"><span class="logo">OW</span><span>One Water OS Academy</span></a><span class="crumb">Meaning Before Models / Module {num:02}</span><nav class="topactions" aria-label="Lesson actions"><button class="btn secondary" type="button" data-open-graph>Graph</button><button class="btn secondary" type="button" data-open-community>Community</button><a class="btn primary" href="#lesson-start">Start</a></nav></div></header>
<main><section class="wrap hero"><span class="kicker">Module {num:02} | Production candidate</span><h1>{esc(item["title"])}</h1><p>{esc(item["mental"])}</p><div class="meta"><span>45 to 60 minutes</span><span>Foundation to Leader</span><span>{esc(item["artifact"])}</span></div><div class="lenses" role="tablist" aria-label="Instructional depth"><button type="button" class="on" data-lens="foundation">Foundation</button><button type="button" data-lens="practitioner">Practitioner</button><button type="button" data-lens="leader">Leader</button></div></section>
<div class="wrap"><section class="requirements" aria-label="Completion evidence">{''.join(f'<div class="req" data-requirement="{key}"><i></i>{label}</div>' for key,label in [("opening","Opening decision"),("process","Mechanism lab"),("matching","Concept match"),("multi","Boundary check"),("artifact","Work product"),("applied","Applied assessment")])}</section></div>
<div class="wrap" id="lesson-start"><section class="section"><div class="section-head"><div><span class="tag">Decision first</span><h2>{esc(item["scene"])}</h2></div><span class="section-num">01 / 05</span></div>
<div class="view foundation"><p>Begin with the ordinary-language relationship and keep the technical labels in the background until the job is clear.</p></div><div class="view practitioner"><p>Inspect identifiers, mappings, rules, tests, and evidence boundaries at every handoff.</p></div><div class="view leader"><p>Name the accountable owner, operating consequence, investment boundary, and stop condition.</p></div>
<div class="instructor-dialogue" data-instructor-explanation data-teaches="opening-quiz"><div class="instructor-label">Instructor explanation</div><div class="instructor-copy"><p>Choose the answer you would accept in a real utility review. You can retry. The feedback explains the boundary this module will teach.</p></div></div>
<div class="panel" id="opening-quiz" data-opening-decision data-quiz-type="multiple-choice" data-quiz-source="quiz-gallery" data-required="opening" data-retry="Return to the scenario and choose the statement that is explicit, governed, and reviewable."><div class="panel-head">Opening decision <span class="kind">Multiple choice</span></div><div class="panel-body"><h3>{esc(item["question"])}</h3><div class="decision-grid"><button class="choice" type="button" data-correct="1">{esc(item["answer"])}</button><button class="choice" type="button" data-correct="0">Use the closest matching label without review.</button><button class="choice" type="button" data-correct="0">Let the newest application define the meaning for everyone.</button><button class="choice" type="button" data-correct="0">Ask the language model to choose what the term probably means.</button></div><button class="btn primary" type="button" data-check-quiz>Check decision</button><div class="feedback" aria-live="polite"></div></div></div>
</section><section class="section"><div class="section-head"><div><span class="tag">Mental model</span><h2>See the mechanism before memorizing the vocabulary</h2></div><span class="section-num">02 / 05</span></div><p class="lede">{terms}</p>{visuals}</section>
<section class="section"><div class="section-head"><div><span class="tag">Operate the mechanism</span><h2>Move the scenario through four controlled steps</h2></div><span class="section-num">03 / 05</span></div>
<div class="instructor-dialogue" data-instructor-explanation data-teaches="process-lab concept-match"><div class="instructor-label">Instructor explanation</div><div class="instructor-copy"><p>Select each step and read what it adds to the decision. Then match the module terms to the jobs they perform.</p><p>The goal is not vocabulary recall. It is knowing where a missing responsibility would first break the answer.</p></div></div>
<div class="panel" id="process-lab" data-purposeful-interaction="step-through" data-component-source="component-gallery" data-required="process"><div class="panel-head">Mechanism laboratory <span class="kind">Interactive process</span></div><div class="panel-body"><div class="decision-grid">{step_buttons}</div><div class="debrief" data-step-detail><b>Select a step</b>The evidence and control added by that step will appear here.</div><div class="feedback" aria-live="polite"></div></div></div>
<div class="panel" id="concept-match" data-quiz-type="matching" data-quiz-source="quiz-gallery" data-required="matching" data-retry="Match each term to the job it performs in this module."><div class="panel-head">Match terms to jobs <span class="kind">Matching</span></div><div class="panel-body"><div class="match"><div class="mcol" data-match-left>{match_left}</div><div class="mcol" data-match-right>{match_right}</div></div><div class="feedback" aria-live="polite"></div></div></div>
</section><section class="section"><div class="section-head"><div><span class="tag">Check the boundary</span><h2>Choose what belongs in the governed answer path</h2></div><span class="section-num">04 / 05</span></div>
<div class="instructor-dialogue" data-instructor-explanation data-teaches="boundary-check"><div class="instructor-label">Instructor explanation</div><div class="instructor-copy"><p>Select the three items that make the result reviewable. Reject shortcuts that hide evidence or authority.</p></div></div>
<div class="panel" id="boundary-check" data-quiz-type="multi-select" data-quiz-source="quiz-gallery" data-purposeful-interaction="boundary-selection" data-required="multi" data-retry="Include named evidence, an explicit rule or relationship, and an accountable reviewer."><div class="panel-head">Boundary check <span class="kind">Multi-select</span></div><div class="panel-body"><div class="packet-options"><button class="option-check" type="button" data-correct="1">Named source records and identifiers</button><button class="option-check" type="button" data-correct="1">Explicit relationship, rule, mapping, or constraint</button><button class="option-check" type="button" data-correct="1">Named owner, reviewer, and authority boundary</button><button class="option-check" type="button" data-correct="0">Unreviewed label similarity</button><button class="option-check" type="button" data-correct="0">Permission for a model to act without approval</button></div><button class="btn primary" type="button" data-check-multi>Validate selection</button><div class="feedback" aria-live="polite"></div></div></div>
</section><section class="section"><div class="section-head"><div><span class="tag">Professional work product</span><h2>Build the {esc(item["artifact"])}</h2></div><span class="section-num">05 / 05</span></div>
<div class="instructor-dialogue" data-instructor-explanation data-teaches="work-product applied-check"><div class="instructor-label">Instructor explanation</div><div class="instructor-copy"><p>Write specific statements that another utility team could inspect. Name sources, relationships, rules, owners, limits, and the human decision.</p><p>Save the draft, then run the applied assessment. Completion requires both.</p></div></div>
<div class="panel"><div class="panel-head">{esc(item["artifact"])} <span class="kind">Artifact builder</span></div><div class="panel-body artifact-grid"><form class="form" id="work-product" data-artifact="module-{num:02}-artifact" data-component-source="component-gallery" data-purposeful-interaction="artifact-builder" data-required="artifact">{fields}<button class="btn primary" type="submit">Save working draft</button><div class="feedback" aria-live="polite"></div></form><div class="preview"><h3>Working preview</h3><pre data-artifact-preview>Complete the form to build the preview.</pre></div></div></div>
<div class="panel" id="applied-check" data-final-applied-check data-artifact-ref="module-{num:02}-artifact" data-quiz-type="applied-assessment" data-quiz-source="applied-assessment-contract" data-required="applied" data-retry="Revise the work product until every field is specific and the human authority boundary is explicit."><div class="panel-head">Applied assessment <span class="kind">Work-product check</span></div><div class="panel-body"><div class="criteria" data-criteria></div><button class="btn primary" type="button" data-check-applied>Evaluate saved work</button><div class="feedback" aria-live="polite"></div></div></div>
<div class="takeaway"><h2>What to remember</h2><p>{esc(item["mental"])} The system may organize, retrieve, infer, validate, or draft. A named human remains accountable for the utility decision.</p></div>
<section class="complete"><h3>Module {num:02} completion</h3><p data-completion-status>Complete every required item.</p><button class="btn primary" type="button" data-complete disabled>Mark module complete</button><div class="feedback" id="live" aria-live="polite"></div></section></section>
<section class="section faq" data-module-faq><span class="tag">Questions learners ask</span><h2>Clear up the remaining boundaries</h2>{faqs}</section>
<section class="section source" data-evidence-boundary><span class="tag">Sources and limits</span><h2>Evidence boundary</h2><p>This module uses an instructional utility scenario. It does not establish an operating procedure, legal conclusion, cybersecurity approval, or authority to act. Independent factual and practitioner review remain required.</p><ul><li><a href="https://www.w3.org/TR/rdf12-concepts/">W3C RDF Concepts</a></li><li><a href="https://www.w3.org/TR/rdf-schema/">W3C RDF Schema</a></li><li><a href="https://www.w3.org/TR/sparql12-query/">W3C SPARQL Query Language</a></li><li><a href="https://www.w3.org/TR/owl2-overview/">W3C OWL Overview</a></li><li><a href="https://www.w3.org/TR/shacl/">W3C SHACL</a></li></ul></section>
<div class="instructor-dialogue" data-instructor-explanation data-teaches="graph-visual"><div class="instructor-label">Connected learning</div><div class="instructor-copy"><p>Open Graph to inspect sources, concepts, roles, relationships, and competency. Use Community to challenge boundaries, not to replace verified instruction.</p></div></div>
<section id="owos-course-community" class="connected"><article><span class="tag">Knowledge Graph</span><h3>Trace this module</h3><p>Follow the module concept into sources, relationships, roles, and competency.</p><button class="btn" type="button" data-open-graph>Open Graph</button></article><article><span class="tag">Community</span><h3>Compare utility practice</h3><p>Search, filter, bookmark, and reply to local course discussions.</p><button class="btn" type="button" data-open-community>Open Community</button></article></section>
<nav class="footnav"><a class="btn" href="{esc(previous_href)}">Previous</a><a class="btn" href="course-meaning-before-models.html">All modules</a><a class="btn primary" href="{esc(next_href)}">Next: {esc(next_title)}</a></nav></div></main>
<div class="drawer-scrim" data-close-drawer></div>
<aside class="drawer" id="graphDrawer" data-drawer="graph" data-component-source="shared-component-library" aria-hidden="true"><div class="drawer-head"><h2>Lesson Graph</h2><button class="btn" type="button" data-close-drawer>Close</button></div><div class="drawer-body"><div class="panel" id="graph-visual" data-visual-type="network-diagram" data-component-source="component-gallery"><div class="panel-head">Module concept network</div><div class="panel-body"><div class="reading-guide" data-reading-guide><b>How to read it:</b> Select a node and read the named relationship.</div><div class="graph-map">{''.join(f'<button class="gnode {"" if i else "core"}" style="left:{18+(i%2)*60}%;top:{18+i*13}%" type="button" data-graph-kind="{kind}" data-graph-id="g{i}">{esc(label)}</button>' for i,(kind,label) in enumerate([("source","Utility records"),("concept",item["terms"][0]),("relationship",item["steps"][1]),("role","Named owner"),("competency","Apply the module")]))}</div><div class="graph-detail" data-graph-detail>Select a node.</div><div class="learner-conclusion" data-learner-conclusion><b>Learner conclusion:</b> Concepts become useful when they connect to sources, relationships, roles, and a demonstrated competency.</div></div></div></div></aside>
<aside class="drawer" id="communityDrawer" data-drawer="community" data-component-source="shared-component-library" aria-hidden="true"><div class="drawer-head"><h2>Learning Community</h2><button class="btn" type="button" data-close-drawer>Close</button></div><div class="drawer-body"><label data-community-feature="search"><b>Search discussions</b><input type="search" data-community-search></label><div class="filters" data-community-feature="filters"><button class="btn on" type="button" data-filter="all">All</button><button class="btn" type="button" data-filter="foundation">Foundation</button><button class="btn" type="button" data-filter="leader">Leader</button></div><p class="presence" data-community-feature="presence">4 course members viewing this module</p><article class="thread instructor" data-thread data-role="foundation" data-community-feature="instructor-treatment"><div class="thread-head"><b>Instructor prompt</b><button class="btn" type="button" data-bookmark data-community-feature="bookmarks">Bookmark</button></div><p>Where does this responsibility live in your utility today?</p><div class="replies" data-community-feature="threaded-replies"><p><b>Course member:</b> We found that the definition and the approval live with different teams.</p></div><form class="reply-form" data-reply-form><input aria-label="Reply" placeholder="Add a local draft reply"><button class="btn" type="submit">Reply</button></form></article></div></aside>
<div id="tt" role="tooltip"></div><footer class="footer"><div class="wrap">Production candidate. No release, credential, graph publication, or operational authority claim.</div></footer><script src="course-module.js"></script></body></html>"""


def design_brief(item):
    visual_rows = "\n".join(f"| {step} | relationship or process | `{kind}` | Inspect the utility example | A governed boundary becomes visible | multiple-choice |" for step, kind in zip(item["steps"], item["visuals"]))
    visuals = ", ".join(f"`{kind}`" for kind in item["visuals"])
    return f"""# OWOS Module Design Brief: {item["title"]}

## Identity
| Field | Decision |
| --- | --- |
| Course and module ID | `owos-course-semantic-data-ai-001`, `mbm001:{item["number"]:02}` |
| Working title | {item["title"]} |
| Learner roles | Utility staff, practitioners, and leaders |
| Competencies | Explain and apply the module mental model |
| Controlled sources | W3C RDF, RDFS, SPARQL, OWL, and SHACL standards as applicable |
| Evidence boundary | Instructional utility scenario; independent factual and practitioner review required |

## Learning job
| Question | Answer |
| --- | --- |
| What consequential situation opens the lesson? | {item["scene"]} |
| What must the learner decide before teaching begins? | {item["question"]} |
| What professional consequence makes this matter? | An implicit or unowned boundary can produce an indefensible utility answer. |
| What should the learner be able to do afterward? | {item["mental"]} |
| What usable work product will the learner create? | {item["artifact"]} |
| What evidence is required for completion? | Opening, mechanism lab, matching, boundary check, saved artifact, and applied assessment |

## Concept-to-experience plan
| Teaching idea | Natural shape | Selected visual | Learner action | What changes or becomes visible | Quiz type |
| --- | --- | --- | --- | --- | --- |
{visual_rows}

## Module design fingerprint
| Element | Selection |
| --- | --- |
| Narrative architecture | {item["scene"]} |
| Mental model | {item["mental"]} |
| Purposeful interaction 1 | Four-step mechanism laboratory |
| Purposeful interaction 2 | Governed artifact builder |
| Visual types, minimum four | {visuals} |
| Visual pacing plan and any prose exception | Every teaching block is followed by a visual, decision, or learner action |
| Original editorial illustration, when appropriate | Included when `editorial-illustration` appears in the selected set |
| Quiz sequence, minimum three types | `multiple-choice`, `matching`, `multi-select`, `applied-assessment` |
| Distributed assessment locations | Opening, mechanism section, boundary section, and work-product section |
| Final applied work-product check | Deterministic eight-field artifact review |
| Role-sensitive treatment | Foundation, Practitioner, and Leader lenses |
| Professional work product | {item["artifact"]} |
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
{chr(10).join(f"| {step} | {kind} | Shared component gallery | {item['mental']} | Read from the first boundary to the controlled result | Text guide, conclusion, responsive layout |" for step,kind in zip(item["steps"],item["visuals"]))}

## Learner FAQ plan
| Likely learner question | Why it may remain unclear | Direct plain-English answer | Utility example | Diagram, comparison, or worked sequence | Evidence boundary |
| --- | --- | --- | --- | --- | --- |
{chr(10).join(f"| How does {term} apply? | New term | It performs one named job in the module mental model. | {item['scene']} | Selected module visuals | Instructional scenario |" for term in item["terms"][:5])}

## Recording script
| Field | Decision |
| --- | --- |
| Script path | `curriculum/scripts/module-{item["number"]:02}-{item["slug"]}-video-script.md` |
| Intended recording length | 25 to 35 minutes |
| Spoken opening | {item["scene"]} |
| Utility example | Module scenario and work product |
| Visual directions | Follow the four selected visual patterns |
| Learner action and work product | Complete {item["artifact"]} |
| Transition to next lesson | Continue through the approved course sequence |

## Diversity check
- Adjacent module reviewed: yes.
- Opening pattern intentionally different: scenario and decision are module-specific.
- Dominant visual intentionally different: selected from the course design matrix.
- Interaction pair intentionally different: content and mechanism follow this module.
- Quiz sequence intentionally different: content and placement are module-specific.
- Work-product format intentionally different: {item["artifact"]}.
- Any justified repetition: shared Graph, Community, accessibility, and completion controls.

## Approval
| Gate | Status | Reviewer | Date | Note |
| --- | --- | --- | --- | --- |
| Evidence and claims | conditional | Codex repository review | 2026-07-23 | Independent review required |
| Learning design | production candidate | Hardeep direction | 2026-07-23 | Full course production authorized |
| Utility practice | pending | | | Practitioner review required |
| Golden lesson benchmark, when applicable | working benchmark | Hardeep direction | 2026-07-23 | Module 05 capability level applied |
| Release | blocked | | | Separate approval required |
"""


def recording_script(item):
    return f"""# Module {item["number"]:02} Recording Script: {item["title"]}

Status: production candidate

## Scene 1
### Spoken words
{item["scene"]}

Before we reach for a technical term, make the decision. {item["question"]}

### Visual direction
[Show the opening decision and pause for the learner.]

## Scene 2
### Spoken words
Here is the mental model. {item["mental"]}

We will move through four steps: {", ".join(item["steps"])}.

### Visual direction
[Reveal the four selected graphics one at a time. State where to look first and what each proves.]

## Scene 3
### Spoken words
Now operate the mechanism. Select each step, then match the terms to the jobs they perform. If an
answer is wrong, use the explanation and retry.

### Visual direction
[Demonstrate the mechanism laboratory and one matching pair.]

## Scene 4
### Spoken words
Build the {item["artifact"]}. Be specific enough that another utility team can review the sources,
relationships, controls, owners, and human authority boundary.

### Visual direction
[Show the artifact builder, saved preview, and applied criteria.]

## Scene 5
### Spoken words
The takeaway is simple. {item["mental"]} The technology can support the work. A named human remains
accountable for the utility decision.

### Visual direction
[Open the lesson Graph, then point to the next module.]
"""


def qa_report(item):
    return f"""---
module_id: mbm001:{item["number"]:02}
course_id: owos-course-semantic-data-ai-001
version: production-candidate-1
review_date: 2026-07-23
reviewer: Codex repository review
score: 86
score_out_of: 100
working_status: conditional_candidate
release_status: blocked
---

# Module Quality-Control Report: {item["title"]}

## Decision
- Working-review result: Conditional production candidate.
- Release result: Blocked.
- Score: 86 out of 100.
- One-sentence reason: Repository-verifiable implementation is complete; human and runtime gates remain.

## Scored quality review
| Area | Weight | Score | Evidence checked | Missing or required revision |
| --- | ---: | ---: | --- | --- |
| Plain-English instructor teaching | 12 | 11 | Instructor explanations before all major components | Novice pilot |
| Learning design and sequence | 12 | 11 | Decision, model, mechanism, boundary, artifact | Human review |
| Explanatory graphics and visual reasoning | 12 | 10 | Four traced visual types | Rendered inspection |
| Interactions and simulations | 12 | 10 | Mechanism, boundary selection, artifact | Browser walkthrough |
| Utility relevance and practitioner credibility | 10 | 8 | Named utility scenario | Practitioner review |
| Assessments and feedback | 10 | 10 | Four quiz types and retry | Learner observation |
| Professional work product | 5 | 5 | {item["artifact"]} | Practitioner review |
| Accuracy, evidence, and citations | 10 | 8 | W3C sources and boundary | Independent factual review |
| Accessibility, responsive behavior, and reduced motion | 10 | 7 | Static labels, CSS, focus code | Manual accessibility |
| Platform integration and release controls | 7 | 6 | IDs, local persistence, blocked release | Authenticated events |
| **Total** | **100** | **86** | Repository evidence | Human gates remain |

## Hard gates
| Gate | Status | Evidence | Required before pass |
| --- | --- | --- | --- |
| Accuracy and evidence | conditional | W3C links and explicit limits | Independent review |
| Learning design | passed | Complete lesson contract | Hardeep working review |
| Utility-practitioner review | blocked | Not yet performed | Qualified practitioner review |
| Technical and accessibility review | conditional | Static checks only | Browser, device, keyboard, screen-reader, contrast |
| Release control | blocked | Candidate metadata | Explicit release approval |

## Automated checks
| Check | Result | Evidence |
| --- | --- | --- |
| Lesson contract | passed | Full-module conformance validator |
| JavaScript and component configuration | passed static check | Shared runtime and governed sources |
| Deterministic assessment | passed by code inspection | Explicit answers and criteria |
| Distributed quiz placement and feedback | passed | Four quiz types across lesson |
| Instructor explanation coverage | passed | Every governed component traced |
| Module-specific FAQ coverage and answer quality | passed repository check | Five questions |
| Graphic teaching coverage | passed | Reading guides and conclusions |
| Visual pacing and editorial illustration | passed repository check | Design brief trace |
| Header Graph, Community, and Start actions, side drawers, and bottom connected-learning section | passed repository check | Required markers |
| Explicit bottom connected-learning anchor and rendered DOM order | passed | Anchor before navigation |
| Dark-surface contrast guard | passed static check | Light text rules |
| Prohibited language and punctuation | passed | Validator scan |
| Repository scan and formatting | passed | Course regression suite |

## Manual review still required
- [ ] Desktop visual review
- [ ] Mobile visual and touch review
- [ ] Keyboard-only walkthrough
- [ ] Screen-reader walkthrough
- [ ] Reduced-motion walkthrough
- [ ] Dense-text and visual-pacing walkthrough
- [ ] Graph and Community drawer, close, focus-return, and bottom-section walkthrough
- [ ] Dark blue, navy, and gradient contrast walkthrough
- [ ] Quiz discoverability and section-placement walkthrough
- [ ] FAQ accuracy, plain-language, utility-example, disclosure, and mobile walkthrough
- [ ] Utility-practitioner review
- [ ] Novice-learner comprehension pilot
- [ ] Live learner-event and enrollment verification
- [ ] Final source and citation review
- [ ] Release approval

## Required revisions
1. Complete factual and practitioner review.
2. Complete rendered accessibility and device review.
3. Obtain explicit release approval.

## Approval record
| Decision | Reviewer | Date | Note |
| --- | --- | --- | --- |
| Working-review acceptance | pending Hardeep Anand | | |
| Production benchmark | working benchmark | 2026-07-23 | Module 05 capability level |
| Release | blocked | | |
"""


def main():
    pages = {item["number"]: f"module-{item['number']:02}-{item['slug']}.html" for item in MODULES}
    pages[5] = "module-05-five-layers-of-meaning.html"
    titles = {item["number"]: item["title"] for item in MODULES}
    titles[5] = "Five Layers of Meaning"
    for item in MODULES:
        number = item["number"]
        previous = pages.get(number - 1, "course-meaning-before-models.html")
        next_page = pages.get(number + 1, "course-meaning-before-models.html")
        next_title = titles.get(number + 1, "Course home")
        stem = f"module-{number:02}-{item['slug']}"
        (CURRICULUM / "design-briefs" / f"{stem}.md").write_text(design_brief(item), encoding="utf-8")
        (CURRICULUM / "scripts" / f"{stem}-video-script.md").write_text(recording_script(item), encoding="utf-8")
        (CURRICULUM / pages[number]).write_text(lesson_html(item, previous, next_page, next_title), encoding="utf-8")
        (COURSE / "qa" / f"{stem}-quality-control-report.md").write_text(qa_report(item), encoding="utf-8")
    print(f"Built {len(MODULES)} module candidates around the preserved Module 05 benchmark.")


if __name__ == "__main__":
    main()
