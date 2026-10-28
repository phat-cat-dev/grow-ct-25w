'use strict';
/**
 * ab-map-structure.js
 *
 * Reads the Adapt holder skeleton (course/nav/page/article/block/component)
 * from the real .hbs templates in src/core/templates/, then reads every
 * component's own root template under src/components/* /templates/*.jsx to
 * discover that component's BEM root and the classes it actually renders.
 *
 * Verified fact this module leans on: every component root template opens
 * its outer element with the literal pair `component__inner <root>__inner`
 * (confirmed across native, extension and "ours" (adapt-ab- / adapt-abbott-)
 * plugins, including multi-template components like narrative, where only
 * the ROOT template carries this marker). The BEM root is extracted from
 * that pair rather than assumed from the directory name, so a plugin whose
 * root token diverges from its package name is still reported correctly.
 *
 * Reads only. Never writes.
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const CORE_TEMPLATES_DIR = path.join(ROOT, 'src', 'core', 'templates');
const COMPONENTS_DIR = path.join(ROOT, 'src', 'components');

const read = (p) => fs.readFileSync(p, 'utf8');

// ---------------------------------------------------------------------------
// Holder skeleton — the uniform page/article/block/component BEM pattern,
// plus nav's own (non-uniform) chrome. Extracted from the live .hbs text,
// not hardcoded, so drift in the source templates surfaces here.
// ---------------------------------------------------------------------------

/** Every literal `class="..."` / `class='...'` in a Handlebars template. Splits
 * each attribute value on whitespace; a token containing `{{` is dynamic. */
function extractClassesFromHbs(text) {
  const literal = new Set();
  const dynamic = new Set();
  const re = /\bclass=(["'])([^"']*)\1/g;
  let m;
  while ((m = re.exec(text))) {
    for (const tok of m[2].split(/\s+/).filter(Boolean)) {
      if (tok.includes('{{')) dynamic.add(tok);
      else literal.add(tok);
    }
  }
  return { literal: [...literal], dynamic: [...dynamic] };
}

const HOLDER_FILES = {
  nav: 'nav.hbs',
  page: 'page.hbs',
  article: 'article.hbs',
  block: 'block.hbs',
  component: path.join('partials', 'component.hbs'),
};

function loadHolders() {
  const holders = {};
  for (const [holder, rel] of Object.entries(HOLDER_FILES)) {
    const file = path.join(CORE_TEMPLATES_DIR, rel);
    if (!fs.existsSync(file)) {
      holders[holder] = { file: rel, present: false, literal: [], dynamic: [] };
      continue;
    }
    const { literal, dynamic } = extractClassesFromHbs(read(file));
    holders[holder] = { file: rel, present: true, literal, dynamic };
  }
  // course/menu: no dedicated core .hbs was found (menu rendering is JS-view
  // driven, not template-driven, in this codebase). Report the absence
  // honestly rather than guessing at classes - the audit band's "notes".
  holders.course = {
    file: null,
    present: false,
    literal: [],
    dynamic: [],
    notes: 'No core/templates .hbs for course/menu; menu markup is JS-view driven. See cascade OBJECT - MENU section instead.',
  };
  return holders;
}

// ---------------------------------------------------------------------------
// Per-component reader — JSX templates. Three literal shapes to extract:
//   className="foo bar"                     - plain literal
//   className={classes([ 'a', cond && 'b' ])} - array helper, string literals inside
//   className={`foo-${x}`}                   - template literal, static chunks only
// This is a pragmatic text scan (matching the house idiom in
// ab-token-source.js), not a JS/JSX parser: conditionally-applied classes are
// still reported (they are real classes that CAN render), but tagged
// `conditional` so a consumer doesn't assume they always apply; template
// literal chunks touching a `${...}` boundary are tagged `partial`.
// ---------------------------------------------------------------------------
function extractClassesFromJsx(text) {
  const literal = new Set();
  const conditional = new Set();
  const partial = new Set();

  // 1) plain quoted className="..."
  const plainRe = /\bclassName=(["'])((?:(?!\1)[^\n])*)\1/g;
  let m;
  while ((m = plainRe.exec(text))) {
    for (const tok of m[2].split(/\s+/).filter(Boolean)) literal.add(tok);
  }

  // 2) className={classes([ ... ])} - scan the array body for string literals
  const classesCallRe = /\bclassName=\{\s*classes\(\[([\s\S]*?)\]\)\s*\}/g;
  while ((m = classesCallRe.exec(text))) {
    const body = m[1];
    const strRe = /'([^']*)'|"([^"]*)"/g;
    let sm;
    while ((sm = strRe.exec(body))) {
      const raw = sm[1] !== undefined ? sm[1] : sm[2];
      for (const tok of raw.split(/\s+/).filter(Boolean)) {
        if (tok.includes('${')) partial.add(tok);
        else conditional.add(tok);
      }
    }
    // template-literal strings inside the array, e.g. `align-image-${x}`
    const tplRe = /`([^`]*)`/g;
    let tm;
    while ((tm = tplRe.exec(body))) {
      for (const chunk of tm[1].split(/\$\{[^}]*\}/)) {
        for (const tok of chunk.split(/\s+/).filter(Boolean)) partial.add(tok);
      }
    }
  }

  // 3) bare className={`foo-${x}`} template literal (not wrapped in classes([]))
  const tplAttrRe = /\bclassName=\{\s*`([^`]*)`\s*\}/g;
  while ((m = tplAttrRe.exec(text))) {
    for (const chunk of m[1].split(/\$\{[^}]*\}/)) {
      for (const tok of chunk.split(/\s+/).filter(Boolean)) partial.add(tok);
    }
  }

  // Literal strictly wins if the same token also showed up conditional/partial.
  for (const tok of literal) { conditional.delete(tok); partial.delete(tok); }

  return { literal: [...literal], conditional: [...conditional], partial: [...partial] };
}

/** `component__inner <root>__inner` - the root template's self-declared BEM
 * root. Returns null (not a guess) if the marker is absent. */
function extractBemRoot(text) {
  const m = text.match(/component__inner[\s'"]+([a-zA-Z0-9-]+)__inner/);
  return m ? m[1] : null;
}

/** The directory is the plugin/package name (e.g. adapt-contrib-accordion);
 * its root template is whichever templates/*.jsx file carries the BEM-root
 * marker. Sibling .jsx files in the same templates/ dir are sub-templates
 * (e.g. narrativeControls.jsx) consumed by the root, not independent roots. */
function loadComponents() {
  const dirs = fs.readdirSync(COMPONENTS_DIR, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name)
    .sort();

  const components = [];
  for (const dir of dirs) {
    const templatesDir = path.join(COMPONENTS_DIR, dir, 'templates');
    if (!fs.existsSync(templatesDir)) {
      components.push({ dir, root: null, rootFile: null, notes: 'no templates/ dir', classes: null, subTemplates: [] });
      continue;
    }
    const files = fs.readdirSync(templatesDir).filter((f) => f.endsWith('.jsx') || f.endsWith('.hbs'));
    let rootFile = null;
    let bemRoot = null;
    let rootClasses = null;
    const subTemplates = [];
    for (const f of files) {
      const text = read(path.join(templatesDir, f));
      const root = extractBemRoot(text);
      if (root) {
        rootFile = f;
        bemRoot = root;
        rootClasses = extractClassesFromJsx(text);
      } else {
        subTemplates.push(f);
      }
    }
    components.push({
      dir,
      root: bemRoot,
      rootFile,
      notes: bemRoot ? null : 'no component__inner <root>__inner marker found in any template file',
      classes: rootClasses,
      subTemplates,
    });
  }
  return components;
}

// ---------------------------------------------------------------------------
// Cascade section order - the real 43 headers from ab-token-structure.less
// (undlaf-intro_261012-235924/adapt-less-compiles/), 3 tier banners. Recorded
// here, not re-derived at run time, because that file lives under the
// timestamped sandbox export directory and is reference material, not a
// stable repo path to re-parse on every run. If it moves, this list is the
// one place to update (plan originally cited "46 sections"; the real,
// counted figure is 43 - reported here as the correction).
// ---------------------------------------------------------------------------
const SECTION_ORDER = [
  { tier: 'utility', name: 'VARIABLES' },
  { tier: 'utility', name: 'COLOURS' },
  { tier: 'utility', name: 'TYPOGRAPHY' },
  { tier: 'utility', name: 'LAYOUT' },
  { tier: 'utility', name: 'DISPLAY' },
  { tier: 'utility', name: 'ANIMATIONS' },
  { tier: 'utility', name: 'ICONS' },
  { tier: 'utility', name: 'A11Y' },
  { tier: 'utility', name: 'TEST' },
  { tier: 'object', name: 'DOCUMENT' },
  { tier: 'object', name: 'ELEMENT RESET' },
  { tier: 'object', name: 'NAV' },
  { tier: 'object', name: 'DRAWER' },
  { tier: 'object', name: 'SHADOW' },
  { tier: 'object', name: 'NOTIFY' },
  { tier: 'object', name: 'TOOLTIP' },
  { tier: 'object', name: 'LOADING' },
  { tier: 'object', name: 'SHARED STRUCTURE' },
  { tier: 'object', name: 'MENU' },
  { tier: 'object', name: 'PAGE' },
  { tier: 'object', name: 'ARTICLE' },
  { tier: 'object', name: 'BLOCK' },
  { tier: 'object', name: 'COMPONENT' },
  { tier: 'object', name: 'BUTTONS' },
  { tier: 'component', group: 'native', name: 'ACCORDION' },
  { tier: 'component', group: 'native', name: 'ASSESSMENTRESULTS' },
  { tier: 'component', group: 'native', name: 'CONFIDENCESLIDER' },
  { tier: 'component', group: 'native', name: 'GMCQ' },
  { tier: 'component', group: 'native', name: 'HOTGRAPHIC' },
  { tier: 'component', group: 'native', name: 'MATCHING' },
  { tier: 'component', group: 'native', name: 'MCQ' },
  { tier: 'component', group: 'native', name: 'MEDIA' },
  { tier: 'component', group: 'native', name: 'NARRATIVE' },
  { tier: 'component', group: 'native', name: 'SLIDER' },
  { tier: 'component', group: 'native', name: 'TEXTINPUT' },
  { tier: 'component', group: 'native extension', name: 'GLOSSARY' },
  { tier: 'component', group: 'native extension', name: 'LANGUAGEPICKER' },
  { tier: 'component', group: 'native extension', name: 'PAGELEVELPROGRESS' },
  { tier: 'component', group: 'native extension', name: 'RESOURCES' },
  { tier: 'component', group: 'native extension', name: 'TRICKLE' },
  { tier: 'component', group: 'native extension', name: 'TUTOR' },
  { tier: 'component', group: 'theme project layer', name: 'ASIDE/FIGURE QUOTES' },
  { tier: 'component', group: 'ours', name: 'EMPTY' },
];

function loadStructure() {
  const holders = loadHolders();
  const components = loadComponents();
  return {
    holders,
    components,
    sectionOrder: SECTION_ORDER,
    counts: {
      holdersPresent: Object.values(holders).filter((h) => h.present).length,
      componentDirs: components.length,
      componentsWithRoot: components.filter((c) => c.root).length,
      sectionOrderTotal: SECTION_ORDER.length,
    },
  };
}

module.exports = {
  CORE_TEMPLATES_DIR,
  COMPONENTS_DIR,
  extractClassesFromHbs,
  extractClassesFromJsx,
  extractBemRoot,
  loadHolders,
  loadComponents,
  SECTION_ORDER,
  loadStructure,
};

if (require.main === module) {
  const data = loadStructure();
  console.log(JSON.stringify(data.counts, null, 2));
  console.log('\nHolders:');
  for (const [name, h] of Object.entries(data.holders)) {
    console.log(`  ${name.padEnd(10)} present=${h.present}  literal=${h.literal.length}  dynamic=${h.dynamic.length}  file=${h.file}`);
  }
  console.log('\nComponents without a detected BEM root:');
  for (const c of data.components) {
    if (!c.root) console.log(`  ${c.dir}: ${c.notes}`);
  }
  console.log('\nSample component (first with a root):');
  const sample = data.components.find((c) => c.root);
  if (sample) console.log(JSON.stringify(sample, null, 2));
}
