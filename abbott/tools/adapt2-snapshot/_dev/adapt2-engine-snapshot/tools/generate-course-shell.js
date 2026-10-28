#!/usr/bin/env node
/**
 * generate-course-shell.js
 *
 * Emits a course's structural shell — config.json plus the four en/*.json
 * files (course.json, contentObjects.json, articles.json, blocks.json,
 * components.json) — from a closed course-design manifest. Sibling to
 * tools/new-course.js, not an extension of it: new-course.js writes the
 * manifest's first two gate records; this tool never touches the manifest
 * and writes only the Adapt content-model files.
 *
 * Usage:
 *   node tools/generate-course-shell.js --manifest=<path> --out=<dir>
 *
 * --manifest is any path to a course-design_*.json file — NOT resolved via
 * tools/lib/course-resolve.js's courses/ convention, so this can be pointed
 * at a temporary manifest outside the repo (Prompt 89 ruling 1: this tool
 * must be provable without writing into courses/<slug>/).
 * --out is the output directory; config.json and en/*.json are written
 * there directly, never inferred from the manifest's slug.
 *
 * WRITE ORDER (governs _trackingId — see TID-1, docs/project/open-
 * decisions.md:2799): pages in fixed-plus-lesson-insertion order (skeletons
 * store pageSet); within a page, articles in section order; within a page,
 * blocks in the archetype's own blockSequence order (NOT grouped by
 * article — blockSequence order already yields section-grouped output
 * because roleToSection is monotonic across a lesson's blockSequence).
 * _trackingId is a single counter across the WHOLE course, dense from 0,
 * incremented once per block written (never per page, article or
 * component). course.json._latestTrackingId is the last value assigned.
 *
 * SLOT RESOLUTION (SCL-1 AMENDMENT, docs/project/open-decisions.md:2839-
 * 2914): a variable slot's component is read from the manifest ONLY where
 * design-kb.skeletons.json's own selectionModel text names a gate. Today
 * that is `signpost` -> les-02_visual-overview alone. Single-realisation slots
 * (componentOptions.length === 1) resolve without any gate, generically —
 * no slot key is hardcoded for this case. Every other variable slot gets
 * its block/article scaffolding written (so the page structure is
 * complete) but NO components.json entry — deferred to Phase B, matching
 * SC-1's own description of ordinary practice, not a failure.
 *
 * Two required:false blocks carry a named inclusion rule, each cited to
 * its own archetype's `notes` field in design-kb.skeletons.json (this is
 * resolution logic referencing a specific gate's decidedValue shape, not
 * vocabulary that belongs in a store):
 *   - c-post/reflective-bridge: included only if act-02_confidence-activities is closed and
 *     decidedValue.reflectiveBridge === 'ON'.
 *   - wrapper-close/where-next: included unless facetSet.tier === 'advanced'.
 * Any other required:false block found in the store with neither of these
 * two keys fails cleanly rather than guessing (see requireInclusionDecision).
 *
 * No vocabulary hardcoded that belongs in a store: the fixed page set, the
 * section-role mapping, and each archetype's blockSequence are all read
 * from design-kb/design-kb.skeletons.json at runtime.
 */

const fs = require('fs');
const path = require('path');
const { scaffoldBoundaryStatus } = require('./lib/phase-gate');

const ROOT = path.resolve(__dirname, '..');

function fail(message) {
  console.error(`REFUSED: ${message}`);
  process.exit(1);
}

function parseArgs() {
  const args = { manifest: null, out: null };
  process.argv.slice(2).forEach(param => {
    const eq = param.indexOf('=');
    if (eq === -1) return;
    const key = param.slice(2, eq);
    const value = param.slice(eq + 1);
    if (key === 'manifest') args.manifest = value;
    if (key === 'out') args.out = value;
  });
  if (!args.manifest) fail('--manifest=<path-to-course-design-json> is required.');
  if (!args.out) fail('--out=<output-dir> is required.');
  return args;
}

// Refusal conditions 1-3: missing / unreadable / invalid JSON.
function loadManifest(manifestPath) {
  const resolved = path.resolve(manifestPath);
  if (!fs.existsSync(resolved)) {
    fail(`manifest not found: ${resolved}`);
  }
  let raw;
  try {
    raw = fs.readFileSync(resolved, 'utf8');
  } catch (err) {
    fail(`manifest unreadable: ${resolved} (${err.message})`);
  }
  let parsed;
  try {
    parsed = JSON.parse(raw);
  } catch (err) {
    fail(`manifest is not valid JSON: ${resolved} (${err.message})`);
  }
  return parsed;
}

// Refusal condition 6 (checked early, before any read/build work).
function requireCleanOutput(outDir) {
  const configPath = path.join(outDir, 'config.json');
  const coursePath = path.join(outDir, 'en', 'course.json');
  if (fs.existsSync(configPath) || fs.existsSync(coursePath)) {
    fail(`output directory already has a shell: ${outDir} (found ${fs.existsSync(configPath) ? configPath : coursePath}). This tool does not overwrite.`);
  }
}

function loadSkeletonsStore() {
  const storePath = path.join(ROOT, 'design-kb', 'design-kb.skeletons.json');
  return JSON.parse(fs.readFileSync(storePath, 'utf8'));
}

function loadPaletteStore() {
  const storePath = path.join(ROOT, 'design-kb', 'design-kb.palette.json');
  return JSON.parse(fs.readFileSync(storePath, 'utf8'));
}

function paletteName(paletteId, paletteLookup) {
  const name = paletteLookup[paletteId];
  if (!name) fail(`palette id "${paletteId}" (named by the skeletons store) has no entry in design-kb.palette.json.`);
  return name;
}

function getLastClosedRecord(manifest, gateId) {
  const entry = (manifest.gates || []).find(g => g.gateId === gateId);
  if (!entry || !Array.isArray(entry.records) || entry.records.length === 0) return null;
  const closed = entry.records.filter(r => r.state === 'closed');
  if (closed.length === 0) return null;
  return closed[closed.length - 1]; // SC-1: last record for the gate.
}

// Refusal condition 4: a required gate record absent/not closed.
function requireGate(manifest, gateId) {
  const record = getLastClosedRecord(manifest, gateId);
  if (!record || !record.decidedValue || typeof record.decidedValue !== 'object') {
    fail(`required gate record absent or not closed: ${gateId} has no closed record with a decidedValue in this manifest.`);
  }
  return record;
}

function main() {
  const args = parseArgs();
  const manifest = loadManifest(args.manifest);
  const outDir = path.resolve(args.out);
  requireCleanOutput(outDir);

  // Gate realignment (Round F, 8 Oct 2026): facets come from manifest.facetSet;
  // slug + display name from onb-04_naming; lessons from crs-04_lesson-map.
  // The retired crs-01_course-facets / crs-03_vocabulary / gates/A3 are gone.
  const naming = requireGate(manifest, 'onb-04_naming');
  const lessonMap = requireGate(manifest, 'crs-04_lesson-map');

  const slug = manifest.slug || naming.decidedValue.slug;
  if (!slug) fail('manifest carries no slug (manifest.slug and onb-04_naming.decidedValue.slug both absent).');
  const displayName = [naming.decidedValue.pathwayName, naming.decidedValue.tierName].filter(Boolean).join(': ') || `[PLACEHOLDER TITLE: ${slug}]`;
  const tier = (manifest.facetSet && manifest.facetSet.tier) || null;
  if (!tier) fail('manifest.facetSet.tier is absent: needed to decide wrapper-close/where-next inclusion.');
  const lessons = lessonMap.decidedValue.lessons;
  if (!Array.isArray(lessons) || lessons.length === 0) {
    fail('crs-04_lesson-map.decidedValue.lessons is missing or empty: no lesson pages to build.');
  }

  // Refusal condition 5 (PHA-1): this tool is ORD-1's own /scaffold
  // point - it must refuse, not merely warn, if a gate ORD-1 places
  // before /scaffold has not yet closed or skipped, rather than
  // leaving out-of-order running to be noticed only afterwards by
  // manifest-completeness.js's clauses 1-2.
  const boundary = scaffoldBoundaryStatus(manifest, slug);
  if (!boundary.reached) {
    fail(`Phase A has not reached the point ORD-1 places before /scaffold: still open: ${boundary.missing.join(', ')}.`);
  }

  // Context coupling is decided AFTER scaffold in the realigned model (per
  // lesson in les-01_lesson-proposal, wrapper pages in wra-*, summative in
  // wra-03), so the skeleton carries no coupling markers at all: les-01, the
  // wrapper gates and CXP mark the built pages' slots later, each recorded in
  // instantiations[]. (Was les-03_context-coupling-plan, read pre-scaffold in
  // the old model; retired, gate-redesign-2026-10-06.md, 8 Oct 2026.)

  const skeletons = loadSkeletonsStore();
  const palette = loadPaletteStore();
  const paletteLookup = {};
  for (const entry of palette.entries) paletteLookup[entry.id] = entry.name;

  // CSTR-1/SVP-1 (docs/project/open-decisions.md): programme-default pass
  // mark and attempts/reshuffle settings are read from the store's own
  // assessmentDefaults, not hardcoded here.
  const assessmentDefaults = skeletons.assessmentDefaults;
  if (!assessmentDefaults || typeof assessmentDefaults.passMark !== 'number') {
    fail('design-kb.skeletons.json carries no usable assessmentDefaults.passMark.');
  }
  if (!assessmentDefaults.attempts || typeof assessmentDefaults.attempts.count !== 'number' || typeof assessmentDefaults.attempts.reshuffleOnAttempt !== 'boolean') {
    fail('design-kb.skeletons.json carries no usable assessmentDefaults.attempts (count/reshuffleOnAttempt).');
  }
  const passMark = assessmentDefaults.passMark;
  const attempts = assessmentDefaults.attempts;

  // CF-1 (docs/project/open-decisions.md): the confidence pair's structural
  // fields and three fixed shell texts are read from the store's own
  // confidenceDefaults, not hardcoded here.
  const confidenceDefaults = skeletons.confidenceDefaults;
  if (!confidenceDefaults || !Array.isArray(confidenceDefaults.scaleLabels) || confidenceDefaults.scaleLabels.length !== 5) {
    fail('design-kb.skeletons.json carries no usable confidenceDefaults.scaleLabels (five strings).');
  }
  if (typeof confidenceDefaults.preConfirmation !== 'string' || !confidenceDefaults.preConfirmation) {
    fail('design-kb.skeletons.json carries no usable confidenceDefaults.preConfirmation.');
  }
  if (!confidenceDefaults.framing || typeof confidenceDefaults.framing.cPre !== 'string' || typeof confidenceDefaults.framing.cPost !== 'string') {
    fail('design-kb.skeletons.json carries no usable confidenceDefaults.framing (cPre/cPost).');
  }

  // TOKEN-1: a fixedBody may contain {{token}} placeholders, restricted to
  // the store's own fixedTextTokens vocabulary (schema: ["passMark"] only,
  // today). Fails loudly on any token not in that vocabulary, or any token
  // this generator itself has no substitution value for — never emits an
  // unresolved {{...}} into authored output. adapt-contrib-assessment's own
  // _isPercentageBased: true (course.schema.json, article.schema.json)
  // means passMark is a percentage, hence the appended "%".
  const fixedTextTokens = skeletons.fixedTextTokens;
  if (!Array.isArray(fixedTextTokens)) {
    fail('design-kb.skeletons.json carries no usable fixedTextTokens array.');
  }
  const tokenValues = { passMark: `${passMark}%` };
  function substituteFixedText(text) {
    if (!text) return text;
    return text.replace(/\{\{\s*([a-zA-Z0-9_]+)\s*\}\}/g, (match, name) => {
      if (!fixedTextTokens.includes(name)) {
        fail(`fixedBody contains token "{{${name}}}" not present in design-kb.skeletons.json's fixedTextTokens (${fixedTextTokens.join(', ')}). Refusing rather than emitting an unresolved token.`);
      }
      if (!(name in tokenValues)) {
        fail(`fixedTextTokens names "${name}" but the generator defines no substitution value for it.`);
      }
      return tokenValues[name];
    });
  }

  // ID-1: block _id numbering is data (blockIdRule), not a hardcoded
  // literal. order is always "render-order" today — the store's own
  // blockSequence array order, which this generator already writes in;
  // no separate ordering logic to swap in for that field.
  const blockIdRule = skeletons.blockIdRule;
  if (!blockIdRule || typeof blockIdRule.step !== 'number') {
    fail('design-kb.skeletons.json carries no usable blockIdRule.step (ID-1).');
  }
  const blockIdStep = blockIdRule.step;

  const archetypeByType = {};
  for (const arch of skeletons.archetypes) archetypeByType[arch.pageType] = arch;

  // --- Build page order: fixedPages with the lesson archetype inserted
  // between lessonInsertionPoint's afterBaseKey/beforeBaseKey, per the
  // store — not a hardcoded page list. ---
  const fixedPages = skeletons.pageSet.fixedPages.slice().sort((a, b) => a.order - b.order);
  const insertion = skeletons.pageSet.lessonInsertionPoint;
  const pages = [];
  for (const fp of fixedPages) {
    pages.push({ kind: 'fixed', baseKey: fp.baseKey, archetypeKey: fp.archetype.replace('skeletons/', '') });
    if (fp.baseKey === insertion.afterBaseKey) {
      for (const lesson of lessons) {
        pages.push({ kind: 'lesson', pageKey: lesson.key, title: lesson.title, conceptTitle: lesson.conceptTitle, archetypeKey: insertion.archetype.replace('skeletons/', '') });
      }
    }
  }

  // --- Slot/inclusion resolution helpers ---
  function requireInclusionDecision(pageArchetypeKey, blockDef) {
    if (pageArchetypeKey === 'c-post' && blockDef.key === 'reflective-bridge') {
      // Confidence (old act-02) is course-level, decided post-scaffold; the
      // skeleton defaults the optional reflective bridge OFF (Round F).
      return false;
    }
    if (pageArchetypeKey === 'wrapper-close' && blockDef.key === 'where-next') {
      return tier !== 'advanced';
    }
    fail(`blockSequence entry "${blockDef.key}" (archetype ${pageArchetypeKey}) is required:false with no named inclusion rule. Refusing rather than guessing.`);
  }

  function resolveComponent(pageArchetypeKey, blockDef) {
    if (blockDef.kind === 'fixed') {
      return { componentId: blockDef.component, deferred: false };
    }
    const slot = blockDef.slot;
    if (slot.componentOptions.length === 1) {
      return { componentId: slot.componentOptions[0], deferred: false }; // single-realisation, no gate.
    }
    if (pageArchetypeKey === 'wrapper-open' && blockDef.key === 'signpost') {
      // Signpost component is a WRA decision (wra-01), post-scaffold; the
      // skeleton defaults to the text signpost and wra-01 refines it (Round F).
      return { componentId: 'palette/text', deferred: false };
    }
    if (slot.componentOptions.length === 0) {
      // Structural impossibility distinct from "no deciding record": the
      // store offers nothing to decide among (reflective-bridge today).
      fail(`slot "${blockDef.key}" (archetype ${pageArchetypeKey}) has zero componentOptions in the skeletons store and the block is included: no component can be realised. Registered and open per CONTEXT; failing cleanly rather than guessing.`);
    }
    // No gate names this slot per SCL-1 AMENDMENT: deferred to Phase B.
    return { componentId: null, deferred: true };
  }

  // --- Assemble content, in write order ---
  const contentObjects = [];
  const articles = [];
  const blocks = [];
  const components = [];
  let trackingCounter = 0;

  for (const page of pages) {
    const stem = page.kind === 'lesson' ? page.pageKey : `${slug}-${page.baseKey}`;
    const archetype = archetypeByType[page.archetypeKey];
    if (!archetype) fail(`skeletons store has no archetype for pageType "${page.archetypeKey}".`);

    const pageTitle = page.kind === 'lesson' ? page.title : archetypeTitle(page.baseKey);
    contentObjects.push({
      _id: `${stem}-co-01`,
      _parentId: 'course',
      _type: 'page',
      _classes: '',
      _htmlClasses: '',
      title: pageTitle,
      displayTitle: '',
      body: '',
      pageBody: '',
      instruction: '',
      _graphic: { src: 'course/en/images/menu-item.png', alt: '' },
      linkText: 'View',
      duration: '',
      _pageLevelProgress: {
        _isEnabled: true,
        _showPageCompletion: true,
        _excludeAssessments: false,
        _isCompletionIndicatorEnabled: false
      }
    });

    // --- Articles: 5 titled sections for lesson pages (v3, lesson-page-model-v3.md), 1 otherwise ---
    const isMultiArticle = skeletons.articleSections.multiArticlePageTypes.includes(page.archetypeKey);
    const sectionOrder = skeletons.articleSections.sectionOrder;
    const roleToSection = skeletons.articleSections.roleToSection;
    const sectionMeta = skeletons.articleSections.sectionMeta || {};
    const articleIdBySection = {};
    if (isMultiArticle) {
      sectionOrder.forEach((section, idx) => {
        const articleId = `${stem}-a-${String(idx + 1).padStart(2, '0')}`;
        articleIdBySection[section] = articleId;
        // Per-section render metadata (v3): the article title shown and its CSS
        // class come from sectionMeta. A section may carry a fixed displayTitle,
        // or titleFrom naming a per-lesson manifest field (conceptTitle) to read
        // the title from; if that field is absent the lesson title is the
        // fallback so a shell still generates.
        const meta = sectionMeta[section] || {};
        let displayTitle = meta.displayTitle || '';
        if (meta.titleFrom) displayTitle = page[meta.titleFrom] || page.title || '';
        articles.push({ _id: articleId, _parentId: `${stem}-co-01`, _type: 'article', _classes: meta.classes || '', title: displayTitle, displayTitle, body: '' });
      });
    } else {
      const articleId = `${stem}-a-01`;
      const articleObj = { _id: articleId, _parentId: `${stem}-co-01`, _type: 'article', _classes: '', body: '' };
      if (page.archetypeKey === 'summative') {
        // SUMM's single article carries the full assessment config —
        // confirmed shape, git show e2dd93f:.../en/articles.json, SUMM-a-01
        // entry. _scoreToPass/_correctToPass/_attempts/_randomisation now
        // read from assessmentDefaults (CSTR-1/SVP-1), not hardcoded.
        // _randomisation._blockCount: 0 (not >0) keeps every block in the
        // shuffle rather than trimming to a subset — confirmed via
        // adapt-assessmentArticleModel.js's _setupRandomisedAssessment():
        // `_.shuffle(blockModels)` always shuffles all blocks; the
        // `_blockCount > 0` guard only ever slices the shuffled set down,
        // never expands it — so reshuffleOnAttempt's "every question,
        // reordered" is _isEnabled: true with _blockCount left at 0.
        articleObj._assessment = {
          _isEnabled: true,
          _id: articleId,
          _suppressMarking: true,
          _scoreToPass: passMark,
          _correctToPass: passMark,
          _isPercentageBased: true,
          _includeInTotalScore: true,
          _assessmentWeight: 1,
          _isResetOnRevisit: false,
          _attempts: attempts.count,
          _allowResetIfPassed: false,
          _scrollToOnReset: false,
          _randomisation: { _isEnabled: attempts.reshuffleOnAttempt, _blockCount: 0 },
          _questions: { _resetType: 'hard', _canShowFeedback: true, _canShowMarking: true, _canShowModelAnswer: false }
        };
        articleObj._trickle = { _isEnabled: true, _onChildren: true, _button: { _isEnabled: true, startText: 'Continue' } };
      }
      articles.push(articleObj);
    }
    const singleArticleId = isMultiArticle ? null : articles[articles.length - 1]._id;

    // --- Blocks, in blockSequence (store) order; trackingId dense/global ---
    for (const blockDef of archetype.blockSequence) {
      let include = true;
      if (blockDef.required === false) {
        include = requireInclusionDecision(page.archetypeKey, blockDef);
      }
      if (!include) continue;

      // Multi-article (lesson) pages: look the block's role up in
      // articleSections.roleToSection to find which of the five articles it
      // belongs to. Single-article pages have exactly one article — every
      // block on the page belongs to it, regardless of role (roleToSection
      // does not cover single-article-page roles like "furniture" or
      // "summative", and does not need to).
      const parentArticleId = isMultiArticle
        ? articleIdBySection[roleToSection[blockDef.role]]
        : singleArticleId;
      if (!parentArticleId) fail(`role "${blockDef.role}" (block "${blockDef.key}") has no section mapping in articleSections.roleToSection.`);

      const suffix = String((blocks.filter(b => b._id.startsWith(`${stem}-b-`)).length + 1) * blockIdStep).padStart(2, '0');
      const blockId = `${stem}-b-${suffix}`;
      const trackingId = trackingCounter;
      trackingCounter += 1;

      blocks.push({
        _id: blockId,
        _parentId: parentArticleId,
        _type: 'block',
        _classes: '',
        title: blockDef.title,
        displayTitle: '',
        body: '',
        instruction: '',
        _trackingId: trackingId,
        _skeletonKey: blockDef.key
      });

      const resolved = resolveComponent(page.archetypeKey, blockDef);
      if (!resolved.deferred) {
        // Marker policy at scaffold time. Multi-option coupled slots are
        // decided post-scaffold (les-01 per lesson, the wrapper gates, CXP)
        // and never reach this branch (they are deferred, no component), so
        // their marker slot__<page>__<slotType> is written later by the land
        // step from the page's instantiations[] entry (LK-1/CPL-1;
        // gate-redesign-2026-10-06.md, 8 Oct 2026, les-03 retired).
        // A single-realisation ALWAYS-COUPLED slot, however, is created
        // directly by this generator and its coupling is fixed by the
        // archetype (no gate decides it), so its marker is written here, at
        // scaffold (MK-1 Part 2's documented "generator's own marker-writing
        // behaviour for the single-realisation slots it creates directly"):
        // the two wrapper practice-connection slots, and the lesson
        // concept-context and summary slots. A slot is always-coupled when
        // its contextCoupling names a coupled variation and never
        // shell-coupled; shell/generic slots (reflective-prompt,
        // lesson-references, course-references, signpost) get no marker. The
        // page token is the archetype key for the fixed single-instance
        // pages (slot__wrapper-open__practice-connection) and the lesson page
        // key for lesson pages (slot__L01__concept-context), matching MK-1's
        // own two conventions (Part 2 and Part 1 respectively).
        const slotCoupling = (blockDef.slot && blockDef.slot.contextCoupling) || [];
        const alwaysCoupled = slotCoupling.length > 0 && !slotCoupling.includes('shell-coupled');
        const markerPage = page.kind === 'lesson' ? page.pageKey : page.archetypeKey;
        const slotMarker = alwaysCoupled ? `slot__${markerPage}__${blockDef.slot.slotType}` : '';
        const componentObj = {
          _id: `${stem}-c-${suffix}`,
          _parentId: blockId,
          _type: 'component',
          _component: paletteName(resolved.componentId, paletteLookup),
          _classes: slotMarker,
          _layout: 'full',
          title: blockDef.title,
          displayTitle: '',
          body: substituteFixedText(blockDef.fixedBody) || '', // CV-1: fixed blocks' literal shell text, substituted per TOKEN-1 when the store carries one.
          instruction: '',
          _pageLevelProgress: { _isEnabled: true, _isCompletionIndicatorEnabled: false }
        };
        if (blockDef.key === 'results') {
          // palette/assessmentresults' own configNotes: "_assessmentId must
          // match the assessment article ID" — sourced from this run's own
          // generated SUMM article id, not invented.
          const summArticle = articles.find(a => a._assessment);
          if (summArticle) componentObj._assessmentId = summArticle._id;
        }
        if (blockDef.key === 'confidence-pre' || blockDef.key === 'confidence-post') {
          // CF-1: structural fields and fixed shell text on both confidence
          // components, read from confidenceDefaults above.
          const isPre = blockDef.key === 'confidence-pre';
          componentObj._mode = isPre ? 'pre' : 'post';
          componentObj._selfAssessmentGroupId = slug;
          componentObj._scale = { _labels: confidenceDefaults.scaleLabels };
          componentObj._preConfirmation = confidenceDefaults.preConfirmation;
          componentObj.instruction = isPre ? confidenceDefaults.framing.cPre : confidenceDefaults.framing.cPost;
        }
        components.push(componentObj);
      }
    }
  }

  function archetypeTitle(baseKey) {
    // Fixed non-lesson pages have no title source anywhere the gates this
    // tool reads (CTX/A1/A3/A4) supply — placeholder, visibly marked
    // (Task 1.6 default 2).
    return `[PLACEHOLDER TITLE: ${baseKey}]`;
  }

  const courseJson = {
    _id: 'course',
    _type: 'course',
    _globals: {
      _accessibility: {
        _isEnabled: true,
        _ariaLevels: { _menu: '1', _menuGroup: '2', _menuItem: '2', _page: '1', _article: '2', _block: '3', _component: '4', _componentItem: '5', _notify: '1' }
      },
      _components: {
        _text: { ariaRegion: '' },
        _mcq: { ariaRegion: 'Multiple choice question' },
        _textInput: { ariaRegion: 'Text input question' },
        _confidence: { ariaRegion: 'Confidence rating' },
        _timeline: { ariaRegion: 'Timeline' },
        _assessmentResults: { ariaRegion: 'Assessment results' }
      },
      _extensions: {
        _pageLevelProgress: { optionalContent: 'Optional content', pageLevelProgress: 'Page sections', _navOrder: 0, _showLabel: true, _drawerPosition: 'auto' },
        _trickle: { completionMessage: '' }
      }
    },
    _buttons: {
      _submit: { buttonText: 'Submit', ariaLabel: 'Submit' },
      _reset: { buttonText: 'Reset', ariaLabel: 'Reset' },
      _showCorrectAnswer: { buttonText: 'Show correct answer', ariaLabel: 'Show correct answer' },
      _hideCorrectAnswer: { buttonText: 'Hide correct answer', ariaLabel: 'Hide correct answer' },
      _showFeedback: { buttonText: 'Show feedback', ariaLabel: 'Show feedback' },
      _remainingAttemptsText: 'Attempts remaining',
      _remainingAttemptText: 'Attempt remaining',
      _disabledAriaLabel: 'This button is disabled at the moment'
    },
    // Course-level assessment defaults (adapt-contrib-assessment's own
    // course.schema.json: _isPercentageBased/_scoreToPass/_correctToPass
    // only — _attempts and _randomisation exist at article level alone,
    // set on the SUMM article's own _assessment block above). Confirmed
    // shape and byte-identical placement (top-level key, sibling to
    // _buttons) via every generated course's course.json in
    // archive/courses-2026-09/_generated-snapshot/. Value now read from
    // assessmentDefaults (CSTR-1) rather than hardcoded.
    _assessment: {
      _isPercentageBased: true,
      _scoreToPass: passMark,
      _correctToPass: passMark
    },
    _latestTrackingId: trackingCounter - 1,
    title: displayName,
    displayTitle: displayName,
    description: '[PLACEHOLDER: course description; no gate this tool reads supplies one]',
    body: '',
    _htmlClasses: '',
    _extensions: {
      _spoor: {
        _isEnabled: true,
        _tracking: { _shouldStoreResponses: true, _shouldStoreAttempts: true, _shouldRecordInteractions: true },
        _reporting: { _onTrackingCriteriaMet: 'completed', _onAssessmentFailure: 'incomplete', _onAssessmentPass: 'completed', _resetStatusOnLanguageChange: false },
        _advancedSettings: { _commitOnStatusChange: true, _timedCommitFrequency: 0, _commitOnAnyChange: false, _showDebugWindow: false, _suppressErrors: false, _commitOnVisibilityChangeHidden: true, _manifestIdentifier: 'adapt_manifest' }
      },
      _pageLevelProgress: { _isEnabled: true, _showPageCompletion: true, _isCompletionIndicatorEnabled: false, _isShownInNavigationBar: true },
      _trickle: { _completionAttribute: '_isComplete' }
    },
    _start: { _isEnabled: false, _startIds: [], _force: false, _isMenuDisabled: false },
    _navigation: { _isDefaultNavigationDisabled: false, _navigationAlignment: 'top', _isBottomOnTouchDevices: false },
    _requireCompletionOf: -1,
    _isSelected: false,
    _isComplete: false,
    _isInteractionComplete: false,
    linkText: 'View',
    duration: '',
    _pageLevelProgress: { _isEnabled: true, _showPageCompletion: true }
    // _passReveal / _resultsDebrief deliberately omitted: both need per-
    // question topic/lessonTitle data that does not exist until summative
    // items are authored (act-04_summative-activities and beyond) — Prompt 87's report flagged
    // this timing as undetermined; fabricating _items here would violate
    // "every value traces to an input or a landed rule".
  };

  // config.json: read from design-kb.skeletons.json's courseConfigBaseline,
  // not archive/ (DR-1, docs/project/open-decisions.md — the archive
  // directory is historical record, not a live build input). The stored
  // value is confirmed byte-identical to Adapt's own config.json across all
  // 4 archived courses (md5sum academic-writing-introductory/intermediate/
  // advanced + presenting-introductory, all 9478a23d28a4a469a6ab56523748cd13)
  // — a safe literal copy, not a per-course value.
  const configJson = skeletons.courseConfigBaseline.config;

  fs.mkdirSync(path.join(outDir, 'en'), { recursive: true });
  fs.writeFileSync(path.join(outDir, 'config.json'), JSON.stringify(configJson, null, 2) + '\n');
  fs.writeFileSync(path.join(outDir, 'en', 'course.json'), JSON.stringify(courseJson, null, 2) + '\n');
  fs.writeFileSync(path.join(outDir, 'en', 'contentObjects.json'), JSON.stringify(contentObjects, null, 2) + '\n');
  fs.writeFileSync(path.join(outDir, 'en', 'articles.json'), JSON.stringify(articles, null, 2) + '\n');
  fs.writeFileSync(path.join(outDir, 'en', 'blocks.json'), JSON.stringify(blocks, null, 2) + '\n');
  fs.writeFileSync(path.join(outDir, 'en', 'components.json'), JSON.stringify(components, null, 2) + '\n');

  console.log(`Wrote shell to ${outDir}`);
  console.log(`Pages: ${contentObjects.length}, Articles: ${articles.length}, Blocks: ${blocks.length}, Components: ${components.length}`);
  console.log(`_latestTrackingId: ${trackingCounter - 1}`);
  console.log(`Blocks with no components.json entry (deferred, not a failure): ${blocks.length - components.length}`);
}

main();
