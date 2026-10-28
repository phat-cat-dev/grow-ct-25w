'use strict';
/**
 * plan-cards.js  —  pathway + tier  →  a plan of content "cards".
 *
 * Adapted from the "read the schema, then emit" shape of ab-map-structure.js,
 * but pointed at the adapt2 engine stores instead of Adapt templates. It reads
 * the engine's grounding + grammar (pathways, tier framing, the lesson
 * skeleton, the book source-map) and produces, for a chosen pathway + tier, the
 * full set of cards to author — each card resolved to its component, its
 * tier-specific agentAuthor brief, and the book chunk that grounds it.
 *
 * Reads only. The prose authoring is a separate pass that consumes this plan.
 * Exports buildPlan() so plan-all.js can batch every pathway × tier.
 *
 * CLI:
 *   node plan-cards.js --list
 *   node plan-cards.js --pathway=<id> --tier=<introductory|intermediate|advanced> [--lessons=N] [--out=plan.json]
 */
const fs = require('fs');
const path = require('path');

const ENGINE = path.resolve(__dirname, '..', 'adapt2-snapshot', '_dev', 'adapt2-engine-snapshot');
const DKB = path.join(ENGINE, 'design-kb');
const read = (p) => JSON.parse(fs.readFileSync(p, 'utf8'));

const TIERS = ['introductory', 'intermediate', 'advanced'];

const pathwaysStore = read(path.join(DKB, 'design-kb.pathways.json'));
const skeletons = read(path.join(DKB, 'design-kb.skeletons.json'));
const book = read(path.join(ENGINE, 'source-kb', 'source-maps', 'book-excelling-at-university-2026.json'));
const bookById = new Map(book.chunks.map(c => [c.id, c]));
const pathways = pathwaysStore.pathways;
const lessonArchetype = skeletons.archetypes.find(a => a.pageType === 'lesson');

const paletteName = (c) => (c || '').replace(/^palette\//, '');
const isGroundable = (p) => !!(p.bookChunks && p.bookChunks.primary && p.bookChunks.primary.length);

function resolveComponent(block) {
  if (block.component && block.component.startsWith('palette/')) return paletteName(block.component);
  const opts = block.slot && block.slot.componentOptions;
  if (Array.isArray(opts) && opts.length) return paletteName(opts[0]);
  return 'text';
}

function resolveTierBrief(block, tier) {
  const aa = block.agentAuthor || {};
  const byTier = aa.context && aa.context.byTier && aa.context.byTier[tier];
  if (byTier && typeof byTier === 'object') {
    if (byTier.applies === false) return { omit: true };
    return { brief: byTier.content || byTier.context || (aa.context && aa.context.all) || aa.content || '', displayTitle: byTier.displayTitle };
  }
  return { brief: byTier || (aa.context && aa.context.all) || aa.content || '' };
}

/** Build the card plan for one pathway + tier. Lessons = the pathway's primary
 *  book chunks that teach a concept (shape content-shapes/concept), one lesson
 *  each (cap with opts.lessons). Each lesson's cards = the lesson skeleton's
 *  blockSequence, tier-resolved and grounded in the lesson's chunk. */
function buildPlan(pathwayId, tier, opts = {}) {
  const pathway = pathways.find(p => p.id === pathwayId);
  if (!pathway) throw new Error(`Unknown pathway "${pathwayId}"`);
  if (!TIERS.includes(tier)) throw new Error(`Unknown tier "${tier}"`);
  if (!isGroundable(pathway)) throw new Error(`Pathway "${pathwayId}" has no primary book chunks (Track B)`);

  const primary = pathway.bookChunks.primary;
  const framing = (pathway.tiers && pathway.tiers[tier]) || {};
  const conceptChunks = primary.map(id => bookById.get(id)).filter(Boolean)
    .filter(c => (c.shapes || []).some(s => s.shapeId === 'content-shapes/concept'));
  const lessonChunks = opts.lessons ? conceptChunks.slice(0, Number(opts.lessons)) : conceptChunks;

  return {
    pathway: pathway.id,
    pathwayName: pathway.name,
    tier,
    focus: framing.focus || null,
    voiceBand: framing.voiceBand || null,
    conceptChunkCount: conceptChunks.length,
    lessons: lessonChunks.map((chunk, i) => ({
      lessonKey: `L${String(i + 1).padStart(2, '0')}`,
      title: chunk.heading,
      grounding: {
        chunkId: chunk.id,
        heading: chunk.heading,
        pages: chunk.locator && chunk.locator.pages,
        shapes: (chunk.shapes || []).map(s => ({ shapeId: s.shapeId, quote: s.quote })),
      },
      cards: lessonArchetype.blockSequence.map(block => {
        const t = resolveTierBrief(block, tier);
        if (t.omit) return null;
        return {
          key: block.key,
          role: block.role,
          kind: block.kind,
          component: resolveComponent(block),
          displayTitle: t.displayTitle || block.displayTitle || block.title,
          tierBrief: t.brief,
          baseContent: (block.agentAuthor && block.agentAuthor.content) || '',
          authoringPrompt: (block.slot && block.slot.authoringPrompt) || null,
        };
      }).filter(Boolean),
    })),
  };
}

module.exports = { buildPlan, pathways, TIERS, isGroundable };

// --------------------------------------------------------------------------- CLI
if (require.main === module) {
  const args = Object.fromEntries(process.argv.slice(2).map(a => {
    const m = a.match(/^--([^=]+)(?:=(.*))?$/);
    return m ? [m[1], m[2] === undefined ? true : m[2]] : [a, true];
  }));

  if (args.list || (!args.pathway && !args.tier)) {
    console.log('Academic-skills pathways:');
    for (const p of pathways) {
      console.log(`  ${String(p.number).padStart(2)}. ${p.id}${isGroundable(p) ? '' : '  (Track B — no book chunks, not groundable)'}`);
    }
    console.log(`\nTiers: ${TIERS.join(', ')}`);
    console.log('\nRun: node plan-cards.js --pathway=<id> --tier=<tier> [--lessons=N] [--out=plan.json]');
    process.exit(0);
  }

  const plan = buildPlan(args.pathway, args.tier, { lessons: args.lessons });
  if (args.out) {
    fs.writeFileSync(args.out, JSON.stringify(plan, null, 2));
    console.log(`[plan] wrote ${args.out}`);
  }
  console.log(`\nPATHWAY  ${plan.pathwayName}  (${plan.pathway})`);
  console.log(`TIER     ${plan.tier}${plan.focus ? '  — ' + plan.focus : ''}`);
  console.log(`LESSONS  ${plan.lessons.length} (of ${plan.conceptChunkCount} concept chunks)   CARDS/lesson ${plan.lessons[0] ? plan.lessons[0].cards.length : 0}`);
  for (const L of plan.lessons) {
    console.log(`\n  ${L.lessonKey}  ${L.title}   [${L.grounding.chunkId}, pp.${L.grounding.pages}]`);
    for (const c of L.cards) {
      console.log(`     - ${c.key.padEnd(20)} ${('(' + c.component + ')').padEnd(16)} ${String(c.tierBrief).slice(0, 72)}`);
    }
  }
  console.log(`\nTotal cards: ${plan.lessons.reduce((n, L) => n + L.cards.length, 0)}`);
}
