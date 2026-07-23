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

async function inspectLesson(browser, lesson, mobile = false) {
  const page = await browser.newPage({
    viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 1000 },
    reducedMotion: mobile ? "reduce" : "no-preference",
  });
  const errors = [];
  page.on("console", message => {
    if (message.type() === "error") errors.push(message.text());
  });
  page.on("pageerror", error => errors.push(error.message));
  await page.goto(base + lesson, { waitUntil: "networkidle" });

  const graphTrigger = page.locator("[data-open-graph]:visible").first();
  await graphTrigger.click();
  const drawerOpened = await page.locator("#graphDrawer").getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  await page.waitForTimeout(50);
  const drawerClosed = await page.locator("#graphDrawer").getAttribute("aria-hidden") === "true";
  const focusReturned = await graphTrigger.evaluate(node => document.activeElement === node);

  const cards = page.locator(".flip-question");
  for (let index = 0; index < await cards.count(); index += 1) await cards.nth(index).click();
  const cardsTurned = await page.locator(".flip-question.turned").count();

  const evidence = await page.evaluate(() => {
    const lessonVisuals = [...document.querySelectorAll('[id^="visual-"][data-visual-shape]')];
    const visualTypes = lessonVisuals.map(node => node.dataset.visualType);
    const visualShapes = lessonVisuals.map(node => node.dataset.visualShape);
    const visualRoots = lessonVisuals.map(node => {
      const root = node.querySelector(".visual-stage")?.firstElementChild;
      return root ? `${root.tagName}.${[...root.classList].join(".")}` : "";
    });
    const quizTypes = [...document.querySelectorAll("[data-quiz-type][data-required]")]
      .map(node => node.dataset.quizType);
    return {
      h1: document.querySelector("h1")?.textContent.trim(),
      visualTypes,
      visualShapes,
      visualRoots,
      quizTypes,
      scrollWidth: document.documentElement.scrollWidth,
      viewportWidth: innerWidth,
      reducedTransition: getComputedStyle(document.querySelector(".drawer")).transitionDuration,
      unlabeledButtons: [...document.querySelectorAll("button")].filter(button =>
        !(button.getAttribute("aria-label") || button.getAttribute("aria-labelledby") ||
          button.textContent.trim() || button.getAttribute("title"))).length,
    };
  });

  if (evidence.visualTypes.length !== 4) errors.push(`expected 4 lesson visuals, found ${evidence.visualTypes.length}`);
  if (new Set(evidence.visualShapes).size !== 4) errors.push("visual shapes are not distinct");
  if (new Set(evidence.visualRoots).size !== 4) errors.push("inner visual structures are not distinct");
  if (cardsTurned < 4) errors.push(`expected four turned question cards, found ${cardsTurned}`);
  if (evidence.scrollWidth > evidence.viewportWidth + 1) errors.push(`horizontal overflow ${evidence.scrollWidth}/${evidence.viewportWidth}`);
  if (evidence.unlabeledButtons) errors.push(`${evidence.unlabeledButtons} unlabeled buttons`);
  if (!drawerOpened || !drawerClosed || !focusReturned) errors.push("drawer focus behavior failed");

  const number = lesson.slice(7, 9);
  const mode = mobile ? "mobile" : "desktop";
  await page.locator("#visual-1").scrollIntoViewIfNeeded();
  await page.screenshot({
    path: `/private/tmp/mbm-${number}-${mode}-visual.png`,
    fullPage: false,
  });
  await page.close();
  return { lesson, mode, errors, cardsTurned, ...evidence };
}

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const results = [];
  for (const lesson of lessons) {
    results.push(await inspectLesson(browser, lesson, false));
    results.push(await inspectLesson(browser, lesson, true));
  }
  await browser.close();
  const failures = results.filter(result => result.errors.length);
  console.log(JSON.stringify({
    inspected: results.length,
    lessons: lessons.length,
    failures,
    visualSequences: results.filter(result => result.mode === "desktop")
      .map(({ lesson, visualTypes, visualShapes, quizTypes }) => ({ lesson, visualTypes, visualShapes, quizTypes })),
  }, null, 2));
  if (failures.length) process.exit(1);
})().catch(error => {
  console.error(error);
  process.exit(1);
});
