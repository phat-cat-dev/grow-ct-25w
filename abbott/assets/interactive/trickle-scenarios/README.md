# Deep trickle scenarios

Open [the player and authoring workshop](index.html) directly in a browser.
It works offline: no server, framework, fonts or network services are required.

## Included scenarios

- [Project rescue](project-rescue.json): evidence, scope and learning clarity.
- [Source detective](source-detective.json): tracing claims and communicating limits.
- [Support conversation](support-conversation.json): privacy, listening and agency.
- [Team conversation](team-conversation.json): genuinely divergent follow-up
  decisions and four endings, with opportunities to return to a shared route.

The first three use branching consequences that rejoin later decisions, with
11 cards on a completed route. The fourth has different route lengths and endings.
All prose is original demonstration content, not a formal assessment.

Design informed by [UWE's guide to making branching online scenarios](https://digitallearning.uwe.ac.uk/making-branching-online-scenarios/):
define learning goals, plan plausible decisions and consequences, consider
alternative outcomes, and make room for reflection and replay.
The guide's cases, clinical scenarios, illustrations and wording are not copied.

## How playback works

- Only the first card is initially rendered. Choices reveal their selected
  destination with a fade. Unchosen branches are never inserted into the player.
- `continue` waits for a button; `choice` always waits for a learner decision.
- `auto` waits for its button unless the learner enables timed trickle.
  Its delay then reveals only its defined next card. Timers never choose answers.
- Earlier cards remain visible. Use Change decision or Return here to remove
  later cards **and their notes** before choosing another route.
- Restart clears the route and notes. Loading a scenario does the same.
  Download a route first if you want to retain it.
- Reflection is optional and does not gate progression.
- Timed reveals do not move keyboard focus. Button-driven reveals focus the new
  title without automatic scrolling. A hidden browser tab pauses timers.
- Pause cancels the pending timer; resuming starts its full delay again.
- Reduced motion shows each new card immediately, without fading.
- There is no automatic persistence, score, LMS tracking or real agent service.
  Route export is JSON for review, not a secure assessment result or resume file.

## Data template for a person or agent

Start with [scenario-template.json](scenario-template.json). It is already a
connected 11-card-deep scaffold with three two-option decisions. Replace every
bracketed placeholder, keeping IDs and routes unless you are changing the graph.
The editor also has a blank-template button.

```json
{
  "version": 1,
  "id": "small-example",
  "title": "A learning decision",
  "intro": "Audience, goal and context.",
  "start": "start",
  "nodes": [
    {
      "id": "start",
      "type": "choice",
      "title": "Which approach?",
      "body": "A specific situation with a meaningful tension.",
      "prompt": "What is your first instinct?",
      "choices": [
        { "label": "Inspect the evidence", "next": "inspect" },
        { "label": "Make an assumption", "next": "assume" }
      ]
    },
    {
      "id": "inspect",
      "type": "auto",
      "title": "What you discover",
      "body": "A plausible consequence.",
      "delayMs": 1800,
      "button": "Consider the outcome",
      "next": "end"
    },
    {
      "id": "assume",
      "type": "continue",
      "title": "A different consequence",
      "body": "Explain what happened without humiliating the learner.",
      "button": "Reflect",
      "next": "end"
    },
    {
      "id": "end",
      "type": "ending",
      "title": "Debrief",
      "body": "Connect the decisions to the learning goal.",
      "prompt": "What would you change next time?"
    }
  ]
}
```

### Authoring contract

Top level: `version: 1`, `id`, `title`, `intro`, `start`, `nodes`.
Each node: unique `id`, `type`, `title`, `body`, optional `prompt`.

| Type | Additional fields |
| --- | --- |
| `choice` | `choices`: 2–8 `{ label, next }` records; no `next` on the node |
| `continue` | `next`, optional `button` |
| `auto` | `next`, `delayMs` 500–30000, optional `button` |
| `ending` | No `next` or `choices` |

Maximum 200 nodes. Node IDs use letters, digits, hyphens and underscores.
Every node must be reachable from `start`; every link must resolve.
Cycles are rejected: use distinct retry nodes or the player's replay controls.
Reconvergence is supported. Every route must eventually reach an ending.
Titles/choice labels max 200 characters, body max 4000, prompt max 300.
Editor/import limit is 1 MB. All scenario text is rendered as text, never HTML.

Suggested agent brief:

> Fill this version-1 scenario template for [audience] learning [objective].
> Use [context], at least three substantial decisions, plausible alternatives,
> delayed or immediate consequences, and distinct outcomes where meaningful.
> Add optional reflection prompts and an ending that connects to the objective.
> Preserve valid node IDs, avoid cycles and unreachable nodes, and return only
> JSON. Do not imply clinical, legal or assessment authority.

Use Validate only before applying. Invalid input reports an error and leaves the
current player in place. Imported files go into the editor first, not into the
active scenario. Changing the example dropdown alone does not discard progress.

## Facilitated use

1. State the learning goal and ask learners to privately record an initial response.
2. Discuss options or take a group vote before pressing a choice.
3. Pause at consequences and ask what information or assumptions mattered.
4. At an outcome, export notes, revisit an earlier choice and compare routes.
5. Finish with an individual transfer question: what changes in real practice?

Avoid using animation, an elaborate story or unnecessary media as a substitute
for a meaningful decision. Pilot with subject specialists and representative
learners before using a scenario in teaching.

## Embed

Include `trickle.css` and `scenario.js`, then supply your JSON object:

```js
const player = TrickleScenario.mount(document.querySelector('#my-scenario'), data);
player.get();     // scenarioId, complete, ordered route/choice/note records
player.pause();
player.destroy(); // cancels timers/listeners and clears host
```

`TrickleScenario.validate(data)` throws explicit graph/content errors.
`trickle:progress` bubbles after advancing to a new card, with a snapshot of the
selected route. Restart, revisit and note edits do not emit this event; call
`player.get()` when exporting or reading the current state.
Do not mount twice on one host without destroying its previous player.
Host component styling is scoped to `.trickle-player`; `.trickle-workshop*`
styles only the authoring page.
Tokens: `--trickle-accent`, `--trickle-paper`, `--trickle-ink`,
`--trickle-muted`, `--trickle-line`, `--trickle-radius`, `--trickle-pad`,
`--trickle-fade-duration`. Defaults consume the existing theme tokens.
Set `color-scheme: light dark` on a standalone host for system fallback colours.

Regenerate built-in examples and JSON files with
`node .\assets\interactive\trickle-scenarios\build-examples.cjs`.
The generator is the source of the built-in examples; edit imported/custom JSON
separately. Run validation tests with
`node --test .\assets\interactive\trickle-scenarios\scenario.test.cjs`.
