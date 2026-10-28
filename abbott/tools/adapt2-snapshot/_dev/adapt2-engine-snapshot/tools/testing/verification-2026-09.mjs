/**
 * verification-2026-09.mjs
 *
 * Moodle Verification Checklist automation — September 2026 build.
 * Runs LOCAL-AUTO checks from docs/project/moodle-verification-2026-09.md.
 *
 * Usage:
 *   node tools/testing/verification-2026-09.mjs --course=academic-writing-introductory --context=baseline
 *
 * Prerequisites:
 *   1. Course built: courses/_generated/<course>-<context>/ exists
 *   2. Symlink set: src/course -> courses/_generated/<course>-<context>/
 *   3. Server running: grunt server (port 9001)
 *
 * Exit codes:
 *   0 - all checks passed
 *   1 - at least one check failed
 *   2 - no checks selected for the given course (misconfiguration)
 */

import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { parseArgs } from 'util';

// --- CLI args ---
const { values: args } = parseArgs({
  options: {
    course: { type: 'string' },
    context: { type: 'string', default: 'baseline' },
    port: { type: 'string', default: '9001' }
  }
});

const COURSE = args.course;
const CONTEXT = args.context;
const BASE_URL = `http://localhost:${args.port}/`;
const COURSE_PATH = path.resolve(`courses/_generated/${COURSE}-${CONTEXT}`);
const ROOT_PATH = path.resolve('.');

// --- Results accumulator ---
const results = {
  checks: {},         // keyed by check id, e.g., 'A1-2-json'
  consoleErrors: [],
  allPassed: true
};

function report(checkId, passed, detail = '') {
  results.checks[checkId] = { passed, detail };
  if (!passed) results.allPassed = false;
}

// --- JSON loaders ---
function loadJson(filename) {
  return JSON.parse(fs.readFileSync(path.join(COURSE_PATH, 'en', filename), 'utf8'));
}

function loadComponents() {
  return JSON.parse(fs.readFileSync(path.join(COURSE_PATH, 'en', 'components.json'), 'utf8'));
}

// --- Character name lookup from context packs ---

/**
 * Get character name from context pack.
 * Tries course-specific override first, then context default.
 * Returns { name, error } — if error is set, name is null.
 */
function getCharacterName(context, course) {
  const overridePath = path.join(ROOT_PATH, 'content', 'context-packs', context, course, 'context.json');
  const defaultPath = path.join(ROOT_PATH, 'content', 'context-packs', context, 'context.json');

  // Try course-specific override first
  if (fs.existsSync(overridePath)) {
    try {
      const data = JSON.parse(fs.readFileSync(overridePath, 'utf8'));
      if (data.character?.name) {
        return { name: data.character.name, error: null };
      }
    } catch (e) {
      // Fall through to default
    }
  }

  // Try context default
  if (fs.existsSync(defaultPath)) {
    try {
      const data = JSON.parse(fs.readFileSync(defaultPath, 'utf8'));
      if (data.character?.name) {
        return { name: data.character.name, error: null };
      }
    } catch (e) {
      // Fall through to error
    }
  }

  return {
    name: null,
    error: `No character.name found in ${overridePath} or ${defaultPath}`
  };
}

// --- Page resolution ---

/**
 * Find a page by code (e.g., 'L02', 'W-OPEN', 'C-PRE', 'SUMM', 'C-POST', 'W-CLOSE').
 *
 * PK-1 (open-decisions #49, 29 Aug 2026) permits exactly two _id forms:
 *   - Bare: `<code>-co-01` (legacy pilot, academic-writing-introductory)
 *   - Slug-prefixed: `<course-slug>-<code>-co-01` (all courses built after PK-1)
 *
 * The pilot is NOT retrofitted per PK-1; retrofit is tracked as backlog 5.23.
 * This function matches both forms explicitly and fails if not exactly one match.
 *
 * Returns { page, error } — if error is set, page is null.
 */
function findPageByCode(contentObjects, courseSlug, code) {
  // Match exactly the two PK-1 forms
  const bareId = `${code}-co-01`;
  const prefixedId = `${courseSlug}-${code}-co-01`;

  const matches = contentObjects.filter(co =>
    co._type === 'page' && (co._id === bareId || co._id === prefixedId)
  );

  if (matches.length === 0) {
    return { page: null, error: `No page found matching ${bareId} or ${prefixedId}` };
  }
  if (matches.length > 1) {
    const ids = matches.map(m => m._id).join(', ');
    return { page: null, error: `Multiple pages (${matches.length}) matched: ${ids}` };
  }

  return { page: matches[0], error: null };
}

/**
 * Get blocks for a page by properly resolving through articles.json.
 * Returns { blocks, error } — if error is set, blocks is empty.
 */
function getBlocksForPage(articles, blocks, pageId) {
  const pageArticles = articles.filter(a => a._parentId === pageId);

  if (pageArticles.length === 0) {
    return { blocks: [], error: `No articles found for page ${pageId}` };
  }
  if (pageArticles.length > 1) {
    return { blocks: [], error: `Multiple articles (${pageArticles.length}) found for page ${pageId}` };
  }

  const articleId = pageArticles[0]._id;
  const pageBlocks = blocks.filter(b => b._parentId === articleId);

  return { blocks: pageBlocks, error: null };
}

// --- Menu order checks ---

/**
 * Expected structural sequence of page codes.
 * W-OPEN, C-PRE (optional for Advanced), lessons ascending, SUMM, C-POST (optional), W-CLOSE.
 */
const STRUCTURAL_CODES = ['W-OPEN', 'C-PRE', 'SUMM', 'C-POST', 'W-CLOSE'];

function extractPageCode(pageId, courseSlug) {
  // Strip course prefix if present (PK-1 prefixed form)
  let code = pageId;
  if (pageId.startsWith(courseSlug + '-')) {
    code = pageId.slice(courseSlug.length + 1);
  }
  // Strip -co-01 suffix
  code = code.replace(/-co-01$/, '');
  return code;
}

function isLessonCode(code) {
  return /^L\d+$/.test(code);
}

function getLessonNumber(code) {
  const match = code.match(/^L(\d+)$/);
  return match ? parseInt(match[1], 10) : null;
}

/**
 * Check menu order JSON: verify structural sequence from _id patterns.
 * Expected order: W-OPEN, C-PRE (if present), lessons ascending by number, SUMM, C-POST (if present), W-CLOSE.
 */
function checkMenuOrderJson(contentObjects, courseSlug, checkId) {
  const pages = contentObjects.filter(co => co._type === 'page');
  const codes = pages.map(p => extractPageCode(p._id, courseSlug));

  // Classify each code
  const sequence = [];
  for (const code of codes) {
    if (STRUCTURAL_CODES.includes(code)) {
      sequence.push({ type: 'structural', code, order: STRUCTURAL_CODES.indexOf(code) });
    } else if (isLessonCode(code)) {
      sequence.push({ type: 'lesson', code, order: getLessonNumber(code) });
    } else {
      sequence.push({ type: 'unknown', code, order: -1 });
    }
  }

  // Build expected sequence: W-OPEN first, then C-PRE if present, then lessons ascending,
  // then SUMM, then C-POST if present, then W-CLOSE
  const actualSequence = codes.join(' -> ');

  // Check W-OPEN is first
  if (codes[0] !== 'W-OPEN') {
    report(`${checkId}-json`, false, `First page is ${codes[0]}, expected W-OPEN. Sequence: ${actualSequence}`);
    return null;
  }

  // Check W-CLOSE is last
  if (codes[codes.length - 1] !== 'W-CLOSE') {
    report(`${checkId}-json`, false, `Last page is ${codes[codes.length - 1]}, expected W-CLOSE. Sequence: ${actualSequence}`);
    return null;
  }

  // Find lesson range and verify ascending order
  const lessonIndices = [];
  for (let i = 0; i < codes.length; i++) {
    if (isLessonCode(codes[i])) {
      lessonIndices.push(i);
    }
  }

  if (lessonIndices.length > 0) {
    // Verify lessons are contiguous and ascending
    for (let i = 1; i < lessonIndices.length; i++) {
      const prevIdx = lessonIndices[i - 1];
      const currIdx = lessonIndices[i];
      if (currIdx !== prevIdx + 1) {
        report(`${checkId}-json`, false, `Lessons not contiguous at position ${currIdx}. Sequence: ${actualSequence}`);
        return null;
      }
      const prevNum = getLessonNumber(codes[prevIdx]);
      const currNum = getLessonNumber(codes[currIdx]);
      if (currNum <= prevNum) {
        report(`${checkId}-json`, false, `Lessons not ascending: ${codes[prevIdx]} -> ${codes[currIdx]}. Sequence: ${actualSequence}`);
        return null;
      }
    }
  }

  // Verify structural codes appear in correct relative order (those that are present)
  const presentStructural = codes.filter(c => STRUCTURAL_CODES.includes(c));
  const expectedStructuralOrder = STRUCTURAL_CODES.filter(c => presentStructural.includes(c));
  for (let i = 0; i < presentStructural.length; i++) {
    if (presentStructural[i] !== expectedStructuralOrder[i]) {
      report(`${checkId}-json`, false, `Structural pages out of order: expected ${expectedStructuralOrder.join(', ')}, got ${presentStructural.join(', ')}. Sequence: ${actualSequence}`);
      return null;
    }
  }

  // Verify SUMM comes after all lessons
  const summIdx = codes.indexOf('SUMM');
  if (summIdx !== -1 && lessonIndices.length > 0) {
    const lastLessonIdx = lessonIndices[lessonIndices.length - 1];
    if (summIdx <= lastLessonIdx) {
      report(`${checkId}-json`, false, `SUMM at position ${summIdx} appears before last lesson at ${lastLessonIdx}. Sequence: ${actualSequence}`);
      return null;
    }
  }

  report(`${checkId}-json`, true, `${pages.length} pages: ${actualSequence}`);

  // Return displayTitles for DOM comparison
  return {
    expectedTitles: pages.map(p => p.displayTitle),
    pageCount: pages.length
  };
}

/**
 * Check menu order DOM: verify rendered menu titles match contentObjects.json displayTitle order.
 */
async function checkMenuOrderDom(page, checkId, jsonResult) {
  if (!jsonResult) {
    report(`${checkId}-dom`, false, 'Skipped: JSON check failed');
    return;
  }

  await page.goto(BASE_URL, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);

  // Extract menu item titles from DOM
  // Menu items are .menu-item[role="listitem"], headings are [role="heading"] inside
  const menuHeadings = await page.locator('.menu-item [role="heading"]').all();
  const domTitles = [];
  for (const heading of menuHeadings) {
    let text = await heading.textContent();
    // Normalize all whitespace (including NBSP \u00A0) and newlines to single spaces, then trim
    text = text.replace(/[\s\u00A0]+/g, ' ').trim();
    // Strip "Incomplete. " or "Complete. " prefix
    text = text.replace(/^(Incomplete|Complete)\.\s*/i, '').trim();
    domTitles.push(text);
  }

  if (domTitles.length !== jsonResult.expectedTitles.length) {
    report(`${checkId}-dom`, false,
      `Menu item count mismatch: DOM has ${domTitles.length}, JSON has ${jsonResult.expectedTitles.length}`);
    return;
  }

  // Compare each title in order
  for (let i = 0; i < domTitles.length; i++) {
    if (domTitles[i] !== jsonResult.expectedTitles[i]) {
      report(`${checkId}-dom`, false,
        `Mismatch at position ${i}: DOM="${domTitles[i]}", JSON="${jsonResult.expectedTitles[i]}"`);
      return;
    }
  }

  report(`${checkId}-dom`, true, `${domTitles.length} menu items match JSON order`);
}

// --- Character token checks ---

/**
 * Get components belonging to a specific page by traversing the hierarchy:
 * page -> article -> block -> component
 */
function getComponentsForPage(articles, blocks, components, pageId) {
  const pageArticles = articles.filter(a => a._parentId === pageId);
  if (pageArticles.length === 0) {
    return { components: [], error: `No articles found for page ${pageId}` };
  }

  const articleIds = pageArticles.map(a => a._id);
  const pageBlocks = blocks.filter(b => articleIds.includes(b._parentId));
  const blockIds = pageBlocks.map(b => b._id);
  const pageComponents = components.filter(c => blockIds.includes(c._parentId));

  return { components: pageComponents, blocks: pageBlocks, error: null };
}

/**
 * Find ALL lesson pages that have a "Worked example" block.
 * Returns { lessons: [{page, code}], error } — if error is set, lessons is empty.
 */
function findAllWorkedExampleLessons(contentObjects, articles, blocks, courseSlug) {
  const pages = contentObjects.filter(co => co._type === 'page');
  const lessons = [];

  for (const page of pages) {
    const code = extractPageCode(page._id, courseSlug);
    if (!isLessonCode(code)) continue;

    const pageArticles = articles.filter(a => a._parentId === page._id);
    const articleIds = pageArticles.map(a => a._id);
    const pageBlocks = blocks.filter(b => articleIds.includes(b._parentId));

    const hasWorkedExample = pageBlocks.some(b =>
      b.title === 'Worked example' || b.title?.toLowerCase().includes('worked example')
    );

    if (hasWorkedExample) {
      lessons.push({ page, code });
    }
  }

  if (lessons.length === 0) {
    return { lessons: [], error: 'No lesson with a Worked example block found' };
  }

  return { lessons, error: null };
}

/**
 * Search all text fields in a component for a character name.
 * Searches: body, title, instruction, _items[].body, _items[].title, alt text fields.
 */
function componentContainsName(component, name) {
  const searchFields = [
    component.body,
    component.title,
    component.instruction,
    component.displayTitle,
    component._graphic?.alt,
    component._graphic?.attribution
  ];

  // Search _items array if present
  if (Array.isArray(component._items)) {
    for (const item of component._items) {
      searchFields.push(item.body, item.title, item.text, item._graphic?.alt);
    }
  }

  // Search accordion items
  if (Array.isArray(component._accordionItems)) {
    for (const item of component._accordionItems) {
      searchFields.push(item.body, item.title);
    }
  }

  for (const field of searchFields) {
    if (typeof field === 'string' && field.includes(name)) {
      return true;
    }
  }

  return false;
}

/**
 * Check character token in wrapper (A*-9a):
 * JSON: name appears in a component belonging to W-OPEN
 * DOM: name is visible on W-OPEN page
 */
function checkCharacterInWrapperJson(articles, blocks, components, contentObjects, courseSlug, context, course, checkId) {
  const { name, error: nameError } = getCharacterName(context, course);
  if (nameError) {
    report(`${checkId}-json`, false, nameError);
    return null;
  }

  const { page: wOpenPage, error: pageError } = findPageByCode(contentObjects, courseSlug, 'W-OPEN');
  if (pageError) {
    report(`${checkId}-json`, false, pageError);
    return null;
  }

  const { components: pageComps, error: compError } = getComponentsForPage(articles, blocks, components, wOpenPage._id);
  if (compError) {
    report(`${checkId}-json`, false, compError);
    return null;
  }

  const matches = pageComps.filter(c => componentContainsName(c, name));

  if (matches.length > 0) {
    report(`${checkId}-json`, true, `"${name}" found in ${matches.length} W-OPEN components`);
    return { characterName: name, pageId: wOpenPage._id, pageCode: 'W-OPEN' };
  } else {
    report(`${checkId}-json`, false, `"${name}" not found in any W-OPEN component (checked ${pageComps.length} components)`);
    return null;
  }
}

/**
 * Check character token in worked example (A*-9):
 * JSON: name appears in at least one component belonging to ANY lesson with a worked-example block
 * DOM: name is visible on the first matching lesson page
 *
 * Per checklist: "character appears in at least one worked example" — search all, pass if any match.
 */
function checkCharacterInWorkedExampleJson(articles, blocks, components, contentObjects, courseSlug, context, course, checkId) {
  const { name, error: nameError } = getCharacterName(context, course);
  if (nameError) {
    report(`${checkId}-json`, false, nameError);
    return null;
  }

  const { lessons, error: lessonError } = findAllWorkedExampleLessons(contentObjects, articles, blocks, courseSlug);
  if (lessonError) {
    report(`${checkId}-json`, false, lessonError);
    return null;
  }

  // Search all lessons with worked-example blocks
  const matchingLessons = [];
  let totalComponentsChecked = 0;

  for (const { page, code } of lessons) {
    const { components: pageComps, error: compError } = getComponentsForPage(articles, blocks, components, page._id);
    if (compError) continue;

    totalComponentsChecked += pageComps.length;
    const matches = pageComps.filter(c => componentContainsName(c, name));

    if (matches.length > 0) {
      matchingLessons.push({ page, code, matchCount: matches.length });
    }
  }

  if (matchingLessons.length > 0) {
    const lessonList = matchingLessons.map(m => `${m.code}(${m.matchCount})`).join(', ');
    report(`${checkId}-json`, true, `"${name}" found in ${matchingLessons.length} lesson(s): ${lessonList}`);
    // Return first matching lesson for DOM check
    return {
      characterName: name,
      pageId: matchingLessons[0].page._id,
      pageCode: matchingLessons[0].code,
      allMatches: matchingLessons.map(m => m.code)
    };
  } else {
    const lessonList = lessons.map(l => l.code).join(', ');
    report(`${checkId}-json`, false, `"${name}" not found in any worked-example lesson (checked ${lessons.length} lessons: ${lessonList}, ${totalComponentsChecked} components)`);
    return null;
  }
}

/**
 * Check character token DOM: verify name visible on first matching lesson page.
 * Reports all matching lessons from JSON check in detail.
 */
async function checkCharacterTokenDom(page, checkId, jsonResult) {
  if (!jsonResult) {
    report(`${checkId}-dom`, false, 'Skipped: JSON check failed');
    return;
  }

  await page.goto(`${BASE_URL}#/id/${jsonResult.pageId}`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1500);

  const pageText = await page.locator('body').textContent();
  const found = pageText.includes(jsonResult.characterName);

  const allMatchesNote = jsonResult.allMatches?.length > 1
    ? ` (also in: ${jsonResult.allMatches.slice(1).join(', ')})`
    : '';

  if (found) {
    report(`${checkId}-dom`, true, `"${jsonResult.characterName}" found on ${jsonResult.pageCode}${allMatchesNote}`);
  } else {
    report(`${checkId}-dom`, false, `"${jsonResult.characterName}" not found on ${jsonResult.pageCode}`);
  }
}

// --- C1: Block order assertion (LS-2 retrofit) ---

async function checkC1BlockOrderJson(articles, blocks, contentObjects, courseSlug, lessonCode, checkIdBase) {
  const checkId = `${checkIdBase}-json`;

  const { page: targetPage, error: pageError } = findPageByCode(contentObjects, courseSlug, lessonCode);
  if (pageError) {
    report(checkId, false, pageError);
    return null;
  }
  const pageId = targetPage._id;

  const { blocks: pageBlocks, error } = getBlocksForPage(articles, blocks, pageId);

  if (error) {
    report(checkId, false, error);
    return null;
  }

  const orientationIdx = pageBlocks.findIndex(b => b.title === 'Orientation');
  const outcomesIdx = pageBlocks.findIndex(b => b.title === 'Learning outcomes');

  if (orientationIdx === -1) {
    report(checkId, false, 'No block with title "Orientation" found');
    return null;
  }
  if (outcomesIdx === -1) {
    report(checkId, false, 'No block with title "Learning outcomes" found');
    return null;
  }

  const passed = orientationIdx < outcomesIdx;
  const detail = passed
    ? `Orientation at [${orientationIdx}], LOs at [${outcomesIdx}]`
    : `WRONG ORDER: Orientation at [${orientationIdx}], LOs at [${outcomesIdx}]`;

  report(checkId, passed, detail);

  return {
    pageId,
    orientationId: pageBlocks[orientationIdx]._id,
    outcomesId: pageBlocks[outcomesIdx]._id,
    expectedOrder: pageBlocks.map(b => b._id)
  };
}

async function checkC1BlockOrderDom(page, checkIdBase, jsonResult) {
  const checkId = `${checkIdBase}-dom`;

  if (!jsonResult) {
    report(checkId, false, 'Skipped: JSON check failed');
    return;
  }

  await page.goto(`${BASE_URL}#/id/${jsonResult.pageId}`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1500);

  const domBlocks = await page.locator('.block[data-adapt-id]').all();
  const domIds = [];
  for (const block of domBlocks) {
    domIds.push(await block.getAttribute('data-adapt-id'));
  }

  const domOrientationPos = domIds.indexOf(jsonResult.orientationId);
  const domOutcomesPos = domIds.indexOf(jsonResult.outcomesId);

  if (domOrientationPos === -1) {
    report(checkId, false, `Orientation block ${jsonResult.orientationId} not found in DOM`);
    return;
  }
  if (domOutcomesPos === -1) {
    report(checkId, false, `Learning outcomes block ${jsonResult.outcomesId} not found in DOM`);
    return;
  }

  const passed = domOrientationPos < domOutcomesPos;
  const detail = passed
    ? `DOM positions: Orientation=${domOrientationPos}, LOs=${domOutcomesPos}`
    : `WRONG DOM ORDER: Orientation=${domOrientationPos}, LOs=${domOutcomesPos}`;

  report(checkId, passed, detail);
}

// --- Main ---
async function run() {
  console.log('=== VERIFICATION HARNESS ===');
  console.log(`Course: ${COURSE}-${CONTEXT}`);
  console.log(`Server: ${BASE_URL}\n`);

  if (!fs.existsSync(COURSE_PATH)) {
    console.error(`ERROR: Course path not found: ${COURSE_PATH}`);
    process.exit(1);
  }

  const articles = loadJson('articles.json');
  const blocks = loadJson('blocks.json');
  const contentObjects = loadJson('contentObjects.json');
  const components = loadComponents();

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await context.newPage();

  page.on('console', msg => {
    if (msg.type() === 'error') results.consoleErrors.push(msg.text());
  });

  let checksSelected = 0;

  try {
    // --- A1: academic-writing-introductory baseline ---
    if (COURSE === 'academic-writing-introductory') {
      // A1-2: Menu order
      checksSelected += 2;
      console.log('Running A1-2 (menu order)...');
      const menuResult = checkMenuOrderJson(contentObjects, COURSE, 'A1-2');
      await checkMenuOrderDom(page, 'A1-2', menuResult);

      // A1-9: Character in worked example
      // (Wrapper excluded: no context pack supplies W-OPEN content, so wrapper is uncoupled)
      checksSelected += 2;
      console.log('Running A1-9 (character in worked example)...');
      const charResult = checkCharacterInWorkedExampleJson(articles, blocks, components, contentObjects, COURSE, CONTEXT, COURSE, 'A1-9');
      await checkCharacterTokenDom(page, 'A1-9', charResult);

      // C1: Block order (LS-2 retrofit)
      checksSelected += 2;
      console.log('Running C1-intro-L02 (block order)...');
      const c1Result = await checkC1BlockOrderJson(articles, blocks, contentObjects, COURSE, 'L02', 'C1-intro-L02');
      await checkC1BlockOrderDom(page, 'C1-intro-L02', c1Result);
    }

    // --- A2: academic-writing-intermediate baseline ---
    // Note: A2-9 (character check) removed 8 Sep 2026 (R65). Intermediate uses technique-
    // demonstration worked examples without named characters (5.30, ruled 1 Sep 2026).
    if (COURSE === 'academic-writing-intermediate') {
      // A2-2: Menu order
      checksSelected += 2;
      console.log('Running A2-2 (menu order)...');
      const menuResult = checkMenuOrderJson(contentObjects, COURSE, 'A2-2');
      await checkMenuOrderDom(page, 'A2-2', menuResult);

      // C1: Block order
      checksSelected += 2;
      console.log('Running C1-inter-L03 (block order)...');
      const c1Result = await checkC1BlockOrderJson(articles, blocks, contentObjects, COURSE, 'L03', 'C1-inter-L03');
      await checkC1BlockOrderDom(page, 'C1-inter-L03', c1Result);
    }

    // --- A3: academic-writing-advanced baseline ---
    // Note: A3-9 (character check) removed 8 Sep 2026 (R65). Advanced uses technique-
    // demonstration worked examples without named characters (D4 minimal scaffold, L04-B3).
    if (COURSE === 'academic-writing-advanced') {
      // A3-2: Menu order
      checksSelected += 2;
      console.log('Running A3-2 (menu order)...');
      const menuResult = checkMenuOrderJson(contentObjects, COURSE, 'A3-2');
      await checkMenuOrderDom(page, 'A3-2', menuResult);

      // C1: Block order
      checksSelected += 2;
      console.log('Running C1-adv-L04 (block order)...');
      const c1Result = await checkC1BlockOrderJson(articles, blocks, contentObjects, COURSE, 'L04', 'C1-adv-L04');
      await checkC1BlockOrderDom(page, 'C1-adv-L04', c1Result);
    }

    // --- A4: presenting-introductory baseline ---
    if (COURSE === 'presenting-introductory') {
      // A4-2: Menu order
      checksSelected += 2;
      console.log('Running A4-2 (menu order)...');
      const menuResult = checkMenuOrderJson(contentObjects, COURSE, 'A4-2');
      await checkMenuOrderDom(page, 'A4-2', menuResult);

      // A4-9: Character in worked example
      checksSelected += 2;
      console.log('Running A4-9 (character in worked example)...');
      const charResult = checkCharacterInWorkedExampleJson(articles, blocks, components, contentObjects, COURSE, CONTEXT, COURSE, 'A4-9');
      await checkCharacterTokenDom(page, 'A4-9', charResult);
    }

  } catch (error) {
    console.error(`FATAL: ${error.message}`);
    console.error(error.stack);
    results.fatalError = error.message;
  } finally {
    await browser.close();
  }

  // --- Check for no-op runs ---
  if (checksSelected === 0) {
    console.log(`\n0 checks selected for ${COURSE}`);
    console.log('No applicable checks for this course. Exiting with code 2.');
    process.exit(2);
  }

  const checkCount = Object.keys(results.checks).length;
  if (checkCount === 0) {
    console.log('\nERROR: No checks recorded despite selection. Exiting with code 2.');
    process.exit(2);
  }

  // --- Report ---
  console.log('\n' + '='.repeat(60));
  console.log('VERIFICATION REPORT');
  console.log('='.repeat(60) + '\n');

  let passed = 0, failed = 0;
  for (const [checkId, result] of Object.entries(results.checks)) {
    const status = result.passed ? '[PASS]' : '[FAIL]';
    const detail = result.detail ? ` (${result.detail})` : '';
    console.log(`${status} ${checkId}${detail}`);
    if (result.passed) passed++; else failed++;
  }

  if (results.consoleErrors.length > 0) {
    console.log('\n--- Console Errors ---');
    results.consoleErrors.slice(0, 5).forEach(e => console.log(`  ${e}`));
    if (results.consoleErrors.length > 5) {
      console.log(`  ... and ${results.consoleErrors.length - 5} more`);
    }
  }

  console.log('\n' + '='.repeat(60));
  console.log(`SUMMARY: ${passed} passed, ${failed} failed`);
  console.log('='.repeat(60) + '\n');

  if (results.fatalError) {
    console.log(`FATAL ERROR: ${results.fatalError}`);
    process.exit(1);
  }

  process.exit(failed > 0 ? 1 : 0);
}

run();
