#!/usr/bin/env node
// build-manifest.mjs
// Regenerates components.manifest.json for the GROW / Abbott component build hub.
//
// What is DERIVED from the source files (so it cannot drift):
//   - identity         <- bower.json (plugins) / package.json (library)
//   - files            <- what actually exists on disk
//   - content.block    <- properties.schema (the fillable blank block)
//   - content.fields   <- properties.schema (per-field required/default/enum/help)
//
// What comes from components.overlay.json (hand-maintained editorial):
//   - _meta, and per-unit: kind, maturity (stage/tests/notes), install, agents,
//     and content for units that have no properties.schema (library, extension).
//
// Usage:
//   node build-manifest.mjs           # regenerate components.manifest.json
//   node build-manifest.mjs --check   # exit 1 if the file is stale (for CI/pre-commit)
//
// Do not hand-edit components.manifest.json; edit the overlay or the source files.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const OVERLAY = path.join(HERE, 'components.overlay.json');
const OUT = path.join(HERE, 'components.manifest.json');

const read = (p) => fs.readFileSync(p, 'utf8');
const readJSON = (p) => JSON.parse(read(p));
const exists = (p) => fs.existsSync(p);
const isDir = (p) => exists(p) && fs.statSync(p).isDirectory();
const lsFiles = (dir, ext) =>
  isDir(dir) ? fs.readdirSync(dir).filter((f) => !ext || f.endsWith(ext)).sort() : [];

// --- voice lint -> embedded voice contract ----------------------------------
// Reads the real voice-lint.js and lifts its rule data into the manifest, so an
// agent generating content can target the exact gate. Derived, so it can't drift.

const stripComments = (src) =>
  src.replace(/\/\*[\s\S]*?\*\//g, '').replace(/^[ \t]*\/\/.*$/gm, '');
const quotedLiterals = (block) => {
  const out = [];
  const re = /'([^']*)'|"([^"]*)"/g;
  let m;
  while ((m = re.exec(block))) out.push(m[1] !== undefined ? m[1] : m[2]);
  return out;
};

function deriveVoiceContract(meta) {
  const rel = meta.voice && meta.voice.source;
  const contract = { source: rel || null, warnings: [] };
  if (!rel) { contract.warnings.push('overlay _meta.voice.source not set'); return contract; }
  const p = path.resolve(HERE, rel);
  if (!exists(p)) {
    contract.available = false;
    const w = `voice-lint not found at ${rel}; rules not embedded`;
    contract.warnings.push(w); console.warn('! ' + w);
    return contract;
  }
  const src = stripComments(read(p));
  const num = (name) => { const m = src.match(new RegExp(`const ${name}\\s*=\\s*(\\d+)`)); return m ? Number(m[1]) : null; };
  const block = (re) => { const m = src.match(re); return m ? m[1] : null; };

  const bannedBlock = block(/const BANNED_PHRASES\s*=\s*\[([\s\S]*?)\]/);
  const banned = bannedBlock ? quotedLiterals(bannedBlock) : [];
  const spellBlock = block(/const AMERICAN_TO_BRITISH\s*=\s*\{([\s\S]*?)\}/);
  const spelling = {};
  if (spellBlock) { const re = /'([^']+)'\s*:\s*'([^']+)'/g; let m; while ((m = re.exec(spellBlock))) spelling[m[1]] = m[2]; }
  const excludedBlock = block(/const EXCLUDED_KEYS\s*=\s*new Set\(\[([\s\S]*?)\]\)/);
  const excluded = excludedBlock ? quotedLiterals(excludedBlock) : [];
  const hard = num('HARD_SENTENCE_WORD_LIMIT'), soft = num('LONG_SENTENCE_THRESHOLD'), maxc = num('MAX_CONSECUTIVE_LONG_SENTENCES');

  for (const [label, ok] of [['BANNED_PHRASES', banned.length], ['AMERICAN_TO_BRITISH', Object.keys(spelling).length], ['EXCLUDED_KEYS', excluded.length], ['sentence limits', hard && soft && maxc]]) {
    if (!ok) { const w = `could not extract ${label} from voice-lint.js (format changed?)`; contract.warnings.push(w); console.warn('! ' + w); }
  }

  contract.available = true;
  contract.run = `node ${rel} --file=<path-to-drafted-components.json>   # or --course=<slug>`;
  contract.appliesTo = 'Every authored-prose string leaf in a filled block: title, displayTitle, body, instruction, and every field tagged `voice: prose` in content.fields (passage, headings, stage labels, tool labels, scene extras...).';
  contract.notLinted = excluded;
  contract.rules = {
    britishEnglish: { detail: 'Use British spelling; each American form here is a hard fail.', americanToBritish: spelling },
    noEmDash: { detail: 'No em dash. Use a comma, parentheses or a full stop.', char: '—' },
    bannedPhrases: { detail: 'None of these substrings may appear (case-insensitive). Note second-person voice: no "the learner", "students should", "one might".', phrases: banned },
    noThereIsAreOpener: { detail: 'Do not start a sentence with "There is/are". Only allowed exception: "There is/are no right or wrong answers".' },
    sentenceLength: { detail: `No sentence over ${hard} words; no more than ${maxc} consecutive sentences of ${soft}+ words.`, hardWordLimit: hard, longThreshold: soft, maxConsecutiveLong: maxc }
  };
  contract.escapeHatch = {
    detail: 'Last resort for prose you cannot reword (e.g. a verbatim quoted source). Put these two keys on the object holding the prose; the reason is required or the lint fails.',
    keys: { _voiceLintIgnore: true, _voiceLintReason: '<<why this prose is exempt>>' }
  };
  return contract;
}

// --- properties.schema -> fillable content ---------------------------------

// One field's documentation (recurses into arrays/objects). `excluded` is the
// voice lint's structural-key set, used to tag which string fields are prose.
function fieldMeta(key, prop, excluded) {
  const m = {};
  if (prop.required === true) m.required = true;
  if (prop.default !== undefined) m.default = prop.default;
  if (prop.enum !== undefined) m.enum = prop.enum;
  const help = prop.help || prop.title;
  if (help) m.help = help;
  if (prop.type === 'string' && !prop.enum && !excluded.has(key)) m.voice = 'prose';
  if (prop.type === 'array' && prop.items && prop.items.properties) {
    m.item = mapFields(prop.items.properties, excluded);
  } else if (prop.type === 'object' && prop.properties) {
    m.properties = mapFields(prop.properties, excluded);
  }
  return m;
}
const mapFields = (props, excluded) =>
  Object.fromEntries(Object.entries(props).map(([k, v]) => [k, fieldMeta(k, v, excluded)]));

// One field's value in the blank skeleton. Object-typed fields are omitted from
// the skeleton (documented in `fields` instead); authors add them by hand.
function blockValue(prop) {
  switch (prop.type) {
    case 'string':  return prop.default ?? '';
    case 'number':  return prop.default ?? 0;
    case 'boolean': return prop.default ?? false;
    case 'array':
      return prop.items && prop.items.type === 'object' && prop.items.properties
        ? [itemSkeleton(prop.items.properties)]
        : [];
    default:        return undefined; // object -> omit from skeleton
  }
}
function itemSkeleton(props) {
  const out = {};
  for (const [k, v] of Object.entries(props)) {
    const val = blockValue(v);
    if (val !== undefined) out[k] = val;
  }
  return out;
}

function deriveContent(schemaPath, component, examplePath, seedKeys, excluded) {
  const schema = readJSON(schemaPath);
  const props = schema.properties || {};
  // Standard component scaffold (these live in Adapt's base model, not the schema).
  const block = {
    _id: `<<unique id, e.g. c-${component}-01>>`,
    _parentId: '<<_id of the block this sits in>>',
    _type: 'component',
    _component: component,
    _classes: '',
    _layout: 'full',
    title: '',
    displayTitle: '',
    body: ''
  };
  const fields = {};
  for (const [k, prop] of Object.entries(props)) {
    if (prop.editorOnly === true || k === '_supportedLayout') continue;
    const val = blockValue(prop);
    if (val !== undefined) block[k] = val;
    fields[k] = fieldMeta(k, prop, excluded);
  }
  // Optionally seed named block fields from the worked example.json, so chosen
  // defaults (e.g. a richer `instruction`) carry over without un-blanking prose.
  if (seedKeys && seedKeys.length && examplePath && exists(examplePath)) {
    const ex = readJSON(examplePath);
    if (ex && !Array.isArray(ex)) {
      for (const key of seedKeys) {
        if (Object.prototype.hasOwnProperty.call(ex, key)) block[key] = ex[key];
        else console.warn(`! seedFromExample "${key}" (${component}) not found in example.json`);
      }
    }
  }
  return { authorable: true, unit: 'component block', reference: 'example.json', block, fields };
}

// --- per-unit derivation -----------------------------------------------------

function deriveIdentity(dir) {
  if (exists(path.join(dir, 'bower.json'))) {
    const b = readJSON(path.join(dir, 'bower.json'));
    const id = { name: b.name, displayName: b.displayName, description: b.description };
    if (b.component) id.component = b.component;
    if (b.extension) id.extension = b.extension;
    if (b.targetAttribute) id.targetAttribute = b.targetAttribute;
    if (b.framework) id.framework = b.framework;
    return { identity: id, version: b.version, main: b.main };
  }
  const p = readJSON(path.join(dir, 'package.json'));
  const id = { name: p.name, displayName: p.name, description: p.description };
  if (p.type) id.type = p.type;
  return { identity: id, version: p.version, main: p.main };
}

function deriveTestCommand(dir) {
  const pkg = exists(path.join(dir, 'package.json')) ? readJSON(path.join(dir, 'package.json')) : null;
  if (pkg && pkg.scripts && pkg.scripts.test) return pkg.scripts.test;
  const tests = lsFiles(path.join(dir, 'test'), '.test.js');
  if (!tests.length) return undefined;
  const pick = tests.find((f) => /Logic\.test\.js$/.test(f)) || tests[0];
  return `node --test test/${pick}`;
}

function deriveFiles(dir, main) {
  const f = {};
  if (exists(path.join(dir, 'README.md'))) f.readme = 'README.md';
  if (exists(path.join(dir, 'bower.json'))) f.manifest = 'bower.json';
  else if (exists(path.join(dir, 'package.json'))) f.manifest = 'package.json';
  if (exists(path.join(dir, 'properties.schema'))) f.schema = 'properties.schema';
  else if (isDir(path.join(dir, 'schema'))) f.schema = lsFiles(path.join(dir, 'schema'), '.json').map((s) => `schema/${s}`);
  if (exists(path.join(dir, 'example.json'))) f.example = 'example.json';
  if (main) f.entry = main.replace(/^\//, '');
  const scripts = lsFiles(path.join(dir, 'js'), '.js');
  if (scripts.length) f.scripts = scripts.map((s) => `js/${s}`);
  if (isDir(path.join(dir, 'src'))) f.src = lsFiles(path.join(dir, 'src'), '.js').map((s) => `src/${s}`);
  const less = lsFiles(path.join(dir, 'less'), '.less');
  if (less.length) f.less = less.map((s) => `less/${s}`);
  if (isDir(path.join(dir, 'js', 'libs'))) f.vendoredLib = 'js/libs/';
  if (isDir(path.join(dir, 'demo'))) f.demo = 'demo/index.html';
  const test = deriveTestCommand(dir);
  if (test) f.test = test;
  return f;
}

function buildUnit(name, dir, ov, excluded) {
  const { identity, version, main } = deriveIdentity(dir);
  const unit = {
    kind: ov.kind,
    root: name,
    identity,
    maturity: { stage: ov.maturity.stage, version, tests: ov.maturity.tests, notes: ov.maturity.notes },
    files: deriveFiles(dir, main)
  };
  if (ov.install) unit.install = ov.install;

  // content: derive from properties.schema when present; else take the overlay's.
  const schemaPath = path.join(dir, 'properties.schema');
  const component = identity.component;
  if (exists(schemaPath) && component) {
    unit.content = deriveContent(schemaPath, component, path.join(dir, 'example.json'), ov.seedFromExample, excluded);
  } else if (ov.content) {
    unit.content = ov.content;
  }

  unit.agents = ov.agents;
  return unit;
}

// --- main --------------------------------------------------------------------

function build() {
  const overlay = readJSON(OVERLAY);
  const voice = deriveVoiceContract(overlay._meta);
  const excluded = new Set(voice.notLinted || []);
  const components = {};
  for (const [name, ov] of Object.entries(overlay.units)) {
    const dir = path.join(HERE, name);
    if (!isDir(dir)) {
      console.warn(`! overlay names "${name}" but no such folder; skipping`);
      continue;
    }
    components[name] = buildUnit(name, dir, ov, excluded);
  }
  // Warn about component folders on disk that the overlay does not cover.
  // Tooling / non-component dirs are not units and are ignored.
  const IGNORE = new Set(['hooks', 'node_modules']);
  for (const entry of fs.readdirSync(HERE, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    if (entry.name.startsWith('.') || IGNORE.has(entry.name)) continue;
    if (!overlay.units[entry.name]) {
      console.warn(`! folder "${entry.name}" has no overlay entry; not in the manifest`);
    }
  }
  return { _meta: { ...overlay._meta, voice }, components };
}

const manifest = build();
const serialized = JSON.stringify(manifest, null, 2) + '\n';

if (process.argv.includes('--check')) {
  const current = exists(OUT) ? read(OUT) : '';
  if (current !== serialized) {
    console.error('✗ components.manifest.json is stale. Run: node build-manifest.mjs');
    process.exit(1);
  }
  console.log('✓ components.manifest.json is up to date.');
} else {
  fs.writeFileSync(OUT, serialized);
  const units = Object.keys(manifest.components);
  console.log(`✓ wrote components.manifest.json (${units.length} units: ${units.join(', ')})`);
}
