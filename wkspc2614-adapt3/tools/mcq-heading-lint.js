#!/usr/bin/env node
/**
 * mcq-heading-lint.js
 *
 * Conformance lint for the mcq displayTitle/body exclusivity rule
 * (docs/authoring/component-specs/mcq.md: "The question stem goes in
 * displayTitle, with body left empty - never both"). header.jsx renders
 * displayTitle as .component__title and body/sizedBody as .component__body
 * independently and simultaneously - when both carry the stem, the
 * question renders twice.
 *
 * There is no single correct field: which one a given mcq uses is set by
 * its own block siblings' convention (e.g. a lesson's check items use
 * displayTitle-only; a course's SUMM items use body-only). This tool does
 * not pick a field for you; it only flags the double-population, which is
 * never correct regardless of which convention a given id group follows.
 *
 * Two modes, same shape as worked-example-lint.js and for the same reason
 * (plan step 7 precedent): conformance-lint.js is a CI gate that must not
 * turn red for every untouched course over a pre-existing backlog.
 *
 *   --all (default)
 *     Walks courses/*\/en/components.json for _component === 'mcq' and
 *     reports every id with both displayTitle and body non-empty.
 *     Ratchets on BACKLOG_CEILING: exits non-zero only if the
 *     non-conformant count EXCEEDS the ceiling.
 *
 *   --course=<slug>
 *     Resolves the slug via lib/course-resolve.js (courses, then
 *     courses/_generated). Hard gate on this one course only: exits
 *     non-zero if ANY mcq component in it has both fields populated. No
 *     ratchet - a course opts in by being clean, same as
 *     worked-example-lint's --course mode.
 *
 * BACKLOG_CEILING = 164, empirically confirmed against the current repo
 * (34 courses, 164 components) after the referencing-{introductory,
 * intermediate,advanced} fix (15 components, 2026-11-07). Every further
 * fix lowers this constant by hand; the ratchet means no new file can
 * push the count back up unnoticed.
 *
 * Usage:
 *   node tools/mcq-heading-lint.js [--all] [--json]
 *   node tools/mcq-heading-lint.js --course=<slug> [--json]
 */

const fs = require('fs');
const path = require('path');
const { resolveCourse } = require('./lib/course-resolve');

const ROOT = path.resolve(__dirname, '..');
const BACKLOG_CEILING = 164;

function parseArgs() {
  const args = { mode: 'all', course: null, json: false };
  for (const raw of process.argv.slice(2)) {
    if (raw === '--all') args.mode = 'all';
    else if (raw.startsWith('--course=')) { args.mode = 'course'; args.course = raw.slice('--course='.length); }
    else if (raw === '--json') args.json = true;
    else {
      console.error(`Unknown argument: ${raw}`);
      console.error('Usage: node tools/mcq-heading-lint.js [--all] [--json]');
      console.error('       node tools/mcq-heading-lint.js --course=<slug> [--json]');
      process.exit(1);
    }
  }
  return args;
}

function findDuplicateStems(components) {
  const out = [];
  for (const c of components) {
    if (c._component !== 'mcq') continue;
    const dt = (c.displayTitle || '').trim();
    const body = (c.body || '').trim();
    if (dt && body) out.push({ id: c._id, displayTitle: c.displayTitle, body: c.body });
  }
  return out;
}

// ── --all mode ───────────────────────────────────────────────────────────

function runAllMode(opts) {
  const coursesDir = path.join(ROOT, 'courses');
  const slugs = fs.readdirSync(coursesDir, { withFileTypes: true })
    .filter(e => e.isDirectory())
    .map(e => e.name)
    .sort();

  const byCourse = {};
  let total = 0;

  for (const slug of slugs) {
    const compPath = path.join(coursesDir, slug, 'en', 'components.json');
    if (!fs.existsSync(compPath)) continue;
    let components;
    try { components = JSON.parse(fs.readFileSync(compPath, 'utf8')); } catch (e) { continue; }
    const bad = findDuplicateStems(components);
    if (bad.length > 0) {
      byCourse[slug] = bad;
      total += bad.length;
    }
  }

  if (opts.json) {
    console.log(JSON.stringify({ mode: 'all', total, ceiling: BACKLOG_CEILING, byCourse }, null, 2));
  } else {
    console.log('mcq-heading-lint --all');
    console.log('='.repeat(60));
    console.log(`Courses with a duplicate-stem mcq: ${Object.keys(byCourse).length}`);
    console.log(`Total duplicate-stem components:   ${total}  (ceiling: ${BACKLOG_CEILING})`);
    console.log('');
    for (const slug of Object.keys(byCourse).sort()) {
      console.log(`  ${slug}: ${byCourse[slug].map(b => b.id).join(', ')}`);
    }
    console.log('');
    if (total > BACKLOG_CEILING) {
      console.log(`mcq-heading-lint --all: FAILED - non-conformant count ${total} exceeds ceiling ${BACKLOG_CEILING}. The backlog may not grow; fix a component and lower BACKLOG_CEILING to match.`);
    } else {
      console.log(`mcq-heading-lint --all: PASSED (ratchet) - ${total} non-conformant <= ceiling ${BACKLOG_CEILING}.`);
    }
  }

  process.exit(total > BACKLOG_CEILING ? 1 : 0);
}

// ── --course mode ────────────────────────────────────────────────────────

function runCourseMode(slug, opts) {
  const resolved = resolveCourse(slug, ['courses', 'courses/_generated']);
  if (!resolved.found) {
    console.error(`Course not found for slug "${slug}". Checked:\n  ${resolved.checked.join('\n  ')}`);
    process.exit(1);
  }
  resolved.warnings.forEach(w => console.error(`WARNING: ${w}`));
  if (!resolved.enDir) {
    console.error(`No en/ directory found under ${resolved.courseDir}`);
    process.exit(1);
  }

  const components = JSON.parse(fs.readFileSync(path.join(resolved.enDir, 'components.json'), 'utf8'));
  const bad = findDuplicateStems(components);

  if (opts.json) {
    console.log(JSON.stringify({ mode: 'course', course: slug, root: resolved.root, bad }, null, 2));
  } else {
    console.log(`mcq-heading-lint --course=${slug}  (resolved under '${resolved.root}')`);
    console.log('='.repeat(60));
    if (bad.length === 0) {
      console.log(`No mcq component has both displayTitle and body populated.`);
      console.log(`\nmcq-heading-lint --course=${slug}: PASSED.`);
    } else {
      for (const b of bad) {
        console.log(`${b.id}: FAIL - both displayTitle and body are populated (renders the stem twice)`);
      }
      console.log(`\nmcq-heading-lint --course=${slug}: FAILED (${bad.length} mcq component(s) with a duplicate stem)`);
    }
  }

  process.exit(bad.length > 0 ? 1 : 0);
}

function main() {
  const args = parseArgs();
  if (args.mode === 'all') runAllMode(args);
  else runCourseMode(args.course, args);
}

main();
