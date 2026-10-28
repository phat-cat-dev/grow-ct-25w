/**
 * adapt-grow-marks
 *
 * An extension that draws hand-drawn ink marks (from the grow-marks engine)
 * onto content in ANY component — the cross-component companion to the
 * adapt-grow-annotate component. Two jobs:
 *
 *  1. Author-tagged draw-on. An author marks words in any text field:
 *
 *       <span data-gm-mark="underline" data-gm-color="accent">matters</span>
 *       <span data-gm-mark="oval">the key idea</span>
 *
 *     and the mark draws on when that word scrolls into view. Zero-config —
 *     on wherever a data-gm-mark span appears. Options come from data-gm-*:
 *     data-gm-mark (required), data-gm-color, data-gm-speed, data-gm-hold.
 *
 *  2. Question right/wrong. Opt-in per question — when the author sets
 *     `_growMarks._feedback._isEnabled`, the extension plays a mark on the
 *     question when it is answered (tick for correct, cross for wrong by
 *     default, both overridable).
 *
 * Enable/disable globally in course.json (default ENABLED):
 *   "_growMarks": { "_isEnabled": false }
 *
 * Deliberately scoped: it marks author-tagged targets and reacts to question
 * state. It does NOT try to pick an arbitrary word inside a foreign component
 * at runtime (fragile); tag the word, or target it with a selector.
 *
 * @license GPL-3.0
 */

import Adapt from 'core/js/adapt';
import logging from 'core/js/logging';
import { drawMark, ensureMarkDefs } from './libs/growMarks.js';
import { markFromDataset } from './libs/marksLogic.js';
import { isGloballyEnabled, isFeedbackEnabled, resolveFeedbackMark } from './marksExtensionLogic.js';

const LOG = '[grow-marks]';
const INIT_ATTR = 'data-gm-init';

class GrowMarks {

  constructor() {
    this._observer = null;
    this._handles = [];          // tagged draw-on handles for the current page
    this._feedback = {};         // componentId -> feedback mark handle (so re-submits replace, not stack)
    Adapt.once('adapt:start', this.onStart.bind(this));
    Adapt.on('pageView:ready', this.onPageReady.bind(this));
    Adapt.on('questionView:showFeedback', this.onQuestionFeedback.bind(this));
    Adapt.on('router:location', this.onNavigate.bind(this));
  }

  enabled() {
    return isGloballyEnabled(Adapt.course && Adapt.course.get('_growMarks'));
  }

  reducedMotion() {
    return typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  onStart() {
    if (this.enabled()) ensureMarkDefs();
  }

  // --- 1. author-tagged draw-on ---------------------------------------------

  onPageReady(view) {
    if (!this.enabled()) return;
    const root = (view && view.$el && view.$el[0]) || document;
    this.observeTagged(root);
  }

  observeTagged(root) {
    const nodes = [...root.querySelectorAll(`[data-gm-mark]:not([${INIT_ATTR}])`)];
    if (!nodes.length) return;

    // No observer support, or reduced motion: just draw them (shown complete).
    if (typeof IntersectionObserver !== 'function' || this.reducedMotion()) {
      nodes.forEach(node => this.drawTagged(node));
      return;
    }

    if (!this._observer) {
      this._observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
          if (!entry.isIntersecting) return;
          obs.unobserve(entry.target);
          this.drawTagged(entry.target);
        });
      }, { threshold: 0.25 });
    }
    nodes.forEach(node => this._observer.observe(node));
    logging.debug(`${LOG} observing ${nodes.length} tagged mark(s)`);
  }

  drawTagged(node) {
    if (node.hasAttribute(INIT_ATTR)) return;
    node.setAttribute(INIT_ATTR, 'true');
    try {
      this._handles.push(drawMark(node, markFromDataset(node.dataset)));
    } catch (e) {
      logging.warn(`${LOG} could not draw a tagged mark: ${e.message}`);
    }
  }

  // --- 2. question right/wrong ----------------------------------------------

  onQuestionFeedback(view) {
    if (!this.enabled() || !view || !view.model) return;
    const config = view.model.get('_growMarks');
    if (!isFeedbackEnabled(config)) return;

    const id = view.model.get('_id');
    if (this._feedback[id]) { this._feedback[id].remove(); delete this._feedback[id]; }

    const { mark, color } = resolveFeedbackMark(this.isCorrect(view.model), config);
    const target = this.feedbackTarget(view, config);
    if (!target) return;
    try {
      this._feedback[id] = drawMark(target, { mark, color });
    } catch (e) {
      logging.warn(`${LOG} feedback mark failed: ${e.message}`);
    }
  }

  isCorrect(model) {
    if (typeof model.isCorrect === 'function') {
      const result = model.isCorrect();
      if (result != null) return !!result;
    }
    return !!model.get('_isCorrect');
  }

  feedbackTarget(view, config) {
    const el = view.$el && view.$el[0];
    if (!el) return null;
    const selector = config && config._feedback && config._feedback._target;
    const find = sel => el.querySelector(sel);
    return (selector && find(selector))
      || find('[data-gm-feedback]')
      || find('.component__title-inner')
      || find('.component__title')
      || find('.component__inner')
      || el;
  }

  // --- teardown on page change ----------------------------------------------

  onNavigate() {
    if (this._observer) { this._observer.disconnect(); this._observer = null; }
    this._handles.forEach(handle => { try { handle.remove(); } catch (e) { /* gone with the DOM */ } });
    this._handles = [];
    this._feedback = {};
  }

}

export default new GrowMarks();

logging.debug(`${LOG} extension loaded`);
