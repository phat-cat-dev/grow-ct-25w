/**
 * OpenTextView
 *
 * View for the open-text component. Extends ComponentView (NOT QuestionView)
 * to stay outside the scoring machinery.
 *
 * Stage 3: auto-grow, character counter, status line updates.
 * Stage 4: completion button and state.
 * Stage 6: over-limit border cascade via widget class.
 * - Auto-grow: textarea resizes to content, up to _maxRows
 * - Counter: visible when approaching/over limit (spec §8)
 * - Status line: updates on save success/failure (spec §9.3)
 * - Completion: button press checks limits, sets completion, announces (spec §7)
 * - All learner-facing strings from schema globals (spec §10)
 */

import Adapt from 'core/js/adapt';
import ComponentView from 'core/js/views/componentView';

class OpenTextView extends ComponentView {

  events() {
    return {
      'input .grow-opentext__textarea': 'onInput',
      'blur .grow-opentext__textarea': 'onBlur',
      'click .grow-opentext__complete-btn': 'onCompletionPress',
      'click .grow-opentext__expand-btn': 'onExpandToggle'
    };
  }

  /**
   * Extend model data with computed properties for the template (spec §2).
   */
  getData() {
    const data = super.getData();
    data._resolvedPlaceholder = this.model.getPlaceholder();
    data._initialText = this.model.getText();
    // Pass globals to template for status line default and completion strings
    data._globals = this._getGlobals();
    // Completion state for template rendering (spec §7)
    data._shouldShowCompletionButton = this.model.shouldShowCompletionButton();
    return data;
  }

  /**
   * Get component globals from Adapt config.
   * @private
   */
  _getGlobals() {
    return Adapt.course?.get('_globals')?._components?._growOpentext || {};
  }

  /**
   * Interpolate placeholders in a template string.
   * Uses {{name}} syntax, matching adapt-grow-confidence pattern.
   * Placeholders are numeric only (count, max, over, remaining).
   * @private
   */
  _interpolate(template, values) {
    if (!template) return '';
    return template.replace(/\{\{(\w+)\}\}/g, (match, key) => {
      const value = values[key];
      if (value === undefined) return match;
      // Only apply toLocaleString to numbers
      return typeof value === 'number' ? value.toLocaleString() : value;
    });
  }

  /**
   * Set up the component after initial render.
   */
  postRender() {
    // Cache DOM elements
    this.$widget = this.$('.grow-opentext__widget');
    this.$textarea = this.$('.grow-opentext__textarea');
    this.$counter = this.$('.grow-opentext__counter');
    this.$overLimit = this.$('.grow-opentext__over-limit');
    this.$status = this.$('.grow-opentext__status');
    this.$liveRegion = this.$('.grow-opentext__live-region');
    this.$alert = this.$('.grow-opentext__alert');
    // Completion elements (spec §7)
    this.$completionContainer = this.$('.grow-opentext__completion');
    this.$completionBtn = this.$('.grow-opentext__complete-btn');
    this.$completedState = this.$('.grow-opentext__completed-state');
    // Manual expand/collapse control
    this.$expandBtn = this.$('.grow-opentext__expand-btn');
    this._isManuallyExpanded = false;

    // Track which thresholds have been announced (spec §9.2)
    // Once announced, stays announced for this component instance
    this._announcedApproaching = false;
    this._announcedOver = false;

    // Create debounced save function with maxWait (spec §6)
    // 2000ms idle before save, but always save at least every 15000ms
    this._debouncedSave = _.debounce(
      this._saveText.bind(this),
      2000,
      { maxWait: 15000 }
    );

    // Run auto-grow on restored text (spec §9.4)
    this._autoGrow();

    // Update counter for restored text
    this._updateCounter();

    // If already complete on restore, show completed state (spec §7)
    if (this.model.get('_isComplete')) {
      this._showCompletedState();
    }

    this.setReadyStatus();
  }

  /**
   * Handle input event — update model, auto-grow, counter, trigger save.
   */
  onInput() {
    const text = this.$textarea.val();
    this.model.setText(text);

    // Auto-grow textarea (spec §9.4) — skipped while manually expanded,
    // since that already holds the textarea at the _maxRows ceiling
    if (!this._isManuallyExpanded) this._autoGrow();

    // Update character counter (spec §8)
    this._updateCounter();

    // Trigger debounced save
    this._debouncedSave();
  }

  /**
   * Handle blur event — save immediately.
   */
  onBlur() {
    // Cancel any pending debounced save and save immediately
    if (this._debouncedSave) {
      this._debouncedSave.cancel();
    }
    this._saveText();
  }

  /**
   * Handle manual expand/collapse button press.
   * Auto-grow already fits the textarea to content on input, so this only
   * matters before the learner has typed anything (or to shrink back down).
   * Expanding forces height to the _maxRows ceiling; collapsing hands control
   * back to _autoGrow, which fits the actual content (never clips text).
   * @private
   */
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

  /**
   * Handle completion button press (spec §7).
   * Button is never disabled — always pressable, announces why if blocked.
   */
  onCompletionPress() {
    // Already complete — nothing to do (sticky completion)
    if (this.model.get('_isComplete')) return;

    const globals = this._getGlobals();

    // Check if over limit — cannot complete
    if (this.model.isOverLimit()) {
      // The over-limit message is already displayed by _updateCounter.
      // Announce it via live region if not already announced (spec §7 case 5)
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

    // Check if below minimum — cannot complete
    if (!this.model.meetsMinimum()) {
      // Announce the below-minimum message (spec §7 case 4)
      this._announce(globals.belowMinimumMessage);
      return;
    }

    // All conditions met — mark complete
    this.model.markComplete();
    this._showCompletedState();
    // No separate _announce() — focusing the completed-state element
    // announces its text, avoiding duplicate announcements (spec §9.5)
  }

  /**
   * Update UI to show completed state (spec §7, §9.5).
   * Replaces button with static "Completed" confirmation.
   * Moves focus to completed-state element to prevent focus loss.
   * @private
   */
  _showCompletedState() {
    if (!this.$completionContainer.length) return;

    // Hide button, show completed state
    this.$completionBtn.addClass('u-display-none');
    this.$completedState.removeClass('u-display-none');

    // Move focus to completed state (spec §9.5)
    // This also announces the element's text, so no separate _announce() needed
    this.$completedState.focus();
  }

  /**
   * Auto-grow textarea to fit content, up to _maxRows (spec §9.4).
   * Technique: reset height, measure scrollHeight, apply with ceiling.
   * @private
   */
  _autoGrow() {
    const textarea = this.$textarea[0];
    if (!textarea) return;

    const maxRows = this.model.get('_maxRows') || 20;
    const lineHeight = parseInt(window.getComputedStyle(textarea).lineHeight, 10) || 20;
    const maxHeight = maxRows * lineHeight;

    // Reset to auto to measure true scrollHeight
    textarea.style.height = 'auto';

    // Apply scrollHeight, capped at maxHeight
    const newHeight = Math.min(textarea.scrollHeight, maxHeight);
    textarea.style.height = newHeight + 'px';

    // Enable scrolling if over max
    textarea.style.overflowY = textarea.scrollHeight > maxHeight ? 'auto' : 'hidden';
  }

  /**
   * Update character counter visibility and content (spec §8).
   * Counter hidden until within 750 of limit; visible when approaching/over.
   * @private
   */
  _updateCounter() {
    if (!this.$counter.length) return;

    const globals = this._getGlobals();
    const wordMode = this.model.isWordMode();
    const count = wordMode ? this.model.getWordCount() : this.model.getCharacterCount();
    const max = wordMode ? this.model.get('_maxWords') : this.model.get('_maxCharacters');
    // How close to the limit the counter appears: ~50 words, else 750 characters.
    const threshold = wordMode ? 50 : 750;
    const remaining = max - count;

    // Counter / limit strings follow the active unit (words vs characters).
    const counterTpl = wordMode ? globals.counterTextWords : globals.counterText;
    const remainingTpl = wordMode ? globals.remainingAnnouncementWords : globals.remainingAnnouncement;
    const overLimitTpl = wordMode ? globals.overLimitTextWords : globals.overLimitText;

    // Counter text from schema (no fallback — schema defaults must resolve)
    const counterText = this._interpolate(counterTpl, { count, max });

    if (remaining > threshold) {
      // Under threshold — hide counter and over-limit message
      this.$widget.removeClass('is-over-limit');
      this.$counter.addClass('u-display-none');
      this.$overLimit.addClass('u-display-none');
    } else if (remaining >= 0) {
      // Approaching limit — show counter, hide over-limit
      this.$widget.removeClass('is-over-limit');
      this.$counter.removeClass('u-display-none');
      this.$counter.text(counterText);
      this.$counter.removeClass('is-over-limit');
      this.$overLimit.addClass('u-display-none');

      // Announce once when first crossing threshold (spec §9.2)
      if (!this._announcedApproaching) {
        this._announce(this._interpolate(remainingTpl, { remaining }));
        this._announcedApproaching = true;
      }
    } else {
      // Over limit — cascade to widget for textarea border (Stage 6)
      const over = Math.abs(remaining);
      this.$widget.addClass('is-over-limit');
      this.$counter.removeClass('u-display-none');
      this.$counter.text(counterText);
      this.$counter.addClass('is-over-limit');

      // Show over-limit message from schema (no fallback — schema defaults must resolve)
      const overLimitText = this._interpolate(overLimitTpl, { over });
      this.$overLimit.text(overLimitText);
      this.$overLimit.removeClass('u-display-none');

      // Announce once when first crossing over (spec §9.2)
      if (!this._announcedOver) {
        this._announce(overLimitText);
        this._announcedOver = true;
      }
    }
  }

  /**
   * Announce message via polite live region (spec §9.2).
   * @private
   */
  _announce(message) {
    if (!this.$liveRegion.length) return;
    // Clear first, then set — ensures re-announcement of same text
    this.$liveRegion.text('');
    setTimeout(() => this.$liveRegion.text(message), 50);
  }

  /**
   * Save text to offlineStorage via model.
   * Updates status line on success/failure (spec §9.3).
   * @private
   */
  _saveText() {
    const result = this.model.saveText();

    if (result && result.success) {
      // Clear any previous failure state
      this._setStatusNormal();
    } else if (result && !result.success) {
      // Show failure message (spec §9.3)
      this._setStatusFailed();
    }
    // If result is undefined (no SCORM), do nothing — status stays normal
  }

  /**
   * Set status line to normal state.
   * @private
   */
  _setStatusNormal() {
    if (!this.$status.length) return;
    const globals = this._getGlobals();
    // No fallback — schema defaults must resolve
    this.$status.text(globals.statusNormal);
    this.$status.removeClass('is-failed');
    this.$alert.text(''); // Clear alert
  }

  /**
   * Set status line to failed state (spec §9.3).
   * Uses role="alert" region for assertive announcement.
   * @private
   */
  _setStatusFailed() {
    if (!this.$status.length) return;
    const globals = this._getGlobals();
    // No fallback — schema defaults must resolve
    this.$status.text(globals.statusFailed);
    this.$status.addClass('is-failed');
    // Also push to alert region for immediate announcement
    this.$alert.text(globals.statusFailed);
  }

  /**
   * Clean up on remove.
   */
  remove() {
    // Cancel any pending debounced save
    if (this._debouncedSave) {
      this._debouncedSave.cancel();
    }
    super.remove();
  }

}

OpenTextView.template = 'growOpentext.jsx';

export default OpenTextView;
