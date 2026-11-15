# timeline (adapt-abbott-timeline) — Authoring Spec

**Version:** 0.1
**Status:** draft — ships with the component (built 31 July 2026). No authored lesson instance yet; the worked example is **build-verified** (rendered and behaviour-confirmed via browser checks including Playwright accessibility-tree verification, 31 July 2026) but no shipped instance — first real instance lands when a Signpost process overview or temporal content lesson is authored.
**Verified against:** `src/components/adapt-abbott-timeline/properties.schema` — **our own schema** (custom component; no `example.json`).
**Relationship to other documents:** this component's build rationale lives in `open-decisions.md` (#36 build-own ladder, TL-1–7 design, TB-1–6 build). This spec references the Voice Specification and `design-kb/design-kb.activity-patterns.json` (component-mapping-artefact.md is SUPERSEDED, MA-1); it restates neither.

---

## 1. Purpose & when to reach for it

A **vertical ordered-process display**: stages along a marked axis, whole process visible at once, per-stage detail expanding in place. **Ordinal, not scalar** — stages render at equal spacing in authored order; there is no date arithmetic or time-proportional spacing.

**Not a question component.** No marking, no correct answer, no `_recordInteraction`, no response semantics. Completion by visiting all stages — expand each stage at least once.

**Two usage registers** (VO-1 Signpost palette, treatment 3):

1. **Signpost process overview** — staged, linear processes where order matters but the process is not cyclical (e.g. the research process, the writing cycle). The timeline shows the shape of the whole before the learner works through it.
2. **Temporal content** — time-bound sequences in pathways like Revising & Exams, Researching, or Work-Based Learning (e.g. "Week 1 → Week 8" project milestones).

Reach for it when:
- A **linear process** benefits from spatial overview — learner sees all stages at once
- **Sequence matters** but the process is not cyclical
- Per-stage detail is substantial enough to collapse/expand rather than show inline
- Content is **text-driven** — no image substrate is required

Do not use it when:
- The process is **cyclical** (use `hotgraphic` with a cycle diagram)
- You need an **image substrate** with positioned hotspots (use `hotgraphic`)
- Learners should **construct** the order, not receive it (use `sortable`)
- The content is a **plain expandable stack** without sequence semantics (use `accordion`)
- A **one-at-a-time narrative** is more appropriate than whole-at-once overview (use `narrative`)

**Context-overlay compatible:** all learner-visible text lives in the swappable JSON fields; no baked-in copy.

---

## 2. The annotated JSON shape

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `_component: "timeline"` | yes | — | Lowercase — the registered component name. |
| `displayTitle` | recommended | — | Student-facing heading. |
| `body` | optional | — | Introductory text above the timeline. |
| `instruction` | recommended | — | "Select each stage to reveal its details." or similar. |
| `_expandBehaviour` | no | `"single"` | `"single"` (default): expanding one stage collapses others — keeps the overview scannable. `"independent"`: stages expand and stay individually. **Note:** default is `"single"`, deliberately inverted from flipcard's `"independent"` (TL-4). |
| `_items[]` | yes | — | Array of stage objects (see below). |

**Each `_items[]` entry:**

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `label` | **yes** | — | Axis marker text. Free text — serves both "Stage 1" and "Week 3" registers. Displayed in the circular marker on the timeline axis. |
| `title` | **yes** | — | Stage title displayed next to the marker. Combined with `label` for the accessible name. |
| `body` | optional | — | Detail content revealed when the stage is expanded. Supports HTML. |
| `_graphic.src` | optional | — | Image path (relative to course assets) displayed in the expanded detail. |
| `_graphic.alt` | if graphic | — | Alt text for the image. Leave blank if decorative and body/title provides context. |

**No `_id` field per item.** Items are index-keyed (TB-3) — persistence uses array position, not explicit ids. See guardrail 7 for implications.

Globals (`ariaRegion`) carry sensible defaults; override only for wording.

---

## 3. Authoring guardrails (hard rules)

1. **Label and title are required.** Every stage must have both `label` (axis marker) and `title`. A missing label renders as empty marker; a missing title renders as blank — both are authoring errors.

2. **Keep stage counts in 3–8 range.** Fewer than 3 stages rarely justifies the timeline overhead (use text or accordion). More than 8 loses the overview benefit and crowds the axis.

3. **Ordinal only — no date arithmetic.** The timeline renders stages at equal spacing in authored order. If proportional time spacing is essential, the component is not a fit. Do not author "Week 1, Week 2, Week 8" expecting visual time-proportionality.

4. **Use `_expandBehaviour: "single"` (the default) for process overviews.** When stages represent a sequence learners will work through, single mode keeps the overview scannable. Use `"independent"` only when multiple details need simultaneous comparison.

5. **Image in detail is optional.** A stage can have body only, body + graphic, or graphic only. If the stage has no body and no graphic, the detail region is empty — avoid this unless the marker + title is self-sufficient.

6. **Completion requires all stages expanded.** The learner must expand every stage at least once; completion fires when the last stage is visited. Stages can be collapsed and re-expanded without penalty.

7. **Index-keyed persistence.** The base class stores visitation as an index-sorted boolean array. Reordering `_items` between sessions breaks restoration. If you must reorder, expect learners to see partial completion reset.

8. **Vertical layout only (v1).** This version implements vertical-only layout. Horizontal orientation is deferred pending a demonstrated need (TB-5 / TL-2).

---

## 4. Voice rules (reference — not restated here)

Presentational throughout — no feedback or scoring copy to voice.

| Field | Content type | Voice Spec |
|-------|--------------|------------|
| `label` | Ordinal marker or time reference | Concise (1–2 words): "1", "Stage 2", "Week 3" |
| `title` | Stage heading | Crisp noun phrase or action heading (§11 clarity) |
| `body` | Stage detail/explanation | Mid-register, explain the *why* (§4), appropriate to tier (§16) |
| `instruction` | Activity instruction | §15.4 |

Contractions follow the lesson context (§11.2) — usually yes for mid-lesson teaching, no for learning-outcome-adjacent content.

---

## 5. Tier-dependent guidance

The component is **not graded**, so the Tier Spec's assessment dimension does not apply. Tier lands in:

- **Detail depth.** Introductory stage bodies may include more scaffolding; intermediate/advanced can assume prior knowledge.
- **Stage count.** Introductory lessons typically 3–5 stages; advanced can stretch to 6–8 without losing focus.
- **Vocabulary complexity.** Titles and body text scale with tier expectations per the Tier Spec.

The expand/collapse interaction itself is tier-neutral — the mechanic is self-paced and non-threatening at all levels.

---

## 6. Accessibility requirements

- **`<ol>` with `<li>` per stage** — sequence semantics live in the HTML list structure, not just visual presentation.
- **Each stage marker is a native `<button>`** with `aria-expanded` reflecting expand state. Keyboard operation is Enter/Space to toggle, Tab to move between stages.
- **Accessible name = label + title**, static across expand/collapse. The button's `aria-label` is `"${label}: ${title}"` (e.g. "1: Identify your question"). It does not change when the stage expands.
- **`aria-controls` links button to detail region.** Each button has `aria-controls="${componentId}-stage-${index}-detail"` pointing to the corresponding detail region's `id`. The linked region exists in DOM; it is revealed/hidden via `aria-hidden` and CSS.
- **Detail region always in DOM; `aria-hidden` when collapsed.** The detail `<div>` is present regardless of expand state; `aria-hidden="true"` when collapsed, `aria-hidden="false"` when expanded.
- **No focus movement on expand.** Focus stays on the button; the expand is a state change, not navigation.
- **`ariaRegion` introduces the interaction** at component level (defaults to "Timeline. Select each stage to reveal its details.").
- **Reduced motion.** CSS includes `@media (prefers-reduced-motion: reduce)` — transitions fall back to instant swap, no animation. *(Deferred to the strategic accessibility-verification pass for live confirmation.)*

---

## 7. Known gotchas & findings

- **`_component` is `"timeline"`** (lowercase), not the plugin directory name.
- **Default is `"single"` mode** — unlike flipcard which defaults to `"independent"`. This is deliberate (TL-4): process overviews benefit from one-at-a-time focus.
- **Completion = visitation, not collapse.** A stage is "visited" when expanded the first time; collapsing doesn't unvisit. All stages must be visited for completion.
- **`_isExpanded` is transient, not persisted.** On revisit, all stages present collapsed. Completion status persists via the base class's `_userAnswer` boolean array; the expand state itself does not.
- **Vertical axis as CSS pseudo-element.** The connecting line is pure decoration (`::before` on the `<ol>`); it carries no semantic meaning the list structure doesn't already provide.
- **No `example.json`** — this spec's worked example is the reference.

---

## 8. Worked example (BUILD-VERIFIED — no shipped instance yet)

Two instances: a single-mode staged-process overview (Signpost register) and an independent-mode temporal sequence with graphic (content-lesson register). **Build-verified** — rendered and behaviour-confirmed via Playwright accessibility-tree checks (31 July 2026); the first real instance is authored when a pathway-tier design session calls for it per VO-1.

### 8.1 Single-mode staged process (Signpost register)

```json
{
  "_component": "timeline",
  "_layout": "full",
  "displayTitle": "The research process",
  "body": "<p>A five-stage overview of the research process, from identifying your question to presenting your findings. Select each stage to see what it involves.</p>",
  "instruction": "Select each stage to reveal its details.",
  "_expandBehaviour": "single",
  "_items": [
    {
      "label": "1",
      "title": "Identify your question",
      "body": "<p>Every research project starts with a question worth answering. At this stage you're defining what you want to find out and why it matters, which shapes everything that follows.</p>"
    },
    {
      "label": "2",
      "title": "Review existing literature",
      "body": "<p>Before gathering new data, find out what's already known. A literature review shows where your work fits in the field and helps you avoid duplicating what others have done.</p>"
    },
    {
      "label": "3",
      "title": "Design your method",
      "body": "<p>Decide how you'll gather evidence to answer your question. Your method needs to be appropriate for what you're investigating and practical given your resources.</p>"
    },
    {
      "label": "4",
      "title": "Collect and analyse data",
      "body": "<p>Gather your evidence systematically and look for patterns. Keep careful records: you'll need to explain your process when you write up.</p>"
    },
    {
      "label": "5",
      "title": "Present your findings",
      "body": "<p>Communicate what you found and what it means. Connect your results back to your original question and the existing literature.</p>"
    }
  ]
}
```

**How it satisfies the spec:** five stages (guardrail 2); each has label + title (guardrail 1); each has body (guardrail 5 — no empty details); `_expandBehaviour: "single"` keeps overview scannable (guardrail 4); numbered labels form accessible names "1: Identify your question" etc. (§6).

### 8.2 Independent-mode temporal content with graphic

```json
{
  "_component": "timeline",
  "_layout": "full",
  "displayTitle": "Key milestones",
  "body": "<p>Independent-mode timeline with a graphic. Multiple stages can be open simultaneously.</p>",
  "instruction": "Select stages to explore. Multiple can be open at once.",
  "_expandBehaviour": "independent",
  "_items": [
    {
      "label": "Week 1",
      "title": "Project kickoff",
      "body": "<p>Initial meeting to establish scope, objectives, and team roles. Set up communication channels and agree on deliverables.</p>",
      "_graphic": {
        "src": "course/en/images/single-width.png",
        "alt": "Placeholder image for project kickoff milestone"
      }
    },
    {
      "label": "Week 4",
      "title": "First draft review",
      "body": "<p>Review the initial draft with stakeholders. Gather feedback and identify areas needing revision.</p>"
    },
    {
      "label": "Week 8",
      "title": "Final submission",
      "body": "<p>Submit the completed work. Ensure all requirements are met and documentation is complete.</p>"
    }
  ]
}
```

**How it satisfies the spec:** three stages (guardrail 2); each has label + title (guardrail 1); first stage includes graphic with alt text (guardrail 5); `_expandBehaviour: "independent"` allows multi-open for comparison; temporal labels "Week 1" etc. demonstrate the temporal-content register.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **timeline** component. Its build rationale (#36 build-own ladder, TL-1–7 design, TB-1–6 build) lives in `open-decisions.md`; register and voice live in the **Voice Specification**; component-to-pedagogy mapping lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1) (routing boundaries: vs hotgraphic for cyclical/image-substrate, vs narrative for one-at-a-time, vs sortable for construct-order, vs accordion for plain stack without sequence semantics). This doc points to them; it does not restate them.

---

*End of timeline authoring spec — v0.1.*
