#!/usr/bin/env node
/**
 * course-script-md.js — emit just the ".script.md" screenplay for a built
 * course: all prose + every activity + feedback/modal text, in reading order.
 *
 * This is the lightweight sibling of tools/course-export.js (which also emits
 * full/structural HTML, a YAML twin, the course-pack of gated decisions, the
 * edit.md round-trip source and real component templates, into a new
 * timestamped folder on every run). That full bundle is a deliberate,
 * on-request "full output" — run it yourself with `npm run course-export` or
 * `npx grunt course-script` when you want it. This script is the one that
 * runs automatically at the end of `grunt build`: one file, overwritten in
 * place, so routine builds don't pile up new exports/ folders.
 *
 * Usage:
 *   node tools/course-script-md.js --course <content-dir> [--short-slug <slug>]
 *        [--subject <ctx>] [--manifest <course-design.json>] [--out exports]
 *
 * Output: <out>/<short-slug>-<YYMMDDHHMMSS>.script.md (a new, timestamped file
 * each run — see tools/lib/content-version.js for the version record kept
 * alongside it at <out>/<short-slug>.version.json).
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { resolveManifest, shortSlugFromManifest, bumpVersion, stamp } = require('./lib/content-version');

function arg(name, def) { const i = process.argv.indexOf('--' + name); return (i >= 0 && i + 1 < process.argv.length) ? process.argv[i + 1] : def; }
const courseDir = arg('course');
let shortSlug = arg('short-slug', null);
const subject = arg('subject', null); // appended to the manifest shortSlug for a subject build
let manifestPath = arg('manifest', null);
const outRoot = arg('out', 'exports');
if (!courseDir) {
  console.error('usage: node tools/course-script-md.js --course <content-dir> [--short-slug <slug>] [--subject <ctx>] [--manifest <file>] [--out exports]');
  process.exit(2);
}
const rd = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const stripTags = s => String(s == null ? '' : s).replace(/<[^>]+>/g, '').trim();
// prose(): HTML -> readable text, preserving paragraph and list breaks.
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

// Auto-discover the base manifest when not passed, same convention as
// course-export.js, so the build task can run with just --course.
const resolved = resolveManifest(courseDir, manifestPath);
manifestPath = resolved.manifestPath;
// shortSlug: explicit --short-slug wins; else from onb-04_naming.shortSlug in the
// manifest, with --subject appended for a subject build.
if (!shortSlug) shortSlug = shortSlugFromManifest(resolved.manifest, subject);
if (!shortSlug) { console.error('No short slug: pass --short-slug, or supply --manifest whose onb-04_naming records a shortSlug.'); process.exit(2); }

// ---- tree ----
const childrenOf = (arr, pid) => arr.filter(x => x._parentId === pid);
const pages = cos.filter(o => o._type === 'page');

// ---- component content extraction (prose, activity items/options, feedback/modal) ----
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

// ---- SCRIPT (.md) — the screenplay ----
function scriptMd(version) {
  const L = [];
  L.push(`# ${stripTags(courseObj.displayTitle || courseObj.title || shortSlug)} — course script  <!-- ${shortSlug} v${version} -->`);
  L.push(`\n_Reading-order export of all authored text (prose, activities, feedback/modal). Generated ${new Date().toISOString()}. Content version ${version}._`);
  for (const page of pages) {
    L.push(`\n## ${stripTags(page.displayTitle || page.title || page._id)}  <!-- page ${page._id} -->`);
    for (const a of childrenOf(articles, page._id)) {
      if (a.displayTitle) L.push(`\n### ${stripTags(a.displayTitle)}  <!-- article ${a._id} -->`);
      for (const b of childrenOf(blocks, a._id)) {
        for (const c of childrenOf(components, b._id)) {
          const head = stripTags(c.displayTitle) || b.title || `(${c._component})`;
          L.push(`\n#### ${head}  <!-- ${c._id} ${c._component} -->`);
          const cpl = coupling(c);
          const chunks = extract(c);
          if (cpl && !chunks.length) L.push(`\n_⟦ CXP slot ${cpl.page}/${cpl.slot}${cpl.part ? '/' + cpl.part : ''} — subject-filled at merge; empty in the base ⟧_`);
          if (c.instruction) L.push(`\n_${stripTags(c.instruction)}_`);
          for (const ch of chunks) {
            if (ch.kind === 'feedback') L.push(`\n> **${ch.label}:** ${stripTags(ch.text)}`);
            else if (ch.label) L.push(`\n- **${ch.label}:** ${stripTags(ch.text)}`);
            else L.push(`\n${prose(ch.text)}`);
          }
        }
      }
    }
  }
  return L.join('\n') + '\n';
}

const fileStamp = stamp();
const fileName = `${shortSlug}-${fileStamp}.script.md`;
const version = bumpVersion(shortSlug, 'script-export', { file: fileName }, outRoot);
fs.mkdirSync(outRoot, { recursive: true });
const outFile = path.join(outRoot, fileName);
fs.writeFileSync(outFile, scriptMd(version));
console.log(`Course script: ${outFile}`);
console.log(`Content version: ${shortSlug} -> v${version}`);
console.log(`Pages: ${pages.length} | articles: ${articles.length} | blocks: ${blocks.length} | components: ${components.length}`);
