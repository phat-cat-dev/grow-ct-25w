# Process assets

Individual, offline-ready examples extracted from the archived process gallery:

- [Flowchart](./flowchart.html): Start, process, decision and return path.
- [Fork / join](./fork-join.html): two parallel branches converge.
- [Loop with counter](./loop-counter.html): three repetitions counted with the token.
- [Pipeline](./pipeline.html): a continuous stream through load, clean and save.
- [Show working](./show-working.html): annotated algebra and substitution check.

[Preview all five](./index.html). Each HTML document works directly from disk.
Copy its `<article>` into a page with `process.css` and `process.js`. No fonts,
frameworks, external images or network services are required.

Controls are local to each article; any number can coexist without ID conflicts.
Nothing auto-plays. Play/replay restarts the demonstration; Pause freezes drawing,
tokens and annotations. Speed (0.5–3x) restarts at the chosen speed so counter
events, delays and movement remain synchronised. Pipeline and parallel-flow
tokens loop until paused. All explanatory text remains readable while stopped.
Reduced motion and host `.no-motion` / `data-tm-no-motion="true"` suppress motion.

`ProcessAssets.mount(host)` mounts a dynamically inserted article and returns
`play()` and `destroy()`. Existing articles mount automatically on script load.

Override `--process-paper`, `--process-stage`, `--process-ink`, `--process-muted`,
`--process-accent`, `--process-line`, `--process-positive`, `--process-font`,
`--process-hand`, `--space-sm/md` and `--radius`. Map the `--process-*` colours to
your host theme tokens if embedding in a themed page. Their standalone fallbacks
are intentional: the asset's source classes cannot inadvertently pick up
unrelated page-global values.

The examples demonstrate ideas; the flowchart doesn't execute arbitrary
conditions, the pipeline doesn't process user data, and the algebra isn't a
calculation engine. Change the SVG labels/paths and explanation for your content.

Regenerate HTML from the known source gallery with:

```powershell
node .\assets\interactive\process\build-process.cjs
```

The generated files are the deliverables; the archived source is only needed
when regenerating them. Shared styles and runtime are hand-maintained.
