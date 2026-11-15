/*
 * adapt-grow-levels
 * Levels shown as independent drop-downs: every panel is available from the
 * start and each opens or closes on its own, so any number can be open at once.
 * Each open level offers an on-demand "In practice" advice pop-out. Completes
 * once every level has been opened.
 *
 * ComponentView.postRender() is a no-op, so (like the other GROW components) this
 * view calls setReadyStatus() itself, or the page never fires
 * contentObjectView:ready and the loading curtain never lifts.
 */
import components from 'core/js/components';
import ComponentView from 'core/js/views/componentView';
import ComponentModel from 'core/js/models/componentModel';

class LevelsView extends ComponentView {

  events() {
    return {
      'click .js-grow-levels-card': 'onCard',
      'click .js-grow-levels-advice': 'onAdvice'
    };
  }

  postRender() {
    this.$items = this.$('.grow-levels__item');
    this.total = this.$items.length;
    // Independent drop-downs: a set of open indices (not one active panel), and
    // nothing is locked - every panel is available from the start.
    this.open = new Set();
    this.viewed = {};

    if (this.model.get('_isComplete')) {
      for (let i = 0; i < this.total; i++) this.viewed[i] = true;
    }
    this.renderState();
    this.setReadyStatus();
  }

  renderState() {
    this.$items.each((i, el) => {
      const isOpen = this.open.has(i);
      el.classList.remove('is-locked'); // no gating - independent drop-downs
      el.classList.toggle('is-open', isOpen);
      el.classList.toggle('is-viewed', !!this.viewed[i]);
      const card = el.querySelector('.js-grow-levels-card');
      if (card) {
        card.setAttribute('aria-expanded', String(isOpen));
        card.removeAttribute('aria-disabled');
      }
      const detail = el.querySelector('.grow-levels__detail');
      if (detail) detail.setAttribute('aria-hidden', String(!isOpen));
    });
  }

  toggle(i) {
    if (i < 0 || i >= this.total) return;
    if (this.open.has(i)) {
      this.open.delete(i);
    } else {
      this.open.add(i);
      this.viewed[i] = true;
    }
    this.renderState();
    if (Object.keys(this.viewed).length >= this.total && !this.model.get('_isComplete')) {
      this.setCompletionStatus();
    }
  }

  onCard(e) {
    const li = e.currentTarget.closest('.grow-levels__item');
    const i = this.$items.index(li);
    this.toggle(i);
  }

  onAdvice(e) {
    e.stopPropagation();
    const btn = e.currentTarget;
    const wrap = btn.closest('.grow-levels__detail');
    const adv = wrap && wrap.querySelector('.grow-levels__advice');
    const open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    if (adv) adv.setAttribute('aria-hidden', String(open));
  }

}

LevelsView.template = 'growLevels.jsx';

export default components.register('growLevels', {
  view: LevelsView,
  model: ComponentModel
});
