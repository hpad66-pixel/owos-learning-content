#!/usr/bin/env python3
"""Generate the publishable build from index.html.

The artifact host supplies its own document skeleton, so it is stripped here.
Platform routes resolve inside OWOS and would 404 standalone, so the published
build says so rather than shipping dead links.
"""
import pathlib, re
here = pathlib.Path(__file__).parent
src = (here / "index.html").read_text()
title = re.search(r"<title>(.*?)</title>", src, re.S).group(1).strip()
style = re.search(r"<style>.*?</style>", src, re.S).group(0)
body = re.search(r"<body>(.*?)</body>", src, re.S).group(1).strip()
body = re.sub(r'href="/community[^"]*"', 'href="#pl-t"', body)
body = body.replace(
    '<p class="taught">Independent water sector education</p>',
    '<p class="taught">Independent water sector education</p>\n'
    '      <p class="taught" style="flex:1 1 100%;font-size:13px;color:#6b665c">'
    'Community, Graph, and sponsorship links resolve inside the OWOS platform '
    'and are inert in this published preview.</p>')
out = f"<title>{title}</title>\n{style}\n{body}"
for bad in ("<!doctype", "<html", "<body", "<head>"):
    assert bad not in out.lower(), f"skeleton tag leaked: {bad}"
(here / "artifact.html").write_text(out)
print(f"artifact.html {len(out)} bytes")
