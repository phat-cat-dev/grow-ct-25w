/*
 * adapt-grow-promptbuilder
 * The learner assembles a learning prompt from parts (e.g. Role, Function,
 * Context). Each part has quick example chips AND/OR a dropdown of fuller
 * "starters" grouped by level; picking a starter fills that field, chips append.
 * The parts combine live (via _assembleTemplate) into a prompt they can copy.
 * Completes once every part is filled.
 *
 * Starters can be inlined on a part (_starters / _starterGroups) OR pulled from
 * a shared library on the course model (_growPromptLibraries) via _library.
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
      'change .js-pb-starter': 'onStarter',
      'click .js-pb-copy': 'onCopy',
      'click .js-pb-clear': 'onClear'
    };
  }

  preRender() {
    this.resolveLibraries();
  }

  // A part may reference a shared starter library instead of inlining starters:
  //   part._library = "<libraryId>"  (+ optional part._libraryStage, else _key)
  // Libraries live on the course model as _growPromptLibraries:
  //   { "<libraryId>": { "<stage>": [ { "label": "...", "items": [...] }, ... ] } }
  // Inline _starterGroups / _starters win, unless _libraryMerge appends the
  // library's groups after the inline ones.
  resolveLibraries() {
    const libs = Adapt.course && Adapt.course.get('_growPromptLibraries');
    if (!libs) return;
    (this.model.get('_parts') || []).forEach(p => {
      const hasInline = (p._starterGroups && p._starterGroups.length) || (p._starters && p._starters.length);
      if (!p._library || (hasInline && !p._libraryMerge)) return;
      const lib = libs[p._library];
      const groups = lib && lib[p._libraryStage || p._key];
      if (!groups || !groups.length) return;
      // a stage that is a plain list of strings fills a select part's options
      if (typeof groups[0] === 'string') {
        if (!(p._options && p._options.length)) p._options = groups;
        return;
      }
      if (p._libraryMerge && p._starterGroups && p._starterGroups.length) {
        if (!p._libraryMerged) p._starterGroups = p._starterGroups.concat(groups);
        p._libraryMerged = true;
      } else {
        p._starterGroups = groups;
      }
    });
  }

  postRender() {
    this.$inputs = this.$('.js-pb-input');
    this.$out = this.$('.js-pb-output');
    this.$copy = this.$('.js-pb-copy');
    this.$clear = this.$('.js-pb-clear');
    this.template = this.model.get('_assembleTemplate') || 'Act as {role}. {function} Context: {context}.';
    this.applyFilters();
    this.assemble();
    this.setReadyStatus();
  }

  // A part with _filterBy: "<key>" shows only the starter groups whose `filter`
  // matches that part's current value (groups with no filter always show; an
  // empty value shows everything). E.g. an "Academic practice" select narrows the
  // Function, Role and Verb starters to one pathway.
  applyFilters() {
    const v = this.partValues();
    (this.model.get('_parts') || []).forEach(p => {
      if (!p._filterBy || !(p._starterGroups && p._starterGroups.length)) return;
      const sel = this.$(`.js-pb-starter[data-key="${p._key}"]`)[0];
      if (!sel) return;
      const want = v[p._filterBy] || '';
      const placeholder = sel.options[0] ? sel.options[0].textContent : '';
      sel.textContent = '';
      sel.appendChild(new Option(placeholder, ''));
      p._starterGroups
        .filter(g => !g.filter || !want || g.filter === want)
        .forEach(g => {
          const og = document.createElement('optgroup');
          og.label = g.label;
          (g.items || []).forEach(item => og.appendChild(new Option(item, item)));
          sel.appendChild(og);
        });
    });
  }

  partValues() {
    const v = {};
    this.$inputs.each((i, el) => { v[el.getAttribute('data-key')] = (el.value || '').trim(); });
    return v;
  }

  // Two passes: the template pulls in each part's text, then any {slot} inside
  // that text (e.g. a starter's {verb} or {topic}) is filled from the parts too.
  // An empty optional part drops out of the template; inside a starter it shows
  // as [key] so the learner sees what is still to fill.
  assemble() {
    const v = this.partValues();
    const optional = new Set((this.model.get('_parts') || []).filter(p => p._optional).map(p => p._key));
    const top = this.template.replace(/\{(\w+)\}/g, (m, k) => v[k] || (optional.has(k) ? '' : `[${k}]`));
    const out = top.replace(/\{(\w+)\}/g, (m, k) => v[k] || `[${k}]`).replace(/\s{2,}/g, ' ').trim();
    if (this.$out.length) this.$out.text(out);
    const allFilled = this.$inputs.length > 0 &&
      Object.keys(v).every(k => optional.has(k) || v[k].length > 0);
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

  // A starter from the dropdown REPLACES the field (pick one, then edit it),
  // then the dropdown returns to its placeholder so it reads as an inserter.
  onStarter(e) {
    const sel = e.currentTarget;
    const key = sel.getAttribute('data-key');
    const text = sel.value;
    sel.selectedIndex = 0;
    if (!text) return;
    const input = this.$(`.js-pb-input[data-key="${key}"]`)[0];
    if (!input) return;
    input.value = text;
    this.assemble();
    input.focus();
  }

  onInput(e) {
    const key = e && e.currentTarget && e.currentTarget.getAttribute('data-key');
    if (key && (this.model.get('_parts') || []).some(p => p._filterBy === key)) this.applyFilters();
    this.assemble();
  }

  onClear() {
    this.$inputs.each((i, el) => { el.value = ''; });
    this.$('.js-pb-starter').each((i, el) => { el.selectedIndex = 0; });
    this.applyFilters();
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
