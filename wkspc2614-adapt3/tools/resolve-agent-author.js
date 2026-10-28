#!/usr/bin/env node
/**
 * resolve-agent-author.js — the agentAuthor CONSUMER.
 *
 * Given a skeleton slot's agentAuthor block and the ACTIVE facets of a course
 * (tier, and later subject / qualifiers / institution) plus the authoring mode,
 * it composes the single effective instruction the authoring agent should follow
 * for that slot.
 *
 * THE ACTIVATION RULE (why the agent does not read every steer):
 *   A context steer applies ONLY when its key matches a facet that is ACTIVE for
 *   this course. The agent never walks all of byQualifier/bySubject/byInstitution;
 *   it reads the entry whose flag is actually set. So:
 *     - byTier[tier]            applies to EVERY course (every course has a tier) -> live now.
 *     - bySubject[cahGrouping]  applies only once CXS sets the grouping facet.
 *     - byQualifier[q]          applies only for each qualifier the CXP/CSP set.
 *     - byInstitution[inst]     applies only when an institution facet is set.
 *   An empty steer ({}), or a steer with no entry matching an active facet,
 *   contributes nothing - it is a ready placeholder, not an instruction.
 *
 * COMPOSITION (most-specific wins for directive scalars; lists accumulate):
 *   baseline (content/relation/warnings/bestPractice)
 *     -> context.all
 *       -> context.byTier[tier]
 *         -> context.bySubject[subject]
 *           -> context.byQualifier[q]  (each active qualifier, in order)
 *             -> context.byInstitution[institution]
 *               -> agentAuthor{Written|Dialogue}.notes   (active mode)
 *   - scalar directive fields (content, relation, context, displayTitle, sideways,
 *     forwardBack, note) are OVERRIDDEN by the most specific level that sets them;
 *   - warnings and bestPractice ACCUMULATE (union, de-duplicated);
 *   - if any applied steer entry has applies:false, the block is OMITTED.
 *
 *   node tools/resolve-agent-author.js --archetype=skeletons/lesson --slot=check \
 *        --tier=introductory --mode=written [--subject=CAH ... --qualifier=x --institution=y]
 *   node tools/resolve-agent-author.js --archetype=... --slot=... --manifest=courses/<slug>/course-design_<slug>.json
 *        (reads the tier from the manifest facetSet)
 */
'use strict';
const fs = require('fs');
const path = require('path');

function findRoot(s) { let d = s; for (let i = 0; i < 10; i++) { if (fs.existsSync(path.join(d, 'Gruntfile.js'))) return d; const u = path.dirname(d); if (u === d) break; d = u; } return s; }
const ROOT = findRoot(fs.existsSync(path.join(process.cwd(), 'Gruntfile.js')) ? process.cwd() : __dirname);
const SKELETONS = path.join(ROOT, 'design-kb', 'design-kb.skeletons.json');

const SCALARS = ['displayTitle', 'content', 'context', 'relation', 'sideways', 'forwardBack', 'note'];

// a steer entry is a string (shorthand for {content}) or an object
function asEntry(v) { return typeof v === 'string' ? { content: v } : (v || {}); }

/**
 * Resolve the effective agentAuthor for one slot.
 * @param block      the skeleton block (carries agentAuthor / agentAuthorWritten / agentAuthorDialogue)
 * @param facets     { tier, subject, qualifiers:[], institution }
 * @param mode       'written' | 'dialogue'
 * Returns { omit, applied:[levels], displayTitle, content, context, relation,
 *           sideways, forwardBack, note, warnings:[], bestPractice:[], modeNotes:[] }
 */
function resolveAgentAuthor(block, facets = {}, mode = 'written') {
  const aa = block.agentAuthor;
  const out = { omit: false, applied: [], warnings: [], bestPractice: [], modeNotes: [] };
  if (aa === undefined) return out;
  const a = typeof aa === 'string' ? { content: aa } : aa;

  // the ordered list of active layers (least -> most specific)
  const layers = [];
  layers.push(['baseline', { content: a.content, relation: a.relation, warnings: a.warnings, bestPractice: a.bestPractice }]);
  const ctx = (a.context && typeof a.context === 'object') ? a.context
    : (typeof a.context === 'string' ? { all: a.context } : {});
  if (ctx.all != null) layers.push(['context.all', { context: ctx.all }]);
  if (facets.tier && ctx.byTier && ctx.byTier[facets.tier] != null)
    layers.push([`byTier.${facets.tier}`, asEntry(ctx.byTier[facets.tier])]);
  if (facets.subject && ctx.bySubject && ctx.bySubject[facets.subject] != null)
    layers.push([`bySubject.${facets.subject}`, asEntry(ctx.bySubject[facets.subject])]);
  for (const q of (facets.qualifiers || []))
    if (ctx.byQualifier && ctx.byQualifier[q] != null) layers.push([`byQualifier.${q}`, asEntry(ctx.byQualifier[q])]);
  if (facets.institution && ctx.byInstitution && ctx.byInstitution[facets.institution] != null)
    layers.push([`byInstitution.${facets.institution}`, asEntry(ctx.byInstitution[facets.institution])]);

  const seen = new Set();
  for (const [name, layer] of layers) {
    if (!layer || Object.keys(layer).length === 0) continue;
    if (layer.applies === false) { out.omit = true; out.applied.push(name + ' (applies:false -> OMIT)'); continue; }
    let touched = false;
    for (const k of SCALARS) if (layer[k] != null) { out[k] = layer[k]; touched = true; }
    for (const w of (layer.warnings || [])) if (!seen.has('w:' + w)) { out.warnings.push(w); seen.add('w:' + w); touched = true; }
    for (const bp of (layer.bestPractice || [])) if (!seen.has('b:' + bp)) { out.bestPractice.push(bp); seen.add('b:' + bp); touched = true; }
    if (touched || name.startsWith('byTier') || name.startsWith('by')) out.applied.push(name);
  }

  // mode notes last
  const modeBlock = mode === 'dialogue' ? block.agentAuthorDialogue : block.agentAuthorWritten;
  if (modeBlock && Array.isArray(modeBlock.notes)) { out.modeNotes = modeBlock.notes.slice(); if (modeBlock.notes.length) out.applied.push(`mode:${mode}`); }
  return out;
}

function findBlock(skeletons, archetypeId, slotKey) {
  const a = skeletons.archetypes.find(x => x.id === archetypeId);
  if (!a) throw new Error(`archetype not found: ${archetypeId}`);
  const b = (a.blockSequence || []).find(x => x.key === slotKey);
  if (!b) throw new Error(`slot not found: ${slotKey} in ${archetypeId}`);
  return b;
}

if (require.main === module) {
  const args = Object.fromEntries(process.argv.slice(2).map(a => { const m = a.replace(/^--/, '').split('='); return [m[0], m[1] ?? true]; }));
  const skeletons = JSON.parse(fs.readFileSync(SKELETONS, 'utf8'));
  let tier = args.tier;
  if (!tier && args.manifest) {
    const man = JSON.parse(fs.readFileSync(path.resolve(ROOT, args.manifest), 'utf8'));
    tier = man.facetSet && man.facetSet.tier;
  }
  const facets = { tier, subject: args.subject, institution: args.institution,
    qualifiers: args.qualifier ? [].concat(args.qualifier) : [] };
  const block = findBlock(skeletons, args.archetype, args.slot);
  const res = resolveAgentAuthor(block, facets, args.mode || 'written');
  console.log(JSON.stringify({ archetype: args.archetype, slot: args.slot, facets, mode: args.mode || 'written', resolved: res }, null, 2));
}

module.exports = { resolveAgentAuthor, findBlock };
