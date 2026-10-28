/**
 * Unit tests for modalLogic — pure functions.
 * Uses Node's built-in test runner (node:test + node:assert/strict).
 * Run with: node --test test/modalLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, deepStrictEqual } from 'node:assert';
import { sizeClass, resolveModal, trapWrapIndex } from '../js/modalLogic.js';

describe('sizeClass', () => {
  it('maps known sizes to modal-* classes', () => {
    strictEqual(sizeClass('sm'), 'modal-sm');
    strictEqual(sizeClass('lg'), 'modal-lg');
    strictEqual(sizeClass('xl'), 'modal-xl');
  });
  it('returns empty for unknown/empty', () => {
    strictEqual(sizeClass(''), '');
    strictEqual(sizeClass('huge'), '');
    strictEqual(sizeClass(undefined), '');
  });
});

describe('resolveModal', () => {
  const modals = [
    { _id: 'refs', title: 'References', body: '<p>list</p>', _size: 'lg', _isStatic: true }
  ];

  it('resolves a configured modal by id', () => {
    const out = resolveModal({ abModal: 'refs' }, modals);
    deepStrictEqual(out, {
      id: 'refs', title: 'References', body: '<p>list</p>',
      size: 'modal-lg', isStatic: true, isCentered: false, isScrollable: false
    });
  });

  it('lets inline data-* override the matched config', () => {
    const out = resolveModal({ abModal: 'refs', abModalTitle: 'Custom', abModalSize: 'sm' }, modals);
    strictEqual(out.title, 'Custom');
    strictEqual(out.size, 'modal-sm');
    strictEqual(out.body, '<p>list</p>'); // body still from config
  });

  it('builds an ad-hoc modal from inline attrs with no config', () => {
    const out = resolveModal({ abModal: '', abModalTitle: 'Hi', abModalBody: '<p>x</p>' }, []);
    strictEqual(out.id, null);
    strictEqual(out.title, 'Hi');
    strictEqual(out.body, '<p>x</p>');
  });

  it('returns null when there is no title and no body', () => {
    strictEqual(resolveModal({ abModal: 'missing' }, modals), null);
    strictEqual(resolveModal({}, []), null);
  });

  it('parses string boolean data-* attributes', () => {
    const out = resolveModal({ abModalTitle: 't', abModalStatic: 'true', abModalCentered: 'true' }, []);
    strictEqual(out.isStatic, true);
    strictEqual(out.isCentered, true);
    strictEqual(out.isScrollable, false);
  });
});

describe('trapWrapIndex', () => {
  it('wraps Tab off the last element to the first', () => {
    strictEqual(trapWrapIndex(2, 3, false), 0);
  });
  it('wraps Shift+Tab off the first element to the last', () => {
    strictEqual(trapWrapIndex(0, 3, true), 2);
  });
  it('does not wrap in the middle', () => {
    strictEqual(trapWrapIndex(1, 3, false), -1);
    strictEqual(trapWrapIndex(1, 3, true), -1);
  });
  it('keeps focus on a single focusable', () => {
    strictEqual(trapWrapIndex(0, 1, false), 0);
    strictEqual(trapWrapIndex(0, 1, true), 0);
  });
  it('returns -1 for an empty trap', () => {
    strictEqual(trapWrapIndex(-1, 0, false), -1);
  });
});
