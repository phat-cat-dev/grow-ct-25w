# Markdown stubs from Handlebars

Two templates that generate a Markdown file with YAML front matter and a body
skeleton, so a new lesson or course starts with its front matter already filled in.

| File | Role |
|---|---|
| `lesson-stub.md.hbs` | Lesson template, in the shape of `frontmatter_spec.md` section 3. |
| `course-stub.md.hbs` | Course template, in the shape of `course_frontmatter_spec.md` section 4. |
| `lesson-stub.defaults.json`, `course-stub.defaults.json` | Placeholders for anything you leave out. |
| `render-stubs.js` | Renders either template. Registers the helpers and sets `noEscape`. |
| `lesson-example.md`, `course-example.md` | Output from the sample data in the other folders. |

## Use

```
npm install handlebars js-yaml        (js-yaml is only for --check)

node render-stubs.js lesson record.json --course course.json --out lesson-03.md
node render-stubs.js course course.json --out course.md
```

`record.json` can hold as little as `{ "id": "lesson-x-01", "title": "My lesson", "sequence": 1 }`.
Everything else falls back to the placeholders. Add `--check` to parse the front
matter back and confirm it equals the data you supplied. `--date YYYY-MM-DD` sets
created and updated (default today).

## Why the helpers

The templates are not HTML, so they compile with `noEscape: true`. Without it
Handlebars turns an apostrophe into `&#x27;`. Three helpers keep the YAML valid:

- `{{q x}}` writes a YAML-safe value: strings are double-quoted and escaped, lists are written `["a", "b"]`, missing values become `null`. A title such as `It's a "quoted" & tricky: title` survives intact.
- `{{e x}}` writes enum values bare (`draft`, `en-GB`, `formative`) and quotes anything else.
- `{{{fold text 4}}}` wraps prose onto folded `>` lines, as in the spec.

## Derived, not retyped (spec section 5)

If you do not supply them, the script derives:

- **Lesson:** `course_id` and `parent_id` from the course, learner-facing duration from `estimated_duration_minutes`, level from the course pitch, learner objectives from the lesson outcomes.
- **Course:** duration from the lesson estimates, level from `audience.learner_pitch`, learner objectives from the course outcomes.

An explicit `null` counts as "not supplied", so it is derived too.

## What the check guarantees

`--check` parses the YAML you generated and compares it with the data you passed
in. It ignores key order and treats null the same as missing. It fails if any
value differs. It warns if your input has a field the template does not write, so
nothing is dropped silently.

## Going the other way

Markdown with front matter is read back with a parser such as gray-matter or
js-yaml. That gives you the front matter as data and the body as text, which you
can pass straight into `lesson-record.hbs`, `lesson-frontmatter.hbs` or the JSX
components.

## Notes

- The body lists (outcomes, lessons table) are generated once as a starting point. After that the front matter is the authority: regenerate the lists if the data changes.
- Placeholders such as `[Lesson title]` are deliberately obvious so they are easy to find and replace. Do not leave invented sources or review approvals in a stub.
- The stub does not state that anything is optional, saves answers or affects completion. Those claims need verifying in Adapt or SCORM first.
