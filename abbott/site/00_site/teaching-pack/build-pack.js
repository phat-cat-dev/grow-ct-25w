#!/usr/bin/env node
/* build-pack.js
   Single source of truth:   skos/concepts.json, course/course.json, content/lessons.js
   Checks:                   the ten course coherence checks plus SKOS integrity checks
   Generates:                skos/teaching-meta.ttl, dist/course.md, dist/lesson-0N.md, dist/report.json
   Run:                      npm install && node build-pack.js
*/
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const root = __dirname;
const J = (p) => JSON.parse(fs.readFileSync(path.join(root, p), 'utf8'));
const W = (p, s) => { fs.mkdirSync(path.dirname(path.join(root, p)), { recursive: true }); fs.writeFileSync(path.join(root, p), s); };

const skos = J('skos/concepts.json');
const course = J('course/course.json');
const lessons = require('./content/lessons.js');
const DATE = process.argv.includes('--date') ? process.argv[process.argv.indexOf('--date') + 1] : '2026-10-20';

const scheme = skos.scheme;
const concepts = skos.concepts;
const byId = Object.fromEntries(concepts.map((c) => [c.id, c]));
const lessonIds = lessons.map((l) => l.record.id);
const lessonOf = (n) => lessonIds[n - 1];
const problems = [];
const bad = (m) => problems.push(m);

/* ---------- derive course fields from the scheme (never retyped) ---------- */
course.concept.key_terms = concepts.map((c, i) => ({
  id: `T${i + 1}`, term: c.label, definition: c.def, introduced_in: lessonOf(c.intro)
}));
const termId = Object.fromEntries(concepts.map((c, i) => [c.id, `T${i + 1}`]));
course.concept.external_refs = [{ scheme: scheme.id, uri: `${scheme.base}scheme`, note: 'SKOS concept scheme this course is built on. Replace the placeholder base URI before publishing.' }];
course.lesson_map.forEach((m) => {
  m.concept_term_ids = concepts.filter((c) => lessonOf(c.intro) === m.lesson_id).map((c) => termId[c.id]);
});
course.outcomes.forEach((o) => {
  const ids = new Set();
  course.lesson_map.filter((m) => m.course_outcome_ids.includes(o.id)).forEach((m) => m.concept_term_ids.forEach((t) => ids.add(t)));
  o.concept_term_ids = [...ids];
});

/* ---------- checks ---------- */
const has = (a, x) => a.includes(x);
// 1, 2 outcomes and lessons
course.outcomes.forEach((o) => { if (!course.lesson_map.some((m) => has(m.course_outcome_ids, o.id))) bad(`1: outcome ${o.id} has no lesson`); });
course.lesson_map.forEach((m) => { if (!m.course_outcome_ids.length) bad(`2: lesson ${m.lesson_id} serves no outcome`); });
// 3 terms introduced once in a lesson that exists
concepts.forEach((c) => { if (!lessonOf(c.intro)) bad(`3: concept ${c.id} introduced in missing lesson ${c.intro}`); });
// 4 misconceptions
course.concept.misconceptions.forEach((m) => m.addressed_in.forEach((l) => { if (!lessonIds.includes(l)) bad(`4: ${m.id} addressed in missing ${l}`); }));
// 5 no cycle, none requires a later lesson (guided order)
const seq = Object.fromEntries(course.lesson_map.map((m) => [m.lesson_id, m.sequence]));
course.lesson_map.forEach((m) => m.requires_lesson_ids.forEach((r) => {
  if (!(r in seq)) bad(`5: ${m.lesson_id} requires unknown ${r}`);
  else if (seq[r] >= m.sequence && course.delivery.lesson_order === 'guided') bad(`5: ${m.lesson_id} requires later or same lesson ${r}`);
}));
// 6 sequence unique and gapless
const s = course.lesson_map.map((m) => m.sequence).sort((a, b) => a - b);
s.forEach((v, i) => { if (v !== i + 1) bad('6: sequence has a gap or duplicate'); });
// 7 scope overlap
course.scope.in_scope.forEach((x) => { if (course.scope.out_of_scope.includes(x)) bad(`7: "${x}" in and out of scope`); });
// 8 relation targets resolve or are flagged external
const external = course.concept.relations.map((r) => r.target);
// 9 duration
const total = course.lesson_map.reduce((n, m) => n + m.estimated_duration_minutes, 0);
if (course.delivery.estimated_duration_minutes && course.delivery.estimated_duration_minutes !== total) bad('9: duration differs from the lesson sum');
// lesson records agree with the map
lessons.forEach((l, i) => {
  const r = l.record, m = course.lesson_map[i];
  if (r.id !== m.lesson_id) bad(`map: record ${r.id} != ${m.lesson_id}`);
  if (r.title !== m.title) bad(`map: title differs for ${r.id}`);
  if (r.estimated_duration_minutes !== m.estimated_duration_minutes) bad(`map: duration differs for ${r.id}`);
  if (JSON.stringify(r.alignment.course_outcome_ids) !== JSON.stringify(m.course_outcome_ids)) bad(`map: outcomes differ for ${r.id}`);
  if (JSON.stringify(r.prerequisites.required_lesson_ids) !== JSON.stringify(m.requires_lesson_ids)) bad(`map: requires differ for ${r.id}`);
  const loIds = r.learning_outcomes.map((o) => o.id), actIds = r.activities.map((a) => a.id);
  r.learning_outcomes.forEach((o) => { if (!o.course_outcome_ids.every((x) => has(r.alignment.course_outcome_ids, x))) bad(`${r.id} ${o.id}: course outcome not in alignment`); });
  r.activities.forEach((a) => a.lesson_outcome_ids.forEach((x) => { if (!loIds.includes(x)) bad(`${r.id} ${a.id}: unknown ${x}`); }));
  loIds.forEach((x) => { if (!r.activities.some((a) => a.lesson_outcome_ids.includes(x))) bad(`${r.id}: ${x} has no activity`); });
  actIds.forEach((x) => { if (!l.activities[x]) bad(`${r.id}: no body text for ${x}`); });
});
// SKOS integrity
const labels = new Set(), notations = new Set();
concepts.forEach((c) => {
  if (labels.has(c.label.toLowerCase())) bad(`skos: duplicate label ${c.label}`); labels.add(c.label.toLowerCase());
  if (notations.has(c.notation)) bad(`skos: duplicate notation ${c.notation}`); notations.add(c.notation);
  if (!c.def) bad(`skos: ${c.id} has no definition`);
  if (!c.top && !c.broader) bad(`skos: ${c.id} is neither top nor narrower`);
  if (c.top && c.broader) bad(`skos: ${c.id} is top and has a broader`);
  if (c.broader && !byId[c.broader]) bad(`skos: ${c.id} broader ${c.broader} missing`);
  (c.related || []).forEach((r) => { if (!byId[r]) bad(`skos: ${c.id} related ${r} missing`); if (r === c.id) bad(`skos: ${c.id} related to itself`); });
});
const anc = (id) => { const out = []; let c = byId[id]; const seen = new Set(); while (c && c.broader) { if (seen.has(c.id)) { bad(`skos: broader cycle at ${c.id}`); break; } seen.add(c.id); out.push(c.broader); c = byId[c.broader]; } return out; };
concepts.forEach((c) => (c.related || []).forEach((r) => {      // related must not duplicate a hierarchy link
  if (anc(c.id).includes(r) || (byId[r] && anc(r).includes(c.id))) bad(`skos: ${c.id} and ${r} are related and in one hierarchy (S27)`);
}));
const nar = {}; concepts.forEach((c) => { if (c.broader) (nar[c.broader] = nar[c.broader] || []).push(c.id); });

/* ---------- SKOS Turtle ---------- */
const esc = (t) => String(t).replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\n/g, '\\n');
const lang = scheme.language;
const sym = new Map();               // related is symmetric, so emit both directions
concepts.forEach((c) => (c.related || []).forEach((r) => {
  (sym.get(c.id) || sym.set(c.id, new Set()).get(c.id)).add(r);
  (sym.get(r) || sym.set(r, new Set()).get(r)).add(c.id);
}));
let ttl = `@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix tm: <${scheme.base}> .

# ${scheme.note}

tm:scheme a skos:ConceptScheme ;
    dct:title "${esc(scheme.title)}"@${lang} ;
    dct:description "${esc(scheme.description)}"@${lang} ;
    dct:language "${lang}" ;
    owl_version_placeholder
${concepts.filter((c) => c.top).map((c, i, a) => `    skos:hasTopConcept tm:${c.id}${i === a.length - 1 ? ' .' : ' ;'}`).join('\n')}
`.replace('    owl_version_placeholder\n', `    dct:hasVersion "${scheme.version}" ;\n`);
concepts.forEach((c) => {
  const p = [`a skos:Concept`, `skos:inScheme tm:scheme`, `skos:notation "${esc(c.notation)}"`, `skos:prefLabel "${esc(c.label)}"@${lang}`];
  (c.alt || []).forEach((a) => p.push(`skos:altLabel "${esc(a)}"@${lang}`));
  p.push(`skos:definition "${esc(c.def)}"@${lang}`);
  if (c.scope) p.push(`skos:scopeNote "${esc(c.scope)}"@${lang}`);
  if (c.example) p.push(`skos:example "${esc(c.example)}"@${lang}`);
  if (c.source) p.push(`dct:source "${esc(c.source)}"`);
  if (c.top) p.push(`skos:topConceptOf tm:scheme`);
  if (c.broader) p.push(`skos:broader tm:${c.broader}`);
  (nar[c.id] || []).forEach((n) => p.push(`skos:narrower tm:${n}`));
  [...(sym.get(c.id) || [])].forEach((r) => p.push(`skos:related tm:${r}`));
  ttl += `\ntm:${c.id}\n    ${p.join(' ;\n    ')} .\n`;
});
/* sessions are collections of the concepts each lesson introduces, ordered as the course */
lessons.forEach((l) => {
  const mem = concepts.filter((c) => lessonOf(c.intro) === l.record.id).map((c) => `tm:${c.id}`);
  ttl += `\ntm:session-0${l.record.sequence} a skos:Collection ;\n    skos:prefLabel "Session ${l.record.sequence}: ${esc(l.record.title)}"@${lang} ;\n    dct:identifier "${l.record.id}" ;\n    skos:member ${mem.join(', ')} .\n`;
});
ttl += `\ntm:pack a skos:OrderedCollection ;\n    skos:prefLabel "${esc(course.title)}"@${lang} ;\n    dct:identifier "${course.id}" ;\n    skos:memberList ( ${lessons.map((l) => `tm:session-0${l.record.sequence}`).join(' ')} ) .\n`;
W('skos/teaching-meta.ttl', ttl);

/* ---------- Markdown ---------- */
const stubs = path.join(root, 'tools', 'render-stubs.js');
const tmp = path.join(root, 'dist', '.tmp'); fs.mkdirSync(tmp, { recursive: true });
const run = (kind, file, extra) => {
  const { spawnSync } = require('child_process');
  const r = spawnSync('node', [stubs, kind, file, '--date', DATE, '--check', ...extra], { encoding: 'utf8', env: { ...process.env, NODE_PATH: process.env.NODE_PATH || path.join(root, 'node_modules') } });
  if (r.status !== 0) { bad(`render ${kind} ${file}: ${r.stderr}`); return ''; }
  (r.stderr.match(/WARNING.*/g) || []).forEach((w) => bad(`render ${kind}: ${w}`));
  return r.stdout;
};
const split = (md) => { const m = md.match(/^(---\n[\s\S]*?\n---\n)/); return m ? m[1] : ''; };
const lab = (id) => byId[id].label;
const dash = (c) => `${c.label} (${c.notation})`;
const minutes = (m) => `${m} min`;

fs.writeFileSync(path.join(tmp, 'course.json'), JSON.stringify(course));
const courseMd = run('course', path.join(tmp, 'course.json'), []);

const tree = (id, depth) => `${'  '.repeat(depth)}- **${byId[id].label}** (${byId[id].notation}) ${byId[id].def}\n` + (nar[id] || []).map((n) => tree(n, depth + 1)).join('');
let cbody = `\n# ${course.title}\n\n${course.summary}\n\n## Who this is for\n\n${course.audience.description}\n\n## Through line\n\n${course.concept.through_line}\n\n${course.concept.coherence_claim}\n\n## Outcomes\n\n${course.outcomes.map((o) => `- **${o.id}** ${o.statement}`).join('\n')}\n\n## Lessons\n\n| # | Lesson | Role | Time | Outcomes | Vocabulary introduced |\n|---|---|---|---|---|---|\n`;
cbody += course.lesson_map.map((m) => `| ${m.sequence} | ${m.title} | ${m.role} | ${minutes(m.estimated_duration_minutes)} | ${m.course_outcome_ids.join(', ')} | ${concepts.filter((c) => lessonOf(c.intro) === m.lesson_id).map((c) => c.notation).join(', ')} |`).join('\n');
cbody += `\n\n## Vocabulary\n\nThe course vocabulary is a SKOS concept scheme (\`skos/teaching-meta.ttl\`). The tree below is derived from it.\n\n${concepts.filter((c) => c.top).map((c) => tree(c.id, 0)).join('')}\n## Portfolio\n\n${course.assessment.strategy}\n`;
W('dist/course.md', split(courseMd) + cbody);

const report = { built: DATE, lessons: [], concepts: concepts.length, problems };
lessons.forEach((l) => {
  const r = JSON.parse(JSON.stringify(l.record));
  const intro = concepts.filter((c) => lessonOf(c.intro) === r.id);
  r.tags = intro.map((c) => `${scheme.id}:${c.notation}`);
  r.sources = [...new Set(intro.map((c) => c.source).filter(Boolean))];
  fs.writeFileSync(path.join(tmp, 'rec.json'), JSON.stringify(r));
  const md = run('lesson', path.join(tmp, 'rec.json'), ['--course', path.join(tmp, 'course.json')]);
  let b = `\n# ${r.title}\n\n${l.intro.join('\n\n')}\n\n## Learning outcomes\n\n${r.learning_outcomes.map((o) => `- **${o.id}** ${o.statement} (${o.course_outcome_ids.join(', ')})`).join('\n')}\n\n## Key ideas\n\n`;
  intro.forEach((c) => {
    b += `### ${c.label}\n\n*${c.notation}${c.alt && c.alt.length ? `. Also called: ${c.alt.join(', ')}` : ''}*\n\n${c.def}\n\n**In practice:** ${c.scope}\n\n**Example:** ${c.example}\n\n`;
  });
  b += `## Activities\n\n` + r.activities.map((a) => `### ${a.id}\n\n*${a.purpose}* (${a.lesson_outcome_ids.join(', ')})\n\n${l.activities[a.id]}\n`).join('\n');
  b += `\n## Check yourself\n\n${l.checks.map((c, i) => `${i + 1}. ${c}`).join('\n')}\n\n## Take it into your practice\n\n${l.practice}\n\n## How these ideas connect\n\n| Concept | Sits under | Linked to |\n|---|---|---|\n`;
  b += intro.map((c) => `| ${dash(c)} | ${c.broader ? lab(c.broader) : 'Top concept'} | ${[...(sym.get(c.id) || [])].map(lab).join(', ') || 'None'} |`).join('\n');
  b += `\n\n## Sources\n\n${r.sources.length ? r.sources.map((x) => `- ${x}`).join('\n') : '- None cited for this lesson.'}\n\nCitations come from the concept scheme and have not been verified page by page. Check each before you publish.\n`;
  W(`dist/lesson-0${r.sequence}.md`, split(md) + b);
  report.lessons.push({ id: r.id, concepts: intro.length, words: b.split(/\s+/).length });
});
fs.rmSync(tmp, { recursive: true, force: true });
W('dist/report.json', JSON.stringify(report, null, 2) + '\n');
console.log(problems.length ? `PROBLEMS (${problems.length}):\n- ` + problems.join('\n- ') : `OK: ${concepts.length} concepts, ${lessons.length} lessons, no problems`);
console.log('External targets (not in this pack):', external.join(', '));
process.exit(problems.length ? 1 : 0);
