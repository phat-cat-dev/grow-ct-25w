#!/usr/bin/env node
/**
 * course-script-import.js — round-trip an exported course-export.js markdown
 * file back into a course's JSON source of truth.
 *
 * Two independent modes:
 *
 *   --edit <edit.md> --course <base-content-dir> [--dry-run]
 *     Reads a `<slug>.edit.md`, writes each changed field back into the base
 *     course's en/components.json, then runs verify-course. v1 scope: the
 *     flat prose fields (body, displayTitle, instruction) and the feedback/
 *     modal strings. Item/option arrays are not round-tripped. Writes only;
 *     staging/commit is left to the user.
 *
 *   --script <script.md> --tier <base-course-slug> --context <subject> [--dry-run]
 *     Reads a `<slug>.script.md` "screenplay" export (course-export.js's
 *     scriptMd()) that was edited by hand, diffs it chunk-by-chunk against
 *     the live GENERATED course (courses/_generated/<tier>-<context>/) using
 *     tools/lib/script-sync.js, and routes each changed chunk to its correct
 *     JSON source: a subject-coupled chunk (one whose component carries a
 *     slot__<page>__<slotType> marker, for the component types merge-
 *     context.js actually substitutes — mcq, matching, and the generic
 *     body-only fallback) goes to its content/context-packs/<context>/
 *     <tier>/<page>.json pack file; everything else goes to the BASE
 *     course's courses/<tier>/en/components.json. Unlike --edit, this
 *     round-trips item/option/feedback text too (not just flat prose),
 *     because script.md prints those. It cannot round-trip an edit that
 *     adds/removes an item or moves a "(correct)" marker (reported and left
 *     untouched), nor a body whose HTML carries inline markup beyond
 *     <p>/<ul>/<li>/<br> (script.md's plain-text rendering is lossy for
 *     that; reported and left untouched). On a successful, non-dry-run
 *     write that passes verify-course, it also re-runs merge-context.js and
 *     grunt build, so the edits are visible in the served course — the
 *     "recompile" step script.md edits need that --edit's flat-JSON edits
 *     don't (those already land straight in the served base course).
 *
 * Usage:
 *   node tools/course-script-import.js --edit <edit.md> --course <base-content-dir> [--dry-run]
 *   node tools/course-script-import.js --script <script.md> --tier <slug> --context <subject> [--dry-run]
 */
'use strict';
const fs = require('fs');
const path = require('path');
const cp = require('child_process');
const { resolveManifest, shortSlugFromManifest, bumpVersion } = require('./lib/content-version');
function arg(n, d) { const i = process.argv.indexOf('--' + n); return (i >= 0 && i + 1 < process.argv.length) ? process.argv[i + 1] : d; }

const scriptPath = arg('script');
if (scriptPath) {
  runScriptMode(scriptPath);
  return;
}

const editPath = arg('edit');
const courseDir = arg('course');
const dryRun = process.argv.includes('--dry-run');
if (!editPath || !courseDir) { console.error('usage: node tools/course-script-import.js --edit <edit.md> --course <base-content-dir> [--dry-run]\n   or: node tools/course-script-import.js --script <script.md> --tier <slug> --context <subject> [--dry-run]'); process.exit(2); }

const compPath = path.join(courseDir, 'en', 'components.json');
const originalText = fs.readFileSync(compPath, 'utf8');
const components = JSON.parse(originalText);
const byId = new Map(components.map(c => [c._id, c]));

// parse edit blocks: <!-- edit:ID:PATH --> then a fenced block
const edits = [];
const re = /<!-- edit:([^:>\s]+):([^\s>]+) -->\s*```[a-z]*\n([\s\S]*?)\n```/g;
let m;
while ((m = re.exec(fs.readFileSync(editPath, 'utf8')))) edits.push({ id: m[1], path: m[2], value: m[3] });

function setField(c, p, value) {
  switch (p) {
    case 'displayTitle': case 'body': case 'instruction':
      if (c[p] === value) return false; c[p] = value; return true;
    case 'feedback.correct':
      if (!c._feedback) return null; if (c._feedback.correct === value) return false; c._feedback.correct = value; return true;
    case 'feedback.incorrect.notFinal':
      if (!c._feedback || !c._feedback._incorrect) return null; if (c._feedback._incorrect.notFinal === value) return false; c._feedback._incorrect.notFinal = value; return true;
    case 'feedback.incorrect.final':
      if (!c._feedback || !c._feedback._incorrect) return null; if (c._feedback._incorrect.final === value) return false; c._feedback._incorrect.final = value; return true;
    case 'feedback.partlyCorrect.notFinal':
      if (!c._feedback || !c._feedback._partlyCorrect) return null; if (c._feedback._partlyCorrect.notFinal === value) return false; c._feedback._partlyCorrect.notFinal = value; return true;
    case 'feedback.partlyCorrect.final':
      if (!c._feedback || !c._feedback._partlyCorrect) return null; if (c._feedback._partlyCorrect.final === value) return false; c._feedback._partlyCorrect.final = value; return true;
    default: return null;
  }
}

let changed = 0, missing = 0, skipped = 0;
const changeLog = [];
for (const e of edits) {
  const c = byId.get(e.id);
  if (!c) { missing++; console.error(`  ! ${e.id} not found`); continue; }
  const r = setField(c, e.path, e.value);
  if (r === null) { skipped++; console.error(`  ~ ${e.id}:${e.path} skipped (no target field)`); }
  else if (r === true) { changed++; changeLog.push(`${e.id}:${e.path}`); }
}
console.log(`Parsed ${edits.length} edit block(s): ${changed} changed, ${missing} not-found, ${skipped} no-target.`);
if (dryRun) { console.log('Dry run — nothing written.'); changeLog.forEach(x => console.log('  changed: ' + x)); process.exit(0); }
if (!changed) { console.log('No changes to write.'); process.exit(0); }

fs.writeFileSync(compPath, JSON.stringify(components, null, 2) + '\n');
console.log(`Wrote ${changed} change(s) to ${compPath}. Validating...`);
changeLog.forEach(x => console.log('  changed: ' + x));

const slug = path.basename(courseDir);
const v = cp.spawnSync('node', ['tools/verify-course.js', '--course=' + slug], { encoding: 'utf8' });
process.stdout.write(v.stdout || ''); process.stderr.write(v.stderr || '');
if (v.status !== 0) {
  fs.writeFileSync(compPath, originalText);
  console.error('\nverify-course FAILED — components.json restored to its pre-import state. No changes landed.');
  process.exit(1);
}
console.log('\nverify-course PASSED. Changes applied; review the diff and stage/commit as usual (no commit made).');

{
  const resolved = resolveManifest(courseDir, null);
  const editShortSlug = shortSlugFromManifest(resolved.manifest, null);
  if (editShortSlug) {
    const version = bumpVersion(editShortSlug, 'edit-import', { file: path.basename(editPath), fields: changeLog });
    console.log(`Content version: ${editShortSlug} -> v${version}`);
  } else {
    console.log(`Content version: could not resolve a short slug for ${courseDir} — version record not updated.`);
  }
}

// =============================================================================
// --script mode: round-trip an edited .script.md back into base JSON + packs.
// =============================================================================

// extractDetailed(): same chunk shape/order as script-sync's extract() (and
// course-export.js's own copy), but each chunk also carries enough to write
// back to its exact source field: itemIndex/optIndex into _items[]/_options[],
// or feedbackKey into _feedback (base) / a pack entry's flat feedback object
// (pack's feedback field names — incorrectNotFinal, incorrectFinal,
// partlyCorrectNotFinal, partlyCorrectFinal — already match these keys, so
// feedbackKey addresses both shapes with no translation).
function extractDetailed(c) {
  const out = [];
  const push = (kind, label, text, meta) => { if (text != null && String(text).length) out.push(Object.assign({ kind, label, text: String(text) }, meta || {})); };
  if (c.body) push('body', null, c.body);
  const t = c._component;
  const items = c._items || [];
  if (t === 'mcq' || t === 'sortable') {
    items.forEach((it, i) => push('option', `Option ${i + 1}${it._shouldBeSelected ? ' (correct)' : ''}`, it.text, { itemIndex: i }));
  } else if (t === 'matching') {
    items.forEach((it, i) => {
      push('match-stem', `Row ${i + 1}`, it.text, { itemIndex: i });
      (it._options || []).forEach((o, j) => push('match-option', `  option${o._isCorrect ? ' (correct)' : ''}`, o.text, { itemIndex: i, optIndex: j }));
    });
  } else if (t === 'flipcard') {
    items.forEach((it, i) => {
      push('card-front', `Card ${i + 1} front`, (it.front && (it.front.title || it.front.body)) || '', { itemIndex: i, part: 'front' });
      push('card-back', `Card ${i + 1} back`, (it.back && (it.back.body || it.back.title)) || '', { itemIndex: i, part: 'back' });
    });
  } else if (t === 'accordion' || t === 'hotgraphic') {
    items.forEach((it, i) => {
      push('item-title', `Item ${i + 1}`, it.title, { itemIndex: i, part: 'title' });
      push('item-body', null, it.body, { itemIndex: i, part: 'body' });
    });
  } else if (t === 'checklist' || t === 'confidence') {
    items.forEach((it, i) => push('item', `Item ${i + 1}`, it.text, { itemIndex: i }));
  } else if (t === 'references') {
    items.forEach((it, i) => push('reference', `Reference ${i + 1}`, [it.title, it.href].filter(Boolean).join(' — '), { itemIndex: i }));
  }
  if (c.placeholder) push('placeholder', 'Placeholder', c.placeholder);
  const fb = c._feedback;
  if (fb) {
    if (fb.correct) push('feedback', 'Feedback — correct', fb.correct, { feedbackKey: 'correct' });
    if (fb._incorrect && fb._incorrect.notFinal) push('feedback', 'Feedback — incorrect (not final)', fb._incorrect.notFinal, { feedbackKey: 'incorrectNotFinal' });
    if (fb._incorrect && fb._incorrect.final) push('feedback', 'Feedback — incorrect (final)', fb._incorrect.final, { feedbackKey: 'incorrectFinal' });
    if (fb._partlyCorrect && fb._partlyCorrect.notFinal) push('feedback', 'Feedback — partly correct (not final)', fb._partlyCorrect.notFinal, { feedbackKey: 'partlyCorrectNotFinal' });
    if (fb._partlyCorrect && fb._partlyCorrect.final) push('feedback', 'Feedback — partly correct (final)', fb._partlyCorrect.final, { feedbackKey: 'partlyCorrectFinal' });
  }
  return out;
}

function truncateForLog(s, n) {
  s = String(s == null ? '' : s).replace(/\s+/g, ' ').trim();
  return s.length > (n || 100) ? s.slice(0, n || 100) + '…' : s;
}

// Writes one changed chunk into a BASE component (_items[]/_options[]/_feedback).
function applyBaseChunk(c, meta, newText) {
  if (meta.feedbackKey) {
    c._feedback = c._feedback || {};
    switch (meta.feedbackKey) {
      case 'correct': c._feedback.correct = newText; return;
      case 'incorrectNotFinal': c._feedback._incorrect = c._feedback._incorrect || {}; c._feedback._incorrect.notFinal = newText; return;
      case 'incorrectFinal': c._feedback._incorrect = c._feedback._incorrect || {}; c._feedback._incorrect.final = newText; return;
      case 'partlyCorrectNotFinal': c._feedback._partlyCorrect = c._feedback._partlyCorrect || {}; c._feedback._partlyCorrect.notFinal = newText; return;
      case 'partlyCorrectFinal': c._feedback._partlyCorrect = c._feedback._partlyCorrect || {}; c._feedback._partlyCorrect.final = newText; return;
    }
    return;
  }
  const item = c._items[meta.itemIndex];
  if (meta.part === 'front') { if (item.front.title) item.front.title = newText; else item.front.body = newText; return; }
  if (meta.part === 'back') { if (item.back.body) item.back.body = newText; else item.back.title = newText; return; }
  if (meta.part === 'title') { item.title = newText; return; }
  if (meta.part === 'body') { item.body = newText; return; }
  if (meta.optIndex !== undefined) { item._options[meta.optIndex].text = newText; return; }
  item.text = newText;
}

// Writes one changed chunk into a pack's generatedItems[key] entry (mcq:
// {body,items:[{text,...}],feedback}; matching: items[i]._options[] too).
function applyPackChunk(packEntry, meta, newText) {
  if (meta.feedbackKey) { packEntry.feedback = packEntry.feedback || {}; packEntry.feedback[meta.feedbackKey] = newText; return; }
  const item = packEntry.items[meta.itemIndex];
  if (meta.optIndex !== undefined) { item._options[meta.optIndex].text = newText; return; }
  item.text = newText;
}

function runScriptMode(scriptMdPath) {
  const sync = require('./lib/script-sync');
  const mergeCtx = require('../merge-context');

  const tier = arg('tier');
  const context = arg('context');
  const dryRun2 = process.argv.includes('--dry-run');
  if (!tier || !context) {
    console.error('usage: node tools/course-script-import.js --script <script.md> --tier <base-course-slug> --context <subject> [--dry-run]');
    process.exit(2);
  }
  if (!fs.existsSync(scriptMdPath)) { console.error(`No such file: ${scriptMdPath}`); process.exit(2); }

  const baseDir = path.join('courses', tier);
  const generatedDir = path.join('courses', '_generated', `${tier}-${context}`);
  const baseComponentsPath = path.join(baseDir, 'en', 'components.json');
  if (!fs.existsSync(baseComponentsPath)) { console.error(`No base course at ${baseDir} (expected ${baseComponentsPath}).`); process.exit(2); }
  if (!fs.existsSync(path.join(generatedDir, 'en', 'components.json'))) {
    console.error(`No generated course at ${generatedDir}. Run merge-context.js --context=${context} --tier=${tier} first.`);
    process.exit(2);
  }

  const liveTree = sync.loadCourseTree(generatedDir);
  const liveById = new Map(liveTree.components.map(c => [c._id, c]));

  const baseOriginalText = fs.readFileSync(baseComponentsPath, 'utf8');
  const baseComponents = JSON.parse(baseOriginalText);
  const baseById = new Map(baseComponents.map(c => [c._id, c]));

  const sections = sync.parseScriptMd(fs.readFileSync(scriptMdPath, 'utf8'));
  const markerPageToPageKey = mergeCtx.loadMarkerPageToPageKey();

  const plan = [];
  const problems = [];
  const packCache = new Map(); // packPath -> { path, data, original }
  function loadPack(pageKey) {
    const p = path.join(mergeCtx.CONTEXT_PACKS_ROOT, context, tier, `${pageKey}.json`);
    if (!packCache.has(p)) {
      if (!fs.existsSync(p)) return null;
      const original = fs.readFileSync(p, 'utf8');
      packCache.set(p, { path: p, original, data: JSON.parse(original) });
    }
    return packCache.get(p);
  }

  const PACK_ITEM_TYPES = ['mcq', 'matching'];
  const PACK_UNSUPPORTED_TYPES = ['accordion', 'annotated', 'branching', 'timeline'];

  for (const sec of sections) {
    const live = liveById.get(sec.id);
    if (!live) { problems.push(`${sec.id}: not found in generated course ${generatedDir} — skipped.`); continue; }
    if (!baseById.get(sec.id)) { problems.push(`${sec.id}: not found in BASE course ${baseDir} — skipped.`); continue; }

    const slot = mergeCtx.parseSlotMarker(live._classes);
    const pageKey = slot ? (markerPageToPageKey.get(slot.page) || slot.page) : null;
    const packKey = slot ? mergeCtx.packKeyFor(slot) : null;
    const isKnowledgeCheck = /knowledge-check-question/.test(live._classes || '');

    // ---- displayTitle ----
    if (live.displayTitle && sync.stripTags(live.displayTitle) !== sec.head) {
      if (slot && isKnowledgeCheck && PACK_ITEM_TYPES.includes(live._component)) {
        const pack = loadPack(pageKey);
        if (pack && pack.data.generatedItems && pack.data.generatedItems[packKey]) {
          plan.push({ id: sec.id, field: 'displayTitle', from: live.displayTitle, to: sec.head, target: 'pack', packPageKey: pageKey, packKey, packField: 'generatedItems' });
        } else {
          problems.push(`${sec.id}: heading changed, routes to a pack (slot__${slot.page}__${slot.slotType}) but no generatedItems["${packKey}"] entry exists in ${pageKey}.json — apply manually.`);
        }
      } else {
        plan.push({ id: sec.id, field: 'displayTitle', from: live.displayTitle, to: sec.head, target: 'base' });
      }
    }

    // ---- instruction (always base; merge-context never substitutes it) ----
    const liveInstruction = live.instruction ? sync.stripTags(live.instruction) : null;
    if ((liveInstruction || null) !== (sec.instruction || null)) {
      plan.push({ id: sec.id, field: 'instruction', from: live.instruction || '', to: sec.instruction || '', target: 'base' });
    }

    // ---- chunks ----
    const liveChunks = extractDetailed(live);
    const liveBody = liveChunks.find(c => c.kind === 'body') || null;
    const liveRest = liveChunks.filter(c => c.kind !== 'body');
    const parsedBodyChunks = sec.chunks.filter(c => c.kind === 'body');
    const parsedRest = sec.chunks.filter(c => c.kind !== 'body');

    // body field — possibly reassembled from several blank-line-split blocks
    const parsedBodyText = parsedBodyChunks.map(c => c.text).join('\n\n');
    const liveBodyPlain = liveBody ? sync.prose(liveBody.text) : '';
    if (liveBodyPlain.trim() !== parsedBodyText.trim()) {
      let routed = false;
      if (slot && !isKnowledgeCheck && !PACK_ITEM_TYPES.includes(live._component) && !PACK_UNSUPPORTED_TYPES.includes(live._component)) {
        const pack = loadPack(pageKey);
        if (pack && pack.data.generatedProse && Object.prototype.hasOwnProperty.call(pack.data.generatedProse, packKey)) {
          plan.push({ id: sec.id, field: 'body', from: liveBodyPlain, to: parsedBodyText, target: 'pack', packPageKey: pageKey, packKey, packField: 'generatedProse' });
          routed = true;
        }
      }
      if (!routed) {
        if (slot && PACK_UNSUPPORTED_TYPES.includes(live._component)) {
          problems.push(`${sec.id}: body changed on a subject-coupled "${live._component}" — pack write-back for this component type is not supported yet; apply manually (base write is also wrong here, since the body is pack-filled at merge).`);
        } else if (!sync.isSimpleHtml(liveBody ? liveBody.text : '')) {
          problems.push(`${sec.id}: body changed but original HTML is too complex to round-trip safely (inline markup beyond <p>/<ul>/<li>/<br>) — apply manually.`);
        } else {
          plan.push({ id: sec.id, field: 'body', from: liveBody ? liveBody.text : '', to: sync.htmlFromPlain(parsedBodyText), target: 'base' });
        }
      }
    }

    if (parsedRest.length !== liveRest.length) {
      problems.push(`${sec.id}: item/option/feedback count changed (live ${liveRest.length}, edited ${parsedRest.length}) — adding/removing items is not supported; left untouched.`);
      continue;
    }

    for (let i = 0; i < liveRest.length; i++) {
      const lc = liveRest[i], pc = parsedRest[i];
      if ((lc.label || null) !== (pc.label || null)) {
        problems.push(`${sec.id}: chunk ${i} label changed from "${lc.label}" to "${pc.label}" (e.g. a (correct) marker moved) — not supported; left untouched.`);
        continue;
      }
      const isHtmlBearing = lc.kind === 'item-body';
      const liveComparable = isHtmlBearing ? sync.prose(lc.text) : sync.stripTags(lc.text);
      if (liveComparable.trim() === pc.text.trim()) continue;

      let routed = false;
      if (slot && PACK_ITEM_TYPES.includes(live._component)) {
        const pack = loadPack(pageKey);
        if (pack && pack.data.generatedItems && pack.data.generatedItems[packKey]) {
          plan.push({ id: sec.id, field: 'chunk', kind: lc.kind, label: lc.label, meta: lc, from: lc.text, to: pc.text, target: 'pack', packPageKey: pageKey, packKey, packField: 'generatedItems' });
          routed = true;
        }
      }
      if (!routed) {
        if (isHtmlBearing && !sync.isSimpleHtml(lc.text)) {
          problems.push(`${sec.id} ${lc.label || lc.kind}: changed but original HTML too complex to round-trip safely — apply manually.`);
        } else {
          plan.push({ id: sec.id, field: 'chunk', kind: lc.kind, label: lc.label, meta: lc, from: lc.text, to: isHtmlBearing ? sync.htmlFromPlain(pc.text) : pc.text, target: 'base' });
        }
      }
    }
  }

  if (problems.length) {
    console.log(`${problems.length} chunk(s)/field(s) flagged as unsupported — left untouched:`);
    problems.forEach(p => console.log('  ! ' + p));
  }
  if (!plan.length) {
    console.log('\nNo supported changes detected.');
    process.exit(problems.length ? 1 : 0);
  }

  console.log(`\n${plan.length} change(s) planned:`);
  for (const ch of plan) {
    const label = ch.field === 'chunk' ? `${ch.id} ${ch.label || ch.kind}` : `${ch.id}.${ch.field}`;
    console.log(`  [${ch.target}] ${label}`);
    console.log(`      - ${truncateForLog(ch.from)}`);
    console.log(`      + ${truncateForLog(ch.to)}`);
  }

  if (dryRun2) { console.log('\nDry run — nothing written.'); process.exit(0); }

  for (const ch of plan) {
    if (ch.target === 'base') {
      const c = baseById.get(ch.id);
      if (ch.field === 'displayTitle') c.displayTitle = ch.to;
      else if (ch.field === 'instruction') c.instruction = ch.to;
      else if (ch.field === 'body') c.body = ch.to;
      else if (ch.field === 'chunk') applyBaseChunk(c, ch.meta, ch.to);
    } else {
      const pack = loadPack(ch.packPageKey);
      if (ch.packField === 'generatedProse') pack.data.generatedProse[ch.packKey] = ch.to;
      else if (ch.field === 'displayTitle') pack.data.generatedItems[ch.packKey].body = ch.to;
      else if (ch.field === 'chunk') applyPackChunk(pack.data.generatedItems[ch.packKey], ch.meta, ch.to);
    }
  }

  fs.writeFileSync(baseComponentsPath, JSON.stringify(baseComponents, null, 2) + '\n');
  for (const entry of packCache.values()) fs.writeFileSync(entry.path, JSON.stringify(entry.data, null, 2) + '\n');
  console.log(`\nWrote ${plan.filter(c => c.target === 'base').length} base change(s) to ${baseComponentsPath}.`);
  console.log(`Wrote pack change(s) to: ${[...packCache.values()].map(e => e.path).join(', ') || '(none)'}.`);

  console.log('\nValidating...');
  const v = cp.spawnSync('node', ['tools/verify-course.js', '--course=' + tier], { encoding: 'utf8' });
  process.stdout.write(v.stdout || ''); process.stderr.write(v.stderr || '');
  if (v.status !== 0) {
    fs.writeFileSync(baseComponentsPath, baseOriginalText);
    for (const entry of packCache.values()) fs.writeFileSync(entry.path, entry.original);
    console.error('\nverify-course FAILED — base components.json and pack file(s) restored. No changes landed.');
    process.exit(1);
  }
  console.log('\nverify-course PASSED.');

  console.log(`\nRecompiling: node merge-context.js --context=${context} --tier=${tier}`);
  const mc = cp.spawnSync('node', ['merge-context.js', `--context=${context}`, `--tier=${tier}`], { encoding: 'utf8' });
  process.stdout.write(mc.stdout || ''); process.stderr.write(mc.stderr || '');
  if (mc.status !== 0) {
    console.error('\nmerge-context.js FAILED — base/pack JSON changes are landed and verified, but the generated course was not refreshed. Fix the error above, then re-run merge-context.js and grunt build yourself.');
    process.exit(1);
  }

  const srcCourse = path.join('src', 'course');
  try { fs.unlinkSync(srcCourse); } catch (e) { /* no existing symlink to remove */ }
  fs.symlinkSync(path.join('..', 'courses', '_generated', `${tier}-${context}`), srcCourse);
  console.log(`Relinked src/course -> courses/_generated/${tier}-${context}`);

  console.log('\nBuilding: npx grunt build');
  const gb = cp.spawnSync('npx', ['grunt', 'build'], { encoding: 'utf8' });
  process.stdout.write(gb.stdout || ''); process.stderr.write(gb.stderr || '');
  if (gb.status !== 0) { console.error('\ngrunt build FAILED — see output above.'); process.exit(1); }

  const resolved = resolveManifest(baseDir, null);
  const subjectShortSlug = shortSlugFromManifest(resolved.manifest, context);
  if (subjectShortSlug) {
    const version = bumpVersion(subjectShortSlug, 'edit-import-subject', { file: path.basename(scriptMdPath), changes: plan.length });
    console.log(`Content version: ${subjectShortSlug} -> v${version}`);
  } else {
    console.log(`Content version: could not resolve a short slug for ${baseDir} (context ${context}) — version record not updated.`);
  }

  console.log('\nDone: edits landed in base/pack JSON, merged, and built.');
  process.exit(0);
}
