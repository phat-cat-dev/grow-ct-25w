# Confidence check: before and after

[Open the offline template](index.html). Rate 1–12 topics from 1 (not yet
confident) to 5 (very confident), before and after a learning activity.
No rating is preselected. Every before/after rating is required for comparison;
incomplete or changed ratings never produce stale or partial results.

Results include grouped Chart.js bars, a complete data table, JSON export,
and plain buttons that programmatically highlight each topic's pair of bars
and open its tooltip. Inspired by the
[Chart.js programmatic-events example](https://www.chartjs.org/docs/latest/samples/advanced/programmatic-events.html);
uses `setActiveElements` on the chart and tooltip, then `update('none')`.
The same values are announced in text for keyboard/touch/screen-reader access.

Confidence is self-report, not competence, attainment, a pass/fail result or
evidence of learning gain. Decreased confidence can reflect better-informed
judgement. No average, percentage gain or assessment interpretation is assigned.

## Author and embed

Edit the topics in `topics.js` for direct/offline use. `topics.json` is the
equivalent data template for a person or agent; it is not fetched by the page.
Use unique alphanumeric/hyphen/underscore IDs and non-empty labels up to 160
characters. Then include:

```html
<link rel="stylesheet" href="confidence.css">
<div class="confidence-check" id="confidence"></div>
<script src="vendor/chart.umd.min.js"></script>
<script src="confidence.js"></script>
<script>
  const check = ConfidenceCheck.mount(document.getElementById('confidence'), {
    topics: [{id:'apply', label:'Apply this idea in practice'}]
  });
</script>
```

`check.get()` returns null until comparison, or a cloned
`{version:1,scale:{min:1,max:5},ratings:[{id,label,before,after,change}]}` object.
`check.highlight(index)` activates a zero-based topic;
`check.destroy()` removes chart, content and listeners. The bubbling
`confidence:results` event carries the result object.

Ratings remain in memory only and are lost on reload. Keep the page open between
before and after, or integrate persistence yourself. JSON export is results-only,
not a resume file. No LMS or backend exists. Changing ratings invalidates the old
comparison and disables export until recalculated. Clear ratings resets all.

Chart load/render failures are reported explicitly; table and JSON remain
available. Reduced motion disables chart animation, including when toggled
during playback. Theme tokens `--confidence-before`, `--confidence-after` and
`--confidence-accent` can be overridden; the table and text do not rely on colour.

## Local dependency

Chart.js 4.5.1 is pinned and bundled locally under `vendor/`, with its MIT licence.
No CDN is needed. To regenerate, run `npm ci` then `npm run build` from this folder.
Do not edit the vendor file manually.
