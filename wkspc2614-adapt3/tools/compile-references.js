#!/usr/bin/env node
/**
 * compile-references.js
 *
 * Build-time compiler for a course's references components:
 *   - each lesson's "Lesson Sources" (_skeletonKey: "lesson-references")
 *   - the course-level "Course Sources" (_skeletonKey: "course-references",
 *     the wra-02_wrapper-close page's end-of-course sources list)
 *
 * Reads the course's crs-04_lesson-map gate record's sourceSections[] -
 * structured data, already human-confirmed at that gate - and writes the
 * fully-formatted LSP-1 pointer-form citation(s) into the matching
 * references component's _items[] in en/components.json.
 *
 * This is deliberately narrower than docs/authoring/component-specs/
 * references.md's RF-2 ("Not a runtime-scanned aggregation; each reference
 * is hand-authored"): this tool only mechanises the one case where the
 * source text already exists as structured, gate-confirmed fields
 * (sourceSections) and the "authoring" step is pure formatting, not
 * judgement.
 *
 * Multi-section convention (observed precedent,
 * understanding-learning-assessment-feedback-introductory, confirmed
 * against its live _items at both levels): sourceSections citing the same
 * chapter collapse into ONE _items entry spanning that chapter's full page
 * range, not one entry per section. At course level this merge runs across
 * every lesson's sourceSections, not just one lesson's (confirmed: that
 * course's L01-L05 chapter-3 ranges 28-34/35-41/41-42/42-43 merge into the
 * course-level entry's 28-43). Chapters are then ordered ascending by
 * chapter number, at both levels.
 *
 * Source bibliographic metadata (title/authors/year) is NOT present in
 * sourceSections, nor in source-kb/source-maps/*.json (chunk-level locators
 * only) - there is no bibliography registry anywhere in the repo. BOOK_META
 * below hardcodes it, keyed by sourceId. The only sourceId in use repo-wide
 * today is book/excelling-at-university-2026 (confirmed by grep across every
 * course-design_*.json). Extend BOOK_META if a second source is ever added;
 * this tool fails loudly, not silently, on an unknown sourceId.
 *
 * Blocks are found by _skeletonKey, not by a hardcoded id convention
 * (stable across every course model version seen - v1's L0N-b-55/60 and
 * v2's L0N-b-80 both carry "lesson-references"). A lesson block's lesson key
 * is read off its id's leading L\d+ prefix and matched case-insensitively
 * against crs-04's lesson.key (which is uppercase in some courses, lowercase
 * in others).
 *
 * Real hrefs: per-chapter EBSCO eBook reader deep links (7 Nov 2026), pasted
 * by the user directly from the authenticated reader's own table of contents
 * (customer "5swjy4", recordId "jh27fa6lnj", one section id "lp_N" per
 * chapter). Cross-checked against canon
 * (wkspc2601-library/canon/cite/*chapter.record.json): every chapter's title
 * in the pasted TOC matches that chapter's canon csl.title exactly for
 * chapters 2-14 (13/13), and the chapter numbering matches the DOI-suffix
 * numbering already confirmed there (e.g. chapter 10, DOI suffix -10, is
 * "Academic integrity and referencing" in both canon and the pasted TOC).
 * CHAPTER_SECTIONS below is that verified map. Chapter 1 ("Introduction") has
 * a section id (lp_1) but no DOI/canon chapter record - unused today, kept
 * for completeness. If a cited chapter number is ever missing from this map,
 * chapterHref() falls back to the book-level Cardiff Met permalink (kind:
 * "ebsco-plink", wkspc2601-library/canon/cite/excelling-at-university-2026
 * -digital.record.json, from book-ebsco-2026-09-28.ris) rather than failing.
 *
 * Separately, the user also pasted a full per-chapter Cardiff Met MetSearch
 * permalink list (7 Nov 2026, from MetSearch's own record page - each URL is
 * of the form https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/
 * 1kul06t/cdi_proquest_ebookcentralchapters_32353950_<n>_<m>). Same
 * cross-check performed and passed (13/13 chapters 2-14, title-exact against
 * canon). CHAPTER_METSEARCH below is that verified map - a genuinely
 * per-chapter, institution-stable discovery-layer link, distinct from the
 * EBSCO reader link (confirmed: not simply "the same permalink" as earlier
 * assumed - canon itself had already flagged no Primo/MetSearch link was
 * resolvable from data in-repo, until the user supplied this directly).
 * CHAPTER_METSEARCH is not wired into chapterHref()/_items yet: it is
 * recorded here as the real fallback data for the redirect-indirection
 * design discussed with the user (one shared redirect file/config across all
 * SCORM packages, primary = EBSCO reader link, fallback = MetSearch
 * permalink), pending a hosting location for that redirect service.
 *
 * Separately, cross-referenced the canon citation records
 * (wkspc2601-library/canon/cite/*.csl.json) against source-kb's
 * book-excelling-at-university-2026.json chapter-number map by title match
 * (13/13 chapters 2-14, exact): each chapter's DOI suffix equals its chapter
 * number, e.g. chapter 10 ("Academic integrity and referencing") is
 * 10.4324/9781003217527-10 - confirmed live-resolving via doi.org. Real and
 * resolving, but not used as href - kept in BOOK_META only as a documented
 * fallback, in case a chapter's section link ever needs replacing.
 *
 * Existing hrefs/permalinks are preserved by matching the new item's
 * compiled title text against the current _items[]  - except this tool's
 * own old placeholder ('#'), which is always upgraded to the real href, so
 * a href filled in by hand or via export-references.js --import survives a
 * re-run, as long as the compiled wording hasn't changed. A dropped item
 * (old title with no match among the newly compiled ones) is reported,
 * never silently discarded.
 *
 * Usage:
 *   node tools/compile-references.js --course=<slug> [--lesson=L01] [--course-only] [--lessons-only] [--dry-run] [--json]
 */
'use strict';

const fs = require('fs');
const path = require('path');
const { resolveCourse } = require('./lib/course-resolve');

const ROOT = path.resolve(__dirname, '..');

// Per-chapter EBSCO eBook reader section ids, verified against canon chapter
// titles (see header comment). customer/recordId identify the Cardiff Met
// EBSCO reader copy of this specific book.
const EBSCO_READER = { customer: '5swjy4', recordId: 'jh27fa6lnj' };
const CHAPTER_SECTIONS = {
  1: 'lp_1',
  2: 'lp_9',
  3: 'lp_27',
  4: 'lp_44',
  5: 'lp_59',
  6: 'lp_75',
  7: 'lp_95',
  8: 'lp_113',
  9: 'lp_135',
  10: 'lp_184',
  11: 'lp_200',
  12: 'lp_220',
  13: 'lp_231',
  14: 'lp_246'
};

// Per-chapter Cardiff Met MetSearch permalinks, verified against canon
// chapter titles (see header comment). Not yet consumed by chapterHref() -
// recorded as the real fallback-link data for the redirect-service design
// discussed with the user, pending a hosting decision.
const CHAPTER_METSEARCH = {
  1: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_11_16',
  2: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_12_24',
  3: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_13_42',
  4: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_14_59',
  5: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_15_74',
  6: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_16_90',
  7: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_17_110',
  8: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_18_128',
  9: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_19_150',
  10: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_20_199',
  11: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_21_215',
  12: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_22_235',
  13: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_23_246',
  14: 'https://metsearch.cardiffmet.ac.uk/permalink/44WHELF_CMU/1kul06t/cdi_proquest_ebookcentralchapters_32353950_24_261'
};

const BOOK_META = {
  'book/excelling-at-university-2026': {
    title: 'Excelling at University',
    authors: 'Dennis and Abbott',
    year: 2026,
    kind: 'book',
    // Book-level fallback only (used when a chapter has no entry in
    // CHAPTER_SECTIONS) - the institution-resolved Cardiff Met permalink via
    // Cardiff Met's EBSCO subscription.
    cardiffMetPermalink: 'https://research.ebsco.com/plink/23dadf12-9e28-322d-a9f7-83d36020980e',
    // Documented fallback only (see header comment) - not used as href.
    doiPrefix: '10.4324/9781003217527'
  }
};

function chapterHref(meta, chapter) {
  const section = CHAPTER_SECTIONS[chapter];
  if (!section) return meta.cardiffMetPermalink;
  return `https://research.ebsco.com/c/${EBSCO_READER.customer}/ebook-viewer/pdf/${EBSCO_READER.recordId}/section/${section}`;
}

function parseArgs() {
  const args = { course: null, lesson: null, courseOnly: false, lessonsOnly: false, dryRun: false, json: false };
  for (const raw of process.argv.slice(2)) {
    if (raw.startsWith('--course=')) args.course = raw.slice('--course='.length);
    else if (raw.startsWith('--lesson=')) args.lesson = raw.slice('--lesson='.length);
    else if (raw === '--course-only') args.courseOnly = true;
    else if (raw === '--lessons-only') args.lessonsOnly = true;
    else if (raw === '--dry-run') args.dryRun = true;
    else if (raw === '--json') args.json = true;
    else {
      console.error(`Unknown argument: ${raw}`);
      console.error('Usage: node tools/compile-references.js --course=<slug> [--lesson=L01] [--course-only] [--lessons-only] [--dry-run] [--json]');
      process.exit(1);
    }
  }
  if (!args.course) {
    console.error('Usage: node tools/compile-references.js --course=<slug> [--lesson=L01] [--course-only] [--lessons-only] [--dry-run] [--json]');
    process.exit(1);
  }
  if (args.courseOnly && args.lessonsOnly) {
    console.error('--course-only and --lessons-only are mutually exclusive.');
    process.exit(1);
  }
  return args;
}

function pageRangePhrase(min, max) {
  return min === max ? `page ${min}` : `pages ${min} to ${max}`;
}

function parsePageNumbers(pagesStr) {
  const nums = (pagesStr || '').match(/\d+/g);
  if (!nums) throw new Error(`sourceSection pages field has no numbers: "${pagesStr}"`);
  return nums.map(n => parseInt(n, 10));
}

/**
 * Group a set of sourceSections by chapter, merge each chapter's page
 * numbers into one min-max range, and format the LSP-1 citation string.
 * Returns items in ascending chapter order. Used for both one lesson's
 * sourceSections and the flattened union of every lesson's (course level).
 */
function compileItems(sourceSections) {
  const byChapter = new Map(); // chapter -> { chapterTitle, sourceId, nums: [] }
  for (const s of sourceSections) {
    if (!byChapter.has(s.chapter)) {
      byChapter.set(s.chapter, { chapterTitle: s.chapterTitle, sourceId: s.sourceId, nums: [] });
    }
    byChapter.get(s.chapter).nums.push(...parsePageNumbers(s.pages));
  }

  const chapters = [...byChapter.keys()].sort((a, b) => a - b);
  return chapters.map(chapter => {
    const { chapterTitle, sourceId, nums } = byChapter.get(chapter);
    const meta = BOOK_META[sourceId];
    if (!meta) throw new Error(`Unknown sourceId "${sourceId}" - add it to BOOK_META in tools/compile-references.js before compiling.`);
    const min = Math.min(...nums);
    const max = Math.max(...nums);
    // Strip any embedded straight single-quote marks from chapterTitle before
    // wrapping it in the citation's own quotes, so a title like "Defining
    // 'learning' at university" (seen once, ch3 of
    // understanding-learning-assessment-feedback-introductory) does not nest
    // quote marks. Matches the existing hand-authored precedent for that
    // exact chapter, which drops them the same way.
    const cleanChapterTitle = chapterTitle.replace(/'/g, '');
    const title = `See ${pageRangePhrase(min, max)} of Chapter ${chapter}, '${cleanChapterTitle}', of ${meta.title} by ${meta.authors} (${meta.year}).`;
    return { title, href: chapterHref(meta, chapter), type: meta.kind, permalink: '' };
  });
}

function findLessonReferenceBlocks(blocks) {
  return blocks.filter(b => b._skeletonKey === 'lesson-references');
}

function findCourseReferenceBlock(blocks) {
  return blocks.find(b => b._skeletonKey === 'course-references') || null;
}

function lessonKeyFromBlockId(blockId) {
  const m = blockId.match(/^(L\d+)-/i);
  return m ? m[1] : null;
}

// hrefs this tool itself can produce as a fallback, not a hand-set final
// value - always upgradable by a fresher compile, never preserved as "prior".
const PLACEHOLDER_HREFS = new Set(['#', ...Object.values(BOOK_META).map(m => m.cardiffMetPermalink)]);

/**
 * Compile one references component's new _items[] from a set of
 * sourceSections, preserving any hand-set (non-placeholder) href/permalink by
 * title match, and report what changed.
 */
function compileComponent(comp, sourceSections, label) {
  const compiled = compileItems(sourceSections);
  const existingByTitle = new Map((comp._items || []).map(it => [it.title, it]));
  const newItems = compiled.map(it => {
    const prior = existingByTitle.get(it.title);
    if (prior && prior.href && !PLACEHOLDER_HREFS.has(prior.href)) {
      return { ...it, href: prior.href, permalink: prior.permalink };
    }
    return it;
  });
  const droppedTitles = (comp._items || []).map(it => it.title).filter(t => !compiled.some(c => c.title === t));
  const changed = JSON.stringify(comp._items || []) !== JSON.stringify(newItems);
  return { label, componentId: comp._id, changed, dropped: droppedTitles, items: newItems, apply: () => { comp._items = newItems; } };
}

function main() {
  const args = parseArgs();
  const resolved = resolveCourse(args.course, ['courses', 'courses/_generated']);
  if (!resolved.found) {
    console.error(`Course not found for slug "${args.course}". Checked:\n  ${resolved.checked.join('\n  ')}`);
    process.exit(1);
  }
  resolved.warnings.forEach(w => console.error(`WARNING: ${w}`));
  if (!resolved.enDir) { console.error(`No en/ directory under ${resolved.courseDir}`); process.exit(1); }
  if (!resolved.courseDesignPath) { console.error(`No course-design file under ${resolved.courseDir}`); process.exit(1); }

  const design = JSON.parse(fs.readFileSync(resolved.courseDesignPath, 'utf8'));
  const gate = (design.gates || []).find(g => g.gateId === 'crs-04_lesson-map');
  if (!gate || !gate.records || !gate.records.length) {
    console.error('No crs-04_lesson-map gate record found - nothing to compile from.');
    process.exit(1);
  }
  const lessons = gate.records[gate.records.length - 1].decidedValue.lessons || [];
  const lessonByKey = new Map(lessons.map(l => [l.key.toUpperCase(), l]));

  const blocksPath = path.join(resolved.enDir, 'blocks.json');
  const componentsPath = path.join(resolved.enDir, 'components.json');
  const blocks = JSON.parse(fs.readFileSync(blocksPath, 'utf8'));
  const components = JSON.parse(fs.readFileSync(componentsPath, 'utf8'));

  const results = [];

  if (!args.courseOnly) {
    let refBlocks = findLessonReferenceBlocks(blocks);
    if (args.lesson) refBlocks = refBlocks.filter(b => lessonKeyFromBlockId(b._id)?.toUpperCase() === args.lesson.toUpperCase());

    for (const block of refBlocks) {
      const lessonKey = lessonKeyFromBlockId(block._id);
      if (!lessonKey) { results.push({ blockId: block._id, error: 'could not read lesson key from block id' }); continue; }
      const lesson = lessonByKey.get(lessonKey.toUpperCase());
      if (!lesson) { results.push({ blockId: block._id, lessonKey, error: `no crs-04 lesson entry for key "${lessonKey}"` }); continue; }
      if (!lesson.sourceSections || !lesson.sourceSections.length) { results.push({ blockId: block._id, lessonKey, error: 'lesson has no sourceSections' }); continue; }

      const comp = components.find(c => c._parentId === block._id && c._component === 'references');
      if (!comp) { results.push({ blockId: block._id, lessonKey, error: 'no references component under this block' }); continue; }

      let r;
      try { r = compileComponent(comp, lesson.sourceSections, `lesson ${lessonKey}`); }
      catch (e) { results.push({ blockId: block._id, lessonKey, error: e.message }); continue; }

      results.push({ blockId: block._id, lessonKey, ...r });
      if (r.changed && !args.dryRun) r.apply();
    }
  }

  if (!args.lessonsOnly && !args.lesson) {
    const courseBlock = findCourseReferenceBlock(blocks);
    if (!courseBlock) {
      results.push({ blockId: null, label: 'course', error: 'no course-references block found in this course' });
    } else {
      const comp = components.find(c => c._parentId === courseBlock._id && c._component === 'references');
      if (!comp) {
        results.push({ blockId: courseBlock._id, label: 'course', error: 'no references component under the course-references block' });
      } else {
        const allSections = lessons.flatMap(l => l.sourceSections || []);
        if (!allSections.length) {
          results.push({ blockId: courseBlock._id, label: 'course', error: 'no lesson has sourceSections yet - nothing to aggregate' });
        } else {
          let r;
          try { r = compileComponent(comp, allSections, 'course'); }
          catch (e) { results.push({ blockId: courseBlock._id, label: 'course', error: e.message }); }
          if (r) {
            results.push({ blockId: courseBlock._id, ...r });
            if (r.changed && !args.dryRun) r.apply();
          }
        }
      }
    }
  }

  if (!args.dryRun && results.some(r => r.changed)) {
    fs.writeFileSync(componentsPath, JSON.stringify(components, null, 2) + '\n');
  }

  if (args.json) {
    console.log(JSON.stringify({ course: args.course, dryRun: args.dryRun, results }, null, 2));
  } else {
    console.log(`compile-references --course=${args.course}${args.dryRun ? ' (dry run)' : ''}`);
    console.log('='.repeat(60));
    for (const r of results) {
      const label = r.lessonKey ? `lesson ${r.lessonKey}` : (r.label || '?');
      if (r.error) { console.log(`${r.blockId || '(no block)'} (${label}): SKIP - ${r.error}`); continue; }
      console.log(`${r.componentId} (${label}): ${r.changed ? (args.dryRun ? 'WOULD CHANGE' : 'WRITTEN') : 'unchanged'}`);
      for (const it of r.items) console.log(`    - ${it.title}`);
      if (r.dropped.length) r.dropped.forEach(t => console.log(`    ! dropped (no longer sourced): ${t}`));
    }
    console.log('');
    const errors = results.filter(r => r.error).length;
    const changedN = results.filter(r => r.changed).length;
    console.log(`${results.length} reference block(s) checked: ${changedN} changed, ${errors} skipped.`);
  }

  process.exit(results.some(r => r.error) ? 1 : 0);
}

main();
