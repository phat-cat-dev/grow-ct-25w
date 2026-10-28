/**
 * AnnotateView — view for the annotate component.
 *
 * The JSX renders a static shell (palette of tools + the passage with target
 * buttons). After render, this view wires the interaction imperatively and
 * drives the grow-marks engine, exactly as scroll-scenes mounts its engine:
 * the marks are appended to the DOM by grow-marks, so we must NOT trigger a
 * React re-render that would discard them. There is therefore no changed()
 * path — all updates after mount are imperative.
 *
 * Flow: pick a tool (palette), click a target to apply/toggle it. The mark
 * animates in; a label chip and the live-region status update; the model
 * records state and completion.
 */

import ComponentView from 'core/js/views/componentView';
import { drawMark } from './libs/growMarks.js';

class AnnotateView extends ComponentView {

  events() {
    return {
      'click .annotate__tool': 'onToolClick',
      'click .annotate__target': 'onTargetClick',
      'click .annotate__reset': 'onReset',
      'click .annotate__submit': 'onSubmit'
    };
  }

  postRender() {
    this._marks = {};   // key -> grow-marks handle
    this._chips = {};   // key -> label chip element
    const tools = this.model.get('_tools') || [];
    this._activeTool = tools.length ? tools[0]._id : null;

    // Draw each tool's own mark onto its palette label, so the palette previews
    // the annotation. (autoplay:false — shown complete, no animation.)
    this.$('.annotate__tool').each((index, button) => {
      const id = button.getAttribute('data-tool');
      const tool = this.model.getTool(id);
      const label = button.querySelector('.annotate__tool-label');
      if (tool && label) {
        try { drawMark(label, { mark: tool._mark, color: tool._color, autoplay: false }); } catch (e) { /* unknown mark: leave the label plain */ }
      }
      button.setAttribute('aria-pressed', String(id === this._activeTool));
    });

    this._freeMarks = {}; // free-select: annotation id -> grow-marks handle

    if (this.model.isFreeSelect()) {
      this._wireFreeSelect();
      this.model.restoreUserAnswers();
      this.model.getFree().forEach(f => this._drawFree(f, false));
    } else {
      // Restore any saved annotations (no animation on revisit).
      this.model.restoreUserAnswers();
      const saved = this.model.getAnnotations();
      Object.keys(saved).forEach(key => this._renderMark(key, saved[key], false));
    }

    // Completion: min 0 means "complete on view"; otherwise handled on interaction.
    if ((this.model.get('_minAnnotations') || 0) <= 0) {
      this.setupInviewCompletion('.component__widget');
    }
    this.model.checkCompletion();

    this.setReadyStatus();
  }

  onToolClick(event) {
    if (this.model.get('_isSubmitted')) return;
    const id = event.currentTarget.getAttribute('data-tool');
    this._activeTool = id;
    this.$('.annotate__tool').each((index, button) => {
      button.setAttribute('aria-pressed', String(button.getAttribute('data-tool') === id));
    });
  }

  onTargetClick(event) {
    if (this.model.get('_isSubmitted')) return;
    if (!this._activeTool) return;
    const button = event.currentTarget;
    const key = button.getAttribute('data-key');
    const applied = this.model.setAnnotation(key, this._activeTool);
    this._renderMark(key, applied, true);
    // If this target was graded on a previous attempt, drop its stale red/green
    // now the learner is changing it; the feedback panel stays until they recheck.
    button.classList.remove('annotate__target--correct', 'annotate__target--incorrect');
    this._announce(button, applied);
  }

  onReset() {
    if (this.model.isFreeSelect()) return this._resetFree();
    const keys = this.model.get('_targetKeys') || [];
    keys.forEach(key => this._renderMark(key, undefined, false));
    this.model.clearAnnotations();
    this._setStatus('Annotations cleared.');

    if (this.model.get('_isQuestion')) {
      keys.forEach(key => {
        const el = this._targetEl(key);
        if (el) el.classList.remove('annotate__target--correct', 'annotate__target--incorrect');
      });
      this._resetQuestionUi();
    }
  }

  // Question mode: check the learner's marks against _answers and mark each
  // scored target correct/incorrect. If everything is right, lock the activity
  // (_lock). If not, keep it open so the learner can fix the marks shown in red
  // with the feedback still in front of them, then check again (_awaitRetry) -
  // they never have to clear and start over.
  onSubmit() {
    if (this.model.get('_isSubmitted')) return;
    const result = this.model.checkAnswers();
    if (!result.total) return; // nothing scored - treat as reflective
    if (this.model.isFreeSelect()) return this._submitFree(result);

    result.marks.forEach(mark => {
      if (!mark.isScored) return;
      const el = this._targetEl(mark.key);
      if (!el) return;
      el.classList.remove('annotate__target--correct', 'annotate__target--incorrect');
      el.classList.add(mark.isCorrect ? 'annotate__target--correct' : 'annotate__target--incorrect');
    });

    const feedback = this.model.get('_feedback') || {};
    const notes = [];
    if (!result.allCorrect) {
      result.marks.forEach(mark => {
        if (!mark.isScored || mark.isCorrect) return;
        const el = this._targetEl(mark.key);
        const word = this._targetWord(el);
        const correctTool = this.model.getTool(mark.correct);
        const correctLabel = correctTool ? correctTool.label : mark.correct;
        notes.push(mark.applied
          ? `"${word}" should be ${correctLabel}.`
          : `"${word}" still needs a mark - it should be ${correctLabel}.`);
      });
    }

    const summary = result.allCorrect
      ? (feedback.correct || 'All correct.')
      : (feedback._incorrect || 'Not quite - adjust the marks shown in red, then check again.');
    this._showFeedback(summary, notes, result.allCorrect);

    this.model.setCompletionStatus();
    this._setStatus(summary);

    if (result.allCorrect) this._lock();
    else this._awaitRetry();
  }

  // Render the summary line + per-target notes into the feedback panel.
  _showFeedback(summary, notes, allCorrect) {
    const items = [summary, ...notes].map(note => `<li>${note}</li>`).join('');
    this.$('.js-annotate-feedback')
      .removeClass('annotate__feedback--correct annotate__feedback--incorrect')
      .addClass(allCorrect ? 'annotate__feedback--correct' : 'annotate__feedback--incorrect')
      .html(items).removeAttr('hidden');
  }

  // All correct: freeze the activity in its solved state.
  _lock() {
    this.model.set('_isSubmitted', true);
    this.$('.annotate__tool').attr('disabled', true);
    this.$('.annotate__submit').attr('disabled', true).text('Submit');
    this.$el.addClass('is-submitted');
  }

  // Wrong, but keep the activity open: the learner corrects the marks in red and
  // rechecks instead of starting over. The marks and feedback stay in place.
  _awaitRetry() {
    this.model.set('_isSubmitted', false);
    this.$('.annotate__tool').removeAttr('disabled');
    this.$('.annotate__submit').removeAttr('disabled').text('Check again');
    this.$el.removeClass('is-submitted');
  }

  // Return the activity to a fresh, re-answerable state (used after a clear).
  _resetQuestionUi() {
    this.model.set('_isSubmitted', false);
    this.$('.annotate__tool').removeAttr('disabled');
    this.$('.annotate__submit').removeAttr('disabled').text('Submit');
    this.$el.removeClass('is-submitted');
    this.$('.js-annotate-feedback')
      .removeClass('annotate__feedback--correct annotate__feedback--incorrect')
      .empty().attr('hidden', '');
  }

  _targetEl(key) {
    return this.$(`.annotate__target[data-key="${key}"]`)[0];
  }

  // The target's own word text only - excludes the label chip and SVG the view
  // appends inside the button, so feedback quotes the word, not "wordLabel".
  _targetWord(el) {
    if (!el) return '';
    let text = '';
    el.childNodes.forEach(node => { if (node.nodeType === 3) text += node.textContent; });
    return text.trim();
  }

  /** Draw, replace or remove the mark + label chip on one target. */
  _renderMark(key, toolId, animate) {
    if (this._marks[key]) { this._marks[key].remove(); delete this._marks[key]; }
    if (this._chips[key]) { this._chips[key].remove(); delete this._chips[key]; }

    const button = this._targetEl(key);
    if (!button) return;

    const tool = toolId ? this.model.getTool(toolId) : null;
    button.classList.toggle('is-annotated', !!tool);

    if (!tool) {
      button.setAttribute('aria-pressed', 'false');
      return;
    }

    button.setAttribute('aria-pressed', 'true');
    try {
      this._marks[key] = drawMark(button, { mark: tool._mark, color: tool._color, autoplay: !!animate });
    } catch (e) { /* unknown mark id: skip the visual, keep state */ }

    if (this.model.get('_showLabels') !== false && tool.label) {
      const chip = document.createElement('span');
      chip.className = 'annotate__tag' + (tool._color ? ` annotate__tag--${tool._color}` : '');
      chip.setAttribute('aria-hidden', 'true');
      chip.textContent = tool.label;
      // Sit the chip inside the target so it can float above the word, on top of
      // the ink mark (appended last, after the grow-marks SVG).
      button.appendChild(chip);
      this._chips[key] = chip;
    }
  }

  _announce(button, toolId) {
    const word = this._targetWord(button);
    const tool = toolId ? this.model.getTool(toolId) : null;
    this._setStatus(tool ? `${word} marked: ${tool.label}` : `${word} unmarked`);
  }

  _setStatus(text) {
    const status = this.$('.annotate__status')[0];
    if (status) status.textContent = text;
  }

  // ---- free-selection mode --------------------------------------------------
  _wireFreeSelect() {
    const passage = this.$('.annotate__passage--free')[0];
    if (!passage) return;
    this._passageEl = passage;
    this._onSelectBound = () => this._onSelect();
    this._onMarkClickBound = (e) => {
      const span = e.target.closest && e.target.closest('.annotate__mark-span');
      if (span && passage.contains(span)) { e.preventDefault(); this._removeFree(span.getAttribute('data-id')); }
    };
    passage.addEventListener('mouseup', this._onSelectBound);
    passage.addEventListener('touchend', this._onSelectBound);
    passage.addEventListener('click', this._onMarkClickBound);
  }

  _wordEl(i) {
    return this._passageEl ? this._passageEl.querySelector(`.annotate__word[data-w="${i}"]`) : null;
  }

  _onSelect() {
    if (this.model.get('_isSubmitted') || !this._activeTool || !this._passageEl) return;
    const sel = window.getSelection && window.getSelection();
    if (!sel || sel.rangeCount === 0 || sel.isCollapsed) return;
    const range = sel.getRangeAt(0);
    const words = Array.prototype.filter.call(
      this._passageEl.querySelectorAll('.annotate__word'), w => range.intersectsNode(w));
    sel.removeAllRanges();
    if (!words.length) return;
    const idxs = words.map(w => Number(w.getAttribute('data-w')));
    const a = Math.min(...idxs), b = Math.max(...idxs);
    for (let i = a; i <= b; i++) {
      const w = this._wordEl(i);
      if (w && w.closest('.annotate__mark-span')) { this._setStatus('That overlaps a mark you have already made.'); return; }
    }
    const id = this.model.addFree({ a, b, tool: this._activeTool });
    this._drawFree({ id, a, b, tool: this._activeTool }, true);
    const tool = this.model.getTool(this._activeTool);
    this._setStatus(`Marked "${words.map(w => w.textContent).join(' ')}"${tool ? ': ' + tool.label : ''}`);
  }

  /** Wrap words a..b in a span and draw the tool's mark on it. */
  _drawFree(ann, animate) {
    const wa = this._wordEl(ann.a), wb = this._wordEl(ann.b);
    if (!wa || !wb) return;
    const range = document.createRange();
    range.setStartBefore(wa);
    range.setEndAfter(wb);
    const wrapper = document.createElement('span');
    wrapper.className = 'annotate__mark-span';
    wrapper.setAttribute('data-id', ann.id);
    wrapper.setAttribute('data-tool', ann.tool);
    try { range.surroundContents(wrapper); } catch (e) { return; }
    const tool = this.model.getTool(ann.tool);
    if (tool) {
      try { this._freeMarks[ann.id] = drawMark(wrapper, { mark: tool._mark, color: tool._color, autoplay: !!animate }); } catch (e) { /* unknown mark */ }
    }
  }

  _unwrap(id) {
    const handle = this._freeMarks[id];
    if (handle) { handle.remove(); delete this._freeMarks[id]; }
    const wrapper = this._passageEl && this._passageEl.querySelector(`.annotate__mark-span[data-id="${id}"]`);
    if (wrapper) {
      const parent = wrapper.parentNode;
      while (wrapper.firstChild) parent.insertBefore(wrapper.firstChild, wrapper);
      parent.removeChild(wrapper);
    }
  }

  _removeFree(id) {
    if (this.model.get('_isSubmitted')) return;
    this._unwrap(id);
    this.model.removeFree(id);
    this._setStatus('Mark removed.');
  }

  _resetFree() {
    (this.model.getFree() || []).slice().forEach(f => this._unwrap(f.id));
    this.model.clearFree();
    if (this.model.get('_isQuestion')) this._resetQuestionUi();
    this._setStatus('Annotations cleared.');
  }

  _submitFree(result) {
    // Clear outcome colouring from any earlier attempt before re-grading.
    this.$('.annotate__mark-span').removeClass('annotate__mark-span--correct annotate__mark-span--incorrect');
    result.annotations.forEach(an => {
      const wrapper = this._passageEl && this._passageEl.querySelector(`.annotate__mark-span[data-id="${an.id}"]`);
      if (wrapper) wrapper.classList.add(an.isCorrect ? 'annotate__mark-span--correct' : 'annotate__mark-span--incorrect');
    });
    const feedback = this.model.get('_feedback') || {};
    const notes = [];
    if (!result.allCorrect) {
      result.targets.forEach(tg => {
        if (tg.isFound) return;
        const tool = this.model.getTool(tg.tool);
        notes.push(`"${tg.text}" still needs ${tool ? tool.label : tg.tool}.`);
      });
    }
    const summary = result.allCorrect
      ? (feedback.correct || `All ${result.total} found.`)
      : (feedback._incorrect || `You found ${result.found} of ${result.total} - adjust your marks, then check again.`);
    this._showFeedback(summary, notes, result.allCorrect);
    this.model.setCompletionStatus();
    this._setStatus(summary);

    if (result.allCorrect) this._lock();
    else this._awaitRetry();
  }

  preRemove() {
    Object.values(this._marks || {}).forEach(handle => handle.remove());
    Object.values(this._freeMarks || {}).forEach(handle => handle.remove());
    if (this._passageEl) {
      this._passageEl.removeEventListener('mouseup', this._onSelectBound);
      this._passageEl.removeEventListener('touchend', this._onSelectBound);
      this._passageEl.removeEventListener('click', this._onMarkClickBound);
    }
    super.preRemove();
  }

}

AnnotateView.template = 'annotate.jsx';

export default AnnotateView;
