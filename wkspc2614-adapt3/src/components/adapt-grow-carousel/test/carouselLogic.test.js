/**
 * Unit tests for carouselLogic — pure functions.
 * Uses Node's built-in test runner (node:test + node:assert/strict).
 * Run with: node --test test/carouselLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, deepStrictEqual } from 'node:assert';
import {
  resolveIndex,
  computeNextVisitation,
  isAllVisited
} from '../js/carouselLogic.js';

describe('resolveIndex', () => {
  describe('cycling (canCycle = true)', () => {
    it('wraps past the end to the start', () => {
      strictEqual(resolveIndex(3, 3, true), 0);
    });
    it('wraps before the start to the end', () => {
      strictEqual(resolveIndex(-1, 3, true), 2);
    });
    it('returns an in-range index unchanged', () => {
      strictEqual(resolveIndex(1, 3, true), 1);
    });
  });

  describe('clamping (canCycle = false)', () => {
    it('clamps above the end to the last index', () => {
      strictEqual(resolveIndex(5, 3, false), 2);
    });
    it('clamps below zero to the first index', () => {
      strictEqual(resolveIndex(-2, 3, false), 0);
    });
  });

  it('returns 0 when there are no slides', () => {
    strictEqual(resolveIndex(2, 0, true), 0);
    strictEqual(resolveIndex(2, 0, false), 0);
  });
});

describe('computeNextVisitation', () => {
  it('marks the visited slide', () => {
    deepStrictEqual(computeNextVisitation([false, false, false], 1), [false, true, false]);
  });
  it('ignores out-of-range indices', () => {
    deepStrictEqual(computeNextVisitation([false, false], 5), [false, false]);
  });
  it('is idempotent', () => {
    deepStrictEqual(computeNextVisitation([true, false], 0), [true, false]);
  });
});

describe('isAllVisited', () => {
  it('is true only when every slide is visited', () => {
    strictEqual(isAllVisited([true, true, true]), true);
    strictEqual(isAllVisited([true, false, true]), false);
  });
  it('is false for an empty set', () => {
    strictEqual(isAllVisited([]), false);
  });
});
