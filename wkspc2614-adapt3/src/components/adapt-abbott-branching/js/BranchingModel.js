/**
 * BranchingModel
 *
 * A multi-step decision-scenario engine. The scenario (`_scenario`) is a graph
 * of nodes (see branchingLogic.js); the learner starts at `_start` and walks it
 * one choice at a time until an outcome node is reached. Arbitrary depth.
 *
 * Extends ComponentModel (not ItemsComponentModel) - the choices are scenario
 * nodes, not Adapt child items. Transient navigation state (`_currentNode`,
 * `_pendingChoice`, `_path`) is held as plain model attributes and is NOT
 * tracked into suspend_data; completion fires when the first outcome is reached.
 */

import ComponentModel from 'core/js/models/componentModel';
import { getNode, isOutcome, choiceAt } from './branchingLogic';

export default class BranchingModel extends ComponentModel {

  init() {
    super.init?.();
    const scenario = this.get('_scenario') || {};
    this.set({
      _currentNode: scenario._start || null,
      _pendingChoice: null,
      _path: []
    });
  }

  getScenario() {
    return this.get('_scenario') || {};
  }

  getCurrentNode() {
    return getNode(this.getScenario(), this.get('_currentNode'));
  }

  /** The choice awaiting "Continue" (its consequence is showing), or null. */
  getPendingChoice() {
    const index = this.get('_pendingChoice');
    if (index == null) return null;
    return choiceAt(this.getCurrentNode(), index);
  }

  isAtOutcome() {
    return isOutcome(this.getCurrentNode());
  }

  /**
   * Pick a choice on the current node. Does not advance yet - it records the
   * choice so the view can show its consequence before the learner continues.
   */
  choose(index) {
    if (this.get('_pendingChoice') != null) return;
    if (!choiceAt(this.getCurrentNode(), index)) return;
    this.set('_pendingChoice', index);
  }

  /** Advance from the pending choice to the node it leads to. */
  advance() {
    const choice = this.getPendingChoice();
    if (!choice) return;
    const path = [...(this.get('_path') || []), this.get('_currentNode')];
    this.set({
      _path: path,
      _currentNode: choice._goto || this.get('_currentNode'),
      _pendingChoice: null
    });
    if (this.isAtOutcome()) this.setCompletionStatus();
  }

  /** Return to the start to try a different route. */
  restart() {
    this.set({
      _currentNode: this.getScenario()._start || null,
      _pendingChoice: null,
      _path: []
    });
  }

}
