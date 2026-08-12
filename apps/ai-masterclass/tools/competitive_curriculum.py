#!/usr/bin/env python3
"""Apply the accepted competitive expansion to the legacy granular curriculum."""

from __future__ import annotations

import json
from pathlib import Path


COURSE_ROOT = Path(__file__).resolve().parents[1]
EXPANSION_SOURCE = COURSE_ROOT / "curriculum" / "competitive-curriculum-expansion.json"


def load_expansion() -> dict:
    return json.loads(EXPANSION_SOURCE.read_text(encoding="utf-8"))


def proposal(expansion: dict) -> dict:
    proposal_id = expansion["proposalId"]
    return {
        "id": proposal_id,
        "gap_id": expansion["id"],
        "competitiveExpansionId": expansion["id"],
        "title": expansion["title"],
        "kind": expansion["kind"],
        "coverage": expansion["coverage"],
        "decision": "accepted",
        "recommendation": expansion["description"],
        "description": expansion["description"],
        "learningObjectives": expansion["objectives"],
        "workProduct": expansion["workProduct"],
        "assessmentEvidence": expansion["assessmentEvidence"],
        "visualDirections": expansion["visualDirections"],
        "secondaryModules": expansion["secondaryModules"],
        "sourceRefs": expansion["sourceRefs"],
        "evidenceBoundary": expansion["evidenceBoundary"],
        "subtopics": [
            {"id": f"{proposal_id}{chr(97 + index)}", "title": title}
            for index, title in enumerate(expansion["subtopics"])
        ],
    }


def apply_competitive_expansion(model: dict) -> dict:
    source = load_expansion()
    modules = {module["id"]: module for module in model["modules"]}
    expansion_ids = {item["id"] for item in source["expansions"]}
    proposal_ids = {item["proposalId"] for item in source["expansions"]}

    for module in model["modules"]:
        module["proposed_additions"] = [
            item for item in module.get("proposed_additions", [])
            if item.get("competitiveExpansionId") not in expansion_ids
            and item.get("id") not in proposal_ids
        ]

    for item in source["expansions"]:
        modules[item["primaryModule"]]["proposed_additions"].append(proposal(item))

    model.setdefault("numbering", {})["competitive_expansion"] = "M41.CE01"
    model.setdefault("status_legend", {})["accepted"] = (
        "Approved for curriculum-blueprint integration. Facts, lesson production, credentials, "
        "and release remain subject to their own gates."
    )
    model["competitive_expansion"] = {
        "schema": source["schema"],
        "title": source["title"],
        "approved": source["approved"],
        "owner": source["owner"],
        "status": source["status"],
        "authority": source["authority"],
        "sourceAudit": source["sourceAudit"],
        "sourcePath": str(EXPANSION_SOURCE.relative_to(COURSE_ROOT)),
        "sourceCount": len(source["sources"]),
        "expansionCount": len(source["expansions"]),
        "expansionIds": [item["id"] for item in source["expansions"]],
    }
    model.setdefault("summary", {})["competitive_expansion_count"] = len(source["expansions"])
    model["summary"]["accepted_competitive_expansions"] = sum(
        addition.get("decision") == "accepted"
        for module in model["modules"]
        for addition in module.get("proposed_additions", [])
        if addition.get("competitiveExpansionId")
    )
    log = [
        item for item in model.get("revision_log", [])
        if item.get("version") != "1.2"
    ]
    log.append({
        "date": "2026-08-11",
        "version": "1.2",
        "change": (
            "Integrated fifteen accepted applied and agentic artificial intelligence curriculum "
            "expansions with stable IDs, learning objectives, work products, assessment evidence, "
            "visual direction, source lineage, and release boundaries."
        ),
    })
    model["revision_log"] = log
    return model

