import Adapt from 'core/js/adapt';
import a11y from 'core/js/a11y';
import ComponentView from 'core/js/views/componentView';
import * as ChartLib from './vendor/chart.umd.min.js';

/**
 * ConfidenceView — view for the pre/post self-efficacy component.
 * Extends ComponentView (NOT QuestionView) per AR-1/BP-1a.
 * Renders JSX, captures ratings, handles submit.
 *
 * POST only: after submit, draws a Chart.js grouped bar chart comparing each
 * statement's Before (pre) and After (post) rating. The chart is a visual echo
 * of the per-item movement list and the summary — never the only carrier of the
 * meaning (the list + table below hold the exact numbers), and it degrades
 * gracefully to nothing if Chart.js is unavailable.
 */
class ConfidenceView extends ComponentView {

  events() {
    return {
      'change .js-grow-confidence-radio': 'onRatingChange',
      'click .js-grow-confidence-submit': 'onSubmitClick'
    };
  }

  preRender() {
    // Listen for model changes to re-render
    this.listenTo(this.model, 'change:_ratings change:_feedback', this.changed);
    // FIX 5: PRE completed after this POST was submitted — the model has
    // recomputed the before/after, so redraw the comparison chart (the
    // change:_feedback re-render above has already rebuilt the <canvas>).
    this.listenTo(this.model, 'confidence:pre-resolved', () => {
      if (this.model.getMode() === 'post' && this.model.get('_isSubmitted')) {
        _.defer(() => this._renderChart());
      }
    });
  }

  postRender() {
    // Set ready when images/content loaded
    this.$('.component__widget').imageready(this.setReadyStatus.bind(this));
    // Revisit case: POST already submitted on mount — draw the chart once the DOM is in.
    if (this.model.getMode() === 'post' && this.model.get('_isSubmitted')) {
      _.defer(() => this._renderChart());
    }
  }

  /**
   * Handle rating selection.
   */
  onRatingChange(event) {
    const $radio = $(event.currentTarget);
    const itemIndex = parseInt($radio.attr('data-item-index'), 10);
    const rating = parseInt($radio.val(), 10);

    this.model.setRating(itemIndex, rating);
  }

  /**
   * Handle submit button click.
   */
  onSubmitClick(event) {
    event.preventDefault();

    if (!this.model.canSubmit()) {
      // Could show error, but BS-4 says button should be disabled
      return;
    }

    this.model.submit();

    // Re-render to show feedback (POST) or confirmation (PRE)
    this.changed();

    // For POST, move focus to feedback region for a11y and draw the comparison chart
    if (this.model.getMode() === 'post') {
      this._focusFeedback();
      // Defer so the re-rendered feedback DOM (with the <canvas>) exists first.
      _.defer(() => this._renderChart());
    }
  }

  /**
   * Move focus to feedback region after POST submit.
   */
  _focusFeedback() {
    // Defer to allow DOM update
    _.defer(() => {
      const $feedback = this.$('.grow-confidence__feedback');
      if ($feedback.length) {
        a11y.focusFirst($feedback);
      }
    });
  }

  /**
   * Resolve the Chart constructor across bundler interop shapes and the global.
   * The vendored UMD (chart.umd.min.js) auto-registers all controllers at load.
   */
  _resolveChart() {
    // Bundler interop: namespace import may expose the ctor as .default or .Chart
    // (CommonJS transform applied); otherwise the UMD ran for its side effect and
    // set window.Chart (global branch). Cover all shapes.
    const candidate = ChartLib && (ChartLib.default || ChartLib.Chart);
    if (typeof candidate === 'function') return candidate;
    if (typeof ChartLib === 'function') return ChartLib;
    if (typeof window !== 'undefined' && typeof window.Chart === 'function') return window.Chart;
    return null;
  }

  /**
   * POST only: draw the Before/After comparison bar chart.
   * Fed purely from the model's computed feedback items (preRating/postRating),
   * so it stays in step with the list and summary. No-op (and harmless) unless
   * POST, submitted, not standalone, and Chart.js is available.
   */
  _renderChart() {
    if (this.model.getMode() !== 'post') return;
    if (!this.model.get('_isSubmitted') || this.model.isStandalone()) return;

    const items = this.model.getFeedbackItems() || [];
    if (!items.length) return;

    const canvas = this.$('.js-grow-confidence-chart')[0];
    if (!canvas) return;

    const Chart = this._resolveChart();
    if (!Chart) return; // graceful: the list + numbers below still tell the story

    this._destroyChart();

    // Belt-and-braces: UMD already registered, but register again in case a
    // tree-shaken build ever replaces the vendored file. Idempotent, guarded.
    try { Chart.register?.(...(Chart.registerables || [])); } catch (e) { /* already registered */ }

    const host = canvas.closest('.grow-confidence__chart') || canvas;
    const css = getComputedStyle(host);
    const token = (name, fallback) => (css.getPropertyValue(name).trim() || fallback);
    const before = token('--confidence-before', '#9aa5ad');
    const after = token('--confidence-after', '#61b5e5');
    // Axis/legend text: use the host's actual rendered text colour so it is
    // correct in any theme (light-on-dark included), not a guessed token.
    const ink = (css.color && css.color !== 'rgba(0, 0, 0, 0)') ? css.color : token('--ab-base-ink', '#1a1a1a');
    const gridColour = token('--ab-base-hairline', 'rgba(128,128,128,0.25)');
    const reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const strip = html => String(html || '').replace(/<[^>]+>/g, '').trim();

    try {
      this._chart = new Chart(canvas, {
        type: 'bar',
        data: {
          labels: items.map((_item, index) => String(index + 1)),
          datasets: [
            { label: 'Before', data: items.map(fi => fi.preRating), backgroundColor: before, borderWidth: 0, borderRadius: 4, maxBarThickness: 44 },
            { label: 'After', data: items.map(fi => fi.postRating), backgroundColor: after, borderWidth: 0, borderRadius: 4, maxBarThickness: 44 }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          animation: reduceMotion ? false : { duration: 350 },
          scales: {
            y: {
              min: 0, max: 5,
              ticks: { stepSize: 1, color: ink },
              grid: { color: gridColour },
              title: { display: true, text: 'Confidence (1–5)', color: ink }
            },
            x: {
              ticks: { color: ink },
              grid: { display: false },
              title: { display: true, text: 'Statement (see list below)', color: ink }
            }
          },
          plugins: {
            legend: { labels: { color: ink } },
            tooltip: {
              callbacks: {
                title: ctx => strip(items[ctx[0].dataIndex] && items[ctx[0].dataIndex].itemText)
              }
            }
          }
        }
      });
    } catch (e) {
      // Chart failed to construct — leave the textual feedback as the record.
      this._chart = null;
    }
  }

  _destroyChart() {
    if (this._chart) {
      try { this._chart.destroy(); } catch (e) { /* noop */ }
      this._chart = null;
    }
  }

  preRemove() {
    this._destroyChart();
    super.preRemove();
  }

}

ConfidenceView.template = 'growConfidence.jsx';

export default ConfidenceView;
