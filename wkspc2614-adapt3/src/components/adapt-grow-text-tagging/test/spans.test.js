/*
 * Standalone verification for TextTaggingModel's span-resolution algorithm.
 *
 * `_resolvePassageSegments()` has no Adapt/Backbone dependency (plain string
 * ops + console.warn), but TextTaggingModel.js itself does
 * (`import QuestionModel from 'core/js/models/questionModel'`), which isn't
 * resolvable outside a running Adapt course. No Adapt framework is installed
 * in this environment, so this test re-declares that one method verbatim
 * (byte-for-byte identical body to js/TextTaggingModel.js) and exercises it
 * directly with plain Node - rather than stubbing out Adapt's module system,
 * which would test the stub, not the logic.
 *
 * IMPORTANT: if you change `_resolvePassageSegments()` in TextTaggingModel.js,
 * update the copy below to match, or this test silently stops verifying the
 * real implementation.
 *
 * Fixture: the real "Sleep and academic performance" passage from pw02's
 * built course (dist/academic-writing-beginner/01-understanding-academic-writing.html,
 * context-slot B1-CS1, passage_b) - 4 tagged phrases from the source fixture
 * (claim, signal-phrase, 2x hedging) plus one of the three `formal_vocabulary`
 * options (5 real spans total), plus one deliberately engineered overlapping
 * span (not from the source fixture) to exercise the overlap-rejection path.
 *
 * Run: node test/spans.test.js
 */

function resolvePassageSegments(text, taggableSpans) {
  if (!taggableSpans || !taggableSpans.length) {
    return [{ text, _isSpan: false }];
  }

  const matches = [];

  taggableSpans.forEach((span, spanIndex) => {
    const start = text.indexOf(span.text);

    if (start === -1) {
      console.warn(`[adapt-grow-text-tagging] span text not found in passage, skipped: "${span.text}"`);
      return;
    }

    matches.push({ start, end: start + span.text.length, span, spanIndex });
  });

  matches.sort((a, b) => a.start - b.start);

  const segments = [];
  let cursor = 0;

  matches.forEach(match => {
    if (match.start < cursor) {
      console.warn(`[adapt-grow-text-tagging] overlapping span ignored: "${match.span.text}"`);
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
      feedback: match.span.feedback || ''
    });

    cursor = match.end;
  });

  if (cursor < text.length) {
    segments.push({ text: text.slice(cursor), _isSpan: false });
  }

  return segments;
}

// --- Fixture ---------------------------------------------------------------

const passageText = 'Sleep has been identified as a significant factor in academic performance among university students. Research indicates that insufficient sleep may impair cognitive functions including memory consolidation and attention, with potentially lasting consequences for academic achievement. Studies by Walker (2017) suggest that students sleeping fewer than six hours per night are significantly more likely to achieve lower grades than their better-rested peers. While individual variation in sleep needs makes it difficult to establish universal recommendations, the available evidence consistently supports a relationship between sleep duration and academic outcomes.';

const taggableSpans = [
  // 0: claim
  { text: 'Sleep has been identified as a significant factor in academic performance among university students.', _tagId: 'claim' },
  // 1: signal-phrase
  { text: 'Studies by Walker (2017) suggest that', _tagId: 'signal-phrase' },
  // 2: hedging (primary)
  { text: 'may impair', _tagId: 'hedging' },
  // 3: hedging (alt) - tests many-spans-to-one-category
  { text: 'potentially lasting', _tagId: 'hedging' },
  // 4: formal-vocabulary (one of three source options)
  { text: 'memory consolidation', _tagId: 'formal-vocabulary' },
  // 5: engineered overlap case (NOT from the source fixture) - this phrase's
  // range fully contains span 2's "may impair", starting earlier in the
  // text, so it should be accepted and span 2 should be rejected as
  // overlapping once matches are sorted by start index.
  { text: 'insufficient sleep may impair', _tagId: 'formal-vocabulary' },
  // 6: not present in the passage at all - tests the not-found warn/skip path
  { text: 'this phrase does not appear anywhere in the passage', _tagId: 'claim' }
];

// --- Assertions --------------------------------------------------------------

let failures = 0;

function assert(condition, message) {
  if (!condition) {
    failures++;
    console.error(`FAIL: ${message}`);
  } else {
    console.log(`PASS: ${message}`);
  }
}

const segments = resolvePassageSegments(passageText, taggableSpans);

const spanSegments = segments.filter(s => s._isSpan);
const plainSegments = segments.filter(s => !s._isSpan);

// Exactly 5 of the 7 declared spans should resolve: span 2 (may impair) is
// rejected as overlapping with span 5, span 6 is rejected as not-found.
assert(spanSegments.length === 5, `expected 5 resolved span segments, got ${spanSegments.length}`);

// Rejected spans must not appear at all.
assert(
  !spanSegments.some(s => s._tagId === 'hedging' && s.text === 'may impair'),
  'overlapping span ("may impair") correctly excluded'
);
assert(
  !spanSegments.some(s => s.text === 'this phrase does not appear anywhere in the passage'),
  'not-found span correctly excluded'
);

// The overlap-winner should be present with the correct, wider boundary.
const overlapWinner = spanSegments.find(s => s.text === 'insufficient sleep may impair');
assert(!!overlapWinner, 'overlap-winning span ("insufficient sleep may impair") is present');
assert(overlapWinner && overlapWinner._tagId === 'formal-vocabulary', 'overlap-winning span has correct _tagId');

// Both hedging spans (primary + alt) resolve as distinct, correctly-ordered
// segments - the many-spans-to-one-category case from the real fixture.
const hedgingSpans = spanSegments.filter(s => s._tagId === 'hedging');
assert(hedgingSpans.length === 1, `expected exactly 1 surviving hedging span (the other was engineered to overlap), got ${hedgingSpans.length}`);
assert(hedgingSpans[0] && hedgingSpans[0].text === 'potentially lasting', 'surviving hedging span is "potentially lasting"');

// Segments must be in strict document order (non-decreasing start position),
// reconstructed by checking the concatenation equals the original text.
const reconstructed = segments.map(s => s.text).join('');
assert(reconstructed === passageText, 'concatenated segments exactly reconstruct the original passage text (no gaps/overlaps/dupes)');

// Span ids are assigned by original declaration index, not resolution order.
const claimSegment = spanSegments.find(s => s._tagId === 'claim');
assert(!!claimSegment && claimSegment._spanId === 'span-0', 'claim span keeps its declared index as _spanId ("span-0")');

const signalPhraseSegment = spanSegments.find(s => s._tagId === 'signal-phrase');
assert(!!signalPhraseSegment && signalPhraseSegment._spanId === 'span-1', 'signal-phrase span keeps its declared index as _spanId ("span-1")');

// Non-span segments (plain passage text between tags) should also be present.
assert(plainSegments.length > 0, 'at least one non-span (plain text) segment resolved between tagged spans');

// A passage with no taggableSpans is a single non-span segment (contrast
// passage pattern).
const contrastSegments = resolvePassageSegments('A read-only contrast passage.', []);
assert(
  contrastSegments.length === 1 && contrastSegments[0]._isSpan === false,
  'a passage with no taggableSpans resolves to a single non-span segment'
);

console.log(`\n${failures === 0 ? 'All assertions passed.' : `${failures} assertion(s) failed.`}`);
process.exit(failures === 0 ? 0 : 1);
