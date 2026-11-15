# W-OPEN (Wrapper Open) Template

> **DRAFT v1** — based on Academic Writing: Introductory Stage instance only
> (28 July 2026). Does NOT yet incorporate all design decisions from the 28
> July P8 walkthrough. See `template-v2-scope.md` for the full list of items
> queued for a v2 pass. **Needs a v2 pass before being treated as authoritative.**
>
> **Change note (13 August 2026):** Block 4 (Confidence PRE) removed per CC-1;
> PRE now lives on the dedicated C-PRE page. See `c-pre-template.md`.
>
> **Change note (14 August 2026, two items):**
> 1. **Wording conformance fix:** W-OPEN-c-25 body changed from "this topic"
>    to "this course" per the 28 July decision already documented below. The
>    instance never conformed; the 14 Aug template-conformance audit (which
>    found block-order MATCH) missed this because structural conformance
>    checking does not catch wording drift. Drift-never-implemented, dated
>    to 28 July.
> 2. **Block reorder (new decision, supersedes WR-1b):** Learning outcomes
>    now render FIRST, before Overview and Signpost. Rationale: LOs set
>    expectations for the whole course; readers should encounter them
>    immediately. This supersedes WR-1b's original order (Overview →
>    Signpost → LOs). See `open-decisions.md` WR-1b annotation.
>
> **Change note (20 September 2026, CV-1):** New required block,
> "How this course works" (`W-OPEN-b-25`), added as the last block, after
> Signpost. Reuses the Block 5 ordinal previously held by the removed
> Confidence PRE block (13 August 2026 change note above). See
> `open-decisions.md` CV-1.
>
> **SKS-1 note (20 September 2026):** Per SKS-1, the skeletons store is
> the single source of truth for structure; this template is an authoring
> guide pointing at it. Prompt 134's nesting audit (Task 5) named 1
> disagreement for this template: the Signpost block's grammar
> description here (a "pattern-led triple") conflicts with the store's
> `signpost` slot, which the store describes as deliberately excluded
> from the activity-pattern layer. Already named as unresolved elsewhere
> (`gate-conversation-map.md`); carried here as a confirmed, still-open
> drift, not a new finding. Where this template and the store disagree,
> the store is authoritative.

Reference template for the Wrapper Open page that introduces every pathway-tier.
This page exists as a single instance per tier (unlike content lessons, which
repeat a pattern).

See also:
- `open-decisions.md` WR-1–4 (wrapper architecture)
- `open-decisions.md` WR-2 (confidence-at-wrapper mechanics — amended by CC-1)
- `open-decisions.md` CC-1 (confidence pages)
- `c-pre-template.md` (C-PRE page — confidence PRE relocated here)
- `c-post-template.md` (C-POST page — confidence POST)
- `summative-template.md` (SUMM page)
- `wrapper-close-template.md` (W-CLOSE page)
- `lesson-structure-template.md` (content lesson structure)

---

## Overview

| Field | Value |
|-------|-------|
| Page ID | `W-OPEN-co-01` |
| Role | Wrapper Open — introduces the tier, sets context |
| Position | First page: **W-OPEN** → C-PRE → lessons → SUMM → C-POST → W-CLOSE |
| Menu numbering | Unnumbered (28 July decision) |

*Ids are generated per ID-1; ids shown here are illustrative.*

---

## Structure Summary

```
W-OPEN-co-01 (page, _classes: "wrapper-open")
└── W-OPEN-a-01 (article)
    ├── W-OPEN-b-15: Learning outcomes [text]          ← FIRST (14 Aug reorder)
    ├── W-OPEN-b-05: Overview & justification [text]
    ├── W-OPEN-b-07: Practice connection [palette/text, coupled slot]
    ├── W-OPEN-b-10: Signpost [text + hotgraphic? + text]
    └── W-OPEN-b-25: How this course works [palette/text, fixed, furniture]
```

**Block order note (14 August 2026):** Learning outcomes now render first,
before Overview and Signpost. Supersedes WR-1b's original order. IDs unchanged.

**Block order note (19 September 2026, CP-1i / Prompt 116):** New
`practice-connection` block (`W-OPEN-b-07`) added directly after Overview and
before Signpost, per CP-1i (`open-decisions.md`). Variable block, coupled
(`whole-prose`) slot. Existing block IDs unchanged; heading numbers below run
1-5 in render order.

**Block order note (20 September 2026, CV-1):** New `course-conventions`
block (`W-OPEN-b-25`) added as the last block, after Signpost. Fixed block,
coupling `none`. See `open-decisions.md` CV-1.

**Block 5 (Confidence PRE, `W-OPEN-b-20`) REMOVED** — relocated to C-PRE per CC-1.

---

## Content Object

```json
{
  "_id": "W-OPEN-co-01",
  "_parentId": "course",
  "_type": "page",
  "_classes": "{{pathwaySlug}} wrapper-open",
  "title": "{{Pathway}}: {{Tier}} Stage",
  "displayTitle": "{{Pathway}}: {{Tier}} Stage",
  "body": "{{TIER-SPECIFIC: Menu blurb describing tier purpose. No internal terminology ('tier' etc.) — use reader-facing language.}}",
  "duration": "10 mins",
  "_pageLevelProgress": {
    "_isEnabled": true,
    "_showPageCompletion": true
  }
}
```

---

## Article

```json
{
  "_id": "W-OPEN-a-01",
  "_parentId": "W-OPEN-co-01",
  "_type": "article",
  "title": "{{Pathway}}: {{Tier}} Stage"
}
```

---

## Blocks

### Block 1: Learning outcomes

**Classification:** Tier-specific content, fixed structure

Course-level synthesis outcomes. **Renders first** (14 August 2026 reorder,
superseding WR-1b's original position 3).

| Field | Value |
|-------|-------|
| Block ID | `W-OPEN-b-15` |
| Block title | "Learning outcomes" |
| Component | `text` |
| displayTitle | "Learning outcomes" |

**Content shape:**
```html
<p>By the end of this course, you will be able to:</p>
<ul>
  <li>{{outcome 1}}</li>
  <li>{{outcome 2}}</li>
  <li>{{outcome 3}}</li>
</ul>
```

**28 July decision:** Wording is "in this course" not "in this topic" — these
are course-level outcomes, not lesson-level. **Conformance note (14 August
2026):** The Academic Writing instance's wording was fixed from "this topic"
to "this course" as a conformance fix — the instance never conformed to this
28 July decision, and the 14 Aug structural audit missed it.

---

### Block 2: Overview & justification

**Classification:** Tier-specific content, fixed structure

Why this practice matters — the cross-module/career relevance argument.

| Field | Value |
|-------|-------|
| Block ID | `W-OPEN-b-05` |
| Block title | "Overview and justification" |
| Component | `text` |
| Voice | §15.10 (practice-level overview, WR-4) |

**Content:** 1-2 paragraphs explaining why this practice matters. TIER-SPECIFIC.

**AL-5 (`open-decisions.md`):** this is where AL-5's "why they matter for
the student's own studies" half is answered. The overview's justification
argument connects to the course outcomes stated in Block 1, not only to
the practice in the abstract.

---

### Block 3: Practice connection

**Classification:** Variable content, context-coupled slot (CP-1i)

A short passage on what the tier means in the student's discipline.

| Field | Value |
|-------|-------|
| Block ID | `W-OPEN-b-07` |
| Block title | "In real academic practice" |
| Component | `palette/text` |
| Slot type | `practice-connection` |
| Context coupling | `whole-prose` |

**Content note (19 September 2026, CP-1i):** This block carries a coupled
slot under CP-1i. Its content is a short passage on what the tier means in
the student's discipline. Shares its key with skeletons/wrapper-close's
`practice-connection` block; see `open-decisions.md` CP-1i AMENDMENT.

---

### Block 4: Signpost

**Classification:** Mixed — text slots are generic; visual overview selected per-pathway from VO-1 palette

Pathway, tier, what's ahead.

| Field | Value |
|-------|-------|
| Block ID | `W-OPEN-b-10` |
| Block title | "Signpost" |
| Components | text + (visual treatment per VO-1) + text |

**Components in order:**
1. **text** — intro paragraph positioning this tier in the pathway
2. **visual overview** — See open-decisions.md #32 (VO-1, RESOLVED). Choose from
   the design palette: hotgraphic (cyclical/circular models), narrative (staged
   processes with per-stage visual identity), timeline (linear/staged non-circular
   processes — not yet built), flip cards (playful/interactive — not yet built),
   or text-only (deliberate choice where background imagery carries the page).
   Decision made once per pathway at Stage 1 design (mapping-artefact exercise).
3. **text** — continued prose listing the lessons ahead

---

### Block 5: How this course works

**Classification:** Fixed shell text, identical in every course (CV-1)

States the course's conventions: that examples and activities use invented
people, authors and sources unless stated otherwise, and where real sources
are listed.

| Field | Value |
|-------|-------|
| Block ID | `W-OPEN-b-25` |
| Block title | "How this course works" |
| Component | `palette/text` |
| Role | `furniture` |
| Interaction mode | `passive` |
| Coupling | `none` |

**Content:**

> The examples and activities in this course use invented people, authors
> and sources to show how things work. Unless we say otherwise, any name,
> citation or reference you meet in an example is fictional.
>
> Where a lesson draws on real work, you'll find it listed under **Lesson
> Sources** at the bottom of that page. Every real source used in the
> course is gathered under **Course Sources** at the end.

**Content note (20 September 2026, CV-1):** New required block, added as
the last block, after Signpost. Fixed shell text, identical in every
course. Adding one is a shell change Abbott rules, not a gate decision.
The per-example "illustrative" marking of fictional citations
(AUD-AWM-L05-3, 10 September 2026) stays alongside it. This ordinal
(Block 5) was previously held by the removed Confidence PRE block (see the
13 August 2026 change note above); the ordinal is reused here, not
renumbered, because Confidence PRE never rendered. See `open-decisions.md`
CV-1.

**Confidence PRE (historical):** relocated to the dedicated C-PRE page per
CC-1 — see `c-pre-template.md`. The `_selfAssessmentGroupId` pairing is now
between C-PRE and C-POST.

---

## Cross-Reference: Confirmed Decisions

| Decision | Status | Notes |
|----------|--------|-------|
| WR-1a | Confirmed | Naming W-OPEN / W-CLOSE |
| WR-1b | **Superseded 14 Aug** | Block order changed: LOs now first (b-15 → b-05 → b-10). See `open-decisions.md`. |
| WR-1d | Confirmed | ID convention |
| WR-2a | Confirmed (amended host) | Confidence items curated, cap 10 — now on C-PRE |
| WR-2b | Superseded by CC-1 | PRE now on C-PRE page |
| CC-1 | Confirmed | Confidence relocated to C-PRE/C-POST pages |

---

## Open Questions

See `template-v2-scope.md` for the full list of items queued for a v2 pass.

Key open items affecting W-OPEN:
- **Visual overview in Signpost:** open-decisions.md #32 (VO-1) — not all
  pathways may have a hotgraphic; evaluate per-pathway
- **Confidence 5-option row overflow:** moved to the C-page templates (CRO-1
  fix landed; verify during CC-1e retrofit)
