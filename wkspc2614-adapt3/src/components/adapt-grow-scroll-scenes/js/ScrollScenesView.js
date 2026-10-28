/**
 * ScrollScenesView
 *
 * View for the scroll-scenes component. Extends ComponentView (presentational,
 * not a question). Renders the JSX once, then mounts the vanilla scroll engine
 * onto the .scroll-scenes host in postRender and tears it down in preRemove.
 *
 * The component holds no reactive state (the design dials are fixed at
 * authoring time), so there is no changed()/re-render path that could discard
 * the engine's inline styles — it is mounted exactly once per view.
 *
 * Completion is inview: the component counts toward page completion once its
 * widget has been seen, matching the timeline component.
 */

import ComponentView from 'core/js/views/componentView';
import { mountScrollScenes } from './scrollScenesDriver';
import { resolvePresentation } from './scrollScenesLogic';

class ScrollScenesView extends ComponentView {

  postRender() {
    this._player = null;

    const host = this.$('.scroll-scenes')[0];
    if (host) {
      const { effect, snap } = resolvePresentation(this.model.toJSON());
      try {
        this._player = mountScrollScenes(host, { effect, snap });
      } catch (error) {
        // The scenes still read and scroll natively without the engine, so a
        // mount failure degrades rather than blanking the component.
        console.warn(`[scrollScenes] ${this.model.get('_id')}: engine did not mount (${error.message}). Native scrolling still works.`);
      }
    }

    // Presentational: visible once = complete (same model as timeline).
    this.setupInviewCompletion('.component__widget');
    this.setReadyStatus();
  }

  preRemove() {
    if (this._player) {
      this._player.destroy();
      this._player = null;
    }
    super.preRemove();
  }

}

ScrollScenesView.template = 'scrollScenes.jsx';

export default ScrollScenesView;
