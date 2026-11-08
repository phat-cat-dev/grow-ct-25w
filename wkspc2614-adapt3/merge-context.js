/**
 * merge-context.js
 *
 * P2 — context-overlay merge tool (open-decisions.md #29, DM-1c).
 *
 * This is a SUBSTITUTION tool, not a generator. It moves already-
 * authored prose (stored in content/context-packs/*.json as
 * generatedProse/generatedHtml) into a copy of the shell course. It
 * does not synthesise new text from the structured `data` fields —
 * that's a separate, deliberately deferred question (does prose
 * GENERATED from structured fields reliably hit the Voice
 * Specification? Still untested — see CP-1's deferred list,
 * open-decisions.md #28).
 *
 * Usage:
 *   node merge-context.js --context=criminology --tier=academic-writing-introductory
 *   node merge-context.js --context=baseline --tier=academic-writing-introductory
 *
 * Stage 1 (always runs): copy this course's own folder
 * (courses/<tier>/) into courses/_generated/<tier>-<context>/.
 *
 * Stage 2 (LK-1/CPL-1, Prompt 154): read the course's coupling plan from
 * its instantiations[] (via requireCouplingPlan()), load each planned page's pack file from
 * content/context-packs/<subject>/<base-course-slug>/<page>.json, and
 * substitute matching slot__<page>__<slotType>-marked components' body
 * content.
 *
 * Stage 3: global token substitution — replaces {{character.name}}
 * and {{character.possessive}} from the pack-level context.json
 * across ALL string fields in the merged course JSON. Fails with
 * hard error if any tokens remain unresolved.
 */

const fs = require('fs-extra');
const path = require('path');
const { resolveCourse } = require('./tools/lib/course-resolve');

const GENERATED_ROOT = path.join(__dirname, 'courses', '_generated');
const CONTEXT_PACKS_ROOT = path.join(__dirname, 'content', 'context-packs');

// Some context packs have been distributed out of content/context-packs/
// into their owning pathway's own directory, classified by scheme (8 Nov
// 2026): a HECoS subject code (psychology), a Cardiff Met institutional
// school (school-of-sport), or the subject-neutral baseline (universal).
// Packs not listed here still read from CONTEXT_PACKS_ROOT as before. The
// pack-level context.json (e.g. content/context-packs/baseline/context.json)
// is unaffected by relocation and always stays at CONTEXT_PACKS_ROOT.
const RELOCATED_CONTEXT_PACKS = {
  psychology: 'context/hecos/psychology',
  'school-of-sport': 'context/cmet/schools/sport',
  baseline: 'context/universal'
};

function pathwayFromSlug(slug) {
  return slug.replace(/-(introductory|intermediate|advanced)$/, '');
}

// Directory holding a given context pack's files for one base course slug -
// either the relocated per-pathway location, or the legacy flat location.
function contextPackDir(context, baseCourseSlug) {
  const relocated = RELOCATED_CONTEXT_PACKS[context];
  if (relocated) {
    return path.join(__dirname, 'courses', 'v1', pathwayFromSlug(baseCourseSlug), relocated, baseCourseSlug);
  }
  return path.join(CONTEXT_PACKS_ROOT, context, baseCourseSlug);
}

// LK-1 wrapper-marker reconciliation: the shell generator writes wrapper
// component markers by archetype key (slot__wrapper-open__..., slot__wrapper-
// close__...), while instantiations[] and the pack file names key those pages
// by their fixedPages baseKey (W-OPEN, W-CLOSE) — see
// tools/manifest-completeness.js loadWrapperBaseKeys() and
// tools/generate-course-shell.js's page-stem construction. This maps the
// archetype-key page form a marker may carry to the pageKey the coupling plan
// and pack files use. Lesson pages (L01, ...) carry their pageKey directly and
// are returned unchanged by the `|| slot.page` fallback at the call site.
function loadMarkerPageToPageKey() {
  const map = new Map();
  const skeletonsPath = path.join(__dirname, 'design-kb', 'design-kb.skeletons.json');
  if (!fs.existsSync(skeletonsPath)) return map;
  const skeletons = fs.readJsonSync(skeletonsPath);
  const fixedPages = skeletons && skeletons.pageSet && Array.isArray(skeletons.pageSet.fixedPages)
    ? skeletons.pageSet.fixedPages : [];
  for (const fp of fixedPages) {
    if (fp && typeof fp.archetype === 'string' && typeof fp.baseKey === 'string') {
      map.set(fp.archetype.replace(/^skeletons\//, ''), fp.baseKey);
    }
  }
  return map;
}

const acceptedArgs = ['context', 'tier'];
const argumentValues = {
  context: null,
  tier: 'academic-writing-introductory'
};

function parseArgs() {
  const parameters = process.argv.slice(2);
  parameters.forEach(param => {
    const parts = param.replace(/^--/, '').split('=');
    if (!acceptedArgs.includes(parts[0])) {
      console.error(`Unrecognised argument: --${parts[0]}. Accepted: ${acceptedArgs.join(', ')}`);
      process.exit(1);
    }
    argumentValues[parts[0]] = parts[1];
  });

  if (!argumentValues.context) {
    console.error('Usage: node merge-context.js --context=<slug> [--tier=<slug>]');
    console.error('  --context is required (e.g. book, criminology, sports-journalism)');
    process.exit(1);
  }
}

async function extractShell(shellDir, outputDir) {
  console.log(`Extracting shell content from ${shellDir} to ${outputDir}...`);
  if (!fs.existsSync(shellDir)) {
    console.error(`No course folder found at ${shellDir}. Each course lives in its own permanently-named folder (courses/<course-slug>/). Confirm --tier matches an actual existing course folder.`);
    process.exit(1);
  }
  await fs.ensureDir(outputDir);
  await fs.copy(shellDir, outputDir, {
    filter: (src) => path.basename(src) !== 'README.md'
  });
  console.log('Extract complete.');
}

// LK-1 (Prompt 154): markers are written by tools/generate-course-shell.js
// as slot__<page>__<slotType>, where <page> is an A3 lesson key or
// wrapper-open/wrapper-close, and <slotType> is the skeletons store's own
// slotType. Old courses are not supported (Abbott, 22 September 2026): no
// fallback to the pre-LK-1 single-hyphen form this replaces.
//
// MP-1 (Prompt 159) / PKY-1 (Prompt 160): a fourth, optional group carries
// the part — slot__<page>__<slotType>__<part> — for a coupled slot that
// carries several marked components, each with its own named part. The
// part is null for the existing two-group form, which keeps working
// unchanged.
function parseSlotMarker(classesString) {
  if (!classesString) return null;
  const match = classesString.match(/(?:^|\s)slot__([A-Za-z0-9-]+)__([A-Za-z0-9-]+)(?:__([A-Za-z0-9-]+))?(?:\s|$)/);
  if (!match) return null;
  return { page: match[1], slotType: match[2], part: match[3] || null };
}

// Rebuilds the marker text a slot object was parsed from, for error
// messages.
function markerString(slot) {
  return `slot__${slot.page}__${slot.slotType}` + (slot.part ? `__${slot.part}` : '');
}

// PKY-1 (Prompt 160, docs/project/open-decisions.md): every pack lookup is
// keyed by <slotType> when the marker carries no part, <slotType>__<part>
// when it does. The existing Intro/Body/Instruction suffixes append to
// that same key.
function packKeyFor(slot) {
  return slot.part ? `${slot.slotType}__${slot.part}` : slot.slotType;
}

/**
 * Load the course's coupling plan and base course slug (LK-1/CPL-1).
 *
 * In the six-phase model the coupling plan is no longer a single
 * les-03_context-coupling-plan gate record (retired, gate-redesign-2026-10-06.md,
 * 8 Oct 2026). Each page's coupling now lives in the manifest's own
 * `instantiations[]` — one entry per built page, carrying `pageKey` and
 * `slotChoices[]`, each slot with `contextCoupling.{coupled, variationType}`.
 * les-01 (per lesson), wra-01, wra-02 and wra-03 all deposit their per-slot
 * coupling there via the land step, so instantiations is the one page-keyed
 * source this merge reads.
 *
 * Fails, naming the course, on: no course-design file found for the tier
 * (via tools/lib/course-resolve.js, the shared resolver — never a
 * templated filename); a course-design file whose own name does not match
 * course-design_<base-slug>.json (the same pattern
 * tools/manifest-completeness.js's CP-1j AMENDMENT clause already uses to
 * derive a base course slug from the file's own name, not by string-
 * guessing a suffix strip); or a manifest with no coupled slot in any
 * instantiations entry (nothing to merge). Returns { baseCourseSlug,
 * planSlotsByPage }, where planSlotsByPage maps each page to a
 * Map(slotType -> variationType) for every slot whose contextCoupling is
 * coupled (the shell-coupled slots — contextCoupling absent or coupled:false
 * — are excluded, as the old depth != "shell-coupled" filter did).
 */
function requireCouplingPlan(tier) {
  const resolved = resolveCourse(tier, ['courses']);
  if (!resolved.found) {
    console.error(`No course folder found at courses/${tier}. merge-context.js reads the course's coupling plan from its course-design instantiations[] before merging anything, for course "${tier}".`);
    process.exit(1);
  }
  if (!resolved.courseDesignPath) {
    const detail = resolved.warnings.length ? resolved.warnings.join('; ') : `no course-design_*.json file was found in ${resolved.courseDir}`;
    console.error(`No course-design file for "${tier}": ${detail}. merge-context.js cannot read the coupling plan without it.`);
    process.exit(1);
  }
  const baseSlugMatch = /^course-design_(.+)\.json$/.exec(path.basename(resolved.courseDesignPath));
  if (!baseSlugMatch) {
    console.error(`Cannot resolve a base course slug from course-design file name "${path.basename(resolved.courseDesignPath)}" for course "${tier}".`);
    process.exit(1);
  }
  const baseCourseSlug = baseSlugMatch[1];

  let manifest;
  try {
    manifest = fs.readJsonSync(resolved.courseDesignPath);
  } catch (err) {
    console.error(`course-design file unreadable or not valid JSON: ${resolved.courseDesignPath} (${err.message})`);
    process.exit(1);
  }

  // page -> Map(slotType -> variationType), coupled slots only, read from
  // instantiations[] (pageKey + slotChoices[].contextCoupling).
  const planSlotsByPage = new Map();
  for (const inst of (manifest.instantiations || [])) {
    const page = inst.pageKey;
    if (!page) continue;
    for (const sc of (inst.slotChoices || [])) {
      const cc = sc.contextCoupling;
      if (!cc || cc.coupled !== true) continue;
      let slotMap = planSlotsByPage.get(page);
      if (!slotMap) { slotMap = new Map(); planSlotsByPage.set(page, slotMap); }
      slotMap.set(sc.slotKey, cc.variationType || null);
    }
  }

  let totalCoupled = 0;
  for (const slotMap of planSlotsByPage.values()) totalCoupled += slotMap.size;
  if (totalCoupled === 0) {
    console.error(`No coupled slot in any instantiations[] entry of ${resolved.courseDesignPath}, for course "${tier}". merge-context.js cannot fill any coupling slot: nothing in this course is context-coupled (or no lesson/wrapper content has been landed yet).`);
    process.exit(1);
  }

  return { baseCourseSlug, planSlotsByPage };
}

function wrapProse(prose, slotName) {
  const paragraphs = prose.split('\n\n');
  // Worked examples contrast a weaker example ({{learner-a}}) with a stronger one
  // ({{learner-b}}). Tag those paragraphs with the we-weaker / we-stronger cue
  // classes (styled in grow-ct's grow-lesson-stages.less: red minus / green plus)
  // so the negative and positive examples are visually separated. The learner
  // tokens are still present here (substitution runs later), so key off them.
  // NB: slotType is "worked-example" (hyphen) - match it hyphen-tolerantly.
  const isWorkedExample = /worked-?example/i.test(slotName);
  return paragraphs
    .map(p => {
      if (isWorkedExample) {
        // Cue only the two example paragraphs, which LEAD with the learner token
        // ("{{learner-a}} did X..."). The "Consider two students..." intro and the
        // "Both..." summary mention a learner mid-sentence but should stay neutral.
        const lead = p.replace(/^\s+/, '');
        if (/^\{\{learner-a\b/.test(lead)) return `<p class="we-weaker">${p}</p>`;
        if (/^\{\{learner-b\b/.test(lead)) return `<p class="we-stronger">${p}</p>`;
      }
      return `<p>${p}</p>`;
    })
    .join('');
}

/**
 * Recursively substitute our tokens in all string fields of an object.
 * Only substitutes tokens we define (character.name, character.possessive,
 * context). Fails if any of OUR tokens remain unresolved; ignores Adapt's
 * runtime template tokens ({{scoreAsPercent}}, {{item}}, {{{feedback}}}, etc.).
 */
function substituteTokens(obj, tokens) {
  const unresolved = [];
  // Only match our specific character tokens
  const ourTokenNames = Object.keys(tokens);
  const ourTokenPattern = new RegExp(
    `\\{\\{(${ourTokenNames.map(t => t.replace('.', '\\.')).join('|')})\\}\\}`,
    'g'
  );

  function processValue(value, path) {
    if (typeof value === 'string') {
      let result = value;
      // Substitute our tokens
      result = result.replace(ourTokenPattern, (match, tokenName) => {
        return tokens[tokenName];
      });
      // Check if any of our tokens remain unresolved (shouldn't happen)
      for (const tokenName of ourTokenNames) {
        const pattern = new RegExp(`\\{\\{${tokenName.replace('.', '\\.')}\\}\\}`, 'g');
        if (pattern.test(result)) {
          unresolved.push({ token: `{{${tokenName}}}`, path });
        }
      }
      return result;
    }
    if (Array.isArray(value)) {
      return value.map((item, i) => processValue(item, `${path}[${i}]`));
    }
    if (value && typeof value === 'object') {
      const processed = {};
      for (const key of Object.keys(value)) {
        processed[key] = processValue(value[key], `${path}.${key}`);
      }
      return processed;
    }
    return value;
  }

  const result = processValue(obj, 'root');
  return { result, unresolved };
}

// ── two-character name pool (learner-a / learner-b worked-example slots) ──────
// Restores character names as true context slots: worked examples use
// {{learner-a}} (the weaker/negative example) and {{learner-b}} (the stronger/
// positive one) plus their .possessive forms; the build fills them from a shared
// pool, chosen deterministically per course so builds stay stable.
let _namePool = null;
// Default used only if _name-pool.json is missing/unreadable; 'they'/'their'
// is the only honest pronoun choice for a name that is itself a placeholder.
const FALLBACK_POOL = [
  { name: 'Student A', pronoun: 'they', possessive: 'their' },
  { name: 'Student B', pronoun: 'they', possessive: 'their' }
];
function normaliseNamePool(names) {
  // Accepts either the legacy flat-string form (["Amara", "Leo", ...]) or the
  // current {name, pronoun, possessive} object form; always returns objects,
  // defaulting pronoun/possessive to 'they'/'their' for a bare legacy string.
  return names.map(n => (typeof n === 'string')
    ? { name: n, pronoun: 'they', possessive: 'their' }
    : { name: n.name, pronoun: n.pronoun || 'they', possessive: n.possessive || 'their' });
}
function loadNamePool() {
  if (_namePool) return _namePool;
  try {
    const j = JSON.parse(fs.readFileSync(path.join(CONTEXT_PACKS_ROOT, '_name-pool.json'), 'utf8'));
    _namePool = (Array.isArray(j.names) && j.names.length >= 2) ? normaliseNamePool(j.names) : FALLBACK_POOL;
  } catch (e) { _namePool = FALLBACK_POOL; }
  return _namePool;
}
function hashStr(s) { let h = 2166136261 >>> 0; for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; } return h; }
function pickTwoNames(seed) {
  const pool = loadNamePool();
  const h = hashStr(String(seed || 'course'));
  const a = h % pool.length;
  let b = (Math.floor(h / pool.length) + 1 + (h % 7)) % pool.length;
  if (b === a) b = (a + 1) % pool.length;
  return [pool[a], pool[b]];
}

/**
 * Read each lesson's third-outcome tokenMode from the generated course's
 * manifest (course-design_<base>.json in outputDir). Returns a map
 * lessonKey -> 'generic' | 'cxp-fillable' (default cxp-fillable when the
 * les-01 check carries no token-substitution o3 item yet). See
 * docs/authoring/token-substitution-coupling-and-three-outcome-model.md.
 */
function readLessonTokenModes(outputDir) {
  const map = {};
  let files = [];
  try {
    files = fs.readdirSync(outputDir).filter(f => /^course-design_.*\.json$/.test(f));
  } catch (e) {
    return map;
  }
  if (files.length === 0) return map;
  const manifest = fs.readJsonSync(path.join(outputDir, files[0]));
  for (const g of manifest.gates || []) {
    const m = /-(L\d{2})-les-01$/.exec(g.gateId || '');
    if (!m) continue;
    const recs = g.records || [];
    const rec = recs[recs.length - 1];
    const items = (rec && rec.decidedValue && rec.decidedValue.check
      && rec.decidedValue.check.items) || [];
    const o3 = items.find(it => typeof it.tests === 'string' && it.tests.endsWith('-o3'));
    map[m[1]] = (o3 && o3.tokenMode) || 'cxp-fillable';
  }
  return map;
}

/**
 * Load context.json and apply token substitution to all course JSON files.
 *
 * Resolution order (CP-1f amendment, 4 Sep 2026):
 *   1. <context>/<tier>/context.json (tier-scoped override)
 *   2. <context>/context.json (pack-level fallback)
 *
 * Tier-level file is OPTIONAL. If present and has a valid character.name,
 * uses WHOLE-OBJECT replacement (no field-level merge with pack-level).
 * If absent or character.name is empty/missing, falls back to pack-level.
 */
async function applyTokenSubstitution(outputDir, context, tier) {
  const tierContextPath = path.join(contextPackDir(context, tier), 'context.json');
  const packContextPath = path.join(CONTEXT_PACKS_ROOT, context, 'context.json');

  let contextData;

  // Try tier-scoped context.json first
  if (fs.existsSync(tierContextPath)) {
    const tierData = await fs.readJson(tierContextPath);
    // Guard: must have non-empty character.name to use tier-level
    if (typeof tierData.character?.name === 'string' && tierData.character.name.trim() !== '') {
      contextData = tierData;
    }
  }

  // Fall back to pack-level context.json
  if (!contextData) {
    if (!fs.existsSync(packContextPath)) {
      console.error(`No pack-level context.json found at ${packContextPath}`);
      process.exit(1);
    }
    contextData = await fs.readJson(packContextPath);
  }
  // FLAGGED, not fixed (v4 lesson page model planning, step 2.4): this seeds on
  // the *tier* string, so every pathway at a given tier gets the same name pair
  // today - despite the comment above and _name-pool.json's own _comment both
  // describing the seed as "the course slug". Changing the seed to baseCourseSlug
  // would re-roll names for every already-merged course; deliberately left as-is
  // pending a decision, so it isn't fixed silently here.
  const [learnerA, learnerB] = pickTwoNames(tier);
  const baseTokens = {
    'character.name': contextData.character?.name || '',
    'character.possessive': contextData.character?.name
      ? `${contextData.character.name}'s`
      : '',
    // Two-character worked-example slots, pool-filled per course (see pickTwoNames).
    'learner-a': learnerA.name,
    'learner-b': learnerB.name,
    'learner-a.possessive': `${learnerA.name}'s`,
    'learner-b.possessive': `${learnerB.name}'s`,
    // Pronoun tokens so third-person prose doesn't need a hardcoded he/she.
    'learner-a-pronoun': learnerA.pronoun,
    'learner-a-possessive-pronoun': learnerA.possessive,
    'learner-b-pronoun': learnerB.pronoun,
    'learner-b-possessive-pronoun': learnerB.possessive
  };

  // {{context}} fills token-substitution coupled slots (the third lesson
  // outcome and its check item). It resolves PER LESSON from that lesson's
  // tokenMode (the les-01 check item that tests o3): 'generic' -> the floor
  // "your subject" regardless of the pack; 'cxp-fillable' -> the pack's
  // context.label, or the floor "your subject" when the pack sets none. One
  // pack can therefore fill some lessons disciplinarily and leave others
  // generic. See
  // docs/authoring/token-substitution-coupling-and-three-outcome-model.md.
  const contextLabel = (contextData.context && contextData.context.label) || null;
  const lessonMode = readLessonTokenModes(outputDir);
  const contextValueForLesson = (lessonKey) => {
    const mode = (lessonKey && lessonMode[lessonKey]) || 'cxp-fillable';
    return mode === 'generic' ? 'your subject' : (contextLabel || 'your subject');
  };

  console.log(`Applying token substitution (character: ${baseTokens['character.name']}, context label: ${contextLabel || '(none -> your subject)'}, lesson modes: ${JSON.stringify(lessonMode)})...`);

  const courseFiles = ['components.json', 'blocks.json', 'articles.json',
    'contentObjects.json', 'course.json'];
  let totalUnresolved = [];

  for (const filename of courseFiles) {
    const filePath = path.join(outputDir, 'en', filename);
    if (!fs.existsSync(filePath)) continue;

    const data = await fs.readJson(filePath);
    let result;
    const unresolved = [];
    if (filename === 'components.json' && Array.isArray(data)) {
      // Per-component {{context}}: resolve by the component's lesson key
      // (its _id's L## prefix) so each lesson's tokenMode governs its own
      // token. The character.* tokens stay global.
      result = data.map((comp) => {
        const lessonKey = (comp && typeof comp._id === 'string'
          && (comp._id.match(/^(L\d{2})/) || [])[1]) || null;
        const tokens = Object.assign({}, baseTokens,
          { 'context': contextValueForLesson(lessonKey) });
        const r = substituteTokens(comp, tokens);
        unresolved.push(...r.unresolved);
        return r.result;
      });
    } else {
      const tokens = Object.assign({}, baseTokens,
        { 'context': contextLabel || 'your subject' });
      const r = substituteTokens(data, tokens);
      result = r.result;
      unresolved.push(...r.unresolved);
    }

    if (unresolved.length > 0) {
      totalUnresolved.push(...unresolved.map(u => ({
        ...u,
        file: filename
      })));
    }

    await fs.writeJson(filePath, result, { spaces: 2 });
  }

  if (totalUnresolved.length > 0) {
    console.error(`\nToken substitution failed with ${totalUnresolved.length} unresolved token(s):`);
    totalUnresolved.forEach(u =>
      console.error(`  - ${u.token} in ${u.file} at ${u.path}`)
    );
    process.exit(1);
  }

  console.log('Token substitution complete.');
}

/**
 * Fill exactly what the coupling plan names (CPL-1, restated for LK-1,
 * Prompt 154). baseCourseSlug and planSlotsByPage come from
 * requireCouplingPlan(). planSlotsByPage maps each page to a
 * Map(slotType -> variationType) for its coupled slots only.
 *
 * Multi-component-fill (quoted from the pre-change code before this
 * function was rewritten, Prompt 154 ruling 5's stop condition): the
 * pre-change loop matched each component independently against its own
 * _classes marker — `const packSlug = slotLessonToPackSlug(slot.lesson);`
 * then per-component branches on `component._component` — with no
 * dedup keyed by marker, so N components carrying the same marker each
 * got filled independently from the same cached pack object. That
 * independent-pass structure is superseded below by MP-1 (Prompt 159) /
 * PKY-1 (Prompt 160, both docs/project/open-decisions.md): two components
 * on one page carrying the same page, slot and part — including two both
 * carrying the part-less form — now fail, naming both, rather than both
 * being filled from the same pack object as before.
 *
 * PKY-1: every pack lookup below is keyed by packKeyFor(slot) —
 * <slotType> when the marker carries no part, <slotType>__<part> when it
 * does — in whichever of generatedProse, generatedItems and
 * generatedItemsHtml the component's type uses. The existing Intro/Body/
 * Instruction suffixes append to that same key. Three legacy lookups this
 * replaces are retired: the flat generatedHtml fallback that assigned the
 * pack's whole generatedHtml value to any unmatched component in a
 * worked-example slot; the fixed key workedExampleIntro in the accordion
 * branch; and the fixed key steerCheck in the mcq branch.
 */
async function mergeContext(outputDir, context, tier, baseCourseSlug, planSlotsByPage) {
  if (context === 'book') {
    console.log('Context is "book" — merging normally, same as any other context (all pack files now have complete data).');
  }

  const componentsPath = path.join(outputDir, 'en', 'components.json');
  const components = await fs.readJson(componentsPath);
  const markerPageToPageKey = loadMarkerPageToPageKey();

  const packCache = {};
  const foundPlanned = new Set(); // "page::slotType" for every planned slot whose marker was found
  const markerOwners = new Map(); // "page::slotType::part" -> owning component._id
  let mergedCount = 0;
  const errors = [];

  for (const component of components) {
    const slot = parseSlotMarker(component._classes);
    if (!slot) continue;

    // LK-1 wrapper-marker reconciliation: a marker's page may be an archetype
    // key for a fixed page (e.g. "wrapper-open"); the coupling plan and pack
    // files key that page by its baseKey (e.g. "W-OPEN"). Lesson pages map to
    // themselves. See loadMarkerPageToPageKey above.
    const pageKey = markerPageToPageKey.get(slot.page) || slot.page;

    const slotMap = planSlotsByPage.get(pageKey);
    if (!slotMap || !slotMap.has(slot.slotType)) {
      errors.push(`Marker "${markerString(slot)}" on component ${component._id} names a page/slot the coupling plan for course "${tier}" does not: no page "${pageKey}" with a coupled slot "${slot.slotType}" in instantiations[].`);
      continue;
    }
    foundPlanned.add(`${pageKey}::${slot.slotType}`);

    // MP-1/PKY-1: two components on one page carrying the same page, slot
    // and part fail, naming both, rather than both being filled from the
    // same pack object.
    const ownerKey = `${pageKey}::${slot.slotType}::${slot.part || ''}`;
    if (markerOwners.has(ownerKey)) {
      errors.push(`Two components carry the same marker "${markerString(slot)}": ${markerOwners.get(ownerKey)} and ${component._id}.`);
      continue;
    }
    markerOwners.set(ownerKey, component._id);

    const key = packKeyFor(slot);

    if (!packCache[pageKey]) {
      const packPath = path.join(contextPackDir(context, baseCourseSlug), `${pageKey}.json`);
      if (!fs.existsSync(packPath)) {
        errors.push(`Pack file the coupling plan needs is missing: no context pack for page "${pageKey}" at ${packPath} (course "${tier}", context "${context}").`);
        continue;
      }
      packCache[pageKey] = await fs.readJson(packPath);
    }
    const pack = packCache[pageKey];

    // PKY-1: mcq reads generatedItems[<key>], like every other item-based
    // component below. Retires the fixed steerCheck key.
    if (component._component === 'mcq' && pack.generatedItems && pack.generatedItems[key]) {
      const sc = pack.generatedItems[key];
      // v3 knowledge-check: the subject question stem is the component header
      // (displayTitle, aria-level-4 heading under the "Check your understanding"
      // article), not body prose. Non-check mcqs (e.g. summative items) keep the
      // question in body as before.
      if ((component._classes || '').includes('knowledge-check-question')) {
        component.displayTitle = sc.body;
        component.body = '';
      } else {
        component.body = `<p>${sc.body}</p>`;
      }
      component._items = sc.items.map(item => {
        const mapped = {
          text: item.text,
          _shouldBeSelected: item._shouldBeSelected
        };
        // Case 1: pass through voice-lint ignore flags from pack item
        if (item._voiceLintIgnore === true) {
          mapped._voiceLintIgnore = true;
          if (item._voiceLintReason) mapped._voiceLintReason = item._voiceLintReason;
        }
        return mapped;
      });
      if (component._feedback) {
        component._feedback.correct = sc.feedback.correct;
        component._feedback._incorrect = component._feedback._incorrect || {};
        component._feedback._incorrect.notFinal = sc.feedback.incorrectNotFinal;
        component._feedback._incorrect.final = sc.feedback.incorrectFinal;
      }
      mergedCount++;
      continue;
    }

    // PKY-1: matching reads generatedItems[<key>], like mcq — each row
    // carries its own _options with correctness. Mirrors the mcq branch
    // above (body + items + feedback), with matching's per-row _options
    // and its _partlyCorrect feedback branch.
    if (component._component === 'matching' && pack.generatedItems && pack.generatedItems[key]) {
      const sc = pack.generatedItems[key];
      // v3 knowledge-check: question stem as the component header (see mcq branch).
      if ((component._classes || '').includes('knowledge-check-question')) {
        component.displayTitle = sc.body;
        component.body = '';
      } else {
        component.body = `<p>${sc.body}</p>`;
      }
      component._items = sc.items.map(item => {
        const mapped = {
          text: item.text,
          _options: item._options.map(o => ({
            text: o.text,
            _isCorrect: o._isCorrect,
            _score: o._score
          }))
        };
        // Case 1: pass through voice-lint ignore flags from pack item
        if (item._voiceLintIgnore === true) {
          mapped._voiceLintIgnore = true;
          if (item._voiceLintReason) mapped._voiceLintReason = item._voiceLintReason;
        }
        return mapped;
      });
      if (component._feedback) {
        component._feedback.correct = sc.feedback.correct;
        component._feedback._incorrect = component._feedback._incorrect || {};
        component._feedback._incorrect.notFinal = sc.feedback.incorrectNotFinal;
        component._feedback._incorrect.final = sc.feedback.incorrectFinal;
        if (sc.feedback.partlyCorrectNotFinal !== undefined || sc.feedback.partlyCorrectFinal !== undefined) {
          component._feedback._partlyCorrect = component._feedback._partlyCorrect || {};
          component._feedback._partlyCorrect.notFinal = sc.feedback.partlyCorrectNotFinal || '';
          component._feedback._partlyCorrect.final = sc.feedback.partlyCorrectFinal || '';
        }
      }
      mergedCount++;
      continue;
    }

    // Accordion: check for pre-wrapped HTML (generatedItemsHtml) first,
    // fall back to raw text (generatedItems) with wrapping
    const itemsHtml = pack.generatedItemsHtml?.[key];
    const itemsRaw = pack.generatedItems?.[key];
    if (component._component === 'accordion' && (itemsHtml || itemsRaw)) {
      // Body intro: check for pre-wrapped HTML first, then raw prose.
      // PKY-1: keyed as `${key}Intro`, retiring the fixed
      // workedExampleIntro key.
      const introKey = `${key}Intro`;
      if (pack.generatedHtml?.[introKey]) {
        component.body = pack.generatedHtml[introKey];
        // Case 2: pass through voice-lint ignore flags from generatedHtml object to component
        // Note: this suppresses all direct string properties of the component, not just body
        if (pack.generatedHtml._voiceLintIgnore === true) {
          component._voiceLintIgnore = true;
          if (pack.generatedHtml._voiceLintReason) component._voiceLintReason = pack.generatedHtml._voiceLintReason;
        }
      } else if (pack.generatedProse?.[introKey]) {
        component.body = `<p>${pack.generatedProse[introKey]}</p>`;
      }
      // Items: use pre-wrapped HTML as-is, or wrap raw text
      if (itemsHtml) {
        component._items = itemsHtml.map(item => {
          const mapped = { title: item.title, body: item.body };
          // Case 1: pass through voice-lint ignore flags from pack item
          if (item._voiceLintIgnore === true) {
            mapped._voiceLintIgnore = true;
            if (item._voiceLintReason) mapped._voiceLintReason = item._voiceLintReason;
          }
          return mapped;
        });
      } else {
        component._items = itemsRaw.map(item => {
          const mapped = { title: item.title, body: `<p><em>${item.body}</em></p>` };
          // Case 1: pass through voice-lint ignore flags from pack item
          if (item._voiceLintIgnore === true) {
            mapped._voiceLintIgnore = true;
            if (item._voiceLintReason) mapped._voiceLintReason = item._voiceLintReason;
          }
          return mapped;
        });
      }
      mergedCount++;
      continue;
    }

    // Annotated: substitute _passage[] from pack data
    // Check for pre-wrapped HTML (generatedItemsHtml) first, fall back to raw (generatedItems)
    const segmentsHtml = pack.generatedItemsHtml?.[key];
    const segmentsRaw = pack.generatedItems?.[key];
    if (component._component === 'annotated' && (segmentsHtml || segmentsRaw)) {
      const segments = segmentsHtml || segmentsRaw;
      const isHtml = !!segmentsHtml;

      // Validate: every segment must have text
      const missingText = segments.filter(s => !s.text);
      if (missingText.length) {
        errors.push(
          `Slot "${slot.slotType}" (annotated) has ${missingText.length} segment(s) missing required "text" field in pack for page "${slot.page}".`
        );
        continue;
      }

      // Validate: noteTitle without noteBody is invalid
      const noteWithoutBody = segments.filter(s => s.noteTitle && !s.noteBody);
      if (noteWithoutBody.length) {
        errors.push(
          `Slot "${slot.slotType}" (annotated) has ${noteWithoutBody.length} segment(s) with noteTitle but missing noteBody in pack for page "${slot.page}".`
        );
        continue;
      }

      // Body intro: check for slot-specific intro (generatedHtml then generatedProse)
      const introKey = `${key}Intro`;
      if (pack.generatedHtml?.[introKey]) {
        component.body = pack.generatedHtml[introKey];
        // Case 2: pass through voice-lint ignore flags from generatedHtml object to component
        // Note: this suppresses all direct string properties of the component, not just body
        if (pack.generatedHtml._voiceLintIgnore === true) {
          component._voiceLintIgnore = true;
          if (pack.generatedHtml._voiceLintReason) component._voiceLintReason = pack.generatedHtml._voiceLintReason;
        }
      } else if (pack.generatedProse?.[introKey]) {
        component.body = `<p>${pack.generatedProse[introKey]}</p>`;
      }

      // Map segments to _passage[] structure
      // Raw noteBody wrapped in <p>...</p> (no italics — commentary, not quoted text)
      component._passage = segments.map(seg => {
        const entry = { text: seg.text };
        if (seg.noteBody) {
          entry._note = {
            title: seg.noteTitle || '',
            body: isHtml ? seg.noteBody : `<p>${seg.noteBody}</p>`
          };
        }
        // Case 1: pass through voice-lint ignore flags from pack segment
        if (seg._voiceLintIgnore === true) {
          entry._voiceLintIgnore = true;
          if (seg._voiceLintReason) entry._voiceLintReason = seg._voiceLintReason;
        }
        return entry;
      });

      mergedCount++;
      continue;
    }

    // Branching: substitute body, instruction, and _items[] from pack data
    // Check for pre-wrapped HTML (generatedItemsHtml) first, fall back to raw (generatedItems)
    const branchingItemsHtml = pack.generatedItemsHtml?.[key];
    const branchingItemsRaw = pack.generatedItems?.[key];
    if (component._component === 'branching' && (branchingItemsHtml || branchingItemsRaw)) {
      const items = branchingItemsHtml || branchingItemsRaw;
      const isHtml = !!branchingItemsHtml;

      // Validate: every item must have text and consequence.body
      const missingText = items.filter(i => !i.text);
      if (missingText.length) {
        errors.push(
          `Slot "${slot.slotType}" (branching) has ${missingText.length} item(s) missing required "text" field in pack for page "${slot.page}".`
        );
        continue;
      }
      const missingConsequence = items.filter(i => !i.consequence?.body);
      if (missingConsequence.length) {
        errors.push(
          `Slot "${slot.slotType}" (branching) has ${missingConsequence.length} item(s) missing required "consequence.body" field in pack for page "${slot.page}".`
        );
        continue;
      }

      // Body: check for slot-specific body (generatedHtml then generatedProse)
      const bodyKey = `${key}Body`;
      if (pack.generatedHtml?.[bodyKey]) {
        component.body = pack.generatedHtml[bodyKey];
        // Case 2: pass through voice-lint ignore flags from generatedHtml object to component
        if (pack.generatedHtml._voiceLintIgnore === true) {
          component._voiceLintIgnore = true;
          if (pack.generatedHtml._voiceLintReason) component._voiceLintReason = pack.generatedHtml._voiceLintReason;
        }
      } else if (pack.generatedProse?.[bodyKey]) {
        component.body = `<p>${pack.generatedProse[bodyKey]}</p>`;
      }

      // Instruction: check for slot-specific instruction (generatedProse only — plain string)
      const instructionKey = `${key}Instruction`;
      if (pack.generatedProse?.[instructionKey]) {
        component.instruction = pack.generatedProse[instructionKey];
      }

      // Map items to _items[] structure with nested consequence objects
      // Copy all fields from pack item; transform consequence.body (wrap raw in <p>)
      component._items = items.map(item => {
        const entry = { ...item };
        // Transform consequence.body: wrap raw in <p>
        if (entry.consequence && entry.consequence.body && !isHtml) {
          entry.consequence = {
            ...entry.consequence,
            body: `<p>${entry.consequence.body}</p>`
          };
        }
        return entry;
      });

      mergedCount++;
      continue;
    }

    // Timeline: substitute body, instruction, and _items[] from pack data
    // Check for pre-wrapped HTML (generatedItemsHtml) first, fall back to raw (generatedItems)
    const timelineItemsHtml = pack.generatedItemsHtml?.[key];
    const timelineItemsRaw = pack.generatedItems?.[key];
    if (component._component === 'timeline' && (timelineItemsHtml || timelineItemsRaw)) {
      const items = timelineItemsHtml || timelineItemsRaw;
      const isHtml = !!timelineItemsHtml;

      // Validate: every item must have label and title (schema required fields)
      const missingLabel = items.filter(i => !i.label);
      if (missingLabel.length) {
        errors.push(
          `Slot "${slot.slotType}" (timeline) has ${missingLabel.length} item(s) missing required "label" field in pack for page "${slot.page}".`
        );
        continue;
      }
      const missingTitle = items.filter(i => !i.title);
      if (missingTitle.length) {
        errors.push(
          `Slot "${slot.slotType}" (timeline) has ${missingTitle.length} item(s) missing required "title" field in pack for page "${slot.page}".`
        );
        continue;
      }

      // Body: check for slot-specific body (generatedHtml then generatedProse)
      const bodyKey = `${key}Body`;
      if (pack.generatedHtml?.[bodyKey]) {
        component.body = pack.generatedHtml[bodyKey];
        // Case 2: pass through voice-lint ignore flags from generatedHtml object to component
        if (pack.generatedHtml._voiceLintIgnore === true) {
          component._voiceLintIgnore = true;
          if (pack.generatedHtml._voiceLintReason) component._voiceLintReason = pack.generatedHtml._voiceLintReason;
        }
      } else if (pack.generatedProse?.[bodyKey]) {
        component.body = `<p>${pack.generatedProse[bodyKey]}</p>`;
      }

      // Instruction: check for slot-specific instruction (generatedProse only — plain string)
      const instructionKey = `${key}Instruction`;
      if (pack.generatedProse?.[instructionKey]) {
        component.instruction = pack.generatedProse[instructionKey];
      }

      // Map items to _items[] structure
      // Copy all fields from pack item; transform body (wrap raw in <p>)
      component._items = items.map(item => {
        const entry = { ...item };
        // Transform body: wrap raw prose in <p>
        if (entry.body && !isHtml) {
          entry.body = `<p>${entry.body}</p>`;
        }
        return entry;
      });

      mergedCount++;
      continue;
    }

    // PKY-1 (Prompt 160): generatedProse[<key>] is the remaining generic
    // fallback. The flat generatedHtml fallback that used to sit here for
    // any unmatched component in a worked-example slot is retired: it
    // assigned the pack's whole generatedHtml value with no key to attach
    // a part to (MP-1's own "Applies to" note, docs/project/open-decisions.md).
    if (pack.generatedProse && pack.generatedProse[key]) {
      component.body = wrapProse(pack.generatedProse[key], slot.slotType);
      mergedCount++;
      continue;
    }

    errors.push(
      `Planned slot has no content in its pack file: marker "${markerString(slot)}" (component ${component._id}, type ${component._component}) has no matching data in the pack for page "${slot.page}", context "${context}", key "${key}".`
    );
  }

  // "a planned slot has no marker in the course" (Prompt 154, ruling 5)
  for (const [page, slotMap] of planSlotsByPage.entries()) {
    for (const slotType of slotMap.keys()) {
      if (!foundPlanned.has(`${page}::${slotType}`)) {
        errors.push(`Planned slot has no marker in the course: the coupling plan for course "${tier}" names coupled slot "${slotType}" on page "${page}" (instantiations[]), but no component in the built course carries marker slot__${page}__${slotType}.`);
      }
    }
  }

  if (errors.length) {
    console.error(`\nMerge failed with ${errors.length} unresolved slot(s):`);
    errors.forEach(e => console.error(`  - ${e}`));
    process.exit(1);
  }

  let totalPlannedSlots = 0;
  for (const slotMap of planSlotsByPage.values()) totalPlannedSlots += slotMap.size;
  if (mergedCount === 0 && totalPlannedSlots > 0) {
    console.error(`\nMerge filled 0 slots for course "${tier}", context "${context}", but the coupling plan names ${totalPlannedSlots} slot(s) across ${planSlotsByPage.size} page(s). Treating this as a failure rather than a correct empty run.`);
    process.exit(1);
  }

  await fs.writeJson(componentsPath, components, { spaces: 2 });
  console.log(`Merge complete: ${mergedCount} slot(s) filled for context "${context}".`);
}

async function main() {
  parseArgs();
  const { context, tier } = argumentValues;
  const { baseCourseSlug, planSlotsByPage } = requireCouplingPlan(tier);
  const resolved = resolveCourse(tier, ['courses']);
  if (!resolved.found) {
    console.error(`No course folder found for "${tier}" under courses/ (checked: ${resolved.checked.join(', ')}).`);
    process.exit(1);
  }
  const shellDir = resolved.courseDir;
  const outputDir = path.join(GENERATED_ROOT, `${tier}-${context}`);

  await extractShell(shellDir, outputDir);
  await mergeContext(outputDir, context, tier, baseCourseSlug, planSlotsByPage);
  await applyTokenSubstitution(outputDir, context, tier);

  console.log(`\nDone. Course ready at courses/_generated/${tier}-${context}/`);
  console.log('To build it: rm src/course && ln -s ../courses/_generated/' +
    `${tier}-${context} src/course && grunt build`);
}

if (require.main === module) {
  main().catch(err => {
    console.error('merge-context.js failed:', err);
    process.exit(1);
  });
}

// Exported for unit testing of the coupling-plan read (the one piece the
// six-phase migration changed); requiring this module does not run main.
// Also exports the slot-marker/pack-key helpers and the packs root so
// course-script-import.js's --script mode can route an edited chunk to the
// same pack file/key this module would read at merge time, without
// duplicating that logic. Requiring this module does not run main.
module.exports = { requireCouplingPlan, parseSlotMarker, packKeyFor, loadMarkerPageToPageKey, CONTEXT_PACKS_ROOT };
