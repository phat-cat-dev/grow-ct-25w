#!/usr/bin/env node
/**
 * template-field-map.js — a visual, field-by-field record of every Adapt page
 * template (W-OPEN, C-PRE, LESSON, SUMM, C-POST, W-CLOSE): every block's
 * naming (key/title/displayTitle), what fills it, and — where one exists —
 * the authoring advice that tells an agent (or a human) what to write there.
 *
 * Single source: design-kb/design-kb.skeletons.json. This tool only reads and
 * formats it; it adds no advice of its own. If a block carries no authoring
 * prompt, the report says so plainly rather than inventing one.
 *
 * Two kinds of advice a coupled slot can carry, shown separately because they
 * have different audiences:
 *   - authoringPrompt       — advice for whoever authors the slot directly
 *                              (the shell author, or a CXP agent on a
 *                              structured/whole-prose slot with no separate
 *                              standing prompt).
 *   - standingContextPrompt — a layout-level instruction a CXP agent applies
 *                              when filling this slot for a specific subject,
 *                              on top of (not instead of) the shell's prose.
 *
 * Usage:
 *   node tools/template-field-map.js [--out exports/template-field-map.md]
 */
'use strict';
const fs = require('fs');
const path = require('path');

function arg(name, def) { const i = process.argv.indexOf('--' + name); return (i >= 0 && i + 1 < process.argv.length) ? process.argv[i + 1] : def; }
const outPath = arg('out', 'exports/template-field-map.md');

const kbPath = path.join(__dirname, '..', 'design-kb', 'design-kb.skeletons.json');
const kb = JSON.parse(fs.readFileSync(kbPath, 'utf8'));

const archetypeById = new Map(kb.archetypes.map(a => [a.id, a]));

// Page order: fixedPages, with the lesson archetype spliced in at its
// declared insertion point (it has no fixed count, so pageSet.fixedPages
// deliberately excludes it).
const order = [];
for (const p of kb.pageSet.fixedPages) {
  order.push({ baseKey: p.baseKey, archetypeId: p.archetype, displayTitle: p.displayTitle || null });
  if (p.baseKey === kb.pageSet.lessonInsertionPoint.afterBaseKey) {
    order.push({ baseKey: 'LESSON (repeats, one per lesson)', archetypeId: kb.pageSet.lessonInsertionPoint.archetype, displayTitle: null });
  }
}

const esc = s => String(s == null ? '' : s);
const joinList = a => Array.isArray(a) ? a.join(', ') : esc(a);

function fmtBlock(n, b) {
  const L = [];
  L.push(`### ${n}. \`${b.key}\` — "${b.title}"`);
  const bits = [];
  bits.push(`kind: **${b.kind}**`);
  bits.push(`role: **${b.role}**`);
  bits.push(`required: **${b.required}**`);
  if (b.interactionMode) bits.push(`interactionMode: **${b.interactionMode}**`);
  if (b.gateAfter) bits.push(`**gate immediately after this block**`);
  L.push('- ' + bits.join(' · '));
  L.push(`- displayTitle (visible heading): ${b.displayTitle === null || b.displayTitle === undefined ? '_(none — no visible heading)_' : `"${b.displayTitle}"`}`);

  if (b.component) {
    L.push(`- component: \`${b.component}\`${b.extensions ? ` + extensions: ${b.extensions.map(e => `\`${e}\``).join(', ')}` : ''}`);
  }
  if (b.fixedBody) {
    L.push(`- **fixed shell text** (identical in every course, not authored per course):`);
    L.push(`  > ${b.fixedBody.replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim()}`);
  }

  const s = b.slot;
  if (s) {
    L.push(`- slotType: \`${s.slotType}\``);
    L.push(`- component options: ${s.componentOptions ? s.componentOptions.map(c => `\`${c}\``).join(', ') : '_(none declared)_'}`);
    L.push(`- content coupling: ${s.contextCoupling ? s.contextCoupling.map(c => `\`${c}\``).join(', ') : '_(none declared)_'}`);
    if (s.band) L.push(`- band: ${s.band.min}–${s.band.max} ${s.band.unit}${s.bandRationale ? ` — ${joinList(s.bandRationale)}` : ''}`);
    if (s.selectionModel) L.push(`- selection model: ${s.selectionModel}`);

    // the two advice channels, called out explicitly
    if (s.authoringPrompt) {
      L.push(`- **authoring prompt (direct — shell author / agent writing this slot):**`);
      L.push(`  > ${s.authoringPrompt}`);
    }
    if (s.standingContextPrompt) {
      L.push(`- **standing context prompt (CXP agent, filling this slot for a subject):**`);
      L.push(`  > ${s.standingContextPrompt}`);
    }
    if (!s.authoringPrompt && !s.standingContextPrompt) {
      L.push(`- authoring advice: _(none recorded for this slot — furniture, or a routing-only slot)_`);
    }
    if (s.authoringVenueNote) L.push(`- authoring venue: ${s.authoringVenueNote}`);
    if (s.positionRules) {
      L.push(`- position rules:`);
      for (const r of s.positionRules) L.push(`  - position ${r.position}: coupling ${joinList(r.contextCoupling)} — ${r.note}`);
    }
  } else if (!b.component && !b.fixedBody) {
    L.push(`- _(no component and no slot declared on this block)_`);
  }

  // agentAuthor: an AI-authoring-agent instruction block, sibling to (not
  // nested in) slot (see docs/authoring/agent-author-metadata.md). Baseline
  // fields: content, context (string, or a tier object), relation,
  // warnings[], bestPractice[]. Optional structural "byTier" overrides the
  // baseline per tier, selected first. Mode overlays agentAuthorWritten /
  // agentAuthorDialogue are siblings of agentAuthor, each { notes: [...] }.
  const aa = b.agentAuthor;
  if (aa) {
    L.push(`- **agentAuthor**:`);
    if (aa.content) L.push(`  - content: ${aa.content}`);
    if (aa.context) {
      if (typeof aa.context === 'string') {
        L.push(`  - context: ${aa.context}`);
      } else {
        for (const tier of ['all', 'introductory', 'intermediate', 'advanced']) {
          if (aa.context[tier]) L.push(`  - context.${tier}: ${aa.context[tier]}`);
        }
      }
    }
    if (aa.relation) L.push(`  - relation: ${aa.relation}`);
    if (aa.warnings) for (const w of aa.warnings) L.push(`  - warning: ${w}`);
    if (aa.bestPractice) for (const p of aa.bestPractice) L.push(`  - bestPractice: ${p}`);
    if (aa.byTier) {
      for (const tier of ['introductory', 'intermediate', 'advanced']) {
        const t = aa.byTier[tier];
        if (!t) continue;
        if (!t.applies) { L.push(`  - byTier.${tier}: applies: false${t.note ? ` — ${t.note}` : ''}`); continue; }
        const extras = Object.keys(t).filter(k => !['applies', 'displayTitle', 'content'].includes(k));
        L.push(`  - byTier.${tier}: displayTitle: "${t.displayTitle || ''}"`);
        L.push(`    > ${t.content}`);
        for (const k of extras) L.push(`    - ${k}: ${JSON.stringify(t[k])}`);
      }
    }
  }
  if (b.agentAuthorWritten && b.agentAuthorWritten.notes) for (const n of b.agentAuthorWritten.notes) L.push(`  - agentAuthorWritten.notes: ${n}`);
  if (b.agentAuthorDialogue && b.agentAuthorDialogue.notes) for (const n of b.agentAuthorDialogue.notes) L.push(`  - agentAuthorDialogue.notes: ${n}`);
  return L.join('\n');
}

function fmtArchetype(label, archetype) {
  const L = [];
  L.push(`\n## ${label}  <!-- ${archetype.id} -->`);
  L.push(`_pageType: \`${archetype.pageType}\` · archetype version ${archetype.version} · source: ${archetype.sourcePointer.doc}${archetype.sourcePointer.ref ? ` (${archetype.sourcePointer.ref})` : ''}_`);
  archetype.blockSequence.forEach((b, i) => { L.push(''); L.push(fmtBlock(i + 1, b)); });
  return L.join('\n');
}

const out = [];
out.push(`# Adapt course template field map`);
out.push(`\n_Generated ${new Date().toISOString()} from \`design-kb/design-kb.skeletons.json\` (kbVersion ${kb.kbVersion}). This is a read-only rendering — the skeletons file is the source of truth; edit that, not this report._`);
out.push(`\n## Legend`);
out.push(`- **kind**: \`fixed\` (same shell content/shape in every course) or \`variable\` (a slot whose filler is chosen per course/lesson).`);
out.push(`- **role**: pedagogical role, also used to key \`completionRules\`/\`iconRules\` elsewhere in the skeletons file.`);
out.push(`- **content coupling**: how the slot's content reaches the learner — \`shell-coupled\` (written once, generic), \`token-substitution\` (shell text carrying a \`{{token}}\`), \`structured-fields\` (shell frame + named fields filled per subject), \`whole-prose\` (empty in the shell, written per subject).`);
out.push(`- **authoring prompt**: direct instruction for whoever writes this slot's content (shell author or an agent).`);
out.push(`- **standing context prompt**: a layout-level instruction a context-pack (CXP) agent applies when filling a coupled slot for a specific subject, on top of the shell's own prose.`);

out.push(`\n## Page order`);
order.forEach((o, i) => out.push(`${i + 1}. ${o.baseKey}${o.displayTitle ? ` ("${o.displayTitle}")` : ''} — \`${o.archetypeId}\``));

for (const o of order) {
  const archetype = archetypeById.get(o.archetypeId);
  if (!archetype) { out.push(`\n## ${o.baseKey}\n_(archetype ${o.archetypeId} not found in design-kb.skeletons.json)_`); continue; }
  out.push(fmtArchetype(o.baseKey + (o.displayTitle ? ` ("${o.displayTitle}")` : ''), archetype));
}

const report = out.join('\n') + '\n';
fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, report);
console.log(`Template field map written to ${outPath}`);
