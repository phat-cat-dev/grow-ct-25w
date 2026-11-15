import ComponentView from 'core/js/views/componentView';
import { mountOverlay } from './overlay';

/**
 * PageNotesView — renders a launch icon-button; on click it mounts a transparent
 * overlay of animated notes over a target region (the parent article by default,
 * or an authored _targetId). Author-authored presentation: viewing completes the
 * component. The overlay itself lives in ./overlay.js (no React), so the notes we
 * append survive without the view re-rendering.
 */
class PageNotesView extends ComponentView {

  preRender() {
    this.onLaunch = this.onLaunch.bind(this);
    this.model.set('onLaunch', this.onLaunch);
  }

  postRender() {
    this.setReadyStatus();
  }

  // Find the DOM node for the region this overlay should sit over.
  resolveTarget() {
    const explicit = this.model.get('_targetId');
    const id = explicit || this.model.findAncestor('articles')?.get('_id');
    return (id && document.querySelector(`[data-adapt-id="${id}"]`)) || this.el;
  }

  onLaunch(event) {
    const launchButton = event?.currentTarget || this.$('.grow-pagenotes__launch')[0];
    const target = this.resolveTarget();
    const overlay = this.model.get('_overlay') || {};
    this._overlay?.destroy();
    this._overlay = mountOverlay(target, this.model.get('_notes') || [], {
      reveal: overlay._reveal || 'stepped',
      scrim: overlay._scrim || 'none',
      ariaLabel: this.model.get('ariaRegion') || this.model.get('displayTitle') || 'Page notes',
      returnFocusTo: launchButton
    });
    this.model.setCompletionStatus();
  }

  remove() {
    this._overlay?.destroy();
    super.remove();
  }
}

PageNotesView.template = 'growPageNotes.jsx';

export default PageNotesView;
