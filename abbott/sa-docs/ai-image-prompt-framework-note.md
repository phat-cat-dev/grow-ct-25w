# AI Image-Prompt Framework — Design Note

*Captured 29 July 2026. This is a queued idea, not a specification — needs its own design pass before becoming a workflow step or a Claude Code build task.*

## The idea

Add a stage to the course-design workflow where AI reviews a finished lesson's image placeholders and generates appropriate photoreal image-generation prompts for each one, tailored to the specific context pack (baseline / criminology / psychology / sports-journalism / future contexts).

## Why this matters

The 22 July commit ("Broaden asset tracking; add visual-assets step to the workflow") added a visual-assets step to `course-creation-workflow.md`, but that step doesn't yet define *how* images actually get generated — this idea would give it a concrete method.

## Two distinct image categories (worth separating from the start)

Abbott's thinking spans two related but distinct needs:

1. **Content placeholder images** — specific, per-lesson images illustrating a specific concept (see open questions below: context-specificity, not every placeholder needs one, etc.). Generated per-placeholder, tied to specific lesson content.
2. **Thematic background imagery** — part of the Cardiff Met theme's overall visual identity, likely more atmospheric/subtle (page backgrounds, section dividers, decorative elements) rather than illustrating a specific concept. These probably want to be generated **once per theme (or once per context, reused consistently)**, not regenerated per-lesson — closer to a design asset than a content asset.

These likely need different generation approaches and different places in the workflow: backgrounds are closer to theme-design work (decided once, applied broadly), content images are closer to per-lesson authoring work (decided per placeholder, tied to that lesson's specific content). Worth resolving what needs an image and what doesn't for each category separately, rather than treating "images" as one undifferentiated bucket.

### Background/content-visual coordination (VO-1 cross-reference)

**Added 29 July 2026, following VO-1 resolution (open-decisions.md #32).**

Thematic background imagery and W-OPEN Signpost content visuals (per VO-1) are **separate but coordinating decisions**, not independent ones. The theme design work needs to resolve how they interact per treatment type:

- **Hotgraphic / Narrative / Timeline / Flip cards:** These treatments have their own visual footprint. Does a background image still render behind/around the component, or does the component's own visual space functionally replace the need for one on that page? If both render, do they compete visually or complement each other?

- **Text only:** The Signpost block deliberately carries no content-level visual. Here the thematic background does all the atmospheric work. This is the cleanest case — no coordination conflict.

The theme design pass cannot assume these are automatically compatible. Each treatment type needs explicit consideration during theme design, not just content authoring.

**This is a design-time decision, not a build-time configuration.** The choice of Signpost treatment (made per-pathway at Stage 1 design per VO-1a) and the choice of background treatment (made during theme design) must be made aware of each other. Neither should be designed in isolation.

## Open design questions (needs resolution before build)

1. **Context-specificity.** Should route through the same context-pack mechanism lesson text already uses — an image for criminology should reflect that discipline's visual world, not a generic or baseline-default scene. This is the visual equivalent of the hardcoded-name ("Rhian") bug already found and queued for fixing in text content — the prompt framework needs to actively pull context, not default to one context's imagery everywhere.
2. **Visual consistency across a pathway/tier.** Multiple independently-generated photoreal images risk inconsistent style, lighting, or quality. Consider whether the prompt framework should enforce a shared visual "voice" (analogous to the written Voice Specification) — e.g. consistent lighting mood, photographic style, framing conventions — so a full tier doesn't look visually disjointed.
3. **Not every placeholder needs a photoreal image.** Hotgraphics are diagrammatic; some content may be better served with no image, an icon (see the separate Material Symbols icon-system decision), or an illustration rather than a photo. The framework needs a decision rule for *when* to generate a photoreal prompt at all, not an assumption that every placeholder gets one.
4. **Representation and bias.** AI image generation carries real risk of baked-in stereotyping (who's shown doing what, in what setting) unless deliberately guided. The prompt framework should include explicit representation/diversity guidance as a standing rule, not leave it to chance per-generation.
5. **Workflow placement.** Likely sits in `course-creation-workflow.md` as a step after content is finalised (so placeholders and their surrounding context are known) and before or alongside the theme pass. Needs a decision on exact sequencing relative to existing phases.
6. **Output format.** Does this stage produce ready-to-use image-generation prompts for a human to run through an external tool, or does it (via Claude Code / an agentic step) actually generate and place the images? Different scope and risk profile — worth deciding deliberately rather than assuming the more automated option.
7. **Rights/licensing of generated images.** Worth a brief check on the terms of whatever image-generation tool is used, particularly for a published, potentially commercially-distributed programme — not a blocker, just due diligence before this goes into production use.

## Relationship to other queued work

- Ties to `docs/authoring/template-v2-scope.md` Group 3 (open design questions) — should probably be added there as its own numbered item.
- Ties to the Material Symbols icon-system decision (also queued 29 July) — both are "what goes in a visual placeholder" decisions and might benefit from being resolved in the same design session.
- Ties to the context-pack architecture generally — any implementation needs to route through context packs the same way text content does.

## Status

**Not actioned.** Logged as a design note for a future dedicated conversation, not yet scoped as a build task.
