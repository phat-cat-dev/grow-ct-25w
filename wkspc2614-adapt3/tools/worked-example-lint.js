#!/usr/bin/env node
/**
 * worked-example-lint.js
 *
 * Conformance lint for the worked-example cast convention: every worked
 * example must contrast a weaker example ({{learner-a}}) with a stronger
 * one ({{learner-b}}), each example paragraph leading with its token
 * (weaker first), never a bare pool first name or a literal "Student A" /
 * "Student B". This is a separate tool from conformance-lint.js
 * deliberately (see plan step 7): conformance-lint.js is a CI gate that
 * reads blocks.json only, never components.json or the context packs, and
 * wiring 423 known-bad files straight into it would turn the build red on
 * work deliberately deferred (see docs/authoring/worked-example-cue-
 * convention.md and the lesson-page-model-v4 plan, step 7).
 *
 * Two modes:
 *
 *   --packs (default)
 *     Walks content/context-packs/**\/*.json and reads each file's
 *     generatedProse['worked-example'] (plain text, '\n\n'-separated
 *     paragraphs - the pre-merge shape merge-context.js's wrapProse()
 *     operates on, see merge-context.js:210-232). Prints the 4-way census
 *     (conformant / studentAB / poolName / noCast) and ratchets on
 *     BACKLOG_CEILING: exits non-zero only if the non-conformant count
 *     EXCEEDS the ceiling, so the backlog can shrink (by hand, lowering
 *     the constant) but never silently grow.
 *
 *   --course=<slug>
 *     Resolves the slug via lib/course-resolve.js against both 'courses'
 *     (the authored, pre-merge shell) and 'courses/_generated' (a merged
 *     tier variant). Walks blocks.json for _skeletonKey === 'worked-example'
 *     and the matching component(s) in components.json (body directly, or
 *     _items[].body for an accordion-shaped component). Which assertions
 *     apply depends on which root the slug resolved under:
 *       - 'courses' (unmerged): the body must still carry the
 *         {{learner-a}}/{{learner-b}} tokens, so assertions 1-5 apply.
 *       - 'courses/_generated' (merged): tokens have already been
 *         substituted for real names by merge-context.js's Stage 3 - that is
 *         the correct, expected outcome, so assertions 1-5 would fail
 *         spuriously there and are skipped. Only assertion 6 (exactly one
 *         we-weaker/we-stronger pair) is checked on merged content.
 *     Exits non-zero if ANY worked-example block in this one course fails
 *     its applicable assertions (a hard per-course gate, not a ratchet -
 *     this is the --strict check wired into verify-course.js).
 *
 * The 8 assertions (plan step 7, extended 7 Nov 2026 with assertion 0):
 *   0. The block's component is _component: "workedExample"              [course mode]
 *      (docs/authoring/component-specs/worked-example.md). Checked in
 *      --course mode only (there is no component type in a context
 *      pack): a worked-example slot realised as "narrative" or "text" is
 *      a spec violation even when its prose is otherwise conformant -
 *      the boundary table in that spec restricts "narrative" to
 *      image-based before/after comparisons, never prose-only contrasts.
 *   1. Contains both {{learner-a}} and {{learner-b}}.                 [tokens mode]
 *   2. At least one paragraph *begins* with each token (mirrors         [tokens mode]
 *      merge-context.js:226-227's /^\{\{learner-a\b/ etc.) - the silent
 *      failure mode: a token can be present mid-paragraph and never get
 *      the we-weaker/we-stronger cue class at merge time.
 *   3. The learner-a-leading paragraph precedes the learner-b-leading     [tokens mode]
 *      one (weaker example first).
 *   4. No bare pool first name (word-boundary, from _name-pool.json).    [tokens mode]
 *   5. No literal "Student A" / "Student B".                            [tokens mode]
 *   6. On a merged course: exactly one <p class="we-weaker"> and one     [merged mode]
 *      <p class="we-stronger">.
 *   7. Warn-level only (never fails the gate): a bare he/she/his/her/    [always, both modes]
 *      they/their inside an already-cued (we-weaker/we-stronger)
 *      paragraph, now that the gendered pronoun tokens exist (step 2).
 *
 * BACKLOG_CEILING = 423 empirically confirmed against the current repo
 * (459 context-pack files carry a worked-example body; 36 are already
 * fully conformant against all five token-mode assertions; 423 are not -
 * 113 hardcoded "Student A"/"Student B", 236 hardcoded pool names, 74 with
 * no named cast at all). Every fix lowers this constant by hand; the
 * ratchet means no new file can push the count back up unnoticed.
 *
 * Usage:
 *   node tools/worked-example-lint.js [--packs] [--json]
 *   node tools/worked-example-lint.js --course=<slug> [--json]
 *
 * Landed: 2 Nov 2026, lesson-page-model-v4 plan, step 7.
 */

const fs = require('fs');
const path = require('path');
const { resolveCourse } = require('./lib/course-resolve');
const { CONTEXT_PACKS_ROOT, RELOCATED_CONTEXT_PACKS } = require('../merge-context');

const ROOT = path.resolve(__dirname, '..');
// 315 confirmed against the current repo (8 Nov 2026). History: 459
// context-pack files carry a worked-example body across all three
// relocated contexts (universal/baseline, hecos/psychology, cmet/
// schools/sport - 153 each). The 2 Nov 2026 figure of 423 non-conformant
// fell to 408 after a first 15-file fix to the universal/baseline
// context, then to 315 after converting the remaining 98 literal
// "Student A"/"Student B" files (the studentAB bucket, now 0 - that
// pattern existed only in the universal/baseline context; hecos/
// psychology and cmet/schools/sport use the poolName pattern instead,
// still outstanding). 144 files are now fully conformant.
// See runPacksMode()'s directory-discovery fix below (8 Nov 2026): this
// ratchet silently read 0 files and always passed from the day the
// context packs were relocated out of content/context-packs/
// (RELOCATED_CONTEXT_PACKS, merge-context.js) until that fix, because its
// file-discovery never followed the relocation. Every fix lowers this
// constant by hand; the ratchet means no new file can push the count
// back up unnoticed.
const BACKLOG_CEILING = 315;

function parseArgs() {
  const args = { mode: 'packs', course: null, json: false };
  for (const raw of process.argv.slice(2)) {
    if (raw === '--packs') args.mode = 'packs';
    else if (raw.startsWith('--course=')) { args.mode = 'course'; args.course = raw.slice('--course='.length); }
    else if (raw === '--json') args.json = true;
    else {
      console.error(`Unknown argument: ${raw}`);
      console.error('Usage: node tools/worked-example-lint.js [--packs] [--json]');
      console.error('       node tools/worked-example-lint.js --course=<slug> [--json]');
      process.exit(1);
    }
  }
  return args;
}

function loadNamePool() {
  const p = path.join(ROOT, 'content', 'context-packs', '_name-pool.json');
  const data = JSON.parse(fs.readFileSync(p, 'utf8'));
  // names[] has carried {name, pronoun, possessive} objects since step 2
  // (2 Nov 2026); tolerate the legacy flat-string shape too.
  return data.names.map(n => (typeof n === 'string' ? n : n.name));
}

function walkJsonFiles(dir) {
  const out = [];
  (function walk(d) {
    for (const entry of fs.readdirSync(d, { withFileTypes: true })) {
      const p = path.join(d, entry.name);
      if (entry.isDirectory()) walk(p);
      else if (entry.name.endsWith('.json')) out.push(p);
    }
  })(dir);
  return out;
}

// Discover every context-pack file carrying a worked-example body,
// following the relocation (RELOCATED_CONTEXT_PACKS, merge-context.js): a
// relocated context's files now live under
// courses/<pathway>/<relocated-subpath>/<tier-slug>/*.json, one subtree
// per pathway, rather than flat under content/context-packs/<context>/. A
// context not listed in RELOCATED_CONTEXT_PACKS is still read from the
// legacy flat location.
// Returns [{file, context, pathway}], pathway being the tier slug
// (e.g. "academic-writing-advanced") for the per-pathway breakdown.
function discoverPackFiles() {
  const out = [];

  // Legacy flat layout: content/context-packs/<context>/<tier-slug>/*.json,
  // for any context not (or not yet) relocated.
  if (fs.existsSync(CONTEXT_PACKS_ROOT)) {
    for (const entry of fs.readdirSync(CONTEXT_PACKS_ROOT, { withFileTypes: true })) {
      if (!entry.isDirectory()) continue;
      const context = entry.name;
      if (RELOCATED_CONTEXT_PACKS[context]) continue; // relocated - handled below
      const contextDir = path.join(CONTEXT_PACKS_ROOT, context);
      for (const f of walkJsonFiles(contextDir)) {
        const segments = path.relative(contextDir, f).split(path.sep);
        out.push({ file: f, context, pathway: segments[0] || null });
      }
    }
  }

  // Relocated layout: courses/<pathway>/<relocated-subpath>/<tier-slug>/*.json.
  const coursesDir = path.join(ROOT, 'courses');
  const pathwayDirs = fs.existsSync(coursesDir)
    ? fs.readdirSync(coursesDir, { withFileTypes: true }).filter(e => e.isDirectory() && !e.name.startsWith('_')).map(e => e.name)
    : [];
  for (const [context, relocatedSubpath] of Object.entries(RELOCATED_CONTEXT_PACKS)) {
    for (const pathwayName of pathwayDirs) {
      const contextDir = path.join(coursesDir, pathwayName, relocatedSubpath);
      if (!fs.existsSync(contextDir)) continue;
      for (const f of walkJsonFiles(contextDir)) {
        const segments = path.relative(contextDir, f).split(path.sep);
        out.push({ file: f, context, pathway: segments[0] || null });
      }
    }
  }

  return out;
}

// ── paragraph extraction ────────────────────────────────────────────────

// --packs mode: generatedProse['worked-example'] is plain text, paragraphs
// separated by a literal blank line - exactly what merge-context.js's
// wrapProse() splits on.
function plainParagraphs(text) {
  return text.split('\n\n').map(t => ({ cls: null, text: t }));
}

// --course mode: component body is HTML. Paragraphs are <p ...>...</p>
// segments; a class attribute, when present, carries the we-weaker/
// we-stronger cue merge-context.js's wrapProse() (or, for a hand-authored
// shell body, the author) assigned.
function htmlParagraphs(html) {
  const out = [];
  const re = /<p(?:\s+class="([^"]*)")?[^>]*>([\s\S]*?)<\/p>/g;
  let m;
  while ((m = re.exec(html))) out.push({ cls: m[1] || null, text: m[2] });
  return out;
}

// ── assertions ───────────────────────────────────────────────────────────

/**
 * paragraphs: [{cls: string|null, text: string}, ...]
 * mode: 'tokens' (pre-merge content - assertions 1-5 apply) or
 *       'merged'  (post-merge content - only assertion 6 applies)
 * namePool: flat array of first names from _name-pool.json
 */
function assess(paragraphs, { namePool, mode }) {
  const allText = paragraphs.map(p => p.text).join('\n\n');
  const assertions = {};

  if (mode === 'tokens') {
    const hasA = allText.includes('{{learner-a}}');
    const hasB = allText.includes('{{learner-b}}');
    const leadIndex = (tok) => paragraphs.findIndex(
      p => new RegExp('^\\{\\{' + tok + '\\b').test(p.text.replace(/^\s+/, ''))
    );
    const aLead = leadIndex('learner-a');
    const bLead = leadIndex('learner-b');
    const hasStudentAB = /\bStudent A\b/.test(allText) || /\bStudent B\b/.test(allText);
    const hasPoolName = namePool.some(n => new RegExp('\\b' + n + '\\b').test(allText));

    assertions.a1_bothTokens = hasA && hasB;
    assertions.a2_leadingToken = aLead !== -1 && bLead !== -1;
    assertions.a3_weakerFirst = aLead !== -1 && bLead !== -1 && aLead < bLead;
    assertions.a4_noBarePoolName = !hasPoolName;
    assertions.a5_noLiteralStudentAB = !hasStudentAB;
  } else {
    const weakerCount = paragraphs.filter(p => p.cls === 'we-weaker').length;
    const strongerCount = paragraphs.filter(p => p.cls === 'we-stronger').length;
    assertions.a6_mergedPairing = weakerCount === 1 && strongerCount === 1;
  }

  // Assertion 7: warn-level, computed in both modes, never affects pass/fail.
  const cuedParagraphs = paragraphs.filter(p => p.cls === 'we-weaker' || p.cls === 'we-stronger');
  const warnBarePronoun = cuedParagraphs.some(p => /\b(he|she|his|her|they|their)\b/i.test(p.text));

  const pass = Object.values(assertions).every(Boolean);

  let bucket = null;
  if (mode === 'tokens') {
    if (assertions.a1_bothTokens) bucket = 'conformant';
    else if (/\bStudent A\b/.test(allText) || /\bStudent B\b/.test(allText)) bucket = 'studentAB';
    else if (namePool.some(n => new RegExp('\\b' + n + '\\b').test(allText))) bucket = 'poolName';
    else bucket = 'noCast';
  }

  return { assertions, pass, bucket, warnBarePronoun };
}

// ── --packs mode ─────────────────────────────────────────────────────────

function runPacksMode(opts) {
  const discovered = discoverPackFiles();
  const namePool = loadNamePool();

  const results = [];
  for (const { file: f, context, pathway } of discovered) {
    let j;
    try { j = JSON.parse(fs.readFileSync(f, 'utf8')); } catch (e) { continue; }
    const we = j.generatedProse && j.generatedProse['worked-example'];
    if (!we) continue;
    const paragraphs = plainParagraphs(we);
    const r = assess(paragraphs, { namePool, mode: 'tokens' });
    const rel = path.relative(ROOT, f);
    results.push({ file: rel, context, pathway, ...r });
  }

  const withWE = results.length;
  const conformant = results.filter(r => r.pass).length;
  const nonConformant = withWE - conformant;
  const buckets = { conformant: 0, studentAB: 0, poolName: 0, noCast: 0 };
  for (const r of results) buckets[r.bucket]++;

  // Per-pathway breakdown (pathway-tier slug, summed across contexts).
  const byPathway = {};
  for (const r of results) {
    if (!r.pathway) continue;
    byPathway[r.pathway] = byPathway[r.pathway] || { total: 0, conformant: 0 };
    byPathway[r.pathway].total++;
    if (r.pass) byPathway[r.pathway].conformant++;
  }

  const census = { withWE, conformant, nonConformant, ceiling: BACKLOG_CEILING, buckets, byPathway };

  if (opts.json) {
    console.log(JSON.stringify({
      mode: 'packs',
      census,
      results: results.map(r => ({
        file: r.file, context: r.context, pathway: r.pathway,
        pass: r.pass, bucket: r.bucket, assertions: r.assertions, warnBarePronoun: r.warnBarePronoun
      }))
    }, null, 2));
  } else {
    console.log('worked-example-lint --packs');
    console.log('='.repeat(60));
    console.log(`Context-pack files carrying a worked-example body: ${withWE}`);
    console.log(`Fully conformant (all 5 token-mode assertions):    ${conformant}`);
    console.log(`Non-conformant:                                    ${nonConformant}  (ceiling: ${BACKLOG_CEILING})`);
    console.log('');
    console.log('4-way census (each non-conformant file classified by its first-matching reason):');
    console.log(`  conformant                                 : ${buckets.conformant}`);
    console.log(`  studentAB (literal "Student A"/"Student B"): ${buckets.studentAB}`);
    console.log(`  poolName (bare pool first name, no tokens) : ${buckets.poolName}`);
    console.log(`  noCast (no named cast, no tokens)          : ${buckets.noCast}`);
    console.log('');
    console.log('Per-pathway breakdown (summed across all context packs):');
    const pathways = Object.keys(byPathway).sort();
    for (const p of pathways) {
      const b = byPathway[p];
      console.log(`  ${p.padEnd(45)} ${b.conformant}/${b.total}`);
    }
    const warnCount = results.filter(r => r.warnBarePronoun).length;
    if (warnCount) {
      console.log('');
      console.log(`WARN: ${warnCount} file(s) use a bare pronoun inside a cued paragraph (informational, not gating).`);
    }

    if (nonConformant > BACKLOG_CEILING) {
      console.log(`\nworked-example-lint --packs: FAILED - non-conformant count ${nonConformant} exceeds ceiling ${BACKLOG_CEILING}. The backlog may not grow; fix a file and lower BACKLOG_CEILING to match.`);
    } else {
      console.log(`\nworked-example-lint --packs: PASSED (ratchet) - ${nonConformant} non-conformant <= ceiling ${BACKLOG_CEILING}.`);
    }
  }

  process.exit(nonConformant > BACKLOG_CEILING ? 1 : 0);
}

// ── --course mode ────────────────────────────────────────────────────────

function extractComponentText(comp) {
  if (comp.body && comp.body.trim()) return comp.body;
  if (Array.isArray(comp._items)) return comp._items.map(i => i.body || '').join('');
  return '';
}

function runCourseMode(slug, opts) {
  const resolved = resolveCourse(slug, ['courses', 'courses/_generated']);
  if (!resolved.found) {
    console.error(`Course not found for slug "${slug}". Checked:\n  ${resolved.checked.join('\n  ')}`);
    process.exit(1);
  }
  resolved.warnings.forEach(w => console.error(`WARNING: ${w}`));
  if (!resolved.enDir) {
    console.error(`No en/ directory found under ${resolved.courseDir}`);
    process.exit(1);
  }

  const blocks = JSON.parse(fs.readFileSync(path.join(resolved.enDir, 'blocks.json'), 'utf8'));
  const components = JSON.parse(fs.readFileSync(path.join(resolved.enDir, 'components.json'), 'utf8'));
  const namePool = loadNamePool();
  const isMerged = resolved.root === 'courses/_generated';
  const mode = isMerged ? 'merged' : 'tokens';

  const weBlocks = blocks.filter(b => b._skeletonKey === 'worked-example');

  if (!opts.json) {
    console.log(`worked-example-lint --course=${slug}  (resolved under '${resolved.root}', treated as ${isMerged ? 'merged - post-substitution' : 'unmerged - pre-merge tokens expected'})`);
    console.log('='.repeat(60));
  }

  if (weBlocks.length === 0) {
    if (opts.json) {
      console.log(JSON.stringify({ mode: 'course', course: slug, root: resolved.root, merged: isMerged, results: [] }, null, 2));
    } else {
      console.log('No worked-example block found in this course (nothing to check).');
      console.log(`\nworked-example-lint --course=${slug}: PASSED (nothing to check).`);
    }
    process.exit(0);
  }

  const results = [];
  for (const b of weBlocks) {
    const comp = components.find(c => c._parentId === b._id);
    if (!comp) { results.push({ blockId: b._id, componentId: null, pass: false, error: 'no component found for this block' }); continue; }
    const text = extractComponentText(comp);
    const paragraphs = htmlParagraphs(text);
    const r = assess(paragraphs, { namePool, mode });
    // Assertion 0: component type. Checked here, not in assess(), since
    // it is a component-level fact assess() (which only sees paragraphs)
    // has no access to - see header comment.
    r.assertions = { a0_componentType: comp._component === 'workedExample', ...r.assertions };
    r.pass = r.pass && r.assertions.a0_componentType;
    results.push({ blockId: b._id, componentId: comp._id, componentType: comp._component, ...r });
  }

  const failing = results.filter(r => r.error || !r.pass);

  if (opts.json) {
    console.log(JSON.stringify({ mode: 'course', course: slug, root: resolved.root, merged: isMerged, results }, null, 2));
  } else {
    for (const r of results) {
      if (r.error) { console.log(`${r.blockId}: ERROR - ${r.error}`); continue; }
      console.log(`${r.blockId} (${r.componentId}): ${r.pass ? 'PASS' : 'FAIL'}`);
      if (!r.pass) {
        for (const [k, v] of Object.entries(r.assertions)) {
          if (!v) console.log(`    FAIL: ${k}`);
        }
      }
      if (r.warnBarePronoun) console.log('    WARN: bare pronoun inside a cued (we-weaker/we-stronger) paragraph');
    }
    if (failing.length > 0) {
      console.log(`\nworked-example-lint --course=${slug}: FAILED (${failing.length} of ${results.length} worked-example block(s) non-conformant)`);
    } else {
      console.log(`\nworked-example-lint --course=${slug}: PASSED (${results.length} worked-example block(s), all conformant)`);
    }
  }

  process.exit(failing.length > 0 ? 1 : 0);
}

function main() {
  const args = parseArgs();
  if (args.mode === 'packs') runPacksMode(args);
  else runCourseMode(args.course, args);
}

main();
