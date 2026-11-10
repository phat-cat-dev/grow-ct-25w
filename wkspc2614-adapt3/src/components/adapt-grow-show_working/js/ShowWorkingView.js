import ComponentView from 'core/js/views/componentView';

/**
 * ShowWorkingView
 *
 * A step-by-step worked solution. All lines are present and readable at rest;
 * when the component scrolls into view (and motion is allowed) they replay the
 * staggered "rise" reveal and the check-mark draws on. A Replay button re-runs
 * it. Under reduced motion nothing animates — the working simply sits there —
 * and the Replay button is hidden.
 *
 * Decorative only: the reveal adds no information a screen reader can't already
 * get from the ordered list, so completion is tied to being seen, not to the
 * animation finishing.
 */
class ShowWorkingView extends ComponentView {

  events() {
    return {
      'click .grow-show-working__replay': 'onReplay'
    };
  }

  postRender() {
    this.reduced = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.$stage = this.$('.grow-show-working__stage');
    this.$replay = this.$('.grow-show-working__replay');
    this._hasPlayed = false;

    // Replay is pointless when nothing moves
    if (this.reduced) this.$replay.addClass('u-display-none');

    this._setupInview();
    this.setReadyStatus();
  }

  /**
   * Play on first view and mark seen. IntersectionObserver keeps it dependency-
   * free; without it, play immediately.
   */
  _setupInview() {
    const el = this.$stage[0] || this.el;
    if (typeof IntersectionObserver !== 'function' || !el) {
      this._onSeen();
      return;
    }
    this._observer = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          this._onSeen();
          this._observer.disconnect();
          this._observer = null;
          break;
        }
      }
    }, { threshold: 0.4 });
    this._observer.observe(el);
  }

  _onSeen() {
    this._play();
    if (this.model.setCompletionStatus) this.model.setCompletionStatus();
  }

  onReplay() {
    this._play();
  }

  /**
   * Restart the CSS animations by removing the trigger class, forcing a reflow,
   * then re-adding it. No-op visual under reduced motion (animations are off).
   */
  _play() {
    if (this.reduced) return;
    this.$stage.removeClass('is-playing');
    // Force reflow so the re-added class restarts the animations
    void this.$stage[0]?.offsetWidth;
    this.$stage.addClass('is-playing');
    this._hasPlayed = true;
  }

  remove() {
    if (this._observer) {
      this._observer.disconnect();
      this._observer = null;
    }
    super.remove();
  }

}

ShowWorkingView.template = 'growShowWorking.jsx';

export default ShowWorkingView;
