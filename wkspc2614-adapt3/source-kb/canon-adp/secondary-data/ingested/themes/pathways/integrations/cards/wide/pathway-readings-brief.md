# Brief: practice, knowledge and practitioner self-identity for an academic practice

The brief the four drafting agents followed on 4 October 2026 (ing N-0156); digests of each pathway's cards were built in the session scratchpad from the long CSV and the plans.

A table of academic practices reads each practice's nine cards (i1 to e3) plus a foundation row (F, before university) and a level 8 row (L8, doctoral and professional). Each row is to be read three ways:

- **Practice**: what one does. An observable action, third person, starting with a verb. Concrete: what the student actually does, with what, for whom.
- **Knowledge**: what one knows and how one understands it. A noun phrase.
- **Practitioner self-identity**: who one is as a practitioner of this academic practice; the holistic whole, self-awareness. A noun phrase, usually "a ... who ...".

## The model to follow

These are the readings already written for Self-Development (the academic practitioner). Match their register, length and rise:

```
F:  ["describes self as a learner when asked and keeps to the tasks set", "what they are good at and want from study, in their own words", "a learner who sees identity as given rather than made"]
i1: ["talks about study as a practice with its own ways of working and names what an academic practitioner does", "what academic practice, an academic practitioner and graduate identity are", "a newcomer who sees that being a student is a practice one can take up"]
i2: ["keeps a learning record each week, logging what was done, strengths shown and goals set", "how a learning record works and what goes in it", "a student who keeps account of their own learning"]
i3: ["notices and notes when a task, a source or feedback touches what matters to them", "own values and what matters in study, named in own words", "a student beginning to recognise their values at work in study"]
d1: ["takes part in seminars and groups by the community's conventions and watches how experienced members work", "how academic communities shape identity and values, from the edge towards the centre, with integrity as shared values", "a participant learning the community's ways and values"]
d2: ["plans own development against values and goals, acts on feedback and checks progress against the plan", "how feedback, reflection and goals connect in a development plan", "a student taking responsibility for their own development"]
d3: ["changes how they study, take part or take feedback when they see their beliefs or background shaping it", "how own values, beliefs and background affect learning and taking part", "a self-aware practitioner whose values begin to steer choices"]
e1: ["writes and speaks about own academic identity and values with evidence, for a tutor, a panel or an employer", "what counts as evidence of identity and values and which evidence suits each reader", "a practitioner with a voice of their own, able to say who they are"]
e2: ["chooses a course of action when values conflict, acts on it and reviews own conduct afterwards", "own values as an ordered set and how they bear on conduct", "a practitioner whose conduct expresses an organised set of values"]
e3: ["examines and reworks own writing and judgements in the light of the assumptions and position they reveal", "own position as a knower and how identity and values shape what one notices, judges and writes", "a reflexive practitioner who examines and remakes their own identity"]
L8: ["authors own scholarly work and supports others' development, questioning own and the field's assumptions", "the field's assumptions and own part in making and changing them", "a practitioner who authors themselves and shapes the community's practice and identity"]
```

And the general row readings the whole table shares (yours are these made specific to the practice):

```
F: follows set tasks with guidance | the facts and ideas a task needs | a learner preparing to become a student
i1: recognises the practice in others' work and names its parts | what the practice is and its terms | a newcomer who knows the practice exists
i2: carries out one set method with support | the steps of that method | a student trying the practice
i3: checks own work against the method | own strengths and gaps in it | a student beginning to see themself as a practitioner
d1: compares ways of doing the practice | why the practice works as it does in a discipline | a participant learning the community's ways
d2: carries out the practice independently and adapts the method to the task | several methods and when each fits | a practitioner taking responsibility for own work
d3: plans monitors and adjusts own practice | own habits and their effects | a self-regulating practitioner whose values begin to steer choices
e1: chooses and justifies an approach to an unfamiliar task | criteria for choosing | a practitioner with a voice of own
e2: practises in complex and unpredictable settings and judges own conduct | how practice and its effects fit together | a practitioner whose practice expresses own values
e3: examines and changes own practice from its assumptions | own position as a knower | a reflexive practitioner who examines that identity itself
L8: originates practice that changes a field | a field's knowledge and own part in making it | a practitioner who shapes others' practice and identity
```

## Input

For each pathway id `<pid>` in your task, read `/tmp/claude-0/-home-claude-wkspc2600-uni/8e110491-2991-5d7a-8b00-c2560247b93c/scratchpad/pr/<pid>.txt` in full. For each row it gives the card (`cell`), its kind of knowledge and, where it exists, the card's full statement. F and L8 cells come from the practice's progression by level 3 and 8 (the bracket is the metacognitive stance). Read nothing else.

## Rules

1. Each reading must rest on that row's card: say what doing that card looks like, what one knows to do it, and who one is when one does it. Do not drift to another card's content.
2. Practice first and concrete: name the actual things done (searches a database, drafts and redrafts an introduction, rehearses to time, logs sources in a manager). Keep names the card uses (Gibbs, Kolb, Boolean operators, the four pillars).
3. Knowledge says what one knows and how one understands it, not a restatement of the practice.
4. Identity shows self-awareness growing up the rows: from a learner doing as asked (F), through a newcomer and a participant, to a practitioner with own voice and values, to reflexive (e3) and shaping others (L8). Name the practitioner by the practice (a searcher, a writer, a presenter, a critical reader ...), not a generic student every time.
5. Each reading 8 to 30 words. British English. No em dashes or en dashes. No Oxford commas. No semicolons. No "you" or "your". Lower-case first letter, no full stop, like the model.
6. Do not copy the card's wording wholesale: restate it as action, knowledge and identity.

## Output

Write `/tmp/claude-0/-home-claude-wkspc2600-uni/8e110491-2991-5d7a-8b00-c2560247b93c/scratchpad/pr/out/<pid>.yaml`, exactly:

```yaml
<pid>:
  F:  ["<practice>", "<knowledge>", "<identity>"]
  i1: [...]
  ... all eleven rows F, i1, i2, i3, d1, d2, d3, e1, e2, e3, L8 ...
```

Every string in double quotes; check it parses with `python3 -c "import yaml,sys; d=yaml.safe_load(open(sys.argv[1])); assert all(len(v)==3 for v in list(d.values())[0].values()) and len(list(d.values())[0])==11" <file>`.

Reply with one line per pathway: pid and "11 rows". Nothing else.
