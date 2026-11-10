import { chromium } from 'playwright';

const BASE = 'http://127.0.0.1:9025/';
const results = [];
function record(label, ok, detail) {
  results.push({ label, ok, detail });
  console.log(`${ok ? 'PASS' : 'FAIL'} — ${label}${detail ? ' :: ' + detail : ''}`);
}

const browser = await chromium.launch();

// 11. Wrapper page: single article, no trickle gate at all behind it.
// Notes should be present and visible immediately on load, no mirror.
{
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto(BASE + '#/id/reflective-practice-introductory-W-OPEN-co-01', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);
  const visibleNotes = await page.locator('.grow-phasenotes__note:not([hidden])').count();
  const mirrorCount = await page.locator('.grow-phasenotes__mirror').count();
  record('11. wrapper page (no gate at all): note visible immediately, no mirror',
    visibleNotes === 1 && mirrorCount === 0, `visible=${visibleNotes} mirror=${mirrorCount}`);
  await context.close();
}

// 9. Persistence: hide notes, navigate away to the menu and back, visibility
// setting persists; the set filter (page-scoped) resets to "all".
{
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto(BASE + '#/id/L01-co-01', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1200);
  await page.locator('.grow-phasenotes__toggle').click();
  await page.waitForTimeout(150);
  await page.locator('.grow-phasenotes__vis').click();
  await page.waitForTimeout(150);
  const lsValue = await page.evaluate(() => window.localStorage.getItem('grow-phasenotes:visible'));
  record('9a. hide toggle persists to localStorage', lsValue === 'off', `value=${lsValue}`);

  // Select a set before navigating away, to prove it resets.
  const setRadios = page.locator('.grow-phasenotes__opt[data-set]:not([data-set="all"])');
  if (await setRadios.count() >= 1) await setRadios.nth(0).click();
  await page.waitForTimeout(150);

  await page.goto(BASE + '#/', { waitUntil: 'networkidle' });
  await page.waitForTimeout(800);
  await page.goto(BASE + '#/id/L01-co-01', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1200);

  const lsValueAfter = await page.evaluate(() => window.localStorage.getItem('grow-phasenotes:visible'));
  record('9b. visibility setting persists across navigation', lsValueAfter === 'off', `value=${lsValueAfter}`);

  await page.locator('.grow-phasenotes__toggle').click();
  await page.waitForTimeout(150);
  const allRadioChecked = await page.locator('.grow-phasenotes__opt[data-set="all"]').getAttribute('aria-checked');
  record('9c. set filter resets to "all" on fresh page load', allRadioChecked === 'true', `checked=${allRadioChecked}`);

  // Clean up: re-show for subsequent checks in other scripts/sessions.
  await page.locator('.grow-phasenotes__vis').click();
  await page.waitForTimeout(150);
  await context.close();
}

// 12. Reduced motion: toggle grow-mode's real Animations control (post-boot,
// via its own click handler -> toggleMotion() -> html[data-motion="off"]),
// the same way a learner actually triggers it. (addInitScript was tried
// first and discarded: Adapt's own early boot wipes any attribute set on
// documentElement that early, even ones no app code references, so it
// can't be used to simulate this.) Once off, reveal the article and
// confirm notes are fully drawn and static, not missing.
{
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto(BASE + '#/id/L01-co-01', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1200);
  await page.locator('.grow-mode__toggle').click();
  await page.waitForTimeout(150);
  await page.locator('.grow-mode__motion').click();
  await page.waitForTimeout(150);
  const motionAttr = await page.evaluate(() => document.documentElement.getAttribute('data-motion'));
  record('12a. grow-mode Animations toggle sets data-motion=off', motionAttr === 'off', `data-motion=${motionAttr}`);
  await page.keyboard.press('Escape');
  await page.waitForTimeout(150);

  const revealBtn = page.locator('.js-grow-outcomes-reveal');
  for (let i = 0; i < 10; i++) {
    if (!(await revealBtn.isVisible().catch(() => false))) break;
    await revealBtn.click();
    await page.waitForTimeout(400);
  }
  await page.waitForTimeout(1000);
  const visibleNotes = await page.locator('.grow-phasenotes__note:not([hidden])').count();
  const runningAnim = await page.locator('.grow-phasenotes__note .am-run').count();
  record('12b. reduced motion: notes fully present and static (no am-run)',
    visibleNotes >= 3 && runningAnim === 0, `visible=${visibleNotes} am-run=${runningAnim}`);
  await context.close();
}

// 8. Scroll/resize tracking: a note region's bounding rect stays aligned
// with its target article after the page scrolls.
{
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto(BASE + '#/id/L01-co-01', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1200);
  const revealBtn = page.locator('.js-grow-outcomes-reveal');
  for (let i = 0; i < 10; i++) {
    if (!(await revealBtn.isVisible().catch(() => false))) break;
    await revealBtn.click();
    await page.waitForTimeout(400);
  }
  await page.waitForTimeout(1000);

  const before = await page.evaluate(() => {
    const region = document.querySelector('.grow-phasenotes__region');
    const article = document.querySelector('.article[data-adapt-id="L01-a-02"]');
    if (!region || !article) return null;
    const r = region.getBoundingClientRect();
    const a = article.getBoundingClientRect();
    return { regionTop: r.top, articleTop: a.top, diff: Math.abs(r.top - a.top) };
  });
  await page.mouse.wheel(0, 400);
  await page.waitForTimeout(400);
  const after = await page.evaluate(() => {
    const region = document.querySelector('.grow-phasenotes__region');
    const article = document.querySelector('.article[data-adapt-id="L01-a-02"]');
    if (!region || !article) return null;
    const r = region.getBoundingClientRect();
    const a = article.getBoundingClientRect();
    return { regionTop: r.top, articleTop: a.top, diff: Math.abs(r.top - a.top) };
  });
  const trackedAfterScroll = before && after && after.diff < 5 && Math.abs(before.articleTop - after.articleTop) > 50;
  record('8. region stays aligned with its target article after scroll',
    !!trackedAfterScroll, `before=${JSON.stringify(before)} after=${JSON.stringify(after)}`);
  await context.close();
}

await browser.close();
const failed = results.filter(r => !r.ok);
console.log(`\n${results.length - failed.length}/${results.length} checks passed.`);
process.exit(failed.length ? 1 : 0);
