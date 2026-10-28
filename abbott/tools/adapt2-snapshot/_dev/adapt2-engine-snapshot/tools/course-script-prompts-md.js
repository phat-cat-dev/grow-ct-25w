#!/usr/bin/env node
/**
 * course-script-prompts-md.js — the ".script.md" screenplay (see
 * course-script-md.js), annotated at every section heading with the
 * authoring-advice metadata for that slot from
 * design-kb/design-kb.skeletons.json (the same source template-field-map.js
 * reports on, cross-referenced here against the actual built course).
 *
 * Each block in a page is matched to its archetype's blockSequence entry by
 * position (the course shell is generated from that same sequence, so
 * position i in the page is position i in the archetype - see
 * generate-course-shell.js). The match is positional only, not by key name,
 * so a page with extra/missing blocks relative to its archetype will show a
 * "position has no skeleton entry" note rather than a wrong guess.
 *
 * The metadata lands in an HTML comment directly under the heading - inert
 * in a rendered Markdown view, but present in the raw file for an agent (or
 * a human with the source open) to read alongside what was actually
 * authored there.
 *
 * Usage:
 *   node tools/course-script-prompts-md.js --course <content-dir>
 *        [--short-slug <slug>] [--subject <ctx>] [--manifest <file>]
 *        [--out <file>]   (default: exports/<short-slug>.script.prompts.md)
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { resolveManifest, shortSlugFromManifest } = require('./lib/content-version');

function arg(name, def) { const i = process.argv.indexOf('--' + name); return (i >= 0 && i + 1 < process.argv.length) ? process.argv[i + 1] : def; }
const courseDir = arg('course');
let shortSlug = arg('short-slug', null);
const subject = arg('subject', null);
let manifestPath = arg('manifest', null);
let outPath = arg('out', null);
if (!courseDir) {
  console.error('usage: node tools/course-script-prompts-md.js --course <content-dir> [--short-slug <slug>] [--subject <ctx>] [--manifest <file>] [--out <file>]');
  process.exit(2);
}
const rd = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const stripTags = s => String(s == null ? '' : s).replace(/<[^>]+>/g, '').trim();
const prose = s => String(s == null ? '' : s)
  .replace(/<li[^>]*>/gi, '\n- ')
  .replace(/<\/(p|li|h[1-6]|div|ul|ol)>/gi, '\n\n')
  .replace(/<br\s*\/?>/gi, '\n')
  .replace(/<[^>]+>/g, '')
  .replace(/\n{3,}/g, '\n\n')
  .replace(/[ \t]+\n/g, '\n')
  .trim();

const en = f => rd(path.join(courseDir, 'en', f));
const course = en('course.json');
const cos = en('contentObjects.json');
const articles = en('articles.json');
const blocks = en('blocks.json');
const components = en('components.json');
const courseObj = Array.isArray(course) ? course[0] : course;

const resolved = resolveManifest(courseDir, manifestPath);
manifestPath = resolved.manifestPath;
if (!shortSlug) shortSlug = shortSlugFromManifest(resolved.manifest, subject);
if (!shortSlug) { console.error('No short slug: pass --short-slug, or supply --manifest whose onb-04_naming records a shortSlug.'); process.exit(2); }
if (!outPath) outPath = path.join('exports', `${shortSlug}.script.prompts.md`);

// ---- skeletons: archetype-by-baseKey, same convention as template-field-map.js ----
const kb = rd(path.join(__dirname, '..', 'design-kb', 'design-kb.skeletons.json'));
const archetypeById = new Map(kb.archetypes.map(a => [a.id, a]));
const baseKeyArchetype = {};
for (const p of kb.pageSet.fixedPages) baseKeyArchetype[p.baseKey] = p.archetype;
baseKeyArchetype.LESSON = kb.pageSet.lessonInsertionPoint.archetype;

// Which fixed baseKey (if any) does this page _id belong to? Fixed baseKeys
// appear verbatim as a path segment in the id (e.g. "...-W-OPEN-co-01");
// anything else matching /L\d+/ (bare or slug-prefixed) is a LESSON page.
const fixedBaseKeys = Object.keys(baseKeyArchetype).filter(k => k !== 'LESSON');
function baseKeyOf(pageId) {
  for (const k of fixedBaseKeys) if (new RegExp(`(^|-)${k}(-|$)`).test(pageId)) return k;
  if (/(^|-)L\d+(-|$)/.test(pageId)) return 'LESSON';
  return null;
}

// ---- tree ----
const childrenOf = (arr, pid) => arr.filter(x => x._parentId === pid);
const pages = cos.filter(o => o._type === 'page');

// ---- component content extraction (unchanged from course-script-md.js) ----
function extract(c) {
  const out = [];
  const push = (kind, label, text, meta) => { if (text != null && String(text).length) out.push({ kind, label, text: String(text), ...(meta || {}) }); };
  if (c.body) push('body', null, c.body);
  const t = c._component;
  const items = c._items || [];
  if (t === 'mcq' || t === 'sortable') {
    items.forEach((it, i) => push('option', `Option ${i + 1}${it._shouldBeSelected ? ' (correct)' : ''}`, it.text));
  } else if (t === 'matching') {
    items.forEach((it, i) => {
      push('match-stem', `Row ${i + 1}`, it.text);
      (it._options || []).forEach(o => push('match-option', `  option${o._isCorrect ? ' (correct)' : ''}`, o.text));
    });
  } else if (t === 'flipcard') {
    items.forEach((it, i) => {
      push('card-front', `Card ${i + 1} front`, (it.front && (it.front.title || it.front.body)) || '');
      push('card-back', `Card ${i + 1} back`, (it.back && (it.back.body || it.back.title)) || '');
    });
  } else if (t === 'accordion' || t === 'hotgraphic') {
    items.forEach((it, i) => { push('item-title', `Item ${i + 1}`, it.title); push('item-body', null, it.body); });
  } else if (t === 'checklist' || t === 'confidence') {
    items.forEach((it, i) => push('item', `Item ${i + 1}`, it.text));
  } else if (t === 'references') {
    items.forEach((it, i) => push('reference', `Reference ${i + 1}`, [it.title, it.href].filter(Boolean).join(' — ')));
  }
  if (c.placeholder) push('placeholder', 'Placeholder', c.placeholder);
  const fb = c._feedback;
  if (fb) {
    if (fb.correct) push('feedback', 'Feedback — correct', fb.correct);
    if (fb._incorrect && fb._incorrect.notFinal) push('feedback', 'Feedback — incorrect (not final)', fb._incorrect.notFinal);
    if (fb._incorrect && fb._incorrect.final) push('feedback', 'Feedback — incorrect (final)', fb._incorrect.final);
    if (fb._partlyCorrect && fb._partlyCorrect.notFinal) push('feedback', 'Feedback — partly correct (not final)', fb._partlyCorrect.notFinal);
    if (fb._partlyCorrect && fb._partlyCorrect.final) push('feedback', 'Feedback — partly correct (final)', fb._partlyCorrect.final);
  }
  return out;
}

const coupling = c => {
  const m = String(c._classes || '').match(/slot__([A-Za-z0-9-]+)__([A-Za-z0-9-]+)(?:__([A-Za-z0-9-]+))?/);
  return m ? { page: m[1], slot: m[2], part: m[3] || null } : null;
};

// HTML comments can't survive a literal "--" in their content; collapse any
// run of two or more hyphens to an en dash so the comment always closes
// cleanly, however the advice text happens to be punctuated.
const commentSafe = s => String(s == null ? '' : s).replace(/-{2,}/g, '–').trim();

// agentAuthor: an AI-authoring-agent instruction block, sibling to (not
// nested in) a block's slot (see docs/authoring/agent-author-metadata.md).
// Baseline fields: content, relation, warnings[], bestPractice[]. `context`
// is the targeting layer: a bare string (shorthand for {all}), or an object
// of named steers - "all" (base) plus any of byTier/byQualifier/bySubject/
// byInstitution (reserved, same entry shape as byTier) - each steer an
// object keyed by an id (tier name / qualifier id / CAH grouping /
// institution id), each entry a plain string or a structural object
// (applies, displayTitle, content, context, relation, warnings[],
// bestPractice[], sideways, forwardBack, note). Mode overlays
// agentAuthorWritten/agentAuthorDialogue sit as siblings of agentAuthor,
// each just { notes: [...] }.
const TIER_ORDER = ['introductory', 'intermediate', 'advanced'];
function fmtSteerEntry(steerName, key, entry, L) {
  const tag = `agentAuthor.context.${steerName}.${key}`;
  if (typeof entry === 'string') { L.push(`${tag}: ${commentSafe(entry)}`); return; }
  if (entry.applies === false) { L.push(`${tag}: applies: false${entry.note ? ` — ${commentSafe(entry.note)}` : ''}`); return; }
  const known = ['applies', 'displayTitle', 'content', 'context', 'relation', 'warnings', 'bestPractice', 'note'];
  const bits = [];
  if (entry.displayTitle) bits.push(`displayTitle: ${entry.displayTitle}`);
  if (entry.content) bits.push(`content: ${commentSafe(entry.content)}`);
  if (entry.context) bits.push(`context: ${commentSafe(entry.context)}`);
  if (entry.relation) bits.push(`relation: ${commentSafe(entry.relation)}`);
  if (entry.warnings) for (const w of entry.warnings) bits.push(`warning: ${commentSafe(w)}`);
  if (entry.bestPractice) for (const p of entry.bestPractice) bits.push(`bestPractice: ${commentSafe(p)}`);
  for (const k of Object.keys(entry).filter(k => !known.includes(k))) bits.push(`${k}: ${commentSafe(JSON.stringify(entry[k]))}`);
  L.push(`${tag}: ${bits.join('; ')}`);
}
function fmtAgentAuthor(b, L) {
  const aa = b.agentAuthor;
  if (aa) {
    if (aa.content) L.push(`agentAuthor.content: ${commentSafe(aa.content)}`);
    if (aa.context) {
      if (typeof aa.context === 'string') {
        L.push(`agentAuthor.context.all: ${commentSafe(aa.context)}`);
      } else {
        if (aa.context.all) L.push(`agentAuthor.context.all: ${commentSafe(aa.context.all)}`);
        for (const steerName of ['byTier', 'byQualifier', 'bySubject', 'byInstitution']) {
          const steer = aa.context[steerName];
          if (!steer) continue;
          const keys = steerName === 'byTier' ? TIER_ORDER.filter(t => steer[t]) : Object.keys(steer);
          for (const key of keys) fmtSteerEntry(steerName, key, steer[key], L);
        }
      }
    }
    if (aa.relation) L.push(`agentAuthor.relation: ${commentSafe(aa.relation)}`);
    if (aa.warnings) for (const w of aa.warnings) L.push(`agentAuthor.warnings: ${commentSafe(w)}`);
    if (aa.bestPractice) for (const p of aa.bestPractice) L.push(`agentAuthor.bestPractice: ${commentSafe(p)}`);
  }
  if (b.agentAuthorWritten && b.agentAuthorWritten.notes) for (const n of b.agentAuthorWritten.notes) L.push(`agentAuthorWritten.notes: ${commentSafe(n)}`);
  if (b.agentAuthorDialogue && b.agentAuthorDialogue.notes) for (const n of b.agentAuthorDialogue.notes) L.push(`agentAuthorDialogue.notes: ${commentSafe(n)}`);
}

// ---- the per-slot metadata panel ----
function fmtSkeletonMeta(skeletonBlock) {
  if (!skeletonBlock) return '<!-- no skeleton block at this position (page/archetype sequence mismatch, or an unmapped page) -->';
  const b = skeletonBlock;
  const L = [];
  L.push(`skeleton key: ${b.key}`);
  L.push(`kind: ${b.kind}; role: ${b.role}; required: ${b.required}`);
  const s = b.slot;
  if (s) {
    if (s.slotType) L.push(`slotType: ${s.slotType}`);
    if (s.contextCoupling) L.push(`content coupling: ${Array.isArray(s.contextCoupling) ? s.contextCoupling.join(', ') : s.contextCoupling}`);
    if (s.authoringPrompt) L.push(`authoringPrompt: ${commentSafe(s.authoringPrompt)}`);
    if (s.standingContextPrompt) L.push(`standingContextPrompt: ${commentSafe(s.standingContextPrompt)}`);
    if (s.authoringVenueNote) L.push(`authoringVenue: ${commentSafe(s.authoringVenueNote)}`);
    if (!s.authoringPrompt && !s.standingContextPrompt) L.push(`authoring advice: (none recorded for this slot - furniture, or a routing-only slot)`);
  } else if (b.fixedBody) {
    L.push(`fixed shell text (not authored per course)`);
  } else {
    L.push(`authoring advice: (none - fixed block, no slot declared)`);
  }
  fmtAgentAuthor(b, L);
  return '<!--\n' + L.join('\n') + '\n-->';
}

// ---- SCRIPT.PROMPTS (.md) — the screenplay, annotated ----
function scriptPromptsMd() {
  const L = [];
  L.push(`# ${stripTags(courseObj.displayTitle || courseObj.title || shortSlug)} — course script (annotated with authoring prompts)  <!-- ${shortSlug} -->`);
  L.push(`\n_Same reading-order content as the plain .script.md, with each section's design-kb.skeletons.json authoring advice attached in an HTML comment underneath its heading (inert in a rendered view; present in the raw file). Generated ${new Date().toISOString()}._`);
  for (const page of pages) {
    const baseKey = baseKeyOf(page._id);
    const archetypeId = baseKey && baseKeyArchetype[baseKey];
    const archetype = archetypeId && archetypeById.get(archetypeId);
    const blockSeq = archetype ? archetype.blockSequence : null;
    L.push(`\n## ${stripTags(page.displayTitle || page.title || page._id)}  <!-- page ${page._id}${archetypeId ? ` archetype:${archetypeId}` : ' archetype:unmapped'} -->`);
    let blockPos = 0;
    for (const a of childrenOf(articles, page._id)) {
      if (a.displayTitle) L.push(`\n### ${stripTags(a.displayTitle)}  <!-- article ${a._id} -->`);
      for (const b of childrenOf(blocks, a._id)) {
        const skeletonBlock = blockSeq ? blockSeq[blockPos] : null;
        blockPos += 1;
        const blockComponents = childrenOf(components, b._id);
        blockComponents.forEach((c, ci) => {
          const head = stripTags(c.displayTitle) || b.title || `(${c._component})`;
          L.push(`\n#### ${head}  <!-- ${c._id} ${c._component} -->`);
          L.push(ci === 0 ? fmtSkeletonMeta(skeletonBlock) : `<!-- same slot as above (${skeletonBlock ? skeletonBlock.key : 'unmapped'}) -->`);
          const cpl = coupling(c);
          const chunks = extract(c);
          if (cpl && !chunks.length) L.push(`\n_⟦ CXP slot ${cpl.page}/${cpl.slot}${cpl.part ? '/' + cpl.part : ''} — subject-filled at merge; empty in the base ⟧_`);
          if (c.instruction) L.push(`\n_${stripTags(c.instruction)}_`);
          for (const ch of chunks) {
            if (ch.kind === 'feedback') L.push(`\n> **${ch.label}:** ${stripTags(ch.text)}`);
            else if (ch.label) L.push(`\n- **${ch.label}:** ${stripTags(ch.text)}`);
            else L.push(`\n${prose(ch.text)}`);
          }
        });
      }
    }
  }
  return L.join('\n') + '\n';
}

fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, scriptPromptsMd());
console.log(`Course script (annotated): ${outPath}`);
console.log(`Pages: ${pages.length} | articles: ${articles.length} | blocks: ${blocks.length} | components: ${components.length}`);
