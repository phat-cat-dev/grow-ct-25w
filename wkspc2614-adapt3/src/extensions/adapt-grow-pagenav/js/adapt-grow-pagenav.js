import Adapt from 'core/js/adapt';

/**
 * GROW Page Navigation
 * --------------------------------------------------------------------------
 * Adds two buttons to Adapt's top navigation bar — previous page / next page —
 * that step the learner through the course's pages in authored order (every
 * content object of _type 'page' directly under the course, in sequence:
 * wrapper-open, confidence-pre, the lessons, summative, confidence-post,
 * wrapper-close).
 *
 * The top nav template is owned by adapt-contrib-navigation (not overridable
 * from the theme here), so the buttons are injected into `.nav__inner` at
 * runtime — the same approach the GROW layer uses for its own UI. The theme
 * (grow-ct/less/grow-chrome.less) styles them and centres the home button; the
 * glyphs are Material Symbols set there.
 *
 * Buttons reuse Adapt's own hash routing (location.hash = 'id/<pageId>'), the
 * route Adapt deep-links use, so navigation goes through the framework rather
 * than around it. At the ends of the sequence the relevant button is disabled.
 */
class GrowPageNav {

  constructor() {
    this._prevId = null;
    this._nextId = null;
    this.$prev = null;
    this.$next = null;
    this.onClickPrev = this.onClickPrev.bind(this);
    this.onClickNext = this.onClickNext.bind(this);
    this.onClickHome = this.onClickHome.bind(this);
    this.listenTo();
  }

  listenTo() {
    Adapt.on('pageView:ready', this.onPageReady, this);
    Adapt.on('menuView:ready', this.onMenuReady, this);
  }

  /** Ordered list of top-level page models (authored order). */
  getPages() {
    const course = Adapt.course;
    if (!course || typeof course.getChildren !== 'function') return [];
    return course.getChildren().filter(model => model.get('_type') === 'page');
  }

  /** Create + insert the two buttons once; returns false if the nav isn't ready. */
  ensureButtons() {
    const nav = document.querySelector('.nav__inner');
    if (!nav) return false;
    if (nav.querySelector('.js-grow-page-prev')) return true; // already in place

    const make = (modifier, label) => {
      const btn = document.createElement('button');
      btn.className = `btn-icon nav__btn ${modifier}`;
      btn.type = 'button';
      btn.setAttribute('aria-label', label);
      const icon = document.createElement('span');
      icon.className = 'icon';
      icon.setAttribute('aria-hidden', 'true');
      btn.appendChild(icon);
      return btn;
    };

    this.$prev = make('nav__btn-page-prev js-grow-page-prev', 'Previous page');
    this.$next = make('nav__btn-page-next js-grow-page-next', 'Next page');
    this.$prev.addEventListener('click', this.onClickPrev);
    this.$next.addEventListener('click', this.onClickNext);

    const back = nav.querySelector('.nav__back-btn');
    // Make the home (back) button ALWAYS return to the course home/menu, not
    // Adapt's history/parent back — which, after a prev/next jump, lands on the
    // last page. Capture phase so we beat Adapt's own delegated backButton.
    if (back && !back.dataset.growHome) {
      back.dataset.growHome = '1';
      back.addEventListener('click', this.onClickHome, true);
    }
    if (back && back.parentNode) {
      back.parentNode.insertBefore(this.$prev, back);            // prev just before home
      back.parentNode.insertBefore(this.$next, back.nextSibling); // next just after home
    } else {
      nav.appendChild(this.$prev);
      nav.appendChild(this.$next);
    }
    return true;
  }

  /** Recompute prev/next targets for the given current page id and reflect state. */
  update(currentId) {
    if (!this.ensureButtons()) return;
    const pages = this.getPages();
    const index = pages.findIndex(model => model.get('_id') === currentId);
    this._prevId = index > 0 ? pages[index - 1].get('_id') : null;
    this._nextId = (index >= 0 && index < pages.length - 1) ? pages[index + 1].get('_id') : null;
    this.setState(this.$prev, this._prevId);
    this.setState(this.$next, this._nextId);
    this.setHidden(false);
  }

  setState(btn, targetId) {
    if (!btn) return;
    const disabled = !targetId;
    btn.classList.toggle('is-disabled', disabled);
    btn.setAttribute('aria-disabled', String(disabled));
    btn.disabled = disabled;
  }

  setHidden(hidden) {
    [this.$prev, this.$next].forEach(btn => { if (btn) btn.style.display = hidden ? 'none' : ''; });
  }

  navigateTo(id) {
    if (!id) return;
    // Adapt's own deep-link route; triggers the framework router.
    window.location.hash = 'id/' + id;
  }

  onClickPrev(event) { event.preventDefault(); this.navigateTo(this._prevId); }
  onClickNext(event) { event.preventDefault(); this.navigateTo(this._nextId); }

  // Home always goes to the course home/menu, regardless of how the learner
  // reached this page (menu click, deep link, or a prev/next jump).
  onClickHome(event) {
    event.preventDefault();
    event.stopImmediatePropagation();
    this.goHome();
  }

  goHome() {
    try {
      const course = Adapt.course;
      const menu = course && typeof course.getChildren === 'function'
        ? course.getChildren().toArray().find(model => model.get('_type') === 'menu')
        : null;
      if (menu) { window.location.hash = 'id/' + menu.get('_id'); return; }
    } catch (e) { /* fall through to the course root */ }
    window.location.hash = '#/';
  }

  onPageReady(view) {
    const id = view && view.model && view.model.get('_id');
    this.update(id);
  }

  onMenuReady() {
    // On a menu there is no sequential page context — hide the pair.
    if (this.ensureButtons()) this.setHidden(true);
  }

}

export default new GrowPageNav();
