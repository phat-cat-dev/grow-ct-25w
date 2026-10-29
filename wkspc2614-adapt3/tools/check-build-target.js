#!/usr/bin/env node
/**
 * check-build-target.js
 *
 * Build/CI gate (Prompt 139 Unit 5, task 9). Refuses the build if
 * src/course is a symlink whose resolved target falls outside the
 * courses/ tree.
 *
 * WHY: src/course is what grunt actually copies from (see grunt/config/
 * copy.js's courseAssets/courseJson globs, all rooted at src/course). If
 * that symlink quietly points somewhere else - a scratch directory, an
 * unrelated course, or (as found live at the time this check was written)
 * archive/, which tools/lib/course-resolve.js's own header states is
 * "not gated against, not reviewed, not repaired, not retrofitted" -
 * reference material, not a live build input - a build can silently ship
 * content nobody meant to ship, indistinguishable by name from the real
 * thing. This is the same failure shape CLAUDE.md's own "Working
 * directory" section already warns about for stray writes one level up;
 * this check catches its build-time counterpart.
 *
 * WHAT COUNTS AS "outside courses/": both named roots
 * tools/lib/course-resolve.js defines under the courses/ tree -
 * courses/<slug> and courses/_generated/<slug> - are accepted. Only
 * archive/ or any other location outside courses/ is refused.
 *
 * UPDATED (28 Oct 2026): historical/retired course material now lives at
 * courses/_archive/ (moved there, inside courses/, on explicit instruction -
 * see courses/_archive/courses-2026-09/README.md and
 * courses/_archive/courses-2026-09-rebuild/README.md for provenance).
 * Underscore-prefixed to match the existing courses/_generated and
 * courses/_component-gallery convention, so verify-all-courses.js's
 * discoverCourses() already skips it (its direct-listing filter drops any
 * name starting with "_"). That placement is still textually "under
 * courses/" though, and would otherwise pass the check below unchanged -
 * exactly the failure this file exists to catch, just one level deeper.
 * courses/_archive/ is therefore refused explicitly here too, by name,
 * regardless of the courses/ check.
 *
 * UPDATED (Prompt 140 CSTR-1, 21 Sep 2026): src/course no longer exists
 * as a checked-in symlink at all (it pointed at
 * archive/courses-2026-09/academic-writing-introductory - see this
 * file's own history). An absent src/course now refuses too, telling
 * the operator plainly that no course is linked and that /new-course
 * links one. This is a behaviour change from Prompt 139's original
 * version of this check, which left an absent src/course to "Adapt's
 * and grunt's own existing failure modes" - CSTR-1 asks for the refusal
 * to happen here instead, with a clear message, rather than downstream
 * as an unrelated-looking crash.
 *
 * WHAT THIS STILL DOES NOT CHECK: src/course existing as a real
 * (non-symlink) directory. That is left to Adapt's and grunt's own
 * existing failure modes - this check has no way to tell a real,
 * intentionally-scaffolded course directory from anything else without
 * a symlink to inspect, and CSTR-1 did not ask for that to change.
 *
 * Usage: node tools/check-build-target.js
 * Exit 0: src/course is not a symlink, or is a symlink resolving under
 *   courses/.
 * Exit 1: src/course does not exist, or is a symlink resolving outside
 *   courses/.
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const TARGET = path.join(ROOT, 'src', 'course');
const COURSES_ROOT = path.join(ROOT, 'courses') + path.sep;
const ARCHIVE_ROOT = path.join(ROOT, 'courses', '_archive') + path.sep;

function main() {
  let lstat;
  try {
    lstat = fs.lstatSync(TARGET);
  } catch (err) {
    console.error(`REFUSED: src/course does not exist (${err.code}) - no course is linked.`);
    console.error('  Run /new-course to create courses/<slug>/ and link it to src/course.');
    console.error('  Build stopped (Prompt 140 CSTR-1): a build must not proceed with no course linked.');
    process.exit(1);
  }

  if (!lstat.isSymbolicLink()) {
    console.log('check-build-target: src/course is not a symlink - nothing to check.');
    process.exit(0);
  }

  const resolved = fs.realpathSync(TARGET);
  const resolvedWithSep = resolved + path.sep;

  if (resolvedWithSep.startsWith(ARCHIVE_ROOT)) {
    console.error(`REFUSED: src/course is a symlink resolving into courses/_archive/.`);
    console.error(`  src/course -> ${resolved}`);
    console.error('  Build stopped: courses/_archive/ holds retired/historical course material');
    console.error('  (reference only, not gated against, not reviewed, not repaired, not');
    console.error('  retrofitted - see courses/_archive/*/README.md). A build must not ship it.');
    process.exit(1);
  }

  if (!resolvedWithSep.startsWith(COURSES_ROOT)) {
    console.error(`REFUSED: src/course is a symlink resolving outside courses/.`);
    console.error(`  src/course -> ${resolved}`);
    console.error(`  courses/ root is: ${COURSES_ROOT.slice(0, -1)}`);
    console.error('  Build stopped (Prompt 139 task 9): a build must not silently ship content from outside courses/ (e.g. archive/, which is reference material only per tools/lib/course-resolve.js).');
    process.exit(1);
  }

  console.log(`check-build-target: src/course -> ${resolved} (under courses/). OK.`);
  process.exit(0);
}

main();
