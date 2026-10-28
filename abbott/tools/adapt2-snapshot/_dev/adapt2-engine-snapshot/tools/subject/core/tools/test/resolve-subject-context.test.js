'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');

const { resolveSubjectContext, ancestorsAbove, readJson } = require('../resolve-subject-context.js');

const FIXTURE_DIR = path.join(__dirname, 'fixtures', 'resolve-subject-context');
const FIXTURE_CAH = path.join(FIXTURE_DIR, 'cah.json');
const FIXTURE_HECOS = path.join(FIXTURE_DIR, 'hecos.json');
const FIXTURE_OPTS = { cahPath: FIXTURE_CAH, hecosPath: FIXTURE_HECOS };

test('"universal" returns an unscoped context, never a blank subject, without reading either store', () => {
  // A bogus path proves neither store is touched for this input.
  const result = resolveSubjectContext('universal', {
    cahPath: path.join(FIXTURE_DIR, 'does-not-exist.json'),
    hecosPath: path.join(FIXTURE_DIR, 'does-not-exist.json'),
  });
  assert.equal(result.level, 'universal');
  assert.equal(result.scoped, false);
  assert.equal(result.code, null);
  assert.equal(result.label, null);
  assert.deepEqual(result.chain, []);
});

test('planted fixture: exact HECoS code resolves, chain is cah3, cah2, cah1 in that order', () => {
  const result = resolveSubjectContext('900001', FIXTURE_OPTS);
  assert.equal(result.level, 'hecos');
  assert.equal(result.scoped, true);
  assert.equal(result.code, '900001');
  assert.equal(result.label, 'fixture subject');
  assert.deepEqual(result.chain, [
    { level: 'cah3', code: 'CAH01-01-01', label: 'fixture narrow subject' },
    { level: 'cah2', code: 'CAH01-01', label: 'fixture middle subject' },
    { level: 'cah1', code: 'CAH01', label: 'fixture top subject' },
  ]);
});

test('planted fixture: HECoS nonPreferredTerms alias resolves by name, same as the code', () => {
  const result = resolveSubjectContext('fixture alias', FIXTURE_OPTS);
  assert.equal(result.level, 'hecos');
  assert.equal(result.code, '900001');
});

test('planted fixture: HECoS term name match is case-insensitive', () => {
  const result = resolveSubjectContext('FIXTURE SUBJECT', FIXTURE_OPTS);
  assert.equal(result.level, 'hecos');
  assert.equal(result.code, '900001');
});

test('planted fixture: exact CAH3 code resolves, chain is only the levels above it (cah2, cah1)', () => {
  const result = resolveSubjectContext('CAH01-01-01', FIXTURE_OPTS);
  assert.equal(result.level, 'cah3');
  assert.equal(result.code, 'CAH01-01-01');
  assert.equal(result.label, 'fixture narrow subject');
  assert.deepEqual(result.chain, [
    { level: 'cah2', code: 'CAH01-01', label: 'fixture middle subject' },
    { level: 'cah1', code: 'CAH01', label: 'fixture top subject' },
  ]);
});

test('planted fixture: a CAH code is matched case-insensitively', () => {
  const result = resolveSubjectContext('cah01-01-01', FIXTURE_OPTS);
  assert.equal(result.level, 'cah3');
  assert.equal(result.code, 'CAH01-01-01');
});

test('planted fixture: exact CAH2 code resolves, chain is only cah1', () => {
  const result = resolveSubjectContext('CAH01-01', FIXTURE_OPTS);
  assert.equal(result.level, 'cah2');
  assert.deepEqual(result.chain, [{ level: 'cah1', code: 'CAH01', label: 'fixture top subject' }]);
});

test('planted fixture: exact CAH1 code resolves, chain is empty (nothing is above cah1)', () => {
  const result = resolveSubjectContext('CAH01', FIXTURE_OPTS);
  assert.equal(result.level, 'cah1');
  assert.deepEqual(result.chain, []);
});

test('planted fixture: a CAH label name match works at cah1, case-insensitive', () => {
  const result = resolveSubjectContext('Fixture Top Subject', FIXTURE_OPTS);
  assert.equal(result.level, 'cah1');
  assert.equal(result.code, 'CAH01');
});

test('planted fixture: an unknown code or name fails by name, the thrown message quoting the exact input', () => {
  assert.throws(
    () => resolveSubjectContext('not-a-real-code-or-name', FIXTURE_OPTS),
    (err) => err instanceof Error && err.message === 'Unknown subject code or name: "not-a-real-code-or-name"'
  );
});

test('ancestorsAbove on a cah1 code returns empty directly, without a hecos lookup', () => {
  const cah = readJson(FIXTURE_CAH);
  assert.deepEqual(ancestorsAbove(cah, 'cah1', 'CAH01'), []);
});

test('real repo data: HECoS 100484 (criminology) resolves with its full CAH chain', () => {
  const result = resolveSubjectContext('100484');
  assert.equal(result.level, 'hecos');
  assert.equal(result.code, '100484');
  assert.equal(result.label, 'criminology');
  assert.deepEqual(result.chain, [
    { level: 'cah3', code: 'CAH15-01-02', label: 'sociology' },
    { level: 'cah2', code: 'CAH15-01', label: 'sociology, social policy and anthropology' },
    { level: 'cah1', code: 'CAH15', label: 'social sciences' },
  ]);
});

test('real repo data: HECoS 100486 (policing) resolves with its full CAH chain', () => {
  const result = resolveSubjectContext('100486');
  assert.equal(result.level, 'hecos');
  assert.equal(result.code, '100486');
  assert.equal(result.label, 'policing');
  assert.deepEqual(result.chain, [
    { level: 'cah3', code: 'CAH16-01-01', label: 'law' },
    { level: 'cah2', code: 'CAH16-01', label: 'law' },
    { level: 'cah1', code: 'CAH16', label: 'law' },
  ]);
});

test('real repo data: the subject name "criminology" resolves to the same HECoS code as 100484', () => {
  const result = resolveSubjectContext('criminology');
  assert.equal(result.level, 'hecos');
  assert.equal(result.code, '100484');
});

test('real repo data: "universal" against the real stores still returns unscoped, not a real code', () => {
  const result = resolveSubjectContext('universal');
  assert.equal(result.level, 'universal');
  assert.equal(result.scoped, false);
});

test('real repo data: an unknown HECoS-shaped code fails by name', () => {
  assert.throws(
    () => resolveSubjectContext('999999'),
    (err) => err instanceof Error && err.message === 'Unknown subject code or name: "999999"'
  );
});
