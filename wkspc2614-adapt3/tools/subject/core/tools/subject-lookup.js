#!/usr/bin/env node
'use strict';

/**
 * subject-lookup.js - a HECoS or CAH code in, the benchmarks that cover it
 * out, most specific CAH level first, each with its match level.
 *
 * Landed: adp-0214, RJ-0049, point (1).
 *
 * Reads tools/standards/core/qaa/benchmarks/index.json first and, for any
 * benchmark entry that carries an optional subjectTags field (hecos/cah3/
 * cah2/cah1 arrays of codes that benchmark is tagged against), treats a
 * code found there as a "tagged" match - this is M2 (benchmark-level HESA
 * tagging). Checked directly against the committed index.json this job:
 * no entry carries subjectTags yet, so M2 has not run for any benchmark.
 * subjectTags is this tool's own extension point for M2's future output,
 * not an existing field copied from anywhere; nothing in the repo defines
 * its shape today, so this tool defines it here, once, for M2 to fill in
 * later, and reports a "tagged" match only if some future entry uses it.
 *
 * Until M2 runs for a given benchmark, this tool falls back to a stated
 * lookup file for that benchmark, read from a directory of such files
 * (default tools/subject/core/data/). A stated lookup file is hand-built,
 * quoting codes and labels directly from cah.json/hecos.json (never from
 * memory), one benchmark per file. Only psychology-2023 has one today
 * (stated-lookup-psychology.json). A match found this way is marked
 * "stated", never "tagged".
 *
 * This tool matches a queried code only against entries whose own code is
 * an exact match (no ancestor or descendant expansion): a stated lookup
 * file lists the benchmark explicitly against every CAH1/CAH2/CAH3/HECoS
 * code in that subject's own lineage, so an exact-code match already
 * covers every level a caller might query at. Ancestor/descendant
 * expansion across codes NOT already listed in a stated file is not
 * built; nothing in RULINGS 3 or the job row asks for it, and inventing
 * it would be undocumented behaviour beyond what was asked.
 *
 * Nothing in tools/subject/core/ names a consuming project (PCP-1/TLS-1).
 */

const fs = require('fs');
const path = require('path');

const REPO_ROOT = path.resolve(__dirname, '..', '..', '..', '..');

const DEFAULT_BENCHMARK_INDEX = path.join(
  REPO_ROOT,
  'tools',
  'standards',
  'core',
  'qaa',
  'benchmarks',
  'index.json'
);

const DEFAULT_STATED_DIR = path.join(REPO_ROOT, 'tools', 'subject', 'core', 'data');

// Most specific first. A HECoS code is finer-grained than any CAH level
// (many HECoS codes can share one CAH3), so it ranks above cah3.
const MATCH_LEVEL_RANK = { hecos: 4, cah3: 3, cah2: 2, cah1: 1 };

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

/**
 * Loads the benchmark index and returns, per benchmark, any subjectTags
 * entries found (the M2 tagged path). Returns an empty array if the file
 * is missing or empty - a missing/empty benchmark index is a gap, not an
 * error, since RJ-0049's fixtures must be able to plant one deliberately.
 */
function loadBenchmarkIndex(indexPath = DEFAULT_BENCHMARK_INDEX) {
  if (!fs.existsSync(indexPath)) {
    return [];
  }
  const raw = readJson(indexPath);
  if (!Array.isArray(raw)) {
    return [];
  }
  return raw;
}

/**
 * Finds a tagged (M2) match for code across every benchmark index entry's
 * optional subjectTags field. Returns null if no entry tags this code.
 */
function findTaggedMatch(code, benchmarkIndexEntries) {
  for (const entry of benchmarkIndexEntries) {
    const tags = entry.subjectTags;
    if (!tags || typeof tags !== 'object') continue;
    for (const level of Object.keys(MATCH_LEVEL_RANK)) {
      const list = tags[level];
      if (Array.isArray(list) && list.includes(code)) {
        return {
          benchmark: entry.slug,
          matchLevel: level,
          source: 'tagged',
        };
      }
    }
  }
  return null;
}

/**
 * Loads every *.json stated lookup file in dir (default
 * tools/subject/core/data/) and returns a flat array of
 * { code, matchLevel, benchmark, label } entries, one per code any file
 * lists. A dir that does not exist, or contains no usable stated lookup
 * file, yields an empty array - the caller (lookupSubject) must then
 * report a gap, not silently return no result.
 */
function loadStatedLookupFiles(dir = DEFAULT_STATED_DIR) {
  const results = [];
  if (!fs.existsSync(dir)) {
    return results;
  }
  const files = fs
    .readdirSync(dir)
    .filter((f) => f.startsWith('stated-lookup-') && f.endsWith('.json'));
  for (const file of files) {
    const data = readJson(path.join(dir, file));
    if (!data || !Array.isArray(data.entries) || !data.benchmark) continue;
    for (const entry of data.entries) {
      if (!entry.code || !entry.codeType) continue;
      results.push({
        code: entry.code,
        matchLevel: entry.codeType,
        benchmark: data.benchmark,
        label: entry.label || null,
      });
    }
  }
  return results;
}

/**
 * The lookup itself. code: a HECoS or CAH code, as it appears in
 * cah.json/hecos.json. Returns:
 *   { input, benchmarks: [ { benchmark, matchLevel, label, source } ],
 *     gap: null | { type, detail } }
 * benchmarks is sorted most specific match level first. If no match is
 * found anywhere (tagged or stated), benchmarks is [] and gap explains
 * why: "no-tag-no-stated" if both sources were loaded but neither covers
 * the code, or "no-sources" if neither a benchmark index nor any stated
 * lookup file could be loaded at all (the empty-fixture-set case).
 */
function lookupSubject(code, options = {}) {
  const benchmarkIndexPath = options.benchmarkIndexPath || DEFAULT_BENCHMARK_INDEX;
  const statedDir = options.statedDir || DEFAULT_STATED_DIR;

  const benchmarkIndexEntries = loadBenchmarkIndex(benchmarkIndexPath);
  const statedEntries = loadStatedLookupFiles(statedDir);

  if (benchmarkIndexEntries.length === 0 && statedEntries.length === 0) {
    return {
      input: code,
      benchmarks: [],
      gap: {
        type: 'no-sources',
        detail:
          'Neither the benchmark index nor any stated lookup file could be loaded ' +
          '(' + benchmarkIndexPath + ', ' + statedDir + '): no lookup is possible.',
      },
    };
  }

  const tagged = findTaggedMatch(code, benchmarkIndexEntries);
  const matches = [];
  if (tagged) {
    matches.push(tagged);
  }
  for (const entry of statedEntries) {
    if (entry.code === code) {
      matches.push({
        benchmark: entry.benchmark,
        matchLevel: entry.matchLevel,
        label: entry.label,
        source: 'stated',
      });
    }
  }

  matches.sort((a, b) => MATCH_LEVEL_RANK[b.matchLevel] - MATCH_LEVEL_RANK[a.matchLevel]);

  if (matches.length === 0) {
    return {
      input: code,
      benchmarks: [],
      gap: {
        type: 'no-tag-no-stated',
        detail:
          'No benchmark index entry tags this code (M2), and no stated lookup file lists it. ' +
          'Not covered by any benchmark yet.',
      },
    };
  }

  return { input: code, benchmarks: matches, gap: null };
}

module.exports = {
  REPO_ROOT,
  DEFAULT_BENCHMARK_INDEX,
  DEFAULT_STATED_DIR,
  MATCH_LEVEL_RANK,
  readJson,
  loadBenchmarkIndex,
  findTaggedMatch,
  loadStatedLookupFiles,
  lookupSubject,
};

if (require.main === module) {
  const code = process.argv[2];
  if (!code) {
    process.stderr.write('Usage: node subject-lookup.js <hecos-or-cah-code>\n');
    process.exit(1);
  }
  const result = lookupSubject(code);
  process.stdout.write(JSON.stringify(result, null, 2) + '\n');
  process.exit(result.gap ? 1 : 0);
}
