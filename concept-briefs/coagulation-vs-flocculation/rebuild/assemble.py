#!/usr/bin/env python3
"""Assemble index.html from the shared shell style, body.html, and logic.js."""
import pathlib, re
here = pathlib.Path(__file__).parent
root = here.parents[2]
shell = (root / "concept-briefs/detention-retention-and-infiltration/variant-b/index.html").read_text()
style = re.search(r"<style>.*?</style>", shell, re.S).group(0)
body = (here / "body.html").read_text().strip()
logic = (here / "logic.js").read_text().strip()

PLANE = """
<!-- COMMUNITY AND VALUE PLANE -->
<section class="plane" aria-labelledby="pl-t">
  <div class="wrap">
    <p class="kicker">From understanding to practice</p>
    <h2 id="pl-t">This is where the concept stops and your plant starts.</h2>
    <div class="prose">
      <p>A brief can give you the mechanism, the vocabulary, and the questions. It cannot tell you
        what is true in your basin on your water today.</p>
    </div>
    <div class="comm-grid">
      <div class="comm-card">
        <h3>Bring a question to practitioners</h3>
        <p>Operators, chemists, and engineers who run these processes answer here. Discussion is
          practitioner conversation, not verified instruction, and it is labelled that way.</p>
        <p style="margin-bottom:6px"><b>Good questions to open with:</b></p>
        <span class="seed">How did you find your window?</span>
        <span class="seed">What finally told you it was mechanical?</span>
        <span class="seed">Do you jar below your setpoint?</span>
        <a class="cta" href="/community?brief=owos:concept-brief:001">Open the practitioner community</a>
      </div>
      <div class="comm-card">
        <h3>Found something wrong here?</h3>
        <p>Say so. A correction is not a comment thread. It becomes a tracked proposal, goes back
          through source and qualified review, and if it holds this brief is versioned and anyone who
          completed it is notified.</p>
        <ul><li>Name the exact sentence.</li><li>Give the source that contradicts it.</li>
          <li>We publish the outcome either way.</li></ul>
        <a class="cta" href="/community?brief=owos:concept-brief:001&amp;intent=correction">Propose a correction</a>
      </div>
    </div>
    <div class="value">
      <h3>Why this is free to read</h3>
      <p>This brief exists because a reasonable reflex costs the sector real money. Adding coagulant
        is fast, visible, and under operator control, and it is often the wrong lever. The cost lands
        in chemical spend, in residuals months later, and in filter runs nobody traced back.</p>
      <p>APAS.ai builds and governs this material. Briefs are published open because a shared
        vocabulary is only worth anything if everyone at the table has it.</p>
    </div>
    <div class="sponsors">
      <div class="sponsor-head">
        <h3>Supported by the companies that build and run this infrastructure</h3>
        <p>Placement is paid. Editorial is not for sale. No sponsor sees a brief before it publishes,
          and none has any authority over a claim, a source, a correction, a review, or a release.
          That separation is the product.</p>
      </div>
      <ul class="sponsor-row">
        <li class="sponsor"><span class="sponsor-logo" data-cat="CH" aria-hidden="true"></span>
          <span class="sponsor-name">Treatment chemicals<span>Coagulants, polymers, pH control</span></span></li>
        <li class="sponsor"><span class="sponsor-logo" data-cat="IN" aria-hidden="true"></span>
          <span class="sponsor-name">Instrumentation<span>Turbidity, streaming current, dosing control</span></span></li>
        <li class="sponsor"><span class="sponsor-logo" data-cat="EQ" aria-hidden="true"></span>
          <span class="sponsor-name">Mixing and basin equipment<span>Flocculators, drives, baffles</span></span></li>
        <li class="sponsor sponsor-open"><span class="sponsor-logo" data-cat="+" aria-hidden="true"></span>
          <span class="sponsor-name">Your category here<span>Reach practitioners while they learn</span></span></li>
      </ul>
      <a class="cta ghost" href="#pl-t" data-route="sponsor">Sponsor a Concept Brief</a>
    </div>
    <div class="brandbar">
      <div class="brandmark">
        <span class="sq" aria-hidden="true"></span>
        <span class="nm">APAS<span class="dot">.</span>ai<span class="sub">One Water Operating System</span></span>
      </div>
      <p class="taught">Independent water sector education</p>
    </div>
    <div class="legal">
      <p>&copy; 2026 APAS.ai. Reproduce for non commercial education with attribution and without
        alteration. Cited federal material is a work of the United States Government and carries no
        copyright in the United States.</p>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <p class="disclaim">This brief explains the concept. Plant decisions still require your approved
      procedures and qualified judgment.</p>
  </div>
</footer>

<div class="backdrop" id="backdrop" hidden></div>

<aside class="drawer" id="graphDrawer" role="dialog" aria-modal="true" aria-labelledby="gd-t" hidden>
  <button type="button" class="drawer-close" data-close aria-label="Close">&times;</button>
  <div class="drawer-in">
    <p class="dk">Concept map</p>
    <h2 id="gd-t">Where this sits</h2>
    <p>Concept Briefs are nodes. These are the ones this brief touches.</p>
    <h3>This brief</h3><span class="node self">Starts It, Grows It</span>
    <h3>Prerequisite for</h3>
    <span class="node">Filtration and What It Inherits</span>
    <span class="node">Residuals: What Removal Costs</span>
    <h3>Adjacent</h3>
    <span class="node">The Sample Is a Choice</span>
    <span class="node">A Non Detect Is Not a Zero</span>
    <span class="node">Compliant Is Not Safe</span>
    <h3>Repairs</h3>
    <p>That performance improves in one direction, and that poor floc is a dosing instruction.</p>
    <a class="cta" href="#" data-route="graph">Open the full OWOS Graph</a>
  </div>
</aside>

<aside class="drawer" id="commDrawer" role="dialog" aria-modal="true" aria-labelledby="cd-t" hidden>
  <button type="button" class="drawer-close" data-close aria-label="Close">&times;</button>
  <div class="drawer-in">
    <p class="dk">Practitioner conversation</p>
    <h2 id="cd-t">Ask the people who run the basin</h2>
    <p>Discussion here is practitioner conversation, not verified instruction, and it is labelled
      that way wherever it appears.</p>
    <h3>Open with</h3>
    <ul><li>How did you find your window?</li><li>What finally told you it was mechanical?</li>
      <li>Do you jar below your setpoint?</li></ul>
    <h3>Found an error?</h3>
    <p>Name the sentence, give the source that contradicts it, and it becomes a tracked proposal that
      re-enters source and qualified review. The outcome publishes either way.</p>
    <a class="cta" href="#" data-route="community">Open the community</a>
    <p style="margin-top:16px;font-size:13px;color:#6b665c">Moderation, verified answers, and
      analytics are shared across every OWOS brief. Nothing facility specific should be posted.</p>
  </div>
</aside>
"""

html = ("<!doctype html>\n<html lang=\"en-US\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "<title>Coagulation and Flocculation | OWOS Concept Brief</title>\n"
        "<meta name=\"description\" content=\"The floc looked wrong, so they added more coagulant, "
        "and the water got worse. Why the cheapest lever is so often the wrong one.\">\n"
        + style + "\n</head>\n<body>\n" + body + "\n" + PLANE
        + "\n<script>\n" + logic + "\n</script>\n</body>\n</html>\n")
(here / "index.html").write_text(html)
print("index.html", len(html), "bytes")
