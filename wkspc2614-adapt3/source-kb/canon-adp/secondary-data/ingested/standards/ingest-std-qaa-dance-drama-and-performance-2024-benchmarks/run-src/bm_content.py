# Judgement for run 0099, QAA Subject Benchmark Statement: Dance, Drama and Performance (April 2024). std run agent.
# Built by tools/bm_build.py dance-drama-and-performance-2024 --check. Brief BM-BRIEF.md 0.2.2; benchmark template 0.6.0-draft; run layer 0.7.0-draft.
HON = "bachelor's with honours"
MA = "master's"
CITE = 'QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para '

META = dict(
    run='0099', p1='2026-10-03 16:54',
    title='Subject Benchmark Statement Dance, Drama and Performance',
    heading='Subject Benchmark Statement: Dance, Drama and Performance (QAA, April 2024)',
    edition='April 2024 (fifth edition)', published='2024-04',
    status='current',
    supersedes='the fourth edition (2019), named in the membership section (section 6)',
    subjects=[
        dict(scheme='hecos', code='100068', label='dance', basis='stated'),
        dict(scheme='hecos', code='100069', label='drama', basis='stated'),
        dict(scheme='hecos', code='100071', label='performing arts', basis='stated'),
        dict(scheme='cah', code='CAH25-02-04', label='dance', basis='stated'),
        dict(scheme='cah', code='CAH25-02-03', label='drama', basis='stated'),
        dict(scheme='cah', code='CAH25-02-01', label='performing arts (non-specific)', basis='stated'),
        dict(scheme='cah', code='CAH25-02', label='performing arts', basis='stated'),
        dict(scheme='hecos', code='100067', label='acting', basis='stated'),
        dict(scheme='hecos', code='100035', label='musical theatre', basis='stated'),
        dict(scheme='hecos', code='100698', label='theatre studies', basis='stated'),
        dict(scheme='hecos', code='100708', label='stage design', basis='inferred'),
        dict(scheme='hecos', code='100710', label='community theatre', basis='inferred'),
        dict(scheme='hecos', code='100700', label='theatre production', basis='inferred'),
    ],
    awards=[HON, MA], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, the 2022 onward revision with cross-cutting themes (fifth edition of this statement)',
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    agentDefinition=("QAA's UK reference point for what a graduate in dance, drama, theatre and performance should know and be able "
                     "to do, with honours standards at three rungs (threshold, typical, excellent), each split into subject knowledge "
                     "and understanding, subject-specific skills and generic skills, and a short list for master's study. Reach for it "
                     "when designing, approving, reviewing or describing a performance course, its outcomes or its marking. It is not "
                     "a curriculum and not a regulatory requirement in England; its outcomes are indicative, written for single honours."),
    summary=("Published by QAA in April 2024 as the fifth edition, the statement covers undergraduate and taught postgraduate "
             "courses in dance, drama and performance and associated areas such as acting, musical theatre and scenography. It "
             "sets out the field's context and purposes, its distinctive features (design, progression, flexibility, partnerships, "
             "monitoring and review), its content, teaching, learning and assessment, and benchmark standards for the honours "
             "degree at threshold (30 items), typical (24) and excellent (24) rungs, each in three lists, plus five master's "
             "outcomes at FHEQ level 7. It carries four cross-cutting themes (equality, diversity and inclusion; accessibility; "
             "sustainability; enterprise and entrepreneurship education), a paragraph on generative AI, points to Annex D for the "
             "degree classes and names professional, statutory and regulatory bodies only in general."),
    authority=("reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a "
               "sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of the "
               "quality arrangements in Northern Ireland (D1, front matter: Relationship to legislation)"))

S2 = dict(
    governs='what a graduate in dance, drama and performance is expected to know, do and understand at honours, at threshold, typical and excellent, and the added outcomes for master\'s study',
    awards=[HON, "master's (taught postgraduate and integrated master's)"],
    levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    statedScope='"Within the scope of this Subject Benchmark Statement are undergraduate and taught postgraduate degree programmes delivered by a broad range of providers, each with their own ethos and pedagogic emphases, as well as varying approaches to student journeys." (D1, 1.2)',
    statedSubjects=[
        dict(name='Dance, Drama and Performance', locator='(D1, title; 1.1; 1.5)', kind='subject',
             codes=[dict(scheme='hecos', code='100068', label='dance'), dict(scheme='hecos', code='100069', label='drama'),
                    dict(scheme='hecos', code='100071', label='performing arts'), dict(scheme='cah', code='CAH25-02', label='performing arts')]),
        dict(name='acting', locator='(D1, 2.2; 2.3.b1)', kind='specialism', codes=[dict(scheme='hecos', code='100067', label='acting')]),
        dict(name='musical theatre', locator='(D1, 2.2; 2.3.b1)', kind='specialism', codes=[dict(scheme='hecos', code='100035', label='musical theatre')]),
        dict(name='theatre', locator='(D1, 2.2.b2; 2.3.b1)', kind='specialism', codes=[dict(scheme='hecos', code='100698', label='theatre studies')]),
        dict(name='scenography and theatre design', locator='(D1, 2.2; 2.3.b1)', kind='specialism', codes=[dict(scheme='hecos', code='100708', label='stage design')]),
        dict(name='applied and social theatre', locator='(D1, 2.2)', kind='specialism', codes=[dict(scheme='hecos', code='100710', label='community theatre')]),
        dict(name='dance theatre; writing for performance', locator='(D1, 2.2)', kind='specialism', codes=[]),
        dict(name='contemporary arts (interdisciplinary courses with no subject named in the award)', locator='(D1, 2.2.b5)', kind='programme title', codes=[]),
    ])

SECTIONS = {
    '1': 'Context and purposes of a Dance, Drama and Performance degree',
    '2': 'Distinctive features of the Dance, Drama and Performance degree',
    '3': 'Content, structure and delivery',
    '4': 'Benchmark standards',
}
SUB = [
    ('1.1', '1.6', 'Context'), ('1.7', '1.10', 'Purposes'), ('1.11', '1.16', 'Characteristics'),
    ('1.17', '1.20', 'Equality, diversity and inclusion'), ('1.21', '1.30', 'Accessibility'), ('1.31', '1.34', 'Sustainability'),
    ('1.35', '1.38', 'Enterprise and entrepreneurship education'),
    ('2.1', '2.7', 'Design'), ('2.8', '2.12', 'Progression'), ('2.13', '2.13', 'Flexibility'), ('2.14', '2.21', 'Partnerships'),
    ('2.22', '2.26', 'Monitoring and review'),
    ('3.1', '3.6', 'Content'), ('3.7', '3.12', 'Teaching and learning'), ('3.13', '3.17', 'Assessment'),
    ('4.1', '4.7', 'Introduction'), ('4.8', '4.10', 'Threshold level'), ('4.11', '4.13', 'Typical level'),
    ('4.14', '4.16', 'Excellent level'), ('4.17', '4.17', "Master's level degrees in Dance, Drama and Performance"),
]

G = {
    '1.1': 'a broad field joining practice and theory, old and new methods',
    '1.2': 'scope: undergraduate and taught postgraduate courses',
    '1.3': 'diverse provision; the four cross-cutting themes named',
    '1.4': 'practice and concept in performance, contested and alive',
    '1.5': 'single, combined and interdisciplinary courses; vocational and hybrid growth',
    '1.6': 'industry-facing, critical, research-led and socially engaged courses',
    '1.7': 'creativity and its communication at the centre',
    '1.8': 'theory and practice across creative, vocational and professional dimensions',
    '1.9': 'embodied learning and knowing',
    '1.10': 'creative industries, cultural change and alternative worlds',
    '1.11': 'six broad strands of study, from practice to employment',
    '1.12': 'learning through collaboration and ensemble',
    '1.13': 'inclusive learning communities; safety balanced with creative risk',
    '1.14': 'many perspectives, cultures and histories; authorship questions',
    '1.15': 'generative AI analysed and used openly as a creative tool',
    '1.16': 'the four themes run through the whole statement',
    '1.17': 'EDI commitment; no structural disadvantage; Equality Act 2010',
    '1.18': 'guiding principles for studios and classrooms',
    '1.19': 'performance as diverse; centring marginalised voices',
    '1.20': 'what inclusive learning opportunities do',
    '1.21': 'inclusive design across every learning setting',
    '1.22': 'questioning ableist knowledge; anticipating access needs',
    '1.23': 'live learning first, blended learning valued',
    '1.24': 'teaching methods that answer to student needs and access',
    '1.25': 'programmes that remove barriers to learning',
    '1.26': 'flexible outcomes and scaffolded curricula',
    '1.27': 'dignity, respect and seeing oneself in the curriculum',
    '1.28': 'fieldwork with attention to individual needs',
    '1.29': 'barriers in group and practical work planned for',
    '1.30': 'belonging, support and students as partners',
    '1.31': 'ESD defined; SDGs, the 2021 guidance and the Theatre Green Book',
    '1.32': 'the art forms well placed for a sustainable future',
    '1.33': 'economic, social and environmental themes for curricula',
    '1.34': 'technology and fair digital access',
    '1.35': 'enterprise education for employability and value to society',
    '1.36': 'social, political and cultural value of the field',
    '1.37': 'critical thinking communicated in many forms',
    '1.38': 'training for roles and portfolio careers',
    '2.1': 'integrative, progressive, co-created course design',
    '2.2': 'associated areas and kinds of course at FHEQ 6 and 7',
    '2.3': 'what degrees in the field study',
    '2.4': 'knowledge made through performance-making',
    '2.5': 'definition must not block innovation or tradition',
    '2.6': 'courses engage with national and international performing arts',
    '2.7': 'critical discourse, synthesis and practical skill',
    '2.8': 'progression by level towards the threshold',
    '2.9': 'readiness for postgraduate study',
    '2.10': 'joint and combined students reach the core skills',
    '2.11': 'integrated master\'s at FHEQ 7 and FQHEIS 11',
    '2.12': 'exit awards and course lengths across the nations',
    '2.13': 'flexible modes, credit and micro-credentials',
    '2.14': 'partnerships for progression and employability',
    '2.15': 'kinds of partnership activity',
    '2.16': 'formal and informal partnerships',
    '2.17': 'equal access to partnership activity; work-based learning guidance',
    '2.18': 'partners support professional development',
    '2.19': 'partners share the community\'s equity principles',
    '2.20': 'transferable skills developed with partners',
    '2.21': 'partners comment on curriculum and skills',
    '2.22': 'routine monitoring and periodic review with the student voice',
    '2.23': 'external reviewers in periodic review',
    '2.24': 'external examiners and their yearly reports',
    '2.25': 'professional accreditation for vocational courses',
    '2.26': 'regular curriculum review',
    '3.1': 'no prescriptive model; courses pick and emphasise areas',
    '3.2': 'areas of knowledge and understanding',
    '3.3': 'thirteen skills students develop',
    '3.4': 'same outcomes for all Performance module students',
    '3.5': 'progression and depth for specialists and others; capstone',
    '3.6': 'diversity, inclusion, access and reasonable adjustments',
    '3.7': 'varied approaches joining practice and theory',
    '3.8': 'experiential and embodied learning as the basis',
    '3.9': 'teaching drawn from the disciplines\' own practice',
    '3.10': 'learning in practical and professional contexts, many roles',
    '3.11': 'tutor-led to independent learning; group work',
    '3.12': 'settings and modes of learning',
    '3.13': 'inclusive, negotiated assessment as part of learning',
    '3.14': 'formats of formative and summative assessment',
    '3.15': 'self and peer assessment; course information',
    '3.16': 'more course information to include',
    '3.17': 'handbooks on academic issues and support',
    '4.1': '\'Performance\' used for the whole field',
    '4.2': 'three rungs shown at the award of honours',
    '4.3': 'most exceed the threshold; Annex D for classes',
    '4.4': 'standards as learning outcomes',
    '4.5': 'the typical goal: creative and critical artists and thinkers',
    '4.6': 'what the threshold and excellent rungs mean',
    '4.7': 'indicative outcomes for single honours; themes in all courses',
    '4.8': 'threshold: subject knowledge and understanding',
    '4.9': 'threshold: subject-specific skills',
    '4.10': 'threshold: generic and graduate skills',
    '4.11': 'typical: subject knowledge, understanding and skills',
    '4.12': 'typical: subject-specific skills',
    '4.13': 'typical: generic and graduate skills',
    '4.14': 'excellent: subject knowledge, understanding and skills',
    '4.15': 'excellent: subject-specific skills',
    '4.16': 'excellent: generic and graduate skills',
    '4.17': 'master\'s: five added outcomes',
}
CTYPE = {
    '1.11': 'area', '2.3': 'area', '3.2': 'area',
    '3.7': 'practice', '3.8': 'practice', '3.10': 'practice', '3.11': 'practice', '3.12': 'practice',
    '3.13': 'practice', '3.14': 'practice', '3.15': 'practice', '3.17': 'practice',
}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='section headings (1 to 4)', kind='other: heading lines'),
    dict(number='5', heading='List of references and further resources', kind='other: references, read for S7 and SB6'),
    dict(number='6', heading='Membership of the Advisory Group', kind='other: membership, read for S7 (earlier editions 2019, 2015, 2007, 2002)'),
]

P = {}
def s(i, **k):
    P[i] = k

# ------------------------------------------------------------- obliging and outcome paragraphs, sections 1 to 4
s('1.17', find='No student should be structurally disadvantaged due to their individual characteristics.',
  type='expectation', rung='none', force='should', level='none', appliesTo='students of the subject', addressee='both',
  verbs=['disadvantaged'], about='no structural disadvantage from personal characteristics', domain='none', award=[HON, MA],
  para="No student in the subject should be put at a built-in disadvantage because of their personal characteristics.",
  prac="Check course structures, assessment and timetabling so that no student is disadvantaged by design because of who they are; the statement says this should not happen.",
  ben="Your course should not be set up in a way that puts you at a disadvantage because of who you are.",
  aaw="Describe this as an expectation (should) on courses in the subject at every level of study, set within its equality, diversity and inclusion section. Cite it as (" + CITE + "1.17) and read it with paras 1.18 to 1.20 and the Equality Act 2010 the paragraph names. Do not claim it creates a legal duty of its own; the legal duties come from the Act.",
  aad="Raise it when a student reports a barrier built into how the course runs, or when a team reviews a module for inclusion. With a student, ask where the course's set-up has made things harder for them than for others; with staff, ask which structures could disadvantage a group by design. Avoid promising a fix the course team has not agreed.")

s('1.24', type='expectation', rung='none', force='will', level='none', appliesTo='teaching in the subject', addressee='provider',
  verbs=['reflect'], about='teaching methods that answer to student needs, access and equity', domain='none', award=[HON, MA],
  para="Teaching methods in the subject will generally answer to the needs of the student body and the professional practices of the disciplines, through an inclusive curriculum that puts access and equity first; suitable resources are key.",
  prac="Shape teaching methods around your student body and the professional practice of the discipline: the curriculum will put access and equity first, backed by suitable learning resources.",
  ben=('n/a', 'a duty on those who design and teach courses; it sets no outcome for the student'),
  aaw="Present this as a stated expectation (will, generally) on teaching in the subject, in its accessibility section, not as an outcome for students. Cite it as (" + CITE + "1.24) and set it beside paras 1.21 to 1.30 and the inclusion commitment in para 3.6. Do not claim it fixes a teaching method; it asks that methods answer to students' needs and to professional practice.",
  aad="Raise it with a programme team planning teaching methods or resources. Ask which students' access needs the current methods serve poorly, and what resources are missing. Keep the duty with staff; do not hand it to a student as something to meet.")

s('2.6', type='expectation', rung='none', force='will', level='none', appliesTo='courses in the subject', addressee='provider',
  verbs=['engage', 'reflect', 'informed'], about='engaging with national and international performing arts', domain='none', award=[HON, MA],
  para="Courses will draw on, mirror and learn from performing arts contexts, industries, people and practices at home and abroad.",
  prac="Build national and international performing arts work into the course: its contexts, industries, practitioners and developments will shape what is taught.",
  ben="Your course will connect you with how the performing arts work in the UK and around the world: their industries, people and practices.",
  aaw="Describe this as a stated expectation (will) on courses in the subject: that they engage with national and international performing arts. Cite it as (" + CITE + "2.6) and set it beside the partnership paragraphs 2.14 to 2.20 and para 1.10. Do not claim it requires international travel or placements; it names contexts to engage with, not activities.",
  aad="Raise it when a team reviews whether the curriculum looks beyond one national tradition, or a student asks how the course links to the profession. Ask staff which international practices or industries the course draws on now; ask a student which work from outside the UK has shaped their own. Avoid treating it as a student requirement.")

s('2.8', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students progressing through the degree', addressee='both',
  verbs=['progress', 'accompanied', 'include'], about='each level builds towards the threshold', domain='none', award=HON,
  para="Students will move up through the levels under each institution's regulations; each level is expected to bring knowledge, expertise and experience that build towards the threshold subject and generic skills, usually with credit for all learning and assessment.",
  prac="Plan each level so that it adds knowledge, expertise and experience leading towards the threshold skills in paras 4.8 to 4.10; progression will follow your institution's regulations and usually means credit for the full range of study.",
  ben="You will move from one year of study to the next under your university's rules, and each year is expected to build what you know and can do towards the minimum standard for your degree.",
  aaw="State it as an expectation (will; it is expected) on progression towards the honours award at FHEQ level 6: each level builds towards the threshold. Cite it as (" + CITE + "2.8) and set it beside the threshold rung in paras 4.8 to 4.10 and the lower-level descriptors from qaa/fheq-2024/4.10.b1 and qaa/fheq-2024/4.12.b1 (FHEQ 4 and 5). Do not claim the statement sets progression rules; each institution's regulations do.",
  aad="Raise it when a student asks how a first or second year relates to the final standard, or when staff map outcomes across levels. Ask a student what this year has added towards the final-year standard; ask staff where each level's outcomes point to the threshold items. Avoid suggesting the statement decides who progresses.")

s('2.9', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='graduates with a second-class degree or higher', addressee='learner',
  verbs=['undertaking'], about='readiness for postgraduate study', domain='none', award=HON,
  para="On completing an undergraduate degree with at least a second-class result, a student is expected to be able and ready to take on postgraduate study in the subject or a related one; entry rules stay with each institution.",
  prac="Prepare students so that those graduating with a second-class degree or better will be ready for postgraduate study in the field or a related one, while noting that entry criteria belong to each institution.",
  ben="If you graduate with a second-class degree or above, you will be ready to take on postgraduate study in this or a related field, though each institution sets its own entry rules.",
  aaw="Present this as a stated expectation (will; it is expected) about honours graduates with a second-class degree or higher at FHEQ level 6: readiness for postgraduate study. Cite it as (" + CITE + "2.9) and set it beside the master's outcomes in para 4.17 and qaa/fheq-2024/4.15.b9.3. Do not claim it guarantees entry to a master's course; the paragraph leaves entry to each institution.",
  aad="Bring it up when a student asks whether they could go on to a master's. Ask what result they are on course for and which postgraduate area interests them. Avoid promising admission; point them to each institution's entry requirements.")

s('2.10', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='joint and combined honours students', addressee='learner',
  verbs=['achieve', 'add', 'explore'], about='core skills for joint and combined students', domain='none', award=HON,
  para="Undergraduates taking the subject within a joint or combined degree will gain the core of its subject and generic skills and add further skills from their other subject, with scope to work across the disciplines.",
  prac="For joint or combined students, make sure the core subject-specific and generic skills are covered; they will add others from their second subject and may work across both.",
  ben="If you take this subject as part of a joint or combined degree, you will gain its core skills and add others from your other subject, with room to explore where the two meet.",
  aaw="Describe this as a stated expectation (will) for joint and combined honours students at FHEQ level 6: the core of the subject's skills, not all of them. Cite it as (" + CITE + "2.10) and set it beside the skills rungs in paras 4.9 and 4.10 and para 3.5 on students for whom Performance is not the main subject. Do not claim joint students meet every single-honours outcome; para 4.7 says the standards are written for single honours.",
  aad="Raise it when a joint honours student worries they cannot cover everything a single honours student does, or when a team plans a combined route. Ask which core skills the route secures and what the other subject adds. Avoid presenting the single honours list as a checklist for joint students.")

s('2.23', type='expectation', rung='none', force='will', level='none', appliesTo='institutions in periodic review', addressee='provider',
  verbs=['use', 'gain', 'ensure', 'achieved'], about='external reviewers in periodic review', domain='none', award=[HON, MA],
  para="Externality is essential to UK quality assurance: institutions will bring in external reviewers in periodic review for an outside view of proposed changes and to make sure threshold standards are met and content suits the subject.",
  prac="In periodic review, use external reviewers: they will give an outside view of planned changes and confirm that threshold standards are met and content fits the subject.",
  ben=('n/a', 'a duty on the institution in periodic review; it sets no outcome for the student'),
  aaw="Describe this as a stated expectation (will) on institutions in periodic review, not an outcome for students. Cite it as (" + CITE + "2.23) and set it beside paras 2.22 and 2.24 on monitoring and external examining. Do not claim the statement prescribes how review is run; it asks only that external reviewers take part.",
  aad="Raise it with a programme team preparing for periodic review. Ask who will act as external reviewer and what they will be asked to judge against the threshold standards. Keep it for staff.")

s('2.24', find='External examiners are required to produce a report each year and make recommendations for changes to modules and assessments (where appropriate).',
  type='requirement', rung='none', force='must', level='none', appliesTo='external examiners', addressee='provider',
  verbs=['produce', 'make'], about='the external examiner\'s yearly report', domain='none', award=[HON, MA],
  para="Each year, external examiners must write a report and, where fitting, recommend changes to modules and assessment.",
  prac="Expect a yearly report from each external examiner, with recommendations on modules and assessment where they see the need, and plan how the course will respond.",
  ben=('n/a', 'a requirement on external examiners and the institution; it sets no outcome for the student'),
  aaw="Present this as a requirement (required; recorded as must) on external examiners within UK external examining, not a standard students meet. Cite it as (" + CITE + "2.24) and set it beside para 2.23 on external review and para 4.3 on threshold standards. Do not claim the statement itself creates the requirement; it describes the sector's external examiner system.",
  aad="Raise it with a programme team reading or answering an external examiner's report. Ask which recommendations from the last report have been acted on and which were set aside, and why. Do not raise it with students as something they must do.")

s('3.1', find='Typically, courses will incorporate several areas listed in paragraphs 3.2 and 3.3, focusing on some as distinguishing features.',
  type='expectation', rung='none', force='will', level='none', appliesTo='courses in the subject', addressee='provider',
  verbs=['incorporate', 'focusing'], about='courses select and emphasise areas', domain='none', award=HON,
  para="Courses usually take up several of the areas and skills set out in 3.2 and 3.3, making some of them the course's distinctive emphasis.",
  prac="Choose several of the content areas and skills from 3.2 and 3.3 and make some of them the course's defining features; courses will typically differ in balance.",
  ben=('n/a', 'about how course teams select content; it sets no outcome for the student'),
  aaw="Describe this as a typical expectation (will, typically) on honours course content, not a required list. Cite it as (" + CITE + "3.1) and set it beside the areas in para 3.2 and the skills in paras 3.3.b1 to 3.3.b13. Do not claim a course must cover every area; the same paragraph rules out a prescriptive model.",
  aad="Raise it when a team asks how much of the subject's range a course must cover. Ask which areas the course makes its distinguishing features and why. Keep it with staff.")

s('3.4', find='Whatever the focus of the course, the same learning outcomes are expected of those students undertaking Performance modules or pathways.',
  type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='students taking Performance modules in any course', addressee='both',
  verbs=['expected', 'undertaking'], about='the same outcomes for all students on Performance modules', domain='none', award=HON,
  para="Whatever course they belong to, students on Performance modules or pathways are held to the same learning outcomes.",
  prac="Hold students on Performance modules to the same outcomes whatever their course: single, joint, combined, major-minor or general.",
  ben="Whatever course you are on, if you take Performance modules you are held to the same learning outcomes as everyone else on them.",
  aaw="Describe this as a stated expectation (are expected; recorded as describes, an obliging word outside the five) that students on Performance modules meet the same outcomes whatever their course, at honours level. Cite it as (" + CITE + "3.4) and read it with para 3.5, which allows less depth where specialist modules are closed to non-specialists. Do not claim non-specialist students must reach single honours depth across the whole subject.",
  aad="Raise it when a student from another subject asks whether a Performance module will be marked differently for them, or when staff set outcomes for an elective. Ask the student which module outcomes they find hardest coming from their own subject. Avoid suggesting easier outcomes for visiting students; the outcomes are the same.")

s('3.5', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='all students of Performance', addressee='learner',
  verbs=['develop', 'facilitate', 'culminate'], about='subject growth and progression for all Performance students; capstone', domain='none', award=HON,
  para="Everyone studying Performance will build subject knowledge or skills with matching experience, and that study will support progress in expertise, personal and social growth and intellectual maturity; courses often end in a capstone project, and non-specialists may not reach the same depth.",
  prac="Plan for every Performance student, specialist or not, to build subject knowledge or skill and grow personally and intellectually; a final-year capstone is common, and depth may differ for students whose main subject lies elsewhere.",
  ben="However you study Performance, you will build knowledge or skills in it and grow personally, socially and intellectually, often finishing with a major final-year project.",
  aaw="Present this as a stated expectation (will) for all students studying Performance at honours level, with the depth expected of non-specialists left lower. Cite it as (" + CITE + "3.5) and set it beside paras 3.4 and 2.10 and the honours descriptor qaa/fheq-2024/4.15.b6 on projects. Do not claim a capstone project is required; the paragraph says courses often have one.",
  aad="Raise it when a student asks how their learning should grow over the course, or whether a final project is expected. Ask what has changed in how they think and work since their first year. Avoid presenting the capstone as compulsory.")

s('3.6', type='expectation', rung='none', force='will', level='none', appliesTo='teaching, learning and assessment in the subject', addressee='both',
  verbs=['underpinned', 'allow', 'made'], about='inclusion, access and reasonable adjustments built in', domain='none', award=[HON, MA],
  para="A commitment to diversity, inclusion and accessibility will underpin teaching, learning and assessment, and design, delivery and assessment will have flexibility built in so that reasonable adjustments can be made for individual needs.",
  prac="Build diversity, inclusion and access into teaching, learning and assessment, and design in the flexibility needed to make reasonable adjustments for individual learning needs.",
  ben="Your teaching and assessment will be built on a commitment to diversity, inclusion and access, with room to make reasonable adjustments for your learning needs.",
  aaw="Describe this as a stated expectation (will) on teaching, learning and assessment in courses in the subject. Cite it as (" + CITE + "3.6) and set it beside the equality and accessibility sections in paras 1.17 to 1.30 and the inclusive assessment in para 3.13. Do not claim the statement sets out the legal duty to make reasonable adjustments; it asks for flexibility to make them.",
  aad="Raise it when a student asks whether an assessment can be adjusted for them, or when a team designs a new module. Ask a student what adjustment would let them show what they can do; ask staff where the module's design already allows adjustment. Avoid promising a particular adjustment, which the institution decides.")

s('3.9', type='expectation', rung='none', force='will', level='none', appliesTo='teaching and learning in the subject', addressee='provider',
  verbs=['informed'], about='teaching drawn from the disciplines\' practice', domain='none', award=[HON, MA],
  para="Teaching and learning will rest on methods that suit and belong to the different disciplines within Performance.",
  prac="Choose teaching and learning activities from the working methods of the disciplines you teach: dance, drama, theatre and related practice.",
  ben=('n/a', 'a duty on those who design teaching; it sets no outcome for the student'),
  aaw="Describe this as a stated expectation (will) on how teaching and learning are designed in courses in the subject. Cite it as (" + CITE + "3.9) and set it beside paras 3.7, 3.8 and 3.12. Do not claim it names required methods; it ties methods to the disciplines' own practice.",
  aad="Raise it when a team plans teaching for a new module. Ask staff which disciplinary practices their sessions borrow from and which they leave out. Keep the duty with staff.")

s('3.10', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students of the subject', addressee='learner',
  verbs=['experience', 'undertake', 'participate'], about='learning in practical and professional contexts, in varied roles', domain='none', award=HON,
  para="Students will usually learn in or alongside practical and professional Performance settings, taking on roles suited to their subject and joining processes from first research through creative work, rehearsal and production to performance.",
  prac="Give students learning in or near practical and professional settings, where they will take varied roles across the whole process from research to performance.",
  ben="You will usually learn in practical and professional settings, take on different roles and work through the whole process from early research to rehearsal, production and performance.",
  aaw="Present this as a stated expectation (will, usually) about students' learning on honours courses in the subject. Cite it as (" + CITE + "3.10) and set it beside the subject skill rung items 4.9.b1 and 4.9.b2 and the honours descriptor qaa/fheq-2024/4.15.b6. Do not claim every student takes every role; the roles fit the student's subject area.",
  aad="Raise it when a student asks what kinds of role they will take on, or staff plan production work. Ask a student which roles they have tried and which they want next. Avoid implying all roles are required of everyone.")

s('3.11', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students of the subject', addressee='learner',
  verbs=['experience', 'progress'], about='tutor-led to independent learning; group work', domain='none', award=HON,
  para="Students will typically meet both tutor-led and self-directed learning, becoming more independent and autonomous as they move through the levels, which builds a positive attitude to lifelong learning; group work is a common feature.",
  prac="Mix tutor-led and self-directed learning and shift the balance towards independence as students move up the levels; group work is a typical part of the course.",
  ben="You will usually learn both with tutors and on your own, becoming more independent as you go, and you will often work in groups.",
  aaw="Describe this as a typical expectation (will, typically) on learning methods across the levels of an honours course in the subject. Cite it as (" + CITE + "3.11) and set it beside qaa/fheq-2024/4.15.b5 on managing one's own learning and spine:6 (strand:autonomy). Do not claim a fixed balance of tutor-led and independent study.",
  aad="Raise it when a student finds the move to independent work hard, or staff plan how support tapers off. Ask a student which parts of their work they now lead themselves. Avoid treating less contact time as less support.")

s('3.12', find='Learning and teaching will normally take place in a variety of continually evolving contexts, both in person and online, including an appropriate balance of workshops, rehearsals, productions, practical classes, laboratory/studio-based practice, screenings, lectures, seminars and tutorials.',
  type='expectation', rung='none', force='will', level='none', appliesTo='teaching and learning in the subject', addressee='provider',
  verbs=['take'], about='a balance of settings, in person and online', domain='none', award=[HON, MA],
  para="Learning and teaching will normally happen in varied and changing settings, face to face and online, balancing workshops, rehearsals, productions, practical and studio classes, screenings, lectures, seminars and tutorials.",
  prac="Offer a suitable mix of settings, in person and online: workshops, rehearsals, productions, studio and practical classes, screenings, lectures, seminars and tutorials.",
  ben=('n/a', 'a duty on those who plan teaching; it sets no outcome for the student'),
  aaw="Present this as a normal expectation (will, normally) on the settings of teaching on courses in the subject. Cite it as (" + CITE + "3.12) and read it with the modes of learning listed after it in the same paragraph, which are typical rather than required. Do not claim every listed setting must appear in every course.",
  aad="Raise it when staff balance in-person and online sessions or plan a timetable. Ask whether the current mix suits the practical work the module asks for. Keep it with staff.")

s('3.15', find='Opportunities should be provided for self and peer assessment to support learning.',
  type='expectation', rung='none', force='should', level='none', appliesTo='assessment in the subject', addressee='both',
  verbs=['provided', 'support'], about='self and peer assessment for learning', domain='none', award=[HON, MA],
  para="Courses should give students chances to assess their own and each other's work, as support for learning.",
  prac="Build in self- and peer-assessment tasks that support learning, with clear guidance on how they work.",
  ben="You should get chances to assess your own work and your classmates' work, to help you learn.",
  aaw="Describe this as an expectation (should) on assessment design in courses in the subject. Cite it as (" + CITE + "3.15) and set it beside paras 3.13 and 3.14 on inclusive and varied assessment and Annex D's reflection row qaa/fheq-2024/annex-d/transferable/r5/3rd. Do not claim self or peer assessment must count towards marks; the paragraph ties it to learning.",
  aad="Raise it when a student asks why they are asked to judge a peer's work, or a team designs formative tasks. Ask a student what they learned about their own work from judging someone else's. Avoid presenting peer marks as final grades.")

s('3.16', find='Details regarding the provision of feedback, tutorial support (academic and pastoral), online resources and access, and bibliographies and screenings should also be included.',
  type='expectation', rung='none', force='should', level='none', appliesTo='course information', addressee='provider',
  verbs=['included'], about='feedback, support and resources in course information', domain='none', award=[HON, MA],
  para="Course information should also set out feedback arrangements, academic and pastoral tutorial support, online resources and access, and reading and viewing lists.",
  prac="Add to the course information how feedback works, what academic and pastoral tutoring is offered, what online resources exist and how to reach them, and reading and screening lists.",
  ben=('n/a', 'a duty on the course team in writing course information'),
  aaw="Present this as an expectation (should) on the course information given to students in the subject. Cite it as (" + CITE + "3.16) and read it with the list of course information in para 3.15. Do not claim it fixes a format or a document; the information may be online or in print.",
  aad="Raise it with a team writing or revising a handbook. Ask where a student would find feedback timings, tutorial support and reading lists today. Keep it with staff.")

s('4.2', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='honours graduates in Performance', addressee='learner',
  verbs=['sets', 'demonstrated', 'show'], about='three rungs shown at the award of honours', domain='none', award=HON,
  para="The standards set out the minimum, typical and excellent achievement a student will have shown on being awarded an honours degree in Performance; showing them over time indicates the expected range of knowledge, understanding and skills.",
  prac="Read the three rungs as what students will have shown at award: minimum, typical and excellent; design assessment so that students show them over time, not in a single task.",
  ben="When you are awarded your honours degree, you will have shown at least the minimum standard, and showing these standards over time shows the range of what you know and can do.",
  aaw="Describe this as the statement's own frame for its rungs: threshold, typical and excellent standards that students will have shown at the award of an honours degree, FHEQ level 6 (FQHEIS level 10). Cite it as (" + CITE + "4.2) and set it beside the rung lead-ins 4.8, 4.11 and 4.14 and qaa/fheq-2024/4.15.b1. Do not claim that every student reaches the excellent standard.",
  aad="Raise it when a student asks what the degree expects of them overall. Ask which of the three standards they are aiming for in their strongest area. Never present the typical or excellent standard as the minimum.")

s('4.3', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='institutions and honours students in Performance', addressee='both',
  verbs=['perform', 'refer'], about='most exceed the threshold; Annex D for classification evidence', domain='none', award=HON,
  para="Most students will do well above the threshold; each institution decides what counts as evidence of that and should refer to Annex D of the qualification frameworks, which describes the four honours classes.",
  prac="When setting what counts as evidence of achievement, refer to Annex D's descriptions of the four honours classes, expecting most students to perform well above the threshold.",
  ben="Most students will do much better than the minimum standard, and your university should judge your work against shared national descriptions of the honours classes.",
  aaw="Describe this as an expectation (should) on institutions to refer to Annex D when deciding evidence of achievement, with a stated expectation (will) that most students exceed the threshold, at FHEQ level 6 and FQHEIS level 10. Cite it as (" + CITE + "4.3) and set it beside qaa/fheq-2024/annex-d/summary/r1/3rd to r1/1st and the FHEQ document's SL6 bands. Do not claim the statement sets the class boundaries itself.",
  aad="Raise it when a team aligns its marking criteria to degree classes, or a student asks what a 2.1 means. Ask staff how their 2.1 criteria compare with Annex D's description; ask a student which class description fits their recent work. Avoid suggesting the threshold is where most students finish.")

s('4.6', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='honours students in Performance', addressee='both',
  verbs=['made', 'meet', 'demonstrated', 'transcend', 'display', 'demonstrate'], about='what meeting the threshold and excellent work mean', domain='none', award=HON,
  para="It matters that students know the standards and are pushed and helped past the minimum. They will meet the threshold when, as fits their course, their knowledge, understanding, creativity and skill are enough to present performance or argument on the discipline's skills or materials; excellent work tends to go past the outcomes, with originality, insight, artistic or technical excellence and research of the highest standard.",
  prac="Make the standards known to students and support them past the minimum. Treat the threshold as met when knowledge, understanding, creativity and skill are enough to present performance, information or argument in the discipline; expect excellent work to exceed the outcomes with originality, insight and artistic or technical excellence.",
  ben="You will meet the minimum standard when what you know and can do is enough to present a performance or an argument on your discipline's skills or materials; excellent work goes beyond the set outcomes, with originality, insight and high artistic or technical quality.",
  aaw="Present this as the statement's own definition of its threshold and excellent rungs (will) for honours graduates at FHEQ level 6, with an expectation that students are supported beyond the minimum. Cite it as (" + CITE + "4.6) and set it beside the rung lists 4.8 to 4.16 and Annex D qaa/fheq-2024/annex-d/summary/r1/3rd and qaa/fheq-2024/annex-d/summary/r1/1st. Do not claim the excellent description is a requirement; it says what excellent work tends to show.",
  aad="Raise it when a student asks what separates passing from excellent work. Ask them where in their recent work they went beyond what the brief asked. Never present originality as a condition of passing.")

s('4.7', find='However, all courses should embed and promote concepts and practices of accessibility, equality, diversity and inclusion, enterprise and sustainable development.',
  type='expectation', rung='none', force='should', level='none', appliesTo='all courses in the subject', addressee='provider',
  verbs=['embed', 'promote'], about='the cross-cutting themes in every course', domain='none', award=[HON, MA],
  para="Every course should build in and advance, as concepts and as practice, access, equality, diversity and inclusion, enterprise and sustainability.",
  prac="Whatever outcomes your course selects from the indicative list, build access, equality, diversity and inclusion, enterprise and sustainability into both content and practice.",
  ben=('n/a', 'a duty on those who design courses; it sets no outcome for the student'),
  aaw="Describe this as an expectation (should) on every course in the subject: that the cross-cutting themes are embedded. Cite it as (" + CITE + "4.7) and set it beside the theme sections in paras 1.17 to 1.38 and the note in the same paragraph that the outcomes are indicative, not a checklist. Do not claim each listed outcome is required; only the themes carry this should.",
  aad="Raise it when a team reviews a module for the four themes. Ask staff where in the module each theme shows in practice, not only in reading. Keep it with staff.")

# ------------------------------------------------------------- 3.3 outcome list ("Students will:")
def o(i, dom, verbs, about, para, prac, ben, fw, link, q):
    s(i, type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students of Performance', addressee='learner',
      verbs=verbs, about=about, domain=dom, award=HON, para=para, prac=prac, ben=ben,
      aaw=("Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. "
           "Cite it as (" + CITE + i + "). Set it beside the rung item " + link + ", the honours descriptor qaa/fheq-2024/" + fw + " and spine:6. "
           "Do not claim every course develops every item to the same depth."),
      aad=("Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. "
           "Ask a student: " + q + " Avoid reading the whole list aloud."))

o('3.3.b1', 'subject-skill', ['engage'], "performing and producing with the field's vocabularies and methods",
  "Will take part in performance and production, grounded in learning and understanding suitable vocabularies, skills, structures, working methods and research approaches.",
  "Give students performance and production work built on the field's vocabularies, skills, structures and research approaches.",
  "You will take part in performing and producing work, built on learning the vocabularies, skills and methods of your field.",
  '4.15.b2', '4.9.b1', "Which performance or production methods can you now use without being shown?")
o('3.3.b2', 'subject-skill', ['develop'], 'techniques from cultural forms or practitioners',
  "Will develop techniques drawn from or shaped by particular cultural forms, histories, contexts or practitioners.",
  "Teach techniques in relation to the cultural forms, histories and practitioners they come from.",
  "You will develop techniques that come from, or are shaped by, particular cultures, histories or practitioners.",
  '4.15.b2', '4.9.b1', "Which tradition or practitioner has shaped your technique most, and how?")
o('3.3.b3', 'generic-skill', ['take'], 'project management and creative decision-making',
  "Will take responsibility for managing projects and making creative decisions, alone or in groups.",
  "Give students ownership of project management and creative decisions, individually and in groups.",
  "You will take charge of managing projects and making creative decisions, on your own or in a group.",
  '4.15.b9.1', '4.10.b10', "When did you last make a creative decision that the group then followed?")
o('3.3.b4', 'subject-skill', ['describe', 'theorise', 'interpret', 'evaluate'], 'analysing performance texts and events',
  "Will describe, theorise, interpret and evaluate texts and events in performance from several perspectives, using the subject's vocabularies.",
  "Ask students to analyse performance texts and events from more than one perspective in the subject's terms.",
  "You will describe, theorise, interpret and judge performance texts and events from different points of view, using the subject's language.",
  '4.15.b7', '4.9.b4', "Which perspective do you reach for first when you analyse a performance, and which do you neglect?")
o('3.3.b5', 'subject-skill', ['access', 'analyse'], 'historical materials',
  "Will find and analyse historical materials.",
  "Include work with archives and historical sources.",
  "You will find and analyse historical sources.",
  '4.15.b5', '4.9.b5', "Which historical source have you worked with directly, not through someone else's account?")
o('3.3.b6', 'understanding', ['analyse'], "performance's role in social, cultural and political discourse",
  "Will analyse what performance does in social, cultural and political debate, past and present.",
  "Set analysis of performance's part in social, cultural and political debate, then and now.",
  "You will analyse what performance does in social, cultural and political debate, past and present.",
  '4.15.b1', '4.8.b5', "Can you name a performance that changed a public conversation, and explain how?")
o('3.3.b7', 'subject-skill', ['plan', 'facilitate', 'deliver', 'evaluate'], 'participatory projects in social, educational and community settings',
  "Will plan, lead, deliver and evaluate projects that use participatory performance skill in social, educational and community settings.",
  "Offer participatory projects that students plan, facilitate, deliver and evaluate in community, educational or social settings.",
  "You will plan, lead, run and evaluate projects that use participatory performance in community, educational and social settings.",
  '4.15.b6', '4.8.b5', "What would you change after evaluating the last participatory session you led?")
o('3.3.b8', 'understanding', ['address'], 'ethical implications of performance',
  "Will deal with the ethical questions performance raises.",
  "Make the ethics of performance an explicit topic and a part of practical work.",
  "You will deal with the ethical questions that performance raises.",
  '4.15.b4', '4.10.b3', "What ethical question did your last project raise, and how did you handle it?")
o('3.3.b9', 'generic-skill', ['research', 'evaluate', 'arrive', 'articulate'], 'research, independent judgement and reasoned argument',
  "Will research and evaluate information, reach their own judgements and make reasoned arguments.",
  "Set tasks that call for research, independent judgement and reasoned argument.",
  "You will research and evaluate information, reach your own judgements and make reasoned arguments.",
  '4.15.b3.1', '4.10.b4', "Where in your last essay or project did you reach a judgement of your own?")
o('3.3.b10', 'generic-skill', ['operate', 'generate', 'pursue'], 'collaboration towards shared goals',
  "Will work with others in intellectual, creative and professional settings to set and pursue shared goals.",
  "Build collaboration into intellectual, creative and professional tasks, with shared goals.",
  "You will work with others in academic, creative and professional settings to set and reach shared goals.",
  '4.15.b9.1', '4.10.b5', "How did your group agree its goals on the last shared project?")
o('3.3.b11', 'generic-skill', ['consider', 'acknowledge', 'respect'], 'respect for diverse views and traditions',
  "Will consider, recognise and respect different opinions, experiences and performance traditions.",
  "Create space where students engage respectfully with different views, experiences and traditions.",
  "You will consider, recognise and respect different opinions, experiences and performance traditions.",
  '4.15.b9.1', '4.10.b2', "Which tradition unlike your own have you learned most from?")
o('3.3.b12', 'generic-skill', ['produce'], 'scholarly and professional writing',
  "Will write in fitting scholarly and professional registers and conventions.",
  "Teach and assess writing in both scholarly and professional registers.",
  "You will write in the right academic and professional styles for the task.",
  '4.15.b8', '4.10.b7', "Which kind of writing for the profession have you practised, beyond essays?")
o('3.3.b13', 'generic-skill', ['present'], 'presenting information in suitable forms',
  "Will present information in a range of forms suited to content, audience and context.",
  "Assess presentation in several forms, fitted to content, audience and setting.",
  "You will present information in different forms to suit the content, the audience and the setting.",
  '4.15.b8', '4.10.b7', "How did you change a presentation for a different audience?")

# ------------------------------------------------------------- the rungs: 4.8 to 4.10 threshold, 4.11 to 4.13 typical, 4.14 to 4.16 excellent
# Each rung has three lists: subject knowledge and understanding, subject-specific skills, generic and graduate skills.
# ROWS link the same outcome across rungs where the content plainly matches (inferred; the issuer does not pair them).
ROWS = [
    # name, domain, threshold, typical, excellent, FHEQ level 6 descriptor, Annex D row, question
    ('forms, traditions and histories', 'knowledge', '4.8.b1', '4.11.b1', '4.14.b1', '4.15.b1', 'knowledge/r1', "Which tradition or history of performance could you explain to a newcomer, and which do you know only by name?"),
    ('components of performance and how work is made', 'knowledge', '4.8.b2', '4.11.b2', '4.14.b2', '4.15.b1', 'knowledge/r1', "Can you trace one of your own pieces from first idea to its record afterwards?"),
    ('critical and theoretical perspectives', 'knowledge', '4.8.b3', '4.11.b3', '4.14.b3', '4.15.b7', 'knowledge/r2', "Which critical or theoretical approach do you use most, and when did you last test it against another?"),
    ('practitioners, theorists and their contexts', 'knowledge', '4.8.b4', '4.11.b4', '4.14.b4', '4.15.b1', 'knowledge/r1', "Which practitioner shaped your work most, and what in their context explains their approach?"),
    ('role of performance in society, education and industry', 'knowledge', '4.8.b5', '4.11.b5', '4.14.b5', '4.15.b1', 'knowledge/r1', "Where have you seen performance do work outside the theatre, in a school, a community or an industry?"),
    ('critical and creative enquiry together', 'understanding', '4.8.b6', '4.11.b6', '4.14.b6', '4.15.b7', 'cognitive/r2', "When did critical reading last change something you made, or making change how you read?"),
    ('interpreting texts and scores to make performance', 'understanding', '4.8.b7', '4.11.b7', '4.14.b7', '4.15.b2', 'knowledge/r2', "How do you move from a script or score to choices in the room?"),
    ('group and collective processes', 'understanding', '4.8.b8', '4.11.b8', '4.14.b8', '4.15.b9.1', 'transferable/r2', "What did your last group process teach you about how ensembles work?"),
    ('elements of performance', 'understanding', '4.8.b9', '4.11.b9', '4.14.b9', '4.15.b1', 'knowledge/r2', "Which element of performance do you tend to overlook, and what happens when you put it first?"),
    ('interdisciplinary elements and their use', 'understanding', '4.8.b10', '4.11.b10', '4.14.b10', '4.15.b3.1', 'knowledge/r2', "Which idea from another discipline has changed your practice, and how did you apply it?"),
    ('knowledge and skills from other disciplines', 'understanding', '4.8.b11', None, None, '4.15.b1', 'knowledge/r2', "Which subject outside performance do you draw on, and for what?"),
    ('safe, ethical and sustainable practice', 'understanding', '4.8.b12', '4.11.b11', '4.14.b11', '4.15.b9.2', 'transferable/r4', "How did you make your last project safe, ethical and environmentally sound?"),
    ('making and producing performance', 'subject-skill', '4.9.b1', '4.12.b3', '4.15.b3', '4.15.b2', 'practical/r3', "Which working methods could you use to make a piece from scratch without being shown?"),
    ('realising a text, stimulus or score', 'subject-skill', '4.9.b2', '4.12.b2', '4.15.b2', '4.15.b2', 'practical/r3', "What did the last text or score you worked on make possible, and what did you do with it?"),
    ('records and documentation', 'subject-skill', '4.9.b3', None, None, '4.15.b2', 'practical/r4', "How did you record your last piece, and could someone restage it from that record?"),
    ('describing and evaluating performance events', 'subject-skill', '4.9.b4', None, None, '4.15.b7', 'cognitive/r1', "Can you describe, interpret and judge a performance you saw recently in a few sentences?"),
    ('independent research', 'subject-skill', '4.9.b5', '4.12.b4', '4.15.b4', '4.15.b6', 'knowledge/r3', "What question did your last independent research answer, and where did you find the evidence?"),
    ('cultural frameworks of performance', 'subject-skill', '4.9.b6', '4.12.b5', '4.15.b5', '4.15.b7', 'cognitive/r1', "What cultural frame shapes the piece you are working on now?"),
    ('performance space', 'subject-skill', '4.9.b7', None, None, '4.15.b6', 'practical/r1', "How did the space change your last piece?"),
    ('selecting, refining and presenting skills', 'subject-skill', None, '4.12.b1', '4.15.b1', '4.15.b2', 'practical/r3', "Which of your skills do you choose to show first, and how have you refined it?"),
    ('self-management and shared goals', 'generic-skill', '4.10.b1', '4.13.b4', '4.16.b4', '4.15.b5', 'transferable/r3', "How do you plan your time when rehearsals and deadlines collide?"),
    ('adaptability and awareness of self and others', 'generic-skill', '4.10.b2', None, None, '4.15.b4', 'transferable/r5', "When did you last change your approach because of feedback, and what did you notice about yourself?"),
    ('risk and ethical practice', 'generic-skill', '4.10.b3', None, None, '4.15.b9.2', 'transferable/r4', "What risks did you assess on your last practical project, and how did you manage them?"),
    ('critical argument', 'generic-skill', '4.10.b4', '4.13.b1', '4.16.b1', '4.15.b3.1', 'cognitive/r2', "What is the strongest argument you have built this year, and how did you present it?"),
    ('group work', 'generic-skill', '4.10.b5', '4.13.b3', '4.16.b3', '4.15.b9.1', 'transferable/r2', "What did you contribute to your last group project that no one else did?"),
    ('creative and interpersonal issues', 'generic-skill', '4.10.b6', '4.13.b5', '4.16.b5', '4.15.b9.1', 'transferable/r2', "How did you handle a disagreement in a creative team?"),
    ('communication and presentation', 'generic-skill', '4.10.b7', None, None, '4.15.b8', 'transferable/r1', "In which forms have you presented your ideas this year, and which worked best for which audience?"),
    ('information retrieval and management', 'generic-skill', '4.10.b8', '4.13.b6', '4.16.b6', '4.15.b5', 'cognitive/r1', "How do you decide which sources to keep and which to drop?"),
    ('digital media and technology', 'generic-skill', '4.10.b9', '4.13.b7', '4.16.b7', '4.15.b6', 'transferable/r1', "Which digital tool have you adapted for your own creative purpose?"),
    ('project management', 'generic-skill', '4.10.b10', None, None, '4.15.b9.1', 'transferable/r3', "How did you plan and organise the last activity you led?"),
    ('numeracy for creative outcomes', 'generic-skill', '4.10.b11', '4.13.b8', '4.16.b8', '4.15.b3.1', 'transferable/r1', "Where did numbers matter in your last production, for example a budget, a schedule or a lighting plot?"),
    ('discourse and representation', 'generic-skill', None, '4.13.b2', '4.16.b2', '4.15.b7', 'cognitive/r2', "How does the way something is talked about shape how audiences receive it?"),
]
ROW = {}
for _r in ROWS:
    for _k, _id in zip(('threshold', 'typical', 'excellent'), _r[2:5]):
        if _id:
            ROW[_id] = _r
LIST = {'4.8': 'subject knowledge and understanding', '4.9': 'subject-specific skills', '4.10': 'generic and graduate skills',
        '4.11': 'subject knowledge, understanding and skills', '4.12': 'subject-specific skills', '4.13': 'generic and graduate skills',
        '4.14': 'subject knowledge, understanding and skills', '4.15': 'subject-specific skills', '4.16': 'generic and graduate skills'}
BL = {'threshold': 'At the minimum standard for your honours degree, ', 'typical': 'At the typical standard, ', 'excellent': 'At the excellent standard, '}
FT = {'threshold': 'the threshold standard: what every honours graduate should be able to show, the minimum for the award (should)',
      'typical': 'the typical standard: what most honours graduates should show, above the minimum (should)',
      'excellent': 'the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should)'}
AV = {'threshold': 'Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement.',
      'typical': 'Do not present it as the pass standard; the minimum is the threshold item.',
      'excellent': 'Do not present it as the minimum or as expected of every student.'}
SIT = {'threshold': 'a student asks what they need to show to pass in this area, or staff check that a module secures the minimum',
       'typical': 'a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes',
       'excellent': 'a student aims for a first, or staff describe what first-class work looks like in this area'}
AVD = {'threshold': 'Avoid reading the list aloud; draw out one example from their own work.',
       'typical': 'Never treat this as the pass mark.',
       'excellent': 'Never present this as what everyone must reach.'}
BAND = {'threshold': ['3rd'], 'typical': ['2.2', '2.1'], 'excellent': ['1st']}

def r(i, rung, verbs, about, para, prac, ben, find=None):
    row = ROW[i]; n = i.rsplit('.b', 1)[0]
    others = [x for x in row[2:5] if x and x != i]
    nb = ('the same outcome at the other rungs (' + ', '.join(others) + ')') if others else ('the other items in para ' + n + ', since this outcome has no counterpart at the other rungs')
    ad = ' and '.join('qaa/fheq-2024/annex-d/' + row[6] + '/' + b for b in BAND[rung])
    k = dict(type=rung, rung=rung, force='should', level='fheq:6', appliesTo='honours graduates in Performance at the %s rung' % rung,
             addressee='learner', award=HON, verbs=verbs, about=about, domain=row[1], para=para, prac=prac, ben=BL[rung] + ben,
             aaw=("Treat this as " + FT[rung] + ", in " + LIST[n] + ", for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). "
                  "Cite it as (" + CITE + i + "). " + AV[rung] + " Set it beside " + nb + ", the honours descriptor qaa/fheq-2024/" + row[5] + " with spine:6, and Annex D " + ad + "."),
             aad=("Raise it when " + SIT[rung] + ". Put it in plain words: second person for a student, and for staff as what a module lets students show. "
                  "Ask: " + row[7] + " " + AVD[rung]))
    if find:
        k['find'] = find
    P[i] = k

# 4.8 threshold: subject knowledge and understanding
r('4.8.b1', 'threshold', [], 'forms, traditions and histories of performance',
  "Should be able to show knowledge of performance's forms, practices, techniques and traditions, its local and global histories and its applications.",
  "Ensure students can show what they know of the art form's forms, practices, techniques and traditions, its histories locally and globally, and its uses.",
  "you should be able to show what you know about the forms, practices, techniques and traditions of performance, its histories around the world and how it is used.")
r('4.8.b2', 'threshold', [], 'components of performance and how it is made',
  "Should show knowledge of the main components of performance and of how work is made, realised, managed, distributed, received and recorded.",
  "Cover the building blocks of performance and the full life of a work, from creation and management to distribution, audience and documentation.",
  "you should know the main parts that make up a performance and how a work is made, managed, shared, watched and recorded.")
r('4.8.b3', 'threshold', [], 'critical and theoretical perspectives',
  "Should show knowledge of the critical and theoretical approaches suited to studying the discipline.",
  "Teach the critical and theoretical approaches the discipline uses and check students can show they know them.",
  "you should know the main critical and theoretical ways of studying your discipline.")
r('4.8.b4', 'threshold', [], 'practitioners, theorists and their contexts',
  "Should show knowledge of practitioners and practices, or theorists, set in their cultural or historical contexts.",
  "Introduce key practitioners, practices or theorists and the cultural and historical settings that shaped them.",
  "you should know about practitioners, practices or theorists and the cultural or historical settings they come from.")
r('4.8.b5', 'threshold', [], 'role of performance in society, education and industry',
  "Should show knowledge of what performance does and how it works in social, educational, participatory and industry settings.",
  "Show students how performance functions in communities, education, participatory work and the industry.",
  "you should know what performance does in society, in education, in participatory work and in the industry.")
r('4.8.b6', 'threshold', [], 'interplay of critical and creative enquiry',
  "Should show understanding of how critical and creative ways of enquiring interact in the field.",
  "Help students see how critical study and creative practice feed each other as ways of enquiring.",
  "you should understand how thinking critically and making creative work feed into each other.")
r('4.8.b7', 'threshold', [], 'interpreting texts and scores to make performance',
  "Should show understanding of how to work with and interpret texts, media, notations or scores in order to make performance.",
  "Teach students to read and interpret scripts, media, notation and scores as material for making performance.",
  "you should understand how to read and interpret scripts, media, notation or scores to make performance.")
r('4.8.b8', 'threshold', [], 'group and collective processes',
  "Should show understanding of group and collective ways of working, with their effects and dynamics.",
  "Help students understand how groups and ensembles work, including their dynamics and effects.",
  "you should understand how groups and ensembles work, and the effects and dynamics they bring.")
r('4.8.b9', 'threshold', [], 'elements of performance',
  "Should show understanding of the key elements of performance in the disciplines, such as source material, performers, space, music, soundscape, text, movement and setting.",
  "Cover the elements performance works with, for example sources, performers, space, sound, text, movement and setting.",
  "you should understand the building blocks of performance, such as source material, performers, space, sound, text, movement and setting.")
r('4.8.b10', 'threshold', [], 'interdisciplinary elements and their use',
  "Should show understanding of the interdisciplinary elements relevant to performance and how to put them to use.",
  "Introduce the interdisciplinary elements that suit the course and show students how to apply them.",
  "you should understand which ideas and methods from across disciplines suit performance, and how to use them.")
r('4.8.b11', 'threshold', [], 'knowledge and skills from other disciplines',
  "Should show understanding of knowledge, practices, concepts and skills drawn from other disciplines.",
  "Bring in knowledge, practices, concepts and skills from neighbouring disciplines and check students understand them.",
  "you should understand ideas, practices and skills that come from other subjects.")
r('4.8.b12', 'threshold', [], 'safe, ethical and sustainable working practice',
  "Should show understanding of performance practitioners' duty to make working practice safe, ethical and environmentally sustainable.",
  "Teach students the duty performance practitioners carry for safe, ethical and environmentally sustainable ways of working.",
  "you should understand your duty, as someone who makes performance, to work safely, ethically and sustainably.",
  find='understanding of the responsibilities of performance practitioners to facilitate safe, ethical and environmentally sustainable working practices.')

# 4.9 threshold: subject-specific skills
r('4.9.b1', 'threshold', ['engage'], "creating or producing performance with the field's vocabularies and methods",
  "Should be able to take part in making or producing performance, drawing on the field's vocabularies, techniques, crafts and technologies, its structures and contexts, and its working and research methods.",
  "Give students repeated practice in making or producing performance with the field's vocabularies, techniques, crafts, technologies and methods.",
  "you should be able to make or produce performance using the techniques, crafts, technologies and working methods of your field.")
r('4.9.b2', 'threshold', ['understand', 'realise'], 'realising the possibilities of a text, stimulus or score',
  "Should be able to see what a text, stimulus, media, dance notation or score makes possible for performance and, where suitable, realise it through design, technology and performance.",
  "Train students to read a text, stimulus, media, notation or score for its performance possibilities and to realise them in design, technology and performance.",
  "you should be able to see what a script, prompt, notation or score could become in performance and bring it to life through design, technology and performance.")
r('4.9.b3', 'threshold', ['make'], 'recording performance through notation or documentation',
  "Should be able to record performance, using notation or documentation skills and technologies.",
  "Teach notation and documentation so students can make records of performance.",
  "you should be able to record performance using notation, documentation and the technology for it.")
r('4.9.b4', 'threshold', ['describe', 'interpret', 'evaluate'], 'describing, interpreting and evaluating performance events',
  "Should be able to describe, interpret and evaluate performance events.",
  "Give students practice in describing, interpreting and judging performances they make or see.",
  "you should be able to describe, interpret and judge performances.")
r('4.9.b5', 'threshold', ['engage'], 'independent research into performance',
  "Should be able to carry out independent research, whether into past or present performance or as part of making or responding to it.",
  "Build independent research into the course, both historical study and research within the making of work.",
  "you should be able to research on your own, whether looking at past or present performance or as part of making or responding to work.")
r('4.9.b6', 'threshold', ['identify'], 'identifying cultural and contextual frameworks',
  "Should be able to identify the cultural and contextual frameworks within which performance sits.",
  "Help students name the cultural and contextual frameworks around the performance they study and make.",
  "you should be able to identify the cultural settings and contexts that frame a performance.")
r('4.9.b7', 'threshold', ['investigate', 'determine'], 'spatial relationships in performance environments',
  "Should be able to investigate performance environments and work out what their spatial relationships mean.",
  "Give students tasks that explore performance spaces and what their spatial relationships mean for the work.",
  "you should be able to explore a performance space and work out what its spatial relationships mean.")

# 4.10 threshold: generic and graduate skills
r('4.10.b1', 'threshold', ['demonstrate', 'set', 'manage', 'meet'], 'self-management: goals, workload and deadlines',
  "Should be able to manage themselves: setting goals, handling workloads and meeting deadlines.",
  "Give students tasks where they set their own goals, manage workloads and meet deadlines.",
  "you should be able to manage yourself: set goals, handle your workload and meet deadlines.")
r('4.10.b2', 'threshold', ['display'], 'adaptability and critical awareness of self and others',
  "Should be able to show adaptability, flexibility and a critical awareness of themselves and others.",
  "Create situations that ask students to adapt and to reflect critically on themselves and others.",
  "you should be able to adapt, stay flexible and think critically about yourself and others.")
r('4.10.b3', 'threshold', ['assess', 'manage', 'employ'], 'risk management and ethical practice',
  "Should be able to assess and manage risk and work ethically.",
  "Teach risk assessment and ethical working, and expect both in practical work.",
  "you should be able to assess and manage risk and work ethically.")
r('4.10.b4', 'threshold', ['deploy', 'operate', 'respond', 'develop', 'construct', 'present'], 'critical engagement and argument',
  "Should be able to engage critically, responding with reflexive, creative and critical thought, to develop ideas and build and present arguments suitably.",
  "Ask students to respond reflexively and critically, develop ideas and make and present arguments in fitting forms.",
  "you should be able to think critically and reflexively, develop ideas and build and present an argument in a suitable form.")
r('4.10.b5', 'threshold', ['work', 'have'], 'group and team work on collaborative projects',
  "Should be able to work in a group or team, with the skills to carry out collaborative project work.",
  "Build collaborative projects that call for and assess team skills.",
  "you should be able to work in a group or team and have the skills to complete a shared project.")
r('4.10.b6', 'threshold', ['demonstrate', 'manage'], 'managing creative, personal and interpersonal issues',
  "Should be able to handle creative, personal and interpersonal relationship issues in creative work.",
  "Support students to manage creative and interpersonal tensions within creative work.",
  "you should be able to handle creative, personal and interpersonal issues that come up in creative work.")
r('4.10.b7', 'threshold', ['demonstrate', 'articulate', 'communicate'], 'communication and presentation',
  "Should be able to communicate and present, expressing ideas and information in different forms suited to content and context.",
  "Assess communication in varied forms, matched to content and context.",
  "you should be able to communicate and present ideas and information in different forms, suited to what you are saying and to whom.")
r('4.10.b8', 'threshold', ['deploy', 'retrieve', 'gather', 'sift', 'evaluate', 'organise'], 'information management',
  "Should be able to manage information: finding it, gathering, sifting, judging and organising it.",
  "Teach information skills: finding, gathering, sifting, judging and organising sources.",
  "you should be able to find, gather, sift, judge and organise information.")
r('4.10.b9', 'threshold', ['demonstrate', 'select', 'employ', 'adapt'], 'using digital media and information technology',
  "Should be able to choose, use and adapt digital media and information technologies.",
  "Give students practice in choosing, using and adapting digital tools for their work.",
  "you should be able to choose, use and adapt digital media and technology.")
r('4.10.b10', 'threshold', ['use', 'investigate', 'organise', 'realise'], 'project management',
  "Should be able to use project management skills to investigate, organise and carry out activities.",
  "Give students projects they plan, organise and deliver themselves.",
  "you should be able to plan, organise and carry out a project.")
r('4.10.b11', 'threshold', ['apply', 'solve', 'realise'], 'numeracy for problem-solving and creative outcomes',
  "Should be able to apply suitable numeracy skills to solve problems and achieve creative outcomes.",
  "Build numeracy into practical work, such as budgets, timings and technical calculations.",
  "you should be able to use numbers to solve problems and make creative work happen.",
  find='apply appropriate numeracy skills to solve problems and realise creative outcomes.')

# 4.11 typical: subject knowledge, understanding and skills
r('4.11.b1', 'typical', [], 'creative and critical engagement with forms and traditions, problematising them',
  "Should show creative and critical engagement with performance's forms, practices, techniques, traditions, histories and applications, and be able to question them.",
  "Expect students to engage creatively and critically with the art form's forms, techniques, traditions and histories, and to problematise them rather than accept them.",
  "you should engage creatively and critically with the forms, techniques, traditions and histories of performance, and be able to question them.")
r('4.11.b2', 'typical', [], 'creative and critical engagement with components and making',
  "Should show creative and critical engagement with the main components of performance and with how work is made, realised, managed, distributed and recorded.",
  "Ask students to work creatively and critically with performance's components and with every stage of a work's life.",
  "you should work creatively and critically with the parts of a performance and with how a work is made, managed, shared and recorded.")
r('4.11.b3', 'typical', [], 'engaging with critical and theoretical perspectives',
  "Should show engagement with the critical and theoretical approaches suited to studying performance.",
  "Expect students to engage with, not only know, the critical and theoretical approaches of the field.",
  "you should engage actively with critical and theoretical ways of studying performance.")
r('4.11.b4', 'typical', [], 'critical understanding of practitioners and contexts',
  "Should show critical understanding of key practitioners, practices or theorists and their cultural or historical settings.",
  "Expect a critical grasp of key practitioners, practices or theorists in their cultural and historical settings.",
  "you should understand key practitioners, practices or theorists critically, in their cultural or historical settings.")
r('4.11.b5', 'typical', [], 'engaging with the role of performance in society and industry',
  "Should show creative and critical engagement with how performance functions in social, educational, participatory and industry settings.",
  "Expect students to engage creatively and critically with performance's place in communities, education, participation and industry.",
  "you should engage creatively and critically with what performance does in society, education, participatory work and the industry.")
r('4.11.b6', 'typical', [], 'strong understanding of critical and creative enquiry',
  "Should show a strong understanding of how critical and creative enquiry interact in the field.",
  "Expect a strong grasp of how critical and creative enquiry work together.",
  "you should have a strong understanding of how critical thinking and creative making feed into each other.")
r('4.11.b7', 'typical', [], 'critical interpretation of texts and scores',
  "Should show critical understanding of how to work with and interpret texts, media, notations or scores to make performance.",
  "Expect students to interpret scripts, media, notation and scores critically as material for performance.",
  "you should understand critically how to read and interpret scripts, media, notation or scores to make performance.")
r('4.11.b8', 'typical', [], 'creative and critical understanding of group processes',
  "Should show creative and critical understanding of group and collective ways of working.",
  "Expect a creative and critical grasp of how groups and ensembles work.",
  "you should understand group and ensemble work creatively and critically.")
r('4.11.b9', 'typical', [], 'creative and critical understanding of the elements of performance',
  "Should show creative and critical understanding of the key elements of performance, such as sources, performers, bodies, space, sound, text, movement and setting.",
  "Expect students to understand performance's elements creatively and critically, the body included.",
  "you should understand the building blocks of performance creatively and critically, including bodies, space, sound, text, movement and setting.")
r('4.11.b10', 'typical', [], 'interdisciplinary elements and drawing on other fields',
  "Should show creative and critical understanding of suitable interdisciplinary elements of performance and how to use ideas, methods and skills taken from other fields.",
  "Expect students to understand, creatively and critically, which interdisciplinary elements suit their work and how to draw on other fields.",
  "you should understand creatively and critically how ideas, methods and skills from other subjects can be used in performance.")
r('4.11.b11', 'typical', [], 'critical understanding of safe, sustainable and ethical practice',
  "Should show critical understanding of performance practitioners' duty to make working practice safe, environmentally sustainable and ethical.",
  "Expect a critical grasp of the practitioner's duty to work safely, sustainably and ethically.",
  "you should understand critically your duty to work safely, sustainably and ethically when making performance.",
  find='critical understanding of the responsibilities of performance practitioners to facilitate safe, environmentally sustainable and ethical working practices.')

# 4.12 typical: subject-specific skills
r('4.12.b1', 'typical', ['engage', 'demonstrate', 'select', 'refine', 'present'], 'selecting, refining and presenting performance and production skills',
  "Should be able to work creatively and critically with performance and production skills and processes, choosing, refining and presenting them in performance.",
  "Expect students to choose, refine and present performance and production skills with creative and critical judgement.",
  "you should be able to work creatively and critically with performance and production skills, choosing, refining and presenting them in your work.")
r('4.12.b2', 'typical', ['engage', 'realise'], 'realising a text or score sensitively',
  "Should be able to work creatively and critically with what a text, stimulus, notation or score offers performance, and where suitable realise it with sensitivity through design and performance.",
  "Expect sensitive, creative and critical realisation of texts, stimuli, notation or scores in design and performance.",
  "you should be able to work creatively and critically with what a script, prompt, notation or score offers and bring it to life with sensitivity through design and performance.")
r('4.12.b3', 'typical', ['engage'], 'making performance with a developed grasp of its vocabularies',
  "Should be able to work creatively and critically on making or producing performance, with a developed grasp of suitable vocabularies, techniques, crafts, structures and working methods.",
  "Expect students to make or produce work creatively and critically, drawing on a developed command of the field's vocabularies and methods.",
  "you should be able to make or produce performance creatively and critically, with a developed grasp of the techniques, crafts and working methods involved.")
r('4.12.b4', 'typical', ['engage'], 'creative and critical independent research',
  "Should be able to carry out suitable independent research creatively and critically, whether into past or present performance or within the making of new work.",
  "Expect independent research that is creative and critical, historical or practice-based.",
  "you should be able to research on your own creatively and critically, whether into past or present performance or as part of making new work.")
r('4.12.b5', 'typical', ['identify', 'interpret'], 'interpreting cultural frameworks in social and historical context',
  "Should be able to identify and interpret the cultural frameworks around performance events and how they relate to social and historical contexts.",
  "Expect students to interpret, not only name, the cultural frameworks of performance events and link them to social and historical context.",
  "you should be able to identify and interpret the cultural frameworks around a performance and how they link to its social and historical setting.",
  find='identify and interpret the cultural frameworks that surround performance events and their specific relation to social and historical contexts.')

# 4.13 typical: generic and graduate skills
r('4.13.b1', 'typical', ['have', 'developing', 'constructing', 'evaluate', 'present'], 'critical and analytical argument',
  "Should be able to analyse critically when developing ideas and building arguments, and judge and present them in different ways.",
  "Expect critical, analytical development of ideas and arguments, judged and presented in several forms.",
  "you should be able to develop ideas and arguments critically and analytically, and judge and present them in different ways.")
r('4.13.b2', 'typical', ['demonstrate', 'examine', 'evaluate'], 'discourse and its effects on representation and reception',
  "Should show a developed ability to examine and evaluate kinds of discourse and their effects on how the arts and wider culture represent and are received.",
  "Expect students to analyse how forms of discourse shape representation and reception in the arts and culture.",
  "you should be able to examine and judge different kinds of discourse and how they shape representation and reception in the arts and culture.")
r('4.13.b3', 'typical', ['work', 'have'], 'productive, creative group work on practice-based projects',
  "Should be able to work productively, creatively and imaginatively in a group, with the creative skills to carry out practice-based work.",
  "Expect productive, imaginative group work and the creative skills to complete practice-based projects.",
  "you should be able to work productively and imaginatively in a group and have the creative skills to complete practical projects.")
r('4.13.b4', 'typical', ['manage', 'meet', 'negotiate', 'pursue'], 'workload, deadlines and goals with others',
  "Should be able to manage their own workload efficiently and effectively, meet deadlines, and agree and pursue goals with others successfully.",
  "Expect students to manage their own workload, meet deadlines and negotiate and achieve goals with others.",
  "you should be able to manage your own workload well, meet deadlines and agree and reach goals with others.")
r('4.13.b5', 'typical', ['manage'], 'managing creative and interpersonal issues constructively',
  "Should be able to manage creative, personal and interpersonal issues in creative work constructively and effectively.",
  "Expect constructive, effective handling of creative and interpersonal issues in group work.",
  "you should be able to deal constructively and effectively with creative, personal and interpersonal issues in creative work.")
r('4.13.b6', 'typical', ['use', 'gather', 'sift', 'organise', 'evaluate'], 'independent information retrieval and critical evaluation',
  "Should be able to use information retrieval skills to gather, sift and organise material on their own and to judge its significance critically.",
  "Expect independent searching and organising of material, with critical judgement of its value.",
  "you should be able to find, sift and organise material on your own and judge critically how much it matters.")
r('4.13.b7', 'typical', ['demonstrate', 'have'], 'technological and digital skills and awareness',
  "Should show suitable technological and digital skills and a considerable awareness of how they apply and what they could do in the field.",
  "Expect sound digital skills and an informed view of how technology serves the field.",
  "you should have suitable technical and digital skills and a good sense of how they can be used in your field.")
r('4.13.b8', 'typical', ['identify', 'apply', 'solve', 'realise'], 'choosing and applying numeracy skills',
  "Should be able to identify and apply a range of suitable numeracy skills to solve problems and achieve creative outcomes.",
  "Expect students to choose the right numeracy skills for practical and creative problems.",
  "you should be able to pick and use the right number skills to solve problems and make creative work happen.",
  find='identify and apply a range of appropriate numeracy skills to solve problems and realise creative outcomes.')

# 4.14 excellent: subject knowledge, understanding and skills
r('4.14.b1', 'excellent', [], 'sophisticated engagement with forms and traditions, interrogating them',
  "Should show sophisticated engagement with performance's forms, practices, techniques, traditions, histories and applications, and the ability to interrogate them.",
  "Look for sophisticated engagement with the art form's forms, techniques, traditions and histories, interrogating them.",
  "you should engage with the forms, techniques, traditions and histories of performance in a sophisticated way and question them closely.")
r('4.14.b2', 'excellent', [], 'sophisticated engagement with components and making, leading to new insight',
  "Should show sophisticated creative and theoretical engagement with performance's components and with how work is made, realised, managed, distributed, interpreted and recorded, producing new insight.",
  "Look for sophisticated creative and theoretical work across performance's components and a work's whole life, leading to fresh insight.",
  "you should work with the parts of a performance and the whole life of a work in a sophisticated creative and theoretical way that produces new insight.")
r('4.14.b3', 'excellent', [], 'sophisticated engagement with critical and theoretical perspectives',
  "Should show sophisticated engagement with the critical and theoretical approaches suited to studying performance.",
  "Look for a sophisticated handling of the field's critical and theoretical approaches.",
  "you should handle critical and theoretical ways of studying performance in a sophisticated way.")
r('4.14.b4', 'excellent', [], 'comprehensive, critical understanding of practitioners and contexts',
  "Should show a comprehensive and critical understanding of key practitioners, practices or theorists and their cultural or historical settings.",
  "Look for a comprehensive, critical grasp of key practitioners, practices or theorists in context.",
  "you should have a full and critical understanding of key practitioners, practices or theorists in their cultural or historical settings.")
r('4.14.b5', 'excellent', [], 'sophisticated engagement with the role of performance in society and industry',
  "Should show sophisticated engagement with how performance functions in social, educational, participatory and industry settings.",
  "Look for sophisticated engagement with performance's place in communities, education, participation and industry.",
  "you should engage in a sophisticated way with what performance does in society, education, participatory work and the industry.")
r('4.14.b6', 'excellent', [], 'sophisticated understanding of critical and creative enquiry',
  "Should show sophisticated understanding of how critical and creative enquiry interact in the field.",
  "Look for a sophisticated grasp of how critical and creative enquiry work together.",
  "you should have a sophisticated understanding of how critical thinking and creative making feed into each other.")
r('4.14.b7', 'excellent', [], 'sophisticated interpretation of texts, notations and scores',
  "Should show sophisticated understanding of how to work with and interpret texts, media, dance notations or scores to make performance.",
  "Look for sophisticated interpretation of scripts, media, dance notation and scores as material for performance.",
  "you should understand in a sophisticated way how to read and interpret scripts, media, dance notation or scores to make performance.")
r('4.14.b8', 'excellent', [], 'sophisticated understanding and use of group processes',
  "Should show sophisticated critical understanding of group processes and the ability to apply it.",
  "Look for a sophisticated critical grasp of group processes, shown in how students use them.",
  "you should understand group processes in a sophisticated, critical way and put that understanding to use.")
r('4.14.b9', 'excellent', [], 'sophisticated understanding of the elements of performance',
  "Should show sophisticated critical understanding of the key elements of performance, such as sources, performers, the body, space, sound, text, movement and setting.",
  "Look for a sophisticated critical grasp of performance's elements, the body included.",
  "you should understand the building blocks of performance in a sophisticated, critical way, including the body, space, sound, text, movement and setting.")
r('4.14.b10', 'excellent', [], 'sophisticated understanding of interdisciplinary elements and other fields',
  "Should show sophisticated critical understanding of suitable interdisciplinary elements of performance and of how to use ideas, methods and skills from other fields.",
  "Look for a sophisticated critical grasp of interdisciplinary elements and of drawing on other fields.",
  "you should understand in a sophisticated, critical way how ideas, methods and skills from other subjects can be used in performance.")
r('4.14.b11', 'excellent', [], 'comprehensive understanding of safe, sustainable and ethical practice',
  "Should show comprehensive understanding of performance practitioners' duty to make working practice safe, environmentally sustainable and ethical.",
  "Look for a comprehensive grasp of the practitioner's duty to work safely, sustainably and ethically.",
  "you should have a full understanding of your duty to work safely, sustainably and ethically when making performance.",
  find='comprehensive understanding of the responsibilities of performance practitioners to facilitate safe, environmentally sustainable and ethical working practices.')

# 4.15 excellent: subject-specific skills
r('4.15.b1', 'excellent', ['engage', 'demonstrate', 'select', 'refine', 'present'], 'thorough critical command of performance and production processes',
  "Should be able to handle performance and production processes with critical depth and thoroughness, choosing, refining and presenting them in performance.",
  "Look for critical, thorough command of performance and production processes in what students select, refine and present.",
  "you should be able to handle performance and production processes with critical depth and thoroughness, choosing, refining and presenting them in your work.")
r('4.15.b2', 'excellent', ['engage', 'realise'], 'realising a text or score to make new or original work',
  "Should be able to work creatively and thoroughly with what a text, dance notation or score offers performance and, where suitable, realise it with sensitivity through design and performance, producing new or original work.",
  "Look for thorough, sensitive realisation of texts, notation or scores that leads to new or original work.",
  "you should be able to explore thoroughly and creatively what a script, notation or score offers and bring it to life with sensitivity, creating new or original work.")
r('4.15.b3', 'excellent', ['engage'], 'making performance with a thorough grasp of its vocabularies',
  "Should be able to work creatively and comprehensively on making or producing performance, with a developed and thorough grasp of suitable vocabularies, techniques, crafts, structures and working methods.",
  "Look for creative, comprehensive making or production backed by a thorough command of the field's vocabularies and methods.",
  "you should be able to make or produce performance creatively and comprehensively, with a thorough grasp of the techniques, crafts and working methods involved.")
r('4.15.b4', 'excellent', ['engage'], 'critical, comprehensive independent research towards new insight',
  "Should be able to carry out suitable independent research critically and comprehensively, into past or present performance or within the making of new or novel work or insight.",
  "Look for thorough, critical independent research that yields new performance or new insight.",
  "you should be able to research on your own critically and thoroughly, whether into past or present performance or as part of creating new work or ideas.")
r('4.15.b5', 'excellent', ['identify', 'interpret'], 'critical investigation of cultural frameworks in context',
  "Should be able to identify and interpret, through critical investigation, the cultural frameworks around performance events and their particular social and historical settings.",
  "Look for critical investigation that identifies and interprets the cultural frameworks of performance events in their social and historical settings.",
  "you should be able to investigate critically the cultural frameworks around a performance and interpret them in their social and historical setting.",
  find='identify and interpret through critical modes of investigation the cultural frameworks that surround performance events and their specific social and historical contexts.')

# 4.16 excellent: generic and graduate skills
r('4.16.b1', 'excellent', ['demonstrate', 'developing', 'constructing', 'evaluate', 'present'], 'sophisticated creative and analytical argument',
  "Should show sophisticated creative and analytical skill in developing and building arguments, and be able to judge and present them in different ways.",
  "Look for sophisticated creative and analytical argument, judged and presented in several forms.",
  "you should be able to develop arguments with sophisticated creative and analytical skill, and judge and present them in different ways.")
r('4.16.b2', 'excellent', ['demonstrate', 'examine', 'evaluate'], 'critical analysis of discourse and representation',
  "Should show a developed critical ability to examine and evaluate kinds of discourse and how they shape representation in the arts and wider culture.",
  "Look for developed critical analysis of how discourse shapes representation in the arts and culture.",
  "you should be able to examine and judge, critically and in depth, how kinds of discourse shape representation in the arts and culture.")
r('4.16.b3', 'excellent', ['work'], 'productive, creative group work',
  "Should be able to work in a group productively, creatively and imaginatively.",
  "Look for productive, imaginative contributions to group work.",
  "you should be able to work in a group productively, creatively and imaginatively.")
r('4.16.b4', 'excellent', ['manage', 'meet', 'negotiate', 'pursue'], 'workload, deadlines and shared goals',
  "Should be able to manage their own workload efficiently and effectively, meet deadlines, and agree and pursue shared goals with others.",
  "Look for efficient self-management and skilled negotiation of shared goals.",
  "you should be able to manage your own workload very well, meet deadlines and agree and work towards shared goals with others.")
r('4.16.b5', 'excellent', ['manage'], 'managing creative, artistic and interpersonal issues',
  "Should be able to manage creative, artistic, personal and interpersonal issues constructively and effectively.",
  "Look for constructive, effective handling of creative, artistic and interpersonal issues.",
  "you should be able to deal constructively and effectively with creative, artistic, personal and interpersonal issues.")
r('4.16.b6', 'excellent', ['use', 'gather', 'sift', 'synthesise', 'organise', 'evaluate'], 'discerning information retrieval and synthesis',
  "Should be able to use discerning information retrieval skills to gather, sift, synthesise and organise material on their own and to judge its significance critically.",
  "Look for discerning searching, synthesis and critical judgement of material.",
  "you should be able to find, sift, combine and organise material with discernment on your own and judge critically how much it matters.")
r('4.16.b7', 'excellent', ['demonstrate', 'be'], 'digital skills and full awareness of their potential',
  "Should show suitable technical and digital skills and full awareness of what they could be used for.",
  "Look for strong digital skills and a full grasp of their possible uses.",
  "you should have suitable technical and digital skills and be fully aware of how they could be used.")
r('4.16.b8', 'excellent', ['identify', 'deploy', 'solve', 'realise'], 'deploying numeracy for creative outputs',
  "Should be able to identify and use several numeracy skills to solve problems and achieve creative outputs.",
  "Look for confident choice and use of numeracy in practical and creative problems.",
  "you should be able to choose and use a range of number skills to solve problems and produce creative work.",
  find='identify and deploy a range of numeracy skills to solve problems and realise creative outputs.')

# ------------------------------------------------------------- 4.17 master's outcomes (no rungs)
def m(i, dom, verbs, about, para, prac, ben, fw, link, q):
    s(i, type='outcome', rung='none', force='should', level='fheq:7', appliesTo="master's students in Performance", addressee='learner',
      verbs=verbs, about=about, domain=dom, award=MA, para=para, prac=prac, ben=BL['threshold'].replace('your honours degree', 'your master\'s degree').replace('At the minimum standard for ', 'By the end of ') + ben,
      aaw=("Treat this as a master's outcome (should) at FHEQ level 7 (FQHEIS level 11), added to the honours standards for master's study in the subject. "
           "Cite it as (" + CITE + i + "). Set it beside the honours excellent rung item " + link + " and the master's descriptor qaa/fheq-2024/" + fw + " with spine:7. "
           "Do not claim it applies to honours graduates or that it sets rungs; the master's list has no threshold, typical or excellent split."),
      aad=("Raise it when a master's student or a postgraduate team asks how master's work differs from honours. Put it in plain words, second person for a student. "
           "Ask: " + q + " Avoid presenting it as an honours expectation."))

m('4.17.b1', 'knowledge', ['demonstrate'], 'systematic, critical grasp of current and emerging directions',
  "Should be able to show a systematic, thorough and critically aware grasp of where practice and research in the field now stand and where they are heading.",
  "Expect master's students to show a systematic, critical grasp of current and emerging directions in the field's practice and research.",
  "you should be able to show a systematic, thorough and critical grasp of where practice and research in your field are now and where they are going.",
  '4.17.b1', '4.14.b1', "Which current development in the field could you explain and critique to a specialist?")
m('4.17.b2', 'understanding', ['evaluate', 'apply'], 'evaluating research to apply knowledge originally',
  "Should be able to evaluate current research and advanced scholarship and use what they know in original ways in the field.",
  "Expect critical evaluation of current research and scholarship, applied with originality.",
  "you should be able to evaluate current research and advanced scholarship and use what you know in original ways.",
  '4.17.b4.1', '4.15.b4', "Where has your reading of recent research changed what you made or argued?")
m('4.17.b3', 'generic-skill', ['evaluate', 'demonstrate', 'dealing'], 'method, self-direction and originality with complex problems',
  "Should be able to evaluate suitable methods and show self-direction and originality in tackling complex problems in practice or research.",
  "Expect students to choose and justify methods and to tackle complex problems with self-direction and originality.",
  "you should be able to weigh up methods and tackle complex problems in practice or research on your own initiative and in original ways.",
  '4.17.b6', '4.16.b1', "Why did you choose the method you used, and what else did you rule out?")
m('4.17.b4', 'generic-skill', ['create', 'communicate'], 'new insight communicated to all audiences',
  "Should be able to create new insight in their field and communicate conclusions clearly to specialists and non-specialists.",
  "Expect new insight and clear communication of conclusions to specialist and general audiences.",
  "you should be able to create new insight in your field and explain your conclusions clearly to experts and non-experts.",
  '4.17.b5', '4.16.b1', "How would you explain your main finding to someone outside the field?")
m('4.17.b5', 'subject-skill', ['complete'], 'a major practice or research project',
  "Should be able to complete a major piece of practice or a substantial research project, grounded in a thorough understanding of the discipline.",
  "Build in a major practice piece or substantial research project grounded in deep knowledge of the discipline.",
  "you should be able to complete a major piece of practice or a substantial research project, built on a thorough understanding of your discipline.",
  '4.17.b2', '4.15.b4', "What will your major project add that a shorter piece could not?")

# ------------------------------------------------------------- gradeOf: inferred (the issuer does not pair the lists)
GRADE = {}
for _r in ROWS:
    th, ty, ex = _r[2:5]
    if ty and th:
        GRADE[ty] = th
    if ex and ty:
        GRADE[ex] = ty

TH = {'1.17': 'theme:edi', '1.24': 'theme:accessibility'}

S5 = dict(
    levels=[
        dict(id='fheq:6', role='cites', locator='D1, 2.2 ("FHEQ Levels 6 and 7"); 4.2 to 4.16 (honours)'),
        dict(id='fqheis:10', role='cites', locator='D1, 2.2 ("FQHEIS 10 and 11")'),
        dict(id='fheq:7', role='cites', locator='D1, 2.2; 2.11 (integrated master\'s); 4.17'),
        dict(id='fqheis:11', role='cites', locator='D1, 2.2; 2.11'),
        dict(id='fheq:4', role='inferred: CertHE named as an exit award (D1, 2.12); level from std:doc:qaa-fheq-2024-framework S5 (Table 1)', locator='D1, 2.12'),
        dict(id='fheq:5', role='inferred: DipHE named as an exit award (D1, 2.12); level from std:doc:qaa-fheq-2024-framework S5 (Table 1)', locator='D1, 2.12'),
        dict(id='spine:6', role='inferred: the reference framework step for the honours standards (std:ref:uk-framework R2, R8)', locator='D1, 4.8 to 4.16'),
        dict(id='spine:7', role='inferred: the reference framework step for the master\'s outcomes (std:ref:uk-framework R2, R8)', locator='D1, 4.17'),
    ],
    crosswalks=[
        dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.2: "FHEQ Levels 6 and 7/FQHEIS 10 and 11")'),
        dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.11: "(FHEQ Level 7; FQHEIS Level 11)")'),
        dict(**{'from': 'fheq:6'}, to='cqfw:6', relation='compares-with', basis='inferred from std:doc:qaa-fheq-2024-framework S5 (its 2.24); the statement does not name the CQFW (Part E)'),
    ])

S6 = [
    dict(id='theme:edi', role='carries', carriedIn=['front matter', '1.3', '1.13', '1.14', '1.16', '1.17', '1.18', '1.19', '1.20', '1.27', '1.28', '1.33', '2.1', '2.7', '2.17', '2.19', '3.6', '3.13', '4.7']),
    dict(id='theme:accessibility', role='carries', carriedIn=['front matter', '1.3', '1.13', '1.16', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '1.28', '1.29', '1.30', '1.34', '3.6', '4.7']),
    dict(id='theme:esd', role='carries', carriedIn=['front matter', '1.3', '1.10', '1.16', '1.31', '1.32', '1.33', '1.34', '4.7', '4.8', '4.11', '4.14']),
    dict(id='theme:enterprise', role='carries', carriedIn=['front matter', '1.3', '1.16', '1.33', '1.35', '1.36', '1.37', '1.38', '2.14', '2.18', '2.20', '4.7']),
    dict(id='theme:generative-ai', role='carries', carriedIn=['1.15']),
]

S7 = [
    dict(rel='supersedes', target='std:doc:qaa-dance-drama-and-performance-2019-benchmarks (not held)', note='the fourth edition, 2019, named in section 6; earlier editions 2015, 2007 and 2002 are named there too'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the degree outcome classification descriptions, cited in 4.3 as Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ levels 6 and 7 (2.2, 2.11)'),
    dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS levels 10 and 11 (2.2, 2.11)'),
    dict(rel='themeReference', target='std:doc:qaa-advancehe-esd-2021-guidance', note='QAA and Advance HE Education for Sustainable Development Guidance (2021), cited in 1.31 and section 5'),
    dict(rel='themeReference', target='std:doc:qaa-enterprise-2018-guidance', note='Enterprise and Entrepreneurship Education guidance, QAA 2018, listed in section 5 only'),
    dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance, including work-based learning (not yet ingested)', note='front matter; 2.17 ("QAA guidance on work-based learning")'),
    dict(rel='refersTo', target='QAA Glossary (not ingested)', note='front matter'),
    dict(rel='refersTo', target='Equality Act 2010 (legislation, not a standards document)', note='1.17'),
    dict(rel='refersTo', target='UN Sustainable Development Goals and the 2030 Agenda; the Theatre Green Book (not standards documents)', note='1.31'),
]

SB1 = [
    "A broad field of established and emerging forms joining practice and theory in studying performance and how it is produced (D1, 1.1, 2.3).",
    "Diversity of provision is a strength: specialist training, single, combined and interdisciplinary courses, from industry-ready to research-led and socially engaged (D1, 1.3, 1.5, 1.6, 2.2).",
    "Embodied and experiential learning is its distinctive way of knowing (D1, 1.9, 3.8).",
    "Creativity and its communication sit at the centre, with critical and creative work feeding each other (D1, 1.7, 1.8, 3.7).",
    "Learning is collaborative: ensembles, companies and group work are typical, balanced with safety and creative risk (D1, 1.12, 1.13, 3.11).",
    "The field's practices are dynamic and contested, open to change and respectful of tradition (D1, 1.4, 2.4, 2.5).",
    "Strongly tied to the creative industries and wider employment through partnerships, placements and portfolio careers (D1, 1.35, 1.38, 2.14 to 2.20).",
    "'Performance' is used inclusively for all of dance, drama and performance in sections 3 and 4 (D1, 3.2, 4.1).",
]

SB2 = [
    dict(theme='theme:edi', inThisSubject="framed through inclusive learning communities and the studio: ethical, non-judgemental conversation about lived realities, centring marginalised voices and histories, no structural disadvantage, the Equality Act 2010, and partners who share the same principles (D1, 1.17 to 1.20, 2.19)",
         statements=['1.17', '3.6', '4.7', '3.3.b11']),
    dict(theme='theme:accessibility', inThisSubject="anticipatory design across studio, classroom, fieldwork and digital work, questioning ableist knowledge, planning for barriers in group and practical work, blended options and fair digital access (D1, 1.21 to 1.30, 1.34)",
         statements=['1.24', '3.6', '4.7']),
    dict(theme='theme:esd', inThisSubject="named sustainability in 1.3 and 1.16; ESD defined with the SDGs, the 2021 guidance and the Theatre Green Book, with economic, social and environmental themes for curricula, and safe, environmentally sustainable practice in each rung (D1, 1.31 to 1.34, 4.8, 4.11, 4.14)",
         statements=['4.7', '4.8.b12', '4.11.b11', '4.14.b11']),
    dict(theme='theme:enterprise', inThisSubject="enterprise and entrepreneurship education for future-ready employability and portfolio careers, authentic assessment, partnerships and operating entrepreneurially; the front matter joins it with employability (D1, 1.35 to 1.38, 2.14, 2.20)",
         statements=['4.7']),
    dict(theme='theme:generative-ai', inThisSubject="generative AI and other new technologies are analysed for their effect on the creative industries and used, with critical reflection and openness, to develop creative material (D1, 1.15)",
         statements=[]),
]

SB3 = dict(
    areas=[
        dict(component='1.11', gloss='six broad strands: practical work, technique, critical studies, technology, communication and collaboration, preparation for employment'),
        dict(component='2.3', gloss='the fields degrees cover: the disciplines and their production, cognate media, practical skill with critical analysis, histories, social contexts and audiences'),
        dict(component='3.2', gloss='eight areas of knowledge and understanding, from practitioners and histories to research methods and interdisciplinarity'),
    ],
    practices=[
        dict(component='3.7', kind='teaching', gloss='varied approaches built round practice and theory together'),
        dict(component='3.8', kind='learning', gloss='experiential and embodied learning as the basis of study'),
        dict(component='3.10', kind='learning', gloss='practical and professional contexts and varied roles'),
        dict(component='3.11', kind='learning', gloss='tutor-led to self-directed learning; group work'),
        dict(component='3.12', kind='teaching', gloss='workshops, rehearsals, productions, studio, lectures, seminars, tutorials, in person and online'),
        dict(component='3.13', kind='assessment', gloss='inclusive, diverse and negotiated assessment as part of learning'),
        dict(component='3.14', kind='assessment', gloss='formats from performance and design outputs to essays, portfolios and dissertations'),
        dict(component='3.15', kind='assessment', gloss='self and peer assessment; course information on assessment'),
        dict(component='3.17', kind='learning', gloss='handbooks on academic practice, support and well-being'),
    ])

SB4 = dict(
    rungs=[
        dict(rung='threshold', leadIn='4.8', award=HON, items=30),
        dict(rung='typical', leadIn='4.11', award=HON, items=24),
        dict(rung='excellent', leadIn='4.14', award=HON, items=24),
    ],
    rungBases=("Each rung is named by a sub-heading (Threshold level, Typical level, Excellent level) and holds three lists, each with its own "
               "lead-in in 'should be able to': subject knowledge and understanding (4.8, 4.11, 4.14), subject-specific skills (4.9, 4.12, 4.15) "
               "and generic and graduate skills (4.10, 4.13, 4.16). Counts: threshold 12, 7 and 11; typical 11, 5 and 8; excellent 11, 5 and 8. "
               "4.2: the minimum threshold, typical and excellent standards shown at the award of honours. 4.3: most students exceed the threshold; "
               "Annex D for the classes. 4.6: the threshold is met when knowledge, understanding, creativity and skill suffice to present performance "
               "or argument; excellent work tends to go past the outcomes. 4.7: outcomes indicative, for single honours, not a checklist."),
    outcomeLists=[
        dict(leadIn='3.3', gloss='thirteen skills students will develop (will; the stem asks courses to enable them, should)', items=13, award=['honours']),
        dict(leadIn='4.17', gloss="five added outcomes for master's study (should), with no rungs", items=5, award=["master's"]),
    ],
    outcomes=[dict(outcome=_r[0], threshold=_r[2] or 'none', typical=_r[3] or 'none', excellent=_r[4] or 'none', basis='inferred', domain=_r[1], award=HON) for _r in ROWS])
SB4A_FULL = []

SB5 = [
    dict(body='professional, statutory and regulatory bodies (PSRBs), in general', says='the statement supports PSRBs on academic standards; courses may consider their requirements; courses with professional and vocational outcomes may need evaluation and accreditation by professional and regulatory bodies (D1, front matter, 2.25)', requirements='not-applicable-by-design: no body named'),
    dict(body='funding and regulatory bodies (unnamed)', says='providers meet the legislative and regulatory requirements these bodies place on them; the statement does not interpret them (D1, front matter)', requirements='not-applicable-by-design: no body named'),
    dict(body='Office for Students', says='in England the statement is not a sector-recognised standard under its regulatory framework (D1, front matter)', requirements='not yet ingested (Part E)'),
    dict(body='Disabled Students Commission', says='listed in section 5 only, with no text in the numbered paragraphs (D1, section 5)', requirements='not yet ingested (Part E)'),
]

SB6 = dict(
    themes=[
        dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=S6[0]['carriedIn'], statements=['1.17', '3.6', '4.7', '3.3.b11']),
        dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=S6[1]['carriedIn'], statements=['1.24', '3.6', '4.7']),
        dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development; 1.31: Education for Sustainable Development (ESD))', carriedIn=S6[2]['carriedIn'], statements=['4.7', '4.8.b12', '4.11.b11', '4.14.b11']),
        dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=S6[3]['carriedIn'], statements=['4.7']),
        dict(id='theme:generative-ai', named='Generative artificial intelligence (AI) and other new technologies', carriedIn=['1.15'], statements=[]),
    ],
    frameworks=[
        dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.2', '2.11']),
        dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.2', '2.11']),
    ],
    bodies=[
        dict(body='professional, statutory and regulatory bodies (PSRBs)', citedIn=['front matter', '2.25']),
        dict(body='funding and regulatory bodies (unnamed)', citedIn=['front matter']),
        dict(body='Office for Students (regulatory framework, England)', citedIn=['front matter']),
        dict(body='Disabled Students Commission', citedIn=['section 5']),
    ],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.3'], role='descriptions of the four honours classes (1st, 2.1, 2.2, 3rd) that providers should refer to when setting evidence of achievement'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='the QAA and Advance HE Education for Sustainable Development Guidance (2021)', citedIn=['1.31', 'section 5'], role='a reference for creating ESD curricula'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='QAA (2018) Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers', citedIn=['section 5'], role='listed as a further resource for the enterprise theme'),
        dict(document='QAA Quality Code, Advice and Guidance (not yet ingested: Part E)', named='Advice and Guidance to support the Quality Code; QAA guidance on work-based learning', citedIn=['front matter', '2.17'], role='course design, teaching, external expertise, monitoring; placement learning'),
        dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
    ])

B1 = [
    dict(slug='performance-inclusive', definition="used inclusively in sections 3 and 4 for activity, practical or theoretical, across all of dance, drama and performance and associated courses (D1, 3.2, 4.1)", beneficiaryDefinition='any dance, drama, theatre or performance work, practical or written', scopeNote='capitalised as Performance in the text', category='unknown', practices=['performing arts']),
    dict(slug='education-for-sustainable-development', definition='the process of creating curricula, with subject content and pedagogy, that support sustainable development (D1, 1.31)', beneficiaryDefinition='learning that helps you act for a sustainable future', scopeNote='the section is headed Sustainability', category='unknown', practices=['education']),
    dict(slug='threshold-typical-excellent', definition='the three rungs of standards: the minimum shown at award, the typical and the excellent (D1, 4.2, 4.6)', beneficiaryDefinition='the minimum, the usual and the highest standard for your honours degree', scopeNote='each rung has three lists in 4.8 to 4.16', category='unknown', practices=['education']),
]
B2A = [
    dict(concept='performance-inclusive', form="'Performance'", lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='education-for-sustainable-development', form='Education for Sustainable Development (ESD)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='threshold-typical-excellent', form='Threshold level; Typical level; Excellent level', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
]
B4 = []; B5 = []

D3 = [
    dict(source='QAA Subject Benchmark Statement: Dance, Drama and Performance (2019, fourth edition)', why='the edition this one supersedes, for the change comparison'),
    dict(source='QAA Quality Code Advice and Guidance: Work-based Learning', why='cited in 2.17 for placement learning; not ingested'),
]

E = [
    'Rungs: three, each named by a sub-heading and split into three lists with their own lead-ins (subject knowledge and understanding; subject-specific skills; generic and graduate skills), 30, 24 and 24 items. Psychology has one list per rung. SB4 leadIn names the first list of each rung (4.8, 4.11, 4.14); the other lead-ins are in rungBases.',
    'Rung force: every rung lead-in reads "should be able to" (4.14: "It is expected that ... graduates should be able to demonstrate"), so all 78 rung items carry should, the issuer\'s own word, not threshold. 4.2 calls the threshold the minimum.',
    'The rung lists are not parallel (threshold 12, 7, 11; typical 11, 5, 8; excellent 11, 5, 8). gradeOf links are all inferred from plain content matches: 22 typical-to-threshold and 24 excellent-to-typical links (the ROWS table in run-src). For P3.',
    '4.11.b10 and 4.14.b10 join the two threshold items 4.8.b10 (interdisciplinary elements) and 4.8.b11 (other disciplines); gradeOf points to 4.8.b10 only, and 4.8.b11 has no counterpart above.',
    'Unmatched items: threshold 4.9.b3 (records), 4.9.b4 (describe and evaluate events), 4.9.b7 (space), 4.10.b2 (adaptability), 4.10.b3 (risk), 4.10.b7 (communication), 4.10.b10 (project management) have no typical or excellent counterpart; typical 4.12.b1 and 4.13.b2 first appear above the threshold.',
    'Domains on the rungs are by outcome row: rows 1 to 5 of each knowledge list as knowledge, rows 6 to 12 as understanding, though the typical and excellent items read as "engagement"; 4.9.b2 opens with "understand" but is a skill list item (subject-skill). Generic skills at fheq:6; master\'s generic items at fheq:7.',
    "Master's: 4.17 lists five added outcomes for master's study (should), with no rungs; recorded as outcome items at fheq:7, award master's. A new pattern against Psychology. 4.17.b5 reads \"complete of a major piece\" (issuer's typo, kept in source).",
    'Outcome list 3.3: thirteen items under "Students will:" after a stem that says courses "should typically be designed to enable" the skills; items recorded with will. The stem\'s should sentence is not cut as its own record: 3.3 is also a reference in 3.1 ("paragraphs 3.2 and 3.3").',
    'Obliging words outside the five: 3.4 "are expected" recorded as describes; 2.24 "are required" recorded as must; 2.8, 2.9 and 4.14 "it is expected that" recorded with will or should as the sentence gives. Not cut: 1.17 "collective responsibility to embed", 1.28 "requires access" and "is crucial", 2.5 "It is vital that", 4.6 "It is important that" (inside a cut record), 1.27 "will see themselves reflected" (inside a noun clause).',
    'Plain-present provider norms, not statements (template open point 5): 1.13, 1.16, 1.20 (committed to), 1.21, 1.22, 1.25, 1.26, 1.29, 1.30, 1.34, 1.35, 1.37, 1.38, 2.1, 2.13, 2.15, 2.17, 2.22, 2.26, 3.2, 3.13, 3.14, 3.15 (course information list), 3.17.',
    'Not statements, judged: 1.11, 1.18 and 2.2 to 2.3 lists (descriptive), 1.33 (suggestions), 3.12 and 3.14 list items (typical modes and formats), 2.11, 2.12, 2.21 and 2.25 (may), 4.1, 4.4 and 4.5 (framing; 4.5 the typical goal).',
    'Recut by find (skeleton spans ran on into the next heading): 4.8.b12, 4.10.b11, 4.11.b11, 4.12.b5, 4.13.b8, 4.14.b11, 4.15.b5, 4.16.b8; and cut to their obliging sentence: 1.17, 2.24, 3.1, 3.4, 3.12, 3.15, 3.16, 4.7.',
    'Themes: the four named in 1.3 and 1.16 (sustainability, not ESD, in the body; ESD in the front matter and 1.31). Generative AI is a paragraph (1.15) inside Characteristics, not a section; recorded as theme:generative-ai. Employability is joined with enterprise in the front matter, under theme:enterprise.',
    'Frameworks: FHEQ and FQHEIS levels 6 and 7 / 10 and 11 are named in 2.2 and 2.11; 4.3 names The Frameworks for Higher Education Qualifications only for Annex D. The front matter names the Quality Assessment Framework for Wales and Scotland\'s Quality Enhancement Framework, which are quality frameworks, not qualification frameworks. CQFW not named; fheq:6 to cqfw:6 recorded as inferred.',
    'Bodies: PSRBs and funding and regulatory bodies are named only in general; the Office for Students in the front matter; the Disabled Students Commission only in section 5. None of their requirements is ingested.',
    'Inferred subject codes (P3 to confirm; held back from lookup): hecos 100708 stage design (for "scenography and theatre design"), hecos 100710 community theatre (for "applied and social theatre"), hecos 100700 theatre production (for production in 2.3). Dance theatre and writing for performance have no matching HECoS term.',
    'Awards: honours is the award of the rungs; the scope (1.2) covers taught postgraduate degrees, and 2.11 integrated master\'s at FHEQ 7 and FQHEIS 11; awardsCovered records both. CertHE and DipHE (2.12) are exit awards; fheq:4 and fheq:5 inferred.',
    'Annex D is cited in 4.3 without a date; linked to its current home in std:doc:qaa-fheq-2024-framework (SL6).',
    'Other references: Equality Act 2010 (1.17), UN SDGs and the 2030 Agenda and the Theatre Green Book (1.31) are not standards documents; recorded in S7 only.',
    'S9 commentary not researched in P1.',
    'Licence: QAA copyright; the document gives no re-use terms in its text.',
]
