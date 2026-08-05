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
    assert sum(len(module["sections"]) for module in registry["lines"][0]["modules"]) == registry["summary"]["legacyCurrentSections"]
    assert sum(len(module["proposals"]) for module in registry["lines"][0]["modules"]) == registry["summary"]["legacyProposedAdditions"]
    print("Academy curriculum registry contract passed")


if __name__ == "__main__":
    main()
