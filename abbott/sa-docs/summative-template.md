# SUMM (Summative Assessment) Template

> **DRAFT v1** — based on Academic Writing: Introductory Stage instance only
> (28 July 2026). Does NOT yet incorporate all design decisions from the 28
> July P8 walkthrough. See `template-v2-scope.md` for the full list of items
> queued for a v2 pass. **Needs a v2 pass before being treated as authoritative.**
>
> **SKS-1 note (20 September 2026):** Per SKS-1, the skeletons store is
> the single source of truth for structure; this template is an authoring
> guide pointing at it. Prompt 134's nesting audit (Task 5) named this
> template as its single strongest drift finding: `gate-conversation-map.md`'s
> own S1 gate text instructs that this document should never be read,
> calling it actively misleading about marking, feedback and furniture
> since it predates the 14 August changes — a finding the audit's own
> structural nesting work (Task 3) corroborates independently, since the
> store models only 2 of the 5 blocks this template describes. The audit
> separately noted that the store's own `completionRules.summative`
> attempts-rule field still reads as unruled even though a partial ruling
> exists elsewhere; the audit attributed that drift to the store's own
> stale field, not to this template, and it is recorded here for
> completeness rather than as a defect of this file. Given the S1
> instruction above, treat this whole document as unreliable pending a
> rewrite, not just the two items named.

Reference template for the Summative Assessment page that tests cross-tier
integration. This page exists as a single instance per tier (unlike content
lessons, which repeat a pattern).

See also:
- `open-decisions.md` SM-1–3 (summative page template)
- `open-decisions.md` S-1–5 (scoring and summative model)
- `wrapper-open-template.md` (W-OPEN page)
- `wrapper-close-template.md` (W-CLOSE page)
- `lesson-structure-template.md` (content lesson structure)

---

## Overview

| Field | Value |
|-------|-------|
| Page ID | `SUMM-co-01` |
| Role | Summative Assessment — cross-tier integration check |
| Position | After all content lessons, before W-CLOSE |
| Menu numbering | Unnumbered (28 July decision) |

*Ids are generated per ID-1; ids shown here are illustrative.*

---

## Structure Summary

```
SUMM-co-01 (page, _classes: "summative")
├── SUMM-a-01 (article, _assessment enabled, trickle on children)
│   ├── SUMM-b-05: Orientation [text]
│   ├── SUMM-b-10 through SUMM-b-45: Assessment items (7-8 total) [mcq/sortable]
│   └── (trickle gates each item)
└── SUMM-a-05 (article, results)
    ├── SUMM-b-50: Assessment complete [text + trickle button]
    └── SUMM-b-55: Results [assessmentResults]
```

---

## Content Object

```json
{
  "_id": "SUMM-co-01",
  "_parentId": "course",
  "_type": "page",
  "_classes": "{{pathwaySlug}} summative",
  "title": "Bringing it together",
  "displayTitle": "Bringing it together",
  "body": "{{TIER-SPECIFIC: Menu blurb describing the cross-tier integration check.}}",
  "duration": "15 mins",
  "_pageLevelProgress": {
    "_isEnabled": true,
    "_showPageCompletion": true
  }
}
```

---

## Article 1: Assessment

**Classification:** Fixed structure

Per SM-1–3, S-1–5.

```json
{
  "_id": "SUMM-a-01",
  "_parentId": "SUMM-co-01",
  "_type": "article",
  "title": "Bringing it together",
  "_assessment": {
    "_isEnabled": true,
    "_id": "SUMM-a-01",
    "_scoreToPass": 70,
    "_isPercentageBased": true,
    "_attempts": -1,
    "_isResetOnRevisit": false,
    "_allowResetIfPassed": false,
    "_questions": {
      "_resetType": "hard",
      "_canShowFeedback": false,
      "_canShowMarking": false,
      "_canShowModelAnswer": false
    }
  },
  "_trickle": {
    "_isEnabled": true,
    "_onChildren": true,
    "_button": {
      "_isEnabled": true,
      "startText": "Continue"
    }
  }
}
```

**Key assessment settings:**
- 70% pass mark (per S-3)
- Unlimited attempts (per S-5)
- Reset on revisit (prevents memorising correct answers by reviewing)
- No feedback during assessment (shown only on results)

---

## Blocks

### Block 1: Orientation

**Classification:** Fixed/generic

Per SM-1. Single §15.4-style paragraph, no mechanical details (pass mark,
attempts remaining etc. are handled by the results component, not prose).

| Field | Value |
|-------|-------|
| Block ID | `SUMM-b-05` |
| Block title | "Orientation" |
| Component | `text` |

**Content example:**
> "This checks whether you can bring together what you've learned across this
> course, not a re-test of each part individually."

---

### Blocks 2-9: Assessment items (7-8 total)

**Classification:** Tier-specific content, fixed structure

Per SM-2. Item count: 7-8 total. Component types: mcq, sortable, matching
(per content fit).

| Field | Value |
|-------|-------|
| Block IDs | `SUMM-b-10` through `SUMM-b-45` (increment by 5) |
| Block title | "Item {{n}}: {{item-topic}}" |
| Component | `mcq` / `sortable` / `matching` |

**Per-item settings:**
```json
{
  "_attempts": 1,
  "_questionWeight": 1,
  "_shouldDisplayAttempts": false,
  "_canShowFeedback": false,
  "_canShowMarking": false,
  "_canShowModelAnswer": false,
  "_recordInteraction": true
}
```

**Item mix:** Tier-specific. Academic Writing uses:
- 2 steer/keyword identification (mcq)
- 2 sequencing (sortable)
- 4 error recognition (mcq)

Other pathways will have different splits based on their lesson content.

---

## Article 2: Results

```json
{
  "_id": "SUMM-a-05",
  "_parentId": "SUMM-co-01",
  "_type": "article",
  "title": "Results"
}
```

---

### Block 10: Assessment complete

**Classification:** Fixed/generic

Transitional text before results, with trickle button.

| Field | Value |
|-------|-------|
| Block ID | `SUMM-b-50` |
| `_parentId` | `SUMM-a-05` |
| Block title | "Show results" |
| `_classes` | `"background-color-inverted"` |
| Component | `text` |

**Trickle settings:**
```json
{
  "_trickle": {
    "_isEnabled": true,
    "_button": {
      "_isEnabled": true,
      "text": "Show results"
    }
  }
}
```

**Content:** "You've completed the assessment."

---

### Block 11: Results

**Classification:** Fixed structure, tier-specific feedback wording

| Field | Value |
|-------|-------|
| Block ID | `SUMM-b-55` |
| `_parentId` | `SUMM-a-05` |
| Block title | "Results" |
| Component | `assessmentResults` |

> **CAVEAT:** This structure may change pending the still-undesigned
> "per-question correct/incorrect breakdown after completion" feature request
> from the 28 July walkthrough. The 4-band-only result below is what exists
> now, not final.

**Settings:**
```json
{
  "_assessmentId": "SUMM-a-01",
  "_isVisibleBeforeCompletion": false,
  "_setCompletionOn": "inview",
  "_retry": {
    "button": "Try again"
  },
  "_completionBody": "{{{feedback}}}",
  "_bands": [
    {
      "_score": 0,
      "feedback": "You didn't pass this time, achieving {{scoreAsPercent}}%. Have another look through this course's topics, then try again when you're ready.",
      "_allowRetry": true
    },
    {
      "_score": 50,
      "feedback": "You're close, achieving {{scoreAsPercent}}%, but not quite at the pass mark yet. A little more review should get you there.",
      "_allowRetry": true
    },
    {
      "_score": 70,
      "feedback": "You passed, achieving {{scoreAsPercent}}%. {{TIER-SPECIFIC: what this demonstrates}}",
      "_allowRetry": true
    },
    {
      "_score": 100,
      "feedback": "You passed with a perfect score, achieving {{scoreAsPercent}}%. {{TIER-SPECIFIC: what this demonstrates}}",
      "_allowRetry": false
    }
  ]
}
```

---

## Cross-Reference: Confirmed Decisions

| Decision | Status | Notes |
|----------|--------|-------|
| SM-1 | Confirmed | Orientation, no mechanical details |
| SM-2 | Confirmed | 7-8 items |
| SM-3 | Confirmed | ID convention SUMM |
| S-3 | Confirmed | 70% pass mark |
| S-5 | Confirmed | Unlimited attempts |

---

## Open Questions

See `template-v2-scope.md` for the full list of items queued for a v2 pass.

Key open items affecting SUMM:
- **Per-question breakdown in Results:** feature request, not yet designed —
  may change the structure of Block 11
- **"Completed activity" chrome:** feature request for theme pass
