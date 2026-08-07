#!/usr/bin/env python3
"""Validate the Academy curriculum registry contract."""

from build_academy_curriculum_registry import build_registry


def main() -> None:
    registry = build_registry()
    assert registry["schema"] == "owos-academy-curriculum-registry/v1"
    assert registry["mode"] == "read-only"
    assert registry["summary"]["registeredModules"] == 128
    assert [line["role"] for line in registry["lines"]] == ["source-curriculum", "curated-delivery-sequence"]
    assert [len(line["modules"]) for line in registry["lines"]] == [64, 64]
    module_ids = [module["id"] for line in registry["lines"] for module in line["modules"]]
    assert len(module_ids) == len(set(module_ids)) == 128
    assert registry["lines"][0]["primaryOutput"]["pages"] == 788
    assert registry["authority"]["sourceOfTruth"] == "hpad66-pixel/owos-learning-content"
    assert registry["summary"]["contributorReviewItems"] == 56
    assert registry["summary"]["researchStarters"] == 64
    assert registry["summary"]["roleTracks"] == 15
    assert registry["summary"]["learningPathways"] == 6
    assert registry["summary"]["guidedLegacyModules"] == 64
    assert registry["summary"]["legacyPlacementRecords"] == 1397
    assert registry["legacyGuidance"]["moduleCount"] == 64
    assert registry["legacyGuidance"]["placementRecordCount"] == 1397
    assert len(registry["contributorReviews"]) == 1
    assert registry["contributorReviews"][0]["contributor"]["name"] == "Shreya"
    contributor_inputs = [item for module in registry["lines"][0]["modules"] for item in module["contributorInputs"]]
    assert len(contributor_inputs) == 56
    assert len({item["id"] for item in contributor_inputs}) == 56
    assert all(item["sourceId"] == "INT-002" for item in contributor_inputs)
    assert len(registry["researchStarters"]["items"]) == 64
    assert len(registry["roleTracks"]["tracks"]) == 15
    assert len(registry["learningPathways"]["pathways"]) == 6
    assert sum(pathway["kind"] == "universal-core" for pathway in registry["learningPathways"]["pathways"]) == 1
    assert sum(pathway["kind"] == "role-lens" for pathway in registry["learningPathways"]["pathways"]) == 5
    assert len(next(pathway for pathway in registry["learningPathways"]["pathways"] if pathway["id"] == "one-water-ai-core")["moduleIds"]) == 64
    assert all(module.get("researchStarter") for module in registry["lines"][1]["modules"])
    m00 = next(module for module in registry["lines"][0]["modules"] if module["id"] == "legacy:M00")
    assert m00["guidance"]["schema"] == "owos-module-guidance/v1"
    assert len(m00["guidance"]["learnerOutcomes"]) == 7
    assert len(m00["guidance"]["placement"]["items"]) == 48
    assert "GOAL.md" in m00["guidance"]["researchPromptMarkdown"]
    guided_modules = [module for module in registry["lines"][0]["modules"] if module.get("guidance")]
    assert len(guided_modules) == 64
    assert all(len(module["guidance"]["learnerOutcomes"]) == 7 for module in guided_modules)
    assert all(module["guidance"]["requiredWorkProduct"] for module in guided_modules)
    assert all("GOAL.md" in module["guidance"]["researchPromptMarkdown"] for module in guided_modules)
    assert all("PLAN.md" in module["guidance"]["researchPromptMarkdown"] for module in guided_modules)
    assert sum(len(module["guidance"]["placement"]["items"]) for module in guided_modules) == 1397
    assert sum(len(module["sections"]) for module in registry["lines"][0]["modules"]) == registry["summary"]["legacyCurrentSections"]
    assert sum(len(module["proposals"]) for module in registry["lines"][0]["modules"]) == registry["summary"]["legacyProposedAdditions"]
    print("Academy curriculum registry contract passed")


if __name__ == "__main__":
    main()
