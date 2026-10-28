# adapt-grow-promptbuilder (GROW)

A **prompt generator**. The learner builds a learning prompt from a **Role**, a
**Function** and some **Context**, using example chips (or typing their own). The
parts assemble live into a full prompt they can copy and take to a real AI tool.
It teaches the Role/Function/Context framework by doing, and completes once every
part is filled. It assembles prompt *text* only — it does not call an AI.

## Authoring

```json
{
  "_component": "growPromptBuilder",
  "displayTitle": "Build a learning prompt",
  "body": "<p>A strong prompt has three parts. Build one below.</p>",
  "instruction": "Pick a chip or type your own in each box.",
  "_assembleTemplate": "Act as {role}. {function} Context: {context}.",
  "_assembledLabel": "Your prompt",
  "_copyText": "Copy prompt",
  "_whyText": "A role, a clear task and your context make the answer specific - and make you do the thinking first.",
  "_setCompletionOn": "allFilled",
  "_parts": [
    { "_key": "role", "label": "Role", "help": "What should the AI act as?", "placeholder": "Act as...", "_chips": ["a supportive tutor for a first-year", "a critical friend", "an expert examiner"] },
    { "_key": "function", "label": "Function", "help": "What should it do?", "placeholder": "Explain / quiz / give feedback...", "_chips": ["explain this three ways: simple, intermediate, advanced", "quiz me and give feedback on my answers", "play devil's advocate against my argument"] },
    { "_key": "context", "label": "Context", "help": "Your level, module, what you have covered.", "placeholder": "I am studying...", "_chips": ["I am a first-year studying {{context}}", "I keep confusing two key terms", "I have already read the set chapter"] }
  ]
}
```

- `_assembleTemplate` uses `{key}` placeholders matching each part's `_key`.
- Chips append their text into that part's field; typing works too.

Like the other GROW components, the view calls `setReadyStatus()` itself.
