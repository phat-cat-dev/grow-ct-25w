# W-CLOSE (Wrapper Close) Template

> **DRAFT v1** — based on Academic Writing: Introductory Stage instance only
> (28 July 2026). Does NOT yet incorporate all design decisions from the 28
> July P8 walkthrough. See `template-v2-scope.md` for the full list of items
> queued for a v2 pass. **Needs a v2 pass before being treated as authoritative.**
>
> **Change note (13 August 2026):** Block 1 (Confidence POST) removed per CC-1;
> POST now lives on the dedicated C-POST page. Two new blocks added per WC-1:
> practice connection and where-this-goes-next. See `c-post-template.md`.
>
> **SKS-1 note (20 September 2026):** Per SKS-1, the skeletons store is
> the single source of truth for structure; this template is an authoring
> guide pointing at it. Prompt 134's nesting audit (Task 5) named 3
> disagreements for this template: (1) the Further reading block's
> classification and settings example still describe it as
> variable/optional recommendation reading, superseded by the W3 ruling
> and the PLR-1 AMENDMENT, which made it required and changed its
> function to the mandatory full bibliography of every source any lesson
> in the course cites; (2) the block is titled "Course Sources" in one
> place and "Further reading" in another within this same file, and only
> "Course Sources" matches the store's live title; (3) the retrofit
> (`b-20`/`b-25`) vs new-course (`b-10`/`b-15`) dual `_id` numbering
> documented here carries a collision risk against `course-references`'s
> own `b-15`, not yet a live collision but a risk in the scheme as
> written. Where this template and the store disagree, the store is
> authoritative.

Reference template for the Wrapper Close page that wraps up every pathway-tier.
This page exists as a single instance per tier (unlike content lessons, which
repeat a pattern).

See also:
- `open-decisions.md` WR-1–4 (wrapper architecture)
- `open-decisions.md` WR-2 (confidence-at-wrapper mechanics — amended by CC-1)
- `open-decisions.md` CC-1 (confidence pages), WC-1 (W-CLOSE enrichment)
- `open-decisions.md` RF-1–4 (references component)
- `c-pre-template.md` (C-PRE page — confidence PRE)
- `c-post-template.md` (C-POST page — confidence POST relocated here)
- `wrapper-open-template.md` (W-OPEN page)
- `summative-template.md` (SUMM page)
- `lesson-structure-template.md` (content lesson structure)

---

## Overview

| Field | Value |
|-------|-------|
| Page ID | `W-CLOSE-co-01` |
| Role | Wrapper Close — course summary, practice connection, what's next, further reading |
| Position | Last page: W-OPEN → C-PRE → lessons → SUMM → C-POST → **W-CLOSE** |
| Menu numbering | Unnumbered (28 July decision) |

*Ids are generated per ID-1; ids shown here are illustrative.*

---

## Structure Summary

```
W-CLOSE-co-01 (page, _classes: "{{pathwaySlug}} wrapper-close")
└── W-CLOSE-a-01 (article)
    ├── W-CLOSE-b-10: Course summary [text]
    ├── W-CLOSE-b-20: Practice connection [text]        ← NEW (WC-1b-i)
    ├── W-CLOSE-b-25: Where this goes next [text]       ← NEW (WC-1b-ii)
    └── W-CLOSE-b-15: Further reading [references]
```

**Block 1 (Confidence POST, `W-CLOSE-b-05`) is REMOVED** — relocated to
C-POST (see `c-post-template.md`).

**ID and ordering note:** existing block IDs `b-10` (summary) and `b-15`
(references) are retained to minimise retrofit churn on tested content;
the two new blocks take fresh IDs (`b-20`, `b-25`) and are ordered by
array position in `blocks.json`, not by ID sequence. Rendering order is
the structure summary above: summary → practice connection → what's next
→ further reading. For NEW courses built from this template, clean gapped
IDs in rendering order are preferred (`b-05` summary, `b-10` practice
connection, `b-15` what's next, `b-20` further reading).

---

## Content Object

```json
{
  "_id": "W-CLOSE-co-01",
  "_parentId": "course",
  "_type": "page",
  "_classes": "{{pathwaySlug}} wrapper-close",
  "title": "{{Pathway}}: {{Tier}} Stage, wrap-up",
  "displayTitle": "Wrap-up",
  "body": "A summary of what you've covered, how it connects to real academic practice, where this pathway goes next, and further reading.",
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
  "_id": "W-CLOSE-a-01",
  "_parentId": "W-CLOSE-co-01",
  "_type": "article",
  "title": "Wrap-up"
}
```

---

## Blocks

### Block 1: Confidence POST — REMOVED

**Confidence POST:** relocated to the dedicated C-POST page per CC-1 —
see `c-post-template.md`. The `_selfAssessmentGroupId` pairing is now
between C-PRE and C-POST.

---

### Block 2: Course summary

**Classification:** Tier-specific content, fixed structure

Per WR-1c.

| Field | Value |
|-------|-------|
| Block ID | `W-CLOSE-b-10` |
| Block title | "Course summary" |
| Component | `text` |
| Voice | §15.10 (practice-level overview) |

**Content:** 2 paragraphs — what was covered, habits to carry forward.
TIER-SPECIFIC.

**AL-5 (`open-decisions.md`):** this summary tells the student what they
can now do, outcome by outcome against the course outcomes stated on
W-OPEN's Learning outcomes block, connects each to how they will use it
in their studies, and refers to the confidence shift the student has
just seen on C-POST. The "what was covered, habits to carry forward"
content above is necessary but not sufficient for AL-5: it must be
outcome-by-outcome, not a general summary, and it must reference the
C-POST confidence comparison, not only the course content.

---

### Block 3: Practice connection (WC-1b-i)

**Classification:** Tier-specific content, fixed structure

How the tier's learning relates to actual academic practice — the
outward-facing counterpart to W-OPEN's "why this matters" overview:
W-OPEN argues relevance prospectively; this block demonstrates it
retrospectively, now the learner has the substance to connect.

| Field | Value |
|-------|-------|
| Block ID | `W-CLOSE-b-20` (retrofit) / `b-10` (new courses) |
| Block title | "In real academic practice" |
| Component | `text` |
| Voice | §15.10 (practice-level overview, WR-4) |

**Content:** 1–2 paragraphs. This block carries a coupled slot under
CP-1i: it becomes a variable block, not a fixed one. What the practice
looks like when actually used: in assessment, in module work, beyond
university. TIER-SPECIFIC.

---

### Block 4: Where this goes next (WC-1b-ii)

**Classification:** Tier-specific content, fixed structure

Forward signposting to the next tier where one exists.

| Field | Value |
|-------|-------|
| Block ID | `W-CLOSE-b-25` (retrofit) / `b-15` (new courses) |
| Block title | "Where this goes next" |
| Component | `text` |
| Voice | §15.10 (practice-level overview) |

**Content shape:** 1 short paragraph naming what the next tier covers.
Per WC-1c, what is signposted forward is precisely what gate A2's
tier-band scoping **held back** from this tier — authored per tier at the
A2/W1 gates, never boilerplate. Example (Academic Writing Introductory):
"Techniques for enhancing your writing" (expression, structure, sources),
held to the intermediate stage and already alluded to via the Common
errors lesson's Cross-reference.

**Terminal-tier rule:** where no next tier exists (advanced), this block
is OMITTED, not filled with filler — the template's fixed structure is
"present where a next tier exists".

---

### Block 5: Further reading

**Classification:** Variable/optional per-pathway (per PLR-1), tier-specific items when present

Per RF-1–4, amended by PLR-1.

| Field | Value |
|-------|-------|
| Block ID | `W-CLOSE-b-15` |
| Block title | "Course Sources" |
| Component | `references` |
| displayTitle | "Course Sources" |

**Icon:** Mandatory (when block is present) per theme build — see
`template-v2-scope.md` #22.

**Settings:**
```json
{
  "instruction": "If you'd like to go deeper on any of this course's topics, this is worth a look.",
  "_items": [
    // TIER-SPECIFIC curated list
    {
      "title": "{{Resource title}}",
      "href": "{{URL}}",
      "type": "book"  // or "article" or "external"
    }
  ]
}
```

**28 July decision:** Links must open in new tab (not within SCORM package).
Implementation: ensure component renders links with `target="_blank"` or
equivalent.

**Content note (20 September 2026, ST-1):** Displayed title changed from
"Further reading for this course" to "Course Sources", matching the
design-kb skeleton's `course-references` block title. See
`open-decisions.md` ST-1.

---

## Cross-Reference: Confirmed Decisions

| Decision | Status | Notes |
|----------|--------|-------|
| WR-1a | Confirmed | Naming W-OPEN / W-CLOSE |
| WR-1c | Confirmed | W-CLOSE structure (amended by CC-1/WC-1) |
| WR-1d | Confirmed | ID convention |
| WR-2b | Superseded by CC-1 | POST now on C-POST, still before W-CLOSE in sequence |
| WR-2d | Confirmed | Five-pattern feedback — now on C-POST; see `c-post-template.md` |
| CC-1 | Confirmed | Confidence relocated to C-PRE/C-POST pages |
| WC-1a | Confirmed | W-CLOSE keeps closing role |
| WC-1b | Confirmed | Two new blocks: practice connection, where this goes next |
| WC-1c | Confirmed | Signposting mirrors A2's held-back scope; per-tier authored |
| WC-1d | Confirmed | References unchanged, still pending PLR-1 |
| RF-1 | **Amended by PLR-1** | W-CLOSE course-level reading block retained but (a) explicitly titled for course-level scope ("Further reading for this course"), (b) now variable/optional per-pathway (same palette logic as VO-1), not assumed mandatory. Per-lesson references are a separate, new block in `lesson-structure-template.md`. See `open-decisions.md` #34 (PLR-1, RESOLVED). |
| RF-3 | Confirmed | Item shape (title/href/type) |

---

## Open Questions

See `template-v2-scope.md` for the full list of items queued for a v2 pass.

Key open items affecting W-CLOSE:
- **"Completed activity" chrome:** feature request for theme pass
- **PLR-1 disposition** still open and now interacts with WC-1: if
  references go per-lesson, W-CLOSE's Further reading block may become a
  course-level "further reading" summary or be removed — resolve at the
  V2 template consolidation.
- **Confidence 5-option row overflow:** moved to the C-page templates (CRO-1
  fix landed; verify during CC-1e retrofit)
