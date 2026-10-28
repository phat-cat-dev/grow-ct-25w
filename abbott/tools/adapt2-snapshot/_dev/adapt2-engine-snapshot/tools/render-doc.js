#!/usr/bin/env node
/**
 * render-doc.js — generic user-facing document renderer.
 *
 * Turns a declarative JSON template + a data object into Markdown.
 * One renderer, many templates (tools/doc-templates/*.template.json),
 * so every user-facing document (course pack first; lesson pack,
 * wrapper notes, etc. to follow) is produced the same way: the data
 * lives in JSON, the template decides how it reads, and the Markdown
 * is generated, never hand-written.
 *
 * Usage:
 *   node tools/render-doc.js --template <t.json> --data <d.json> [--out <file.md>]
 *
 * Section kinds:
 *   fields  — labelled key/value lines from an object (arrays joined inline)
 *   list    — bulleted list from an array (strings, or objects via itemPath)
 *   table   — Markdown table from an array of objects (columns: [{header,path}])
 *   prose   — a paragraph (or paragraphs) from a string path
 *   group   — iterate an array; per item render a sub-heading + nested blocks[]
 *
 * Shared keys: heading, note (italic line under the heading), empty
 * (text shown when a value/array is absent or empty; default "absent").
 * Paths are dot-separated ("a.b.c"); interpolation uses "{a.b}".
 */
'use strict';
const fs = require('fs');

function parseArgs(argv) {
  const a = {};
  for (let i = 2; i < argv.length; i++) {
    const t = argv[i];
    if (t === '--template') a.template = argv[++i];
    else if (t === '--data') a.data = argv[++i];
    else if (t === '--out') a.out = argv[++i];
    else throw new Error(`unknown arg: ${t}`);
  }
  if (!a.template || !a.data) throw new Error('usage: render-doc.js --template <t.json> --data <d.json> [--out <file.md>]');
  return a;
}

function resolve(ctx, path) {
  if (!path) return ctx;
  let v = ctx;
  for (const seg of String(path).split('.')) {
    if (v == null) return undefined;
    v = v[seg];
  }
  return v;
}

function interpolate(str, ctx) {
  return String(str).replace(/\{([^}]+)\}/g, (_, p) => {
    const v = resolve(ctx, p.trim());
    return v == null ? '' : String(v);
  });
}

function isEmpty(v) {
  return v == null || v === '' || (Array.isArray(v) && v.length === 0);
}

// A single scalar/array value as inline text.
function scalar(v) {
  if (v == null) return '';
  if (Array.isArray(v)) return v.map(scalar).join('; ');
  if (typeof v === 'boolean') return v ? 'yes' : 'no';
  if (typeof v === 'object') {
    if ('label' in v && 'code' in v) return `${v.label} (${v.code})`;
    if ('label' in v) return String(v.label);
    if ('text' in v) return String(v.text);
    return JSON.stringify(v);
  }
  return String(v);
}

function cell(v) { return scalar(v).replace(/\|/g, '\\|').replace(/\n+/g, ' '); }

function renderFields(sec, data) {
  const src = resolve(data, sec.source) || {};
  const lines = [];
  for (const f of sec.fields) {
    const v = resolve(src, f.path);
    const text = isEmpty(v) ? (f.empty || sec.empty || 'absent') : scalar(v);
    lines.push(`- **${f.label}:** ${text}`);
  }
  return lines.join('\n');
}

function renderList(sec, data) {
  const arr = resolve(data, sec.source);
  if (isEmpty(arr)) return `_${sec.empty || 'none'}_`;
  return arr.map(it => {
    const v = sec.itemPath ? resolve(it, sec.itemPath) : it;
    return `- ${scalar(v)}`;
  }).join('\n');
}

function renderTable(sec, data) {
  const arr = resolve(data, sec.source);
  if (isEmpty(arr)) return `_${sec.empty || 'none'}_`;
  const cols = sec.columns;
  const head = `| ${cols.map(c => c.header).join(' | ')} |`;
  const rule = `| ${cols.map(() => '---').join(' | ')} |`;
  const rows = arr.map(it => `| ${cols.map(c => cell(resolve(it, c.path))).join(' | ')} |`);
  return [head, rule, ...rows].join('\n');
}

function renderProse(sec, data) {
  const v = resolve(data, sec.path);
  if (isEmpty(v)) return `_${sec.empty || 'absent'}_`;
  const body = Array.isArray(v) ? v.map(scalar).join('\n\n') : scalar(v);
  return sec.label ? `**${sec.label}.** ${body}` : body;
}

function renderBlock(block, item) {
  // blocks inside a group render relative to the current item
  switch (block.kind) {
    case 'prose': return renderProse(block, item);
    case 'list': return renderList(block, item);
    case 'table': return renderTable(block, item);
    case 'fields': return renderFields(block, item);
    default: throw new Error(`unknown block kind: ${block.kind}`);
  }
}

function renderGroup(sec, data) {
  const arr = resolve(data, sec.source);
  if (isEmpty(arr)) return `_${sec.empty || 'none'}_`;
  return arr.map(item => {
    const parts = [];
    if (sec.itemHeading) parts.push(`### ${interpolate(sec.itemHeading, item)}`);
    for (const b of sec.blocks) {
      const out = renderBlock(b, item);
      if (out) parts.push(out);
    }
    return parts.join('\n\n');
  }).join('\n\n');
}

function renderSection(sec, data) {
  const parts = [];
  if (sec.heading) parts.push(`## ${sec.heading}`);
  if (sec.note) parts.push(`_${sec.note}_`);
  let body;
  switch (sec.kind) {
    case 'fields': body = renderFields(sec, data); break;
    case 'list': body = renderList(sec, data); break;
    case 'table': body = renderTable(sec, data); break;
    case 'prose': body = renderProse(sec, data); break;
    case 'group': body = renderGroup(sec, data); break;
    default: throw new Error(`unknown section kind: ${sec.kind}`);
  }
  if (body) parts.push(body);
  return parts.join('\n\n');
}

function render(template, data) {
  const out = [];
  const title = template.titleTemplate ? interpolate(template.titleTemplate, data) : template.title;
  if (title) out.push(`# ${title}`);
  if (template.intro) out.push(interpolate(template.intro, data));
  for (const sec of template.sections) out.push(renderSection(sec, data));
  return out.join('\n\n') + '\n';
}

function main() {
  const args = parseArgs(process.argv);
  const template = JSON.parse(fs.readFileSync(args.template, 'utf8'));
  const data = JSON.parse(fs.readFileSync(args.data, 'utf8'));
  const md = render(template, data);
  if (args.out) { fs.writeFileSync(args.out, md); process.stderr.write(`wrote ${args.out}\n`); }
  else process.stdout.write(md);
}

if (require.main === module) {
  try { main(); } catch (e) { process.stderr.write(`render-doc: ${e.message}\n`); process.exit(1); }
}

module.exports = { render, resolve, interpolate };
