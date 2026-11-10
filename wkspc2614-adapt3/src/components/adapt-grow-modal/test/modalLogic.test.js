import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { resolveCompletionMode, buildPopupOptions, COMPLETION } from '../js/modalLogic.js';

describe('resolveCompletionMode', () => {
  test('defaults unknown/undefined to trigger', () => {
    assert.equal(resolveCompletionMode(undefined), COMPLETION.TRIGGER);
    assert.equal(resolveCompletionMode('nonsense'), COMPLETION.TRIGGER);
    assert.equal(resolveCompletionMode(''), COMPLETION.TRIGGER);
  });
  test('passes through view and none', () => {
    assert.equal(resolveCompletionMode('view'), COMPLETION.VIEW);
    assert.equal(resolveCompletionMode('none'), COMPLETION.NONE);
  });
  test('passes through explicit trigger', () => {
    assert.equal(resolveCompletionMode('trigger'), COMPLETION.TRIGGER);
  });
});

describe('buildPopupOptions', () => {
  test('defaults empty popup, always namespaced + cancellable', () => {
    const o = buildPopupOptions();
    assert.equal(o.title, '');
    assert.equal(o.body, '');
    assert.equal(o._classes, 'cm-notify cm-modal');
    assert.equal(o._isCancellable, true);
  });
  test('carries title/body and appends author classes', () => {
    const o = buildPopupOptions({ title: 'T', body: '<p>B</p>', _classes: 'extra wide' });
    assert.equal(o.title, 'T');
    assert.equal(o.body, '<p>B</p>');
    assert.equal(o._classes, 'cm-notify cm-modal extra wide');
  });
  test('honours _isCancellable:false, keeps true otherwise', () => {
    assert.equal(buildPopupOptions({ _isCancellable: false })._isCancellable, false);
    assert.equal(buildPopupOptions({ _isCancellable: true })._isCancellable, true);
    assert.equal(buildPopupOptions({})._isCancellable, true);
  });
  test('custom base classes', () => {
    assert.equal(buildPopupOptions({ _classes: 'x' }, 'base')._classes, 'base x');
  });
});
