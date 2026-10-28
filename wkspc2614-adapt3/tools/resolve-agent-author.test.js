'use strict';
const { test } = require('node:test');
const assert = require('node:assert');
const { resolveAgentAuthor } = require('./resolve-agent-author.js');

// a minimal block mirroring the live shape: baseline + context{all,byTier,empty reserved} + mode notes
const block = {
  agentAuthor: {
    content: 'BASE content',
    relation: 'BASE relation',
    warnings: ['BASE warn'],
    bestPractice: ['BASE bp'],
    context: {
      all: 'ALL context',
      byTier: {
        introductory: 'INTRO steer',
        advanced: { applies: false, note: 'omit at advanced' }
      },
      byQualifier: {},
      bySubject: {},
      byInstitution: {}
    }
  },
  agentAuthorWritten: { notes: ['WRITTEN note'] },
  agentAuthorDialogue: { notes: ['DIALOGUE note'] }
};

test('byTier string overrides baseline content; all + warnings + written note apply', () => {
  const r = resolveAgentAuthor(block, { tier: 'introductory' }, 'written');
  assert.equal(r.omit, false);
  assert.equal(r.content, 'INTRO steer');          // byTier overrode baseline
  assert.equal(r.context, 'ALL context');          // context.all applied
  assert.equal(r.relation, 'BASE relation');       // untouched baseline kept
  assert.deepEqual(r.warnings, ['BASE warn']);
  assert.deepEqual(r.modeNotes, ['WRITTEN note']);
  assert.ok(r.applied.includes('byTier.introductory'));
});

test('empty reserved steers contribute nothing (not read)', () => {
  const r = resolveAgentAuthor(block, { tier: 'introductory', subject: 'CAH17', institution: 'cardiffmet', qualifiers: ['widening'] }, 'written');
  // none of the reserved steers has a matching entry, so none appears in applied
  assert.ok(!r.applied.some(a => a.startsWith('bySubject') || a.startsWith('byQualifier') || a.startsWith('byInstitution')));
});

test('applies:false on the active tier omits the block', () => {
  const r = resolveAgentAuthor(block, { tier: 'advanced' }, 'written');
  assert.equal(r.omit, true);
});

test('dialogue mode selects the dialogue notes', () => {
  const r = resolveAgentAuthor(block, { tier: 'introductory' }, 'dialogue');
  assert.deepEqual(r.modeNotes, ['DIALOGUE note']);
});

test('a populated reserved steer, once set, applies and overrides', () => {
  const b2 = JSON.parse(JSON.stringify(block));
  b2.agentAuthor.context.bySubject = { CAH17: 'SUBJECT steer wins' };
  const r = resolveAgentAuthor(b2, { tier: 'introductory', subject: 'CAH17' }, 'written');
  assert.equal(r.content, 'SUBJECT steer wins'); // bySubject more specific than byTier
  assert.ok(r.applied.includes('bySubject.CAH17'));
});

test('no agentAuthor -> empty result, no omit', () => {
  const r = resolveAgentAuthor({}, { tier: 'introductory' }, 'written');
  assert.equal(r.omit, false);
  assert.equal(r.applied.length, 0);
});
