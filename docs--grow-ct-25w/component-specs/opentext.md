# adapt-abbott-opentext — Component Specification

**Status:** DRAFT v0.4 — 31 July 2026 (Stage 4: completion)
**Supersedes:** `adapt-abbott-reflective-store` (extension) and the reflective-answer portion of `patches/adapt-contrib-textInput+reflective-answer-restore.patch`
**Related decisions:** RTR-1 (open-decisions.md), RTR-1e (measured suspend_data ceiling), CB-1 (commit behaviour), BS-2 (storage & recording contract — amended)

---

## 1. Purpose and scope

A general-purpose open-text component for learner-authored writing that has no correct answer.

Reflective prompts are the first use case, but the component is deliberately general: the programme's thirteen pathways will want free-text elsewhere, and none of it is question-shaped.

**What it is:** a notebook page held in the course. The learner writes; the writing persists; it displays back when they return.

**What it is not:** a question. It does not mark, score, contribute to assessment, or report a result.

### 1.1 Why not adapt-contrib-textInput

The six existing reflective prompts use `adapt-contrib-textInput`, a question component, with five workarounds layered on:

| Workaround | Reason |
|---|---|
| `_isOptional: true` | stop it blocking completion |
| no `_answers` | nothing to mark against |
| Phase 1 vendor patch | make it retain typed text (`_userAnswerText`) |
| `adapt-abbott-reflective-store` | make it persist across sessions |
| (proposed) further extension | make it multi-line and readable |

The mismatch is visible in the tracking record: every reflection is written to `cmi.interactions` with `result: incorrect`, because the component can only think in right and wrong. It is also truncated to 250 characters there (SCORM 2004 SPM for `localized_string_type` — see RTR-1).

This component stops fighting that.

---

## 2. Model / view split

**`OpenTextModel extends ComponentModel`** — *not* `QuestionModel`.

This is the load-bearing decision. Extending `QuestionModel` would pull the component into the scoring machinery: submit semantics, marking, `_isCorrect`, attempt counting, assessment participation. None of it applies.

**Why `ComponentModel`, not `ItemsComponentModel`:** The spec originally specified `ItemsComponentModel` by analogy to `adapt-abbott-confidence`, but the analogy doesn't hold. Confidence genuinely has multiple items (the rating statements); opentext holds one string. `ItemsComponentModel` creates a Backbone Collection of child `ItemModel`s and tracks `_isVisited` per item — machinery this component doesn't need. The `text` component is the closer precedent: it extends `ComponentModel` directly and stays outside the scoring machinery. What matters is avoiding `QuestionModel`; the choice between `ComponentModel` and `ItemsComponentModel` is about items, not scoring.

**Model property for stored text: `_text`** — not `_userAnswer`. The `_userAnswer` name is `QuestionModel` vocabulary and invites exactly the confusion this component exists to remove. The model stores text in `_text`; the offlineStorage shape uses `t` for the same value (see §6).

**Model owns:** text value (`_text`), character count, persistence read/write, variant resolution, completion state and rule, limit evaluation. No DOM.

**View owns:** textarea render, auto-grow, input capture, counter render and visibility, status-line state, live-region announcements, completion affordance. No storage, no completion rule.

---

## 3. Variants

`_variant` distinguishes purposes that share a mechanism but differ in framing. It sets **defaults**, it does not lock behaviour — except where noted.

**Naming note:** `_variant`, not `_type`. Adapt already uses `_type` in its content model (`page`, `article`, `block`, `component`); reusing it on component settings invites collision. Verify at build time that `_variant` is unused elsewhere.

| | `reflection` (default) | `notes` |
|---|---|---|
| Placeholder | `Write your reflection here…` | `Make your notes here…` |
| `_maxCharacters` | 4000 | 4000 |
| `_isCompletionBearing` | `false` (author may enable) | **not available** — see below |
| CSS class | `is-variant-reflection` | `is-variant-notes` |
| Stored tag | `"v":"reflection"` | `"v":"notes"` |

**Notes are never completion-bearing — enforced, not defaulted.** The model ignores `_isCompletionBearing` when `_variant` is `notes`. If a notes component needs to count toward completion, it is a reflection wearing the wrong hat, and the variant exists to make that distinction visible.

**Schema limitation:** Conditional field visibility (hiding `_isCompletionBearing` when `_variant` is `notes`) is not supported in this framework's schema format (JSON Schema draft-04 with Adapt extensions; `if/then/else` requires draft-07+). The field is therefore exposed for all variants, with help text stating it has no effect for notes. Enforcement is model-side only.

**Default variant is `reflection`.** Safe, because reflection is itself non-completion-bearing by default: an unspecified component cannot accidentally count.

---

## 4. Author-facing schema

| Property | Type | Default | Purpose |
|---|---|---|---|
| `body` | string | — | The prompt itself |
| `instruction` | string | — | Optional guidance above the field |
| `_variant` | string | `reflection` | `reflection` \| `notes` — see §3 |
| `placeholder` | string | per variant | Empty-state text |
| `_maxCharacters` | number | `4000` | Soft limit — see §8 |
| `_minCharacters` | number | `0` | Minimum for completion when completion-bearing |
| `_isCompletionBearing` | boolean | `false` | Reflection variant only. Has no effect when `_variant` is `notes`. |
| `_rows` | number | `8` | Initial textarea height |
| `_maxRows` | number | `20` | Auto-grow ceiling before scrolling |

`_maxCharacters` is configurable but should not be raised without re-checking the suspend_data budget (§8.1).

---

## 5. States and lifecycle

The component has **no locked or read-only state**. It is freely editable at all times, including after completion.

| State | Trigger | Appearance |
|---|---|---|
| Empty | Initial render, no stored text | Placeholder visible, counter hidden, status line normal |
| Writing | Text present, under threshold | Counter hidden, status line normal |
| Approaching limit | Within 750 chars of `_maxCharacters` | Counter appears |
| Over limit | Above `_maxCharacters` | Counter visible, over-limit message shown, completion blocked |
| Save failed | Write returned an error | Status line shows failure message (§9.3) |
| Complete | "Mark as complete" pressed | Button replaced by static "Completed" confirmation |

**On return:** the learner sees their writing in an editable textarea, correctly sized (§9.4). There is no separate read-back view. This is deliberate — it is a notebook, not a submission.

**Completion is sticky.** Once earned it is not lost by subsequent editing or deletion. Engaged is engaged. This is enforced by overriding `reset()` in the model: even if `_isResetOnRevisit: true` triggers a hard reset on page revisit, `_isComplete` is preserved. The override deliberately protects only `_isComplete` because `_text` is unaffected — `AdaptModel.reset()` sets only `_isEnabled`, `_isInteractionComplete`, and `_isComplete`; it does not clear arbitrary model attributes.

---

## 6. Persistence

**Mechanism:** Adapt's `offlineStorage` custom-key API, writing into `cmi.suspend_data`.

**Key:** `ot:<componentId>` — one key per component. Individual keys have a smaller blast radius than a combined key on a failed write, and are easier to identify in track-details extraction.

**Stored shape:**

```json
{"v":"reflection","t":"the learner's writing…"}
```

The variant tag travels with the text so extraction can distinguish reflections from notes without cross-referencing the course JSON.

**Restore must parse defensively.** Accept the object shape; accept a bare string as legacy/fallback (treating it as `reflection`); never throw on unexpected input. A shape assumption that turns out wrong loses learner writing.

**Write triggers:**
- On blur
- On debounced typing: **2000ms idle, 15000ms maxWait**

The maxWait matters. Pure debounce means a learner typing continuously never saves, because the idle gap never arrives. With maxWait they save at least every fifteen seconds regardless. Lodash supports this directly (`_.debounce(fn, 2000, { maxWait: 15000 })`) and spoor already bundles it.

Blur is the real safety net; the debounce covers the laptop-dies-with-tab-open case.

**Commit behaviour:** with `_commitOnAnyChange: true` in force (CB-1), each `offlineStorage.set()` commits to the LMS within ~100ms of the debounce settling. No submit gesture is required for persistence.

**Write verification:** fail-closed, following the pattern established in `adapt-abbott-reflective-store` — check the SCORM error code after each write, treat an unreadable code as failure, never assume success. Surface failures (§9.3).

**No `cmi.interactions` writes.** This removes the 250-character truncation and the false `result: incorrect` in one move.

### 6.1 Extraction implications (BS-2)

If open-text content ever needs extracting for cohort analysis, it comes from `cmi.suspend_data` in Moodle's track-details view, where it sits in full and in plain text — verified 31 July 2026. BS-2's interactions-based extraction path does not apply to this component.

---

## 7. Completion

**Default: not completion-bearing.** The component renders with no button and contributes nothing to lesson or course completion. Notes cannot be made completion-bearing at all (§3).

**When `_isCompletionBearing: true` (reflection only):**

- A "Mark as complete" button appears below the field
- The button **marks only** — it does not save, because saving is automatic. This distinction must be visible in the label and must not be blurred back into "Submit"
- Pressing it sets completion and replaces the button with a static "Completed" confirmation
- Completion requires text of at least `_minCharacters` and not over `_maxCharacters`
- Completion is sticky (§5)

**Rationale for the explicit action:** where completion counts for something, the learner should signal it deliberately rather than have it inferred from keystrokes. Where it doesn't count, no gesture should be demanded at all.

### 7.1 Edge cases

| Case | Behaviour |
|---|---|
| Press when below `_minCharacters` | Nothing completes. The button stays live (never disabled — disabled controls are skipped by screen readers). Announce the below-minimum message via the polite live region. The required count is not displayed in advance; the message arrives when the learner asks for it. |
| Press when over `_maxCharacters` | Nothing completes. The over-limit message is already displayed by the counter logic. Announce it via the live region if not already announced (threshold tracking prevents duplicates). |
| Notes variant with `_isCompletionBearing: true` | Ignored — no button, no completion. Log a console warning naming the component, matching the variant validation pattern. An author who sets a flag and gets no effect needs to know why. |
| Complete, then edit to over limit | Stays complete. The over-limit warning still shows. Completion and the character limit are separate concerns — the writing is still at risk of LMS rejection regardless of completion state. |

### 7.2 Accessibility

The completion button must never be `disabled`. Disabled controls are frequently skipped by screen readers and communicate nothing about *why* the learner cannot proceed. The button stays pressable at all times; pressing it when conditions aren't met announces the reason via the polite live region.

---

## 8. Character limit

**Soft limit. No `maxlength`. No truncation. Ever.**

Truncation is what the interactions route did, and it is why RTR-1 took two days. A learner must never lose text they can see on screen.

| Condition | Effect |
|---|---|
| Under `_maxCharacters − 750` | Counter hidden |
| Within 750 of limit | Counter visible: `3,250 of 4,000 characters` |
| Over limit | Counter visible, over-limit message, completion blocked |

The learner may continue typing past the limit. They simply cannot mark the component complete until they trim, and are told by how much.

### 8.1 Why 4,000

Derived in RTR-1e from a *measured* ceiling, not a spec figure:

- 51,892 characters of `cmi.suspend_data` accepted by Cardiff Met Moodle
- minus ~4,000 reserved for spoor's own `c`/`q` state at full course completion
- minus ~15% for JSON escaping of real prose (quotes, apostrophes, newlines)
- ≈ 40,000 usable, across six prompts ≈ 6,600 each; across twelve ≈ 3,300 each

4,000 (~700 words) holds in both cases with margin, and sits well above the ~300-word pedagogical target.

**Exceeding the LMS ceiling is catastrophic, not degraded:** error 406 discards the *entire* suspend_data write, including course location and component state, and shows the learner a browser dialog naming "technical support". Hence client-side enforcement.

---

## 9. Accessibility

### 9.1 Structure

- The textarea has a programmatic label via `aria-labelledby`, referencing a rendered element by ID
- **Label fallback chain** (when body is empty): instruction → displayTitle → ariaRegion. The fallback element is rendered visually-hidden with an ID; `aria-labelledby` always points at a real element, never uses `aria-label` (which would expose raw HTML markup)
- The status line is associated via `aria-describedby` so it is available on focus
- The counter element is `aria-hidden="true"` — it must not be announced on every keystroke. It is deliberately excluded from `aria-describedby`; learners approaching the limit are informed via threshold announcements instead

### 9.2 Announcements

A `aria-live="polite"` region carries routine announcements, at **thresholds only**:

| Event | Announcement |
|---|---|
| Counter first appears (750 remaining) | `750 characters remaining.` |
| Limit crossed | The over-limit message (§10) |
| Completion blocked (below minimum) | The below-minimum message (§10) |

Completion success is **not** announced via the live region — see §9.5 (focus management).

Debounce as needed to prevent duplicate or rapid-fire announcements.

### 9.3 Write failure

**The status line doubles as the failure indicator** — it is already where the learner looks for reassurance, so it becomes the status line rather than adding a second element:

- Normal: `Your writing saves automatically.`
- Failed: `Your writing could not be saved. Please copy it somewhere safe before you leave this page.`

Self-healing: the next successful autosave clears it, and a retry happens naturally on the next debounce. No retry button required.

**Urgency:** failure uses `role="alert"` (assertive), unlike everything else in the component. Interrupting mid-sentence is justified when the learner's writing is at risk. Everything else stays polite.

**Not a modal.** Moodle's 406 dialog is a modal and it is exactly the experience to avoid.

This supersedes the existing backlog item on write-failure warnings.

### 9.4 Sizing

Auto-grow from `_rows` to `_maxRows`, then scroll.

Technique: on input, set `height: auto` then `height: scrollHeight + 'px'`, with `max-height` in CSS and `overflow-y: auto` taking over at the ceiling. (`field-sizing: content` is the clean modern answer but browser support is too recent to rely on institutionally.)

**Auto-grow must also run on restore, not just on input.** Otherwise a learner returning to a 2,000-character reflection gets an 8-row box with their text scrolling inside it — precisely the bug being fixed.

Fallback if it misbehaves: fixed height at `_maxRows`, reported rather than substituted silently.

### 9.5 Focus management

When the completion button is pressed and conditions are met:

1. The button is hidden (`display: none`)
2. The "Completed" static element is shown
3. **Focus moves to the completed-state element** (which has `tabindex="-1"`)

This prevents focus from falling to `<body>` when the button disappears. Moving focus also announces the element's text ("Completed"), so no separate live-region announcement is needed — a single announcement conveys the state change without collision or duplication.

The completed-state element is non-interactive (`tabindex="-1"` allows programmatic focus but keeps it out of the normal tab order).

---

## 10. Learner-facing strings

Formative register throughout. Contractions permitted (Open Decision #15). Author-overridable where reasonable; these are defaults. All strings live in schema globals and are translatable.

| Element | Schema key | Default |
|---|---|---|
| Placeholder (reflection) | — (model default) | `Write your reflection here…` |
| Placeholder (notes) | — (model default) | `Make your notes here…` |
| Status line — normal | `statusNormal` | `Your writing saves automatically.` |
| Status line — failed | `statusFailed` | `Your writing could not be saved. Please copy it somewhere safe before you leave this page.` |
| Counter | `counterText` | `{{count}} of {{max}} characters` |
| Approaching limit announcement | `remainingAnnouncement` | `{{remaining}} characters remaining.` |
| Over limit | `overLimitText` | `You're {{over}} characters over the limit — please shorten your writing before continuing.` |
| Completion button | `completionButton` | `Mark as complete` |
| Completed state | `completedState` | `Completed` (also serves as completion announcement via focus — see §9.5) |
| Below minimum message | `belowMinimumMessage` | `Please write a little more before marking this complete.` |

**Note on the status line:** it does the job of the learner-instructions backlog item at the point of need, rather than in wrapper text a learner will have forgotten by L05.

---

## 11. Retirement and migration

Once this component is built and verified in Moodle:

**Retire:**
- `adapt-abbott-reflective-store` (extension) — its whole purpose was making textInput persist
- The reflective-answer portion of `patches/adapt-contrib-textInput+reflective-answer-restore.patch` — check whether the patch does anything else before removing it wholesale

**Migrate:**
- Six existing reflective prompts in L02–L07, from `_component: "textinput"` to `_component: "opentext"`, `_variant: "reflection"`
- Existing content stored under `rtr:<componentId>` keys becomes orphaned. Accepted — pilot data only, no loss of record

**Do not retire anything until the new component is verified in Moodle**, following the same discipline as RTR-1: write, persist, restore, across a genuine cross-session resume on a clean attempt.

---

## 12. Resolved build questions

| Question | Resolution |
|---|---|
| Autosave debounce | 2000ms idle, 15000ms maxWait |
| Auto-grow | JS `scrollHeight` technique; must run on restore; fixed-height fallback reported not silent |
| Write-failure treatment | Status line doubles as indicator; assertive announcement; self-healing; no modal |
| Variant flag | `_variant`, implemented now: `reflection` (default) and `notes` |
