# Brief: FHEQ equivalences for an academic practice's readings

The brief the four drafting agents followed on 4 October 2026 (ing N-0174).

Each academic practice (pathway) has, at each row, a card and three readings: **practice** (what one does), **knowledge** (what one knows and how one understands it) and **practitioner self-identity** (who one is). Your job: for each row, find the FHEQ statements that answer each reading, and write one sentence on how the practice at that row relates to the **discipline** and to the **practitioner**, as the FHEQ frames it.

## Input

1. `/tmp/claude-0/-home-claude-wkspc2600-uni/8e110491-2991-5d7a-8b00-c2560247b93c/scratchpad/fq/fheq.txt`: every FHEQ 2024 statement at levels 4 to 8, as `id | dimension | paraphrase`. Read it in full first.
2. For each pathway id `<pid>` in your task, `.../scratchpad/fq/<pid>.txt`: for rows i2 to L8, the FHEQ level, the card, the ids the card already cites, and the three readings.

Read nothing else.

## Rules

1. Use only statements at the row's FHEQ level (given in the row header). Copy ids exactly as in fheq.txt (`fheq-2024/4.15.b5`).
2. For each reading, list 1 to 3 ids that genuinely correspond. Rough guide: knowledge usually matches threshold outcomes on knowledge and understanding; practice matches threshold outcomes on applying methods and the wider abilities; self-identity matches the employment qualities (responsibility, initiative, decision-making, learning ability) and the statements on autonomy, the limits of knowledge and own development. Use judgement: a statement fits only if it says what the reading says, at its level.
3. If nothing at that level fits a reading, give an empty list. Do not stretch.
4. `relation`: one sentence, 15 to 35 words, on how this row's practice relates to the discipline (its knowledge, methods, conventions, forefront) and to the practitioner (autonomy, responsibility, professional or scholarly identity), grounded in the ids chosen. Specific to the practice. British English, no em dashes, no Oxford commas, no semicolons, no "you".
5. Note in `new` which of your ids are not among the card's existing framework ids (compare the number part: `4.15.b5` matches an existing `4.15.b5`; CQFW ids like `l6/...` never match).

## Output

Write `.../scratchpad/fq/out/<pid>.yaml`:

```yaml
<pid>:
  i2: {practice: [ids], knowledge: [ids], identity: [ids], relation: "...", new: [ids]}
  i3: {...}
  ... d1, d2, d3, e1, e2, e3, L8 ...
```

Every string in double quotes; ids as quoted strings; check it parses with `python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))" <file>`.

Reply with one line per pathway: pid, rows written, how many ids in total and how many are new. Nothing else.
