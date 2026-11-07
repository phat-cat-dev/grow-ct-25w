#!/usr/bin/env node
/**
 * gate-order.js
 *
 * RJ-0059 (adp-0215): the gates store (design-kb/design-kb.gates.json) is
 * the sole source of run order, Phase A's closure set and per-gate
 * procedure flags. `.claude/commands/gate.md`, `land.md`, `new-course.md`
 * and `scaffold.md` read these through this one small tool instead of
 * keeping their own hardcoded lists. Phase A's closure set is computed
 * from the store's own `phase` field, not typed out by hand, so a new
 * phase-A gate (gates/CO here, gates/EXM before it) is picked up without
 * any command doc needing to change: this is what fixes finding F6
 * (EXM previously left out of scaffold.md's and new-course.md's typed
 * closure sets).
 *
 * The tool deliberately does not hold a hardcoded list of which gate ids
 * must exist. Instead it checks that every gate's `sequence` value forms
 * a contiguous run 0..(n-1) with no gaps and no duplicates. A gate
 * deleted from the store (by mistake, by a bad edit, or by a planted
 * fixture in the tests below) breaks that contiguity and is caught as a
 * named check failure, not silently computed around. This is the
 * project's own "a check that reaches no subjects has not passed"
 * discipline applied to the closure-set computation itself.
 *
 * Usage:
 *   node tools/gate-order.js --order [--store=<path>]
 *   node tools/gate-order.js --closure-set=A [--store=<path>]
 *   node tools/gate-order.js --flags=gates/B2 [--store=<path>]
 *
 * Default --store is design-kb/design-kb.gates.json at the repo root.
 */

'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const DEFAULT_STORE = path.join(ROOT, 'design-kb', 'design-kb.gates.json');
const DEFAULT_GATE_PROFILES = path.join(ROOT, 'design-kb', 'design-kb.gate-profiles.json');

/**
 * Loads and parses the gates store. Throws (never returns undefined, never
 * silently falls back) when the store cannot be reached: RJ-0059's own
 * requirement that "a run that reaches no store fails".
 */
function loadStore(storePath) {
  const resolved = storePath ? path.resolve(storePath) : DEFAULT_STORE;
  if (!fs.existsSync(resolved)) {
    throw new Error(`gate-order: no store at ${resolved}`);
  }
  let raw;
  try {
    raw = fs.readFileSync(resolved, 'utf8');
  } catch (err) {
    throw new Error(`gate-order: store unreadable at ${resolved} (${err.message})`);
  }
  let parsed;
  try {
    parsed = JSON.parse(raw);
  } catch (err) {
    throw new Error(`gate-order: store is not valid JSON at ${resolved} (${err.message})`);
  }
  if (!parsed || !Array.isArray(parsed.gates)) {
    throw new Error(`gate-order: store at ${resolved} carries no "gates" array`);
  }
  return parsed;
}

/**
 * Loads and parses the gate-profiles store (design-kb/design-kb.gate-profiles.json).
 * Same throw-never-silently-fall-back discipline as loadStore above.
 */
function loadGateProfiles(storePath) {
  const resolved = storePath ? path.resolve(storePath) : DEFAULT_GATE_PROFILES;
  if (!fs.existsSync(resolved)) {
    throw new Error(`gate-order: no gate-profiles store at ${resolved}`);
  }
  let raw;
  try {
    raw = fs.readFileSync(resolved, 'utf8');
  } catch (err) {
    throw new Error(`gate-order: gate-profiles store unreadable at ${resolved} (${err.message})`);
  }
  let parsed;
  try {
    parsed = JSON.parse(raw);
  } catch (err) {
    throw new Error(`gate-order: gate-profiles store is not valid JSON at ${resolved} (${err.message})`);
  }
  if (!parsed || !Array.isArray(parsed.profiles)) {
    throw new Error(`gate-order: gate-profiles store at ${resolved} carries no "profiles" array`);
  }
  return parsed;
}

/**
 * RJ-0062 D8(a) profile wiring (4 Nov 2026): the set of gate ids a named
 * profile's own step list claims in design-kb.gate-profiles.json - each
 * step's own `gates` array, plus `continuesWith` - read from the store
 * itself, never a hardcoded list of gate ids or a hardcoded check against
 * a profile name. Deliberately mirrors validate-design-schemas.py's
 * `_profile_gate_ids` (NSK-1) field-for-field, so the two resolvers
 * cannot silently diverge on what a profile's gate-id set is.
 *
 * Returns null, never an empty set, when `profileId` names no profile the
 * store defines; the caller treats null as "can't resolve this, fall back
 * to the universal default" rather than "nothing claimed by this profile."
 */
function profileGateIds(gateProfilesStore, profileId) {
  for (const prof of gateProfilesStore.profiles || []) {
    if (prof.id === profileId) {
      const ids = new Set(prof.continuesWith || []);
      for (const step of prof.steps || []) {
        for (const g of step.gates || []) ids.add(g);
      }
      return ids;
    }
  }
  return null;
}

/**
 * Named check: every gate carries a numeric `sequence`, and the full set
 * of sequence values is exactly 0..(n-1), no gaps, no duplicates. Throws
 * on failure, naming what it found, so a gate missing from the store (its
 * sequence value absent from the run) is never silently passed over.
 */
function checkSequenceContiguous(store) {
  const gates = store.gates;
  const seen = new Map();
  for (const g of gates) {
    if (typeof g.sequence !== 'number') {
      throw new Error(`gate-order: checkSequenceContiguous: ${g.id} carries no numeric sequence`);
    }
    if (seen.has(g.sequence)) {
      throw new Error(`gate-order: checkSequenceContiguous: sequence ${g.sequence} used by both ${seen.get(g.sequence)} and ${g.id}`);
    }
    seen.set(g.sequence, g.id);
  }
  const n = gates.length;
  const missing = [];
  for (let i = 0; i < n; i++) {
    if (!seen.has(i)) missing.push(i);
  }
  if (missing.length > 0) {
    throw new Error(`gate-order: checkSequenceContiguous: sequence gap at ${missing.join(', ')} (found ${n} gates, sequence values must run 0..${n - 1})`);
  }
  return true;
}

/** Full run order, lowest sequence first. Runs the named check first. */
function getOrder(store) {
  checkSequenceContiguous(store);
  return store.gates.slice().sort((a, b) => a.sequence - b.sequence);
}

/**
 * A phase's closure set: every gate whose own `phase` field equals the
 * named phase, ordered by sequence. Computed from the store's phase
 * field, not typed out by hand, so new gates in a phase are picked up
 * without the command docs keeping their own list (F6).
 *
 * Gate realignment (Round D, 7 Oct 2026): generalised from the old
 * Phase-A-only form to take a phase argument, now that phases are
 * ONB|CXS|CRS|LES|WRA|CXP rather than the old A/B/S/W/D letters.
 */
function getPhaseClosureSet(store, phase) {
  return getOrder(store)
    .filter(g => g.phase === phase)
    .map(g => g.id);
}
// Back-compat alias (old name); the old literal Phase "A" no longer exists.
function getPhaseAClosureSet(store, phase) {
  return getPhaseClosureSet(store, phase);
}

/**
 * Every OTHER gate in the store whose own `dependsOn` array names
 * `gateId` as an upstream dependency (dimension 5, S2, 26 Aug 2026,
 * docs/design/gate-conversation-model-draft-v1.md 5.1): the sweep
 * net's reverse-edge view, read for RJ-0062's `/reopen`. Static edges
 * are stored on the DEPENDENT gate pointing at its upstream dependency
 * (schemas/design-kb.gates.schema.json's own dependsOn shape: each
 * entry is `{gate, dependencyClass, note?}` naming what THIS gate
 * depends on), so finding who depends on a given gate is a scan across
 * every gate's own dependsOn array, never a field read on the gate
 * itself. Throws, naming the gate, when gateId is not in the store
 * (RJ-0062 test: "reopening a gate not in the store fails with a named
 * error"), the same discipline as getFlags below.
 */
function getDependents(store, gateId) {
  if (!store.gates.some(g => g.id === gateId)) {
    throw new Error(`gate-order: getDependents: no gate ${gateId} in store`);
  }
  const dependents = [];
  for (const g of store.gates) {
    if (!Array.isArray(g.dependsOn)) continue;
    for (const edge of g.dependsOn) {
      if (edge.gate === gateId) {
        dependents.push({ gate: g.id, dependencyClass: edge.dependencyClass });
      }
    }
  }
  return dependents;
}

/**
 * A named gate's repeatsPer, procedureFlags and sourceConsultation, read
 * from the store. sourceConsultation added 3 Nov 2026 (task #21: gate.md
 * step 2 previously named "currently crs-02_thematic-scope,
 * les-01_lesson-proposal and cxp-04_context-generation" as hardcoded prose
 * - the same staleness risk RJ-0059 already fixed for procedureFlags/
 * repeatsPer. A gate gaining a sourceConsultation block now needs no
 * command-doc edit to be picked up.
 */
function getFlags(store, gateId) {
  const gate = store.gates.find(g => g.id === gateId);
  if (!gate) {
    throw new Error(`gate-order: getFlags: no gate ${gateId} in store`);
  }
  return {
    repeatsPer: gate.repeatsPer || null,
    procedureFlags: gate.procedureFlags || {},
    sourceConsultation: gate.sourceConsultation || null
  };
}

function parseArgs(argv) {
  const args = { order: false, closureSet: null, flags: null, store: null };
  argv.forEach(param => {
    if (param === '--order') { args.order = true; return; }
    const eq = param.indexOf('=');
    if (eq === -1) return;
    const key = param.slice(2, eq);
    const value = param.slice(eq + 1);
    if (key === 'closure-set') args.closureSet = value;
    if (key === 'flags') args.flags = value;
    if (key === 'store') args.store = value;
  });
  return args;
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  let store;
  try {
    store = loadStore(args.store);
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }

  try {
    if (args.order) {
      console.log(JSON.stringify(getOrder(store).map(g => g.id), null, 2));
      return;
    }
    if (args.closureSet) {
      console.log(JSON.stringify(getPhaseClosureSet(store, args.closureSet), null, 2));
      return;
    }
    if (args.flags) {
      console.log(JSON.stringify(getFlags(store, args.flags), null, 2));
      return;
    }
    console.error('gate-order: usage: --order | --closure-set=<PHASE> | --flags=<gate-id> [--store=<path>]');
    process.exit(1);
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = {
  loadStore,
  loadGateProfiles,
  checkSequenceContiguous,
  getOrder,
  getPhaseClosureSet,
  getPhaseAClosureSet,
  getFlags,
  getDependents,
  profileGateIds
};
