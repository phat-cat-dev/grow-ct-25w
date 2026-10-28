/**
 * Unit tests for toastLogic — pure functions.
 * Run with: node --test test/toastLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, deepStrictEqual } from 'node:assert';
import { resolveToast, toDelay } from '../js/toastLogic.js';

describe('toDelay', () => {
  it('falls back on empty/undefined', () => {
    strictEqual(toDelay(undefined, 5000), 5000);
    strictEqual(toDelay('', 5000), 5000);
  });
  it('parses non-negative integers', () => {
    strictEqual(toDelay('0', 5000), 0);
    strictEqual(toDelay(3000, 5000), 3000);
  });
  it('falls back on invalid/negative', () => {
    strictEqual(toDelay('x', 5000), 5000);
    strictEqual(toDelay(-1, 5000), 5000);
  });
});

describe('resolveToast', () => {
  it('defaults: autohide, 5000ms, close shown, no variant', () => {
    deepStrictEqual(resolveToast({ title: 'Hi' }), {
      id: null, title: 'Hi', body: '', variant: '',
      autohide: true, delay: 5000, showClose: true
    });
  });
  it('keeps a known variant and custom delay', () => {
    const t = resolveToast({ body: 'x', variant: 'success', delay: 2000 });
    strictEqual(t.variant, 'success');
    strictEqual(t.delay, 2000);
  });
  it('drops an unknown variant', () => {
    strictEqual(resolveToast({ title: 'x', variant: 'purple' }).variant, '');
  });
  it('honours autohide:false and showClose:false', () => {
    const t = resolveToast({ title: 'x', autohide: false, showClose: false });
    strictEqual(t.autohide, false);
    strictEqual(t.showClose, false);
  });
});
