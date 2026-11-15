/**
 * HeroModel
 *
 * Model for the grow-hero component. Extends ComponentModel (presentational -
 * no question semantics). A single hero banner read straight from the model's
 * attributes; completion is handled by inview in the view.
 */

import ComponentModel from 'core/js/models/componentModel';

export default class HeroModel extends ComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      _variant: 'neutral',
      _align: 'left',
      _animate: false
    };
  }

  /**
   * @returns {Object} the hero media ({ _type, src, alt, poster }), never undefined
   */
  getMedia() {
    return this.get('_media') || {};
  }

  /**
   * Whether the hero carries a front image to wait for before marking ready.
   * @returns {boolean}
   */
  hasImage() {
    const media = this.getMedia();
    return media._type === 'image' && !!media.src;
  }

}
