#!/usr/bin/env node
/**
 * a11y-scan.js
 *
 * Live accessibility scan of a built Adapt course, using Playwright +
 * axe-core (@axe-core/playwright, already a devDependency) against every
 * content-object page, in each display mode the GROW mode switcher offers
 * (light / dark / contrast). Checks the full WCAG rule set axe-core knows
 * about (2.0/2.1 A+AA, plus whatever 2.2 rules the installed axe-core
 * ships), not just colour contrast — see tools/contrast-audit.js for a
 * narrower, no-server contrast-only check of the high-contrast theme's
 * tokens.
 *
 * Serves build/ itself with a tiny static file server (no grunt/browser
 * dependency, so this can run headless in CI) — equivalent to
 * `grunt server-scorm --port=<port>` but without the keepalive/open-browser
 * behaviour grunt's connect task has.
 *
 * Usage:
 *   node tools/a11y-scan.js --course=<course-slug> [--port=9001]
 *     [--modes=light,dark,contrast] [--impact=serious] [--max-pages=N] [--verbose]
 *
 *   --course     Required. Cross-checked against src/course (the symlink
 *                `grunt build` actually compiles) — warns on mismatch, since
 *                a stale build/ would silently scan the wrong course.
 *   --modes      Comma-separated subset of light,dark,contrast. Default: all three.
 *   --impact     Minimum axe impact level that fails the run: minor, moderate,
 *                serious (default), or critical. Lower-impact violations are
 *                still listed, just don't affect the exit code — axe flags
 *                some structural things (region/landmark rules) that are
 *                Adapt-core/vendor-component territory, not ours to silently
 *                "fix" by suppressing the check; serious+critical is the
 *                practical signal-to-noise default for this course content.
 *   --max-pages  Cap the number of content-object pages scanned (debugging).
 *
 * Prerequisite: `grunt build` must have been run first (this tool does not
 * build; per CLAUDE.md "fix applied" vs "verified" must stay distinct, and
 * re-building silently here would hide a stale/failed build from the user).
 *
 * Exit: 0 = no violation at or above --impact across any page/mode scanned.
 *       1 = at least one such violation, or a hard error (course mismatch,
 *           build/ missing, server/browser failure).
 */

const fs = require('fs');
const path = require('path');
const http = require('http');
const { chromium } = require('playwright');
const AxeBuilder = require('@axe-core/playwright').default;
const { resolveCourse } = require('./lib/course-resolve');

const ROOT = path.resolve(__dirname, '..');
const BUILD_DIR = path.join(ROOT, 'build');
const IMPACT_ORDER = ['minor', 'moderate', 'serious', 'critical'];
const MIME = {
  '.html': 'text/html', '.js': 'application/javascript', '.css': 'text/css',
  '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png',
  '.jpg': 'image/jpeg', '.woff': 'font/woff', '.woff2': 'font/woff2',
  '.ttf': 'font/ttf', '.mp3': 'audio/mpeg', '.mp4': 'video/mp4'
};

function parseArgs() {
  const args = { course: null, port: 9001, modes: ['light', 'dark', 'contrast'], impact: 'serious', maxPages: Infinity, verbose: false };
  const accepted = ['course', 'port', 'modes', 'impact', 'max-pages', 'verbose'];
  process.argv.slice(2).forEach(param => {
    const parts = param.replace(/^--/, '').split('=');
    const [key, ...rest] = parts;
    if (!accepted.includes(key)) {
      console.error(`Unrecognised argument: --${key}. Accepted: ${accepted.map(a => '--' + a).join(', ')}`);
      process.exit(1);
    }
    const value = rest.join('=');
    if (key === 'course') args.course = value;
    else if (key === 'port') args.port = parseInt(value, 10);
    else if (key === 'modes') args.modes = value.split(',').map(s => s.trim()).filter(Boolean);
    else if (key === 'impact') args.impact = value;
    else if (key === 'max-pages') args.maxPages = parseInt(value, 10);
    else if (key === 'verbose') args.verbose = true;
  });
  if (!args.course) {
    console.error('Usage: node tools/a11y-scan.js --course=<course-slug> [--port=9001] [--modes=light,dark,contrast] [--impact=serious]');
    process.exit(1);
  }
  if (!IMPACT_ORDER.includes(args.impact)) {
    console.error(`--impact must be one of: ${IMPACT_ORDER.join(', ')}`);
    process.exit(1);
  }
  const unknownModes = args.modes.filter(m => !['light', 'dark', 'contrast'].includes(m));
  if (unknownModes.length) {
    console.error(`Unknown --modes value(s): ${unknownModes.join(', ')}. Accepted: light, dark, contrast`);
    process.exit(1);
  }
  return args;
}

function startStaticServer(dir, port) {
  return new Promise((resolve, reject) => {
    const server = http.createServer((req, res) => {
      const urlPath = decodeURIComponent(req.url.split('?')[0]);
      let filePath = path.join(dir, urlPath === '/' ? 'index.html' : urlPath);
      // Adapt is an SPA using hash routing (#/id) — the hash never reaches the
      // server, and any non-asset path should fall back to index.html.
      if (!fs.existsSync(filePath) || fs.statSync(filePath).isDirectory()) {
        filePath = path.join(dir, 'index.html');
      }
      fs.readFile(filePath, (err, data) => {
        if (err) { res.writeHead(404); res.end('Not found'); return; }
        const ext = path.extname(filePath);
        res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
        res.end(data);
      });
    });
    server.on('error', reject);
    server.listen(port, () => resolve(server));
  });
}

/** Set the GROW mode-switcher's theme the same way its own JS does (localStorage key, read on load). */
async function setGrowTheme(page, mode) {
  if (mode === 'light') return; // light has no explicit data-theme — it's the default
  await page.evaluate((m) => {
    try { localStorage.setItem('grow-mode-theme', m); } catch (e) { /* ignore */ }
    document.documentElement.setAttribute('data-theme', m);
  }, mode);
}

async function scanPage(page, baseUrl, pageId, mode) {
  await page.goto(`${baseUrl}/#/${pageId}`, { waitUntil: 'networkidle' });
  await setGrowTheme(page, mode);
  // Adapt renders async after the hash changes; wait for this page's root node.
  try {
    await page.waitForSelector(`[data-adapt-id="${pageId}"]`, { timeout: 8000 });
  } catch (e) {
    return { error: `page [data-adapt-id="${pageId}"] never rendered (timed out)` };
  }
  await page.waitForTimeout(300); // let any CSS transitions/animations settle before the scan
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
    .analyze();
  return { violations: results.violations };
}

async function main() {
  const { course, port, modes, impact, maxPages, verbose } = parseArgs();

  // 1. Sanity: does build/ exist, and does it look like the requested course?
  if (!fs.existsSync(BUILD_DIR)) {
    console.error(`build/ not found at ${BUILD_DIR}. Run "grunt build" first — this tool scans an existing build, it does not build one.`);
    process.exit(1);
  }
  const resolved = resolveCourse(course, ['courses', 'courses/_generated']);
  if (!resolved.found) {
    console.error(`Course not found for slug "${course}". Checked:\n  ${resolved.checked.join('\n  ')}`);
    process.exit(1);
  }
  const courseLinkTarget = fs.existsSync(path.join(ROOT, 'src/course'))
    ? fs.realpathSync(path.join(ROOT, 'src/course'))
    : null;
  if (courseLinkTarget && path.resolve(courseLinkTarget) !== path.resolve(resolved.courseDir)) {
    console.error(`WARNING: src/course currently points to ${path.relative(ROOT, courseLinkTarget)}, not ${path.relative(ROOT, resolved.courseDir)}.`);
    console.error(`WARNING: build/ was almost certainly compiled from the symlinked course, not "${course}". Results below may be for the wrong course.`);
  }

  const contentObjectsPath = path.join(BUILD_DIR, 'course/en/contentObjects.json');
  if (!fs.existsSync(contentObjectsPath)) {
    console.error(`${path.relative(ROOT, contentObjectsPath)} not found — unexpected build/ layout.`);
    process.exit(1);
  }
  const contentObjects = JSON.parse(fs.readFileSync(contentObjectsPath, 'utf8'));
  const pages = contentObjects.filter(c => c._type === 'page').slice(0, maxPages);
  if (pages.length === 0) {
    console.error('No pages found in build/course/en/contentObjects.json — nothing to scan.');
    process.exit(1);
  }

  console.log(`a11y-scan: ${course}`);
  console.log(`Build: ${path.relative(ROOT, BUILD_DIR)} | Pages: ${pages.length} | Modes: ${modes.join(', ')} | Fail threshold: ${impact}+`);
  console.log('');

  // 2. Serve build/ and scan.
  const server = await startStaticServer(BUILD_DIR, port);
  const baseUrl = `http://localhost:${port}`;
  const browser = await chromium.launch();

  const allResults = []; // { pageId, title, mode, violations: [...] } | { pageId, mode, error }
  try {
    const context = await browser.newContext();
    const page = await context.newPage();
    for (const co of pages) {
      for (const mode of modes) {
        const result = await scanPage(page, baseUrl, co._id, mode);
        allResults.push({ pageId: co._id, title: co.title, mode, ...result });
      }
    }
  } finally {
    await browser.close();
    server.close();
  }

  // 3. Report.
  const impactRank = (i) => IMPACT_ORDER.indexOf(i);
  const thresholdRank = impactRank(impact);
  let failingCount = 0;
  let totalViolations = 0;
  const errors = allResults.filter(r => r.error);

  for (const r of allResults) {
    if (r.error) {
      console.log(`ERROR  | ${r.mode.padEnd(8)} | ${r.pageId} — ${r.error}`);
      continue;
    }
    if (!r.violations.length) {
      if (verbose) console.log(`CLEAN  | ${r.mode.padEnd(8)} | ${r.pageId} (${r.title || ''})`);
      continue;
    }
    for (const v of r.violations) {
      totalViolations++;
      const rank = impactRank(v.impact);
      const fails = rank >= thresholdRank;
      if (fails) failingCount++;
      console.log(`${(fails ? 'FAIL' : 'warn').padEnd(6)} | ${r.mode.padEnd(8)} | ${r.pageId} | [${v.impact}] ${v.id}: ${v.description}`);
      console.log(`       nodes: ${v.nodes.length} | help: ${v.helpUrl}`);
      if (verbose) {
        v.nodes.slice(0, 3).forEach(n => console.log(`         target: ${n.target.join(' ')}`));
      }
    }
  }

  console.log('');
  console.log('='.repeat(60));
  console.log('SUMMARY');
  console.log('='.repeat(60));
  console.log(`Pages x modes scanned: ${allResults.length - errors.length} (${errors.length} failed to render)`);
  console.log(`Total violations found: ${totalViolations} (${failingCount} at or above "${impact}")`);

  if (errors.length || failingCount > 0) {
    console.log('');
    console.log('a11y-scan: FAILED');
    process.exit(1);
  } else {
    console.log('');
    console.log('a11y-scan: PASSED');
    process.exit(0);
  }
}

main().catch(err => {
  console.error('a11y-scan: unexpected error:', err);
  process.exit(1);
});
