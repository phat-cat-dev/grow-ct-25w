'use strict';

// Tests for reopen.js. Node's built-in test runner, no dependencies.
// Run with: node --test tools/test/reopen.test.js
//
// RJ-0062 (adp-0216): exactly the 4 scenarios its ruling names, on a
// planted course design record. The ruling's own wording used the
// old-model ids (A2 = crs-02_thematic-scope, CO = crs-03_course-outcomes);
// the fixtures and assertions were realigned to the six-phase gate ids
// (8 Oct 2026), so the scenarios read:
//   1. "reopening crs-02_thematic-scope lists crs-03_course-outcomes
//      (constitutive) and its own dependents by class."
//   2. "reopening a gate nothing depends on lists none."
//   3. "reopening a gate not in the store fails with a named error."
//   4. "a run reaching no record fails."

const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const fs = require('node:fs');

const TOOL = path.join(__dirname, '..', 'reopen.js');
const FIXTURES = path.join(__dirname, 'fixtures');
const reopen = require(TOOL);
const gateOrder = require(path.join(__dirname, '..', 'gate-order.js'));

const STORE_FIXTURE = path.join(FIXTURES, 'gates-reopen.json');
const COURSE_DESIGN_FIXTURE = path.join(FIXTURES, 'course-design-reopen.json');

function loadCourseDesign() {
  return JSON.parse(fs.readFileSync(COURSE_DESIGN_FIXTURE, 'utf8'));
}

// Scenario 1: reopening crs-02_thematic-scope lists crs-03_course-outcomes
// (constitutive) and its own dependents by class.
test('reopening crs-02_thematic-scope lists crs-03_course-outcomes (constitutive) and its own dependents by class', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  const courseDesign = loadCourseDesign();
  const preview = reopen.buildReopenPreview(store, courseDesign, 'crs-02_thematic-scope');
  assert.equal(preview.currentSeq, 1);
  const byGate = new Map(preview.dependents.map(d => [d.gate, d.dependencyClass]));
  assert.equal(byGate.get('crs-03_course-outcomes'), 'constitutive');
  assert.equal(byGate.get('wra-04_confidence'), 'substantive');
  assert.equal(byGate.get('crs-05_course-spec'), 'nominal');
  assert.equal(preview.dependents.length, 3);
});

// Scenario 2: reopening a gate nothing depends on lists none.
test('reopening a gate nothing depends on lists none', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  const courseDesign = loadCourseDesign();
  const preview = reopen.buildReopenPreview(store, courseDesign, 'wra-01_wrapper-open');
  assert.deepEqual(preview.dependents, []);
});

// Scenario 3: reopening a gate not in the store fails with a named error.
test('reopening a gate not in the store fails with a named error', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  const courseDesign = loadCourseDesign();
  assert.throws(
    () => reopen.buildReopenPreview(store, courseDesign, 'gates/NOPE'),
    /no gate gates\/NOPE in store/
  );
});

// Scenario 4: a run reaching no record fails.
test('a run reaching no record fails', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  const courseDesign = loadCourseDesign();
  // cxs-05_external-standards is in the store (fixture) but carries no
  // record in the planted course design.
  assert.throws(
    () => reopen.buildReopenPreview(store, courseDesign, 'cxs-05_external-standards'),
    /cxs-05_external-standards has no record in the course design: nothing to reopen/
  );
});

// A universal-scope gate (cxs-01_institutional-context) is refused by name, never
// silently reported as having no dependents.
test('reopening a universal-scope gate fails with a named error, never an empty dependents list', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  const courseDesign = loadCourseDesign();
  assert.throws(
    () => reopen.buildReopenPreview(store, courseDesign, 'cxs-01_institutional-context'),
    /cxs-01_institutional-context has propagationScope 'universal'/
  );
});

// defaultVerdictForClass: refuses an unrecognised dependencyClass by
// name rather than guessing a verdict for it.
test('defaultVerdictForClass refuses an unrecognised dependencyClass by name', () => {
  assert.throws(
    () => reopen.defaultVerdictForClass('cosmetic'),
    /unrecognised dependencyClass 'cosmetic'/
  );
});

// buildReopen: the full write-shape build, appending the reopened
// gate's new record and the sweep event, from a draft's dispositions.
test('buildReopen appends the new record and writes the sweep event in the schema shape', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  const courseDesign = loadCourseDesign();
  const answer = {
    changeKind: 'amended',
    note: 'crs-02 picked up a third lesson',
    provenance: 'human-specified',
    decidedValue: { lessons: ['L01', 'L02', 'L03'] },
    dispositions: [
      { gate: 'crs-03_course-outcomes', verdict: 'invalidate', mode: 'confirmed', resolution: { status: 'open' } },
      { gate: 'wra-04_confidence', verdict: 'flag-for-review', mode: 'amended', note: 'wra-04 still cites L01-L02 only', resolution: { status: 'open' } },
      { gate: 'crs-05_course-spec', verdict: 'stand-with-warning', mode: 'stood' }
    ]
  };
  const result = reopen.buildReopen(store, courseDesign, 'crs-02_thematic-scope', answer);

  assert.equal(result.newRecord.seq, 2);
  assert.equal(result.newRecord.supersedes, 1);
  assert.equal(result.newRecord.provenance, 'human-specified');

  assert.match(result.sweepEvent.eventId, /^SW-1$/);
  assert.equal(result.sweepEvent.trigger.gate, 'crs-02_thematic-scope');
  assert.equal(result.sweepEvent.trigger.oldRecordSeq, 1);
  assert.equal(result.sweepEvent.trigger.newRecordSeq, 2);

  const byGate = new Map(result.sweepEvent.sweep.map(s => [s.gate, s]));
  assert.equal(byGate.get('crs-03_course-outcomes').defaultVerdict, 'invalidate');
  assert.deepEqual(byGate.get('crs-03_course-outcomes').basis, { gate: 'crs-02_thematic-scope', dependencyClass: 'constitutive' });
  assert.deepEqual(byGate.get('crs-03_course-outcomes').resolution, { status: 'open' });
  assert.equal(byGate.get('wra-04_confidence').disposition.note, 'wra-04 still cites L01-L02 only');
  assert.equal(byGate.get('crs-05_course-spec').resolution, undefined);

  reopen.applyReopen(courseDesign, result);
  assert.equal(courseDesign.gates.find(g => g.gateId === 'crs-02_thematic-scope').records.length, 2);
  assert.equal(courseDesign.sweepEvents.length, 1);
});

// buildReopen refuses a draft missing a disposition for a dependent
// the preview named (mirrors phase-confirm.js's own refusal).
test('buildReopen fails with a named error when a dependent has no disposition', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  const courseDesign = loadCourseDesign();
  const answer = {
    changeKind: 'amended',
    note: 'crs-02 amended',
    provenance: 'human-specified',
    decidedValue: { lessons: ['L01'] },
    dispositions: [
      { gate: 'crs-03_course-outcomes', verdict: 'invalidate', mode: 'confirmed', resolution: { status: 'open' } }
      // wra-04_confidence and crs-05_course-spec have no disposition.
    ]
  };
  assert.throws(
    () => reopen.buildReopen(store, courseDesign, 'crs-02_thematic-scope', answer),
    /no disposition supplied for wra-04_confidence/
  );
});

// CLI end-to-end, preview mode: never writes.
test('CLI --preview prints the dependents and writes nothing', () => {
  const { execFileSync } = require('node:child_process');
  const before = fs.readFileSync(COURSE_DESIGN_FIXTURE, 'utf8');
  const out = execFileSync('node', [
    TOOL,
    '--preview',
    '--gate=crs-02_thematic-scope',
    `--course-design=${COURSE_DESIGN_FIXTURE}`,
    `--store=${STORE_FIXTURE}`
  ], { encoding: 'utf8' });
  const parsed = JSON.parse(out);
  assert.equal(parsed.gateId, 'crs-02_thematic-scope');
  assert.equal(parsed.dependents.length, 3);
  const after = fs.readFileSync(COURSE_DESIGN_FIXTURE, 'utf8');
  assert.equal(before, after);
});

// CLI end-to-end, apply mode: runs against a disposable copy of the
// planted course-design fixture, written and removed inside
// tools/test/fixtures itself (never under /tmp/, per the no-/tmp/
// working rule), so the committed fixture itself is never mutated.
test('CLI apply writes the new record and the sweep event into a temp course-design', () => {
  const { execFileSync } = require('node:child_process');

  const tmpCourseDesign = path.join(FIXTURES, `.tmp-reopen-${process.pid}.json`);
  const tmpDraft = path.join(FIXTURES, `.tmp-reopen-draft-${process.pid}.json`);
  fs.copyFileSync(COURSE_DESIGN_FIXTURE, tmpCourseDesign);
  fs.writeFileSync(tmpDraft, JSON.stringify({
    changeKind: 'amended',
    note: 'crs-02 picked up a third lesson',
    provenance: 'human-specified',
    decidedValue: { lessons: ['L01', 'L02', 'L03'] },
    dispositions: [
      { gate: 'crs-03_course-outcomes', verdict: 'invalidate', mode: 'confirmed', resolution: { status: 'open' } },
      { gate: 'wra-04_confidence', verdict: 'flag-for-review', mode: 'confirmed', resolution: { status: 'open' } },
      { gate: 'crs-05_course-spec', verdict: 'stand-with-warning', mode: 'stood' }
    ]
  }, null, 2));

  try {
    const out = execFileSync('node', [
      TOOL,
      `--course-design=${tmpCourseDesign}`,
      `--draft=${tmpDraft}`,
      '--gate=crs-02_thematic-scope',
      `--store=${STORE_FIXTURE}`
    ], { encoding: 'utf8' });
    const parsed = JSON.parse(out);
    assert.equal(parsed.gateId, 'crs-02_thematic-scope');
    assert.equal(parsed.newSeq, 2);
    assert.equal(parsed.eventId, 'SW-1');

    const written = JSON.parse(fs.readFileSync(tmpCourseDesign, 'utf8'));
    assert.equal(written.gates.find(g => g.gateId === 'crs-02_thematic-scope').records.length, 2);
    assert.equal(written.sweepEvents.length, 1);
  } finally {
    fs.rmSync(tmpCourseDesign, { force: true });
    fs.rmSync(tmpDraft, { force: true });
  }
});

test('CLI with a gate not in the store fails with exit 1, named error on stderr', () => {
  const { execFileSync } = require('node:child_process');
  try {
    execFileSync('node', [
      TOOL,
      '--preview',
      '--gate=gates/NOPE',
      `--course-design=${COURSE_DESIGN_FIXTURE}`,
      `--store=${STORE_FIXTURE}`
    ], { encoding: 'utf8' });
    assert.fail('expected a non-zero exit');
  } catch (e) {
    assert.equal(e.status, 1);
    assert.match(e.stderr, /no gate gates\/NOPE in store/);
  }
});

// RJ-0062 D8(a) (4 Nov 2026): buildReopenPreview's profile filter, read
// through gateOrder.profileGateIds against design-kb.gate-profiles.json
// (never hardcoded to a profile name).
const GATE_PROFILES_FIXTURE = path.join(FIXTURES, 'gate-profiles-reopen.json');

test('D8(a): a gate the active profile does not claim reports an empty dependents list', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  const gateProfilesStore = gateOrder.loadGateProfiles(GATE_PROFILES_FIXTURE);
  const courseDesign = loadCourseDesign();
  courseDesign.profile = 'no-crs02'; // this profile's step list omits crs-02_thematic-scope
  const preview = reopen.buildReopenPreview(store, courseDesign, 'crs-02_thematic-scope', gateProfilesStore);
  assert.deepEqual(preview.dependents, []);
});

test('D8(a): a gate the active profile does claim keeps its unfiltered dependents', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  const gateProfilesStore = gateOrder.loadGateProfiles(GATE_PROFILES_FIXTURE);
  const courseDesign = loadCourseDesign();
  courseDesign.profile = 'has-crs02'; // this profile's step list names crs-02_thematic-scope
  const preview = reopen.buildReopenPreview(store, courseDesign, 'crs-02_thematic-scope', gateProfilesStore);
  assert.equal(preview.dependents.length, 3);
});

test('D8(a): a profile name the store cannot resolve falls back to the unfiltered list', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  const gateProfilesStore = gateOrder.loadGateProfiles(GATE_PROFILES_FIXTURE);
  const courseDesign = loadCourseDesign();
  courseDesign.profile = 'unknown-profile-not-in-fixture';
  const preview = reopen.buildReopenPreview(store, courseDesign, 'crs-02_thematic-scope', gateProfilesStore);
  assert.equal(preview.dependents.length, 3);
});

test('D8(a): omitting gateProfilesStore skips the filter entirely (pre-existing behaviour)', () => {
  const store = gateOrder.loadStore(STORE_FIXTURE);
  const courseDesign = loadCourseDesign();
  courseDesign.profile = 'no-crs02'; // would be filtered to [] if a gateProfilesStore were supplied
  const preview = reopen.buildReopenPreview(store, courseDesign, 'crs-02_thematic-scope');
  assert.equal(preview.dependents.length, 3);
});

// RJ-0062 D8(b) (4 Nov 2026): hasRecord's repeatsPer:'lesson' id-expansion.
// les-01_lesson-proposal is never stored under its own bare id; three
// closed per-lesson records exist under <slug>-<lessonKey>-les-01. Before
// the fix, hasRecord found none of them and misclassified the dependent
// as authoredFresh.
const LESSON_STORE_FIXTURE = path.join(FIXTURES, 'gates-reopen-lessons.json');
const LESSON_COURSE_DESIGN_FIXTURE = path.join(FIXTURES, 'course-design-reopen-lessons.json');

function loadLessonCourseDesign() {
  return JSON.parse(fs.readFileSync(LESSON_COURSE_DESIGN_FIXTURE, 'utf8'));
}

test('D8(b): a repeatsPer:lesson dependent with real per-lesson records is sweep-eligible, not authoredFresh', () => {
  const store = gateOrder.loadStore(LESSON_STORE_FIXTURE);
  const courseDesign = loadLessonCourseDesign();
  const answer = {
    changeKind: 'amended',
    note: 'lesson map picked up a third lesson',
    provenance: 'human-specified',
    decidedValue: { lessons: [{ key: 'L01' }, { key: 'L02' }, { key: 'L03' }] },
    dispositions: [
      { gate: 'les-01_lesson-proposal', verdict: 'flag-for-review', mode: 'confirmed', resolution: { status: 'open' } }
    ]
  };
  const result = reopen.buildReopen(store, courseDesign, 'crs-04_lesson-map', answer);

  assert.deepEqual(result.authoredFresh, []);
  const byGate = new Map(result.sweepEvent.sweep.map(s => [s.gate, s]));
  const sweptLes01 = byGate.get('les-01_lesson-proposal');
  assert.ok(sweptLes01, 'les-01_lesson-proposal should appear in the sweep, not authoredFresh');
  // Max seq across the three per-lesson records (seq 1, 2, 1) is 2.
  assert.equal(sweptLes01.recordSeq, 2);
  assert.deepEqual(sweptLes01.basis, { gate: 'crs-04_lesson-map', dependencyClass: 'constitutive' });
});

test('D8(b): recordsForDependent expands a repeatsPer:lesson gate into its real per-lesson manifest entries', () => {
  const store = gateOrder.loadStore(LESSON_STORE_FIXTURE);
  const courseDesign = loadLessonCourseDesign();
  const found = reopen.recordsForDependent(store, courseDesign, { gate: 'les-01_lesson-proposal', dependencyClass: 'constitutive' });
  assert.equal(found.length, 3);
  const ids = found.map(e => e.gateId).sort();
  assert.deepEqual(ids, [
    'reopen-lessons-fixture-L01-les-01',
    'reopen-lessons-fixture-L02-les-01',
    'reopen-lessons-fixture-L03-les-01'
  ]);
});
