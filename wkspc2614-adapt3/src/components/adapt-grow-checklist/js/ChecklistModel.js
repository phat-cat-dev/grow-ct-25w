/**
 * ChecklistModel
 *
 * Model for the checklist component. Extends ItemsComponentModel.
 *
 * NOT a question component - no marking, no _recordInteraction, no response
 * semantics. The base class's _userAnswer array (storing visitation booleans)
 * is legitimate persistence plumbing and stays intact.
 *
 * _isChecked is TRANSIENT - not persisted to SCORM. Tick state resets on
 * every visit; the fact the learner worked through the checklist persists
 * via the base's _userAnswer visitation array.
 *
 * Visitation is ONE-WAY: first tick marks the item visited permanently for
 * the session; tick state toggles freely thereafter. Once completion fires
 * it stays. (CL-4)
 *
 * Design refs: CL-1 (schema), CL-2 (ephemeral ticks), CL-3 (completion),
 *              CL-4 (untick does not unvisit), CB-2 (model)
 */

import ItemsComponentModel from 'core/js/models/itemsComponentModel';
import {
  computeNextCheckedState,
  computeNextVisitation,
  isAllVisited,
  countChecked,
  getExpectedTrackableFields
} from './checklistLogic';

export default class ChecklistModel extends ItemsComponentModel {

  /**
   * Initialize the model.
   *
   * Sets up the checked state map (transient) and restores visitation
   * from persisted _userAnswer if available.
   */
  init() {
    super.init();

    // Initialize transient checked state for each item (all unchecked)
    const items = this.getChildren();
    const checkedMap = {};
    items.forEach((item, index) => {
      checkedMap[index] = false;
    });
    this._checkedMap = checkedMap;
  }

  /**
   * Toggle an item's checked state.
   *
   * Checked state is ephemeral. However, the FIRST tick marks the item
   * as visited (one-way). Subsequent toggles do not affect visitation.
   *
   * @param {number} index - The item index to toggle
   */
  toggleItem(index) {
    // Update checked state (ephemeral)
    this._checkedMap = computeNextCheckedState(this._checkedMap, index);

    // On first tick of this item, mark as visited (one-way, CL-4)
    if (this._checkedMap[index]) {
      const item = this.getItem(index);
      if (item && !item.get('_isVisited')) {
        item.set('_isVisited', true);
      }
    }

    // Notify view of state change
    this.trigger('change:_checkedMap');

    // Check completion
    this.checkCompletion();
  }

  /**
   * Check if an item is currently checked.
   *
   * @param {number} index - Item index
   * @returns {boolean}
   */
  isItemChecked(index) {
    return !!this._checkedMap[index];
  }

  /**
   * Get the count of currently checked items.
   *
   * @returns {number}
   */
  getCheckedCount() {
    return countChecked(this._checkedMap);
  }

  /**
   * Get total item count.
   *
   * @returns {number}
   */
  getItemCount() {
    return this.getChildren().length;
  }

  /**
   * Check completion status.
   *
   * Completion fires when all items have been visited (ticked at least once).
   * Uses the base class's areAllItemsCompleted() which checks _isVisited
   * on all items.
   */
  checkCompletion() {
    if (this.areAllItemsCompleted() && !this.get('_isComplete')) {
      this.setCompletionStatus();
    }
  }

  /**
   * Reset checked state (called on re-visit).
   *
   * Clears all ticks but preserves visitation. This implements CL-2:
   * ticks do not persist across visits.
   */
  resetCheckedState() {
    const items = this.getChildren();
    const checkedMap = {};
    items.forEach((item, index) => {
      checkedMap[index] = false;
    });
    this._checkedMap = checkedMap;
    this.trigger('change:_checkedMap');
  }

}
