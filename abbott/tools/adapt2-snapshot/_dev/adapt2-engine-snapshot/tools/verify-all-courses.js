#!/usr/bin/env node
/**
 * verify-all-courses.js
 *
 * Build/CI gate. Runs the four canonical validators against every course
 * found under courses/ and courses/_generated/ (PR-1-13, Option 2 ruling,
 * 17 Sep 2026 - see the third dated part below) and fails the job if any
 * of three of them fail on any course. Implements A80's Option 4 ruling
 * (docs/project/audit-2026-09/audit-actions-arising.md:93):
 *
 *   - voice-lint.js, conformance-lint.js and validate-design-schemas.py
 *     GATE: a non-zero exit from any of them on any course fails this
 *     script's own exit.
 *   - manifest-completeness.js RUNS and its output is printed in full,
 *     but its exit code does not affect this script's exit. It stays
 *     out of the gate because it currently fails on all four courses on
 *     conditions owned by A102 (clause 6), A104 (clause 3) and A106
 *     (clause 1/AWI) - see A80's row, standing condition, 17 Sep 2026
 *     note. None of those three is fixed by this script; gating on them
 *     now would block builds on faults nobody here can act on today.
 *
 * tools/verify-course.js is not used or modified by this script. Its
 * own anyFailed loop treats all four checks identically (no
 * gating/reporting split), and A80's ruling 3 (17 Sep 2026) keeps that
 * wrapper's behaviour as-is: the gating/reporting distinction belongs
 * to this build gate, not to the per-course wrapper four other things
 * depend on. This script calls the four tools directly instead.
 *
 * FAIL vs ERROR: a tool that ran and exited non-zero (it found real
 * problems) reports FAIL. A tool that could not run at all (missing
 * interpreter, missing script file, any other spawn failure) reports
 * ERROR - distinct so a broken CI environment cannot be misread as
 * four courses failing validation. Both still fail this script's exit
 * if the tool is a gating one; only the label differs.
 *
 * Detection is via execFileSync (no shell), not execSync on a shell
 * string. Tested directly (17 Sep 2026, part 2): under execSync with
 * the default shell, a missing interpreter is swallowed by the shell
 * and surfaces as a completed process with exit code 127 - the same
 * shape as a real non-zero exit, err.status a number, err.code
 * undefined - so status/code cannot distinguish ERROR from FAIL.
 * Under execFileSync (no shell), a missing interpreter is a genuine
 * spawn failure: err.status is null, err.code is 'ENOENT'. That is
 * the only case checked here - real exit codes (0, 1, 127 from the
 * tool's own logic, whatever) always leave err.status a number.
 *
 * Usage:
 *   node tools/verify-all-courses.js
 *
 * Exit 0: voice-lint, conformance-lint and validate-design-schemas all
 *         passed (no FAIL, no ERROR) on every course
 *         (manifest-completeness's result is irrelevant to this).
 * Exit 1: at least one of those three FAILed or ERRORed on at least
 *         one course.
 * Exit 2: zero courses discovered under courses/ (and courses/_generated/).
 *         Nothing was checked, so this is not a pass - distinct from
 *         exit 1 so "ran nothing" and "ran and failed" cannot be misread
 *         as the same condition by a caller that branches on the code.
 *
 * Landed: 17 Sep 2026, A80 wiring part 1 (script only).
 * Extended: 17 Sep 2026, A80 wiring part 2 (FAIL/ERROR distinction;
 * anyGatingFailed computed from results, not while rendering the
 * summary table).
 * Extended: 17 Sep 2026, A80 wiring part 3 (PR-1-13, Abbott's Option 2
 * ruling: discoverCourses() now also recurses one level into
 * courses/_generated/, additively to courses/ itself, and the
 * resolveCourse() call below carries 'courses/_generated' as a second
 * root, matching voice-lint.js and conformance-lint.js's own default).
 * This changes what the gate asserts, from "the committed courses pass"
 * to "the current build output passes" - deliberate, per Abbott's
 * ruling, not inherited: nothing is committed under courses/ directly
 * any more since the archive move at b152c3a.
 * Extended: 17 Sep 2026, PR-1-15 (zero-discovery exit split: zero
 * discovery now exits 2, not 1. Previously indistinguishable at the
 * exit code from a real gating failure - see PR-1-15's register row for
 * the CI incident this caused. grunt/tasks/verify-all-courses.js updated
 * to branch on the new code so the distinction survives that caller too).
 */

const { execFileSync } = require('child_process');
const path = require('path');
const fs = require('fs');
const { resolveCourse } = require('./lib/course-resolve');

const ROOT = path.resolve(__dirname, '..');
const COURSES_DIR = path.join(ROOT, 'courses');

// Tools that gate: non-zero exit here fails this script's own exit.
const GATING_TOOLS = ['voice-lint', 'conformance-lint', 'validate-design-schemas'];
// Tool that reports only: runs, output shown, exit code discarded.
const REPORTING_TOOLS = ['manifest-completeness'];

// E2(a) freeze (gate realignment, 7 Oct 2026, gate-redesign-2026-10-06.md): a
// course directory carrying a `.superseded` marker file is a frozen pre-
// realignment pilot. Its records speak the old gate ids and are deliberately
// out of scope for the realigned store and its validators; it is skipped here
// rather than migrated. Generic (marker-driven), so no slug is hardcoded.
const SUPERSEDED_MARKER = '.superseded';
function isSuperseded(absDir) {
  try { return fs.existsSync(path.join(absDir, SUPERSEDED_MARKER)); }
  catch { return false; }
}

function discoverCourses() {
  const skipped = [];
  // Direct: anything committed straight under courses/ (excluding the
  // leading-underscore _generated directory itself, handled separately
  // below). Kept so a course committed here again in future is still
  // found - additive to Option 1's checked surface, not a replacement of
  // it, per PR-1-13's Option 2 ruling (17 Sep 2026).
  const direct = fs.readdirSync(COURSES_DIR, { withFileTypes: true })
    .filter(entry => entry.isDirectory())
    .map(entry => entry.name)
    .filter(name => !name.startsWith('_'))
    .filter(name => {
      if (isSuperseded(path.join(COURSES_DIR, name))) { skipped.push(name); return false; }
      return true;
    });

  // Generated: recurse one level into courses/_generated/'s own
  // subdirectories. Deliberately not "drop the leading-underscore
  // filter" - that makes _generated itself the sole discovered "course",
  // a directory with no course-design_*.json or en/ of its own, and
  // every gating tool FAILs on it for the wrong reason (confirmed
  // empirically before this fix landed).
  const generatedDir = path.join(COURSES_DIR, '_generated');
  const generated = fs.existsSync(generatedDir)
    ? fs.readdirSync(generatedDir, { withFileTypes: true })
        .filter(entry => entry.isDirectory())
        .map(entry => entry.name)
        .filter(name => {
          if (isSuperseded(path.join(generatedDir, name))) { skipped.push(name); return false; }
          return true;
        })
    : [];

  return { active: [...direct, ...generated].sort(), skipped: skipped.sort() };
}

function runCheck(name, file, args) {
  const printable = `${file} ${args.join(' ')}`;
  console.log('-'.repeat(60));
  console.log(`> ${printable}`);
  console.log('-'.repeat(60));

  try {
    const output = execFileSync(file, args, {
      cwd: ROOT,
      encoding: 'utf8',
      stdio: ['pipe', 'pipe', 'pipe']
    });
    console.log(output);
    return { name, pass: true, error: false, output };
  } catch (err) {
    // execFileSync (no shell): a genuine spawn failure (interpreter
    // missing, etc.) leaves err.status null/undefined with err.code
    // set (e.g. 'ENOENT'). A real non-zero exit from the tool itself
    // always leaves err.status a number. See header comment for the
    // execSync-vs-execFileSync evidence behind this check.
    const spawnFailed = (err.status === null || err.status === undefined);
    if (spawnFailed) {
      const message = `[ERROR] could not run "${printable}": ${err.code || err.message}`;
      console.log(message);
      return { name, pass: false, error: true, output: message };
    }
    const output = (err.stdout || '') + (err.stderr || '');
    console.log(output);
    return { name, pass: false, error: false, output };
  }
}

function runCourse(course) {
  console.log('='.repeat(60));
  console.log(`COURSE: ${course}`);
  console.log('='.repeat(60));

  const results = {};

  // Resolve the manifest FIRST. The content lints (voice-lint,
  // conformance-lint) and manifest-completeness check BUILT page content,
  // which exists only once /scaffold has instantiated pages. A design-stage
  // course (empty instantiations[]) has nothing for them to check, so per the
  // PHA-1 carve-out (documented in new-course.js and .claude/commands/land.md
  // step 5) they report WAITING, not FAIL. validate-design-schemas is
  // design-level and always runs. (Gate realignment, Round F, 8 Oct 2026.)
  const resolvedForDesign = resolveCourse(course, ['courses', 'courses/_generated']);
  resolvedForDesign.warnings.forEach(w => console.log(`WARNING: ${w}`));
  const courseDesignPath = resolvedForDesign.courseDesignPath;
  const courseDesignRel = courseDesignPath
    ? path.relative(ROOT, courseDesignPath)
    : `courses/${course}/course-design_*.json`;

  let hasContent = false;
  if (courseDesignPath && fs.existsSync(courseDesignPath)) {
    try {
      const manifest = JSON.parse(fs.readFileSync(courseDesignPath, 'utf8'));
      hasContent = Array.isArray(manifest.instantiations) && manifest.instantiations.length > 0;
    } catch (e) { hasContent = false; }
  }

  function waiting(name) {
    console.log('-'.repeat(60));
    console.log(`> ${name} (course ${course}) — WAITING`);
    console.log('-'.repeat(60));
    console.log('WAITING: design-stage course, no instantiated content yet; content lint not applicable until /scaffold (PHA-1 carve-out).\n');
    return { name, pass: true, error: false, waiting: true, output: 'WAITING (pre-content)' };
  }

  // voice-lint.js lives at repo root, not tools/.
  results['voice-lint'] = hasContent
    ? runCheck('voice-lint', 'node', ['voice-lint.js', `--course=${course}`])
    : waiting('voice-lint');

  // conformance-lint.js
  results['conformance-lint'] = hasContent
    ? runCheck('conformance-lint', 'node', ['tools/conformance-lint.js', `--course=${course}`])
    : waiting('conformance-lint');

  // validate-design-schemas.py takes --course-design=<path>, not
  // --course=<slug>. Uses the shared resolver (PR-1-11). Always runs: the
  // design record is checkable at every stage.
  if (courseDesignPath && fs.existsSync(courseDesignPath)) {
    results['validate-design-schemas'] = runCheck(
      'validate-design-schemas',
      'python3',
      ['tools/validate-design-schemas.py', '--course-design', courseDesignRel]
    );
  } else {
    console.log('-'.repeat(60));
    console.log(`> (skipped: no course-design file at ${courseDesignRel})`);
    console.log('-'.repeat(60));
    console.log(`FAIL: course-design file missing\n`);
    results['validate-design-schemas'] = {
      name: 'validate-design-schemas',
      pass: false,
      error: false,
      output: 'FAIL: course-design file missing'
    };
  }

  // manifest-completeness.js - reports, does not gate. See header.
  results['manifest-completeness'] = hasContent
    ? runCheck('manifest-completeness', 'node', ['tools/manifest-completeness.js', `--course=${course}`])
    : waiting('manifest-completeness');

  return results;
}

function main() {
  const { active: courses, skipped } = discoverCourses();

  if (skipped.length > 0) {
    console.log(`verify-all-courses: skipping ${skipped.length} superseded course(s) (E2a freeze): ${skipped.join(', ')}`);
  }

  if (courses.length === 0) {
    if (skipped.length > 0) {
      // Every discovered course is a frozen pre-realignment pilot (E2a). Post-
      // reset there are legitimately no active courses to verify yet; that is
      // the correct state, not a failure.
      console.log('verify-all-courses: no active (non-superseded) courses to verify. PASSED (nothing to check; exit 0).');
      process.exit(0);
    }
    console.error(`No course directories found under ${path.relative(ROOT, COURSES_DIR)} - zero discovery is not a pass.`);
    console.error('verify-all-courses: NOT VERIFIED (zero discovery, exit 2)');
    process.exit(2);
  }

  console.log(`verify-all-courses: ${courses.length} course(s) found: ${courses.join(', ')}\n`);

  const allResults = {};
  for (const course of courses) {
    allResults[course] = runCourse(course);
  }

  // Compute the exit-determining result before any rendering, so a
  // change to how the table is drawn can never change what the script
  // decides to exit with.
  const allTools = [...GATING_TOOLS, ...REPORTING_TOOLS];
  let anyGatingFailed = false;
  for (const course of courses) {
    for (const tool of GATING_TOOLS) {
      if (!allResults[course][tool].pass) anyGatingFailed = true;
    }
  }

  // Summary
  console.log('='.repeat(60));
  console.log('SUMMARY');
  console.log('='.repeat(60));
  console.log('');
  const colWidth = Math.max(...courses.map(c => c.length), 5);
  console.log('Tool                       | Gates | ' + courses.map(c => c.padEnd(colWidth)).join(' | '));
  console.log('-'.repeat(28) + '|-------|' + courses.map(() => '-'.repeat(colWidth + 1)).join(''));

  for (const tool of allTools) {
    const gates = GATING_TOOLS.includes(tool);
    const cells = courses.map(course => {
      const r = allResults[course][tool];
      const status = r.error ? 'ERROR' : (r.waiting ? 'WAIT' : (r.pass ? 'PASS' : 'FAIL'));
      return status.padEnd(colWidth);
    });
    console.log(`${tool.padEnd(27)}| ${gates ? 'yes  ' : 'no   '} | ${cells.join(' | ')}`);
  }

  console.log('');
  console.log('manifest-completeness reports but does not gate. Per A80');
  console.log('(docs/project/audit-2026-09/audit-actions-arising.md:93, Option 4');
  console.log('ruling and 17 Sep 2026 standing-condition note), it fails on all');
  console.log('four courses on conditions owned by A102 (clause 6), A104');
  console.log('(clause 3) and A106 (clause 1/AWI) - none of which this gate can');
  console.log('fix, so its failures are shown above but do not affect this');
  console.log("script's exit code.");
  console.log('');

  // Repeated here, not just at the top: CLAUDE.md's own verification
  // discipline reads only "the tail plus the exit line" when output is
  // long (CLAUDE.md:79). A discovery count printed once before all the
  // per-course/per-tool noise does not survive that reading. Restating
  // it beside the exit-determining line means a run that covered two
  // courses instead of four is visible in the tail, not just inferable
  // by scrolling back to the top.
  console.log(`Courses checked: ${courses.length} (${courses.join(', ')})`);
  if (anyGatingFailed) {
    console.log('verify-all-courses: FAILED (a gating tool failed on at least one course)');
    process.exit(1);
  } else {
    console.log('verify-all-courses: PASSED (voice-lint, conformance-lint and validate-design-schemas all passed on every course)');
    process.exit(0);
  }
}

main();
