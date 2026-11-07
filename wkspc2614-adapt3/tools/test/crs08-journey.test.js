'use strict';

// Tests for the cross-tier learning journey pass on crs-08_progression
// (adp-cross-tier-journey-map plan, 4 Nov 2026). No new code to unit-test
// here - the capability is entirely decidedValueShape growth on the
// real store (design-kb/design-kb.gates.json), enforced free by SHP-1 once
// a shape is present. These tests prove that enforcement empirically
// against planted fixtures, the same way tools/validate-design-schemas.py
// is exercised elsewhere (CLI end-to-end, never a hardcoded reimplementation
// of its checks).
//
// Run with: node --test tools/test/crs08-journey.test.js

const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const { execFileSync } = require('node:child_process');

const VALIDATOR = path.join(__dirname, '..', 'validate-design-schemas.py');
const FIXTURES = path.join(__dirname, 'fixtures');
const GOOD_FIXTURE = path.join(FIXTURES, 'course-design-crs08-journey.json');
const BAD_FIXTURE = path.join(FIXTURES, 'course-design-crs08-journey-bad-grounding.json');

function runValidator(fixturePath) {
  try {
    const out = execFileSync('python3', [VALIDATOR, '--course-design', fixturePath], { encoding: 'utf8' });
    return { status: 0, stdout: out };
  } catch (err) {
    return { status: err.status, stdout: err.stdout || '' };
  }
}

// A closed crs-07_tiered-outcomes record plus a closed crs-08_progression
// record carrying a grounded journey (practice/knowledge/identity/
// ladderRows all present) and a grounded spreadReading (reading/basis
// both present): SHP-1 passes both records, exit 0.
test('SHP-1 passes a crs-08 record whose journey/spreadReading are grounded', () => {
  const result = runValidator(GOOD_FIXTURE);
  assert.equal(result.status, 0);
  assert.match(result.stdout, /SHP-1 PASS: crs-08_progression seq 1/);
  assert.match(result.stdout, /SHP-1: 2 closed record\(s\) checked against a decidedValueShape, 0 failed/);
  assert.match(result.stdout, /^PASS$/m);
});

// crs-08's provenance (ai-proposal-stood) must itself be GI-2-clean: soft
// hardness + ai-proposal-stands defaultType is exactly what ai-proposal-stood
// is reserved for. A mislabelled provenance here would make GI-2 reject the
// very record this plan's ruling 2 says lands on silence as ai-proposal-stood.
test('GI-2 accepts ai-proposal-stood on crs-08 (soft, ai-proposal-stands)', () => {
  const result = runValidator(GOOD_FIXTURE);
  assert.match(result.stdout, /GI-2 PASS: crs-08_progression seq 1 \(crs-08_progression\) provenance=ai-proposal-stood/);
});

// The sibling fixture: journey is present but ladderRows is missing.
// decidedValueShape's journey.required (["practice","knowledge","identity",
// "ladderRows"]) makes this an SHP-1 failure, not a silent pass - the
// "requires grounding when a journey block is present" compensation the
// plan names for crs-08 staying soft + ai-proposal-stands.
test('SHP-1 fails a crs-08 record whose journey is present but ladderRows is missing', () => {
  const result = runValidator(BAD_FIXTURE);
  assert.equal(result.status, 1);
  assert.match(result.stdout, /SHP-1 FAIL: crs-08_progression seq 1/);
  assert.match(result.stdout, /ladderRows' is a required property/);
  assert.match(result.stdout, /SHP-1: 2 closed record\(s\) checked against a decidedValueShape, 1 failed/);
  assert.match(result.stdout, /^FAIL - 1 error\(s\):$/m);
});
