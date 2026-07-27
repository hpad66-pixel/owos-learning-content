#!/usr/bin/env python3
"""Build the archetype comparison page: state-switcher against Diagnose."""
import pathlib, re
here = pathlib.Path(__file__).parent
root = here.parents[2]
shell = (root / "concept-briefs/detention-retention-and-infiltration/variant-b/index.html").read_text()
style = re.search(r"<style>.*?</style>", shell, re.S).group(0)
page = (here / "index.html").read_text()

# lift the existing pin floc section verbatim so the comparison is honest
m = re.search(r'<!-- INTERACTIVE 2: PIN FLOC -->(.*?)</section>', page, re.S)
pinfloc = m.group(1) + "</section>"

logic = (here / "logic.js").read_text()
lines = logic.split("\n")
a = next(i for i,l in enumerate(lines) if "interactive 2: pin floc" in l)
b = next(i for i,l in enumerate(lines) if "flip cards" in l and i > a)
pin_js = "\n".join(lines[a+1:b])
dx_js = (here / "archetype-diagnose.js").read_text()

EXTRA = """
.cmp{padding:64px 0;border-bottom:1px solid var(--line)}
.cmp-a{background:var(--charcoal)} .cmp-b{background:var(--deep)}
.cmp-tag{display:inline-block;margin-bottom:16px;padding:7px 14px;border-radius:100px;
  font:700 11px/1 var(--mono);letter-spacing:.14em}
.tag-a{border:1px solid var(--muted);color:var(--muted)}
.tag-b{border:1px solid var(--water);color:var(--water)}
#dx{margin-top:26px}
.dx-head{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;
  padding-bottom:14px;border-bottom:1px solid var(--line)}
.dx-case,.dx-cost{font:700 11px/1 var(--mono);letter-spacing:.13em;color:var(--muted)}
.dx-cost b{color:var(--amber);font-size:14px}
.dx-symptom{margin:18px 0 0;font-size:17px;color:var(--white);max-width:66ch}
.dx-block{margin-top:28px}
.dx-block h4{margin:0 0 14px;font:700 12px/1.4 var(--mono);letter-spacing:.1em;
  text-transform:uppercase;color:var(--water)}
.dx-ev{display:flex;flex-wrap:wrap;gap:10px}
.dx-btn{position:relative;font:600 14px/1.3 var(--sans);padding:13px 16px;min-height:46px;
  background:var(--panel);color:var(--white);border:1px solid #4a4741;border-radius:3px;
  cursor:pointer;text-align:left}
.dx-btn:hover:not(:disabled){border-color:var(--water);color:var(--water)}
.dx-btn:disabled{opacity:.45;cursor:default}
.dx-btn.got{border-color:var(--muted);opacity:.6}
.dx-btn.chosen{background:var(--water-deep);border-color:var(--water);color:#fff;opacity:1}
.dx-btn.primary{background:var(--water-deep);border-color:var(--water)}
.dx-tag{display:block;margin-top:5px;font:600 10px/1 var(--mono);letter-spacing:.1em;color:var(--muted)}
.dx-btn.chosen .dx-tag{color:#cdeaf8}
.dx-results{margin-top:16px;padding:18px 20px;background:var(--panel);border-left:3px solid var(--muted)}
.dx-results p{margin:0 0 9px;font-size:15px}
.dx-results p:last-child{margin:0}
.dx-out{display:flex;flex-wrap:wrap;gap:22px;align-items:flex-start;margin-top:28px;padding:24px;
  border-left:4px solid var(--muted);background:var(--panel)}
.dx-out.better{border-left-color:var(--green)} .dx-out.worse{border-left-color:var(--red)}
.dx-out-txt{flex:1 1 320px;min-width:0}
.dx-out p{margin:0 0 10px;font-size:15.5px}
.dx-verdict{display:inline-block;margin-bottom:12px;padding:7px 13px;border-radius:100px;
  font:700 11px/1 var(--mono);letter-spacing:.12em}
.dx-verdict.ok{background:rgba(127,176,105,.16);color:var(--green);border:1px solid var(--green)}
.dx-verdict.no{background:rgba(224,122,99,.16);color:var(--red);border:1px solid var(--red)}
.dx-recon p{margin:0 0 11px;padding:11px 14px;font-size:14.5px;border-left:3px solid var(--muted);
  background:rgba(242,241,236,.03)}
.dx-recon .good{border-left-color:var(--green)}
.dx-recon .waste{border-left-color:var(--amber)}
.dx-recon .missed{border-left-color:var(--red)}
.dx-next{display:flex;gap:10px;margin-top:24px;flex-wrap:wrap}
@media (max-width:640px){.dx-btn{flex:1 1 100%}}
"""
style = style.replace("</style>", EXTRA + "</style>")

html = f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Archetype comparison: state switcher against Diagnose</title>
<meta name="description" content="The same evidence and the same claims, taught two ways. One lets you select a state. The other makes you commit before you know.">
{style}
</head>
<body>

<header>
  <div class="wrap">
    <span class="variant-flag">OWOS ARCHETYPE STUDY &middot; NOT A BRIEF</span>
    <h1>Same evidence.<br>Two mechanics.</h1>
    <p class="lede">Identical claims, identical sources, identical certificate. The only thing that
      changes is what the learner is asked to do.</p>
  </div>
</header>

<section class="cmp cmp-a" aria-labelledby="a-t">
  <div class="wrap">
    <span class="cmp-tag tag-a">A &middot; WHAT WE BUILD NOW</span>
    <h2 id="a-t">State switcher</h2>
    <div class="prose">
      <p>Pick a cause. A diagram changes. A paragraph appears. This is the mechanic in both briefs
        shipped so far, and it is the one under review.</p>
      <p><b>The learner selects from states somebody else already decided, and cannot be wrong.</b></p>
    </div>
    {pinfloc}
  </div>
</section>

<section class="cmp cmp-b" aria-labelledby="b-t">
  <div class="wrap">
    <span class="cmp-tag tag-b">B &middot; THE DIAGNOSE ARCHETYPE</span>
    <h2 id="b-t">Commit before you know</h2>
    <div class="prose">
      <p>Same three causes. Same evidence. But the cause is hidden, evidence costs shifts, you commit
        to a diagnosis before anyone tells you, and then you act and live with it.</p>
      <p><b>Add coagulant to an overdose and the water gets worse.</b> Then you find out what the
        evidence was worth, including what you paid for that told you nothing and what you skipped
        that would have settled it.</p>
      <p>Three cases. The cause differs each time.</p>
    </div>
    <div id="dx"></div>
  </div>
</section>

<section class="cmp" aria-labelledby="c-t">
  <div class="wrap">
    <span class="cmp-tag tag-b">WHAT CHANGED</span>
    <h2 id="c-t">Nothing about the evidence. Everything about the learner.</h2>
    <div class="split">
      <div class="split-card"><span class="tagline">Unchanged</span>
        <h3>The governed layer</h3>
        <p>Same claims, same federal sources, same boundary statements, same certificate. Both
          mechanics teach that pin floc has three causes and two of them worsen with coagulant.</p>
        <p>The trust shell does not move. That is deliberate: a learner should find the sources and
          the boundary in the same place in every brief.</p></div>
      <div class="split-card wrong"><span class="tagline">Changed</span>
        <h3>What the learner does</h3>
        <p>A reads about being wrong. B is wrong, pays a shift for it, and has to recover.</p>
        <p>A can be completed by clicking three buttons in order. B cannot be completed without
          committing to a judgment under uncertainty, which is the actual skill.</p></div>
    </div>
    <div class="prose" style="margin-top:28px">
      <p><b style="color:var(--white)">The cost of B is real and worth naming.</b> It takes longer to
        author, it needs a truth model per case rather than a paragraph per state, and it can only be
        built where the topic genuinely has a hidden cause and competing evidence. Forcing it onto a
        topic that is a straight trace would be the same mistake in the other direction.</p>
      <p>That is the argument for archetypes chosen by cognitive task rather than one template or
        five skins: <b>Trace</b> for following something through a system, <b>Diagnose</b> for one
        symptom with competing causes, <b>Judge a number</b> for what a measurement establishes,
        <b>Trade off</b> for when both options cost something, <b>Sequence</b> for when order is the
        lesson.</p>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <p class="disclaim">Archetype study for design review. Not a Concept Brief, not released, and
      carries no certificate of its own. The claims and sources are those of
      <code>owos:concept-brief:001</code>.</p>
  </div>
</footer>

<script>
window.OWOS = window.OWOS || {{}};
window.OWOS.track = window.OWOS.track || function(){{}};
(function(){{
  "use strict";
  var G = {{ deep:"#141311", w:"#7dc6e8", wd:"#2b7399", am:"#e0a64a", rd:"#e07a63",
             gn:"#7fb069", mu:"#a29c91", wh:"#f2f1ec" }};
  {pin_js}
}})();
</script>
<script>
{dx_js}
</script>
</body>
</html>
"""
(here / "archetype-comparison.html").write_text(html)
print("archetype-comparison.html", len(html), "bytes")
