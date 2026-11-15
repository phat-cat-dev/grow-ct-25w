/**
 * AccordionModel
 *
 * Extends ItemsComponentModel for per-item visitation tracking and
 * completion-when-all-visited. NOT a question component - no marking, no
 * response semantics; the base class's _userAnswer array stores visitation
 * booleans only.
 *
 * Per-item transient state: _isOpen (not in trackable(), so it never enters
 * suspend_data). On revisit, panels restore to closed (or first-expanded).
 *
 * Decision logic is delegated to accordionLogic.js (pure, tested).
 */

import ItemsComponentModel from 'core/js/models/itemsComponentModel';
import { computeNextOpenState } from './accordionLogic';

export default class AccordionModel extends ItemsComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      _isMultiSelect: false,
      _shouldExpandFirst: false
    };
  }

  init() {
    super.init();
    if (this.get('_shouldExpandFirst')) {
      this.toggleItem(0, true);
    }
  }

  /**
   * Toggle (or force) a panel's open state.
   *
   * @param {number} index - the item index
   * @param {boolean} [forceOpen] - if boolean, set that state instead of toggling
   */
  toggleItem(index, forceOpen) {
    const children = this.getChildren();
    const item = this.getItem(index);
    if (!item) return;

    const current = {};
    children.forEach((child, i) => { current[i] = !!child.get('_isOpen'); });

    const next = computeNextOpenState(current, index, this.get('_isMultiSelect'), forceOpen);

    children.forEach((child, i) => {
      const newState = !!next[i];
      if (child.get('_isOpen') !== newState) child.set('_isOpen', newState);
    });

    // visitation feeds completion (base class handles the rest)
    if (next[index] && !item.get('_isVisited')) {
      item.set('_isVisited', true);
    }
  }

  /**
   * On revisit, close all panels (then re-apply first-expanded if set).
   */
  checkIfResetOnRevisit() {
    const isResetOnRevisit = this.get('_isResetOnRevisit');
    if (isResetOnRevisit) {
      this.getChildren().forEach(item => item.set('_isOpen', false));
      if (this.get('_shouldExpandFirst')) this.toggleItem(0, true);
    }
    super.checkIfResetOnRevisit?.();
  }

}
