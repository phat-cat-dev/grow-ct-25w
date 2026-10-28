#!/usr/bin/env node
/**
 * l2-adapt-core-less-generator.js — compile src/core/less standalone, mapped
 * onto the L1 structural spine.
 *
 * L1 (adapt-template-classes.js) inventoried the classes Adapt's views/templates
 * EMIT. This layer answers the next question: of those classes, which ones does
 * src/core/less actually put a rule on, and what does that rule compute to?
 *
 * This is the real "mandatory" stage of grunt's LESS compile (grunt/tasks/less.js:
 * 53-66) — core/less is compiled alone here, in the same file order the real
 * build uses, with nothing from components/extensions/menu/theme mixed in. See
 * tools/theme-mapping/layers/l2-adapt-core-less/_index.md for the full compile
 * sequence this was derived from.
 *
 * Reads (never writes):
 *   grunt/config/less.js                      — only read, to cite sortLESSFilePaths;
 *                                                the sort below is a faithful copy, not a require(),
 *                                                since that file is a grunt option factory, not an export.
 *   src/core/less/**\/*.less                   — compiled via `npx lessc`
 *   src/core/schema/config.schema.json         — screenSize defaults (no course config.json is assumed)
 *   tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.json
 *   tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.less (only to resolve line numbers)
 *
 * Writes:
 *   tools/theme-mapping/layers/l2-adapt-core-less/l2-adapt-core-less.less
 *   tools/theme-mapping/layers/l2-adapt-core-less/l2-adapt-core-less.json
 *
 * Usage:
 *   node tools/theme-mapping/layers/l2-adapt-core-less/l2-adapt-core-less-generator.js
 *   node tools/theme-mapping/layers/l2-adapt-core-less/l2-adapt-core-less-generator.js --json-only
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..', '..', '..', '..');
const CORE_LESS_DIR = path.join(ROOT, 'src', 'core', 'less');
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

// ---- 1. file order: faithful copy of grunt/config/less.js's sortLESSFilePaths ----
// (grunt/config/less.js:7-18 — re-implemented here, not required, because that
// file is a grunt option factory (module.exports = function(grunt, options) {...}),
// not a plain function export.)
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

// ---- 2. Stage-0 device variables: schema defaults (grunt/tasks/less.js:19-51) ----
// No course config.json is read here — this mirrors the framework DEFAULTS
// (src/core/schema/config.schema.json:174-202: small:0 medium:720 large:960
// xlarge:1280, px, converted >300 -> em per grunt/tasks/less.js:33-42), not any
// one course's override. A course that sets its own screenSize would get
// different clamp()/@device-width-* values in L3+; that is explicitly out of
// scope for L2 (core has no course-specific behaviour).
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

// ---- 3. compile core/less standalone via lessc (same precedent as ab-theme-computed.js) ----
function runLessc(bundleText, label) {
  const tmpFile = path.join(require('os').tmpdir(), `l2-core-${label}-${process.pid}-${Math.random().toString(36).slice(2)}.less`);
  fs.writeFileSync(tmpFile, bundleText);
  const r = spawnSync('npx', ['lessc', tmpFile], { encoding: 'utf8', shell: true, cwd: ROOT });
  fs.unlinkSync(tmpFile);
  return r;
}
// Whole-bundle compile: used only as an overall "does core/less compile clean,
// standalone" sanity check and line-count stat - NOT used for per-hook bodies,
// because several core files can declare the identically-named bare selector
// (e.g. .block in both accessibility.less and block.less) and a single merged
// compile can't tell which file contributed which resulting declaration.
function compileWholeBundle(files, screenSizeVars) {
  let bundle = screenSizeVars + '\n';
  for (const f of files) bundle += `\n/* ===== ${rel(f)} ===== */\n` + fs.readFileSync(f, 'utf8');
  const r = runLessc(bundle, 'whole');
  if (r.status !== 0) {
    console.error('FATAL: lessc failed to compile src/core/less standalone.');
    console.error(r.stderr || r.stdout);
    process.exit(1);
  }
  return r.stdout;
}
// Per-file isolated compile: screenSize vars + EVERY OTHER core/less file (so
// any mixin a file needs - e.g. button.less calling .transform(), defined in
// core/transform.less, a sibling core file, not a _defaults file - resolves)
// + a unique comment marker + exactly this one file's own text. Only the CSS
// compiled AFTER the marker is kept, so a selector this file shares with
// another file (e.g. .block, declared in both accessibility.less and
// block.less) is attributed only to the file that is actually being isolated,
// never to whichever other file happens to compile to the same selector text.
function compilePerFile(allFiles, screenSizeVars) {
  const perFileCompiled = new Map(); // file (rel path) -> Map(selector -> body)
  const marker = '/* L2-ISOLATE-MARKER */';
  for (const target of allFiles) {
    const others = allFiles.filter((f) => f !== target);
    const prefixText = others.map((f) => fs.readFileSync(f, 'utf8')).join('\n');
    const bundle = screenSizeVars + '\n' + prefixText + '\n' + marker + '\n' + fs.readFileSync(target, 'utf8');
    const r = runLessc(bundle, 'file');
    if (r.status !== 0) {
      console.error(`WARNING: isolated compile failed for ${rel(target)} - hooks from this file will show no compiled body.`);
      perFileCompiled.set(rel(target), new Map());
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
    perFileCompiled.set(rel(target), map);
  }
  return perFileCompiled;
}

// ---- 4. split compiled CSS into top-level rule blocks (depth-aware, same bracket-walk style as L1) ----
function splitCssRules(css) {
  const rules = [];
  let depth = 0;
  let buf = '';
  let selStart = 0;
  for (let i = 0; i < css.length; i++) {
    const ch = css[i];
    if (ch === '{') {
      if (depth === 0) {
        rules.push({ selector: buf.trim(), bodyStart: i + 1 });
      }
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

// ---- 5. resolve every selector src/core/less/*.less itself declares (source attribution) ----
// Handles the one real pattern these files use: a top-level `.context { &__x {...} }`,
// transparent through `@media (...)` wrappers, plus top-level comma lists
// (core/global.less: `.menu, .menu-item, .page, .article, .block, .component {}`).
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
  const found = []; // { selector, file, line }
  const stack = []; // { alts: string[], isTransparent }
  let depth = 0;
  let buf = '';
  let line = 1;
  let bufLine = 1;
  for (let i = 0; i < clean.length; i++) {
    const ch = clean[i];
    if (ch === '\n') { line++; }
    if (ch === '{') {
      const rawParts = splitTopLevelCommas(buf.trim());
      const parentAlts = depth === 0 ? [''] : (stack[depth - 1]?.alts || ['']);
      let alts = [];
      let isTransparent = false;
      if (/^@/.test(rawParts[0] || '')) {
        // @media / @supports etc - pass the parent context straight through
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

// ---- 6. token-set matching between a declared/compiled selector and an L1 spine selector ----
function classTokens(sel) {
  return (sel.match(/\.[A-Za-z0-9_-]+/g) || []).map((s) => s.slice(1));
}
function tokensEqual(a, b) {
  if (a.length !== b.length) return false;
  const sb = new Set(b);
  return a.every((t) => sb.has(t));
}
// true if every token in `a` is present in `b` (a is a subset of b, or equal)
function tokensSubset(a, b) {
  if (!a.length) return false;
  const sb = new Set(b);
  return a.every((t) => sb.has(t));
}
// a core rule hooks onto a (possibly compound) L1 spine selector if either is
// a subset of the other - e.g. core's plain `.page {}` hooks onto the view's
// compound `.page.contentobject` because every element matching the latter
// also matches the former (and vice versa for single-token rungs).
function selectorsRelated(declaredTokens, rungTokens) {
  return tokensSubset(declaredTokens, rungTokens) || tokensSubset(rungTokens, declaredTokens);
}

// ---- 7. find the L1 .less line number for each spine rung (self-updating cross-reference) ----
function buildL1LineIndex(l1LessText, spine) {
  const lines = l1LessText.split('\n');
  const index = {};
  for (const rung of spine) {
    // exact rule line: "<selector> {}"  OR, for the two comment-only placeholder
    // rungs (no own {} line), the preceding comment line itself.
    let found = null;
    for (let i = 0; i < lines.length; i++) {
      const escaped = rung.selector.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      if (new RegExp(`^${escaped}\\s*\\{\\}`).test(lines[i].trim())) { found = i + 1; break; }
      if (lines[i].includes(`/* ${rung.selector}`)) { found = i + 1; }
    }
    index[rung.selector] = found;
  }
  return index;
}

function writeLess(data) {
  const lines = [];
  lines.push('/* =====================================================================');
  lines.push(' * l2-adapt-core-less.less');
  lines.push(' * Generated by tools/theme-mapping/layers/l2-adapt-core-less/l2-adapt-core-less-generator.js');
  lines.push(' * Do not hand-edit - re-run the generator.');
  lines.push(' *');
  lines.push(' * src/core/less compiled standalone (real lessc output), mapped onto the');
  lines.push(' * L1 structural spine. Every block below is commented with the exact line');
  lines.push(' * in tools/theme-mapping/layers/l1-adapt-templates/adapt-template-classes.less');
  lines.push(' * it corresponds to, so the two files can be read side by side.');
  lines.push(' * ===================================================================== */');
  lines.push('');
  lines.push('/* ---- STRUCTURAL SPINE x CORE LESS ---- */');
  for (const rung of data.spine) {
    const l1Line = data.l1LineIndex[rung.selector];
    const l1Ref = l1Line ? `adapt-template-classes.less:${l1Line}` : 'adapt-template-classes.less (not found)';
    lines.push(`/* L1 SPINE: ${rung.selector}  <->  ${l1Ref}   (L1 source: ${rung.source}) */`);
    if (!rung.coreHooks.length) {
      lines.push(`/* CORE: no rule in src/core/less for this selector. */`);
      lines.push('');
      continue;
    }
    for (const hook of rung.coreHooks) {
      const relNote = hook.relation === 'subset' ? ` (${hook.selector} is a strict subset of ${rung.selector} - every element matching the spine selector also matches this rule)` : '';
      lines.push(`/* CORE HOOK [${hook.relation}]: ${hook.file}:${hook.line}  declares  ${hook.selector}${relNote} */`);
      if (hook.compiled) {
        lines.push(`${hook.selector} {`);
        for (const decl of hook.compiled.split(';').map((d) => d.trim()).filter(Boolean)) {
          lines.push(`  ${decl};`);
        }
        lines.push('}');
      } else {
        lines.push(`/*   (container only - declarations are on a descendant, see below) */`);
      }
    }
    lines.push('');
  }

  lines.push('/* ---- PER-COMPONENT CORE RULES ---- */');
  lines.push(`/* src/core/less has no plugin/component directory - it never touches any`);
  lines.push(`   of the ${data.l1ComponentCount} components L1 inventoried. Per-component LESS is a`);
  lines.push(`   later, separate compile stage (src/components/*/less), styled for real`);
  lines.push(`   by adapt-contrib-vanilla's src/theme/adapt-contrib-vanilla/less/plugins/*`);
  lines.push(`   - see L3. */`);
  lines.push('');

  lines.push('/* ---- OTHER CORE RULES (outside the L1 spine) ---- */');
  lines.push('/* Everything src/core/less declares that has no class-token overlap with');
  lines.push('   any L1 spine selector - nav, drawer, notify, tooltip, button, loading,');
  lines.push('   shadow, transform/transitions, scrolling, accessibility utilities,');
  lines.push('   normalize.css. Listed by source file, selectors only (no bodies - see');
  lines.push('   the source file directly for these; they are not part of the L1 spine');
  lines.push('   this layer is cross-referencing). */');
  for (const f of data.otherFiles) {
    lines.push(`/* ${f.file}  (${f.selectors.length} selector(s)): ${f.selectors.slice(0, 12).join(', ')}${f.selectors.length > 12 ? ', ...' : ''} */`);
  }
  lines.push('');

  fs.writeFileSync(path.join(OUT_DIR, 'l2-adapt-core-less.less'), lines.join('\n') + '\n');
}

function writeJson(data) {
  fs.writeFileSync(
    path.join(OUT_DIR, 'l2-adapt-core-less.json'),
    JSON.stringify(data, null, 2) + '\n'
  );
}

function printInventory(data) {
  console.log('\nL2 spine x core-less inventory:');
  console.log('selector'.padEnd(32) + 'l1 line'.padEnd(12) + 'core hooks'.padEnd(12) + 'notes');
  for (const rung of data.spine) {
    const l1Line = data.l1LineIndex[rung.selector] || '-';
    console.log(
      rung.selector.padEnd(32) +
      String(l1Line).padEnd(12) +
      String(rung.coreHooks.length).padEnd(12) +
      (rung.coreHooks.length ? rung.coreHooks.map((h) => `${h.file}:${h.line}`).join('; ') : 'no core rule')
    );
  }
  console.log(`\nOther (non-spine) core files: ${data.otherFiles.length}`);
  console.log(`Total core .less files compiled: ${data.fileCount}`);
}

function main() {
  const args = parseArgs(process.argv.slice(2));

  if (!fs.existsSync(L1_JSON_PATH)) {
    console.error(`FATAL: L1 output not found at ${rel(L1_JSON_PATH)}. Run the L1 generator first.`);
    process.exit(1);
  }
  const l1 = JSON.parse(fs.readFileSync(L1_JSON_PATH, 'utf8'));
  const l1LessText = fs.readFileSync(L1_LESS_PATH, 'utf8');
  const l1LineIndex = buildL1LineIndex(l1LessText, l1.spine);

  const files = walkLessFiles(CORE_LESS_DIR).sort(compareFilePaths);
  console.log(`Compiling ${files.length} src/core/less file(s) standalone via lessc ...`);

  const screenSize = loadScreenSizeDefaults();
  const screenSizeVars = screenSizeToLessVars(screenSize);
  const wholeCss = compileWholeBundle(files, screenSizeVars);
  console.log(`  lessc OK (whole bundle) - ${wholeCss.split('\n').length} line(s) of compiled CSS.`);
  console.log(`  Compiling ${files.length} file(s) in isolation for correct per-file attribution ...`);
  const perFileCompiled = compilePerFile(files, screenSizeVars);

  // source attribution: scan every core .less file for the selectors it declares
  const declared = []; // { selector, file, line }
  for (const f of files) {
    const text = fs.readFileSync(f, 'utf8');
    for (const d of scanDeclaredSelectors(text, rel(f))) declared.push(d);
  }

  const spineOut = [];
  const matchedDeclaredIndexes = new Set();
  for (const rung of l1.spine) {
    const rungTokens = classTokens(rung.selector);
    const hooks = [];
    declared.forEach((d, idx) => {
      const dTokens = classTokens(d.selector);
      if (!dTokens.length) return;
      if (selectorsRelated(dTokens, rungTokens)) {
        matchedDeclaredIndexes.add(idx);
        const fileMap = perFileCompiled.get(d.file);
        const compiledBody = fileMap ? fileMap.get(d.selector) : null;
        hooks.push({
          selector: d.selector,
          file: d.file,
          line: d.line,
          relation: tokensEqual(dTokens, rungTokens) ? 'exact' : 'subset',
          compiled: compiledBody || null
        });
      }
    });
    spineOut.push({ selector: rung.selector, source: rung.source, coreHooks: hooks });
  }

  // everything declared that did NOT match any spine rung, grouped by file
  const otherByFile = new Map();
  declared.forEach((d, idx) => {
    if (matchedDeclaredIndexes.has(idx)) return;
    if (!classTokens(d.selector).length) return;
    if (!otherByFile.has(d.file)) otherByFile.set(d.file, new Set());
    otherByFile.get(d.file).add(d.selector);
  });
  const otherFiles = [...otherByFile.entries()].map(([file, set]) => ({ file, selectors: [...set] }));

  const data = {
    generatedBy: 'tools/theme-mapping/layers/l2-adapt-core-less/l2-adapt-core-less-generator.js',
    l1Source: rel(L1_JSON_PATH),
    screenSizeDefaults: screenSize,
    fileCount: files.length,
    l1LineIndex,
    l1ComponentCount: l1.counts.componentDirs,
    spine: spineOut,
    otherFiles
  };

  if (!args.jsonOnly) writeLess(data);
  writeJson(data);
  printInventory(data);
  console.log(`\nWritten: ${rel(path.join(OUT_DIR, 'l2-adapt-core-less.json'))}`);
  if (!args.jsonOnly) console.log(`Written: ${rel(path.join(OUT_DIR, 'l2-adapt-core-less.less'))}`);
}

main();
