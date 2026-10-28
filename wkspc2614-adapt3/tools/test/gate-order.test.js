'use strict';

// Tests for gate-order.js. Node's built-in test runner, no dependencies.
// Run with: node --test tools/test/

const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');

const TOOL = path.join(__dirname, '..', 'gate-order.js');
const FIXTURES = path.join(__dirname, 'fixtures');
const gateOrder = require(TOOL);

const REAL_STORE = path.join(__dirname, '..', '..', 'design-kb', 'design-kb.gates.json');
const SMALL_FIXTURE = path.join(FIXTURES, 'gates-small.json');
const MISSING_GATE_FIXTURE = path.join(FIXTURES, 'gates-missing-gate.json');

// RJ-0059 test 1: the tool reads a planted store (not just the repo's own).
// RJ-0108 C (adp-0230) renamed this fixture's CTX, A1, A2 and S1 entries
// to their new ids (gates-small.json), so the order this test asserts
// changes with it; B1 is unrenamed (split target) and keeps its id.
test('reads a planted store and computes its order', () => {
  const store = gateOrder.loadStore(SMALL_FIXTURE);
  const order = gateOrder.getOrder(store).map(g => g.id);
  assert.deepEqual(order, ['crs-01_course-facets', 'crs-03_vocabulary', 'crs-02_thematic-scope', 'gates/B1', 'act-04_summative-activities']);
});

test('reads flags from a planted store', () => {
  const store = gateOrder.loadStore(SMALL_FIXTURE);
  assert.deepEqual(gateOrder.getFlags(store, 'gates/B1'), {
    repeatsPer: 'lesson',
    procedureFlags: { candidates: true }
  });
  assert.deepEqual(gateOrder.getFlags(store, 'act-04_summative-activities'), {
    repeatsPer: null,
    procedureFlags: {}
  });
});

// RJ-0059 test 2: a command's named check (checkSequenceContiguous, via
// getOrder/getPhaseAClosureSet) fails on a planted store with a gate
// missing: the deleted gate (crs-02_thematic-scope, renamed from A2 by
// RJ-0108 B, adp-0230) leaves a sequence gap.
test('named check fails on a planted store with a gate missing', () => {
  const store = gateOrder.loadStore(MISSING_GATE_FIXTURE);
  assert.throws(
    () => gateOrder.checkSequenceContiguous(store),
    /sequence gap at 2/
  );
  assert.throws(
    () => gateOrder.getPhaseAClosureSet(store),
    /sequence gap at 2/
  );
});

// RJ-0059 test 3: the closure set on the real store, post-RJ-0108 B
// (adp-0230). RJ-0108 B renamed 8 of the 11 gates this test previously
// listed (CTX, A1, A2, CO, OBK, A4, A5, A6) off phase "A" entirely, onto
// CRS, LES or ACT; gate-order.js itself is unchanged (out of scope,
// adp-0230 rule 6) and still filters on the literal phase "A", so the
// closure set it computes now shrinks to the 3 gates ADP-19 to ADP-36
// left on phase "A" unrenamed: EXM (parked, store unchanged), A3
// (merged, store unchanged) and A7 (open, D-0090, store unchanged). This
// is a real behavioural narrowing of gate-order.js's own closure-set
// semantics, not a test bug; named in adp-0230's report as a fault this
// job does not fix (tools/gate-order.js is out of scope to change).
// Gate realignment (Round D, 7 Oct 2026): closure-set generalised to take a
// phase argument now that phases are ONB|CXS|CRS|LES|WRA|CXP. The ONB closure
// set on the realigned real store is the four onboarding gates, in order.
test('ONB closure set on the real store is the four onboarding gates, in order', () => {
  const store = gateOrder.loadStore(REAL_STORE);
  const closureSet = gateOrder.getPhaseClosureSet(store, 'ONB');
  assert.deepEqual(closureSet, ['onb-01_theme-preset', 'onb-02_course-theme', 'onb-03_pitch', 'onb-04_naming']);
});

// RJ-0059 test 4: a run that reaches no store fails.
test('a run that reaches no store fails', () => {
  assert.throws(
    () => gateOrder.loadStore(path.join(FIXTURES, 'does-not-exist.json')),
    /no store at/
  );
});

// RJ-0108 B (adp-0230) rebuilt the store from 21 to 30 gates: 9 renamed
// (ADP-19 to ADP-36), 9 new (hardness advisory, defaultType none per
// ADP-38), 12 left in their old id and relative order (merged, split,
// parked, retired, open). 30 is the rebuilt count, not the count this
// test asserted before that commit. The running order now opens on
// ctx-01 (CTX, asked before CRS per the gate map's own running order)
// and still closes on gates/D1 (retired, store write deferred per the
// gate map, sequence unchanged in relative terms, now last at 29).
// Gate realignment (Round C/D, 7 Oct 2026): the realigned store has 21 gates
// across six phases; the order opens on onb-01_theme-preset and closes on
// cxp-04_context-generation. Updated 8 Oct 2026: two post-scaffold WRA
// authoring gates (wra-03_summative, wra-04_confidence) were added (Abbott),
// raising the count to 23; then the reserved cxs-06_resources placeholder
// was added (Abbott: resources drawer in CXS), raising it to 24. The open
// and close gates are unchanged.
test('CLI --order prints the real store\'s full order, exit 0', () => {
  const { execFileSync } = require('node:child_process');
  const out = execFileSync('node', [TOOL, '--order'], { encoding: 'utf8' });
  const parsed = JSON.parse(out);
  assert.equal(parsed.length, 24);
  assert.equal(parsed[0], 'onb-01_theme-preset');
  assert.equal(parsed[parsed.length - 1], 'cxp-04_context-generation');
});

test('CLI with no store fails with exit 1, named error on stderr', () => {
  const { execFileSync } = require('node:child_process');
  try {
    execFileSync('node', [TOOL, '--order', '--store=/tmp/no-such-gate-store.json'], { encoding: 'utf8' });
    assert.fail('expected a non-zero exit');
  } catch (e) {
    assert.equal(e.status, 1);
    assert.match(e.stderr, /no store at/);
  }
});
