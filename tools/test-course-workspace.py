#!/usr/bin/env python3
"""Regression tests for persistent OWOS course workspace scans."""

from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("course_workspace.py")
SPEC = importlib.util.spec_from_file_location("course_workspace", MODULE_PATH)
assert SPEC and SPEC.loader
course_workspace = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(course_workspace)


def run() -> None:
    with tempfile.TemporaryDirectory() as temporary:
        course = Path(temporary) / "test-course"
        inbox = course / "inbox"
        conversations = course / "conversations"
        inbox.mkdir(parents=True)
        conversations.mkdir(parents=True)
        (inbox / "README.md").write_text("instructions", encoding="utf-8")
        source = inbox / "source.txt"
        source.write_text("first", encoding="utf-8")

        first = course_workspace.scan_course(course)
        assert first["changes"]["new"] == ["inbox/source.txt"]
        assert first["totals"]["tracked"] == 1

        second = course_workspace.scan_course(course)
        assert second["changes"]["new"] == []
        assert second["changes"]["unchanged"] == ["inbox/source.txt"]

        source.write_text("second", encoding="utf-8")
        note = conversations / "direction.md"
        note.write_text("Build for utility leaders.", encoding="utf-8")
        third = course_workspace.scan_course(course)
        assert third["changes"]["changed"] == ["inbox/source.txt"]
        assert third["changes"]["new"] == ["conversations/direction.md"]

        source.unlink()
        fourth = course_workspace.scan_course(course)
        assert fourth["changes"]["removed"] == ["inbox/source.txt"]


if __name__ == "__main__":
    run()
    print("course workspace tests passed")
