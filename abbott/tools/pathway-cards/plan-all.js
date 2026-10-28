'use strict';
/**
 * plan-all.js  —  batch the planner over EVERY groundable pathway × all 3 tiers.
 *
 * Writes one plan JSON per pathway+tier into ./plans/, plus plans/index.json.
 * (Produces the grounded card PLANS; the prose authoring is a separate AI pass.)
 *
 *   node plan-all.js
 */
const fs = require('fs');
const path = require('path');
const { buildPlan, pathways, TIERS, isGroundable } = require('./plan-cards.js');

const outDir = path.join(__dirname, 'plans');
fs.mkdirSync(outDir, { recursive: true });

const index = [];
let written = 0;
let cardsTotal = 0;

for (const p of pathways) {
  if (!isGroundable(p)) {
    index.push({ pathway: p.id, groundable: false, note: 'Track B — no primary book chunks; author directly, not book-grounded' });
    console.log(`  ${p.id.padEnd(42)} — skipped (Track B, not groundable)`);
    continue;
  }
  for (const tier of TIERS) {
    const plan = buildPlan(p.id, tier);
    const file = `${p.id}-${tier}.json`;
    fs.writeFileSync(path.join(outDir, file), JSON.stringify(plan, null, 2));
    const cards = plan.lessons.reduce((n, L) => n + L.cards.length, 0);
    cardsTotal += cards;
    written++;
    index.push({ pathway: p.id, tier, groundable: true, lessons: plan.lessons.length, cards, file: `plans/${file}` });
    console.log(`  ${(p.id + ' / ' + tier).padEnd(54)} → ${String(plan.lessons.length).padStart(2)} lessons, ${String(cards).padStart(3)} cards`);
  }
}

fs.writeFileSync(path.join(outDir, 'index.json'), JSON.stringify({
  generated: new Date().toISOString(),
  pathwaysTotal: pathways.length,
  plansWritten: written,
  cardsTotal,
  plans: index,
}, null, 2));

console.log(`\nWrote ${written} plans (${cardsTotal} cards total) to ${outDir}`);
console.log(`Index: ${path.join(outDir, 'index.json')}`);
