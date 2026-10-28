#!/usr/bin/env node
'use strict';

/**
 * consult-maps.js - benchmark ids, a pathway id and a tier in; for each
 * benchmark, the map's group for path-<pathway-id>: confirmed pairs only,
 * and the gaps, as one JSON bundle.
 *
 * Landed: adp-0214, RJ-0049, point (2).
 *
 * Per statement pair, carries: studentFacingStatement, whyItMatters,
 * scopeElement, strength, chunkId, agentInstruction. No extract and no
 * benchmark text anywhere in the bundle (SFS-1): this tool never reads
 * or copies a statement's extract/orientationExtract field into any
 * output.
 *
 * studentFacingStatement, whyItMatters and scopeElement do not exist on
 * any committed statement yet. Checked directly this job against
 * tools/pathways/core/rules/source-mapping-rules.md's Output Template
 * (section 6) and against the real psychology-2023 map's own JSON:
 * neither defines or carries any of the three. SFS-1
 * (docs/project/open-decisions.md, 1 October 2026) requires
 * studentFacingStatement but postdates the rules document and has not
 * been built into it; "scope element" has no field definition anywhere
 * in the repo. This tool reads each field from a statement if present
 * (so a future schema version, or a test fixture, can supply it) and
 * reports null plus the field's name in that pair's fieldsMissing array
 * when it is absent, rather than inventing a value.
 *
 * Looks the group up strictly by the key path-<pathway-id>, per RULINGS
 * 3 (adp-0214, RJ-0049): never falls back to an adapt-<pathway-id> key.
 * No committed map uses the path- prefix yet (D-0045's rename is ruled,
 * not landed, pending RJ-0033), so a real run against a real map
 * reports a "no-group" gap, not "no confirmed pairs" - this is expected
 * and is not a bug to fix here; no committed map is changed by this
 * tool.
 *
 * Tier is carried into the bundle as given. No ruled capability cards
 * are committed (checked this job: no file under any capability-card
 * location exists), so tier filtering is never applied; the bundle
 * states this explicitly rather than silently dropping, or silently
 * keeping, any tier's statements.
 *
 * Nothing in tools/pathways/core/ names a consuming project (PCP-1).
 */

const fs = require('fs');
const path = require('path');

const REPO_ROOT = path.resolve(__dirname, '..', '..', '..', '..');

const DEFAULT_BENCHMARK_INDEX_PATH = path.join(
  REPO_ROOT,
  'tools',
  'standards',
  'core',
  'qaa',
  'benchmarks',
  'index.json'
);

const DEFAULT_MAP_INDEX_PATH = path.join(
  REPO_ROOT,
  'tools',
  'pathways',
  'core',
  'mapping',
  'index.json'
);

const DEFAULT_MAPS_DIR = path.join(REPO_ROOT, 'tools', 'pathways', 'core', 'mapping');

const SFS1_FIELDS = ['studentFacingStatement', 'whyItMatters', 'scopeElement'];

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

function loadJsonArray(filePath) {
  if (!fs.existsSync(filePath)) return [];
  const raw = readJson(filePath);
  return Array.isArray(raw) ? raw : [];
}

function groupKeyFor(pathwayId) {
  return 'path-' + pathwayId;
}

/**
 * Builds the confirmed-pair entry for one statement, reading the three
 * SFS-1 fields if present and recording which are missing rather than
 * inventing a value. Never includes extract or orientationExtract.
 */
function buildConfirmedPair(statement) {
  const pair = {
    chunkId: statement.chunkId || null,
    strength: statement.strength || null,
    agentInstruction: statement.agentInstruction || null,
  };
  const fieldsMissing = [];
  for (const field of SFS1_FIELDS) {
    if (Object.prototype.hasOwnProperty.call(statement, field)) {
      pair[field] = statement[field];
    } else {
      pair[field] = null;
      fieldsMissing.push(field);
    }
  }
  if (fieldsMissing.length > 0) {
    pair.fieldsMissing = fieldsMissing;
  }
  return pair;
}

/**
 * Consults one benchmark for one pathway. Returns:
 *   { benchmarkId, gap: null | { type, detail }, confirmedPairs: [...] }
 * gap.type is one of: no-benchmark, no-map, map-not-active, no-group,
 * empty-group, no-confirmed-pairs. confirmedPairs is [] whenever gap is
 * not null.
 */
function consultBenchmark(benchmarkId, pathwayId, options = {}) {
  const benchmarkIndexPath = options.benchmarkIndexPath || DEFAULT_BENCHMARK_INDEX_PATH;
  const mapIndexPath = options.mapIndexPath || DEFAULT_MAP_INDEX_PATH;
  const mapsDir = options.mapsDir || DEFAULT_MAPS_DIR;

  const benchmarkEntries = loadJsonArray(benchmarkIndexPath);
  const knownBenchmark = benchmarkEntries.some((e) => e.slug === benchmarkId);
  if (!knownBenchmark) {
    return {
      benchmarkId,
      gap: {
        type: 'no-benchmark',
        detail: `"${benchmarkId}" is not a benchmark in ${benchmarkIndexPath}.`,
      },
      confirmedPairs: [],
    };
  }

  const mapEntries = loadJsonArray(mapIndexPath);
  const mapEntry = mapEntries.find((e) => e.slug === benchmarkId);
  if (!mapEntry) {
    return {
      benchmarkId,
      gap: {
        type: 'no-map',
        detail: `No pathways map is indexed for benchmark "${benchmarkId}" in ${mapIndexPath}.`,
      },
      confirmedPairs: [],
    };
  }

  if (mapEntry.status !== 'active') {
    return {
      benchmarkId,
      gap: {
        type: 'map-not-active',
        detail:
          `The map indexed for "${benchmarkId}" has status "${mapEntry.status}", not "active". ` +
          `Not read further.`,
      },
      confirmedPairs: [],
    };
  }

  const mapFilePath = path.join(mapsDir, mapEntry.file);
  if (!fs.existsSync(mapFilePath)) {
    return {
      benchmarkId,
      gap: {
        type: 'no-map',
        detail: `Map index names file "${mapEntry.file}" for "${benchmarkId}", but it does not exist at ${mapFilePath}.`,
      },
      confirmedPairs: [],
    };
  }

  const map = readJson(mapFilePath);
  const groupKey = groupKeyFor(pathwayId);
  const group = map.pathways ? map.pathways[groupKey] : undefined;
  if (!group) {
    return {
      benchmarkId,
      gap: {
        type: 'no-group',
        detail:
          `No group found at key "${groupKey}" in "${benchmarkId}"'s map. ` +
          `(This map's own tagPrefix is "${map.tagPrefix || 'unknown'}"; the path- key rename, ` +
          `D-0045, is ruled but not yet landed on any committed map.)`,
      },
      confirmedPairs: [],
    };
  }

  const statements = Array.isArray(group.statements) ? group.statements : [];
  if (statements.length === 0) {
    return {
      benchmarkId,
      gap: {
        type: 'empty-group',
        detail: `Group "${groupKey}" in "${benchmarkId}"'s map has no statements.`,
      },
      confirmedPairs: [],
    };
  }

  const confirmed = statements.filter((s) => s.status === 'confirmed');
  if (confirmed.length === 0) {
    return {
      benchmarkId,
      gap: {
        type: 'no-confirmed-pairs',
        detail: `Group "${groupKey}" in "${benchmarkId}"'s map has ${statements.length} statement(s), none confirmed.`,
      },
      confirmedPairs: [],
    };
  }

  return {
    benchmarkId,
    gap: null,
    confirmedPairs: confirmed.map(buildConfirmedPair),
  };
}

/**
 * The full consultation bundle for one pathway and tier, across every
 * benchmark id given. If benchmarkIds is empty, or both the benchmark
 * index and the map index load to zero entries, this is a run that
 * reaches no fixtures: it fails explicitly via a top-level gap, never a
 * silent empty bundle.
 */
function consult(benchmarkIds, pathwayId, tier, options = {}) {
  const benchmarkIndexPath = options.benchmarkIndexPath || DEFAULT_BENCHMARK_INDEX_PATH;
  const mapIndexPath = options.mapIndexPath || DEFAULT_MAP_INDEX_PATH;
  const mapsDir = options.mapsDir || DEFAULT_MAPS_DIR;

  const bundle = {
    pathwayId,
    tier,
    tierFilterApplied: false,
    tierNote:
      'Tier filtering was not applied. No ruled capability cards are committed yet, ' +
      'so there is no tierNote to filter statements against; every confirmed pair for ' +
      'this pathway and these benchmarks is included regardless of tier.',
    benchmarks: [],
  };

  const benchmarkEntries = loadJsonArray(benchmarkIndexPath);
  const mapEntries = loadJsonArray(mapIndexPath);

  if (!Array.isArray(benchmarkIds) || benchmarkIds.length === 0) {
    bundle.gap = {
      type: 'no-sources',
      detail: 'No benchmark ids were given: no consultation is possible.',
    };
    return bundle;
  }

  if (benchmarkEntries.length === 0 && mapEntries.length === 0) {
    bundle.gap = {
      type: 'no-sources',
      detail:
        `Both the benchmark index (${benchmarkIndexPath}) and the map index ` +
        `(${mapIndexPath}) loaded to zero entries: no consultation is possible.`,
    };
    return bundle;
  }

  for (const benchmarkId of benchmarkIds) {
    bundle.benchmarks.push(
      consultBenchmark(benchmarkId, pathwayId, { benchmarkIndexPath, mapIndexPath, mapsDir })
    );
  }
  return bundle;
}

module.exports = {
  REPO_ROOT,
  DEFAULT_BENCHMARK_INDEX_PATH,
  DEFAULT_MAP_INDEX_PATH,
  DEFAULT_MAPS_DIR,
  SFS1_FIELDS,
  readJson,
  loadJsonArray,
  groupKeyFor,
  buildConfirmedPair,
  consultBenchmark,
  consult,
};

if (require.main === module) {
  const args = process.argv.slice(2);
  const benchmarkIds = [];
  let pathwayId = null;
  let tier = null;
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--pathway') {
      pathwayId = args[++i];
    } else if (args[i] === '--tier') {
      tier = args[++i];
    } else {
      benchmarkIds.push(args[i]);
    }
  }
  if (!pathwayId || benchmarkIds.length === 0) {
    process.stderr.write(
      'Usage: node consult-maps.js <benchmark-id> [<benchmark-id> ...] --pathway <pathway-id> [--tier <tier>]\n'
    );
    process.exit(1);
  }
  const bundle = consult(benchmarkIds, pathwayId, tier);
  process.stdout.write(JSON.stringify(bundle, null, 2) + '\n');
  process.exit(bundle.gap ? 1 : 0);
}
