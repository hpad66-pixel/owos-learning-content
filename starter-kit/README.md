# Starter Kit — One Water OS Project

Copy this whole folder to start a new job. Rename it to the project, then open it with Claude
(Fable 5, effort High) and say: **"Read CLAUDE.md and interview me for the brief."**

Everything here is a **plain file**. The pretty HTML dashboards are always *regenerated* from these
files — you never hand-edit HTML, and the file is always the source of truth. Stay model-agnostic:
if any model is down, paste these same files into another and keep going.

## What's in the folder

| File | What it holds | Classification |
|---|---|---|
| `CLAUDE.md` | Project instructions Claude reads every session | Internal |
| `Brief.md` | The project brief (built by interview — Sheet 03) | Internal |
| `Board.md` | Kanban data (phases + cards) | Internal |
| `Schedule.md` | Critical path, milestones, dependencies | Internal |
| `Budget.csv` | Estimated / committed / actual / forecast per line | **Restricted** |
| `Risks.md` | Risk register (P × I, owner, trigger, mitigation, contingency) | **Restricted** |
| `Permits.md` | Permit & Sunshine 811 locate tracker | Internal |
| `Compliance.md` | Safety & regulatory checklist, tied to phases | Internal |
| `Stakeholders.md` | Stakeholder map + RACI | Internal |
| `Classification.md` | Which files are cleared for the public site | Internal |
| `Notes.md` | Dated running log (absolute dates only) | Internal |
| `Inbox.md` | Quick-capture — whatever you jot between sessions | Internal |

## The order of operations (maps to the playbook)

1. `CLAUDE.md` sets the frame → **interview** builds `Brief.md` (Sheet 03)
2. Constraints → `Schedule.md` critical path (Sheets 02, 07)
3. Blind Spot Pass → `Risks.md` (Sheets 05, 06)
4. Run it: weekly ritual updates `Board.md`, `Schedule.md`, `Budget.csv`, `Permits.md` (Sheet 14)
5. Reports & public site generated on demand (Sheets 12, 13, 11)
6. Close out → `Retro.md` → `Next Project Starter.md` (Sheet 17)

## The one rule
Classify before you publish (Sheet 00). Only files on the cleared list in `Classification.md`
ever go to `/public`. Infrastructure detail never leaves the control center.
