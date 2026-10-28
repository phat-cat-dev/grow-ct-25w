# C-PRE (Confidence Pre) Template

> **DRAFT v1** — drafted 13 August 2026 from CC-1 (open-decisions.md),
> claude.ai planning sessions 4 and 13 August 2026. No built instance yet;
> the Academic Writing: Introductory Stage retrofit (CC-1e) will be the
> first. **Validate against that retrofit before treating as authoritative.**
>
> **SKS-1 note (20 September 2026):** Per SKS-1, the skeletons store is
> the single source of truth for structure; this template is an authoring
> guide pointing at it. Prompt 134's nesting audit (Task 5) named 1
> disagreement for this template: the block title given here
> ("Confidence PRE") does not match the store's live title field for the
> same block ("Confidence check"). Cosmetic, not yet corrected. Where
> this template and the store disagree, the store is authoritative.

Reference template for the Confidence Pre page. This page exists as a single
instance per tier. It carries the confidence PRE check, relocated out of
W-OPEN per CC-1 — the learner rates themselves against the tier outcomes
they have just seen, immediately before the lessons begin.

See also:
- `open-decisions.md` CC-1 (confidence pages)
- `open-decisions.md` WR-2 (confidence mechanics — amended by CC-1, not discarded)
- `c-post-template.md` (C-POST page — paired instrument)
- `wrapper-open-template.md` (W-OPEN — precedes this page; Block 4 removed by CC-1)
- `lesson-structure-template.md` (content lesson structure)

---

## Overview

| Field | Value |
|-------|-------|
| Page ID | `C-PRE-co-01` |
| Role | Confidence Pre — baseline self-efficacy rating against tier outcomes |
| Position | Second page: W-OPEN → **C-PRE** → lessons → SUMM → C-POST → W-CLOSE |
| Menu numbering | Unnumbered (structural page, following the 28 July wrapper decision) |

*Ids are generated per ID-1; ids shown here are illustrative.*

**Why a dedicated page (CC-1a):** PRE is rated against outcomes the learner
has just seen in W-OPEN; separating it from W-OPEN keeps the wrapper's
orientation role clean and gives the instrument its own uncluttered moment.

---

## Structure Summary

```
C-PRE-co-01 (page, _classes: "{{pathwaySlug}} confidence-pre")
└── C-PRE-a-01 (article)
    └── C-PRE-b-05: Confidence PRE [text framing? — no: framing via instruction field] [confidence]
```

One block, one component. Per CC-1c, C-PRE carries a single §15.4-style
framing sentence plus the PRE component — **nothing else**. The framing
sentence lives in the component's `instruction`/page `body` fields, not a
separate text component, keeping the page to its single job.

---

## Content Object

```json
{
  "_id": "C-PRE-co-01",
  "_parentId": "course",
  "_type": "page",
  "_classes": "{{pathwaySlug}} confidence-pre",
  "title": "{{Pathway}}: {{Tier}} Stage, confidence check",
  "displayTitle": "Before you start",
  "body": "A quick check of how confident you feel about this course's outcomes before you begin. You'll rate the same statements again at the end.",
  "duration": "5 mins",
  "_pageLevelProgress": {
    "_isEnabled": true,
    "_showPageCompletion": true
  }
}
```

Menu body is reader-facing — no internal terminology ("tier", "PRE").

---

## Article

```json
{
  "_id": "C-PRE-a-01",
  "_parentId": "C-PRE-co-01",
  "_type": "article",
  "title": "Before you start"
}
```

---

## Blocks

### Block 1: Confidence PRE

**Classification:** Fixed structure, tier-specific items

Per WR-2a (curated items, cap 10) and CC-1c/CC-1d. Mechanism unchanged from
the wrapper-era design — only the host page changes.

| Field | Value |
|-------|-------|
| Block ID | `C-PRE-b-05` |
| Block title | "Confidence check" |
| Component | `confidence` |
| `_mode` | `"pre"` |

**Settings:**
```json
{
  "_mode": "pre",
  "_selfAssessmentGroupId": "{{pathwaySlug}}-confidence",
  "instruction": "Rate how confident you feel about each statement, then select Submit.",
  "_preConfirmation": "Thank you. You'll rate these again at the end of the course, and see how your confidence has shifted.",
  "_scale": {
    "_labels": ["Not at all confident", "Slightly confident", "Fairly confident", "Very confident", "Completely confident"]
  },
  "_items": [
    // Curated mix of tier + lesson outcomes, max 10 items (WR-2a)
    { "_id": "{{outcome-slug}}", "text": "I can {{outcome}}." }
  ]
}
```

**Pairing:** `_selfAssessmentGroupId` links this PRE to the POST on C-POST.
Both must use the same group ID for the pre/post comparison to work. Items
are single-sourced on the PRE (AR-3).

**Item selection:** decided at gate A6 (course-level), which now targets the
C-pages rather than the wrappers.

---

## Cross-Reference: Confirmed Decisions

| Decision | Status | Notes |
|----------|--------|-------|
| CC-1a | Confirmed | Dedicated page; sequence W-OPEN → C-PRE → lessons |
| CC-1b | Confirmed | Naming C-PRE (C-OPEN rejected) |
| CC-1c | Confirmed | Framing sentence + PRE only, nothing else |
| CC-1d | Confirmed | GroupId pairing, WR-2a cap, modes all unchanged |
| WR-2a | Confirmed (amended host) | Items curated, cap 10 |

---

## Open Questions

- **Retrofit verification (CC-1e):** rose pattern and suspend/resume were
  verified under wrapper placement; the retrofit needs its own verification
  pass, not an assumption of equivalence.
- **Confidence 5-option row overflow:** three-tier responsive layout landed
  (CRO-1); confirm it holds on the new page's context during the retrofit
  verification.
- **Menu numbering for C-pages:** "unnumbered" here follows the wrapper
  precedent as a proposal; confirm at the retrofit.
