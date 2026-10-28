# references — Authoring Spec

**Version:** 0.1
**Status:** draft (F4 spec)
**Verified against:** `src/components/adapt-abbott-references/properties.schema` — **our own schema** (custom component)
**Grounded in:** `W-CLOSE-c-15` — the "Further reading" block in the Academic Writing / Introductory Stage wrapper close (`courses/academic-writing-introductory`)
**Relationship to other documents:** references the Voice Specification, RF-1–4 (open-decisions.md), PLR-1 (open-decisions.md); restates none. This doc is the single source for how to author a references component.

---

## 1. Purpose & when to reach for it

A **presentational list of curated further-reading references** — links to book sections, external resources, or library permalinks that extend the lesson or tier. Not a runtime-scanned aggregation (RF-2); each reference is hand-authored.

- **Reach for references** when RF-4's reference-worthiness test is met: the book or resource offers additional or more extensive discussion beyond what the lesson itself provides. The component renders a structured list with consistent styling, new-tab behaviour, and optional library permalinks.
- **Don't use references** for inline cross-references to other lessons or pages (→ use the Cross-reference teaching move, an inline anchor), for navigation (→ standard Adapt navigation), or for sources the lesson already restates in full (no new value).

### Placement (PLR-1)

Per PLR-1 (#34, open-decisions.md):

- **Per-lesson references** (PLR-1b): a content-dependent block at the end of individual lessons — after Summary, after Reflective prompt. Author when the lesson is genuinely rooted in specific book material.
- **W-CLOSE course-level references** (PLR-1a): retained but variable/optional per pathway. Explicitly titled to signal course scope ("Further reading for this tier"). Not assumed mandatory; decided at Stage 1 design per pathway.

---

## 2. The annotated JSON shape

Skeleton below is the authoring-relevant field set. **[LB]** marks a *load-bearing* field.

```jsonc
{
  "_id": "W-CLOSE-c-15",          // lesson-key convention; see portable-unit-and-shell-format.md
  "_parentId": "W-CLOSE-b-15",    // the block this sits in
  "_type": "component",
  "_component": "references",
  "_classes": "",
  "_layout": "full",              // full-width standard

  "title": "Further reading",     // internal tracking title
  "displayTitle": "Further reading", // learner-facing heading
  "body": "",                     // optional body text; usually blank
  "instruction": "If you'd like to go deeper on any of this tier's topics, this is worth a look.", // [LB] see §4

  "_items": [                     // [LB] the reference list
    {
      "title": "Excelling at University, Chapter 8: Writing critically, 'The language of criticality'", // [LB] display text
      "href": "https://research-ebsco-com.ezproxy.cardiffmet.ac.uk/plink/a270c888-61a1-3ba3-a15e-30ce2cc1578d", // [LB] clickable URL
      "type": "book",             // [LB] category label (see §3)
      "permalink": ""             // optional library permalink (see §3)
    }
    // …remaining items
  ],

  "_pageLevelProgress": {
    "_isEnabled": true,
    "_isCompletionIndicatorEnabled": false  // reference list doesn't drive completion indicator
  }
}
```

---

## 3. Authoring guardrails (hard rules)

1. **RF-4 reference-worthiness.** Only include a reference where the book or resource offers additional or more extensive discussion beyond what the lesson itself already provides. A reference is not warranted merely because content was sourced from that chapter — the test is whether a student would gain something *new* by following the link.

2. **Item shape per RF-3.**
   - `title` (required): display text — typically "Excelling at University, Chapter N: [Title], '[Section]'" for book references.
   - `href` (required): clickable URL to the resource. Use `#` as a placeholder if the real URL is not yet confirmed; a draft with `#` should not ship live (PLR-1d).
   - `type` (required): free-text category, e.g. `"book"` or `"external"`. Not a locked enum — add new values when a real instance needs distinguishing, but don't enumerate in advance.
   - `permalink` (optional): a university library catalogue permalink for the same resource, independent of `href`, not a fallback. Both render when both exist; omit when absent.

3. **Never fabricate hrefs.** Every `href` must point to a real, accessible resource. References are tracked in `book-sourcing-log.md` during authoring; URLs are sourced in a batched consolidation step per PLR-1d — not invented during generation.

4. **New-tab behaviour.** Links open in a new tab by default (component behaviour). This is intentional — the learner stays in the course and can return. Do not override.

5. **No score, no assessment.** This is a presentational component. It does not participate in assessment, does not track interaction, and completion is on inview.

---

## 4. Voice rules (reference — not restated here)

| Field | Content type | Voice Spec |
|---|---|---|
| `displayTitle` | Section heading | §14 (heading register) |
| `instruction` | Activity instruction — optional orienting line | §15.4 |
| `_items[].title` | Reference citation — formal, complete | §15.6 (formal register, no contractions) |

The `instruction` field uses mid-register, direct student address — contractions permitted. Reference titles (`_items[].title`) use formal register: no contractions, complete citation form.

---

## 5. Tier-dependent guidance

The references component is **tier-neutral** in structure. Tier applies only to *which* references are selected:

- **Introductory**: foundational chapters, introductory material.
- **Intermediate**: chapters with deeper analysis or broader application.
- **Advanced**: specialist sections, advanced technique, external scholarly resources.

The component structure, rendering, and behaviour do not change by tier.

---

## 6. Accessibility requirements

- **Meaningful link text.** `_items[].title` must be descriptive enough to convey the destination without surrounding context — screen-reader users navigating by links should understand where each link goes.
- **New-tab announcement.** The component should announce that links open in a new tab (handled by component template).
- **No images in items.** References are text links only; no visual discrimination required.

---

## 7. Known gotchas & findings

- **`href: "#"` is a draft marker.** A reference with `href: "#"` is not ready for production. The PLR-1d workflow requires a consolidation step where real URLs are sourced in batch. Lint or review should flag any `#` before packaging.
- **`type` is not an enum.** The schema accepts any string. Current values: `"book"`, `"external"`. Add new values when genuinely needed; don't pre-enumerate.
- **`permalink` is independent.** When present, it renders alongside `href` as a separate link (e.g. "Library permalink"), not as a fallback. Don't use it as an alternative URL for the same target — use it for a catalogue entry.
- **Completion is on inview.** The component completes when scrolled into view, regardless of whether any link is clicked. This is intentional — further reading is supplementary.

---

## 8. Worked example

`W-CLOSE-c-15`, the real authored course-level references block from Academic Writing / Introductory wrapper close. Reproduced in full.

```json
{
  "_id": "W-CLOSE-c-15",
  "_parentId": "W-CLOSE-b-15",
  "_type": "component",
  "_component": "references",
  "_classes": "",
  "_layout": "full",
  "title": "Further reading",
  "displayTitle": "Further reading",
  "body": "",
  "instruction": "If you'd like to go deeper on any of this tier's topics, this is worth a look.",
  "_items": [
    {
      "title": "Excelling at University, Chapter 8: Writing critically, 'The language of criticality'",
      "href": "https://research-ebsco-com.ezproxy.cardiffmet.ac.uk/plink/a270c888-61a1-3ba3-a15e-30ce2cc1578d",
      "type": "book"
    },
    {
      "title": "Excelling at University, Chapter 9: Writing in practice, 'The writing cycle'",
      "href": "https://research-ebsco-com.ezproxy.cardiffmet.ac.uk/plink/79b8cbe3-b278-3b91-9a7d-f9758a386ae3",
      "type": "book"
    }
  ],
  "_pageLevelProgress": {
    "_isEnabled": true,
    "_isCompletionIndicatorEnabled": false
  }
}
```

**How it satisfies the spec:**

- **Guardrail 1 (RF-4)** — both references point to book sections that extend the tier's topics beyond what the lessons cover in full.
- **Guardrail 2 (RF-3)** — item shape complete: `title`, `href`, `type`. No `permalink` needed (EBSCO link is direct access).
- **Guardrail 3** — hrefs are real EBSCO permalinks, not placeholders.
- **§4 voice** — instruction uses mid-register with contractions ("you'd"); reference titles are formal complete citations.
- **§5 tier** — introductory tier; foundational book chapters selected.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **references** component. The reference-worthiness test and sourcing workflow are defined in **RF-1–4 and PLR-1** (open-decisions.md); register and content-type voice live in the **Voice Specification**; the `_id` conventions live in **`portable-unit-and-shell-format.md`**. This doc points to them; it does not restate them.

---

*End of references authoring spec — v0.1.*
