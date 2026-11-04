#!/usr/bin/env node
/**
 * verify-course.js
 *
 * Combined verification wrapper. Single command to run all four
 * canonical validation tools in sequence, with full output shown
 * for each. Exits non-zero if ANY check fails.
 *
 * Usage:
 *   node tools/verify-course.js --course=<course-slug> [--strict]
 *
 * Runs in order:
 *   1. voice-lint.js --course=<slug>
 *   2. validate-design-schemas.py --course-design courses/<slug>/course-design_<slug>.json
 *   3. conformance-lint.js --course=<slug>
 *   4. manifest-completeness.js --course=<slug>
 *   5. worked-example-lint.js --course=<slug>  (--strict only, see below)
 *
 * Landed: 31 Aug 2026, session retrospective (fixes: validation skipped piecemeal).
 * Extended: 8 Sep 2026, backlog 5.88 (manifest-completeness added as check 4;
 * missing-course-design SKIP-as-PASS fixed to FAIL, backlog 5.106).
 * Extended: 2 Nov 2026, lesson-page-model-v4 plan step 7: worked-example-lint
 * added as check 5, gated behind --strict only. Unlike checks 1-4, it is not
 * unconditional: the 423-file worked-example backlog (plan step 7) means most
 * courses fail it today on content deliberately deferred, not broken, so it
 * must not fail a plain `verify-course.js` run for every untouched course.
 * --strict opts a specific course in once its worked examples are conformant
 * (or are being driven to conformance) - see worked-example-lint.js's header.
 */

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');
const { resolveCourse } = require('./lib/course-resolve');

const ROOT = path.resolve(__dirname, '..');

function parseArgs() {
  const args = { course: null, strict: false };
  process.argv.slice(2).forEach(param => {
    if (param === '--strict') { args.strict = true; return; }
    const parts = param.replace(/^--/, '').split('=');
    if (parts[0] === 'course') {
      args.course = parts[1];
    }
  });
  if (!args.course) {
    console.error('Usage: node tools/verify-course.js --course=<course-slug> [--strict]');
    process.exit(1);
  }
  return args;
}

function runCheck(name, command) {
  console.log('='.repeat(60));
  console.log(`CHECK: ${name}`);
  console.log('='.repeat(60));
  console.log(`> ${command}\n`);

  try {
    const output = execSync(command, {
      cwd: ROOT,
      encoding: 'utf8',
      stdio: ['pipe', 'pipe', 'pipe']
    });
    console.log(output);
    return { name, pass: true, output };
  } catch (err) {
    // Command failed (non-zero exit)
    const output = (err.stdout || '') + (err.stderr || '');
    console.log(output);
    return { name, pass: false, output };
  }
}

function main() {
  const { course, strict } = parseArgs();

  // Verify course directory exists
  const resolved = resolveCourse(course, ['courses', 'courses/_generated']);
  if (!resolved.found) {
    console.error(`Course not found for slug "${course}". Checked:\n  ${resolved.checked.join('\n  ')}`);
    process.exit(1);
  }
  resolved.warnings.forEach(w => console.error(`WARNING: ${w}`));

  const courseDir = resolved.courseDir;
  const courseDesignPath = resolved.courseDesignPath;

  console.log(`\nverify-course: ${course}`);
  console.log(`Course directory: ${path.relative(ROOT, courseDir)}`);
  console.log('');

  const results = [];

  // 1. voice-lint
  results.push(runCheck(
    'voice-lint',
    `node voice-lint.js --course=${course}`
  ));

  // 2. validate-design-schemas (only if course-design file exists)
  if (courseDesignPath && fs.existsSync(courseDesignPath)) {
    results.push(runCheck(
      'validate-design-schemas',
      `python3 tools/validate-design-schemas.py --course-design ${courseDesignPath}`
    ));
  } else {
    console.log('='.repeat(60));
    console.log('CHECK: validate-design-schemas');
    console.log('='.repeat(60));
    console.log(`FAIL: No course-design file found under ${path.relative(ROOT, courseDir)}\n`);
    // 5.106: a missing manifest is a FAIL, not a SKIP recorded as pass:true.
    // validate-design-schemas cannot run without a course-design file to
    // validate, and "nothing to check" is not the same as "checked, clean".
    results.push({ name: 'validate-design-schemas', pass: false, output: 'FAIL: course-design file missing' });
  }

  // 3. conformance-lint
  results.push(runCheck(
    'conformance-lint',
    `node tools/conformance-lint.js --course=${course}`
  ));

  // 4. manifest-completeness
  results.push(runCheck(
    'manifest-completeness',
    `node tools/manifest-completeness.js --course=${course}`
  ));

  // 5. worked-example-lint (--strict only - see header comment)
  if (strict) {
    results.push(runCheck(
      'worked-example-lint',
      `node tools/worked-example-lint.js --course=${course}`
    ));
  }

  // Summary table
  console.log('='.repeat(60));
  console.log('SUMMARY');
  console.log('='.repeat(60));
  console.log('');
  console.log('Check                      | Result');
  console.log('---------------------------|--------');

  let anyFailed = false;
  for (const r of results) {
    const status = r.pass ? 'PASS' : 'FAIL';
    if (!r.pass) anyFailed = true;
    console.log(`${r.name.padEnd(26)} | ${status}`);
  }

  console.log('');
  if (anyFailed) {
    console.log('verify-course: FAILED (one or more checks failed)');
    process.exit(1);
  } else {
    console.log('verify-course: PASSED (all checks passed)');
    process.exit(0);
  }
}

main();
