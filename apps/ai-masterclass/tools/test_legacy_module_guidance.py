#!/usr/bin/env python3
"""Validate full guidance and granular placement coverage for legacy M00-M63."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from build_legacy_module_guidance import ROOT, build


CURRICULUM = ROOT / "curriculum" / "one-water-ai-granular-toc.json"
SPECS = ROOT / "curriculum" / "legacy-module-guidance-specs.json"
SHREYA = ROOT / "curriculum" / "shreya-technical-foundations-review.json"
MANIFEST = ROOT / "curriculum" / "legacy-module-guidance-manifest.json"
ALLOWED_DISPOSITIONS = {
    "retain", "refine", "move", "copy", "cross-reference",
    "optional-preparation", "consolidate", "defer",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(paths: list[Path]) -> str:
    result = hashlib.sha256()
    for path in sorted(paths):
        result.update(str(path.relative_to(ROOT)).encode())
        result.update(path.read_bytes())
    return result.hexdigest()


def expected_ids(module: dict, contributor_ids: list[str]) -> list[str]:
    values = [item["id"] for item in module.get("current_sections", [])]
    for proposal in module.get("proposed_additions", []):
        values.append(proposal["id"])
        values.extend(item["id"] for item in proposal.get("subtopics", []))
    values.extend(item["id"] for item in module.get("targeted_enhancements", []))
    values.extend(contributor_ids)
    return values


def main() -> None:
    curriculum = load(CURRICULUM)
    specs = load(SPECS)
    shreya = load(SHREYA)
    manifest = load(MANIFEST)
    assert manifest["schema"] == "owos-legacy-module-guidance-manifest/v1"
    assert manifest["guidedModuleCount"] == manifest["moduleCount"] == 64
    assert manifest["placementRecordCount"] == 1397
    assert len(specs["modules"]) == 63
    assert len({item["code"] for item in specs["modules"]}) == 63
    assert len({item["workProduct"] for item in specs["modules"]}) == 63
    assert len({tuple(item["visuals"]) for item in specs["modules"]}) == 63

    modules = {item["id"]: item for item in curriculum["modules"]}
    contributors: dict[str, list[str]] = {}
    for item in shreya["items"]:
        contributors.setdefault(item["primary_module"], []).append(item["id"])
    known_destinations = {f"legacy:M{number:02d}" for number in range(64)}
    generated_paths: list[Path] = []

    for record in manifest["modules"]:
        code = record["code"]
        module = modules[code]
        package = ROOT / record["packagePath"]
        guidance_path = ROOT / record["guidancePath"]
        guidance = load(guidance_path)
        placement_path = ROOT / guidance["placementRegisterPath"]
        placement = load(placement_path)
        design_path = ROOT / guidance["designBriefPath"]
        staff_path = ROOT / guidance["staffDirectionPath"]
        prompt_path = ROOT / guidance["researchPromptPath"]
        expected = expected_ids(module, contributors.get(code, []))
        actual = [item["contentId"] for item in placement["items"]]
        assert actual == expected, f"Granular placement drift in {code}"
        assert len(actual) == len(set(actual)), f"Duplicate placement ID within {code}"
        assert record["placementRecordCount"] == len(actual)
        assert guidance["moduleId"] == f"legacy:{code}"
        assert len(guidance["learnerOutcomes"]) == 7
        assert len(guidance["curriculumOutcomes"]) >= 5
        assert len(guidance["marketingOutcomes"]) >= 3
        assert guidance["requiredWorkProduct"]
        assert guidance["definitionOfDone"]
        assert guidance["scopeBoundary"]
        assert staff_path.is_file() and prompt_path.is_file() and design_path.is_file()
        assert (package / "README.md").is_file()
        assert (package / "production-status.md").is_file()
        prompt = prompt_path.read_text(encoding="utf-8")
        assert "GOAL.md" in prompt and "PLAN.md" in prompt
        assert code in prompt and guidance["requiredWorkProduct"] in prompt
        for item in placement["items"]:
            assert item["recommendedDisposition"] in ALLOWED_DISPOSITIONS
            assert item["destinationModuleId"] in known_destinations
            assert item["keepReference"] is True
            assert item["reason"]
            if item["contentType"] == "contributor-input":
                assert item["sourceId"] == "INT-002"
                assert item["contributor"] == "Shreya"
        for path in [
            guidance_path, placement_path, design_path, staff_path, prompt_path,
            package / "README.md", package / "production-status.md",
        ]:
            text = path.read_text(encoding="utf-8")
            assert "—" not in text and "–" not in text, f"Prohibited dash in {path}"
            generated_paths.append(path)

    assert sum(record["placementRecordCount"] for record in manifest["modules"]) == 1397
    before = digest(generated_paths)
    rebuilt = build()
    assert rebuilt["placementRecordCount"] == 1397
    after = digest(generated_paths)
    assert before == after, "Guidance build is not deterministic"
    print("Legacy M00-M63 guidance and placement contract passed")


if __name__ == "__main__":
    main()
