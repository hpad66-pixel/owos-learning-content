#!/usr/bin/env node
/* Build the Version 3 System Bible PDF from its governed Markdown source. */

const fs = require("node:fs");
const path = require("node:path");
const { pathToFileURL } = require("node:url");

async function main() {
  const markedModulePath = require.resolve("marked");
  const { marked } = await import(pathToFileURL(markedModulePath).href);
  const { chromium } = require("playwright");

  const packageDir = path.resolve(__dirname, "..");
  const rootDir = path.resolve(packageDir, "..");
  const markdownPath = path.join(packageDir, "ii-intelligence-system-bible-v3.md");
  const outputDir = path.join(rootDir, "output", "pdf");
  const tempDir = path.join(rootDir, "tmp", "pdfs");
  const htmlPath = path.join(tempDir, "ii-intelligence-system-bible-v3.print.html");
  const pdfPath = path.join(outputDir, "ii-intelligence-system-bible-v3.pdf");
  const mermaidPath = "/private/tmp/owos-v3-pdf-deps/node_modules/mermaid/dist/mermaid.min.js";

  fs.mkdirSync(outputDir, { recursive: true });
  fs.mkdirSync(tempDir, { recursive: true });

  const renderer = {
    code(token) {
      const language = (token.lang || "").trim().toLowerCase();
      const escaped = token.text
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;");
      if (language === "mermaid") {
        return `<figure class="diagram"><div class="mermaid">${escaped}</div></figure>`;
      }
      const className = language ? ` class="language-${language}"` : "";
      return `<pre><code${className}>${escaped}</code></pre>`;
    },
  };

  marked.use({
    renderer,
    gfm: true,
    breaks: false,
  });

  const markdown = fs.readFileSync(markdownPath, "utf8");
  if (!fs.existsSync(mermaidPath)) {
    throw new Error(
      `Local Mermaid dependency not found at ${mermaidPath}. ` +
      "Install it with: npm install --prefix /private/tmp/owos-v3-pdf-deps mermaid@11.16.0"
    );
  }
  const mermaidScript = fs.readFileSync(mermaidPath, "utf8").replaceAll("</script", "<\\/script");
  const body = marked.parse(markdown).replaceAll('src="figures/', 'src="../figures/');
  const baseHref = pathToFileURL(packageDir + path.sep).href;
  const html = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <base href="${baseHref}">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PumpOS and I&amp;I Intelligence System Bible - Version 3</title>
  <script>${mermaidScript}</script>
  <style>
    :root {
      --ink: #182127;
      --muted: #53616a;
      --line: #b8c3c9;
      --paper: #ffffff;
      --panel: #f1f4f5;
      --accent: #007f86;
      --accent-dark: #075d63;
      --warning: #9a5b00;
      --code: #eef2f3;
    }
    * { box-sizing: border-box; }
    html { background: var(--paper); }
    body {
      margin: 0;
      color: var(--ink);
      background: var(--paper);
      font-family: "Avenir Next", "Helvetica Neue", Arial, sans-serif;
      font-size: 9.4pt;
      line-height: 1.46;
      orphans: 3;
      widows: 3;
      print-color-adjust: exact;
      -webkit-print-color-adjust: exact;
    }
    h1, h2, h3, h4, h5, h6 {
      color: var(--ink);
      font-weight: 700;
      line-height: 1.16;
      break-after: avoid-page;
      page-break-after: avoid;
    }
    h1 {
      margin: 0 0 18pt;
      padding: 22pt 0 9pt;
      color: var(--accent-dark);
      font-size: 24pt;
      border-bottom: 2.5pt solid var(--accent);
      break-before: page;
      page-break-before: always;
    }
    body > h1:first-child {
      break-before: auto;
      page-break-before: auto;
      padding-top: 80pt;
      font-size: 30pt;
      border-bottom-width: 4pt;
    }
    h2 {
      margin: 20pt 0 8pt;
      font-size: 16pt;
      color: var(--accent-dark);
    }
    h3 { margin: 15pt 0 6pt; font-size: 12.5pt; }
    h4 { margin: 12pt 0 5pt; font-size: 10.5pt; color: var(--accent-dark); }
    h5, h6 { margin: 10pt 0 4pt; font-size: 9.5pt; }
    p { margin: 0 0 8pt; }
    ul, ol { margin: 0 0 9pt 19pt; padding: 0; }
    li { margin: 0 0 3pt; }
    li > ul, li > ol { margin-top: 3pt; margin-bottom: 3pt; }
    strong { font-weight: 700; }
    a { color: var(--accent-dark); text-decoration: none; }
    blockquote {
      margin: 10pt 0;
      padding: 8pt 11pt;
      color: #2f3d44;
      background: #eef5f5;
      border-left: 4pt solid var(--accent);
      break-inside: avoid-page;
    }
    hr {
      margin: 15pt 0;
      border: 0;
      border-top: 0.75pt solid var(--line);
    }
    table {
      width: 100%;
      margin: 9pt 0 13pt;
      border-collapse: collapse;
      table-layout: auto;
      font-size: 7.3pt;
      line-height: 1.28;
    }
    thead { display: table-header-group; }
    tr { break-inside: avoid-page; page-break-inside: avoid; }
    th, td {
      padding: 4pt 4.5pt;
      text-align: left;
      vertical-align: top;
      overflow-wrap: anywhere;
      border: 0.5pt solid var(--line);
    }
    th {
      color: #ffffff;
      background: var(--accent-dark);
      font-weight: 700;
    }
    tbody tr:nth-child(even) td { background: #f5f7f8; }
    code {
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
      font-size: 0.88em;
      overflow-wrap: anywhere;
    }
    :not(pre) > code {
      padding: 0.7pt 2.2pt;
      background: var(--code);
      border-radius: 2pt;
    }
    pre {
      margin: 8pt 0 12pt;
      padding: 8pt 9pt;
      color: #162026;
      background: var(--code);
      border-left: 3pt solid #8a9ba3;
      border-radius: 2pt;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
      font-size: 6.8pt;
      line-height: 1.27;
      white-space: pre-wrap;
      overflow-wrap: anywhere;
      break-inside: auto;
    }
    img {
      display: block;
      max-width: 100%;
      max-height: 8.35in;
      height: auto;
      margin: 9pt auto 13pt;
      object-fit: contain;
      break-inside: avoid-page;
      page-break-inside: avoid;
    }
    figure.diagram {
      display: block;
      width: 100%;
      margin: 10pt 0 14pt;
      padding: 8pt;
      background: #fbfcfc;
      border: 0.75pt solid var(--line);
      break-inside: avoid-page;
      page-break-inside: avoid;
    }
    .mermaid {
      display: flex;
      justify-content: center;
      width: 100%;
    }
    .mermaid svg {
      display: block;
      max-width: 100% !important;
      max-height: 8.1in;
      height: auto !important;
      margin: 0 auto;
    }
    .mermaid .nodeLabel, .mermaid .edgeLabel {
      font-family: "Avenir Next", "Helvetica Neue", Arial, sans-serif !important;
    }
    .mermaid-error {
      padding: 8pt;
      color: #7b1b1b;
      background: #fff0f0;
      border: 1pt solid #b84040;
      font-family: monospace;
      white-space: pre-wrap;
    }
    @page {
      size: Letter;
      margin: 0.68in 0.62in 0.72in;
    }
    @media print {
      body { background: #ffffff; }
      a { color: var(--accent-dark); }
      h1 + h2, h1 + p { break-before: avoid-page; }
    }
  </style>
</head>
<body>
${body}
<script>
  (async () => {
    try {
      mermaid.initialize({
        startOnLoad: false,
        securityLevel: "loose",
        theme: "base",
        fontFamily: "Avenir Next, Helvetica Neue, Arial, sans-serif",
        themeVariables: {
          primaryColor: "#dceff0",
          primaryTextColor: "#182127",
          primaryBorderColor: "#007f86",
          lineColor: "#53616a",
          secondaryColor: "#eef3f4",
          tertiaryColor: "#ffffff",
          fontSize: "12px"
        },
        flowchart: { htmlLabels: true, curve: "basis", useMaxWidth: true }
      });
      await mermaid.run({ querySelector: ".mermaid" });
      document.body.dataset.mermaid = "complete";
    } catch (error) {
      document.body.dataset.mermaid = "failed";
      const notice = document.createElement("pre");
      notice.className = "mermaid-error";
      notice.textContent = "Mermaid rendering failed: " + String(error);
      document.body.prepend(notice);
    } finally {
      document.body.dataset.rendered = "true";
    }
  })();
</script>
</body>
</html>`;

  fs.writeFileSync(htmlPath, html);

  const browser = await chromium.launch({
    executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    headless: true,
    args: ["--allow-file-access-from-files", "--disable-dev-shm-usage"],
  });
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  await context.route(/^https?:\/\//, (route) => route.abort());
  const page = await context.newPage();
  await page.goto(pathToFileURL(htmlPath).href, {
    waitUntil: "networkidle",
    timeout: 120000,
  });
  await page.waitForSelector('body[data-rendered="true"]', { timeout: 120000 });
  await page.evaluate(async () => {
    await document.fonts.ready;
    for (const image of document.images) {
      if (!image.complete) {
        await new Promise((resolve) => {
          image.addEventListener("load", resolve, { once: true });
          image.addEventListener("error", resolve, { once: true });
        });
      }
    }
  });

  const diagnostics = await page.evaluate(() => ({
    mermaid: document.body.dataset.mermaid,
    diagrams: document.querySelectorAll("figure.diagram").length,
    renderedSvgs: document.querySelectorAll("figure.diagram svg").length,
    images: document.images.length,
    brokenImages: [...document.images].filter((image) => !image.naturalWidth).map((image) => image.src),
  }));
  if (diagnostics.mermaid !== "complete") {
    throw new Error(`Mermaid rendering did not complete: ${JSON.stringify(diagnostics)}`);
  }
  if (diagnostics.diagrams !== diagnostics.renderedSvgs) {
    throw new Error(`Not every Mermaid diagram rendered: ${JSON.stringify(diagnostics)}`);
  }
  if (diagnostics.brokenImages.length) {
    throw new Error(`Broken images found: ${JSON.stringify(diagnostics.brokenImages)}`);
  }

  await page.pdf({
    path: pdfPath,
    format: "Letter",
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: `
      <div style="width:100%;padding:0 0.62in;font-family:Arial,sans-serif;font-size:7px;color:#53616a;">
        PumpOS and I&amp;I Intelligence System Bible - Version 3
      </div>`,
    footerTemplate: `
      <div style="width:100%;padding:0 0.62in;font-family:Arial,sans-serif;font-size:7px;color:#53616a;display:flex;justify-content:space-between;">
        <span>Internal governed candidate - not approved for production use</span>
        <span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
      </div>`,
    margin: { top: "0.68in", right: "0.62in", bottom: "0.72in", left: "0.62in" },
    tagged: true,
    outline: true,
  });

  await browser.close();
  console.log(JSON.stringify({ htmlPath, pdfPath, diagnostics }, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
