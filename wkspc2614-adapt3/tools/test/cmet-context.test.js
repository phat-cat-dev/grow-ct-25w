'use strict';

// Tests for cmet-context.js. Node's built-in test runner, no dependencies.
// Run with: node --test tools/test/cmet-context.test.js
//
// tools/context-cmet is a private submodule and will not be populated on a
// fresh clone (git submodule update --init at the true repo root is needed).
// Tests that depend on the submodule's real data are skip-guarded on
// cmetAvailable() so the suite still passes when it is absent; the
// missing-submodule and unknown-command gap paths do not depend on it and
// always run.

const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');

const TOOL = path.join(__dirname, '..', 'cmet-context.js');
const cmetContext = require(TOOL);

const SUBMODULE_PRESENT = cmetContext.cmetAvailable();
const MISSING_BIN = path.join(__dirname, 'fixtures', 'does-not-exist.js');

// 1. A known HECoS code resolves, with cmetDataVersion present.
test('a known HECoS code resolves, with cmetDataVersion present', { skip: !SUBMODULE_PRESENT }, () => {
  const result = cmetContext.lookupCmetContext('100484');
  assert.equal(result.gap, null);
  assert.equal(result.resolved.subject.code, '100484');
  assert.equal(result.resolved.subject.label, 'criminology');
  assert.ok(typeof result.cmetDataVersion === 'string' && result.cmetDataVersion.length > 0);
  assert.ok(Array.isArray(result.benchmark.benchmarks));
});

// 2. An ambiguous text input returns a gap carrying candidates, not a crash.
test('an ambiguous subject returns a gap with candidates, not a crash', { skip: !SUBMODULE_PRESENT }, () => {
  const result = cmetContext.lookupCmetContext('fine art');
  assert.equal(result.resolved, null);
  assert.equal(result.benchmark, null);
  assert.equal(result.gap.type, 'no-cmet-match');
  assert.ok(Array.isArray(result.gap.candidates));
  assert.ok(result.gap.candidates.length > 0);
});

// 3. An unknown subcommand surfaces gap.type 'cmet-unknown-command' (the
// submodule's exit-code-2 path), distinct from a plain no-match. Does not
// need the submodule's data, only its presence, to tell exit 2 from exit 1.
test('an unknown subcommand surfaces cmet-unknown-command, not a no-match', { skip: !SUBMODULE_PRESENT }, () => {
  const result = cmetContext.run(['bogus-command']);
  assert.equal(result.ok, false);
  assert.equal(result.gap, 'unknown-command');
});

// 4. A missing submodule yields the probe gap, not a crash, regardless of
// whether the real submodule happens to be populated in this checkout.
test('a missing submodule binary yields the cmet-not-populated gap', () => {
  assert.equal(cmetContext.cmetAvailable(MISSING_BIN), false);
  const result = cmetContext.lookupCmetContext('100484', { bin: MISSING_BIN });
  assert.equal(result.resolved, null);
  assert.equal(result.benchmark, null);
  assert.equal(result.gap.type, 'cmet-not-populated');
  assert.match(result.gap.detail, /git submodule update --init/);
});

// 5. Pathway pass-through: a valid pathway is accepted and an unknown one is
// a miss, not a guess - cmet-context.js never invents a pathway mapping.
test('a valid pathway id is accepted and passed through', { skip: !SUBMODULE_PRESENT }, () => {
  const result = cmetContext.lookupCmetContext('100484', { pathway: 'criticality' });
  assert.equal(result.gap, null);
  assert.equal(result.resolved.pathway, 'criticality');
  assert.equal(result.benchmark.pathway.id, 'criticality');
});

test('an unknown pathway id is a miss, not a guess', { skip: !SUBMODULE_PRESENT }, () => {
  const result = cmetContext.lookupCmetContext('100484', { pathway: 'not-a-real-pathway' });
  assert.equal(result.resolved, null);
  assert.equal(result.gap.type, 'no-cmet-match');
  assert.match(result.gap.detail, /No pathway/);
});
