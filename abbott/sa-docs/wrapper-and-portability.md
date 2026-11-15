# Wrapper Layer and Portable-Unit Authoring

**Status:** Established
**Scope:** All pathway-tiers; documented as part of the pilot build phase

This document captures two related authoring decisions: the three-layer copy model (shell / context slots / wrapper) and the portable-unit discipline. These decisions ensure lessons are both consistent within a pathway-tier and reusable across different delivery contexts.

---

## The three-layer copy model

Copy generation holds **three** distinct layers:

### 1. Shell

The teaching prose and structure shared across contexts:
- The six-part section flow (orientation, concept, worked example, analysis, practical guidance, reflective prompt)
- Core explanations and definitions
- Practical guidance and habits

Shell content is **pathway-specific but context-neutral**. It doesn't change when the discipline or overlay changes.

### 2. Context slots

The context-specific fills supplied by a context pack:
- Character name (e.g. Rhian, David)
- Discipline or subject area (e.g. criminology, sports journalism)
- Worked-example details (the specific question, keywords, scenario details)
- Any context-specific terminology

Context slots swap by overlay without touching the shell. They're marked in the JSON by `_classes` containing `context-slot` and a slot identifier (e.g. `slot-understandingTheTask-workedExample`).

**Summative slots:** When summative content sits in a context slot, it must be authored to the **tier's** demand level (per the Voice Specification), not matched question-for-question to a sibling context — parity rides on the tier, not the context. See `docs/curriculum/scoring-and-summative-model.md`.

### 3. Wrapper

The connective framing that makes lessons feel like one coherent programme within a pathway-tier:
- How a lesson opens and orients ("In the last lesson, you saw...")
- Signposting where it sits in the pathway-tier sequence
- How it closes or hands off to the next lesson ("The next lesson picks up...")

The wrapper is **scoped to the pathway-tier** (e.g. "Academic Writing — Introductory" has one wrapper around its lesson set). It is **not fixed boilerplate** — it flexes deliberately by:
- **Pathway:** Writing vs Criticality vs Presenting
- **Tier:** Introductory (more scaffolding) vs Advanced (assume prior knowledge)
- **Lesson-type:** Orientation lesson vs skill lesson
- **Context:** The overlay in use

When generating lesson copy, the wrapper is a conscious design decision — "how does the frame flex for this material?" — not a pasted-in constant.

---

## Relationship between layers

```
PATHWAY-TIER
└── Wrapper (connective framing around lessons)
    └── LESSON (content object / page)
        └── Six-part section flow (within lesson)
            ├── Shell (context-neutral prose)
            └── Context slots (context-specific fills)
```

The six-part section flow operates **within** a lesson. The wrapper operates **around** lessons at the pathway-tier level. These are distinct authoring concerns; do not conflate them.

---

## Portable-unit authoring discipline

Each lesson is authored as a **portable unit** from the start, enabling two deployment modes:

### Standard deployment (one SCORM per tier)

- One Adapt course per pathway-tier
- Menu-as-wrapper: the course menu provides the wrapper framing
- Lessons as pages within that course
- Gated by trickle where pedagogically appropriate
- **One SCORM package** uploaded to Moodle

Wrapping is native Adapt structure (menu/pages/trickle), NOT hyperlinks.

### Bespoke deployment (Moodle-assembled suite)

- Hand-assembled suite drawing lessons from multiple pathway-tiers
- Assembly at the Moodle level (or a lightweight wrapper course)
- Cross-package sequencing/completion is Moodle's job
- Hyperlinks only used here (Moodle level), not inside standard tiers

### What makes a lesson portable

A lesson is portable when it:

1. **Uses clean, non-colliding ids:** Each lesson's content objects/articles/blocks/components use a distinct id series (e.g. lesson 1 = co-400/a-400/b-400–b-430/c-400–c-435; lesson 2 = co-500 series).

2. **Has self-contained tracking:** TrackingIds are contiguous within the lesson and don't depend on sibling lessons' ranges.

3. **Has no hard dependencies on sibling lessons:** References to "the next lesson" are wrapper text, not structural dependencies. A lesson's internal content doesn't use another lesson's ids or require another lesson to function.

4. **Marks context slots by CSS class:** Discipline-specific content is identified by `_classes` markers, not by cross-lesson references.

This is the same "cut the seam early" discipline as the context slots: cheap to build in from the start, painful to retrofit.

---

## Verification

To confirm a lesson is portable, check:

- [ ] Its ids (co-xxx, a-xxx, b-xxx, c-xxx) are in a distinct range not overlapping with sibling lessons
- [ ] Its trackingIds are contiguous and don't reference other lessons' ranges
- [ ] No `_parentId` or other structural field references another lesson's ids
- [ ] Context slots are marked by `_classes`, not by cross-lesson wiring
- [ ] Wrapper text (lesson open/close) uses natural language, not structural dependencies

---

## Related documents

- `docs/authoring/book-to-adapt-mapping-workflow.md` — includes the three-layer model and portable-unit step
- `docs/authoring/portable-unit-and-shell-format.md` — wrapper vs six-part section flow distinction (moved here from component-mapping-artefact.md, SUPERSEDED under MA-1)
- `content/drafts/pilot/context-overlay-variation-analysis.md` — context-slot analysis for the pilot
- `content/drafts/pilot/overlay-tokens-lesson1.md` — inline token manifest for lesson 1
- `CLAUDE.md` — working conventions including portable-unit rule

---

*Established during pilot build phase. This discipline applies to all future lesson authoring.*
