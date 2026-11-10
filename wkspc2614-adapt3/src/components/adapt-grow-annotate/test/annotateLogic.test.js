/**
 * Unit tests for annotateLogic (passage parsing + annotation state).
 * Run with: node --test test/annotateLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, deepStrictEqual } from 'node:assert';
import {
  parsePassage, applyTool, annotationCount, isComplete, toUserAnswer, fromUserAnswer, markAnswers
} from '../js/annotateLogic.js';

describe('parsePassage', () => {
  it('returns a single text segment when there are no targets', () => {
    const { segments, keys } = parsePassage('just plain text');
    deepStrictEqual(segments, [{ type: 'text', text: 'just plain text' }]);
    deepStrictEqual(keys, []);
  });

  it('splits text around a single target and auto-keys it', () => {
    const { segments, keys } = parsePassage('A [[landscape]] needs depth.');
    deepStrictEqual(segments, [
      { type: 'text', text: 'A ' },
      { type: 'target', text: 'landscape', key: 't0' },
      { type: 'text', text: ' needs depth.' }
    ]);
    deepStrictEqual(keys, ['t0']);
  });

  it('honours an explicit key', () => {
    const { segments, keys } = parsePassage('the [[horizon|hz]] line');
    strictEqual(segments[1].key, 'hz');
    deepStrictEqual(keys, ['hz']);
  });

  it('handles adjacent targets with sequential auto keys', () => {
    const { keys } = parsePassage('[[a]][[b]]');
    deepStrictEqual(keys, ['t0', 't1']);
  });

  it('auto-keys by target order even when some keys are explicit', () => {
    const { keys } = parsePassage('[[a|x]] and [[b]]');
    deepStrictEqual(keys, ['x', 't1']);
  });

  it('keeps an empty target as literal text', () => {
    const { segments, keys } = parsePassage('keep [[]] me');
    deepStrictEqual(segments, [{ type: 'text', text: 'keep [[]] me' }]);
    deepStrictEqual(keys, []);
  });

  it('leaves stray single brackets as text', () => {
    const { keys } = parsePassage('an array[0] and [a thought]');
    deepStrictEqual(keys, []);
  });

  it('tolerates empty / nullish input', () => {
    deepStrictEqual(parsePassage('').segments, []);
    deepStrictEqual(parsePassage(null).segments, []);
  });
});

describe('applyTool', () => {
  it('applies a tool to a key', () => {
    deepStrictEqual(applyTool({}, 't0', 'idea'), { t0: 'idea' });
  });
  it('toggles the same tool off', () => {
    deepStrictEqual(applyTool({ t0: 'idea' }, 't0', 'idea'), {});
  });
  it('replaces with a different tool', () => {
    deepStrictEqual(applyTool({ t0: 'idea' }, 't0', 'doubt'), { t0: 'doubt' });
  });
  it('clears with a null/empty tool', () => {
    deepStrictEqual(applyTool({ t0: 'idea' }, 't0', null), {});
    deepStrictEqual(applyTool({ t0: 'idea' }, 't0', ''), {});
  });
  it('does not mutate the input', () => {
    const before = { t0: 'idea' };
    applyTool(before, 't1', 'doubt');
    deepStrictEqual(before, { t0: 'idea' });
  });
});

describe('annotationCount / isComplete', () => {
  it('counts annotated targets', () => {
    strictEqual(annotationCount({ t0: 'idea', t1: 'doubt' }), 2);
    strictEqual(annotationCount({}), 0);
  });
  it('is complete at or above the minimum', () => {
    strictEqual(isComplete({ t0: 'idea' }, 1), true);
    strictEqual(isComplete({}, 1), false);
    strictEqual(isComplete({ t0: 'idea', t1: 'doubt' }, 2), true);
  });
  it('a minimum of 0 is complete immediately', () => {
    strictEqual(isComplete({}, 0), true);
  });
});

describe('toUserAnswer / fromUserAnswer', () => {
  const keys = ['t0', 't1', 'hz'];

  it('serialises aligned to target order, blanks for unannotated', () => {
    deepStrictEqual(toUserAnswer({ t0: 'idea', hz: 'doubt' }, keys), ['idea', '', 'doubt']);
  });

  it('round-trips through serialise/deserialise', () => {
    const state = { t1: 'idea', hz: 'doubt' };
    deepStrictEqual(fromUserAnswer(toUserAnswer(state, keys), keys), state);
  });

  it('deserialising junk yields empty state', () => {
    deepStrictEqual(fromUserAnswer(null, keys), {});
    deepStrictEqual(fromUserAnswer(['idea'], null), {});
  });
});

describe('markAnswers (question mode)', () => {
  const keys = ['t0', 't1', 't2'];
  const answers = ['claim', 'evidence', 'hedge'];

  it('marks every scored target correct', () => {
    const r = markAnswers({ t0: 'claim', t1: 'evidence', t2: 'hedge' }, keys, answers);
    strictEqual(r.correctCount, 3);
    strictEqual(r.total, 3);
    strictEqual(r.allCorrect, true);
  });

  it('counts a wrong tool and an unmarked target as incorrect', () => {
    const r = markAnswers({ t0: 'claim', t2: 'claim' }, keys, answers);
    strictEqual(r.correctCount, 1);
    strictEqual(r.total, 3);
    strictEqual(r.allCorrect, false);
    strictEqual(r.marks[1].isCorrect, false); // t1 left unmarked
    strictEqual(r.marks[2].isCorrect, false); // t2 marked with the wrong tool
  });

  it('does not score a target that has no answer', () => {
    const r = markAnswers({ t0: 'claim' }, keys, ['claim', '', '']);
    strictEqual(r.total, 1);
    strictEqual(r.allCorrect, true);
    strictEqual(r.marks[1].isScored, false);
  });
});
