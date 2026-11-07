#!/usr/bin/env node
'use strict';

/**
 * cmet-context.js - a subject name or HECoS/CAH code in, the matching
 * HECoS/CAH grouping, subject benchmark context and pathway reading out, by
 * shelling out to the context-cmet submodule's CLI
 * (tools/context-cmet/bin/context-cmet.js).
 *
 * This is a complement to resolve-subject-benchmark.js, not a replacement:
 * that tool answers "which host benchmark file matches this subject"; this
 * one answers "what does context-cmet's HECoS/CAH hierarchy, Cardiff Met
 * course data and benchmark-to-pathway mapping say about it". The host's own
 * catalogue/context/subject/benchmarks/*.json files carry pathwayMapping
 * mostly empty (53 of 55, verified); context-cmet holds the mapping for all
 * 54 maps. The two corpora are complementary, not duplicates.
 *
 * context-cmet is `"type": "module"` (ESM); every tools/*.js in this repo is
 * CommonJS and the root package.json carries no "type" field, so `require()`
 * of it throws ERR_REQUIRE_ESM. Shell exec is therefore the only route in,
 * not a style choice. Precedent: tools/phase-confirm.js, render-course-spec.js
 * and verify-all-courses.js all shell out with execFileSync.
 *
 * Usage:
 *   node tools/cmet-context.js <subject-or-code> [--pathway=<id>] [--row=<row>] [--authoring]
 * --authoring calls the submodule's `authoring` command (standards, subject
 * definitions, reading) instead of `lookup`. --pathway is passed through
 * verbatim: context-cmet's pathway ids are the host's course-slug stems, an
 * identity mapping for 13 of 14 (the host builds no `self-development`
 * pathway; context-cmet has no `sandbox-les01-hardstop` fixture). --row is
 * passed only when the caller supplies one: the host records tier
 * (introductory/intermediate/advanced), not the row-level FHEQ distinction
 * context-cmet's rows carry (e.g. intermediate spans d1/d2/d3 = L4/L5/L6), so
 * a row is never synthesised here.
 */

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const REPO_ROOT = path.resolve(__dirname, '..');
const CMET_BIN = path.join(
  REPO_ROOT, 'tools', 'context-cmet', 'bin', 'context-cmet.js'
);

/**
 * True once the submodule is actually populated. It will not be on a fresh
 * clone: `gitmodules.js`'s preinstall drives this repo's own
 * wkspc2614-adapt3/.gitmodules, which is a stale leftover listing only
 * `src/core` - the real submodule entry lives in the true repo root's
 * .gitmodules, one level up, and needs `git submodule update --init` there.
 */
function cmetAvailable(bin = CMET_BIN) {
  return fs.existsSync(bin);
}

function missingSubmoduleGap(input) {
  return {
    input,
    resolved: null,
    benchmark: null,
    gap: {
      type: 'cmet-not-populated',
      detail:
        'tools/context-cmet is not populated. Run `git submodule update ' +
        '--init` from the true repo root (one level above wkspc2614-adapt3; ' +
        'its own wkspc2614-adapt3/.gitmodules is a stale leftover and does ' +
        'not drive this submodule).',
    },
  };
}

/**
 * Run a context-cmet CLI command and parse its JSON. Always appends --json.
 * Re-parses stdout even on a non-zero exit, since ContextError still prints
 * usable JSON on some paths; captures stderr (the candidate list on an
 * ambiguous match) separately. Exit code 2 means "unknown command" in the
 * submodule - distinct from every other non-zero exit, which means "no
 * match" - so it is reported as its own gap reason rather than read as a
 * subject miss.
 */
function run(args, { bin = CMET_BIN } = {}) {
  if (!cmetAvailable(bin)) {
    return { ok: false, gap: 'missing-submodule' };
  }
  try {
    const stdout = execFileSync(
      process.execPath, [bin, ...args, '--json'], { encoding: 'utf8' }
    );
    return { ok: true, data: JSON.parse(stdout) };
  } catch (err) {
    const status = err.status;
    const stdout = err.stdout ? String(err.stdout).trim() : '';
    const stderr = err.stderr ? String(err.stderr).trim() : '';
    let data = null;
    if (stdout) {
      try { data = JSON.parse(stdout); } catch { /* not JSON on this path */ }
    }
    if (status === 2) {
      return { ok: false, gap: 'unknown-command', stderr, data };
    }
    return { ok: false, gap: 'no-match', stderr, data };
  }
}

/**
 * Resolve a subject to its context-cmet grouping, benchmark context and
 * pathway reading. Returns { input, resolved, benchmark, gap }, matching the
 * shape of resolveSubjectBenchmark in resolve-subject-benchmark.js.
 * options: { pathway, row, authoring, bin }.
 */
function lookupCmetContext(input, options = {}) {
  const { pathway, row, authoring, bin = CMET_BIN } = options;

  if (!cmetAvailable(bin)) {
    return missingSubmoduleGap(input);
  }

  const args = [authoring ? 'authoring' : 'lookup', input];
  if (pathway) args.push('--pathway', pathway);
  if (row) args.push('--row', row);

  const result = run(args, { bin });

  if (!result.ok) {
    if (result.gap === 'unknown-command') {
      return {
        input,
        resolved: null,
        benchmark: null,
        gap: {
          type: 'cmet-unknown-command',
          detail: `context-cmet does not recognise the command "${args[0]}".`,
        },
      };
    }
    // 'no-match' / ambiguous: candidates, if any, are on stderr as plain
    // text lines (the CLI's own ContextError rendering), not JSON.
    const candidates = result.stderr
      ? result.stderr.split('\n').map((l) => l.trim()).filter(Boolean)
      : [];
    return {
      input,
      resolved: null,
      benchmark: null,
      gap: {
        type: 'no-cmet-match',
        detail: result.stderr || 'context-cmet found no match for this subject.',
        candidates,
      },
    };
  }

  const payload = result.data;
  return {
    input,
    resolved: { subject: payload.subject || null, pathway: pathway || null, row: row || null },
    benchmark: payload,
    cmetDataVersion: payload.dataVersion || null,
    gap: null,
  };
}

/** `search` - find subjects/courses/schools/contexts by free text. */
function searchCmet(text, { bin = CMET_BIN } = {}) {
  if (!cmetAvailable(bin)) return missingSubmoduleGap(text);
  const result = run(['search', text], { bin });
  if (!result.ok) {
    return {
      input: text, resolved: null, benchmark: null,
      gap: { type: 'no-cmet-match', detail: result.stderr || 'No results.' },
    };
  }
  return { input: text, resolved: null, benchmark: { results: result.data }, gap: null };
}

/** `crosswalk` - how HECoS terms reach QAA benchmarks. */
function crosswalkCmet(code, { bin = CMET_BIN } = {}) {
  if (!cmetAvailable(bin)) return missingSubmoduleGap(code);
  const result = run(code ? ['crosswalk', code] : ['crosswalk'], { bin });
  if (!result.ok) {
    return {
      input: code || null, resolved: null, benchmark: null,
      gap: { type: 'no-cmet-match', detail: result.stderr || 'No crosswalk entry.' },
    };
  }
  return { input: code || null, resolved: null, benchmark: result.data, gap: null };
}

module.exports = {
  REPO_ROOT,
  CMET_BIN,
  cmetAvailable,
  run,
  lookupCmetContext,
  searchCmet,
  crosswalkCmet,
};

if (require.main === module) {
  const args = process.argv.slice(2);
  const flags = {};
  const positionals = [];
  for (const a of args) {
    if (a === '--authoring') flags.authoring = true;
    else if (a.startsWith('--pathway=')) flags.pathway = a.slice('--pathway='.length);
    else if (a.startsWith('--row=')) flags.row = a.slice('--row='.length);
    else positionals.push(a);
  }
  const input = positionals[0];
  if (!input) {
    process.stderr.write(
      'Usage: node cmet-context.js <subject-or-code> [--pathway=<id>] ' +
      '[--row=<row>] [--authoring]\n'
    );
    process.exit(1);
  }
  const result = lookupCmetContext(input, flags);
  process.stdout.write(JSON.stringify(result, null, 2) + '\n');
  process.exit(result.gap ? 1 : 0);
}
