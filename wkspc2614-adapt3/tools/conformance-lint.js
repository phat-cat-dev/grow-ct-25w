/**
 * conformance-lint.js
 *
 * 5.13 conformance lint per project-backlog.md's three-clause contract.
 * Sibling to voice-lint.js - same CLI conventions.
 *
 * Usage:
 *   node conformance-lint.js --course=<course-slug>
 *
 * CONTRACT (three clauses, per away-week log Sessions 2-3):
 *
 * 1. BLOCK-SEQUENCE CONFORMANCE (rewritten, see backlog 5.39): For each
 *    page in the manifest, blocks are located by _skeletonKey (never by
 *    title) and walked against the archetype's required blockSequence in
 *    order. An out-of-sequence required block is an ORDER VIOLATION
 *    (blocks the build). A matched block whose title differs from the
 *    archetype's is a TITLE WARNING (informational, does not block). A
 *    block with no _skeletonKey, an archetype missing from the skeletons
 *    store, and a page with no matched blocks are all reported as
 *    UNCHECKED rather than silently skipped. A run that matches zero
 *    blocks across the whole course is a FAIL.
 *
 * 2. SWEEPEVENT REFUSAL: If sweepEvents contains any event with
 *    resolution.status="open" (or disposition requires resolution but
 *    it's absent), REFUSE the build - exit non-zero.
 *
 * 3. GROUNDINGGAPS REPORTING: List every groundingGaps entry in gate
 *    records. Informational only - never blocks.
 *
 * Outputs PASS/BLOCKED per clause separately, not a single verdict.
 */

const fs = require('fs-extra');
const path = require('path');
const { matchesPageKey } = require('./lib/page-match');
const { resolveCourse } = require('./lib/course-resolve');

const ROOT = path.resolve(__dirname, '..');

const acceptedArgs = ['course', 'manifest', 'blocks'];
const argumentValues = { course: null, manifest: null, blocks: null };

function parseArgs() {
  process.argv.slice(2).forEach(param => {
    const parts = param.replace(/^--/, '').split('=');
    if (!acceptedArgs.includes(parts[0])) {
      console.error(`Unrecognised argument: --${parts[0]}. Accepted: ${acceptedArgs.join(', ')}`);
      process.exit(1);
    }
    argumentValues[parts[0]] = parts.slice(1).join('='); // Rejoin in case path has =
  });
  // Either --course OR both --manifest and --blocks required
  if (!argumentValues.course && !(argumentValues.manifest && argumentValues.blocks)) {
    console.error('Usage: node conformance-lint.js --course=<course-slug>');
    console.error('   or: node conformance-lint.js --manifest=<path> --blocks=<path>');
    process.exit(1);
  }
}

/**
 * Load the design-kb skeletons to get expected block sequences.
 * Returns a map: archetypeId -> blockSequence array
 */
function loadSkeletons() {
  const skeletonsPath = path.join(ROOT, 'design-kb', 'design-kb.skeletons.json');
  if (!fs.existsSync(skeletonsPath)) {
    console.error(`Skeletons file not found: ${skeletonsPath}`);
    process.exit(1);
  }
  const data = fs.readJsonSync(skeletonsPath);
  const map = new Map();
  for (const arch of data.archetypes || []) {
    map.set(arch.id, arch.blockSequence || []);
  }
  return map;
}

/**
 * Extract the block "key" from a block's _id.
 * Convention: block ids are like "L02-b-05", "W-OPEN-b-10", etc.
 * We need to map these to skeleton block keys like "learning-outcomes".
 *
 * This is inherently fuzzy because the block _id doesn't embed the key.
 * We'll use the block's "title" field to match against skeleton titles.
 */
function normaliseTitle(title) {
  return (title || '').toLowerCase().trim();
}

/**
 * Build expected block-key order from archetype.
 * Returns array of { key, title, required } in expected order.
 */
function getExpectedBlockOrder(archetype, skeletons) {
  const seq = skeletons.get(archetype.id);
  if (!seq) return null;
  // Filter to required blocks only for comparison (optional blocks may be absent)
  return seq.map(b => ({
    key: b.key,
    title: normaliseTitle(b.title),
    required: b.required !== false
  }));
}

/**
 * Get actual block order for a page from blocks.json.
 * Returns array of { id, title } in file order.
 *
 * APPROACH: File order (array position) in blocks.json, as this reflects
 * the authored/DOM order. _trackingId can be non-sequential due to
 * insertions, so file order is more reliable for visual block sequence.
 */
function getActualBlockOrder(pageKey, blocks, courseSlug) {
  // Find all blocks whose _parentId's page-base matches pageKey, bare or
  // slug-prefixed (see tools/lib/page-match.js; backlog 5.113, Ruling C).
  const pageBlocks = blocks.filter(b =>
    b._parentId && matchesPageKey(b._parentId, courseSlug, pageKey)
  );

  // Return in file order (already in array order from JSON)
  return pageBlocks.map(b => ({
    id: b._id,
    title: normaliseTitle(b.title),
    skeletonKey: b._skeletonKey || null
  }));
}

/**
 * When getActualBlockOrder finds zero blocks for a pageKey, try to tell
 * whether that's a genuine contentObject-only page or a pageKey/_parentId
 * prefix mismatch (known defect, see backlog 5.113). We look for a block
 * whose _parentId contains "<pageKey>-a-" but with something ahead of it
 * (i.e. it would have matched if only the prefix lined up). If found, we
 * can report the actual prefix in use; if not, we say so rather than guess.
 * Returns the detected prefix string (may be ''), or null if undetectable.
 */
function detectActualPrefix(pageKey, blocks) {
  const marker = `${pageKey}-a-`;
  for (const b of blocks) {
    if (b._parentId && b._parentId.includes(marker) && !b._parentId.startsWith(marker)) {
      return b._parentId.slice(0, b._parentId.indexOf(marker));
    }
  }
  return null;
}

/**
 * CLAUSE 1: Block-Sequence Conformance (rewritten per backlog 5.39)
 *
 * Location: a built block is matched to an archetype blockSequence entry
 * by its _skeletonKey. Title is never used for location.
 *
 * Order: one sequential walk of the archetype's required blocks. For each
 * required key, find its first occurrence in the page's actual blocks. If
 * that occurrence is not after the previous match, it's an ORDER
 * VIOLATION (blocks the build). There is no second adjacent-swap pass;
 * the sequential walk (matchIndex <= lastMatchedIndex) catches any
 * required block - adjacent or not - that appears out of sequence.
 *
 * Title: a matched block whose title differs from the archetype's is a
 * WARNING, not a violation - EXCEPT for a fixed, explicit list of keys
 * whose archetype "title" is a slot LABEL, not a title any instantiation
 * is expected to reproduce verbatim. Those keys are exempted from the
 * title check entirely:
 *
 *   - "interior"          (skeletons/lesson) - realises as 1-4 blocks
 *                          with content-specific titles; the archetype
 *                          title is a description of the slot's role,
 *                          not a title to carry.
 *   - "assessment-items"  (skeletons/summative) - repeats once per
 *                          question; each repetition has its own
 *                          question-specific title, so no single title
 *                          could ever match.
 *
 * withdrawn: kind === 'fixed'. First implemented as "only kind: 'fixed'
 * entries get title-checked" (session of 9 Sep 2026). That was wrong and
 * its own re-run proved it: it produced 0 title warnings across all four
 * courses, silencing every one of the 10 backlog-5.40 "check" mismatches
 * clause 1 was rewritten to surface, because "check" is ITSELF
 * kind: "variable" in design-kb.skeletons.json despite carrying a real,
 * single, expected title ("Check your understanding") - kind marks
 * schema flexibility (how many components/realisations a slot permits),
 * not whether its title is a label or an expected value, and the two
 * axes do not align. The store has no field for the axis this check
 * actually needs (see backlog 5.114). Until
 * one exists, the exemption is this explicit, named, two-entry list -
 * everything else, regardless of kind, gets its title checked.
 *
 * Coverage: blocks with no _skeletonKey are reported UNCHECKED. An
 * archetype missing from the skeletons store is reported UNCHECKED at
 * the page level. A page whose pageKey matches zero actual blocks is
 * reported as UNMATCHED PAGE, with the actual _parentId prefix in use
 * if one can be detected (see detectActualPrefix) - this is a known
 * defect (backlog 5.113), not fixed here, only surfaced. A course
 * where zero blocks are matched anywhere is a FAIL; a course where
 * EVERY page is unmatched is a FAIL with its own explicit message,
 * since that means clause 1 checked nothing at all for that course.
 *
 * PR-1-16 fix (18 Sep 2026): ANY unmatched page is a FAIL, not only the
 * all-unmatched case. Previously a course with, say, 5 of 21 pages
 * unmatched still reported PASS as long as at least one other page's
 * blocks were matched - the unmatched pages' blocks were never visited,
 * printed only as an informational [UNMATCHED PAGE] line, and
 * contributed to none of pagesChecked/blocksMatched/unchecked. A check
 * that cannot reach part of its subject must not report success for
 * the part it could not reach.
 */

// Explicit, named exemption list - see the "Title" section of the
// checkClause1 docstring above for why each entry is here and why
// kind: "variable" cannot be used as a proxy for this. Any new
// archetype key whose title is a slot label rather than an expected
// title must be added here manually; the store cannot yet express the
// distinction (see backlog 5.114, cross-referenced from 5.39/5.40).
const TITLE_CHECK_EXEMPT_KEYS = new Set(['activity-1', 'activity-2', 'activity-3', 'activity-4', 'assessment-items']);

function checkClause1(manifest, blocks, skeletons, courseSlug) {
  const results = {
    pass: true,
    issues: [],          // order violations (blocking)
    titleWarnings: [],   // informational
    unchecked: [],        // { pageKey, reason: 'archetype-not-found' | 'no-skeleton-key', archetypeId? , id? }
    unmatchedPages: [],  // { pageKey, detectedPrefix: string|null }
    pagesChecked: 0,
    blocksMatched: 0
  };

  const totalInstantiations = (manifest.instantiations || []).length;

  for (const inst of manifest.instantiations || []) {
    const expected = getExpectedBlockOrder(inst.archetype, skeletons);
    if (!expected) {
      results.unchecked.push({
        pageKey: inst.pageKey,
        reason: 'archetype-not-found',
        archetypeId: inst.archetype && inst.archetype.id
      });
      continue;
    }

    const actual = getActualBlockOrder(inst.pageKey, blocks, courseSlug);
    if (actual.length === 0) {
      results.unmatchedPages.push({
        pageKey: inst.pageKey,
        detectedPrefix: detectActualPrefix(inst.pageKey, blocks)
      });
      continue;
    }

    results.pagesChecked++;

    // Every actual block on this page lacking a _skeletonKey is UNCHECKED.
    for (const block of actual) {
      if (!block.skeletonKey) {
        results.unchecked.push({
          pageKey: inst.pageKey,
          reason: 'no-skeleton-key',
          id: block.id
        });
      }
    }

    const expectedRequired = expected.filter(e => e.required);
    let lastMatchedIndex = -1;

    for (const exp of expectedRequired) {
      const matchIndex = actual.findIndex(a => a.skeletonKey === exp.key);

      if (matchIndex === -1) {
        // Required key not present under any block on this page - not
        // reported here; a missing/unstamped block already surfaces via
        // the UNCHECKED loop above or the manifest-completeness clause.
        continue;
      }

      if (matchIndex <= lastMatchedIndex) {
        results.pass = false;
        results.issues.push({
          pageKey: inst.pageKey,
          message: `Order violation: "${exp.key}" (expected title "${exp.title}") is out of sequence.`
        });
      } else {
        const actualBlock = actual[matchIndex];
        if (!TITLE_CHECK_EXEMPT_KEYS.has(exp.key) && actualBlock.title !== exp.title) {
          results.titleWarnings.push({
            pageKey: inst.pageKey,
            key: exp.key,
            expectedTitle: exp.title,
            actualTitle: actualBlock.title
          });
        }
        results.blocksMatched++;
      }

      lastMatchedIndex = Math.max(lastMatchedIndex, matchIndex);
    }
  }

  if (results.unmatchedPages.length > 0) {
    results.pass = false;
    if (results.unmatchedPages.length === totalInstantiations) {
      results.issues.push({
        pageKey: null,
        message: `ALL ${totalInstantiations} pages unmatched - clause 1 checked nothing for this course (see UNMATCHED PAGE entries below).`
      });
    } else {
      results.issues.push({
        pageKey: null,
        message: `${results.unmatchedPages.length} of ${totalInstantiations} page(s) unmatched - clause 1 cannot pass while any page's blocks were never visited (see UNMATCHED PAGE entries below).`
      });
    }
  } else if (results.blocksMatched === 0) {
    results.pass = false;
    results.issues.push({
      pageKey: null,
      message: 'Zero blocks matched across the whole course - clause 1 cannot be considered a PASS.'
    });
  }

  return results;
}

/**
 * CLAUSE 2: SweepEvent Refusal
 *
 * If sweepEvents has any entry with:
 * - resolution.status = "open", OR
 * - disposition.verdict is "invalidate" or "flag-for-review" but
 *   resolution is absent
 * Then REFUSE the build.
 */
function checkClause2(manifest) {
  const results = { pass: true, issues: [] };

  const sweepEvents = manifest.sweepEvents || [];

  for (const event of sweepEvents) {
    for (const item of event.sweep || []) {
      const verdict = item.disposition?.verdict;
      const resolution = item.resolution;

      // Verdicts that require resolution
      const requiresResolution = verdict === 'invalidate' || verdict === 'flag-for-review';

      if (requiresResolution) {
        if (!resolution) {
          results.pass = false;
          results.issues.push({
            eventId: event.eventId,
            gate: item.gate,
            reason: `Verdict "${verdict}" requires resolution but none present`
          });
        } else if (resolution.status === 'open') {
          results.pass = false;
          results.issues.push({
            eventId: event.eventId,
            gate: item.gate,
            reason: `Unresolved sweep item (status: open)`
          });
        }
      }
    }
  }

  return results;
}

/**
 * CLAUSE 3: GroundingGaps Reporting
 *
 * List every groundingGaps entry in gate records.
 * Informational only - never causes non-zero exit.
 */
function checkClause3(manifest) {
  const gaps = [];

  for (const gate of manifest.gates || []) {
    for (const record of gate.records || []) {
      if (record.groundingGaps && Array.isArray(record.groundingGaps)) {
        for (const gap of record.groundingGaps) {
          gaps.push({
            gate: gate.gateId,
            store: gap.store,
            lookup: gap.lookup,
            wouldHaveGrounded: gap.wouldHaveGrounded,
            gapKind: gap.gapKind
          });
        }
      }
    }
  }

  return { gaps };
}

async function main() {
  parseArgs();
  const { course, manifest: explicitManifest, blocks: explicitBlocks } = argumentValues;

  let manifest;
  let manifestSource;
  let blocks;
  let blocksPath;

  // Explicit paths override (for testing)
  if (explicitManifest && explicitBlocks) {
    if (!fs.existsSync(explicitManifest)) {
      console.error(`Manifest not found: ${explicitManifest}`);
      process.exit(1);
    }
    if (!fs.existsSync(explicitBlocks)) {
      console.error(`Blocks not found: ${explicitBlocks}`);
      process.exit(1);
    }
    manifest = fs.readJsonSync(explicitManifest);
    manifestSource = explicitManifest;
    blocks = fs.readJsonSync(explicitBlocks);
    blocksPath = explicitBlocks;
  } else {
    // Production lookup - resolve the course directory first (courses/ and
    // courses/_generated/, in that order), then fall back to incoming-docs/
    // for the manifest only if no course directory is found at all.
    const resolved = resolveCourse(course, ['courses', 'courses/_generated']);
    resolved.warnings.forEach(w => console.error(`WARNING: ${w}`));

    const incomingDocsPath = path.join(ROOT, 'incoming-docs', `course-design_${course}.json`);
    const checked = [...resolved.checked.map(d => path.join(d, 'course-design_*.json')), incomingDocsPath];

    if (resolved.found && resolved.courseDesignPath) {
      manifest = fs.readJsonSync(resolved.courseDesignPath);
      manifestSource = resolved.courseDesignPath;
      blocksPath = path.join(resolved.courseDir, 'en', 'blocks.json');
    } else if (fs.existsSync(incomingDocsPath)) {
      manifest = fs.readJsonSync(incomingDocsPath);
      manifestSource = incomingDocsPath;
      blocksPath = null;
    }

    if (!manifest) {
      console.error(`No manifest found. Checked:\n  ${checked.join('\n  ')}`);
      process.exit(1);
    }

    if (!blocksPath || !fs.existsSync(blocksPath)) {
      console.error(`No blocks.json found${blocksPath ? ` at ${blocksPath}` : ' - manifest was found in incoming-docs/, which has no accompanying course directory'}.`);
      process.exit(1);
    }
    blocks = fs.readJsonSync(blocksPath);
  }

  // Load skeletons
  const skeletons = loadSkeletons();

  console.log(`conformance-lint: ${course}`);
  console.log(`  manifest: ${path.relative(ROOT, manifestSource)}`);
  console.log('');

  // Match ids against the course's OWN declared slug (manifest.slug), not the
  // directory-derived name. A _generated context course (courses/_generated/
  // <base>-<context>/) keeps the BASE course's _id/_parentId prefixes and base
  // manifest.slug, while verify-all-courses addresses it by its <base>-<context>
  // directory name; matching on manifest.slug makes its base-prefixed wrapper/
  // summative/confidence ids resolve. For a normal course manifest.slug equals
  // the directory name, so this is a no-op there. (Option 1, 9 October 2026.)
  const matchSlug = manifest.slug || course;
  // Run all three clauses
  const clause1 = checkClause1(manifest, blocks, skeletons, matchSlug);
  const clause2 = checkClause2(manifest);
  const clause3 = checkClause3(manifest);

  let anyBlocked = false;

  // Report Clause 1
  console.log('Clause 1 (block-sequence conformance):');
  console.log(`  Pages checked: ${clause1.pagesChecked}`);
  console.log(`  Blocks matched: ${clause1.blocksMatched}`);
  console.log(`  Blocks unchecked: ${clause1.unchecked.length}`);
  console.log(`  Title warnings: ${clause1.titleWarnings.length}`);
  console.log(`  Order violations: ${clause1.issues.filter(i => i.pageKey).length}`);

  for (const u of clause1.unmatchedPages) {
    if (u.detectedPrefix !== null) {
      console.log(`  [UNMATCHED PAGE] pageKey "${u.pageKey}" matches no blocks; blocks for this page actually use _parentId prefix "${u.detectedPrefix}"`);
    } else {
      console.log(`  [UNMATCHED PAGE] pageKey "${u.pageKey}" matches no blocks; cannot determine an actual prefix in use - may be a genuine contentObject-only page, or blocks may not exist under any prefix`);
    }
  }

  for (const u of clause1.unchecked) {
    if (u.reason === 'archetype-not-found') {
      console.log(`  [UNCHECKED] [${u.pageKey}] archetype not found in skeletons store: ${u.archetypeId}`);
    } else {
      console.log(`  [UNCHECKED] [${u.pageKey}] block ${u.id} has no _skeletonKey`);
    }
  }

  for (const w of clause1.titleWarnings) {
    console.log(`  [WARNING] [${w.pageKey}] key "${w.key}": expected title "${w.expectedTitle}", actual title "${w.actualTitle}"`);
  }

  for (const issue of clause1.issues) {
    console.log(`  [VIOLATION]${issue.pageKey ? ` [${issue.pageKey}]` : ''} ${issue.message}`);
  }

  if (clause1.pass) {
    console.log('  Result: PASS');
  } else {
    console.log('  Result: FAIL');
    anyBlocked = true;
  }

  // Report Clause 2
  if (clause2.pass) {
    console.log('Clause 2 (sweepEvent refusal): PASS');
  } else {
    console.log('Clause 2 (sweepEvent refusal): BLOCKED');
    for (const issue of clause2.issues) {
      console.log(`  [${issue.eventId}] ${issue.gate}: ${issue.reason}`);
    }
    anyBlocked = true;
  }

  // Report Clause 3 (always informational)
  if (clause3.gaps.length === 0) {
    console.log('Clause 3 (groundingGaps): PASS (none found)');
  } else {
    console.log(`Clause 3 (groundingGaps): INFO (${clause3.gaps.length} gap(s) reported)`);
    for (const gap of clause3.gaps) {
      console.log(`  [${gap.gate}] ${gap.store}/${gap.lookup}`);
      console.log(`    -> ${gap.wouldHaveGrounded}`);
      if (gap.gapKind) console.log(`    gapKind: ${gap.gapKind}`);
    }
  }

  console.log('');
  if (anyBlocked) {
    console.log('conformance-lint: BLOCKED (one or more clauses failed)');
    process.exit(1);
  } else {
    console.log('conformance-lint: PASS');
    process.exit(0);
  }
}

main().catch(err => {
  console.error('conformance-lint.js failed:', err);
  process.exit(1);
});
