#!/usr/bin/env node
'use strict';

/**
 * resolve-subject-benchmark.js - a subject name or HECoS/CAH code in, the
 * matching subject-benchmark reference out (its id and file path), by
 * searching the subjects catalogue (catalogue/context/subject/benchmarks.json).
 *
 * This is the ADAPT-level "plug in" that connects the context-pack flow to the
 * subjects catalogue: the context-pack authoring agent resolves the subject it
 * is writing for to that subject's benchmark reference, and grounds the pack in
 * it (tier readings, statements, pathwayMapping, digest).
 *
 * It reuses the project-neutral core resolver (tools/subject/core/tools/
 * resolve-subject-context.js) to turn the input into a HECoS code + CAH chain,
 * then matches that code - most specific first (the resolved code, then its
 * cah3, cah2, cah1 ancestors) - against each catalogue entry's own codes[].
 * A direct subject-name match is tried if no code matches. This lives in
 * tools/ (not tools/subject/core/), which must not name a consuming project or
 * read its catalogue (TLS-1); the catalogue search is ADAPT's, so it sits here.
 *
 * Usage:
 *   node tools/resolve-subject-benchmark.js <subject-name-or-code> [--load]
 * --load also prints the resolved reference file's absolute path on its own
 * final line (for a caller to read), and exits non-zero if the file is missing.
 */

const fs = require('fs');
const path = require('path');
const { resolveSubjectContext } = require(
  './subject/core/tools/resolve-subject-context.js'
);

const REPO_ROOT = path.resolve(__dirname, '..');
const DEFAULT_INDEX = path.join(
  REPO_ROOT, 'catalogue', 'context', 'subject', 'benchmarks.json'
);
const RANK = { hecos: 4, cah3: 3, cah2: 2, cah1: 1, name: 0 };

// The baseline (universal) sibling: the shared core of the 54 subject
// benchmarks, which a baseline / unscoped context is grounded in instead of a
// single subject's statement. See tools/build-universal-benchmark.py.
const UNIVERSAL_ID = 'universal-reference';
const UNIVERSAL_FILE =
  'catalogue/context/subject/benchmarks/universal-reference.json';
// Inputs that explicitly select the baseline context rather than a subject.
const BASELINE_INPUTS = new Set(['baseline', 'universal', 'generic', 'none', '']);

function universalBenchmark(input, resolved) {
  return {
    input,
    resolved: resolved || null,
    benchmark: {
      id: UNIVERSAL_ID,
      file: UNIVERSAL_FILE,
      matchedCode: null,
      matchLevel: 'baseline',
    },
    gap: null,
  };
}

function readJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

/**
 * Resolve a subject to its catalogue benchmark entry.
 * Returns { input, resolved, benchmark, gap }. benchmark is
 * { id, file, matchedCode, matchLevel } or null; gap names why on a miss.
 * options.indexPath / cahPath / hecosPath override the defaults (tests).
 */
function resolveSubjectBenchmark(input, options = {}) {
  const indexPath = options.indexPath || DEFAULT_INDEX;
  const index = readJson(indexPath);
  const entries = index.benchmarks || [];

  // An explicit baseline / universal context grounds in the universal sibling,
  // not a subject benchmark.
  if (BASELINE_INPUTS.has(String(input).trim().toLowerCase())) {
    return universalBenchmark(input, null);
  }

  let resolved;
  try {
    resolved = resolveSubjectContext(input, options);
  } catch (err) {
    resolved = null;
  }

  // "universal" (or anything that resolves unscoped) grounds in the baseline
  // sibling rather than a single subject's benchmark.
  if (resolved && resolved.scoped === false) {
    return universalBenchmark(input, resolved);
  }

  // Candidate codes, most specific first: the resolved code then its chain.
  const candidates = [];
  if (resolved && resolved.code) {
    candidates.push({ code: resolved.code, level: resolved.level });
    for (const c of resolved.chain || []) {
      candidates.push({ code: c.code, level: c.level });
    }
  }

  for (const cand of candidates) {
    for (const e of entries) {
      if ((e.codes || []).some((c) => c.code === cand.code)) {
        return {
          input,
          resolved,
          benchmark: {
            id: e.id,
            file: e.file,
            matchedCode: cand.code,
            matchLevel: cand.level,
          },
          gap: null,
        };
      }
    }
  }

  // Fallback: direct subject-name match against the catalogue.
  const lower = String(input).toLowerCase();
  for (const e of entries) {
    if (String(e.subject || '').toLowerCase() === lower) {
      return {
        input,
        resolved,
        benchmark: {
          id: e.id, file: e.file, matchedCode: null, matchLevel: 'name',
        },
        gap: null,
      };
    }
  }

  return {
    input,
    resolved,
    benchmark: null,
    gap: {
      type: 'no-benchmark',
      detail:
        'No catalogue benchmark matches this subject by code or name. ' +
        'Either the subject has no benchmark reference yet, or the input is unknown.',
    },
  };
}

module.exports = {
  REPO_ROOT,
  DEFAULT_INDEX,
  resolveSubjectBenchmark,
};

if (require.main === module) {
  const args = process.argv.slice(2);
  const load = args.includes('--load');
  const input = args.filter((a) => a !== '--load')[0];
  if (!input) {
    process.stderr.write(
      'Usage: node resolve-subject-benchmark.js <subject-name-or-code> [--load]\n'
    );
    process.exit(1);
  }
  const result = resolveSubjectBenchmark(input);
  process.stdout.write(JSON.stringify(result, null, 2) + '\n');
  if (result.gap) {
    process.exit(1);
  }
  if (load) {
    const abs = path.join(REPO_ROOT, result.benchmark.file);
    if (!fs.existsSync(abs)) {
      process.stderr.write('Reference file missing: ' + abs + '\n');
      process.exit(1);
    }
    process.stdout.write(abs + '\n');
  }
  process.exit(0);
}
