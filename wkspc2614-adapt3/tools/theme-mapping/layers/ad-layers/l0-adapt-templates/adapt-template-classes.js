#!/usr/bin/env node
/**
 * adapt-template-classes.js
 *
 * Layer 1 of the theme-mapping pipeline. Produces the authoritative inventory
 * of the structural classes Adapt actually emits, from the page shell down to
 * the component plug-in hooks, with one section per component in
 * src/components. Later layers (l2 core, l3 vanilla, l4 output-uuid,
 * l5 page-tokens) consume adapt-template-classes.json.
 *
 * NOTE on scope: src/core/schema carries no structural classes - it defines
 * only the authorable `_classes` free-text field (content.schema.json:63,
 * default ""). The classes actually rendered come from three places, all
 * read below:
 *   - src/core/js/views/*.js        className() methods  - OUTER classes
 *   - src/core/templates/*.hbs      (via ab-map-structure) - INNER/BEM classes
 *   - src/components/* /templates/*.jsx (via ab-map-structure) - component hooks
 *
 * There is no `.course` DOM element. The real chain starts at html#adapt
 * (src/core/required/index.html:2) > #app > #wrapper > .page.contentobject.
 * course/menu are recorded honestly as "no core template" rather than guessed.
 *
 * Reuses tools/lib/ab-map-structure.js for .hbs/.jsx parsing rather than
 * re-implementing it - that module's own banner records two historical bugs
 * caused by this parsing logic drifting across copies.
 *
 * Reads (never writes):
 *   src/core/required/index.html
 *   src/core/js/views/{contentObjectView,pageView,menuView,articleView,
 *     blockView,componentView,questionView,menuItemView,adaptView}.js
 *   src/core/templates/*.hbs (via ab-map-structure.loadHolders)
 *   src/components/* / (bower.json, templates/*.jsx via ab-map-structure.loadComponents)
 *
 * Writes:
 *   tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.json
 *   tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.less
 *
 * Usage, from the repo root:
 *   node tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.js [--out=<dir>] [--json-only]
 */

'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..', '..', '..');
const OUT_DIR = path.join(ROOT, 'tools', 'theme-mapping', 'layers', 'l1-adapt-templates');
const CORE_VIEWS_DIR = path.join(ROOT, 'src', 'core', 'js', 'views');
const COMPONENTS_DIR = path.join(ROOT, 'src', 'components');

const mapStructure = require(path.join(ROOT, 'tools', 'lib', 'ab-map-structure'));

const read = (p) => fs.readFileSync(p, 'utf8');
const rel = (p) => path.relative(ROOT, p).split(path.sep).join('/');

function parseArgs(argv) {
  const args = { out: OUT_DIR, jsonOnly: false };
  for (const arg of argv) {
    if (arg === '--json-only') args.jsonOnly = true;
    else if (arg.startsWith('--out=')) args.out = path.resolve(arg.slice('--out='.length));
  }
  return args;
}

// ---------------------------------------------------------------------------
// The structural spine - html#adapt down to .component__widget. Each rung is
// cited to the file:line it was read from, never invented. childContainer
// edges are the static props set on each core view class, confirmed by
// direct read of each file.
// ---------------------------------------------------------------------------
function buildSpine() {
  const indexHtml = path.join(CORE_VIEWS_DIR, '..', '..', 'required', 'index.html');
  return [
    { selector: 'html#adapt', source: `${rel(indexHtml)}:2` },
    { selector: '#app', source: `${rel(indexHtml)}:16` },
    { selector: '#wrapper', source: `${rel(indexHtml)}:17` },
    { selector: '.page.contentobject', source: `${rel(path.join(CORE_VIEWS_DIR, 'pageView.js'))} (type='page', extends ContentObjectView.className())` },
    { selector: '.page__inner', source: 'src/core/templates/page.hbs:5' },
    { selector: '.article__container', source: 'src/core/templates/page.hbs:66 (childContainer, pageView.js:16)' },
    { selector: '.article', note: 'articleView extends AdaptView directly, not ContentObjectView - no contentobject literal (contrast with .page.contentobject above)', source: `${rel(path.join(CORE_VIEWS_DIR, 'articleView.js'))}:6-16` },
    { selector: '.article__inner', source: 'src/core/templates/article.hbs:4' },
    { selector: '.block__container', source: 'src/core/templates/article.hbs:47 (childContainer, articleView.js:21)' },
    { selector: '.block', source: `${rel(path.join(CORE_VIEWS_DIR, 'blockView.js'))}:6-16` },
    { selector: '.block__inner', source: 'src/core/templates/block.hbs:4' },
    { selector: '.component__container', source: 'src/core/templates/block.hbs:47 (childContainer, blockView.js:21)' },
    { selector: '.component', source: `${rel(path.join(CORE_VIEWS_DIR, 'componentView.js'))}:16-28` },
    { selector: '.component__inner.<name>__inner', note: 'NOT a core class - emitted by each component\'s own root .jsx template, not src/core', source: 'see components[].bemRoot below' },
    { selector: '.component__widget', note: 'NOT a core class - optional, present only in some component templates (e.g. mcq.jsx:36); absent in e.g. text.jsx', source: 'see components[].classes.literal below' },
  ];
}

// ---------------------------------------------------------------------------
// View className() extraction - the OUTER classes. Text-scan, not a JS
// parser (house idiom, matches ab-map-structure.js's own approach): locate
// the `return [ ... ]` array literal, split on top-level commas (none of
// the array elements in these six files contain an internal comma - directly
// verified by reading each file), classify each element.
// ---------------------------------------------------------------------------
const VIEW_FILES = [
  'contentObjectView.js',
  'pageView.js',
  'menuView.js',
  'articleView.js',
  'blockView.js',
  'componentView.js',
  'questionView.js',
  'menuItemView.js',
];

// Sourced directly from adaptView.js:409-422 - setVisibility()/setHidden()
// are helpers defined there, not in the six files above, so their emitted
// classes are recorded here with their own citation.
const KNOWN_HELPERS = {
  setVisibility: { classes: ['u-visibility-hidden'], source: 'src/core/js/views/adaptView.js:409-410' },
  setHidden: { classes: ['u-display-none'], source: 'src/core/js/views/adaptView.js:417-418' },
};

function splitTopLevel(text) {
  const parts = [];
  let depth = 0;
  let current = '';
  for (const ch of text) {
    if (ch === '(' || ch === '[' || ch === '{') depth++;
    if (ch === ')' || ch === ']' || ch === '}') depth--;
    if (ch === ',' && depth === 0) {
      parts.push(current.trim());
      current = '';
      continue;
    }
    current += ch;
  }
  if (current.trim()) parts.push(current.trim());
  return parts;
}

function classifyElement(expr) {
  let m;
  if ((m = expr.match(/^'([^']*)'$/) || expr.match(/^"([^"]*)"$/))) {
    return { kind: 'literal', value: m[1] };
  }
  if ((m = expr.match(/^this\.model\.get\('([^']+)'\)(\.toLowerCase\(\))?$/))) {
    return { kind: 'model-field', field: m[1], lowercased: !!m[2] };
  }
  if ((m = expr.match(/^this\.constructor\.(\w+)$/))) {
    return { kind: 'static-field', field: m[1] };
  }
  if ((m = expr.match(/^this\.(setVisibility|setHidden)\(\)$/))) {
    const helper = KNOWN_HELPERS[m[1]];
    return { kind: 'helper', helper: m[1], emits: helper.classes, conditional: true, source: helper.source };
  }
  if ((m = expr.match(/^'([^']*)'\s*\+\s*this\.model\.get\('([^']+)'\)$/))) {
    return { kind: 'literal-prefix+model-field', prefix: m[1], field: m[2] };
  }
  if ((m = expr.match(/^\((.+?)\s*\?\s*'([^']*)'\s*:\s*''\)$/))) {
    return { kind: 'conditional', condition: m[1], whenTrue: m[2] };
  }
  return { kind: 'unparsed', raw: expr };
}

function extractClassNameMethod(text) {
  const idx = text.indexOf('className()');
  if (idx === -1) return null;
  const returnIdx = text.indexOf('return [', idx);
  if (returnIdx === -1) return null;
  const arrayStart = text.indexOf('[', returnIdx);
  let depth = 0;
  let i = arrayStart;
  for (; i < text.length; i++) {
    if (text[i] === '[') depth++;
    if (text[i] === ']') { depth--; if (depth === 0) break; }
  }
  const body = text.slice(arrayStart + 1, i);
  const tail = text.slice(i + 1, text.indexOf('\n', i)).trim(); // e.g. .join(' ') or .filter(Boolean).join(' ')
  const elements = splitTopLevel(body).map((el) => ({ raw: el, ...classifyElement(el) }));
  return { elements, tail };
}

function loadViewClasses() {
  const views = {};
  for (const file of VIEW_FILES) {
    const full = path.join(CORE_VIEWS_DIR, file);
    if (!fs.existsSync(full)) {
      views[file] = { present: false };
      continue;
    }
    const text = read(full);
    const parsed = extractClassNameMethod(text);
    const extendsMatch = text.match(/extends\s+(\w+)/);
    const childContainerMatch = text.match(/childContainer:\s*'([^']+)'/);
    const typeMatch = text.match(/type:\s*'([^']+)'/);
    views[file] = {
      present: true,
      extendsClass: extendsMatch ? extendsMatch[1] : null,
      childContainer: childContainerMatch ? childContainerMatch[1] : null,
      type: typeMatch ? typeMatch[1] : null,
      classNameMethod: parsed,
      source: rel(full),
    };
  }
  return views;
}

// ---------------------------------------------------------------------------
// Component name resolution - directory name is NOT the _component value.
// bower.json's "component" field is what the framework registers and what
// componentView.js's className() lowercases at render time (so
// adapt-contrib-assessmentResults -> registered 'assessmentResults' ->
// rendered class 'assessmentresults').
// ---------------------------------------------------------------------------
function resolveComponentName(dir) {
  const bowerPath = path.join(COMPONENTS_DIR, dir, 'bower.json');
  if (!fs.existsSync(bowerPath)) {
    return { registered: null, rendered: null, source: null, notes: 'no bower.json found' };
  }
  const bower = JSON.parse(read(bowerPath));
  const registered = bower.component || null;
  return {
    registered,
    rendered: registered ? registered.toLowerCase() : null,
    source: rel(bowerPath),
    notes: registered && registered !== registered.toLowerCase()
      ? `directory/registered casing differs from rendered class (componentView.js:19 .toLowerCase())`
      : null,
  };
}

// The header family is a pure function of classNamePrefixes via
// prefixClasses() (src/core/js/reactHelpers.js:99-112), wired in
// src/core/templates/header.jsx and src/core/templates/partials/component.hbs.
const HEADER_SUFFIXES = [
  '__header', '__header-inner',
  '__title', '__title-inner',
  '__body', '__body-inner',
  '__instruction', '__instruction-inner',
  '__priority', '__priority-label',
];

function deriveHeaderFamily(renderedName) {
  if (!renderedName) return null;
  return HEADER_SUFFIXES.map((suffix) => `${renderedName}${suffix}`);
}

function buildComponentSections(structureComponents) {
  const sections = [];
  for (const c of structureComponents) {
    const name = resolveComponentName(c.dir);
    const headerFamily = deriveHeaderFamily(name.rendered);
    const literalClasses = c.classes ? c.classes.literal : [];
    const conditionalClasses = c.classes ? c.classes.conditional : [];
    const partialClasses = c.classes ? c.classes.partial : [];
    // A component may render its root classes via className={classes([...])}
    // rather than a plain className="..." string; ab-map-structure.js puts
    // everything inside that array into `conditional` (it cannot tell which
    // entries are unconditional vs truly conditional from text alone), so
    // "standard hooks only" and "has a widget" must be checked across all
    // three buckets, not literal alone.
    const allEmitted = [...literalClasses, ...conditionalClasses, ...partialClasses];
    const standardOnly = new Set(['component__inner', `${c.root}__inner`]);
    const nonStandard = allEmitted.filter((cls) => !standardOnly.has(cls));
    const hasWidget = allEmitted.includes('component__widget');
    const repeatsStandardHooksOnly = Boolean(c.root) && nonStandard.length === 0;

    sections.push({
      dir: c.dir,
      component: name,
      rootFile: c.rootFile,
      rootTemplateSource: c.rootFile ? rel(path.join(COMPONENTS_DIR, c.dir, 'templates', c.rootFile)) : null,
      bemRoot: c.root,
      derivedHeaderFamily: headerFamily,
      classes: {
        literal: literalClasses,
        conditional: conditionalClasses,
        partial: partialClasses,
      },
      subTemplates: c.subTemplates,
      hasComponentWidget: hasWidget,
      repeatsStandardHooksOnly,
      notes: c.notes,
    });
  }
  return sections;
}

// ---------------------------------------------------------------------------
// Output writers
// ---------------------------------------------------------------------------
function writeJson(outDir, data) {
  const file = path.join(outDir, 'adapt-template-classes.json');
  fs.writeFileSync(file, JSON.stringify(data, null, 2) + '\n');
  return file;
}

function writeLess(outDir, data) {
  const lines = [];
  lines.push('/* =====================================================================');
  lines.push(' * adapt-template-classes.less');
  lines.push(' * Generated by tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.js');
  lines.push(' * Do not hand-edit - re-run the generator.');
  lines.push(' *');
  lines.push(' * Human-scannable selector skeleton of the structural spine and every');
  lines.push(' * component in src/components. Empty rule bodies - this is a map for the');
  lines.push(' * theme author, not shipped CSS.');
  lines.push(' * ===================================================================== */');
  lines.push('');
  lines.push('/* ---- STRUCTURAL SPINE ---- */');
  for (const rung of data.spine) {
    const note = rung.note ? ` NOTE: ${rung.note}` : '';
    lines.push(`/* ${rung.selector}  <-  ${rung.source}${note} */`);
    // Only .component__inner.<name>__inner is not a concrete selector - it carries
    // a per-component placeholder resolved in each section below. Every other
    // rung, including .component__widget, is a real fixed selector and gets an
    // empty rule body like the component sections do, so the file keeps its
    // "selector skeleton" promise instead of leaving the spine comment-only.
    if (!rung.selector.includes('<')) {
      lines.push(`${rung.selector} {}`);
    }
  }
  lines.push('');
  for (const c of data.components) {
    lines.push(`/* ===== ${c.dir} ===== */`);
    lines.push(`/* _component (registered): ${c.component.registered || 'null'}  rendered: ${c.component.rendered || 'null'} */`);
    if (c.component.notes) lines.push(`/* NOTE: ${c.component.notes} */`);
    lines.push(`/* bemRoot: ${c.bemRoot || 'null (no component__inner <root>__inner marker found)'} */`);
    if (c.repeatsStandardHooksOnly) {
      lines.push('/* repeats standard hooks only - no component-specific classes beyond component__inner / <name>__inner / header family */');
    }
    if (c.derivedHeaderFamily) {
      lines.push(`.${c.derivedHeaderFamily.join(', .')} {}`);
    }
    if (c.bemRoot) {
      lines.push(`.component__inner.${c.bemRoot}__inner {}`);
    }
    if (c.hasComponentWidget) {
      lines.push('.component__widget {}');
    }
    const seen = new Set(['component__inner', `${c.bemRoot}__inner`, 'component__widget']);
    for (const cls of [...c.classes.literal, ...c.classes.conditional, ...c.classes.partial]) {
      if (seen.has(cls)) continue;
      seen.add(cls);
      lines.push(`.${cls} {}`);
    }
    lines.push('');
  }
  const text = lines.join('\n');
  const file = path.join(outDir, 'adapt-template-classes.less');
  fs.writeFileSync(file, text);
  return file;
}

function printInventory(data) {
  console.log(`Structural spine: ${data.spine.length} rungs, all sourced.\n`);
  console.log('View className() methods read:');
  for (const [file, v] of Object.entries(data.views)) {
    if (!v.present) { console.log(`  ${file.padEnd(22)} MISSING`); continue; }
    const n = v.classNameMethod ? v.classNameMethod.elements.length : 0;
    console.log(`  ${file.padEnd(22)} extends=${(v.extendsClass || '-').padEnd(18)} childContainer=${(v.childContainer || '-').padEnd(20)} classNameElements=${n}`);
  }
  console.log('');
  console.log(`Component sections: ${data.components.length} (expected 32)\n`);
  const header = `${'dir'.padEnd(34)}${'_component'.padEnd(22)}${'bemRoot'.padEnd(20)}${'literal'.padEnd(9)}${'standard-only'}`;
  console.log(header);
  console.log('-'.repeat(header.length));
  for (const c of data.components) {
    console.log(
      `${c.dir.padEnd(34)}${(c.component.rendered || '-').padEnd(22)}${(c.bemRoot || '-').padEnd(20)}${String(c.classes.literal.length).padEnd(9)}${c.repeatsStandardHooksOnly}`
    );
  }
  const standardOnlyCount = data.components.filter((c) => c.repeatsStandardHooksOnly).length;
  console.log('');
  console.log(`Totals: ${data.components.length} components, ${standardOnlyCount} repeat standard hooks only.`);
}

function main() {
  const args = parseArgs(process.argv.slice(2));

  let structure;
  try {
    structure = mapStructure.loadStructure();
  } catch (err) {
    console.error(`FATAL: could not load structure via tools/lib/ab-map-structure.js: ${err.message}`);
    process.exit(1);
  }

  const data = {
    generatedBy: 'tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.js',
    spine: buildSpine(),
    views: loadViewClasses(),
    holders: structure.holders,
    components: buildComponentSections(structure.components),
    counts: {
      spineRungs: 0,
      componentDirs: structure.components.length,
    },
  };
  data.counts.spineRungs = data.spine.length;
  data.counts.componentsWithBemRoot = data.components.filter((c) => c.bemRoot).length;
  data.counts.componentsRepeatingStandardHooksOnly = data.components.filter((c) => c.repeatsStandardHooksOnly).length;

  if (!fs.existsSync(args.out)) fs.mkdirSync(args.out, { recursive: true });

  const jsonFile = writeJson(args.out, data);
  console.log(`Written: ${rel(jsonFile)}`);

  if (!args.jsonOnly) {
    const lessFile = writeLess(args.out, data);
    console.log(`Written: ${rel(lessFile)}`);
  }

  console.log('');
  printInventory(data);
}

main();
