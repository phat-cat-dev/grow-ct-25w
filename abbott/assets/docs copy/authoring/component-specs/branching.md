# branching (adapt-abbott-branching) — Authoring Spec

**Version:** 0.1
**Status:** draft — ships with the component (built 31 July 2026). No authored lesson instance yet; the worked examples are **build-verified** (rendered and behaviour-confirmed via Playwright check, 31 July 2026) but no shipped instance — a step stronger than illustrative, still short of a real authored placement. First real instance lands when Presenting (7) is authored.
**Verified against:** `src/components/adapt-abbott-branching/properties.schema` — **our own schema** (custom component; no `example.json`).
**Relationship to other documents:** this component's build rationale lives in `open-decisions.md` (build-own ladder entry, BR-1–7 design, BB-1–6 build). This spec references the Voice Specification and `design-kb/design-kb.activity-patterns.json` (component-mapping-artefact.md is SUPERSEDED, MA-1); it restates neither.

---

## 1. Purpose & when to reach for it

A **self-contained decision-scenario component** for "what would you do?" interactions. Presents scenario prose with 2–4 choices as buttons; selecting one reveals that choice's consequence. Single-choice-then-reveal only — no multi-level trees, no cross-page or cross-block navigation.

**Not a question component.** No marking, no correct answer, no `_recordInteraction`, no response semantics. There is no "right" choice — every option is plausible, and every consequence is instructive rather than punitive. The base class's visitation tracking (`_userAnswer` as a boolean array) handles persistence; in commit mode, the visited item IS the chosen item.

**First homes:** Presenting (7), Reflective Practice (10), Work-Based Learning (11) — pathways where professional-judgement and decision-under-uncertainty scenarios recur.

Reach for it when:
- A scenario presents a genuine **professional dilemma** with multiple defensible responses
- You want learners to **commit to a choice** and then reflect on its trade-offs
- The learning lies in **understanding consequences**, not getting the "right answer"

Do not use it when:
- There IS a correct answer (use `mcq`)
- You need multi-level branching trees (consider a structured page sequence or external tool)
- The content is purely informational (use `text`, `accordion`, or `flipcard`)
- The scenario has a trick answer or gotcha (violates BR-6 — see §3)

**Routing boundaries:**
- **vs mcq:** mcq marks correctness; branching reveals consequences without marking. If the answer is graded, use mcq.
- **vs adapt-contrib-branching extension:** that extension routes between blocks based on question correctness — page-flow control. This component is self-contained: the decision and consequence are in one place.
- **vs accordion:** accordion is disclosure-driven (click to reveal); branching is choice-driven (select one, see what happens). Accordion suits "explore all"; branching suits "commit and reflect."

---

## 2. The annotated JSON shape

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `_component: "branching"` | yes | — | Lowercase — the registered component name. |
| `displayTitle` | recommended | — | Student-facing heading (often the scenario hook). |
| `body` | yes | — | The scenario prose — the situation the learner is being asked to respond to. |
| `instruction` | recommended | — | The ask: "What would you do?" or similar. Becomes the group label for accessibility. |
| `_selectionBehaviour` | no | `"commit"` | `"commit"`: one choice only, locked after selection (the decision is final). `"explore"`: choices can be tried in turn, one consequence visible at a time. |
| `_items[]` | yes | — | Array of 2–4 choice objects (see below). |

**Each `_items[]` entry:**

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `text` | yes | — | The choice label — displayed on the button. |
| `consequence.title` | recommended | — | Heading for the consequence region. Leave blank for no heading. |
| `consequence.body` | yes | — | The consequence text — what happens if the learner chooses this option. Must be instructive, not punitive (BR-6). |

**Index-keyed persistence (BR-4).** Items are keyed by array index, not `_id`. Reordering `_items` between sessions breaks restoration. If you must reorder, expect learners to see partial completion reset.

Globals (`ariaRegion`) carry sensible defaults; override only for wording.

---

## 3. Authoring guardrails (hard rules)

1. **2–4 choices.** Every scenario must have between 2 and 4 options. Fewer than 2 isn't a decision; more than 4 dilutes the dilemma. The schema enforces this.

2. **Every choice is plausible.** No choice should be an obvious wrong answer or a trap. If you can imagine a reasonable person choosing it, it belongs. If you can't, it doesn't.

3. **Every consequence is instructive.** The consequence explains the trade-offs of that choice — what it achieves, what it costs, what it assumes. It is never punitive ("You failed because…") or dismissive ("Bad choice"). Consequences are narrative, not verdicts.

4. **No correct answer.** If one choice is objectively right and the others are objectively wrong, use `mcq` instead. Branching is for genuine dilemmas, not dressed-up multiple-choice.

5. **Scenario prose sets the context.** The `body` field must give the learner enough information to make a meaningful choice. If key facts are missing, the decision becomes arbitrary.

6. **Instruction frames the ask.** The `instruction` field should make clear what the learner is being asked to do: "What would you do?", "Which approach would you take?", etc. This also serves as the accessible group label.

7. **Commit mode is the default.** Use `_selectionBehaviour: "commit"` unless you explicitly want learners to explore all consequences. Commit mode forces reflection; explore mode invites comparison.

8. **Completion fires on first selection.** The component completes when the learner makes their first choice (in either mode). This is deliberate: the decision IS the learning moment. Requiring exhaustive exploration would contradict the commitment framing.

9. **Index-keyed persistence.** Items persist by array index, not `_id`. Do not reorder `_items` between course versions unless you accept learner progress may not restore correctly.

---

## 4. Voice rules (reference — not restated here)

Decision-scenario throughout — scenario prose and consequence prose, no feedback or scoring copy.

| Field | Content type | Voice Spec |
|-------|--------------|------------|
| `body` | Scenario prose — mid-register narrative | §13 (teaching prose), §4 (explain the why), §11 (clarity) |
| `instruction` | Activity instruction | §15.4 (instruction conventions) |
| `_items[].text` | Choice label — crisp, parallel structure | §11 (clarity), keep choices structurally parallel |
| `consequence.title` | Consequence heading — neutral, not judgemental | Match scenario register |
| `consequence.body` | Consequence prose — trade-offs, not verdicts | §4 (explain the why), §13 (mid-register), never punitive |

**Voice principle (BR-6):** No choice is a gotcha. Every option must be plausible, and every consequence must be instructive rather than punitive. Consequences are narrative ("Here's what happens…"), not verdicts ("Wrong because…").

Contractions follow the lesson context (§11.2) — usually yes for mid-lesson teaching, no for learning-outcome-adjacent content.

---

## 5. Tier-dependent guidance

The component is **not graded**, so the Tier Spec's assessment dimension does not apply. Tier lands in three places:

- **Scenario complexity.** Introductory scenarios present clearer trade-offs with more scaffolding in the consequences; intermediate/advanced scenarios present genuine dilemmas where reasonable people disagree.
- **Choice nuance.** Introductory choices are more distinct (different approaches); advanced choices may be more subtle (variations on a theme).
- **Consequence depth.** Introductory consequences explain trade-offs more explicitly; advanced consequences may assume the learner can infer some implications.

The interaction itself is tier-neutral — the mechanic is the same at all levels.

---

## 6. Accessibility requirements

- **Choices in a `role="group"`** with `aria-labelledby` pointing to the instruction. The group semantics convey that these are related options.

- **Each choice is a native `<button>`** with `aria-pressed` reflecting selection state (`"true"` when selected, `"false"` otherwise).

- **Commit-locked buttons use `aria-disabled="true"`, NOT `disabled`.** Reason: the HTML `disabled` attribute removes elements from the tab order. In a decision scenario, unchosen options are meaningful record — the learner should be able to read back what they didn't choose. `aria-disabled` keeps them in the tab order while preventing interaction.

- **Chosen button has visible marker.** The selected state is indicated by more than colour: a checkmark (✓), bold weight, and border change. Colour alone is insufficient (WCAG 1.4.1).

- **Consequence region has `tabindex="-1"`** for programmatic focus. When the learner selects a choice, focus moves to the consequence region. This is a deliberate divergence from flipcard/timeline's stay-put rule: in branching, new content appears elsewhere and (in commit mode) the trigger becomes unavailable, so moving focus follows the confidence component's precedent.

- **Consequence region has `role="region"` and `aria-live="polite"`** to announce new content to screen readers.

- **`ariaRegion` introduces the interaction** at component level (defaults to "Decision scenario. Read the situation and select one of the choices to see what happens.").

- **Reduced motion.** CSS includes `@media (prefers-reduced-motion: reduce)` — reveal animation falls back to instant, no transform. *(Not yet verified live; carried to the strategic accessibility-verification pass.)*

---

## 7. Known gotchas & findings

- **`_component` is `"branching"`** (lowercase), not the plugin directory name.

- **Completion = first selection, not all-visited.** Unlike flipcard/timeline (which complete when all items are visited), branching completes on the first selection. This is deliberate (BR-3): the decision is the learning moment.

- **`_isSelected` is transient, not persisted.** On revisit, selection is restored from visitation: in commit mode, the visited item IS the selected item. In explore mode, multiple items may be visited but no auto-selection occurs on revisit — the learner re-explores from a clean state.

- **Commit-lock is enforced in the model, not just the UI.** Even if someone bypasses the UI guard, the model rejects second selections in commit mode. The aria-disabled UI state is a presentation of a model-level invariant.

- **Full-width stacked buttons.** Choices render as a vertical list of full-width buttons, not a grid. This ensures readability at all viewport widths and maintains visual hierarchy.

- **No images.** This component has no image fields. The scenario is text-driven. If you need visual context, use a text component with a graphic above the branching component.

- **No `example.json`** — this spec's worked examples are the reference.

---

## 8. Worked examples (BUILD-VERIFIED — no shipped instance yet)

Two real scenarios used in build verification (31 July 2026). Both are **build-verified** — rendered and behaviour-confirmed via Playwright checks. First shipped instance lands when Presenting (7) is authored.

### 8.1 Commit mode (Presenting-flavoured)

A professional-judgement scenario with three choices. Commit mode enforces a single decision.

```json
{
  "_component": "branching",
  "_layout": "full",
  "displayTitle": "You're about to present",
  "body": "<p>You're presenting your group project findings tomorrow. Two hours before, you discover your slides have a significant factual error on the third slide. Your co-presenter has already left campus.</p>",
  "instruction": "What would you do?",
  "_selectionBehaviour": "commit",
  "_items": [
    {
      "text": "Fix the error yourself, then message your co-presenter to let them know",
      "consequence": {
        "title": "A reasonable call",
        "body": "<p>You've taken ownership of the problem and kept your co-presenter informed. The fix is made, and they can review it if they check their messages. This approach works well when the error is clear-cut and the fix is within your competence.</p><p>The trade-off: you've made an editorial decision without joint agreement. If your co-presenter would have handled it differently, that conversation comes after the fact.</p>"
      }
    },
    {
      "text": "Leave the slide as-is and mention the correction verbally during the presentation",
      "consequence": {
        "title": "Transparency over polish",
        "body": "<p>You've avoided making unilateral changes, and the audience will hear the correct information. This can work if the error is minor and the verbal correction lands clearly.</p><p>The trade-off: audiences remember what they see more than what they hear. A slide with a visible error may undermine confidence, even if you correct it verbally.</p>"
      }
    },
    {
      "text": "Wait until your co-presenter is reachable so you can decide together",
      "consequence": {
        "title": "Collaboration under pressure",
        "body": "<p>You've prioritised joint decision-making, which matters in a genuine partnership. If you can reach them in time, you'll present a version you both stand behind.</p><p>The trade-off: you're betting on contact happening. If it doesn't, you've run out of time to fix it yourself, and you present knowing the error is there.</p>"
      }
    }
  ]
}
```

**How it satisfies the spec:** three choices (guardrail 1); all plausible (guardrail 2); all consequences instructive, not punitive (guardrail 3); no objectively correct answer (guardrail 4); scenario prose sets context (guardrail 5); instruction frames the ask (guardrail 6); commit mode default (guardrail 7).

### 8.2 Explore mode

A feedback-response scenario with four choices. Explore mode invites comparison across approaches.

```json
{
  "_component": "branching",
  "_layout": "full",
  "displayTitle": "Feedback approaches",
  "body": "<p>You've received feedback on your essay saying 'Your argument needs more structure.' Explore each approach to see what it involves.</p>",
  "instruction": "Select each approach to explore what it means.",
  "_selectionBehaviour": "explore",
  "_items": [
    {
      "text": "Add signposting language throughout",
      "consequence": {
        "title": "Signposting",
        "body": "<p>Signposting makes your structure visible: phrases like 'This essay will argue...', 'Having established X, this section turns to Y', 'In conclusion'. It guides the reader through your argument.</p><p>When it helps: when you have a clear structure but haven't made it explicit. When it doesn't help: when the underlying structure is unclear or illogical — signposting can't fix that.</p>"
      }
    },
    {
      "text": "Reorganise your paragraphs",
      "consequence": {
        "title": "Paragraph-level structure",
        "body": "<p>If your paragraphs are in the wrong order, the argument won't flow. Each paragraph should do one job, and their sequence should build toward your conclusion.</p><p>Try this: write one sentence per paragraph summarising its job. If you can't, or if the sequence doesn't make sense, reorganise.</p>"
      }
    },
    {
      "text": "Revisit your plan",
      "consequence": {
        "title": "Back to planning",
        "body": "<p>If the structure feels broken throughout, the problem may be in the plan. A plan that seemed clear before drafting sometimes reveals gaps when you try to write it out.</p><p>This is normal. Going back to the plan isn't failure — it's part of how writing clarifies thinking.</p>"
      }
    },
    {
      "text": "Focus on paragraph openings",
      "consequence": {
        "title": "Topic sentences",
        "body": "<p>The first sentence of each paragraph should signal what that paragraph is about. Strong topic sentences let a reader skim your structure before reading in detail.</p><p>Test: read only your first sentences in order. If the argument isn't visible, your openings aren't doing their job.</p>"
      }
    }
  ]
}
```

**How it satisfies the spec:** four choices (guardrail 1); all plausible (guardrail 2); all consequences instructive (guardrail 3); explore mode explicit (not default) for a compare-all scenario; instruction signals explore intent; consequences explain when each approach does and doesn't help.

---

## Boundaries — what this doc does and does not govern

This doc governs the JSON shape and field-level authoring of the **branching** component. Its build rationale (build-own ladder entry, BR-1–7 design, BB-1–6 build) lives in `open-decisions.md`; register and voice live in the **Voice Specification**; component-to-pedagogy mapping lives in **`design-kb/design-kb.activity-patterns.json`** (component-mapping-artefact.md is SUPERSEDED, MA-1). This doc points to them; it does not restate them.

---

*End of branching authoring spec — v0.1.*
