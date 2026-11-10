/**
 * CardModel
 *
 * Model for the grow-card component. Extends ComponentModel (presentational -
 * no per-item visitation or question semantics). Cards are read straight from
 * the `_items` array; completion is handled by inview in the view.
 */

import ComponentModel from 'core/js/models/componentModel';

export default class CardModel extends ComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      _variant: 'neutral',
      _isGroup: false
    };
  }

  /**
   * @returns {Array} the authored cards (never undefined)
   */
  getItems() {
    return this.get('_items') || [];
  }

  /**
   * Whether more than one card is present (renders as a .card-group), or the
   * author forced grouping via _isGroup.
   * @returns {boolean}
   */
  isGroup() {
    return this.getItems().length > 1 || !!this.get('_isGroup');
  }

  /**
   * Whether any card has a front graphic (so the view can wait for images).
   * @returns {boolean}
   */
  hasAnyGraphics() {
    return this.getItems().some(item => {
      const graphic = item._graphic || {};
      return !!graphic.src;
    });
  }

}
