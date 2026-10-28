#!/usr/bin/env node
/**
 * cxp-open.js
 *
 * Opens the CXP (context-pack) phase for an existing course by auto-stating
 * its one reserved gate, cxp-03_exemplar-programmes (Abbott, 8 Oct 2026:
 * "wire cxp-03 record-writing into the CXP flow"). cxp-03 is reserved,
 * advisory, defaultType none, and subject-independent ("exemplar programmes:
 * none" whatever the subject), so it is written ONCE per course when the
 * course enters CXP — not per context pack. The live CXP gates (cxp-01_subject,
 * cxp-02_qualifiers, cxp-04_context-generation) are decided per context pack
 * via the ordinary /gate + /land path and are NOT written here.
 *
 * Record shape mirrors new-course.js's reserved CXS records: state "closed",
 * provenance "advisory-stated" (GI-2's word for an advisory gate stated at the
 * moment it applies, never opened), grounding [], and a decidedValue (a closed
 * record requires one) of {value:"none", reserved:true}.
 *
 * Idempotent: if cxp-03 already carries a record, this is a no-op.
 *
 * Usage:
 *   node tools/cxp-open.js --course=<slug>
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const CXP_RESERVED_GATE = 'cxp-03_exemplar-programmes';
const CXP_RESERVED_VALUE = { value: 'none', reserved: true };

function fail(message) {
  console.error(`REFUSED: ${message}`);
  process.exit(1);
}

function parseArgs() {
  const args = { course: null };
  process.argv.slice(2).forEach(param => {
    const eq = param.indexOf('=');
    if (eq === -1) return;
    const key = param.slice(2, eq);
    const value = param.slice(eq + 1);
    if (key === 'course') args.course = value;
  });
  if (!args.course) fail('--course=<slug> is required.');
  return args;
}

function main() {
  const args = parseArgs();
  const slug = args.course;
  const manifestPath = path.join(ROOT, 'courses', slug, `course-design_${slug}.json`);
  if (!fs.existsSync(manifestPath)) {
    fail(`no manifest at ${path.relative(ROOT, manifestPath)}: cxp-open runs on an existing course.`);
  }

  const before = fs.readFileSync(manifestPath, 'utf8');
  let manifest;
  try { manifest = JSON.parse(before); }
  catch (err) { fail(`manifest is not valid JSON: ${manifestPath} (${err.message})`); }

  manifest.gates = manifest.gates || [];
  const existing = manifest.gates.find(g => g.gateId === CXP_RESERVED_GATE);
  if (existing && Array.isArray(existing.records) && existing.records.length > 0) {
    console.log(`cxp-open: ${slug} already carries a ${CXP_RESERVED_GATE} record; nothing to do (idempotent).`);
    return;
  }

  const now = new Date().toISOString();
  const record = {
    seq: 1,
    state: 'closed',
    provenance: 'advisory-stated',
    grounding: [],
    decidedValue: CXP_RESERVED_VALUE,
    timestamp: now
  };

  if (existing) {
    existing.records = [record];
  } else {
    manifest.gates.push({ gateId: CXP_RESERVED_GATE, records: [record] });
  }

  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n');
  console.log(`cxp-open: wrote the reserved ${CXP_RESERVED_GATE} record to ${path.relative(ROOT, manifestPath)}`);
  console.log(JSON.stringify(record));
  console.log('');

  console.log('='.repeat(60));
  console.log('VALIDATE: validate-design-schemas.py --course-design');
  console.log('='.repeat(60));
  try {
    const out = execSync(
      `python3 tools/validate-design-schemas.py --course-design "${manifestPath}"`,
      { cwd: ROOT, encoding: 'utf8', stdio: ['pipe', 'pipe', 'pipe'] }
    );
    console.log(out);
  } catch (err) {
    console.log(err.stdout || '');
    console.error(err.stderr || '');
    fs.writeFileSync(manifestPath, before);
    fail(`manifest failed schema validation after writing ${CXP_RESERVED_GATE}; reverted ${path.relative(ROOT, manifestPath)} to its prior content.`);
  }

  console.log('');
  console.log(`CXP phase opened for ${slug}. The live CXP gates (cxp-01_subject, cxp-02_qualifiers,`);
  console.log('cxp-04_context-generation) are decided per context pack via /gate + /land.');
}

main();
