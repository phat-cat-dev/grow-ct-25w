/**
 * Unit tests for closeLogic — pure functions.
 * Uses Node's built-in test runner (node:test + node:assert/strict).
 * Run with: node --test test/closeLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, deepStrictEqual } from 'node:assert';
import { resolveDismiss, toMs } from '../js/closeLogic.js';

describe('resolveDismiss', () => {
  it('defaults: nearest ancestor, remove, 200ms fade', () => {
    deepStrictEqual(resolveDismiss({ abDismiss: '' }), { selector: null, remove: true, fadeMs: 200 });
  });
  it('treats "true" as "nearest ancestor" (no selector)', () => {
    strictEqual(resolveDismiss({ abDismiss: 'true' }).selector, null);
  });
  it('uses a selector value', () => {
    strictEqual(resolveDismiss({ abDismiss: '#notice-1' }).selector, '#notice-1');
  });
  it('remove=false keeps the element', () => {
    strictEqual(resolveDismiss({ abDismiss: '', abDismissRemove: 'false' }).remove, false);
  });
  it('reads a custom fade, and 0 disables it', () => {
    strictEqual(resolveDismiss({ abDismiss: '', abDismissFade: '350' }).fadeMs, 350);
    strictEqual(resolveDismiss({ abDismiss: '', abDismissFade: '0' }).fadeMs, 0);
  });
});

describe('toMs', () => {
  it('falls back on empty/undefined', () => {
    strictEqual(toMs(undefined, 200), 200);
    strictEqual(toMs('', 200), 200);
  });
  it('parses valid non-negative integers', () => {
    strictEqual(toMs('0', 200), 0);
    strictEqual(toMs('500', 200), 500);
  });
  it('falls back on invalid or negative', () => {
    strictEqual(toMs('abc', 200), 200);
    strictEqual(toMs('-5', 200), 200);
  });
});
