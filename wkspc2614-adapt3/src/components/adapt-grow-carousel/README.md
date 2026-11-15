# adapt-grow-carousel

A **slide carousel** for the Adapt framework — a set of slides (image, title and
caption) shown one at a time, with previous/next controls and a row of dot
indicators. Use it for a short sequence a learner steps through at their own
pace: a plan, a gallery, a before/after set of panels.

Part of the **GROW** plugin set. Its colours, surfaces and spacing come from the
theme's `--ab-*` tokens (accent controls/indicators, base ink captions), so it
repaints with the active theme and has a dark mode for free.

## Behaviour

- **One slide visible at a time.** Previous/next move between slides; the dots
  jump straight to a slide.
- **Cycle** (`_canCycle`, on by default) wraps from the last slide back to the
  first and vice versa; with it off the controls clamp at the ends.
- **Auto-scroll is off by default** (`_shouldAutoScroll`) for accessibility and
  reliable completion.
- **Completes on view** — the component is marked complete when it scrolls into
  view, so it passes the trickle without the learner reaching the last slide.
- Optional image-framing looks are available as classes on the block
  (`cover` frames each slide to 16:9; `caption-overlay` lays the caption over the
  foot of the image under a scrim).

## Accessibility

- The carousel has `aria-roledescription="carousel"` and an `aria-label`
  (`ariaRegion`); each slide is a `role="group"` labelled "N of M", and
  non-current slides are `aria-hidden`.
- Previous/next and the indicators are native `<button>`s with visually-hidden
  labels; the slide track is an `aria-live="polite"` region while not
  auto-scrolling.

## Authoring

| Field | Purpose |
|---|---|
| `instruction` | Instruction text shown below the body. |
| `_shouldAutoScroll` | Auto-advance slides (off by default). |
| `_canCycle` | Wrap from the last slide back to the first. |
| `_items` | The slides. Each may carry a `title`, a `caption` and a `_graphic` (`src` + `alt`); `_id` is an optional stable id for analytics. |

See `example.json` for a full block.

## Settings

`_component` must be `growCarousel`; the target attribute is `_growCarousel`.
Requires Adapt framework `>=5.19.1`.

## License

GPL-3.0, consistent with the Adapt framework.
