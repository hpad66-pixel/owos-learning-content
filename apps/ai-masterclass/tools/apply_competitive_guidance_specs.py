#!/usr/bin/env python3
"""Strengthen affected legacy guidance specifications for the 2026-08-11 expansion."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPECS = ROOT / "curriculum" / "legacy-module-guidance-specs.json"


UPDATES = {
    "M05": {
        "learningJob": "Explain how models and language systems move from data and design through training, evaluation, release, monitoring, incident response, rollback, correction, and retirement so learners can ask where behavior and limitations came from.",
        "decision": "Identify the complete lifecycle, provenance, evaluation, operating, and recovery evidence a utility needs before accepting a model or language-system suitability claim.",
        "workProduct": "production AI lifecycle and provenance card",
        "distinction": "data preparation, experiment, training, adaptation, evaluation, artifact, release, deployment, monitoring, incident, rollback, correction, and retirement",
        "boundary": "Do not infer training data, architecture, labor, performance, monitoring quality, or production fitness from marketing or one demonstration. Keep proprietary, unknown, untested, and unapproved details visible.",
        "visuals": ["production lifecycle phase gates", "training and evidence funnel", "versioned artifact provenance network", "monitor-incident-rollback loop"]
    },
    "M10": {
        "learningJob": "Give learners a practical autonomy and interaction model for deciding how much an artificial intelligence system may suggest, prepare, act, retry, explain, pause, recover, or escalate while a person retains usable control.",
        "decision": "Set the narrowest useful automation level and specify visible status, evidence, preview, confirmation, interruption, correction, recovery, prohibited action, and human escalation.",
        "workProduct": "agent interaction, autonomy, and recovery specification",
        "distinction": "assistance, augmentation, workflow automation, bounded agency, autonomous action, transparency, confirmation, interruption, correction, recovery, escalation, and operating authority",
        "boundary": "Never imply that a friendly interface, explanation, or artificial intelligence system may operate treatment, distribution, collection, flood-control, or safety systems without approved deterministic controls and qualified human authority.",
        "visuals": ["autonomy and interaction spectrum", "human-agent state map", "confirmation and authority swimlane", "failure recovery decision tree"]
    },
    "M12": {
        "learningJob": "Connect artificial intelligence to tasks, work design, baseline, adoption, quality, risk, complete cost, review effort, time to value, benefit ownership, and utility economics without turning estimates into promised results.",
        "decision": "Decide which tasks should change, what new work appears, which measures establish value, who owns each benefit, and when the evidence requires redesign or stop.",
        "workProduct": "utility AI value and benefit-realization record",
        "distinction": "job, task, output, activity, adoption, quality, service outcome, risk reduction, direct cost, shifted cost, public value, financial value, and realized benefit",
        "boundary": "Do not promise staff reductions, productivity, return, ratepayer savings, service improvement, risk reduction, or public value without an approved baseline, complete cost, measured evidence, and accountable benefit owner.",
        "visuals": ["baseline-to-benefit chain", "total-cost and shifted-work iceberg", "measure hierarchy", "continue-redesign-stop phase gates"]
    },
    "M24": {
        "learningJob": "Teach evaluation and observability as a continuing evidence process that tests answer and task quality, source coverage, tool correctness, trajectory, policy behavior, refusal, recovery, drift, latency, cost, and human-review effort.",
        "decision": "Define the test set, signals, metrics, thresholds, reviewers, incident response, regression checks, correction action, and stop rule for a utility artificial intelligence or agent system.",
        "workProduct": "agent evaluation, observability, and continuing-assurance plan",
        "distinction": "test case, task outcome, groundedness, source coverage, tool correctness, trajectory, metric, signal, trace, threshold, benchmark, drift, incident, acceptance, and continuing assurance",
        "boundary": "A benchmark, dashboard, average score, missing alert, or one successful demonstration does not prove utility fitness, safety, fairness, compliance, or performance under changed conditions.",
        "visuals": ["agent evaluation coverage matrix", "trace and signal map", "drift-incident-correction timeline", "continuing-assurance loop"]
    },
    "M31": {
        "learningJob": "Teach provenance, explanation, transparency, and audit as the ability to trace an answer or action through sources, versions, identities, transformations, system behavior, approvals, limitations, decisions, and corrections.",
        "decision": "Decide whether an artificial intelligence-supported record provides the explanation, evidence, trace, provenance, justification, uncertainty, and human approval required for its consequence and audience.",
        "workProduct": "explanation, provenance, and decision-justification record",
        "distinction": "explanation, transparency, interpretability, traceability, source, lineage, provenance, evidence, version, transformation, approval, audit, decision justification, uncertainty, and correction",
        "boundary": "A fluent explanation can be wrong. Provenance can show origin without proving accuracy, completeness, applicability, or professional judgment. Keep what remains unknown visible.",
        "visuals": ["explanation and evidence stack", "source-to-decision provenance network", "audience-consequence matrix", "known-unknown and correction map"]
    },
    "M37": {
        "learningJob": "Teach image, audio, video, and synthetic-media creation together with source integrity, consent, provenance, disclosure, approval, accessibility, publication, incident response, and correction.",
        "decision": "Decide whether generated or altered media may be created, shared, published, corrected, restricted, or rejected for a utility communication purpose.",
        "workProduct": "utility synthetic-media integrity and production protocol",
        "distinction": "generated media, edited media, misleading context, impersonation, deepfake, error, satire, disinformation, source, transformation, disclosure, approval, and correction",
        "boundary": "Do not label media authentic or false without recorded evidence and qualified review. Do not generate a person's likeness or voice without authority, or publish unsupported water-quality, service, emergency, or public claims.",
        "visuals": ["media provenance and transformation chain", "content-integrity decision tree", "publication approval swimlane", "false-message correction timeline"]
    },
    "M40": {
        "learningJob": "Teach artificial-intelligence-assisted software building as a governed process from problem, goal, and plan through repository change, review, tests, dependencies, environment, artifact, release, deployment, observation, and rollback.",
        "decision": "Decide what a coding agent may inspect or change, what tests and review prove the change, what release evidence is required, and when a qualified person must stop, approve, recover, or roll back.",
        "workProduct": "AI-assisted software release evidence package",
        "distinction": "problem, goal, plan, repository, branch, difference, code change, test, dependency, environment, artifact, review, commit, release, deployment, monitoring, and rollback",
        "boundary": "Use sandboxed examples, protect credentials, inspect changes, reproduce builds, and preserve review. Generated code and passing tests do not transfer engineering, security, privacy, accessibility, or release responsibility.",
        "visuals": ["goal-plan-build-test-release loop", "branch and review graph", "change evidence chain", "release and rollback phase gates"]
    },
    "M41": {
        "learningJob": "Teach agents as bounded work systems with goals, environment, observations, actions, plans, tools, state, evidence, evaluation, handoffs, coordination, interaction, stop conditions, recovery, and accountable humans.",
        "decision": "Choose between a fixed workflow, one agent, or multiple specialists, then define the planning pattern, tool and state boundary, handoff, disagreement, recovery, escalation, and human-decision contract.",
        "workProduct": "utility agent architecture, coordination, and recovery contract",
        "distinction": "workflow, agent, goal, environment, observation, action, plan, Reason and Act, tool, state, specialist, orchestrator, shared state, handoff, evaluation, retry, conflict, deadlock, recovery, escalation, and stop",
        "boundary": "Do not imply that planning text, multiple agents, perceived agency, or tool access creates independent truth, professional judgment, or operating authority. Preserve sources, permissions, cost limits, dissent, and human decision rights.",
        "visuals": ["agent-environment and planning stepper", "multi-agent coordination topology", "shared-state and disagreement ledger", "failure-propagation and recovery chain"]
    },
    "M43": {
        "learningJob": "Teach the production infrastructure and operating disciplines behind model, language-model, and agent applications, including cloud foundations, environments, pipelines, artifacts, deployment, observability, cost, resilience, incidents, recovery, and exit.",
        "decision": "Design the smallest supportable architecture and operating pipeline for a bounded utility application, assign every responsibility, and define release, observation, incident, rollback, cost, support, and exit evidence.",
        "workProduct": "AI deployment, operations, and release architecture record",
        "distinction": "development, test, production, container, compute, storage, network, identity, secret, artifact, pipeline, continuous integration, delivery, deployment, observability, drift, incident, scaling, recovery, and exit",
        "boundary": "Keep services, prices, limits, model versions, platform features, and scaling claims dated. Do not publish credentials or facility-sensitive architecture, skip security review, or represent a classroom deployment as a supported production service.",
        "visuals": ["cloud and deployment architecture stack", "artifact and environment promotion pipeline", "observability-drift-incident map", "operate-recover-exit responsibility matrix"]
    },
    "M52": {
        "learningJob": "Teach adoption as a change in tasks, identity, confidence, participation, learning, incentives, support, authority, feedback, and operating routines, supported by fit-to-purpose change methods and operating models.",
        "decision": "Design a responsible adoption and support plan that gives affected people a voice, psychological safety, training, peer support, feedback, correction, clear authority, and an operating model that can sustain the work.",
        "workProduct": "workforce adoption, participation, and support plan",
        "distinction": "communication, training, capability, participation, psychological safety, champion, support, adoption, compliance, confidence, concern, resistance, feedback, operating model, and professional identity",
        "boundary": "Do not label concern as resistance, use learning data as undisclosed job-performance evidence, or promise adoption from communication and training alone. Keep labor, accessibility, privacy, participation, support, and professional authority visible.",
        "visuals": ["adoption and correction feedback loop", "task-identity-capability map", "champion and support network", "centralized-federated-hybrid operating-model comparison"]
    }
}


def main() -> None:
    payload = json.loads(SPECS.read_text(encoding="utf-8"))
    by_code = {item["code"]: item for item in payload["modules"]}
    if not set(UPDATES).issubset(by_code):
        raise ValueError("A required legacy guidance specification is missing")
    for code, fields in UPDATES.items():
        by_code[code].update(fields)
    payload["status"] = "accepted-blueprint-expansion"
    payload["authority"] = (
        "Hardeep Anand approved the 2026-08-11 applied and agentic artificial intelligence "
        "curriculum expansion. Specifications remain blocked from factual and learner-facing "
        "release until the required evidence and production gates pass."
    )
    SPECS.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Updated {len(UPDATES)} legacy guidance specifications")


if __name__ == "__main__":
    main()

