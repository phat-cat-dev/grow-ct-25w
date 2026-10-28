# glossary (adapt-abbott-glossary) — Authoring Spec

**Version:** 0.1
**Status:** draft — ships with the component (built 2 August 2026). No authored lesson instance yet; the worked examples are **build-verified** (rendered and behaviour-confirmed via Playwright verification, 2 August 2026) but no shipped instance — a step stronger than illustrative, still short of a real authored placement. First real instance lands when a Researching or Reflective Practice lesson introduces methodological vocabulary.
**Verified against:** `src/components/adapt-abbott-glossary/properties.schema` — **our own schema** (custom component).
**Relationship to other documents:** this component's build rationale lives in design decisions GL-1–8 (accessibility model GL-A) and build spec GB-1–6. This spec references the Voice Specification and `design-kb/design-kb.palette.json` (component-mapping-artefact.md is SUPERSEDED, MA-1); it restates neither.

---

## 1. Purpose & when to reach for it

A **presentational glossary-passage component** rendering continuous prose with inline term markers. Selecting a marked term reveals its definition in place, without leaving the page. Designed for **definition at point of need** — technical vocabulary arrives where it's introduced, not in a separate glossary section.

**Not a question component.** No marking, no correct answer, no `_recordInteraction`, no response semantics. Completion is by visitation — opening each term definition at least once.

### The three-way routing rule

The project has three patterns for definitions; this spec covers when to use which:

| Pattern | Component | Use when |
|---------|-----------|----------|
| **Glossary passage** | `glossary` | Introducing several terms (2–8) in teaching prose where inline definitions would interrupt the flow. Terms revealed on demand. |
| **Standalone glossary** | `accordion` | A browsable reference section listing terms alphabetically. No surrounding prose — learner looks up terms as needed. |
| **Inline parenthetical** | `text` | One or two brief definitions that fit naturally in the sentence. Example: "Your thesis (the central argument of the essay) should be stated early." |

**Reach for `glossary` when:**
- Introducing **2–8 technical terms** within teaching prose
- Definitions would **interrupt the reading flow** if shown inline
- Terms need **more than a parenthetical phrase** to explain properly
- The passage establishes vocabulary that will recur throughout the lesson

**Do not use it when:**
- There's only one term (use parenthetical in `text`)
- The glossary is standalone/browsable (use `accordion`)
- Definitions are very short and fit naturally inline (use parenthetical)
- You need to assess vocabulary knowledge (use `matching` or `mcq`)

---

## 2. The glossary JSON shape

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `_component: "glossary"` | yes | — | Lowercase — the registered component name. |
| `displayTitle` | recommended | — | Student-facing heading. |
| `body` | optional | — | Introductory framing prose above the passage. |
| `instruction` | recommended | — | "Select each marked term to see its definition." |
| `_passage[]` | yes | — | Array of segment objects (see below). Minimum 2 segments. |

**Each `_passage[]` entry:**

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `text` | yes | — | The text content of this segment (word, phrase, or sentence). |
| `_term` | no | — | If present, this segment is a marked term (carries a definition). |

**`_term` object (when present):**

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `term` | yes | — | The glossary headword. May differ from segment text (e.g. "reference" for "referencing"). |
| `definition` | yes | — | The definition. First sentence must be self-contained. No contractions. HTML allowed. |

Globals (`ariaRegion`) carry sensible defaults; override only for wording.

---

## 3. Authoring guardrails (hard rules)

1. **Every segment needs `text`.** Even plain segments (no `_term`) require a `text` value — this forms the visible prose.

2. **Both `term` and `definition` are required when `_term` is present.** The headword names the concept; the definition explains it.

3. **Mark 2–8 terms per passage.** The schema requires at least 2 passage segments (you cannot carry 2 terms with fewer), but the 2–8 term bound itself cannot be fully enforced by JSON Schema draft-04. **A console warning appears at runtime if the term count is outside this range.** Fewer than 2 terms: use parenthetical. More than 8 terms: split into multiple passages or use an accordion glossary section.

4. **First-use marking only.** Mark the first occurrence of each term in the lesson. If "thesis" appears again later, it's no longer marked — the definition is already available. This is enforced by authoring discipline, not code.

5. **This component owns its passage.** It does NOT reach into other components' `body` text to mark terms. Each glossary component marks terms within its own `_passage` only. If you need definitions for terms in a separate `text` component, either move the prose into a `glossary` passage or use parenthetical definitions.

6. **Definition voice: first sentence self-contained.** The first sentence of each definition must explain the term without relying on preceding context. It should be quotable on its own. (Voice Spec §15.7)

7. **No contractions in definitions.** Definitions use formal register even when surrounding prose uses contractions freely. This matches the glossary/definition style in *Excelling at University*.

8. **No circular definitions.** Do not define "thesis" as "the thesis of an essay". The definition must use different words.

9. **Segment the passage at authoring time.** You must pre-divide the passage into segments. Each segment either carries a `_term` (marked) or not (plain prose). The component cannot auto-detect terms from continuous text.

10. **Preserve whitespace between segments.** Include leading/trailing spaces in segment `text` where needed to preserve prose flow. The component concatenates segments directly.

---

## 4. Voice rules (reference — not restated here)

Presentational throughout — no feedback or scoring copy.

| Field | Content type | Voice Spec |
|-------|--------------|------------|
| `_term.term` | Glossary headword | Noun or noun phrase; usually singular ("reference" not "references") |
| `_term.definition` | Term definition | §15.7: first sentence self-contained; no circularity; no contractions |
| `body` | Introductory context | §15.1: mid-register; keep brief |
| `instruction` | Activity instruction | §15.4: one sentence on what to do |

Contractions follow the lesson context (§11.2) for the surrounding `_passage` prose — usually yes for mid-lesson teaching. Definitions themselves never use contractions.

---

## 5. Tier-dependent guidance

The component is **not graded**, so the Tier Spec's assessment dimension does not apply. Tier lands in:

- **Definition depth and vocabulary.** Introductory definitions use simpler explanations and concrete examples; advanced definitions can assume familiarity with related concepts and use technical language.
- **Term density.** Introductory passages may introduce fewer terms with more surrounding context; advanced passages can be denser.
- **Examples in definitions.** Introductory definitions benefit from worked examples inside the definition body; advanced tiers can be more abstract.

The interaction itself is tier-neutral — markers and definitions work the same way at all levels.

---

## 6. Accessibility requirements

- **Term markers are native `<button>`** with `aria-expanded` and `aria-controls` pointing to the definition region. Keyboard operation: Tab to navigate, Enter/Space to toggle.
- **Accessible name = "Definition of: [term]"** — the headword is short and informative, so we use the full term in the accessible name (unlike the annotated component's terse "Note N" pattern).
- **Definition region is `role="region"`** with `aria-live="polite"` for dynamic content updates. The heading inside the region names the term.
- **Focus management.** When a marker is clicked, focus moves to the definition region. The "Back to passage" button returns focus to the originating marker.
- **Single-open simplifies focus.** Only one definition is ever expanded; no complex focus-trap handling required.
- **Reduced motion.** CSS includes `@media (prefers-reduced-motion: reduce)` — transition disabled for users who prefer reduced motion.
- **Component-prefixed IDs.** All IDs are prefixed with the component's `_id` to avoid collisions when multiple glossary components appear on one page.

### Why not ARIA Annotations or aria-details?

The build recon (2 August 2026) established that:
- **aria-details** has unverified assistive technology support across screen readers
- **WAI-ARIA Annotations roles** are still 1.3 draft, not production-ready

We use the **footnote/disclosure pattern** (button + controlled region) which has established support. This matches the annotated component and provides reliable keyboard and screen reader interaction.

### Tap-target size (inline exception)

Term markers are inline `<button>` elements within prose. Their tap-target size follows the text — width varies by term length, height follows the line box (typically ~26px at body size). This is smaller than the 44×44px commonly cited for touch targets.

This is an **accepted trade-off**, not an oversight. WCAG 2.5.8 (Target Size: Minimum) explicitly exempts "targets that are in a sentence or block of text" — the inline exception exists precisely because requiring large targets would break prose layout. The same characteristic applies to `adapt-abbott-annotated` markers.

Mitigations: visible focus ring, adequate text size at body scale, and the fact that the entire term text is the tap target (not a small icon).

---

## 7. Known gotchas & findings

- **`_component` is `"glossary"`** (lowercase), not the plugin directory name.
- **Segments are concatenated directly.** Whitespace matters — include trailing/leading spaces in `text` to preserve prose flow.
- **No `_items` in the schema.** Unlike most Adapt components, this uses `_passage` (the prose segments) as the source; the model derives internal items from segments that have `_term`. This follows the `annotated` pattern.
- **Completion = visitation, not read time.** A term is "visited" when its definition is opened; there's no read-time requirement.
- **`_expandedIndex` is transient.** On revisit, no term is expanded. Completion status persists via the base class's `_userAnswer` boolean array; the expanded state itself does not.
- **Definition region focus is programmatic.** The region has `tabindex="-1"` for focus receipt but is not in the natural tab order.
- **Index-keying.** Terms are assigned contiguous 0-based indices in passage order. The base class's `storeUserAnswer`/`restoreUserAnswers` use this index for persistence.
- **2–8 term bound is runtime-warned, not schema-enforced.** JSON Schema draft-04 cannot constrain a filtered subset of an array. The schema sets `minItems: 2` on the passage array and documents the bound in help text; the model logs a console warning if the derived term count is outside 2–8.
- **Tap targets are text-sized, not 44px.** Inline term buttons follow the prose line height (~26px). This is covered by WCAG 2.5.8's inline exception and is an accepted trade-off shared with `adapt-abbott-annotated`. See §6 for details.

---

## 8. Worked examples (BUILD-VERIFIED — no shipped instance yet)

These examples were **build-verified** via Playwright testing (2 August 2026) — rendered correctly, accessibility attributes confirmed, single-open behaviour working, completion firing. No shipped lesson instance yet; first real placement lands when a Researching or Reflective Practice lesson introduces vocabulary.

### 8.1 Two-term glossary (minimum)

```json
{
  "_component": "glossary",
  "_layout": "full",
  "displayTitle": "Key terms",
  "body": "",
  "instruction": "Select each marked term to see its definition.",
  "_passage": [
    { "text": "When you write an essay, you need to support your claims with " },
    {
      "text": "evidence",
      "_term": {
        "term": "evidence",
        "definition": "Facts, data, or examples that support an argument or claim. Evidence gives your reader a reason to believe what you are saying, rather than asking them to take your word for it."
      }
    },
    { "text": ". This is what distinguishes academic writing from opinion: every significant claim connects back to something concrete, whether that is a research finding, a quotation from a source, or a worked example. Your " },
    {
      "text": "thesis",
      "_term": {
        "term": "thesis",
        "definition": "The central argument or main claim of an essay. A thesis statement typically appears early in the introduction and tells the reader what position you will defend throughout the piece."
      }
    },
    { "text": " should be supported throughout." }
  ]
}
```

**How it satisfies the spec:** five segments (guardrail 1 — each has `text`); two have `_term` with both `term` and `definition` (guardrails 2, 3); definitions have self-contained first sentences (guardrail 6); no contractions in definitions (guardrail 7); whitespace preserved in segment text (guardrail 10).

### 8.2 Eight-term glossary (maximum)

```json
{
  "_component": "glossary",
  "_layout": "full",
  "displayTitle": "Writing cycle terminology",
  "body": "",
  "instruction": "Select each marked term to see its definition.",
  "_passage": [
    { "text": "Academic writing follows a " },
    {
      "text": "writing cycle",
      "_term": {
        "term": "writing cycle",
        "definition": "A structured process for producing written work. The cycle typically includes planning, drafting, editing, and proofreading stages, each serving a distinct purpose."
      }
    },
    { "text": " rather than happening in a single sitting. It begins with understanding the " },
    {
      "text": "task",
      "_term": {
        "term": "task",
        "definition": "The assignment or question you have been asked to address. Understanding the task means identifying what kind of response is expected and what the question is really asking."
      }
    },
    { "text": ", which involves separating the " },
    {
      "text": "steer",
      "_term": {
        "term": "steer",
        "definition": "The instruction words in an assignment question that tell you what to do. Words like 'analyse', 'compare', or 'evaluate' are steers that shape how you should approach the topic."
      }
    },
    { "text": " from the " },
    {
      "text": "keywords",
      "_term": {
        "term": "keywords",
        "definition": "The subject words in an assignment question that tell you what the question is about. These are the concepts, theories, or topics you need to address in your response."
      }
    },
    { "text": ". After " },
    {
      "text": "planning",
      "_term": {
        "term": "planning",
        "definition": "The stage of writing where you organise your ideas before drafting. A good plan bridges your research and your writing, giving you a structure to follow when you begin composing."
      }
    },
    { "text": " comes " },
    {
      "text": "drafting",
      "_term": {
        "term": "drafting",
        "definition": "The stage of writing where you turn your plan into connected prose. A first draft is a working document, not a finished piece; its purpose is to get your ideas onto the page."
      }
    },
    { "text": ", then " },
    {
      "text": "editing",
      "_term": {
        "term": "editing",
        "definition": "The stage of writing where you revise for clarity, structure, and argument. Editing is about improving what you have written, not just correcting errors."
      }
    },
    { "text": ", and finally " },
    {
      "text": "proofreading",
      "_term": {
        "term": "proofreading",
        "definition": "The final stage of writing where you check for surface errors such as typos, spelling mistakes, and formatting inconsistencies. Proofreading should happen after all substantive editing is complete."
      }
    },
    { "text": "." }
  ]
}
```

**How it satisfies the spec:** 17 segments forming continuous prose; 8 terms (maximum allowed); each definition has a self-contained first sentence; no contractions; terms are first-use marked at their natural introduction points in the writing cycle explanation.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **glossary** component. Its design rationale (GL-1–8, GL-A accessibility model, GB-1–6 build spec) lives in build records. Register and voice live in the **Voice Specification**; component-to-pedagogy mapping lives in **`design-kb/design-kb.palette.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

The three-way routing rule (glossary passage vs accordion vs inline parenthetical) is recorded in `design-kb/design-kb.palette.json`'s `palette/glossary` config notes; this spec documents the rule for author reference.

---

*End of glossary authoring spec — v0.1.*
