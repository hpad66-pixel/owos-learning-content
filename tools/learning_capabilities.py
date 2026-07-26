#!/usr/bin/env python3
"""Load the shared OWOS learning-capability registry."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "core/learning-capabilities/registry.yaml"


class LearningCapabilityError(ValueError):
    """Raised when the shared learning-capability registry is invalid."""


def load_learning_capabilities() -> dict[str, Any]:
    try:
        data = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        raise LearningCapabilityError(f"{REGISTRY_PATH}: cannot read registry: {error}") from error
    if not isinstance(data, dict):
        raise LearningCapabilityError("learning-capability registry must be an object")
    if data.get("registry_version") != 1:
        raise LearningCapabilityError("learning-capability registry_version must be 1")
    for key in (
        "engines",
        "catalog_sources",
        "assessment_types",
        "interaction_components",
        "experience_contract",
        "continuing_education",
    ):
        if not data.get(key):
            raise LearningCapabilityError(f"learning-capability registry is missing {key}")
    for label, relative in data["catalog_sources"].items():
        path = ROOT / str(relative)
        if not path.is_file():
            raise LearningCapabilityError(f"catalog source {label} does not exist: {relative}")
    return data


def assessment_types(
    registry: dict[str, Any],
    engine: str | None = None,
) -> set[str]:
    if engine is None:
        return set(registry["assessment_types"])
    return {
        identifier
        for identifier, record in registry["assessment_types"].items()
        if engine in record.get("compiler_support", [])
    }


def interaction_components(registry: dict[str, Any]) -> set[str]:
    return {str(item) for item in registry["interaction_components"]}


def visual_component_ids(registry: dict[str, Any]) -> set[str]:
    return {str(item) for item in registry.get("visual_component_ids", [])}
