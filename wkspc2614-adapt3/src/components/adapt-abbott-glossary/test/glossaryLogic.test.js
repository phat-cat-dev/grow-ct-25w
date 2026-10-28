/**
 * Unit tests for glossaryLogic.js
 *
 * Run with: node --test src/components/adapt-abbott-glossary/test/glossaryLogic.test.js
 */

import { describe, it } from 'node:test';
import assert from 'node:assert/strict';

import {
  deriveTermsFromPassage,
  computeNextTermState,
  computeNextVisitation,
  isAllVisited,
  isTermCountValid,
  getExpectedTrackableFields
} from '../js/glossaryLogic.js';

// =============================================================================
// deriveTermsFromPassage tests
// =============================================================================

describe('deriveTermsFromPassage', () => {

  it('extracts terms in order with contiguous indices', () => {
    const passage = [
      { text: 'When you write an essay, ' },
      { text: 'referencing', _term: { term: 'reference', definition: 'Acknowledging sources.' } },
      { text: ' is essential. Your ' },
      { text: 'thesis', _term: { term: 'thesis', definition: 'The main argument.' } },
      { text: ' must be supported by ' },
      { text: 'evidence', _term: { term: 'evidence', definition: 'Facts supporting claims.' } }
    ];

    const terms = deriveTermsFromPassage(passage);

    assert.equal(terms.length, 3);

    // Check contiguous termIndex (0, 1, 2)
    assert.equal(terms[0].termIndex, 0);
    assert.equal(terms[1].termIndex, 1);
    assert.equal(terms[2].termIndex, 2);

    // Check sourceIndex tracks original passage position
    assert.equal(terms[0].sourceIndex, 1);
    assert.equal(terms[1].sourceIndex, 3);
    assert.equal(terms[2].sourceIndex, 5);

    // Check content extracted correctly
    assert.equal(terms[0].text, 'referencing');
    assert.equal(terms[0].term, 'reference');
    assert.equal(terms[0].definition, 'Acknowledging sources.');

    assert.equal(terms[1].text, 'thesis');
    assert.equal(terms[1].term, 'thesis');
    assert.equal(terms[1].definition, 'The main argument.');
  });

  it('handles passage with zero terms without crashing', () => {
    const passage = [
      { text: 'Plain text one.' },
      { text: 'Plain text two.' }
    ];

    const terms = deriveTermsFromPassage(passage);

    assert.equal(terms.length, 0);
    assert.deepEqual(terms, []);
  });

  it('handles empty passage', () => {
    assert.deepEqual(deriveTermsFromPassage([]), []);
  });

  it('handles null/undefined passage', () => {
    assert.deepEqual(deriveTermsFromPassage(null), []);
    assert.deepEqual(deriveTermsFromPassage(undefined), []);
  });

  it('handles minimum term count (2)', () => {
    const passage = [
      { text: 'term1', _term: { term: 'T1', definition: 'D1' } },
      { text: ' and ' },
      { text: 'term2', _term: { term: 'T2', definition: 'D2' } }
    ];

    const terms = deriveTermsFromPassage(passage);

    assert.equal(terms.length, 2);
    assert.equal(terms[0].termIndex, 0);
    assert.equal(terms[0].sourceIndex, 0);
    assert.equal(terms[1].termIndex, 1);
    assert.equal(terms[1].sourceIndex, 2);
  });

  it('handles maximum term count (8)', () => {
    const passage = [];
    for (let i = 0; i < 8; i++) {
      passage.push({
        text: `term${i + 1}`,
        _term: { term: `T${i + 1}`, definition: `D${i + 1}` }
      });
      if (i < 7) passage.push({ text: ', ' });
    }

    const terms = deriveTermsFromPassage(passage);

    assert.equal(terms.length, 8);
    for (let i = 0; i < 8; i++) {
      assert.equal(terms[i].termIndex, i);
    }
  });

  it('handles missing term/definition gracefully', () => {
    const passage = [
      { text: 'word', _term: {} }
    ];

    const terms = deriveTermsFromPassage(passage);

    assert.equal(terms.length, 1);
    assert.equal(terms[0].term, '');
    assert.equal(terms[0].definition, '');
  });

  it('handles missing text gracefully', () => {
    const passage = [
      { _term: { term: 'T', definition: 'D' } }
    ];

    const terms = deriveTermsFromPassage(passage);

    assert.equal(terms.length, 1);
    assert.equal(terms[0].text, '');
  });

  it('preserves difference between segment text and headword', () => {
    const passage = [
      { text: 'referencing', _term: { term: 'reference', definition: 'The act of citing.' } }
    ];

    const terms = deriveTermsFromPassage(passage);

    assert.equal(terms[0].text, 'referencing');  // What appears in prose
    assert.equal(terms[0].term, 'reference');    // The glossary headword
  });

});

// =============================================================================
// computeNextTermState tests (single-open, re-select closes)
// =============================================================================

describe('computeNextTermState', () => {

  it('opens a term when none is expanded', () => {
    assert.equal(computeNextTermState(null, 0), 0);
    assert.equal(computeNextTermState(null, 2), 2);
  });

  it('switches to a different term (single-open)', () => {
    assert.equal(computeNextTermState(0, 1), 1);
    assert.equal(computeNextTermState(2, 0), 0);
  });

  it('closes the term when re-selected', () => {
    assert.equal(computeNextTermState(0, 0), null);
    assert.equal(computeNextTermState(3, 3), null);
  });

});

// =============================================================================
// computeNextVisitation tests
// =============================================================================

describe('computeNextVisitation', () => {

  it('marks unvisited term as visited on first expansion', () => {
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

  it('returns true when all terms visited', () => {
    assert.equal(isAllVisited([true, true, true]), true);
    assert.equal(isAllVisited([true, true]), true);
  });

  it('returns false when some terms unvisited', () => {
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

  it('fires completion on last term', () => {
    // Simulate progression to last term
    let visited = [false, false, false];

    visited = computeNextVisitation(visited, 0);
    assert.equal(isAllVisited(visited), false);

    visited = computeNextVisitation(visited, 1);
    assert.equal(isAllVisited(visited), false);

    visited = computeNextVisitation(visited, 2); // last term
    assert.equal(isAllVisited(visited), true);
  });

});

// =============================================================================
// isTermCountValid tests (GL-8 bounds)
// =============================================================================

describe('isTermCountValid', () => {

  it('returns true for minimum valid count (2)', () => {
    assert.equal(isTermCountValid(2), true);
  });

  it('returns true for maximum valid count (8)', () => {
    assert.equal(isTermCountValid(8), true);
  });

  it('returns true for mid-range counts', () => {
    assert.equal(isTermCountValid(3), true);
    assert.equal(isTermCountValid(5), true);
    assert.equal(isTermCountValid(7), true);
  });

  it('returns false for count below minimum (0, 1)', () => {
    assert.equal(isTermCountValid(0), false);
    assert.equal(isTermCountValid(1), false);
  });

  it('returns false for count above maximum (9+)', () => {
    assert.equal(isTermCountValid(9), false);
    assert.equal(isTermCountValid(15), false);
  });

  it('returns false for non-integer values', () => {
    assert.equal(isTermCountValid(2.5), false);
    assert.equal(isTermCountValid(NaN), false);
    assert.equal(isTermCountValid(null), false);
    assert.equal(isTermCountValid(undefined), false);
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
