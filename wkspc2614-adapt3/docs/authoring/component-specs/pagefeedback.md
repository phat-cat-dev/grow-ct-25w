# pagefeedback (adapt-abbott-pagefeedback) — Authoring Spec

**Version:** 0.1
**Status:** draft — ships with the component (built 5 November 2026). No authored lesson instance yet; the worked example below is **illustrative**.
**Verified against:** `src/components/adapt-abbott-pagefeedback/properties.schema` — **our own schema** (custom component; no `example.json`).
**Relationship to other documents:** this component has no `open-decisions.md` entry yet — it was built directly from a staged third-party demo (`incoming-components/page-feedback/`, status `idea` in the candidates register) rather than from a prior design discussion. This spec is the first record of its rationale.

---

## 1. Purpose & when to reach for it

An **end-of-page self-report**: did this page help, yes or no, plus an optional free-text note. It is **not graded** and has no correct answer — a quick temperature-check, not an assessment (mirrors `adapt-abbott-confidence`'s AR-1 stance, but flat and single-shot rather than pre/post and item-based).

Reach for it at the close of a page where a lightweight "was this useful" signal is worth capturing without the overhead of a full reflective prompt. Do not use it where the learner's response needs to feed forward into subsequent content (it has no branching/feedback logic) — for that, reach for `adapt-abbott-branching`. Do not use it for genuine reflective writing with no fixed choices — for that, `adapt-abbott-opentext`'s `reflection` variant is the right tool; `pagefeedback`'s note is secondary to its two-choice response, not the main event.

> **Routing note:** this component is new and does not yet have an entry in `design-kb/design-kb.activity-patterns.json` (component-mapping-artefact.md is SUPERSEDED, MA-1). It was evaluated against that store's content-shape vocabulary before building (no existing shape matched — it is meta-furniture framing the page, like `adapt-abbott-confidence`'s wrapper-page precedent, not authored teaching content). Adding a routing entry is a pending follow-up.

---

## 2. The annotated JSON shape

`_component` is `"pagefeedback"` (lowercase). **[LB]** = load-bearing.

| Field | Authored? | Notes |
|---|---|---|
| `_component: "pagefeedback"` | ✓ | **[LB]** lowercase — not the plugin dir name. |
| `title` / `displayTitle` / `body` / `instruction` | optional | Standard component fields (inherited via the schema's `$ref`). `body` is the natural place for the framing question (e.g. "Did this page help you find your next step?"). |
| `_variant` | optional | **[LB]** enum `conversation` \| `growth` \| `fieldnote`. Visual treatment only (illustration/accent) — never changes behaviour or the persisted data shape. Default `conversation`. |
| `_choicePositiveLabel` / `_choiceNegativeLabel` | optional | Override the two button labels. Blank (the default) falls back to the variant's default wording (e.g. conversation: "Yes, it helped" / "Not quite"; growth: "That made sense" / "I need more clarity"; fieldnote: "Found what I needed" / "Something is missing"). |
| `_isCompletionBearing` | optional | **[LB]** boolean, default `false`. When true, a successful Save contributes to lesson completion. Completion is sticky — never revoked by a later Clear (mirrors `adapt-abbott-opentext`'s `reset()` override). |

Globals (`ariaRegion`, `choicesGroupLabel`, `notePlaceholder`, `noteLabel`, `statusPrompt`, `statusChosen`, `statusChooseFirst`, `statusSaved`, `statusFailed`, `statusCleared`, `submitButtonLabel`, `clearButtonLabel`, `completedState`) carry sensible defaults; override only for wording.

---

## 3. Authoring guardrails (hard rules)

1. **Two fixed choices, not an items array.** Unlike `confidence`, there is no `_items[]` — the response is always exactly one of `helpful` / `needs-work`. Do not try to add more choices; a third option is a different component, not a config change here.
2. **The note is always optional and always secondary.** It is hidden until a choice is made (matching the source demo), never required, and never gates Save.
3. **Nothing is saved until Save response is pressed.** Choosing a response or typing a note only updates local view state; Save response persists both together, Clear response wipes and persists the cleared state immediately. This mirrors the source demo's "choose, then explicitly act" flow — adapted from client-side file download (meaningless inside a SCORM/Moodle iframe) to `offlineStorage`/suspend_data persistence (the correct in-course equivalent).
4. **`_isCompletionBearing` has no separate complete button.** Unlike `opentext`'s minimum-characters gate needing its own affordance, completion here is simply "did you respond" — Save does both jobs. Do not add a second button for this.
5. **Variant is cosmetic only.** `_variant` must never be read as a behavioural switch (unlike `opentext`'s `reflection`/`notes` variants, which do change completion eligibility). If a future requirement needs behavioural differences per variant, that is a new property, not an overload of `_variant`.

---

## 4. Voice rules (reference — not restated here)

| Field | Content type | Voice Spec |
|---|---|---|
| `body` / `instruction` | The framing question | §15.4 (activity instruction) |
| `_choicePositiveLabel` / `_choiceNegativeLabel` | Short response labels | §11.7 (concise, no hedging) |
| `globals.*` status/button strings | UI chrome, not teaching content | Not voice-governed — plain, functional English; CLAUDE.md's golden rules (student-facing *course* copy) do not extend to component chrome strings, but keep them calm and non-alarming regardless (`statusFailed` especially). |

---

## 5. Tier-dependent guidance (reference — Tier Spec)

Not graded, so the Tier Spec's assessment dimension (§7) does not apply, and the component carries no tier-sensitive logic — register follows the pathway's general §16 band for whatever framing question the author writes in `body`. There is no other tier dimension to this component; it is pure UI chrome plus a binary self-report.

---

## 6. Accessibility requirements

- **Toggle-button pair, not radios.** The two choices are `<button aria-pressed>` elements in a `role="group"` container with a group-level `aria-label` (`choicesGroupLabel`). This is a **novel pattern for this repo** — no existing component implements an `aria-pressed` toggle pair — chosen because the source demo's two independent, mutually-exclusive buttons map onto the standard WAI-ARIA toggle-button convention more directly than a radio-group (which implies a single control, not two separately-styled buttons). If a second instance of this pattern is built, promote it to a shared note rather than re-deriving it.
- **Status line is declarative, not imperative.** Unlike `opentext` (which keeps its status line outside the React re-render loop so a debounced autosave never fights a live region), `pagefeedback`'s status only changes on discrete user actions (choose / save / clear), so it is driven straight from model state (`_saveStatus`) through the normal re-render — no `_announce()`/clear-then-settimeout trick is needed, and adding one would be unused complexity.
- **The note field sits outside the re-render loop.** Typing updates the model silently (`model.setNote()`, no `change:_note` listener) so the textarea never loses focus or cursor position mid-sentence — the same rationale `opentext` documents for keeping its textarea off the render path.
- **Completion chip, not a second button.** When `_isCompletionBearing` and complete, a static confirmation shows (no interactive control to manage focus for, unlike `opentext`'s button→confirmation swap).

---

## 7. Known gotchas & findings

- **`_component` is `"pagefeedback"`** (lowercase), not the plugin directory name.
- **No `cmi.interactions` recording** — persists via a custom `offlineStorage` key (`pf:<id>`) into `cmi.suspend_data`, exactly like `opentext`, and for the same reason: a two-choice self-report has no `correct`/`incorrect` to report, and `cmi.interactions` would coerce one.
- **`clearResponse()` is deliberately not named `reset()`.** `reset(type, canReset)` is `ComponentModel`'s own revisit-reset lifecycle method; a same-named "clear the form" action would silently shadow it. This was caught during design, before any code was written — flagging here so a future refactor doesn't reintroduce the collision.
- **Save/Clear in preview without SCORM (no `grunt server-scorm`) will show the Failed status.** `saveResponse()`/`clearResponse()` return `success: false` whenever `Adapt.spoor?.scorm` or `lmsConnected` is absent, and the view surfaces that as `statusFailed` — this is the same behaviour `opentext` has always had, not a new bug; per CLAUDE.md's tracking-behaviour guardrail, persistence must be verified empirically with `grunt server-scorm`, not assumed from preview.
- **No `example.json`** — this spec's worked example is the reference.

---

## 8. Worked example (ILLUSTRATIVE — no authored instance yet)

An end-of-page check for an introductory lesson page, `growth` variant:

```json
{
  "_component": "pagefeedback",
  "_variant": "growth",
  "body": "Was this explanation useful for your learning?",
  "_isCompletionBearing": false
}
```

**How it satisfies the spec:** `body` carries the framing question (guardrail — standard field, §2); `_variant: "growth"` selects the lesson-focused illustration/accent and its default choice labels ("That made sense" / "I need more clarity") without any behavioural change (guardrail 5); no `_choicePositiveLabel`/`_choiceNegativeLabel` override, so the variant defaults apply; `_isCompletionBearing` left at its default `false` since this is a mid-pathway lesson page, not a page where the author wants the response itself to gate completion.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **pagefeedback** component. There is no upstream design-decision record for it yet (§1) — this spec is that record until one exists. Register and chrome-string voice live in the **Voice Specification** only where noted (§4); tier register in the **Tier Specification** (§5, thin — this component carries almost no tier dimension); routing in the mapping artefact once an entry is added (§1 routing note); the deliberate separation from scoring lives in **`scoring-and-summative-model.md`** (this component is never graded). This doc points to them; it does not restate them.

---

*End of pagefeedback authoring spec — v0.1.*
