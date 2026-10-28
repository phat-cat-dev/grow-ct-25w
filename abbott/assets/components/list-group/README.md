# List groups with badges

Open [the examples](index.html). Three variants:

1. Static semantic list with right-aligned count badges.
2. Full-row resource links, descriptions and collection counts.
3. Selectable learning groups that update an adjacent prompt panel.

Copy [the basic HTML fragment](list-group.html) and include `list-group.css`.
Static lists and link groups need no JavaScript. `list-group.js` implements only
the demonstration learning-group selector; adapt its prompt records for your own
activity. Native buttons support Enter and Space, retain focus and expose the
selected state with `aria-pressed`. A status announces the new group and count.
Use unique panel/heading IDs if copying the interactive example.

Use `ul`/`li` for all variants. Put an anchor or button *inside* each `li` for
interactive rows; do not make informational rows pretend buttons. Badge text
includes a visually hidden count description for assistive technology. Badge
counts should describe the actual linked collection or displayed content.

Theme tokens: `--list-paper`, `--list-ink`, `--list-muted`, `--list-line`,
`--list-accent`, `--list-radius`, `--list-pad`. Defaults consume existing
`--surface-1`, `--ink`, `--ink-soft`, `--line`, `--accent`, `--radius` and
`--space-sm`. Layout uses flexbox, wrapping labels and non-shrinking badges.
Set `color-scheme: light dark` on your host for system-aware fallback colours.
Component rules are scoped to `.list-group`; demo rules use `.list-group-demo`.

No network, dependencies, storage or animation. The examples work offline.
