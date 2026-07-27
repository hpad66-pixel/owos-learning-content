#!/usr/bin/env python3
"""Produce platform-ready Concept Brief pages for onewater-os-platform/site/.

Takes a self-contained brief page and adapts it to the live site's conventions:
the owos meta block, the graphite body attribute, the community mount anchor,
and platform routes for Community and Graph in place of the placeholder links.
"""
import hashlib, pathlib, re, sys, urllib.parse, yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]

BRIEFS = {
    "coagulation-vs-flocculation": {
        "src": "concept-briefs/coagulation-vs-flocculation/rebuild/index.html",
        "pkg": "concept-briefs/coagulation-vs-flocculation",
        "id": "owos:concept-brief:001",
        "number": "01",
        "title": "Coagulation and Flocculation",
        "edition": "REBUILD 1.0",
        "space": "owos-community:concept-brief:001",
        "topics": ["coagulation", "flocculation", "jar-testing", "treatment-diagnosis"],
        "summary": "One starts the floc, the other grows it, and the wrong one gets blamed. "
                   "Why adding coagulant is the usual answer and often the wrong lever.",
    },
    "detention-retention-and-infiltration": {
        "src": "concept-briefs/detention-retention-and-infiltration/variant-b/index.html",
        "pkg": "concept-briefs/detention-retention-and-infiltration",
        "id": "owos:concept-brief:003",
        "number": "03",
        "title": "Detention, Retention, and Infiltration",
        "edition": "EDITION B.3.0",
        "space": "owos-community:concept-brief:003",
        "topics": ["detention", "retention", "infiltration", "stormwater", "inflow-and-infiltration"],
        "summary": "A pond in good condition, a clear outlet, a passed inspection, and a street that "
                   "flooded anyway. A name tells you a category; only the route tells you behaviour.",
    },
}


def package_checksum(pkg_dir: pathlib.Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(pkg_dir.rglob("*")):
        if path.is_file() and "dist" not in path.parts and "rebuild" not in path.parts \
           and "variant-b" not in path.parts and "qa-qc" not in path.parts:
            digest.update(path.relative_to(pkg_dir).as_posix().encode())
            digest.update(path.read_bytes())
    return digest.hexdigest()


def community_url(slug: str, meta: dict) -> str:
    q = urllib.parse.urlencode({
        "course": slug,
        "lesson": meta["id"],
        "label": meta["title"],
        "topics": ",".join(meta["topics"]),
        "space": meta["space"],
        "version": meta["edition"].lower().replace(" ", "-"),
    })
    return "course-community.html?" + q


def build(slug: str, meta: dict) -> tuple[pathlib.Path, str, str]:
    src = (ROOT / meta["src"]).read_text()
    pkg_sum = package_checksum(ROOT / meta["pkg"])
    comm = community_url(slug, meta)
    graph = f"/os?node={slug}"

    head_meta = (
        '<meta name="owos-contract" content="owos-concept-brief/2">\n'
        f'<meta name="owos-brief-id" content="{meta["id"]}">\n'
        f'<meta name="owos-brief-version" content="{meta["edition"]}">\n'
        f'<meta name="owos-package-checksum" content="{pkg_sum}">\n'
        '<meta name="owos-release-state" content="public-review-preview">\n'
        '<meta name="owos-evidence-cutoff" content="2026-07-27">\n'
    )
    out = src.replace('<meta name="viewport"', head_meta + '<meta name="viewport"', 1)
    out = out.replace("<body>", '<body data-owos-theme="graphite">', 1)

    # Platform routes in place of the placeholder links.
    # The community page ignores an intent parameter, so both calls to action go
    # to the same working space rather than shipping a link that promises a route
    # the platform does not have.
    out = re.sub(r'href="/community\?brief=[^"]*intent=correction"', f'href="{comm}"', out)
    out = re.sub(r'href="/community\?brief=[^"]*"', f'href="{comm}"', out)
    out = re.sub(r'href="#" data-route="community"', f'href="{comm}" data-route="community"', out)
    out = re.sub(r'href="#" data-route="graph"', f'href="{graph}" data-route="graph"', out)
    out = re.sub(r'href="#pl-t" data-route="sponsor"', 'href="/sponsor.html" data-route="sponsor"', out)

    # The platform deep-links to this mount, so it has to exist by that id.
    out = out.replace('<section class="plane" aria-labelledby="pl-t">',
                      '<section class="plane" id="owos-concept-community" aria-labelledby="pl-t">', 1)

    # Runtime hooks. Seed prompts become buttons the runtime can wire to the
    # feedback field, and the feedback form, testimonials, and completion marker
    # are added because the injected runtime looks for them by selector.
    out = re.sub(r'<span class="seed">([^<]*)</span>',
                 r'<button type="button" class="seed seed-question">\1</button>', out)
    out = out.replace('</div>\n    </div>\n\n    <div class="value">',
                      '</div>\n' + FEEDBACK_BLOCK + '    </div>\n\n    <div class="value">', 1)
    if "data-concept-feedback" not in out:  # layout differs, append into the grid
        out = out.replace('<div class="value">', FEEDBACK_BLOCK + '\n    <div class="value">', 1)
    out = out.replace('<div class="legal">', TESTIMONIALS + '\n    <div class="legal">', 1)
    out = out.replace('<section class="recap"',
                      '<section class="recap" id="owos-concept-finish"', 1)
    out = out.replace('</style>', RUNTIME_CSS + '</style>', 1)

    # The injected runtime reads topics and the graph node from the page instead
    # of its own literals once the platform patch below lands.
    out = out.replace('<meta name="owos-contract"',
        f'<meta name="owos-brief-topics" content="{",".join(meta["topics"])}">\n'
        f'<meta name="owos-brief-slug" content="{slug}">\n<meta name="owos-contract"', 1)

    for hook in ("owos-concept-finish", "data-concept-feedback", "data-concept-testimonials",
                 "seed-question", "data-testimonial-consent"):
        assert hook in out, f"runtime hook missing: {hook}"

    assert "/community?brief=" not in out, "placeholder community link survived"
    assert 'data-route="graph"' not in out or graph in out, "graph route not wired"
    dest = ROOT / f".platform-build/concept-brief-{slug}.html"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(out)
    return dest, hashlib.sha256(out.encode()).hexdigest(), pkg_sum




# ---- runtime hook block -------------------------------------------------
# The platform injects concept-brief-runtime.js and expects these hooks. Without
# them the community drawer, feedback form, testimonials, and completion metric
# do nothing.
FEEDBACK_BLOCK = """
      <div class="comm-card" data-concept-feedback-card>
        <h3>Comment on this brief</h3>
        <p>Goes to the OWOS Community and into the Concept Brief review queue. Sign in is required
          to post.</p>
        <form data-concept-feedback>
          <label class="cf-label" for="cf-kind">What kind of comment is this?</label>
          <select id="cf-kind" name="kind">
            <option value="question">A question</option>
            <option value="technical-feedback">Technical feedback</option>
            <option value="source-suggestion">A better source</option>
            <option value="field-note">A field observation</option>
            <option value="appreciation">What worked for me</option>
          </select>
          <label class="cf-label" for="cf-body">Your comment</label>
          <textarea id="cf-body" name="body" rows="4"
            placeholder="Name the exact sentence or graphic if you are proposing a correction."></textarea>
          <label class="cf-consent" data-testimonial-consent-row hidden>
            <input type="checkbox" data-testimonial-consent>
            <span>You may publish this comment with my name, role, and organisation. A steward must
              approve it first, and I can ask for it to be removed.</span>
          </label>
          <button class="cta" type="submit">Post comment</button>
          <p class="cf-status" data-concept-feedback-status role="status" aria-live="polite"></p>
        </form>
      </div>
"""

TESTIMONIALS = """
    <section data-concept-testimonials hidden aria-label="Reader voices">
      <h3 class="rv-head">What readers said</h3>
      <p class="rv-note">Learner experience, published with consent and steward approval. Not
        technical evidence and not a vendor endorsement.</p>
      <div data-concept-testimonial-list></div>
    </section>
"""

RUNTIME_CSS = """
.cf-label{display:block;margin:14px 0 6px;font:700 11px/1 var(--mono);letter-spacing:.1em;
  text-transform:uppercase;color:#5c574e}
[data-concept-feedback] select,[data-concept-feedback] textarea{width:100%;padding:11px 12px;
  border:1px solid #c9c3b8;border-radius:3px;background:#fff;color:#211f1b;font:15px/1.5 var(--sans);
  min-height:44px;color-scheme:light}
[data-concept-feedback] textarea{min-height:104px;resize:vertical}
.cf-consent{display:flex;gap:10px;align-items:flex-start;margin:14px 0 4px;font-size:13.5px;
  color:#3d3a34}
.cf-consent input{width:24px;height:24px;min-width:24px;accent-color:#1d5c90;margin:1px 0 0}
.cf-status{margin:12px 0 0;font:600 13px/1.5 var(--mono);color:#5c574e;min-height:1.2em}
.rv-head{margin:34px 0 6px;font-size:19px;color:#151412}
.rv-note{margin:0 0 16px;font-size:13.5px;color:#5c574e}
.reader-voice{margin:0 0 14px;padding:18px 20px;background:#f0ede6;border-left:3px solid #1d5c90}
.reader-voice blockquote{margin:0 0 8px;font-size:15.5px;color:#211f1b}
.reader-voice figcaption{font:600 12.5px/1.4 var(--mono);color:#5c574e}
"""

if __name__ == "__main__":
    for slug, meta in BRIEFS.items():
        dest, html_sum, pkg_sum = build(slug, meta)
        print(f"{dest.name}\n  html {html_sum[:16]}...  package {pkg_sum[:16]}...")
