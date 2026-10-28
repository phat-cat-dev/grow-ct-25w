/**
 * branchingLogic.js
 *
 * Pure navigation functions for the branching scenario engine. A scenario is a
 * directed graph of nodes; each node is either a DECISION (has `_choices`, each
 * with a `_goto` node id) or an OUTCOME (has `_outcome`: 'good' | 'poor' |
 * 'neutral'). Navigation starts at `_scenario._start` and ends when an outcome
 * node is reached. Arbitrary depth - a choice leads to another decision node.
 *
 * Extracted for testability without Backbone/DOM. Design ref: BB-3 (unit tests).
 */

/** The node object for an id, or null. */
export function getNode(scenario, id) {
  if (!scenario || !scenario._nodes || id == null) return null;
  return scenario._nodes[id] || null;
}

/** True when a node is an ending (carries an `_outcome`). */
export function isOutcome(node) {
  return !!(node && node._outcome);
}

/** The choice object at an index on a node, or null. */
export function choiceAt(node, index) {
  if (!node || !Array.isArray(node._choices)) return null;
  return node._choices[index] || null;
}

/** The node id a choice leads to, or null. */
export function nextNodeId(node, index) {
  const choice = choiceAt(node, index);
  return choice ? (choice._goto || null) : null;
}

/** The start node id of a scenario, or null. */
export function startNodeId(scenario) {
  return (scenario && scenario._start) || null;
}

/**
 * Validate a scenario graph: every choice `_goto` must resolve to a real node,
 * the start must exist, and every path must be able to reach an outcome (no
 * dead decision node with no choices). Returns a list of problem strings (empty
 * when the graph is sound). Used by tests and as an authoring guard.
 */
export function validateScenario(scenario) {
  const problems = [];
  if (!scenario || !scenario._nodes) { problems.push('no _nodes'); return problems; }
  const start = startNodeId(scenario);
  if (!getNode(scenario, start)) problems.push(`start node "${start}" is missing`);
  Object.keys(scenario._nodes).forEach(id => {
    const node = scenario._nodes[id];
    if (isOutcome(node)) return;
    const choices = Array.isArray(node._choices) ? node._choices : [];
    if (!choices.length) { problems.push(`decision node "${id}" has no choices`); return; }
    choices.forEach((choice, i) => {
      if (!choice._goto) problems.push(`node "${id}" choice ${i} has no _goto`);
      else if (!getNode(scenario, choice._goto)) problems.push(`node "${id}" choice ${i} points to missing node "${choice._goto}"`);
    });
  });
  return problems;
}
