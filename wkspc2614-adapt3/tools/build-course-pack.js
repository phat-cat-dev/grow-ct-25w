#!/usr/bin/env node
/**
 * build-course-pack.js
 *
 * The crs-05_course-spec rollup (gate-redesign-2026-10-06.md, A5): assembles
 * the user-facing "course pack" from a course's closed ONB+CRS gate records
 * and renders it via tools/render-doc.js + tools/doc-templates/
 * course-pack.template.json. Auto-stands: a read of already-confirmed records,
 * never a writer of gate records.
 *
 * Usage:
 *   node tools/build-course-pack.js --course=<slug> [--out=<file.md>]
 *   (no --out: prints the Markdown to stdout)
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { render } = require('./render-doc.js');

const ROOT = path.resolve(__dirname, '..');

function fail(m) { console.error(`build-course-pack: ${m}`); process.exit(1); }

function parseArgs() {
  const a = {};
  process.argv.slice(2).forEach(p => {
    const eq = p.indexOf('='); if (eq === -1) return;
    a[p.slice(2, eq)] = p.slice(eq + 1);
  });
  if (!a.course) fail('--course=<slug> is required.');
  return a;
}

function lastClosed(manifest, gateId) {
  const g = (manifest.gates || []).find(x => x.gateId === gateId);
  if (!g || !Array.isArray(g.records)) return null;
  for (let i = g.records.length - 1; i >= 0; i--) {
    if (g.records[i].state === 'closed') return g.records[i];
  }
  return null;
}
const dv = (manifest, gateId) => { const r = lastClosed(manifest, gateId); return r ? (r.decidedValue || {}) : {}; };

function main() {
  const args = parseArgs();
  const slug = args.course;
  const manifestPath = path.join(ROOT, 'courses', slug, `course-design_${slug}.json`);
  if (!fs.existsSync(manifestPath)) fail(`no manifest at ${path.relative(ROOT, manifestPath)}`);
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

  const naming = dv(manifest, 'onb-04_naming');
  const facet = manifest.facetSet || {};
  const referencing = dv(manifest, 'cxs-04_referencing-style');
  const scope = dv(manifest, 'crs-02_thematic-scope');
  const outcomesDV = dv(manifest, 'crs-03_course-outcomes');
  const mapDV = dv(manifest, 'crs-04_lesson-map');

  const courseName = [naming.pathwayName, naming.tierName].filter(Boolean).join(': ') || slug;
  const banksByOutcome = {};
  for (const b of (outcomesDV.courseOutcomeBanks || [])) banksByOutcome[b.outcomeId] = b;

  const data = {
    identity: { courseName, theme: facet.pathway || null, pitch: facet.tier || null, slug: manifest.slug || slug },
    contextShell: {
      // The CXS gates are reserved auto-pass placeholders ("none") except
      // cxs-04_referencing-style, which carries a live default. A reserved
      // placeholder renders as null (not set); referencing shows its value.
      institutional: null, subject: null, qualifiers: null,
      referencing: referencing.referencingStyle || null,
      externalStandards: null
    },
    thematicScope: {
      sourceType: scope.sourceType || null,
      sectionsInScope: scope.sectionsInScope || [],
      sectionsOutOfScope: scope.sectionsOutOfScope || [],
      priorExperienceAnchor: scope.priorExperienceAnchor || null,
      tierWindow: scope.tierWindow || {}
    },
    thematicStrands: scope.subThemes || [],
    courseOutcomes: (outcomesDV.courseOutcomes || []).map(o => {
      const bank = banksByOutcome[o.id] || {};
      const conf = bank.confidenceStatement || {};
      return {
        id: o.id, text: o.text,
        confidenceStatement: { text: conf.text || null, status: conf.status || null },
        // The banks hold MCQ-SET specs (coupling/application/feedback), not
        // authored question stems yet; show the drafted count rather than
        // inventing stems. Stems are authored later (SUMM page).
        mcqQuestions: (bank.mcqSets || []).map((s, i) => ({ stem: `MCQ set ${i + 1} (${s.status || 'drafted'}; cross-lesson, feedback on every answer)` }))
      };
    }),
    lessonMap: {
      progression: mapDV.progression || null,
      lessons: (mapDV.lessons || []).map((l, i) => ({
        key: l.key, sequence: i + 1, title: l.title || l.key, topic: l.topic || null,
        description: l.description || null, outcomes: l.outcomes || []
      }))
    }
  };

  const template = JSON.parse(fs.readFileSync(path.join(ROOT, 'tools', 'doc-templates', 'course-pack.template.json'), 'utf8'));
  const md = render(template, data);
  if (args.out) { fs.writeFileSync(args.out, md); console.error(`wrote ${args.out}`); }
  else process.stdout.write(md);
}

if (require.main === module) main();
