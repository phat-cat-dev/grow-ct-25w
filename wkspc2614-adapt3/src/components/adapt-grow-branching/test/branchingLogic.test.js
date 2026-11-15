/**
 * Unit tests for branchingLogic - the scenario navigation functions.
 * Uses Node's built-in test runner (node:test + node:assert/strict).
 * Run with: node --test test/branchingLogic.test.js
 */

import { describe, it } from 'node:test';
import { strictEqual, deepStrictEqual, ok } from 'node:assert';
import {
  getNode, isOutcome, choiceAt, nextNodeId, startNodeId, validateScenario
} from '../js/branchingLogic.js';

const scenario = {
  _start: 's1',
  _nodes: {
    s1: {
      body: 'A client calls about a late order.',
      _choices: [
        { text: 'Apologise at once', consequence: 'Calms them, but you have not checked.', _goto: 's2' },
        { text: 'Ask for the order number', consequence: 'You establish the facts.', _goto: 'good' }
      ]
    },
    s2: {
      body: 'They ask when it will arrive.',
      _choices: [
        { text: 'Promise a time you are unsure of', consequence: 'You risk breaking a second promise.', _goto: 'poor' },
        { text: 'Say you will check and call back', consequence: 'Honest and recoverable.', _goto: 'good' }
      ]
    },
    good: { body: 'Handled well.', _outcome: 'good' },
    poor: { body: 'This went badly.', _outcome: 'poor' }
  }
};

describe('getNode / startNodeId', () => {
  it('resolves a node by id', () => {
    strictEqual(getNode(scenario, 's1').body, 'A client calls about a late order.');
  });
  it('returns null for a missing node or bad input', () => {
    strictEqual(getNode(scenario, 'nope'), null);
    strictEqual(getNode(null, 's1'), null);
    strictEqual(getNode(scenario, null), null);
  });
  it('reads the start id', () => {
    strictEqual(startNodeId(scenario), 's1');
    strictEqual(startNodeId({}), null);
  });
});

describe('isOutcome', () => {
  it('is true only for outcome nodes', () => {
    strictEqual(isOutcome(getNode(scenario, 'good')), true);
    strictEqual(isOutcome(getNode(scenario, 's1')), false);
    strictEqual(isOutcome(null), false);
  });
});

describe('choiceAt / nextNodeId', () => {
  it('reads a choice and where it leads', () => {
    strictEqual(choiceAt(getNode(scenario, 's1'), 1).text, 'Ask for the order number');
    strictEqual(nextNodeId(getNode(scenario, 's1'), 1), 'good');
  });
  it('returns null out of range or on an outcome', () => {
    strictEqual(choiceAt(getNode(scenario, 's1'), 9), null);
    strictEqual(choiceAt(getNode(scenario, 'good'), 0), null);
    strictEqual(nextNodeId(getNode(scenario, 's1'), 9), null);
  });
});

describe('validateScenario', () => {
  it('passes a sound graph', () => {
    deepStrictEqual(validateScenario(scenario), []);
  });
  it('flags a missing start', () => {
    ok(validateScenario({ _start: 'x', _nodes: { good: { body: '', _outcome: 'good' } } })
      .some(p => p.includes('start node')));
  });
  it('flags a choice that points nowhere', () => {
    const bad = { _start: 's1', _nodes: { s1: { body: '', _choices: [{ text: 'a', consequence: 'b', _goto: 'ghost' }] } } };
    ok(validateScenario(bad).some(p => p.includes('missing node "ghost"')));
  });
  it('flags a decision node with no choices', () => {
    const bad = { _start: 's1', _nodes: { s1: { body: '' } } };
    ok(validateScenario(bad).some(p => p.includes('no choices')));
  });
});
