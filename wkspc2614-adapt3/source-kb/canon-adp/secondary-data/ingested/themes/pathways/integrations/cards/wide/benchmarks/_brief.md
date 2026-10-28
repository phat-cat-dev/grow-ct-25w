# Brief: subject benchmark readings for the wide table

The brief each drafting agent followed on 4 October 2026 (ing N-0154); digests were built from the 54 runs' records (id, level, heading, domain, about, paraphrase) into the session scratchpad. Checked afterwards by `check-benchmark-readings.py`.

You draft, for each QAA subject benchmark statement named in your task, three short readings at each level where the benchmark speaks: **practice** (what a practitioner of the subject does), **knowledge** (what they know) and **practitioner self-identity** (who they are as a practitioner of the subject). These sit beside a table of academic practice whose general rows read, for example:

- d3 (level 6): practice "plans monitors and adjusts own practice"; knowledge "own habits and their effects"; identity "a self-regulating practitioner whose values begin to steer choices"
- e3 (level 7): practice "examines and changes own practice from its assumptions"; knowledge "own position as a knower"; identity "a reflexive practitioner who examines that identity itself"

Yours are the same three readings made specific to the subject.

## Input

For each benchmark `<slug>`, read `/tmp/claude-0/-home-claude-wkspc2600-uni/8e110491-2991-5d7a-8b00-c2560247b93c/scratchpad/bm/<slug>.txt` in full (use offset/limit to page through a long file; read every line). Header lines: RUN, TITLE, LEVELS. Then one statement per line:

`<id> | <level> | <headingPath> | <domain> | <about> | <paraphrase>`

Work only from these lines. Do not open any other file; do not look for the issuer's text.

## Where readings go (rows)

- `d2`: level 5 statements (`fheq:5`), only if the benchmark has them.
- `d3`: level 6, the threshold standard and the level 6 content statements (subject knowledge, subject skills, generic skills).
- `e2`: level 6, the typical and excellent standards (more autonomy, judgement, originality). If the benchmark has no separate typical or excellent standard, draw e2 from the more demanding level 6 statements and say so in `note`.
- `e3`: level 7 statements (`fheq:7`), only if the benchmark has them.

No other rows. A benchmark with only level 7 statements has only `e3`.

## Output

Write `/home/claude/wkspc2600-uni/adp/claude/adp-relay/sandboxes/ing/integrations/cards/wide/benchmarks/<slug>.yaml`, exactly this shape:

```yaml
slug: <slug>
name: "<subject name as in TITLE, short, with year, e.g. Psychology (2023)>"
run: "<the RUN value>"
subject: "<one sentence: what the subject studies and what it is for, in your own words>"
subjectIds: [<1 to 4 ids, usually level none, that ground the sentence>]
rows:
  d3:
    practice: "<starts with a verb, third person, e.g. designs and runs ethical studies of behaviour ...>"
    knowledge: "<a noun phrase, e.g. the main theories of mind and behaviour and how ...>"
    identity: "<a noun phrase, e.g. a psychologist in training who ...>"
    ids: [<3 to 8 statement ids that ground these three readings>]
  e2: { ... same keys ... }
  e3: { ... same keys, only if level 7 exists ... }
note: "<optional: anything a reader should know, e.g. no typical or excellent split>"
```

## Rules

1. Every id you list must appear in the input file, at the level of the row it grounds (level 6 ids for d3 and e2, level 7 for e3, level 5 for d2; level none only in `subjectIds`). Copy ids exactly.
2. Each reading 10 to 35 words. Plain, specific, active. British English. No em dashes. No Oxford commas. No semicolons. Avoid "you".
3. Your own words. Do not copy more than six consecutive words from any paraphrase.
4. Make the readings specific to the subject: name its methods, objects, settings and values. A reading that would fit any subject is a failure.
5. Practice is what one does; knowledge is what one knows; identity is who one is as a practitioner of this subject: values, ethics, responsibilities, a professional or disciplinary self. Ground identity in statements on ethics, values, professionalism, self-reflection or graduate roles where they exist. Where the benchmark gives nothing for identity at that level, write the reading from what it does give and end it with " (ing's reading)".
6. e2 must read as a step beyond d3, and e3 beyond e2.
7. Quote every string value in double quotes; check the YAML parses (`python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))" <file>`).

When all your files are written and parse, reply with one line per benchmark: slug, rows written, and any note. Nothing else.
