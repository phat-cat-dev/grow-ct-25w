'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');

const { consult, consultBenchmark, groupKeyFor } = require('../consult-maps.js');

const FIXTURES = path.join(__dirname, 'fixtures', 'consult-maps');
const OPTS = {
  benchmarkIndexPath: path.join(FIXTURES, 'benchmark-index.json'),
  mapIndexPath: path.join(FIXTURES, 'map-index.json'),
  mapsDir: path.join(FIXTURES, 'maps'),
};

const EMPTY_FIXTURES = path.join(__dirname, 'fixtures', 'consult-maps-empty');
const EMPTY_OPTS = {
  benchmarkIndexPath: path.join(EMPTY_FIXTURES, 'benchmark-index.json'),
  mapIndexPath: path.join(EMPTY_FIXTURES, 'map-index.json'),
  mapsDir: path.join(EMPTY_FIXTURES, 'maps'),
};

test('groupKeyFor prefixes path-, never adapt-', () => {
  assert.equal(groupKeyFor('fixture-pathway'), 'path-fixture-pathway');
});

test('a confirmed map: only confirmed statements surface, proposed ones excluded, no extract anywhere', () => {
  const result = consultBenchmark('fixture-confirmed-benchmark', 'fixture-pathway', OPTS);
  assert.equal(result.gap, null);
  assert.equal(result.confirmedPairs.length, 2);
  for (const pair of result.confirmedPairs) {
    assert.ok(!('extract' in pair));
    assert.ok(!('orientationExtract' in pair));
  }
  const withFields = result.confirmedPairs.find((p) => p.chunkId === 'fixture/benchmark/1.1');
  assert.equal(withFields.studentFacingStatement, 'Fixture student-facing statement, second person.');
  assert.equal(withFields.whyItMatters, 'Fixture why-it-matters line.');
  assert.equal(withFields.scopeElement, 'fixture-scope-element');
  assert.ok(!('fieldsMissing' in withFields));

  const withoutFields = result.confirmedPairs.find((p) => p.chunkId === 'fixture/benchmark/1.2');
  assert.equal(withoutFields.studentFacingStatement, null);
  assert.equal(withoutFields.whyItMatters, null);
  assert.equal(withoutFields.scopeElement, null);
  assert.deepEqual(withoutFields.fieldsMissing, ['studentFacingStatement', 'whyItMatters', 'scopeElement']);
});

test('an empty group: statements array present but empty yields gap empty-group', () => {
  const result = consultBenchmark('fixture-empty-group-benchmark', 'fixture-pathway', OPTS);
  assert.equal(result.gap.type, 'empty-group');
  assert.equal(result.confirmedPairs.length, 0);
});

test('a map with only proposed pairs yields gap no-confirmed-pairs (mirrors the real psychology-2023 map)', () => {
  const result = consultBenchmark('fixture-proposed-only-benchmark', 'fixture-pathway', OPTS);
  assert.equal(result.gap.type, 'no-confirmed-pairs');
  assert.equal(result.confirmedPairs.length, 0);
});

test('a missing map: benchmark is real but not indexed in the pathways map index yields gap no-map', () => {
  const result = consultBenchmark('fixture-no-map-benchmark', 'fixture-pathway', OPTS);
  assert.equal(result.gap.type, 'no-map');
  assert.equal(result.confirmedPairs.length, 0);
});

test('a benchmark not in the standards benchmark index at all yields gap no-benchmark', () => {
  const result = consultBenchmark('fixture-unknown-benchmark', 'fixture-pathway', OPTS);
  assert.equal(result.gap.type, 'no-benchmark');
  assert.equal(result.confirmedPairs.length, 0);
});

test('a superseded map yields gap map-not-active, never reads its groups', () => {
  const result = consultBenchmark('fixture-superseded-benchmark', 'fixture-pathway', OPTS);
  assert.equal(result.gap.type, 'map-not-active');
  assert.match(result.gap.detail, /superseded/);
  assert.equal(result.confirmedPairs.length, 0);
});

test('an active map whose groups still use the old adapt- prefix yields gap no-group, not a forced match', () => {
  const result = consultBenchmark('fixture-wrong-prefix-benchmark', 'fixture-pathway', OPTS);
  assert.equal(result.gap.type, 'no-group');
  assert.match(result.gap.detail, /path-fixture-pathway/);
  assert.equal(result.confirmedPairs.length, 0);
});

test('consult() builds one bundle across several benchmark ids, tier carried but not applied as a filter', () => {
  const bundle = consult(
    ['fixture-confirmed-benchmark', 'fixture-proposed-only-benchmark'],
    'fixture-pathway',
    'introductory',
    OPTS
  );
  assert.equal(bundle.pathwayId, 'fixture-pathway');
  assert.equal(bundle.tier, 'introductory');
  assert.equal(bundle.tierFilterApplied, false);
  assert.match(bundle.tierNote, /not applied/);
  assert.equal(bundle.benchmarks.length, 2);
  assert.equal(bundle.benchmarks[0].gap, null);
  assert.equal(bundle.benchmarks[1].gap.type, 'no-confirmed-pairs');
});

test('a run that reaches no fixtures at all fails explicitly (planted empty fixture set)', () => {
  const bundle = consult(['anything'], 'fixture-pathway', 'introductory', EMPTY_OPTS);
  assert.equal(bundle.gap.type, 'no-sources');
  assert.equal(bundle.benchmarks.length, 0);
});

test('consult() with no benchmark ids fails explicitly too', () => {
  const bundle = consult([], 'fixture-pathway', 'introductory', OPTS);
  assert.equal(bundle.gap.type, 'no-sources');
});

test('real repo data: the real psychology-2023 map reports a gap, not confirmed pairs, group key mismatch expected', () => {
  const result = consultBenchmark('psychology-2023', 'starting-progressing-succeeding');
  // The real map is indexed with status "superseded" (mapping/index.json),
  // so map-not-active fires before any group lookup is attempted. This is
  // the gap RULINGS 3 point (4) anticipated ("the map superseded"), not
  // "no confirmed pairs" - recorded here as the proof, not forced to match
  // the job row's illustrative wording.
  assert.equal(result.gap.type, 'map-not-active');
  assert.match(result.gap.detail, /superseded/);
  assert.equal(result.confirmedPairs.length, 0);
});
