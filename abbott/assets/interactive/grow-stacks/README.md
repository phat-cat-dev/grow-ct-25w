# Interactive Grow stacks

Open [the comparison](index.html), [Adapt stack](adapt-core-base.html) or
[Grow stack](grow-core-base.html). Each page works offline with local CSS and a
classic script; no fonts, frameworks, storage or network services are required.

- Expand layer explanations using native keyboard-accessible disclosure headings.
- Walk through layers in their displayed build order, restart or show everything.
- Switch a visual token profile independently on each stack. This changes colour,
  spacing and corners, not architecture; it is not a LESS compiler.
- Check structure ownership with feedback and retry. Practice only, not a secure exam.

Progress and answers are intentionally temporary. Both stacks work independently
when displayed together. Profile switching never changes the layer text or order.
There is no animation, so reduced-motion users see the same presentation.

For reuse, iframe an individual page for style isolation, or copy its
`[data-stack]` section and load `stack-layout.css`, `stacks.css` and `stacks.js`
after the markup. The layout stylesheet includes document-wide foundation rules.
Theme tokens include `--h`, `--s`, `--ink`, `--surface-1`, `--accent`, `--mech` and
`--sty`. Light/dark follows the system; `data-theme="light"` or `"dark"` on the
document element overrides it.

Regenerate HTML and layout CSS from the original gallery with:

```powershell
node .\assets\interactive\grow-stacks\build-stacks.cjs
```

The source gallery is not modified. Edit the generator rather than generated HTML.
