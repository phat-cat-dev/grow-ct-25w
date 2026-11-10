/*
 * adapt-grow-text-tagging - View
 *
 * Interaction model ported from pw02's src/shared/js/activities/grow-text-tagging.js
 * (TextTagging.init/handlePaletteClick/handleSpanClick/applyTag/removeTag/
 * updateCounter), adapted onto Adapt's QuestionView lifecycle instead of the
 * source's bespoke ActivityEngine + ActivityStateManager.
 *
 * Bugs fixed, not ported (full detail in README.md):
 *   - `activeCategory` is an instance property (this._activeCategoryIndex),
 *     not shared module-level state - two grow-text-tagging questions on one page
 *     no longer interfere with each other.
 *   - The applied-tag label is rendered via a `data-applied-label` attribute +
 *     CSS `::after { content: attr(data-applied-label) }` (see less/grow-text-tagging.less)
 *     instead of being appended as a child <span>, so it never contaminates
 *     the span's text content (the source's feedback-truncation logic read
 *     `span.textContent`, which included the appended label).
 *   - Correct/incorrect marking classes are scoped under both the page body
 *     and `.modal`/`.popup` containers (the source CSS only had `.lap`, not
 *     `.modal`, so marking never rendered inside the activity modal).
 *   - The palette/tagged-span colour classes are keyed on the category's
 *     *index* (`grow-text-tagging__tag-target--tag-N`), not its author-defined
 *     `_id`, so less/grow-text-tagging.less can ship a fixed N-slot palette that
 *     works for any author-chosen `_id` string (the source hardcoded CSS
 *     colours for 4 specific category ids). The semantic
 *     `grow-text-tagging__tag-target--{_id}` class is still added alongside it,
 *     for authors who want to target a specific category in custom CSS.
 *
 * Adapt API fidelity note: QuestionView lifecycle method names below
 * (resetQuestion, restoreUserAnswer, disableQuestion, enableQuestion,
 * showMarking, hideMarking) follow the common pattern used by official
 * question components such as adapt-contrib-matching. Verify these against
 * the exact Adapt framework version installed, since method signatures have
 * shifted slightly between major versions.
 */
import Adapt from 'core/js/adapt';
import QuestionView from 'core/js/views/questionView';

export default class TextTaggingView extends QuestionView {

  events() {
    return {
      'click .js-grow-text-tagging-tag-btn': 'onPaletteClick',
      'click .js-grow-text-tagging-tag-target': 'onSpanClick',
      'keydown .js-grow-text-tagging-tag-target': 'onSpanKeydown'
    };
  }

  initialize(...args) {
    super.initialize(...args);
    // Per-instance, not a shared singleton (fixes the source's module-level bug).
    this._activeCategoryIndex = -1;
  }

  onQuestionRendered() {
    // QuestionView does not call this for us; without it the page never
    // fires contentObjectView:ready and the loading screen never lifts.
    this.setReadyStatus();
    this.updateCounter();
    this.restoreUserAnswer();
  }

  // --- Interaction handlers ---

  onPaletteClick(event) {
    event.preventDefault();

    if (this.model.get('_isSubmitted')) return;

    const $btn = $(event.currentTarget);
    const categoryIndex = parseInt($btn.attr('data-tag-index'), 10);

    // Deactivate all buttons first (radio-like palette, matches source).
    this.$('.js-grow-text-tagging-tag-btn')
      .removeClass('grow-text-tagging__tag-btn--active')
      .attr('aria-pressed', 'false');

    if (this._activeCategoryIndex === categoryIndex) {
      // Clicking the already-active button toggles selection off.
      this._activeCategoryIndex = -1;
      return;
    }

    $btn.addClass('grow-text-tagging__tag-btn--active').attr('aria-pressed', 'true');
    this._activeCategoryIndex = categoryIndex;
  }

  onSpanClick(event) {
    event.preventDefault();
    this._handleSpanInteraction(event.currentTarget);
  }

  onSpanKeydown(event) {
    if (event.key !== 'Enter' && event.key !== ' ') return;
    event.preventDefault();
    this._handleSpanInteraction(event.currentTarget);
  }

  _handleSpanInteraction(spanEl) {
    if (this.model.get('_isSubmitted')) return;

    const $span = $(spanEl);
    const spanId = $span.attr('data-span-id');

    // Click-to-untag: a tagged span is always cleared by clicking it again,
    // regardless of whether a palette category is currently selected.
    if (this.model.getSpanTag(spanId) !== -1) {
      this._removeTag($span, spanId);
      this.updateCounter();
      return;
    }

    // No category selected and span is untagged: no-op (matches source).
    if (this._activeCategoryIndex === -1) return;

    this._applyTag($span, spanId, this._activeCategoryIndex);
    this.updateCounter();
  }

  _applyTag($span, spanId, categoryIndex) {
    const categories = this.model.get('_tagCategories') || [];
    const category = categories[categoryIndex];
    if (!category) return;

    this.model.setSpanTag(spanId, categoryIndex);

    $span
      .attr('data-applied-tag', category._id)
      .attr('data-applied-index', categoryIndex)
      .attr('data-applied-label', category.label)
      .attr('aria-label', `${$span.text()} - tagged as ${category.label}`)
      .addClass(`grow-text-tagging__tag-target--tagged grow-text-tagging__tag-target--${category._id} grow-text-tagging__tag-target--tag-${categoryIndex}`);
  }

  _removeTag($span, spanId) {
    const appliedTag = $span.attr('data-applied-tag');
    const appliedIndex = $span.attr('data-applied-index');

    this.model.setSpanTag(spanId, -1);

    $span
      .removeAttr('data-applied-tag')
      .removeAttr('data-applied-index')
      .removeAttr('data-applied-label')
      .attr('aria-label', $span.text())
      .removeClass(`grow-text-tagging__tag-target--tagged grow-text-tagging__tag-target--${appliedTag} grow-text-tagging__tag-target--tag-${appliedIndex}`);
  }

  updateCounter() {
    const allSpans = this.model.get('_allSpans') || [];
    const userAnswer = this.model.get('_userAnswer') || [];
    const taggedCount = userAnswer.filter(value => value !== -1).length;

    this.$('.js-grow-text-tagging-tagged-count').text(taggedCount);
    this.$('.js-grow-text-tagging-total-count').text(allSpans.length);

    const $counter = this.$('.js-grow-text-tagging-progress-counter');
    $counter
      .removeClass('grow-text-tagging__progress-counter--none grow-text-tagging__progress-counter--partial grow-text-tagging__progress-counter--all')
      .addClass(
        taggedCount === 0
          ? 'grow-text-tagging__progress-counter--none'
          : taggedCount === allSpans.length
            ? 'grow-text-tagging__progress-counter--all'
            : 'grow-text-tagging__progress-counter--partial'
      );
  }

  // --- QuestionView lifecycle ---

  resetQuestion() {
    this._activeCategoryIndex = -1;

    this.$('.js-grow-text-tagging-tag-btn')
      .removeClass('grow-text-tagging__tag-btn--active')
      .attr('aria-pressed', 'false');

    this.$('.js-grow-text-tagging-tag-target').each((i, el) => {
      const $span = $(el);
      const appliedTag = $span.attr('data-applied-tag');
      const appliedIndex = $span.attr('data-applied-index');
      $span
        .removeAttr('data-applied-tag')
        .removeAttr('data-applied-index')
        .removeAttr('data-applied-label')
        .removeAttr('title')
        .removeClass(`grow-text-tagging__tag-target--tagged grow-text-tagging__tag-target--correct grow-text-tagging__tag-target--incorrect ${appliedTag ? `grow-text-tagging__tag-target--${appliedTag}` : ''} ${appliedIndex ? `grow-text-tagging__tag-target--tag-${appliedIndex}` : ''}`)
        .attr('aria-label', $span.text());
    });

    this.updateCounter();
  }

  restoreUserAnswer() {
    const allSpans = this.model.get('_allSpans') || [];
    const userAnswer = this.model.get('_userAnswer') || [];

    allSpans.forEach((span, i) => {
      const categoryIndex = userAnswer[i];
      if (categoryIndex === -1) return;

      const $span = this.$(`.js-grow-text-tagging-tag-target[data-span-id="${span._spanId}"]`);
      this._applyTag($span, span._spanId, categoryIndex);
    });

    this.updateCounter();

    if (this.model.get('_isSubmitted')) {
      this.showMarking();
      this.disableQuestion();
    }
  }

  disableQuestion() {
    this.$('.js-grow-text-tagging-tag-btn').attr('disabled', true).attr('tabindex', '-1');
    this.$('.js-grow-text-tagging-tag-target').attr('tabindex', '-1');
  }

  enableQuestion() {
    this.$('.js-grow-text-tagging-tag-btn').removeAttr('disabled').attr('tabindex', '0');
    this.$('.js-grow-text-tagging-tag-target').attr('tabindex', '0');
  }

  /**
   * Adds correct/incorrect marking classes and surfaces each span's
   * `feedback` string via a tooltip-style title attribute. Note the matching
   * CSS selectors in less/grow-text-tagging.less are scoped under both the page
   * body and `.modal`/`.popup` - the source CSS only covered `.lap`, so
   * marking rings never rendered inside the activity modal there.
   */
  showMarking() {
    const allSpans = this.model.get('_allSpans') || [];
    const userAnswer = this.model.get('_userAnswer') || [];
    const categories = this.model.get('_tagCategories') || [];
    const labelFor = id => {
      const category = categories.find(c => c._id === id);
      return category ? category.label : id;
    };

    const notes = [];

    allSpans.forEach((span, i) => {
      const chosenCategory = categories[userAnswer[i]];
      const isCorrect = !!chosenCategory && chosenCategory._id === span._tagId;

      const $span = this.$(`.js-grow-text-tagging-tag-target[data-span-id="${span._spanId}"]`);

      $span
        .removeClass('grow-text-tagging__tag-target--correct grow-text-tagging__tag-target--incorrect')
        .addClass(isCorrect ? 'grow-text-tagging__tag-target--correct' : 'grow-text-tagging__tag-target--incorrect');

      if (isCorrect) {
        if (span.feedback) $span.attr('title', span.feedback);
        return;
      }

      // Wrong, or left untagged: say why, from the authored feedbackIncorrect
      // or a generated explanation naming the chosen vs. the correct category.
      const chosenLabel = chosenCategory ? chosenCategory.label : null;
      const why = span.feedbackIncorrect
        || (chosenLabel
          ? `"${span.text}" is not ${chosenLabel}; it is ${labelFor(span._tagId)}.`
          : `"${span.text}" should be tagged as ${labelFor(span._tagId)}.`);
      $span.attr('title', why);
      notes.push(why);
    });

    const $feedback = this.$('.js-grow-text-tagging-feedback');
    if (notes.length) {
      $feedback.html(notes.map(note => `<li>${note}</li>`).join('')).removeAttr('hidden');
    } else {
      $feedback.empty().attr('hidden', '');
    }
  }

  hideMarking() {
    this.$('.js-grow-text-tagging-tag-target')
      .removeClass('grow-text-tagging__tag-target--correct grow-text-tagging__tag-target--incorrect')
      .removeAttr('title');
    this.$('.js-grow-text-tagging-feedback').empty().attr('hidden', '');
  }

}
