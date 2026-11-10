/**
 * Unit tests for tabsLogic.js
 *
 * Run with: node --test src/components/adapt-grow-tabs/test/tabsLogic.test.js
 */

import { describe, it } from 'node:test';
import assert from 'node:assert/strict';

import {
  computeNextIndex,
  computeNextVisitation,
  keyToDirection,
  Direction
} from '../js/tabsLogic.js';

// =============================================================================
// computeNextIndex tests
// =============================================================================

describe('computeNextIndex', () => {

  describe('Direction.RIGHT', () => {
    it('moves from 0 to 1 in 3-item list', () => {
      assert.equal(computeNextIndex(0, Direction.RIGHT, 3), 1);
    });

    it('moves from 1 to 2 in 3-item list', () => {
      assert.equal(computeNextIndex(1, Direction.RIGHT, 3), 2);
    });

    it('wraps from last to first', () => {
      assert.equal(computeNextIndex(2, Direction.RIGHT, 3), 0);
    });

    it('wraps in 2-item list', () => {
      assert.equal(computeNextIndex(1, Direction.RIGHT, 2), 0);
    });
  });

  describe('Direction.LEFT', () => {
    it('moves from 2 to 1 in 3-item list', () => {
      assert.equal(computeNextIndex(2, Direction.LEFT, 3), 1);
    });

    it('moves from 1 to 0 in 3-item list', () => {
      assert.equal(computeNextIndex(1, Direction.LEFT, 3), 0);
    });

    it('wraps from first to last', () => {
      assert.equal(computeNextIndex(0, Direction.LEFT, 3), 2);
    });

    it('wraps in 2-item list', () => {
      assert.equal(computeNextIndex(0, Direction.LEFT, 2), 1);
    });
  });

  describe('Direction.HOME', () => {
    it('returns 0 from any position', () => {
      assert.equal(computeNextIndex(0, Direction.HOME, 4), 0);
      assert.equal(computeNextIndex(1, Direction.HOME, 4), 0);
      assert.equal(computeNextIndex(2, Direction.HOME, 4), 0);
      assert.equal(computeNextIndex(3, Direction.HOME, 4), 0);
    });
  });

  describe('Direction.END', () => {
    it('returns last index from any position', () => {
      assert.equal(computeNextIndex(0, Direction.END, 4), 3);
      assert.equal(computeNextIndex(1, Direction.END, 4), 3);
      assert.equal(computeNextIndex(2, Direction.END, 4), 3);
      assert.equal(computeNextIndex(3, Direction.END, 4), 3);
    });

    it('handles 2-item list', () => {
      assert.equal(computeNextIndex(0, Direction.END, 2), 1);
    });
  });

  describe('edge cases', () => {
    it('handles single-item list (always returns 0)', () => {
      assert.equal(computeNextIndex(0, Direction.LEFT, 1), 0);
      assert.equal(computeNextIndex(0, Direction.RIGHT, 1), 0);
      assert.equal(computeNextIndex(0, Direction.HOME, 1), 0);
      assert.equal(computeNextIndex(0, Direction.END, 1), 0);
    });

    it('handles empty list (returns 0)', () => {
      assert.equal(computeNextIndex(0, Direction.RIGHT, 0), 0);
    });

    it('returns current index for unknown direction', () => {
      assert.equal(computeNextIndex(1, 'Unknown', 3), 1);
    });
  });

});

// =============================================================================
// computeNextVisitation tests
// =============================================================================

describe('computeNextVisitation', () => {

  it('marks unvisited tab as visited', () => {
    const current = [false, false, false];
    const result = computeNextVisitation(current, 1);
    assert.deepEqual(result, [false, true, false]);
  });

  it('keeps already visited tab as visited', () => {
    const current = [false, true, false];
    const result = computeNextVisitation(current, 1);
    assert.deepEqual(result, [false, true, false]);
  });

  it('marks first tab as visited', () => {
    const current = [false, false, false];
    const result = computeNextVisitation(current, 0);
    assert.deepEqual(result, [true, false, false]);
  });

  it('marks last tab as visited', () => {
    const current = [false, false, false];
    const result = computeNextVisitation(current, 2);
    assert.deepEqual(result, [false, false, true]);
  });

  it('does not mutate original array', () => {
    const current = [false, false, false];
    const result = computeNextVisitation(current, 1);
    assert.deepEqual(current, [false, false, false]);
    assert.notStrictEqual(result, current);
  });

  it('handles out-of-bounds index gracefully', () => {
    const current = [false, false];
    const result = computeNextVisitation(current, 5);
    assert.deepEqual(result, [false, false]);
  });

  it('handles negative index gracefully', () => {
    const current = [false, false];
    const result = computeNextVisitation(current, -1);
    assert.deepEqual(result, [false, false]);
  });

});

// =============================================================================
// keyToDirection tests
// =============================================================================

describe('keyToDirection', () => {

  it('maps ArrowLeft to LEFT', () => {
    assert.equal(keyToDirection('ArrowLeft'), Direction.LEFT);
  });

  it('maps ArrowRight to RIGHT', () => {
    assert.equal(keyToDirection('ArrowRight'), Direction.RIGHT);
  });

  it('maps ArrowUp to LEFT (vertical semantics)', () => {
    assert.equal(keyToDirection('ArrowUp'), Direction.LEFT);
  });

  it('maps ArrowDown to RIGHT (vertical semantics)', () => {
    assert.equal(keyToDirection('ArrowDown'), Direction.RIGHT);
  });

  it('maps Home to HOME', () => {
    assert.equal(keyToDirection('Home'), Direction.HOME);
  });

  it('maps End to END', () => {
    assert.equal(keyToDirection('End'), Direction.END);
  });

  it('returns null for non-navigation keys', () => {
    assert.equal(keyToDirection('Enter'), null);
    assert.equal(keyToDirection('Space'), null);
    assert.equal(keyToDirection('Tab'), null);
    assert.equal(keyToDirection('a'), null);
  });

});
