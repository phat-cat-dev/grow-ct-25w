/**
 * Unit tests for collapseLogic — pure functions.
 * Run with: node --test test/collapseLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, deepStrictEqual } from 'node:assert';
import { resolveCollapse, ariaExpanded } from '../js/collapseLogic.js';

describe('resolveCollapse', () => {
  it('reads a target selector', () => {
    deepStrictEqual(resolveCollapse({ abCollapse: '#more' }), { selector: '#more', parent: null });
  });
  it('reads an accordion parent', () => {
    deepStrictEqual(resolveCollapse({ abCollapse: '#p1', abCollapseParent: '#faq' }), { selector: '#p1', parent: '#faq' });
  });
  it('treats empty / "true" as no selector', () => {
    strictEqual(resolveCollapse({ abCollapse: '' }).selector, null);
    strictEqual(resolveCollapse({ abCollapse: 'true' }).selector, null);
  });
  it('handles a missing attribute', () => {
    deepStrictEqual(resolveCollapse({}), { selector: null, parent: null });
  });
});

describe('ariaExpanded', () => {
  it('maps to the aria string', () => {
    strictEqual(ariaExpanded(true), 'true');
    strictEqual(ariaExpanded(false), 'false');
  });
});
