/**
 * HotgraphicModel
 *
 * Extends ItemsComponentModel for per-hotspot visitation and completion.
 * The diagram itself (the inlined SVG element) never lives on the model -
 * only `_isDiagramReady` and `_revealedIndex`, neither of which is trackable.
 *
 * Completion excludes decorative hotspots (`_action: "none"`) from the
 * denominator - see isAllRequiredVisited in hotgraphicLogic.js - so a
 * diagram with context-only wedges can still reach completion.
 */

import ItemsComponentModel from 'core/js/models/itemsComponentModel';
import { isAllRequiredVisited, slugFromSrc } from './hotgraphicLogic';

export default class HotgraphicModel extends ItemsComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      _isDiagramReady: false,
      _revealedIndex: null
    };
  }

  /**
   * @returns {string} the diagram's slug, derived from `_diagram._slug` if
   *   authored, else from the asset filename.
   */
  getDiagramSlug() {
    const diagram = this.get('_diagram') || {};
    return diagram._slug || slugFromSrc(diagram.src);
  }

  /**
   * Override: a hotgraphic is complete when every required (non-decorative)
   * hotspot has been visited, not merely every item.
   * @returns {boolean}
   */
  areAllItemsCompleted() {
    return isAllRequiredVisited(this.getChildren().toJSON());
  }

  /**
   * Reveal an item inline (the `inlineReveal` action), marking it visited.
   * Set to null to collapse any open panel.
   * @param {number|null} index
   */
  revealItem(index) {
    this.set('_revealedIndex', index);
    if (index === null) return;
    const item = this.getItem(index);
    if (item && !item.get('_isVisited')) item.set('_isVisited', true);
  }

}
