/**
 * CarouselModel
 *
 * Extends ItemsComponentModel for per-slide visitation and
 * completion-when-all-visited. NOT a question component.
 *
 * _activeIndex is transient (not trackable), so it never enters suspend_data;
 * on revisit the carousel returns to the first slide. Index resolution is
 * delegated to carouselLogic.js (pure, tested).
 */

import ItemsComponentModel from 'core/js/models/itemsComponentModel';
import { resolveIndex } from './carouselLogic';

export default class CarouselModel extends ItemsComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      _activeIndex: 0,
      _shouldAutoScroll: false,
      _canCycle: true
    };
  }

  init() {
    super.init();
    // first slide is shown on load, so mark it visited
    const first = this.getItem(0);
    if (first && !first.get('_isVisited')) first.set('_isVisited', true);
  }

  /**
   * Go to a specific slide (resolved/cycled), marking it visited.
   * @param {number} requested
   */
  goTo(requested) {
    const length = this.getChildren().length;
    const index = resolveIndex(requested, length, this.get('_canCycle'));
    this.set('_activeIndex', index);
    const item = this.getItem(index);
    if (item && !item.get('_isVisited')) item.set('_isVisited', true);
  }

  next() { this.goTo((this.get('_activeIndex') || 0) + 1); }

  prev() { this.goTo((this.get('_activeIndex') || 0) - 1); }

  /**
   * Whether any slide has a graphic (so the view can wait for images).
   * @returns {boolean}
   */
  hasAnyGraphics() {
    return (this.get('_items') || []).some(item => {
      const graphic = item._graphic || {};
      return !!graphic.src;
    });
  }

  /**
   * On revisit, return to the first slide.
   */
  checkIfResetOnRevisit() {
    if (this.get('_isResetOnRevisit')) this.set('_activeIndex', 0);
    super.checkIfResetOnRevisit?.();
  }

}
