/**
 * Unit tests for flipcardLogic — FB-5 (testable pure functions).
 * Uses Node's built-in test runner (node:test + node:assert/strict).
 * Run with: node --test test/flipcardLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, deepStrictEqual } from 'node:assert';
import {
  computeNextFlippedState,
  computeNextVisitation,
  isAllVisited,
  getExpectedTrackableFields
} from '../js/flipcardLogic.js';

describe('computeNextFlippedState', () => {
  describe('independent mode', () => {
    it('toggles unflipped card to flipped', () => {
      const current = { 0: false, 1: false, 2: false };
      const next = computeNextFlippedState(current, 1, 'independent');
      deepStrictEqual(next, { 0: false, 1: true, 2: false });
    });

    it('toggles flipped card to unflipped', () => {
      const current = { 0: false, 1: true, 2: false };
      const next = computeNextFlippedState(current, 1, 'independent');
      deepStrictEqual(next, { 0: false, 1: false, 2: false });
    });

    it('leaves other cards unchanged when flipping', () => {
      const current = { 0: true, 1: false, 2: true };
      const next = computeNextFlippedState(current, 1, 'independent');
      deepStrictEqual(next, { 0: true, 1: true, 2: true });
    });

    it('handles empty initial state', () => {
      const current = {};
      const next = computeNextFlippedState(current, 0, 'independent');
      deepStrictEqual(next, { 0: true });
    });
  });

  describe('single mode', () => {
    it('unflips all others when flipping a card', () => {
      const current = { 0: true, 1: false, 2: true };
      const next = computeNextFlippedState(current, 1, 'single');
      deepStrictEqual(next, { 0: false, 1: true, 2: false });
    });

    it('keeps others as-is when unflipping (closing) a card', () => {
      // When toggling an already-flipped card to unflipped,
      // we're NOT flipping TO true, so others stay as they are
      const current = { 0: false, 1: true, 2: false };
      const next = computeNextFlippedState(current, 1, 'single');
      deepStrictEqual(next, { 0: false, 1: false, 2: false });
    });

    it('unflips all others even when only one was flipped', () => {
      const current = { 0: true, 1: false, 2: false };
      const next = computeNextFlippedState(current, 2, 'single');
      deepStrictEqual(next, { 0: false, 1: false, 2: true });
    });
  });
});

describe('computeNextVisitation', () => {
  it('marks item as visited on first flip to back', () => {
    const current = [false, false, false];
    const next = computeNextVisitation(current, 1, true);
    deepStrictEqual(next, [false, true, false]);
  });

  it('is idempotent — already visited stays visited', () => {
    const current = [false, true, false];
    const next = computeNextVisitation(current, 1, true);
    deepStrictEqual(next, [false, true, false]);
  });

  it('does not mark as visited when flipping back to front', () => {
    const current = [false, false, false];
    const next = computeNextVisitation(current, 1, false);
    deepStrictEqual(next, [false, false, false]);
  });

  it('preserves existing visitation for other items', () => {
    const current = [true, false, true];
    const next = computeNextVisitation(current, 1, true);
    deepStrictEqual(next, [true, true, true]);
  });

  it('handles last card being visited', () => {
    const current = [true, true, false];
    const next = computeNextVisitation(current, 2, true);
    deepStrictEqual(next, [true, true, true]);
  });
});

describe('isAllVisited (completion predicate)', () => {
  it('returns true when all items visited', () => {
    strictEqual(isAllVisited([true, true, true]), true);
  });

  it('returns false when some items not visited', () => {
    strictEqual(isAllVisited([true, false, true]), false);
  });

  it('returns false when no items visited', () => {
    strictEqual(isAllVisited([false, false, false]), false);
  });

  it('returns true for single-item all visited', () => {
    strictEqual(isAllVisited([true]), true);
  });

  it('returns false for single-item not visited', () => {
    strictEqual(isAllVisited([false]), false);
  });

  it('returns false for empty array', () => {
    strictEqual(isAllVisited([]), false);
  });

  it('returns false for null/undefined', () => {
    strictEqual(isAllVisited(null), false);
    strictEqual(isAllVisited(undefined), false);
  });

  it('last-card flip triggers completion (integration scenario)', () => {
    // Simulate: 3 cards, first two visited, last card flipped
    const beforeLastFlip = [true, true, false];
    const afterLastFlip = computeNextVisitation(beforeLastFlip, 2, true);
    strictEqual(isAllVisited(afterLastFlip), true);
  });
});

describe('getExpectedTrackableFields', () => {
  it('returns array of standard ItemsComponentModel trackable fields', () => {
    const fields = getExpectedTrackableFields();
    strictEqual(Array.isArray(fields), true);
    strictEqual(fields.length > 0, true);
  });

  it('does NOT include _isFlipped', () => {
    const fields = getExpectedTrackableFields();
    strictEqual(fields.includes('_isFlipped'), false);
  });

  it('includes _isComplete for completion tracking', () => {
    const fields = getExpectedTrackableFields();
    strictEqual(fields.includes('_isComplete'), true);
  });

  it('includes _isVisited for visitation tracking', () => {
    const fields = getExpectedTrackableFields();
    strictEqual(fields.includes('_isVisited'), true);
  });
});
