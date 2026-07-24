#!/usr/bin/env python3
"""Validate the Data Before AI working retrofit for Chapters 10 through 15."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "apps/data-ai-governance"
CHAPTERS = range(10, 16)


def one(pattern: str) -> Path:
    matches = list((COURSE / "curriculum").glob(pattern))
    if len(matches) != 1:
        raise AssertionError(f"expected one file for {pattern}, found {len(matches)}")
    return matches[0]


def run_conformance(chapter: int) -> None:
    lesson = one(f"module-{chapter}-*.html")
    brief = one(f"design-briefs/module-{chapter}-*.md")
    qa = COURSE / "qa" / f"module-{chapter}-quality-control-report.md"
    command = [
        sys.executable,
        str(ROOT / "tools/course_conformance.py"),
        "--lesson",
        str(lesson),
        "--qa",
        str(qa),
        "--brief",
        str(brief),
        "--contract",
        str(COURSE / ".course/full-module-contract.json"),
    ]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode:
        raise AssertionError(f"Chapter {chapter} conformance failed:\n{result.stderr}")


def main() -> int:
    manifest = json.loads(
        (COURSE / ".course/experience-architecture.json").read_text(encoding="utf-8")
    )
    quiz_sequences = set()
    interaction_sequences = set()
    visual_sequences = set()
    count_vectors = set()

    for chapter in CHAPTERS:
        lesson = one(f"module-{chapter}-*.html")
        text = lesson.read_text(encoding="utf-8")
        soup = BeautifulSoup(text, "html.parser")
        config = manifest["lessons"][lesson.name]
        for block in soup.select('script[type="application/json"]'):
            json.loads(block.get_text())
        assert "content pending" not in text.lower()
        assert "structure-ready-content-pending" not in text
        assert "—" not in text and "–" not in text
        assert soup.find("meta", attrs={"name": "owos-release-state"})["content"] == "working-review"
        assert soup.find("meta", attrs={"name": "owos-lesson-archetype"})["content"] == config["archetype"]
        assert (
            soup.find("meta", attrs={"name": "owos-signature-mechanism"})["content"]
            == config["signature_mechanism"]
        )
        visuals = tuple(node["data-visual-type"] for node in soup.select("[data-visual-type]"))
        quizzes = tuple(node["data-quiz-type"] for node in soup.select("[data-quiz-type]"))
        interactions = tuple(
            node["data-purposeful-interaction"]
            for node in soup.select("[data-purposeful-interaction]")
        )
        assert 2 <= len(set(visuals)) <= 3, (chapter, visuals)
        assert interactions, chapter
        assert quizzes, chapter
        assert len(soup.select("[data-module-faq] details")) >= 5
        assert len(soup.select("[data-worked-example]")) >= 1
        assert len(soup.select(".term[data-def]")) >= 5
        assert visuals not in visual_sequences, (chapter, visuals)
        assert quizzes not in quiz_sequences, (chapter, quizzes)
        assert interactions not in interaction_sequences, (chapter, interactions)
        visual_sequences.add(visuals)
        quiz_sequences.add(quizzes)
        interaction_sequences.add(interactions)
        vector = (
            len(soup.select("main section")),
            len(soup.find_all("button")),
            len(soup.find_all(["input", "select", "textarea"])),
            len(soup.find_all("details")),
        )
        assert vector not in count_vectors, (chapter, vector)
        count_vectors.add(vector)
        run_conformance(chapter)

    audit = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/course_distinctiveness.py"),
            "--course",
            str(COURSE),
            "--json",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    report = json.loads(audit.stdout)
    retrofit_names = {one(f"module-{chapter}-*.html").name for chapter in CHAPTERS}
    retrofit_errors = [
        error for error in report["errors"] if any(name in error for name in retrofit_names)
    ]
    assert not retrofit_errors, retrofit_errors
    print(
        "PASS: Chapters 10-15 conform individually and have unique visual, quiz, "
        "interaction, and control-count fingerprints."
    )
    if report["errors"]:
        print(
            f"EXPECTED COURSE BLOCK: {len(report['errors'])} distinctiveness findings "
            "remain in content-pending Chapters 16-24."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
