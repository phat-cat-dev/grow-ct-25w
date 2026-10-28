#!/usr/bin/env node
'use strict';

/**
 * publish.js - mark a course published (status -> production) and thereby
 * locked. After this, every gate field is locked: a reopen may change only
 * the decidedValue paths it unlocks, and the lint
 * (validate-design-schemas.py / conformance-lint) refuses any out-of-scope
 * change to a record written after publishedAt. See
 * docs/authoring/field-locks-and-edit-mode.md.
 *
 * Idempotent: a course already in production keeps its original publishedAt.
 *
 * Usage:
 *   node tools/publish.js --course=<slug>
 */

const fs = require('fs');
const path = require('path');

function main() {
  const args = process.argv.slice(2);
  const courseArg = args.find(a => a.startsWith('--course='));
  if (!courseArg) {
    process.stderr.write('Usage: node tools/publish.js --course=<slug>\n');
    process.exit(1);
  }
  const slug = courseArg.split('=')[1];
  const manifestPath = path.resolve(
    __dirname, '..', 'courses', slug, `course-design_${slug}.json`
  );
  if (!fs.existsSync(manifestPath)) {
    process.stderr.write(`REFUSED: no manifest at ${manifestPath}\n`);
    process.exit(1);
  }
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

  if (manifest.status === 'production' && manifest.publishedAt) {
    process.stdout.write(
      `No-op: ${slug} is already published (status production, publishedAt ${manifest.publishedAt}).\n`
    );
    process.exit(0);
  }

  manifest.status = 'production';
  manifest.publishedAt = new Date().toISOString();
  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n');
  process.stdout.write(
    `Published ${slug}: status=production, publishedAt=${manifest.publishedAt}. ` +
    `All gate fields are now locked; reopen with explicit --unlock paths.\n`
  );
  process.exit(0);
}

main();
