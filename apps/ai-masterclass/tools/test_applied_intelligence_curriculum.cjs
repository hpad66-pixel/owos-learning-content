const { chromium } = require("playwright");
const path = require("path");

const pagePath = path.resolve(
  __dirname,
  "../output/html/one-water-ai-applied-intelligence-curriculum.html",
);
const url = `file://${pagePath}`;

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

(async () => {
  const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const errors = [];
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  page.on("console", (msg) => {
    if (msg.type() === "error") errors.push(`console: ${msg.text()}`);
  });
  page.on("pageerror", (err) => errors.push(`pageerror: ${err.message}`));
  await page.goto(url, { waitUntil: "load" });

  assert((await page.locator("details.toc-module").count()) === 64, "Expected all 64 module groups.");
  const detailedLinks = await page.locator("button.section-link").count();
  assert(detailedLinks > 600, "Expected detailed section navigation.");

  await page.locator("#search").fill("M40.P06");
  assert((await page.locator("details.toc-module").count()) === 1, "Stable-ID search did not isolate Module 40.");
  const planned = page.locator('button.section-link[data-anchor="owai-m40-p06"]');
  assert((await planned.count()) === 1, "The planned Module 40 section is missing.");
  await planned.click();
  await page.waitForTimeout(300);
  assert(page.url().includes("module=40"), "The detailed navigation did not open Module 40.");
  assert(page.url().includes("section=owai-m40-p06"), "The section deep link was not preserved.");

  const frame = page.locator("#frame");
  assert((await frame.getAttribute("title")).startsWith("Module 40"), "The module reader did not update.");
  const target = page.frameLocator("#frame").locator("#owai-m40-p06");
  assert((await target.count()) === 1, "The requested planned section is not present in the module.");

  const desktopOverflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
  assert(!desktopOverflow, "Desktop view has page-level horizontal overflow.");
  await page.screenshot({ path: "/tmp/one-water-ai-curriculum-desktop.png", fullPage: false });

  await page.setViewportSize({ width: 390, height: 844 });
  await page.reload({ waitUntil: "load" });
  const mobileOverflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
  assert(!mobileOverflow, "Mobile view has page-level horizontal overflow.");
  await page.locator("#menu").click();
  assert(await page.locator("body").evaluate((node) => node.classList.contains("nav-open")), "Mobile contents drawer did not open.");
  await page.locator("#search").fill("M40.03");
  assert((await page.locator("details.toc-module").count()) === 1, "Mobile section search did not isolate Module 40.");
  await page.waitForTimeout(300);
  const sidebarBox = await page.locator("#sidebar").boundingBox();
  assert(sidebarBox && sidebarBox.x >= -1, "Mobile contents drawer is not visible after search.");
  await page.screenshot({ path: "/tmp/one-water-ai-curriculum-mobile.png", fullPage: false });

  assert(errors.length === 0, errors.join("\n"));
  await browser.close();
  console.log(JSON.stringify({
    modules: 64,
    detailedLinks,
    desktopOverflow,
    mobileOverflow,
    errors,
    screenshots: [
      "/tmp/one-water-ai-curriculum-desktop.png",
      "/tmp/one-water-ai-curriculum-mobile.png",
    ],
  }, null, 2));
})().catch((err) => {
  console.error(err.stack || err.message);
  process.exit(1);
});
