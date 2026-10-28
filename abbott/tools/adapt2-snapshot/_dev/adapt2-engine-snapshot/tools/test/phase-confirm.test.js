'use strict';

// Tests for phase-confirm.js. Node's built-in test runner, no dependencies.
// Run with: node --test tools/test/phase-confirm.test.js
//
// RJ-0061 (adp-0216): exactly the 3 scenarios RULINGS 5 names, verbatim:
//   1. "a planted course with a phase of soft gates, where some are marked
//      and some are not, shows the right provenance and confirmedAt on
//      each."
//   2. "A planted course missing a gate fails with a named error."
//   3. "A run reaching no gates fails."

const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const fs = require('node:fs');

const TOOL = path.join(__dirname, '..', 'phase-confirm.js');
const FIXTURES = path.join(__dirname, 'fixtures');
const phaseConfirm = require(TOOL);
const gateOrder = require(path.join(__dirname, '..', 'gate-order.js'));

const STORE_FIXTURE = path.join(FIXTURES, 'gates-phase-batch.json');
const COURSE_DESIGN_FIXTURE = path.join(FIXTURES, 'course-design-phase-batch.json');

// Scenario 1: a phase of soft (and advisory) gates, some marked, some not,
// shows the right provenance and confirmedAt on each.
test('phase batch with some gates marked and some not: right provenance and confirmedAt on each', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  const answers = [
    // not marked, defaultType fixed-value -> ai-default-stood, confirmedAt phase-close
    { gateId: 'gates/fx-soft-fixed', decidedValue: { outcome: 'stood' }, marked: false },
    // marked -> human-amended, originalProposal required, no confirmedAt
    {
      gateId: 'gates/fx-soft-proposal',
      decidedValue: { slot: 'amended-choice' },
      marked: true,
      originalProposal: { slot: 'original-choice' }
    },
    // not marked, advisory -> advisory-stated, confirmedAt phase-close
    { gateId: 'gates/fx-advisory', decidedValue: { note: 'reviewed' }, marked: false }
  ];

  const batch = phaseConfirm.buildPhaseBatch(store, 'FX-BATCH', answers);
  const byGate = new Map(batch.records.map(r => [r.gateId, r.record]));

  assert.equal(byGate.get('gates/fx-soft-fixed').provenance, 'ai-default-stood');
  assert.equal(byGate.get('gates/fx-soft-fixed').confirmedAt, 'phase-close');
  assert.equal(byGate.get('gates/fx-soft-fixed').originalProposal, undefined);

  assert.equal(byGate.get('gates/fx-soft-proposal').provenance, 'human-amended');
  assert.equal(byGate.get('gates/fx-soft-proposal').confirmedAt, undefined);
  assert.deepEqual(byGate.get('gates/fx-soft-proposal').originalProposal, { slot: 'original-choice' });

  assert.equal(byGate.get('gates/fx-advisory').provenance, 'advisory-stated');
  assert.equal(byGate.get('gates/fx-advisory').confirmedAt, 'phase-close');

  assert.deepEqual(batch.phaseEntry.bulkBlessing.stood, ['gates/fx-soft-fixed']);
  assert.deepEqual(batch.phaseEntry.bulkBlessing.proposalStood, []);
  assert.equal(batch.amendRate.marked, 1);
  assert.equal(batch.amendRate.total, 3);

  // applyPhaseBatch on a planted course-design: records land with seq 1,
  // the phase entry is appended, nothing pre-existing is touched. The
  // fixture itself already carries one gate entry (crs-03_course-outcomes, RJ-0102:
  // needed so the real validator's NSK-1 check does not fire on an
  // unrelated gap once phase-confirm.js starts running it) plus the
  // three this batch adds.
  const courseDesign = JSON.parse(fs.readFileSync(COURSE_DESIGN_FIXTURE, 'utf8'));
  assert.equal(courseDesign.gates.length, 1);
  phaseConfirm.applyPhaseBatch(courseDesign, batch);
  assert.equal(courseDesign.gates.length, 4);
  assert.equal(courseDesign.gates.find(g => g.gateId === 'gates/fx-soft-proposal').records[0].seq, 1);
  assert.equal(courseDesign.phases.length, 1);
  assert.equal(courseDesign.phases[0].phaseId, 'FX-BATCH');
});

// Scenario 2: a planted course missing a gate fails with a named error.
test('a planted course missing a gate fails with a named error', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  const answers = [
    { gateId: 'gates/fx-soft-fixed', decidedValue: { outcome: 'stood' }, marked: false },
    { gateId: 'gates/fx-advisory', decidedValue: { note: 'reviewed' }, marked: false }
    // gates/fx-soft-proposal has no answer: phase FX-BATCH requires it.
  ];
  assert.throws(
    () => phaseConfirm.buildPhaseBatch(store, 'FX-BATCH', answers),
    /no answer supplied for gates\/fx-soft-proposal/
  );
});

// Scenario 3: a run reaching no gates fails.
test('a run reaching no gates fails', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  // Phase FX-SOLO in the fixture has only gates/fx-hardstop, which is hard-stop:
  // no soft or advisory gate for phase-confirm to batch.
  assert.throws(
    () => phaseConfirm.buildPhaseBatch(store, 'FX-SOLO', []),
    /phase FX-SOLO has no soft or advisory gate in the store: nothing to batch/
  );
});

// computeProvenance: the soft-gate branch refuses an unrecognised
// defaultType by name rather than guessing a word for it.
test('computeProvenance refuses an unrecognised soft defaultType by name', () => {
  assert.throws(
    () => phaseConfirm.computeProvenance({ id: 'fx-x1', hardness: 'soft', defaultType: 'none' }, false),
    /fx-x1 is soft with defaultType 'none'/
  );
});

// CLI end-to-end: runs against a disposable copy of the planted
// course-design fixture, written and removed inside tools/test/fixtures
// itself (never under /tmp/, per the no-/tmp/ working rule), so the
// committed fixture itself is never mutated by a test run.
test('CLI writes the batch into a temp course-design and prints the amend rate', () => {
  const { execFileSync } = require('node:child_process');

  const tmpCourseDesign = path.join(FIXTURES, `.tmp-phase-confirm-${process.pid}.json`);
  const tmpDraft = path.join(FIXTURES, `.tmp-phase-confirm-draft-${process.pid}.json`);
  fs.copyFileSync(COURSE_DESIGN_FIXTURE, tmpCourseDesign);
  fs.writeFileSync(tmpDraft, JSON.stringify({
    answers: [
      { gateId: 'gates/fx-soft-fixed', decidedValue: { outcome: 'stood' }, marked: false },
      {
        gateId: 'gates/fx-soft-proposal',
        decidedValue: { slot: 'amended-choice' },
        marked: true,
        originalProposal: { slot: 'original-choice' }
      },
      { gateId: 'gates/fx-advisory', decidedValue: { note: 'reviewed' }, marked: false }
    ]
  }, null, 2));

  let readBackSpecPath = null;
  try {
    const out = execFileSync('node', [
      TOOL,
      `--course-design=${tmpCourseDesign}`,
      `--draft=${tmpDraft}`,
      '--phase=FX-BATCH',
      `--store=${STORE_FIXTURE}`
    ], { encoding: 'utf8' });
    const parsed = JSON.parse(out);
    assert.equal(parsed.phaseId, 'FX-BATCH');
    assert.equal(parsed.amendRate, '1/3');
    assert.deepEqual(parsed.bulkBlessing, { stood: ['gates/fx-soft-fixed'], proposalStood: [] });

    const written = JSON.parse(fs.readFileSync(tmpCourseDesign, 'utf8'));
    assert.equal(written.gates.length, 4);
    assert.equal(written.phases.length, 1);

    // RJ-0080 read-back: the same run also renders the course design
    // specification beside the just-written record, without a second
    // change to the record (already asserted above: still 3 gates, 1
    // phase, exactly what buildPhaseBatch produced).
    readBackSpecPath = parsed.readBack.specPath;
    assert.equal(readBackSpecPath, path.join(FIXTURES, 'adp-course-design-specification_phase-batch-fixture.md'));
    assert.equal(typeof parsed.readBack.notReadyCount, 'number');
    const specText = fs.readFileSync(readBackSpecPath, 'utf8');
    assert.match(specText, /^# Course design specification: phase-batch-fixture/);
    assert.match(specText, /## Not ready/);
  } finally {
    fs.rmSync(tmpCourseDesign, { force: true });
    fs.rmSync(tmpDraft, { force: true });
    if (readBackSpecPath) fs.rmSync(readBackSpecPath, { force: true });
  }
});

// RJ-0102 (adp-0226, D-0081 (a)): a planted invalid record. The fixture
// store's gates/fx-soft-fixed gate carries a decidedValueShape requiring
// outcomeCountReason once outcomes.length >= 4 (the validator resolves
// the written record against that store, forwarded via --store ->
// --course-design-gates; six-phase realignment 8 Oct 2026, where the old
// gates/B1 that carried this shape in design-kb was retired). This draft
// supplies 4 outcomes and no reason. Before RJ-0102, phase-confirm.js wrote this
// record and rendered a read-back from it anyway (proved empirically
// against a git-archive extraction of the tool at the commit before
// this fix, under 00-tmp/00-outputs/00-scratch/adp-0226/, reported in
// the session report rather than pinned here as a permanent test
// against a historical commit). This test checks only the current
// tool's own behaviour: the write stands, the validator's own named
// error reaches stderr, and no read-back is rendered.
test('CLI on a record the validator refuses: write stands, read-back skipped, named error, exit 1', () => {
  const { execFileSync } = require('node:child_process');

  const tmpCourseDesign = path.join(FIXTURES, `.tmp-phase-confirm-invalid-${process.pid}.json`);
  const tmpDraft = path.join(FIXTURES, `.tmp-phase-confirm-draft-invalid-${process.pid}.json`);
  const specPath = path.join(FIXTURES, 'adp-course-design-specification_phase-batch-fixture.md');
  fs.copyFileSync(COURSE_DESIGN_FIXTURE, tmpCourseDesign);
  fs.rmSync(specPath, { force: true }); // clean slate: no earlier run's spec file lingering
  fs.writeFileSync(tmpDraft, JSON.stringify({
    answers: [
      {
        gateId: 'gates/fx-soft-fixed',
        decidedValue: {
          outcomes: [
            { id: 'o1', text: 't1', serves: 'CO1' },
            { id: 'o2', text: 't2', serves: 'CO2' },
            { id: 'o3', text: 't3', serves: 'CO3' },
            { id: 'o4', text: 't4', serves: 'CO1' }
          ]
        },
        marked: false
      },
      {
        gateId: 'gates/fx-soft-proposal',
        decidedValue: { slot: 'amended-choice' },
        marked: true,
        originalProposal: { slot: 'original-choice' }
      },
      { gateId: 'gates/fx-advisory', decidedValue: { note: 'reviewed' }, marked: false }
    ]
  }, null, 2));

  try {
    try {
      execFileSync('node', [
        TOOL,
        `--course-design=${tmpCourseDesign}`,
        `--draft=${tmpDraft}`,
        '--phase=FX-BATCH',
        `--store=${STORE_FIXTURE}`
      ], { encoding: 'utf8' });
      assert.fail('expected a non-zero exit: the validator should have refused this record');
    } catch (e) {
      assert.equal(e.status, 1);
      assert.match(e.stderr, /outcomeCountReason/);
      assert.match(e.stderr, /write stands/);
    }

    // Report-failed-state (RJ-0102's decision, not rollback): the bad
    // record is still on disk, exactly as written.
    const written = JSON.parse(fs.readFileSync(tmpCourseDesign, 'utf8'));
    const b1 = written.gates.find(g => g.gateId === 'gates/fx-soft-fixed');
    assert.equal(b1.records[0].decidedValue.outcomes.length, 4);
    assert.equal(b1.records[0].decidedValue.outcomeCountReason, undefined);

    // No read-back was rendered for this run.
    assert.equal(fs.existsSync(specPath), false);
  } finally {
    fs.rmSync(tmpCourseDesign, { force: true });
    fs.rmSync(tmpDraft, { force: true });
    fs.rmSync(specPath, { force: true });
  }
});

test('CLI with a phase reaching no gates fails with exit 1, named error on stderr', () => {
  const { execFileSync } = require('node:child_process');

  const tmpCourseDesign = path.join(FIXTURES, `.tmp-phase-confirm-nogate-${process.pid}.json`);
  const tmpDraft = path.join(FIXTURES, `.tmp-phase-confirm-draft-nogate-${process.pid}.json`);
  fs.copyFileSync(COURSE_DESIGN_FIXTURE, tmpCourseDesign);
  fs.writeFileSync(tmpDraft, JSON.stringify({ answers: [] }, null, 2));

  try {
    execFileSync('node', [
      TOOL,
      `--course-design=${tmpCourseDesign}`,
      `--draft=${tmpDraft}`,
      '--phase=FX-SOLO',
      `--store=${STORE_FIXTURE}`
    ], { encoding: 'utf8' });
    assert.fail('expected a non-zero exit');
  } catch (e) {
    assert.equal(e.status, 1);
    assert.match(e.stderr, /phase FX-SOLO has no soft or advisory gate in the store: nothing to batch/);
  } finally {
    fs.rmSync(tmpCourseDesign, { force: true });
    fs.rmSync(tmpDraft, { force: true });
  }
});
