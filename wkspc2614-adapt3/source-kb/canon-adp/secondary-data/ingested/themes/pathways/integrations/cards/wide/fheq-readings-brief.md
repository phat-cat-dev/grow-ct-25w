# Brief: FHEQ descriptors read into an academic practice's practice, knowledge and self-identity

The brief the four drafting agents followed on 4 October 2026 (ing N-0176).

Each academic practice (pathway) has, at each row, a card and three readings: **practice** (what one does), **knowledge** (what one knows and how one understands it) and **practitioner self-identity** (who one is). Each reading has been matched to one or more FHEQ 2024 descriptors at the row's level.

The formula: **FHEQ descriptor + the pathway's practice and knowledge = the practitioner's practice, knowledge and self-identity.** For every matched descriptor, read it and ask:

1. What does this descriptor look like in this academic practice, at this row, in the student's disciplinary, professional and personal academic development? (`here`)
2. How is it evidenced across the disciplines? Give two or three concrete forms from different kinds of discipline (for example a lab report in the sciences, a case study in nursing or social work, a critical essay in history, a design portfolio in art). (`evidence`)

Write each as it bears on the reading it sits under: a practice entry says what the student does, a knowledge entry what they know and understand, a self-identity entry who they are becoming.

## Input

For each pathway id `<pid>` in your task, read `/tmp/claude-0/-home-claude-wkspc2600-uni/8e110491-2991-5d7a-8b00-c2560247b93c/scratchpad/fx/<pid>.txt`: per row, the card, then each reading with the FHEQ descriptors matched to it (id, dimension, paraphrase). Read nothing else.

## Rules

1. One entry per descriptor listed under a reading, in the order given. Do not add or drop descriptors.
2. `here`: 15 to 35 words, specific to the practice and the card; name what the student does, knows or becomes, and where the disciplinary, professional or personal side shows.
3. `evidence`: 10 to 30 words, naming two or three concrete forms of evidence in different disciplines, joined with commas and "and".
4. Your own words: do not copy the descriptor's paraphrase.
5. British English. No em dashes or en dashes. No Oxford commas. No semicolons. No "you" or "your". Lower-case first letter, no full stop at the end.

## Output

Write `/tmp/claude-0/-home-claude-wkspc2600-uni/8e110491-2991-5d7a-8b00-c2560247b93c/scratchpad/fx/out/<pid>.yaml`:

```yaml
<pid>:
  i2:
    practice: [{id: "fheq-2024/4.10.b4", here: "...", evidence: "..."}]
    knowledge: []
    identity: [{id: "...", here: "...", evidence: "..."}]
  ... every row in the input, in order ...
```

Every string in double quotes; check it parses with `python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))" <file>`.

Reply with one line per pathway: pid and the number of entries written. Nothing else.
