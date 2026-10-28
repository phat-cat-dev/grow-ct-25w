/**
 * Unit tests for progressLogic — pure functions.
 * Uses Node's built-in test runner (node:test + node:assert/strict).
 * Run with: node --test test/progressLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual } from 'node:assert';
import { clampPercent, resolveProgress, progressText } from '../js/progressLogic.js';

describe('clampPercent', () => {
  it('computes value/max as a percentage', () => {
    strictEqual(clampPercent(40, 100), 40);
    strictEqual(clampPercent(7, 10), 70);
  });
  it('rounds to 1 decimal place', () => {
    strictEqual(clampPercent(1, 3), 33.3);
  });
  it('clamps to [0,100]', () => {
    strictEqual(clampPercent(150, 100), 100);
    strictEqual(clampPercent(-5, 100), 0);
  });
  it('returns 0 for max<=0 or non-finite', () => {
    strictEqual(clampPercent(5, 0), 0);
    strictEqual(clampPercent('x', 100), 0);
  });
});

describe('resolveProgress', () => {
  it('defaults value 0 / max 100', () => {
    const p = resolveProgress({});
    strictEqual(p.value, 0);
    strictEqual(p.max, 100);
    strictEqual(p.percent, 0);
  });
  it('parses value/max and computes percent', () => {
    const p = resolveProgress({ abProgressValue: '3', abProgressMax: '4' });
    strictEqual(p.percent, 75);
  });
  it('reads flags and variant', () => {
    const p = resolveProgress({ abProgressShowLabel: 'true', abProgressStriped: 'true', abProgressVariant: 'success' });
    strictEqual(p.showLabel, true);
    strictEqual(p.striped, true);
    strictEqual(p.variant, 'success');
    strictEqual(p.animated, false);
  });
});

describe('progressText', () => {
  it('prefers an explicit label', () => {
    strictEqual(progressText({ label: 'Done', showLabel: true, percent: 50 }), 'Done');
  });
  it('shows percent when showLabel and no label', () => {
    strictEqual(progressText({ label: '', showLabel: true, percent: 50 }), '50%');
  });
  it('is empty otherwise', () => {
    strictEqual(progressText({ label: '', showLabel: false, percent: 50 }), '');
  });
});
