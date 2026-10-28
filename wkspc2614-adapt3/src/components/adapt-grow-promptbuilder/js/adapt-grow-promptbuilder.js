/*
 * adapt-grow-promptbuilder
 * The learner assembles a learning prompt from a Role, a Function and some
 * Context. Clicking an example chip inserts its text into that part; the parts
 * combine live (via _assembleTemplate) into a full prompt they can copy. Teaches
 * the Role/Function/Context framework by doing. Completes once every part is
 * filled.
 *
 * Like the other GROW components, the view calls setReadyStatus() itself (core
 * ComponentView.postRender is a no-op), or the loading curtain never lifts.
 */
import Adapt from 'core/js/adapt';
import ComponentView from 'core/js/views/componentView';
import ComponentModel from 'core/js/models/componentModel';

class PromptBuilderView extends ComponentView {

  events() {
    return {
      'click .js-pb-chip': 'onChip',
      'input .js-pb-input': 'onInput',
      'change .js-pb-input': 'onInput',
      'click .js-pb-copy': 'onCopy',
      'click .js-pb-clear': 'onClear'
    };
  }

  postRender() {
    this.$inputs = this.$('.js-pb-input');
    this.$out = this.$('.js-pb-output');
    this.$copy = this.$('.js-pb-copy');
    this.$clear = this.$('.js-pb-clear');
    this.template = this.model.get('_assembleTemplate') || 'Act as {role}. {function} Context: {context}.';
    this.assemble();
    this.setReadyStatus();
  }

  partValues() {
    const v = {};
    this.$inputs.each((i, el) => { v[el.getAttribute('data-key')] = (el.value || '').trim(); });
    return v;
  }

  assemble() {
    const v = this.partValues();
    let out = this.template.replace(/\{(\w+)\}/g, (m, k) => v[k] || `[${k}]`);
    if (this.$out.length) this.$out.text(out);
    const allFilled = this.$inputs.length > 0 && Object.values(v).every(s => s.length > 0);
    this.$('.prompt-builder').toggleClass('is-ready', allFilled);
    if (this.$copy.length) this.$copy.prop('disabled', !allFilled);
    if (allFilled && this.model.get('_setCompletionOn') !== 'inview' && !this.model.get('_isComplete')) {
      this.setCompletionStatus();
    }
  }

  onChip(e) {
    const btn = e.currentTarget;
    const key = btn.getAttribute('data-key');
    const text = btn.getAttribute('data-text') || btn.textContent.trim();
    const input = this.$(`.js-pb-input[data-key="${key}"]`)[0];
    if (!input) return;
    const cur = input.value.trim();
    input.value = cur ? `${cur} ${text}` : text;
    this.assemble();
    input.focus();
  }

  onInput() { this.assemble(); }

  onClear() {
    // Reset every field (text boxes and dropdowns both expose .value), re-assemble
    // so the output/copy/completion state follows, and return focus to the first.
    this.$inputs.each((i, el) => { el.value = ''; });
    this.assemble();
    const first = this.$inputs[0];
    if (first) first.focus();
  }

  onCopy() {
    const text = this.$out.text();
    const done = () => {
      const $c = this.$copy;
      const orig = $c.text();
      $c.text('Copied');
      setTimeout(() => $c.text(orig), 1500);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done).catch(() => done());
    } else {
      try {
        const ta = document.createElement('textarea');
        ta.value = text; document.body.appendChild(ta); ta.select();
        document.execCommand('copy'); document.body.removeChild(ta);
      } catch (e) { /* no-op */ }
      done();
    }
  }

}

export default Adapt.register('growPromptBuilder', {
  view: PromptBuilderView,
  model: ComponentModel
});
