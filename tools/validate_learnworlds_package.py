#!/usr/bin/env python3
"""Validate a MODULE-PACKAGE.md file against owos-learnworlds-module/v1.

Usage:
    python3 tools/validate_learnworlds_package.py <path-to-MODULE-PACKAGE.md> \
        [--placement-register <path.json>] [--claims-register <path.md>] [--json]

Exit code 0 when every rule passes, 1 when any rule fails.
Structure only. This script does not approve facts, claims, placements, or release.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("PyYAML is required: pip install pyyaml --break-system-packages\n")
    raise SystemExit(2)

SCHEMA = "owos-learnworlds-module/v1"

ACTIVITY_TYPES = {
    "ebook", "video", "audio", "pdf", "presentation", "embed", "external-link",
    "html5", "scorm", "exam", "self-assessment", "form", "reflection-journal",
    "certificate",
}
QUESTION_TYPES = {
    "multiple-choice", "multiple-response", "true-false", "fill-blank",
    "matching", "ordering", "open-ended",
}
VISUAL_TYPES = {
    "diagram", "flow", "matrix", "role-network", "timeline", "comparison",
    "data-chart", "map", "annotated-screenshot",
}
INTERACTION_TYPES = {
    "decision-branch", "sorter", "self-diagnostic", "builder", "hotspot",
    "comparison-table", "scenario-walkthrough",
}
ASSESSMENT_ACTIVITY_TYPES = {"exam", "self-assessment"}

ALLOWED_STATUS = {
    "research-draft", "blueprint-candidate", "manuscript-candidate",
    "production-candidate", "release-candidate",
}
PROHIBITED_STATUS_WORDS = {
    "approved", "production ready", "production-ready", "public", "complete",
    "certified", "released",
}

REQUIRED_FRONT_MATTER = [
    "schema", "courseId", "moduleId", "moduleCode", "title", "sectionTitle",
    "status", "approvalState", "approvalRecord", "workProduct",
    "seatTimeMinutes", "readingLevelTarget", "accessibilityTarget",
    "registers", "reviewers", "outcomes", "claims",
]

BANNED_PHRASES = [
    "guarantee", "ensure compliance", "certify", "eliminate risk",
    "revolutioniz", "seamless", "cutting edge", "cutting-edge", "unlock",
    "game changer", "game-changer", "state of the art", "world class",
]
BANNED_VERB_LEVERAGE = re.compile(r"\bleverag(e|es|ing|ed)\b", re.I)

DASHES = {"—": "em dash", "–": "en dash"}

FENCE_RE = re.compile(r"^```(owos-[a-z]+)\s*$")
H2_RE = re.compile(r"^##\s+(?!#)(.+?)\s*$")
CLAIM_IN_PROSE_RE = re.compile(r"\[(CLM-[A-Z0-9]+-\d+)\]")
CLAIM_ID_RE = re.compile(r"^CLM-[A-Z0-9]+-\d+$")
ALT_TEXT_MAX = 250


@dataclass
class Report:
    failures: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    stats: dict = field(default_factory=dict)

    def fail(self, rule: str, message: str, line: int | None = None) -> None:
        self.failures.append({"rule": rule, "message": message, "line": line})

    def warn(self, rule: str, message: str, line: int | None = None) -> None:
        self.warnings.append({"rule": rule, "message": message, "line": line})

    @property
    def ok(self) -> bool:
        return not self.failures


def split_front_matter(text: str, rep: Report):
    if not text.startswith("---\n"):
        rep.fail("FM-001", "File must begin with YAML front matter delimited by ---", 1)
        return None, text, 0
    end = text.find("\n---\n", 4)
    if end == -1:
        rep.fail("FM-001", "Front matter block is not closed with ---", 1)
        return None, text, 0
    raw = text[4:end]
    body = text[end + 5:]
    offset = raw.count("\n") + 3
    try:
        fm = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        rep.fail("FM-002", f"Front matter is not valid YAML: {exc}", 1)
        return None, body, offset
    if not isinstance(fm, dict):
        rep.fail("FM-002", "Front matter must be a mapping", 1)
        return None, body, offset
    return fm, body, offset


def parse_blocks(body: str, offset: int, rep: Report):
    """Return (blocks, h2s). blocks are (kind, dict, line). h2s are (title, line)."""
    blocks, h2s = [], []
    lines = body.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        m_h2 = H2_RE.match(line)
        if m_h2:
            h2s.append((m_h2.group(1), offset + i + 1))
            i += 1
            continue
        m_f = FENCE_RE.match(line)
        if m_f:
            kind = m_f.group(1)
            start = i
            i += 1
            buf = []
            while i < len(lines) and lines[i].strip() != "```":
                buf.append(lines[i])
                i += 1
            if i >= len(lines):
                rep.fail("BLK-001", f"Unclosed {kind} block", offset + start + 1)
                break
            try:
                data = yaml.safe_load("\n".join(buf)) or {}
            except yaml.YAMLError as exc:
                rep.fail("BLK-002", f"{kind} block is not valid YAML: {exc}", offset + start + 1)
                data = {}
            if not isinstance(data, dict):
                rep.fail("BLK-002", f"{kind} block must be a mapping", offset + start + 1)
                data = {}
            blocks.append((kind, data, offset + start + 1))
            i += 1
            continue
        i += 1
    return blocks, h2s


def check_front_matter(fm: dict, rep: Report) -> None:
    for key in REQUIRED_FRONT_MATTER:
        if key not in fm:
            rep.fail("FM-003", f"Missing required front matter key: {key}", 1)

    if fm.get("schema") != SCHEMA:
        rep.fail("FM-004", f"schema must be {SCHEMA}, found {fm.get('schema')!r}", 1)

    status = str(fm.get("status", "")).strip()
    if status and status not in ALLOWED_STATUS:
        rep.fail("FM-005", f"status {status!r} is not in the allowed vocabulary", 1)
    if status.lower() in PROHIBITED_STATUS_WORDS:
        rep.fail("FM-006", f"status {status!r} claims approval that no repository record supports", 1)

    approval_record = str(fm.get("approvalRecord", "none")).strip().lower()
    if fm.get("approvalState") != "proposed" and approval_record in {"none", ""}:
        rep.fail("FM-007", "approvalState is not 'proposed' but approvalRecord names no record", 1)

    for key in ("claims", "sources", "evidenceBoundaries", "placement"):
        if key not in (fm.get("registers") or {}):
            rep.fail("FM-008", f"registers.{key} is required", 1)

    reviewers = fm.get("reviewers") or {}
    for role in ("utilityPractitioner", "noviceLearner", "accessibility", "sourceVerification"):
        if role not in reviewers:
            rep.fail("FM-009", f"reviewers.{role} must be present, use 'unassigned' if not yet named", 1)
        elif str(reviewers[role]).strip().lower() == "unassigned" and status in {
            "production-candidate", "release-candidate"
        }:
            rep.fail("FM-010", f"reviewers.{role} is unassigned but status is {status}", 1)

    for cid in fm.get("claims") or []:
        if not CLAIM_ID_RE.match(str(cid)):
            rep.fail("FM-011", f"Malformed claim ID in front matter: {cid!r}", 1)


def check_outcomes(fm: dict, activity_ids: set, question_ids: set,
                   interaction_ids: set, rep: Report) -> None:
    outcomes = fm.get("outcomes") or []
    if not outcomes:
        rep.fail("OUT-001", "At least one outcome is required", 1)
    known = activity_ids | question_ids | interaction_ids
    seen_ids = set()
    for out in outcomes:
        if not isinstance(out, dict):
            rep.fail("OUT-002", f"Outcome entries must be mappings, found {out!r}", 1)
            continue
        oid = out.get("id")
        if not oid:
            rep.fail("OUT-002", "Outcome is missing an id", 1)
            continue
        if oid in seen_ids:
            rep.fail("OUT-003", f"Duplicate outcome id {oid}", 1)
        seen_ids.add(oid)
        if not str(out.get("statement", "")).strip():
            rep.fail("OUT-004", f"Outcome {oid} has no statement", 1)
        verb = str(out.get("verb", "")).strip().lower()
        vague = {"understand", "know", "learn", "appreciate", "be aware", "grasp", "familiarize"}
        if verb in vague:
            rep.fail("OUT-005", f"Outcome {oid} uses unobservable verb {verb!r}", 1)
        ev = out.get("evidence")
        ev_list = [e.strip() for e in ev.split(",")] if isinstance(ev, str) else list(ev or [])
        if not ev_list:
            rep.fail("OUT-006", f"Outcome {oid} names no completion evidence, backward design gate", 1)
        for e in ev_list:
            if e and e not in known:
                rep.fail("OUT-007", f"Outcome {oid} cites unknown evidence id {e}", 1)


def check_activities(blocks, h2s, fm, rep: Report):
    activities = [(d, ln) for k, d, ln in blocks if k == "owos-activity"]
    code = str(fm.get("moduleCode", "")).strip()
    seen, ids = set(), []

    if len(activities) != len(h2s):
        rep.fail(
            "ACT-001",
            f"Each level 2 heading needs exactly one owos-activity block. "
            f"Found {len(h2s)} headings and {len(activities)} activity blocks.",
        )

    for (data, line), (heading, h_line) in zip(activities, h2s):
        aid = str(data.get("id", "")).strip()
        if not aid:
            rep.fail("ACT-002", "Activity block has no id", line)
        else:
            ids.append(aid)
            if aid in seen:
                rep.fail("ACT-003", f"Duplicate activity id {aid}", line)
            seen.add(aid)
            if code and not re.match(rf"^{re.escape(code)}\.A\d{{2}}$", aid):
                rep.fail("ACT-004", f"Activity id {aid} must match {code}.ANN", line)
        atype = str(data.get("type", "")).strip()
        if atype not in ACTIVITY_TYPES:
            rep.fail("ACT-005", f"Activity {aid or '?'} type {atype!r} is not in the closed list", line)
        title = str(data.get("title", "")).strip()
        if title != heading.strip():
            rep.fail(
                "ACT-006",
                f"Activity {aid or '?'} title does not match its heading. "
                f"Heading {heading.strip()!r}, title {title!r}",
                line,
            )
        if not data.get("outcomeRefs"):
            rep.fail("ACT-007", f"Activity {aid or '?'} names no outcomeRefs", line)
        if not isinstance(data.get("estimatedMinutes"), (int, float)):
            rep.fail("ACT-008", f"Activity {aid or '?'} needs a numeric estimatedMinutes", line)
    return activities, seen


def check_seat_time(activities, fm, rep: Report) -> None:
    total = sum(
        d.get("estimatedMinutes", 0)
        for d, _ in activities
        if isinstance(d.get("estimatedMinutes"), (int, float))
    )
    declared = fm.get("seatTimeMinutes")
    if not isinstance(declared, (int, float)) or declared <= 0:
        rep.fail("TIME-001", "seatTimeMinutes must be a positive number", 1)
        return
    lo, hi = declared * 0.9, declared * 1.1
    if not (lo <= total <= hi):
        rep.fail(
            "TIME-002",
            f"Activity minutes total {total} but seatTimeMinutes is {declared}. "
            f"Allowed range is {lo:.1f} to {hi:.1f}.",
        )


def check_questions(blocks, activities, fm, rep: Report):
    by_id = {str(d.get("id", "")): d for d, _ in activities}
    qs = [(d, ln) for k, d, ln in blocks if k == "owos-question"]
    types, ids = set(), set()
    for data, line in qs:
        qid = str(data.get("id", "")).strip()
        if not qid:
            rep.fail("Q-001", "Question block has no id", line)
        elif qid in ids:
            rep.fail("Q-002", f"Duplicate question id {qid}", line)
        ids.add(qid)

        qtype = str(data.get("type", "")).strip()
        if qtype not in QUESTION_TYPES:
            rep.fail("Q-003", f"Question {qid or '?'} type {qtype!r} is not in the closed list", line)
        types.add(qtype)

        act = str(data.get("activity", "")).strip()
        if act not in by_id:
            rep.fail("Q-004", f"Question {qid or '?'} references unknown activity {act!r}", line)
        elif by_id[act].get("type") not in ASSESSMENT_ACTIVITY_TYPES:
            rep.fail(
                "Q-005",
                f"Question {qid or '?'} attaches to activity {act} of type "
                f"{by_id[act].get('type')!r}, which is not an assessment",
                line,
            )
        if not str(data.get("stem", "")).strip():
            rep.fail("Q-006", f"Question {qid or '?'} has no stem", line)
        if not data.get("outcomeRef"):
            rep.fail("Q-007", f"Question {qid or '?'} proves no outcome", line)
        for fb in ("feedbackCorrect", "feedbackIncorrect"):
            if not str(data.get(fb, "")).strip():
                rep.fail("Q-008", f"Question {qid or '?'} is missing {fb}, retry with explanation is required", line)
        if qtype in {"multiple-choice", "multiple-response", "matching", "ordering"}:
            opts = data.get("options") or []
            if len(opts) < 2:
                rep.fail("Q-009", f"Question {qid or '?'} needs at least two options", line)
            correct = data.get("correct")
            idxs = correct if isinstance(correct, list) else [correct]
            for c in idxs:
                if not isinstance(c, int) or not (1 <= c <= len(opts)):
                    rep.fail("Q-010", f"Question {qid or '?'} correct index {c!r} is out of range", line)
    return ids, types


def check_visuals_and_interactions(blocks, rep: Report):
    vis = [(d, ln) for k, d, ln in blocks if k == "owos-visual"]
    inter = [(d, ln) for k, d, ln in blocks if k == "owos-interaction"]
    vtypes, itypes, iids = set(), set(), set()

    for data, line in vis:
        vid = str(data.get("id", "?"))
        vtype = str(data.get("type", "")).strip()
        if vtype not in VISUAL_TYPES:
            rep.fail("VIS-001", f"Visual {vid} type {vtype!r} is not in the closed list", line)
        vtypes.add(vtype)
        alt = str(data.get("altText", "") or "").strip()
        if not alt:
            rep.fail("VIS-002", f"Visual {vid} has no altText, accessibility gate", line)
        elif len(alt) > ALT_TEXT_MAX:
            rep.fail("VIS-003", f"Visual {vid} altText is {len(alt)} characters, limit is {ALT_TEXT_MAX}", line)

    for data, line in inter:
        iid = str(data.get("id", "?"))
        iids.add(iid)
        itype = str(data.get("type", "")).strip()
        if itype not in INTERACTION_TYPES:
            rep.fail("INT-001", f"Interaction {iid} type {itype!r} is not in the closed list", line)
        itypes.add(itype)
    return vtypes, itypes, iids


def check_design_minimums(vtypes, itypes, qtypes, fm, rep: Report) -> None:
    exception = str(fm.get("approvalRecord", "none")).strip().lower() not in {"none", ""}
    checks = [
        ("MIN-001", len(vtypes), 4, "distinct visual types"),
        ("MIN-002", len(itypes), 2, "purposeful interaction types"),
        ("MIN-003", len(qtypes), 3, "distinct question types"),
    ]
    for rule, actual, need, label in checks:
        if actual < need:
            msg = f"Full module needs at least {need} {label}, found {actual}"
            if exception:
                rep.warn(rule, msg + " (approvalRecord present, exception may apply)")
            else:
                rep.fail(rule, msg)


def check_charter_builder(itypes, fm, rep: Report) -> None:
    if str(fm.get("moduleCode", "")).upper() == "M00" and "builder" not in itypes:
        rep.fail("M00-001", "M00 must contain an owos-interaction of type 'builder' for the Learning Charter")


def check_prose(body: str, fm: dict, offset: int, rep: Report):
    lines = body.split("\n")
    in_fence = False
    declared = {str(c) for c in (fm.get("claims") or [])}
    used = set()

    for i, line in enumerate(lines):
        ln = offset + i + 1
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        for ch, name in DASHES.items():
            if ch in line:
                rep.fail("WRT-001", f"Contains an {name}, which the writing standard prohibits", ln)
        if in_fence:
            continue
        low = line.lower()
        for phrase in BANNED_PHRASES:
            if phrase in low:
                rep.fail("WRT-002", f"Banned marketing phrase {phrase!r} in learner facing prose", ln)
        if BANNED_VERB_LEVERAGE.search(line):
            rep.fail("WRT-003", "Banned verb 'leverage' in learner facing prose", ln)
        used.update(CLAIM_IN_PROSE_RE.findall(line))

    for cid in sorted(used - declared):
        rep.fail("CLM-001", f"Prose cites {cid} but it is not listed in front matter claims")
    for cid in sorted(declared - used):
        rep.warn("CLM-002", f"Front matter declares {cid} but no prose cites it")
    return used


def check_placement(fm: dict, blocks, register_path: Path | None, rep: Report) -> None:
    if register_path is None or not register_path.exists():
        rep.warn("PLC-000", "Placement register not supplied, placement rules skipped")
        return
    try:
        reg = json.loads(register_path.read_text())
    except json.JSONDecodeError as exc:
        rep.fail("PLC-001", f"Placement register is not valid JSON: {exc}")
        return
    items = reg.get("items") or []
    known = {str(i.get("contentId")) for i in items}
    referenced = set()
    for _, data, line in blocks:
        for ref in data.get("placementRefs") or []:
            ref = str(ref)
            referenced.add(ref)
            if ref not in known:
                rep.fail("PLC-002", f"placementRef {ref} is not in the placement register", line)

    this_module = str(fm.get("moduleId", ""))
    for item in items:
        cid = str(item.get("contentId"))
        disp = str(item.get("recommendedDisposition", ""))
        dest = str(item.get("destinationModuleId", ""))
        if dest == this_module and disp in {"retain", "refine", "consolidate"} and cid not in referenced:
            rep.fail(
                "PLC-003",
                f"Placement record {cid} is dispositioned {disp} into this module but no activity "
                f"references it. The no-delete rule is broken.",
            )


def check_claims_register(fm: dict, used: set, register_path: Path | None, rep: Report) -> None:
    if register_path is None or not register_path.exists():
        rep.warn("CLM-000", "Claims register not supplied, claim state rules skipped")
        return
    text = register_path.read_text()
    status = str(fm.get("status", ""))
    for cid in sorted({str(c) for c in (fm.get("claims") or [])} | used):
        if cid not in text:
            rep.fail("CLM-003", f"Claim {cid} does not appear in the claims register")
            continue
        for line in text.splitlines():
            if cid in line and re.search(r"\bVERIFY\b", line):
                if status in {"manuscript-candidate", "production-candidate", "release-candidate"}:
                    rep.fail("CLM-004", f"Claim {cid} is marked VERIFY but module status is {status}")
                else:
                    rep.warn("CLM-005", f"Claim {cid} is marked VERIFY, allowed at status {status}")
                break


def validate(path: Path, placement: Path | None, claims: Path | None) -> Report:
    rep = Report()
    text = path.read_text()

    fm, body, offset = split_front_matter(text, rep)
    if fm is None:
        return rep

    check_front_matter(fm, rep)
    blocks, h2s = parse_blocks(body, offset, rep)
    activities, act_ids = check_activities(blocks, h2s, fm, rep)
    check_seat_time(activities, fm, rep)
    q_ids, q_types = check_questions(blocks, activities, fm, rep)
    v_types, i_types, i_ids = check_visuals_and_interactions(blocks, rep)
    check_outcomes(fm, act_ids, q_ids, i_ids, rep)
    check_design_minimums(v_types, i_types, q_types, fm, rep)
    check_charter_builder(i_types, fm, rep)
    used = check_prose(body, fm, offset, rep)
    check_placement(fm, blocks, placement, rep)
    check_claims_register(fm, used, claims, rep)

    rep.stats = {
        "activities": len(activities),
        "questions": len(q_ids),
        "questionTypes": sorted(q_types),
        "visualTypes": sorted(v_types),
        "interactionTypes": sorted(i_types),
        "claimsCited": len(used),
        "status": fm.get("status"),
        "approvalState": fm.get("approvalState"),
    }
    return rep


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate an OWOS module package file.")
    ap.add_argument("package")
    ap.add_argument("--placement-register", default=None)
    ap.add_argument("--claims-register", default=None)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rep = validate(
        Path(args.package),
        Path(args.placement_register) if args.placement_register else None,
        Path(args.claims_register) if args.claims_register else None,
    )

    if args.json:
        print(json.dumps({
            "package": args.package,
            "conformant": rep.ok,
            "failures": rep.failures,
            "warnings": rep.warnings,
            "stats": rep.stats,
        }, indent=2))
        return 0 if rep.ok else 1

    print(f"Package: {args.package}")
    print(f"Schema:  {SCHEMA}")
    print()
    for f in rep.failures:
        loc = f" line {f['line']}" if f["line"] else ""
        print(f"  FAIL [{f['rule']}]{loc}: {f['message']}")
    for w in rep.warnings:
        loc = f" line {w['line']}" if w["line"] else ""
        print(f"  WARN [{w['rule']}]{loc}: {w['message']}")
    print()
    for k, v in rep.stats.items():
        print(f"  {k}: {v}")
    print()
    print(f"  {len(rep.failures)} failure(s), {len(rep.warnings)} warning(s)")
    print("  RESULT: " + ("CONFORMANT (structure only, no content approval)" if rep.ok else "NOT CONFORMANT"))
    return 0 if rep.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
