#!/usr/bin/env node
/**
 * session-audit.js
 *
 * Session-start audit script. Trust nothing from a prior session,
 * re-derive from real state before continuing any work.
 *
 * Usage:
 *   node tools/session-audit.js --course=<course-slug>
 *
 * Does in order:
 *   1. git log --oneline -15 -- courses/<slug>/ - recent commit history
 *   2. Extract every grounding/sessionRef citation from course-design;
 *      verify each against real design-kb stores or file paths
 *   3. Run verify-course.js --course=<slug>
 *   4. Print final report
 *
 * Landed: 31 Aug 2026, session retrospective (fixes: unverified claims
 * sitting undetected between sessions).
 */

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs-extra');
const { resolveCourse } = require('./lib/course-resolve');
const { scaffoldBoundaryStatus } = require('./lib/phase-gate');

const ROOT = path.resolve(__dirname, '..');

// Design-KB store files and their ID arrays
const DESIGN_KB_STORES = {
  'gates': { file: 'design-kb/design-kb.gates.json', idField: 'id', arrayName: 'gates' },
  'palette': { file: 'design-kb/design-kb.palette.json', idField: 'id', arrayName: 'entries' },
  'tier-bands': { file: 'design-kb/design-kb.tier-bands.json', idField: 'id', arrayName: 'tiers' },
  'activity-patterns': { file: 'design-kb/design-kb.activity-patterns.json', idField: 'id', arrayName: 'patterns' },
  'skeletons': { file: 'design-kb/design-kb.skeletons.json', idField: 'id', arrayName: 'archetypes' }
};

function parseArgs() {
  const args = { course: null };
  process.argv.slice(2).forEach(param => {
    const parts = param.replace(/^--/, '').split('=');
    if (parts[0] === 'course') {
      args.course = parts[1];
    }
  });
  if (!args.course) {
    console.error('Usage: node tools/session-audit.js --course=<course-slug>');
    process.exit(1);
  }
  return args;
}

function loadDesignKbIds() {
  const ids = new Map();

  for (const [prefix, config] of Object.entries(DESIGN_KB_STORES)) {
    const filePath = path.join(ROOT, config.file);
    if (!fs.existsSync(filePath)) {
      console.log(`  [WARN] Design-KB file not found: ${config.file}`);
      continue;
    }

    const data = fs.readJsonSync(filePath);
    const items = data[config.arrayName] || [];
    for (const item of items) {
      const id = item[config.idField];
      if (id) {
        ids.set(id, config.file);
      }
    }
  }

  return ids;
}

function extractCitations(courseDesign, designKbIds, course) {
  const citations = [];

  // Walk all gates and their records
  for (const gate of courseDesign.gates || []) {
    for (const record of gate.records || []) {
      // Extract grounding citations
      for (const grounding of record.grounding || []) {
        if (grounding.store === 'design-kb' && grounding.id) {
          citations.push({
            type: 'design-kb',
            id: grounding.id,
            source: `${gate.gateId} record ${record.seq}`
          });
        } else if (grounding.store === 'course-design' && grounding.id) {
          // Internal cross-reference to another gate in the same course-design
          citations.push({
            type: 'course-design',
            id: grounding.id,
            source: `${gate.gateId} record ${record.seq}`
          });
        } else if (grounding.doc) {
          citations.push({
            type: 'doc',
            path: grounding.doc,
            ref: grounding.ref,
            source: `${gate.gateId} record ${record.seq}`
          });
        }
      }

      // sessionRef is informational only, not validated (it's a session description string)
    }
  }

  return citations;
}

function verifyCitation(citation, designKbIds, courseDesign) {
  if (citation.type === 'design-kb') {
    const exists = designKbIds.has(citation.id);
    return {
      ...citation,
      pass: exists,
      detail: exists
        ? `Found in ${designKbIds.get(citation.id)}`
        : `ID not found in any design-kb store`
    };
  } else if (citation.type === 'course-design') {
    // Check if the referenced gate exists in the course-design itself
    const gateIds = (courseDesign.gates || []).map(g => g.gateId);
    const exists = gateIds.includes(citation.id);
    return {
      ...citation,
      pass: exists,
      detail: exists
        ? `Found in course-design`
        : `Gate ID not found in course-design`
    };
  } else if (citation.type === 'doc') {
    const filePath = path.join(ROOT, citation.path);
    const exists = fs.existsSync(filePath);
    return {
      ...citation,
      pass: exists,
      detail: exists
        ? `File exists`
        : `File not found at ${citation.path}`
    };
  }

  return { ...citation, pass: false, detail: 'Unknown citation type' };
}

function main() {
  const { course } = parseArgs();

  // Verify course directory exists
  const resolved = resolveCourse(course, ['courses', 'courses/_generated']);
  if (!resolved.found) {
    console.error(`Course not found for slug "${course}". Checked:\n  ${resolved.checked.join('\n  ')}`);
    process.exit(1);
  }
  resolved.warnings.forEach(w => console.error(`WARNING: ${w}`));

  const courseDir = resolved.courseDir;
  const courseDesignPath = resolved.courseDesignPath;

  console.log('='.repeat(60));
  console.log(`SESSION AUDIT: ${course}`);
  console.log('='.repeat(60));
  console.log('');

  // Step 1: Git log
  console.log('─'.repeat(60));
  console.log('1. RECENT COMMIT HISTORY (ground truth)');
  console.log('─'.repeat(60));
  try {
    const gitLog = execSync(`git log --oneline -15 -- ${path.relative(ROOT, courseDir)}/`, {
      cwd: ROOT,
      encoding: 'utf8'
    });
    console.log(gitLog || '  (no commits found for this course)');
  } catch (err) {
    console.log('  (git log failed or no commits found)');
  }
  console.log('');

  // Step 2: Citation verification
  console.log('─'.repeat(60));
  console.log('2. CITATION VERIFICATION');
  console.log('─'.repeat(60));

  if (!courseDesignPath || !fs.existsSync(courseDesignPath)) {
    console.log(`  SKIP: No course-design file found under ${path.relative(ROOT, courseDir)}`);
    console.log('');
  } else {
    const courseDesign = fs.readJsonSync(courseDesignPath);
    const designKbIds = loadDesignKbIds();

    console.log(`  Design-KB IDs loaded: ${designKbIds.size}`);
    console.log('');

    const citations = extractCitations(courseDesign, designKbIds, course);

    if (citations.length === 0) {
      console.log('  No citations found in course-design.');
    } else {
      console.log(`  Checking ${citations.length} citation(s):`);
      console.log('');

      const results = [];
      let failCount = 0;

      for (const citation of citations) {
        const result = verifyCitation(citation, designKbIds, courseDesign);
        results.push(result);
        if (!result.pass) failCount++;

        const status = result.pass ? 'PASS' : 'FAIL';
        const idOrPath = result.type === 'doc' ? result.path : result.id;
        console.log(`  [${status}] ${result.type}: ${idOrPath}`);
        console.log(`         Source: ${result.source}`);
        if (!result.pass) {
          console.log(`         ${result.detail}`);
        }
      }

      console.log('');
      console.log(`  Citation summary: ${citations.length - failCount} PASS, ${failCount} FAIL`);
    }
  }
  console.log('');

  // Step 2.5 (PHA-1): has this course reached the point ORD-1 places
  // before /scaffold? Informational only - verify-course.js (step 3,
  // via manifest-completeness.js's own NOT-YET-REACHABLE clauses 1-2)
  // already carries the correctness of this into this tool's own
  // PASS/FAIL; this step exists so a session starting mid-Phase-A sees
  // the reason named here, not just absorbed silently into step 3.
  console.log('─'.repeat(60));
  console.log('2.5 PHASE BOUNDARY (PHA-1: every gate ORD-1 places before /scaffold)');
  console.log('─'.repeat(60));
  if (!courseDesignPath || !fs.existsSync(courseDesignPath)) {
    console.log('  SKIP: No course-design file found.');
  } else {
    const courseDesign = fs.readJsonSync(courseDesignPath);
    const boundary = scaffoldBoundaryStatus(courseDesign, course);
    if (boundary.reached) {
      console.log('  REACHED: every gate ORD-1 places before /scaffold is closed or skipped.');
    } else {
      console.log(`  NOT YET REACHED - still open: ${boundary.missing.join(', ')}`);
    }
  }
  console.log('');

  // Step 3: Run verify-course.js
  console.log('─'.repeat(60));
  console.log('3. VERIFICATION (verify-course.js)');
  console.log('─'.repeat(60));
  let verifyPassed = false;
  try {
    const verifyOutput = execSync(`node tools/verify-course.js --course=${course}`, {
      cwd: ROOT,
      encoding: 'utf8',
      stdio: ['pipe', 'pipe', 'pipe']
    });
    console.log(verifyOutput);
    verifyPassed = true;
  } catch (err) {
    const output = (err.stdout || '') + (err.stderr || '');
    console.log(output);
    verifyPassed = false;
  }

  // Step 4: Final report
  console.log('='.repeat(60));
  console.log('SESSION AUDIT REPORT');
  console.log('='.repeat(60));

  // Re-run citation check for final stats
  let citationsFailed = [];
  if (courseDesignPath && fs.existsSync(courseDesignPath)) {
    const courseDesign = fs.readJsonSync(courseDesignPath);
    const designKbIds = loadDesignKbIds();
    const citations = extractCitations(courseDesign, designKbIds, course);
    for (const citation of citations) {
      const result = verifyCitation(citation, designKbIds, courseDesign);
      if (!result.pass) {
        citationsFailed.push(result);
      }
    }
    console.log(`Citations checked:    ${citations.length}`);
    console.log(`Citations failed:     ${citationsFailed.length}`);
  } else {
    console.log('Citations checked:    N/A (no course-design file)');
  }

  console.log(`Validators passed:    ${verifyPassed ? 'YES' : 'NO'}`);
  console.log('');

  if (citationsFailed.length > 0) {
    console.log('FAILED CITATIONS:');
    for (const fail of citationsFailed) {
      const idOrPath = fail.type === 'doc' ? fail.path : fail.id;
      console.log(`  - [${fail.type}] ${idOrPath}`);
      console.log(`    Source: ${fail.source}`);
      console.log(`    Reason: ${fail.detail}`);
    }
    console.log('');
  }

  const anyFailed = citationsFailed.length > 0 || !verifyPassed;
  if (anyFailed) {
    console.log('session-audit: FAILED');
    process.exit(1);
  } else {
    console.log('session-audit: PASSED');
    process.exit(0);
  }
}

main();
