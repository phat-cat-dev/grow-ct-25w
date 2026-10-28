/**
 * Unit tests for timelineLogic — TB-3 (testable pure functions).
 * Uses Node's built-in test runner (node:test + node:assert/strict).
 * Run with: node --test test/timelineLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, deepStrictEqual } from 'node:assert';
import {
  computeNextExpandedState,
  computeNextVisitation,
  isAllVisited,
  getExpectedTrackableFields
} from '../js/timelineLogic.js';

describe('computeNextExpandedState', () => {
  describe('single mode (default)', () => {
    it('collapses all others when expanding a stage', () => {
      const current = { 0: true, 1: false, 2: true };
      const next = computeNextExpandedState(current, 1, 'single');
      deepStrictEqual(next, { 0: false, 1: true, 2: false });
    });

    it('toggles collapsed stage to expanded, collapsing others', () => {
      const current = { 0: false, 1: false, 2: false };
      const next = computeNextExpandedState(current, 1, 'single');
      deepStrictEqual(next, { 0: false, 1: true, 2: false });
    });

    it('keeps others as-is when collapsing (closing) a stage', () => {
      // When toggling an already-expanded stage to collapsed,
      // we're NOT expanding TO true, so others stay as they are
      const current = { 0: false, 1: true, 2: false };
      const next = computeNextExpandedState(current, 1, 'single');
      deepStrictEqual(next, { 0: false, 1: false, 2: false });
    });

    it('collapses all others even when only one was expanded', () => {
      const current = { 0: true, 1: false, 2: false };
      const next = computeNextExpandedState(current, 2, 'single');
      deepStrictEqual(next, { 0: false, 1: false, 2: true });
    });
  });

  describe('independent mode', () => {
    it('toggles collapsed stage to expanded', () => {
      const current = { 0: false, 1: false, 2: false };
      const next = computeNextExpandedState(current, 1, 'independent');
      deepStrictEqual(next, { 0: false, 1: true, 2: false });
    });

    it('toggles expanded stage to collapsed', () => {
      const current = { 0: false, 1: true, 2: false };
      const next = computeNextExpandedState(current, 1, 'independent');
      deepStrictEqual(next, { 0: false, 1: false, 2: false });
    });

    it('leaves other stages unchanged when expanding', () => {
      const current = { 0: true, 1: false, 2: true };
      const next = computeNextExpandedState(current, 1, 'independent');
      deepStrictEqual(next, { 0: true, 1: true, 2: true });
    });

    it('handles empty initial state', () => {
      const current = {};
      const next = computeNextExpandedState(current, 0, 'independent');
      deepStrictEqual(next, { 0: true });
    });
  });
});

describe('computeNextVisitation', () => {
  it('marks item as visited on first expand', () => {
    const current = [false, false, false];
    const next = computeNextVisitation(current, 1, true);
    deepStrictEqual(next, [false, true, false]);
  });

  it('is idempotent — already visited stays visited', () => {
    const current = [false, true, false];
    const next = computeNextVisitation(current, 1, true);
    deepStrictEqual(next, [false, true, false]);
  });

  it('does not mark as visited when collapsing', () => {
    const current = [false, false, false];
    const next = computeNextVisitation(current, 1, false);
    deepStrictEqual(next, [false, false, false]);
  });

  it('preserves existing visitation for other items', () => {
    const current = [true, false, true];
    const next = computeNextVisitation(current, 1, true);
    deepStrictEqual(next, [true, true, true]);
  });

  it('handles last stage being visited', () => {
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

  it('last-stage expand triggers completion (integration scenario)', () => {
    // Simulate: 3 stages, first two visited, last stage expanded
    const beforeLastExpand = [true, true, false];
    const afterLastExpand = computeNextVisitation(beforeLastExpand, 2, true);
    strictEqual(isAllVisited(afterLastExpand), true);
  });
});

describe('getExpectedTrackableFields', () => {
  it('returns array of standard ItemsComponentModel trackable fields', () => {
    const fields = getExpectedTrackableFields();
    strictEqual(Array.isArray(fields), true);
    strictEqual(fields.length > 0, true);
  });

  it('does NOT include _isExpanded', () => {
    const fields = getExpectedTrackableFields();
    strictEqual(fields.includes('_isExpanded'), false);
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
