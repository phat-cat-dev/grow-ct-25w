/**
 * Unit tests for annotatedLogic.js
 *
 * Run with: node --test src/components/adapt-abbott-annotated/test/annotatedLogic.test.js
 */

import { describe, it } from 'node:test';
import assert from 'node:assert/strict';

import {
  deriveNotesFromPassage,
  computeNextNoteState,
  computeNextVisitation,
  isAllVisited,
  getExpectedTrackableFields
} from '../js/annotatedLogic.js';

// =============================================================================
// deriveNotesFromPassage tests
// =============================================================================

describe('deriveNotesFromPassage', () => {

  it('extracts notes in order with contiguous indices', () => {
    const passage = [
      { text: 'Plain text.' },
      { text: 'Annotated one.', _note: { title: 'T1', body: 'B1' } },
      { text: 'More plain.' },
      { text: 'Annotated two.', _note: { title: 'T2', body: 'B2' } },
      { text: 'Annotated three.', _note: { title: 'T3', body: 'B3' } }
    ];

    const notes = deriveNotesFromPassage(passage);

    assert.equal(notes.length, 3);

    // Check contiguous noteIndex (0, 1, 2)
    assert.equal(notes[0].noteIndex, 0);
    assert.equal(notes[1].noteIndex, 1);
    assert.equal(notes[2].noteIndex, 2);

    // Check sourceIndex tracks original passage position
    assert.equal(notes[0].sourceIndex, 1);
    assert.equal(notes[1].sourceIndex, 3);
    assert.equal(notes[2].sourceIndex, 4);

    // Check content extracted correctly
    assert.equal(notes[0].text, 'Annotated one.');
    assert.equal(notes[0].title, 'T1');
    assert.equal(notes[0].body, 'B1');
  });

  it('handles passage with zero notes without crashing', () => {
    const passage = [
      { text: 'Plain text one.' },
      { text: 'Plain text two.' }
    ];

    const notes = deriveNotesFromPassage(passage);

    assert.equal(notes.length, 0);
    assert.deepEqual(notes, []);
  });

  it('handles empty passage', () => {
    assert.deepEqual(deriveNotesFromPassage([]), []);
  });

  it('handles null/undefined passage', () => {
    assert.deepEqual(deriveNotesFromPassage(null), []);
    assert.deepEqual(deriveNotesFromPassage(undefined), []);
  });

  it('handles minimum note count (1)', () => {
    const passage = [
      { text: 'Annotated.', _note: { title: 'T', body: 'B' } }
    ];

    const notes = deriveNotesFromPassage(passage);

    assert.equal(notes.length, 1);
    assert.equal(notes[0].noteIndex, 0);
    assert.equal(notes[0].sourceIndex, 0);
  });

  it('handles maximum note count (8)', () => {
    const passage = [];
    for (let i = 0; i < 8; i++) {
      passage.push({
        text: `Note ${i + 1}.`,
        _note: { title: `T${i + 1}`, body: `B${i + 1}` }
      });
    }

    const notes = deriveNotesFromPassage(passage);

    assert.equal(notes.length, 8);
    for (let i = 0; i < 8; i++) {
      assert.equal(notes[i].noteIndex, i);
      assert.equal(notes[i].sourceIndex, i);
    }
  });

  it('handles missing title/body gracefully', () => {
    const passage = [
      { text: 'Span.', _note: {} }
    ];

    const notes = deriveNotesFromPassage(passage);

    assert.equal(notes.length, 1);
    assert.equal(notes[0].title, '');
    assert.equal(notes[0].body, '');
  });

  it('handles missing text gracefully', () => {
    const passage = [
      { _note: { title: 'T', body: 'B' } }
    ];

    const notes = deriveNotesFromPassage(passage);

    assert.equal(notes.length, 1);
    assert.equal(notes[0].text, '');
  });

});

// =============================================================================
// computeNextNoteState tests (single-open, re-select closes)
// =============================================================================

describe('computeNextNoteState', () => {

  it('opens a note when none is expanded', () => {
    assert.equal(computeNextNoteState(null, 0), 0);
    assert.equal(computeNextNoteState(null, 2), 2);
  });

  it('switches to a different note (single-open)', () => {
    assert.equal(computeNextNoteState(0, 1), 1);
    assert.equal(computeNextNoteState(2, 0), 0);
  });

  it('closes the note when re-selected', () => {
    assert.equal(computeNextNoteState(0, 0), null);
    assert.equal(computeNextNoteState(3, 3), null);
  });

});

// =============================================================================
// computeNextVisitation tests
// =============================================================================

describe('computeNextVisitation', () => {

  it('marks unvisited note as visited on first expansion', () => {
    const visited = [false, false, false];
    const result = computeNextVisitation(visited, 1);

    assert.deepEqual(result, [false, true, false]);
  });

  it('is idempotent - already visited stays visited', () => {
    const visited = [true, false, false];
    const result = computeNextVisitation(visited, 0);

    assert.deepEqual(result, [true, false, false]);
  });

  it('does not mutate original array', () => {
    const visited = [false, false, false];
    const result = computeNextVisitation(visited, 0);

    assert.notStrictEqual(result, visited);
    assert.deepEqual(visited, [false, false, false]); // unchanged
    assert.deepEqual(result, [true, false, false]);
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
// isAllVisited tests
// =============================================================================

describe('isAllVisited', () => {

  it('returns true when all notes visited', () => {
    assert.equal(isAllVisited([true, true, true]), true);
    assert.equal(isAllVisited([true]), true);
  });

  it('returns false when some notes unvisited', () => {
    assert.equal(isAllVisited([true, false, true]), false);
    assert.equal(isAllVisited([false, false, false]), false);
  });

  it('returns false for empty array', () => {
    assert.equal(isAllVisited([]), false);
  });

  it('returns false for null/undefined', () => {
    assert.equal(isAllVisited(null), false);
    assert.equal(isAllVisited(undefined), false);
  });

  it('fires completion on last note', () => {
    // Simulate progression to last note
    let visited = [false, false, false];

    visited = computeNextVisitation(visited, 0);
    assert.equal(isAllVisited(visited), false);

    visited = computeNextVisitation(visited, 1);
    assert.equal(isAllVisited(visited), false);

    visited = computeNextVisitation(visited, 2); // last note
    assert.equal(isAllVisited(visited), true);
  });

});

// =============================================================================
// getExpectedTrackableFields tests
// =============================================================================

describe('getExpectedTrackableFields', () => {

  it('confirms _expandedIndex is transient (not in trackable)', () => {
    const fields = getExpectedTrackableFields();

    assert.ok(fields.transient.includes('_expandedIndex'));
    assert.ok(!fields.persisted.includes('_expandedIndex'));
  });

  it('confirms _userAnswer is persisted', () => {
    const fields = getExpectedTrackableFields();

    assert.ok(fields.persisted.includes('_userAnswer'));
  });

});
