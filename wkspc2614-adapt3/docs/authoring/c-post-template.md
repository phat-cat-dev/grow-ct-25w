# C-POST (Confidence Post) Template

> **DRAFT v1** — drafted 13 August 2026 from CC-1 (open-decisions.md),
> claude.ai planning sessions 4 and 13 August 2026. No built instance yet;
> the Academic Writing: Introductory Stage retrofit (CC-1e) will be the
> first. **Validate against that retrofit before treating as authoritative.**
>
> **SKS-1 note (20 September 2026):** Per SKS-1, the skeletons store is
> the single source of truth for structure; this template is an authoring
> guide pointing at it. Prompt 134's nesting audit (Task 5) named 1
> disagreement for this template: the reflective-bridge block is
> described here as realised by `opentext`, but the store's live
> `componentOptions` for that slot is currently empty, meaning the store
> cannot presently route this block to any component. Where this
> template and the store disagree, the store is authoritative.

Reference template for the Confidence Post page. This page exists as a
single instance per tier. It carries the confidence POST check, relocated
out of W-CLOSE per CC-1 — positioned after SUMM and before W-CLOSE, so the
closing wrap-up can reference the confidence shift rather than precede it.

See also:
- `open-decisions.md` CC-1 (confidence pages), WR-2d (five-pattern feedback)
- `c-pre-template.md` (C-PRE page — paired instrument)
- `summative-template.md` (SUMM — precedes this page)
- `wrapper-close-template.md` (W-CLOSE — follows this page; Block 1 removed by CC-1, enriched by WC-1)
- `component-specs/opentext.md` (optional bridge component)

---

## Overview

| Field | Value |
|-------|-------|
| Page ID | `C-POST-co-01` |
| Role | Confidence Post — repeat rating, pre/post comparison feedback, optional reflective bridge |
| Position | Fifth page: W-OPEN → C-PRE → lessons → SUMM → **C-POST** → W-CLOSE |
| Menu numbering | Unnumbered (structural page, following the 28 July wrapper decision) |

*Ids are generated per ID-1; ids shown here are illustrative.*

**Sequencing constraint (WR-2c, unchanged):** SUMM must render before this
page. The POST never reads another component's score — it compares only its
own pre/post ratings — but the shell sequence keeps the boundary clean.

---

## Structure Summary

```
C-POST-co-01 (page, _classes: "{{pathwaySlug}} confidence-post")
└── C-POST-a-01 (article)
    ├── C-POST-b-05: Confidence POST [confidence]
    └── C-POST-b-10: Reflective bridge [opentext] — OPTIONAL, off by default
```

Per CC-1c: a framing sentence (in `instruction`/page `body`, not a separate
text component), the POST with all five-pattern comparison feedback intact,
and an OPTIONAL reflective bridge revealed only after the POST completes.

---

## Content Object

```json
{
  "_id": "C-POST-co-01",
  "_parentId": "course",
  "_type": "page",
  "_classes": "{{pathwaySlug}} confidence-post",
  "title": "{{Pathway}}: {{Tier}} Stage, confidence check revisited",
  "displayTitle": "How far you've come",
  "body": "Rate the same statements you saw at the start, and see how your confidence has shifted across the course.",
  "duration": "5 mins",
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
  "_id": "C-POST-a-01",
  "_parentId": "C-POST-co-01",
  "_type": "article",
  "title": "How far you've come"
}
```

**If the bridge is enabled**, the article carries trickle to gate the reveal
— see Block 2's technical requirement.

---

## Blocks

### Block 1: Confidence POST

**Classification:** Fixed structure, tier-specific items and feedback

Per WR-2b (POST before the closing wrap-up) and WR-2d (five-pattern
classification, per-item authored feedback as primary). Mechanism unchanged
from the wrapper-era design — only the host page changes (CC-1d).

| Field | Value |
|-------|-------|
| Block ID | `C-POST-b-05` |
| Block title | "Confidence check" |
| Component | `confidence` |
| `_mode` | `"post"` |

**Settings:**
```json
{
  "_mode": "post",
  "_selfAssessmentGroupId": "{{pathwaySlug}}-confidence",
  "instruction": "Rate how confident you feel about each statement now, then select Submit.",
  "_standalone": "Thanks for completing this. If any of these felt less solid than you'd like, it's worth revisiting that part of the course before you move on.",
  "_feedback": {
    "_patterns": {
      "rose": "That's a genuine shift in how confident you feel about {{item}}.",
      "stayedHigh": "Your confidence in {{item}} was already strong, and it's held.",
      "dropped": "Your confidence in {{item}} dropped, which is often a sign of a more accurate view, not a worse one.",
      "stayedLow": "Your confidence in {{item}} has stayed low. Worth revisiting before you move on.",
      "noMovement": "No real change in your confidence about {{item}}."
    },
    "_summary": {
      "_predominantlyUp": "Your confidence has grown across most of what this course covered...",
      "_mixed": "Your confidence has moved in different directions across these statements...",
      "_flatOrLow": "Your confidence hasn't shifted much, or has dropped, across most of these statements..."
    },
    "_itemFeedbackOverrides": [
      // TIER-SPECIFIC per-item feedback for each outcome (WR-2d: primary
      // authoring mechanism, each item gets all five patterns)
      {
        "_itemId": "{{outcome-slug}}",
        "rose": "{{tier-specific rose feedback}}",
        "stayedHigh": "{{tier-specific stayedHigh feedback}}",
        "dropped": "{{tier-specific dropped feedback}}",
        "stayedLow": "{{tier-specific stayedLow feedback}}",
        "noMovement": "{{tier-specific noMovement feedback}}"
      }
    ]
  }
}
```

**Pairing:** same `_selfAssessmentGroupId` as C-PRE's component. SA-8
degradation applies unchanged: if no PRE exists, the POST degrades
gracefully to standalone feedback.

---

### Block 2: Reflective bridge — OPTIONAL

**Classification:** Fixed structure when enabled; OFF by default

Per CC-1c. The POST's feedback is *told to* the learner; the bridge is
*asked of* them — a genuinely different move, not duplication. Off by
default programme-wide; enabled per course at gate A6. Obvious candidates:
the reflection-heavy pathways (Reflective Practice, Work-Based Learning).

| Field | Value |
|-------|-------|
| Block ID | `C-POST-b-10` |
| Block title | "Your reflection" |
| Component | `opentext` |
| `_variant` | `"reflection"` |

**Settings:**
```json
{
  "_component": "opentext",
  "_variant": "reflection",
  "displayTitle": "Your reflection",
  "instruction": "Looking at how your confidence has shifted, note what you would act on next.",
  "_isCompletionBearing": false
}
```

`_isCompletionBearing: false` deliberately: the bridge must not block page
or course completion — it is an offered reflection, not a required task
(the over-testing concern from decision #25: SUMM → POST → bridge is
already three consecutive asks).

**TECHNICAL REQUIREMENT — completion-gated reveal (CC-1c):** the bridge
renders only after the POST reports complete, so the learner reflects on
the movement they have *just been shown*, not a prediction of it. Proposed
mechanism: article-level trickle on `C-POST-a-01` gating block 2 behind
block 1's completion (the established trickle pattern from SUMM). To be
confirmed at the first enabled instance's verification pass — flag if
trickle's button chrome is wrong for this context and a
visibility-on-completion alternative is needed.

**Persistence:** learner text persists via `adapt-abbott-reflective-store`
(SCORM 2004 `suspend_data` custom keys, RTR-1 fix) — verified end-to-end
on Cardiff Met Moodle, 31 July 2026, under lesson placement; re-verify
under C-POST placement when first enabled.

---

## Cross-Reference: Confirmed Decisions

| Decision | Status | Notes |
|----------|--------|-------|
| CC-1a | Confirmed | Dedicated page; POST before W-CLOSE so wrap-up can reference the shift |
| CC-1b | Confirmed | Naming C-POST (C-CLOSE rejected — misread as a closing page) |
| CC-1c | Confirmed | Framing + POST + optional post-completion bridge |
| CC-1d | Confirmed | GroupId pairing, WR-2a cap, modes all unchanged |
| WR-2b | Confirmed (amended host) | POST precedes the closing wrap-up |
| WR-2d | Confirmed | Five-pattern feedback, per-item overrides primary |

---

## Open Questions

- **Bridge reveal mechanism:** trickle proposed; confirm at first enabled
  instance (button chrome vs visibility-on-completion).
- **Retrofit verification (CC-1e):** rose pattern, suspend/resume (RTR-1 /
  SRF-1) verified under wrapper placement — re-verify under C-POST
  placement, plus the bridge reveal if enabled.
- **Bridge prompt authoring:** one prompt shape shown here; whether A6
  offers alternative phrasings per pathway is a gate-design detail for the
  workflow rewrite (queue 3.3).
