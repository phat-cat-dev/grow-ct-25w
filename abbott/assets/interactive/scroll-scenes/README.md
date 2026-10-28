# Scroll scenes

[Open the demo](index.html) or reuse [the HTML fragment](section.template.html).
Original code, copy and CSS artwork; no images, external libraries, fonts or
network access required. Existing fade-in and scenario assets are unchanged.

## Embed

Include `scroll-scenes.css`, paste the fragment, then load `scroll-scenes.js`:

```html
<script src="scroll-scenes.js"></script>
<script>
  const player = ScrollScenes.mount(document.querySelector('.scroll-scenes'), {
    effect: 'zoom', snap: true
  });
</script>
```

Add/remove `data-scroll-scene` sections and their plain navigation buttons.
Buttons use zero-based `data-scroll-to` indices. Each scene needs a
`data-scene-content` wrapper. Mount after adding content; destroy and remount
if changing the scene count. Navigation, progress and status are optional.

Effects: `zoom`, `blur`, `fade`, `slide`, `none`. Use `player.set({effect:'fade'})`,
`player.go(1)`, `player.get()` and `player.destroy()`. Invalid effects, snap
values and indices throw explicit errors. `scroll-scenes:change` bubbles with
`detail.index` when the nearest scene changes. Destroy removes listeners and
restores content inline styles and viewport snapping.

Effects follow distance from the viewport centre and reverse when scrolling
back. There is no playback duration or automatic progression. A single
requestAnimationFrame update handles scroll changes, with resize observation
for wrapped content. This deliberately uses a JavaScript scroll-linked driver
rather than requiring browser support for CSS scroll timelines.

The viewport uses native scrolling and **proximity**, not mandatory snapping:
tall scenes remain scrollable. Scenes expand to fit content. Keyboard navigation
works by focusing the scroll region; focused links/buttons within a scene bring
that scene into view. Navigation does not move focus away from its buttons.
No content is hidden from assistive technology.

Without JavaScript, all scenes remain available through native scrolling.
System reduced motion and ancestor `.no-motion` / `data-tm-no-motion="true"`
disable visual effects; navigation is instant. Print shows all scenes clearly.
Theme tokens: `--scene-accent`, `--scene-ink`, `--scene-paper`, and optional
per-scene `--scene-colour`. Defaults consume existing theme tokens.

## References

User-supplied inspiration, not copied implementations:

- [Giana: CSS scroll-driven scroll-snapping animations](https://codepen.io/giana/pen/BabdgjB)
- [zrichard: Zoom and Blur background Image](https://codepen.io/zrichard/pen/vYqMEY)
- [Additional supplied reference](https://codepen.io/uriuriuriu/pen/DpKwGy)
  was unavailable during implementation; its effect was not assumed.

The blur study here acts on scene content, not an external background photo.

Additional supplied references could not be loaded or independently identified.
Their effects have **not** been implemented or assumed:

- https://codepen.io/ksenia-k/pen/jXbWaJ
- https://codepen.io/baarbaracrr/pen/KKovmGb
- https://codepen.io/brunopereiradonascimento/pen/ZjLNmO
- https://codepen.io/porsake/pen/JjydjLz
- https://codepen.io/MoorLex/pen/pRRzKx
