/**
 * TimelineModel
 *
 * Model for the timeline component. Extends ItemsComponentModel for
 * per-item visitation tracking and completion-when-all-visited.
 *
 * NOT a question component — no marking, no _recordInteraction, no response
 * semantics. The base class's _userAnswer array (storing visitation booleans)
 * is legitimate persistence plumbing and stays intact.
 *
 * _isExpanded is per-item transient state — NOT in trackable(), so it never
 * enters suspend_data. On revisit, all stages present collapsed;
 * completion restores via the base class's visitation mechanism.
 *
 * Design refs: TL-1 (schema), TB-2 (model), TL-4 (single-default behaviour)
 */

import ItemsComponentModel from 'core/js/models/itemsComponentModel';
import { computeNextExpandedState, computeNextVisitation } from './timelineLogic';

export default class TimelineModel extends ItemsComponentModel {

  /**
   * Default values.
   * Note: _expandBehaviour defaults to 'single' (unlike flipcard's 'independent')
   * to keep the overview scannable — deliberately inverted per TL-4.
   */
  defaults() {
    return {
      ...super.defaults(),
      _expandBehaviour: 'single'
    };
  }

  /**
   * Toggle the expanded state of a stage by its index.
   *
   * Delegates decision logic to pure functions (timelineLogic.js) for testability.
   * - In 'single' mode (default): expanding one stage collapses others.
   * - In 'independent' mode: toggles just that stage's _isExpanded.
   *
   * On first expand, marks the item as visited (base class handles completion).
   *
   * @param {number} index - The item index to toggle
   */
  toggleItemExpanded(index) {
    const children = this.getChildren();
    const item = this.getItem(index);
    if (!item) return;

    // Extract current expanded state map from Backbone models
    const currentExpandedMap = {};
    children.forEach((child, idx) => {
      currentExpandedMap[idx] = !!child.get('_isExpanded');
    });

    // Compute next expanded state via pure function
    const behaviour = this.get('_expandBehaviour') || 'single';
    const nextExpandedMap = computeNextExpandedState(currentExpandedMap, index, behaviour);

    // Apply expanded state changes back to Backbone models
    children.forEach((child, idx) => {
      const newState = !!nextExpandedMap[idx];
      if (child.get('_isExpanded') !== newState) {
        child.set('_isExpanded', newState);
      }
    });

    // Extract current visitation array
    const currentVisited = children.map(child => !!child.get('_isVisited'));

    // Compute next visitation via pure function
    const newExpandedState = nextExpandedMap[index];
    const nextVisited = computeNextVisitation(currentVisited, index, newExpandedState);

    // Apply visitation change (only for this item, idempotent)
    if (nextVisited[index] && !item.get('_isVisited')) {
      item.set('_isVisited', true);
    }
  }

  /**
   * Get the expanded state of a stage by index.
   * @param {number} index
   * @returns {boolean}
   */
  isItemExpanded(index) {
    const item = this.getItem(index);
    return item ? !!item.get('_isExpanded') : false;
  }

  /**
   * Check if any items have detail graphics (for imageReady handling).
   * @returns {boolean}
   */
  hasAnyDetailGraphics() {
    return this.getChildren().some(item => {
      const graphic = item.get('_graphic') || {};
      return !!graphic.src;
    });
  }

  /**
   * Reset on revisit — base class handles _isVisited restoration.
   * We just need to ensure _isExpanded is reset (stages collapsed on revisit).
   */
  checkIfResetOnRevisit() {
    const isResetOnRevisit = this.get('_isResetOnRevisit');
    if (!isResetOnRevisit) return;

    // Reset all stages to collapsed
    this.getChildren().forEach(item => {
      item.set('_isExpanded', false);
    });

    // Let base class handle its reset
    super.checkIfResetOnRevisit?.();
  }

}
