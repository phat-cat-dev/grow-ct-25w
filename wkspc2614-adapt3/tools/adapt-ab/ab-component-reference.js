#!/usr/bin/env node
/**
 * ab-component-reference.js — a per-component learning reference (NOT a build artifact).
 *
 * For every plugin in src/components and src/extensions it emits one Markdown
 * doc describing the component: its bower metadata, its authorable properties
 * (from properties.schema), its real JSX template, a live example pulled from a
 * course's authored JSON, and notes on the files a custom component needs. Plus
 * an index. Contrib plugins fetched only at `adapt install` are documented from
 * a course example where one is present, and flagged as source-absent here.
 *
 * Usage:
 *   node tools/ab-component-reference.js [--course <content-dir>] [--out exports/component-reference]
 */
'use strict';
const fs = require('fs');
const path = require('path');
function arg(n, d) { const i = process.argv.indexOf('--' + n); return (i >= 0 && i + 1 < process.argv.length) ? process.argv[i + 1] : d; }
const courseDir = arg('course', 'courses/understanding-learning-assessment-feedback-introductory');
const outDir = arg('out', 'exports/component-reference');
const readJSON = p => { try { return JSON.parse(fs.readFileSync(p, 'utf8')); } catch { return null; } };
const read = p => { try { return fs.readFileSync(p, 'utf8'); } catch { return null; } };

// course examples, keyed by _component
const courseComponents = readJSON(path.join(courseDir, 'en', 'components.json')) || [];
const exampleFor = type => courseComponents.find(c => c._component === type);
const usedTypes = [...new Set(courseComponents.map(c => c._component))];

// scan src for plugins
function scanPlugins() {
  const found = [];
  for (const base of ['src/components', 'src/extensions']) {
    if (!fs.existsSync(base)) continue;
    for (const name of fs.readdirSync(base)) {
      const dir = path.join(base, name);
      const bower = readJSON(path.join(dir, 'bower.json'));
      if (!bower) continue;
      const kind = base.endsWith('components') ? 'component' : 'extension';
      const tdir = path.join(dir, 'templates');
      const templates = fs.existsSync(tdir) ? fs.readdirSync(tdir).filter(f => /\.(jsx|hbs)$/.test(f)) : [];
      found.push({ name, dir, kind, bower, schema: readJSON(path.join(dir, 'properties.schema')), templates: templates.map(f => ({ f, src: read(path.join(tdir, f)) })) });
    }
  }
  return found;
}

function fieldRows(schema) {
  if (!schema) return '_properties.schema not present in this checkout (contrib plugin — fetched at `adapt install`)._';
  const rows = [];
  const walk = (obj, where) => {
    if (!obj || typeof obj !== 'object') return;
    for (const [k, v] of Object.entries(obj)) {
      if (!v || typeof v !== 'object') continue;
      const type = v.type || (v.properties ? 'object' : v.items ? 'array' : '');
      const title = v.title || '';
      const def = v.default !== undefined ? JSON.stringify(v.default) : '';
      const help = (v.help || '').replace(/\|/g, '\\|');
      const en = v.enum ? ' enum: ' + v.enum.join(', ') : '';
      if (type || title || help) rows.push(`| \`${k}\` | ${type}${en} | ${v.required ? 'yes' : ''} | ${String(def).slice(0, 40).replace(/\|/g, '\\|')} | ${title} ${help} |`);
      if (v.properties) walk(v.properties, k);
      if (v.items && v.items.properties) walk(v.items.properties, k + '[]');
    }
  };
  walk(schema.globals, 'globals');
  walk(schema.properties, 'properties');
  if (!rows.length) return '_no authorable properties found in schema._';
  return '| field | type | req | default | title / help |\n|---|---|---|---|---|\n' + rows.join('\n');
}

function docFor(p) {
  const b = p.bower;
  const type = b.component || b.extension || p.name;
  const ex = exampleFor(type);
  const L = [];
  L.push(`# ${b.displayName || p.name}  (\`${type}\`)`);
  L.push(`\n- plugin: \`${p.name}\` (${p.kind})`);
  L.push(`- targetAttribute: \`${b.targetAttribute || '(n/a)'}\``);
  L.push(`- framework: \`${b.framework || ''}\``);
  L.push(`- used in this course: ${usedTypes.includes(type) ? 'yes' : 'no'}`);
  L.push(`\n## Authorable properties\n\n${fieldRows(p.schema)}`);
  L.push(`\n## JSX template(s)`);
  if (p.templates.length) for (const t of p.templates) L.push(`\n**${t.f}**\n\n\`\`\`jsx\n${t.src.trim()}\n\`\`\``);
  else L.push('\n_No template in this checkout (contrib plugin templates arrive at `adapt install`)._');
  L.push(`\n## Live example (from this course)`);
  if (ex) L.push('\n```json\n' + JSON.stringify(ex, null, 2) + '\n```');
  else L.push('\n_No instance of this component in the sampled course._');
  L.push(`\n## Files a component like this needs\n
- \`bower.json\` — name, \`component\` (the type string used in JSON), \`targetAttribute\` (the \`_config\` key), \`displayName\`, \`main\` (the JS entry).
- \`properties.schema\` — JSON Schema (draft-04) of authorable fields; drives the authoring UI and validation.
- \`js/<Name>Model.js\` + \`js/<Name>View.js\` + \`js/<name>.js\` (registers the component with Adapt).
- \`templates/<name>.jsx\` — the React template (modern Adapt renders components with JSX, not Handlebars).
- \`less/<name>.less\` — styles (compiled globally; see adapt-ab-theme for the committed-CSS pattern).`);
  return L.join('\n') + '\n';
}

fs.mkdirSync(outDir, { recursive: true });
const plugins = scanPlugins().sort((a, b) => a.name.localeCompare(b.name));
const written = [];
for (const p of plugins) { const f = `${p.name}.md`; fs.writeFileSync(path.join(outDir, f), docFor(p)); written.push(f); }
// contrib types used in course but with no src plugin here
const srcTypes = new Set(plugins.map(p => p.bower.component || p.bower.extension));
const contribOnly = usedTypes.filter(t => !srcTypes.has(t));
for (const t of contribOnly) {
  const ex = exampleFor(t);
  const L = [`# ${t}  (contrib — source not in this checkout)`,
    `\nFetched at \`adapt install\`; documented here from a course example only.`,
    `\n## Live example (from this course)\n\n\`\`\`json\n${JSON.stringify(ex, null, 2)}\n\`\`\``];
  fs.writeFileSync(path.join(outDir, `_contrib-${t}.md`), L.join('\n') + '\n'); written.push(`_contrib-${t}.md`);
}
// index
const idx = ['# Component reference\n', `_Generated ${new Date().toISOString()} from \`src/\` + \`${courseDir}\`._\n`,
  '## Custom components / extensions (source present)'];
for (const p of plugins) idx.push(`- [${p.bower.displayName || p.name}](${p.name}.md) — \`${p.bower.component || p.bower.extension}\` (${p.kind})`);
idx.push('\n## Contrib types used (source at build)');
for (const t of contribOnly) idx.push(`- [${t}](_contrib-${t}.md)`);
fs.writeFileSync(path.join(outDir, 'index.md'), idx.join('\n') + '\n'); written.push('index.md');
console.log(`Component reference: ${outDir}`);
written.forEach(f => console.log('  ' + f));
console.log(`\n${plugins.length} src plugin(s), ${contribOnly.length} contrib-only type(s).`);
