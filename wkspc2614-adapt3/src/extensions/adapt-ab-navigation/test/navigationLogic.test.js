/**
 * Unit tests for navigationLogic — pure functions.
 * Run with: node --test test/navigationLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, deepStrictEqual } from 'node:assert';
import { normaliseItems, insertionIndex } from '../js/navigationLogic.js';

describe('normaliseItems', () => {
  it('normalises label/icon/order/action and defaults order', () => {
    const out = normaliseItems([
      { label: 'Glossary', _icon: 'icon-search', _order: 95, _abModal: 'glossary' },
      { title: 'Home', _url: '#/' }
    ]);
    strictEqual(out.length, 2);
    deepStrictEqual(out[0], { label: 'Glossary', icon: 'icon-search', order: 95, url: '', event: '', abModal: 'glossary', classes: '' });
    strictEqual(out[1].label, 'Home');
    strictEqual(out[1].url, '#/');
  });
  it('drops items with no action', () => {
    strictEqual(normaliseItems([{ label: 'Nope' }]).length, 0);
  });
  it('drops items with no label and no icon', () => {
    strictEqual(normaliseItems([{ _url: '#/' }]).length, 0);
  });
  it('falls back to a computed order when absent', () => {
    const out = normaliseItems([{ label: 'A', _event: 'x' }, { label: 'B', _event: 'y' }]);
    strictEqual(out[0].order, 50);
    strictEqual(out[1].order, 51);
  });
});

describe('insertionIndex', () => {
  it('inserts before the first larger order', () => {
    strictEqual(insertionIndex([0, 90, 100], 95), 2);
  });
  it('inserts at the end when largest', () => {
    strictEqual(insertionIndex([0, 90], 100), 2);
  });
  it('inserts at the start when smallest', () => {
    strictEqual(insertionIndex([0, 90], -100), 0);
  });
  it('handles an empty bar', () => {
    strictEqual(insertionIndex([], 50), 0);
  });
});
