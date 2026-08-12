#!/usr/bin/env node
/**
 * Rendered-quality audit for compiled OWOS Concept Briefs.
 *
 * The package validator checks structure. It cannot see the page. This audit
 * opens the compiled HTML at desktop, tablet, and phone and fails on the
 * defects that structure checks miss:
 *
 *   contrast  WCAG 2.1 contrast ratio below 4.5:1 for normal text or 3:1 for
 *             large text, measured against the real composited background
 *             rather than the nearest declared colour.
 *   gutter    text sitting closer to the viewport edge than the page's own
 *             content inset, which is how a band, header, or full-bleed panel
 *             ends up flush against the screen.
 *   layout    a container whose content is far larger than the box holding it,
 *             or a positioned/3D box that computes to display:inline where its
 *             width, height, and transform-style are silently ignored. This is
 *             how a card built from inline elements collapses: the text stays
 *             on screen and legible, so contrast and overflow both pass while
 *             the component is visually destroyed.
 *   overflow  horizontal document overflow at any width.
 *   tap       interactive controls below the 24px minimum on touch widths.
 *
 * Usage:
 *   node tools/audit-concept-brief-rendering.cjs <compiled.html> [more.html ...]
 *   node tools/audit-concept-brief-rendering.cjs --json <compiled.html>
 */

const path = require('path');
const { chromium } = require('playwright');

const VIEWPORTS = [
  { name: 'desktop', width: 1440, height: 900 },
  { name: 'tablet', width: 820, height: 1180 },
  { name: 'phone', width: 390, height: 844 },
];

// Minimum distance from the viewport edge to the start of readable text.
// Below these the page reads as broken even though nothing overflows.
const MIN_GUTTER = { desktop: 24, tablet: 20, phone: 12 };

const AUDIT = () => {
  const parseColor = (value) => {
    if (!value) return null;
    const parts = value.match(/[\d.]+/g);
    if (!parts) return null;
    const [r, g, b] = parts.map(Number);
    const a = parts.length > 3 ? Number(parts[3]) : 1;
    if ([r, g, b].some((n) => Number.isNaN(n))) return null;
    return { r, g, b, a };
  };

  const over = (fg, bg) => ({
    r: fg.r * fg.a + bg.r * (1 - fg.a),
    g: fg.g * fg.a + bg.g * (1 - fg.a),
    b: fg.b * fg.a + bg.b * (1 - fg.a),
    a: 1,
  });

  // Composite every translucent ancestor background down to an opaque colour.
  const effectiveBackground = (el) => {
    const stack = [];
    let node = el;
    while (node && node.nodeType === 1) {
      const style = getComputedStyle(node);
      const colour = parseColor(style.backgroundColor);
      if (colour && colour.a > 0) {
        stack.push(colour);
        if (colour.a >= 1) break;
      }
      if (style.backgroundImage && style.backgroundImage !== 'none') {
        // A gradient or image can carry the contrast. Treat it as unknown and
        // stop, rather than reporting a false positive against what is behind it.
        return { unknown: true, colour: { r: 255, g: 255, b: 255, a: 1 } };
      }
      node = node.parentElement;
    }
    let base = { r: 255, g: 255, b: 255, a: 1 };
    for (let i = stack.length - 1; i >= 0; i -= 1) base = over(stack[i], base);
    return { unknown: false, colour: base };
  };

  const channel = (c) => {
    const s = c / 255;
    return s <= 0.03928 ? s / 12.92 : ((s + 0.055) / 1.055) ** 2.4;
  };
  const luminance = (c) =>
    0.2126 * channel(c.r) + 0.7152 * channel(c.g) + 0.0722 * channel(c.b);
  const ratio = (a, b) => {
    const la = luminance(a);
    const lb = luminance(b);
    return (Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05);
  };

  const label = (el) => {
    const cls = (el.className || '').toString().trim().split(/\s+/).slice(0, 3).join('.');
    return `${el.tagName.toLowerCase()}${cls ? '.' + cls : ''}`;
  };

  const ownText = (el) => {
    let out = '';
    for (const node of el.childNodes) {
      if (node.nodeType === 3) out += node.textContent;
    }
    return out.trim();
  };

  const visible = (el) => {
    const s = getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden') return false;
    if (Number(s.opacity) === 0) return false;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) return false;
    // Skip anything inside a closed drawer or dialog.
    if (el.closest('[hidden]')) return false;
    return true;
  };

  // A wide table or diagram that scrolls inside its own wrapper is correct.
  const inScrollContainer = (el) => {
    let node = el.parentElement;
    while (node && node !== document.body) {
      const ox = getComputedStyle(node).overflowX;
      if (ox === 'auto' || ox === 'scroll') return true;
      node = node.parentElement;
    }
    return false;
  };

  const contrast = [];
  const gutter = [];
  const tap = [];
  const layout = [];

  // Content taller than the box that holds it, with nothing to clip or scroll
  // it. A box whose height is free grows to fit its text, so this only happens
  // when the height was constrained or the container collapsed. It is how a
  // card built out of inline elements silently loses its layout: the text is
  // still on screen and still legible, so contrast and overflow checks pass
  // while the component is visually destroyed.
  // Threshold is a ratio, not a few pixels. Line-height, descenders, and a child
  // with a negative margin all paint slightly outside their box without anything
  // being wrong, and overflow:visible means nothing is actually clipped. A
  // genuinely collapsed container is not marginal: the flip card that prompted
  // this check held 281px of content in a 44px box, six times over.
  const spilling = (el) => {
    const s = getComputedStyle(el);
    if (s.overflowY !== 'visible' || s.display === 'inline') return false;
    if (s.position === 'absolute' && el.offsetParent === null) return false;
    if (el.clientHeight <= 0) return false;
    return (
      el.scrollHeight > el.clientHeight * 1.5 &&
      el.scrollHeight - el.clientHeight > 24
    );
  };

  // width, height, min-height and transform-style do nothing on an inline box.
  // Authoring a card, panel, or stage as a <span> is the usual cause.
  const inlineButSized = (el) => {
    const s = getComputedStyle(el);
    if (s.display !== 'inline') return false;
    if (s.position === 'relative' || s.position === 'absolute') return true;
    return s.transformStyle === 'preserve-3d' || s.perspective !== 'none';
  };

  // Establish the page's own content inset from its dominant wrapper.
  const wraps = [...document.querySelectorAll('.wrap')]
    .filter(visible)
    .map((w) => Math.round(w.getBoundingClientRect().left))
    .sort((a, b) => a - b);
  const pageInset = wraps.length ? wraps[Math.floor(wraps.length / 2)] : 0;

  for (const el of document.querySelectorAll('body *')) {
    if (!visible(el)) continue;
    const text = ownText(el);
    if (!text) continue;

    const style = getComputedStyle(el);
    const rect = el.getBoundingClientRect();

    // ---- contrast
    const fgRaw = parseColor(style.color);
    const bg = effectiveBackground(el);
    if (fgRaw && !bg.unknown) {
      const fg = fgRaw.a < 1 ? over(fgRaw, bg.colour) : fgRaw;
      const size = parseFloat(style.fontSize);
      const weight = Number(style.fontWeight) || 400;
      const large = size >= 24 || (size >= 18.66 && weight >= 700);
      const need = large ? 3 : 4.5;
      const got = ratio(fg, bg.colour);
      if (got < need) {
        contrast.push({
          el: label(el),
          text: text.slice(0, 60),
          fg: style.color,
          bg: `rgb(${Math.round(bg.colour.r)}, ${Math.round(bg.colour.g)}, ${Math.round(bg.colour.b)})`,
          ratio: Number(got.toFixed(2)),
          need,
          fontSize: size,
        });
      }
    }

    // ---- gutter
    // Measure where the text actually starts, not where the box does. A
    // full-bleed bar is fine as long as its padding holds the text off the edge.
    const padL = parseFloat(style.paddingLeft) || 0;
    const padR = parseFloat(style.paddingRight) || 0;
    const bordL = parseFloat(style.borderLeftWidth) || 0;
    const bordR = parseFloat(style.borderRightWidth) || 0;
    const textLeft = rect.left + padL + bordL;
    const textRight = rect.right - padR - bordR;
    if (textLeft < pageInset - 2 && rect.width > 40) {
      gutter.push({
        el: label(el),
        text: text.slice(0, 60),
        left: Math.round(textLeft),
        expected: pageInset,
      });
    }
    if (textRight > window.innerWidth + 2) {
      gutter.push({
        el: label(el),
        text: text.slice(0, 60),
        right: Math.round(textRight),
        expected: window.innerWidth,
        overflowRight: true,
      });
    }
    // Separately from where the text sits, the box itself must stay on screen.
    // A full-bleed panel using a negative inline margin can escape the viewport
    // without its text ever crossing the gutter. Content inside a horizontal
    // scroll container is exempt: a wide table scrolling inside its own wrapper
    // is the correct pattern, not an overflow defect.
    if (!inScrollContainer(el) && (rect.left < -1 || rect.right > window.innerWidth + 1)) {
      gutter.push({
        el: label(el),
        text: text.slice(0, 60),
        left: Math.round(rect.left),
        right: Math.round(rect.right),
        expected: window.innerWidth,
        boxEscapesViewport: true,
      });
    }
  }

  // Layout integrity gets its own pass. It cannot reuse `visible`, because that
  // rejects zero-height elements and a collapsed container is exactly the thing
  // being looked for. It also cannot require own text, since the container that
  // collapsed usually holds only other elements.
  for (const el of document.querySelectorAll('body *')) {
    // SVG uses a different box model; clientHeight there is not comparable.
    if (el.namespaceURI !== 'http://www.w3.org/1999/xhtml') continue;
    const s = getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden') continue;
    if (Number(s.opacity) === 0) continue;
    if (el.closest('[hidden]')) continue;
    const sample = (el.textContent || '').trim().slice(0, 60);
    if (spilling(el)) {
      layout.push({
        el: label(el), kind: 'content-spills-its-box', text: sample,
        boxH: el.clientHeight, contentH: el.scrollHeight,
      });
    }
    if (inlineButSized(el)) {
      layout.push({
        el: label(el), kind: 'positioned-or-3d-box-computes-inline', text: sample,
        boxH: Math.round(el.getBoundingClientRect().height), contentH: 0,
      });
    }
  }

  for (const el of document.querySelectorAll('a, button, input, select, textarea, [role="button"]')) {
    if (!visible(el)) continue;
    const r = el.getBoundingClientRect();
    if (r.height < 24 || r.width < 24) {
      tap.push({ el: label(el), w: Math.round(r.width), h: Math.round(r.height) });
    }
  }

  const dedupe = (rows, key) => {
    const seen = new Set();
    return rows.filter((row) => {
      const k = key(row);
      if (seen.has(k)) return false;
      seen.add(k);
      return true;
    });
  };

  return {
    pageInset,
    horizontalOverflow: Math.max(
      0,
      document.documentElement.scrollWidth - window.innerWidth,
    ),
    contrast: dedupe(contrast, (r) => r.el + r.fg + r.bg),
    gutter: dedupe(
      gutter,
      (r) => r.el + (r.overflowRight ? 'R' : r.boxEscapesViewport ? 'B' : 'L'),
    ),
    layout: dedupe(layout, (r) => r.el + r.kind),
    tap: dedupe(tap, (r) => r.el),
  };
};

async function auditFile(browser, file) {
  const url = 'file://' + path.resolve(file);
  const results = [];
  for (const vp of VIEWPORTS) {
    const page = await browser.newPage({
      viewport: { width: vp.width, height: vp.height },
    });
    await page.goto(url, { waitUntil: 'load' });
    // Let reveal animations settle so nothing is measured mid-transition.
    await page.evaluate(() => {
      document.querySelectorAll('.editorial-reveal').forEach((el) => el.classList.add('visible'));
    });
    await page.waitForTimeout(250);
    const found = await page.evaluate(AUDIT);
    found.viewport = vp.name;
    found.minGutter = MIN_GUTTER[vp.name];
    // A gutter finding only counts if it also breaks the absolute minimum.
    found.gutter = found.gutter.filter(
      (row) =>
        row.overflowRight ||
        row.boxEscapesViewport ||
        row.left < MIN_GUTTER[vp.name],
    );
    if (vp.name === 'desktop') found.tap = [];
    results.push(found);
    await page.close();
  }
  return { file, results };
}

(async () => {
  const args = process.argv.slice(2);
  const asJson = args.includes('--json');
  const files = args.filter((a) => a !== '--json');
  if (!files.length) {
    console.error('usage: audit-concept-brief-rendering.cjs [--json] <compiled.html> ...');
    process.exit(2);
  }

  const browser = await chromium.launch();
  const reports = [];
  for (const file of files) reports.push(await auditFile(browser, file));
  await browser.close();

  if (asJson) {
    console.log(JSON.stringify(reports, null, 2));
  }

  let failures = 0;
  for (const report of reports) {
    if (!asJson) console.log('\n=== ' + path.basename(report.file) + ' ===');
    for (const r of report.results) {
      const count = r.contrast.length + r.gutter.length + r.layout.length + r.tap.length + (r.horizontalOverflow > 0 ? 1 : 0);
      failures += count;
      if (asJson) continue;
      console.log(
        `\n  [${r.viewport}] inset=${r.pageInset}px  contrast=${r.contrast.length}  ` +
          `gutter=${r.gutter.length}  layout=${r.layout.length}  ` +
          `tap=${r.tap.length}  hOverflow=${r.horizontalOverflow}px`,
      );
      for (const c of r.contrast) {
        console.log(
          `    contrast ${c.ratio}:1 (need ${c.need}) ${c.el}  ${c.fg} on ${c.bg}\n` +
            `       "${c.text}"`,
        );
      }
      for (const g of r.gutter) {
        console.log(
          g.boxEscapesViewport
            ? `    box-escapes-viewport ${g.el} left=${g.left} right=${g.right} vw=${g.expected}\n       "${g.text}"`
            : g.overflowRight
              ? `    overflow-right ${g.el} right=${g.right} > ${g.expected}\n       "${g.text}"`
              : `    gutter ${g.el} left=${g.left} (page inset ${g.expected})\n       "${g.text}"`,
        );
      }
      for (const l of r.layout) {
        console.log(
          l.kind === 'content-spills-its-box'
            ? `    layout ${l.kind} ${l.el} box=${l.boxH}px content=${l.contentH}px\n       "${l.text}"`
            : `    layout ${l.kind} ${l.el} height=${l.boxH}px\n       "${l.text}"`,
        );
      }
      for (const t of r.tap) console.log(`    tap-target ${t.el} ${t.w}x${t.h}`);
    }
  }

  if (!asJson) {
    console.log(
      failures === 0
        ? '\nRendered audit passed: no contrast, gutter, layout, overflow, or tap-target defects.'
        : `\nRendered audit found ${failures} defect(s).`,
    );
  }
  process.exit(failures === 0 ? 0 : 1);
})();
