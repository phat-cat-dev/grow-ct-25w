'use strict';

// Tests for validate-map.js. Node's built-in test runner, no dependencies.
// Run with: node --test tools/pathways/core/tools/test/

const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const { execFileSync } = require('node:child_process');

const TOOL = path.join(__dirname, '..', 'validate-map.js');
const FIXTURES = path.join(__dirname, 'fixtures');

function runCli(fixtureName, extraArgs) {
  const args = [TOOL, path.join(FIXTURES, fixtureName)].concat(extraArgs || []);
  try {
    const out = execFileSync('node', args, { encoding: 'utf8' });
    return { code: 0, stdout: out, stderr: '' };
  } catch (e) {
    return { code: e.status, stdout: e.stdout, stderr: e.stderr };
  }
}

test('good-map.json passes with exit 0', () => {
  const { code, stdout } = runCli('good-map.json');
  assert.equal(code, 0);
  assert.match(stdout, /^OK: /);
});

const failureCases = [
  { file: 'bad-shape.json', mustContain: 'shape: missing top-level field "mappedBy"' },
  { file: 'bad-tag.json', mustContain: 'is not "adapt-" plus a catalogue/pathways.json id' },
  { file: 'bad-count-mismatch.json', mustContain: 'coverage: "adapt-referencing".direct is 2, statements give 1' },
  { file: 'bad-blocktype.json', mustContain: "is not one of BM-1's 15" },
  { file: 'bad-status.json', mustContain: 'is not "proposed" or "confirmed"' },
  { file: 'chunkid-missing.json', mustContain: 'does not exist in the chunks file' },
  { file: 'chunkid-excluded.json', mustContain: 'is excluded in the chunks file' },
  { file: 'extract-not-verbatim.json', mustContain: 'does not appear verbatim in chunk' },
  { file: 'bad-wordcount.json', mustContain: 'must be 4 to 25' },
  { file: 'bad-hash.json', mustContain: "does not equal index's sha256" },
  { file: 'empty-map.json', mustContain: 'the map holds no statements at all' },
  { file: 'missing-coverage-entry.json', mustContain: 'missing entry for catalogue pathway "adapt-presenting"' },
  { file: 'summary-stale-basis.json', mustContain: 'summary.basis "qaa/fixture-subject-2026/1.2" is not the chunkId of a statement in pathway "adapt-referencing"' },
  { file: 'summary-stale-citation.json', mustContain: 'summary.text cites paragraph "1.2" which no statement in pathway "adapt-referencing" holds' },
];

for (const { file, mustContain } of failureCases) {
  test(`${file} fails with exit 1 and reports its defect`, () => {
    const { code, stderr } = runCli(file);
    assert.equal(code, 1);
    assert.ok(stderr.includes(mustContain), `expected stderr to include "${mustContain}", got:\n${stderr}`);
  });
}

// RJ-0046 point 2: a map index with 0 active entries must FAIL explicitly
// (exit 1), never a silent pass, since nothing was actually validated.
test('--index with 0 active maps fails explicitly, exit 1, never a silent pass', () => {
  const indexPath = path.join(FIXTURES, 'map-index-zero-active.json');
  try {
    const out = execFileSync('node', [TOOL, '--index', indexPath], { encoding: 'utf8' });
    assert.fail(`expected a non-zero exit, got exit 0 with stdout:\n${out}`);
  } catch (e) {
    assert.equal(e.status, 1);
    assert.match(e.stderr, /FAIL: 0 active maps/);
    assert.match(e.stderr, /1 total, 1 not active/);
    assert.match(e.stderr, /skipped: slug="fixture-subject-2026" status="superseded"/);
  }
});

test('checkNotEmpty passes when at least one statement exists', () => {
  const { checkNotEmpty } = require(TOOL);
  const failures = [];
  checkNotEmpty({ pathways: { 'adapt-referencing': { statements: [{}] } } }, failures);
  assert.equal(failures.length, 0);
});

test('wordCount counts whitespace-separated words', () => {
  const { wordCount } = require(TOOL);
  assert.equal(wordCount('one two three'), 3);
  assert.equal(wordCount('  spaced   out  words  '), 3);
  assert.equal(wordCount(''), 0);
});

test('collapseWhitespace collapses runs of whitespace to one space', () => {
  const { collapseWhitespace } = require(TOOL);
  assert.equal(collapseWhitespace('a\n\n  b   c'), 'a b c');
});

test('strength-warning.json passes in default mode and prints a warning', () => {
  const { code, stdout } = runCli('strength-warning.json');
  assert.equal(code, 0);
  assert.match(stdout, /^OK: /m);
  assert.match(stdout, /WARN: 1 strength warning/);
  assert.match(stdout, /chunkId="qaa\/fixture-subject-2026\/1\.1" pathway="adapt-creativity"/);
});

test('strength-warning.json fails with exit 1 under --strict', () => {
  const { code, stdout, stderr } = runCli('strength-warning.json', ['--strict']);
  assert.equal(code, 1);
  assert.match(stdout, /WARN: 1 strength warning/);
  assert.ok(stderr.includes('strength: pathways.adapt-creativity.statements[0] chunkId "qaa/fixture-subject-2026/1.1" is "direct" but its extract matches no pathway-term-lists.json pattern for "creativity"'));
});

test('good-map.json prints no strength warning in default mode', () => {
  const { code, stdout } = runCli('good-map.json');
  assert.equal(code, 0);
  assert.ok(!stdout.includes('WARN'));
});

test('good-map.json still passes under --strict', () => {
  const { code, stdout } = runCli('good-map.json', ['--strict']);
  assert.equal(code, 0);
  assert.match(stdout, /^OK: /m);
});

test('checkStrength warns (not fails) by default when extract matches no pattern', () => {
  const { checkStrength } = require(TOOL);
  const map = {
    pathways: {
      'adapt-creativity': {
        statements: [
          { chunkId: 'x/1', tag: 'adapt-creativity', strength: 'direct', extract: 'reference sources and academic integrity' },
        ],
      },
    },
  };
  const termLists = { pathways: { creativity: [{ pattern: '\\bcreativ\\w*', flags: 'i' }] } };
  const failures = [];
  const warnings = [];
  checkStrength(map, termLists, false, failures, warnings);
  assert.equal(failures.length, 0);
  assert.equal(warnings.length, 1);
  assert.deepEqual(warnings[0], { chunkId: 'x/1', tag: 'adapt-creativity', extract: 'reference sources and academic integrity' });
});

test('checkStrength also fails under strict when extract matches no pattern', () => {
  const { checkStrength } = require(TOOL);
  const map = {
    pathways: {
      'adapt-creativity': {
        statements: [
          { chunkId: 'x/1', tag: 'adapt-creativity', strength: 'direct', extract: 'reference sources and academic integrity' },
        ],
      },
    },
  };
  const termLists = { pathways: { creativity: [{ pattern: '\\bcreativ\\w*', flags: 'i' }] } };
  const failures = [];
  const warnings = [];
  checkStrength(map, termLists, true, failures, warnings);
  assert.equal(warnings.length, 1);
  assert.equal(failures.length, 1);
  assert.match(failures[0], /matches no pathway-term-lists\.json pattern for "creativity"/);
});

test('checkStrength does not warn when a direct extract matches its pathway pattern', () => {
  const { checkStrength } = require(TOOL);
  const map = {
    pathways: {
      'adapt-creativity': {
        statements: [
          { chunkId: 'x/1', tag: 'adapt-creativity', strength: 'direct', extract: 'a creative and innovative solution' },
        ],
      },
    },
  };
  const termLists = { pathways: { creativity: [{ pattern: '\\bcreativ\\w*', flags: 'i' }] } };
  const failures = [];
  const warnings = [];
  checkStrength(map, termLists, true, failures, warnings);
  assert.equal(warnings.length, 0);
  assert.equal(failures.length, 0);
});

test('checkStrength ignores indirect statements', () => {
  const { checkStrength } = require(TOOL);
  const map = {
    pathways: {
      'adapt-creativity': {
        statements: [
          { chunkId: 'x/1', tag: 'adapt-creativity', strength: 'indirect', extract: 'reference sources and academic integrity' },
        ],
      },
    },
  };
  const termLists = { pathways: { creativity: [{ pattern: '\\bcreativ\\w*', flags: 'i' }] } };
  const failures = [];
  const warnings = [];
  checkStrength(map, termLists, true, failures, warnings);
  assert.equal(warnings.length, 0);
  assert.equal(failures.length, 0);
});

// RJ-0028 / SRB-1: checkSummaryBasis must pass a citation that falls inside
// a range-paragraph chunk's locator, not just a chunk's own single paragraph.
test('checkSummaryBasis passes a range citation that falls inside a range-paragraph chunk', () => {
  const { checkSummaryBasis, buildParagraphsByChunkId } = require(TOOL);
  const chunks = [
    { chunkId: 'x/3.28-3.32', locator: { paragraphs: '3.28-3.32' } },
  ];
  const map = {
    pathways: {
      'adapt-referencing': {
        statements: [{ chunkId: 'x/3.28-3.32' }],
        summary: {
          basis: ['x/3.28-3.32'],
          text: 'Students reference sources appropriately (3.30).',
        },
      },
    },
  };
  const failures = [];
  checkSummaryBasis(map, buildParagraphsByChunkId(chunks), failures);
  assert.deepEqual(failures, []);
});

// RJ-0028 / SRB-1: a pathway with no statements and an empty summary basis
// (the real shape a zero-coverage pathway takes, not the literal "none")
// must pass without failures.
test('checkSummaryBasis passes a pathway with no statements and an empty basis', () => {
  const { checkSummaryBasis, buildParagraphsByChunkId } = require(TOOL);
  const chunks = [];
  const map = {
    pathways: {
      'adapt-creativity': {
        statements: [],
        summary: { basis: [], text: 'No creativity-pathway content was found in this source.' },
      },
    },
  };
  const failures = [];
  checkSummaryBasis(map, buildParagraphsByChunkId(chunks), failures);
  assert.deepEqual(failures, []);
});
