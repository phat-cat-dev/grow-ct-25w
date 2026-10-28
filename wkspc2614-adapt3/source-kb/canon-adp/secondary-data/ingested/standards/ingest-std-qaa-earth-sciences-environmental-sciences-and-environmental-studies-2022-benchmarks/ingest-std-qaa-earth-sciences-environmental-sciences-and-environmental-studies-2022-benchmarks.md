---
id: std:doc:qaa-earth-sciences-environmental-sciences-and-environmental-studies-2022-benchmarks
title: "Subject Benchmark Statement Earth Sciences, Environmental Sciences and Environmental Studies"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100394", label: "earth sciences", basis: "stated" }
  - { scheme: "hecos", code: "100381", label: "environmental sciences", basis: "stated" }
  - { scheme: "hecos", code: "100469", label: "environmental management", basis: "inferred" }
  - { scheme: "hecos", code: "100395", label: "geology", basis: "inferred" }
  - { scheme: "cah", code: "CAH26-01-06", label: "earth sciences", basis: "stated" }
  - { scheme: "cah", code: "CAH26-01-04", label: "environmental sciences", basis: "stated" }
  - { scheme: "cah", code: "CAH26-01-03", label: "human geography", basis: "inferred" }
  - { scheme: "cah", code: "CAH26-01", label: "geography, earth and environmental studies", basis: "stated" }
  - { scheme: "cah", code: "CAH26", label: "geography, earth and environmental studies", basis: "stated" }
edition: "March 2022 (fifth edition)"
published: 2022-03
status: current
supersedes: "the fourth edition (2019), which QAA revised from the third (2014); the back matter names both"
heldText: { method: sha256-bytes, raw: c7438a7671a1574ab16aed46e2e989cbb8bfa4763c166a6ef31cc3b162195c5f, normalised: b55484446e08b2874ca8fa160855aa9afd67c8ba4e357f38d2e3afcafa1f9c8b }
heldTextStan: { method: sha256-stan, raw: c7438a7671a1574ab16aed46e2e989cbb8bfa4763c166a6ef31cc3b162195c5f, normalised: de07c57595ef765db69ed9e6646391e4b63602432f66898deeaf3cf8906f30c8 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2022 revision with cross-cutting themes (this statement's fifth edition)"
awardsCovered: ["bachelor's with honours", "integrated master's", "master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary of its own (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0101 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:09"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Earth Sciences, Environmental Sciences and Environmental Studies (QAA, March 2022)

> Run 0101, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2022-earth-sciences-environmental-sciences-environmental-studies-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in Earth sciences, environmental sciences or environmental studies (ES3) knows and can do at the end of an honours degree, with shorter notes for integrated master's and taught master's awards. It sets one rung only, the threshold, as four skill lists, and pairs it with content lists for each subject. Reach for it when designing, reviewing or describing an ES3 course or its outcomes. It is not a curriculum, not a professional body's accreditation standard and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2022 as the fifth edition, the statement treats Earth sciences, environmental sciences and environmental studies together as ES3. It sets out the context (the climate and biodiversity crises), the common character of the subjects, their distinctive features, the content of each subject and its applications, teaching, learning and assessment, and threshold standards for honours graduates in four groups: intellectual skills, practical skills, communication skills and personal and professional skills. It states no typical or excellent rung and sends providers to Annex D for performance above the threshold. Integrated master's and taught master's graduates are described in two paragraphs. It carries the cross-cutting themes of equality, diversity and inclusion, accessibility, sustainability (ESD) and employability, entrepreneurship and enterprise, cites the FHEQ and the FQHEIS at levels 6 and 7 (10 and 11) and names five professional bodies.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Earth Sciences, Environmental Sciences and Environmental Studies"
edition: "March 2022 (fifth edition)"
dates:
  published: 2022-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of quality requirements in Northern Ireland (D1, front matter: Relationship to legislation and regulation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2022", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate in Earth sciences, environmental sciences or environmental studies can be expected to know, do and understand at the end of their studies, and the nature of awards in the subjects (D1, front matter: About this Statement; 4.1)"
appliesTo:
  awards: ["bachelor's degrees with honours (BSc, sometimes BA), placement years included", "integrated master's degrees (MSci)", "taught postgraduate degrees (MSc, sometimes MA)", "foundation degrees (FdSc): may find it useful, not covered as such"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This Subject Benchmark Statement covers the subjects as delivered at bachelor's degree with honours level (including degrees with placement years and generally leading to the award of BSc or sometimes BA), integrated master's degrees and taught postgraduate degrees (generally leading to the award of MSci, MSc or sometimes MA).\" (D1, front matter: About this Statement)"
statedSubjects:
  - { name: "Earth Sciences", locator: "(D1, title; 1.1; 3.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100394", label: "earth sciences" }, { scheme: "cah", code: "CAH26-01-06", label: "earth sciences" }] }
  - { name: "Environmental Sciences", locator: "(D1, title; 1.1; 3.4; 3.7)", kind: "subject", codes: [{ scheme: "hecos", code: "100381", label: "environmental sciences" }, { scheme: "cah", code: "CAH26-01-04", label: "environmental sciences" }] }
  - { name: "Environmental Studies", locator: "(D1, title; 1.1; 3.4; 3.10)", kind: "subject", codes: [{ scheme: "hecos", code: "100469", label: "environmental management" }] }
  - { name: "ES3", locator: "(D1, 1.1)", kind: "subject", codes: [] }
  - { name: "joint honours", locator: "(D1, 2.5)", kind: "programme title", codes: [] }
  - { name: "integrated master's (MSci); postgraduate (MSc or MA)", locator: "(D1, front matter; 2.3; 4.7; 4.8)", kind: "programme title", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "the three subjects named together as ES3" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "climate and biodiversity crises as the setting; graduates base decisions on sound science and fairness" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "why one statement serves several subjects" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "environmental sciences and studies merged where possible; Earth science content unchanged" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "environment read broadly, human and non-human life included" }
  - { number: "1.6", order: 8, componentType: stem, parent: "section 1", heading: "Characteristics of an ES3 degree", gloss: "nine shared traits of ES3 study" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Characteristics of an ES3 degree", gloss: "professional bodies in the field and the five named" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI as subject matter and practice; a duty to remove barriers" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "ways to explore EDI; graduates culturally aware and ethical" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainability as more than environment, central to ES3" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "ESD defined, with the UNESCO vision and the SDGs" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "users pointed to the joint ESD guidance" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise", gloss: "employability and entrepreneurship defined; links with employers" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise", gloss: "what Earth science employers seek" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise", gloss: "what environmental employers seek" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise", gloss: "users pointed to the enterprise guidance" }
  - { number: "2.1", order: 20, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "design: rooted in sustainability, practical, research-informed, decolonising" }
  - { number: "2.2", order: 21, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "accessibility as inclusive design; field and lab barriers; risk assessment" }
  - { number: "2.3", order: 22, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "yearly progression to the threshold; integrated master's year; exit awards; Scottish four-year degree" }
  - { number: "2.4", order: 23, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "second-class graduates ready for postgraduate study" }
  - { number: "2.5", order: 24, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint honours graduates reach part of the skills" }
  - { number: "2.6", order: 25, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes of study and possible specialisms" }
  - { number: "2.7", order: 26, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "students and external bodies as partners; work-based learning; apprenticeships" }
  - { number: "2.8", order: 27, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring, periodic review and awarding gaps" }
  - { number: "2.9", order: 28, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.10", order: 29, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and the statement's part in their advice" }
  - { number: "3.1", order: 31, componentType: stem, parent: "section 3", heading: "Earth Sciences", gloss: "Earth sciences: knowledge every graduate is anticipated to hold (18 items)" }
  - { number: "3.2", order: 32, componentType: area, parent: "section 3", heading: "Earth Sciences", gloss: "Earth sciences: typical components" }
  - { number: "3.3", order: 33, componentType: area, parent: "section 3", heading: "Earth Sciences", gloss: "Earth sciences: applications" }
  - { number: "3.4", order: 34, componentType: stem, parent: "section 3", heading: "Environmental Sciences and Environmental Studies", gloss: "environmental sciences and studies: shared knowledge (20 items)" }
  - { number: "3.5", order: 35, componentType: area, parent: "section 3", heading: "Environmental Sciences and Environmental Studies", gloss: "environmental sciences and studies: typical components" }
  - { number: "3.6", order: 36, componentType: area, parent: "section 3", heading: "Environmental Sciences and Environmental Studies", gloss: "environmental sciences and studies: applications" }
  - { number: "3.7", order: 37, componentType: stem, parent: "section 3", heading: "Environmental Sciences only content", gloss: "environmental sciences only: further knowledge (6 items)" }
  - { number: "3.8", order: 38, componentType: area, parent: "section 3", heading: "Environmental Sciences only content", gloss: "environmental sciences only: further components" }
  - { number: "3.9", order: 39, componentType: area, parent: "section 3", heading: "Environmental Sciences only content", gloss: "environmental sciences only: further applications" }
  - { number: "3.10", order: 40, componentType: stem, parent: "section 3", heading: "Environmental Studies only content", gloss: "environmental studies only: further knowledge (3 items)" }
  - { number: "3.11", order: 41, componentType: area, parent: "section 3", heading: "Environmental Studies only content", gloss: "environmental studies only: further components" }
  - { number: "3.12", order: 42, componentType: area, parent: "section 3", heading: "Environmental Studies only content", gloss: "environmental studies only: further applications" }
  - { number: "3.13", order: 43, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching and learning defined" }
  - { number: "3.14", order: 44, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "methods open; outcomes reachable and made clear" }
  - { number: "3.15", order: 45, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "inclusive methods; research-led and enquiry-based courses" }
  - { number: "3.16", order: 46, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "fieldwork at the heart; inclusive activities and adjustments" }
  - { number: "3.17", order: 47, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "ESD to underpin teaching and learning" }
  - { number: "3.18", order: 48, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment strategy; authentic assessment" }
  - { number: "3.19", order: 49, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "inclusive assessment linked to outcomes" }
  - { number: "3.20", order: 50, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "feedback, reflection, peer and self-assessment" }
  - { number: "3.21", order: 51, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "examples of authentic assessment" }
  - { number: "3.22", order: 52, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "multidisciplinary assessment grounded in ESD" }
  - { number: "4.1", order: 54, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the threshold standards for honours defined" }
  - { number: "4.2", order: 55, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most students exceed the threshold; Annex D for classes" }
  - { number: "4.3", order: 56, componentType: stem, parent: "section 4", heading: "Threshold level: Intellectual skills (knowledge and understanding)", gloss: "threshold: intellectual skills (9 items)" }
  - { number: "4.4", order: 57, componentType: stem, parent: "section 4", heading: "Practical skills", gloss: "threshold: practical skills (7 items)" }
  - { number: "4.5", order: 58, componentType: stem, parent: "section 4", heading: "Communication skills", gloss: "threshold: communication skills (5 items)" }
  - { number: "4.6", order: 59, componentType: stem, parent: "section 4", heading: "Personal and professional skills", gloss: "threshold: personal and professional skills (13 items)" }
  - { number: "4.7", order: 60, componentType: paragraph, parent: "section 4", heading: "Personal and professional skills", gloss: "integrated master's graduates: a specialism through an independent research project" }
  - { number: "4.8", order: 61, componentType: paragraph, parent: "section 4", heading: "Personal and professional skills", gloss: "taught postgraduate students: greater depth in one aspect" }
  - { number: "1", componentType: section, parent: none, heading: "Context and characteristics of an Earth Sciences, Environmental Sciences and Environmental Studies degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of an Earth Sciences, Environmental Sciences and Environmental Studies degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "section headings 1 to 4", heading: "the four section heading lines", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for SB6 and D3" }
  - { number: "6", heading: "Membership of the Advisory Groups (2022, 2019, 2014, 2007, 2000)", kind: "other: back matter, read for S8 and supersedes" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 98 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.2
  locator: { number: "1.2", headingPath: ["Context and characteristics of an Earth Sciences, Environmental Sciences and Environmental Studies degree", "Context"] }
  span: { start: 9994, end: 10506 }
  source: "The wider context for this Subject Benchmark Statement is the ongoing climate emergency and biodiversity crisis, as well as other threats to the natural environment. These require action at every level, from global and national political commitment to practical measures at a local level. Graduates in ES3 subjects will be required to ensure actions and decisions are based on sound science, and that they take into account equity, equality, diversity and inclusivity to deliver long-term, sustainable solutions."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "graduates in ES3 subjects"
  addressee: learner
  verbs: ["ensure", "deliver"]
  about: "decisions grounded in sound science and fairness"
  themes: [theme:edi]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Set against the climate emergency, biodiversity loss and other pressures on nature, which call for action from global policy to local practice, ES3 graduates will be required to make sure that actions and decisions rest on good science and weigh equity, equality, diversity and inclusion, so that solutions last and are sustainable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.5
  locator: { number: "1.5", headingPath: ["Context and characteristics of an Earth Sciences, Environmental Sciences and Environmental Studies degree", "Context"] }
  span: { start: 12192, end: 12382 }
  source: "Note that the term ‘environment’ as used throughout this document should be interpreted as inclusive in its scope and should be taken to include all livings things, both human and non-human."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "readers and users of the statement"
  addressee: provider
  verbs: ["interpreted", "include"]
  about: "reading environment broadly"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The word environment, wherever the statement uses it, should be read broadly, so that it covers every living thing, human and non-human."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.8
  locator: { number: "1.8", headingPath: ["Context and characteristics of an Earth Sciences, Environmental Sciences and Environmental Studies degree", "Equality, diversity and inclusion"] }
  span: { start: 14082, end: 14783 }
  source: "Equality, diversity and inclusivity (EDI) are integral to the ES3 disciplines, not only informing pedagogical practice but also as subject knowledge. Inclusion of diverse groups is critical to the development of subject learning communities, yet these groups may encounter multiple barriers to engagement. ES3 communities have a duty to confront and encourage the dismantling of all barriers to engagement and participation in our disciplines. Equality Impact Assessments may be a useful mechanism to explore these issues. ES3 communities can commit to creating safe, inclusive and supportive environments that value diversity and encourage discussion, learning and the co-production of ES3 curricula."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "duty" read as must
  level: none
  appliesTo: "ES3 academic communities"
  addressee: provider
  verbs: ["confront", "encourage", "commit"]
  about: "removing barriers to taking part in the disciplines"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "EDI belongs to the ES3 subjects both as how they are taught and as knowledge in its own right; diverse groups matter to learning communities but face many barriers, which ES3 communities have a duty to challenge and help take down, perhaps using equality impact assessments, and they can commit to safe, inclusive settings that welcome diversity and co-produced curricula."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.9
  locator: { number: "1.9", headingPath: ["Context and characteristics of an Earth Sciences, Environmental Sciences and Environmental Studies degree", "Equality, diversity and inclusion"] }
  span: { start: 14788, end: 15673 }
  source: "EDI can be explored in discipline contexts and by challenging discipline identities and stereotypes, including the impact of colonialism, embedding diverse representation within curriculums, broadening interdisciplinary and cross-disciplinary perspectives and particularly valuing different cultural perspectives, ways of knowing and lived experience. The ES3 subjects are a route to justice through delivery of the UN Sustainable Development Goals and diverse perspectives are essential to confronting global grand challenges. To achieve this, academic programmes in ES3 disciplines cultivate graduates who are culturally aware, show ethical behaviour, consideration and respect and who can reflect on equality in the context of their discipline. They will also be proficient in systems thinking, flexibility, interdisciplinarity and open to different ways of thinking and practising."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of ES3 programmes"
  addressee: learner
  verbs: ["cultivate", "reflect"]
  about: "cultural awareness, ethics and openness to other ways of knowing"
  themes: [theme:edi]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "EDI can be explored by challenging the disciplines' identities and stereotypes, colonial legacies included, diversifying curricula and valuing other cultures' knowledge and lived experience; the subjects serve justice through the SDGs, so programmes develop graduates who are culturally aware, ethical and respectful and can reflect on equality; they will also think in systems, adapt, work across disciplines and stay open to other ways of thinking."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.12
  locator: { number: "1.12", headingPath: ["Context and characteristics of an Earth Sciences, Environmental Sciences and Environmental Studies degree", "Sustainability"] }
  span: { start: 16885, end: 17191 }
  source: "To support the inclusion of sustainable development within the ES3 disciplines, users should refer to the QAA and Advance HE Education for Sustainable Development Guidance to address teaching and learning for sustainable development, key competencies, learning outcomes and assessment within the curricula."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "users of the statement designing ES3 curricula"
  addressee: provider
  verbs: ["support", "refer", "address"]
  about: "using the joint ESD guidance"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Those building sustainable development into ES3 courses should consult the joint QAA and Advance HE guidance on ESD for teaching, competencies, outcomes and assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.16
  locator: { number: "1.16", headingPath: ["Context and characteristics of an Earth Sciences, Environmental Sciences and Environmental Studies degree", "Employability, entrepreneurship and enterprise"] }
  span: { start: 19030, end: 19258 }
  source: "To support the inclusion of employability, entrepreneurship and enterprise within the ES3 disciplines, users should refer to the QAA document Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "users of the statement designing ES3 curricula"
  addressee: provider
  verbs: ["support", "refer"]
  about: "using the enterprise and entrepreneurship guidance"
  themes: [theme:enterprise]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Those building employability, entrepreneurship and enterprise into ES3 courses should consult QAA's guidance on enterprise and entrepreneurship education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/2.2
  locator: { number: "2.2", headingPath: ["Distinctive features of an Earth Sciences, Environmental Sciences and Environmental Studies degree", "Accessibility"] }
  span: { start: 20411, end: 21720 }
  source: "In this Statement, we approach accessibility as the inclusive design of curriculum and pedagogy that does not exclude any individual from participation. Individuals and marginalised groups experience a variety of barriers to participation, many of which are intersectional. These barriers are purposefully addressed in the ES3 subjects so that all learners can equally access and thrive, with inclusive practices a pedagogical norm. While inclusive curriculum design should enable all learners to participate fully, flexibility is required, and reasonable adjustments may be needed in practice. The ES3 subjects are visual and graphic subjects traditionally underpinned by laboratory and field-based approaches, which can sometimes be exclusionary. Ensuring that all students can participate in such activities may require a mix of strategies, including careful design of curricula and field programmes and leveraging accessible technologies. Health, safety and well-being of participants should be included in risk assessments, including any specific risks a student with protected characteristics may face. A choice of blended learning through online learning and practical exercises can enable a wide range of learners to engage, making for effective teams and group work rather than reinforcing otherness."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course and field programme design"
  addressee: provider
  verbs: ["addressed", "enable", "included"]
  about: "accessible design, adjustments and inclusive risk assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Accessibility means designing curriculum and teaching so nobody is shut out; barriers, often overlapping, are tackled deliberately so all learners can take part and do well; inclusive design should let everyone take part, though flexibility and reasonable adjustments may still be needed; field and laboratory work can exclude, so courses may need several strategies and accessible technology; risk assessments should cover health, safety and well-being, including risks to students with protected characteristics; blended options help a wide range of learners."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of an Earth Sciences, Environmental Sciences and Environmental Studies degree", "Progression"] }
  span: { start: 21737, end: 22976 }
  source: "Over the course of a bachelor’s degree with honours (FHEQ Level 6; FQHEIS SCQF Level 10), a student studying for a degree in the ES3 subject area will progress from one year of study to the next, in line with the regulations and processes for each institution. However, it is expected that in each year, the attainment of certain levels of knowledge, expertise and experience are achieved. These will build towards the final achievement of meeting all of the threshold-level subject-specific and generic skills listed in this Statement. Integrated master’s degrees (FHEQ Level 7; FQHEIS SCQF Level 11) require one further academic year of study and it is expected that at the end of this further year, students are able to demonstrate increased critical thinking, evaluation skills and independence. In a standard three-year undergraduate honours degree course, students may exit earlier and be eligible for a Certificate of Higher Education, a Diploma of Higher Education or an honours degree, depending upon the levels of study completed to a satisfactory standard. Scottish bachelor’s degrees with honours are typically designed to include four years of study, which relates to the structure of Scottish primary and secondary education."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and integrated master's students"
  addressee: learner
  verbs: ["progress", "build", "demonstrate"]
  about: "progression to the threshold and the integrated master's year"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Across an honours degree (at FHEQ level 6, or SCQF level 10 in Scotland) each student moves up year by year under each institution's rules, reaching set levels of knowledge, expertise and experience each year that build towards meeting every threshold subject-specific and generic skill; an integrated master's (FHEQ level 7; SCQF level 11) adds a year, after which students are able to show stronger critical thinking, evaluation and independence; early exit awards are possible, and Scottish honours degrees usually last four years."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of an Earth Sciences, Environmental Sciences and Environmental Studies degree", "Progression"] }
  span: { start: 22984, end: 23397 }
  source: "Where relevant, upon graduation from an undergraduate degree, it would normally be expected that a student who had achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in Earth Science, Environmental Science, Environmental Studies or associated sustainability disciplines and would also be equipped for entering courses that cross and combine disciplines."
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "undergraduates with a second-class degree or above"
  addressee: learner
  verbs: ["equipped", "undertaking", "entering"]
  about: "readiness for postgraduate and cross-disciplinary study"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Where it applies, a graduate with at least a second-class degree would normally be expected to be able and ready to go on to postgraduate study in ES3 or related sustainability fields, and to enter courses that combine disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of an Earth Sciences, Environmental Sciences and Environmental Studies degree", "Progression"] }
  span: { start: 23402, end: 23579 }
  source: "Joint honours undergraduates will achieve elements of the specific and generic skills for the subject but will add others according to the subjects covered in a joint programme."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint honours undergraduates"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "joint honours and the skill lists"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students on joint honours will reach part of the subject-specific and generic skills for ES3 and add further skills from their other subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b1
  locator: { number: "3.1.b1", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 27134, end: 27314 }
  source: "The concepts and applications of sustainable development and systems thinking. This should be consistent with the QAA and Advance HE Education for Sustainable Development Guidance."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: both
  verbs: []
  about: "sustainable development and systems thinking"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of the ideas and uses of sustainable development and systems thinking, taught in a way that should match the joint QAA and Advance HE guidance on ESD."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b2
  locator: { number: "3.1.b2", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 27317, end: 27402 }
  source: "The formation of the Earth and other planets and their place within the solar system."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: []
  about: "how the Earth and planets formed"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of how the Earth and the other planets came into being and where they sit in the solar system."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b3
  locator: { number: "3.1.b3", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 27405, end: 27599 }
  source: "The central paradigms in the Earth sciences: uniformitarianism (the present is the key to the past); the extent of geological time; evolution (the history of life on Earth); and plate tectonics."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: []
  about: "the central paradigms of the Earth sciences"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding of the field's core paradigms: uniformitarianism, the span of geological time, evolution and plate tectonics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b4
  locator: { number: "3.1.b4", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 27602, end: 27799 }
  source: "Geological time, including the principles of stratigraphy, the stratigraphic column, the fossil record, the methods of geochronology, the rates of Earth processes and major events in Earth history."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: []
  about: "geological time and Earth history"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of geological time: stratigraphic principles and the column, the fossil record, dating methods, how fast processes run and the major events of Earth history."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b5
  locator: { number: "3.1.b5", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 27802, end: 28015 }
  source: "The structure, composition and materials of the solid Earth, the hydrosphere, the atmosphere, the cryosphere and the biosphere; the processes operating and the cycling of matter and energy within and between them."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: []
  about: "Earth spheres and the cycling of matter and energy"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of the make-up of the solid Earth, oceans and waters, air, ice and living world, the processes acting in each and how matter and energy cycle through them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b6
  locator: { number: "3.1.b6", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 28018, end: 28142 }
  source: "The study of the biological, chemical and physical processes that underpin our understanding of Earth and planetary systems."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: []
  about: "processes behind Earth and planetary systems"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding of the biological, chemical and physical processes on which knowledge of Earth and planetary systems rests."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b7
  locator: { number: "3.1.b7", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 28145, end: 28281 }
  source: "The study of structures, materials and processes that includes an appreciation of temporal and spatial variations at appropriate scales."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: []
  about: "variation in time and space at fitting scales"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding of structures, materials and processes with attention to how they vary over time and space at suitable scales."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b8
  locator: { number: "3.1.b8", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 28284, end: 28344 }
  source: "The formation of igneous, metamorphic and sedimentary rocks."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: []
  about: "formation of the main rock types"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of how igneous, metamorphic and sedimentary rocks form."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b9
  locator: { number: "3.1.b9", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 28347, end: 28484 }
  source: "The identification of rocks, minerals, fossils and geological structures and their relevant terminology, nomenclature and classification."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: []
  about: "identifying rocks, minerals, fossils and structures"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Recognising rocks, minerals, fossils and geological structures and using the right terms, names and classifications for them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b10
  locator: { number: "3.1.b10", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 28487, end: 28696 }
  source: "Collection and analysis of Earth science data of the surface and subsurface, and the appropriate presentation, manipulation, modelling and extrapolation of these (sometimes incomplete) data in four dimensions."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: []
  about: "collecting and modelling Earth data in four dimensions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Gathering and analysing data from the surface and subsurface, then presenting, handling, modelling and extrapolating these often incomplete data across space and time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b11
  locator: { number: "3.1.b11", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 28699, end: 28794 }
  source: "Observation and interpretation of field-based data (in situ and virtual) from first principles."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: []
  about: "interpreting field data from first principles"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Observing and interpreting field data, gathered in person or virtually, by reasoning from first principles."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b12
  locator: { number: "3.1.b12", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 28797, end: 28905 }
  source: "Surveying and measurement, both in the field and laboratory, using quantitative and instrumental techniques."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: []
  about: "surveying and measuring in the field and laboratory"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Surveying and measuring in the field and the laboratory with quantitative and instrumental methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b13
  locator: { number: "3.1.b13", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 28908, end: 29056 }
  source: "The use of qualitative and quantitative data, an understanding of using data sets and an appreciation of how to assess data quality and uncertainty."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: ["assess"]
  about: "data use, quality and uncertainty"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Working with qualitative and quantitative data and datasets, and knowing how to assess data quality and uncertainty."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b14
  locator: { number: "3.1.b14", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 29059, end: 29205 }
  source: "The importance of Earth sciences in resource management and the mitigation of, and adaptation to, environmental hazards, including climate change."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: []
  about: "Earth sciences in resources, hazards and climate change"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding why the Earth sciences matter for managing resources and for reducing and adapting to environmental hazards, climate change among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b15
  locator: { number: "3.1.b15", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 29208, end: 29371 }
  source: "An awareness that the understanding and knowledge gained from the subject and its application is considered within a wider socioeconomic and environmental context."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: ["considered"]
  about: "the wider socioeconomic and environmental context"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Awareness that the subject's knowledge and its uses are weighed within a broader social, economic and environmental setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b16
  locator: { number: "3.1.b16", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 29374, end: 29542 }
  source: "An understanding of the ethical issues surrounding the legacy and uses of the discipline, engaging in contemporary debates and appreciating the need for decolonisation."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: ["engaging", "appreciating"]
  about: "ethics, legacy and decolonisation of the discipline"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding the ethical questions raised by the discipline's history and uses, taking part in current debates and seeing why decolonisation is needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b17
  locator: { number: "3.1.b17", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 29545, end: 29633 }
  source: "The importance of equality, diversity and inclusivity in the practice of the discipline."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: []
  about: "EDI in the practice of the discipline"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding why equality, diversity and inclusivity matter in how the discipline is practised."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b18
  locator: { number: "3.1.b18", headingPath: ["Content, structure and delivery", "Earth Sciences"] }
  span: { start: 29640, end: 29759 }
  source: "An awareness of field work codes of practice and an ability to confidently complete health and safety risk assessments."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in Earth sciences"
  addressee: learner
  verbs: ["complete"]
  about: "fieldwork codes and risk assessment"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Awareness of codes of practice for fieldwork and the ability to complete health and safety risk assessments with confidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b1
  locator: { number: "3.4.b1", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 31978, end: 32158 }
  source: "The concepts and applications of sustainable development and systems thinking. This should be consistent with the QAA and Advance HE Education for Sustainable Development Guidance."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: both
  verbs: []
  about: "sustainable development and systems thinking"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of the ideas and uses of sustainable development and systems thinking, taught in a way that should match the joint QAA and Advance HE guidance on ESD."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b2
  locator: { number: "3.4.b2", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 32161, end: 32270 }
  source: "A holistic approach to the study of the complexity and interconnections of the Earth's systems and processes."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: []
  about: "a holistic view of Earth systems"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Studying Earth's systems and processes as a whole, with their complexity and links."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b3
  locator: { number: "3.4.b3", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 32273, end: 32403 }
  source: "The principles of sustainability and the use of sustainable approaches to manage natural and human-induced cycles of resource use."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: []
  about: "sustainability principles and resource cycles"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of sustainability principles and of sustainable ways to manage natural and human-driven cycles of resource use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b4
  locator: { number: "3.4.b4", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 32406, end: 32559 }
  source: "The importance of timescale (geological, present, short term, long term and future) on the impacts of natural and human-induced activities on ecosystems."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: []
  about: "timescale and impacts on ecosystems"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding how the timescale considered, from geological to future, shapes the effects of natural and human activity on ecosystems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b5
  locator: { number: "3.4.b5", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 32562, end: 32677 }
  source: "The spatial scale, from global to local, of human impacts on the environment and responses to environmental change."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: []
  about: "spatial scale of human impacts"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding the spatial scale, global to local, of human effects on the environment and of responses to change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b6
  locator: { number: "3.4.b6", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 32680, end: 32779 }
  source: "The interconnections and inter-dependencies of all organisms within natural and managed ecosystems."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: []
  about: "interdependence of organisms in ecosystems"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of how all organisms in natural and managed ecosystems connect with and depend on each other."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b7
  locator: { number: "3.4.b7", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 32782, end: 32891 }
  source: "The positive and negative impacts of development on the environment and management tools for addressing them."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: ["addressing"]
  about: "impacts of development and tools to manage them"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of the good and harmful effects of development on the environment and of the management tools for dealing with them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b8
  locator: { number: "3.4.b8", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 32894, end: 32971 }
  source: "The impacts of environmental change on humans, non-humans and infrastructure."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: []
  about: "effects of environmental change on people, other species and infrastructure"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of how environmental change affects people, other species and infrastructure."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b9
  locator: { number: "3.4.b9", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 32974, end: 33071 }
  source: "Monitoring, modelling and managing natural and human-induced environmental changes and behaviour."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: ["monitoring", "modelling", "managing"]
  about: "monitoring, modelling and managing environmental change"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Monitoring, modelling and managing environmental change and behaviour, natural and human-induced."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b10
  locator: { number: "3.4.b10", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 33074, end: 33183 }
  source: "Understand how to predict, mitigate and manage risks presented by a changing environment and human pressures."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: ["understand", "predict", "mitigate", "manage"]
  about: "predicting and managing environmental risk"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowing how to forecast, reduce and manage the risks posed by a changing environment and human pressure."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b11
  locator: { number: "3.4.b11", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 33186, end: 33269 }
  source: "Understanding uncertainty and how it applies to current and future decision-making."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: ["applies"]
  about: "uncertainty in decision-making"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding uncertainty and how it bears on decisions now and in future."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b12
  locator: { number: "3.4.b12", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 33272, end: 33418 }
  source: "The role of institutions, organisations, governance structures and other stakeholders in managing and regulating human impacts on the environment."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: ["managing", "regulating"]
  about: "institutions and governance of human impacts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of the part institutions, organisations, governance and other stakeholders play in managing and regulating human effects on the environment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b13
  locator: { number: "3.4.b13", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 33421, end: 33587 }
  source: "The importance of environmental sciences and studies in resource management and the mitigation of, and adaptation to, environmental hazards, including climate change."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: []
  about: "the subjects in resources, hazards and climate change"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding why environmental sciences and studies matter for managing resources and for reducing and adapting to environmental hazards, climate change among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b14
  locator: { number: "3.4.b14", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 33590, end: 33685 }
  source: "Observation and interpretation of field-based data (in situ and virtual) from first principles."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: []
  about: "interpreting field data from first principles"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Observing and interpreting field data, gathered in person or virtually, by reasoning from first principles."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b15
  locator: { number: "3.4.b15", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 33688, end: 33836 }
  source: "The use of qualitative and quantitative data, an understanding of using data sets and an appreciation of how to assess data quality and uncertainty."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: ["assess"]
  about: "data use, quality and uncertainty"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Working with qualitative and quantitative data and datasets, and knowing how to assess data quality and uncertainty."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b16
  locator: { number: "3.4.b16", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 33839, end: 33905 }
  source: "Developing relevant and appropriate digital skills and technology."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: ["developing"]
  about: "digital skills and technology"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Building digital skills and technology use that are relevant and fit for purpose."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b17
  locator: { number: "3.4.b17", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 33908, end: 34071 }
  source: "An awareness that the understanding and knowledge gained from the subject and its application is considered within a wider socioeconomic and environmental context."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: ["considered"]
  about: "the wider socioeconomic and environmental context"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Awareness that the subject's knowledge and its uses are weighed within a broader social, economic and environmental setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b18
  locator: { number: "3.4.b18", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 34074, end: 34229 }
  source: "Understand the ethical issues surrounding the legacy and uses of the discipline, engage in contemporary debates and appreciate the need for decolonisation."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: ["understand", "engage", "appreciate"]
  about: "ethics, legacy and decolonisation of the discipline"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding the ethical questions raised by the discipline's history and uses, taking part in current debates and seeing why decolonisation is needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b19
  locator: { number: "3.4.b19", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 34236, end: 34323 }
  source: "The importance of equality, diversity and inclusivity in the practise of the discipline"
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: []
  about: "EDI in the practice of the discipline"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding why equality, diversity and inclusivity matter in how the discipline is practised."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b20
  locator: { number: "3.4.b20", headingPath: ["Content, structure and delivery", "Environmental Sciences and Environmental Studies"] }
  span: { start: 34326, end: 34439 }
  source: "Awareness of field work codes of practice and ability to confidently complete health and safety risk assessments."
  stem: "3.4"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences or environmental studies"
  addressee: learner
  verbs: ["complete"]
  about: "fieldwork codes and risk assessment"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Awareness of codes of practice for fieldwork and the ability to complete health and safety risk assessments with confidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.7.b1
  locator: { number: "3.7.b1", headingPath: ["Content, structure and delivery", "Environmental Sciences only content"] }
  span: { start: 36738, end: 36844 }
  source: "the scientific study of physical, chemical, biological and anthropogenic processes operating on ecosystems"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences"
  addressee: learner
  verbs: []
  about: "scientific study of processes acting on ecosystems"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge, from scientific study, of the physical, chemical, biological and human-driven processes that act on ecosystems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.7.b2
  locator: { number: "3.7.b2", headingPath: ["Content, structure and delivery", "Environmental Sciences only content"] }
  span: { start: 36847, end: 36988 }
  source: "major environmental processes on scales from global to organismal, and, where appropriate, to the molecular and atomic levels of organisation"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences"
  addressee: learner
  verbs: []
  about: "environmental processes from global to atomic scale"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of the main environmental processes at scales from the planet to the organism and, where it fits, down to molecules and atoms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.7.b3
  locator: { number: "3.7.b3", headingPath: ["Content, structure and delivery", "Environmental Sciences only content"] }
  span: { start: 36991, end: 37125 }
  source: "a scientific and multidisciplinary approach to identifying, understanding and managing the Earth's structure, processes and ecosystems"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences"
  addressee: learner
  verbs: ["identifying", "understanding", "managing"]
  about: "a scientific approach to Earth's structure, processes and ecosystems"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A scientific, multidisciplinary way to recognise, understand and manage the structure, processes and ecosystems of the Earth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.7.b4
  locator: { number: "3.7.b4", headingPath: ["Content, structure and delivery", "Environmental Sciences only content"] }
  span: { start: 37128, end: 37255 }
  source: "the use of scientific and technological information and tools to inform decision- making processes and environmental management"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences"
  addressee: learner
  verbs: ["inform"]
  about: "scientific information and tools for decisions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Using scientific and technical information and tools to support decisions and environmental management."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.7.b5
  locator: { number: "3.7.b5", headingPath: ["Content, structure and delivery", "Environmental Sciences only content"] }
  span: { start: 37258, end: 37352 }
  source: "observation and interpretation of field-based data (in situ and virtual) from first principles"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences"
  addressee: learner
  verbs: []
  about: "interpreting field data from first principles"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Observing and interpreting field data, gathered in person or virtually, by reasoning from first principles."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.7.b6
  locator: { number: "3.7.b6", headingPath: ["Content, structure and delivery", "Environmental Sciences only content"] }
  span: { start: 37355, end: 37463 }
  source: "surveying and measurement, both in the field and laboratory, using quantitative and instrumental techniques."
  stem: "3.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental sciences"
  addressee: learner
  verbs: []
  about: "surveying and measuring in the field and laboratory"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Surveying and measuring in the field and the laboratory with quantitative and instrumental methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.10.b1
  locator: { number: "3.10.b1", headingPath: ["Content, structure and delivery", "Environmental Studies only content"] }
  span: { start: 38545, end: 38627 }
  source: "the history and current evidence of natural and human-induced environmental change"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental studies"
  addressee: learner
  verbs: []
  about: "history and evidence of environmental change"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of the history of environmental change, natural and human-driven, and the evidence for it now."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.10.b2
  locator: { number: "3.10.b2", headingPath: ["Content, structure and delivery", "Environmental Studies only content"] }
  span: { start: 38630, end: 38726 }
  source: "the sociological, political and economic implications of human interactions with the environment"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental studies"
  addressee: learner
  verbs: []
  about: "social, political and economic implications"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding the social, political and economic consequences of how people interact with the environment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.10.b3
  locator: { number: "3.10.b3", headingPath: ["Content, structure and delivery", "Environmental Studies only content"] }
  span: { start: 38729, end: 38800 }
  source: "the relationship between the environment and human cultures and values."
  stem: "3.10"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "honours graduates in environmental studies"
  addressee: learner
  verbs: []
  about: "environment, culture and values"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Understanding how the environment relates to human cultures and values."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.14
  locator: { number: "3.14", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 39995, end: 40240 }
  source: "This Subject Benchmark Statement does not specify which methods of teaching or learning should be employed in relevant courses; however, learning outcomes should be achievable through the methods utilised and clearly articulated to the learners."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "ES3 courses"
  addressee: provider
  verbs: ["achievable", "articulated"]
  about: "outcomes reachable by the methods used and made clear"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The statement does not choose teaching or learning methods, but the outcomes should be reachable through the methods a course uses and set out clearly for learners."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 40246, end: 40543 }
  source: "Teaching and learning are interlinked as part of the curriculum design process and methods chosen should be inclusive and appropriate to develop the knowledge and skills identified in sections 1 and 2. Research-led and enquiry-based courses may develop specific subject-based knowledge and skills."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "ES3 courses"
  addressee: provider
  verbs: ["interlinked", "develop"]
  about: "inclusive, fitting teaching methods"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching and learning link within curriculum design, and the methods chosen should be inclusive and fit to build the knowledge and skills in sections 1 and 2; courses led by research or enquiry may build subject-based knowledge and skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.16
  locator: { number: "3.16", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 40549, end: 41761 }
  source: "The ES3 subjects are characterised by the integration of practical work, especially field-based activities, with theoretical studies. Courses therefore offer all students opportunities for significant field-based learning and teaching to foster skills such as the ability to visualise and extrapolate data in three dimensions or understand the application of practical methodologies. Much advancement in knowledge and understanding in these subject areas is founded on accurate observation and recording in the field and the collection of empirical data for analysis. Developing field-related practical and research skills is therefore important for students wishing to pursue careers in ES3-related sectors. Field- based studies allow students to develop and enhance many graduate attributes and transferable skills, for example leadership, team working, problem-solving, self-management and interpersonal relationships, which are of value to their employability, entrepreneurship and active citizenship. Activities should be designed to be inclusive to all students. If required, reasonable adjustments should be arranged in order to enable all students to take part in practical work and fieldwork activities."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "ES3 courses and their field and practical activities"
  addressee: provider
  verbs: ["designed", "arranged"]
  about: "fieldwork for all, inclusively designed with adjustments"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Practical work, above all fieldwork, is woven through the subjects, so courses give every student substantial field-based learning that builds skills such as visualising data in three dimensions and applying practical methods; field skills matter for ES3 careers and build transferable attributes; activities should be inclusive, and reasonable adjustments should be arranged where needed so all can take part."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.17
  locator: { number: "3.17", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 41767, end: 42034 }
  source: "ES3 subjects have sustainability at their core. Teaching and learning should be clearly underpinned by education for sustainable development to achieve positive graduate outcomes and teaching and learning methods should embody sustainability principles and solutions."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "ES3 courses"
  addressee: provider
  verbs: ["underpinned", "embody"]
  about: "teaching grounded in ESD"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Sustainability is central to ES3, so teaching and learning should rest plainly on education for sustainable development and its methods should live out sustainable principles and solutions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44264, end: 44743 }
  source: "The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers awarding ES3 honours degrees"
  addressee: provider
  verbs: ["perform", "refer"]
  about: "Annex D for performance above the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do much better than the threshold; each provider decides what evidence shows this and should use Annex D, QAA's descriptions of the four honours classifications (1st, 2:1, 2:2, 3rd) at FHEQ level 6 and FQHEIS level 10."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b1
  locator: { number: "4.3.b1", headingPath: ["Benchmark standards", "Threshold level: Intellectual skills (knowledge and understanding)"] }
  span: { start: 44857, end: 44956 }
  source: "have a knowledge and understanding of subject-specific theories, paradigms, concepts and principles"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["have"]
  about: "subject theories, paradigms, concepts and principles"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Know and understand the theories, paradigms, concepts and principles particular to the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b2
  locator: { number: "4.3.b2", headingPath: ["Benchmark standards", "Threshold level: Intellectual skills (knowledge and understanding)"] }
  span: { start: 44959, end: 45033 }
  source: "integrate evidence from a range of sources to test findings and hypotheses"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["integrate", "test"]
  about: "testing findings against several sources of evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Bring together evidence from varied sources to check findings and hypotheses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b3
  locator: { number: "4.3.b3", headingPath: ["Benchmark standards", "Threshold level: Intellectual skills (knowledge and understanding)"] }
  span: { start: 45036, end: 45133 }
  source: "consider and appraise issues from a range of multidisciplinary and interdisciplinary perspectives"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["consider", "appraise"]
  about: "looking at issues across disciplines"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Weigh up and judge issues from several multidisciplinary and interdisciplinary angles."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b4
  locator: { number: "4.3.b4", headingPath: ["Benchmark standards", "Threshold level: Intellectual skills (knowledge and understanding)"] }
  span: { start: 45136, end: 45212 }
  source: "analyse, synthesise, summarise, appraise and critically evaluate information"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["analyse", "synthesise", "summarise", "appraise", "evaluate"]
  about: "analysing and critically evaluating information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Analyse, combine, summarise, judge and critically evaluate information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b5
  locator: { number: "4.3.b5", headingPath: ["Benchmark standards", "Threshold level: Intellectual skills (knowledge and understanding)"] }
  span: { start: 45215, end: 45282 }
  source: "define complex problems and develop and evaluate possible solutions"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["define", "develop", "evaluate"]
  about: "defining complex problems and weighing solutions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Set out complex problems clearly, then work up and judge possible solutions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b6
  locator: { number: "4.3.b6", headingPath: ["Benchmark standards", "Threshold level: Intellectual skills (knowledge and understanding)"] }
  span: { start: 45285, end: 45366 }
  source: "develop and test hypotheses to inform and design investigations (and experiments)"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["develop", "test", "inform", "design"]
  about: "hypotheses that shape investigations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Form and test hypotheses that guide the design of investigations and experiments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b7
  locator: { number: "4.3.b7", headingPath: ["Benchmark standards", "Threshold level: Intellectual skills (knowledge and understanding)"] }
  span: { start: 45369, end: 45443 }
  source: "plan, conduct and present an independent project with appropriate guidance"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["plan", "conduct", "present"]
  about: "an independent project with guidance"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Plan, carry out and present an independent project, with suitable guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b8
  locator: { number: "4.3.b8", headingPath: ["Benchmark standards", "Threshold level: Intellectual skills (knowledge and understanding)"] }
  span: { start: 45446, end: 45532 }
  source: "take a critical approach to academic literature, data and other sources of information"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["take"]
  about: "a critical approach to literature and data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Approach academic writing, data and other information critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b9
  locator: { number: "4.3.b9", headingPath: ["Benchmark standards", "Threshold level: Intellectual skills (knowledge and understanding)"] }
  span: { start: 45535, end: 45623 }
  source: "have confidence and competence in dealing with uncertainty in data and systems response."
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["have"]
  about: "handling uncertainty in data and systems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Deal with uncertainty in data and in how systems respond, with confidence and competence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Practical skills"] }
  span: { start: 45686, end: 45762 }
  source: "conduct fieldwork and laboratory investigations competently (as appropriate)"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["conduct"]
  about: "competent field and laboratory investigation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Carry out field and laboratory investigations competently, as fits the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Practical skills"] }
  span: { start: 45765, end: 45837 }
  source: "describe and record observations effectively in the field and laboratory"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["describe", "record"]
  about: "recording observations in field and laboratory"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Describe and record observations well in the field and the laboratory."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Practical skills"] }
  span: { start: 45840, end: 45900 }
  source: "interpret and evaluate practical results in a logical manner"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["interpret", "evaluate"]
  about: "logical interpretation of practical results"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Interpret and judge practical results logically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Practical skills"] }
  span: { start: 45903, end: 46034 }
  source: "undertake laboratory and fieldwork ethically and safely with an appreciation of appropriate codes of conduct and legal requirements"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["undertake"]
  about: "ethical and safe practical work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Do laboratory and fieldwork ethically and safely, aware of the relevant codes of conduct and legal requirements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Practical skills"] }
  span: { start: 46037, end: 46109 }
  source: "gather, prepare, process and interpret data using appropriate techniques"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["gather", "prepare", "process", "interpret"]
  about: "gathering and processing data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Collect, prepare, process and interpret data with suitable methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Practical skills"] }
  span: { start: 46112, end: 46177 }
  source: "use appropriate numerical, statistical and qualitative techniques"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["use"]
  about: "numerical, statistical and qualitative techniques"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Apply suitable numerical, statistical and qualitative methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Practical skills"] }
  span: { start: 46180, end: 46244 }
  source: "use appropriate technologies in addressing problems effectively."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["use"]
  about: "technologies for solving problems"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use fitting technologies to tackle problems well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Communication skills"] }
  span: { start: 46315, end: 46401 }
  source: "communicate effectively with a variety of audiences using a range of formats and media"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating with varied audiences and media"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Communicate well with different audiences in a range of formats and media."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Communication skills"] }
  span: { start: 46404, end: 46481 }
  source: "have good interpersonal communication skills to enable effective team working"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["have", "enable"]
  about: "interpersonal skills for teamwork"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Have sound interpersonal communication skills that make teamwork effective."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Communication skills"] }
  span: { start: 46484, end: 46533 }
  source: "acknowledge and understand different perspectives"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["acknowledge", "understand"]
  about: "recognising different perspectives"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Recognise and understand viewpoints other than one's own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Communication skills"] }
  span: { start: 46536, end: 46585 }
  source: "effectively articulate and synthesise an argument"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["articulate", "synthesise"]
  about: "building and expressing an argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Put an argument together and express it clearly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Communication skills"] }
  span: { start: 46588, end: 46643 }
  source: "present a case in an influential and persuasive manner."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["present"]
  about: "making a persuasive case"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Present a case persuasively, so that it influences others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 46724, end: 46805 }
  source: "reflect on the process of learning and evaluate personal strengths and weaknesses"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["reflect", "evaluate"]
  about: "reflecting on learning and own strengths"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Reflect on how one learns and judge one's own strengths and weaknesses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 46808, end: 46850 }
  source: "develop the skills for autonomous learning"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["develop"]
  about: "skills for autonomous learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Build the skills to learn independently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 46853, end: 46910 }
  source: "plan and organise workloads, including project management"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["plan", "organise"]
  about: "planning workloads and managing projects"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Plan and organise workloads, project management included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 46913, end: 46941 }
  source: "develop leadership qualities"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["develop"]
  about: "leadership"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Grow qualities of leadership."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 46944, end: 46977 }
  source: "work effectively as a team member"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["work"]
  about: "working well in a team"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Contribute well as a member of a team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 46980, end: 47025 }
  source: "work online and remotely as well as in person"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["work"]
  about: "working online, remotely and in person"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Work online and at a distance as well as face to face."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b7
  locator: { number: "4.6.b7", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 47028, end: 47063 }
  source: "demonstrate professional behaviours"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "professional behaviour"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show professional conduct."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b8
  locator: { number: "4.6.b8", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 47066, end: 47147 }
  source: "display an appreciation of developing graduate skills relevant to career pathways"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["display"]
  about: "graduate skills for career pathways"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show awareness of building graduate skills that fit possible careers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b9
  locator: { number: "4.6.b9", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 47150, end: 47287 }
  source: "recognise the importance of planning for personal, career and professional development, including identifying and working towards targets"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["recognise"]
  about: "planning personal, career and professional development"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "See why planning for personal, career and professional growth matters, including setting and working towards targets."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b10
  locator: { number: "4.6.b10", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 47290, end: 47331 }
  source: "recognise and respect the views of others"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["recognise", "respect"]
  about: "respecting the views of others"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Recognise and respect other people's views."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b11
  locator: { number: "4.6.b11", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 47334, end: 47460 }
  source: "demonstrate an understanding of the importance of risk assessment and associated legislation for health, safety and well-being"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "risk assessment and health and safety law"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show understanding of why risk assessment and the related health, safety and well-being law matter."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b12
  locator: { number: "4.6.b12", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 47463, end: 47566 }
  source: "recognise the importance of equality, diversity and inclusivity and develop behaviours that support EDI"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["recognise", "develop", "support"]
  about: "EDI and inclusive behaviour"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "See why equality, diversity and inclusivity matter and develop behaviour that supports EDI."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b13
  locator: { number: "4.6.b13", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 47569, end: 47686 }
  source: "appreciate the need to act and work in an ethical and sustainable manner and in compliance with relevant legislation."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in ES3 at the threshold"
  addressee: learner
  verbs: ["appreciate", "act", "work"]
  about: "acting ethically, sustainably and lawfully"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Appreciate the need to act and work ethically and sustainably and within the relevant law."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.7
  locator: { number: "4.7", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 47691, end: 48252 }
  source: "In addition to the competencies developed over the course of their programme, graduates of integrated master’s courses will have gained significant specialism in a specific subject area through developing and leading an independent research project. Graduates of integrated master’s courses will demonstrate the ability to independently interrogate the relevant literature, applying ideas, techniques and data to a range of questions, demonstrating key skills and working independently to design and carry out a project to address important practical questions."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of integrated master's courses"
  addressee: learner
  verbs: ["gained", "demonstrate", "interrogate", "applying", "design", "carry"]
  about: "specialism and an independent research project"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Beyond the skills built over the course, integrated master's graduates will have gained a substantial specialism by developing and leading an independent research project, and will show they can probe the literature on their own, apply ideas, techniques and data to varied questions and design and run a project on a significant practical question."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.8
  locator: { number: "4.8", headingPath: ["Benchmark standards", "Personal and professional skills"] }
  span: { start: 48257, end: 48545 }
  source: "At postgraduate (MSc or MA) level it is expected that students will build on the competencies listed above that are developed in their undergraduate studies but focus in greater depth on a specific aspect of the subject area, achieving knowledge and skills to enhance their employability."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "taught postgraduate (MSc or MA) students"
  addressee: learner
  verbs: ["build", "focus", "achieving", "enhance"]
  about: "postgraduate depth in one aspect of the subject"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "At taught postgraduate level (MSc or MA), students are expected to build on the competencies from their first degree and go deeper into one aspect of the subject, gaining knowledge and skills that make them more employable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.2
  forPractitioner: { text: "Prepare students for a working world in which they will be required to ground decisions in sound science and to weigh equity and inclusion, so that the solutions they propose last; the climate and biodiversity crises are the setting for the whole course.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be expected, in your working life, to make sure that the decisions you take part in rest on sound science and treat people fairly, so that the solutions you help to build last.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat para 1.2 as a stated expectation of ES3 graduates across all the awards covered, in 'will be required' terms: decisions grounded in sound science that weigh fairness and inclusion and aim at lasting solutions. Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 1.2. Do not present it as a threshold outcome from section 4 or as a professional licensing rule. Set it beside the threshold items 4.6.b13 and 4.3.b5 and the honours descriptor qaa/fheq-2024/4.15.b9.2 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks why the subjects matter now or what graduates are trusted to do. For a student, say plainly that you will be expected to base decisions on evidence and fairness; for staff, frame it as the purpose the course serves. Ask: Where in your work have you had to weigh evidence and fairness together before reaching a decision? Avoid reading the paragraph aloud or treating it as a graded outcome."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.5
  forPractitioner: { text: "Read environment, in every part of the statement, as covering all living things, people and other species alike, and carry that breadth into course documents.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a note to readers on how to read a term in the document, not a standard for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat para 1.5 as a reading instruction in 'should' terms: wherever the statement says environment, it means all living things, human and non-human. Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 1.5 when you define the term in a course document. Do not narrow environment to the physical or natural world alone. Set it beside para 1.10, which says sustainability is not only about the environment."
  author-agent-dialogue: "Raise it when a programme team drafts outcomes or a teacher frames a topic and the word environment is doing a lot of work. Put it plainly to staff as a broad reading that takes in people and other species. Ask: Does your course use environment to include people, or only the natural world? Do not present it to a student as an outcome."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.8
  forPractitioner: { text: "Treat equality, diversity and inclusion as subject content and as practice; your teaching community carries a duty to challenge and help remove barriers to taking part, for example through equality impact assessments, and to build safe, inclusive spaces where curricula can be co-produced with students.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the academic community and the course, not a standard for the student", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat para 1.8 as a duty on ES3 academic communities to challenge and help dismantle barriers to taking part; the word is duty, recorded here as descriptive force because it is none of must, should, may or will. Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 1.8. Do not call it a legal duty or a student outcome. Set it beside para 1.9, the student-facing outcome 4.6.b12 and para 2.2 on accessibility."
  author-agent-dialogue: "Raise it with a programme team or teacher when barriers to taking part in ES3, equality impact assessments or co-produced curricula comes up in design, approval or review, framed for staff as something the course ought to do. Ask: Which barriers to fieldwork, labs or class discussion have you identified, and what has the team done about them? Do not hand it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.9
  forPractitioner: { text: "Use the discipline itself to explore EDI, by questioning its stereotypes and colonial history and valuing other knowledge systems; graduates will be culturally aware, ethical and respectful and able to reflect on equality in the subject; they will also think in systems, adapt and work across disciplines.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will become culturally aware, act ethically and with respect, reflect on equality in your subject, think in terms of whole systems, adapt to change and stay open to ways of knowing that differ from your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat para 1.9 as a stated outcome in 'will' terms for ES3 graduates generally, read here at honours level (FHEQ level 6, FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 1.9. Do not present it as one of the section 4 threshold items, though it overlaps them. Set it beside 4.6.b10, 4.6.b12 and 4.5.b3, and beside qaa/fheq-2024/4.15.b9.1 and spine:6 in std:ref:uk-framework."
  author-agent-dialogue: "Raise it when a student reflects on fieldwork with communities, on colonial history in the subject or on working with people from other disciplines. For a student, put it in plain words as qualities you will grow; for staff, as outcomes the curriculum should make room for. Ask: When did another culture's knowledge change how you read an environmental problem? Avoid reading the paragraph out or treating it as a checklist."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.12
  forPractitioner: { text: "When you build sustainable development into an ES3 curriculum, you should use the joint QAA and Advance HE ESD guidance for teaching, key competencies, outcomes and assessment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a pointer for course designers, not a standard for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat para 1.12 as a duty on the course or provider, in 'should' terms, about using the joint ESD guidance when building sustainable development into the curriculum; it is not an outcome a student has to show. Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 1.12. Do not call it statutory or regulatory, and do not rewrite it as a student learning outcome. Set it beside std:doc:qaa-advancehe-esd-2021-guidance, paras 1.10 and 1.11 and the content items 3.1.b1 and 3.4.b1."
  author-agent-dialogue: "Raise it with a programme team or teacher when education for sustainable development comes up in design, approval or review, framed for staff as something the course ought to do. Ask: Which of the ESD key competencies do your module outcomes and assessments already cover? Do not hand it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.16
  forPractitioner: { text: "When you build employability, enterprise and entrepreneurship into an ES3 course, you should use QAA's enterprise and entrepreneurship education guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a pointer for course designers, not a standard for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat para 1.16 as a duty on the course or provider, in 'should' terms, about using the enterprise and entrepreneurship guidance; it is not an outcome a student has to show. Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 1.16. Do not call it statutory or regulatory, and do not rewrite it as a student learning outcome. Set it beside std:doc:qaa-enterprise-2018-guidance and paras 1.13 to 1.15."
  author-agent-dialogue: "Raise it with a programme team or teacher when employability, enterprise or links with employers comes up in design, approval or review, framed for staff as something the course ought to do. Ask: Where do students meet enterprise or employer-set tasks, and have you checked them against the guidance? Do not hand it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/2.2
  forPractitioner: { text: "Design curricula and field programmes so that no one is excluded: inclusive design should let all learners take part, with flexibility and reasonable adjustments where needed; plan for the barriers labs and fieldwork can raise and use accessible technology; make risk assessments cover health, safety and well-being, including risks a student with protected characteristics may face.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat para 2.2 as a duty on the course or provider, in 'should' terms, about accessible curriculum and field design, reasonable adjustments and inclusive risk assessment; it is not an outcome a student has to show. Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 2.2. Do not call it statutory or regulatory, and do not rewrite it as a student learning outcome. Set it beside para 3.16 on inclusive fieldwork, para 3.19 on inclusive assessment and the student-facing items 4.4.b4 and 4.6.b11."
  author-agent-dialogue: "Raise it with a programme team or teacher when fieldwork, laboratory work or blended options for disabled students or students with protected characteristics comes up in design, approval or review, framed for staff as something the course ought to do. Ask: Does your field programme risk assessment name the specific risks a student with protected characteristics might face? Do not hand it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/2.3
  forPractitioner: { text: "Plan each year so attainment builds towards every threshold skill by the end of the honours degree (FHEQ level 6; SCQF level 10); in an integrated master's (FHEQ level 7; SCQF level 11), the extra year will leave students able to show stronger critical thinking, evaluation and independence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Each year of your honours degree will build your knowledge and experience towards the full set of skills expected at graduation; if you take an integrated master's, your extra year will leave you thinking more critically, evaluating more sharply and working more independently.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat para 2.3 as a stated expectation of progression in 'will' and 'are able to' terms: year-on-year attainment that builds to all the threshold skills at honours (FHEQ level 6, FQHEIS level 10), and a further step at integrated master's (FHEQ level 7, FQHEIS level 11). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 2.3. Do not claim it fixes what each year must contain or that it sets a separate master's standard. Set it beside 4.1, 4.7, qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b6 and the steps spine:6 and spine:7."
  author-agent-dialogue: "Raise it when a student asks how their years add up or a team maps outcomes across levels. For a student, explain in plain words that each year builds towards what you need by graduation; for staff, frame it as a progression design question. Ask: Which threshold skills does each year of the course build, and where does the master's year add independence? Do not read out the paragraph or treat its exit awards as targets."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/2.4
  forPractitioner: { text: "A graduate with a second-class honours degree or better would normally be expected to be capable of and ready for postgraduate study in ES3 or related sustainability fields, including cross-disciplinary courses.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "If you graduate with a second-class degree or higher, you would normally be ready to go on to postgraduate study in your subject, in a related sustainability field or on a course that combines disciplines.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat para 2.4 as an expectation the statement words as 'would normally be expected', recorded as descriptive force: readiness for postgraduate study for honours graduates at a 2:2 or above (FHEQ level 6). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 2.4. Do not present it as an entry rule for any postgraduate course or as a promise. Set it beside Annex D (qaa/fheq-2024/annex-d/summary) and qaa/fheq-2024/4.15.b9.3."
  author-agent-dialogue: "Raise it when a student asks whether their likely classification opens postgraduate study. In plain words and the second person, say that a second-class result or above normally leaves you ready, and that each course sets its own entry terms. Ask: Which postgraduate field are you looking at, and what does it ask for? Avoid treating it as a guarantee of entry."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/2.5
  forPractitioner: { text: "Joint honours students will achieve some of the ES3 subject-specific and generic skills, with others drawn from the partner subject; map which ones each route covers.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study ES3 in a joint honours degree, you will gain some of its subject and general skills and add others from your second subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat para 2.5 as a stated outcome in 'will' terms for joint honours students at FHEQ level 6: they reach some, not all, of the ES3 skills. Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 2.5. Do not claim that joint honours graduates meet every threshold item in 4.3 to 4.6. Set it beside 4.1 and qaa/fheq-2024/4.15.i1 (honours meets the descriptor in full)."
  author-agent-dialogue: "Raise it when a joint honours student or team asks which ES3 skills apply. For a student, say plainly that you will gain part of the ES3 skills and others from your second subject; for staff, frame it as a mapping task. Ask: Which of the threshold skills in sections 4.3 to 4.6 does your ES3 half cover? Avoid implying they fall short of honours."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b1
  forPractitioner: { text: "Teach what sustainable development and systems thinking are and how they are put to use; this should line up with the joint ESD guidance from QAA and Advance HE.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You can expect to learn what sustainable development and systems thinking mean and how they are used in Earth science.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat 3.1, item 1 (sustainable development and systems thinking) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive for the knowledge, with a 'should' on how the topic aligns with the ESD guidance. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 1. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers sustainable development and systems thinking. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Where in the course do students apply systems thinking to a sustainability problem? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b2
  forPractitioner: { text: "Cover the origin of the Earth and other planets and their position in the solar system.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn how the Earth and the other planets formed and how they fit into the solar system.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 2 (how the Earth and planets formed) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 2. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers how the Earth and planets formed. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Where does the course teach planetary formation and the solar system? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b3
  forPractitioner: { text: "Teach the field's core paradigms, from uniformitarianism and deep time to evolution and plate tectonics.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to understand the big ideas of Earth science: that present processes explain the past, how vast geological time is, how life evolved and how plates move.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 3 (the central paradigms of the Earth sciences) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 3. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers the central paradigms of the Earth sciences. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Can you explain how plate tectonics and uniformitarianism shape the way you read a rock sequence? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b4
  forPractitioner: { text: "Cover stratigraphy and the stratigraphic column, the fossil record, geochronology, process rates and major events in Earth history.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn how geological time is measured and divided, what the fossil record shows and which major events shaped Earth's history.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 4 (geological time and Earth history) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 4. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers geological time and Earth history. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which dating methods have you used, and how confident are you in the ages they gave? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b5
  forPractitioner: { text: "Teach how the solid Earth, hydrosphere, atmosphere, cryosphere and biosphere are built and composed and the processes and cycles linking them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn what the solid Earth, oceans, atmosphere, ice and living world are made of and how matter and energy move between them.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 5 (Earth spheres and the cycling of matter and energy) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 5. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers Earth spheres and the cycling of matter and energy. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Can you trace one element or form of energy through several Earth spheres? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b6
  forPractitioner: { text: "Teach the biological, chemical and physical processes that explain how Earth and planetary systems work.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to understand the biological, chemical and physical processes that explain how the Earth and other planets work.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 6 (processes behind Earth and planetary systems) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 6. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers processes behind Earth and planetary systems. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which processes, biological, chemical or physical, do you find hardest to connect? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b7
  forPractitioner: { text: "Teach structures, materials and processes so students appreciate how they vary in time and space at appropriate scales.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to study structures, materials and processes and how they change across time and place, from small to large scales.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 7 (variation in time and space at fitting scales) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 7. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers variation in time and space at fitting scales. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: How does the scale you work at change what you can say about a process? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b8
  forPractitioner: { text: "Cover the formation of igneous, metamorphic and sedimentary rocks.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn how igneous, metamorphic and sedimentary rocks form.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 8 (formation of the main rock types) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 8. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers formation of the main rock types. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Can you explain how each main rock type forms and give a field example? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b9
  forPractitioner: { text: "Teach students to identify rocks, minerals, fossils and geological structures and to use the field's terminology, nomenclature and classification.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn to identify rocks, minerals, fossils and geological structures and to name and classify them correctly.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 9 (identifying rocks, minerals, fossils and structures) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 9. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers identifying rocks, minerals, fossils and structures. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: How reliably can you identify common rocks and minerals in hand specimen? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b10
  forPractitioner: { text: "Teach collection and analysis of surface and subsurface data and their presentation, manipulation, modelling and extrapolation in four dimensions, including incomplete data.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn to collect and analyse data from above and below ground and to model and extend them across space and time, even when they are incomplete.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 10 (collecting and modelling Earth data in four dimensions) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 10. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers collecting and modelling Earth data in four dimensions. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Where have you had to extrapolate from incomplete subsurface data, and how did you handle the gaps? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b11
  forPractitioner: { text: "Train students to observe and interpret field data, in situ or virtual, from first principles.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn to observe in the field, in person or virtually, and to interpret what you see by reasoning from first principles.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 11 (interpreting field data from first principles) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 11. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers interpreting field data from first principles. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which field observation have you interpreted without a model answer to lean on? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b12
  forPractitioner: { text: "Teach surveying and measurement in field and laboratory using quantitative and instrumental techniques.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn to survey and take measurements in the field and the laboratory with numerical methods and instruments.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 12 (surveying and measuring in the field and laboratory) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 12. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers surveying and measuring in the field and laboratory. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which instruments have you used, and how did you check their readings? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b13
  forPractitioner: { text: "Teach the use of qualitative and quantitative data and datasets and how to assess data quality and uncertainty.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn to work with both qualitative and numerical data and to judge how good and how certain your data are.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 13 (data use, quality and uncertainty) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 13. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers data use, quality and uncertainty. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: How do you decide how much to trust a dataset? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b14
  forPractitioner: { text: "Teach the role of the Earth sciences in resource management and in mitigating and adapting to environmental hazards, including climate change.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to understand how Earth science helps manage natural resources and lessen and adapt to hazards such as climate change.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 14 (Earth sciences in resources, hazards and climate change) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 14. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers Earth sciences in resources, hazards and climate change. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Can you give an example where Earth science changed how a resource or hazard was managed? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b15
  forPractitioner: { text: "Develop students' awareness that the subject and its application sit within a wider socioeconomic and environmental context.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to become aware that what you learn and how it is used sit within wider social, economic and environmental concerns.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 15 (the wider socioeconomic and environmental context) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 15. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers the wider socioeconomic and environmental context. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Who else, beyond scientists, has a stake in the problem you are studying? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b16
  forPractitioner: { text: "Teach the ethics of the discipline's legacy and uses, engage students in current debates and help them see the case for decolonisation.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to explore the ethical questions raised by Earth science's past and present uses, join current debates and understand why decolonising the subject matters.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 16 (ethics, legacy and decolonisation of the discipline) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 16. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers ethics, legacy and decolonisation of the discipline. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which part of the subject's history raises ethical questions for you? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b17
  forPractitioner: { text: "Teach why equality, diversity and inclusivity matter in Earth science practice.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to understand why equality, diversity and inclusion matter in how Earth science is done.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 17 (EDI in the practice of the discipline) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 17. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers EDI in the practice of the discipline. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Who is missing from fieldwork and research in your area, and why? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b18
  forPractitioner: { text: "Teach fieldwork codes of practice and have students complete health and safety risk assessments confidently.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn the codes of practice for fieldwork and to complete health and safety risk assessments with confidence.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.1, item 18 (fieldwork codes and risk assessment) as knowledge the statement expects an honours graduate in Earth sciences to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.1, item 18. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers fieldwork codes and risk assessment. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Have you written a field risk assessment yourself, and what did it make you change? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b1
  forPractitioner: { text: "Teach what sustainable development and systems thinking are and how they are put to use; this should line up with the joint ESD guidance from QAA and Advance HE.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You can expect to learn what sustainable development and systems thinking mean and how they are used in environmental work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat 3.4, item 1 (sustainable development and systems thinking) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive for the knowledge, with a 'should' on how the topic aligns with the ESD guidance. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 1. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers sustainable development and systems thinking. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Where in the course do students apply systems thinking to a sustainability problem? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b2
  forPractitioner: { text: "Take a holistic approach to the complexity and interconnections of Earth's systems and processes.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to study the Earth's systems and processes as a connected whole.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 2 (a holistic view of Earth systems) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 2. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers a holistic view of Earth systems. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Can you show how a change in one Earth system spreads to others? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b3
  forPractitioner: { text: "Teach the principles of sustainability and sustainable approaches to managing natural and human-induced resource cycles.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn the principles of sustainability and how to manage the use of resources sustainably.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 3 (sustainability principles and resource cycles) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 3. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers sustainability principles and resource cycles. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which resource cycle have you analysed, and where could it be made more sustainable? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b4
  forPractitioner: { text: "Teach why timescale, geological, present, short and long term and future, matters to the impacts of natural and human activities on ecosystems.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to understand how looking over different timescales, from geological to future, changes how you judge effects on ecosystems.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 4 (timescale and impacts on ecosystems) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 4. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers timescale and impacts on ecosystems. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: How would your conclusion change if you looked over a century instead of a decade? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b5
  forPractitioner: { text: "Teach how human effects on the environment, and responses to change, differ from the global scale down to the local.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to understand how human effects on the environment, and responses to change, play out from global to local scales.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 5 (spatial scale of human impacts) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 5. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers spatial scale of human impacts. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which local issue you know links to a global pattern? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b6
  forPractitioner: { text: "Teach the interconnections and interdependencies of organisms in natural and managed ecosystems.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn how living things in natural and managed ecosystems depend on each other.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 6 (interdependence of organisms in ecosystems) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 6. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers interdependence of organisms in ecosystems. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Can you map the dependencies in one ecosystem you have studied? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b7
  forPractitioner: { text: "Teach the positive and negative environmental impacts of development and the management tools that address them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn how development helps and harms the environment and which tools can manage those effects.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 7 (impacts of development and tools to manage them) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 7. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers impacts of development and tools to manage them. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which management tool would you choose for a development you know, and why? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b8
  forPractitioner: { text: "Teach how environmental change affects people, other species and built infrastructure.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn how environmental change affects people, other species and the things we build.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 8 (effects of environmental change on people, other species and infrastructure) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 8. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers effects of environmental change on people, other species and infrastructure. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which group, species or structure is most exposed in a case you have studied? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b9
  forPractitioner: { text: "Teach monitoring, modelling and management of natural and human-induced environmental change and behaviour.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn to monitor, model and manage environmental change, whether natural or caused by people.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 9 (monitoring, modelling and managing environmental change) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 9. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers monitoring, modelling and managing environmental change. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which monitoring or modelling method have you used, and what did it miss? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b10
  forPractitioner: { text: "Teach how to predict, mitigate and manage risks from environmental change and human pressures.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn how to forecast, reduce and manage risks from a changing environment and from human pressure.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 10 (predicting and managing environmental risk) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 10. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers predicting and managing environmental risk. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: How did you weigh likelihood against impact in a risk you assessed? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b11
  forPractitioner: { text: "Teach what uncertainty is and how it affects present and future decisions.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to understand uncertainty and how it affects decisions now and later.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 11 (uncertainty in decision-making) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 11. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers uncertainty in decision-making. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: How did you communicate uncertainty in your last piece of advice or report? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b12
  forPractitioner: { text: "Teach how institutions, organisations, governance structures and stakeholders manage and regulate what people do to the environment.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn how institutions, organisations, governments and other stakeholders manage and regulate human effects on the environment.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 12 (institutions and governance of human impacts) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 12. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers institutions and governance of human impacts. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which body regulates the issue you are studying, and how well does it work? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b13
  forPractitioner: { text: "Teach why environmental science and environmental studies matter for managing resources and for reducing and adapting to hazards, climate change included.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to understand how your subject helps manage resources and lessen and adapt to hazards such as climate change.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 13 (the subjects in resources, hazards and climate change) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 13. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers the subjects in resources, hazards and climate change. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Can you give an example where environmental evidence changed how a hazard was managed? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b14
  forPractitioner: { text: "Train students to observe and interpret field data, in situ or virtual, from first principles.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn to observe in the field, in person or virtually, and to interpret what you see by reasoning from first principles.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 14 (interpreting field data from first principles) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 14. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers interpreting field data from first principles. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which field observation have you interpreted without a model answer to lean on? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b15
  forPractitioner: { text: "Teach the use of qualitative and quantitative data and datasets and how to assess data quality and uncertainty.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn to work with both qualitative and numerical data and to judge how good and how certain your data are.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 15 (data use, quality and uncertainty) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 15. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers data use, quality and uncertainty. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: How do you decide how much to trust a dataset? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b16
  forPractitioner: { text: "Develop relevant, appropriate digital skills and use of technology.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to build the digital skills and confidence with technology your field needs.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 16 (digital skills and technology) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 16. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers digital skills and technology. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which digital tools will you need in the job you want, and which can you already use? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b17
  forPractitioner: { text: "Develop students' awareness that the subject and its application sit within a wider socioeconomic and environmental context.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to become aware that what you learn and how it is used sit within wider social, economic and environmental concerns.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 17 (the wider socioeconomic and environmental context) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 17. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers the wider socioeconomic and environmental context. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Who else, beyond scientists, has a stake in the problem you are studying? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b18
  forPractitioner: { text: "Teach the ethics of the discipline's legacy and uses, engage students in current debates and help them see the case for decolonisation.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to explore the ethical questions raised by your subject's past and present uses, join current debates and understand why decolonising it matters.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 18 (ethics, legacy and decolonisation of the discipline) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 18. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers ethics, legacy and decolonisation of the discipline. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which part of the subject's history raises ethical questions for you? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b19
  forPractitioner: { text: "Teach why equality, diversity and inclusivity matter in environmental practice.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to understand why equality, diversity and inclusion matter in how your subject is practised.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 19 (EDI in the practice of the discipline) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 19. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers EDI in the practice of the discipline. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Who is missing from environmental decision-making in your area, and why? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b20
  forPractitioner: { text: "Teach fieldwork codes of practice and have students complete health and safety risk assessments confidently.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn the codes of practice for fieldwork and to complete health and safety risk assessments with confidence.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.4, item 20 (fieldwork codes and risk assessment) as knowledge the statement expects an honours graduate in environmental sciences or environmental studies to hold; its force is descriptive: content the statement anticipates, not a requirement. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.4, item 20. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the threshold item 4.3.b1 and the Earth sciences list in 3.1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers fieldwork codes and risk assessment. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Have you written a field risk assessment yourself, and what did it make you change? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.7.b1
  forPractitioner: { text: "Include scientific study of the physical, chemical, biological and human-made processes that act on ecosystems.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to study scientifically the physical, chemical, biological and human processes that act on ecosystems.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.7, item 1 (scientific study of processes acting on ecosystems) as knowledge the statement expects an honours graduate in environmental sciences to hold; its force is descriptive: the course is normally expected to include it, a word outside must, should, may and will. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.7, item 1. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the shared list in 3.4 and the threshold item 4.3.b1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers scientific study of processes acting on ecosystems. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which process acting on an ecosystem have you measured directly? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.7.b2
  forPractitioner: { text: "Include major environmental processes across scales from global to organismal and, where relevant, to molecular and atomic levels.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn the main environmental processes from the global scale down to single organisms and, where useful, molecules and atoms.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.7, item 2 (environmental processes from global to atomic scale) as knowledge the statement expects an honours graduate in environmental sciences to hold; its force is descriptive: the course is normally expected to include it, a word outside must, should, may and will. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.7, item 2. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the shared list in 3.4 and the threshold item 4.3.b1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers environmental processes from global to atomic scale. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: At which scale do you feel least confident explaining a process? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.7.b3
  forPractitioner: { text: "Include a scientific, multidisciplinary approach to identifying, understanding and managing Earth's structure, processes and ecosystems.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn a scientific approach, drawing on several disciplines, to recognising, understanding and managing the structure, processes and ecosystems of the Earth.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.7, item 3 (a scientific approach to Earth's structure, processes and ecosystems) as knowledge the statement expects an honours graduate in environmental sciences to hold; its force is descriptive: the course is normally expected to include it, a word outside must, should, may and will. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.7, item 3. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the shared list in 3.4 and the threshold item 4.3.b1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers a scientific approach to Earth's structure, processes and ecosystems. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which disciplines did you draw on in your last environmental investigation? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.7.b4
  forPractitioner: { text: "Include using scientific and technical information and tools to support decisions and environmental management.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn to use scientific information and technical tools to support decisions and environmental management.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.7, item 4 (scientific information and tools for decisions) as knowledge the statement expects an honours graduate in environmental sciences to hold; its force is descriptive: the course is normally expected to include it, a word outside must, should, may and will. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.7, item 4. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the shared list in 3.4 and the threshold item 4.3.b1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers scientific information and tools for decisions. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which tool or dataset have you used to support an environmental decision? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.7.b5
  forPractitioner: { text: "Include observation and interpretation of field data, in situ or virtual, from first principles.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn to observe in the field, in person or virtually, and to interpret what you see from first principles.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.7, item 5 (interpreting field data from first principles) as knowledge the statement expects an honours graduate in environmental sciences to hold; its force is descriptive: the course is normally expected to include it, a word outside must, should, may and will. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.7, item 5. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the shared list in 3.4 and the threshold item 4.3.b1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers interpreting field data from first principles. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which field observation have you interpreted without a model answer to lean on? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.7.b6
  forPractitioner: { text: "Include surveying and measurement in field and laboratory using quantitative and instrumental techniques.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn to survey and take measurements in the field and the laboratory with numerical methods and instruments.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.7, item 6 (surveying and measuring in the field and laboratory) as knowledge the statement expects an honours graduate in environmental sciences to hold; its force is descriptive: the course is normally expected to include it, a word outside must, should, may and will. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.7, item 6. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the shared list in 3.4 and the threshold item 4.3.b1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers surveying and measuring in the field and laboratory. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which instruments have you used, and how did you check their readings? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.10.b1
  forPractitioner: { text: "Include the history and present evidence of natural and human-induced environmental change.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to learn the history of environmental change, both natural and caused by people, and the evidence for it today.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.10, item 1 (history and evidence of environmental change) as knowledge the statement expects an honours graduate in environmental studies to hold; its force is descriptive: the course is normally expected to include it, a word outside must, should, may and will. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.10, item 1. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the shared list in 3.4 and the threshold item 4.3.b1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers history and evidence of environmental change. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: What evidence would you use to separate natural from human-caused change in a case you know? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.10.b2
  forPractitioner: { text: "Include the social, political and economic consequences of how people interact with the environment.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to understand the social, political and economic consequences of how people treat the environment.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.10, item 2 (social, political and economic implications) as knowledge the statement expects an honours graduate in environmental studies to hold; its force is descriptive: the course is normally expected to include it, a word outside must, should, may and will. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.10, item 2. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the shared list in 3.4 and the threshold item 4.3.b1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers social, political and economic implications. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: Which political or economic factor most shaped the environmental issue you are studying? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.10.b3
  forPractitioner: { text: "Include how the environment relates to human cultures and their values.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to understand how the environment and human cultures and values shape each other.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat 3.10, item 3 (environment, culture and values) as knowledge the statement expects an honours graduate in environmental studies to hold; its force is descriptive: the course is normally expected to include it, a word outside must, should, may and will. Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.10, item 3. Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. Set it beside the shared list in 3.4 and the threshold item 4.3.b1 and qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team checks whether a course covers environment, culture and values. Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. Ask: How do different communities value the same landscape you have studied? Do not read the whole list aloud or treat one item as a pass condition."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.14
  forPractitioner: { text: "Choose your own teaching and learning methods, but check that students can reach the outcomes through them and that the outcomes are stated clearly to students.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat para 3.14 as a duty on the course or provider, in 'should' terms, about matching teaching methods to outcomes and stating outcomes clearly; it is not an outcome a student has to show. Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.14. Do not call it statutory or regulatory, and do not rewrite it as a student learning outcome. Set it beside paras 3.15, 3.19 and qaa/fheq-2024/4.15."
  author-agent-dialogue: "Raise it with a programme team or teacher when module outcomes and teaching methods comes up in design, approval or review, framed for staff as something the course ought to do. Ask: Can a student reach each outcome through the methods the module actually uses, and is each outcome written so a student understands it? Do not hand it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.15
  forPractitioner: { text: "Pick teaching and learning methods that are inclusive and fit to develop the knowledge and skills sections 1 and 2 describe; research-led and enquiry-based designs are one option.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat para 3.15 as a duty on the course or provider, in 'should' terms, about choosing inclusive teaching methods fit for the subject knowledge and skills; it is not an outcome a student has to show. Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.15. Do not call it statutory or regulatory, and do not rewrite it as a student learning outcome. Set it beside paras 3.14, 3.16 and 2.2."
  author-agent-dialogue: "Raise it with a programme team or teacher when choosing teaching methods comes up in design, approval or review, framed for staff as something the course ought to do. Ask: Which methods in your module would exclude some students, and what would an inclusive alternative look like? Do not hand it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.16
  forPractitioner: { text: "Give every student substantial fieldwork, integrated with theory; design field and practical activities to be inclusive, and arrange reasonable adjustments where required so that all students can take part in practical work and fieldwork.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat para 3.16 as a duty on the course or provider, in 'should' terms, about inclusive field and practical work, with reasonable adjustments; it is not an outcome a student has to show. Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.16. Do not call it statutory or regulatory, and do not rewrite it as a student learning outcome. Set it beside para 2.2 and the threshold items 4.4.b1, 4.4.b2 and 4.4.b4."
  author-agent-dialogue: "Raise it with a programme team or teacher when fieldwork, field trips or practical classes comes up in design, approval or review, framed for staff as something the course ought to do. Ask: For each field activity, what reasonable adjustment is ready if a student cannot take part as planned? Do not hand it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.17
  forPractitioner: { text: "Ground teaching and learning in education for sustainable development, and choose methods that themselves practise sustainable principles and solutions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat para 3.17 as a duty on the course or provider, in 'should' terms, about grounding teaching and learning in ESD; it is not an outcome a student has to show. Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 3.17. Do not call it statutory or regulatory, and do not rewrite it as a student learning outcome. Set it beside para 3.22, para 1.12 and std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise it with a programme team or teacher when how sustainability shows in teaching comes up in design, approval or review, framed for staff as something the course ought to do. Ask: How do the module's own teaching methods practise sustainability, not only teach about it? Do not hand it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.2
  forPractitioner: { text: "Expect most students to go well beyond the threshold; set your own evidence for this and use Annex D's descriptions of first, upper second, lower second and third-class honours (FHEQ level 6; FQHEIS level 10).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in judging classifications", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat para 4.2 as a provider duty in 'should' terms: judge performance above the threshold against Annex D at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.2. Do not claim the statement sets its own typical or excellent rung, and do not read Annex D as subject-specific. Set it beside 4.1 and qaa/fheq-2024/annex-d/summary (SL6 in std:doc:qaa-fheq-2024-framework)."
  author-agent-dialogue: "Raise it with a programme team or teacher when classification or what earns a 2:1 or a first comes up in design, approval or review, framed for staff as something the course ought to do. Ask: Where do your marking criteria draw on the Annex D class descriptions for the ES3 threshold skills? Do not hand it to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b1
  forPractitioner: { text: "At threshold, graduates know and understand the subject's own theories, paradigms, concepts and principles.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the time you graduate with honours, you will know and understand the main theories, paradigms, concepts and principles of your subject.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.3, item 1 (subject theories, paradigms, concepts and principles) as a threshold standard among the intellectual skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.3, item 1. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 3.1.b3 and 3.4.b2 and the honours descriptor qaa/fheq-2024/4.15.b1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about subject theories, paradigms, concepts and principles. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Which core idea of your subject could you explain to a first-year student? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b2
  forPractitioner: { text: "At threshold, graduates combine evidence from several sources to test findings and hypotheses.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to combine evidence from different sources to test findings and hypotheses.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.3, item 2 (testing findings against several sources of evidence) as a threshold standard among the intellectual skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.3, item 2. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.3.b4 and 4.3.b6 and the honours descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about testing findings against several sources of evidence. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: When did evidence from a second source change a finding you were sure of? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b3
  forPractitioner: { text: "At threshold, graduates weigh up and judge issues from several multidisciplinary and interdisciplinary viewpoints.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to look at an issue from the viewpoints of several disciplines and judge them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.3, item 3 (looking at issues across disciplines) as a threshold standard among the intellectual skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.3, item 3. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.3.b2 and 1.9 and the honours descriptor qaa/fheq-2024/4.15.b3.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about looking at issues across disciplines. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Which other discipline has changed how you see an environmental issue? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b4
  forPractitioner: { text: "At threshold, graduates analyse, synthesise, summarise, appraise and critically evaluate information.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to analyse, pull together, summarise and critically judge information.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.3, item 4 (analysing and critically evaluating information) as a threshold standard among the intellectual skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.3, item 4. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.3.b8 and 4.5.b4 and the honours descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about analysing and critically evaluating information. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Where have you had to weigh conflicting information and reach a view of your own? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b5
  forPractitioner: { text: "At threshold, graduates set out complex problems and work up and judge possible solutions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to define a complex problem and come up with and judge possible solutions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.3, item 5 (defining complex problems and weighing solutions) as a threshold standard among the intellectual skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.3, item 5. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 1.2 and 4.3.b9 and the honours descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about defining complex problems and weighing solutions. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Which complex problem have you framed yourself, and how did you compare the options? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b6
  forPractitioner: { text: "At threshold, graduates form and test hypotheses and use them to shape and design investigations, experiments included.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to form and test hypotheses and use them to design investigations and experiments.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.3, item 6 (hypotheses that shape investigations) as a threshold standard among the intellectual skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.3, item 6. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.3.b2 and 4.3.b7 and the honours descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about hypotheses that shape investigations. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: How did your hypothesis shape the way you designed your last investigation? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b7
  forPractitioner: { text: "At threshold, graduates plan, carry out and present an independent project, with suitable guidance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will have planned, carried out and presented a project of your own, with suitable support.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.3, item 7 (an independent project with guidance) as a threshold standard among the intellectual skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.3, item 7. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.3.b6 and 4.7 and the honours descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about an independent project with guidance. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Which decisions in your project were yours, and where did you need guidance? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b8
  forPractitioner: { text: "At threshold, graduates read academic literature, data and other information sources critically.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will read academic work, data and other sources critically.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.3, item 8 (a critical approach to literature and data) as a threshold standard among the intellectual skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.3, item 8. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.3.b4 and qaa/fheq-2024/4.15.b3.2 and the honours descriptor qaa/fheq-2024/4.15.b5 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about a critical approach to literature and data. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: How do you decide whether a published source is reliable? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.3.b9
  forPractitioner: { text: "At threshold, graduates deal confidently and competently with uncertainty in data and in system responses.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to work confidently with uncertainty in data and in how systems behave.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.3, item 9 (handling uncertainty in data and systems) as a threshold standard among the intellectual skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.3, item 9. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 3.4.b11 and 3.1.b13 and the honours descriptor qaa/fheq-2024/4.15.b4 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about handling uncertainty in data and systems. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: How did you handle uncertainty in your last dataset or model? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b1
  forPractitioner: { text: "At threshold, graduates conduct fieldwork and laboratory investigations competently, as appropriate to the course.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to carry out fieldwork and laboratory investigations competently.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.4, item 1 (competent field and laboratory investigation) as a threshold standard among the practical skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.4, item 1. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.4.b2 and 3.16 and the honours descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about competent field and laboratory investigation. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Which field or lab investigation could you now run without supervision? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b2
  forPractitioner: { text: "At threshold, graduates describe and record observations effectively in field and laboratory.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to describe and record what you observe clearly in the field and the lab.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.4, item 2 (recording observations in field and laboratory) as a threshold standard among the practical skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.4, item 2. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.4.b1 and 3.1.b11 and the honours descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about recording observations in field and laboratory. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Could someone else repeat your work from your field or lab notes? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b3
  forPractitioner: { text: "At threshold, graduates interpret and evaluate practical results logically.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to interpret and judge practical results logically.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.4, item 3 (logical interpretation of practical results) as a threshold standard among the practical skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.4, item 3. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.4.b5 and 4.3.b2 and the honours descriptor qaa/fheq-2024/4.15.b7 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about logical interpretation of practical results. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: How did you check that your interpretation of a result followed from the data? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b4
  forPractitioner: { text: "At threshold, graduates carry out lab and field work ethically and safely, aware of the codes of conduct and the law that apply.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will carry out lab and field work ethically and safely, knowing the codes of conduct and the law that apply.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.4, item 4 (ethical and safe practical work) as a threshold standard among the practical skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.4, item 4. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 3.1.b18, 3.4.b20 and 4.6.b11 and the honours descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about ethical and safe practical work. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Which code of conduct or legal requirement shaped your last fieldwork? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b5
  forPractitioner: { text: "At threshold, graduates collect, prepare, process and interpret data with suitable techniques.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to collect, prepare, process and interpret data with the right methods.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.4, item 5 (gathering and processing data) as a threshold standard among the practical skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.4, item 5. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.4.b6 and 3.1.b10 and the honours descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about gathering and processing data. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Which step of handling your data was hardest to get right? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b6
  forPractitioner: { text: "At threshold, graduates use appropriate numerical, statistical and qualitative techniques.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to use suitable numerical, statistical and qualitative methods.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.4, item 6 (numerical, statistical and qualitative techniques) as a threshold standard among the practical skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.4, item 6. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.4.b5 and 3.1.b13 and the honours descriptor qaa/fheq-2024/4.15.b2 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about numerical, statistical and qualitative techniques. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Which statistical test would you pick for your data, and why that one? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.4.b7
  forPractitioner: { text: "At threshold, graduates use appropriate technologies to address problems effectively.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to use the right technologies to tackle problems well.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.4, item 7 (technologies for solving problems) as a threshold standard among the practical skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.4, item 7. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 3.4.b16 and 4.3.b5 and the honours descriptor qaa/fheq-2024/4.15.b6 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about technologies for solving problems. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Which technology has most helped you solve a problem in your subject? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.5.b1
  forPractitioner: { text: "At threshold, graduates communicate effectively with varied audiences across formats and media.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to communicate well with different audiences in different formats and media.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.5, item 1 (communicating with varied audiences and media) as a threshold standard among the communication skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.5, item 1. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.5.b5 and 3.21 and the honours descriptor qaa/fheq-2024/4.15.b8 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about communicating with varied audiences and media. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Who was the least specialist audience you have explained your work to, and how did you adapt? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.5.b2
  forPractitioner: { text: "At threshold, graduates have good interpersonal communication skills for effective team working.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will communicate well with others so that the teams you work in function effectively.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.5, item 2 (interpersonal skills for teamwork) as a threshold standard among the communication skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.5, item 2. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.6.b5 and 3.16 and the honours descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about interpersonal skills for teamwork. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: What did you do the last time a team you were in stopped communicating well? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.5.b3
  forPractitioner: { text: "At threshold, graduates acknowledge and understand different perspectives.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will recognise and understand points of view that differ from yours.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.5, item 3 (recognising different perspectives) as a threshold standard among the communication skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.5, item 3. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.6.b10 and 1.9 and the honours descriptor qaa/fheq-2024/4.15.b8 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about recognising different perspectives. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Which view you disagreed with did you come to understand better? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.5.b4
  forPractitioner: { text: "At threshold, graduates articulate and synthesise an argument effectively.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to build an argument and express it clearly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.5, item 4 (building and expressing an argument) as a threshold standard among the communication skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.5, item 4. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.3.b4 and 4.5.b5 and the honours descriptor qaa/fheq-2024/4.15.b8 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about building and expressing an argument. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Can you state the main line of your last essay or report in two sentences? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.5.b5
  forPractitioner: { text: "At threshold, graduates present a case in an influential, persuasive way.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to present a case in a way that persuades others.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.5, item 5 (making a persuasive case) as a threshold standard among the communication skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.5, item 5. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.5.b1 and 4.5.b4 and the honours descriptor qaa/fheq-2024/4.15.b3.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about making a persuasive case. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: When did you change someone's mind with evidence, and how did you present it? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b1
  forPractitioner: { text: "At threshold, graduates reflect on their learning process and evaluate their own strengths and weaknesses.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will reflect on how you learn and judge your own strengths and weaknesses.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.6, item 1 (reflecting on learning and own strengths) as a threshold standard among the personal and professional skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.6, item 1. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.6.b9 and 3.20 and the honours descriptor qaa/fheq-2024/4.15.b5 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about reflecting on learning and own strengths. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: What has your last piece of feedback told you about how you learn? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b2
  forPractitioner: { text: "At threshold, graduates develop the skills for autonomous learning.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will have built the skills to learn on your own.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.6, item 2 (skills for autonomous learning) as a threshold standard among the personal and professional skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.6, item 2. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.6.b1 and qaa/fheq-2024/4.15.b9.3 and the honours descriptor qaa/fheq-2024/4.15.b5 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about skills for autonomous learning. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: What did you last teach yourself without a class, and how? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b3
  forPractitioner: { text: "At threshold, graduates plan and organise workloads, including project management.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to plan and organise your workload and manage a project.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.6, item 3 (planning workloads and managing projects) as a threshold standard among the personal and professional skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.6, item 3. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.3.b7 and the honours descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about planning workloads and managing projects. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: How did you plan your time on your last large piece of work? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b4
  forPractitioner: { text: "At threshold, graduates develop leadership qualities.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will have developed qualities that let you lead others.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.6, item 4 (leadership) as a threshold standard among the personal and professional skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.6, item 4. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.6.b5 and 3.16 and the honours descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about leadership. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: When have you led a group, and what would you do differently? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b5
  forPractitioner: { text: "At threshold, graduates work effectively as team members.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will work well as a member of a team.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.6, item 5 (working well in a team) as a threshold standard among the personal and professional skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.6, item 5. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.5.b2 and 4.6.b4 and the honours descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about working well in a team. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: What part do you usually play in a team, and how well does it work? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b6
  forPractitioner: { text: "At threshold, graduates work online and at a distance as well as face to face.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will be able to work online and remotely as well as face to face.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.6, item 6 (working online, remotely and in person) as a threshold standard among the personal and professional skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.6, item 6. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 2.6 and 4.6.b5 and the honours descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about working online, remotely and in person. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: What changes in how you work when a team meets only online? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b7
  forPractitioner: { text: "At threshold, graduates demonstrate professional behaviours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will behave professionally.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.6, item 7 (professional behaviour) as a threshold standard among the personal and professional skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.6, item 7. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.6.b13 and 1.7 and the honours descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about professional behaviour. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: What does professional behaviour look like on a field trip or placement? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b8
  forPractitioner: { text: "At threshold, graduates show they value building the graduate skills that suit their possible careers.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will understand which graduate skills matter for the careers you are considering and be building them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.6, item 8 (graduate skills for career pathways) as a threshold standard among the personal and professional skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.6, item 8. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.6.b9 and 1.13 and the honours descriptor qaa/fheq-2024/4.15.b9.3 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about graduate skills for career pathways. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Which skills does the career you are considering need, and which do you already have? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b9
  forPractitioner: { text: "At threshold, graduates recognise the importance of planning their personal, career and professional development, including setting and working towards targets.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will see why planning your personal and career development matters, and you will set targets and work towards them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.6, item 9 (planning personal, career and professional development) as a threshold standard among the personal and professional skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.6, item 9. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.6.b1 and 4.6.b8 and the honours descriptor qaa/fheq-2024/4.15.b9.3 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about planning personal, career and professional development. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: What development target have you set yourself this year? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b10
  forPractitioner: { text: "At threshold, graduates recognise and respect the views of others.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will recognise and respect other people's views.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.6, item 10 (respecting the views of others) as a threshold standard among the personal and professional skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.6, item 10. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.5.b3 and 1.9 and the honours descriptor qaa/fheq-2024/4.15.b8 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about respecting the views of others. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: How do you respond when a teammate holds a view you think is wrong? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b11
  forPractitioner: { text: "At threshold, graduates demonstrate understanding of the importance of risk assessment and related health, safety and well-being legislation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will understand why risk assessment and the law on health, safety and well-being matter.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.6, item 11 (risk assessment and health and safety law) as a threshold standard among the personal and professional skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.6, item 11. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 4.4.b4, 3.1.b18 and 2.2 and the honours descriptor qaa/fheq-2024/4.15.b9.2 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about risk assessment and health and safety law. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Which risk did your last risk assessment catch that you might have missed? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b12
  forPractitioner: { text: "At threshold, graduates see why equality, diversity and inclusivity matter and build behaviours that support EDI.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will understand why equality, diversity and inclusion matter and act in ways that support them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.6, item 12 (EDI and inclusive behaviour) as a threshold standard among the personal and professional skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.6, item 12. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 1.8, 1.9, 3.1.b17 and 3.4.b19 and the honours descriptor qaa/fheq-2024/4.15.b9.1 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about EDI and inclusive behaviour. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: What have you done to make a group you worked in more inclusive? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b13
  forPractitioner: { text: "At threshold, graduates appreciate the need to act and work ethically, sustainably and in compliance with relevant legislation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By graduation, you will understand why you need to act and work ethically, sustainably and within the law.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat 4.6, item 13 (acting ethically, sustainably and lawfully) as a threshold standard among the personal and professional skills: the least every ES3 honours graduate will have shown, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.6, item 13. Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. Set it beside 1.2, 3.17 and 4.4.b4 and the honours descriptor qaa/fheq-2024/4.15.b9.2 (spine:6)."
  author-agent-dialogue: "Raise it when a student or a programme team asks what an honours graduate must be able to show about acting ethically, sustainably and lawfully. For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. Ask: Where has an ethical or sustainability concern changed what you did in your work? Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.7
  forPractitioner: { text: "Integrated master's graduates will have built a significant specialism through an independent research project they develop and lead, and will show they can interrogate the literature alone and design and carry out a project on an important practical question.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "In an integrated master's, you will build a real specialism by planning and leading your own research project, and you will show that you can search the literature independently, apply ideas, methods and data to different questions and design and run a project that tackles a practical problem.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat para 4.7 as a stated outcome in 'will' terms for integrated master's graduates at FHEQ level 7 (FQHEIS level 11), on top of the honours threshold. Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.7. Do not present it as a typical or excellent rung for honours, nor as a standard for taught MSc courses (para 4.8). Set it beside 4.3.b7, para 2.3, qaa/fheq-2024/4.17.b3, qaa/fheq-2024/4.17.b6 and spine:7."
  author-agent-dialogue: "Raise it when an integrated master's student plans the final-year project or a team designs the master's year. For a student, put it plainly: you will lead your own research and work independently; for staff, frame it as the step up from 4.3.b7. Ask: What practical question will your project tackle, and which parts of it did you design yourself? Avoid treating it as an honours requirement."
- statement: qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.8
  forPractitioner: { text: "Taught MSc or MA students will build on the undergraduate competencies above and focus in more depth on one aspect of the subject, gaining knowledge and skills that improve their employability.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a taught master's, you will build on what you learned as an undergraduate and go deeper into one area of the subject, gaining knowledge and skills that strengthen your career prospects.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat para 4.8 as a stated expectation in 'will' terms for taught master's students at FHEQ level 7 (FQHEIS level 11): depth in one aspect, building on the honours threshold. Cite it as QAA, 2022, Earth Sciences, Environmental Sciences and Environmental Studies (ES3) Subject Benchmark Statement, para 4.8. Do not claim it sets detailed master's outcomes; the statement gives none. Set it beside 4.3 to 4.6, para 4.7, qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it when a taught master's student or team asks what the statement says about postgraduate study. Say plainly that you will build on your first-degree skills and go deeper in one area; for staff, frame it as a reason to use the FHEQ master's descriptor for detail. Ask: Which aspect of the subject will you specialise in, and which of your undergraduate skills will it stretch? Avoid inventing master's outcomes the text does not state."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.3; 4.2" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.3" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.3; 4.2" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.3" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.3: honours at FHEQ Level 6, FQHEIS SCQF Level 10; 4.2)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.3: integrated master's at FHEQ Level 7, FQHEIS SCQF Level 11)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["front matter", "1.2", "1.4", "1.8", "1.9", "3.1", "3.4", "3.19", "4.6"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["2.2", "3.16", "3.19"] }
- { id: "theme:esd", role: "carries", carriedIn: ["front matter", "1.4", "1.6", "1.10", "1.11", "1.12", "2.1", "3.1", "3.3", "3.4", "3.6", "3.17", "3.22", "4.6"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["front matter", "1.6", "1.13", "1.14", "1.15", "1.16", "3.16", "3.18", "4.8"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-earth-sciences-environmental-sciences-and-environmental-studies-2019-benchmarks (not yet ingested)", note: "the fourth edition, 2019, named in the back matter; this is the fifth edition" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the honours classification descriptions, cited as QAA 2019 (4.2; section 5)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "levels 6 and 7 (2.3; 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "SCQF levels 10 and 11 (2.3; 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "1.12; 3.1.b1; 3.4.b1; section 5" }
- { rel: "refersTo", target: "std:doc:qaa-enterprise-2018-guidance", note: "1.16; section 5" }
- { rel: "refersTo", target: "QAA Characteristics Statement: Higher Education in Apprenticeships (not yet ingested)", note: "2.7; section 5" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance (not yet ingested)", note: "front matter" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2022-03"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "none-stated"
replacedBy: "none"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- Earth sciences, environmental sciences and environmental studies are treated together as ES3, with enough overlap for one statement (D1, 1.1, 1.3).
- The setting is the climate emergency, biodiversity loss and wider threats to nature; graduates act on sound science with fairness in view (D1, 1.2).
- Environment is read broadly, covering human and non-human life (D1, 1.5).
- The subjects study physical, chemical and biological Earth systems to learn from the past and shape the future, across scales of space and time, through systems thinking (D1, 1.6).
- They are practical and field-based, with observation and analysis to support decisions under uncertainty (D1, 1.6, 3.16).
- They are multidisciplinary and interdisciplinary, overlapping with biology, chemistry, geography, informatics and physics (D1, 1.6, 2.1).
- Sustainability is at their root and at their core (D1, 2.1, 3.17).
- EDI is subject matter as well as practice, with attention to colonial legacies and other ways of knowing (D1, 1.8, 1.9, 2.1).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "EDI as subject knowledge and practice: removing barriers to field and lab participation, decolonising the curriculum, valuing other ways of knowing, and a route to justice through the SDGs (D1, 1.2, 1.8, 1.9, 2.1)"
  statements: ["qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.2", "qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.8", "qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.9", "qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b17", "qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b19", "qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b12"]
- theme: theme:accessibility
  inThisSubject: "inclusive design of curricula and field programmes, accessible technology, reasonable adjustments for practical work and fieldwork, and risk assessments that cover students with protected characteristics (D1, 2.2, 3.16, 3.19)"
  statements: ["qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/2.2", "qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.16"]
- theme: theme:esd
  inThisSubject: "headed Sustainability: the subjects are rooted in it; ESD defined with UNESCO's vision and the SDGs; content, applications, teaching and assessment all grounded in it, with the joint ESD guidance as the reference (D1, 1.10 to 1.12, 2.1, 3.17, 3.22)"
  statements: ["qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.12", "qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.1.b1", "qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b1", "qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.4.b3", "qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/3.17", "qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b13"]
- theme: theme:enterprise
  inThisSubject: "headed Employability, entrepreneurship and enterprise: employability defined, what Earth science and environmental employers look for, employer links, field skills that build graduate attributes, and authentic assessment (D1, 1.13 to 1.16, 3.16, 3.18)"
  statements: ["qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/1.16", "qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.6.b8", "qaa/earth-sciences-environmental-sciences-and-environmental-studies-2022/4.8"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.1", gloss: "Earth sciences: anticipated knowledge from planetary formation and geological time to field data, ethics and risk" }
  - { component: "3.2", gloss: "Earth sciences: 29 typical components, from Earth materials and geochemistry to volcanology and urban geoscience" }
  - { component: "3.3", gloss: "Earth sciences: applications in the SDGs, resources, energy transition, past climates, engineering geology and geohazards" }
  - { component: "3.4", gloss: "environmental sciences and studies: shared anticipated knowledge of systems, scales, impacts, risk, governance and data" }
  - { component: "3.5", gloss: "environmental sciences and studies: 28 typical components, from air quality and biodiversity to waste and water" }
  - { component: "3.6", gloss: "environmental sciences and studies: applications in the SDGs, energy, greening industry, modelling, policy and cities" }
  - { component: "3.7", gloss: "environmental sciences only: scientific study of processes and scales, field data and measurement" }
  - { component: "3.8", gloss: "environmental sciences only: biogeochemical cycles, environmental engineering, principles of environmental science" }
  - { component: "3.9", gloss: "environmental sciences only: contamination, future impacts, carbon footprints, corporate practice, biodiversity loss" }
  - { component: "3.10", gloss: "environmental studies only: history of change, social and political implications, culture and values" }
  - { component: "3.11", gloss: "environmental studies only: conflict, environmental justice, philosophies, indigenous knowledge, values-based ethics" }
  - { component: "3.12", gloss: "environmental studies only: philosophies and ethics in practice; indigenous communities in managing the environment" }
practices:
  - { component: "3.13", kind: "teaching", gloss: "teaching and learning defined, inclusive of all students" }
  - { component: "3.14", kind: "teaching", gloss: "methods left open; outcomes reachable and clearly stated" }
  - { component: "3.15", kind: "teaching", gloss: "inclusive methods; research-led and enquiry-based courses" }
  - { component: "3.16", kind: "learning", gloss: "substantial fieldwork for every student, inclusive, with adjustments" }
  - { component: "3.17", kind: "teaching", gloss: "teaching and learning grounded in ESD" }
  - { component: "3.18", kind: "assessment", gloss: "assessment strategy in course design; authentic assessment for employability" }
  - { component: "3.19", kind: "assessment", gloss: "inclusive assessment tied to outcomes, with adjustments" }
  - { component: "3.20", kind: "assessment", gloss: "formative feedback, reflection, peer and self-assessment" }
  - { component: "3.21", kind: "assessment", gloss: "authentic assessment examples: practical investigations, case studies, case reports, presentations" }
  - { component: "3.22", kind: "assessment", gloss: "multidisciplinary assessment grounded in ESD" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.1", award: "bachelor's with honours", items: 34 }
rungBases: "4.1 defines the threshold as the minimum an honours graduate will have demonstrated; the heading 'Threshold level' (before 4.3) opens four lists, 4.3 intellectual (9), 4.4 practical (7), 4.5 communication (5) and 4.6 personal and professional (13), each with a lead-in and no modal; 4.2 sends performance above the threshold to Annex D; no typical or excellent rung is stated"
outcomeLists:
  - { leadIn: "3.1", gloss: "Earth sciences knowledge all graduates are anticipated to hold", items: 18, award: ["honours"] }
  - { leadIn: "3.4", gloss: "environmental sciences and studies knowledge all graduates are anticipated to hold", items: 20, award: ["honours"] }
  - { leadIn: "3.7", gloss: "environmental sciences only: further knowledge graduates are expected to demonstrate", items: 6, award: ["honours"] }
  - { leadIn: "3.10", gloss: "environmental studies only: further knowledge graduates are expected to demonstrate", items: 3, award: ["honours"] }
outcomes: []
```

### SB4a Student and practitioner versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
written: fresh from the held text; no consumer's statements read (benchmark variant rule 6)
fullRewrites: []
```

### SB5 Bodies
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { body: "Chartered Institution of Water and Environmental Management", says: "a notable PSRB in the ES3 field (D1, 1.7)", requirements: "not yet ingested (Part E)" }
- { body: "Geological Society of London", says: "a notable PSRB in the ES3 field (D1, 1.7)", requirements: "not yet ingested (Part E)" }
- { body: "Institution of Environmental Sciences", says: "a notable PSRB in the ES3 field (D1, 1.7)", requirements: "not yet ingested (Part E)" }
- { body: "Chartered Institute of Ecology and Environmental Management", says: "a notable PSRB in the ES3 field (D1, 1.7)", requirements: "not yet ingested (Part E)" }
- { body: "Institute of Environmental Management and Assessment", says: "a notable PSRB in the ES3 field (D1, 1.7)", requirements: "not yet ingested (Part E)" }
- { body: "PSRBs in general", says: "several cover the ES3 range, some accrediting programmes and CPD and offering membership up to chartered status; the list changes over time; they and external experts can partner with courses through guidance, accreditation and standards (D1, front matter, 1.7, 2.7)", requirements: "not-applicable-by-design" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["front matter", "1.2", "1.4", "1.8", "1.9", "3.1", "3.4", "3.19", "4.6"], statements: ["1.2", "1.8", "1.9", "3.1.b17", "3.4.b19", "4.6.b12"] }
  - { id: "theme:accessibility", named: "Accessibility", carriedIn: ["2.2", "3.16", "3.19"], statements: ["2.2", "3.16"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["front matter", "1.4", "1.6", "1.10", "1.11", "1.12", "2.1", "3.1", "3.3", "3.4", "3.6", "3.17", "3.22", "4.6"], statements: ["1.12", "3.1.b1", "3.4.b1", "3.4.b3", "3.17", "4.6.b13"] }
  - { id: "theme:enterprise", named: "Employability, entrepreneurship and enterprise (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["front matter", "1.6", "1.13", "1.14", "1.15", "1.16", "3.16", "3.18", "4.8"], statements: ["1.16", "4.6.b8", "4.8"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.3", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.3", "4.2"] }
bodies:
  - { body: "Chartered Institution of Water and Environmental Management", citedIn: ["1.7"] }
  - { body: "Geological Society of London", citedIn: ["1.7"] }
  - { body: "Institution of Environmental Sciences", citedIn: ["1.7"] }
  - { body: "Chartered Institute of Ecology and Environmental Management", citedIn: ["1.7"] }
  - { body: "Institute of Environmental Management and Assessment", citedIn: ["1.7"] }
  - { body: "PSRBs (general)", citedIn: ["front matter", "1.7", "2.7"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "descriptions of the four honours classes, for judging performance above the threshold" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA and Advance HE Education for Sustainable Development Guidance", citedIn: ["1.12", "3.1", "3.4"], role: "the reference for ESD in teaching, competencies, outcomes and assessment" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers", citedIn: ["1.16"], role: "the reference for employability, enterprise and entrepreneurship" }
  - { document: "QAA Characteristics Statement: Higher Education in Apprenticeships (not yet ingested: Part E)", named: "QAA's Higher Education in Apprenticeships Characteristics Statement", citedIn: ["2.7"], role: "describes apprenticeship degrees" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested: Part E)", named: "Advice and Guidance to support the Quality Code", citedIn: ["front matter"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested: Part E)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "UN Sustainable Development Goals (external)", named: "UN Sustainable Development Goals", citedIn: ["1.9", "1.11", "3.3", "3.6"], role: "frame of the sustainability theme" }
  - { document: "UNESCO 2019 definition of ESD (external)", named: "the UNESCO 2019 definition", citedIn: ["1.11"], role: "defines ESD" }
  - { document: "OfS regulatory framework; Quality Assessment Framework for Wales; Quality Enhancement Framework (regulatory, external)", named: "Office for Students' regulatory framework; Quality Assessment Framework for Wales; Quality Enhancement Framework", citedIn: ["front matter"], role: "the statement's regulatory status in each nation" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "es3", definition: "the shorthand the statement uses for Earth sciences, environmental sciences and environmental studies taken together (D1, 1.1)", beneficiaryDefinition: "the name for the three subjects as one family", scopeNote: "used throughout", category: "unknown", practices: ["education"] }
- { slug: "employability", definition: "the competencies, shown through knowledge, skills and behaviours, that make people likelier to gain work and succeed in it (D1, 1.13)", beneficiaryDefinition: "what makes you likely to find work and do well in it", scopeNote: "linked to entrepreneurship and enterprise", category: "unknown", practices: ["education"] }
- { slug: "accessibility", definition: "inclusive design of curriculum and teaching so that no one is excluded from taking part (D1, 2.2)", beneficiaryDefinition: "courses designed so that you can take full part", scopeNote: "with reasonable adjustments where needed", category: "unknown", practices: ["education"] }
- { slug: "education-for-sustainable-development", definition: "building curriculum structures and subject content that support and put sustainable development into practice (D1, 1.11)", beneficiaryDefinition: "learning that prepares you to help make development sustainable", scopeNote: "abbreviated ESD; UNESCO 2019 quoted", category: "unknown", practices: ["education"] }
- { slug: "authentic-assessment", definition: "assessment based on tasks likely to arise at work (D1, 3.18)", beneficiaryDefinition: "assessment that looks like the work you may do after graduating", scopeNote: "examples in 3.21", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the minimum an honours graduate in ES3 will have demonstrated (D1, 4.1)", beneficiaryDefinition: "the least you need to show to gain the degree", scopeNote: "the only rung the statement sets", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "es3", form: "ES3", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "employability", form: "employability", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "accessibility", form: "accessibility", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "education-for-sustainable-development", form: "Education for Sustainable Development", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "education-for-sustainable-development", form: "ESD", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "formal" }
- { concept: "authentic-assessment", form: "authentic assessment", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "minimum threshold standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
`not-applicable-by-design`: no relations between the terms are stated.

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement Earth Sciences, Environmental Sciences and Environmental Studies"
  edition: "March 2022 (fifth edition)"
  year: 2022
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/earth-sciences-environmental-sciences-and-environmental-studies-2022/earth-sciences-environmental-sciences-and-environmental-studies-2022.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: c7438a7671a1574ab16aed46e2e989cbb8bfa4763c166a6ef31cc3b162195c5f
  heldFiles: ["wkspc2601-library/txt/qaa-2022-earth-sciences-environmental-sciences-environmental-studies-standard.txt", "wkspc2601-library/txt/qaa-2022-earth-sciences-environmental-sciences-environmental-studies-standard.norm.txt", "wkspc2601-library/records/qaa-2022-earth-sciences-environmental-sciences-environmental-studies-standard.chunks.json", "wkspc2601-library/records/qaa-2022-earth-sciences-environmental-sciences-environmental-studies-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0036", citation: "QAA (2019) Characteristics Statement: Higher Education in Apprenticeships", settles: ["SB6", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0055", citation: "QAA (2019) Subject Benchmark Statement: Earth Sciences, Environmental Sciences and Environmental Studies, fourth edition", settles: ["S7"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- SB4, rungs: the statement sets one rung only, the threshold (4.1, the heading "Threshold level" and the lists 4.3 to 4.6, 34 items); no typical or excellent rung; 4.2 sends performance above it to Annex D. Same shape as Archaeology (run 0085). No gradeOf links.
- SB4, lead-ins: the four threshold lists have lead-ins with no modal ("Graduates with an honours degree in ES3:", "Graduates of an honours degree in ES3:"); force recorded as threshold from 4.1 (forceFrom 4.1).
- S4, skeleton correction: std_prep marked 3.2, 3.5, 3.8 and 3.11 ("Typical components may include") as typical-rung lists (65 items). They are lists of typical course components, not a rung: recorded as S3 areas (SB3), not statements.
- S4, skeleton correction: 4.3.b9 and 4.5.b5 ran on into the next sub-heading ("Practical skills", "Personal and professional skills"); the paragraph statements 1.5, 1.9, 1.12, 2.2, 2.5 and 4.2 ran on into their next sub-heading, and 1.16, 2.3, 3.17 and 4.8 into a page number. All re-cut with find.
- S4, outcome lists in other words: 3.1 and 3.4 say "it is anticipated that all graduates have appropriate knowledge and skills" of the listed items, and 3.7 and 3.10 that a programme "is normally expected to include" them "with graduates expected to demonstrate knowledge and understanding". Taken as outcome lists (47 records) with force describes, as "anticipated" and "expected" are outside the five; for Abbott: should they read as will or should?
- S4, 3.1.b1 and 3.4.b1 carry their own "should" (consistency with the ESD guidance); force recorded as should, addressee both.
- S4, 3.7 and 3.10 point to "the combined content in paragraph 3.2"; the combined environmental content is 3.4 (3.2 is Earth science components). The issuer's slip, kept; read as 3.4.
- S4, 1.8 obliges with "a duty to confront and encourage the dismantling of all barriers" (ES3 communities): an obliging word outside the five, recorded as describes, addressee provider; for Abbott.
- S4, 1.2 "Graduates in ES3 subjects will be required to ensure..." taken as a will statement about graduates (expectation, all awards); "required" here describes their future working duty, not a condition of the award.
- S4, 2.4 "it would normally be expected that a student who had achieved a second-class degree or higher would be capable of" postgraduate study: an obliging phrase outside the five, recorded as describes.
- S4, 1.5 (should, how to read "environment") taken as a statement under the obliging-paragraph rule, though it binds readers, not courses or students; student version not applicable. For Abbott at P3.
- S4, not taken as statements (plain-present provider norms or descriptions, template open point 5): 2.1 ("Courses are focused...", "Courses allow students to reflect..."); 3.16's "Courses therefore offer all students opportunities for significant field-based learning" (the paragraph is a statement by its should); 3.19 ("Assessment is inclusive for all students"); 3.22 ("assessments take multidisciplinary and interdisciplinary approaches").
- S4, not taken as statements (predictive or descriptive will): 1.13 ("will contribute positively to graduate employability"); 1.14 and 1.15 ("employers will be looking for competence..."): employer demand, not an outcome; 2.8 to 2.10 (degree-awarding bodies, providers and external examiners "will" review and examine): descriptions of quality assurance. For Abbott at P3: 1.14 and 1.15 could be read as expected competences.
- S4, not taken as statements: 1.6, nine shared traits ("ES3 is characterised by"), descriptive with no modal; recorded in SB1. 2.6 and 2.7 use "may" for options only.
- S4, 2.3 holds two outcomes, honours progression and the integrated master's year; kept as one record by the issuer's numbering, level fheq:6, award honours and integrated master's.
- S4, 4.7 and 4.8 (integrated master's, taught MSc or MA) sit under the heading "Personal and professional skills" with no heading of their own; recorded rung none, level fheq:7.
- S2, statedScope: the scope also says foundation degrees (FdSc) may find the guidance useful and that research degrees are not addressed.
- Subjects: HECoS has no preferred term "environmental studies"; it is a non-preferred term of 100469 environmental management (CAH26-01-03 human geography): entered as inferred. Geology (100395) inferred: the statement names Earth sciences, not geology, as the subject. CAH26-01-03 inferred with it.
- SB5: five bodies named in 1.7 as notable PSRBs; the statement says nothing more of each; their own requirements are not yet ingested. The Disabled Students' Commission, the Environment Agency, the British Geological Survey and others appear only in the back matter (excluded).
- SB6, sharedDocuments: section 5 also lists HEA (2016) Framework for embedding employability in higher education, cited nowhere in the body; not tagged. The Apprenticeships Characteristics Statement and the Quality Code Advice and Guidance are not yet ingested (D3).
- SB6, themes: the front matter names three cross-cutting themes (EDI; ESD; employability, entrepreneurship and enterprise education); accessibility has its own heading (2.2) as a fourth. Tags follow what each paragraph says; 1.14 and 1.15 tagged enterprise for employer expectations.
- S5: no CQFW level cited; FQHEIS levels cited as "FQHEIS SCQF Level 10" and "11" (2.3) and "FQHEIS Level 10" (4.2).
- S7, supersedes: the back matter names the fourth edition (2019) and the third (2014); the 2019 document is not yet ingested (D3).
- S9: not researched in P1.
- Patterns that differ from Psychology: threshold only, no typical or excellent rung; threshold lead-ins with no modal; subject content lists phrased as "anticipated" and "normally expected" knowledge; three subjects in one statement with shared and subject-only lists; integrated master's and taught master's covered in one paragraph each; no glossary; 4.2 cites Annex D as QAA 2019.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:09: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0101 (P1); built by tools/bm_build.py.
