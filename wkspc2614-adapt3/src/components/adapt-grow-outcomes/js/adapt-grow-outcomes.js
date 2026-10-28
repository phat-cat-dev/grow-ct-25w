/*
 * adapt-grow-outcomes
 * Learning outcomes revealed one at a time with a button. Nothing is shown to
 * begin with; each press reveals the next outcome. When the last is revealed the
 * SAME button becomes the "Continue" button: the component completes its block
 * (which readies the trickle step) and, on the next press, drives trickle's own
 * (hidden) Continue to reveal the next article. So the learner sees one button
 * throughout — reveal, reveal, …, Continue — never a second button appearing.
 *
 * ComponentView.postRender() is a no-op, so (like the other GROW/GOW components)
 * this view calls setReadyStatus() itself or the page never fires
 * contentObjectView:ready and the loading screen never lifts. It must NOT use
 * setupInviewCompletion — completion here is the reveal interaction.
 */
import Adapt from 'core/js/adapt';
import ComponentView from 'core/js/views/componentView';
import ComponentModel from 'core/js/models/componentModel';

class OutcomesView extends ComponentView {

  events() {
    return {
      'click .js-outcomes-reveal': 'onButton'
    };
  }

  postRender() {
    this.total = (this.model.get('_items') || []).length;
    this.$itemEls = this.$('.outcomes__item');
    this.$button = this.$('.js-outcomes-reveal');
    this.$label = this.$('.outcomes__reveal-label');
    this.$counter = this.$('.js-outcomes-counter');
    this.isContinue = false;

    if (this.model.get('_isComplete')) {
      // Completed on a previous visit — show everything; trickle is already
      // unlocked (not re-locked on revisit), so no button is needed.
      this.revealed = this.total;
      this.updateView();
      this.$button.attr('hidden', true);
    } else {
      this.revealed = 0;
      this.updateView();
    }
    this.setReadyStatus();
  }

  onButton() {
    if (this.isContinue) { this.continueViaTrickle(); return; }
    if (this.revealed >= this.total) return;
    this.revealed++;
    this.updateView();
    if (this.revealed >= this.total) this.becomeContinue();
  }

  updateView() {
    this.$itemEls.each((i, el) => {
      const shown = i < this.revealed;
      el.classList.toggle('is-revealed', shown);
      el.setAttribute('aria-hidden', String(!shown));
    });
    if (this.$counter.length) this.$counter.text(`${this.revealed} of ${this.total}`);
  }

  // Last outcome shown: the reveal button turns into the Continue button. Mark
  // the component complete so the trickle step readies its (hidden) button.
  becomeContinue() {
    this.isContinue = true;
    this.$('.outcomes').addClass('is-complete');
    this.$button.addClass('is-continue');
    this.$label.text(this.model.get('_continueButtonText') || 'Continue');
    if (this.$counter.length) this.$counter.text('');
    if (!this.model.get('_isComplete')) this.setCompletionStatus();
  }

  // Drive trickle's own hidden Continue button for this step, which renders the
  // next article and scrolls to it. Scoped to the nearest article/page first,
  // then the document (only the outcomes gate uses trickle here).
  continueViaTrickle() {
    const scope = this.$el.closest('.article')[0] || this.$el.closest('.page')[0] || document;
    const btn = scope.querySelector('.js-trickle-btn') || document.querySelector('.js-trickle-btn');
    if (btn) {
      this.$button.attr('hidden', true);
      btn.click();
    }
  }

}

export default Adapt.register('growOutcomes', {
  view: OutcomesView,
  model: ComponentModel
});
