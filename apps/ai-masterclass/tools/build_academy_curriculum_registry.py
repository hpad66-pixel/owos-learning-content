#!/usr/bin/env python3
"""Build the governed two-line curriculum registry for Academy Author Studio."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEGACY_SOURCE = ROOT / "curriculum" / "one-water-ai-granular-toc.json"
SHREYA_REVIEW_SOURCE = ROOT / "curriculum" / "shreya-technical-foundations-review.json"
RESEARCH_STARTERS_SOURCE = ROOT / "curriculum" / "research-starters" / "index.json"
ROLE_TRACKS_SOURCE = ROOT / "curriculum" / "role-tracks.json"
LEARNING_PATHWAYS_SOURCE = ROOT / "curriculum" / "learning-pathways.json"
MODULES_ROOT = ROOT / "curriculum" / "modules"
FELLOWSHIP_SOURCE = ROOT / "SYLLABUS.md"
LEGACY_PDF = ROOT / "output" / "pdf" / "one-water-ai-applied-intelligence-curriculum.pdf"
FELLOWSHIP_PDF = ROOT / "output" / "pdf" / "one-water-ai-executive-fellowship-master-curriculum.pdf"
OUTPUT = ROOT / "output" / "academy-curriculum-registry.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_fellowship() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    text = FELLOWSHIP_SOURCE.read_text(encoding="utf-8")
    course_matches = list(re.finditer(r"^## Course (\d+): (.+)$", text, re.MULTILINE))
    courses: list[dict[str, object]] = []
    modules: list[dict[str, object]] = []
    for index, match in enumerate(course_matches):
        course_number = int(match.group(1))
        end = course_matches[index + 1].start() if index + 1 < len(course_matches) else len(text)
        section = text[match.start():end]
        promise_match = re.search(r"### Course promise\s+\n\s*(.+?)(?=\n\n\| Module)", section, re.DOTALL)
        promise = " ".join(promise_match.group(1).split()) if promise_match else ""
        course_module_ids: list[str] = []
        for line in section.splitlines():
            module_match = re.match(r"\|\s*(\d+)\.\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$", line)
            if not module_match:
                continue
            number = int(module_match.group(1))
            module_id = f"fellowship:M{number:02d}"
            course_module_ids.append(module_id)
            modules.append({
                "id": module_id,
                "code": f"M{number}",
                "number": number,
                "title": module_match.group(2).strip(),
                "groupId": f"course-{course_number}",
                "groupTitle": f"Course {course_number}: {match.group(2).strip()}",
                "learningJob": module_match.group(3).strip(),
                "appliedResult": module_match.group(4).strip(),
                "status": "curriculum-candidate",
            })
        courses.append({
            "id": f"course-{course_number}",
            "number": course_number,
            "title": match.group(2).strip(),
            "promise": promise,
            "moduleIds": course_module_ids,
        })
    if len(courses) != 8 or len(modules) != 64:
        raise ValueError(f"Expected 8 fellowship courses and 64 modules, found {len(courses)} and {len(modules)}")
    if [module["number"] for module in modules] != list(range(1, 65)):
        raise ValueError("Fellowship module numbers must be consecutive from 1 through 64")
    return courses, modules


def build_registry() -> dict[str, object]:
    legacy = json.loads(LEGACY_SOURCE.read_text(encoding="utf-8"))
    shreya_review = json.loads(SHREYA_REVIEW_SOURCE.read_text(encoding="utf-8"))
    research_starters = json.loads(RESEARCH_STARTERS_SOURCE.read_text(encoding="utf-8"))
    role_tracks = json.loads(ROLE_TRACKS_SOURCE.read_text(encoding="utf-8"))
    learning_pathways = json.loads(LEARNING_PATHWAYS_SOURCE.read_text(encoding="utf-8"))
    module_guidance: dict[str, dict[str, object]] = {}
    for guidance_path in MODULES_ROOT.glob("*/MODULE-GUIDANCE.json"):
        guidance = json.loads(guidance_path.read_text(encoding="utf-8"))
        module_id = guidance["moduleId"]
        if module_id in module_guidance:
            raise ValueError(f"Duplicate module guidance for {module_id}")
        staff_path = ROOT / guidance["staffDirectionPath"]
        prompt_path = ROOT / guidance["researchPromptPath"]
        placement_path = ROOT / guidance["placementRegisterPath"]
        module_guidance[module_id] = {
            **guidance,
            "staffDirectionMarkdown": staff_path.read_text(encoding="utf-8"),
            "researchPromptMarkdown": prompt_path.read_text(encoding="utf-8"),
            "placement": json.loads(placement_path.read_text(encoding="utf-8")),
        }
    if len(shreya_review["items"]) != 56:
        raise ValueError("Expected 56 items in Shreya's technical foundations review")
    contributor_inputs: dict[str, list[dict[str, object]]] = {}
    for item in shreya_review["items"]:
        contributor_inputs.setdefault(item["primary_module"], []).append({
            **item,
            "sourceId": shreya_review["source_id"],
            "contributor": shreya_review["contributor"],
            "reviewId": shreya_review["review_id"],
            "releaseBoundary": shreya_review["authority"],
        })
    legacy_modules = []
    for module in legacy["modules"]:
        proposed = module.get("proposed_additions", [])
        enhancements = module.get("targeted_enhancements", [])
        module_id = f"legacy:{module['id']}"
        legacy_modules.append({
            "id": module_id,
            "code": module["id"],
            "number": int(module["number"]),
            "title": module["title"],
            "groupId": f"part-{module['part']['id']}",
            "groupTitle": module["part"]["title"],
            "pageStart": module["pages"]["start"],
            "pageEnd": module["pages"]["end"],
            "sourceFile": module["source_file"],
            "currentSectionCount": len(module.get("current_sections", [])),
            "proposedAdditionCount": len(proposed),
            "targetedEnhancementCount": len(enhancements),
            "sections": [
                {
                    "id": section["id"],
                    "title": section["title"],
                    "level": section.get("level", 1),
                    "type": section.get("type", "instruction"),
                    "coverage": section.get("coverage", "current"),
                }
                for section in module.get("current_sections", [])
            ],
            "proposals": [
                {
                    "id": addition["id"],
                    "title": addition["title"],
                    "coverage": addition.get("coverage", "missing"),
                    "decision": addition.get("decision", "proposed"),
                    "subtopics": addition.get("subtopics", []),
                }
                for addition in proposed
            ],
            "enhancements": enhancements,
            "contributorInputs": contributor_inputs.get(module["id"], []),
            "status": "proposal-review" if proposed or enhancements or any(
                item["classification"] != "already-done-exactly"
                for item in contributor_inputs.get(module["id"], [])
            ) else "source-current",
            **({"guidance": module_guidance[module_id]} if module_id in module_guidance else {}),
        })
    if len(legacy_modules) != 64:
        raise ValueError(f"Expected 64 legacy modules, found {len(legacy_modules)}")
    if [module["number"] for module in legacy_modules] != list(range(64)):
        raise ValueError("Legacy module numbers must be consecutive from 0 through 63")
    fellowship_courses, fellowship_modules = parse_fellowship()
    starter_by_module = {item["moduleId"]: item for item in research_starters["items"]}
    if len(starter_by_module) != 64 or len(role_tracks["tracks"]) != 15:
        raise ValueError("Expected 64 research starters and 15 source role profiles")
    if len(learning_pathways["pathways"]) != 6:
        raise ValueError("Expected one universal core and five role lenses")
    valid_module_ids = {module["id"] for module in fellowship_modules}
    valid_track_ids = {track["id"] for track in role_tracks["tracks"]}
    for pathway in learning_pathways["pathways"]:
        if not set(pathway["moduleIds"]).issubset(valid_module_ids):
            raise ValueError(f"Unknown module in learning pathway {pathway['id']}")
        if not set(pathway["sourceTrackIds"]).issubset(valid_track_ids):
            raise ValueError(f"Unknown source profile in learning pathway {pathway['id']}")
    for module in fellowship_modules:
        module["researchStarter"] = starter_by_module[module["id"]]
    all_ids = [module["id"] for module in legacy_modules + fellowship_modules]
    if len(all_ids) != len(set(all_ids)):
        raise ValueError("Namespaced module IDs must be unique across both curriculum lines")
    legacy_groups = [{
        "id": f"part-{part['id']}",
        "title": part["title"],
        "subtitle": part.get("subtitle", ""),
        "moduleIds": [f"legacy:M{number}" for number in part["modules"]],
    } for part in legacy["parts"]]
    return {
        "schema": "owos-academy-curriculum-registry/v1",
        "generated": "2026-08-06",
        "title": "One Water AI Academy",
        "mode": "read-only",
        "authority": {
            "decision": "The legacy M00-M63 curriculum is the source curriculum line. The Fellowship M1-M64 curriculum is a curated program and delivery sequence derived from the same One Water AI body of knowledge.",
            "sourceOfTruth": "hpad66-pixel/owos-learning-content",
            "application": "hpad66-pixel/apas-academy-studio",
            "releaseBoundary": "Registry visibility does not approve proposed content, production, credentialing, publication, or release.",
            "attribution": "Contributor inputs retain contributor identity, source ID, source page, stable item ID, placement decision, and release boundary. A duplicate never overwrites original authorship.",
        },
        "summary": {
            "curriculumLines": 2,
            "registeredModules": 128,
            "legacyModules": 64,
            "fellowshipModules": 64,
            "legacyCurrentSections": sum(module["currentSectionCount"] for module in legacy_modules),
            "legacyProposedAdditions": sum(module["proposedAdditionCount"] for module in legacy_modules),
            "legacyTargetedEnhancements": sum(module["targetedEnhancementCount"] for module in legacy_modules),
            "contributorReviewItems": len(shreya_review["items"]),
            "contributorReviewCounts": shreya_review["summary"],
            "researchStarters": len(research_starters["items"]),
            "roleTracks": len(role_tracks["tracks"]),
            "learningPathways": len(learning_pathways["pathways"]),
        },
        "researchStarters": {
            "schema": research_starters["schema"],
            "authority": research_starters["authority"],
            "items": research_starters["items"],
        },
        "roleTracks": {
            "schema": role_tracks["schema"],
            "authority": role_tracks["authority"],
            "tracks": role_tracks["tracks"],
        },
        "learningPathways": learning_pathways,
        "contributorReviews": [{
            "id": shreya_review["review_id"],
            "title": shreya_review["title"],
            "sourceId": shreya_review["source_id"],
            "sourcePath": shreya_review["source_file"],
            "sourceSha256": shreya_review["source_sha256"],
            "contributor": shreya_review["contributor"],
            "received": shreya_review["received"],
            "reviewed": shreya_review["reviewed"],
            "summary": shreya_review["summary"],
            "authority": shreya_review["authority"],
        }],
        "lines": [
            {
                "id": "legacy",
                "label": "Applied Intelligence source curriculum",
                "shortLabel": "Source curriculum",
                "numbering": "M00-M63",
                "role": "source-curriculum",
                "description": "The governed module source, granular contents, evidence, and proposed additions behind the complete Applied Intelligence curriculum.",
                "source": {"path": str(LEGACY_SOURCE.relative_to(ROOT)), "sha256": sha256(LEGACY_SOURCE)},
                "primaryOutput": {"path": str(LEGACY_PDF.relative_to(ROOT)), "pages": 788, "sha256": sha256(LEGACY_PDF)},
                "groups": legacy_groups,
                "modules": legacy_modules,
            },
            {
                "id": "fellowship",
                "label": "Executive Fellowship delivery sequence",
                "shortLabel": "Fellowship sequence",
                "numbering": "M1-M64",
                "role": "curated-delivery-sequence",
                "description": "The eight-course premium cohort sequence that organizes the shared One Water AI body of knowledge into a 24-week applied program.",
                "source": {"path": str(FELLOWSHIP_SOURCE.relative_to(ROOT)), "sha256": sha256(FELLOWSHIP_SOURCE)},
                "primaryOutput": {"path": str(FELLOWSHIP_PDF.relative_to(ROOT)), "pages": 17, "sha256": sha256(FELLOWSHIP_PDF)},
                "groups": fellowship_courses,
                "modules": fellowship_modules,
            },
        ],
    }


def main() -> None:
    registry = build_registry()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Built {OUTPUT.relative_to(ROOT)} with {registry['summary']['registeredModules']} registered modules")


if __name__ == "__main__":
    main()
