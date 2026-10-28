# adapt-abbott-pass-reveal

Extension specification for the pass-reveal mechanism.

**Grounded in:** `courses/academic-writing-introductory` (SUMM-a-01 assessment, Academic Writing: Introductory Stage).

---

## 1. Purpose

Prevents learners from revealing correct answers (via the "Show correct answer" button) before demonstrating competence. Model answers remain hidden until the learner passes the assessment; on pass, `_canShowModelAnswer` is set to `true` on all question components in the targeted assessment(s).

**Pedagogical rationale:** Learners should attempt to answer from their own understanding first. Revealing model answers before passing enables answer-grinding without genuine learning. After passing, model-answer review supports reflection and consolidation.

---

## 2. Configuration

Add to `course.json`:

```json
"_passReveal": {
  "_isEnabled": true,
  "_assessmentIds": ["SUMM-a-01"]
}
```

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `_isEnabled` | boolean | Yes | `false` | Master switch. When `false` or absent, the extension does nothing (inert). |
| `_assessmentIds` | string[] | No | `[]` | Assessment IDs to apply pass-reveal to. If empty or absent, applies to ALL assessments in the course. |

---

## 3. Guard Chain (execution order)

The extension enforces a strict guard chain. All guards must pass for model answers to be enabled:

1. **Extension enabled** (MUST be first) — `_passReveal._isEnabled === true`. If disabled or absent, the extension is completely inert.
2. **Assessment ID match** — The completing assessment's ID is in `_assessmentIds`, OR `_assessmentIds` is empty/absent (meaning "all assessments").
3. **isPass true** — The assessment completion event's `isPass` property is `true`.

Only when all three guards pass does the extension set `_canShowModelAnswer: true` on the assessment's question components.

---

## 4. Events Handled

| Event | When fired | Action |
|-------|------------|--------|
| `assessments:complete` | Learner completes an assessment attempt (pass or fail) | Runs guard chain; enables model answers if all guards pass |
| `assessment:restored` | Assessment state restored from SCORM on revisit | Same as above (preserves pass-reveal state across sessions) |

---

## 5. Behaviour Notes

- **Pre-pass:** No "Show correct answer" button appears on assessment questions (standard Adapt behaviour when `_canShowModelAnswer: false`).
- **Post-pass:** "Show correct answer" button becomes available on all questions in the assessment.
- **Idempotent:** If `_canShowModelAnswer` is already `true`, the extension does not re-set it.
- **Per-assessment:** Each assessment is evaluated independently. Passing one assessment does not reveal model answers on a different assessment.

---

## 6. Interaction with Other Settings

| Setting | Interaction |
|---------|-------------|
| `_canShowFeedback` | Independent. Feedback can be shown regardless of pass-reveal state. |
| `_canShowMarking` | Independent. Marking (correct/incorrect indicators) can be shown regardless of pass-reveal state. |
| `_suppressMarking` | Independent. Marking suppression is an assessment-level setting unrelated to model-answer visibility. |
| `_attempts` | Independent. Pass-reveal does not affect attempt limits. |

---

## 7. Authoring Checklist

- [ ] Add `_passReveal` block to `course.json`
- [ ] Set `_isEnabled: true`
- [ ] Specify `_assessmentIds` if targeting specific assessments (omit or leave empty for all)
- [ ] Ensure assessment questions have `_canShowModelAnswer` set to `false` initially (or rely on default)
- [ ] Verify via browser: "Show correct answer" button hidden before pass, visible after pass

---

## 8. Technical Details

**Source:** `src/extensions/adapt-abbott-pass-reveal/js/adapt-abbott-pass-reveal.js`

**Schema:** `src/extensions/adapt-abbott-pass-reveal/schema/course.schema.json`

**Unit tests:** `src/extensions/adapt-abbott-pass-reveal/test/unit/pass-reveal.js` (12 tests covering all guards and behaviours)

**Dependencies:** None beyond Adapt core (`core/js/adapt`, `core/js/logging`).

---

## 9. Known Limitations

- **Non-native confirmation:** Adapt's built-in assessment extension does not fire a distinct "assessment passed" event. This extension listens to the generic `assessments:complete` event and inspects `state.isPass`. This is the standard Adapt pattern, not a custom workaround.
- **No per-question control:** Pass-reveal applies to ALL questions in a targeted assessment. There is no mechanism to reveal model answers on only some questions.

---

## 10. History

| Date | Change |
|------|--------|
| 2026-08-14 | Initial build for Academic Writing: Introductory Stage SUMM-a-01 |
