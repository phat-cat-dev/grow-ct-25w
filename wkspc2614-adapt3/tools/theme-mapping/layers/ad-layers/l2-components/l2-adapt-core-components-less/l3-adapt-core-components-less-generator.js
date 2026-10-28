#!/usr/bin/env node
/**
 * l3-adapt-core-components-less-generator.js — compile each L1 component's own
 * less (src/components/<dir>/less/**\/*.less) standalone, mapped onto that
 * component's own class vocabulary (not the L1 spine - L2/L4 already cover
 * that; this is the first layer to touch per-component classes at all).
 *
 * This is the real Stage 2a of grunt's LESS compile (grunt/tasks/less.js:
 * 68-82), theme-independent and filtered by installedFilter to only the
 * components actually present in src/components - compiled here, like L4
 * found for vanilla, with core's less in the bundle too, because component
 * less calls core mixins (.transform, .transition, .visually-hidden(),
 * .u-display-none, .u-float-left/right, .icon-*) that only exist in
 * src/core/less. Confirmed empirically by grep - every component less file
 * calling a bare mixin statement (e.g. `.icon-tick;`) depends on
 * src/core/less/_defaults/icons.less being in scope. See _index.md.
 *
 * Matching target is NOT the L1 structural spine (component__container,
 * .component etc - L2/L4's job) but each component's OWN class vocabulary,
 * as L1 already derived it:
 *   - classes.literal / classes.conditional / classes.partial (JSX-level,
 *     from tools/theme-mapping/layers/l1-adapt-templates)
 *   - derivedHeaderFamily (generic header-family pattern, component-specific
 *     strings)
 *   - the bare BEM-root token itself - NOT a JSX-template class, but a
 *     VIEW-level one: componentView.js's className() puts
 *     `this.model.get('_component').toLowerCase()` directly on the outer
 *     `.component` element (src/core/js/views/componentView.js:19, already
 *     modelled in L1's `views['componentView.js']` section) - cited from
 *     there, not re-derived, so a component's own `.<bemRoot> { ... }`
 *     wrapper rule is correctly resolved as a real hook, not dead CSS.
 *
 * Reads (never writes):
 *   src/core/less/**\/*.less                — compile CONTEXT only; never
 *                                              scanned/attributed here.
 *   src/components/<dir>/less/**\/*.less     — compiled + scanned/attributed,
 *                                              for the 30 of 32 L1 components
 *                                              that have one (confirmed by
 *                                              existsSync - assessmentResults
 *                                              and text do not).
 *   src/core/schema/config.schema.json       — screenSize defaults (same as L2/L4)
 *   tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.json
 *   tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.less (line numbers)
 *
 * Writes:
 *   tools/theme-mapping/layers/l3-adapt-core-components-less/l3-adapt-core-components-less.less
 *   tools/theme-mapping/layers/l3-adapt-core-components-less/l3-adapt-core-components-less.json
 *
 * Usage:
 *   node tools/theme-mapping/layers/l3-adapt-core-components-less/l3-adapt-core-components-less-generator.js
 *   node tools/theme-mapping/layers/l3-adapt-core-components-less/l3-adapt-core-components-less-generator.js --json-only
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..', '..', '..', '..');
const CORE_LESS_DIR = path.join(ROOT, 'src', 'core', 'less');
const COMPONENTS_DIR = path.join(ROOT, 'src', 'components');
const CONFIG_SCHEMA = path.join(ROOT, 'src', 'core', 'schema', 'config.schema.json');
const L1_DIR = path.join(ROOT, 'tools', 'theme-mapping', 'layers', 'l1-adapt-templates');
const L1_JSON_PATH = path.join(L1_DIR, 'adapt-template-classes.json');
const L1_LESS_PATH = path.join(L1_DIR, 'adapt-template-classes.less');
const OUT_DIR = __dirname;

function rel(p) { return path.relative(ROOT, p).replace(/\\/g, '/'); }

function parseArgs(argv) {
  const out = { jsonOnly: false };
  for (const a of argv) {
    if (a === '--json-only') out.jsonOnly = true;
  }
  return out;
}

// ---- 1. file order: same faithful copy of grunt/config/less.js's sortLESSFilePaths as L2/L4 ----
function alphanumericOrder(a, b) { return a > b ? 1 : a < b ? -1 : 0; }
function lengthOrder(a, b) { return a.length > b.length ? 1 : a.length < b.length ? -1 : 0; }
function compareFilePaths(a, b) {
  const aParsed = path.parse(a);
  const bParsed = path.parse(b);
  if (aParsed.dir !== bParsed.dir) return alphanumericOrder(a, b);
  const aStartsB = bParsed.name.startsWith(aParsed.name);
  const bStartsA = aParsed.name.startsWith(bParsed.name);
  if (!aStartsB && !bStartsA) return alphanumericOrder(a, b);
  return lengthOrder(aParsed.name, bParsed.name);
}
function walkLessFiles(dir) {
  let out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, entry.name);
    if (entry.isDirectory()) out = out.concat(walkLessFiles(p));
    else if (entry.name.endsWith('.less')) out.push(p);
  }
  return out;
}

// ---- 2. Stage-0 device variables (identical to L2/L4 - same framework defaults) ----
function loadScreenSizeDefaults() {
  const schema = JSON.parse(fs.readFileSync(CONFIG_SCHEMA, 'utf8'));
  const props = schema.properties.screenSize.properties;
  const out = {};
  for (const [name, def] of Object.entries(props)) out[name] = def.default;
  return out;
}
function screenSizeToLessVars(screenSize) {
  const threshold = 300;
  const baseFontSize = 16;
  let vars = '';
  for (const [name, value] of Object.entries(screenSize)) {
    const em = value > threshold ? value / baseFontSize : value;
    vars += `@adapt-device-${name}: ${em}em;\n`;
  }
  return vars;
}

// ---- 3. compile via lessc ----
function runLessc(bundleText, label) {
  const tmpFile = path.join(require('os').tmpdir(), `l3-core-components-${label}-${process.pid}-${Math.random().toString(36).slice(2)}.less`);
  fs.writeFileSync(tmpFile, bundleText);
  const r = spawnSync('npx', ['lessc', tmpFile], { encoding: 'utf8', shell: true, cwd: ROOT });
  fs.unlinkSync(tmpFile);
  return r;
}
// Whole-bundle: core (mandatory) then every component's less, in L1 dir order
// - sanity check / line-count stat only, same caveat as L2/L4 (shared bare
// selectors across components make this unusable for per-hook attribution).
// Non-fatal on failure (unlike L2/L4's whole-bundle check): this bundle
// includes every component at once, and at least one component is known to
// depend on a Stage-2b EXTENSION variable, not just core - see the
// `@ab-cq-wide` finding in _index.md. core+components alone is not always
// sufficient here, which is itself the finding this check exists to surface,
// so a failure is logged and the per-component isolation below (which can
// fail individually, per-component, without blocking the rest) is still run.
function compileWholeBundle(coreFiles, componentFiles, screenSizeVars) {
  let bundle = screenSizeVars + '\n';
  for (const f of coreFiles) bundle += `\n/* ===== ${rel(f)} ===== */\n` + fs.readFileSync(f, 'utf8');
  for (const f of componentFiles) bundle += `\n/* ===== ${rel(f)} ===== */\n` + fs.readFileSync(f, 'utf8');
  const r = runLessc(bundle, 'whole');
  if (r.status !== 0) {
    console.error('WARNING: lessc failed to compile core+components together as one bundle (sanity-check stat skipped, not fatal):');
    console.error(r.stderr || r.stdout);
    return null;
  }
  return r.stdout;
}
// Per-COMPONENT isolated compile (not per-file, unlike L2/L4 - a component's
// own less files see each other, since matching here is per-component, not
// per-file): screenSize vars + ALL core/less files (mixin context only,
// never scanned) + every OTHER component's less files + a unique marker +
// exactly this one component's own file(s). Only CSS after the marker is
// kept, so bare selectors shared across components (e.g. two components both
// declaring a `.icon` rule) are attributed only to the component being
// isolated - same marker technique as L2/L4.
// Preflight: find components whose own less fails to compile with ONLY core
// as context (i.e. a genuine Stage-2a self-sufficiency problem, not just
// noise from being bundled with everyone else). Needed because `others` below
// puts every other component's text into context for every isolated compile
// - without this preflight, one broken component (see `@ab-cq-wide` finding
// in _index.md: adapt-ab-hotgraphic needs a Stage-2b extension variable) gets
// included in `others` for all 29 other components and silently kills every
// one of their compiles too, which is not a property of THEIR less, it is a
// property of the context bundle. Excluding only the genuinely-broken
// component's text from everyone else's `others` fixes the cascade while
// still failing (correctly, and only) for the broken component's own hooks.
function findBrokenStandalone(coreText, components, screenSizeVars) {
  const broken = new Set();
  for (const comp of components) {
    const ownText = comp.files.map((f) => fs.readFileSync(f, 'utf8')).join('\n');
    const bundle = screenSizeVars + '\n' + coreText + '\n' + ownText;
    const r = runLessc(bundle, 'preflight');
    if (r.status !== 0) broken.add(comp.dir);
  }
  return broken;
}

function compilePerComponent(coreContextFiles, components, screenSizeVars) {
  const perComponentCompiled = new Map();
  const marker = '/* L3-ISOLATE-MARKER */';
  const coreText = coreContextFiles.map((f) => fs.readFileSync(f, 'utf8')).join('\n');
  const broken = findBrokenStandalone(coreText, components, screenSizeVars);
  if (broken.size) {
    console.error(`WARNING: ${broken.size} component(s) do not compile with core alone (genuine cross-stage dependency, see _index.md): ${[...broken].join(', ')}`);
    console.error('  Excluded from every OTHER component\'s isolation context so this does not cascade; each still fails only its own isolated compile below.');
  }
  for (const comp of components) {
    const others = components.filter((c) => c.dir !== comp.dir && !broken.has(c.dir));
    const othersText = others.map((c) => c.files.map((f) => fs.readFileSync(f, 'utf8')).join('\n')).join('\n');
    const ownText = comp.files.map((f) => fs.readFileSync(f, 'utf8')).join('\n');
    const bundle = screenSizeVars + '\n' + coreText + '\n' + othersText + '\n' + marker + '\n' + ownText;
    const r = runLessc(bundle, 'component');
    if (r.status !== 0) {
      console.error(`WARNING: isolated compile failed for ${comp.dir} - hooks from this component will show no compiled body.`);
      console.error(r.stderr || r.stdout);
      perComponentCompiled.set(comp.dir, new Map());
      continue;
    }
    const markerIdx = r.stdout.indexOf(marker);
    const ownCss = markerIdx >= 0 ? r.stdout.slice(markerIdx + marker.length) : r.stdout;
    const rules = splitCssRules(ownCss);
    const map = new Map();
    for (const rule of rules) {
      if (!map.has(rule.selector)) map.set(rule.selector, rule.body);
      else map.set(rule.selector, map.get(rule.selector) + '; ' + rule.body);
    }
    perComponentCompiled.set(comp.dir, map);
  }
  return perComponentCompiled;
}

// ---- 4. split compiled CSS into top-level rule blocks (identical to L2/L4) ----
function splitCssRules(css) {
  const rules = [];
  let depth = 0;
  let buf = '';
  for (let i = 0; i < css.length; i++) {
    const ch = css[i];
    if (ch === '{') {
      if (depth === 0) rules.push({ selector: buf.trim(), bodyStart: i + 1 });
      depth++;
      buf = '';
      continue;
    }
    if (ch === '}') {
      depth--;
      if (depth === 0 && rules.length && rules[rules.length - 1].body === undefined) {
        rules[rules.length - 1].body = css.slice(rules[rules.length - 1].bodyStart, i).trim();
      }
      buf = '';
      continue;
    }
    if (depth === 0) buf += ch;
  }
  return rules.filter((r) => r.selector && !r.selector.startsWith('@') && r.body !== undefined);
}

// ---- 5. resolve every selector a component's own files declare (identical algorithm to L2/L4) ----
function stripComments(text) {
  return text.replace(/\/\*[\s\S]*?\*\//g, '').replace(/\/\/.*$/gm, '');
}
function splitTopLevelCommas(text) {
  const parts = [];
  let depth = 0;
  let buf = '';
  for (const ch of text) {
    if (ch === '(') depth++;
    if (ch === ')') depth--;
    if (ch === ',' && depth === 0) { parts.push(buf.trim()); buf = ''; continue; }
    buf += ch;
  }
  if (buf.trim()) parts.push(buf.trim());
  return parts;
}
function scanDeclaredSelectors(text, file) {
  const clean = stripComments(text);
  const found = [];
  const stack = [];
  let depth = 0;
  let buf = '';
  let line = 1;
  let bufLine = 1;
  for (let i = 0; i < clean.length; i++) {
    const ch = clean[i];
    if (ch === '\n') line++;
    if (ch === '{') {
      const rawParts = splitTopLevelCommas(buf.trim());
      const parentAlts = depth === 0 ? [''] : (stack[depth - 1]?.alts || ['']);
      let alts = [];
      let isTransparent = false;
      if (/^@/.test(rawParts[0] || '')) {
        alts = parentAlts;
        isTransparent = true;
      } else {
        for (const parentAlt of parentAlts) {
          for (const raw of rawParts) {
            let resolved;
            if (raw.includes('&')) resolved = raw.replace(/&/g, parentAlt);
            else resolved = parentAlt ? `${parentAlt} ${raw}` : raw;
            alts.push(resolved);
          }
        }
      }
      if (!isTransparent) {
        for (const a of alts) found.push({ selector: a, file, line: bufLine });
      }
      stack.push({ alts, isTransparent });
      depth++;
      buf = '';
      bufLine = line;
      continue;
    }
    if (ch === '}') {
      depth--;
      stack.pop();
      buf = '';
      bufLine = line;
      continue;
    }
    if (ch === ';') { buf = ''; bufLine = line; continue; }
    buf += ch;
    if (!buf.trim()) bufLine = line;
  }
  return found;
}

// ---- 6. token extraction (identical to L2/L4) ----
function classTokens(sel) {
  return (sel.match(/\.[A-Za-z0-9_-]+/g) || []).map((s) => s.slice(1));
}

// ---- 7. L1 line index for the component's own section header (adapted from
// L2/L4's spine-line-index - here indexed by component dir, since there is
// no shared spine line to point at; points at the `/* ===== <dir> ===== */`
// banner line in adapt-template-classes.less instead). ----
function buildL1ComponentLineIndex(l1LessText, components) {
  const lines = l1LessText.split('\n');
  const index = {};
  for (const c of components) {
    let found = null;
    for (let i = 0; i < lines.length; i++) {
      if (lines[i].includes(c.dir)) { found = i + 1; break; }
    }
    index[c.dir] = found;
  }
  return index;
}

// ---- 8. per-component known-class vocabulary, cited from L1 (never invented) ----
// Bucket 'jsx' = classes.literal / classes.conditional / derivedHeaderFamily
// (template-level, from the component's own .jsx).
// Bucket 'view' = componentView.js's className() elements (view-level,
// outside any template) - cited from L1's views['componentView.js'] section,
// which already models each element's kind (literal / model-field / helper /
// conditional / literal-prefix+model-field). Resolved here per-component
// where the element's value is knowable (literal, helper emits, conditional
// whenTrue, or the _component model-field - which IS knowable, it is this
// component's own bemRoot); left as an "unresolvable" wildcard prefix where
// it is genuinely dynamic (_id, _classes: free authoring text; is-<_layout>:
// enumerable prefix 'is-' only, exact value not fixed).
function buildViewLevelVocab(l1, component) {
  const el = l1.views['componentView.js'].classNameMethod.elements;
  const exact = new Set();
  let isPrefixWildcard = false;
  for (const e of el) {
    if (e.kind === 'literal') exact.add(e.value);
    else if (e.kind === 'helper' && e.emits) for (const v of e.emits) exact.add(v);
    else if (e.kind === 'conditional' && e.whenTrue) exact.add(e.whenTrue);
    else if (e.kind === 'model-field' && e.field === '_component') exact.add(component.bemRoot);
    else if (e.kind === 'literal-prefix+model-field' && e.prefix === 'is-') isPrefixWildcard = true;
    // e.field === '_id' / '_classes': free authoring text, not enumerable - left unresolved on purpose.
  }
  return { exact, isPrefixWildcard, source: l1.views['componentView.js'].source };
}

// Classify one declared selector's class tokens against a component's
// combined vocabulary. A selector matches only if EVERY class token on it
// resolves to a known source - a compound selector with one unresolved token
// can never match anything in the real DOM, same CSS semantics L2/L4 relied
// on for subset/exact matching.
function classifySelector(tokens, vocab) {
  const perToken = [];
  for (const t of tokens) {
    if (t === 'component' || t === 'component__inner' || t === 'component__widget') {
      perToken.push({ token: t, bucket: 'spine-generic (see L2/L4)' });
    } else if (vocab.view.exact.has(t)) {
      perToken.push({ token: t, bucket: `view-level (${vocab.view.source})` });
    } else if (vocab.view.isPrefixWildcard && t.startsWith('is-')) {
      perToken.push({ token: t, bucket: `view-level, is-<_layout> prefix (${vocab.view.source})` });
    } else if (vocab.jsx.exactSet.has(t)) {
      perToken.push({ token: t, bucket: 'jsx literal/conditional/header-family' });
    } else if (vocab.jsx.partialPrefixes.some((p) => t.startsWith(p))) {
      perToken.push({ token: t, bucket: 'jsx partial-prefix' });
    } else {
      perToken.push({ token: t, bucket: null });
    }
  }
  const unresolved = perToken.filter((p) => !p.bucket).map((p) => p.token);
  return { perToken, matched: unresolved.length === 0, unresolved };
}

function writeLess(data) {
  const lines = [];
  lines.push('/* =====================================================================');
  lines.push(' * l3-adapt-core-components-less.less');
  lines.push(' * Generated by tools/theme-mapping/layers/l3-adapt-core-components-less/l3-adapt-core-components-less-generator.js');
  lines.push(' * Do not hand-edit - re-run the generator.');
  lines.push(' *');
  lines.push(' * src/components/<dir>/less compiled per-component, standalone from any');
  lines.push(' * theme (Stage 2a - theme-independent, mandatory\'s core only as mixin');
  lines.push(' * context). Mapped onto each component\'s OWN class vocabulary as L1 already');
  lines.push(' * derived it - NOT the shared L1 structural spine, which is L2/L4\'s territory.');
  lines.push(' * Each section below shows, for one component: its own declared selectors,');
  lines.push(' * the real compiled body for each (isolated per component via the same');
  lines.push(' * marker technique L2/L4 use), and which known source resolves every class');
  lines.push(' * token on that selector - jsx template, view-level className(), or the');
  lines.push(' * shared L1/L2/L4 spine. A selector with an unresolved token is flagged,');
  lines.push(' * not asserted dead - see _index.md for why that distinction matters.');
  lines.push(' * ===================================================================== */');
  lines.push('');
  for (const comp of data.components) {
    const l1Line = data.l1LineIndex[comp.dir];
    const l1Ref = l1Line ? `adapt-template-classes.less:${l1Line}` : 'adapt-template-classes.less (not found)';
    lines.push(`/* ===== ${comp.dir}  (_component: ${comp.component.rendered}, bemRoot: ${comp.bemRoot})  <->  ${l1Ref} ===== */`);
    lines.push(`/* own less file(s): ${comp.files.join(', ')} */`);
    if (!comp.hooks.length) {
      lines.push('/* no selectors declared. */');
      lines.push('');
      continue;
    }
    for (const hook of comp.hooks) {
      const tokNote = hook.unresolved.length ? `  [UNRESOLVED TOKEN(S): ${hook.unresolved.join(', ')}]` : '';
      lines.push(`/* HOOK [${hook.matched ? 'matched' : 'partial'}]: ${hook.file}:${hook.line}  declares  ${hook.selector}${tokNote} */`);
      if (hook.compiled) {
        lines.push(`${hook.selector} {`);
        for (const decl of hook.compiled.split(';').map((d) => d.trim()).filter(Boolean)) lines.push(`  ${decl};`);
        lines.push('}');
      } else {
        lines.push('/*   (container only - declarations are on a descendant, see below) */');
      }
    }
    lines.push('');
  }
  lines.push('/* ===== no less directory (deferred to _index.md - see L5 (vanilla plugins) for where these ARE styled) ===== */');
  for (const dir of data.noLessDir) lines.push(`/* ${dir}: no src/components/${dir}/less directory. */`);
  lines.push('');
  fs.writeFileSync(path.join(OUT_DIR, 'l3-adapt-core-components-less.less'), lines.join('\n') + '\n');
}

function writeJson(data) {
  fs.writeFileSync(
    path.join(OUT_DIR, 'l3-adapt-core-components-less.json'),
    JSON.stringify(data, null, 2) + '\n'
  );
}

function printInventory(data) {
  console.log('\nL3 per-component less inventory:');
  console.log('component'.padEnd(30) + 'hooks'.padEnd(8) + 'matched'.padEnd(10) + 'partial'.padEnd(10) + 'files');
  for (const comp of data.components) {
    const matched = comp.hooks.filter((h) => h.matched).length;
    const partial = comp.hooks.length - matched;
    console.log(
      comp.dir.padEnd(30) +
      String(comp.hooks.length).padEnd(8) +
      String(matched).padEnd(10) +
      String(partial).padEnd(10) +
      comp.files.map((f) => path.basename(f)).join(', ')
    );
  }
  console.log(`\nComponents with no less directory: ${data.noLessDir.join(', ')}`);
  console.log(`Total component .less files compiled: ${data.fileCount} (+ ${data.coreContextFileCount} core files as mixin context, not scanned)`);
}

function main() {
  const args = parseArgs(process.argv.slice(2));

  if (!fs.existsSync(L1_JSON_PATH)) {
    console.error(`FATAL: L1 output not found at ${rel(L1_JSON_PATH)}. Run the L1 generator first.`);
    process.exit(1);
  }
  const l1 = JSON.parse(fs.readFileSync(L1_JSON_PATH, 'utf8'));
  const l1LessText = fs.readFileSync(L1_LESS_PATH, 'utf8');

  const coreFiles = walkLessFiles(CORE_LESS_DIR).sort(compareFilePaths);

  const components = [];
  const noLessDir = [];
  for (const c of l1.components) {
    const dir = path.join(COMPONENTS_DIR, c.dir, 'less');
    if (!fs.existsSync(dir)) { noLessDir.push(c.dir); continue; }
    const files = walkLessFiles(dir).sort(compareFilePaths);
    components.push({ ...c, files });
  }
  const l1LineIndex = buildL1ComponentLineIndex(l1LessText, components);

  const allComponentFiles = components.flatMap((c) => c.files);
  console.log(`Compiling ${allComponentFiles.length} component less file(s) across ${components.length} component(s), with ${coreFiles.length} core file(s) as mixin context ...`);

  const screenSize = loadScreenSizeDefaults();
  const screenSizeVars = screenSizeToLessVars(screenSize);
  const wholeCss = compileWholeBundle(coreFiles, allComponentFiles, screenSizeVars);
  if (wholeCss !== null) {
    console.log(`  lessc OK (whole bundle, core+components) - ${wholeCss.split('\n').length} line(s) of compiled CSS.`);
  } else {
    console.log('  whole-bundle sanity check failed (see WARNING above) - continuing with per-component isolation, which does not depend on this.');
  }
  console.log(`  Compiling ${components.length} component(s) in isolation for correct per-component attribution ...`);
  const perComponentCompiled = compilePerComponent(coreFiles, components, screenSizeVars);

  const componentsOut = [];
  for (const comp of components) {
    const vocab = {
      jsx: {
        exactSet: new Set([
          ...comp.classes.literal,
          ...comp.classes.conditional,
          ...comp.derivedHeaderFamily
        ]),
        partialPrefixes: comp.classes.partial
      },
      view: buildViewLevelVocab(l1, comp)
    };
    const declared = [];
    for (const f of comp.files) {
      const text = fs.readFileSync(f, 'utf8');
      for (const d of scanDeclaredSelectors(text, rel(f))) declared.push(d);
    }
    const fileMap = perComponentCompiled.get(comp.dir);
    const hooks = declared.map((d) => {
      const tokens = classTokens(d.selector);
      const cls = tokens.length ? classifySelector(tokens, vocab) : { perToken: [], matched: true, unresolved: [] };
      return {
        selector: d.selector,
        file: d.file,
        line: d.line,
        tokens: cls.perToken,
        matched: cls.matched,
        unresolved: cls.unresolved,
        compiled: (fileMap && fileMap.get(d.selector)) || null
      };
    });
    componentsOut.push({
      dir: comp.dir,
      component: comp.component,
      bemRoot: comp.bemRoot,
      files: comp.files.map(rel),
      repeatsStandardHooksOnly: comp.repeatsStandardHooksOnly,
      hooks
    });
  }

  const data = {
    generatedBy: 'tools/theme-mapping/layers/l3-adapt-core-components-less/l3-adapt-core-components-less-generator.js',
    l1Source: rel(L1_JSON_PATH),
    screenSizeDefaults: screenSize,
    fileCount: allComponentFiles.length,
    coreContextFileCount: coreFiles.length,
    l1LineIndex,
    components: componentsOut,
    noLessDir
  };

  if (!args.jsonOnly) writeLess(data);
  writeJson(data);
  printInventory(data);
  console.log(`\nWritten: ${rel(path.join(OUT_DIR, 'l3-adapt-core-components-less.json'))}`);
  if (!args.jsonOnly) console.log(`Written: ${rel(path.join(OUT_DIR, 'l3-adapt-core-components-less.less'))}`);
}

main();
