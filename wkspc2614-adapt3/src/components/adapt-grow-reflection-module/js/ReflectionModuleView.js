/**
 * ReflectionModuleView
 *
 * View for the GROW reflection module. The writing half is the same lined
 * journal interaction as adapt-grow-journal (auto-grow, counter, autosave,
 * optional completion); the lens prompts are static and need no behaviour.
 *
 * Extends ComponentView (NOT QuestionView) — the module is reflective, never
 * scored.
 */

import Adapt from 'core/js/adapt';
import ComponentView from 'core/js/views/componentView';

class ReflectionModuleView extends ComponentView {

  events() {
    return {
      'input .grow-reflection-module__textarea': 'onInput',
      'blur .grow-reflection-module__textarea': 'onBlur',
      'click .grow-reflection-module__complete-btn': 'onCompletionPress',
      'click .grow-reflection-module__expand-btn': 'onExpandToggle'
    };
  }

  getData() {
    const data = super.getData();
    data._resolvedPlaceholder = this.model.getPlaceholder();
    data._initialText = this.model.getText();
    data._globals = this._getGlobals();
    data._shouldShowCompletionButton = this.model.shouldShowCompletionButton();
    return data;
  }

  _getGlobals() {
    return Adapt.course?.get('_globals')?._components?._growReflectionModule || {};
  }

  _interpolate(template, values) {
    if (!template) return '';
    return template.replace(/\{\{(\w+)\}\}/g, (match, key) => {
      const value = values[key];
      if (value === undefined) return match;
      return typeof value === 'number' ? value.toLocaleString() : value;
    });
  }

  postRender() {
    this.$widget = this.$('.grow-reflection-module__widget');
    this.$textarea = this.$('.grow-reflection-module__textarea');
    this.$counter = this.$('.grow-reflection-module__counter');
    this.$overLimit = this.$('.grow-reflection-module__over-limit');
    this.$status = this.$('.grow-reflection-module__status');
    this.$liveRegion = this.$('.grow-reflection-module__live-region');
    this.$alert = this.$('.grow-reflection-module__alert');
    this.$completionContainer = this.$('.grow-reflection-module__completion');
    this.$completionBtn = this.$('.grow-reflection-module__complete-btn');
    this.$completedState = this.$('.grow-reflection-module__completed-state');
    this.$expandBtn = this.$('.grow-reflection-module__expand-btn');
    this._isManuallyExpanded = false;

    this._announcedApproaching = false;
    this._announcedOver = false;

    this._debouncedSave = _.debounce(
      this._saveText.bind(this),
      2000,
      { maxWait: 15000 }
    );

    this._autoGrow();
    this._updateCounter();

    if (this.model.get('_isComplete')) {
      this._showCompletedState();
    }

    this.setReadyStatus();
  }

  onInput() {
    const text = this.$textarea.val();
    this.model.setText(text);
    if (!this._isManuallyExpanded) this._autoGrow();
    this._updateCounter();
    this._debouncedSave();
  }

  onBlur() {
    if (this._debouncedSave) this._debouncedSave.cancel();
    this._saveText();
  }

  onExpandToggle() {
    const textarea = this.$textarea[0];
    if (!textarea) return;

    const globals = this._getGlobals();
    this._isManuallyExpanded = !this._isManuallyExpanded;

    if (this._isManuallyExpanded) {
      const maxRows = this.model.get('_maxRows') || 20;
      const lineHeight = parseInt(window.getComputedStyle(textarea).lineHeight, 10) || 20;
      textarea.style.height = (maxRows * lineHeight) + 'px';
      textarea.style.overflowY = textarea.scrollHeight > (maxRows * lineHeight) ? 'auto' : 'hidden';
    } else {
      this._autoGrow();
    }

    this.$expandBtn
      .attr('aria-expanded', this._isManuallyExpanded.toString())
      .attr('aria-label', this._isManuallyExpanded ? globals.collapseButtonLabel : globals.expandButtonLabel)
      .toggleClass('is-expanded', this._isManuallyExpanded);
  }

  onCompletionPress() {
    if (this.model.get('_isComplete')) return;

    const globals = this._getGlobals();

    if (this.model.isOverLimit()) {
      if (!this._announcedOver) {
        const over = this.model.getOverLimitCount();
        const overLimitText = this._interpolate(
          this.model.isWordMode() ? globals.overLimitTextWords : globals.overLimitText,
          { over }
        );
        this._announce(overLimitText);
        this._announcedOver = true;
      }
      return;
    }

    if (!this.model.meetsMinimum()) {
      this._announce(globals.belowMinimumMessage);
      return;
    }

    this.model.markComplete();
    this._showCompletedState();
  }

  _showCompletedState() {
    if (!this.$completionContainer.length) return;
    this.$completionBtn.addClass('u-display-none');
    this.$completedState.removeClass('u-display-none');
    this.$completedState.focus();
  }

  /**
   * Auto-grow textarea to fit content, up to _maxRows. The ruled background uses
   * background-attachment:local so the lines scroll with the text.
   */
  _autoGrow() {
    const textarea = this.$textarea[0];
    if (!textarea) return;

    const maxRows = this.model.get('_maxRows') || 20;
    const lineHeight = parseInt(window.getComputedStyle(textarea).lineHeight, 10) || 20;
    const maxHeight = maxRows * lineHeight;

    textarea.style.height = 'auto';
    const newHeight = Math.min(textarea.scrollHeight, maxHeight);
    textarea.style.height = newHeight + 'px';
    textarea.style.overflowY = textarea.scrollHeight > maxHeight ? 'auto' : 'hidden';
  }

  _updateCounter() {
    if (!this.$counter.length) return;

    const globals = this._getGlobals();
    const wordMode = this.model.isWordMode();
    const count = wordMode ? this.model.getWordCount() : this.model.getCharacterCount();
    const max = wordMode ? this.model.get('_maxWords') : this.model.get('_maxCharacters');
    const threshold = wordMode ? 50 : 750;
    const remaining = max - count;

    const counterTpl = wordMode ? globals.counterTextWords : globals.counterText;
    const remainingTpl = wordMode ? globals.remainingAnnouncementWords : globals.remainingAnnouncement;
    const overLimitTpl = wordMode ? globals.overLimitTextWords : globals.overLimitText;

    const counterText = this._interpolate(counterTpl, { count, max });

    if (remaining > threshold) {
      this.$widget.removeClass('is-over-limit');
      this.$counter.addClass('u-display-none');
      this.$overLimit.addClass('u-display-none');
    } else if (remaining >= 0) {
      this.$widget.removeClass('is-over-limit');
      this.$counter.removeClass('u-display-none');
      this.$counter.text(counterText);
      this.$counter.removeClass('is-over-limit');
      this.$overLimit.addClass('u-display-none');

      if (!this._announcedApproaching) {
        this._announce(this._interpolate(remainingTpl, { remaining }));
        this._announcedApproaching = true;
      }
    } else {
      const over = Math.abs(remaining);
      this.$widget.addClass('is-over-limit');
      this.$counter.removeClass('u-display-none');
      this.$counter.text(counterText);
      this.$counter.addClass('is-over-limit');

      const overLimitText = this._interpolate(overLimitTpl, { over });
      this.$overLimit.text(overLimitText);
      this.$overLimit.removeClass('u-display-none');

      if (!this._announcedOver) {
        this._announce(overLimitText);
        this._announcedOver = true;
      }
    }
  }

  _announce(message) {
    if (!this.$liveRegion.length) return;
    this.$liveRegion.text('');
    setTimeout(() => this.$liveRegion.text(message), 50);
  }

  _saveText() {
    const result = this.model.saveText();
    if (result && result.success) {
      this._setStatusNormal();
    } else if (result && !result.success) {
      this._setStatusFailed();
    }
  }

  _setStatusNormal() {
    if (!this.$status.length) return;
    const globals = this._getGlobals();
    this.$status.text(globals.statusNormal);
    this.$status.removeClass('is-failed');
    this.$alert.text('');
  }

  _setStatusFailed() {
    if (!this.$status.length) return;
    const globals = this._getGlobals();
    this.$status.text(globals.statusFailed);
    this.$status.addClass('is-failed');
    this.$alert.text(globals.statusFailed);
  }

  remove() {
    if (this._debouncedSave) this._debouncedSave.cancel();
    super.remove();
  }

}

ReflectionModuleView.template = 'growReflectionModule.jsx';

export default ReflectionModuleView;
