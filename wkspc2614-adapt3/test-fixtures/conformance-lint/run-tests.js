#!/usr/bin/env node
/**
 * run-tests.js
 *
 * Test runner for conformance-lint.js fixtures.
 * Invokes the lint with explicit --manifest and --blocks paths.
 *
 * Usage: node test-fixtures/conformance-lint/run-tests.js
 */

const { execSync } = require('child_process');
const path = require('path');

const ROOT = path.join(__dirname, '..', '..');
const FIXTURES_DIR = __dirname;

const fixtures = [
  {
    name: 'clause1-documented-pass',
    expectPass: true,
    description: 'Documented deviation should PASS'
  },
  {
    name: 'clause1-undocumented-fail',
    expectPass: false,
    description: 'Undocumented deviation should FAIL'
  },
  {
    name: 'clause2-unresolved-fail',
    expectPass: false,
    description: 'Unresolved sweepEvent should BLOCK'
  },
  {
    name: 'clause3-gaps-info',
    expectPass: true,
    description: 'GroundingGaps should report INFO but PASS'
  }
];

let passed = 0;
let failed = 0;

console.log('conformance-lint fixture tests\n');

for (const fixture of fixtures) {
  const manifestPath = path.join(FIXTURES_DIR, fixture.name, `course-design_${fixture.name}.json`);
  const blocksPath = path.join(FIXTURES_DIR, fixture.name, 'en', 'blocks.json');

  const cmd = `node "${path.join(ROOT, 'tools', 'conformance-lint.js')}" --manifest="${manifestPath}" --blocks="${blocksPath}"`;

  let exitCode = 0;
  let output = '';

  try {
    output = execSync(cmd, { encoding: 'utf8', stdio: ['pipe', 'pipe', 'pipe'] });
  } catch (err) {
    exitCode = err.status || 1;
    output = (err.stdout || '') + (err.stderr || '');
  }

  const actualPass = exitCode === 0;
  const testPassed = actualPass === fixture.expectPass;

  if (testPassed) {
    console.log(`  [PASS] ${fixture.name}: ${fixture.description}`);
    passed++;
  } else {
    console.log(`  [FAIL] ${fixture.name}: ${fixture.description}`);
    console.log(`         Expected ${fixture.expectPass ? 'PASS' : 'FAIL'}, got ${actualPass ? 'PASS' : 'FAIL'}`);
    console.log(`         Output:\n${output.split('\n').map(l => '           ' + l).join('\n')}`);
    failed++;
  }
}

console.log(`\n${passed} passed, ${failed} failed`);
process.exit(failed > 0 ? 1 : 0);
