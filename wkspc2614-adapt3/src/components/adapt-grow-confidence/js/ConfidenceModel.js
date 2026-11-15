import Adapt from 'core/js/adapt';
import data from 'core/js/data';
import offlineStorage from 'core/js/offlineStorage';
import ItemsComponentModel from 'core/js/models/itemsComponentModel';
import { classifyItem, selectSummary } from './confidenceLogic';

/**
 * ConfidenceModel — model for the pre/post self-efficacy component.
 * Extends ItemsComponentModel (NOT QuestionModel) per AR-1/BP-1a.
 * No scoring, no correctness — only ratings and metacognitive feedback.
 */
export default class ConfidenceModel extends ItemsComponentModel {

  init() {
    this._mode = this.get('_mode') || 'pre';
    this._groupId = this.get('_selfAssessmentGroupId') || '';
    this._isStandalone = false;

    // POST: inherit items and scale from PRE BEFORE super.init() calls setUpItems()
    // (FIX 3/4: must modify _items before base sets up children)
    if (this._mode === 'post') {
      this._inheritFromPre();
    }

    // FIX 4: Let super.init() call setUpItems() — do NOT call it manually
    // Base ItemsComponentModel.init() calls setUpItems() then sets up listeners
    super.init();

    // Initialize ratings array AFTER items exist (FIX 4)
    const itemCount = this.getChildren().length;
    this._ratings = new Array(itemCount).fill(null);

    // FIX 5 (POST-completed-first): if the learner finishes POST before PRE,
    // there is no before/after yet, so the graph can't draw (standalone). Watch
    // the PRE component; when it later completes, recompute so the before/after
    // feedback + chart appear without needing a manual revisit of this page.
    if (this._mode === 'post') {
      const preModel = this._findPreModel();
      if (preModel) {
        this.listenTo(preModel, 'change:_isComplete', () => {
          if (this.get('_isSubmitted') && preModel.get('_isComplete')) {
            this._computeFeedback();                 // fresh-resolves PRE → clears standalone
            this.trigger('confidence:pre-resolved');  // view redraws the chart
          }
        });
      }
    }
  }

  /**
   * POST: find the PRE by _selfAssessmentGroupId and inherit its _items and _scale.
   * AR-3 load-time guard: warn if POST has its own items AND a PRE exists (drift).
   * SA-8: if no PRE exists at init, set _isStandalone (but re-check at compute time).
   */
  _inheritFromPre() {
    const ownItems = this.get('_items') || [];
    const preModel = this._findPreModel();

    if (!preModel) {
      // SA-8: no PRE reachable at init — standalone mode
      // (FIX 3: will re-check at compute time in case PRE was authored but not found)
      if (ownItems.length === 0) {
        console.warn(`[confidence] POST ${this.get('_id')}: no PRE found for group "${this._groupId}" and no own items. Running as standalone (SA-8).`);
        this._isStandalone = true;
      }
      return;
    }

    // AR-3 guard: POST has its own non-empty _items AND a PRE exists
    if (ownItems.length > 0) {
      console.warn(`[confidence] POST ${this.get('_id')}: has its own _items but PRE exists. Ignoring POST items to prevent drift (AR-3).`);
    }

    // Inherit items and scale from PRE (deep copy)
    const preItems = preModel.get('_items') || [];
    const preScale = preModel.get('_scale') || {};
    this.set('_items', JSON.parse(JSON.stringify(preItems)));
    this.set('_scale', JSON.parse(JSON.stringify(preScale)));
  }

  /**
   * Find the PRE component in the same group.
   * (FIX 3: single resolver used both at init and compute time)
   */
  _findPreModel() {
    const groupId = this._groupId;
    if (!groupId) return null;

    const preModels = data.filter(model =>
      model.get('_selfAssessmentGroupId') === groupId &&
      model.get('_mode') === 'pre' &&
      model.get('_id') !== this.get('_id')
    );
    return preModels.length > 0 ? preModels[0] : null;
  }

  /**
   * Set a rating for an item (1-5).
   */
  setRating(index, rating) {
    if (index < 0 || index >= this._ratings.length) return;
    if (rating < 1 || rating > 5) return;
    this._ratings[index] = rating;
    this.trigger('change:_ratings');
    this.trigger('change', this);
  }

  /**
   * Get ratings array.
   */
  getRatings() {
    return this._ratings;
  }

  /**
   * BS-4: can submit only when ALL items have ratings.
   */
  canSubmit() {
    return this._ratings.every(r => r !== null && r >= 1 && r <= 5);
  }

  /**
   * Store user answer for persistence.
   * _userAnswer holds the ratings array (integers 1-5).
   */
  storeUserAnswer() {
    this.set('_userAnswer', [...this._ratings]);
  }

  /**
   * Restore user answer on revisit.
   */
  restoreUserAnswers() {
    const saved = this.get('_userAnswer');
    if (!saved || !Array.isArray(saved)) return;

    this._ratings = [...saved];

    // If submitted, restore that state
    if (this.get('_isComplete')) {
      this.set('_isSubmitted', true);
      // For POST, recompute feedback fresh (CD-4)
      if (this._mode === 'post') {
        this._computeFeedback();
      }
    }
  }

  /**
   * Called on submit — store, record interactions, mark complete.
   */
  submit() {
    this.storeUserAnswer();
    this.set('_isSubmitted', true);

    // Record each rating to cmi.interactions
    if (this.get('_recordInteraction') !== false) {
      this._recordInteractions();
    }

    // For POST, compute feedback
    if (this._mode === 'post') {
      this._computeFeedback();
    }

    // Mark complete
    this.setCompletionStatus();
  }

  /**
   * FIX 2: Record each item rating to cmi.interactions via direct offlineStorage.set.
   * One interaction per item: id = conf-<groupId>-<mode>-<itemId>, type = numeric.
   *
   * KNOWN LIMITATION (pass 3c):
   * - 'likert' type is not supported by spoor wrapper switch; using 'numeric' instead.
   * - SCORM result: The wrapper (wrapper.js:637,648) coerces any falsy `correct` arg
   *   to 'wrong' (SCORM 1.2) or 'incorrect' (SCORM 2004). SCORM specs allow 'neutral',
   *   but the wrapper's ternary (`correct ? 'correct' : 'wrong'`) doesn't produce it.
   *   Self-report ratings are therefore recorded as 'incorrect'/'wrong' in cmi.interactions.
   *   This is a cosmetic issue for LMS reporting; the actual rating is in learner_response.
   *   Fixing this would require patching adapt-contrib-spoor, which is out of scope.
   */
  _recordInteractions() {
    const items = this.get('_items') || [];

    items.forEach((item, index) => {
      const rating = this._ratings[index];
      if (rating == null) return;

      const id = `conf-${this._groupId}-${this._mode}-${item._id}`;
      // offlineStorage.set('interaction', id, response, result, latency, type, correctResponsesPattern, objectiveIds, description)
      // result=null → wrapper coerces to 'wrong'/'incorrect' (see KNOWN LIMITATION above)
      offlineStorage.set('interaction', id, String(rating), null, null, 'numeric', null, null, item.text);
    });
  }

  /**
   * POST: compute feedback by comparing PRE and POST ratings.
   * Implements CD-3 (classifyItem) and CD-4 (selectSummary).
   * FIX 1: Appends forward hand-off (SA-7) to summary.
   * FIX 3: Fresh resolve of PRE at compute time, not reliant on init-time reference.
   */
  _computeFeedback() {
    const items = this.get('_items') || [];
    const postRatings = this._ratings;
    const feedback = this.get('_feedback') || {};
    const patterns = feedback._patterns || {};
    const summaryVariants = feedback._summary || {};
    const overrides = this.get('_itemFeedbackOverrides') || [];
    const hasSummativeFollowing = this.get('_hasSummativeFollowing') || false;

    // FIX 3: Fresh resolve of PRE at compute time. Build a BY-ID map (pre item
    // _id -> rating) so pre and post pair by identity, not by position. This is
    // what keeps the statistics extensible: a confidence item ADDED after an
    // earlier attempt has no pre rating for its _id, so it is accommodated (left
    // out of the before/after stats and chart) rather than mis-paired by index;
    // existing items match whatever their order; and when nothing is added every
    // item pairs exactly as before.
    const preModel = this._findPreModel();
    let preRatingById = null;

    if (preModel && preModel.get('_isSubmitted')) {
      const preUserAnswer = preModel.get('_userAnswer');
      const preItems = preModel.get('_items') || [];
      if (Array.isArray(preUserAnswer)) {
        preRatingById = {};
        preItems.forEach((preItem, i) => {
          if (preItem && preItem._id != null) preRatingById[preItem._id] = preUserAnswer[i];
        });
      }
    }

    // FIX 1: Resolve forward hand-off text (SA-7)
    const forward = feedback._forward || {};
    const forwardText = hasSummativeFollowing
      ? (forward._summative || '')
      : (forward._application || '');

    // SA-8: no PRE ratings — standalone mode
    // FIX 3: Only set standalone when fresh resolve confirms no PRE with ratings
    if (!preRatingById) {
      this._isStandalone = true;
      this._feedbackItems = items.map((item) => ({
        itemId: item._id,
        itemText: item.text,
        pattern: null,
        feedbackText: this._resolveFeedbackText(feedback._standalone || '', item.text)
      }));
      // FIX 1: Append forward to standalone summary
      const standaloneSummary = feedback._standalone || '';
      this._summaryText = [standaloneSummary, forwardText].filter(Boolean).join(' ');
      this.trigger('change:_feedback');
      return;
    }

    // Compute per-item patterns. Only include items the learner rated in BOTH
    // pre and post. If an earlier attempt stored a SHORTER pre (e.g. the course
    // later gained confidence items, so a 3-rating pre meets a 6-item post), the
    // extra indices have no pre rating - skipping them avoids NaN flowing into
    // the movement maths, the feedback list and the Before/After chart (which
    // otherwise renders broken/empty bars).
    this._isStandalone = false;
    const itemPatterns = [];
    this._feedbackItems = [];
    items.forEach((item, index) => {
      const pre = preRatingById[item._id]; // pair by identity, not position
      const post = postRatings[index];
      if (!Number.isFinite(pre) || !Number.isFinite(post)) return;
      const pattern = classifyItem(pre, post);
      itemPatterns.push(pattern);

      // Resolve feedback text: check overrides first, then patterns
      const override = overrides.find(o => o._itemId === item._id);
      let feedbackText = '';
      if (override && override[pattern]) {
        feedbackText = override[pattern];
      } else if (patterns[pattern]) {
        feedbackText = patterns[pattern];
      }

      this._feedbackItems.push({
        itemId: item._id,
        itemText: item.text,
        preRating: pre,
        postRating: post,
        pattern,
        // movement output (SA/CD): signed change + direction, for the view's
        // colour-coded badge. delta = post - pre; direction up/down/same.
        delta: post - pre,
        direction: post > pre ? 'up' : (post < pre ? 'down' : 'same'),
        feedbackText: this._resolveFeedbackText(feedbackText, item.text)
      });
    });

    // Compute summary
    const summaryKey = selectSummary(itemPatterns);
    const baseSummary = summaryVariants[summaryKey] || '';

    // FIX 1: Append forward hand-off to summary (SA-7)
    this._summaryText = [baseSummary, forwardText].filter(Boolean).join(' ');

    this.trigger('change:_feedback');
  }

  /**
   * Replace {{item}} placeholder with item text.
   */
  _resolveFeedbackText(template, itemText) {
    if (!template) return '';
    return template.replace(/\{\{item\}\}/g, itemText);
  }

  /**
   * Get computed feedback items for the view.
   */
  getFeedbackItems() {
    return this._feedbackItems || [];
  }

  /**
   * Get computed summary text.
   */
  getSummaryText() {
    return this._summaryText || '';
  }

  /**
   * Is this a standalone POST (no PRE ratings)?
   */
  isStandalone() {
    return this._isStandalone;
  }

  /**
   * Get mode (pre/post).
   */
  getMode() {
    return this._mode;
  }

  /**
   * For interaction recording — response type.
   */
  getResponseType() {
    return 'numeric';
  }

  /**
   * For interaction recording — response is the ratings array as string.
   */
  getResponse() {
    return this._ratings.join(',');
  }

  /**
   * No correct answer for self-efficacy ratings.
   */
  isCorrect() {
    return null;
  }

}
