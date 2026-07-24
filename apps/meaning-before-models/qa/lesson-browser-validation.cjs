const { chromium } = require("playwright");

const base = "http://127.0.0.1:8765/apps/meaning-before-models/curriculum/";
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const lessons = [
  "module-01-rdf-in-15-minutes.html",
  "module-02-anatomy-of-a-triple.html",
  "module-03-which-pump-do-you-mean.html",
  "module-04-from-triples-to-a-utility-knowledge-graph.html",
  "module-05-five-layers-of-meaning.html",
  "module-06-taxonomies-vocabularies-and-rdfs.html",
  "module-07-ontology-engineering-in-plain-language.html",
  "module-08-ask-the-graph-with-sparql.html",
  "module-09-reasoning-and-inference-with-owl.html",
  "module-10-validation-with-shacl.html",
  "module-11-references-provenance-authority-and-time.html",
  "module-12-running-knowledge-spine.html",
  "module-13-map-meaning-to-data.html",
  "module-14-virtualize-cache-index-or-materialize.html",
  "module-15-structured-and-unstructured-knowledge.html",
  "module-16-context-engines-and-runtime-ai-context.html",
  "module-17-bi-rag-graph-and-agentic-applications.html",
  "module-18-design-the-one-water-knowledge-spine.html",
];

async function inspect(browser, lesson, mobile) {
  const page = await browser.newPage({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 1000 },
    reducedMotion: mobile ? "reduce" : "no-preference",
  });
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") errors.push(message.text());
  });
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(base + lesson, { waitUntil: "networkidle" });

  const graphTrigger = page.locator("[data-open-graph]").first();
  await graphTrigger.click();
  const graphOpen = await page.locator("#graphDrawer").getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  const graphClosed = await page.locator("#graphDrawer").getAttribute("aria-hidden") === "true";
  const focusReturned = await graphTrigger.evaluate((node) => document.activeElement === node);

  await page.locator('.lenses [data-lens="practitioner"]').click();
  const lensChanged = await page.locator("body").getAttribute("data-lens") === "practitioner";

  const state = await page.evaluate(() => {
    const transition = getComputedStyle(document.querySelector(".drawer")).transitionDuration;
    const transitionMs = transition.endsWith("ms")
      ? Number.parseFloat(transition)
      : Number.parseFloat(transition) * 1000;
    return {
      h1: document.querySelectorAll("h1").length,
      main: document.querySelectorAll("main").length,
      tooltip: document.querySelectorAll("#tt").length,
      width: document.documentElement.clientWidth,
      scrollWidth: document.documentElement.scrollWidth,
      reducedDrawerTransition: transition,
      reducedDrawerTransitionMs: transitionMs,
      emptyButtons: [...document.querySelectorAll("button")].filter(
        (button) => !button.textContent.trim() && !button.getAttribute("aria-label")
      ).length,
    };
  });
  await page.close();
  return {
    lesson,
    mode: mobile ? "mobile-reduced-motion" : "desktop",
    errors,
    graphOpen,
    graphClosed,
    focusReturned,
    lensChanged,
    ...state,
  };
}

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const results = [];
  for (const lesson of lessons) {
    results.push(await inspect(browser, lesson, false));
    results.push(await inspect(browser, lesson, true));
  }
  await browser.close();

  const failures = results.filter((item) => (
    item.errors.length
    || !item.graphOpen
    || !item.graphClosed
    || !item.focusReturned
    || !item.lensChanged
    || item.h1 !== 1
    || item.main !== 1
    || item.tooltip !== 1
    || item.scrollWidth > item.width + 1
    || item.emptyButtons
    || (item.mode === "mobile-reduced-motion" && item.reducedDrawerTransitionMs > 0.01)
  ));
  console.log(JSON.stringify({ results, failureCount: failures.length }, null, 2));
  if (failures.length) process.exitCode = 1;
})();
