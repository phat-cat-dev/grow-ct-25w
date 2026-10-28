#!/usr/bin/env node
// EXPERIMENT — first "knowledge -> component data object" generator:
// pathway capabilities  ->  a growLevels component data object (a tier ladder),
// pitched to the resolved level (level.js). Reads real knowledge data, writes a
// sample component instance. Not wired into the build.
const fs = require('fs'), path = require('path');
const { resolveLevel } = require('./level.js');
const ROOT = path.resolve(__dirname, '..');
const rd = p => JSON.parse(fs.readFileSync(path.join(ROOT, p), 'utf8'));

const PATHWAY = 'ai-technology';
const ref = rd(`catalogue/context/pathway/${PATHWAY}.json`);
const facing = rd('catalogue/context/pathway-student-facing.json').pathways[PATHWAY] || [];
const caps = (ref.capabilities || []).filter(c => c.statement);

// student-facing "you can…" matched to a capability by tier + fheqLevel
const sf = (tier, L) => {
  const m = facing.find(f => f.tier === tier && f.fheqLevel === L);
  return m ? m.studentFacing : '';
};
const TONES = ['restricted', 'guarded', 'open']; // low -> high rung

// Build a growLevels ladder from a set of capabilities (already ordered low->high).
function ladder({ title, instruction, rungs }) {
  return {
    _component: 'growLevels',
    _id: 'exp-growlevels',
    title: '', displayTitle: title, body: '', instruction,
    _items: rungs.map((c, i) => ({
      _tone: TONES[Math.min(i, TONES.length - 1)],
      title: `L${c.fheqLevel} — ${c.statement}`,
      body: sf(c.tier, c.fheqLevel) || c.statement,
      advice: `In practice, this means ${lowerFirst(sf(c.tier, c.fheqLevel) || c.statement).replace(/^you /, 'you ')}`
    }))
  };
}
const lowerFirst = s => s ? s[0].toLowerCase() + s.slice(1) : s;

// (1) PITCH path — the resolved tier's 3 capabilities become a 3-rung ladder.
function byTier(level) {
  const tier = level.resolvedTier;
  const rungs = caps.filter(c => c.tier === tier).sort((a, b) => a.fheqLevel - b.fheqLevel);
  return ladder({
    title: `${cap(tier)}: what you can do, level by level`,
    instruction: `This ${tier} course builds across ${rungs.length} levels. Open each to see what it means in practice.`,
    rungs
  });
}
// (2) EXPLICIT-L path — capabilities AT the resolved FHEQ level, across tiers
// (the finer targeting the explicit L enables when pitch is none).
function byExplicitL(level) {
  const L = level.resolvedFheq;
  const rungs = caps.filter(c => c.fheqLevel === L).sort((a, b) => a.tier.localeCompare(b.tier));
  return ladder({
    title: `Working at FHEQ level ${L}`,
    instruction: `These are the level-${L} capabilities for this pathway.`,
    rungs
  });
}
const cap = s => s ? s[0].toUpperCase() + s.slice(1) : s;

const demos = {
  'pitch=introductory': byTier(resolveLevel({ pitch: 'introductory' })),
  'pitch=none,explicitL=5': byExplicitL(resolveLevel({ pitch: 'none', explicitL: 'fheq:5' }))
};

fs.writeFileSync(path.join(__dirname, 'growlevels-sample.json'), JSON.stringify(demos, null, 2) + '\n');
console.log('pathway:', PATHWAY, '| capabilities:', caps.length);
for (const [k, v] of Object.entries(demos)) {
  console.log(`\n### ${k}  ->  growLevels "${v.displayTitle}" (${v._items.length} rungs)`);
  v._items.forEach(it => console.log(`   [${it._tone}] ${it.title}\n        advice: ${it.advice}`));
}
console.log('\nwrote gate-experiment/growlevels-sample.json');
