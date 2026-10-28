S = '/home/claude/wkspc2601-library/ingested/standards/ingest-std-qaa-enterprise-2018-guidance/run-src'
JUDGE = S + '/eee_j.py'
SLUG = 'qaa-enterprise-entrepreneurship-2018'
PREFIX = 'qaa/enterprise-2018'
_ns = {}; exec(open(JUDGE).read(), _ns); OUTTHEME = _ns['OUTTHEME']; STAGES = _ns['STAGES']
GU6ROWS = open(S + '/gu6_rows.md').read()

FRONT = '''---
id: std:doc:qaa-enterprise-2018-guidance
title: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers"
profile: standards/guidance   # proposed variant (D-std-0011, P5b); not yet in the profile
profileVersion: 0.1.6-draft
issuer: The Quality Assurance Agency for Higher Education (QAA)
kind: guidance
theme: theme:enterprise
jurisdiction: [England, Wales, Scotland, Northern Ireland]
subjectScope: universal
subjects: []
edition: January 2018 (QAA2042)
published: 2018-01
status: current   # as at the held text; not checked against QAA's site (Part E)
supersedes: "Enterprise and entrepreneurship education: Guidance for UK higher education providers (QAA, 2012)"
heldText: {{ method: sha256-bytes, raw: {raw}, normalised: {norm} }}
original: {{ method: sha256-bytes, pdf: c11bde8113a7d57d84ba8f8400aab80306027f6de167777ac5217e4356b3d3ff, held: no }}
licence: none read yet
parts:
  S: "full: 103 statements in eleven families"
  GU: "guidance analysis: families, progression, employability, framework and criteria links, pathways, the benchmark web, pedagogy handed on"
  B: "the guidance's defined terms"
  C: "none (the guidance sets no process standards bodies must follow)"
pins: {{ structure: 0.13.0-draft, template: "guidance 0.1.0-draft (proposed)", runFrame: 0.1.1-draft, runLayer: 0.5.0-draft }}
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0056
passes:
  P1: "2026-10-03, std (claude.ai, META Project): read direct from Abbott's PDF (05:40); built 05:52"
  P2: "skipped: read direct from the issuer's PDF"
  P3: open
version: 0.1.2
---
'''

HEAD = '''<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.6.1-draft under the proposed standards/guidance variant (template wpk-0016-ingest-pd-template-standards-guidance.md 0.1.0-draft), with the guidance analysis Part GU -->
# Enterprise and Entrepreneurship Education (QAA, 2018)

> Run 0056, P1 by std. **A guidance document read for its standards statements** (Abbott, 05:40): what it says a student or graduate should be able to do, be or show, and what it asks educators and providers to offer so that students can. The teaching ideas it carries (learning about, for and through enterprise; experiential learning; EntreComp; Venture Creation Programmes) go to theory ingest and are only named here (GU7). Every link to a framework statement, a marking criterion, a benchmark or a pathway is our reading and marked `inferred`.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's 2018 guidance on enterprise and entrepreneurship in UK higher education: a cross-cutting theme, written for any subject. Reach for it to say what an enterprising graduate can do (23 outcomes in seven themes), how that capability grows (four stages from awareness to effectiveness), what teaching should give students the chance to do, how such learning can be assessed, and how enterprise sits beside employability. It sets no levels and no thresholds: its statements are level-free and lean on the frameworks and the benchmarks for both.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
The guidance defines enterprise (generating ideas and applying them in practical settings) and entrepreneurship (applying enterprise to create cultural, social or economic value, sometimes through a new venture), and keeps both apart from employability, for which it takes Knight and Yorke's (2003) definition. Its standards content falls into eleven families: a principle of opportunity for every student, aims, a vocabulary of behaviours, attributes and competencies, assessment goals, a four-stage learning journey, the qualities of an entrepreneurial mindset, 23 graduate outcomes, 33 delivery opportunities, nine assessment considerations, the educator's role (after SFEDI's occupational standards) and five marks of an entrepreneurial institution. Most statements are bridges: capabilities that serve both study and work (GU3).

## Part S Standard

### S1 Identity
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers"
edition: January 2018
dates: { published: 2018-01, other: ["first edition 2012"] }
kind: guidance
code: QAA2042
partners: "named in the guidance's Appendix 3 (enterprise educator and entrepreneurship education bodies)"
heldText: wkspc2601-library/txt/qaa-2018-enterprise-entrepreneurship-education-guidance-standard.norm.txt
```

### S2 Purpose and scope
<!-- label: both; status: drafted; basis: primary -->
Written for educators in any subject and for the providers that support them, the guidance aims to help embed enterprise and entrepreneurship in curricular, co-curricular and extracurricular learning. It states its principle at the start: every student should be able to take part, in a form that fits their subject. It is advisory. Unlike a framework or a benchmark it carries no expectation that providers meet it, and it sets no level; its "should" statements say what good provision looks like.

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
Foreword; introduction and context (the value, the aims and vision, policy context in the UK and abroad); definitions and distinctions (enterprise, entrepreneurship, employability, enterprise education, entrepreneurship education, entrepreneurial education, and how employability, enterprise and entrepreneurship relate); delivering enterprise and entrepreneurship education (the educator's role, delivery, assessment, the gateway triangle, EntreComp, the four-stage journey); graduate outcomes in seven themes, each with its delivery opportunities; evaluation and impact; the supporting institution; Venture Creation Programmes; three appendices (resources, the 2018 advisory group, partner organisations). The standards statements are cut from the definitions, the journey, the outcomes and delivery lists, the assessment list, the educator list and the institution list (GU1).
'''

MID = '''
### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary for the absence of levels; inferred for the alignment -->
The guidance names no FHEQ, FQHEIS or CQFW level. Its outcomes describe a graduate at the end of study and its four stages describe growth across a course. GU2 reads the stages against the frameworks' levels; GU4 lists the framework statements each record most resembles. Neither is the issuer's.

### S6 Themes
`theme:enterprise` (this document is the theme's reference text); `theme:esd` (the definitions tie green and social entrepreneurship to sustainability education and cite QAA and HEA's 2014 ESD guidance, now replaced by std:doc:qaa-advancehe-esd-2021-guidance); employability (defined, kept separate, GU3).

### S7 Relations
```yaml
- { type: themeReference, target: theme:enterprise }
- { type: supersedes, target: "QAA enterprise and entrepreneurship guidance 2012 (not held)" }
- { type: cites, target: "QAA and HEA, Education for Sustainable Development (2014); replaced by std:doc:qaa-advancehe-esd-2021-guidance", basis: primary }
- { type: citedBy, target: "36 of the 54 subject benchmark statements held (GU6)", basis: primary }
- { type: citedBy, target: std:doc:qaa-advancehe-esd-2021-guidance, note: "its employers and enterprise section and resources", basis: primary }
- { type: mapsTo, target: std:doc:qaa-fheq-2024-framework, basis: inferred, note: "20 records linked (GU4)" }
- { type: mapsTo, target: std:doc:bristol-generic-2024-assesscriteria, basis: inferred }
- { type: mapsTo, target: std:doc:cardiffmet-generic-2020-assesscriteria, basis: inferred }
- { type: handsTo, target: "theory ingest (ing): the pedagogy in GU7" }
- { type: relatedTo, target: "ing:doc for Advance HE's PSF 2023 (run 0053): staff standards beside this guidance's educator family", basis: inferred }
```

### S8 Currency and review
<!-- label: both; status: drafted; basis: primary -->
January 2018, replacing the 2012 edition. Whether QAA has revised it since has not been checked (Part E, E1).

### S9 Commentary (optional)
<!-- label: practitioner; status: drafted; basis: inferred -->
The guidance writes in three voices. To students and graduates it says what they will become ("should be able to"); to educators it lists the chances teaching should give; to institutions it lists commitments. Only the first is a standard in the sense the frameworks use. The other two are conditions for meeting it, and we keep them because they say what a student can expect to be offered (student versions in S4a where that holds).
'''

def _stages():
    lv = {'awareness': ('L4', 'first year: knowing what enterprise is and why it matters to you', '4.10 (CertHE)'),
          'mindset': ('L4 to L5', 'seeing yourself as enterprising; motivation and resilience', '4.10, 4.12'),
          'capability': ('L5 to L6', 'doing it: designing, spotting and acting on opportunities in guided projects', '4.12, 4.15'),
          'effectiveness': ('L6 to L7', 'self-directed, with external clients, at the transition to work, venture or further study', '4.15, 4.17')}
    rows = []
    for k, name, focus, mode in STAGES:
        l, gloss, fh = lv[k]
        rows.append(f'| {k} | {name} | {gloss} | {l} | {fh} |')
    return '\n'.join(rows)

GU2 = '''
### GU2 Progression
<!-- label: both; status: drafted; basis: primary for the stages; inferred for the levels -->
The guidance's progression model has four stages, each named and described, with a teaching mode for each (education about, for and through enterprise; the model itself goes to theory ingest, GU7). It does not tie a stage to a level or a year; it says only that effectiveness comes near the end of study. Read against the frameworks, the stages fall like this:

| Stage | Name | What it means for the student (our gloss) | Level (our reading) | FHEQ descriptors |
|---|---|---|---|---|
''' + _stages() + '''

**What changes from stage to stage.** Three things move together, and they are the same three the FHEQ's descriptors move: *autonomy* (taught, then guided, then self-directed), *context* (the classroom, then simulations and projects, then live clients and ventures) and *uncertainty* (the outcomes ask graduates to work where change, ambiguity and risk are expected, which is the master's descriptor's "complex and unpredictable situations"). The guidance adds a fourth that the frameworks lack: *identity* (the mindset stage is about seeing yourself as enterprising).

**Suggestion: a levelled outcome ladder.** The 23 outcomes are level-free. To use one as a module learning outcome, keep its object and change its verb and context by stage. Three examples, ours (`suggested`):

| Theme | Awareness (L4) | Capability (L5 to L6) | Effectiveness (L6 to L7) |
|---|---|---|---|
| opportunity | describe how opportunities arise in your subject | identify and analyse an opportunity and plan a response | evaluate competing responses to an opportunity under uncertainty and lead one |
| reflection | describe your own enterprising strengths | review a project you took part in and set development goals | evaluate your own development across a live project and act on the gaps |
| communication | explain an idea to peers | present a proposal to a stakeholder and respond to questions | persuade external stakeholders of an idea's value, financial, social or environmental |

The verbs follow the FHEQ document's verb ladder (std:doc:qaa-fheq-2024-framework, SL3): describe and explain at L4, apply and analyse at L5, evaluate and critically review at L6, lead and act autonomously in unpredictable contexts at L7.
'''

GU3 = '''
**Reading.** The guidance is an employability document that declines the word: it keeps employability (Knight and Yorke's achievements that make employment more likely) separate from enterprise (a way of acting) and entrepreneurship (creating value), and its figure on the three shows them overlapping. In its statements, 43 name work, ventures, markets or stakeholders outright (`direct`) and 59 describe capabilities that hold as well in study as at work (`bridge`): creativity, decision-making, reflection, resilience. Only one stays within study. Direct statements cluster in the opportunity, implementation, communication and digital themes, and in the institution family (intrapreneurship, alumni, business links).

**Suggestions.**
1. Treat the `bridge` statements as the link between academic outcomes and professional competence: each one has an academic face (an assessed criterion, GU4) and a work face (an employer's competency). A module outcome built from a bridge statement can name both.
2. Treat the `direct` statements as the guidance's professional competencies. They are the ones a benchmark's employability paragraph most often echoes (GU6) and the ones a placement, live brief or venture module would assess.
3. In the standards profile, record `employability` on every guidance statement (direct, bridge, academic) and, later, on benchmark statements too, so that a query for "what professional competence does this subject's standard build" can run across documents.
'''

GU4 = '''
**Reading.** Twenty records sit close to an FHEQ statement, almost all at Level 6 (4.15: dealing with complex issues, communicating to specialist and non-specialist audiences, the qualities for employment) or Level 7 (4.17: deciding in complex and unpredictable situations, independent learning, initiative and personal responsibility). The guidance's outcomes are, in effect, the FHEQ's "wider abilities of typical holders" rewritten for enterprise. Against the marking criteria, Bristol's skills criteria (problem-solving, insight, decision-making, self-management, communication, teamwork) take most links, because Bristol writes criteria for practical and professional abilities that Cardiff Met's generic grid folds into argument, analysis, research and presentation.

**Suggestions for assessment.**
1. The guidance's three assessment modes line up with three assessment forms: learning *about* enterprise with essays and examinations (Cardiff Met's argument and analysis rows), learning *for* it with practical tasks and pitches (Bristol's problem-solving and communication rows), learning *through* it with reflective portfolios (Bristol's insight and self-management rows). A module can say which mode it assesses and borrow the matching criterion rows, banded on the UK marking scale (std:doc:bristol-generic-2024-assesscriteria AC3).
2. Two of its considerations need a criterion neither grid has: crediting temporary failure that is reflected on, and judging process where the outcome cannot be known in advance. A guidance-derived criterion row ("learning from setbacks", banded from description of what went wrong at the pass band to evaluated change of approach at 70 and above) would fill that.
3. Teamwork with individual marks (peer review, contribution audits) fits Bristol's teamwork criterion; the guidance's point is that the individual's share be evidenced, not assumed.
'''

GU5 = '''
**Reading.** The guidance spreads across nine of the thirteen pathways but leans on five: work-based and experiential learning, criticality, reflective practice, creativity, and starting, progressing and succeeding. It is the strongest source we hold for the **creativity** pathway (no framework names creativity as a capability; this guidance makes it the first outcome theme) and for **work-based and experiential learning** (live projects, placements, ventures). Reflection runs through every stage and has an outcome theme of its own. Writing, referencing, revision and exams are thin: the guidance links them only through intellectual property (referencing, loosely) and learning "about" assessment (essays and exams).

**Suggestions for pathways.**
1. Creativity: take the creativity and opportunity outcomes as the pathway's first standards statements, with the ladder in GU2 for levels.
2. Reflective practice: the reflection theme gives five outcomes and six delivery opportunities, including before-and-after skills audits and SMART action planning, which a reflective-practice pathway can use as its practice tasks.
3. Starting, progressing and succeeding: the mindset family (self-aware, motivated, resilient, tolerant of ambiguity, reflecting on failure) is a ready description of the dispositions that pathway builds.
4. AI and technology: the digital theme (digital advances, data-driven decisions, connecting technologies) is 2018's view and predates generative AI; use it for the data-literacy strand and look elsewhere for AI.
'''

TAIL = '''
### GU6 The benchmark web
<!-- label: practitioner; status: drafted; basis: primary for the paragraph and citation counts (a scan of the 54 benchmark texts held in stan); inferred for the reading -->
How this theme reaches the subject benchmark statements. Columns: paragraphs on enterprise or entrepreneurship, on sustainability, and on employability anywhere in the statement; whether it cites this guidance and the ESD guidance by title; and the paragraphs of its benchmark standards (the threshold, typical and excellent statements) that use theme words. References and reading lists excluded. Paragraph numbers are the statement's own.

| Benchmark (held text) | Enterprise ¶ | ESD ¶ | Employability ¶ | Cites EEE 2018 | Cites ESD | Enterprise in standards | ESD in standards | Employability in standards |
|---|---|---|---|---|---|---|---|---|
''' + GU6ROWS + '''

**Reading.** The benchmarks revised from 2019 on carry a short section on each cross-cutting theme (equality, diversity and inclusion; accessibility; sustainability; enterprise and entrepreneurship): 52 of the 54 held have enterprise paragraphs, and 36 cite this guidance by title. But the theme stays mostly in the context sections: only 12 benchmarks carry enterprise words into their standards, against 37 for sustainability and 23 for employability. Where they do, the strongest is a three-rung ladder in communication, media, film and cultural studies (applying entrepreneurial skills at threshold, at a high level for typical, at an exceptional level for excellent); creative writing, English, housing, librarianship, physics, public policy, agriculture and art and design carry one or two statements each.

So the web has three strands, in falling strength: **cites** (the benchmark names the guidance), **theme paragraph** (the benchmark says what enterprise means in its subject, outside its standards), and **theme in standards** (a benchmark standard asks for enterprise). Only the third binds a subject's threshold. The relations index (wkspc2601-library/ingested/standards/ingest-std-relations-index.md) holds these as edges.

**Suggestion.** When a benchmark is ingested (S-02), tag its theme paragraphs with `theme:enterprise` and link each to the guidance families it echoes (most often the outcome themes); tag its standards that use theme words with the same theme and a `mapsTo` to the outcome. Then a subject's enterprise standard can be read as "this guidance outcome, at this benchmark's level".

### GU7 Pedagogy handed to theory ingest
<!-- label: practitioner; status: drafted; basis: primary -->
Named here, not ingested; for ing to judge as theory items:
- learning about, for and through enterprise (the guidance's three modes, after the wider literature);
- the four-stage model of enterprise learning (awareness, mindset, capability, effectiveness) and its figure;
- the gateway triangle for assessing enterprise and entrepreneurship (the guidance's figure 3);
- EntreComp, the European Commission's entrepreneurship competence framework (three areas: ideas and opportunities, resources, into action);
- Venture Creation Programmes;
- SFEDI's National Occupational Standards for Enterprise Educators (2016), the source of the educator family;
- Knight and Yorke's (2003) definition of employability;
- experiential learning, business simulations and live projects as delivery methods;
- the "optimum strategic employment spot" figure (location, skills gaps, established businesses).

EntreComp and SFEDI's standards are themselves standards documents; if Abbott supplies them they belong in this profile (Part D, D3).

## Part B Terminology
<!-- label: both; status: drafted; basis: primary; paraphrased -->
```yaml
- { term: enterprise, gloss: "Generating ideas and applying them in practical settings during a project or undertaking; generic to all education and work." }
- { term: entrepreneurship, gloss: "Applying enterprise behaviours, attributes and competencies to create cultural, social or economic value, which may but need not mean a new venture; in any sector." }
- { term: entrepreneurial, gloss: "The guidance's word for enterprise and entrepreneurship together." }
- { term: enterprise education, gloss: "Education aimed at graduates able to generate original ideas for needs and opportunities and act on them, in uncertain conditions." }
- { term: entrepreneurship education, gloss: "Education building on enterprise competencies towards creating or growing a venture, in settings with real risk." }
- { term: employability, gloss: "Achievements (skills, understandings, personal attributes) that make employment and success in an occupation more likely (Knight and Yorke, 2003, as quoted)." }
- { term: intrapreneurship, gloss: "Enterprise exercised inside an existing organisation of any size or sector." }
- { term: social entrepreneurship, gloss: "Ventures driven by social or cultural problems rather than profit." }
- { term: green entrepreneurship, gloss: "Ventures aiming at a net benefit to the natural environment by sustainable means." }
- { term: digital entrepreneurship, gloss: "Ventures whose products or services are created, sold and supported online." }
- { term: enterprise behaviours, gloss: "Ways of acting (S4 vocab.behaviours)." }
- { term: enterprise attributes, gloss: "Personal qualities (S4 vocab.attributes)." }
- { term: enterprise competencies, gloss: "Capabilities that combine knowledge and skill (S4 vocab.competencies)." }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->
None: the guidance sets no process that providers must follow.

## Part D Sources

### D1 Held text
The PDF Abbott supplied (36 pages, sha256-bytes c11bde81…), converted with pdftotext and normalised (normalise.js 1.0); the PDF is not held in UNI. The figures' text survives only as fragments and is not cut into statements.

### D2 Research log
- 2026-10-03 05:40 to 05:52, std: read direct; 103 statements in eleven families; benchmark scan over the 54 held texts.

### D3 Wanted sources
- W-std-0013: EntreComp (Bacigalupo and others, 2016), the competence framework the guidance cites: a standards document for this profile.
- W-std-0014: SFEDI, National Occupational Standards for Enterprise Educators (2016): staff standards behind the educator family.
- W-std-0015: QAA's 2012 edition, for the change record.
- W-std-0016: Any QAA revision after 2018.

## Part E Gaps and questions
- E1 Currency: not checked against QAA's site.
- E2 The educator and institution families are standards for staff and providers, not students. Kept (Abbott's scope is what a student should be able to do "in some form"; these say what students can expect), with no student version where the statement says nothing a student can use.
- E3 The level reading (GU2) and every map (GU4, GU5, GU6) are ours.

---

## Change notes
- 0.1.2, 3 October 2026, 07:34: provenance lines added to Parts B and C; wanted sources in D3 given their W-std ids from the wanted-sources list (the ingest tool's G3 and G7 warnings; std N-0100). No statement changed.
- 0.1.1, 3 October 2026, 06:59: S7 records that the full ESD guidance 2021 (run 0063) cites this guidance.
- 0.1.0, 3 October 2026, 05:52: first build, run 0056 (std; Abbott, 05:40).
'''
