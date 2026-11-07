/**
 * Unit tests for flipbuttonLogic — pure functions.
 * Run with: node --test test/flipbuttonLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual } from 'node:assert';
import { nextFlipped, ariaPressed } from '../js/flipbuttonLogic.js';

describe('nextFlipped', () => {
  it('flips an unflipped state to flipped', () => {
    strictEqual(nextFlipped(false), true);
  });
  it('flips a flipped state back to unflipped', () => {
    strictEqual(nextFlipped(true), false);
  });
});

describe('ariaPressed', () => {
  it('maps to the aria string', () => {
    strictEqual(ariaPressed(true), 'true');
    strictEqual(ariaPressed(false), 'false');
  });
});
