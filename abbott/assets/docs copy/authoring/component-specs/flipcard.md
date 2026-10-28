# flipcard (adapt-abbott-flipcard) — Authoring Spec

**Version:** 0.1
**Status:** draft — ships with the component (built 31 July 2026). No authored lesson instance yet; the worked example is **build-verified** (rendered and behaviour-confirmed via browser check, 31 July 2026) but no shipped instance — a step stronger than illustrative, still short of a real authored placement. First real instance lands when a terminology cluster or comparable visual-concept lesson is authored.
**Verified against:** `src/components/adapt-abbott-flipcard/properties.schema` — **our own schema** (custom component; no `example.json`).
**Relationship to other documents:** this component's build rationale lives in `open-decisions.md` (#35 build-own ladder, FC-1–6 design, FB-1–5 build). This spec references the Voice Specification and `design-kb/design-kb.activity-patterns.json` (component-mapping-artefact.md is SUPERSEDED, MA-1); it restates neither.

---

## 1. Purpose & when to reach for it

A **presentational card-set component** with front and back faces. Each card flips to reveal back content on selection. Supports text-front (title and/or body) and image-front (graphic). Completion by visiting all cards — flip each card at least once. Part of the VO-1 Signpost design palette (treatment 4 — playful/interactive reveal).

**Not a question component.** No marking, no correct answer, no `_recordInteraction`, no response semantics. The base class's visitation tracking (`_userAnswer` as a boolean array) is legitimate persistence plumbing only (FC-1 amendment: items are index-keyed, not `_id`-keyed — diverges deliberately from confidence, where `_id` is load-bearing).

Reach for it when:
- A concept is best taught through **paired reveal** — a prompt on the front, explanation on the back
- A set of **visual terms or diagrams** benefits from flip-to-reveal (e.g. labelled images)
- You want learners to **self-pace through a small set** rather than scroll or paginate

Do not use it when:
- You need to assess understanding (use `mcq`, `matching`, `sortable`)
- The content is purely linear text (use `text` or `narrative`)
- The set is large (>6 cards); consider `accordion` or `hotgraphic` instead

---

## 2. The annotated JSON shape

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `_component: "flipcard"` | yes | — | Lowercase — the registered component name. |
| `displayTitle` | recommended | — | Student-facing heading. |
| `body` | optional | — | Introductory text above the cards. |
| `instruction` | recommended | — | "Select each card to flip it…" or similar. |
| `_flipBehaviour` | no | `"independent"` | `"independent"`: cards flip and stay individually; `"single"`: only one card open at a time (auto-closes others). |
| `_items[]` | yes | — | Array of card objects (see below). |

**Each `_items[]` entry:**

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `_id` | optional | index | Stable identifier for analytics. If blank, array index is used. **Not load-bearing** for persistence (FC-1). |
| `front.title` | at-least-one | — | Front face title. Also used as accessible name if present. |
| `front.body` | at-least-one | — | Front face body text. Supports HTML. |
| `front._graphic.src` | at-least-one | — | Image path (relative to course assets). |
| `front._graphic.alt` | if graphic | — | Alt text; leave blank if decorative and title provides context. |
| `back.title` | at-least-one | — | Back face title. |
| `back.body` | at-least-one | — | Back face body text. Supports HTML. |

**"At-least-one" rule:** Each front face must have at least one of `title`, `body`, or `_graphic`. Each back face must have at least one of `title` or `body`. The schema help text documents this; validation is the author's responsibility (JSON Schema draft-04 cannot enforce cross-field disjunctions).

Globals (`ariaRegion`) carry sensible defaults; override only for wording.

---

## 3. Authoring guardrails (hard rules)

1. **At least one front-face element.** Every card's front must have title, body, or graphic — never all three empty. A blank front renders as "Card N" fallback but should be avoided.

2. **At least one back-face element.** Every card's back must have title or body. A blank back renders as "(No back content)" and is always an authoring error.

3. **Keep card sets small.** 3–6 cards per component instance. Larger sets lose the flip affordance's value; use `accordion` or break into multiple instances.

4. **Use `_flipBehaviour: "single"` for sequential reveal.** When back content builds on previous cards (e.g. "stages in order"), single mode ensures the learner processes one at a time.

5. **Image alt text or title.** When using `front._graphic`, either provide `alt` or ensure `front.title` supplies sufficient accessible name. Do not leave both empty.

6. **Completion requires all cards flipped.** The learner must flip every card (to back) at least once; completion fires when the last card is visited. Cards can be re-flipped without penalty.

7. **Index-keyed persistence (FC-1).** The base class stores visitation as an index-sorted boolean array. Reordering `_items` between sessions breaks restoration. If you must reorder, expect learners to see partial completion reset. The `_id` field is for analytics clarity, not persistence.

---

## 4. Voice rules (reference — not restated here)

Presentational throughout — no feedback or scoring copy to voice.

| Field | Content type | Voice Spec |
|-------|--------------|------------|
| `front.title` | Term, concept label, or question hook | Crisp noun phrase or short question (§11 clarity) |
| `front.body` | Brief prompt or context-setter | Mid-register, concise (§13) |
| `back.title` | Answer heading or "Why this matters" | Match front register |
| `back.body` | Explanation, definition, or worked micro-example | Explain the *why* (§4), appropriate to tier (§16) |
| `instruction` | Activity instruction | §15.4 |

Contractions follow the lesson context (§11.2) — usually yes for mid-lesson teaching, no for learning-outcome-adjacent content.

---

## 5. Tier-dependent guidance

The component is **not graded**, so the Tier Spec's assessment dimension does not apply. Tier lands in two places:

- **Vocabulary and concept complexity.** Introductory cards introduce foundational terms with more scaffolding on the back; intermediate/advanced cards can assume prior knowledge.
- **Card count.** Introductory lessons may use fewer cards (3–4); advanced lessons can stretch to 5–6 without losing focus.

The flip interaction itself is tier-neutral — the mechanic is self-paced and non-threatening at all levels.

---

## 6. Accessibility requirements

- **Each card is a native `<button>`** containing both faces, with `aria-expanded` reflecting flip state. Keyboard operation is Enter/Space to toggle, Tab to move between cards.
- **Accessible name = front title**, stable across flip. The button's `aria-label` is derived from `front.title` (fallback: "Card N"). It does not change when the card flips.
- **Both faces in DOM; non-current face `aria-hidden`.** Front has `aria-hidden` when flipped; back has `aria-hidden` when not flipped — symmetrical.
- **No focus movement on flip.** Focus stays on the button; the flip is a state change, not navigation.
- **`ariaRegion` introduces the interaction** at component level (defaults to "Flip cards. Select each card to reveal its other side.").
- **Reduced motion.** CSS includes `@media (prefers-reduced-motion: reduce)` — animation falls back to instant opacity swap, no rotation. *(Not yet verified live; carried to the strategic accessibility-verification pass.)*

---

## 7. Known gotchas & findings

- **`_component` is `"flipcard"`** (lowercase), not the plugin directory name.
- **Completion = visitation, not flip-back.** A card is "visited" when flipped to back the first time; flipping back to front doesn't unvisit. All cards must be visited for completion.
- **`_isFlipped` is transient, not persisted.** On revisit, all cards present front-face-up. Completion status persists via the base class's `_userAnswer` boolean array; the flip state itself does not.
- **Grid layout with auto-fit.** Cards flow into a responsive grid with min-width ~280px per card. Narrow viewports collapse to single-column. Long back content scrolls within the card face (`overflow-y: auto`); the card does not grow.
- **No `example.json`** — this spec's worked example is the reference.

---

## 8. Worked example (BUILD-VERIFIED — no shipped instance yet)

A text-front card set for a writing-cycle topic, three cards in independent mode. **Build-verified** — rendered and behaviour-confirmed via browser check (31 July 2026); the first real instance is authored when a real lesson needs this pattern.

### 8.1 Text-front, independent mode

```json
{
  "_component": "flipcard",
  "_layout": "full",
  "displayTitle": "Key stages of the writing cycle",
  "body": "<p>Each stage of the writing cycle has a distinct purpose. Flip each card to see why.</p>",
  "instruction": "Select each card to flip it and reveal the back.",
  "_flipBehaviour": "independent",
  "_items": [
    {
      "front": {
        "title": "Planning",
        "body": "<p>The first stage of the writing cycle.</p>"
      },
      "back": {
        "title": "Why planning matters",
        "body": "<p>Planning separates the thinking from the writing. When you have a plan, you're not trying to invent your argument and your sentences at the same time.</p>"
      }
    },
    {
      "front": {
        "title": "Drafting",
        "body": "<p>Getting your ideas onto the page.</p>"
      },
      "back": {
        "title": "The purpose of a first draft",
        "body": "<p>A first draft is meant to be rough. Its job is to give you something to improve, not to be perfect on the first attempt.</p>"
      }
    },
    {
      "front": {
        "title": "Editing",
        "body": "<p>Improving what you've written.</p>"
      },
      "back": {
        "title": "Editing vs proofreading",
        "body": "<p>Editing focuses on meaning and argument. Proofreading focuses on surface errors. They're different jobs that benefit from being done separately.</p>"
      }
    }
  ]
}
```

**How it satisfies the spec:** three cards (guardrail 3); each front has title + body (guardrail 1); each back has title + body (guardrail 2); `_flipBehaviour: "independent"` allows multiple cards flipped at once — appropriate when order doesn't matter; front titles serve as accessible names (guardrail 5/§6).

### 8.2 Image-front, single mode (secondary illustration)

```json
{
  "_component": "flipcard",
  "_layout": "full",
  "displayTitle": "Visual concepts",
  "body": "<p>Some concepts are easier to grasp with an image. Flip each card to explore.</p>",
  "instruction": "Select each card to flip it. Only one card can be open at a time.",
  "_flipBehaviour": "single",
  "_items": [
    {
      "front": {
        "title": "The writing cycle",
        "_graphic": {
          "src": "course/en/images/L01-writing-cycle.png",
          "alt": "Diagram showing the five stages of the writing cycle"
        }
      },
      "back": {
        "title": "Five interconnected stages",
        "body": "<p>The writing cycle comprises five stages: understand the task, plan, draft, edit, and proofread. Each stage has a distinct purpose, and moving through them in order prevents common problems.</p>"
      }
    },
    {
      "front": {
        "title": "Single-width placeholder",
        "_graphic": {
          "src": "course/en/images/single-width.png",
          "alt": "Placeholder image for single-width layout"
        }
      },
      "back": {
        "title": "Image cards in practice",
        "body": "<p>Image-front cards work well for visual concepts, diagrams, or any content where an image provides a more immediate hook than text alone.</p>"
      }
    }
  ]
}
```

**How it satisfies the spec:** two cards; each front has title + graphic (guardrail 1); each back has title + body (guardrail 2); `_flipBehaviour: "single"` enforces one-at-a-time reveal (guardrail 4); image alt text provided (guardrail 5).

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **flipcard** component. Its build rationale (#35 build-own ladder, FC-1–6 design, FB-1–5 build) lives in `open-decisions.md`; register and voice live in the **Voice Specification**; component-to-pedagogy mapping lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of flipcard authoring spec — v0.1.*
