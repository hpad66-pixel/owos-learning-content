#!/usr/bin/env python3
"""
Build a self-contained module page for deployment.

Takes a curriculum module that links ../../../core/components/academy.css and
academy.js, and produces ONE HTML file with the library inlined, so it renders
identically anywhere (owos.ai / 2-brain, an external LMS, an artifact) with no
path or shell-cascade surprises.

Usage:
  python3 tools/build-selfcontained.py SOURCE.html OUTPUT.html
It also rewrites in-course nav links to their deployed 2-brain filenames.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CSS  = (ROOT / "core/components/academy.css").read_text(encoding="utf-8")
JS   = (ROOT / "core/components/academy.js").read_text(encoding="utf-8")

# When inlined, any literal </script> (even inside a JS comment or string) would
# close the inline <script> early. Escape it so the HTML parser keeps reading.
JS  = re.sub(r'</(script)', r'<\\/\1', JS, flags=re.I)
CSS = re.sub(r'</(style)',  r'<\\/\1', CSS, flags=re.I)

# curriculum filename -> deployed 2-brain filename
LINK_MAP = {
    "masterclass-project-management.html": "course-project-management.html",
    "module-01-what-is-a-project.html":    "lesson-pm-01-what-is-a-project.html",
    "module-02-delivery-and-life-cycles.html": "lesson-pm-02-delivery-life-cycles.html",
    "module-03-governance-integration-tailoring.html": "lesson-pm-03-governance-integration-tailoring.html",
    "module-04-scope-and-requirements.html": "lesson-pm-04-scope-and-requirements.html",
    "module-05-scheduling-critical-path.html": "lesson-pm-05-scheduling-critical-path.html",
}

def build(src_path, out_path):
    html = pathlib.Path(src_path).read_text(encoding="utf-8")

    # inline the stylesheet
    html = re.sub(
        r'<link rel="stylesheet" href="[^"]*academy\.css">',
        "<style>\n" + CSS + "\n</style>",
        html,
    )
    # inline the script
    html = re.sub(
        r'<script src="[^"]*academy\.js"></script>',
        "<script>\n" + JS + "\n</script>",
        html,
    )
    # rewrite nav links to deployed names
    for a, b in LINK_MAP.items():
        html = html.replace('href="' + a + '"', 'href="' + b + '"')

    # writing standard: no em/en dashes may reach a built page
    assert "—" not in html, "em dash found in built page"
    assert "–" not in html, "en dash found in built page"
    # library must actually be inlined, not left as external references
    assert not re.search(r'<link[^>]*academy\.css', html), "academy.css still linked"
    assert not re.search(r'<script src="[^"]*academy\.js"', html), "academy.js still linked"

    pathlib.Path(out_path).write_text(html, encoding="utf-8")
    print("built", out_path, "(%d KB)" % (len(html.encode("utf-8")) // 1024))

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
