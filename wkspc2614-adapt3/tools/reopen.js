#!/usr/bin/env node
/**
 * reopen.js
 *
 * RJ-0062 (adp-0216), verbatim: "It builds a preview from the store's
 * `dependsOn` edges, read through `tools/gate-order.js` or a function
 * beside it, never a list. It appends the new record, lists each
 * dependent record by class for Abbott to rule on, and writes the
 * sweep event in the shape the record schema already defines." This
 * closes finding F5 (wpk-0017-agentic-pd-review-adp-course-design.md):
 * reopening (scope preview, then a sweep) was designed in the gate
 * model (docs/design/gate-conversation-model-draft-v1.md 5) and in the
 * record schema's sweepEvents array, but no command ran it.
 *
 * The preview: tools/gate-order.js's own getDependents(store, gateId)
 * (added alongside this tool, RJ-0062), the reverse-edge scan over the
 * store's static dependsOn edges -- never a hardcoded list.
 *
 * Verdict default per edge class (design-kb.gates.schema.json's own
 * dependsOn description; gate-conversation-model-draft-v1.md 5.2-5.3):
 * constitutive -> invalidate, substantive -> flag-for-review,
 * nominal -> stand-with-warning. The edge class is the default; Abbott
 * disposes (confirmed / amended / stood) per dependent in the draft.
 *
 * Sweep event shape (schemas/course-design.schema.json's own
 * sweepEvents item, quoted here, not re-derived): required eventId
 * (`^SW-[0-9]+$`), timestamp, trigger ({gate, changeKind, oldRecordSeq,
 * newRecordSeq, note}), sweep[] ({gate, recordSeq, basis:
 * {gate, dependencyClass}, defaultVerdict, disposition: {verdict, mode,
 * note required when mode=amended}, resolution: required when
 * disposition.verdict is invalidate or flag-for-review, absent for
 * stand-with-warning}).
 *
 * The reopened gate's own new record: appended (never rewritten) with
 * the next seq, `supersedes` citing the record it replaces -- the
 * schema's own append-only reopen path (course-design.schema.json's
 * records[].supersedes description).
 *
 * Nothing under courses/ is read or written beyond the one
 * course-design.json passed on the command line; this tool never
 * touches config.json or en/*.json (RJ-0062's own scope line).
 *
 * Usage:
 *   node tools/reopen.js --preview --gate=<id> --course-design=<path> [--store=<path>]
 *   node tools/reopen.js --course-design=<path> --draft=<path> --gate=<id> [--store=<path>]
 *
 * Draft file shape (written by a /reopen session, GDP-1), for the
 * second (apply) form above:
 *   { "changeKind": "amended", "note": "one sentence",
 *     "provenance": "human-specified", "decidedValue": {...},
 *     "dispositions": [
 *       { "gate": "crs-03_course-outcomes", "verdict": "invalidate", "mode": "confirmed" },
 *       { "gate": "wra-04_confidence", "verdict": "flag-for-review", "mode": "amended",
 *         "note": "why this one differs from the default",
 *         "resolution": { "status": "open" } }
 *   ] }
 */

'use strict';

const fs = require('fs');
const path = require('path');
const gateOrder = require('./gate-order.js');

/** The sweep's default verdict for one dependsOn edge's class. Refuses an unrecognised class by name, never guesses. */
function defaultVerdictForClass(dependencyClass) {
  if (dependencyClass === 'constitutive') return 'invalidate';
  if (dependencyClass === 'substantive') return 'flag-for-review';
  if (dependencyClass === 'nominal') return 'stand-with-warning';
  throw new Error(`reopen: unrecognised dependencyClass '${dependencyClass}': refusing to choose a default verdict for it`);
}

/** Deep structural equality by canonical JSON (sufficient for gate decidedValue). */
function deepEqual(a, b) {
  return JSON.stringify(a) === JSON.stringify(b);
}

/**
 * The coarsest decidedValue dot-paths at which `newV` differs from `oldV`.
 * Recurses through plain objects; reports an array or a leaf as a whole node.
 * Used by the published-course edit-mode check: every changed path must be
 * covered by the reopen's `unlocked` set (field-locks-and-edit-mode.md).
 */
function changedPaths(oldV, newV, prefix) {
  if (deepEqual(oldV, newV)) return [];
  const isPlainObj = v => v && typeof v === 'object' && !Array.isArray(v);
  if (isPlainObj(oldV) && isPlainObj(newV)) {
    const keys = new Set([...Object.keys(oldV), ...Object.keys(newV)]);
    let out = [];
    for (const k of keys) {
      out = out.concat(changedPaths(oldV[k], newV[k], prefix ? `${prefix}.${k}` : k));
    }
    return out;
  }
  return [prefix || '(root)'];
}

/**
 * Published-course edit-mode gate (field-locks-and-edit-mode.md): on a course
 * whose status is 'production', a reopen may change only the decidedValue
 * dot-paths it unlocks; every other field must be carried forward verbatim.
 * Throws, naming the stray paths, when a change falls outside `unlocked`.
 * A path is covered when it equals, sits under, or is an ancestor of an
 * unlocked path. No-op for an in-development course.
 */
function enforceUnlockScope(courseDesign, priorDecidedValue, newDecidedValue, unlocked) {
  if (courseDesign.status !== 'production') return;
  const locks = Array.isArray(unlocked) ? unlocked : [];
  const changed = changedPaths(priorDecidedValue, newDecidedValue, '');
  const covered = p => locks.some(u => p === u || p.startsWith(`${u}.`) || u.startsWith(`${p}.`));
  const stray = changed.filter(p => !covered(p));
  if (stray.length > 0) {
    throw new Error(
      `reopen: course is published (status 'production'); decidedValue path(s) changed but not unlocked: ${stray.join(', ')}. ` +
      `Unlock them explicitly (draft "unlocked": [...]) or leave them unchanged.`
    );
  }
}

/**
 * The scope preview (gate-conversation-model-draft-v1.md 5.5, beat
 * one): the gate's current record seq and its dependents by class.
 * Pure, read-only. Throws, naming the gate, when gateId is not in the
 * store (RJ-0062 test: "reopening a gate not in the store fails with a
 * named error") or when the course design carries no record for it yet
 * (RJ-0062 test: "a run reaching no record fails").
 *
 * Refuses a gate whose store entry carries `propagationScope:
 * "universal"` (gate-conversation-model-draft-v1.md 5.1) rather than
 * silently returning an empty dependents list. No gate in the current
 * six-phase store carries the flag (the old course-facets/CTX gate that
 * did was retired in the six-phase migration); the check stays generic,
 * reading the flag from whatever store it is handed, so it refuses any
 * gate a future store marks universal. Universal scope means the static
 * net does not apply at all -- every gate is in play via the change-kind
 * tracer rule on the sourceConsultation facet->store mapping, the
 * opposite of "nothing depends on it". This tool implements only the
 * listed (static-edge) net; a universal-scope reopen is out of its scope
 * and is named here, not guessed at.
 *
 * `gateProfilesStore` (optional, D8(a), 4 Nov 2026): when supplied, the
 * dependents list is filtered through gateOrder.profileGateIds, mirroring
 * validate-design-schemas.py's own NSK-1 resolver. A gate the manifest's
 * active profile does not claim in its own step list (crs-02/crs-03 under
 * pathway-distillation - see those gates' dependency notes in
 * design-kb.gates.json) has, under that profile, no live edge pointing at
 * it, so its dependents are reported empty rather than listing edges that
 * are not-applicable under this profile. Omitting the argument (as every
 * call before this fix did) skips the filter entirely - the pre-existing,
 * unfiltered behaviour - matching profileGateIds' own "null means can't
 * resolve, fall back to universal" contract.
 */
function buildReopenPreview(store, courseDesign, gateId, gateProfilesStore) {
  const gateDef = store.gates.find(g => g.id === gateId);
  if (gateDef && gateDef.propagationScope === 'universal') {
    throw new Error(`reopen: ${gateId} has propagationScope 'universal': its sweep runs the change-kind tracer rule over every gate (gate-conversation-model-draft-v1.md 5.4), not this tool's static dependsOn net; refusing to report an empty dependents list for it`);
  }
  let dependents = gateOrder.getDependents(store, gateId);
  if (gateProfilesStore) {
    const activeProfile = courseDesign.profile || 'built-course-shape';
    const ids = gateOrder.profileGateIds(gateProfilesStore, activeProfile);
    if (ids !== null && !ids.has(gateId)) {
      dependents = [];
    }
  }
  const entry = (courseDesign.gates || []).find(g => g.gateId === gateId);
  if (!entry || entry.records.length === 0) {
    throw new Error(`reopen: ${gateId} has no record in the course design: nothing to reopen`);
  }
  const currentSeq = Math.max(...entry.records.map(r => r.seq));
  return { gateId, currentSeq, dependents };
}

/**
 * RJ-0062 D8(b) lesson-id wiring (4 Nov 2026): the manifest entry/entries
 * a dependent's bare store gate id actually resolves to. A once-per-course
 * gate is a single, direct gateId match. A `repeatsPer: 'lesson'` gate
 * (design-kb.gates.schema.json's own repeatsPer description -
 * schemas/design-kb.gates.schema.json:126-131) is never stored under its
 * own bare id; each lesson's decision is a separate manifest entry keyed
 * `<slug>-<lessonKey>-<shortCode>` (the same convention
 * tools/manifest-completeness.js's own per-lesson checks already read -
 * `shortCode` is the gate id's own code before its first underscore, e.g.
 * "les-01" from "les-01_lesson-proposal", read off the gate itself rather
 * than hardcoded). Reads the gate's own repeatsPer flag off the store, so
 * a gate that later gains repeatsPer: 'lesson' is picked up here with no
 * edit to this function. 'context-pack' gates key differently
 * (`<slug>-<subject>-<phase-nn>`, no lesson list to expand from) and are
 * out of this expansion's scope - returned as a direct (and here, always
 * absent) bare-id match, the pre-existing behaviour for them.
 */
function recordsForDependent(store, courseDesign, dep) {
  const manifestGates = courseDesign.gates || [];
  const gateDef = store.gates.find(g => g.id === dep.gate);
  if (!gateDef || gateDef.repeatsPer !== 'lesson') {
    const e = manifestGates.find(g => g.gateId === dep.gate);
    return e ? [e] : [];
  }
  const shortCode = dep.gate.split('_')[0];
  const matchSlug = courseDesign.slug;
  const mapEntry = manifestGates.find(g => g.gateId === 'crs-04_lesson-map');
  const lastMapRecord = mapEntry && Array.isArray(mapEntry.records) && mapEntry.records.length > 0
    ? mapEntry.records[mapEntry.records.length - 1]
    : null;
  const lessons = (lastMapRecord && lastMapRecord.decidedValue && lastMapRecord.decidedValue.lessons) || [];
  const found = [];
  for (const lesson of lessons) {
    const key = lesson.key;
    if (typeof key !== 'string' || key.length === 0) continue;
    const bareKey = key.startsWith(`${matchSlug}-`) ? key.slice(matchSlug.length + 1) : key;
    const perLessonId = `${matchSlug}-${bareKey}-${shortCode}`;
    const e = manifestGates.find(g => g.gateId === perLessonId);
    if (e) found.push(e);
  }
  return found;
}

/**
 * Builds the reopened gate's new record and the sweep event, from the
 * preview and a draft's answer (changeKind, note, provenance,
 * decidedValue, dispositions[] -- one per dependent the preview named).
 * Pure: takes and returns plain objects, writes nothing. Throws, naming
 * the gate, when a dependent the preview named has no disposition in
 * the draft (mirrors phase-confirm.js's "no answer supplied" refusal),
 * and when a disposition's own schema conditional is unmet (resolution
 * required for invalidate/flag-for-review; note required when mode is
 * amended).
 */
function buildReopen(store, courseDesign, gateId, answer, gateProfilesStore) {
  const preview = buildReopenPreview(store, courseDesign, gateId, gateProfilesStore);
  const nowIso = new Date().toISOString();
  const newSeq = preview.currentSeq + 1;

  // Published-course edit-mode (field-locks-and-edit-mode.md): a reopen may
  // change only the decidedValue paths it unlocks; everything else is carried
  // forward verbatim. No-op while the course is in-development.
  const gateEntry = (courseDesign.gates || []).find(g => g.gateId === gateId);
  const priorRecord = gateEntry.records.find(r => r.seq === preview.currentSeq);
  enforceUnlockScope(
    courseDesign,
    priorRecord ? priorRecord.decidedValue : undefined,
    answer.decidedValue,
    answer.unlocked
  );

  const newRecord = {
    seq: newSeq,
    state: 'closed',
    provenance: answer.provenance,
    decidedValue: answer.decidedValue,
    supersedes: preview.currentSeq,
    timestamp: nowIso
  };
  if (Array.isArray(answer.unlocked)) newRecord.unlocked = answer.unlocked;

  const byGate = new Map((answer.dispositions || []).map(d => [d.gate, d]));
  // A graph-dependent with no closed record carries no decision to sweep: a
  // gate reopened before its downstream gates are landed (e.g. narrowing CRS
  // scope before the lesson map is authored) is a normal case, not an error.
  // Such dependents are reported as "authored fresh against the new decision"
  // and neither require nor receive a sweep entry; the sweep tracks only the
  // decisions that actually exist.
  const hasRecord = dep => recordsForDependent(store, courseDesign, dep).some(e => e.records && e.records.length > 0);
  const authoredFresh = preview.dependents.filter(dep => !hasRecord(dep)).map(dep => dep.gate);
  const sweep = preview.dependents.filter(hasRecord).map(dep => {
    const disposition = byGate.get(dep.gate);
    if (!disposition) {
      throw new Error(`reopen: no disposition supplied for ${dep.gate}, a dependent of ${gateId}`);
    }
    if (disposition.mode === 'amended' && !disposition.note) {
      throw new Error(`reopen: ${dep.gate}'s disposition is amended but carries no note (required when mode is amended)`);
    }
    const needsResolution = disposition.verdict === 'invalidate' || disposition.verdict === 'flag-for-review';
    if (needsResolution && !disposition.resolution) {
      throw new Error(`reopen: ${dep.gate}'s disposition verdict is '${disposition.verdict}' but carries no resolution (required for invalidate and flag-for-review)`);
    }
    const depEntries = recordsForDependent(store, courseDesign, dep);
    const depSeqs = depEntries.flatMap(e => (e.records || []).map(r => r.seq));
    const sweepEntry = {
      gate: dep.gate,
      recordSeq: Math.max(...depSeqs),
      basis: { gate: gateId, dependencyClass: dep.dependencyClass },
      defaultVerdict: defaultVerdictForClass(dep.dependencyClass),
      disposition: { verdict: disposition.verdict, mode: disposition.mode }
    };
    if (disposition.note) sweepEntry.disposition.note = disposition.note;
    if (needsResolution) sweepEntry.resolution = disposition.resolution;
    return sweepEntry;
  });

  const existingEvents = courseDesign.sweepEvents || [];
  const nextEventN = existingEvents.length === 0
    ? 1
    : Math.max(...existingEvents.map(e => Number(String(e.eventId).replace('SW-', '')) || 0)) + 1;

  const sweepEvent = {
    eventId: `SW-${nextEventN}`,
    timestamp: nowIso,
    trigger: {
      gate: gateId,
      changeKind: answer.changeKind,
      oldRecordSeq: preview.currentSeq,
      newRecordSeq: newSeq,
      note: answer.note
    },
    sweep
  };

  return { gateId, newRecord, sweepEvent, dependents: preview.dependents, authoredFresh };
}

/**
 * Appends the reopened gate's new record and the sweep event into a
 * course-design object. Mutates and returns the same object;
 * append-only, matching the manifest's own invariant (never rewrites
 * the superseded record).
 */
function applyReopen(courseDesign, result) {
  const entry = courseDesign.gates.find(g => g.gateId === result.gateId);
  entry.records.push(result.newRecord);
  courseDesign.sweepEvents = courseDesign.sweepEvents || [];
  courseDesign.sweepEvents.push(result.sweepEvent);
  return courseDesign;
}

function parseArgs(argv) {
  const args = { preview: false, courseDesign: null, draft: null, gate: null, store: null, gateProfiles: null };
  argv.forEach(param => {
    if (param === '--preview') { args.preview = true; return; }
    const eq = param.indexOf('=');
    if (eq === -1) return;
    const key = param.slice(2, eq);
    const value = param.slice(eq + 1);
    if (key === 'course-design') args.courseDesign = value;
    if (key === 'draft') args.draft = value;
    if (key === 'gate') args.gate = value;
    if (key === 'store') args.store = value;
    if (key === 'gate-profiles') args.gateProfiles = value;
  });
  return args;
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.gate || !args.courseDesign) {
    console.error('reopen: usage: --preview --gate=<id> --course-design=<path> [--store=<path>] [--gate-profiles=<path>]');
    console.error('    or: --course-design=<path> --draft=<path> --gate=<id> [--store=<path>] [--gate-profiles=<path>]');
    process.exit(1);
  }
  try {
    const store = gateOrder.loadStore(args.store);
    const gateProfilesStore = args.gateProfiles ? gateOrder.loadGateProfiles(args.gateProfiles) : null;
    const courseDesignPath = path.resolve(args.courseDesign);
    const courseDesign = JSON.parse(fs.readFileSync(courseDesignPath, 'utf8'));

    if (args.preview) {
      const preview = buildReopenPreview(store, courseDesign, args.gate, gateProfilesStore);
      console.log(JSON.stringify(preview, null, 2));
      return;
    }

    if (!args.draft) {
      console.error('reopen: usage: --course-design=<path> --draft=<path> --gate=<id> [--store=<path>] [--gate-profiles=<path>]');
      process.exit(1);
    }
    const draft = JSON.parse(fs.readFileSync(path.resolve(args.draft), 'utf8'));
    const result = buildReopen(store, courseDesign, args.gate, draft, gateProfilesStore);
    applyReopen(courseDesign, result);
    fs.writeFileSync(courseDesignPath, JSON.stringify(courseDesign, null, 2) + '\n');
    console.log(JSON.stringify({
      wrote: courseDesignPath,
      gateId: result.gateId,
      newSeq: result.newRecord.seq,
      eventId: result.sweepEvent.eventId,
      dependents: result.dependents
    }, null, 2));
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = {
  defaultVerdictForClass,
  buildReopenPreview,
  buildReopen,
  applyReopen,
  recordsForDependent
};
