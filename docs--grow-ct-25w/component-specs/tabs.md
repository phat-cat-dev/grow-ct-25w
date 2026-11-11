# tabs (adapt-abbott-tabs) — Authoring Spec

**Version:** 0.1
**Status:** draft — ships with the component (built 1 August 2026). No authored lesson instance yet; the worked examples are **build-verified** (rendered and behaviour-confirmed via Playwright check, 1 August 2026) but no shipped instance — a step stronger than illustrative, still short of a real authored placement. First real instance lands when a content-dense pathway calls for tabbed organisation.
**Verified against:** `src/components/adapt-abbott-tabs/properties.schema` — **our own schema** (custom component; no `example.json`).
**Relationship to other documents:** this component's build rationale lives in `open-decisions.md` (build-own ladder entry, TA-1 design, TS-1–6 build). This spec references the Voice Specification and `design-kb/design-kb.activity-patterns.json` (component-mapping-artefact.md is SUPERSEDED, MA-1); it restates neither.

---

## 1. Purpose & when to reach for it

A **tabbed-panes component** for organising parallel content into selectable panels. Presents 2–4 tabs; selecting one reveals its panel content while hiding others. The first tab is selected by default.

**Not a question component.** No marking, no correct answer, no `_recordInteraction`, no response semantics. The base class's visitation tracking (`_userAnswer` as a boolean array) handles persistence; completion triggers when all tabs have been visited.

**First homes:** Content-dense pathways where related but distinct concepts benefit from parallel organisation — comparing approaches, presenting alternatives, or chunking information that would otherwise require excessive scrolling.

Reach for it when:
- You have **2–4 parallel chunks** of related content that don't need to be read in sequence
- The content is **genuinely parallel** — the tabs represent categories, not a hidden sequence
- **Space is at a premium** and stacking all content vertically would be overwhelming

Do not use it when:
- Content must be read in order (use `narrative` or `timeline`)
- You have more than 4 categories (consider `accordion` or restructuring)
- There's a single main piece of content with optional extras (use `text` + `accordion`)
- You need images as the primary content in each panel (use `narrative`)

**Routing boundaries:**
- **vs accordion:** accordion is disclosure-driven (any number of panels, vertical expand/collapse); tabs present parallel alternatives (exactly one visible at a time). Accordion suits "explore some or all"; tabs suit "choose one view."
- **vs narrative:** narrative is image-led with prev/next navigation; tabs are text-led with random access. Narrative suits sequential visual content; tabs suit parallel conceptual content.
- **vs timeline:** timeline presents ordered stages; tabs present unordered alternatives. If the order matters, use timeline.

---

## 2. The annotated JSON shape

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `_component: "tabs"` | yes | — | Lowercase — the registered component name. |
| `displayTitle` | recommended | — | Student-facing heading. |
| `body` | recommended | — | Introductory prose — what the tabs collectively cover. |
| `instruction` | recommended | — | The ask: "Select each tab to explore the content." |
| `_items[]` | yes | — | Array of 2–4 tab objects (see below). |

**Each `_items[]` entry:**

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `tabTitle` | yes | — | The tab label — displayed on the tab button. Keep concise (1–3 words). |
| `title` | no | — | Optional heading displayed inside the panel. |
| `body` | yes | — | The panel content — displayed when this tab is selected. |
| `_graphic.src` | no | — | Optional image displayed in the panel. |
| `_graphic.alt` | no | — | Alt text for the image. Leave blank for decorative images. |

**Index-keyed persistence.** Items are keyed by array index, not `_id`. Reordering `_items` between sessions breaks restoration. If you must reorder, expect learners to see partial completion reset.

Globals (`ariaRegion`) carry sensible defaults; override only for wording.

---

## 3. Authoring guardrails (hard rules)

1. **2–4 tabs.** Every instance must have between 2 and 4 tabs. Fewer than 2 isn't a choice; more than 4 becomes overwhelming. The schema enforces this.

2. **Tab titles are concise.** Each `tabTitle` should be 1–3 words. Long titles break the horizontal layout and wrap awkwardly. If you can't summarise in 3 words, the content may not be properly chunked.

3. **Content is genuinely parallel.** Each tab should present content of similar weight and kind. If one tab has a sentence and another has five paragraphs, the structure doesn't fit.

4. **Order doesn't matter.** If the tabs must be read in sequence, use `timeline` or `narrative` instead. Tabs imply random access — the learner can visit them in any order.

5. **No hidden dependencies.** Each panel's content should be self-contained. Don't write "As described in the previous tab…" — there is no previous tab in random-access navigation.

6. **Completion requires visiting all tabs.** Unlike branching (which completes on first selection), tabs complete when all tabs have been visited. The first tab counts as visited on load.

7. **Index-keyed persistence.** Items persist by array index, not `_id`. Do not reorder `_items` between course versions unless you accept learner progress may not restore correctly.

---

## 4. Voice rules (reference — not restated here)

Informational throughout — panel content is teaching prose, not feedback or scenario.

| Field | Content type | Voice Spec |
|-------|--------------|------------|
| `body` (component) | Intro prose — mid-register | §13 (teaching prose), §11 (clarity) |
| `instruction` | Activity instruction | §15.4 (instruction conventions) |
| `tabTitle` | Tab label — crisp, parallel structure | §11 (clarity), keep labels structurally parallel |
| `_items[].title` | Panel heading — matches lesson register | §13 |
| `_items[].body` | Panel content — teaching prose | §4 (explain the why), §13 (mid-register) |

Tab labels should use parallel structure: if one tab is "Planning", the others should be "Drafting", "Editing" — not "How to draft" or "The editing stage".

Contractions follow the lesson context (§11.2) — usually yes for mid-lesson teaching, no for learning-outcome-adjacent content.

---

## 5. Tier-dependent guidance

The component is **not graded**, so the Tier Spec's assessment dimension does not apply. Tier lands in two places:

- **Content depth.** Introductory panels may explain more; advanced panels may assume more prior knowledge.
- **Vocabulary load.** Introductory tabs may use simpler labels; advanced tabs may use technical terminology if it's established elsewhere.

The interaction itself is tier-neutral — the mechanic is the same at all levels.

---

## 6. Accessibility requirements

- **Tablist container has `role="tablist"`** with `aria-orientation="horizontal"` (switches to `"vertical"` below the medium breakpoint — handled by CSS media query).

- **Each tab is a native `<button>`** with `role="tab"`, `aria-selected`, and `aria-controls` linking to its panel.

- **Roving tabindex.** The active tab has `tabindex="0"`; inactive tabs have `tabindex="-1"`. Only one tab is in the tab order at a time.

- **Keyboard navigation follows WAI-ARIA Tabs pattern:**
  - Left/Right arrow keys move between tabs with wraparound
  - Home jumps to first tab; End jumps to last tab
  - Up/Down arrows also work (for vertical orientation)
  - Automatic activation: focusing a tab selects it immediately

- **Tab panels have `role="tabpanel"`** with `aria-labelledby` linking back to their tab. Active panel has `tabindex="0"` for focus; inactive panels have `tabindex="-1"` and `aria-hidden="true"`.

- **`ariaRegion` introduces the interaction** at component level (defaults to "Tabbed content. Use arrow keys to navigate between tabs.").

- **Reduced motion.** CSS includes `@media (prefers-reduced-motion: reduce)` — transitions are suppressed. *(Carried to the strategic accessibility-verification pass.)*

---

## 7. Known gotchas & findings

- **`_component` is `"tabs"`** (lowercase), not the plugin directory name.

- **First tab is selected on load** and counts as visited. This means a 3-tab component needs only 2 additional selections to complete.

- **No toggle behaviour.** Unlike accordion, you cannot "close" a tab. Exactly one tab is always selected.

- **Horizontal by default, vertical at narrow viewports.** Below the medium breakpoint (60rem / 960px), the tablist stacks vertically with an inline-end border indicator instead of a bottom border. The keyboard navigation remains the same (Left/Up = previous, Right/Down = next).

- **No `example.json`** — this spec's worked examples are the reference.

- **Images are optional.** The component works text-only. If you add images, ensure alt text is meaningful.

---

## 8. Worked examples (BUILD-VERIFIED — no shipped instance yet)

Two real scenarios used in build verification (1 August 2026). Both are **build-verified** — rendered and behaviour-confirmed via Playwright checks. First shipped instance lands when a content-dense pathway is authored.

### 8.1 Three-tab text-only (Writing-cycle-flavoured)

Parallel writing stages presented as tabs.

```json
{
  "_component": "tabs",
  "_layout": "full",
  "displayTitle": "The writing stages",
  "body": "<p>These three stages follow understanding the task. Each has a different focus.</p>",
  "instruction": "Select each tab to explore what the stage involves.",
  "_items": [
    {
      "tabTitle": "Planning",
      "title": "The planning stage",
      "body": "<p>Planning is about deciding what you'll say and in what order. A clear plan means you're not trying to invent your argument and your sentences at the same time.</p><p>Your plan doesn't need to be perfect — it's a thinking tool, not a contract. Expect to revise it as you read more and your ideas sharpen.</p>"
    },
    {
      "tabTitle": "Drafting",
      "title": "The drafting stage",
      "body": "<p>The first draft gets your ideas down roughly. Its job is to turn your plan into prose, not to be perfect. A draft you can improve is worth far more than a blank page.</p><p>If you get stuck on a sentence, move on. You can come back to it. Staying stuck is the trap; moving on is the release.</p>"
    },
    {
      "tabTitle": "Editing",
      "title": "The editing stage",
      "body": "<p>Editing is where you shape your draft into something that makes a clear argument. This is not the same as proofreading: editing is about substance, not just surface errors.</p><p>Read your draft asking: does each paragraph do one job? Do the paragraphs connect? Is the argument visible?</p>"
    }
  ]
}
```

**How it satisfies the spec:** three tabs (guardrail 1); tab titles are concise (guardrail 2); content is parallel in structure and weight (guardrail 3); order doesn't matter — these are stages but the learner doesn't need to read them sequentially here (guardrail 4); each panel is self-contained (guardrail 5).

### 8.2 Four-tab with optional graphics

Approaches to structuring an essay, with optional images.

```json
{
  "_component": "tabs",
  "_layout": "full",
  "displayTitle": "Essay structures",
  "body": "<p>Different disciplines favour different essay structures. Here are four common patterns.</p>",
  "instruction": "Select each tab to see the structure.",
  "_items": [
    {
      "tabTitle": "Thesis-led",
      "title": "Thesis-led structure",
      "body": "<p>State your argument upfront, then support it with evidence. Common in humanities essays where you're defending a position.</p><p>Structure: Introduction with thesis, paragraphs supporting the thesis, conclusion restating the thesis with implications.</p>"
    },
    {
      "tabTitle": "Problem-solution",
      "title": "Problem-solution structure",
      "body": "<p>Define a problem, then propose and evaluate solutions. Common in social sciences and professional contexts.</p><p>Structure: Introduction defining the problem, analysis of causes, proposed solutions, evaluation of trade-offs, conclusion with recommendations.</p>"
    },
    {
      "tabTitle": "Comparative",
      "title": "Comparative structure",
      "body": "<p>Compare two or more things systematically. Common when evaluating theories, methods, or case studies.</p><p>Structure: Introduction with basis for comparison, point-by-point or block comparison, synthesis of findings, conclusion with judgement.</p>"
    },
    {
      "tabTitle": "Chronological",
      "title": "Chronological structure",
      "body": "<p>Present content in time order. Common in historical analysis or process descriptions.</p><p>Structure: Introduction establishing the timeframe, sequential sections by period, conclusion drawing together the narrative.</p>"
    }
  ]
}
```

**How it satisfies the spec:** four tabs (guardrail 1 maximum); tab titles are concise single words (guardrail 2); content is parallel — each describes a structure with the same elements (guardrail 3); order doesn't matter — these are alternatives, not a sequence (guardrail 4); each panel is self-contained (guardrail 5).

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **tabs** component. Its build rationale (build-own ladder entry, TA-1 design, TS-1–6 build) lives in `open-decisions.md`; register and voice live in the **Voice Specification**; component-to-pedagogy mapping lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of tabs authoring spec — v0.1.*
