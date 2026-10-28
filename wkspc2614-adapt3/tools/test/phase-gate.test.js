'use strict';

// Tests for tools/lib/phase-gate.js. Node's built-in test runner, no
// dependencies. Run with: node --test tools/test/phase-gate.test.js
//
// PHA-1 (docs/project/open-decisions.md): a check depending on later-stage
// work reports it as waiting until every gate before /scaffold is closed or
// skipped. Gate realignment (Round C/D, 7 Oct 2026, gate-redesign-2026-10-06.md):
// the pre-scaffold boundary is the course-level ONB+CRS design gates
// (onb-01..04, crs-01..04). Lesson outcomes moved into crs-04_lesson-map
// (A6.1 amendment), so there is no longer a per-lesson B1 gate in this
// boundary; les-01/wra-*/cxp-* are post-scaffold.

const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');

const { scaffoldBoundaryStatus, SHARED_PRE_SCAFFOLD_GATES } = require(
  path.join(__dirname, '..', 'lib', 'phase-gate.js')
);

function closedRecord(decidedValue) {
  return { state: 'closed', decidedValue: decidedValue || {} };
}

function skippedRecord() {
  return { state: 'skipped' };
}

function gate(gateId, record) {
  return { gateId, records: record ? [record] : [] };
}

// Scenario 1: mid-design - some ONB/CRS gates closed, the later CRS design
// gates not yet recorded -> boundary not reached, names exactly the missing.
test('mid-design course: boundary not reached, names the unclosed CRS gates', () => {
  const courseDesign = {
    gates: [
      gate('onb-01_theme-preset', closedRecord()),
      gate('onb-02_course-theme', closedRecord()),
      gate('onb-03_pitch', closedRecord()),
      gate('onb-04_naming', closedRecord()),
      gate('crs-01_sources', closedRecord()),
      gate('crs-02_thematic-scope', closedRecord())
      // crs-03_course-outcomes and crs-04_lesson-map: no record at all.
    ]
  };

  const status = scaffoldBoundaryStatus(courseDesign, 'phasegatetest');

  assert.equal(status.reached, false);
  assert.ok(status.missing.includes('crs-03_course-outcomes'));
  assert.ok(status.missing.includes('crs-04_lesson-map'));
  for (const satisfied of ['onb-01_theme-preset', 'onb-02_course-theme', 'onb-03_pitch', 'onb-04_naming', 'crs-01_sources', 'crs-02_thematic-scope']) {
    assert.ok(!status.missing.includes(satisfied), `${satisfied} wrongly reported missing`);
  }
});

// Scenario 2: every pre-scaffold gate closed -> boundary reached, nothing missing.
test('every pre-scaffold gate closed: boundary reached', () => {
  const courseDesign = {
    gates: SHARED_PRE_SCAFFOLD_GATES.map(id => gate(id, closedRecord()))
  };
  const status = scaffoldBoundaryStatus(courseDesign, 'phasegatetest');
  assert.deepEqual(status.missing, []);
  assert.equal(status.reached, true);
});

// Scenario 3: all skipped (not closed) still counts as past - PHA-1's own
// words, "closed or skipped".
test('a skipped gate counts as past the boundary, same as closed', () => {
  const courseDesign = {
    gates: SHARED_PRE_SCAFFOLD_GATES.map(id => gate(id, skippedRecord()))
  };
  const status = scaffoldBoundaryStatus(courseDesign, 'phasegatetest');
  assert.deepEqual(status.missing, []);
  assert.equal(status.reached, true);
});

// Scenario 4: the lesson map not yet closed -> not reached, named.
test('crs-04_lesson-map not closed: boundary not reached, named', () => {
  const courseDesign = {
    gates: SHARED_PRE_SCAFFOLD_GATES
      .filter(id => id !== 'crs-04_lesson-map')
      .map(id => gate(id, closedRecord()))
  };
  const status = scaffoldBoundaryStatus(courseDesign, 'phasegatetest');
  assert.equal(status.reached, false);
  assert.deepEqual(status.missing, ['crs-04_lesson-map']);
});

// Scenario 5: no gates at all -> every shared gate reported missing.
test('empty courseDesign.gates[]: every shared gate reported missing', () => {
  const status = scaffoldBoundaryStatus({ gates: [] }, 'phasegatetest');
  assert.equal(status.reached, false);
  assert.deepEqual(status.missing, SHARED_PRE_SCAFFOLD_GATES);
});
