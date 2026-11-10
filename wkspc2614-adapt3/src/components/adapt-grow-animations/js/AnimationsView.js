import ComponentView from 'core/js/views/componentView';
import { instanceMarkup } from './engine';

// One shared hand-drawn "ink" wobble filter, id="ink" — the same filter the GROW /
// Abbott theme injects. We only add it as a fallback so marks still wobble on a page
// that has no theme present. The base marks CSS references filter:url(#ink).
const INK_FILTER = '<svg class="grow-ink-defs" width="0" height="0" aria-hidden="true" ' +
  'focusable="false" style="position:absolute;width:0;height:0;overflow:hidden">' +
  '<filter id="ink" x="-20%" y="-20%" width="140%" height="140%" color-interpolation-filters="sRGB">' +
  '<feTurbulence type="fractalNoise" baseFrequency="0.016" numOctaves="2" seed="4" result="n"/>' +
  '<feDisplacementMap in="SourceGraphic" in2="n" scale="2"/></filter></svg>';

class AnimationsView extends ComponentView {

  preRender() {
    AnimationsView.injectInkFilter();
    this.buildMarks();
  }

  // Turn each authored mark into its self-contained HTML via the shared engine.
  // Unknown ids or bad options are skipped rather than breaking the component.
  buildMarks() {
    const marks = (this.model.get('_marks') || []).map(mark => {
      const options = {
        text: mark.text,
        over: mark.over,
        color: mark._color,
        speed: mark._speed,
        scale: mark._scale,
        rotation: mark._rotation,
        repeats: mark._repeats,
        jitter: mark._jitter,
        band: mark._band,
        play: true
      };
      try {
        return instanceMarkup(mark._id, options);
      } catch (error) {
        return '';
      }
    }).filter(Boolean);
    this.model.set('_marksHtml', marks);
  }

  postRender() {
    this.setReadyStatus();
  }

  static injectInkFilter() {
    if (typeof document === 'undefined') return;
    if (document.getElementById('ink')) return; // theme or a sibling already provides it
    document.body.insertAdjacentHTML('beforeend', INK_FILTER);
  }
}

AnimationsView.template = 'growAnimations.jsx';

export default AnimationsView;
