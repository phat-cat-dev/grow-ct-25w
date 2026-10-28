# confidence (adapt-abbott-confidence) — Authoring Spec

**Version:** 0.1
**Status:** draft — ships with the component (built 13 July 2026). No authored lesson instance yet; the worked example is **illustrative** and the recording path awaits live Moodle validation (BS-2a-iii). First real instance lands in C2.
**Verified against:** `src/components/adapt-abbott-confidence/properties.schema` — **our own schema** (custom component; no `example.json`).
**Relationship to other documents:** this component's full rationale lives in `open-decisions.md` #17–23 (SA-1–8 model, AR-1–6 architecture, CD-1–4 schema/logic, BS-1–5 build spec, BP-1 build-prep, BS-2a recording). This spec references the Voice Specification, the Tier Specification, and `portable-unit-and-shell-format.md`; it restates none of them.

---

## 1. Purpose & when to reach for it

A **pre/post self-efficacy instrument** that brackets a lesson: before the lesson a *pre* asks the learner to rate their confidence against the lesson's learning points; after the lesson a *post* re-rates the same points and gives progress feedback that calibrates the learner before whatever comes next. It is **not graded** — confidence is not competence (AR-1).

Reach for it when a lesson benefits from metacognitive book-ending — the learner noticing where their confidence moved, and being pointed forward to test it. It is one component authored as **two instances** (`_mode: "pre"` and `_mode: "post"`), joined by a shared group id.

Do not use it to assess anything (it has no correct answer — use `mcq`/`textInput`/`matching` for that), and do not use it where a lesson has no explicit learning outcomes to phrase the items from (SA-2 — the items *are* the outcomes; a lesson without stated outcomes cannot author the pre).

> **Routing note:** this component is new and does not yet have an entry in `design-kb/design-kb.activity-patterns.json` (component-mapping-artefact.md is SUPERSEDED, MA-1). Adding one (teaching move → "confidence check / metacognitive book-end") is a pending follow-up.

---

## 2. The annotated JSON shape (two modes)

One schema, two instances. `_component` is `"confidence"` (lowercase). **[LB]** = load-bearing. The right-hand columns show which mode authors each field.

| Field | pre | post | Notes |
|---|---|---|---|
| `_component: "confidence"` | ✓ | ✓ | **[LB]** lowercase — not the plugin dir name. |
| `_mode` | `"pre"` | `"post"` | **[LB]** the mode switch (AR-2). |
| `_selfAssessmentGroupId` | ✓ | ✓ | **[LB]** identical on both; unique to the lesson (AR-2/AR-6). The post finds its pre by this. |
| `instruction` | ✓ | ✓ | §15.4. |
| `ariaQuestion` | optional | optional | §6. |
| `_items[]` (`_id` + `text`) | ✓ authored | — leave empty | **[LB]** SA-2. Each item = a lesson outcome as a can-do statement; stable unique `_id` keys rating + delta + override (CD-2). Post **inherits** by group id (AR-3). |
| `_scale._labels` | ✓ authored | — leave empty | **[LB]** five anchored labels low→high (SA-3). Inherited by the post. |
| `_preConfirmation` | ✓ | — | Shown after the pre submits. §15.3/§15.5. |
| `_hasSummativeFollowing` | — | ✓ (assembly-set) | **[LB]** AR-5. Selects the forward hand-off. Default `false`. Set at assembly, not by hand. |
| `_feedback._patterns` (`rose`,`stayedHigh`,`stayedLow`,`noMovement`,`dropped`) | — | ✓ authored | **[LB]** SA-5/CD-3. `{{item}}` slots the statement text. |
| `_feedback._summary` (`_predominantlyUp`,`_mixed`,`_flatOrLow`) | — | ✓ authored | **[LB]** SA-6/CD-4. |
| `_feedback._standalone` | — | ✓ authored | SA-8. Shown when no pre ratings exist. `{{item}}` available. |
| `_feedback._forward` (`_summative`,`_application`) | — | ✓ authored | **[LB]** SA-7. One is appended to the summary on every path per `_hasSummativeFollowing`. Author **both**. |
| `_itemFeedbackOverrides[]` (keyed by `_itemId`) | — | optional | Bespoke pattern wording for a specific item; empty → use `_patterns`. |
| `_recordInteraction` | ✓ | ✓ | Default true. Records each rating to `cmi.interactions` (see §7). |
| `_buttons._submit` | optional | optional | Defaults inherited. |

Globals (`ariaRegion`, `ariaScaleName`, `ariaItemRated`) carry sensible defaults; override only for wording.

---

## 3. Authoring guardrails (hard rules)

1. **Two instances, one group id.** The pre and post carry the *same* `_selfAssessmentGroupId`, and it must be **unique to the lesson** (derive it from the lesson id/slug per AR-6) so a post never resolves the wrong pre.
2. **Items on the PRE only.** Author `_items` and `_scale` on the pre; leave them empty on the post — an empty items array on the post is *correct*, not an omission (it inherits). A post with its own items *and* a reachable pre → its items are ignored (guard warns, AR-3). A post with *no* reachable pre → runs standalone (SA-8), which is legitimate at runtime but usually an authoring error if unintended.
3. **Every item needs a stable, unique `_id`.** It keys the stored rating, the pre/post delta, and any per-item override (CD-2). Because the post inherits the pre's items, the ids match automatically — never hand-duplicate items onto the post.
4. **Author the full POST feedback set.** All five `_patterns`, all three `_summary` variants, `_standalone`, and **both** `_forward` strings. Author both forward strings even if you expect only one to fire — assembly sets `_hasSummativeFollowing`, and a missing string yields a truncated hand-off.
5. **Don't hand-set `_hasSummativeFollowing`.** It is set at assembly from whether the lesson shell contains a summative article (AR-5). Default `false` → the application/practice hand-off.
6. **All-required if engaged; skippable as a whole.** The learner must rate *every* item before Submit enables (BS-4). The whole component is skippable at lesson level (it never blocks completion) — the freedom is in skipping, not half-finishing.
7. **Placement (CC-1a/CC-1c).** PRE and POST do not sit inside a lesson, and are not embedded in W-OPEN/W-CLOSE (AR-6's lesson-level placement and WR-2b's wrapper-embedded placement are both superseded). They live on two dedicated pages: **C-PRE** — a single §15.4-style framing sentence plus the PRE component, nothing else — and **C-POST** — a framing sentence, the POST component (five-pattern comparison feedback, WR-2d), plus an OPTIONAL reflective bridge (an `adapt-abbott-opentext` reflection instance, revealed only after the POST reports complete, off by default and enabled per course via gate A6). Page sequence: W-OPEN → C-PRE → lessons → SUMM → C-POST → W-CLOSE.

---

## 4. Voice rules (reference — not restated here)

Formative throughout, so contractions are used (open-decisions #15); the register is reflective (§15.3), a touch more formal than a mid-lesson check (the SA-5 voice decision).

| Field | Content type | Voice Spec |
|---|---|---|
| `_items[].text` | A lesson outcome as a can-do confidence statement | §16 (outcome register) + §11.7 |
| `instruction` | Activity instruction | §15.4 |
| `_preConfirmation` | Warm formative close that points forward | §15.3 / §15.5 |
| `_feedback._patterns.*` | Metacognitive feedback per movement pattern — evaluative about the work, never the person; the *dropped* pattern reframes a fall as a more accurate view, not a failure | §15.5 (reflective, §15.3) |
| `_feedback._summary.*` | Synthesising close that normalises mixed/downward movement | §15.5 |
| `_feedback._forward.*` | The forward hand-off (SA-7) — never asserts mastery | §15.5 |
| `_feedback._standalone` | Single-reading feedback, pointed forward | §15.5 |

---

## 5. Tier-dependent guidance (reference — Tier Spec + Voice Spec §16)

The component is **not graded**, so the Tier Spec's assessment dimension (§7) does not apply. Tier lands in two places instead:

- **The items** track the lesson's learning outcomes (SA-2), which are already tier-calibrated — an introductory lesson's outcomes yield introductory confidence statements. Register follows the pathway's **§16** band.
- **The feedback register** follows the learner-autonomy progression (Tier Spec autonomy dimension; open-decisions #12): introductory feedback is more concrete and directive, higher tiers more open and self-directing. As with every component, the feedback *voice* is constant across tiers; only vocabulary shifts (open-decisions #2) — do not add scaffolding to the feedback at lower tiers.

---

## 6. Accessibility requirements

- **Radio-group Likert, not a slider.** Each item is a radio group: the statement labels the group, and the five scale points are labelled radio inputs. This is deliberate — it fixes the known missing-label accessibility bug in the `confidenceSlider` reference plugin, and keyboard operation is native to radios (arrows within a group, Tab between).
- **Every option carries its scale-label word** plus position ("…Fairly confident, 3 of 5") — never a bare number. This is the non-negotiable a11y rule for this component (BS-4).
- **Feedback is announced.** On post submit, focus moves to the feedback region (an `aria-live` region) so the patterns and summary are read out — a sighted-only feedback render would leave screen-reader users with silence. The pre confirmation is an `aria-live` status.
- **No meaning by colour alone.** Every pattern is a written sentence; the `pre → post` delta numbers are `aria-hidden` decoration, and any tint/arrow is decorative over text.
- Scale-name and per-rating announcements come from the `ariaScaleName` / `ariaItemRated` globals.

---

## 7. Known gotchas & findings

- **`_component` is `"confidence"`** (lowercase), not the plugin directory name.
- **Empty `_items`/`_scale` on the post is correct** — it inherits from the pre by group id. Do not copy items onto the post (that's the drift the AR-3 guard warns about).
- **SCORM recording — two accepted wrapper constraints (BS-2a):** interaction type is `numeric`, not `likert` (the spoor wrapper has no `likert` case); and each rating's `result` records as `wrong`/`incorrect` because the wrapper coerces a non-truthy `correct` arg — there is no `neutral` without forking spoor, which we don't do. Both are cosmetic in the LMS report; the rating itself lives in `cmi.interactions.n.learner_response`, extractable and pre/post-pairable by the `conf-<groupId>-<mode>-<itemId>` id.
- **Delta is computed fresh, never stored** (CD-4). Only the raw ratings persist (via `_userAnswer`/`trackable()`, serialised into suspend data). Cohort deltas are a subtraction done in the Moodle export, not a stored value.
- **Live-validation still owed (BS-2a-iii):** confirm the `numeric` interactions render per-item in Moodle's report (mind the 1.2 dot→underscore id quirk), that the `wrong` result doesn't disrupt extraction, and that on revisit the post reads the pre's restored ratings in the right order (the one residual timing risk).
- **No `example.json`** — this spec's worked example is the reference.

---

## 8. Worked example (ILLUSTRATIVE — no authored instance yet)

A pre/post pair for an introductory "Understanding the task" lesson, three outcomes. **Illustrative** — copy is placeholder-quality, not Voice-Spec-authored; the first real instance is authored in C2 against a real lesson's outcomes.

**PRE instance:**
```json
{
  "_component": "confidence",
  "_mode": "pre",
  "_selfAssessmentGroupId": "understanding-the-task-confidence",
  "instruction": "Rate how confident you feel about each statement, then select Submit.",
  "_scale": { "_labels": ["Not at all confident","Slightly confident","Fairly confident","Very confident","Completely confident"] },
  "_items": [
    { "_id": "steer",   "text": "I can identify the steer in an essay question." },
    { "_id": "keywords","text": "I can pick out the keywords that shape my answer." },
    { "_id": "scope",   "text": "I can work out the scope of what a question is asking." }
  ],
  "_preConfirmation": "Thank you. You will revisit these statements at the end of the lesson to see how your confidence has changed."
}
```

**POST instance** (same group id; items/scale left empty — inherited):
```json
{
  "_component": "confidence",
  "_mode": "post",
  "_selfAssessmentGroupId": "understanding-the-task-confidence",
  "instruction": "Now rate how confident you feel about each statement.",
  "_hasSummativeFollowing": false,
  "_feedback": {
    "_patterns": {
      "rose":       "Your confidence in {{item}} has grown over the lesson.",
      "stayedHigh": "You were confident about {{item}} and remain so.",
      "stayedLow":  "{{item}} still feels uncertain. It would be worth revisiting this before you move on.",
      "noMovement": "Your confidence in {{item}} has not shifted much.",
      "dropped":    "Your confidence in {{item}} has fallen. This often reflects a more accurate view of what the task demands rather than a step backwards, and noticing it is itself progress. It would be worth another look."
    },
    "_summary": {
      "_predominantlyUp": "Your confidence grew across most of these.",
      "_mixed":           "Your confidence grew in some areas and settled lower in others. Both are useful to know.",
      "_flatOrLow":       "Several of these still feel unsettled, which is worth knowing now."
    },
    "_standalone": "Here is where your confidence sits on each statement.",
    "_forward": {
      "_summative":   "The check ahead is where this confidence will be tested.",
      "_application": "The real measure will be how this holds up when you next apply it."
    }
  }
}
```

**How it satisfies the spec:** two instances sharing one lesson-unique group id (guardrail 1); items + scale on the pre only, each item with a stable `_id` (2, 3); post authors all five patterns, three summaries, standalone, and both forward strings (4); `_hasSummativeFollowing: false` here would append the `_application` hand-off (SA-7); `dropped` reframes rather than faults (§4/§15.5). The five-pattern classification and summary selection are the tested `confidenceLogic` functions (CD-3/CD-4).

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **confidence** component. Its design rationale lives in `open-decisions.md` #17–23; register and reflective/feedback voice live in the **Voice Specification**; tier register and the autonomy progression live in the **Tier Specification**; the pre/post placement convention (§3 guardrail 7) and group-id derivation (§3 guardrail 1) are set out in this doc, per AR-6; the deliberate separation from scoring lives in **`scoring-and-summative-model.md`** (this component is never graded). This doc points to them; it does not restate them.

---

*End of confidence authoring spec — v0.1.*
