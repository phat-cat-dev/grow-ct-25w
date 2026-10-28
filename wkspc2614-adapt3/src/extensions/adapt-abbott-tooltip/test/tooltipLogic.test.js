/**
 * Unit tests for tooltipLogic.js
 *
 * Run with: node --test src/extensions/adapt-abbott-tooltip/test/tooltipLogic.test.js
 */

import { describe, it } from 'node:test';
import assert from 'node:assert/strict';

import { computePlacement } from '../js/tooltipLogic.js';

const VP = { width: 1000, height: 800 };
const BUB = { width: 200, height: 60 };

describe('computePlacement', () => {
  it('places above the trigger when there is room, centred horizontally', () => {
    // trigger mid-screen, plenty of room above
    const t = { top: 400, left: 500, width: 100, height: 20 };
    const { top, left, placement } = computePlacement(t, BUB, VP, 8);
    assert.equal(placement, 'top');
    assert.equal(top, 400 - 60 - 8);          // above with gap
    assert.equal(left, 550 - 100);            // centre (550) minus half bubble
  });

  it('flips below when there is not enough room above', () => {
    const t = { top: 10, left: 500, width: 100, height: 20 };
    const { top, placement } = computePlacement(t, BUB, VP, 8);
    assert.equal(placement, 'bottom');
    assert.equal(top, 10 + 20 + 8);           // below with gap
  });

  it('clamps to the left edge when the trigger is near the left', () => {
    const t = { top: 400, left: 0, width: 40, height: 20 };
    const { left } = computePlacement(t, BUB, VP, 8);
    assert.equal(left, 8);                    // min gap, not negative
  });

  it('clamps to the right edge when the trigger is near the right', () => {
    const t = { top: 400, left: 980, width: 20, height: 20 };
    const { left } = computePlacement(t, BUB, VP, 8);
    assert.equal(left, VP.width - BUB.width - 8); // 792, not off-screen
  });

  it('pins to the left gap when the bubble is wider than the viewport', () => {
    const narrow = { width: 320, height: 800 };
    const wide = { width: 400, height: 60 };
    const t = { top: 400, left: 100, width: 50, height: 20 };
    const { left } = computePlacement(t, wide, narrow, 8);
    assert.equal(left, 8);
  });

  it('when flipped below would overflow the bottom, clamps upward inside the viewport', () => {
    const shortVp = { width: 1000, height: 100 };
    const bigBub = { width: 200, height: 80 };
    // trigger near top (forces below) in a short viewport
    const t = { top: 4, left: 500, width: 100, height: 20 };
    const { top, placement } = computePlacement(t, bigBub, shortVp, 8);
    assert.equal(placement, 'bottom');
    assert.ok(top + bigBub.height + 8 <= shortVp.height + 0.001, 'bubble kept within viewport height');
    assert.ok(top >= 8, 'bubble kept below the top gap');
  });
});
