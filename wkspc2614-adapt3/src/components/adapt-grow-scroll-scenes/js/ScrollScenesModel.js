/**
 * ScrollScenesModel
 *
 * Model for the scroll-scenes component. Extends ItemsComponentModel so each
 * authored scene is an item (consistent with the adapt-abbott-* family, e.g.
 * timeline). This is a presentational component — no marking, no response
 * semantics. Completion is handled by the view (inview), like timeline.
 *
 * All look-and-motion settings (preset + overrides) are plain author-time
 * attributes; nothing here is reactive, so the view mounts the engine once and
 * never re-renders.
 */

import ItemsComponentModel from 'core/js/models/itemsComponentModel';

export default class ScrollScenesModel extends ItemsComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      _preset: 'original',
      _scheme: '',
      _background: '',
      _transition: '',
      _effect: '',
      _snap: true,
      _showNav: true,
      _showProgress: true,
      _showStatus: true
    };
  }

}
