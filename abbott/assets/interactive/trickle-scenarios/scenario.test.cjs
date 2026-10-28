const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { validate } = require('./scenario.js');
const load = name => JSON.parse(fs.readFileSync(path.join(__dirname, `${name}.json`), 'utf8'));
test('all built-in scenarios and fill-in template validate', () => {
  for (const name of ['project-rescue', 'source-detective', 'support-conversation', 'team-conversation', 'scenario-template']) assert.doesNotThrow(() => validate(load(name)));
});
test('deep scaffold has eight possible routes, each eleven cards deep', () => {
  const data = load('scenario-template');
  const nodes = new Map(data.nodes.map(node => [node.id, node]));
  const lengths = [];
  function walk(id, depth) {
    const node = nodes.get(id);
    if (node.type === 'ending') lengths.push(depth);
    else if (node.type === 'choice') node.choices.forEach(choice => walk(choice.next, depth + 1));
    else walk(node.next, depth + 1);
  }
  walk(data.start, 1);
  assert.equal(lengths.length, 8);
  assert.ok(lengths.every(depth => depth === 11));
});
test('divergent example has four reachable endings and multiple path lengths', () => {
  const data = load('team-conversation');
  const nodes = new Map(data.nodes.map(node => [node.id, node]));
  const endings = new Set(), depths = new Set();
  function walk(id, depth) {
    const node = nodes.get(id);
    if (node.type === 'ending') { endings.add(id); depths.add(depth); }
    else if (node.type === 'choice') node.choices.forEach(choice => walk(choice.next, depth + 1));
    else walk(node.next, depth + 1);
  }
  walk(data.start, 1);
  assert.equal(endings.size, 4); assert.ok(depths.size > 1);
});
test('rejects invalid destinations, cycles, duplicate IDs and unreachable content', () => {
  let data = load('project-rescue'); data.nodes[0].next = 'missing';
  assert.throws(() => validate(data), /missing destination/);
  data = load('project-rescue'); data.nodes[0].next = data.start;
  assert.throws(() => validate(data), /cycle/);
  data = load('project-rescue'); data.nodes.push(data.nodes[0]);
  assert.throws(() => validate(data), /duplicate/);
  data = load('project-rescue'); data.nodes.push({ id: 'unused', type: 'ending', title: 'Unused', body: 'Unused.' });
  assert.throws(() => validate(data), /unreachable/);
});
test('checks timer bounds, choice counts, text and ending contracts', () => {
  let data = load('project-rescue'); data.nodes.find(node => node.type === 'auto').delayMs = 499;
  assert.throws(() => validate(data), /delayMs/);
  data = load('project-rescue'); data.nodes.find(node => node.type === 'choice').choices.pop();
  assert.throws(() => validate(data), /2-8/);
  data = load('project-rescue'); data.nodes[0].body = '';
  assert.throws(() => validate(data), /non-empty/);
  data = load('project-rescue'); data.nodes.at(-1).next = 'opening';
  assert.throws(() => validate(data), /ending cannot/);
});
