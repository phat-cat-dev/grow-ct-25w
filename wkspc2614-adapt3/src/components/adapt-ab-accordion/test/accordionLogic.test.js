/**
 * Unit tests for accordionLogic — pure functions.
 * Uses Node's built-in test runner (node:test + node:assert/strict).
 * Run with: node --test test/accordionLogic.test.js
 */

import { describe, it } from 'node:test';
import { deepStrictEqual } from 'node:assert';
import {
  computeNextOpenState,
  computeNextVisitation
} from '../js/accordionLogic.js';

describe('computeNextOpenState', () => {
  describe('single-open mode (isMultiSelect = false)', () => {
    it('opens a closed panel and closes the others', () => {
      const current = { 0: false, 1: false, 2: false };
      const next = computeNextOpenState(current, 1, false);
      deepStrictEqual(next, { 0: false, 1: true, 2: false });
    });

    it('closes the previously open panel when another opens', () => {
      const current = { 0: true, 1: false, 2: false };
      const next = computeNextOpenState(current, 2, false);
      deepStrictEqual(next, { 0: false, 1: false, 2: true });
    });

    it('toggles an open panel closed (leaving all closed)', () => {
      const current = { 0: false, 1: true, 2: false };
      const next = computeNextOpenState(current, 1, false);
      deepStrictEqual(next, { 0: false, 1: false, 2: false });
    });
  });

  describe('multi-open mode (isMultiSelect = true)', () => {
    it('opens a panel without closing the others', () => {
      const current = { 0: true, 1: false, 2: false };
      const next = computeNextOpenState(current, 1, true);
      deepStrictEqual(next, { 0: true, 1: true, 2: false });
    });

    it('toggles only the targeted panel', () => {
      const current = { 0: true, 1: true, 2: false };
      const next = computeNextOpenState(current, 0, true);
      deepStrictEqual(next, { 0: false, 1: true, 2: false });
    });
  });

  describe('forceOpen', () => {
    it('forces open regardless of current state', () => {
      const current = { 0: false, 1: false };
      const next = computeNextOpenState(current, 0, false, true);
      deepStrictEqual(next, { 0: true, 1: false });
    });

    it('forces closed regardless of current state', () => {
      const current = { 0: true, 1: false };
      const next = computeNextOpenState(current, 0, true, false);
      deepStrictEqual(next, { 0: false, 1: false });
    });
  });
});

describe('computeNextVisitation', () => {
  it('marks an item visited when opened', () => {
    deepStrictEqual(computeNextVisitation([false, false], 1, true), [false, true]);
  });

  it('does not un-set visitation when closed', () => {
    deepStrictEqual(computeNextVisitation([true, false], 0, false), [true, false]);
  });

  it('is idempotent on an already-visited item', () => {
    deepStrictEqual(computeNextVisitation([true, true], 0, true), [true, true]);
  });
});
