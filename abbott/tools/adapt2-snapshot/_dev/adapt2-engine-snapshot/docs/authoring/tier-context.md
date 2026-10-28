# Tier context — how to author the tier-sensitive conclusion slots

**Status:** draft, 10 October 2026. A consultable **tier context** the authoring
agent reads (or is directed to) when filling the slots named below, so a
conclusion is pitched and framed for the course's tier. It changes the
**instruction**, not the page/lesson template.

**What this is / is not.** This is *not* `tier-specification.md` (which defines
what introductory / intermediate / advanced *mean* — demand, cognition, voice
band). This is the thin, actionable layer on top: for a short list of
**tier-sensitive slots**, how to use the slot at each tier — heading, content
brief, and whether the slot applies at all. Most slots are tier-neutral and are
not listed here; only the ones whose *content depends on where the course sits
relative to its siblings* are.

**Scope (deliberately narrow).** Two conclusion slots, both in the close
wrapper (`design-kb.skeletons.json`, `skeletons/wrapper-close`):

- `practice-connection` — "In real academic practice". A coupled `palette/text`
  slot that already carries a `standingContextPrompt` (the *subject* axis). The
  tier context adds the *tier* axis beneath it.
- `where-next` — "Where this goes next". A fixed furniture slot, `required:
  false` — already marked optional **because the terminal (advanced) tier omits
  it**. This doc states that rule in full and the framing for the tiers that do
  carry it.

## The two mapping axes

A conclusion points the learner outward in two directions. The tier governs how
much of each, and in which direction:

- **Sideways (pathway → pathway)** — "put it into practice": how this practice
  connects to the *other* academic-practice pathways (Writing, Criticality,
  Reflection…). Horizontal. Driven by the pathway relationship table
  (`design-kb.pathways.json` `routes`; see `agent-author-metadata.md`).
- **Forward / back (tier → tier)** — "go deeper / look back": the *higher and
  lower tiers of the same pathway*. Vertical. Applicability differs by tier,
  because introductory has nothing below and advanced has nothing above.

## `where-next` — "Where this goes next" by tier

| Tier | Applies? | Heading | Content brief |
|---|---|---|---|
| **Introductory** | yes | *Where this goes next* | **Forward only.** Name the next tier of this pathway as the deliberate next step, and outline what it adds. No "look back" (nothing below). Encouraging; concrete. |
| **Intermediate** | yes | *Building on this* | **Forward *and* back.** Briefly connect to the introductory groundwork it assumes, then point up to the advanced tier and what it extends into. |
| **Advanced** | **no — omit the slot** | — | Terminal tier: there is no "next tier up". Do not author a forward step; the outward move collapses into `practice-connection` (sideways). This is why the slot is `required: false`. |

## `practice-connection` — "In real academic practice" by tier

The subject recast (`standingContextPrompt`) still applies; the tier sets *how
far outward* and *how self-directed* the framing is. Sideways (pathway) emphasis
grows with tier.

| Tier | Heading | Content brief | Sideways (pathway) rule |
|---|---|---|---|
| **Introductory** | *In real academic practice* | How to start applying this practice in current study; first concrete actions. Light sideways reach. | Name at most one strongly-related pathway, as "you'll also use this when you…". |
| **Intermediate** | *In real academic practice* | Applying it across modules and tasks; begins to connect practices. | Draw the 2–3 strongest pathway links from the relationship table; show the transfer. |
| **Advanced** | *Into your own practice* | Self-directed extension, cross-pathway transfer, contribution — not "how to apply the basics". Carries the outward move that `where-next` no longer does. | Full sideways map: how this practice integrates with the others in independent work. |

## Resolution order (how the agent consults this)

For a slot authored at tier *T*, subject *S*, mode *M*:

```
tier context (this doc) for T   →  sets heading + brief + applicability
  then subject axis (standingContextPrompt / CXP pack for S)
    then mode (agentAuthorWritten / agentAuthorDialogue)
```

Tier is resolved **first** (it can omit the slot entirely, e.g. advanced
`where-next`), then the subject recast and mode layer on top — the same
`(tier, mode)` selection specced in `docs/authoring/agent-author-metadata.md`.

## Generalises to a level axis

The tier axis is keyed to our introductory / intermediate / advanced. If
institutional **modules** are ever authored, the same structure keys on **FHEQ
level** instead (L4/L5/L6/L7), via the tier→level mapping already held in
`design-kb.tier-bands.json` (`indicativeLevels`) and the correspondences well's
dual axes (`catalogue/context/correspondences.json`, `rows[].meta` = Tier +
Indicative level). A level-authored module would carry a `level-context` of the
same shape as this doc; the forward/back and sideways rules port directly.

## Landing it (follow-on, governed)

Wiring this into the agent means tier-keying these two slots in
`design-kb.skeletons.json` — a tier-keyed `agentAuthor` block (or a
tier-applicability flag) on `practice-connection` and `where-next`, resolved per
the order above. Per `agent-author-metadata.md`'s Governance section that is a
`kbVersion` bump on the skeletons store plus a rule in
`tools/validate-design-schemas.py`, so the new shape is checked, not just
tolerated. This document is the prose source for that landing; the skeletons
wiring is the next step, not done here.
