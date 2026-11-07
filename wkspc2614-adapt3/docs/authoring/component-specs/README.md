# Component Authoring-Schema Specs

*Per-component authoring specifications for the Adapt components this programme uses. Each doc captures what the validation schema does not: how to author that component WELL — on-voice, on-tier, first time. The contract lives with the component so a human or AI author pulls in one doc and authors correctly, without the rules being re-explained each generation.*

**Status:** Format agreed 10 July 2026 (open-decisions.md, D-F4-1–5). This README is the format spec; the per-component docs follow it. First doc: `mcq.md`.

---

## Where these sit

One doc per component in this folder: `docs/authoring/component-specs/<component>.md` (e.g. `mcq.md`, `textinput.md`, `sortable.md`). Cross-linked from the shell manifest/registry. They are NOT placed inside `src/components/…`, because contrib plugin folders are overwritten on update; the authoring canon lives in `docs/`, which we own.

## Sources of truth — reference, never restate

Every per-component doc sits downstream of these authoritative documents and duplicates none of them. At least three always apply; a doc lists whichever are relevant in its Boundaries footer.

| Upstream | Governs | Cite as |
|---|---|---|
| `reference/excelling-voice-specification.md` | How copy sounds — register, rhythm, content-type voice | `Voice Spec §15.5` |
| `docs/curriculum/tier-specification.md` | What demand — assumed experience, cognitive demand, complexity, autonomy, assessment parity | `Tier Spec §7` |
| `design-kb/design-kb.activity-patterns.json`, `design-kb/design-kb.palette.json` | When to reach for the component at all — teaching-move routing (component-mapping-artefact.md is SUPERSEDED, MA-1) | `activity-patterns/<pattern-id>` or `palette/<component>` |
| `docs/curriculum/scoring-and-summative-model.md` | Scoring / formative-vs-summative mechanics (components that score) | `scoring-and-summative-model.md` |
| `docs/authoring/portable-unit-and-shell-format.md` | `_id` and context-slot conventions (context-slot components) | `portable-unit-and-shell-format.md` |

If a per-component doc finds itself writing more than a pointer plus a component-specific application of one of these, that content belongs upstream, not here.

## The nine-part format

Each doc has these nine parts plus a Boundaries footer. Parts are marked OWN (component-specific content that lives nowhere else — the reason these docs exist) or REF (a pointer to an upstream doc, never a restatement).

| # | Part | Type | What it holds |
|---|------|------|---------------|
| 1 | Front-matter / status | OWN | Version, status, "Relationship to other documents", the installed schema file this doc is verified against, and the pilot instance it is grounded in. |
| 2 | Purpose & when to reach for it | REF (+ thin OWN) | Pointer to the Mapping Artefact's routing decision, plus only the component-specific "prefer this / don't" the artefact does not already carry. |
| 3 | Annotated JSON shape | OWN — the core | A real skeleton from the installed schema, every field annotated: what it does, what WE set it to and why, load-bearing fields flagged. |
| 4 | Authoring guardrails — hard rules | OWN | Component-level invariants currently re-explained every build. |
| 5 | Voice rules | REF | A map of which field carries which content-type, each pointing at its Voice Spec §. No Voice Spec text copied in. |
| 6 | Tier-dependent guidance | REF (+ thin OWN) | Only where THIS component's authoring shifts by tier, as a pointer to Tier Spec + §16, naming which fields those rows govern. |
| 7 | Accessibility requirements | OWN | Field-level, component-specific. |
| 8 | Known gotchas & findings | OWN | Hard-won, dated, tied to the finding. |
| 9 | Worked example | OWN | One real annotated instance lifted from the pilot, every guardrail satisfied. |

**Boundaries footer (every doc ends with this, adapted):** states that register/voice live in the Voice Spec, tier demand in the Tier Spec, routing in the mapping artefact, scoring in the scoring model, and id/slot conventions in the portable-unit doc — and that this doc points to them, not restates them.

## Coverage

Every installed **teaching** component now has a spec. The adopted/built set (`component-candidates-register.md`) — mcq, textInput, adapt-abbott-sortable, hotgraphic, accordion, matching, text — was written first, grounded in real authored pilot instances. Coverage then extended to the remaining installed teaching components — gmcq, graphic, narrative, slider, media — as a readiness measure; these have no authored lesson instance yet, so their worked examples are illustrative and flagged to validate on first real use.

**Questions:** mcq, gmcq, textInput, matching, slider, adapt-abbott-sortable, adapt-abbott-confidence (custom, self-report/ungraded), adapt-abbott-opentext (custom, self-report/ungraded), adapt-abbott-pagefeedback (custom, self-report/ungraded, build-verified, no shipped instance yet). **Presentation:** text, graphic, accordion, hotgraphic, narrative, media, adapt-abbott-flipcard (custom, build-verified, no shipped instance yet), adapt-abbott-timeline (custom, build-verified, no shipped instance yet). **References/resources:** adapt-abbott-references (custom, grounded in W-CLOSE-c-15). **Tabbed navigation:** adapt-abbott-tabs (custom, build-verified, no shipped instance yet — first home is content-dense pathways). **Decision-scenario:** adapt-abbott-branching (custom, build-verified, no shipped instance yet — first home is Presenting 7). **Annotated exemplar:** adapt-abbott-annotated (custom, build-verified, no shipped instance yet — first home is worked examples in Academic Writing with weak/strong passage pairs). **Glossary passage:** adapt-abbott-glossary (custom, build-verified, no shipped instance yet — first home is Researching or Reflective Practice vocabulary introduction). **Working-aid checklist:** adapt-abbott-checklist (custom, build-verified, no shipped instance yet — first homes are Presenting 7 rehearsal/delivery, Revising & Exams 8 revision-readiness, Academic Writing 6 pre-submission, Work-Based 11 placement prep).

**Assessment feedback:** assessmentResults (contrib, grounded in SUMM-c-50 — spec closes #16 deferral, 13 August 2026).

**Non-teaching components:** `blank` is a utility spacer with no authorable content — no spec needed.
