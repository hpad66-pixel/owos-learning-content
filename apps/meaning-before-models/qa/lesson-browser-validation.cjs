const { chromium } = require("playwright");

const base = "http://127.0.0.1:8765/apps/meaning-before-models/curriculum/";
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

async function answerSingle(page, quizName) {
  const quiz = page.locator(`[data-quiz="${quizName}"]`);
  await quiz.locator('[data-correct="1"]').click();
  await quiz.locator("[data-check-quiz]").click();
}

async function answerMatching(page, matchName) {
  const root = page.locator(`[data-match="${matchName}"]`);
  const fields = root.locator("select[data-answer]");
  for (let index = 0; index < await fields.count(); index += 1) {
    const field = fields.nth(index);
    await field.selectOption(await field.getAttribute("data-answer"));
  }
  await root.locator("[data-check-match]").click();
}

async function advanceStepper(page, name) {
  const root = page.locator(`[data-stepper="${name}"]`);
  const count = await root.locator(".step").count();
  for (let index = 1; index < count; index += 1) {
    await root.locator("[data-next]").click();
  }
}

async function sharedChecks(page, moduleId) {
  const errors = [];
  page.on("console", (message) => {
    if (message.type() === "error") errors.push(message.text());
  });
  page.on("pageerror", (error) => errors.push(error.message));
  await page.evaluate(() => localStorage.clear());
  await page.reload({ waitUntil: "networkidle" });

  const graphTrigger = page.locator("[data-open-graph]").first();
  await graphTrigger.click();
  const drawerOpened = await page.locator("#graphDrawer").getAttribute("aria-hidden") === "false";
  await page.keyboard.press("Escape");
  await page.waitForTimeout(350);
  const drawerClosed = await page.locator("#graphDrawer").getAttribute("aria-hidden") === "true";
  const focusReturned = await graphTrigger.evaluate((node) => document.activeElement === node);

  await page.locator('[data-lens="practitioner"]').click();
  const practitionerLens = await page.locator("body").getAttribute("data-lens") === "practitioner";

  const mainCount = await page.locator("main").count();
  const h1Count = await page.locator("h1").count();
  const unlabeledControlText = await page.locator("button").evaluateAll((buttons) =>
    buttons
      .filter((button) => !(
        button.getAttribute("aria-label")
        || button.getAttribute("aria-labelledby")
        || button.textContent.trim()
        || button.getAttribute("title")
      ))
      .map((button) => button.outerHTML)
  );
  const unlabeledControls = unlabeledControlText.length;

  return {
    moduleId,
    errors,
    drawerOpened,
    drawerClosed,
    focusReturned,
    practitionerLens,
    mainCount,
    h1Count,
    unlabeledControls,
    unlabeledControlText,
  };
}

async function completeModuleOne(browser) {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  await page.goto(base + "module-01-rdf-in-15-minutes.html", { waitUntil: "networkidle" });
  const checks = await sharedChecks(page, "module-01");

  await page.locator("[data-record]").nth(0).click();
  await page.locator("[data-record]").nth(1).click();

  const triple = page.locator("[data-triple-builder]");
  await triple.locator("select").nth(0).selectOption({ label: "Pump_P104" });
  await triple.locator("select").nth(1).selectOption({ label: "serves" });
  await triple.locator("select").nth(2).selectOption({ label: "Pressure_Zone_3" });
  await triple.locator("[data-check-triple]").click();
  await answerSingle(page, "triple-check");

  await advanceStepper(page, "graph");
  await answerSingle(page, "path-check");
  await page.locator('[data-stack-item][data-title="SHACL"]').click();
  await answerMatching(page, "standards-match");

  const form = page.locator('form[data-artifact="relationship-card"]');
  const values = [
    "Pump P-104",
    "serves",
    "Pressure Zone 3",
    "Approved GIS asset-zone mapping",
    "Which accounts may be affected when Pump P-104 is unavailable?",
  ];
  const fields = form.locator("input, textarea");
  for (let index = 0; index < values.length; index += 1) {
    await fields.nth(index).fill(values[index]);
  }
  await form.locator('button[type="submit"]').click();

  const complete = page.locator("[data-complete]");
  checks.completionEnabled = !(await complete.isDisabled());
  checks.requirementsDone = await page.locator(".req.done").count();
  checks.requirementsTotal = await page.locator(".req").count();
  await complete.click();
  checks.completionRecorded = (await complete.textContent()).includes("Lesson complete");
  await page.close();
  return checks;
}

async function completeModuleFive(browser) {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  await page.goto(base + "module-05-five-layers-of-meaning.html", { waitUntil: "networkidle" });
  const checks = await sharedChecks(page, "module-05");

  const opening = page.locator("#opening-quiz");
  await opening.locator('[data-correct="1"]').click();
  await opening.locator("[data-check-quiz]").click();

  for (let index = 0; index < 5; index += 1) {
    await page.locator(`[data-match-question="${index}"]`).click();
    await page.locator(`[data-match-job="${index}"]`).click();
  }

  const sortRows = page.locator("[data-sort-index]");
  for (let index = 0; index < await sortRows.count(); index += 1) {
    const row = sortRows.nth(index);
    const answer = await row.getAttribute("data-answer");
    await row.locator(`[data-sort-job="${answer}"]`).click();
  }

  for (let index = 1; index < 6; index += 1) {
    await page.locator("[data-next]").click();
  }

  const desiredOrder = [
    "Read stable source structure",
    "Resolve shared concepts and relationships",
    "Apply approved mappings and source authority",
    "Retrieve current evidence, policy, time, and permission",
    "Assemble bounded AI context",
    "Send cited draft to human authority",
  ];
  for (let target = 0; target < desiredOrder.length; target += 1) {
    for (;;) {
      const rows = page.locator(".order-row");
      const texts = await rows.locator("span").allTextContents();
      const current = texts.indexOf(desiredOrder[target]);
      if (current === target) break;
      await rows.nth(current).locator("[data-move-up]").click();
    }
  }
  await page.locator("[data-check-order]").click();

  await page.locator('[data-failure="semantic"]').click();

  const tfRows = page.locator(".tf-row");
  for (let index = 0; index < await tfRows.count(); index += 1) {
    const row = tfRows.nth(index);
    const answer = await row.getAttribute("data-answer");
    await row.locator(`[data-value="${answer}"]`).click();
  }
  await page.locator("[data-check-tf]").click();

  const contextQuiz = page.locator("#context-quiz");
  const desired = contextQuiz.locator('[data-correct="1"]');
  for (let index = 0; index < await desired.count(); index += 1) {
    await desired.nth(index).click();
  }
  await contextQuiz.locator("[data-check-multi]").click();

  const raciRows = page.locator("[data-raci-body] tr");
  for (let index = 0; index < await raciRows.count(); index += 1) {
    const row = raciRows.nth(index);
    await row.locator("select").nth(0).selectOption(await row.getAttribute("data-owner"));
    await row.locator("select").nth(1).selectOption(await row.getAttribute("data-responsible"));
  }
  await page.locator("[data-check-raci]").click();

  const form = page.locator('form[data-artifact="five-layer-meaning-map"]');
  const values = [
    "Which active critical-facility accounts may be exposed to Pressure Event 771?",
    "CIS account and status fields, GIS premise-zone keys, and SCADA event records.",
    "Critical facility and customer service categories.",
    "Account serves premise; premise is in zone; pressure event affects zone.",
    "Governed CIS, GIS, and SCADA mappings with effective-time and source-authority tests.",
    "Event 771, current policy, user permission, known stale GIS link, evidence, and draft-only limit.",
    "Operations owner, customer domain owner, GIS steward, cybersecurity, and policy steward.",
    "The model cannot issue an advisory. An authorized human must review and decide.",
  ];
  const fields = form.locator("input, textarea");
  for (let index = 0; index < values.length; index += 1) {
    await fields.nth(index).fill(values[index]);
  }
  await form.locator('button[type="submit"]').click();
  await page.locator("[data-check-applied]").click();

  const complete = page.locator("[data-complete]");
  checks.completionEnabled = !(await complete.isDisabled());
  checks.requirementsDone = await page.locator(".req.done").count();
  checks.requirementsTotal = await page.locator(".req").count();
  await complete.click();
  checks.completionRecorded = (await page.locator("#live").textContent()).includes("marked complete");
  await page.close();
  return checks;
}

async function mobileAndMotionChecks(browser, lesson) {
  const page = await browser.newPage({
    viewport: { width: 390, height: 844 },
    reducedMotion: "reduce",
  });
  await page.goto(base + lesson, { waitUntil: "networkidle" });
  const result = await page.evaluate(() => ({
    viewport: window.innerWidth,
    scrollWidth: document.documentElement.scrollWidth,
    bodyWidth: document.body.getBoundingClientRect().width,
    reducedTransition: getComputedStyle(document.querySelector(".drawer")).transitionDuration,
    reducedAnimation: getComputedStyle(document.querySelector(".reading")).animationDuration,
  }));
  await page.screenshot({
    path: `/private/tmp/${lesson.replace(".html", "")}-mobile-top.png`,
    fullPage: false,
  });
  await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight / 2));
  await page.waitForTimeout(100);
  await page.screenshot({
    path: `/private/tmp/${lesson.replace(".html", "")}-mobile-middle.png`,
    fullPage: false,
  });
  await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(100);
  await page.screenshot({
    path: `/private/tmp/${lesson.replace(".html", "")}-mobile-bottom.png`,
    fullPage: false,
  });
  await page.close();
  return { lesson, ...result };
}

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const results = {
    moduleOne: await completeModuleOne(browser),
    moduleFive: await completeModuleFive(browser),
    mobile: [
      await mobileAndMotionChecks(browser, "module-01-rdf-in-15-minutes.html"),
      await mobileAndMotionChecks(browser, "module-05-five-layers-of-meaning.html"),
    ],
  };
  await browser.close();
  console.log(JSON.stringify(results, null, 2));
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
