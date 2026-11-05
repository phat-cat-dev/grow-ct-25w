import test from 'node:test';
import assert from 'node:assert/strict';
import {
  isValidResponse,
  resolveChoiceLabels,
  resolveStatusKey,
  buildPayload,
  parsePayload
} from '../js/pagefeedbackLogic.js';

test('isValidResponse accepts only the two known choices', () => {
  assert.equal(isValidResponse('helpful'), true);
  assert.equal(isValidResponse('needs-work'), true);
  assert.equal(isValidResponse('maybe'), false);
  assert.equal(isValidResponse(null), false);
  assert.equal(isValidResponse(undefined), false);
});

test('resolveChoiceLabels falls back to variant defaults when blank', () => {
  assert.deepEqual(
    resolveChoiceLabels('conversation', '', ''),
    { positive: 'Yes, it helped', negative: 'Not quite' }
  );
  assert.deepEqual(
    resolveChoiceLabels('growth', '', ''),
    { positive: 'That made sense', negative: 'I need more clarity' }
  );
  assert.deepEqual(
    resolveChoiceLabels('fieldnote', '', ''),
    { positive: 'Found what I needed', negative: 'Something is missing' }
  );
});

test('resolveChoiceLabels prefers author overrides over variant defaults', () => {
  assert.deepEqual(
    resolveChoiceLabels('conversation', 'Yes!', 'No.'),
    { positive: 'Yes!', negative: 'No.' }
  );
});

test('resolveChoiceLabels falls back to conversation for an unknown variant', () => {
  assert.deepEqual(
    resolveChoiceLabels('not-a-real-variant', '', ''),
    { positive: 'Yes, it helped', negative: 'Not quite' }
  );
});

test('resolveStatusKey maps explicit outcomes regardless of response state', () => {
  assert.equal(resolveStatusKey('saved', true), 'statusSaved');
  assert.equal(resolveStatusKey('failed', false), 'statusFailed');
  assert.equal(resolveStatusKey('cleared', false), 'statusCleared');
  assert.equal(resolveStatusKey('no-response', false), 'statusChooseFirst');
});

test('resolveStatusKey falls back on hasResponse when idle', () => {
  assert.equal(resolveStatusKey('idle', true), 'statusChosen');
  assert.equal(resolveStatusKey('idle', false), 'statusPrompt');
});

test('buildPayload shapes the persisted record', () => {
  assert.deepEqual(
    buildPayload('conversation', 'helpful', 'Great page'),
    { v: 'conversation', r: 'helpful', n: 'Great page' }
  );
  assert.deepEqual(
    buildPayload('growth', 'needs-work', undefined),
    { v: 'growth', r: 'needs-work', n: '' }
  );
});

test('parsePayload accepts the expected object shape', () => {
  assert.deepEqual(
    parsePayload({ v: 'conversation', r: 'helpful', n: 'Great page' }),
    { response: 'helpful', note: 'Great page' }
  );
});

test('parsePayload defaults a missing note to an empty string', () => {
  assert.deepEqual(
    parsePayload({ v: 'conversation', r: 'helpful' }),
    { response: 'helpful', note: '' }
  );
});

test('parsePayload nulls an invalid response rather than trusting it', () => {
  assert.deepEqual(
    parsePayload({ v: 'conversation', r: 'not-a-choice', n: 'x' }),
    { response: null, note: 'x' }
  );
});

test('parsePayload rejects non-object input', () => {
  assert.equal(parsePayload('a bare string'), null);
  assert.equal(parsePayload(null), null);
  assert.equal(parsePayload(undefined), null);
});
