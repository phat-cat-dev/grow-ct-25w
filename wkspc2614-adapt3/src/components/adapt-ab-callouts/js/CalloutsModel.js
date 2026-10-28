/**
 * CalloutsModel
 *
 * Model for the ab-callouts component. Extends ComponentModel (presentational -
 * no per-item visitation or question semantics). Callouts are read straight
 * from the `_items` array; completion is handled by inview in the view.
 */

import ComponentModel from 'core/js/models/componentModel';

export default class CalloutsModel extends ComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      _variant: 'neutral',
      _isGroup: false
    };
  }

  /**
   * @returns {Array} the authored callouts (never undefined)
   */
  getItems() {
    return this.get('_items') || [];
  }

  /**
   * Whether more than one callout is present (renders as a group), or the
   * author forced grouping via _isGroup.
   * @returns {boolean}
   */
  isGroup() {
    return this.getItems().length > 1 || !!this.get('_isGroup');
  }

}
