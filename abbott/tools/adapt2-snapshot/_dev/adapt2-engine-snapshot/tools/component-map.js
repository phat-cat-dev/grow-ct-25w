#!/usr/bin/env node
/**
 * component-map.js — organise the components against the design data structures.
 *
 * Cross-references the palette (design-kb.palette.json), the activity patterns
 * (design-kb.activity-patterns.json), the content shapes, the real src plugins
 * and a course's actual usage, then reports coverage and gaps. The analytical
 * companion to ab-component-reference.js (which documents each component on its
 * own). Read-only; writes a Markdown report.
 *
 * Usage: node tools/component-map.js [--course <content-dir>] [--out exports/component-map.md]
 */
'use strict';
const fs = require('fs');
const path = require('path');
function arg(n, d) { const i = process.argv.indexOf('--' + n); return (i >= 0 && i + 1 < process.argv.length) ? process.argv[i + 1] : d; }
const courseDir = arg('course', 'courses/understanding-learning-assessment-feedback-introductory');
const outPath = arg('out', 'exports/component-map.md');
const rd = p => JSON.parse(fs.readFileSync(p, 'utf8'));

const palette = rd('design-kb/design-kb.palette.json').entries;
const patterns = rd('design-kb/design-kb.activity-patterns.json').patterns;
const shapes = rd('design-kb/design-kb.content-shapes.json').shapes;
const courseComponents = (() => { try { return rd(path.join(courseDir, 'en', 'components.json')); } catch { return []; } })();
const usedCount = {};
for (const c of courseComponents) usedCount[c._component] = (usedCount[c._component] || 0) + 1;

// src plugins by their component/extension name (lowercased)
const srcByName = {};
for (const base of ['src/components', 'src/extensions']) {
  if (!fs.existsSync(base)) continue;
  for (const d of fs.readdirSync(base)) {
    const bp = path.join(base, d, 'bower.json');
    if (!fs.existsSync(bp)) continue;
    const b = rd(bp); const nm = (b.component || b.extension || '').toLowerCase();
    if (nm) srcByName[nm] = { plugin: d, kind: b.component ? 'component' : 'extension' };
  }
}

// palette name -> Adapt _component alias (where they differ)
const ALIAS = { textinput: 'opentext' };
const adaptName = n => ALIAS[n] || n;
const usedFor = n => usedCount[adaptName(n)] || usedCount[n] || 0;

// patterns that realise a given palette id
const realisersOf = palId => patterns.filter(p => (p.realisations || []).some(r => r.component === palId)).map(p => p.id.replace('activity-patterns/', ''));

// ---- report ----
const L = [];
L.push('# Component map — components against the data structures\n');
L.push(`_Generated ${new Date().toISOString()}. Cross-references palette x patterns x shapes x src plugins x usage in \`${path.basename(courseDir)}\`._\n`);

L.push('## Palette entries\n');
L.push('| palette id | kind | origin | build | src plugin | used (course) | realised by patterns | fits shapes |');
L.push('|---|---|---|---|---|---|---|---|');
for (const e of palette) {
  const src = srcByName[e.name.toLowerCase()];
  const used = usedFor(e.name);
  const pats = realisersOf(e.id);
  const fits = (e.contentFit || []).map(f => f.shape).join(', ');
  L.push(`| \`${e.id}\` | ${e.kind} | ${e.origin} | ${e.build || 'available'} | ${src ? src.plugin : (e.origin === 'core' ? '(contrib)' : '—')} | ${used ? used : '·'} | ${pats.join(', ') || '·'} | ${fits || '·'} |`);
}

L.push('\n## Activity patterns\n');
L.push('| pattern | intent | slotTypes | servesShapes | realisations |');
L.push('|---|---|---|---|---|');
for (const p of patterns) L.push(`| \`${p.id.replace('activity-patterns/', '')}\` | ${p.intent || ''} | ${(p.slotTypes || []).join(', ')} | ${(p.servesShapes || []).map(s => s.replace('content-shapes/', '')).join(', ')} | ${(p.realisations || []).map(r => r.component.replace('palette/', '')).join(', ')} |`);

// ---- findings ----
L.push('\n## Findings / gaps\n');
const F = [];
// 1. palette entries not used in the pilot
const unused = palette.filter(e => e.kind === 'component' && !usedFor(e.name)).map(e => e.name);
F.push(`**Palette components not used in this course (${unused.length}):** ${unused.join(', ')}. Available to author with, not yet exercised.`);
// 2. src plugins absent from the palette (built, not wired into the design model)
const palNames = new Set(palette.map(e => e.name.toLowerCase()));
const srcNotInPalette = Object.values(srcByName).filter(s => !palNames.has(s.plugin.replace(/^adapt-abbott-/, '').toLowerCase()) && !palNames.has((s.plugin.match(/adapt-abbott-(.+)/) || [])[1] || ''));
// recompute simply by bower name
const srcMissing = [];
for (const base of ['src/components', 'src/extensions']) {
  if (!fs.existsSync(base)) continue;
  for (const d of fs.readdirSync(base)) {
    const bp = path.join(base, d, 'bower.json'); if (!fs.existsSync(bp)) continue;
    const b = rd(bp); const nm = (b.component || b.extension || '').toLowerCase(); if (!nm) continue;
    if (nm === 'abbotttheme') continue;
    if (!palNames.has(nm)) srcMissing.push(`${d} (${nm})`);
  }
}
F.push(`**Built src plugins NOT represented in the palette (${srcMissing.length}):** ${srcMissing.join(', ') || 'none'}. These can't be chosen by \`/gate\`'s palette selection until added.`);
// 3. palette entries resolving to no component source (excluding intentional pending/deprecated)
const unresolved = palette.filter(e => !srcByName[e.name.toLowerCase()] && e.origin !== 'core' && e.build !== 'pending' && e.build !== 'deprecated').map(e => `${e.name} (${e.origin})`);
F.push(`**Palette entries with no resolvable source here (${unresolved.length}):** ${unresolved.join(', ') || 'none'}. (core = contrib, fetched at install; others should map to a src plugin. Entries flagged build=pending/deprecated are excluded — see below.)`);
// 3b. pending / deprecated (intentional states)
const pending = palette.filter(e => e.build === 'pending').map(e => e.name);
const deprecated = palette.filter(e => e.build === 'deprecated').map(e => e.name);
F.push(`**Designed but not built (build=pending, ${pending.length}):** ${pending.join(', ') || 'none'}. Design retained; component awaiting (re)build; do not author with these yet.`);
F.push(`**Deprecated (build=deprecated, ${deprecated.length}):** ${deprecated.join(', ') || 'none'}. Superseded; retained for provenance, not for new authoring.`);
// 4. patterns referencing a missing palette id
const palIds = new Set(palette.map(e => e.id));
const badReal = [];
for (const p of patterns) for (const r of (p.realisations || [])) if (!palIds.has(r.component)) badReal.push(`${p.id} -> ${r.component}`);
F.push(`**Pattern realisations pointing at a missing palette id (${badReal.length}):** ${badReal.join(', ') || 'none'}.`);
// 5. overlaps — resolved
F.push(`**Overlaps resolved (9 Oct 2026):** \`textinput\` vs \`opentext\` was a genuine duplicate (both serve reflective-prompt) — \`textinput\` is now build=deprecated and \`opentext\` is canonical (write-own-thinking realises opentext only). \`mcq\` vs \`gmcq\` is NOT a duplicate — \`gmcq\` is the graphic/image MCQ (visual-discrimination), a distinct core component kept alongside \`mcq\`.`);
// 6. two shape vocabularies
F.push(`**Two shape vocabularies:** patterns' \`servesShapes\` use \`content-shapes/*\` (${shapes.length} knowledge-type shapes: ${shapes.map(s => s.id.replace('content-shapes/', '')).join(', ')}), while palette \`contentFit\` uses a different set of shape names (teaching-prose, retrieval-practice, …). These are not reconciled; a component is matched to a slot through *patterns* (servesShapes), so the palette contentFit vocabulary is advisory. Worth unifying or cross-walking.`);
L.push(F.map((f, i) => `${i + 1}. ${f}`).join('\n\n'));

fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, L.join('\n') + '\n');
console.log(`Component map: ${outPath}`);
console.log(`palette: ${palette.length} | patterns: ${patterns.length} | shapes: ${shapes.length} | src plugins: ${Object.keys(srcByName).length} | course component types: ${Object.keys(usedCount).length}`);
console.log(`findings: ${F.length}`);
