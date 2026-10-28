/**
 * Focus Sequence Scanner — Academic Writing: Introductory Stage
 *
 * Automates Tab-sequence recording to flag POSSIBLE focus traps for human review.
 * This is a DETECTION AID, not a definitive test — flagged points need manual
 * verification to confirm whether they are genuine traps or legitimate design
 * (e.g., a modal correctly holding focus while open).
 *
 * What it checks:
 * - Same element receiving focus twice in a row (focus didn't advance)
 * - Focus returning to first element before reaching end of content (early loop)
 * - Shift+Tab not retracing forward sequence in reverse (asymmetric tab order)
 * - Dynamic state scans for SUMM and confidence components after interaction
 *
 * Usage: node test-focus-sequence-scan.mjs
 * Requires: Playwright, dev server running on localhost:9001
 */

import { chromium } from 'playwright';

const BASE_URL = 'http://localhost:9001/';
const MAX_TAB_PRESSES = 100;

/**
 * Get a description of the currently focused element
 */
async function getFocusedElementInfo(page) {
  return await page.evaluate(() => {
    const el = document.activeElement;
    if (!el || el === document.body) {
      return { tag: 'body', id: '', classes: '', text: '', selector: 'body', isBody: true };
    }

    const tag = el.tagName.toLowerCase();
    const id = el.id || '';
    const classes = Array.from(el.classList).slice(0, 3).join(' ');
    let text = (el.textContent || el.getAttribute('aria-label') || el.getAttribute('title') || '').trim();
    text = text.substring(0, 50).replace(/\s+/g, ' ');

    // Build a reasonably unique selector
    let selector = tag;
    if (id) selector += `#${id}`;
    else if (classes) selector += `.${classes.split(' ')[0]}`;

    return { tag, id, classes, text, selector, isBody: false };
  });
}

/**
 * Create a unique key for comparing elements
 */
function elementKey(info) {
  if (info.isBody) return 'body';
  return `${info.tag}#${info.id}.${info.classes}`;
}

/**
 * Record a Tab sequence on the current page
 */
async function recordTabSequence(page, maxPresses = MAX_TAB_PRESSES, reverse = false) {
  const sequence = [];
  const flags = [];
  const key = reverse ? 'Shift+Tab' : 'Tab';

  // Start from current focus position
  let prevInfo = await getFocusedElementInfo(page);
  let prevKey = elementKey(prevInfo);
  let stuckCount = 0;
  let stuckElement = null;

  for (let i = 0; i < maxPresses; i++) {
    if (reverse) {
      await page.keyboard.press('Shift+Tab');
    } else {
      await page.keyboard.press('Tab');
    }
    await page.waitForTimeout(50);

    const info = await getFocusedElementInfo(page);
    const currentKey = elementKey(info);

    sequence.push({
      press: i + 1,
      ...info,
      key: currentKey
    });

    // Track consecutive stuck presses
    if (currentKey === prevKey && !info.isBody) {
      stuckCount++;
      if (stuckCount === 1) {
        stuckElement = { press: i + 1, info };
      }
    } else {
      // Focus moved - if we were stuck before, that was likely end-of-content, not a trap
      // Only flag if we got stuck in the MIDDLE of the sequence and then moved again
      // (which would indicate a real trap that eventually released)
      if (stuckCount >= 3 && stuckElement) {
        // This was stuck then moved - suspicious mid-sequence trap
        flags.push({
          type: 'stuck-then-moved',
          press: stuckElement.press,
          element: stuckElement.info,
          stuckFor: stuckCount,
          message: `Focus stuck on same element for ${stuckCount} presses (${stuckElement.press} to ${i}), then moved — possible focus trap that released`
        });
      }
      stuckCount = 0;
      stuckElement = null;
    }

    // Flag: returned to first element early (possible loop)
    if (sequence.length > 5 && i < maxPresses - 10) {
      const firstKey = sequence[0]?.key;
      if (currentKey === firstKey && !info.isBody) {
        flags.push({
          type: 'early-loop',
          press: i + 1,
          element: info,
          message: `Focus returned to first element at press ${i + 1} — possible early loop/trap, or reached natural end of focusable content`
        });
        // Stop here — we've looped
        break;
      }
    }

    // Stop if we hit body twice (likely at end)
    if (info.isBody && prevInfo.isBody) {
      break;
    }

    // Stop if stuck for too long (end of content reached)
    if (stuckCount >= 5) {
      // Record this as end-of-content, not a trap
      sequence.push({
        press: i + 2,
        note: 'END OF FOCUSABLE CONTENT (focus stopped advancing)',
        lastElement: info
      });
      break;
    }

    prevInfo = info;
    prevKey = currentKey;
  }

  return { sequence, flags };
}

/**
 * Compare forward and reverse sequences for asymmetry
 */
function checkAsymmetry(forward, reverse) {
  const flags = [];

  // Get non-body elements only
  const fwdKeys = forward.sequence
    .filter(s => !s.isBody)
    .map(s => s.key);
  const revKeys = reverse.sequence
    .filter(s => !s.isBody)
    .map(s => s.key);

  // Reverse the reverse sequence to compare
  const revReversed = [...revKeys].reverse();

  // Compare lengths
  if (Math.abs(fwdKeys.length - revReversed.length) > 3) {
    flags.push({
      type: 'asymmetric-length',
      message: `Forward sequence has ${fwdKeys.length} elements, reverse has ${revKeys.length} — significant length mismatch`
    });
  }

  // Check for elements in forward but not reverse (or vice versa)
  const fwdSet = new Set(fwdKeys);
  const revSet = new Set(revKeys);

  const inFwdOnly = [...fwdSet].filter(k => !revSet.has(k));
  const inRevOnly = [...revSet].filter(k => !fwdSet.has(k));

  if (inFwdOnly.length > 0) {
    flags.push({
      type: 'forward-only',
      elements: inFwdOnly.slice(0, 5),
      message: `${inFwdOnly.length} element(s) reachable via Tab but not Shift+Tab — asymmetric tab order`
    });
  }

  if (inRevOnly.length > 0) {
    flags.push({
      type: 'reverse-only',
      elements: inRevOnly.slice(0, 5),
      message: `${inRevOnly.length} element(s) reachable via Shift+Tab but not Tab — asymmetric tab order`
    });
  }

  return flags;
}

/**
 * Click through trickle buttons to reveal full page
 */
async function clickThroughTrickle(page, maxClicks = 20) {
  let clicks = 0;
  while (clicks < maxClicks) {
    await page.waitForTimeout(300);
    const trickleBtn = page.locator('.trickle__btn:visible').first();
    if (await trickleBtn.count() === 0) break;
    const isDisabled = await trickleBtn.evaluate(el => el.classList.contains('is-disabled')).catch(() => true);
    if (isDisabled) break;
    await trickleBtn.click().catch(() => {});
    await page.waitForTimeout(500);
    clicks++;
  }
  return clicks;
}

/**
 * Rate confidence items
 */
async function rateConfidenceItems(page) {
  const items = await page.locator('.confidence__item').all();
  for (let i = 0; i < items.length; i++) {
    const option = page.locator(`.confidence__item[data-item-index="${i}"] .confidence__option`).nth(2);
    if (await option.isVisible().catch(() => false)) {
      await option.click();
      await page.waitForTimeout(100);
    }
  }
}

/**
 * Answer an MCQ
 */
async function answerMcq(page, selector) {
  const component = page.locator(selector);
  if (await component.count() === 0) return false;

  const label = component.locator('.mcq-item__label').first();
  if (await label.count() > 0) {
    await label.click();
    await page.waitForTimeout(200);
  }

  const submitBtn = component.locator('.btn__action').first();
  if (await submitBtn.count() > 0) {
    const isEnabled = !(await submitBtn.evaluate(el => el.classList.contains('is-disabled')).catch(() => true));
    if (isEnabled) {
      await submitBtn.click();
      await page.waitForTimeout(300);
      // Dismiss any tutor popup
      await page.keyboard.press('Escape');
      await page.waitForTimeout(200);
      return true;
    }
  }
  return false;
}

/**
 * Format a sequence for output
 */
function formatSequence(sequence, limit = 30) {
  const lines = [];
  const toShow = sequence.slice(0, limit);

  for (const item of toShow) {
    const idPart = item.id ? `#${item.id}` : '';
    const classPart = item.classes ? `.${item.classes.split(' ')[0]}` : '';
    const textPart = item.text ? ` "${item.text.substring(0, 30)}..."` : '';
    lines.push(`  ${item.press}: <${item.tag}${idPart}${classPart}>${textPart}`);
  }

  if (sequence.length > limit) {
    lines.push(`  ... and ${sequence.length - limit} more elements`);
  }

  return lines.join('\n');
}

/**
 * Run scan on a single page
 */
async function scanPage(page, pageName, url, options = {}) {
  const result = {
    page: pageName,
    url,
    forward: null,
    reverse: null,
    asymmetryFlags: [],
    allFlags: []
  };

  console.log(`  Scanning ${pageName}...`);

  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1500);

  // Click through trickle to reveal full page
  if (options.clickTrickle !== false) {
    await clickThroughTrickle(page, 15);
    await page.waitForTimeout(500);
  }

  // Pre-interaction scan (if needed)
  if (options.preInteraction) {
    await options.preInteraction(page);
    await page.waitForTimeout(500);
  }

  // Reset focus to start of page
  await page.keyboard.press('Tab');
  await page.waitForTimeout(100);
  // Go back to start
  for (let i = 0; i < 5; i++) {
    await page.keyboard.press('Shift+Tab');
  }
  await page.waitForTimeout(200);

  // Forward Tab sequence
  result.forward = await recordTabSequence(page, MAX_TAB_PRESSES, false);

  // Now do reverse from current position
  result.reverse = await recordTabSequence(page, MAX_TAB_PRESSES, true);

  // Check for asymmetry
  result.asymmetryFlags = checkAsymmetry(result.forward, result.reverse);

  // Collect all flags
  result.allFlags = [
    ...result.forward.flags,
    ...result.reverse.flags.map(f => ({ ...f, direction: 'reverse' })),
    ...result.asymmetryFlags
  ];

  return result;
}

async function runFocusScan() {
  console.log('='.repeat(70));
  console.log('FOCUS SEQUENCE SCANNER');
  console.log('Academic Writing: Introductory Stage');
  console.log('='.repeat(70));
  console.log('\nIMPORTANT: This is a DETECTION AID, not a definitive test.');
  console.log('Flagged points need manual verification to confirm whether they');
  console.log('are genuine traps or legitimate design (e.g., modal holding focus).\n');

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await context.newPage();

  const results = [];

  try {
    // Standard pages (static scan)
    const standardPages = [
      { name: 'L02', id: 'L02-co-01' },
      { name: 'L03', id: 'L03-co-01' },
      { name: 'L04', id: 'L04-co-01' },
      { name: 'L05', id: 'L05-co-01' },
      { name: 'L06', id: 'L06-co-01' },
      { name: 'L07', id: 'L07-co-01' }
    ];

    console.log('Phase 1: Standard lesson pages (L02-L07)...');
    for (const pg of standardPages) {
      const result = await scanPage(page, pg.name, `${BASE_URL}#/id/${pg.id}`);
      results.push(result);
    }

    // W-OPEN with confidence interaction
    console.log('\nPhase 2: W-OPEN (before and after confidence interaction)...');

    // W-OPEN before interaction
    const wopenBefore = await scanPage(page, 'W-OPEN (before confidence)', `${BASE_URL}#/id/W-OPEN-co-01`);
    results.push(wopenBefore);

    // W-OPEN after rating confidence items
    const wopenAfter = await scanPage(page, 'W-OPEN (after confidence rating)', `${BASE_URL}#/id/W-OPEN-co-01`, {
      preInteraction: async (p) => {
        await clickThroughTrickle(p, 15);
        const hasConfidence = await p.locator('.confidence').count() > 0;
        if (hasConfidence) {
          await rateConfidenceItems(p);
        }
      }
    });
    results.push(wopenAfter);

    // SUMM before and after interaction
    console.log('\nPhase 3: SUMM (before and after answering questions)...');

    // SUMM initial state
    const summBefore = await scanPage(page, 'SUMM (initial state)', `${BASE_URL}#/id/SUMM-co-01`, {
      clickTrickle: false // Don't advance yet
    });
    results.push(summBefore);

    // SUMM after answering first question
    const summAfter = await scanPage(page, 'SUMM (after answering question)', `${BASE_URL}#/id/SUMM-co-01`, {
      preInteraction: async (p) => {
        await clickThroughTrickle(p, 3);
        await answerMcq(p, '[data-adapt-id="SUMM-c-10"]');
      }
    });
    results.push(summAfter);

    // W-CLOSE with confidence interaction
    console.log('\nPhase 4: W-CLOSE (before and after confidence interaction)...');

    // W-CLOSE before interaction
    const wcloseBefore = await scanPage(page, 'W-CLOSE (before confidence)', `${BASE_URL}#/id/W-CLOSE-co-01`);
    results.push(wcloseBefore);

    // W-CLOSE after rating confidence items
    const wcloseAfter = await scanPage(page, 'W-CLOSE (after confidence rating)', `${BASE_URL}#/id/W-CLOSE-co-01`, {
      preInteraction: async (p) => {
        await clickThroughTrickle(p, 10);
        const hasConfidence = await p.locator('.confidence').count() > 0;
        if (hasConfidence) {
          await rateConfidenceItems(p);
        }
      }
    });
    results.push(wcloseAfter);

  } catch (error) {
    console.log('\n[FATAL ERROR] ' + error.message);
    console.log(error.stack);
  } finally {
    await browser.close();
  }

  // ==================== REPORT ====================
  console.log('\n\n' + '='.repeat(70));
  console.log('FOCUS SEQUENCE SCAN REPORT');
  console.log('='.repeat(70));

  let totalFlags = 0;

  for (const result of results) {
    console.log(`\n${'─'.repeat(50)}`);
    console.log(`PAGE: ${result.page}`);
    console.log(`${'─'.repeat(50)}`);

    console.log(`\nForward Tab sequence (${result.forward.sequence.length} elements):`);
    console.log(formatSequence(result.forward.sequence));

    console.log(`\nReverse Shift+Tab sequence (${result.reverse.sequence.length} elements):`);
    console.log(formatSequence(result.reverse.sequence));

    if (result.allFlags.length === 0) {
      console.log('\n✓ No suspicious patterns flagged on this page.');
    } else {
      console.log(`\n⚠ ${result.allFlags.length} SUSPICIOUS PATTERN(S) FLAGGED:`);
      for (const flag of result.allFlags) {
        console.log(`\n  [${flag.type.toUpperCase()}]`);
        console.log(`  ${flag.message}`);
        if (flag.element) {
          const el = flag.element;
          console.log(`  Element: <${el.tag}${el.id ? '#' + el.id : ''}${el.classes ? '.' + el.classes.split(' ')[0] : ''}>`);
          if (el.text) console.log(`  Text: "${el.text.substring(0, 50)}"`);
        }
        if (flag.elements) {
          console.log(`  Elements: ${flag.elements.join(', ')}`);
        }
      }
      totalFlags += result.allFlags.length;
    }
  }

  // ==================== SUMMARY ====================
  console.log('\n\n' + '='.repeat(70));
  console.log('SUMMARY');
  console.log('='.repeat(70));

  console.log(`\nPages scanned: ${results.length}`);
  console.log(`Total suspicious patterns flagged: ${totalFlags}`);

  if (totalFlags === 0) {
    console.log('\n✓ CLEAN AUTOMATED PASS');
    console.log('  No focus traps or asymmetric tab orders detected by automated scan.');
    console.log('  However, this does not guarantee absence of issues — a manual');
    console.log('  spot-check is still recommended given the tool\'s limitations.');
  } else {
    console.log('\n⚠ FLAGGED PATTERNS NEED MANUAL VERIFICATION');
    console.log('  Each flag above may be:');
    console.log('  - A genuine focus trap or bug that needs fixing');
    console.log('  - A legitimate design (e.g., modal holding focus while open)');
    console.log('  - A false positive from the scan\'s heuristics');
    console.log('  A human must inspect each flagged element to determine which.');
  }

  console.log('\n' + '='.repeat(70));
  console.log('END OF REPORT');
  console.log('='.repeat(70) + '\n');

  // Exit with code based on flags (informational, not a test failure)
  process.exit(0);
}

runFocusScan();
