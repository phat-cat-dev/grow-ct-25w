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
      'click .annotate__reset': 'onReset'
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

    // Restore any saved annotations (no animation on revisit).
    this.model.restoreUserAnswers();
    const saved = this.model.getAnnotations();
    Object.keys(saved).forEach(key => this._renderMark(key, saved[key], false));

    // Completion: min 0 means "complete on view"; otherwise handled on interaction.
    if ((this.model.get('_minAnnotations') || 0) <= 0) {
      this.setupInviewCompletion('.component__widget');
    }
    this.model.checkCompletion();

    this.setReadyStatus();
  }

  onToolClick(event) {
    const id = event.currentTarget.getAttribute('data-tool');
    this._activeTool = id;
    this.$('.annotate__tool').each((index, button) => {
      button.setAttribute('aria-pressed', String(button.getAttribute('data-tool') === id));
    });
  }

  onTargetClick(event) {
    if (!this._activeTool) return;
    const button = event.currentTarget;
    const key = button.getAttribute('data-key');
    const applied = this.model.setAnnotation(key, this._activeTool);
    this._renderMark(key, applied, true);
    this._announce(button, applied);
  }

  onReset() {
    const keys = this.model.get('_targetKeys') || [];
    keys.forEach(key => this._renderMark(key, undefined, false));
    this.model.clearAnnotations();
    this._setStatus('Annotations cleared.');
  }

  _targetEl(key) {
    return this.$(`.annotate__target[data-key="${key}"]`)[0];
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
      chip.className = 'annotate__tag';
      chip.setAttribute('aria-hidden', 'true');
      chip.textContent = tool.label;
      button.after(chip);
      this._chips[key] = chip;
    }
  }

  _announce(button, toolId) {
    const word = (button.textContent || '').trim();
    const tool = toolId ? this.model.getTool(toolId) : null;
    this._setStatus(tool ? `${word} marked: ${tool.label}` : `${word} unmarked`);
  }

  _setStatus(text) {
    const status = this.$('.annotate__status')[0];
    if (status) status.textContent = text;
  }

  preRemove() {
    Object.values(this._marks || {}).forEach(handle => handle.remove());
    super.preRemove();
  }

}

AnnotateView.template = 'annotate.jsx';

export default AnnotateView;
