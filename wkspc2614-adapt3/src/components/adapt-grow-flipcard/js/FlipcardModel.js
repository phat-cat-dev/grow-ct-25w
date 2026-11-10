/**
 * FlipcardModel
 *
 * Model for the flipcard component. Extends ItemsComponentModel for
 * per-item visitation tracking and completion-when-all-visited.
 *
 * NOT a question component — no marking, no _recordInteraction, no response
 * semantics. The base class's _userAnswer array (storing visitation booleans)
 * is legitimate persistence plumbing and stays intact.
 *
 * _isFlipped is per-item transient state — NOT in trackable(), so it never
 * enters suspend_data. On revisit, all cards present front-face-up;
 * completion restores via the base class's visitation mechanism.
 *
 * Design refs: FC-1 (schema), FB-2 (model), AR-1/BP-1a (no question semantics),
 * FB-5 (pure logic extraction)
 */

import ItemsComponentModel from 'core/js/models/itemsComponentModel';
import { computeNextFlippedState, computeNextVisitation } from './flipcardLogic';

export default class FlipcardModel extends ItemsComponentModel {

  /**
   * Default values.
   */
  defaults() {
    return {
      ...super.defaults(),
      _flipBehaviour: 'independent',
      _isRandomised: false
    };
  }

  /**
   * On setup, shuffle the cards into a fresh order when _isRandomised is set.
   * Done BEFORE super.init() (which calls setUpItems() to build the child models
   * from _items), so the children - and their flip indices - follow the shuffle.
   * init() runs on each page visit, so the order is re-randomised each time.
   */
  init() {
    if (this.get('_isRandomised')) {
      const items = (this.get('_items') || []).slice();
      for (let i = items.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [items[i], items[j]] = [items[j], items[i]];
      }
      this.set('_items', items);
    }
    super.init();
  }

  /**
   * Toggle the flipped state of a card by its index.
   *
   * Delegates decision logic to pure functions (flipcardLogic.js) for testability.
   * - In 'independent' mode: toggles just that card's _isFlipped.
   * - In 'single' mode: also unflips all other cards.
   *
   * On first flip, marks the item as visited (base class handles completion).
   *
   * @param {number} index - The item index to toggle
   */
  toggleItemFlipped(index) {
    const children = this.getChildren();
    const item = this.getItem(index);
    if (!item) return;

    // Extract current flipped state map from Backbone models
    const currentFlippedMap = {};
    children.forEach((child, idx) => {
      currentFlippedMap[idx] = !!child.get('_isFlipped');
    });

    // Compute next flipped state via pure function
    const behaviour = this.get('_flipBehaviour') || 'independent';
    const nextFlippedMap = computeNextFlippedState(currentFlippedMap, index, behaviour);

    // Apply flipped state changes back to Backbone models
    children.forEach((child, idx) => {
      const newState = !!nextFlippedMap[idx];
      if (child.get('_isFlipped') !== newState) {
        child.set('_isFlipped', newState);
      }
    });

    // Extract current visitation array
    const currentVisited = children.map(child => !!child.get('_isVisited'));

    // Compute next visitation via pure function
    const newFlippedState = nextFlippedMap[index];
    const nextVisited = computeNextVisitation(currentVisited, index, newFlippedState);

    // Apply visitation change (only for this item, idempotent)
    if (nextVisited[index] && !item.get('_isVisited')) {
      item.set('_isVisited', true);
    }
  }

  /**
   * Get the flipped state of a card by index.
   * @param {number} index
   * @returns {boolean}
   */
  isItemFlipped(index) {
    const item = this.getItem(index);
    return item ? !!item.get('_isFlipped') : false;
  }

  /**
   * Check if any items have front graphics (for imageReady handling).
   * @returns {boolean}
   */
  hasAnyFrontGraphics() {
    return this.getChildren().some(item => {
      const front = item.get('front') || {};
      const graphic = front._graphic || {};
      return !!graphic.src;
    });
  }

  /**
   * Reset on revisit — base class handles _isVisited restoration.
   * We just need to ensure _isFlipped is reset (cards show front on revisit).
   */
  checkIfResetOnRevisit() {
    const isResetOnRevisit = this.get('_isResetOnRevisit');
    if (!isResetOnRevisit) return;

    // Reset all cards to front-face-up
    this.getChildren().forEach(item => {
      item.set('_isFlipped', false);
    });

    // Let base class handle its reset
    super.checkIfResetOnRevisit?.();
  }

}
