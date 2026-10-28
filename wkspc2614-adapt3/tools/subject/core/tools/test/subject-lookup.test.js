'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');

const {
  lookupSubject,
  loadStatedLookupFiles,
  loadBenchmarkIndex,
  MATCH_LEVEL_RANK,
} = require('../subject-lookup.js');

const FIXTURES = path.join(__dirname, 'fixtures');
const STATED_OK = path.join(FIXTURES, 'stated-ok');
const STATED_EMPTY = path.join(FIXTURES, 'stated-empty');
const BM_PLAIN = path.join(FIXTURES, 'benchmark-index-plain', 'index.json');
const BM_TAGGED = path.join(FIXTURES, 'benchmark-index-tagged', 'index.json');
const BM_MISSING = path.join(FIXTURES, 'does-not-exist', 'index.json');

test('stated match: exact HECoS code, most specific level', () => {
  const result = lookupSubject('900001', {
    benchmarkIndexPath: BM_PLAIN,
    statedDir: STATED_OK,
  });
  assert.equal(result.gap, null);
  assert.equal(result.benchmarks.length, 1);
  assert.equal(result.benchmarks[0].benchmark, 'fixture-benchmark-2026');
  assert.equal(result.benchmarks[0].matchLevel, 'hecos');
  assert.equal(result.benchmarks[0].source, 'stated');
});

test('stated match: exact CAH1 code (least specific level, still an exact match)', () => {
  const result = lookupSubject('CAH99', {
    benchmarkIndexPath: BM_PLAIN,
    statedDir: STATED_OK,
  });
  assert.equal(result.gap, null);
  assert.equal(result.benchmarks[0].matchLevel, 'cah1');
});

test('tagged match (M2) takes the tagged source when a benchmark index entry carries subjectTags', () => {
  const result = lookupSubject('900002', {
    benchmarkIndexPath: BM_TAGGED,
    statedDir: STATED_EMPTY,
  });
  assert.equal(result.gap, null);
  assert.equal(result.benchmarks[0].source, 'tagged');
  assert.equal(result.benchmarks[0].benchmark, 'fixture-tagged-benchmark');
});

test('most specific level first when both a tagged and a stated match exist for the same code', () => {
  // FIXCODE-1 is planted in both fixtures: tagged at cah3 level (benchmark-index-tagged),
  // stated at hecos level (stated-ok). hecos outranks cah3, so the stated hecos
  // match must sort first even though the tagged match was found first in source order.
  const result = lookupSubject('FIXCODE-1', {
    benchmarkIndexPath: BM_TAGGED,
    statedDir: STATED_OK,
  });
  assert.equal(result.gap, null);
  assert.equal(result.benchmarks.length, 2);
  assert.equal(result.benchmarks[0].matchLevel, 'hecos');
  assert.equal(result.benchmarks[0].source, 'stated');
  assert.equal(result.benchmarks[1].matchLevel, 'cah3');
  assert.equal(result.benchmarks[1].source, 'tagged');
  assert.ok(MATCH_LEVEL_RANK.hecos > MATCH_LEVEL_RANK.cah3);
  assert.ok(MATCH_LEVEL_RANK.cah3 > MATCH_LEVEL_RANK.cah2);
  assert.ok(MATCH_LEVEL_RANK.cah2 > MATCH_LEVEL_RANK.cah1);
});

test('a subject with no benchmark: code not in any source yields a named gap, not a thrown error', () => {
  const result = lookupSubject('000000-not-a-real-code', {
    benchmarkIndexPath: BM_PLAIN,
    statedDir: STATED_OK,
  });
  assert.equal(result.benchmarks.length, 0);
  assert.equal(result.gap.type, 'no-tag-no-stated');
});

test('a run that reaches no fixtures at all fails explicitly (planted empty fixture set)', () => {
  const result = lookupSubject('100497', {
    benchmarkIndexPath: BM_MISSING,
    statedDir: STATED_EMPTY,
  });
  assert.equal(result.benchmarks.length, 0);
  assert.equal(result.gap.type, 'no-sources');
});

test('loadStatedLookupFiles on an existing but file-less directory returns an empty array, not an error', () => {
  const entries = loadStatedLookupFiles(STATED_EMPTY);
  assert.deepEqual(entries, []);
});

test('loadBenchmarkIndex on a missing path returns an empty array, not a thrown error', () => {
  const entries = loadBenchmarkIndex(BM_MISSING);
  assert.deepEqual(entries, []);
});

test('real repo data: HECoS 100497 (psychology) resolves to psychology-2023 via the stated path, M2 not run', () => {
  const result = lookupSubject('100497');
  assert.equal(result.gap, null);
  assert.equal(result.benchmarks.length, 1);
  assert.equal(result.benchmarks[0].benchmark, 'psychology-2023');
  assert.equal(result.benchmarks[0].matchLevel, 'hecos');
  assert.equal(result.benchmarks[0].source, 'stated');
});

test('real repo data: the committed benchmark index has no subjectTags field yet (M2 has not run)', () => {
  const entries = loadBenchmarkIndex();
  assert.ok(entries.length > 0);
  for (const entry of entries) {
    assert.equal(
      entry.subjectTags,
      undefined,
      'benchmark ' + entry.slug + ' unexpectedly carries subjectTags; M2 may have run, update this test'
    );
  }
});
