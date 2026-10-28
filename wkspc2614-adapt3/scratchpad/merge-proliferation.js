// Merge the 4 proliferation outputs into the student-facing store: confirmed 9 (identified)
// + new 9 (proliferated, drafted) = 18 per pathway. Asserts coverage, then writes in place.
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..');
const storePath = path.join(ROOT, 'catalogue/context/pathway-student-facing.json');
const store = JSON.parse(fs.readFileSync(storePath, 'utf8'));

const prolif = {};
for (const n of [1, 2, 3, 4]) {
  const p = JSON.parse(fs.readFileSync(path.join(__dirname, `prolif-${n}.json`), 'utf8'));
  for (const slug of Object.keys(p)) prolif[slug] = p[slug];
}

const problems = [];
let addedTotal = 0;
for (const slug of Object.keys(store.pathways)) {
  const existing = store.pathways[slug];
  existing.forEach(e => { if (!e.origin) e.origin = 'identified'; if (!e.status) e.status = 'confirmed'; });
  const neu = prolif[slug];
  if (!neu) { problems.push(`${slug}: NO proliferated set`); continue; }
  if (neu.length !== 9) problems.push(`${slug}: expected 9 new, got ${neu.length}`);
  const tierCount = {};
  const seen = new Set(existing.map(e => e.id));
  for (const b of neu) {
    tierCount[b.tier] = (tierCount[b.tier] || 0) + 1;
    if (seen.has(b.id)) problems.push(`${slug}: new id ${b.id} collides with existing`);
    seen.add(b.id);
    b.origin = 'proliferated';
    b.status = 'drafted';
  }
  for (const t of ['introductory', 'intermediate', 'advanced']) {
    if ((tierCount[t] || 0) !== 3) problems.push(`${slug}: ${t} has ${tierCount[t] || 0} new (want 3)`);
  }
  store.pathways[slug] = existing.concat(neu);
  addedTotal += neu.length;
}
// pathways present in prolif but not store?
for (const slug of Object.keys(prolif)) if (!store.pathways[slug]) problems.push(`prolif has unknown pathway ${slug}`);

const total = Object.values(store.pathways).reduce((a, b) => a + b.length, 0);
const perPathway = Object.fromEntries(Object.entries(store.pathways).map(([k, v]) => [k, v.length]));
console.log('pathways:', Object.keys(store.pathways).length, '| total benchmarks:', total, '| new added:', addedTotal);
console.log('per-pathway sizes:', JSON.stringify(perPathway));
if (problems.length) { console.log('PROBLEMS:\n  ' + problems.join('\n  ')); process.exit(1); }
if (!Object.values(perPathway).every(n => n === 18)) { console.log('NOT all 18'); process.exit(1); }

store.note = store.note.replace(/First move of the 9->18 benchmark proliferation[^.]*\. /, '')
  + ' PROLIFERATED: each pathway now carries 18 (6/tier) -- the confirmed 9 (origin:identified) plus 9 new (origin:proliferated, status:drafted) drawn from each tier\'s tierProgression.levels skills/understandings (blurryTop on the top rung of each tier).';
store.status = 'mixed (identified=confirmed, proliferated=drafted)';
store.proliferatedGenerated = new Date().toISOString().slice(0, 10);

fs.writeFileSync(storePath, JSON.stringify(store, null, 2) + '\n');
console.log('OK -> catalogue/context/pathway-student-facing.json (18 per pathway)');
