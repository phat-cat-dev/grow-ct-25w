# Judgement fields for run 0083, QAA Subject Benchmark Statement: Agriculture, Rural Environmental Sciences, Animal Studies,
# Consumer Science, Forestry, Food, Horticulture and Human Nutrition (April 2024). std. Built by tools/bm_build.py.
# Keys are S4 ids under qaa/<slug>/. Rung tables in 4.2 list each outcome once under three column lead-ins: the threshold record
# keeps the skeleton id 4.2.b<n>; the typical and excellent records sit on the same span as 4.2.b<n>.typical and 4.2.b<n>.excellent.
import json as _json, os as _os

HON = "bachelor's with honours"
SLUG = 'agriculture-rural-environmental-sciences-animal-studies-consumer-science-forestry-food-horticulture-and-human-nutrition-2024'
# the builder is run from the standards folder (BM-BRIEF); the skeleton and held text are read from there
_DIR = _os.path.join(_os.getcwd(), 'ingest-std-qaa-' + SLUG.rsplit('-', 1)[0] + '-2024-benchmarks')
_SK = _json.load(open(_os.path.join(_DIR, 'run-src/bm-skel.json'), encoding='utf-8'))
_NORM = open(_os.path.join(_os.path.dirname(_DIR), 'stan/core/qaa/benchmarks', SLUG + '.norm.txt'), encoding='utf-8').read()
_SPAN = {c['id'].split('/')[-1]: c['span'] for c in _SK['candidateStatements']}

CITE = 'QAA (2024) Agriculture ... Human Nutrition Subject Benchmark Statement'

META = dict(
    run='0083', p1='2026-10-03 16:15',
    title='Subject Benchmark Statement Agriculture, Rural Environmental Sciences, Animal Studies, Consumer Science, Forestry, Food, Horticulture and Human Nutrition',
    heading='Subject Benchmark Statement: Agriculture, Rural Environmental Sciences, Animal Studies, Consumer Science, Forestry, Food, Horticulture and Human Nutrition (QAA, April 2024)',
    edition='April 2024', published='2024-04',
    status='current',
    supersedes='the fourth edition, Agriculture, Horticulture, Forestry, Food, Nutrition and Consumer Sciences (2019), as the back matter states; this is the fifth edition',
    subjects=[
        dict(scheme='cah', code='CAH06-01', label='agriculture, food and related studies', basis='inferred'),
        dict(scheme='hecos', code='100517', label='agriculture', basis='inferred'),
        dict(scheme='hecos', code='100529', label='horticulture', basis='inferred'),
        dict(scheme='hecos', code='100520', label='forestry and arboriculture', basis='inferred'),
        dict(scheme='hecos', code='100468', label='countryside management', basis='inferred'),
        dict(scheme='hecos', code='100523', label='animal science', basis='inferred'),
        dict(scheme='hecos', code='100527', label='food science', basis='inferred'),
        dict(scheme='hecos', code='100247', label='nutrition', basis='inferred'),
    ],
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series="QAA Subject Benchmark Statements, the revision with cross-cutting themes; this statement's fifth edition (D1, back cover)",
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what an honours graduate should know, understand and be able to do across a family of "
        "land-based and food subjects: agriculture, horticulture and forestry; rural environmental sciences; animal studies (non-production "
        "animals); and food science, food technology, human nutrition and consumer science. Reach for it when designing, approving, reviewing "
        "or describing an honours course or its outcomes in any of these areas, or when placing a student's work against the threshold, "
        "typical and excellent rungs. It is a sector reference point, not a curriculum, a regulation or a professional body's accreditation standard."),
    summary=("Published by QAA in April 2024 as the fifth edition, the statement covers four subject groupings, each a subject in its own right. "
        "It sets out the context and purposes of the subjects, with the cross-cutting themes of equality, diversity and inclusion, accessibility, "
        "sustainability (education for sustainable development) and enterprise and entrepreneurship education, plus a section on generative AI; "
        "the distinctive features of course design, progression, flexibility, partnership and review; content, teaching and assessment; and the "
        "benchmark standards. The standards are six subject tables (agriculture, horticulture, forestry, rural environmental sciences, animal studies, "
        "and food science, technology, nutrition and consumer science), 76 outcomes in all, each read at three rungs by depth: familiarity and "
        "awareness at threshold, well-founded understanding at typical, deep and full understanding at excellent. Nineteen generic skills in five "
        "groups follow. It covers bachelor's degrees with honours only and points to Annex D of the qualifications frameworks for degree classes. "
        "It names professional and accrediting bodies in general terms and cites the QAA and Advance HE ESD guidance and several neighbouring "
        "benchmark statements."),
    authority='reference: a sector-owned reference point, not a regulatory requirement; a key reference point in Wales and Scotland and part of the quality requirements in Northern Ireland, not a sector-recognised standard in England (D1, front matter)')

S2 = dict(
    governs=("what honours graduates in agriculture, horticulture and forestry, rural environmental sciences, animal studies, and food science, "
             "food technology, human nutrition and consumer science can be expected to know, understand and do, at threshold, typical and excellent "
             "rungs, with generic skills and the context for course design, teaching and assessment"),
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    statedScope=('"The subject areas encompassed by this title are referred to individually and in combination, where appropriate, and are: '
                 'Agriculture, Horticulture and Forestry; Rural Environmental Sciences; Animal Studies; Food Science, Food Technology, Human '
                 'Nutrition and Consumer Science." (D1, 1.2)'),
    statedSubjects=[
        dict(name='Agriculture, Horticulture and Forestry', locator='(D1, 1.2; 2.3 to 2.6; 3.1)', kind='subject grouping',
             codes=[dict(scheme='hecos', code='100517', label='agriculture'), dict(scheme='hecos', code='100529', label='horticulture'),
                    dict(scheme='hecos', code='100520', label='forestry and arboriculture')]),
        dict(name='Rural Environmental Sciences', locator='(D1, 1.2; 2.7; 3.3)', kind='subject grouping',
             codes=[dict(scheme='hecos', code='100468', label='countryside management')]),
        dict(name='Animal Studies', locator='(D1, 1.2; 2.8; 3.5)', kind='subject grouping',
             codes=[dict(scheme='hecos', code='100523', label='animal science')]),
        dict(name='Food Science, Food Technology, Human Nutrition and Consumer Science', locator='(D1, 1.2; 2.9; 2.10; 3.7)', kind='subject grouping',
             codes=[dict(scheme='hecos', code='100527', label='food science'), dict(scheme='hecos', code='100247', label='nutrition')]),
    ])

SECTIONS = {
    '1': 'Context and purposes of an Agriculture, Rural Environmental Sciences, Animal Studies, Consumer Science, Forestry, Food, Horticulture and Human Nutrition Degree',
    '2': 'Distinctive features of an Agriculture, Rural Environmental Sciences, Animal Studies, Consumer Science, Forestry, Food, Horticulture and Human Nutrition Degree',
    '3': 'Content, structure and delivery',
    '4': 'Benchmark standards',
}
SUB = [('1.1', '1.4', 'Context'), ('1.5', '1.10', 'Equality, diversity and inclusion'), ('1.11', '1.12', 'Accessibility'),
       ('1.13', '1.16', 'Sustainability'), ('1.17', '1.22', 'Enterprise and entrepreneurship education'), ('1.23', '1.23', 'Generative AI'),
       ('2.1', '2.10', 'Design'), ('2.11', '2.12', 'Progression'), ('2.13', '2.13', 'Flexibility'), ('2.14', '2.14', 'Partnership'),
       ('2.15', '2.18', 'Monitoring and review'), ('3.1', '3.8', 'Content'), ('3.9', '3.17', 'Teaching and learning'),
       ('3.18', '3.24', 'Assessment'), ('4.1', '4.1', 'Introduction'),
       ('4.2', '4.2', 'Introduction; Subject knowledge, understanding and skills'), ('4.3', '4.3', 'Generic skills')]

G = {
    '1.1': 'the field-to-fork scope with allied land-based areas; evidence-based solutions in practice',
    '1.2': 'the four subject groupings the statement covers',
    '1.3': 'a practical guide to essentials, not full coverage',
    '1.4': 'economic and social importance; graduates as evidence-informed decision makers from policy to local practice',
    '1.5': 'EDI built into every stage of the student journey',
    '1.6': 'safe, inclusive settings and promoted financial support',
    '1.7': 'unequal access and the duty to break down barriers; widening participation',
    '1.8': 'inclusive recruitment, marketing and flexible entry',
    '1.9': 'support that fits each student; belonging in the course community',
    '1.10': 'the hidden curriculum as a barrier',
    '1.11': 'accessibility as inclusive design of curriculum and experience',
    '1.12': 'risk assessment, proactive adjustment and accessible technology',
    '1.13': 'sustainability as a priority; One Health; more than the environment',
    '1.14': 'ESD as holistic and transformational; the SDGs in the curriculum',
    '1.15': 'curriculum structures for sustainable development; the ESD guidance',
    '1.16': 'practical sustainability topics, from waste to food security',
    '1.17': 'enterprise education for careers and links with external bodies',
    '1.18': 'creative problem-solving, start-ups and a self-determined working life',
    '1.19': 'professional and accrediting bodies and employability',
    '1.20': 'what employers seek in rural environmental sciences',
    '1.21': 'what employers seek in agriculture, horticulture, forestry and animal studies',
    '1.22': 'what employers seek in food science, nutrition and consumer science',
    '1.23': 'generative AI: its effect on the agri-food chain and its responsible use',
    '2.1': 'inclusive design; Universal Design for Learning; student-centred teaching',
    '2.2': 'addressing bias in content; decolonising lens; co-creating content',
    '2.3': 'indicative headings for the course areas',
    '2.4': 'agriculture courses: farming systems, production and economics',
    '2.5': 'horticulture courses: plant science, production, landscapes; graduate roles',
    '2.6': 'forestry courses: woodland management for market and wider benefit',
    '2.7': 'rural environmental sciences courses: multidisciplinary land use and the countryside',
    '2.8': 'animal studies courses: husbandry and welfare of non-production animals',
    '2.9': 'food science, technology and nutrition courses across the supply chain',
    '2.10': 'consumer food choices and how they can change',
    '2.11': 'progression through levels towards the threshold; postgraduate readiness',
    '2.12': 'joint and combined degrees',
    '2.13': 'flexible modes, formats and micro-credentials',
    '2.14': 'co-creation and co-delivery with stakeholders',
    '2.15': 'monitoring, periodic review and the student voice',
    '2.16': 'external reviewers in periodic review',
    '2.17': 'the external examiner system',
    '2.18': 'accreditation by professional and regulatory bodies',
    '3.1': 'content areas in agriculture, horticulture and forestry',
    '3.2': 'that grouping covers section 4 and links to other statements',
    '3.3': 'content areas in rural environmental sciences',
    '3.4': 'rural environmental courses cover section 4; links to other statements',
    '3.5': 'animal studies subdivisions: applied animal science and conservation',
    '3.6': 'animal studies courses cover section 4; other statements to read',
    '3.7': 'content areas in food science, technology, nutrition and consumer science',
    '3.8': 'other statements useful for the food grouping',
    '3.9': 'active, individualised teaching; students as partners',
    '3.10': 'blended learning and the digital divide',
    '3.11': 'staff and students working together on quality',
    '3.12': 'work-based learning and equitable placements',
    '3.13': 'what teaching and learning are',
    '3.14': 'methods left open; outcomes achievable by the methods used',
    '3.15': 'teaching and learning within curriculum design; research-led courses',
    '3.16': 'typical formats of teaching and learning',
    '3.17': 'field observation, practical skills and fieldwork adjustments',
    '3.18': 'assessment strategy, range and choice; peer and self-assessment',
    '3.19': 'student voice in assessment; authentic assessment',
    '3.20': 'assessment strategy and authentic tasks',
    '3.21': 'inclusive assessment and reasonable adjustments',
    '3.22': 'feedback and reflection',
    '3.23': 'examples of authentic assessment',
    '3.24': 'multidisciplinary assessment underpinned by ESD',
    '4.1': 'the three rungs on the honours award',
    '4.2': 'most exceed threshold; Annex D for classes; the six subject tables at three rungs',
    '4.3': 'generic skills on graduating, in five groups',
}
CTYPE = {'3.1': 'area', '3.3': 'area', '3.5': 'area', '3.7': 'area',
         '3.9': 'practice', '3.10': 'practice', '3.12': 'practice', '3.16': 'practice', '3.17': 'practice',
         '3.18': 'practice', '3.20': 'practice', '3.21': 'practice', '3.22': 'practice', '3.23': 'practice', '3.24': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1 and S2'),
    dict(number='section headings 1 to 4', heading='the four section heading lines', kind='other: heading lines'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for S7 and SB6'),
    dict(number='6', heading='Membership of the Advisory Group', kind='other: back matter, read for S8 (editions)'),
]

P = {}
def s(i, **k):
    P[i] = k

# ------------------------------------------------------------------ obliging and outcome paragraphs (sections 1 to 4)
NA_P = ('n/a', 'a duty on the provider or course team; the student meets its effect, not a standard to reach')
s('1.5', type='expectation', rung='none', force='should', level='none', appliesTo='courses in these subjects', addressee='provider',
  verbs=['embedded'], about='EDI through the whole student journey', domain='none', award=HON,
  para="Courses aim for graduates who are culturally aware global citizens and have had fair access and opportunity; EDI is integral to the courses and should be built into every stage, from first interest and entry through to graduation, work and after.",
  prac="Treat EDI as part of the course, not an add-on: it should run through recruitment, transition, study, graduation and the move into work.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation on the course team and institution, not a student outcome: EDI built into each stage of the student journey. It holds for honours courses in all four groupings. Cite it as {CITE}, para 1.5. Do not present it as a legal duty; set it beside 1.6, 1.10, 2.1 and 3.21 in this document.",
  aad="Raise this with a programme team reviewing recruitment, induction, teaching or careers support. Frame it for staff as an expectation that inclusion reaches every stage, not one module. Ask: 'At which stage of the student journey is inclusion weakest in your course, and what evidence shows it?' Do not hand this to a student as something they must achieve.")
s('1.6', type='expectation', rung='none', force='should', level='none', appliesTo='providers and their institutions', addressee='provider',
  verbs=['commit', 'promoted'], about='inclusive settings and financial support', domain='none', award=HON,
  para="Providers commit to safe, inclusive and supportive settings that value diversity; related help, such as bursaries and scholarships, should be open and made known to applicants and students.",
  prac="Make sure bursaries, scholarships and similar support are accessible and actively publicised to applicants and current students, alongside a safe, inclusive environment.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation on the provider: inclusive environments, with financial support made accessible and publicised. It is about the institution, not a level of study. Cite it as {CITE}, para 1.6. Do not phrase it as a student outcome; set it beside 1.5 and 1.7 to 1.9 (the plain-present EDI commitments).",
  aad="Raise this when a team or a student services colleague asks how financial and inclusion support should reach students. Put it to staff as a duty to promote what exists, not only to have it. Ask: 'How would an applicant from a low-income background find out about your bursaries before they apply?' Avoid presenting it to a student as their responsibility.")
s('1.10', type='expectation', rung='none', force='should', level='none', appliesTo='course teams', addressee='provider',
  verbs=['consider'], about='the hidden curriculum', domain='none', award=HON,
  para="Course teams should think about the hidden curriculum, the unwritten lessons students pick up beyond formal teaching, since unequal access to it can hold some students back.",
  prac="Look at what students learn implicitly about the discipline's norms and values; where some students reach that knowledge later or less fully than others, it becomes a barrier to address.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation on course teams to consider the hidden curriculum as a barrier to success. It applies to honours courses in these subjects. Cite it as {CITE}, para 1.10. Do not claim it sets an outcome for students; set it beside 1.5, 1.9 and 2.2 in this document.",
  aad="Raise this with a team reviewing why some groups of students do less well, or planning induction. For staff, put it as the unwritten expectations that some students learn late. Ask: 'Which unspoken norms in your course, such as how fieldwork or placements are found, favour students who already know the sector?' Avoid lecturing a student about it; it is a duty on the team.")
s('1.14', type='expectation', rung='none', force='should', level='none', appliesTo='curriculum and module design', addressee='provider',
  verbs=['integrated'], about='the SDGs across the curriculum', domain='none', award=HON,
  para="Sustainability and sustainable development are holistic ideas with global reach; following UNESCO's 2019 account of ESD as transformational education, an understanding of the UN Sustainable Development Goals is central, and where it fits the SDGs should be woven through the curriculum.",
  prac="Treat sustainability as holistic when building curricula and modules, and, where it fits, weave the SDGs through the whole curriculum rather than one unit.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation on curriculum design: the SDGs integrated across the curriculum where appropriate, with ESD defined after UNESCO (2019). Cite it as {CITE}, para 1.14. Do not present the SDGs as a mandatory checklist; set it beside 1.15, 3.24 and the QAA and Advance HE ESD guidance (std:doc:qaa-advancehe-esd-2021-guidance).",
  aad="Raise this when a team maps sustainability content or plans a curriculum review. Frame it for staff as integration across the course, not a single sustainability module. Ask: 'Which SDGs does your course touch, and where do students meet them more than once?' Avoid reading out the UNESCO definition at length.")
s('1.15', type='expectation', rung='none', force='should', level='none', appliesTo='providers', addressee='provider',
  verbs=['refer'], about='using the ESD guidance', domain='none', award=HON,
  para="Sustainable development in higher education means building curriculum structures and content that support it; to include sustainable principles, providers should consult the QAA ESD guidance on key competencies, outcomes and assessment.",
  prac="When building sustainability into outcomes and assessment, use the QAA and Advance HE ESD guidance on key competencies, learning outcomes and assessment.",
  ben=NA_P,
  aaw=f"Treat this as a should-level pointer for providers to the QAA and Advance HE Education for Sustainable Development Guidance (std:doc:qaa-advancehe-esd-2021-guidance). Cite it as {CITE}, para 1.15. Do not claim the guidance is binding; set it beside 1.14 and 3.24 here and the guidance's own competencies.",
  aad="Raise this when a team writes outcomes or assessments on sustainability and asks where to start. Point staff to the ESD guidance's competencies as the reference. Ask: 'Which of the guidance's competencies do your current outcomes already assess?' Avoid presenting the guidance as a student requirement.")
s('1.23', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='courses and graduates in these subjects', addressee='both',
  verbs=['analysed', 'used', 'recognise'], about='generative AI and its responsible use', domain='generic-skill', award=HON,
  para="Generative AI and related technologies should be examined for their effect on the agri-food supply chain and used, with critical reflection, for varied purposes; being open about their use allows judgements on what is appropriate, and graduates should see both the opportunities and the need for responsibility.",
  prac="Teach students to analyse what generative AI does to the agri-food supply chain and to use it reflectively and transparently; graduates should recognise both its benefits and the need for responsible use.",
  ben="You should be able to see where AI and similar tools can help, judge their effect on the food and farming supply chain, use them openly and with care and understand why responsible use matters.",
  aaw=f"Treat this as a should-level expectation with two parts: a course duty to analyse and use generative AI critically, and a graduate outcome of recognising its opportunities and the need for responsible use, at honours (FHEQ level 6). Cite it as {CITE}, para 1.23. Do not present it as an AI policy or academic integrity rule; set it beside generic skill 4.3.b17 here and the FHEQ honours descriptor qaa/fheq-2024/4.15.b7.",
  aad="Raise this when a student asks whether or how to use AI tools, or a team plans guidance on AI. To a student, put it plainly: you are expected to use these tools openly and think about their effects; to staff, as both a teaching topic and a practice. Ask: 'Where has an AI tool helped your work, and where would its use be hard to justify?' Avoid treating it as a ban or as permission without limits.")
s('2.1', type='expectation', rung='none', force='should', level='none', appliesTo='courses, components and learning experiences', addressee='provider',
  verbs=['ensure', 'embedded'], about='inclusive course design', domain='none', award=HON,
  para="Courses, their parts and each learning experience should be designed inclusively; providers draw on frameworks such as Universal Design for Learning, leaders consider their students' profiles so outcomes are inclusive, and graduate skills are built in throughout with student-centred teaching.",
  prac="Design inclusively from the start, using a framework such as UDL, checking programme outcomes against your actual and likely students, and building graduate skills in throughout.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation on course design: inclusive design of courses and learning experiences, with UDL named as one framework. Cite it as {CITE}, para 2.1. Do not claim UDL is required; set it beside 1.5, 2.2 and 3.21 in this document.",
  aad="Raise this when a team is designing or revalidating a course. Frame it for staff as design for the whole likely cohort, not adjustments after the event. Ask: 'Who among your students would find your programme outcomes hardest to reach, and why?' Do not present it to students as their task.")
s('2.5', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='horticulture graduates', addressee='learner',
  verbs=['equipped', 'advise', 'apply'], about='what horticulture graduates are ready for', domain='subject-skill', award=HON,
  para="Horticulture courses cover plant biology and soils, horticultural practice and the management of production systems and landscapes, with sustainability throughout; graduates will be ready to advise and to apply their skills to industry standards in production, landscape and amenity horticulture and research.",
  prac="Prepare horticulture graduates to advise on and apply their skills to industry standard in roles such as production horticulture, landscape management, amenity horticulture and research.",
  ben="If you study horticulture, you will be ready to give advice and use your skills to industry standard in work such as growing crops, managing landscapes, amenity horticulture or research.",
  aaw=f"Treat this as a will-level expected outcome for horticulture honours graduates (FHEQ level 6): readiness to advise and apply skills to industry standards. Cite it as {CITE}, para 2.5. Do not claim it guarantees employment or a professional licence; set it beside the horticulture rung items 4.2.b13 to 4.2.b22 and the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3.",
  aad="Raise this when a horticulture student asks what the degree prepares them for. Put it plainly to a student: you will be able to advise and work to industry standard; to staff, as an outcome their placements and practicals should evidence. Ask: 'Which industry standard have you worked to, and could you advise someone on it?' Avoid promising particular jobs.")
s('2.11', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='undergraduates in these subjects', addressee='learner',
  verbs=['progress', 'include'], about='progression towards the threshold', domain='none', award=HON,
  para="Students will move from level to level under their institution's rules, each level building towards the threshold subject-specific and generic skills; this will usually mean completing and gaining credit for all learning and assessment, practical and work-related parts included; a second-class degree or better is expected to prepare a graduate for postgraduate study, though each provider sets its own entry rules.",
  prac="Build each level towards the threshold skills of section 4; credit for all learning and assessment, practical and work-related parts included, will usually be needed; a 2.2 or better is expected to fit a graduate for postgraduate study.",
  ben="As you move through your course, each year builds towards the minimum subject and general skills you need at the end, and you will usually have to complete and gain credit for everything, practical and work-related parts included. With a second-class result or better you can expect to be ready for postgraduate study, though each course sets its own entry rules.",
  aaw=f"Treat this as a will-level description of progression: each level builds towards the threshold standards of section 4, with full credit usually required, and a second-class degree expected to equip a graduate for postgraduate study. Cite it as {CITE}, para 2.11. Do not claim it sets entry rules for postgraduate courses; set it beside 4.1 and 4.2 here and the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3.",
  aad="Raise this when a student asks whether every module counts or whether their result will let them go on to postgraduate study. To a student, say that each year builds towards the final minimum and that a second-class result usually opens postgraduate study; to staff, frame it as level-by-level design. Ask: 'Which practical or work-based parts have you still to complete for credit?' Avoid promising entry to a particular postgraduate course.")
s('2.12', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students on joint or combined degrees', addressee='learner',
  verbs=['achieve', 'add'], about='joint and combined degrees', domain='none', award=HON,
  para="Students taking these subjects in a joint or combined degree will reach the core subject and generic skills and add others from their other subject, with room for interdisciplinary study where the disciplines overlap.",
  prac="On joint or combined degrees, secure the core subject-specific and generic skills, and let the other subject add its own; use the overlap for interdisciplinary work.",
  ben="If you study one of these subjects alongside another, you will gain the core skills of this subject and others from your second subject, and you may find chances to work across both.",
  aaw=f"Treat this as a will-level expectation for joint and combined honours: the core skills of this statement plus those of the other subject. Cite it as {CITE}, para 2.12. Do not claim joint students must meet every item of every subject table; set it beside 4.2 and 4.3 here and the FHEQ honours descriptor qaa/fheq-2024/4.15.i1.",
  aad="Raise this when a joint-honours student or their team asks which standards apply. To a student, put it as: you will cover the core of this subject plus your other subject's skills; to staff, as a core set rather than the whole table. Ask: 'Which core outcomes of this subject does your joint pathway cover, and where?' Avoid implying they must meet every single item.")
s('2.14', type='expectation', rung='none', force='should', level='none', appliesTo='course teams and providers', addressee='provider',
  verbs=['considered', 'harnessing'], about='co-creation and co-delivery', domain='none', award=HON,
  para="Co-creating and co-delivering teaching and learning should be considered as a way to draw on prospective and current students, graduates, staff, accreditors and employers to improve courses.",
  prac="Consider co-creation and co-delivery with students, graduates, accreditors and employers as a route to course improvement.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation that course teams consider co-creation and co-delivery with stakeholders. Cite it as {CITE}, para 2.14. Do not claim co-delivery is required; set it beside 2.2 and 3.11 in this document.",
  aad="Raise this when a team plans a review or new module and asks whom to involve. Frame it for staff as an option to weigh seriously. Ask: 'Which stakeholders, such as employers or recent graduates, have shaped this course, and how?' Avoid presenting it to a student as a duty.")
s('2.16', type='expectation', rung='none', force='will', level='none', appliesTo='providers in periodic review', addressee='provider',
  verbs=['use', 'ensure'], about='external reviewers in periodic review', domain='none', award=HON,
  para="Externality is essential to UK quality assurance; providers will use external reviewers in periodic review to give an outside view of proposed changes and to make sure threshold standards are met and content suits the subject.",
  prac="Include external reviewers in periodic review to test proposed changes, confirm the threshold standards are met and check that content fits the subject.",
  ben=NA_P,
  aaw=f"Treat this as a will-level statement of provider practice: external reviewers in periodic review, partly to confirm threshold standards. Cite it as {CITE}, para 2.16. Do not present it as a student outcome or as the external examiner role (2.17 describes that); set it beside 2.15 and 2.17 in this document.",
  aad="Raise this with a team preparing a periodic review. Frame it for staff as the external check that the threshold rungs are met. Ask: 'Which external reviewer will see your threshold evidence, and what will they compare it with?' Avoid presenting it to students.")
s('3.4', type='expectation', rung='none', force='will', level='none', appliesTo='rural environmental sciences courses', addressee='provider',
  verbs=['include'], about='rural environmental courses cover section 4', domain='none', award=HON,
  para="Courses in rural environmental sciences will cover the knowledge, understanding, skills and expertise set out in section 4; the area links with agriculture, horticulture and forestry and with the Earth sciences, geography and biosciences statements.",
  prac="Map a rural environmental sciences course against the section 4 table and generic skills; read it alongside the earth sciences, geography and biosciences statements.",
  ben=NA_P,
  aaw=f"Treat this as a will-level statement that rural environmental sciences courses include what section 4 sets out. Cite it as {CITE}, para 3.4. Do not claim other statements apply as standards here; set it beside the rural environmental sciences rung items 4.2.b33 to 4.2.b42 and std:doc:qaa-earth-sciences-environmental-sciences-and-environmental-studies-2022-benchmarks.",
  aad="Raise this when a rural environmental sciences team maps its curriculum. Frame it for staff as coverage of the section 4 table. Ask: 'Where does your course cover each of the ten rural environmental sciences outcomes?' Avoid treating the neighbouring statements as requirements.")
s('3.6', type='expectation', rung='none', force='will', level='none', appliesTo='animal studies courses', addressee='provider',
  verbs=['include'], about='animal studies courses cover section 4', domain='none', award=HON,
  para="Animal studies courses will cover the knowledge, understanding, skills and expertise in section 4; readers may also find other statements useful, such as events, hospitality, leisure, sport and tourism for equine sports coaching and biosciences for bioveterinary science.",
  prac="Map an animal studies course against the section 4 table; for equine sports coaching or bioveterinary science, read the relevant neighbouring statement as well.",
  ben=NA_P,
  aaw=f"Treat this as a will-level statement that animal studies courses include what section 4 sets out, with other statements suggested as further reading. Cite it as {CITE}, para 3.6. Do not claim the other statements bind these courses; set it beside the animal studies rung items 4.2.b43 to 4.2.b52 and std:doc:qaa-biosciences-2023-benchmarks.",
  aad="Raise this when an animal studies team maps its curriculum or a specialism such as equine coaching. Frame it for staff as coverage of the section 4 table plus optional reading. Ask: 'Which other statement best fits your specialism, and what does it add?' Avoid treating the neighbouring statements as requirements.")
s('3.14', type='expectation', rung='none', force='should', level='none', appliesTo='courses in these subjects', addressee='provider',
  verbs=['taking'], about='outcomes achievable by the methods used', domain='none', award=HON,
  para="The statement does not prescribe teaching or learning methods, but learning outcomes should be reachable through the methods chosen, allowing for any professional body requirements.",
  prac="Choose any teaching methods, provided students can actually reach the learning outcomes through them and any professional body requirements are met.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation that outcomes be achievable through the methods used, with methods left to the course. Cite it as {CITE}, para 3.14. Do not claim it prescribes methods; set it beside 3.9, 3.13 and 3.15 in this document.",
  aad="Raise this when a team aligns methods with outcomes. Frame it for staff as a check of fit, not a list of required methods. Ask: 'For each outcome, which activity gives students the chance to reach it?' Avoid presenting it to students.")
s('3.17', type='expectation', rung='none', force='should', level='none', appliesTo='practical and fieldwork activities', addressee='provider',
  verbs=['made', 'enable'], about='adjustments for practical work and fieldwork', domain='none', award=HON,
  para="Progress in these subjects rests on careful field observation and empirical data, so practical and research skills matter; practical work builds attributes such as leadership, teamwork and problem-solving; activities are designed to be inclusive, and reasonable adjustments should be made so all students can do practical work and fieldwork.",
  prac="Design practical and field activities inclusively and make reasonable adjustments so that every student can take part in practical work and fieldwork.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation on providers: reasonable adjustments so all students can take part in practical work and fieldwork, set in a paragraph on why practical skills matter. Cite it as {CITE}, para 3.17. Do not frame it as a student outcome; set it beside 1.11, 1.12 and 3.21 in this document.",
  aad="Raise this when a team plans fieldwork or labs, or a student with a disability asks about practical work. Frame it for staff as a duty to adjust, and to a student only as what they can expect. Ask: 'What would stop a student using a wheelchair from doing your field course, and what would you change?' Avoid placing the duty on the student.")
s('3.19', type='requirement', rung='none', force='must', level='none', appliesTo='providers', addressee='provider',
  verbs=['promote'], about='student voice in assessment; authentic assessment', domain='none', award=HON,
  para="Providers must take every chance to promote the student voice, including co-designing assessment; to help employability, assessment should reflect life after study.",
  prac="Give students a real say in assessment, including co-design, as a must; and make assessment authentic to post-study life, as a should.",
  ben=NA_P,
  aaw=f"Treat this as a must-level duty on providers to promote the student voice, including assessment co-design, with a should-level expectation of authentic assessment. Cite it as {CITE}, para 3.19. Do not weaken the must or strengthen the should; set it beside 3.18, 3.20 and 3.23 in this document.",
  aad="Raise this when a team reviews its assessment strategy. Frame it for staff as a firm duty to involve students and an expectation of authentic tasks. Ask: 'Where have students helped design an assessment, and which tasks resemble work they will do after graduating?' Avoid presenting it to a student as their own obligation.")
s('3.21', type='expectation', rung='none', force='should', level='none', appliesTo='assessment in these subjects', addressee='provider',
  verbs=['designed', 'facilitates', 'supports', 'linked'], about='inclusive assessment and adjustments', domain='none', award=HON,
  para="Assessment should be inclusive, designed to support learning and success and tied to the stated outcomes or competencies; where fitting, modified or alternative provision with reasonable adjustments should be available.",
  prac="Make assessment inclusive and linked to the stated outcomes, and provide modified or alternative arrangements with reasonable adjustments where appropriate.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation on assessment design: inclusive, linked to outcomes, with reasonable adjustments where appropriate. Cite it as {CITE}, para 3.21. Do not present it as a student outcome; set it beside 1.12, 2.1 and 3.17 in this document.",
  aad="Raise this when a team designs or reviews assessments, or a student asks about alternative arrangements. Frame it for staff as an expectation of inclusive design first and adjustments second. Ask: 'Which of your assessments would need the most adjustment, and could it be designed differently?' Avoid placing the duty on the student.")
s('4.2', find=("The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own "
               "method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education "
               "Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for "
               "bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd."),
  type='expectation', rung='none', force='should', level='fheq:6', appliesTo='providers judging achievement', addressee='provider',
  verbs=['perform', 'refer'], about='evidence of achievement and Annex D', domain='none', award=HON,
  para="Most students will do much better than the minimum threshold; each provider decides what counts as evidence of achievement and should refer to Annex D of the qualifications frameworks, which describes the four honours classes.",
  prac="When deciding how to evidence achievement above threshold, use Annex D's descriptions of the 1st, 2.1, 2.2 and 3rd classes as the common reference.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation on providers to refer to Annex D (std:doc:qaa-fheq-2024-framework, Annex D) when judging achievement, with the statement that most students exceed threshold. Cite it as {CITE}, para 4.2. Do not claim the statement maps its rungs onto degree classes; set it beside 4.1 and the Annex D third-class descriptions such as qaa/fheq-2024/annex-d/summary/r1/3rd.",
  aad="Raise this when a team sets marking criteria or links the rungs to classes. Frame it for staff as a pointer to Annex D, with the mapping theirs to make. Ask: 'How do your marking bands relate to the Annex D descriptions, and where did you decide that?' Avoid telling a student that the typical rung equals a particular class.")

# ------------------------------------------------------------------ 4.2: six subject tables, each item at three rungs on one span
TABLES = {  # first item, last item, table name, short subject name for prose
    'AG': (1, 12, 'Agriculture', 'agriculture'),
    'HO': (13, 22, 'Horticulture', 'horticulture'),
    'FO': (23, 32, 'Forestry', 'forestry'),
    'RE': (33, 42, 'Rural Environmental Sciences', 'rural environmental sciences'),
    'AS': (43, 52, 'Animal Studies', 'animal studies (non-production animals)'),
    'FN': (53, 76, 'Food Science, Technology, Nutrition and Consumer Science', 'food, nutrition and consumer science'),
}
def table_of(n):
    for k, (a, b, t, sn) in TABLES.items():
        if a <= n <= b:
            return t, sn
K, SK = 'knowledge', 'subject-skill'
# n: (domain, verbs, about, X: our paraphrase of the outcome, used in the rung versions)
ITEMS = {
 1: (K, ['underpin'], 'the science behind sustainable production', "the scientific principles and theories, agricultural, animal and environmental, on which sustainable production systems rest"),
 2: (K, [], 'sustainable crops and high-welfare husbandry', "how crops are grown sustainably and how animals are kept to high welfare standards"),
 3: (K, [], "farming's environmental impact", "the effects farming practice has on the agri-environment: landscape, soil, water, air, biodiversity and the climate"),
 4: (K, ['address'], 'sustainable, ethical production systems', "how sustainable, ethical production systems are developed and run to meet a farm's aims, from economic viability and food security to social inclusion, animal health and welfare and environmental gain"),
 5: (K, ['inform'], 'agri-tech and digital data for decisions', "how agri-tech is applied and built into farming, and how digital data can guide management decisions well"),
 6: (K, [], 'environmental, nutrient and waste management', "the way environment, nutrients and waste are managed in sustainable farming systems"),
 7: (K, [], 'agricultural policy and law', "the policy and law that govern farming, land use and the rural economy, including how farmed land, animal welfare and safety at work are regulated"),
 8: (K, [], 'agri-environment schemes', "agri-environment schemes: what they do and how they are applied and fitted into sustainable farming systems"),
 9: (K, [], 'farm business economics and management', "the economic and business management theory and methods that suit sustainable farm businesses"),
 10: (K, [], 'farming, global change and net zero', "farming's part in global environmental change and the practical steps for managing carbon on farms on the way to net zero"),
 11: (SK, ['researching', 'communicate'], 'researching and communicating agricultural issues', "researching agricultural issues and ideas well and putting views across to varied audiences in traditional and digital forms"),
 12: (SK, ['undertaking'], 'safe, lawful practical farm work', "carrying out practical work on a farm safely, lawfully and competently"),
 13: (K, [], 'plant form, physiology and adaptation', "how plants differ in form, make-up, physiology and adaptation"),
 14: (K, ['play'], 'plant biomes and ecosystem roles', "the main plant biomes and the parts plants play in ecosystems"),
 15: (K, [], 'propagation, breeding and plant manipulation', "the science behind propagation and plant manipulation, including breeding, genomic and phenomic methods and growth regulators"),
 16: (K, [], 'managing plant production systems', "running plant production systems for both conservation and commercial ends across many kinds of plant"),
 17: (K, [], 'the science and technology of crop production', "the science and technology on which growing edible and ornamental crops depends"),
 18: (K, ['achieve'], 'factors in sustainable crop production', "why social, economic and environmental factors matter for sustainable growing, supply chains and circular economies"),
 19: (K, [], 'landscape management', "how varied landscapes are managed and kept up for environmental horticulture"),
 20: (SK, ['evaluating', 'make'], 'evaluating practice and recommending change', "appraising current commercial horticultural practice and, where it fits, proposing changes towards a more sustainable future"),
 21: (K, [], 'horticultural policy, law and safety', "the policy, rules, law, ethics and health and safety guidance that apply to growing and manipulating plants, horticultural practice and landscape upkeep"),
 22: (K, [], 'horticulture at home and abroad', "horticultural practice in the UK and worldwide, taking in gender equity, socio-economic conditions and public worries about sustainable land use and growing"),
 23: (K, ['managing'], 'the science and commerce of forest management', "the scientific and commercial grounds for managing trees and forests"),
 24: (K, [], 'how forests differ', "how forests vary, globally and locally, in make-up, structure, productivity and function"),
 25: (K, ['influence'], 'processes shaping forests', "the physical and ecological processes that shape where natural, semi-natural and managed forests occur and what they contain"),
 26: (K, ['providing'], 'forest ecosystem services', "what forests contribute through provisioning, supporting and regulating ecosystem services"),
 27: (K, ['balancing', 'achieve'], 'balancing aims in forest management', "why weighing social, economic and environmental aims together matters for managing forests sustainably"),
 28: (K, ['maximise'], 'the benefits of forests', "how forest management can draw the most benefit for the economy, health, well-being and the landscape"),
 29: (K, [], 'long horizons and planning in forestry', "the long timescales of forestry and why planning matters"),
 30: (K, ['increasing'], 'forest resilience', "ways of making forests more resistant and resilient to climate change, pests and diseases"),
 31: (K, [], 'forestry law and policy', "the social, legal and policy setting for forestry in the UK and internationally"),
 32: (SK, ['manage', 'encourage'], 'risk and a safety culture', "managing risk and fostering a culture of health and safety"),
 33: (K, ['limiting'], 'the rural environment and its limits', "the physical and ecological features of the countryside and what constrains its development"),
 34: (K, ['applied'], 'applied ecology', "ecological principles applied to communities of people, plants, animals and microbes, and the intricate ecology of landscapes from natural to near-natural and managed"),
 35: (K, ['underpinning'], 'principles behind rural industries', "the economic and biological principles behind the different rural industries and settings"),
 36: (K, [], 'wildlife and landscape conservation', "the principles of conserving wildlife and landscape, seen in past, present and future contexts"),
 37: (K, ['impact'], 'climate change in the countryside', "the principles of climate change, its likely effects on the countryside and the steps needed to mitigate and adapt"),
 38: (K, ['managing'], 'social and ethical factors in rural management', "the key social, cultural and ethical considerations in managing the countryside"),
 39: (K, [], 'rural law, planning and agencies', "the law, planning and policy that apply to the countryside, and what statutory, advisory and non-governmental bodies are responsible for"),
 40: (K, [], 'conflicts and trade-offs in the countryside', "the clashing interests and compromises found in the rural economy and environment"),
 41: (K, ['supported', 'develop', 'manage'], 'supporting sustainable rural development', "how rural businesses, communities and other parties can be helped to develop and look after the countryside sustainably"),
 42: (K, ['managing', 'evaluating', 'monitoring'], 'GIS, remote sensing and monitoring', "using GIS, remote sensing and other environmental science methods to manage, assess and monitor the countryside"),
 43: (K, ['optimised', 'utilising', 'ensure'], "optimising animals' quality of life", "how animals' quality of life can be made as good as possible, using evidence-informed management and practice to secure positive welfare"),
 44: (K, [], 'animal anatomy and physiology', "the physical and biochemical workings of life behind animal anatomy and physiology"),
 45: (K, [], 'evolution, breeding, health, behaviour and nutrition', "evolution, its genetic basis and its bearing on modern breeding, together with the principles of animal health, behaviour and nutrition"),
 46: (K, [], 'the sustainability of animal management', "how sustainable animal management and practice is, financially, environmentally and socially, at global, national and local scales"),
 47: (K, [], 'social and ethical issues with animals', "the social and ethical questions that animal management and practice raise"),
 48: (K, [], 'animal sector law and policy', "the socio-economic, legal and policy setting of the animal sector"),
 49: (K, [], 'health and safety with animals', "health and safety in working with and managing animals"),
 50: (K, ['enhance'], 'industry-led and industry-leading practice', "why it matters to follow and to lead industry, drawing on the latest evidence-based developments, data and technology to improve animal management and practice"),
 51: (K, ['achieving'], 'education for human behaviour change', "the part education and communication play in changing human behaviour so that animals are managed as well as possible"),
 52: (K, ['consider'], 'human-animal interactions', "why interactions between people and animals matter to society, and the need to weigh animal welfare in every interaction, such as in sport, therapy or education"),
 53: (K, ['understand'], 'food science and human health', "food science and the chemistry and make-up of food, nutrients and non-nutrients alike, with the physiology, biochemistry, genetics and nutrition that form the basis for seeing how food affects human health"),
 54: (K, ['affect'], 'the supply chain and raw material quality', "the food supply chain and how primary production and the quality of raw materials, and what affects that quality, shape the final product"),
 55: (K, [], 'food analysis', "physical, chemical, microbiological and allergen analysis of food"),
 56: (K, ['enhance', 'measure'], 'sensory science', "why the sensory side of food, nutrition and health matters for consumer choice, and how sensory evaluation is used to measure product attributes and consumer response"),
 57: (K, [], 'quality, safety and management systems', "why quality control and assurance, food safety and systems for managing waste and the environment matter to the food industry"),
 58: (K, [], 'preservation and processing', "the principles and practice of preserving and processing food, and their effects on its safety and nutritional quality"),
 59: (K, [], 'hygienic design', "the main engineering and innovation points in designing food equipment and premises hygienically"),
 60: (SK, ['improve'], 'digital innovation in food production', "raising food productivity, nutritional quality and efficiency with new digital technologies"),
 61: (K, [], 'food microbiology methods', "the standard methods for detecting and counting microorganisms that matter for food safety"),
 62: (K, ['ensure'], 'food risk and traceability', "the risks from food fraud, intolerances and allergies, and why food risk management and new traceability methods are needed to keep food safe and acceptable to consumers"),
 63: (SK, ['apply', 'communicate', 'meet'], 'applying and communicating food knowledge', "applying knowledge and conveying it to varied audiences in fitting formats and media, to serve consumers, industry and society in securing a food supply that is sustainable, ethical, safe, affordable, assured and resilient"),
 64: (SK, ['apply'], 'nutrition education and health promotion', "using theories of nutrition education and health promotion to shape public health messages"),
 65: (K, ['promote', 'mitigate'], 'global food system challenges', "the global challenges of producing, processing and making food commodities ethically and sustainably and of supplying consumer services, with the approaches that make supply chains resilient and reduce their impact"),
 66: (SK, ['design', 'reformulate', 'meet', 'considering'], 'designing diets and products for particular needs', "designing or reformulating a diet or food product for the needs of a person or group, taking account of age, gender, religion, culture, socio-economic background, place, environment, physical activity and sustainability"),
 67: (K, ['showing', 'address'], 'diet, health and disease', "how diet, health and disease interact, and how to respond to the effects of nutritional imbalance at any stage of life"),
 68: (K, ['understanding'], 'nutritional assessment', "the principles and methods of assessing nutrition (anthropometric, biochemical and dietary), with the strengths and limits of each"),
 69: (K, [], 'food and nutrition policy', "food, nutrition, health and consumer policy at local, national and international levels"),
 70: (K, [], 'law, ethics and codes of conduct', "the legal, moral and ethical issues and frameworks, professional codes of conduct among them, that bear on the food, nutrition and consumer sectors"),
 71: (K, ['operate', 'recognising'], 'the agri-food business environment', "the business setting of agri-food firms and why innovation and entrepreneurship matter in developing food that is affordable, sustainable, nutritious and safe"),
 72: (K, ['reveal', 'make', 'drive', 'reduce', 'meet', 'address'], 'connected manufacturing and big data', "connected digital manufacturing systems for communication and analysis, and using big data to spot trends, improve decisions and drive change that cuts waste, meets food security challenges and responds to shifting consumer needs"),
 73: (SK, ['applying'], 'consumer attitudes and behaviour', "the socio-cultural and personal influences on what consumers know, think, intend and do, applied to everyday real situations"),
 74: (K, ['face'], 'unequal consumer access', "the social and economic reasons access to goods and services differs, and the inequity various consumer groups meet in that access"),
 75: (K, [], 'roles of consumer and health bodies', "what consumer organisations, food and health charities, nutrition bodies, public health agencies and nutrition and health professionals do and are responsible for"),
 76: (K, ['understand', 'aid'], 'consumer research methods', "theories and methods for understanding how consumers respond, choose and behave, and for designing and running consumer and intervention studies"),
}
COMM = {11, 63}
CUT = {52: "the importance of human animal interactions to society, and the need to consider animal welfare during all interactions (including, for example, sport, therapy and education)"}

def refs(n, dom):
    if n in COMM:
        return 'qaa/fheq-2024/4.15.b8', 'qaa/fheq-2024/annex-d/transferable/r1/'
    if dom == SK:
        return 'qaa/fheq-2024/4.15.b2', 'qaa/fheq-2024/annex-d/practical/r1/'
    return 'qaa/fheq-2024/4.15.b1', 'qaa/fheq-2024/annex-d/knowledge/r2/'

GRADE = {}
OUTCOMES = []
for n, (dom, verbs, about, X) in ITEMS.items():
    tname, sn = table_of(n)
    i = '4.2.b%d' % n
    sp = _SPAN[i]
    text = CUT.get(n, _NORM[sp['start']:sp['end']])
    fheq, ad = refs(n, dom)
    base = dict(level='fheq:6', addressee='learner', verbs=verbs, about=about, domain=dom, award=HON, force='will',
                find=text, after=sp['start'])
    ids = {'threshold': i, 'typical': i + '.typical', 'excellent': i + '.excellent'}
    s(ids['threshold'], type='threshold', rung='threshold', appliesTo=f'honours graduates in {sn}, at the threshold rung', **base,
      para=f"Will have some familiarity with, and awareness of, {X}.",
      prac=f"At threshold, honours graduates in {sn} will have at least some familiarity with, and awareness of, {X}. Teaching and assessment need to secure this for every graduate.",
      ben=f"To reach the threshold, you will have at least some familiarity with {X}.",
      aaw=(f"Treat this as a threshold outcome that every honours graduate in {sn} will have met: at least some familiarity with {about} (FHEQ level 6; FQHEIS level 10 in Scotland). "
           f"Cite it as {CITE}, para 4.2, {tname} table, threshold column. "
           f"Do not present it as a regulatory requirement, a mark scheme or a standard for any award other than honours. "
           f"Set it beside the same outcome at {ids['typical']} and {ids['excellent']} in this document, the FHEQ honours descriptor {fheq} and the Annex D third-class description {ad}3rd."),
      aad=(f"Raise this when a student in {sn} asks what they need to know about {about} to pass, or when a team checks that every graduate meets the minimum. "
           f"To a student, say plainly that by the end you need at least a working familiarity with it; to staff, frame it as the floor the course has to secure. "
           f"Ask: 'Where in your course have you met {about}, and could you explain the basics in your own words?' "
           f"Do not read the table aloud, and do not present the typical or excellent columns as the minimum."))
    s(ids['typical'], type='typical', rung='typical', appliesTo=f'honours graduates in {sn}, at the typical rung', **base,
      para=f"Will have a sound, well-founded understanding of {X}.",
      prac=f"At the typical rung, honours graduates in {sn} will have a sound, well-founded understanding of {X}: the level most of them reach.",
      ben=f"At the typical level, you will have a sound understanding of {X}.",
      aaw=(f"Treat this as the typical rung: a well-founded understanding of {about} that most honours graduates in {sn} reach, above the threshold (FHEQ level 6; FQHEIS level 10 in Scotland). "
           f"Cite it as {CITE}, para 4.2, {tname} table, typical column. "
           f"Do not claim it as the pass standard or as regulation, and do not equate it with one degree class: the statement draws no such line. "
           f"Set it beside {ids['threshold']} and {ids['excellent']} in this document, the FHEQ honours descriptor {fheq} and, as an inferred reading only, the Annex D descriptions {ad}2.2 and {ad}2.1."),
      aad=(f"Raise this when a student who has the basics of {about} wants to know what a solid result looks like, or when a team plans the core of a module. "
           f"To a student, put it as the sound understanding most people reach by the end; to staff, as the expected standard above the floor. "
           f"Ask: 'What does {about} involve in practice, and why does it matter?' "
           f"Avoid presenting it as the pass mark or reading the issuer's wording at length."))
    s(ids['excellent'], type='excellent', rung='excellent', appliesTo=f'honours graduates in {sn}, at the excellent rung', **base,
      para=f"Will have a deep and thorough understanding of {X}.",
      prac=f"At the excellent rung, honours graduates in {sn} will have a deep and thorough understanding of {X}; design tasks that give the strongest students room to show it.",
      ben=f"At the excellent level, you will have a deep and thorough understanding of {X}.",
      aaw=(f"Treat this as the excellent rung, an aspiration rather than a requirement: a deep, thorough understanding of {about} for honours graduates in {sn} (FHEQ level 6; FQHEIS level 10 in Scotland). "
           f"Cite it as {CITE}, para 4.2, {tname} table, excellent column. "
           f"Do not present it as expected of every graduate, as regulation or as master's-level work. "
           f"Set it beside {ids['threshold']} and {ids['typical']} in this document, the FHEQ honours descriptor {fheq} and, as an inferred reading only, the Annex D first-class description {ad}1st."),
      aad=(f"Raise this with a student aiming for the top of the range in {sn}, or with a team designing stretch tasks. "
           f"To a student, describe it as a deep, thorough command of {about} that you can apply to new cases; to staff, as what the strongest work shows. "
           f"Ask: 'Could you weigh competing views on {about} and apply them to a case you have not met before?' "
           f"Avoid implying that everyone has to reach this or that falling short of it means failing."))
    GRADE[ids['typical']] = ids['threshold']
    GRADE[ids['excellent']] = ids['typical']
    OUTCOMES.append(dict(outcome=about, threshold=ids['threshold'], typical=ids['typical'], excellent=ids['excellent'],
                         basis='inferred', domain=dom, award=HON))

# ------------------------------------------------------------------ 4.3 generic skills (lead-in: students should be able to)
GROUPS = [(1, 6, 'People skills'), (7, 8, 'Communication skills'), (9, 13, 'Analytical skills'), (14, 16, 'Business skills'), (17, 19, 'Wider skills')]
def group_of(n):
    for a, b, h in GROUPS:
        if a <= n <= b:
            return h
GFIND = {6: "appreciate how different stakeholders may have varying opinions on topics and respond sensitively to these in communication and decision making and when dealing with conflict",
         13: "demonstrate skills in recognising, describing, categorising and collating data",
         16: "perform assigned tasks individually or as part of a team, participating in verbal and non-verbal communication"}
# n: (verbs, about, Y: our paraphrase after "able to", FHEQ id, Annex D id, question)
GEN = {
 1: (['demonstrate', 'listen', 'comprehend'], 'listening to new ideas', "show that they can listen to new ideas or information and take them in", '4.15.b8', 'transferable/r1', "When did you last meet an unfamiliar idea in class, and how did you check you had grasped it?"),
 2: (['recognise'], "judging others' arguments", "see where other people's arguments are strong and where they are weak", '4.15.b7', 'cognitive/r2', "Take an argument from a recent reading: where is it strongest, and where does it fall short?"),
 3: (['appreciate', 'engage'], 'taking part in current debates', "understand current debates and take part in them constructively", '4.15.b3.2', 'cognitive/r1', "Which current debate in your field have you taken part in, and what did you add to it?"),
 4: (['reflect', 'make'], 'reflection and use of feedback', "reflect well on their own progress and act on the feedback they receive", '4.15.b5', 'transferable/r5', "What did your last piece of feedback ask you to change, and what did you do about it?"),
 5: (['identify', 'work'], 'setting development targets', "set personal, academic and career targets and work towards them", '4.15.b9.3', 'transferable/r3', "What is one academic or career target you have set this year, and how are you tracking it?"),
 6: (['appreciate', 'respond'], 'responding to stakeholder views', "see that stakeholders can hold differing views and respond to those views with care when communicating, deciding and handling conflict", '4.15.b9.2', 'transferable/r2', "Think of a project with people who disagreed: how did you take their views into account?"),
 7: (['express'], 'clear communication to varied audiences', "express themselves clearly to different audiences by several means of communication", '4.15.b8', 'transferable/r1', "Who was the least specialist audience you have explained your subject to, and how did you adapt?"),
 8: (['present'], 'presenting so others can follow', "set out knowledge or an argument so that others can follow and use it", '4.15.b8', 'transferable/r1', "Could someone outside your course follow your last presentation or report without help?"),
 9: (['identify', 'apply', 'generate'], 'critical thinking for creative solutions', "spot problems and questions and use critical thinking to reach creative answers", '4.15.b7', 'cognitive/r3', "Name a problem you found yourself rather than one you were given: how did you work towards a solution?"),
 10: (['undertake'], 'critical analysis of facts', "analyse factual information critically", '4.15.b7', 'cognitive/r1', "When you last used a statistic or report, how did you test whether it was reliable?"),
 11: (['produce'], 'synthesising the state of knowledge', "draw together what is known on a given subject or topic", '4.15.b3.2', 'knowledge/r3', "Could you sum up in a page what is currently known on your project topic, and where the gaps are?"),
 12: (['undertake'], 'working alone and with guidance', "carry out tasks both independently and under guidance", '4.15.b9.1', 'transferable/r3', "Which recent task did you complete on your own, and where did you still need guidance?"),
 13: (['demonstrate'], 'handling data', "show skill in recognising, describing, sorting and gathering data", '4.15.b2', 'practical/r4', "How did you organise and describe the data in your last practical or project?"),
 14: (['develop'], 'leadership and commercial skills', "build leadership and commercial skills", '4.15.b9.1', 'transferable/r4', "Where have you led something or made a commercial judgement, on placement or in a project?"),
 15: (['develop'], 'project planning', "build skills in planning projects", '4.15.b6', 'transferable/r3', "How did you plan your last project, and what would you plan differently?"),
 16: (['perform', 'participating'], 'individual and team work', "carry out tasks given to them alone or in a team, communicating verbally and non-verbally", '4.15.b9.1', 'transferable/r2', "What did you contribute to your last group task, and how did the team communicate?"),
 17: (['consider'], 'responsible use of data, technology and AI', "think through the responsible use of big data and technology, AI and what follows it included", '4.15.b7', 'transferable/r1', "When you used a data set or AI tool, what made its use responsible or not?"),
 18: (['use', 'collate', 'analyse', 'select', 'present'], 'numeracy and digital literacy', "use suitable numeracy and IT skills to gather, analyse, choose and present information", '4.15.b2', 'transferable/r1', "Which software and numerical methods have you used to analyse and present your own data?"),
 19: (['understand'], 'health, safety and inclusion at work', "understand why health and safety, and equity, diversity and inclusion, matter at work", '4.15.b9.2', 'transferable/r4', "What did you do on your last placement or field trip to keep yourself and others safe and included?"),
}
for n, (verbs, about, Y, fh, ad, qn) in GEN.items():
    i = '4.3.b%d' % n
    grp = group_of(n)
    extra = dict(find=GFIND[n]) if n in GFIND else {}
    s(i, type='outcome', rung='none', force='should', level='fheq:6', appliesTo='honours graduates in these subjects', addressee='learner',
      verbs=verbs, about=about, domain='generic-skill', award=HON, **extra,
      para=f"Should be able to {Y}.",
      prac=f"On graduating with honours, students should be able to {Y} ({grp.lower()}).",
      ben=f"By the time you graduate, you should be able to {Y.replace('their own', 'your own').replace('they receive', 'you receive').replace('they can', 'you can').replace('given to them', 'given to you').replace('others can', 'others can')}.",
      aaw=(f"Treat this as a generic skill that honours graduates in these subjects should be able to show at graduation (FHEQ level 6; FQHEIS level 10 in Scotland), listed under {grp} outside the three rungs. "
           f"Cite it as {CITE}, para 4.3. "
           f"Do not present it as a regulatory requirement, a rung of the subject tables or a skill pitched at another level. "
           f"Set it beside the FHEQ honours descriptor qaa/fheq-2024/{fh}, the Annex D descriptions qaa/fheq-2024/annex-d/{ad}/3rd to 1st and the reference step spine:6."),
      aad=(f"Bring this up when a student or team talks about {about}, in study, placements or careers planning. "
           f"To a student, put it in plain words as something you should be able to do by graduation; to staff, as a generic outcome to build and assess across the course. "
           f"Ask: '{qn}' "
           f"Avoid reading the issuer's list aloud or treating it as one of the subject-specific rungs."))

# ------------------------------------------------------------------ themes, levels, relations
TH = {'1.5': 'theme:edi', '1.6': 'theme:edi', '1.10': 'theme:edi', '1.14': 'theme:esd', '1.15': 'theme:esd', '1.23': 'theme:generative-ai'}

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 4.1; 4.2 (honours degree; the Frameworks named, level number not stated: inferred)'),
                  dict(id='fqheis:10', role='refers', locator='inferred: Scottish honours under the Frameworks, Table 1; not named in the statement')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent',
                           basis='inferred from std:doc:qaa-fheq-2024-framework, Table 1 (bachelor\'s degrees with honours: FHEQ 6, FQHEIS 10); the statement states no crosswalk')])

EDI_P = ['1.5', '1.6', '1.7', '1.8', '1.9', '1.10', '2.1', '2.2', '3.9', '3.10', '3.12', '3.13', '3.15', '3.17', '3.18', '3.21', '4.2', '4.3']
ACC_P = ['1.11', '1.12', '2.1', '3.10', '3.17', '3.21']
ESD_P = ['1.4', '1.13', '1.14', '1.15', '1.16', '2.4', '2.5', '2.7', '2.8', '2.9', '2.10', '3.1', '3.7', '3.24', '4.2']
ENT_P = ['1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '3.17', '3.19', '3.20', '4.2', '4.3']
AI_P = ['1.23', '4.3']
S6 = [dict(id='theme:edi', role='carries', carriedIn=EDI_P), dict(id='theme:accessibility', role='carries', carriedIn=ACC_P),
      dict(id='theme:esd', role='carries', carriedIn=ESD_P), dict(id='theme:enterprise', role='carries', carriedIn=ENT_P),
      dict(id='theme:generative-ai', role='carries', carriedIn=AI_P)]

S7 = [
    dict(rel='supersedes', target="std:doc:qaa-agriculture-horticulture-forestry-food-nutrition-and-consumer-sciences-2019-benchmarks (not yet ingested)",
         note='the fourth edition (2019), named in the back matter; key changes listed in the front matter'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the degree classification descriptions for honours (4.2); the Frameworks also named in the front matter for master\'s guidance'),
    dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='Education for Sustainable Development Guidance, for key competencies, outcomes and assessment (1.15)'),
    dict(rel='relatedTo', target='std:doc:qaa-earth-sciences-environmental-sciences-and-environmental-studies-2022-benchmarks', note='an aligned statement (3.2, 3.4)'),
    dict(rel='relatedTo', target='std:doc:qaa-geography-2022-benchmarks', note='an aligned statement (3.2, 3.4)'),
    dict(rel='relatedTo', target='std:doc:qaa-biosciences-2023-benchmarks', note='an aligned statement (3.2, 3.4, 3.6, 3.8)'),
    dict(rel='relatedTo', target='std:doc:qaa-psychology-2023-benchmarks', note='useful for the food grouping (3.8)'),
    dict(rel='relatedTo', target='Subject Benchmark Statement for Events, Hospitality, Leisure, Sport and Tourism (not yet ingested)', note='for equine sports coaching (3.6)'),
    dict(rel='refersTo', target='UNESCO (2019), Education for Sustainable Development', note='the ESD definition quoted (1.14)'),
    dict(rel='refersTo', target='United Nations, Sustainable Development Goals', note='1.14'),
    dict(rel='refersTo', target='CAST, Universal Design for Learning', note='2.1'),
    dict(rel='refersTo', target="QAA Master's Degree Characteristics Statement (not yet ingested)", note='front matter, for master\'s degrees'),
    dict(rel='refersTo', target='QAA Quality Code for Higher Education, Advice and Guidance (not yet ingested)', note='front matter'),
    dict(rel='refersTo', target="QAA Glossary (not ingested)", note='front matter'),
]

SB1 = [
    'A family of separate but closely related land-based and food subjects, each a subject in its own right, running from field to fork (D1, front matter; 1.1, 1.2).',
    'Its context is economic and social: the subjects bear on global sustainability, and graduates make evidence-informed decisions from international policy down to local practice (D1, 1.4).',
    'Sustainability is a priority, taken holistically and through approaches such as One Health that link people, animals, plants and environment (D1, 1.13, 1.14).',
    'Agriculture covers farming systems, crop and animal production, natural resources and farm economics; horticulture covers plant science, production systems and landscapes; forestry covers woodland and forest management for market and wider benefits (D1, 2.4 to 2.6).',
    'Rural environmental sciences treat the countryside as a complex environmental and cultural resource, multidisciplinary and analytical (D1, 2.7).',
    'Animal studies concern the husbandry, welfare and management of non-production animals and a good life for them (D1, 2.8; 3.5; 4.2).',
    'Food science, food technology, human nutrition and consumer science span the food supply chain, safe and sustainable food, health and how consumer choices are made and changed (D1, 2.9, 2.10).',
    'The subjects are practical: field observation, empirical data, laboratory and field work and work-based learning are central (D1, 3.12, 3.17).',
]
SB2 = [
    dict(theme='theme:edi', inThisSubject='inclusive access, recruitment and support across the student journey, with attention to the hidden curriculum, rural and disadvantaged students, equitable work-based learning, gender equity in horticulture and unequal consumer access (D1, 1.5 to 1.10; 2.1; 2.2; 3.10; 3.12; 4.2)',
         statements=['1.5', '1.6', '1.10', '2.1', '3.21', '4.2.b22', '4.2.b74', '4.3.b19']),
    dict(theme='theme:accessibility', inThisSubject='inclusive design and risk assessment for practical and field activities, reasonable adjustments to fieldwork and assessment, and the digital divide in blended learning (D1, 1.11, 1.12; 3.10; 3.17; 3.21)',
         statements=['3.17', '3.21']),
    dict(theme='theme:esd', inThisSubject='sustainability runs through every grouping: sustainable production, net zero on farms, circular economies, sustainable forest and rural management and a resilient food supply; the SDGs and One Health frame it (D1, 1.13 to 1.16; 2.4 to 2.10; 3.24; 4.2)',
         statements=['1.14', '1.15', '4.2.b1', '4.2.b2', '4.2.b4', '4.2.b6', '4.2.b8', '4.2.b9', '4.2.b10', '4.2.b18', '4.2.b20', '4.2.b22', '4.2.b27',
                     '4.2.b37', '4.2.b41', '4.2.b46', '4.2.b63', '4.2.b65', '4.2.b71']),
    dict(theme='theme:enterprise', inThisSubject='enterprise and employability through placements, start-ups, accrediting bodies and authentic assessment, with employer expectations set out for each grouping (D1, 1.17 to 1.22; 3.17; 3.19; 3.20)',
         statements=['3.19', '4.2.b71', '4.3.b14']),
    dict(theme='theme:generative-ai', inThisSubject='generative AI analysed for its effect on the agri-food supply chain and used reflectively and transparently (D1, 1.23; 4.3)',
         statements=['1.23', '4.3.b17']),
]
SB3 = dict(
    areas=[dict(component='3.1', gloss='agriculture (production, sustainable management and agri-tech, farm business); horticulture (plant biology, crop systems, landscapes); forestry (forest and woodland management, conservation)'),
           dict(component='3.3', gloss='the rural environment, managed and unmanaged landscapes, land management'),
           dict(component='3.5', gloss='applied animal science and management (equine, canine, zoo) and wildlife conservation'),
           dict(component='3.7', gloss='food composition and quality, processing and packaging, safety and fraud, diet and health, nutrition science, ethics, consumer behaviour and research methods')],
    practices=[dict(component='3.9', kind='teaching', gloss='active, individualised, differentiated approaches; students as partners'),
               dict(component='3.10', kind='teaching', gloss='blended and online learning, with care for the digital divide'),
               dict(component='3.12', kind='learning', gloss='work-based learning, placements and apprenticeships, made equitable with partners'),
               dict(component='3.16', kind='teaching', gloss='lectures, practicals in real settings, seminars, group work, case studies, problem-based learning, self-study, visits, placements, a project or dissertation'),
               dict(component='3.17', kind='learning', gloss='field observation, practical and research skills, inclusive fieldwork'),
               dict(component='3.18', kind='assessment', gloss='a varied strategy with choice, peer and self-assessment'),
               dict(component='3.20', kind='assessment', gloss='formative and summative, continuous and controlled; authentic tasks'),
               dict(component='3.21', kind='assessment', gloss='inclusive assessment with reasonable adjustments'),
               dict(component='3.22', kind='assessment', gloss='feedback and reflection'),
               dict(component='3.23', kind='assessment', gloss='examples of authentic assessment: field and lab investigations, case reports, presentations, capstones, vivas, timed tasks'),
               dict(component='3.24', kind='assessment', gloss='multidisciplinary assessment underpinned by ESD')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.2', award=HON, items=76),
           dict(rung='typical', leadIn='4.2', award=HON, items=76),
           dict(rung='excellent', leadIn='4.2', award=HON, items=76)],
    rungBases=('4.1 and 4.2: six subject tables, each listing its outcomes once under three column lead-ins graded by depth: some familiarity '
               'and awareness at threshold, a well-founded understanding at typical, a deep and full understanding at excellent; each item is one '
               'S4 record per rung on the same span; most students are said to perform well above threshold, with Annex D for the classes'),
    outcomeLists=[dict(leadIn='4.3', gloss='generic skills on graduating with honours, in five groups (people, communication, analytical, business, wider)', items=19, award=[HON])],
    outcomes=OUTCOMES)
SB4A_FULL = []
SB5 = [dict(body='professional, statutory and regulatory bodies (PSRBs), none named',
            says='support the academic standards expected and may add requirements on content, assessment or delivery; professional and accrediting bodies matter in many related sectors and aligning with them can help employment; they may evaluate and accredit vocational courses by site visits and desk review, and take part in co-creating content (D1, front matter; 1.19; 2.2; 2.14; 2.18; 3.14)',
            requirements='not yet ingested: no body is named (Part E)')]
SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=EDI_P, statements=SB2[0]['statements']),
            dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=ACC_P, statements=SB2[1]['statements']),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=ESD_P, statements=SB2[2]['statements']),
            dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=ENT_P, statements=SB2[3]['statements']),
            dict(id='theme:generative-ai', named='Generative AI (a section heading, not one of the four themes in the front matter)', carriedIn=AI_P, statements=SB2[4]['statements'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6'], citedIn=['4.2'])],
    bodies=[dict(body='professional, statutory and regulatory bodies (PSRBs), unnamed', citedIn=['1.19', '2.2', '2.14', '2.18', '3.14'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.2'],
             role='common descriptions of the four honours classes (1st, 2.1, 2.2, 3rd), for judging evidence of achievement above threshold'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='the QAA Education for Sustainable Development Guidance', citedIn=['1.15'],
             role='key competencies, learning outcomes and assessment for sustainability'),
        dict(document='std:doc:qaa-earth-sciences-environmental-sciences-and-environmental-studies-2022-benchmarks', named='Earth Sciences, Environmental Sciences and Environmental Studies (ES3)', citedIn=['3.2', '3.4'], role='aligned subject area'),
        dict(document='std:doc:qaa-geography-2022-benchmarks', named='Geography', citedIn=['3.2', '3.4'], role='aligned subject area'),
        dict(document='std:doc:qaa-biosciences-2023-benchmarks', named='Biosciences', citedIn=['3.2', '3.4', '3.6', '3.8'], role='aligned subject area; bioveterinary science; food'),
        dict(document='std:doc:qaa-psychology-2023-benchmarks', named='Psychology', citedIn=['3.8'], role='useful for the food and consumer grouping'),
        dict(document='not yet ingested: listed in Part E', named='Subject Benchmark Statement for Events, Hospitality, Leisure, Sport and Tourism', citedIn=['3.6'], role='equine sports coaching'),
    ])

B1 = [
    dict(slug='hidden-curriculum', definition='the implicit lessons students absorb beyond formal teaching, which shape their sense of the discipline\'s values and norms and can be a barrier when access to them is unequal (D1, 1.10)',
         beneficiaryDefinition='the unwritten things you pick up about how your subject and course work, beyond what is taught', scopeNote='used of course design and EDI', category='unknown', practices=['education']),
    dict(slug='accessibility', definition='inclusive design of curriculum, teaching and the wider student experience so that nobody is shut out, above all through barriers linked to disability (D1, 1.11)',
         beneficiaryDefinition='courses designed so that everyone, including disabled students, can take part', scopeNote='a cross-cutting theme', category='unknown', practices=['education']),
    dict(slug='education-for-sustainable-development', definition='after UNESCO (2019), holistic and transformational education covering content, outcomes, pedagogy and environment, aiming to change society (D1, 1.14)',
         beneficiaryDefinition='learning that helps you understand and act on sustainability, and changes how you see the world', scopeNote='ESD; a cross-cutting theme', category='unknown', practices=['education']),
    dict(slug='sustainability', definition='a continuing process of tackling social, environmental, ethical, political and economic concerns for a better world, not only an environmental matter (D1, 1.13)',
         beneficiaryDefinition='meeting today\'s needs fairly while protecting the planet and people for the future', scopeNote='used with sustainable development', category='unknown', practices=['education', 'agriculture']),
    dict(slug='one-health', definition='an approach that sees people, animals, plants and their shared environment as interconnected (D1, 1.13)',
         beneficiaryDefinition='the idea that human, animal and plant health and the environment depend on each other', scopeNote='named as an example', category='unknown', practices=['agriculture', 'health']),
    dict(slug='work-based-learning', definition='learning through placements, internships and apprenticeships (D1, 3.12)',
         beneficiaryDefinition='learning you do in a workplace, such as a placement or apprenticeship', scopeNote='WBL', category='unknown', practices=['education']),
    dict(slug='authentic-assessment', definition='assessment built on tasks of the kind met in the workplace (D1, 3.20)',
         beneficiaryDefinition='assessment that asks you to do the kind of task you would do at work', scopeNote='examples in 3.23', category='unknown', practices=['education']),
]
B2A = [
    dict(concept='hidden-curriculum', form='hidden curriculum', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='accessibility', form='Accessibility', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='education-for-sustainable-development', form='Education for Sustainable Development (ESD)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='sustainability', form='sustainability', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='one-health', form='One Health approach', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='work-based-learning', form='Work-based learning (WBL)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='authentic-assessment', form='Authentic assessment', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
]
B4 = []; B5 = []
D3 = []

E = [
    'Rung shape (new against Psychology): no separate rung lists. Section 4.2 holds six subject tables (agriculture 12 items, horticulture 10, forestry 10, rural environmental sciences 10, animal studies 10, food science, food technology, human nutrition and consumer science 24), each listing its outcomes once under three column lead-ins ("Threshold Typical Excellent", then the three "Graduates have ..." lines). Each item is recorded as three S4 records on the same span: the threshold record keeps the skeleton id 4.2.b<n> (stan\'s chunk); the typical and excellent records take 4.2.b<n>.typical and 4.2.b<n>.excellent, our ids, not the issuer\'s numbering (rule 3: for P3). The builder sorts these suffixed ids after the numbered ones.',
    'Rungs differ only by depth of the lead-in (some familiarity and awareness; well-grounded understanding; deep and comprehensive understanding), not by content, so every outcome has all three rungs.',
    'gradeOf: 152 links (each typical record to its threshold record, each excellent to its typical), all on the same span and content, so the link is plain; the builder writes basis inferred. P3 to rule whether a table that pairs rungs by layout counts as stated.',
    'Force: the column lead-ins are plain present ("Graduates have"); force will is taken from 4.1 ("will have demonstrated"), as in Psychology. The generic skills (4.3) take should from their lead-in ("students should be able to").',
    'Skeleton corrections: rung counts (threshold 76, typical 0, excellent 0) replaced by 76 at each rung; 4.2 recorded by `find` as its own three sentences, not the whole table span; 4.2.b52 cut before the trailing note "Please note, as highlighted in section 3 (above), this refers to non-production animals" (a scope note on the animal studies table); 4.3.b6, 4.3.b13 and 4.3.b16 cut before the sub-headings that follow them (Communication skills, Business skills, Wider skills).',
    '4.2.b45 seems to run two bullets together ("... modern breeding practice principles of animal health, behaviour and nutrition"): an extraction or issuer fault; kept as one record.',
    'Item wording: 4.2.b11, 4.2.b20 and 4.2.b14 mix a gerund or a verb ("communicate", "make") under a noun lead-in; read as subject skills (domain subject-skill for 4.2.b11, b12, b20, b32, b60, b63, b64, b66, b73).',
    'Levels: the statement covers honours degrees only and names no level number; fheq:6 is read from "honours degree" and the Frameworks (4.2) against std:doc:qaa-fheq-2024-framework S5 and Table 1, fqheis:10 is inferred (Scotland is in scope, front matter). No SCQF, FQHEIS or CQFW name appears outside the front matter. Master\'s degrees are referred to the FHEQ and the Master\'s Degree Characteristics Statement (front matter).',
    'Subject codes: the statement states none; all eight in front matter (CAH06-01; HECoS 100517, 100529, 100520, 100468, 100523, 100527, 100247) are basis inferred. Rural environmental sciences has no exact HECoS term (countryside management chosen; rural estate management 100977 and environmental management 100469 are alternatives); consumer science has no HECoS term found. For P3.',
    'Plain-present provider norms not recorded as statements (benchmark template open point 5): 1.6 (first sentence), 1.7, 1.8, 1.9, 1.11, 1.12, 2.13, 2.15, 3.2, 3.9, 3.11, 3.12 (the list of what providers do with work-based learning partners), 3.15, 3.18, 3.20, 3.22, 3.24. 3.2 ("include") is the plain-present twin of 3.4 and 3.6 ("will include"), which are recorded.',
    'Obliging words beyond the five, not recorded as force: 2.2 ("It is important that course teams identify and address ..."), 3.10 ("requires effective design"), 3.9 and 2.2 ("encouraged"), 2.11 ("it is expected", "would").',
    '3.19 holds a must (the student voice) and a should (authentic assessment) in one paragraph; one record with force must, the should kept in the paraphrase and versions.',
    '1.23 has two addressees (the course analyses and uses AI; graduates should recognise its uses and limits): addressee both, domain generic-skill.',
    'Themes: generative AI is a section-1 heading beside the four cross-cutting themes, so a new theme id theme:generative-ai is used (not in the shared theme list: for P3). Employability is named with enterprise in the front matter and recorded under theme:enterprise.',
    'Bodies: none named in the body of the text; PSRBs only in general terms. The advisory group lists bodies (IFST, Association for Nutrition, CIEEM, National Equine Welfare Council, Landex) only in the excluded back matter; not recorded as cited.',
    'Shared documents not yet ingested: the Events, Hospitality, Leisure, Sport and Tourism statement (3.6); the 2019 fourth edition (supersedes); the Master\'s Degree Characteristics Statement, Quality Code Advice and Guidance and QAA Glossary (front matter).',
    'The agent instructions read typical against the Annex D 2.2 and 2.1 descriptions and excellent against the first-class description; this pairing is ours and inferred: the statement maps no rung to a class.',
    'Text faults noted, not acted on: front matter "This document is a QAA Subject Benchmark Statement is for"; 3.23.b5 "which could capstone projects"; 3.23.b9 "schoolchildren social media".',
    'S9 commentary not researched in P1.',
]
