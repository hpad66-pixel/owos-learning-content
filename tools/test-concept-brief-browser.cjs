const { chromium } = require("playwright");
const path = require("node:path");
const { pathToFileURL } = require("node:url");

const root = path.resolve(__dirname, "..");
const target = process.argv[3]
  ? path.resolve(process.argv[3])
  : path.join(
    root,
    "concept-briefs/coagulation-vs-flocculation/dist/final-public-candidate.html",
  );
const outputDir = process.argv[2] || path.join(root, "concept-briefs/coagulation-vs-flocculation/dist");
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const modes = [
  { name: "desktop", width: 1440, height: 1000, reducedMotion: "no-preference" },
  { name: "tablet", width: 820, height: 1180, reducedMotion: "no-preference" },
  { name: "phone-reduced-motion", width: 390, height: 844, reducedMotion: "reduce" },
];

async function inspect(browser, mode) {
  const page = await browser.newPage({
    viewport: { width: mode.width, height: mode.height },
    reducedMotion: mode.reducedMotion,
  });
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") errors.push(message.text());
  });
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(pathToFileURL(target).href, { waitUntil: "load" });
  await page.waitForSelector(".jar-model");
  await page.screenshot({
    path: path.join(outputDir, `coagulation-brief-${mode.name}-top.png`),
    fullPage: false,
  });
  await page.locator("#block-jar").screenshot({
    path: path.join(outputDir, `coagulation-brief-${mode.name}-jar-initial.png`),
  });
  const canvasFrameOne = await page.locator(".jar-canvas").evaluate((canvas) => canvas.toDataURL());
  await page.waitForTimeout(140);
  const canvasFrameTwo = await page.locator(".jar-canvas").evaluate((canvas) => canvas.toDataURL());
  const canvasChanged = canvasFrameOne !== canvasFrameTwo;

  const initial = await page.locator(".jar-result").innerText();
  await page.getByRole("button", { name: "Flocculation", exact: true }).click();
  await page.getByRole("button", { name: "Excessive energy", exact: true }).click();
  const changed = await page.locator(".jar-result").innerText();
  const modelState = await page.locator(".jar-model").evaluate((node) => ({
    stage: node.dataset.stage,
    flocculation: node.dataset.flocculation,
  }));
  const stageCheck = page.locator('[data-concept-assessment="multiple-choice"]');
  await stageCheck.locator('input[data-correct="true"]').check();
  await stageCheck.locator(".assessment-check").click();
  const stageCheckComplete = await stageCheck.getAttribute("data-complete");
  const reflection = page.locator('[data-concept-assessment="reflection"]');
  await reflection.locator("textarea").fill(
    "Which source, sample, process, procedure, reviewer, monitoring, and rollback evidence is missing?",
  );
  await reflection.locator(".assessment-reveal").click();
  const reflectionComplete = await reflection.getAttribute("data-complete");
  const communityOpener = page.getByRole("button", { name: "Community", exact: true });
  await communityOpener.click();
  const communityDrawerVisible = await page.locator("#community-drawer").isVisible();
  await page.keyboard.press("Escape");
  const drawerFocusReturned = await communityOpener.evaluate(
    (node) => document.activeElement === node,
  );
  await page.locator("#owos-concept-sop").scrollIntoViewIfNeeded();
  await page.getByRole("button", { name: "Copy the outline", exact: true }).click();
  await page.waitForFunction(
    () => /copied|blocked/i.test(document.querySelector("#copy-sop-status")?.textContent || ""),
  );
  const sopCopyStatus = await page.locator("#copy-sop-status").innerText();

  await page.locator("body").click({ position: { x: 2, y: 2 } });
  let focusedJarControl = false;
  for (let index = 0; index < 20; index += 1) {
    await page.keyboard.press("Tab");
    focusedJarControl = await page.evaluate(
      () => document.activeElement?.classList.contains("jar-control") || false,
    );
    if (focusedJarControl) break;
  }
  const focusOutline = focusedJarControl
    ? await page.evaluate(() => getComputedStyle(document.activeElement).outlineStyle)
    : "missing";
  const state = await page.evaluate(() => {
    const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
    return {
      h1: document.querySelectorAll("h1").length,
      main: document.querySelectorAll("main").length,
      width: document.documentElement.clientWidth,
      scrollWidth: document.documentElement.scrollWidth,
      buttons: document.querySelectorAll(".jar-control").length,
      pressedButtons: document.querySelectorAll('.jar-control[aria-pressed="true"]').length,
      liveRegion: Boolean(document.querySelector('.jar-result[aria-live="polite"]')),
      relatedAnchor: Boolean(document.querySelector("#owos-concept-related")),
      communityAnchor: Boolean(document.querySelector("#owos-concept-community")),
      sopAnchor: Boolean(document.querySelector("#owos-concept-sop")),
      quickTakeaway: Boolean(document.querySelector(".quick-takeaway")),
      primaryNavControls: document.querySelectorAll(".quick-nav > a, .quick-nav > button").length,
      finalRecapItems: document.querySelectorAll(".final-recap-grid article").length,
      feedbackForm: Boolean(document.querySelector("#owos-concept-finish [data-concept-feedback]")),
      testimonialMount: Boolean(document.querySelector("[data-concept-testimonials]")),
      testimonialConsent: Boolean(document.querySelector("[data-testimonial-consent]")),
      appreciationOption: Boolean(document.querySelector('#concept-feedback-kind option[value="appreciation"]')),
      feedbackAfterCommercial: Boolean(
        document.querySelector("#owos-commercial-placements")
        && document.querySelector("#owos-concept-finish")
        && (document.querySelector("#owos-commercial-placements").compareDocumentPosition(
          document.querySelector("#owos-concept-finish"),
        ) & Node.DOCUMENT_POSITION_FOLLOWING)
      ),
      inactiveVendorHidden: !document.querySelector('[data-placement-slot="concept-vendor"]'),
      boundaryVisible: Boolean(document.querySelector(".boundary")?.innerText.trim()),
      reduced,
      scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior,
      emptyButtons: [...document.querySelectorAll("button")].filter(
        (button) => !button.textContent.trim() && !button.getAttribute("aria-label"),
      ).length,
      canvasReady: Boolean(
        document.querySelector(".jar-canvas")?.width
        && document.querySelector(".jar-canvas")?.height
      ),
      assessmentCount: document.querySelectorAll("[data-concept-assessment]").length,
      crossSectorVisual: Boolean(
        document.querySelector('img[src*="cross-sector-particle-pathways.svg"]'),
      ),
      overflowElements: [...document.querySelectorAll("body *")]
        .map((node) => ({ node, rect: node.getBoundingClientRect() }))
        .filter(({ rect }) => rect.right > innerWidth + 0.5 || rect.left < -0.5)
        .slice(0, 8)
        .map(({ node, rect }) => ({
          tag: node.tagName,
          className: node.className?.baseVal || node.className || "",
          left: Math.round(rect.left * 10) / 10,
          right: Math.round(rect.right * 10) / 10,
        })),
    };
  });
  await page.screenshot({
    path: path.join(outputDir, `coagulation-brief-${mode.name}.png`),
    fullPage: true,
  });
  await page.locator("#block-jar").screenshot({
    path: path.join(outputDir, `coagulation-brief-${mode.name}-jar.png`),
  });
  await page.locator("#block-system-fit").screenshot({
    path: path.join(outputDir, `coagulation-brief-${mode.name}-treatment-train.png`),
  });
  await page.locator("#owos-concept-related").screenshot({
    path: path.join(outputDir, `coagulation-brief-${mode.name}-related.png`),
  });
  await page.locator("#owos-concept-community").screenshot({
    path: path.join(outputDir, `coagulation-brief-${mode.name}-community.png`),
  });
  await page.locator("#owos-concept-sop").screenshot({
    path: path.join(outputDir, `coagulation-brief-${mode.name}-sop.png`),
  });
  await page.locator("#owos-commercial-placements").screenshot({
    path: path.join(outputDir, `coagulation-brief-${mode.name}-commercial.png`),
  });
  await page.locator("#owos-concept-finish").screenshot({
    path: path.join(outputDir, `coagulation-brief-${mode.name}-finish.png`),
  });
  await page.close();
  return {
    mode: mode.name,
    errors,
    initialResultPresent: initial.trim().length > 0,
    changedResultMentionsBreakage: /breakage/i.test(changed),
    canvasChanged,
    modelState,
    stageCheckComplete,
    reflectionComplete,
    focusOutline,
    focusedJarControl,
    communityDrawerVisible,
    drawerFocusReturned,
    sopCopyStatus,
    ...state,
  };
}

async function inspectNoJavaScript(browser) {
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    javaScriptEnabled: false,
  });
  const page = await context.newPage();
  await page.goto(pathToFileURL(target).href, { waitUntil: "load" });
  const state = await page.evaluate(() => ({
    fallbackText: document.querySelector("noscript")?.innerText || "",
    boundary: document.querySelector(".boundary")?.innerText || "",
    scrollWidth: document.documentElement.scrollWidth,
    width: document.documentElement.clientWidth,
  }));
  await context.close();
  return {
    mode: "phone-no-javascript",
    fallbackPresent: state.fallbackText.includes("Text equivalent"),
    boundaryPresent: state.boundary.includes("Model boundary"),
    contained: state.scrollWidth <= state.width + 1,
  };
}

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const results = [];
  for (const mode of modes) results.push(await inspect(browser, mode));
  const noJavaScript = await inspectNoJavaScript(browser);
  await browser.close();

  const failures = results.filter((item) => (
    item.errors.length
    || item.h1 !== 1
    || item.main !== 1
    || item.scrollWidth > item.width + 1
    || item.buttons !== 10
    || item.pressedButtons !== 3
    || !item.initialResultPresent
    || !item.changedResultMentionsBreakage
    || item.modelState.stage !== "flocculation"
    || item.modelState.flocculation !== "excess"
    || !item.focusedJarControl
    || item.focusOutline === "none"
    || !item.liveRegion
    || !item.relatedAnchor
    || !item.communityAnchor
    || !item.sopAnchor
    || !item.quickTakeaway
    || item.primaryNavControls !== 4
    || item.finalRecapItems !== 3
    || !item.feedbackForm
    || !item.testimonialMount
    || !item.testimonialConsent
    || !item.appreciationOption
    || !item.feedbackAfterCommercial
    || !item.inactiveVendorHidden
    || !item.communityDrawerVisible
    || !item.drawerFocusReturned
    || !/copied|blocked/i.test(item.sopCopyStatus)
    || !item.boundaryVisible
    || !item.canvasReady
    || item.assessmentCount < 2
    || item.stageCheckComplete !== "true"
    || item.reflectionComplete !== "true"
    || !item.crossSectorVisual
    || (item.mode === "phone-reduced-motion" ? item.canvasChanged : !item.canvasChanged)
    || item.emptyButtons
    || (
      item.mode === "phone-reduced-motion"
      && (!item.reduced || item.scrollBehavior !== "auto")
    )
  ));
  if (!noJavaScript.fallbackPresent || !noJavaScript.boundaryPresent || !noJavaScript.contained) {
    failures.push(noJavaScript);
  }
  console.log(JSON.stringify({
    pageRuns: results.length + 1,
    failureCount: failures.length,
    results,
    noJavaScript,
  }, null, 2));
  if (failures.length) process.exitCode = 1;
})();
