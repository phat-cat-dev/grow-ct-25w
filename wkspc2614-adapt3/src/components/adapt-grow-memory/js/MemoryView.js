/**
 * MemoryView
 *
 * View for the memory match component. Extends ComponentView (NOT QuestionView).
 *
 * Gameplay is driven by direct DOM class toggling (not React re-renders) because
 * the flip-back on a mismatch is time-based and a two-tile lock must survive
 * between clicks; this keeps the timing logic in one place and mirrors the
 * self-contained gallery pattern this component was matured from.
 *
 * Accessibility:
 *  - Each tile is a native <button>, so Tab / Enter / Space work with no extra
 *    key handling. Matched tiles carry aria-disabled but stay focusable so they
 *    can still be reviewed.
 *  - Every turn is announced through a single polite live region: the tile's
 *    content on reveal, the outcome on the second tile, and the win message.
 *  - A tile's accessible name updates with its state (face down / content /
 *    matched). All learner-facing strings come from the schema globals.
 *  - Reduced motion is respected: the reveal/flip-back pauses are kept short and
 *    the CSS drops the scale-in transition.
 *
 * Completion (formative only):
 *  - _isCompletionBearing true (default): completes when all pairs are found.
 *  - _isCompletionBearing false: completes on view, so it never gates the page,
 *    while the win message still appears when the learner finishes.
 *
 * Like the other GROW components, ComponentView.postRender() is a no-op, so this
 * view calls setReadyStatus() itself or the loading curtain never lifts.
 */

import Adapt from 'core/js/adapt';
import ComponentView from 'core/js/views/componentView';

// Safety-net defaults mirroring the schema globals. The schema is the authorable
// source of truth; these guarantee the game is never silent if the globals
// namespace cannot be resolved at runtime.
const GLOBAL_DEFAULTS = {
  ariaRegion: 'Memory match game. Select a tile to turn it over, then find its matching pair.',
  tileLabel: 'Tile {{number}}, face down',
  revealAnnouncement: '{{label}} revealed.',
  matchAnnouncement: 'Match found. {{found}} of {{total}} pairs found.',
  noMatchAnnouncement: 'Not a match. Those two tiles will turn back over.',
  matchedState: 'matched',
  winMessage: 'Well done. You found all the pairs.'
};

// Comprehension pauses (ms). These are reading pauses, not decoration, so they
// are kept even under reduced motion; the match pause is trimmed a little there.
const MATCH_DELAY = 400;
const MATCH_DELAY_REDUCED = 150;
const NO_MATCH_DELAY = 900;

class MemoryView extends ComponentView {

  events() {
    return {
      'click .js-grow-memory-tile': 'onTileClick'
    };
  }

  /**
   * Hand the shuffled deck and resolved globals to the template.
   */
  getData() {
    const data = super.getData();
    data._deck = this.model.getDeck();
    data._globals = this._getGlobals();
    return data;
  }

  /**
   * Resolve component globals, falling back to local defaults.
   * @private
   */
  _getGlobals() {
    const globals = Adapt.course?.get('_globals')?._components?._growMemory || {};
    return { ...GLOBAL_DEFAULTS, ...globals };
  }

  postRender() {
    this.globals = this._getGlobals();

    this.$board = this.$('.js-grow-memory-board');
    this.$tiles = this.$('.js-grow-memory-tile');
    this.$feedback = this.$('.js-grow-memory-feedback');
    this.$live = this.$('.js-grow-memory-live');

    this.openTiles = [];
    this.lock = false;
    this.found = 0;
    this.total = this.model.getPairCount();
    this._flipBackTimer = null;

    this.reducedMotion = Boolean(
      window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches
    );

    // If the learner already completed this game, present it solved (no noise).
    if (this.model.get('_isComplete')) {
      this._revealAllMatched();
    }

    // When the game is not the completion gate, fall back to inview completion
    // so a formative game never blocks the page.
    if (!this.model.isCompletionBearing()) {
      this.setupInviewCompletion('.component__widget');
    }

    this.setReadyStatus();
  }

  onTileClick(event) {
    this._flip(event.currentTarget);
  }

  /**
   * Turn a tile over, if the game state allows it.
   * @private
   */
  _flip(tile) {
    if (this.lock) return;
    if (tile.classList.contains('is-up') || tile.classList.contains('is-matched')) return;

    tile.classList.add('is-up');
    this._setTileAria(tile, 'up');
    this._announce(this._interpolate(this.globals.revealAnnouncement, {
      label: tile.getAttribute('data-label') || ''
    }));

    this.openTiles.push(tile);
    if (this.openTiles.length < 2) return;

    // Two tiles up — lock the board until they resolve.
    this.lock = true;
    const [first, second] = this.openTiles;
    const isMatch = first.getAttribute('data-pair') === second.getAttribute('data-pair');

    if (isMatch) {
      const delay = this.reducedMotion ? MATCH_DELAY_REDUCED : MATCH_DELAY;
      this._flipBackTimer = setTimeout(() => this._onMatch(first, second), delay);
    } else {
      this._flipBackTimer = setTimeout(() => this._onNoMatch(first, second), NO_MATCH_DELAY);
    }
  }

  /**
   * Resolve a matched pair: it stays revealed.
   * @private
   */
  _onMatch(first, second) {
    [first, second].forEach(tile => {
      tile.classList.remove('is-up');
      tile.classList.add('is-matched');
      this._setTileAria(tile, 'matched');
    });

    this.openTiles = [];
    this.lock = false;
    this.found++;

    if (this.found >= this.total) {
      this._onWin();
    } else {
      this._announce(this._interpolate(this.globals.matchAnnouncement, {
        found: this.found,
        total: this.total
      }));
    }
  }

  /**
   * Resolve a mismatched pair: both turn back over.
   * @private
   */
  _onNoMatch(first, second) {
    [first, second].forEach(tile => {
      tile.classList.remove('is-up');
      this._setTileAria(tile, 'down');
    });

    this.openTiles = [];
    this.lock = false;
    this._announce(this.globals.noMatchAnnouncement);
  }

  /**
   * Handle the win: show and announce the message, and complete if bearing.
   * @private
   */
  _onWin() {
    if (this.$feedback.length) {
      this.$feedback.text(this.globals.winMessage).addClass('is-visible');
    }
    this._announce(this.globals.winMessage);

    if (this.model.isCompletionBearing() && !this.model.get('_isComplete')) {
      this.setCompletionStatus();
    }
  }

  /**
   * Present every tile as matched, without announcements. Used on revisit when
   * the component is already complete.
   * @private
   */
  _revealAllMatched() {
    this.$tiles.each((index, tile) => {
      tile.classList.remove('is-up');
      tile.classList.add('is-matched');
      this._setTileAria(tile, 'matched');
    });
    this.found = this.total;
    if (this.$feedback.length) {
      this.$feedback.text(this.globals.winMessage).addClass('is-visible');
    }
  }

  /**
   * Update a tile's accessible name to reflect its state.
   * @private
   */
  _setTileAria(tile, state) {
    const label = tile.getAttribute('data-label') || '';
    const number = Number(tile.getAttribute('data-index')) + 1;

    if (state === 'down') {
      tile.setAttribute('aria-label', this._interpolate(this.globals.tileLabel, { number }));
      tile.removeAttribute('aria-disabled');
      return;
    }

    if (state === 'matched') {
      const matched = this.globals.matchedState || '';
      tile.setAttribute('aria-label', label ? `${label}, ${matched}` : matched);
      tile.setAttribute('aria-disabled', 'true');
      return;
    }

    // 'up'
    tile.setAttribute('aria-label', label || this._interpolate(this.globals.tileLabel, { number }));
  }

  /**
   * Announce a message through the polite live region.
   * Clears first so the same text re-announces if it repeats.
   * @private
   */
  _announce(message) {
    if (!this.$live || !this.$live.length) return;
    this.$live.text('');
    setTimeout(() => this.$live.text(message), 50);
  }

  /**
   * Interpolate {{name}} placeholders in a globals string.
   * @private
   */
  _interpolate(template, values) {
    if (!template) return '';
    return template.replace(/\{\{(\w+)\}\}/g, (match, key) => (
      values[key] !== undefined && values[key] !== null ? values[key] : match
    ));
  }

  remove() {
    if (this._flipBackTimer) {
      clearTimeout(this._flipBackTimer);
      this._flipBackTimer = null;
    }
    super.remove();
  }

}

MemoryView.template = 'growMemory.jsx';

export default MemoryView;
