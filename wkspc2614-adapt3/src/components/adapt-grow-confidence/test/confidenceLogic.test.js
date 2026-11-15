/**
 * Unit tests for confidenceLogic — CD-3 (classifyItem) and CD-4 (selectSummary).
 * Uses Node's built-in test runner (node:test + node:assert/strict).
 * Run with: node --test test/confidenceLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, throws } from 'node:assert';
import { classifyItem, selectSummary } from '../js/confidenceLogic.js';

describe('classifyItem (CD-3)', () => {
  // Dropped — any downward move, checked FIRST (even within high band)
  it('(5,4) -> dropped (drop within high band — honoured, not "stayed high")', () => {
    strictEqual(classifyItem(5, 4), 'dropped');
  });
  it('(3,2) -> dropped', () => {
    strictEqual(classifyItem(3, 2), 'dropped');
  });
  it('(5,1) -> dropped', () => {
    strictEqual(classifyItem(5, 1), 'dropped');
  });

  // Rose — any upward move, band-agnostic
  it('(1,2) -> rose (up but still low)', () => {
    strictEqual(classifyItem(1, 2), 'rose');
  });
  it('(2,5) -> rose', () => {
    strictEqual(classifyItem(2, 5), 'rose');
  });
  it('(3,4) -> rose', () => {
    strictEqual(classifyItem(3, 4), 'rose');
  });

  // Stayed high — same rating in high band (4-5)
  it('(4,4) -> stayedHigh', () => {
    strictEqual(classifyItem(4, 4), 'stayedHigh');
  });
  it('(5,5) -> stayedHigh', () => {
    strictEqual(classifyItem(5, 5), 'stayedHigh');
  });

  // Stayed low — same rating in low band (1-2)
  it('(1,1) -> stayedLow', () => {
    strictEqual(classifyItem(1, 1), 'stayedLow');
  });
  it('(2,2) -> stayedLow', () => {
    strictEqual(classifyItem(2, 2), 'stayedLow');
  });

  // No movement — same rating in mid band (3)
  it('(3,3) -> noMovement', () => {
    strictEqual(classifyItem(3, 3), 'noMovement');
  });

  // Invalid inputs throw
  it('(0,3) throws — pre out of range', () => {
    throws(() => classifyItem(0, 3), /ratings must be integers 1-5/);
  });
  it('(3,6) throws — post out of range', () => {
    throws(() => classifyItem(3, 6), /ratings must be integers 1-5/);
  });
  it('(null,3) throws — null', () => {
    throws(() => classifyItem(null, 3), /ratings must be integers 1-5/);
  });
  it('(3,3.5) throws — non-integer', () => {
    throws(() => classifyItem(3, 3.5), /ratings must be integers 1-5/);
  });
});

describe('selectSummary (CD-4)', () => {
  // Predominantly up — no attention items
  it('all rose -> _predominantlyUp', () => {
    strictEqual(selectSummary(['rose', 'rose', 'rose', 'rose', 'rose']), '_predominantlyUp');
  });
  it('rose + noMovement (a=0, p=4) -> _predominantlyUp', () => {
    strictEqual(selectSummary(['rose', 'rose', 'rose', 'rose', 'noMovement']), '_predominantlyUp');
  });
  it('stayedHigh + noMovement (a=0, p=2) -> _predominantlyUp', () => {
    strictEqual(selectSummary(['stayedHigh', 'stayedHigh', 'noMovement']), '_predominantlyUp');
  });

  // Flat or low — all neutral OR attention > positive
  it('all noMovement (all neutral) -> _flatOrLow', () => {
    strictEqual(selectSummary(['noMovement', 'noMovement', 'noMovement', 'noMovement', 'noMovement']), '_flatOrLow');
  });
  it('a=3, p=2 (attention > positive) -> _flatOrLow', () => {
    strictEqual(selectSummary(['rose', 'rose', 'dropped', 'dropped', 'dropped']), '_flatOrLow');
  });
  it('all dropped -> _flatOrLow', () => {
    strictEqual(selectSummary(['dropped', 'dropped', 'dropped', 'dropped', 'dropped']), '_flatOrLow');
  });

  // Mixed — attention present but attention <= positive
  it('a=2, p=3 (attention <= positive) -> _mixed', () => {
    strictEqual(selectSummary(['rose', 'rose', 'rose', 'dropped', 'dropped']), '_mixed');
  });
  it('a=1, p=1 (attention == positive) -> _mixed', () => {
    strictEqual(selectSummary(['rose', 'stayedLow']), '_mixed');
  });
  it('a=1, p=3 -> _mixed', () => {
    strictEqual(selectSummary(['stayedHigh', 'stayedHigh', 'stayedHigh', 'stayedLow', 'noMovement']), '_mixed');
  });
});
