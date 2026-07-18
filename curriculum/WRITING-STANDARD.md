# OWOS Academy Writing Standard (read before writing ANY module)

The goal is a 10 out of 10 lesson that sounds like a real, experienced person explaining
something to a coworker over coffee. Warm, plain, and clear. Never robotic, never clever for
its own sake.

## Hard rules
1. **No em dashes (—) anywhere.** Use commas, periods, parentheses, or words like "and", "so",
   "because", "which". Hyphens in compound words (benefit-cost, one-page) are fine.
2. **No AI/ChatGPT cliché words or phrases.** Banned: delve, leverage, robust, seamless, crucial,
   essential, elevate, unlock, harness, navigate, realm, landscape, tapestry, testament,
   cutting-edge, game-changer, streamline, empower, "in today's world", "it's important to note",
   "at the end of the day", "when it comes to", "dive in", and the "it's not just X, it's Y" pattern.
3. **No cryptic, punchy one-liners.** Do not write clever fragments and expect the reader to
   decode them. Explain the point in full, plain sentences.
4. **Explain everything.** If you use a term, define it in normal English right there. Assume the
   reader is smart but new to this.
5. **Always include a concrete water example.** Every concept gets tied to a real utility situation
   (a main replacement, a lift station, a meter route, the Millpond job, etc.).

## Voice
- Write like you're talking to one person. Use "you" and contractions ("you're", "it's", "that's").
- Short, clear sentences. One idea at a time.
- Prefer everyday words over jargon. When jargon is required (PMBOK, NPV), say the plain meaning first.
- Be encouraging and calm, not hype-y. No exclamation-point energy, no salesy adjectives.
- It is fine to sound a little informal ("Here's the easiest way to tell them apart.").

## Structure every module keeps
- Three levels (Foundation / Practitioner / Leader), switchable.
- Learn by doing: each idea comes with something interactive suited to that topic.
- Droobi guides, in the same plain voice.
- Hover definitions on every new term.
- "Try it yourself" checks at the end, with full plain-English answers.
- A short takeaway in plain sentences.

## Learning components every module should draw from
A module is not just text with one widget. Reach for the right teaching tool for each idea. Every
module should use several of these, and across a chapter you should hit most of them. Each block in
the template carries a small "kind" tag so the learner sees what they are looking at.

1. **Process** — a step-by-step flow (for example the project life cycle), ideally clickable so the
   learner can step through it. Show the order and any gates or checkpoints.
2. **Diagram** — a picture of how parts relate (for example the iron triangle). Make it react to input
   where it helps (drag or step a value and the diagram changes).
3. **Chart** — bars comparing quantities (spend vs. get back, planned vs. actual).
4. **Graph / curve** — a line over time (cash-flow curve, S-curve, burn-down). Mark the meaningful
   points (payback, break-even, the finish).
5. **Framework** — a named way of thinking, drawn simply (a one-question test, a 2x2, a decision flow).
6. **Method** — a numbered "how to do it" recipe the learner can follow on a real job.
7. **Interactivity** — sliders, steppers, drag, and click that recompute live and show the effect.
8. **Engagement** — a "what you will be able to do" checklist, Droobi call-outs that react, progress.
9. **Quizzes, in variety.** Do not use only one kind. Rotate through:
   - **Classify / sort** (put items in the right bucket)
   - **Multiple choice** with instant right/wrong feedback and an explanation
   - **Estimate** (drag a slider to a value, then check against the real answer)
   - **Reflection** (a real-world question with a full plain-English answer revealed)
   - optional: **matching**, **true / false**, **fill-in / short answer**

Rule of thumb: if a section is more than a couple of paragraphs of text with no picture, chart, or
interaction, it is under-built. Add the component that fits.

## Pick visuals from the arsenal, do not default
Before building any module, run the **Selection Prompt** in `VISUAL-ARSENAL.md`. It maps each idea to
the visual that fits its shape (a three-legged stool for sustainability, a fishbone for root cause, a
2x2 for priorities, a wire diagram for a network, and so on). This is required.
- Use at least **4 different visual types** per module, and do not repeat a type unless it truly fits.
- **Never** default to the iron triangle or a cash-flow curve out of habit. That is what makes modules
  feel cheesy and identical. The variety is where the flair, clarity, and uniqueness come from.
- If an idea has no natural visual, keep it as plain text plus a quiz. Do not force a picture.

## Quick before-you-publish check
- Search the file for "—". There should be zero.
- Read it out loud. If a sentence sounds like a press release or a robot, rewrite it.
- Every concept: is there an example? Is every term explained?
- Component check: does the module include a process, a diagram, a chart or curve, a framework, a
  method, and at least three different quiz types? If not, it is not done.
- Reuse `module-template.html` as the starting scaffold so every course looks and behaves the same.

## The three connected reference files (the palette)
Everything is wired together. Before and during a build, use these:
- **`VISUAL-ARSENAL.md`** — the catalog of ~35 visual types plus the Selection Prompt. Run it first.
- **`component-gallery.html`** — every visual (framework, diagram, chart, curve, process, method)
  rendered live. Pick and copy the block you need.
- **`quiz-gallery.html`** — every quiz type (flip cards, matching, multiple choice, multi-select,
  classify, estimate, true/false, fill-in, ordering, reflection) rendered live and working.

**Mix the quiz types.** Do not use the same quiz twice in a row. Rotate them through a chapter so the
learner keeps getting a different kind of task. Aim for at least 3 different quiz types per module.
