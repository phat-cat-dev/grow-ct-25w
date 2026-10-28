/*
 * adapt-gow-textTagging - Model
 *
 * Ported from:
 *   - behaviour: wkspc2610-pw02/src/shared/js/activities/text-tagging.js
 *   - data model: wkspc2611-congen11/schemas/activities/text-tagging.schema.json
 *
 * Bugs fixed, not ported (see README.md "Deviations from source" for full detail):
 *   1. Category id vocabulary normalised to a single `_id` used everywhere (source
 *      had underscore ids in content data vs hyphen ids in the palette, which broke
 *      scoring for half the categories in the shipped pw02 build).
 *   2. Span text location uses an ordered, non-overlapping, cursor-based scan
 *      instead of source's unescaped `String.replace` (first-occurrence-only,
 *      order-dependent, broke on substring overlaps).
 *   3. `_userAnswer` is a compact array of category indices (one per span, in
 *      document order, -1 = untagged) rather than a DOM-attribute/object map -
 *      relevant given the source project's documented 48KB SCORM
 *      cmi.suspend_data ceiling.
 */
import QuestionModel from 'core/js/models/questionModel';

export default class TextTaggingModel extends QuestionModel {

  init() {
    super.init();
    this._buildSegments();
    this._buildAllSpans();
    this.setupRandomisation();
  }

  // QuestionModel calls this during init() in the standard Adapt question
  // lifecycle; text-tagging doesn't randomise, so this is a deliberate no-op.
  setupRandomisation() {}

  /**
   * For every passage, resolve `text` + `_taggableSpans` into an ordered
   * segment array: [{ text, _isSpan, _spanId, _tagId, feedback }, ...].
   * A passage with no `_taggableSpans` becomes a single non-span segment
   * (the read-only "contrast passage" pattern from the source schema).
   */
  _buildSegments() {
    const passages = this.get('_passages') || [];

    passages.forEach(passage => {
      passage._segments = this._resolvePassageSegments(passage.text, passage._taggableSpans);
    });

    this.set('_passages', passages);
  }

  _resolvePassageSegments(text, taggableSpans) {
    if (!taggableSpans || !taggableSpans.length) {
      return [{ text, _isSpan: false }];
    }

    // Locate every span's position first, then sort by document order, then
    // scan with a cursor so overlapping/duplicate matches are detected and
    // skipped (with a warning) rather than silently mis-tagged as the
    // source's first-occurrence String.replace did.
    const matches = [];

    taggableSpans.forEach((span, spanIndex) => {
      const start = text.indexOf(span.text);

      if (start === -1) {
        console.warn(`[adapt-gow-textTagging] span text not found in passage, skipped: "${span.text}"`);
        return;
      }

      matches.push({ start, end: start + span.text.length, span, spanIndex });
    });

    matches.sort((a, b) => a.start - b.start);

    const segments = [];
    let cursor = 0;

    matches.forEach(match => {
      if (match.start < cursor) {
        console.warn(`[adapt-gow-textTagging] overlapping span ignored: "${match.span.text}"`);
        return;
      }

      if (match.start > cursor) {
        segments.push({ text: text.slice(cursor, match.start), _isSpan: false });
      }

      segments.push({
        text: text.slice(match.start, match.end),
        _isSpan: true,
        _spanId: `span-${match.spanIndex}`,
        _tagId: match.span._tagId,
        feedback: match.span.feedback || '',
        feedbackIncorrect: match.span.feedbackIncorrect || ''
      });

      cursor = match.end;
    });

    if (cursor < text.length) {
      segments.push({ text: text.slice(cursor), _isSpan: false });
    }

    return segments;
  }

  /**
   * Flatten every taggable span, across every passage, into a single ordered
   * list - this is the scoring unit. Initialises `_userAnswer` (one entry per
   * span, aligned by index) to all-untagged (-1) if not already present
   * (e.g. on first render vs. a revisit with a stored _userAnswer).
   */
  _buildAllSpans() {
    const allSpans = [];

    (this.get('_passages') || []).forEach(passage => {
      (passage._segments || []).forEach(segment => {
        if (segment._isSpan) {
          allSpans.push({
            _spanId: segment._spanId,
            _tagId: segment._tagId,
            text: segment.text,
            feedback: segment.feedback,
            feedbackIncorrect: segment.feedbackIncorrect
          });
        }
      });
    });

    this.set('_allSpans', allSpans);

    if (!Array.isArray(this.get('_userAnswer')) || this.get('_userAnswer').length !== allSpans.length) {
      this.set('_userAnswer', allSpans.map(() => -1));
    }
  }

  /**
   * Record the learner's choice for one span.
   * @param {string} spanId
   * @param {number} categoryIndex index into _tagCategories, or -1 to clear
   */
  setSpanTag(spanId, categoryIndex) {
    const allSpans = this.get('_allSpans') || [];
    const index = allSpans.findIndex(span => span._spanId === spanId);

    if (index === -1) return;

    const userAnswer = (this.get('_userAnswer') || []).slice();
    userAnswer[index] = categoryIndex;
    this.set('_userAnswer', userAnswer);
    // Re-evaluate whether Submit should enable now the answer has changed -
    // without this the submit button never leaves its initial disabled state.
    this.checkCanSubmit();
  }

  getSpanTag(spanId) {
    const allSpans = this.get('_allSpans') || [];
    const index = allSpans.findIndex(span => span._spanId === spanId);

    if (index === -1) return -1;

    return (this.get('_userAnswer') || [])[index];
  }

  // --- Standard QuestionModel API ---

  /**
   * Mirrors pw02's check(): every scorable span (one with a _tagId) must have
   * an applied tag matching that _tagId to be correct. Untagged scorable
   * spans count as incorrect. _isCorrect requires 100%; partial credit is
   * exposed via _isPartlyCorrect (any correct, but not all) and the numeric
   * score set in setScore().
   */
  isCorrect() {
    const allSpans = this.get('_allSpans') || [];
    const userAnswer = this.get('_userAnswer') || [];
    const categories = this.get('_tagCategories') || [];

    let correctCount = 0;

    allSpans.forEach((span, i) => {
      const chosenCategory = categories[userAnswer[i]];
      if (chosenCategory && chosenCategory._id === span._tagId) {
        correctCount++;
      }
    });

    const total = allSpans.length;

    this.set('_numberOfCorrectAnswers', correctCount);
    this.set('_numberOfSpans', total);
    this.set('_isPartlyCorrect', correctCount > 0 && correctCount < total);

    return total > 0 && correctCount === total;
  }

  setScore() {
    this.set('_score', this.get('_numberOfCorrectAnswers') || 0);
    this.set('_maxScore', this.get('_numberOfSpans') || 0);
  }

  /**
   * multi (default): every scorable span must be tagged before submitting -
   * matches pw02's implicit "Check tags" availability (the button was always
   * enabled, but this enforces the single/multi distinction congen11's schema
   * declares and pw02's JS never consumed).
   * single: at least one tag applied.
   */
  canSubmit() {
    const userAnswer = this.get('_userAnswer') || [];
    if (!userAnswer.length) return false;

    const tagMode = this.get('_tagMode') || 'multi';
    return tagMode === 'single'
      ? userAnswer.some(value => value !== -1)
      : userAnswer.every(value => value !== -1);
  }

  storeUserAnswer() {
    // _userAnswer is already maintained incrementally by setSpanTag() as the
    // learner interacts, so there is nothing further to persist here.
  }

  resetUserAnswer() {
    const allSpans = this.get('_allSpans') || [];
    this.set('_userAnswer', allSpans.map(() => -1));
  }

  getResponseType() {
    return 'extended';
  }

  /** SCORM cmi.interactions response string, e.g. "span-0:claim, span-1:hedging". */
  getResponse() {
    const allSpans = this.get('_allSpans') || [];
    const userAnswer = this.get('_userAnswer') || [];
    const categories = this.get('_tagCategories') || [];

    return allSpans
      .map((span, i) => {
        const category = categories[userAnswer[i]];
        return `${span._spanId}:${category ? category._id : 'untagged'}`;
      })
      .join(', ');
  }

  getInteractionObject() {
    const categories = this.get('_tagCategories') || [];

    return {
      type: 'matching',
      source: (this.get('_allSpans') || []).map(span => ({ id: span._spanId })),
      target: categories.map(category => ({ id: category._id, description: category.label }))
    };
  }

}
