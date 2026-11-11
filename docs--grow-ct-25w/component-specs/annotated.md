# annotated (adapt-abbott-annotated) — Authoring Spec

**Version:** 0.1
**Status:** draft — ships with the component (built 2 August 2026). No authored lesson instance yet; the worked examples are **build-verified** (rendered and behaviour-confirmed via Playwright verification, 2 August 2026) but no shipped instance — a step stronger than illustrative, still short of a real authored placement. First real instance lands when an exemplar-analysis lesson (weak/strong writing pairs) is authored.
**Verified against:** `src/components/adapt-abbott-annotated/properties.schema` — **our own schema** (custom component).
**Relationship to other documents:** this component's build rationale lives in design decisions AE-1–8 (accessibility model AE-A) and build spec AB-1–6. This spec references the Voice Specification and `design-kb/design-kb.activity-patterns.json` (component-mapping-artefact.md is SUPERSEDED, MA-1); it restates neither.

---

## 1. Purpose & when to reach for it

A **presentational annotated-passage component** rendering continuous prose with inline marker buttons for annotated segments. Each marker reveals an explanatory note (title + body). Designed for exemplar analysis — showing weaker and stronger versions of academic writing with expert commentary on what makes each phrase effective or problematic.

**Not a question component.** No marking, no correct answer, no `_recordInteraction`, no response semantics. Completion is by visitation — opening each annotated segment at least once.

Reach for it when:
- Showing a **text passage with phrase-level expert commentary** embedded inline
- Contrasting **weak and strong examples** where specific phrases warrant explanation
- Teaching **rhetorical awareness** by highlighting what makes sentences effective or problematic
- The content is best understood as **continuous prose** with annotations, not separate scenario + analysis blocks

Do not use it when:
- You need to assess understanding (use `mcq`, `matching`)
- The analysis is at paragraph or section level rather than phrase level (use `narrative` with side-by-side pairs)
- There are no annotated segments (use plain `text`)
- The commentary is purely spoken/video (use `media`)

---

## 2. The annotated JSON shape

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `_component: "annotated"` | yes | — | Lowercase — the registered component name. |
| `displayTitle` | recommended | — | Student-facing heading. |
| `body` | optional | — | Introductory text above the passage. |
| `instruction` | recommended | — | "Select each marked phrase to see the commentary." |
| `_passage[]` | yes | — | Array of segment objects (see below). |

**Each `_passage[]` entry:**

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `text` | yes | — | The text content of this segment (sentence, phrase, or fragment). |
| `_note` | no | — | If present, this segment is annotated (carries commentary). |

**`_note` object (when present):**

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `title` | no | — | Short heading for the note (e.g. "Vague claim", "Clear thesis"). |
| `body` | yes | — | The explanatory commentary. HTML allowed. |

Globals (`ariaRegion`) carry sensible defaults; override only for wording.

---

## 3. Authoring guardrails (hard rules)

1. **Every segment needs `text`.** Even plain segments (no `_note`) require a `text` value — this forms the visible prose.

2. **`_note.body` is required when `_note` is present.** Title is optional (may be left blank for simple annotations), but body must explain the significance.

3. **Segment the passage at authoring time.** You must pre-divide the passage into segments. Each segment either carries a `_note` (annotated) or not (plain prose). The component cannot auto-detect segments from continuous text.

4. **Keep note titles terse.** 2–4 words: "Vague claim", "Specific evidence", "Empty signposting". The title labels the kind of move; the body explains why.

5. **Completion requires visiting all annotated segments.** Plain segments (no `_note`) do not count toward completion. The learner must open every marker at least once.

6. **Zero-note passages never complete.** A passage with no `_note` segments has no interactive requirement and will not auto-complete. Avoid this authoring pattern unless deliberately paired with a sibling component that gates progress.

7. **Single-open by default.** Opening a new note closes any currently open note. This keeps focus on one point at a time and is not configurable in this version.

8. **Preserve whitespace between segments.** Include leading/trailing spaces in segment `text` where needed to preserve prose flow. The component concatenates segments directly.

---

## 4. Voice rules (reference — not restated here)

Presentational throughout — no feedback or scoring copy.

| Field | Content type | Voice Spec |
|-------|--------------|------------|
| `_note.title` | Label for the move/pattern | Terse noun phrase: "Vague claim", "Clear thesis", "Signposting" |
| `_note.body` | Expert commentary | §15.2: evaluative about work not person; explain why (§4); mid-register (§13) |
| `body` | Introductory context | §15.1: mid-register; keep brief |
| `instruction` | Activity instruction | §15.4: one sentence on what to do |

Contractions follow the lesson context (§11.2) — usually yes for mid-lesson teaching.

---

## 5. Tier-dependent guidance

The component is **not graded**, so the Tier Spec's assessment dimension does not apply. Tier lands in:

- **Note body length and vocabulary.** Introductory notes use simpler explanations; advanced notes can assume rhetorical terminology.
- **Scaffolding.** Introductory passages may have more notes per segment; advanced passages can leave more implicit.

The interaction itself is tier-neutral — markers and notes work the same way at all levels.

---

## 6. Accessibility requirements

- **Marker buttons are native `<button>`** with `aria-expanded` and `aria-controls` pointing to the note region. Keyboard operation: Tab to navigate, Enter/Space to toggle.
- **Accessible name = "Note N"** (concise form). The marker does not quote the span text in its accessible name — that would make names overly long.
- **Note region is `role="region"`** with `aria-live="polite"` for dynamic content updates.
- **Focus management.** When a marker is clicked, focus moves to the note region. The "Back to passage" button returns focus to the originating marker.
- **Single-open simplifies focus.** Only one note is ever expanded; no complex focus-trap handling required.
- **Reduced motion.** CSS includes `@media (prefers-reduced-motion: reduce)` — transition disabled for users who prefer reduced motion.
- **Component-prefixed IDs.** All IDs are prefixed with the component's `_id` to avoid collisions when multiple annotated components appear on one page.

---

## 7. Known gotchas & findings

- **`_component` is `"annotated"`** (lowercase), not the plugin directory name.
- **Segments are concatenated directly.** Whitespace matters — include trailing/leading spaces in `text` to preserve prose flow.
- **No `_items` in the schema.** Unlike most Adapt components, this uses `_passage` (the prose segments) as the source; the model derives internal items from segments that have `_note`.
- **Completion = visitation, not read time.** A note is "visited" when opened; there's no read-time requirement.
- **`_expandedIndex` is transient.** On revisit, no note is expanded. Completion status persists via the base class's `_userAnswer` boolean array; the expanded state itself does not.
- **Note region focus is programmatic.** The region has `tabindex="-1"` for focus receipt but is not in the natural tab order.

---

## 8. Worked example (BUILD-VERIFIED — no shipped instance yet)

A weak-example passage with three annotated segments. **Build-verified** — rendered and behaviour-confirmed via Playwright verification (2 August 2026); the first real instance is authored when a real lesson needs this pattern.

### 8.1 Weak introduction with phrase-level commentary

```json
{
  "_component": "annotated",
  "_layout": "full",
  "displayTitle": "A weaker introduction",
  "body": "<p>This introduction shows some common issues. Select the marked phrases to see what could be improved.</p>",
  "instruction": "Select each marked phrase to see the commentary.",
  "_passage": [
    { "text": "In this essay I will discuss crime. " },
    {
      "text": "Crime is a big problem in society today.",
      "_note": {
        "title": "Vague claim",
        "body": "<p>This sentence states the obvious without adding anything specific. What kind of crime? Where? The reader learns nothing they didn't already know.</p>"
      }
    },
    { "text": " There are many different types of crime. " },
    {
      "text": "Some people think crime is bad.",
      "_note": {
        "title": "Trivial observation",
        "body": "<p>This is not a debatable claim. Academic writing should engage with questions where reasonable people might disagree, not restate universally held views.</p>"
      }
    },
    { "text": " I will now explain why. " },
    {
      "text": "This essay will look at crime from different angles.",
      "_note": {
        "title": "Empty signposting",
        "body": "<p>Announcing that you'll 'look at' something from 'different angles' tells the reader nothing about what those angles are or why they matter. Effective signposting previews the actual structure.</p>"
      }
    }
  ]
}
```

**How it satisfies the spec:** six segments (guardrail 1 — each has `text`); three have `_note` with `body` (guardrail 2); note titles are terse ("Vague claim", "Trivial observation", "Empty signposting") (guardrail 4); whitespace preserved in segment text (guardrail 8).

### 8.2 Strong introduction with phrase-level commentary

```json
{
  "_component": "annotated",
  "_layout": "full",
  "displayTitle": "A stronger introduction",
  "body": "<p>This introduction demonstrates clearer academic writing. Select the marked phrases to see why they work.</p>",
  "instruction": "Select each marked phrase to see the commentary.",
  "_passage": [
    {
      "text": "Youth crime in England and Wales fell by 23% between 2010 and 2020, yet public perception of the problem intensified over the same period.",
      "_note": {
        "title": "Specific, sourced claim",
        "body": "<p>This opening grounds the discussion in verifiable data and immediately establishes a tension worth exploring: the gap between reality and perception.</p>"
      }
    },
    { "text": " This essay examines " },
    {
      "text": "how media framing of knife crime contributed to this perception gap,",
      "_note": {
        "title": "Clear focus",
        "body": "<p>The reader now knows exactly what the essay will argue about. 'Media framing' and 'perception gap' are specific enough to direct the analysis.</p>"
      }
    },
    { "text": " drawing on Cohen's moral panic framework and three case studies from 2018-2019. " },
    {
      "text": "It argues that episodic news coverage systematically overweights rare but dramatic incidents.",
      "_note": {
        "title": "Thesis statement",
        "body": "<p>This is the essay's central claim, stated directly. The reader knows what position the writer will defend and can evaluate the evidence against it.</p>"
      }
    }
  ]
}
```

**How it satisfies the spec:** five segments; three annotated; note titles label the rhetorical move ("Specific, sourced claim", "Clear focus", "Thesis statement"); body explains why each works.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **annotated** component. Its design rationale (AE-1–8, AE-A accessibility model, AB-1–6 build spec) lives in build records. Register and voice live in the **Voice Specification**; component-to-pedagogy mapping lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of annotated authoring spec — v0.1.*
