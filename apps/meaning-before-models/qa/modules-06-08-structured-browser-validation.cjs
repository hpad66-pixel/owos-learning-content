const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");

const modules = [
  ["06", "module-06-taxonomies-vocabularies-and-rdfs", "lesson-meaning-before-models-06-taxonomies-vocabularies-and-rdfs.html"],
  ["07", "module-07-ontology-engineering-in-plain-language", "lesson-meaning-before-models-07-ontology-engineering-in-plain-language.html"],
  ["08", "module-08-ask-the-graph-with-sparql", "lesson-meaning-before-models-08-ask-the-graph-with-sparql.html"],
];
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const root = path.resolve(__dirname, "..");
const captureRoot = path.join(__dirname, "rendered");
const target = process.env.OWOS_TARGET || "build";

function lessonUrl(slug, distName) {
  if (process.env.OWOS_BASE_URL) return `${process.env.OWOS_BASE_URL.replace(/\/$/, "")}/${distName}?batch=0608`;
  if (target === "dist") return `file://${path.join(root, "dist/site", distName)}`;
  return `file://${path.join(root, "modules", slug, "build/index.html")}`;
}

async function complete(page) {
  for (const group of await page.locator("[data-choice-group]").all()) {
    await group.locator("[data-choice][data-correct=true]").click();
    await group.locator("[data-check-choice]").click();
  }
  for (const group of await page.locator("[data-flip-group]").all()) {
    for (const card of await group.locator("[data-flip-card]").all()) await card.click();
  }
  for (const group of await page.locator("[data-matching]").all()) {
    for (const field of await group.locator("[data-match-answer]").all()) await field.selectOption(await field.getAttribute("data-match-answer"));
    await group.locator("[data-check-matching]").click();
  }
  for (const group of await page.locator("[data-multi-select]").all()) {
    for (const option of await group.locator("[data-multi-option]").all()) if (await option.getAttribute("data-correct") === "true") await option.check();
    await group.locator("[data-check-multi]").click();
  }
  for (const lab of await page.locator("[data-hierarchy-repair]").all()) {
    for (const item of await lab.locator("[data-hierarchy-case]").all()) {
      const answer = await item.getAttribute("data-answer");
      await item.locator(`[data-hierarchy-choice="${answer}"]`).click();
    }
  }
  for (const canvas of await page.locator("[data-ontology-canvas]").all()) {
    for (const field of await canvas.locator("[data-canvas-answer]").all()) await field.selectOption(await field.getAttribute("data-canvas-answer"));
    await canvas.locator("[data-check-canvas]").click();
  }
  for (const lab of await page.locator("[data-sparql-builder]").all()) {
    for (const clause of await lab.locator("[data-query-clause]").all()) await clause.click();
  }
  for (const form of await page.locator("[data-work-product]").all()) {
    let index = 0;
    for (const field of await form.locator("[required]").all()) {
      index += 1;
      await field.fill(`Specific reviewable batch evidence ${index}`);
    }
    await form.locator('button[type="submit"]').click();
  }
}

async function inspect(browser, moduleNumber, slug, distName, mode) {
  const mobile = mode === "phone";
  const tablet = mode === "tablet";
  const context = await browser.newContext({
    viewport: mobile ? {width: 390, height: 844} : tablet ? {width: 820, height: 1080} : {width: 1440, height: 1000},
    reducedMotion: mobile ? "reduce" : "no-preference",
    hasTouch: mobile || tablet,
    isMobile: mobile,
  });
  const page = await context.newPage();
  const errors = [];
  page.on("console", (message) => { if (message.type() === "error") errors.push(message.text()); });
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(lessonUrl(slug, distName), {waitUntil: "load"});
  await page.waitForSelector("main");
  await page.evaluate(async () => Promise.all([...document.images].map((image) => image.complete && image.naturalWidth > 0 ? Promise.resolve() : image.decode())));

  const graph = page.getByRole("button", {name: "Graph"}).first();
  await graph.click();
  const graphOpen = await page.locator('[data-drawer="graph"]').getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  const graphClosed = await page.locator('[data-drawer="graph"]').getAttribute("aria-hidden") === "true";
  const graphFocusReturned = await graph.evaluate((node) => document.activeElement === node);
  await page.getByRole("button", {name: "Glossary", exact: true}).click();
  const glossaryOpen = await page.locator('[data-drawer="glossary"]').getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  await complete(page);

  const state = await page.evaluate(() => ({
    h1Count: document.querySelectorAll("h1").length,
    sectionCount: document.querySelectorAll(".lesson-section").length,
    visualCount: document.querySelectorAll(".learning-visual").length,
    visualTypes: [...document.querySelectorAll(".learning-visual")].map((node) => node.dataset.visualType),
    imagesLoaded: [...document.images].every((image) => image.complete && image.naturalWidth > 0),
    requiredComplete: [...document.querySelectorAll("[data-completion-id]")].every((item) => item.classList.contains("done")),
    completeEnabled: !document.querySelector("[data-complete-module]").disabled,
    width: document.documentElement.clientWidth,
    scrollWidth: document.documentElement.scrollWidth,
    emptyButtons: [...document.querySelectorAll("button")].filter((button) => !button.textContent.trim() && !button.getAttribute("aria-label")).length,
    maxTransitionMs: Math.max(0, ...[...document.querySelectorAll("*")].map((node) => {
      const duration = getComputedStyle(node).transitionDuration.split(",")[0];
      return duration.endsWith("ms") ? Number.parseFloat(duration) : Number.parseFloat(duration) * 1000;
    }).filter(Number.isFinite)),
  }));
  const captureDir = path.join(captureRoot, `module-${moduleNumber}`, mode);
  fs.mkdirSync(captureDir, {recursive: true});
  await page.screenshot({path: path.join(captureDir, "full-page.png"), fullPage: true});
  await page.locator(".signature-component").screenshot({path: path.join(captureDir, "signature-component.png")});
  await context.close();
  return {moduleNumber, mode, errors, graphOpen, graphClosed, graphFocusReturned, glossaryOpen, ...state};
}

(async () => {
  const browser = await chromium.launch({headless: true, executablePath: chrome});
  const results = [];
  for (const [number, slug, distName] of modules) for (const mode of ["desktop", "tablet", "phone"]) results.push(await inspect(browser, number, slug, distName, mode));
  await browser.close();
  const failures = [];
  for (const result of results) {
    if (result.errors.length) failures.push({module: result.moduleNumber, mode: result.mode, errors: result.errors});
    if (!result.graphOpen || !result.graphClosed || !result.graphFocusReturned || !result.glossaryOpen) failures.push({module: result.moduleNumber, mode: result.mode, drawers: result});
    if (result.h1Count !== 1 || result.sectionCount !== 7 || result.visualCount !== 4 || !result.imagesLoaded || new Set(result.visualTypes).size !== 4) failures.push({module: result.moduleNumber, mode: result.mode, visuals: result});
    if (!result.requiredComplete || !result.completeEnabled) failures.push({module: result.moduleNumber, mode: result.mode, completion: result});
    if (result.scrollWidth > result.width + 1 || result.emptyButtons) failures.push({module: result.moduleNumber, mode: result.mode, layout: result});
    if (result.mode === "phone" && result.maxTransitionMs > 1) failures.push({module: result.moduleNumber, mode: result.mode, reducedMotionMs: result.maxTransitionMs});
  }
  console.log(JSON.stringify({pageRuns: results, failureCount: failures.length, failures}, null, 2));
  if (failures.length) process.exitCode = 1;
})();
