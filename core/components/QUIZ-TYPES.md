# Quiz Types Catalog (Markdown reference)

The Markdown list of every quiz in `quiz-gallery.html`. Open the gallery to try them live.
Mix them across a chapter so the learner never does the same kind of task twice in a row.

**Copy the exact quiz block** (its markup and its piece of the script) out of `quiz-gallery.html`.
Do not hand-roll a plainer version. The gallery is the source of truth for how a quiz looks and works.
Also: spell out every acronym in full the first time it appears, and give every term a hover tooltip
(one tooltip element per page, never a second `title`-attribute tooltip).

**Last updated:** 2026-07-18 &middot; **v0.1.0**

| Quiz type | Use it for | How it works |
|---|---|---|
| **Flip cards** | learning terms and definitions, quick recall | click a card, it flips to show the definition |
| **Matching** | pairing items across two columns | click an item on the left, then its match on the right; correct pairs lock green |
| **Multiple choice** | one correct answer | pick an option, instant right/wrong feedback with an explanation |
| **Multi-select** | more than one right answer | tick all that apply, then Check; grades your set |
| **Classify / sort** | putting items in the right bucket | for each item, pick its bucket; scored as you go |
| **Estimate** | guessing a number, then checking it | drag a slider to your guess, then Check against the real answer |
| **True / false** | quick myth-busting | pick True or False per statement; reveals the correct one with a note |
| **Fill in the blank** | recall of a key word or number | type the answer, checked against accepted answers |
| **Put in order** | sequencing the steps of a process | nudge items up or down with arrows, then Check the order |
| **Reflection** | an open question | the reader thinks, then reveals a full plain-English answer |

## Guidance
- Use at least 3 different quiz types per module.
- Do not put the same quiz type twice in a row.
- Match the quiz to the idea: terms fit flip cards, sequences fit ordering, definitions fit matching,
  judgment calls fit multiple choice or reflection, and numbers fit estimate.

To reuse one, copy its block from `quiz-gallery.html` (both the markup and its piece of the script).
The `module-template.html` already includes the common ones ready to fill in.
