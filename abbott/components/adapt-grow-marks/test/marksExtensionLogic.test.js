/**
 * Unit tests for the grow-marks extension config logic.
 * Run with: node --test test/marksExtensionLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, deepStrictEqual } from 'node:assert';
import {
  DEFAULT_FEEDBACK, isGloballyEnabled, isFeedbackEnabled, resolveFeedbackMark
} from '../js/marksExtensionLogic.js';

describe('isGloballyEnabled', () => {
  it('is on when there is no course config', () => {
    strictEqual(isGloballyEnabled(undefined), true);
    strictEqual(isGloballyEnabled(null), true);
  });
  it('is on unless explicitly disabled', () => {
    strictEqual(isGloballyEnabled({}), true);
    strictEqual(isGloballyEnabled({ _isEnabled: true }), true);
    strictEqual(isGloballyEnabled({ _isEnabled: false }), false);
  });
});

describe('isFeedbackEnabled', () => {
  it('is off by default (opt-in per component)', () => {
    strictEqual(isFeedbackEnabled(undefined), false);
    strictEqual(isFeedbackEnabled({}), false);
    strictEqual(isFeedbackEnabled({ _feedback: {} }), false);
  });
  it('is on only when _feedback._isEnabled is true', () => {
    strictEqual(isFeedbackEnabled({ _feedback: { _isEnabled: true } }), true);
  });
  it('a disabled component config overrides feedback', () => {
    strictEqual(isFeedbackEnabled({ _isEnabled: false, _feedback: { _isEnabled: true } }), false);
  });
});

describe('resolveFeedbackMark', () => {
  it('uses the defaults when nothing is overridden', () => {
    deepStrictEqual(resolveFeedbackMark(true, { _feedback: { _isEnabled: true } }), DEFAULT_FEEDBACK.correct);
    deepStrictEqual(resolveFeedbackMark(false, { _feedback: { _isEnabled: true } }), DEFAULT_FEEDBACK.incorrect);
  });
  it('honours per-outcome overrides', () => {
    const cfg = { _feedback: { _isEnabled: true, _correct: { _mark: 'star', _color: 'neutral' }, _incorrect: { _mark: 'scribble' } } };
    deepStrictEqual(resolveFeedbackMark(true, cfg), { mark: 'star', color: 'neutral' });
    // incorrect overrides mark only; colour falls back to the default
    deepStrictEqual(resolveFeedbackMark(false, cfg), { mark: 'scribble', color: 'negative' });
  });
  it('falls back cleanly with no config at all', () => {
    deepStrictEqual(resolveFeedbackMark(true, null), DEFAULT_FEEDBACK.correct);
  });
});
