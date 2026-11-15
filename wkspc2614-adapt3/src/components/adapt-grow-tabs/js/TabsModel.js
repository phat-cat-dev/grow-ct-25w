/**
 * TabsModel
 *
 * Model for the tabs component. Extends ItemsComponentModel for
 * per-item visitation tracking and completion-when-all-visited.
 *
 * NOT a question component — no marking, no _recordInteraction, no response
 * semantics. The base class's _userAnswer array (storing visitation booleans)
 * is legitimate persistence plumbing and stays intact.
 *
 * _activeIndex tracks which tab is currently selected. The first tab (index 0)
 * is active on initial render. On revisit, _activeIndex resets to 0.
 *
 * Design refs: TA-1 (schema), TC-2 (model), TC-4 (ARIA tabs pattern)
 */

import ItemsComponentModel from 'core/js/models/itemsComponentModel';
import { computeNextIndex, computeNextVisitation, keyToDirection, Direction } from './tabsLogic';

export default class TabsModel extends ItemsComponentModel {

  /**
   * Default values.
   */
  defaults() {
    return {
      ...super.defaults(),
      _activeIndex: 0
    };
  }

  /**
   * Initialize - mark first tab as visited on setup.
   */
  init() {
    super.init();

    // First tab is active by default, so mark it visited
    const firstItem = this.getItem(0);
    if (firstItem && !firstItem.get('_isVisited')) {
      firstItem.set('_isVisited', true);
    }
  }

  /**
   * Select a tab by index.
   *
   * Updates _activeIndex and marks the tab as visited.
   *
   * @param {number} index - The tab index to select
   */
  selectTab(index) {
    const children = this.getChildren();
    const item = this.getItem(index);
    if (!item) return;

    // Update active index
    this.set('_activeIndex', index);

    // Mark as visited
    if (!item.get('_isVisited')) {
      item.set('_isVisited', true);
    }
  }

  /**
   * Navigate to adjacent tab using keyboard direction.
   *
   * @param {string} direction - Direction constant from tabsLogic
   * @returns {number} The new active index
   */
  navigateTab(direction) {
    const currentIndex = this.get('_activeIndex') || 0;
    const itemCount = this.getChildren().length;

    const nextIndex = computeNextIndex(currentIndex, direction, itemCount);
    this.selectTab(nextIndex);

    return nextIndex;
  }

  /**
   * Handle keyboard navigation from a key event.
   *
   * @param {string} key - The KeyboardEvent.key value
   * @returns {number|null} The new active index, or null if not a navigation key
   */
  handleKeyNavigation(key) {
    const direction = keyToDirection(key);
    if (!direction) return null;

    return this.navigateTab(direction);
  }

  /**
   * Get the currently active tab index.
   * @returns {number}
   */
  getActiveIndex() {
    return this.get('_activeIndex') || 0;
  }

  /**
   * Check if a tab at given index is active.
   * @param {number} index
   * @returns {boolean}
   */
  isTabActive(index) {
    return this.getActiveIndex() === index;
  }

  /**
   * Check if any items have graphics (for imageReady handling).
   * @returns {boolean}
   */
  hasAnyGraphics() {
    return this.getChildren().some(item => {
      const graphic = item.get('_graphic') || {};
      return !!graphic.src;
    });
  }

  /**
   * Reset on revisit — base class handles _isVisited restoration.
   * We reset _activeIndex to 0 and ensure first tab is visited.
   */
  checkIfResetOnRevisit() {
    const isResetOnRevisit = this.get('_isResetOnRevisit');
    if (!isResetOnRevisit) return;

    // Reset to first tab
    this.set('_activeIndex', 0);

    // Ensure first tab is visited
    const firstItem = this.getItem(0);
    if (firstItem && !firstItem.get('_isVisited')) {
      firstItem.set('_isVisited', true);
    }

    // Let base class handle its reset
    super.checkIfResetOnRevisit?.();
  }

}
