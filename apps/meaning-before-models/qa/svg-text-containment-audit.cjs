const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");

const courseRoot = path.resolve(__dirname, "..");
const moduleRoot = path.join(courseRoot, "modules");
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const files = fs.readdirSync(moduleRoot)
  .filter((name) => /^module-(0[1-9]|1[0-8])-/.test(name))
  .flatMap((name) => {
    const visualRoot = path.join(moduleRoot, name, "visuals");
    if (!fs.existsSync(visualRoot)) return [];
    return fs.readdirSync(visualRoot)
      .filter((file) => file.endsWith(".svg"))
      .map((file) => path.join(visualRoot, file));
  })
  .sort();

function fileUrl(file) {
  return `file://${file}`;
}

async function inspect(page, file) {
  await page.goto(fileUrl(file), { waitUntil: "load" });
  return page.evaluate(() => {
    const svg = document.documentElement;
    const viewBox = svg.viewBox.baseVal;
    const svgClient = svg.getBoundingClientRect();
    const rootBounds = {
      x: svgClient.left,
      y: svgClient.top,
      right: svgClient.right,
      bottom: svgClient.bottom,
    };
    const transformedBox = (element) => {
      const box = element.getBoundingClientRect();
      return {
        x: box.left,
        y: box.top,
        right: box.right,
        bottom: box.bottom,
        width: box.width,
        height: box.height,
      };
    };
    const rects = [...svg.querySelectorAll("rect")]
      .map((element) => ({ element, box: transformedBox(element) }))
      .filter(({ box }) => box.width < svgClient.width * 0.96 || box.height < svgClient.height * 0.96);
    const violations = [];
    for (const [index, text] of [...svg.querySelectorAll("text")].entries()) {
      const content = text.textContent.trim();
      if (!content) continue;
      if ((text.getAttribute("transform") || "").includes("rotate")) continue;
      const box = transformedBox(text);
      const center = { x: (box.x + box.right) / 2, y: (box.y + box.bottom) / 2 };
      const containers = rects
        .filter(({ box: candidate }) =>
          center.x >= candidate.x && center.x <= candidate.right &&
          center.y >= candidate.y && center.y <= candidate.bottom)
        .sort((a, b) => a.box.width * a.box.height - b.box.width * b.box.height);
      const container = containers[0]?.box || rootBounds;
      const padding = containers.length ? Math.min(10, container.width * 0.025) : 2;
      const overflow = {
        left: Math.max(0, container.x + padding - box.x),
        right: Math.max(0, box.right - (container.right - padding)),
        top: Math.max(0, container.y + padding - box.y),
        bottom: Math.max(0, box.bottom - (container.bottom - padding)),
      };
      const maximum = Math.max(...Object.values(overflow));
      if (maximum > 1) {
        violations.push({
          index,
          text: content,
          box,
          container,
          overflow,
          maximum,
          hasExplicitLength: text.hasAttribute("textLength"),
        });
      }
    }
    return {
      title: svg.querySelector("title")?.textContent || "",
      textCount: svg.querySelectorAll("text").length,
      violations,
    };
  });
}

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  const results = [];
  for (const file of files) {
    const result = await inspect(page, file);
    results.push({ file: path.relative(courseRoot, file), ...result });
  }
  await browser.close();
  const failures = results.filter((result) => result.violations.length);
  const report = {
    filesChecked: results.length,
    textElementsChecked: results.reduce((sum, result) => sum + result.textCount, 0),
    filesWithViolations: failures.length,
    violationCount: failures.reduce((sum, result) => sum + result.violations.length, 0),
    failures,
  };
  console.log(JSON.stringify(report, null, 2));
  if (failures.length) process.exitCode = 1;
})();
