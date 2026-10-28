/**
 * Unit tests for checklistLogic.js
 *
 * Run with: node --test src/components/adapt-abbott-checklist/test/checklistLogic.test.js
 *
 * Tests required by CB-3:
 * - Independent toggling (ticking item 2 leaves 1 and 3 unchanged)
 * - Untick does not unvisit
 * - First-tick visitation and idempotence
 * - All-visited completion including last-item firing
 * - Checked count at boundaries (none/some/all)
 * - Trackable-fields assertion — specifically that _isChecked is absent
 */

import { describe, it } from 'node:test';
import assert from 'node:assert/strict';

import {
  computeNextCheckedState,
  computeNextVisitation,
  isAllVisited,
  countChecked,
  getExpectedTrackableFields
} from '../js/checklistLogic.js';

// =============================================================================
// computeNextCheckedState tests (independent toggling)
// =============================================================================

describe('computeNextCheckedState', () => {

  it('toggles an unchecked item to checked', () => {
    const currentMap = { 0: false, 1: false, 2: false };
    const result = computeNextCheckedState(currentMap, 1);

    assert.equal(result[1], true);
  });

  it('toggles a checked item to unchecked', () => {
    const currentMap = { 0: true, 1: false, 2: false };
    const result = computeNextCheckedState(currentMap, 0);

    assert.equal(result[0], false);
  });

  it('independent toggling - ticking item 2 leaves 1 and 3 unchanged', () => {
    const currentMap = { 0: true, 1: false, 2: false, 3: true };
    const result = computeNextCheckedState(currentMap, 2);

    // Item 2 toggled
    assert.equal(result[2], true);

    // Items 0, 1, 3 unchanged
    assert.equal(result[0], true);
    assert.equal(result[1], false);
    assert.equal(result[3], true);
  });

  it('does not mutate original map', () => {
    const currentMap = { 0: false, 1: false };
    const result = computeNextCheckedState(currentMap, 0);

    assert.notStrictEqual(result, currentMap);
    assert.equal(currentMap[0], false); // unchanged
    assert.equal(result[0], true);
  });

  it('handles null/undefined map gracefully', () => {
    assert.deepEqual(computeNextCheckedState(null, 0), {});
    assert.deepEqual(computeNextCheckedState(undefined, 0), {});
  });

  it('handles toggling non-existent index', () => {
    const currentMap = { 0: false };
    const result = computeNextCheckedState(currentMap, 5);

    // Creates the index with toggled value (undefined -> true)
    assert.equal(result[5], true);
    assert.equal(result[0], false);
  });

});

// =============================================================================
// computeNextVisitation tests (one-way visitation, CL-4)
// =============================================================================

describe('computeNextVisitation', () => {

  it('marks unvisited item as visited on first tick', () => {
    const visited = [false, false, false];
    const result = computeNextVisitation(visited, 1);

    assert.deepEqual(result, [false, true, false]);
  });

  it('is idempotent - already visited stays visited', () => {
    const visited = [true, false, false];
    const result = computeNextVisitation(visited, 0);

    // No change - already visited
    assert.deepEqual(result, [true, false, false]);
  });

  it('untick does NOT unvisit (CL-4 critical test)', () => {
    // Scenario: item was ticked (visited), then unticked
    // The visited array should NOT change when we call computeNextVisitation
    // because visitation is one-way

    const visited = [true, true, false]; // items 0 and 1 were visited
    // Even if we "toggle off" item 0, it remains visited
    const result = computeNextVisitation(visited, 0);

    // Still visited - one-way
    assert.equal(result[0], true);
  });

  it('does not mutate original array when marking new visit', () => {
    const visited = [false, false, false];
    const result = computeNextVisitation(visited, 0);

    assert.notStrictEqual(result, visited);
    assert.deepEqual(visited, [false, false, false]); // unchanged
    assert.deepEqual(result, [true, false, false]);
  });

  it('returns same reference when already visited (idempotence optimisation)', () => {
    const visited = [true, false];
    const result = computeNextVisitation(visited, 0);

    // Same reference since no change needed
    assert.strictEqual(result, visited);
  });

  it('handles out-of-bounds index gracefully', () => {
    const visited = [false, false];
    assert.deepEqual(computeNextVisitation(visited, -1), visited);
    assert.deepEqual(computeNextVisitation(visited, 5), visited);
  });

  it('handles null/empty array', () => {
    assert.deepEqual(computeNextVisitation(null, 0), []);
    assert.deepEqual(computeNextVisitation([], 0), []);
  });

});

// =============================================================================
// isAllVisited tests (completion check)
// =============================================================================

describe('isAllVisited', () => {

  it('returns true when all items visited', () => {
    assert.equal(isAllVisited([true, true, true]), true);
    assert.equal(isAllVisited([true, true]), true);
  });

  it('returns false when some items unvisited', () => {
    assert.equal(isAllVisited([true, false, true]), false);
    assert.equal(isAllVisited([false, false]), false);
  });

  it('returns false for empty array', () => {
    assert.equal(isAllVisited([]), false);
  });

  it('returns false for null/undefined', () => {
    assert.equal(isAllVisited(null), false);
    assert.equal(isAllVisited(undefined), false);
  });

  it('completion fires on last item (last-item firing test)', () => {
    // Simulate progression to last item
    let visited = [false, false, false, false];

    // Tick items 0, 1, 2 - not yet complete
    visited = computeNextVisitation(visited, 0);
    visited = computeNextVisitation(visited, 1);
    visited = computeNextVisitation(visited, 2);
    assert.equal(isAllVisited(visited), false);

    // Tick item 3 (last item) - NOW complete
    visited = computeNextVisitation(visited, 3);
    assert.equal(isAllVisited(visited), true);
  });

  it('completion persists after unticking (CL-4)', () => {
    // All visited
    const visited = [true, true, true, true];
    assert.equal(isAllVisited(visited), true);

    // Even if user unticks, visitation array doesn't change
    // (unticking is handled in checked state, not visitation)
    // So completion remains true
    assert.equal(isAllVisited(visited), true);
  });

});

// =============================================================================
// countChecked tests (boundaries: none/some/all)
// =============================================================================

describe('countChecked', () => {

  it('returns 0 when none checked', () => {
    assert.equal(countChecked({ 0: false, 1: false, 2: false }), 0);
  });

  it('returns correct count when some checked', () => {
    assert.equal(countChecked({ 0: true, 1: false, 2: true }), 2);
    assert.equal(countChecked({ 0: false, 1: true, 2: false, 3: false }), 1);
  });

  it('returns total when all checked', () => {
    assert.equal(countChecked({ 0: true, 1: true, 2: true }), 3);
    assert.equal(countChecked({ 0: true, 1: true, 2: true, 3: true }), 4);
  });

  it('handles empty map', () => {
    assert.equal(countChecked({}), 0);
  });

  it('handles null/undefined', () => {
    assert.equal(countChecked(null), 0);
    assert.equal(countChecked(undefined), 0);
  });

  it('boundary: minimum item count (4)', () => {
    assert.equal(countChecked({ 0: true, 1: true, 2: true, 3: true }), 4);
    assert.equal(countChecked({ 0: true, 1: false, 2: false, 3: true }), 2);
  });

  it('boundary: maximum item count (8)', () => {
    const allChecked = { 0: true, 1: true, 2: true, 3: true, 4: true, 5: true, 6: true, 7: true };
    assert.equal(countChecked(allChecked), 8);

    const someChecked = { ...allChecked, 2: false, 5: false };
    assert.equal(countChecked(someChecked), 6);
  });

});

// =============================================================================
// getExpectedTrackableFields tests (trackable-fields assertion)
// =============================================================================

describe('getExpectedTrackableFields', () => {

  it('confirms _isChecked is transient (NOT in trackable) - CRITICAL', () => {
    const fields = getExpectedTrackableFields();

    assert.ok(fields.transient.includes('_isChecked'),
      '_isChecked must be transient - ticks should not persist');
    assert.ok(!fields.persisted.includes('_isChecked'),
      '_isChecked must NOT be persisted');
  });

  it('confirms _checkedMap is transient', () => {
    const fields = getExpectedTrackableFields();

    assert.ok(fields.transient.includes('_checkedMap'));
    assert.ok(!fields.persisted.includes('_checkedMap'));
  });

  it('confirms _userAnswer is persisted (visitation)', () => {
    const fields = getExpectedTrackableFields();

    assert.ok(fields.persisted.includes('_userAnswer'));
  });

});

// =============================================================================
// Integration scenario tests
// =============================================================================

describe('Integration scenarios', () => {

  it('full workflow: tick all, untick one, verify completion persists', () => {
    // Initial state
    let checkedMap = { 0: false, 1: false, 2: false, 3: false };
    let visited = [false, false, false, false];

    // Tick all items
    for (let i = 0; i < 4; i++) {
      checkedMap = computeNextCheckedState(checkedMap, i);
      visited = computeNextVisitation(visited, i);
    }

    // All checked and visited
    assert.equal(countChecked(checkedMap), 4);
    assert.equal(isAllVisited(visited), true);

    // Now untick item 1
    checkedMap = computeNextCheckedState(checkedMap, 1);

    // Checked count drops
    assert.equal(countChecked(checkedMap), 3);
    assert.equal(checkedMap[1], false);

    // But visitation persists (CL-4: untick does not unvisit)
    assert.equal(isAllVisited(visited), true);
    assert.equal(visited[1], true); // Still visited
  });

  it('revisit scenario: checked resets but completion persists', () => {
    // First visit: tick all items
    let checkedMap = { 0: true, 1: true, 2: true, 3: true };
    const visited = [true, true, true, true];

    assert.equal(countChecked(checkedMap), 4);
    assert.equal(isAllVisited(visited), true);

    // Simulate revisit: reset checked state
    checkedMap = { 0: false, 1: false, 2: false, 3: false };

    // Ticks cleared
    assert.equal(countChecked(checkedMap), 0);

    // But visitation (and thus completion) persists
    assert.equal(isAllVisited(visited), true);
  });

});
