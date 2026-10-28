# Judgement fields for run 0086, QAA Architectural Technology 2022 (std). Keys are S4 ids under qaa/architectural-technology-2022/.
# Built by tools/bm_build.py under the benchmark template 0.6.0-draft, run layer 0.7.0-draft and BM-BRIEF 0.2.0.
HON = "bachelor's with honours"
MAS = "master's"
BOTH = [HON, MAS]
CITE = 'QAA, 2022, Architectural Technology Subject Benchmark Statement, para '

META = dict(
    run='0086', p1='2026-10-03 16:15',
    title='Subject Benchmark Statement Architectural Technology',
    heading='Subject Benchmark Statement: Architectural Technology (QAA, March 2022)',
    edition='March 2022 (fifth edition)', published='2022-03',
    status='current', supersedes='the fourth edition, 2019 (D1, back matter); not held',
    subjects=[dict(scheme='hecos', code='100121', label='architectural technology', basis='stated'),
              dict(scheme='cah', code='CAH13-01-01', label='architecture', basis='stated'),
              dict(scheme='cah', code='CAH13-01', label='architecture, building and planning', basis='stated'),
              dict(scheme='cah', code='CAH13', label='architecture, building and planning', basis='stated')],
    awards=[HON, MAS], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2022 revision with cross-cutting themes (this subject\'s fifth edition)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what a graduate in Architectural Technology should know and be able to do at the end of "
                     "an honours degree or a master's degree. It states one rung only, the threshold, for each award (honours in 4.6, master's in 4.7), "
                     "with a list of generic skills for honours graduates (4.8) and lists of course aims (3.6) and master's abilities (3.7). "
                     "Reach for it when designing, reviewing or describing a course in the subject or its outcomes. It is not a curriculum and "
                     "not a regulatory requirement in England, though the lead professional body bases its accreditation on it."),
    summary=("Published by QAA in March 2022 for the sector, the statement describes architectural technology as a design discipline "
             "rooted in science and engineering that links design and construction, and sets out its context, purposes, distinctive "
             "features, content, teaching, learning and assessment. Its benchmark standards are threshold only: one list for bachelor's "
             "degrees with honours (FHEQ Level 6, FQHEIS Level 10) and an added list for master's degrees, with honours generic skills "
             "beside them; performance above threshold is left to the degree classification descriptions (Annex D). It carries the four "
             "cross-cutting themes (equality, diversity and inclusion, framed by its own EDI Vision Statement; accessibility; sustainability; "
             "enterprise and entrepreneurship with employability) and names the Chartered Institute of Architectural Technologists (CIAT) "
             "as the lead PSRB, whose accreditation and Chartered Membership standards rest on it."),
    authority=('reference: a sector reference point; in England not a sector-recognised standard under the OfS framework; a key reference '
               'point in Wales and Scotland; part of quality requirements in Northern Ireland; the basis of CIAT\'s accreditation and of its '
               'standards of education for Chartered Membership (D1, front matter: Relationship to legislation)'))

S2 = dict(
    governs=("what an Architectural Technology graduate can be expected to know, do and understand at the end of an honours or a master's "
             "degree, and the nature and characteristics of awards in the subject (D1, front matter: About this Statement; 4.1)"),
    awards=["bachelor's degrees with honours", "master's degrees, generalist and specialist, conversion or specialising (2.7; 4.5)",
            "graduate and degree apprenticeships (4.1)"],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    howUsed=['design', 'approval', 'review', 'other: external examining; PSRB accreditation (CIAT); information for prospective students and employers'],
    statedScope=('"The ever-increasing professional diversity within architectural technology is recognised in this Statement alongside the need '
                 'and demand to develop the subject at honours and master\'s degree level." (D1, front matter: About this Statement)'),
    statedSubjects=[
        dict(name='Architectural Technology', locator='(D1, title; 1.1)', kind='subject',
             codes=[dict(scheme='hecos', code='100121', label='architectural technology'), dict(scheme='cah', code='CAH13-01-01', label='architecture')]),
        dict(name="honours and master's degree level qualifications in Architectural Technology or related subjects", locator='(D1, front matter: Relationship to legislation)',
             kind='programme title', codes=[dict(scheme='hecos', code='100121', label='architectural technology')]),
        dict(name='graduate and degree apprenticeship programmes', locator='(D1, 4.1; 1.39)', kind='programme title',
             codes=[dict(scheme='hecos', code='100121', label='architectural technology')]),
        dict(name='Sustainable Design', locator='(D1, 2.16)', kind='specialism', codes=[]),
        dict(name='Fire Safety', locator='(D1, 2.16)', kind='specialism', codes=[]),
        dict(name='Architectural Engineering', locator='(D1, 2.16)', kind='specialism', codes=[dict(scheme='hecos', code='100120', label='architectural engineering')]),
        dict(name='Building Performance', locator='(D1, 2.16)', kind='specialism', codes=[]),
        dict(name='Design Management', locator='(D1, 2.16)', kind='specialism', codes=[]),
        dict(name='Project Management', locator='(D1, 2.16)', kind='specialism', codes=[dict(scheme='hecos', code='100812', label='project management')]),
        dict(name='Retrofit Design', locator='(D1, 2.16)', kind='specialism', codes=[]),
        dict(name='Conservation', locator='(D1, 2.16)', kind='specialism', codes=[]),
    ])

SECTIONS = {'1': 'Context and purposes of an Architectural Technology degree',
            '2': 'Distinctive features of an Architectural Technology degree',
            '3': 'Content, structure and delivery',
            '4': 'Benchmark standards'}
SUB = [('1.1', '1.10', 'Context'), ('1.11', '1.14', 'Purposes of an Architectural Technology degree'),
       ('1.15', '1.18', 'Characteristics of an Architectural Technology degree'), ('1.19', '1.20', 'Equality, diversity and inclusion (EDI)'),
       ('1.21', '1.26', 'Architectural Technology EDI Vision Statement'), ('1.27', '1.34', 'Sustainability'),
       ('1.35', '1.40', 'Entrepreneurship, enterprise and employment'),
       ('2.1', '2.7', 'Design of courses'), ('2.8', '2.14', 'Accessibility'), ('2.15', '2.17', 'Progression'),
       ('2.18', '2.19', 'Flexibility'), ('2.20', '2.21', 'Partnership'), ('2.22', '2.25', 'Monitoring and review'),
       ('3.1', '3.5', 'Content'), ('3.6', '3.6', 'Structure and aims of Architectural Technology honours degrees'),
       ('3.7', '3.7', "Structure and aims of Architectural Technology master's degrees"), ('3.8', '3.17', 'Teaching and learning'),
       ('3.18', '3.22', 'Assessment'),
       ('4.1', '4.5', 'Introduction'), ('4.6', '4.6', 'Benchmark standards for honours degrees (threshold)'),
       ('4.7', '4.7', "Benchmark standards for master's degrees (threshold)"), ('4.8', '4.8', 'Generic skills for Architectural Technology graduates')]

G = {
    '1.1': 'the discipline defined: how buildings are put together and perform, grounded in science and engineering; growing weight on retrofit and energy',
    '1.2': 'building and life safety after major failures; new law and standards reach education and practice',
    '1.3': 'the climate emergency will change how professionals in the field think and work',
    '1.4': 'a changing built environment calls for more diverse and specialised education',
    '1.5': 'effects on design, construction and use: retrofit, carbon, safety, advanced and offsite methods',
    '1.6': 'decisions driven by data across the building process, reducing risk and overruns',
    '1.7': 'reliable, usable data and information management support design; the move to digital working',
    '1.8': 'the role widens to embed new technology and help prevent safety, cost and performance failures',
    '1.9': 'this changing focus frames the next standards of education and leaves institutions room to design',
    '1.10': 'the specifications are a broad framework for responsive, challenging courses',
    '1.11': 'purpose: an independent design discipline linking design and construction within the built environment',
    '1.12': 'the field in project and design management across the life cycle, and in the digital age',
    '1.13': 'leading roles as designers, lead or principal designers; degrees build critical understanding of design, technology, leadership and practice',
    '1.14': 'diverse careers; the standards as a broad framework for agility and employability; inclusive design and wellbeing',
    '1.15': 'characteristics: a real-world, vocational curriculum preparing professionals for building design and delivery',
    '1.16': 'numeracy, literacy, industry awareness and technical competence underpin study; subject and wider skills',
    '1.17': 'a distinct subject with four educational components (theoretical, experiential, professional, ethical)',
    '1.18': 'a pointer to the front matter on PSRB accreditation',
    '1.19': 'a record of widening participation; a duty on providers to make curricula inclusive',
    '1.20': 'CIAT uses inclusivity in accreditation; the subject\'s EDI vision, set within the Equality Act 2010, runs across the statement',
    '1.21': 'the vision: wider participation and a commitment to equality, diversity and inclusion',
    '1.22': 'the whole life cycle of a project includes the changing lives of its end-users',
    '1.23': 'inclusive design as a requirement; EDI to be embedded like health and safety (S4)',
    '1.24': 'honesty, integrity and respect for a diverse population at the core of practice',
    '1.25': 'the profession\'s widening participation record should inform how it is promoted',
    '1.26': 'inquisitive professionals who weigh the effect of decisions on users\' comfort, safety and wellbeing',
    '1.27': 'core skills match the ESD guidance\'s outcomes (Advance HE and QAA, 2021)',
    '1.28': 'the discipline\'s key part in sustainability; the three pillars early in a career',
    '1.29': 'UNESCO\'s eight sustainability competencies to be aligned with outcomes (S4)',
    '1.30': 'the vision of integrated sustainability; real-life case studies and reflection (S4)',
    '1.31': 'an ESD framework may renew pedagogy and raise real-world application',
    '1.32': 'problem-based learning; balance soft and hard skills; software not at the expense of sustainability',
    '1.33': 'collaborative and enquiry-based learning; working with industry stakeholders (S4)',
    '1.34': 'interdisciplinary and independent learning; theory with practical projects; partnerships with industry (S4)',
    '1.35': 'enterprise and entrepreneurship education as QAA (2018) defines them',
    '1.36': 'enterprise education adds value to careers and to society',
    '1.37': 'the subject is well placed for enterprise through live projects and visiting expertise',
    '1.38': 'the degree prepares for work and inspires creative, critical thinking; teams encouraged to build this in',
    '1.39': 'employer engagement, required in CIAT accreditation; apprenticeships; the aspirATion network',
    '1.40': 'involving employers of different sizes and sectors; corporate social responsibility (S4)',
    '2.1': 'the statement as dialogue for course design; adaptability and specialisms for a fast-changing industry (S4)',
    '2.2': 'master\'s degrees: deeper, professional or interdisciplinary variants',
    '2.3': 'restates the subject and its four educational components (see 1.17)',
    '2.4': 'inclusive design and awareness of health, safety, welfare and ethics',
    '2.5': 'national and international context; an international dimension in courses; CIAT accredits overseas (S4)',
    '2.6': 'technology\'s growing effect calls for modelling and coordination across the whole building process',
    '2.7': 'generalist (broader) and specialist (deeper) master\'s degrees',
    '2.8': 'an obligation on all providers to make study accessible, onsite and online',
    '2.9': 'support expected of institutions: screening, specialist support, mentors, adjustments, claims, accessible curricula',
    '2.10': 'those services as the basic minimum (S4)',
    '2.11': 'design-led modules bring varied learning and assessment types and outputs',
    '2.12': 'adjustments for presentation-based design assessment (S4)',
    '2.13': 'clear assessment expectations; a digital route for students who cannot afford physical models',
    '2.14': 'remote and blended learning widen access; attention to digital poverty (S4)',
    '2.15': 'progression through honours (FHEQ 6, FQHEIS 10) towards all the threshold skills',
    '2.16': 'master\'s specialisms named, such as fire safety and retrofit design',
    '2.17': 'exit awards; four-year Scottish honours; a second-class degree fits a student for postgraduate study',
    '2.18': 'modes of delivery and a range of teaching methods',
    '2.19': 'industry input; a design project or dissertation expected of students (S4)',
    '2.20': 'partnership with employers and the organisations around them',
    '2.21': 'ways employers take part, and the burden on small firms',
    '2.22': 'monitoring and periodic review, with this statement as an external reference point',
    '2.23': 'external reviewers in periodic review',
    '2.24': 'external examiners and how the statement supports them',
    '2.25': 'accreditation by CIAT through visits and desk reviews',
    '3.1': 'content: a creative design discipline of building systems, materials and BIM across the life cycle',
    '3.2': 'efficient, low-carbon, safe buildings and the social and ethical demands on the profession',
    '3.3': 'inclusive design and the needs of all stakeholders (repeats 2.4)',
    '3.4': 'researching needs and requirements, including social needs and life safety',
    '3.5': 'modelling, procurement and services make design and construction complex; degrees develop understanding in context (S4)',
    '3.6': 'course aims for honours degrees: fourteen things students learn how to do (S4 items)',
    '3.7': 'master\'s entry assumes broad understanding; eight added subject-specific abilities (S4 items)',
    '3.8': 'teaching that joins theory, practice and employability; case studies, live sites, simulations',
    '3.9': 'studio-based, problem-based learning with input from industry',
    '3.10': 'knowledge of context, core concepts and theories, plus subject and wider skills',
    '3.11': 'simulation, interdisciplinary work and practical sessions; problem-based studio learning',
    '3.12': 'active and reflective learning; a final collaborative interdisciplinary project',
    '3.13': 'master\'s level: debate on current and emerging topics',
    '3.14': 'master\'s level: critical understanding, creative response, learner-centred study',
    '3.15': 'master\'s courses widen and refine knowledge; professional, ethical and practical issues (S4)',
    '3.16': 'master\'s level: advanced research, analytical and practical techniques',
    '3.17': 'master\'s research: an advanced project and communicating it professionally (S4)',
    '3.18': 'a wide range of assessment methods suited to a vocational subject',
    '3.19': 'an explicit assessment strategy tied to learning outcomes (S4)',
    '3.20': 'accessible assessment, adjustments and fairness; coverage, coursework and feedback (S4)',
    '3.21': 'a range of methods matched to outcomes, with an indicative list of ten (S4 for the lead sentence)',
    '3.22': 'master\'s level: the major project as the decisive assessment',
    '4.1': 'the standards as threshold, the baseline for all honours and master\'s graduates, apprenticeships included',
    '4.2': 'most students exceed threshold; providers refer to Annex D for the classifications (S4)',
    '4.3': 'the standards can be met in several ways and do not map onto single modules',
    '4.4': 'courses enable fluency in design, technology, management and practice (S4)',
    '4.5': 'master\'s degrees, conversion or specialising, share one set of standards',
    '4.6': 'honours threshold: ten areas of knowledge and ability (S4 items)',
    '4.7': 'master\'s threshold: five added items (S4 items)',
    '4.8': 'generic skills of honours graduates: seventeen items (S4 items)',
}
CTYPE = {'2.9': 'stem', '3.6': 'stem', '3.7': 'stem', '3.21': 'stem', '4.6': 'stem', '4.7': 'stem', '4.8': 'stem',
         '3.1': 'area', '3.2': 'area', '3.3': 'area', '3.4': 'area', '3.5': 'area',
         '3.8': 'practice', '3.9': 'practice', '3.10': 'practice', '3.11': 'practice', '3.12': 'practice', '3.13': 'practice',
         '3.14': 'practice', '3.16': 'practice', '3.18': 'practice', '3.19': 'practice', '3.20': 'practice', '3.22': 'practice',
         '2.18': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points; '
         'Architectural technology course accreditation; Chartered Architectural Technologist: protected title; CIAT\'s Chartered Standards',
         kind='other: front matter, read for S1, S2, S7, SB5 and SB6'),
    dict(number='section headings', heading='headings of sections 1 to 4', kind='other: heading lines'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for S7 and SB6'),
    dict(number='6', heading='Membership of the Advisory Group for the Subject Benchmark Statement for Architectural Technology', kind='other: back matter, read for S1 (editions) and S8'),
]

P = {}
def s(i, **k):
    P[i] = k

# ---------------------------------------------------------------- the agent instructions, built per record from its own parts
FR6 = 'qaa/fheq-2024/4.15'
FR7 = 'qaa/fheq-2024/4.17'
def aaw(n, kind, nots, beside):
    return f'{kind} Cite it as ({CITE}{n}). Do not claim {nots}. Set it beside {beside}.'
def aad(when, how, ask, avoid):
    return f'Raise it when {when}. {how} Ask: {ask} Avoid {avoid}.'

HOW_S = 'With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show.'
HOW_P = 'With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it.'
AV_TH = 'reading the issuer\'s wording out at length, or treating this minimum as the mark of a good degree'
AV_SH = 'reading the issuer\'s list aloud, or turning a should into a must'
AV_P = 'handing this duty to a student as something they must achieve, or reading the paragraph aloud'

# ---------------------------------------------------------------- obliging and outcome paragraphs (sections 1 to 4)
s('1.23', type='requirement', rung='none', force='should', level='none', appliesTo='education and practice in the subject',
  addressee='both', verbs=['embedded', 'communicate'], about='EDI embedded like health and safety; communicating the value of inclusive design',
  domain='subject-skill', award=BOTH,
  para='Equality, diversity and inclusion should be built into education and practice as visibly as health and safety, since poorly designed buildings harm people and society; professionals in the field should be able to explain the worth of inclusive design in an accessible way.',
  prac='Build equality, diversity and inclusion into the curriculum as firmly as health and safety, and give students practice in explaining, accessibly, why inclusive design matters.',
  ben='You should come to treat inclusion as seriously as safety in your design work, and be able to explain clearly to anyone why designing for everyone matters.',
  aaw=aaw('1.23', 'Present this as a should-level expectation on courses and on professionals, part of the EDI Vision Statement (1.21 to 1.26), for honours and master\'s study alike.',
          'that it is a legal duty in itself or that it sets a level of attainment', 'para 4.8 (item 15), para 3.6 (items 12 and 13) and the honours descriptor qaa/fheq-2024/4.15.b8 on communication'),
  aad=aad('a team reviews how inclusion appears in studio briefs or a student asks why inclusive design is assessed',
          'With a student, say it in plain second-person words; with staff, frame it as a curriculum commitment on a par with health and safety.',
          'Where in your project could you show who the building serves and who it might shut out? How would you explain that choice to a client?',
          'presenting it as a box to tick, or reading the Vision Statement out in full'))
s('1.29', type='requirement', rung='none', force='should', level='none', appliesTo='curricula in the subject', addressee='provider',
  verbs=['aligned'], about='UNESCO sustainability competencies aligned with outcomes', domain='none', award=BOTH,
  para='The eight UNESCO competencies for sustainability should be matched to suitable learning outcomes in the curriculum, to change how staff and students think about and practise sustainable development.',
  prac='Map UNESCO\'s eight sustainability competencies (systems, futures, critical, strategic, collaborative, integrated problem-solving, self-awareness, normative) onto your module learning outcomes.',
  ben=('n/a', 'a duty on curriculum design; the student meets its effect in their outcomes'),
  aaw=aaw('1.29', 'Present this as a should-level duty on curriculum design within the sustainability theme, applying to every course in the subject.',
          'that students are assessed on the UNESCO list itself, or that the duty is regulatory', 'paras 1.27 and 1.30, the ESD guidance std:doc:qaa-advancehe-esd-2021-guidance, and para 4.8 (items 16 and 17)'),
  aad=aad('a programme team maps sustainability across its modules', HOW_P,
          'Which of the eight competencies does each core module already develop, and which have no home yet?', AV_P))
s('1.30', type='requirement', rung='none', force='should', level='none', appliesTo='courses in the subject', addressee='provider',
  verbs=['engaged', 'support', 'develop'], about='integrated sustainability and real-life case studies', domain='none', award=BOTH,
  para='Every course is meant to treat sustainability in a balanced, integrated and interdisciplinary way, so graduates know the goals they can serve; learners should work on real cases that build critical judgement of current and new solutions, and reflection.',
  prac='Thread sustainability through the whole course rather than one module, and use real case studies that make students judge existing and novel solutions and reflect on their choices.',
  ben=('n/a', 'a duty on course design and teaching; the student meets it as case-study work'),
  aaw=aaw('1.30', 'Present this as a should-level expectation on teaching within the sustainability theme, for all courses in the subject.',
          'that a single sustainability module meets it, or that it is a student outcome', 'paras 1.29, 1.32 and 1.34 and the honours items in para 4.6 (items 5 and 8)'),
  aad=aad('staff plan case studies or ask how sustainability should run through the course', HOW_P,
          'Where does each year of the course use a real project to test sustainable solutions? Where do students reflect on those choices?', AV_P))
s('1.33', type='requirement', rung='none', force='should', level='none', appliesTo='teaching in the subject', addressee='provider',
  verbs=['encouraged', 'disseminate', 'introduced'], about='collaborative and enquiry-based learning', domain='none', award=BOTH,
  para='Learners should be encouraged to share what they learn with peers and in their communities through collaborative learning, and be introduced to working with clients, contractors and suppliers; enquiry-based learning on real scenarios may also be used.',
  prac='Give students chances to share their learning with peers and beyond the classroom, bring in clients, contractors and suppliers, and consider enquiry-based projects set in real situations.',
  ben=('n/a', 'a teaching approach the course adopts; not a standard for the student to reach'),
  aaw=aaw('1.33', 'Present this as a should-level expectation on teaching methods under the sustainability theme, with enquiry-based learning as a may.',
          'that it requires a particular pedagogy, or that the may-clause is binding', 'paras 1.32 and 1.34 and para 3.9 on studio and problem-based learning'),
  aad=aad('a team designs group or community-facing work', HOW_P,
          'Where do students meet clients, contractors or suppliers in the course? How do they share what they learn outside the class?', AV_P))
s('1.34', type='requirement', rung='none', force='should', level='none', appliesTo='curricula and courses in the subject', addressee='provider',
  verbs=['ensure', 'combined', 'fostered'], about='theory with practical projects; partnerships with industry',
  domain='none', award=BOTH,
  find="1.34 Architectural Technology courses need to involve both interdisciplinary work and independent learning aspects to develop well-rounded students. 'Problem-based learning' may be adopted to facilitate creative environments for interdisciplinary learning in which students work together to address complex, multifaceted problems. New curricula should ensure that theory is combined with practical projects to achieve environmentally sustainable design objectives and enhance student learning experience. Academic-industry partnerships should be fostered by Architectural Technology courses. These are hugely beneficial for the development of student confidence and allow the real-world application of the theory taught by higher education providers in a professional setting. In addition, these will develop student employability skills and readiness for industry which will ensure sustainably aware graduates are employed where they can make a real-world impact.",
  para='Courses need both interdisciplinary and independent learning; new curricula should join theory to practical projects with sustainable design aims, and courses should build partnerships with industry, which grow confidence and employability.',
  prac='Pair interdisciplinary and independent work, join theory to practical projects with sustainable design aims, and build partnerships with industry so students apply theory in professional settings.',
  ben=('n/a', 'a duty on curriculum design; the student meets it as projects and industry links'),
  aaw=aaw('1.34', 'Present this as a should-level duty on curricula under the sustainability theme, with problem-based learning as a may and "need to" for the interdisciplinary mix (Part E).',
          'that partnerships with industry are a condition of the award', 'paras 1.33, 1.39 and 3.9'),
  aad=aad('a team reviews live projects or industry partnerships', HOW_P,
          'Which projects tie theory to a sustainable design goal? Which employers or firms work with students, and how often?', AV_P))
s('1.40', type='requirement', rung='none', force='should', level='none', appliesTo='higher education providers', addressee='provider',
  verbs=['consider'], about='involving varied employers', domain='none', award=BOTH,
  find="1.40 Higher education providers should consider the benefits of involving employers of different sizes and from different sectors through a variety of modes of engagement, including subgroups, that work on specific employer-related issues, which meet less frequently and use electronic communication. A key driver of employer involvement is corporate social responsibility (CSR). The CSR ethos of businesses is a key driver of employer involvement, with emphasis on widening participation, local employment for local people, and activity being driven by 'finding the right job for the right person'. There are\n\n10\n\nbenefits of employer involvement for both the course and employers. Learning from employer perspectives brings a kind of 'business realism' to the student learning.",
  para='Providers should weigh the gains of involving employers of varied size and sector in several ways, including small groups on employer issues; corporate social responsibility drives much of that involvement, and employer views bring commercial realism to learning.',
  prac='Consider engaging employers of different sizes and sectors in light-touch ways, such as small working groups meeting online, and use their perspective to give learning commercial realism.',
  ben=('n/a', 'a duty on the institution in engaging employers'),
  aaw=aaw('1.40', 'Present this as a should-level matter for the institution to consider, under the enterprise and employment theme.',
          'that particular modes of employer engagement are required', 'paras 1.39, 2.20 and 2.21'),
  aad=aad('a team plans an employer forum or asks how to involve small firms', HOW_P,
          'Which sizes and sectors of employer are missing from your current links? What low-effort way could bring them in?', AV_P))
s('2.1', type='requirement', rung='none', force='should', level='none', appliesTo='course design in the subject', addressee='provider',
  verbs=['reflected', 'encouraging'], about='adaptability and specialisms in course design', domain='none', award=BOTH,
  para='The statement sets general expectations and invites collaborative course design; since careers will be diverse and the industry will change, course design should foster adaptability, agility, diversity and specialisms to keep knowledge current.',
  prac='Use the statement as a starting point for shared course design, and build in room for adaptability, specialisms and new competencies so the course keeps pace with industry change.',
  ben=('n/a', 'a duty on course design'),
  aaw=aaw('2.1', 'Present this as a should-level expectation on course design, framing the statement as general and dialogic.',
          'that the statement prescribes content or structure', 'paras 1.4, 1.14, 2.2 and 2.7'),
  aad=aad('a team asks how much the statement constrains its design or how to plan for specialisms', HOW_P,
          'How does the course let a student start to specialise? What will you change when industry practice shifts?', AV_P))
s('2.5', type='expectation', rung='none', force='will', level='none', appliesTo='students of the subject', addressee='learner',
  verbs=['develop', 'included'], about='design, technology and practice in national and international context', domain='understanding', award=BOTH,
  para='All degrees in the subject are expected to develop students\' knowledge and critical understanding of design, technology and practice in national and international settings, and courses need an international dimension so graduates know the global context of their field.',
  prac='Students will build knowledge and critical understanding of design, technology and practice at home and abroad; include an international dimension so graduates understand where their profession works globally.',
  ben='You will build knowledge and a critical understanding of design, technology and practice, both in the UK and internationally, and learn how your profession works across borders.',
  aaw=aaw('2.5', 'Present this as an expected outcome in the issuer\'s will, for honours and master\'s students alike, with the international dimension as something important for courses to include.',
          'that it fixes a level of attainment by itself', 'paras 3.5 and 4.4, para 4.6 (item 1) and para 4.7 (item 1)'),
  aad=aad('a student asks why international examples matter, or a team checks its international content', HOW_S,
          'Which projects or case studies from outside the UK have you met so far? How do rules and practice differ there?', AV_TH))
s('2.10', type='requirement', rung='none', force='should', level='none', appliesTo='institutions offering the subject', addressee='provider',
  verbs=['supporting'], about='basic support services for students', domain='none', award=BOTH,
  para='The support set out in 2.9 (screening, specialist help, mentors, reasonable adjustments, help with claims, accessible curricula) should be the minimum services for students, and the list is not complete.',
  prac='Treat screening for learning differences, specialist support, mentoring, reasonable adjustments, help with external claims and accessible curricula as the minimum support you offer.',
  ben=('n/a', 'a duty on the institution; the student meets it as support they can ask for'),
  aaw=aaw('2.10', 'Present this as a should-level duty on the institution, setting the services listed in 2.9 as a floor, under the accessibility theme.',
          'that the list is exhaustive or that it is a student outcome', 'paras 2.8, 2.9 and 2.12'),
  aad=aad('staff review student support or a student asks what help exists', HOW_P,
          'Which of these services can your students reach today, and how would a student find them?', AV_P))
s('2.12', type='requirement', rung='none', force='should', level='none', appliesTo='assessment in the subject', addressee='provider',
  verbs=['sit', 'present', 'made'], about='adjustments for presentation-based design assessment', domain='none', award=BOTH,
  find='2.12 Specific adjustments for the types of assessments associated with these courses should sit alongside the expectations for adjustments to exams and assessments detailed above at any education establishment. With regard to a design module, for example, to create a convincing studio or client engagement scenario, students are expected to verbally and visually present their design and technology solutions to the assessment tasks they are set. For students with learning differences or conditions such as anxiety, adjustments can be made to the nature of these presentations, and can, for instance, include a progression across an academic year from one-on-one sessions to a growing number of peers being present at each subsequent presentation to boost confidence.',
  para='Adjustments suited to the subject\'s own assessments, such as presenting design work in person, should sit beside the usual exam adjustments; for students with learning differences or anxiety, presentations can build from one-to-one sessions to larger audiences over the year.',
  prac='Plan adjustments for design presentations as well as for exams: for example, let a student with anxiety start with one-to-one crits and build up to a full audience across the year.',
  ben=('n/a', 'a duty on assessment design; a student may ask for the adjustment'),
  aaw=aaw('2.12', 'Present this as a should-level duty on assessment design under the accessibility theme.',
          'that the example given is the only acceptable adjustment', 'paras 2.11, 2.13 and 3.20'),
  aad=aad('staff design a studio crit or a student worries about presenting work', HOW_P,
          'How could the presentation be staged so the student builds confidence step by step?', AV_P))
s('2.14', type='requirement', rung='none', force='should', level='none', appliesTo='institutions offering the subject', addressee='provider',
  verbs=['making'], about='digital poverty and individual circumstances', domain='none', award=BOTH,
  find='Such considerations should always be mindful of the circumstances of individual students, with progressive higher education providers making use of funding support for those experiencing forms of digital poverty, including access to suitable equipment, and data and bandwidth provision.',
  para='Remote and blended learning widen access, but their use should always take account of each student\'s situation, with funding used to help those short of equipment, data or bandwidth.',
  prac='When moving teaching online or blended, check each student\'s access to equipment, data and bandwidth and use available funds to close the gaps.',
  ben=('n/a', 'a duty on the institution; the student meets it as support with equipment and data'),
  aaw=aaw('2.14', 'Present this as a should-level duty on the institution under the accessibility theme.',
          'that blended delivery is required', 'paras 2.13 and 2.18'),
  aad=aad('a team plans blended delivery or a student lacks equipment', HOW_P,
          'Which students on the course might lack a suitable device, data or connection, and what fund could help?', AV_P))
s('2.19', type='expectation', rung='none', force='will', level='none', appliesTo='students of the subject', addressee='learner',
  verbs=['undertake', 'demonstrate', 'address'], about='a design project or dissertation with critical analysis of risks and ethics',
  domain='subject-skill', award=BOTH,
  find="Within Architectural Technology courses, there is an expectation that students will undertake a design project and/or a dissertation. This part\n\n14\n\nof the student's learning requires them to demonstrate critical analysis, evaluation and reflection to address potential risks and ethical issues associated with a proposed project.",
  para='Students are expected to complete a design project, a dissertation or both, showing critical analysis, evaluation and reflection on the risks and ethical questions a proposed project raises.',
  prac='Students will complete a design project, a dissertation or both, in which they analyse, evaluate and reflect critically on the risks and ethics of a proposal.',
  ben='You will complete a design project, a dissertation or both, in which you analyse and reflect critically on the risks and ethical questions your proposal raises.',
  aaw=aaw('2.19', 'Present this as an expected outcome in the issuer\'s will, for honours and master\'s courses.',
          'that both a project and a dissertation are required, or that the form is fixed', 'paras 3.12, 3.17 and 3.22 and para 4.7 (item 5)'),
  aad=aad('a student chooses a final project or asks what it must cover', HOW_S,
          'What risks and ethical questions does your proposal raise? How will your project show that you weighed them?', AV_TH))
s('3.5', type='expectation', rung='none', force='will', level='none', appliesTo='students of the subject', addressee='learner',
  verbs=['develop'], about='design, technology, management and practice in context', domain='understanding', award=BOTH,
  find="It is anticipated that all Architectural Technology degrees will develop students' knowledge and critical understanding relating to design, technology, management and practice within a national and international context.",
  para='All degrees in the subject are expected to develop knowledge and critical understanding of design, technology, management and practice in UK and international settings.',
  prac='Students will gain knowledge and critical understanding across all four aspects (design, technology, management, practice), set in UK and international contexts.',
  ben='You will build knowledge and a critical understanding of design, technology, management and practice, in the UK and abroad.',
  aaw=aaw('3.5', 'Present this as an expected outcome in the issuer\'s will for all degrees in the subject; it adds management to the three aspects named in 2.5.',
          'that it sets separate standards beyond those in section 4', 'paras 2.5 and 4.4 and para 4.6 (items 1 to 3)'),
  aad=aad('a student asks what the four aspects of the subject are', HOW_S,
          'Which of the four aspects do you feel strongest in, and which have you met least?', AV_TH))
s('3.15', type='outcome', rung='none', force='will', level='fheq:7', appliesTo="master's students in the subject", addressee='learner',
  verbs=['develop'], about="professional, ethical and practical issues at master's level", domain='understanding', award=MAS,
  find='Students will further develop their subject with a consideration of professional, ethical, and practical issues.',
  para='Master\'s students will deepen their subject while weighing its professional, ethical and practical questions.',
  prac='Master\'s students will extend their command of the subject and weigh its professional, ethical and practical questions as they do so.',
  ben='At master\'s level, you will take your subject further while weighing the professional, ethical and practical questions it raises.',
  aaw=aaw('3.15', 'Present this as an expected outcome in the issuer\'s will for master\'s students, at FHEQ Level 7 (SCQF 11).',
          'that it applies at honours level', f'paras 3.14 and 3.16, para 4.7 and the master\'s descriptor {FR7}.b3'),
  aad=aad('a master\'s student plans their study or a team describes its master\'s aims', HOW_S,
          'Which professional or ethical question in your specialism do you want to explore further?', AV_TH))
s('3.17', type='outcome', rung='none', force='will', level='fheq:7', appliesTo="master's students in the subject", addressee='learner',
  verbs=['develop', 'completing', 'communicate'], about="an advanced research or design project, communicated professionally", domain='subject-skill', award=MAS,
  find='Students will develop their research skills further completing an advanced research or design project. Students are challenged to think in critical, creative and applied ways, devise research questions, design and conduct a research methodology, and produce original knowledge which will be important to the discipline. As well as conducting their own research project, students will communicate their research professionally to the academic and/or professional community using professional written, oral and visual means.',
  para='Master\'s students will strengthen their research skills through an advanced research or design project, thinking critically and creatively, framing questions, designing a method and producing original knowledge, and will present the work to academic or professional audiences in writing, speech and visuals.',
  prac='Master\'s students will complete an advanced research or design project with their own questions and method, aiming at original knowledge, and will present it professionally in written, spoken and visual forms.',
  ben='At master\'s level, you will carry out an advanced research or design project with your own questions and methods, aim to add something new to the field, and present it professionally in writing, in person and visually.',
  aaw=aaw('3.17', 'Present this as an expected outcome in the issuer\'s will for master\'s students, at FHEQ Level 7.',
          'that every master\'s project must be research rather than design', f'para 3.22, para 4.7 (item 5), para 3.7 (item 8) and the descriptors {FR7}.b2 and {FR7}.b3'),
  aad=aad('a master\'s student shapes a research question or plans how to present findings', HOW_S,
          'What is your question, and what method will answer it? Who outside the course should hear your findings, and in what form?', AV_TH))
s('3.19', type='requirement', rung='none', force='should', level='none', appliesTo='courses in the subject', addressee='provider',
  verbs=['contain', 'reflect', 'support', 'enable', 'demonstrate'], about='an explicit assessment strategy', domain='none', award=BOTH,
  para='Courses should have a clear assessment strategy in their design that follows the learning outcomes, supports learning, lets students show rising attainment and matches the teaching methods used.',
  prac='Write an explicit assessment strategy into the course design, tied to the outcomes and the teaching methods, that lets students show progress level by level.',
  ben=('n/a', 'a duty on course design'),
  aaw=aaw('3.19', 'Present this as a should-level duty on course design.',
          'that it prescribes particular assessment types', 'paras 3.18, 3.20 and 3.21'),
  aad=aad('a team prepares for validation or reviews assessment', HOW_P,
          'Can you show, module by module, which outcome each task assesses and how the demand rises across the years?', AV_P))
s('3.20', type='requirement', rung='none', force='should', level='none', appliesTo='assessment in the subject', addressee='provider',
  verbs=['include'], about='an accessible mix of assessment methods', domain='none', award=BOTH,
  find='The assessment strategies and vehicles of assessment of Architectural Technology courses should include a mix of methods that are, overall, accessible to students from varying educational and cultural backgrounds within different learning situations.',
  para='Assessment in the subject should use a mix of methods that, taken together, students from different educational and cultural backgrounds can access.',
  prac='Use a varied mix of assessment methods so that, across the course, students from different educational and cultural backgrounds are not shut out.',
  ben=('n/a', 'a duty on assessment design'),
  aaw=aaw('3.20', 'Present this as a should-level duty on assessment design, under the accessibility theme; the next sentence (3.20.s2) carries a must.',
          'that every single task must suit every student', 'paras 2.12, 2.13 and 3.21'),
  aad=aad('a team reviews the balance of its assessment types', HOW_P,
          'Would a student from a different educational background meet tasks they recognise somewhere in each year?', AV_P))
s('3.20.s2', type='requirement', rung='none', force='must', level='none', appliesTo='assessment in the subject', addressee='provider',
  verbs=['considered', 'ensuring'], about='adjustments discussed with the student', domain='none', award=BOTH,
  find='Where individual students may be disadvantaged by particular assessment methods, adjustments to those assessments must be considered in discussion with the student concerned, while ensuring fairness across the full cohort.',
  para='Where a method of assessment may disadvantage a student, adjustments must be considered together with that student, keeping the whole cohort fairly treated.',
  prac='If an assessment method could disadvantage a student, you must discuss possible adjustments with them, while keeping things fair for the rest of the cohort.',
  ben=('n/a', 'a duty on the course; the student takes part in the discussion it requires'),
  aaw=aaw('3.20, second sentence', 'Present this as a must-level duty on the course under the accessibility theme: adjustments have to be considered, with the student.',
          'that an adjustment must always be granted', 'paras 2.9, 2.12 and 3.20'),
  aad=aad('a student says a task puts them at a disadvantage, or staff handle an adjustment request',
          'With staff, frame it as a must: the conversation with the student has to happen; with a student, say they can expect to be asked what would help.',
          'Has the student been asked what would help? Does the change keep the task fair for the others?', AV_P))
s('3.21', type='requirement', rung='none', force='should', level='none', appliesTo='courses in the subject', addressee='provider',
  verbs=['use', 'reflect'], about='a range of assessment methods matched to outcomes', domain='none', award=BOTH,
  find='Architectural Technology courses should use a range of assessment methods during the course that reflect the range of learning outcomes.',
  para='Courses should use varied assessment methods that match the variety of their learning outcomes; the ten methods listed after it are an indication of practice, not a checklist.',
  prac='Match the variety of assessment methods to the variety of learning outcomes; the listed methods (design projects, exams, reports, presentations, portfolios and others) show current practice, not a required set.',
  ben=('n/a', 'a duty on course design'),
  aaw=aaw('3.21', 'Present this as a should-level duty on course design; its list of methods is indicative only.',
          'that every listed method must appear in a course', 'paras 3.19, 3.20 and 3.22'),
  aad=aad('a team audits its assessment types', HOW_P,
          'Which outcomes are assessed only by one kind of task? Which listed methods have you not tried?', AV_P))
s('4.2', type='requirement', rung='none', force='should', level='fheq:6', appliesTo='higher education providers', addressee='provider',
  verbs=['refer'], about='Annex D for performance above threshold', domain='none', award=HON,
  para='Most students will do far better than threshold; each provider decides what evidence shows this and should refer to the degree classification descriptions in Annex D for FHEQ Level 6 and FQHEIS Level 10.',
  prac='When setting marking criteria above the pass, refer to Annex D\'s descriptions of the four honours classifications rather than to this statement, which stops at threshold.',
  ben=('n/a', 'a duty on the provider in setting classification criteria'),
  aaw=aaw('4.2', 'Present this as a should-level duty on the provider for honours degrees, at FHEQ Level 6 (FQHEIS Level 10).',
          'that the statement itself defines the classes', 'the Annex D bands in std:doc:qaa-fheq-2024-framework (SL6; for example qaa/fheq-2024/annex-d/summary/r1/3rd) and para 4.6'),
  aad=aad('a team writes grade descriptors or asks what a first looks like in the subject', HOW_P,
          'Which Annex D band does each of your grade descriptors draw on? Where does the subject\'s own detail enter?', AV_P))
s('4.4', type='expectation', rung='none', force='will', level='none', appliesTo='students of the subject', addressee='learner',
  verbs=['enable', 'become'], about='fluency in design, technology, management and practice', domain='knowledge', award=BOTH,
  find='It is anticipated that all courses in Architectural Technology will enable students to become conversant with the main aspects of the subject (that is, design, technology, management and practice).',
  para='All courses are expected to make students fluent in the four main aspects of the subject: design, technology, management and practice.',
  prac='Students will become fluent in the four main aspects of the subject (design, technology, management, practice); the standards are met by showing understanding of these and applying them.',
  ben='You will become at home in the four main parts of the subject: design, technology, management and practice.',
  aaw=aaw('4.4', 'Present this as an expected outcome in the issuer\'s will for honours and master\'s students, the frame for the threshold lists in 4.6 and 4.7.',
          'that it sets a level beyond threshold', 'paras 2.5, 3.5, 4.6 and 4.7'),
  aad=aad('a student asks what the course is meant to make them good at', HOW_S,
          'Which of the four, design, technology, management or practice, could you explain best to someone outside the field?', AV_TH))

# ---------------------------------------------------------------- 3.6 honours course aims (should; "courses should typically be designed to allow students to understand how to")
L36 = dict(type='expectation', rung='none', force='should', level='fheq:6', appliesTo='honours courses and their students', addressee='both', award=HON)
def a36(i, beside, when, ask, **k):
    k['aaw'] = aaw(f'3.6 (item {i})', 'Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10).',
                   'that it is a threshold standard or a condition of the award', beside)
    k['aad'] = aad(when, 'With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve.', ask, AV_SH)
    s('3.6.b%d' % i, **L36, **k)
a36(1, 'para 4.6 (items 5 and 8) and the honours descriptor qaa/fheq-2024/4.15.b6', 'a student plans a whole design from concept to completion',
    'How does your scheme balance cost, sustainability and efficiency from concept to handover?',
    verbs=['create'], about='economical, sustainable processes and solutions from concept to completion', domain='subject-skill',
    para='Courses should help students learn to devise economical, environmentally sustainable, efficient processes and design solutions for complex design and construction problems, from concept to completion, to optimise how buildings are produced and perform.',
    prac='Design the course so students learn to produce economical, sustainable and efficient solutions to complex design and construction problems, carried from concept through to completion.',
    ben='Your course should teach you to create cost-effective, sustainable and efficient design solutions to complex building problems, from the first idea to the finished project.')
a36(2, 'para 3.7 (items 1 and 4) and para 4.6 (item 8)', 'a student asks how design can answer the climate emergency',
    'Which design decisions in your project cut carbon most, and how do you know?',
    verbs=['adopt', 'respond', 'minimising'], about='innovative design for the climate emergency', domain='subject-skill',
    para='Courses should help students learn to take innovative design approaches that answer the climate emergency and cut the effect of building on natural and built environments, reducing carbon emissions.',
    prac='Give students practice in innovative design that responds to the climate emergency and reduces carbon and environmental harm.',
    ben='Your course should teach you to use new design approaches that respond to the climate emergency and cut carbon emissions.')
a36(3, 'para 4.8 (items 9, 10 and 12) and qaa/fheq-2024/4.15.b8', 'a student works on drawings, reports or a presentation',
    'Which forms of communication, drawn, written, digital or spoken, are you least confident in?',
    verbs=['develop', 'mastering'], about='graphical, written, digital and oral communication', domain='generic-skill',
    para='Courses should help students learn to build a wide range of communication skills, graphical and written, by hand and digitally, and to master oral presentation for any setting.',
    prac='Develop students\' communication across drawing, writing, manual and digital media, and their spoken presentation to public and private audiences.',
    ben='Your course should help you communicate well through drawings, writing and digital media, by hand and on screen, and present confidently to any audience.')
a36(4, 'para 4.6 (items 2 and 9)', 'a student meets digital design management or retrofit work',
    'How would you manage the design process for a retrofit compared with a new building?',
    verbs=['manage'], about='managing design and construction with digital technologies', domain='subject-skill',
    para='Courses should help students learn to manage design and construction by integrating architectural technology and digital tools, for new buildings and for retrofit.',
    prac='Teach students to manage the design and construction process using architectural technology and digital tools, on new-build and retrofit work.',
    ben='Your course should teach you to manage design and construction using digital tools, both for new buildings and for updating existing ones.')
a36(5, 'para 4.6 (item 1) and para 4.7 (item 1)', 'a student considers the wider context of a site or brief',
    'What social, economic or political factors on this site would change your design?',
    verbs=['respond'], about='responding to wider context, including climate change', domain='understanding',
    para='Courses should help students learn to respond quickly and intelligently to social, economic, environmental, technical, cultural and political contexts, climate change included, at every scale from local to international.',
    prac='Help students read and respond to the wider setting of a project (its social, cultural, economic, political, technical and environmental sides), climate change included, from local to global.',
    ben='Your course should teach you to respond thoughtfully to the wider context of a project, from local to global, including climate change.')
a36(6, 'para 4.6 (items 5 and 7)', 'a student prepares technical drawings or specifications',
    'How do you check that your design information meets the relevant standards and law?',
    verbs=['adopt', 'satisfies', 'integrating'], about='accurate design information that meets standards', domain='subject-skill',
    para='Courses should help students learn to work systematically in producing accurate design information that meets standards and law, integrating envelope and interior with structure, fabric and services.',
    prac='Teach a systematic method for producing accurate design information that complies with standards and law and coordinates envelope, interior, structure, fabric and services.',
    ben='Your course should teach you to produce accurate design information that meets standards and the law, fitting the outside, inside, structure and services together.')
a36(7, 'para 4.6 (item 9)', 'a student meets information management or building operation',
    'How could the information you produce help the people who run and maintain the building safely?',
    verbs=['adopt', 'optimise'], about='managing the building life cycle with information systems', domain='subject-skill',
    para='Courses should help students learn strategies that use information management systems to run the building life cycle well, for safety and use.',
    prac='Give students strategies for using information management systems to manage a building across its life cycle, for safety and use.',
    ben='Your course should teach you to use information systems to manage a building well across its whole life, for safety and everyday use.')
a36(8, 'para 4.6 (item 10)', 'a student asks how to keep up with new technology',
    'Which emerging technology or practice could change how your project is built or maintained?',
    verbs=['embrace'], about='new concepts, technologies and practices', domain='understanding',
    para='Courses should help students learn to take up new concepts, technologies and practices that affect long-term production, performance and upkeep of buildings, new and existing.',
    prac='Prepare students to adopt new concepts, technologies and practices that bear over time on how buildings are produced, how they perform and how they are maintained.',
    ben='Your course should help you take up new ideas, technologies and practices that affect how buildings are made, perform and are maintained over time.')
a36(9, 'para 4.6 (item 4)', 'a student works on an existing building',
    'What did your survey of the existing structure reveal, and how did it shape your proposal?',
    verbs=['evaluate', 'ensure'], about='diagnosing existing structures', domain='subject-skill',
    para='Courses should help students learn to assess existing structures through building diagnostics and pathology so that solutions suit the existing structure, fabric and services.',
    prac='Teach building diagnostics and pathology so students can assess existing structures and make proposals that fit them.',
    ben='Your course should teach you to diagnose the condition of existing buildings so that your designs suit what is already there.')
a36(10, 'para 4.6 (item 7) and paras 1.2 and 4.8 (item 15)', 'a student considers fire or life safety in a design',
    'Where in your design did health and safety thinking start, and what does it mean for the people who maintain it?',
    verbs=['embed'], about='health and safety from first principles to occupation', domain='subject-skill',
    para='Courses should help students learn to build health and safety practice in from first principles through occupation and maintenance, fire and life safety and legislation among them.',
    prac='Teach students to embed health and safety, including fire and life safety and the law, from first design principles through occupation and maintenance.',
    ben='Your course should teach you to build health and safety, including fire and life safety, into your designs from the start through to how the building is used and maintained.')
a36(11, 'para 4.6 (item 2)', 'a student asks about professional practice, clients or procurement',
    'How would you manage a client relationship and work with other professionals on this project?',
    verbs=['develop'], about='business and management skills for practice', domain='generic-skill',
    para='Courses should help students learn to build business and management skills, covering industry and professional standards, client engagement, procurement and work with other professionals, service providers and authorities.',
    prac='Develop students\' business and management skills: professional and industry standards, clients, procurement and working with other professionals and authorities.',
    ben='Your course should help you build business and management skills, from working with clients and other professionals to how projects are procured.')
a36(12, 'para 1.23, para 4.8 (item 15) and the EDI Vision Statement (1.21 to 1.26)', 'inclusion comes up in teamwork or design choices',
    'How does your team make sure everyone has a fair chance to contribute?',
    verbs=['embrace', 'promote', 'ensure'], about='promoting equality, diversity and inclusion', domain='generic-skill',
    para='Courses should help students learn to take up and champion equality, diversity and inclusion so that people are treated fairly and given fair chances.',
    prac='Help students adopt and champion equality, diversity and inclusion so that treatment and opportunity are fair.',
    ben='Your course should help you champion equality, diversity and inclusion, so that people are treated fairly and get fair chances.')
a36(13, 'para 3.6 (item 12) and para 4.8 (item 16)', 'a student works in a diverse group or asks about bias',
    'Where might unconscious bias shape who gets heard in your group, and what would you change?',
    verbs=['recognise', 'respect', 'celebrate', 'create', 'understand', 'prevent'], about='respecting difference and preventing unconscious bias', domain='generic-skill',
    para='Courses should help students learn to recognise and value difference, make settings where all feel welcome and valued whatever their identity, and understand and guard against unconscious bias.',
    prac='Help students value difference, build welcoming settings for people of every identity, and understand and counter unconscious bias.',
    ben='Your course should help you value people\'s differences, make everyone feel welcome whoever they are, and notice and guard against your own unconscious bias.')
a36(14, 'para 4.8 (item 17) and para 1.24', 'conduct, ethics or social justice arise in project work',
    'What ethical choice did your last project involve, and who did it affect?',
    verbs=['behave', 'demonstrating'], about='ethical, professional and responsible conduct', domain='generic-skill',
    para='Courses should help students learn to act ethically, professionally and responsibly, aware of social justice and ethics and working collaboratively and communicating well.',
    prac='Help students conduct themselves ethically, professionally and responsibly, aware of social justice, working collaboratively and communicating effectively.',
    ben='Your course should help you act ethically, professionally and responsibly, with an eye to social justice, working well with others and communicating clearly.')

# ---------------------------------------------------------------- 3.7 master's added subject-specific abilities (no modal: "to be demonstrated")
L37 = dict(type='outcome', rung='none', force='describes', level='fheq:7', appliesTo="master's graduates in the subject", addressee='learner', award=MAS)
def a37(i, beside, when, ask, **k):
    k['aaw'] = aaw(f'3.7 (item {i})', 'Present this as an additional subject-specific ability shown at master\'s level, FHEQ Level 7 (SCQF 11); the text states it without a modal verb (Part E).',
                   'that it applies to honours graduates', beside)
    k['aad'] = aad(when, 'With a master\'s student, say it plainly in the second person; with staff, frame it as something the master\'s course has to give students room to show.', ask, AV_TH)
    s('3.7.b%d' % i, **L37, **k)
a37(1, f'para 3.6 (item 2), para 4.7 and the master\'s descriptor {FR7}.b5', 'a master\'s student weighs sustainability or inclusion in a design decision',
    'What evidence did you weigh before your last sustainable or inclusive design choice?',
    verbs=['make', 'influence'], about='critically informed choices for sustainable, inclusive design', domain='subject-skill',
    para='Make choices grounded in critical thought about the factors that shape the delivery of sustainable and inclusive design.',
    prac='Master\'s graduates make critically grounded choices on the factors shaping sustainable and inclusive design.',
    ben='At master\'s level, you can make well-argued choices about what shapes sustainable and inclusive design.')
a37(2, f'para 4.6 (item 4) and {FR7}.b4.2', 'a master\'s student studies building fabric, envelope or indoor comfort',
    'Which design methods for the envelope have you compared, and what did they show about comfort and health?',
    verbs=['research', 'analyse', 'appraise', 'identify'], about='appraising fabric and envelope methods for healthy buildings', domain='subject-skill',
    para='Research, analyse and critically judge design methods for building fabric and envelope, and find how they bear on a healthy, comfortable indoor environment.',
    prac='Master\'s graduates investigate and critically judge design methods for fabric and envelope and trace their effect on health and comfort indoors.',
    ben='At master\'s level, you can research and critically judge ways of designing a building\'s fabric and envelope, and show how they affect health and comfort inside.')
a37(3, f'para 4.7 (item 2) and {FR7}.b1', 'a master\'s student explains advanced technology, materials or services',
    'How would you argue for a new material or system in a way an expert would accept?',
    verbs=['articulate'], about='articulating advanced technology linked to sustainability and inclusion', domain='subject-skill',
    para='Explain, with critical judgement, the growth of more complex technology, construction, materials and services tied to sustainability and to advances in the built environment and community, inclusive design among them.',
    prac='Master\'s graduates explain critically the development of more complex technology, construction, materials and services in relation to sustainability, inclusive design and wider community advances.',
    ben='At master\'s level, you can explain critically how more advanced technology, materials and services develop in relation to sustainability, inclusion and the wider community.')
a37(4, f'para 3.7 (items 1 and 7) and {FR7}.b5', 'a master\'s student meets trade-offs in sustainable design',
    'Where did sustainability theory meet a practical constraint in your project, and how did you resolve it?',
    verbs=['acquire', 'applying'], about='complexity and constraints of sustainable design', domain='understanding',
    para='Gain critical awareness of how the parts of sustainable design depend on one another and of the limits met when theory is put into practice at different scales.',
    prac='Master\'s graduates understand critically how sustainable design\'s parts interlock and the constraints on applying its theory at scales from building to district.',
    ben='At master\'s level, you understand how the parts of sustainable design depend on each other and why theory meets limits in practice at different scales.')
a37(5, f'para 3.6 (item 2) and {FR7}.b1', 'a master\'s student considers climate, resources and the natural world',
    'How do your choices of method and material tie back to climate and natural resources?',
    verbs=['examine'], about='technology, construction and materials in relation to climate and resources', domain='understanding',
    para='Examine critically how architectural technology relates design and construction methods, materials and components to climate, the natural world and resources.',
    prac='Master\'s graduates examine critically how the discipline links construction methods, materials and components to climate, nature and resources.',
    ben='At master\'s level, you can examine critically how building methods and materials relate to the climate, the natural world and its resources.')
a37(6, f'para 4.7 (item 2) and {FR7}.b1', 'a master\'s student reviews emerging sustainable technologies',
    'Which sources did you use to judge a new technology, and how far do you trust each?',
    verbs=['demonstrate', 'using'], about='sustainable design principles and emerging technologies', domain='knowledge',
    para='Show critical awareness of the principles of sustainable design and of new technologies and ideas, drawing on many kinds of source.',
    prac='Master\'s graduates show critical awareness of sustainable design principles and emerging technologies, drawn from a wide range of sources.',
    ben='At master\'s level, you show critical awareness of sustainable design principles and new technologies, drawing on many sources.')
a37(7, f'para 4.7 (item 4) and {FR7}.b4.1', 'a master\'s student judges a design or theory at a larger scale',
    'How would you judge the spatial, technical and social qualities of a scheme at the scale of its neighbourhood?',
    verbs=['evaluate', 'form'], about='judging theory and the qualities of sustainable design at scale', domain='subject-skill',
    para='Evaluate theoretical approaches critically and reach reasoned judgements on how a sustainable design works in space, appearance, technique and society at the scale of wider development.',
    prac='Master\'s graduates evaluate theories critically and judge the spatial, aesthetic, technical and social qualities of sustainable design in its wider setting.',
    ben='At master\'s level, you can critically weigh theories and judge how a sustainable design works spatially, visually, technically and socially in its wider setting.')
a37(8, f'para 3.17, para 4.7 (item 5) and {FR7}.b2', 'a master\'s student plans a dissertation or research project',
    'What are your research objectives, and which established method fits them best?',
    verbs=['define', 'evaluate', 'apply', 'pursuing'], about='research objectives and methods', domain='subject-skill',
    find='define objectives pertinent to the chosen architectural technology research problem, critically evaluate and apply established techniques of research and enquiry in pursuing those research objectives.',
    para='Set objectives for a chosen research problem in the subject, then judge critically and use established research techniques to meet them.',
    prac='Master\'s graduates set research objectives for their problem and critically choose and apply established research techniques to pursue them.',
    ben='At master\'s level, you can set objectives for a research problem in your field and choose and use established research methods to meet them.')

# ---------------------------------------------------------------- 4.6 honours threshold (rung list)
L46 = dict(type='threshold', rung='threshold', force='threshold', level='fheq:6', appliesTo='honours graduates at threshold', addressee='learner', award=HON)
def t46(i, beside, when, ask, **k):
    k['aaw'] = aaw(f'4.6 (item {i})', 'Present this as a threshold standard: every honours graduate in the subject is expected to have reached it, at FHEQ Level 6 (FQHEIS Level 10, spine:6).',
                   'that it describes a good or typical degree, or that it is a regulatory requirement', beside)
    k['aad'] = aad(when, HOW_S, ask, AV_TH)
    s('4.6.b%d' % i, **L46, **k)
TH6 = 'To reach the threshold for your honours degree, '
t46(1, f'para 4.7 (item 1), the honours descriptor {FR6}.b1 and the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/3rd', 'a student studies context, regulation or policy',
    'Which social, economic or legal factor most shaped your last project, and at what scale?',
    verbs=['inform', 'influence'], about='the wider factors shaping the discipline', domain='understanding',
    para='At threshold, the graduate shows grasp of the wider forces (social, economic, environmental, political, legal, ethical and technical) acting on the discipline and its practice at local, regional and global scale.',
    prac='At threshold, honours graduates understand the social, economic, environmental, political, legal, ethical and technical forces on the discipline, from local to global.',
    ben=TH6 + 'you will show that you understand the social, economic, environmental, political, legal, ethical and technical forces on your field, locally and globally.')
t46(2, f'para 3.6 (item 11) and {FR6}.b9.1', 'a student asks about professional roles, procurement or contracts',
    'What does a principal designer do, and how does the procurement route change your role?',
    verbs=[], about='professional conduct, practice, design leadership, procurement and contracts', domain='knowledge',
    para='At threshold, the graduate shows grasp of professional conduct and ethics, how practice works, design leadership and management roles (such as lead or principal designer, design and information management), procurement routes and contract administration.',
    prac='At threshold, honours graduates know professional conduct and ethics, practice, design leadership and management roles, procurement and contract administration.',
    ben=TH6 + 'you will show that you know how to behave professionally and ethically, how practice runs, what design leaders and managers do, and how projects are procured and contracts run.')
t46(3, f'para 4.6 (item 4) and {FR6}.b1', 'a student studies building elements, systems and materials',
    'How do the elements of the building you are designing work together to serve its function?',
    verbs=['used', 'contribute'], about='building technologies and how elements interrelate', domain='knowledge',
    para='At threshold, the graduate shows grasp of building technologies and how elements, systems, components, materials and methods fit together across building types, in new construction and adaptation, and serve the building\'s functions.',
    prac='At threshold, honours graduates know construction technologies and how elements, systems, components and materials interact across building types and serve their function.',
    ben=TH6 + 'you will show that you understand how building parts, systems and materials fit together in different kinds of building and what each does.')
t46(4, f'para 3.6 (item 9) and {FR6}.b1', 'a student works on building physics, pathology or an existing building',
    'Which principles of building physics explain the defect or design choice in front of you?',
    verbs=['drive'], about='design principles, building science and values for new and existing buildings', domain='understanding',
    para='At threshold, the graduate shows grasp of architectural and technical design principles, building science (the basics of building physics and pathology) and the values guiding work on new and existing buildings, such as conservation, renovation and adaptation.',
    prac='At threshold, honours graduates understand design principles, the basics of building physics and pathology, and the values behind work on new and existing buildings.',
    ben=TH6 + 'you will show that you understand design principles, the basic science of how buildings behave and decay, and what guides work on old and new buildings.')
t46(5, f'para 3.6 (items 1, 2 and 6) and {FR6}.b6', 'a student details a design or asks how far detailing must go',
    'Can you take one junction in your design from first principles to a buildable detail, and say why it performs?',
    verbs=['designing', 'detail'], about='holistic design and detailing from first principles', domain='subject-skill',
    para='At threshold, the graduate shows the ability to design as a whole and detail from first principles for production, performance and sustainability, responding to regulation, health and safety, wellbeing and new sustainable technologies.',
    prac='At threshold, honours graduates design holistically and detail from first principles for production, performance and sustainability, meeting regulation, safety and wellbeing.',
    ben=TH6 + 'you will show that you can design a building as a whole and work out its details from first principles, so it can be built, performs well and is sustainable, safe and healthy.')
t46(6, f'{FR6}.b7 and the Annex D cell qaa/fheq-2024/annex-d/cognitive/r3/3rd', 'a student works from a brief or meets a client',
    'Whose needs does the brief serve, and how did you decide the scope of the project?',
    verbs=['analysing', 'interpreting', 'evaluating', 'determine'], about='client, user and stakeholder needs and project scope', domain='subject-skill',
    para='At threshold, the graduate shows the ability to work with client, user and stakeholder needs, analysing a development and reading its context to set a fitting project scope.',
    prac='At threshold, honours graduates analyse client, user and stakeholder needs and the setting of a development to define its scope.',
    ben=TH6 + 'you will show that you can work out what clients, users and others need, analyse the proposal and its setting, and decide what the project should cover.')
t46(7, f'para 3.6 (item 10) and {FR6}.b9.2', 'a student considers risk, compliance or fire safety',
    'Which hazards did you find in your design, and how does your solution manage them over the building\'s life?',
    verbs=['identifying', 'analysing', 'evaluating', 'ensure'], about='health and safety, hazards and risk over the life cycle', domain='subject-skill',
    para='At threshold, the graduate shows the ability to work within regulatory health and safety requirements, finding, analysing and judging hazards and risks when designing, to secure health, safety, welfare and security over a building\'s life, compliance and enforcement included.',
    prac='At threshold, honours graduates apply regulatory health and safety requirements, assessing hazards and risks in design for safety and security across the building life cycle.',
    ben=TH6 + 'you will show that you can spot and assess hazards and risks in your designs and keep people safe and secure throughout a building\'s life, within the law.')
t46(8, f'para 3.7 (item 1) and {FR6}.b3.1', 'a student designs for resilience, sustainability or inclusion',
    'How does your design hold up as a whole system and in the detail, and for whom?',
    verbs=['creating'], about='resilient, sustainable, inclusive solutions', domain='subject-skill',
    para='At threshold, the graduate shows the ability to produce design solutions that are resilient, sustainable and inclusive, both as complete systems and in detail, for varied situations, informed by current thinking and by climate change.',
    prac='At threshold, honours graduates create resilient, sustainable and inclusive solutions, whole and detailed, informed by current knowledge and climate change.',
    ben=TH6 + 'you will show that you can create designs that are resilient, sustainable and inclusive, both as a whole and in detail, with climate change in mind.')
t46(9, f'para 3.6 (item 7) and {FR6}.b8', 'a student uses BIM, modelling or shared information',
    'How did shared information change a decision in your last team project?',
    verbs=['apply', 'support'], about='modelling and information management in collaborative work', domain='subject-skill',
    para='At threshold, the graduate shows grasp of current approaches, processes and technologies for modelling, communicating and managing information, and applies them in collaborative work to support decisions driven by data.',
    prac='At threshold, honours graduates understand and apply current methods and tools for modelling and managing information in collaboration, for data-driven decisions.',
    ben=TH6 + 'you will show that you understand and use current tools for modelling and sharing information in a team, so decisions rest on data.')
t46(10, f'para 3.6 (item 8), {FR6}.b5 and the Annex D cell qaa/fheq-2024/annex-d/transferable/r5/3rd', 'a student plans their development or asks how to stay current',
    'Which new regulation or technology do you need to learn next, and what is your plan?',
    verbs=['inform', 'maintain', 'accommodate'], about='staying current through reflection and development planning', domain='generic-skill',
    find='current and emerging topics, technologies and practices (including regulations and standards) that inform the architectural technology discipline through self-reflection, identification of personal development needs, and action planning to maintain awareness and currency, and to accommodate specialisation in light of new and emerging professional environments.',
    para='At threshold, the graduate shows awareness of current and new topics, technologies and practices, regulations and standards included, kept up through reflecting on oneself, naming development needs and planning action, so as to stay current and to specialise.',
    prac='At threshold, honours graduates track current and emerging topics, technology, regulation and standards, and use reflection and development planning to stay current and specialise.',
    ben=TH6 + 'you will show that you keep up with new topics, technologies, rules and standards by reflecting on your own needs and planning how to develop.')

# ---------------------------------------------------------------- 4.7 master's threshold (rung list, added to 4.6)
L47 = dict(type='threshold', rung='threshold', force='threshold', level='fheq:7', appliesTo="master's graduates at threshold", addressee='learner', award=MAS)
def t47(i, beside, when, ask, **k):
    k['aaw'] = aaw(f'4.7 (item {i})', 'Present this as a threshold standard for a master\'s degree in the subject, at FHEQ Level 7 (SCQF 11, spine:7), held on top of the honours list in para 4.6.',
                   'that it describes a merit or distinction, or that it applies to honours graduates', beside)
    k['aad'] = aad(when, 'With a master\'s student, say it plainly in the second person; with staff, frame it as the least every master\'s graduate has to show.', ask, AV_TH)
    s('4.7.b%d' % i, **L47, **k)
TH7 = 'To reach the threshold for your master\'s degree, '
t47(1, f'para 4.6 (item 1) and the master\'s descriptor {FR7}.b1', 'a master\'s student reads history or theory of the discipline',
    'Which theory best explains how your area of practice got where it is today?',
    verbs=['inform', 'influence'], about='critical awareness of context and underpinning theories', domain='knowledge',
    para='At threshold, the master\'s graduate shows critical awareness of the past and present context and of the social, economic, environmental, political, legal, ethical and technical theories shaping practice.',
    prac='At threshold, master\'s graduates show critical awareness of historical and current context and of the theories behind practice.',
    ben=TH7 + 'you will show critical awareness of your field\'s history and present context and of the theories that shape its practice.')
t47(2, f'para 3.7 (item 6) and {FR7}.b1', 'a master\'s student explores digital construction or other trends',
    'Which current trend in the field do you understand best, and what are its limits?',
    verbs=[], about='current and emerging trends such as digital construction', domain='knowledge',
    para='At threshold, the master\'s graduate shows systematic understanding and critical awareness of present and emerging trends, digital construction among them.',
    prac='At threshold, master\'s graduates understand systematically and critically the current and emerging trends in the field, such as digital construction.',
    ben=TH7 + 'you will show a systematic, critical understanding of current and emerging trends in your field, such as digital construction.')
t47(3, f'{FR7}.b4.2 and {FR7}.b5', 'a master\'s student chooses how to tackle a complex problem',
    'Which methods did you consider for this problem, and why did you reject the others?',
    verbs=['dealing'], about='evaluating methods for complex problems', domain='subject-skill',
    para='At threshold, the master\'s graduate shows the ability to weigh up suitable methods for handling complex problems.',
    prac='At threshold, master\'s graduates evaluate which methods suit complex problems.',
    ben=TH7 + 'you will show that you can weigh up which methods suit complex problems.')
t47(4, f'{FR7}.b3 and {FR7}.b6', 'a master\'s student builds an argument or critique',
    'Where in your argument did you go beyond the sources to say something of your own?',
    verbs=['applied', 'working'], about='independent analysis with some originality', domain='subject-skill',
    para='At threshold, the master\'s graduate shows independent analysis of complex ideas, used to drive critical discussion, with some originality.',
    prac='At threshold, master\'s graduates analyse complex concepts independently and bring some originality to critical discussion.',
    ben=TH7 + 'you will show that you can analyse complex ideas on your own and add something original to critical debate.')
t47(5, f'paras 3.17 and 3.22 and {FR7}.b2', 'a master\'s student plans the major project',
    'What will your major project show about your grasp of the discipline?',
    verbs=['informed'], about='a major design work or substantial research project', domain='subject-skill',
    find='completion of a major piece of design work, or substantial research project, informed by thorough understandings of the discipline.',
    para='At threshold, the master\'s graduate has completed a major design work or a substantial research project grounded in a thorough grasp of the discipline.',
    prac='At threshold, master\'s graduates complete a major design or substantial research project based on thorough disciplinary understanding.',
    ben=TH7 + 'you will complete a major design or research project that rests on a thorough understanding of your field.')

# ---------------------------------------------------------------- 4.8 honours generic skills (should be able to)
L48 = dict(type='outcome', rung='none', force='should', level='fheq:6', appliesTo='honours graduates of the subject', addressee='learner', award=HON, domain='generic-skill')
def g48(i, beside, when, ask, **k):
    k['aaw'] = aaw(f'4.8 (item {i})', 'Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should.',
                   'that it is subject-specific, or that it is a must', beside)
    k['aad'] = aad(when, 'With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show.', ask, AV_SH)
    s('4.8.b%d' % i, **L48, **k)
SH = 'By the end of your honours degree, you should be able to '
g48(1, 'the Annex D cell qaa/fheq-2024/annex-d/transferable/r2/3rd', 'group work is planned or goes wrong',
    'What task did you own in your last group project, and did you deliver it?',
    verbs=['perform'], about='teamwork on assigned tasks',
    para='Should be able to carry out the tasks given to them within a team.', prac='Honours graduates should be able to complete the tasks they are given as team members.',
    ben=SH + 'carry out your share of the work in a team.')
g48(2, 'the Annex D cell qaa/fheq-2024/annex-d/cognitive/r1/3rd', 'a student researches a topic',
    'Which sources did you combine, and how did they fit together?',
    verbs=['bring'], about='combining information from several sources',
    para='Should be able to gather information and material from varied sources into one whole.', prac='Honours graduates should be able to combine information and material from several sources.',
    ben=SH + 'pull together information and material from different sources.')
g48(3, f'{FR6}.b7', 'a student starts a project or brief',
    'What is the real problem here, and what question would you ask first?',
    verbs=['identify'], about='identifying problems and questions',
    para='Should be able to spot problems and the questions they raise.', prac='Honours graduates should be able to identify problems and frame questions.',
    ben=SH + 'spot problems and work out the right questions to ask.')
g48(4, 'the Annex D cell qaa/fheq-2024/annex-d/cognitive/r1/3rd', 'a student handles data or facts',
    'What does this data tell you, and what does it not?',
    verbs=['undertake'], about='analysing factual information',
    para='Should be able to analyse information of a factual kind.', prac='Honours graduates should be able to analyse factual information.',
    ben=SH + 'analyse facts and data.')
g48(5, 'the Annex D cell qaa/fheq-2024/annex-d/cognitive/r2/3rd', 'a student reviews others\' work or literature',
    'Where is this author\'s argument strongest, and where is it weakest?',
    verbs=['recognise'], about='judging others\' arguments',
    para='Should be able to see where the arguments of other people are strong and where weak.', prac='Honours graduates should be able to judge the strengths and weaknesses of others\' arguments.',
    ben=SH + 'see what is strong and what is weak in other people\'s arguments.')
g48(6, 'the Annex D cell qaa/fheq-2024/annex-d/knowledge/r3/3rd', 'a student writes a literature review',
    'How would you sum up what is known on your topic in a page?',
    verbs=['produce'], about='synthesising what is known on a topic',
    para='Should be able to draw together what is currently known about a given subject or topic.', prac='Honours graduates should be able to synthesise the current state of knowledge on a topic.',
    ben=SH + 'sum up and draw together what is known about a topic.')
g48(7, 'the Annex D cell qaa/fheq-2024/annex-d/transferable/r3/3rd', 'a student works alone between supervisions',
    'What can you take forward on your own before we next meet?',
    verbs=['undertake'], about='working independently with guidance',
    para='Should be able, with guidance, to carry out tasks on their own.', prac='Honours graduates should be able to work on tasks independently, with guidance available.',
    ben=SH + 'work on tasks on your own, with guidance when you need it.')
g48(8, 'the Annex D cell qaa/fheq-2024/annex-d/transferable/r5/3rd', 'a student receives feedback',
    'What did the last feedback ask you to change, and what did you change?',
    verbs=['reflect', 'make'], about='reflection and using feedback',
    para='Should be able to review their own progress and act on the feedback given.', prac='Honours graduates should be able to reflect on their progress and use feedback.',
    ben=SH + 'reflect on how you are progressing and act on the feedback you get.')
g48(9, 'the Annex D cell qaa/fheq-2024/annex-d/transferable/r1/3rd', 'a student presents or discusses work',
    'How did your audience react, and what would make your point clearer?',
    verbs=['express'], about='communicating verbally and non-verbally',
    para='Should be able to communicate well in speech, in other forms, or both.', prac='Honours graduates should be able to communicate effectively verbally, non-verbally or both.',
    ben=SH + 'express yourself clearly, in speech and in other ways.')
g48(10, f'{FR6}.b8', 'a student explains an argument to others',
    'Could someone outside the field follow your argument? Where might they lose the thread?',
    verbs=['present'], about='presenting so others understand',
    para='Should be able to set out knowledge or an argument so other people can follow it.', prac='Honours graduates should be able to present knowledge or an argument clearly to others.',
    ben=SH + 'present what you know, or an argument, so others can follow it.')
g48(11, 'the Annex D cell qaa/fheq-2024/annex-d/transferable/r1/3rd and para 4.6 (item 9)', 'a student handles information digitally',
    'Which digital tool do you use to organise and present information, and how well?',
    verbs=['use', 'collate', 'analyse', 'select', 'present'], about='digital information handling',
    para='Should be able to use suitable digital systems to gather, analyse, choose and present information.', prac='Honours graduates should be able to gather, analyse, choose and present information with suitable digital systems.',
    ben=SH + 'use the right digital systems to gather, analyse, choose and present information.')
g48(12, 'the Annex D cell qaa/fheq-2024/annex-d/practical/r4/3rd', 'a student prepares a presentation',
    'What visual or media support will make your presentation clearer?',
    verbs=['deliver', 'utilising'], about='presentations with visual aids and media',
    para='Should be able to give presentations supported by visual aids and media.', prac='Honours graduates should be able to deliver presentations using visual aids and multimedia.',
    ben=SH + 'give presentations using visuals and multimedia.')
g48(13, 'the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/3rd', 'a student meets new ideas or unfamiliar material',
    'What is the main new idea here, in your own words?',
    verbs=['demonstrate', 'comprehend'], about='grasping new ideas and information',
    para='Should be able to show they can grasp new ideas or information when met.', prac='Honours graduates should be able to show they understand new ideas or information.',
    ben=SH + 'show that you can grasp new ideas and information.')
g48(14, 'the Annex D cell qaa/fheq-2024/annex-d/knowledge/r3/3rd', 'a student surveys or describes material, a building or a sample',
    'What do you see here, and how would you describe it precisely?',
    verbs=['demonstrate', 'recognising', 'describing'], about='recognising and describing material',
    para='Should be able to show skill in identifying and describing material.', prac='Honours graduates should be able to show skill in recognising and describing material.',
    ben=SH + 'show skill in recognising and describing what you are looking at.')
g48(15, 'para 1.23, para 3.6 (items 10 and 12) and para 4.6 (item 7)', 'workplace safety or inclusion comes up',
    'Why do health and safety and inclusion both matter in a design office or on site?',
    verbs=['understand'], about='health and safety and EDI at work',
    para='Should be able to understand why health and safety, and equality, diversity and inclusion, matter at work.', prac='Honours graduates should be able to explain why health and safety, and equality, diversity and inclusion, matter in the workplace.',
    ben=SH + 'understand why health and safety, and equality, diversity and inclusion, matter at work.')
g48(16, 'paras 1.29 and 1.36 and para 3.6 (item 13)', 'current debates on sustainability, careers or decolonisation arise',
    'Which current debate in the field do you have a view on, and what is it?',
    verbs=['appreciate', 'engage'], about='current debates on sustainability, employability and global perspectives',
    para='Should be able to value and take part in current debates on sustainability, employability and global outlooks, decolonisation and anti-racism included.', prac='Honours graduates should be able to appreciate and join current debates on sustainability, on employability and on global outlooks, decolonisation and anti-racism among them.',
    ben=SH + 'understand and join current debates on sustainability, careers and global perspectives, including decolonisation and anti-racism.')
g48(17, 'para 3.6 (item 14) and paras 1.24 and 1.30', 'ethics or sustainable behaviour arises',
    'What would acting sustainably and ethically look like in your next project?',
    verbs=['appreciate', 'act', 'display'], about='acting sustainably and ethically',
    para='Should be able to see the need to act sustainably and to behave and conduct themselves ethically.', prac='Honours graduates should be able to appreciate the need for sustainable action and show ethical behaviour.',
    ben=SH + 'see why acting sustainably matters and behave ethically.')

# ---------------------------------------------------------------- gradeOf: only threshold rungs, for different awards: no links
GRADE = {}
TH = {'1.23': 'theme:edi', '1.29': 'theme:esd', '1.30': 'theme:esd', '1.33': 'theme:esd', '1.34': 'theme:esd',
      '1.40': 'theme:enterprise', '2.10': 'theme:accessibility', '2.12': 'theme:accessibility', '2.14': 'theme:accessibility'}

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.15; 4.2'),
                  dict(id='fqheis:10', role='cites', locator='D1, 2.15; 4.2'),
                  dict(id='fheq:7', role='inferred', locator="D1, 2.2; 3.7; 4.5; 4.7 (master's degrees; no level named): std:doc:qaa-fheq-2024-framework S5, 4.17"),
                  dict(id='fqheis:11', role='inferred', locator="D1, as fheq:7: std:doc:qaa-fqheis-2024-framework S5 (shared descriptor 4.17)")],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.15: "FHEQ Level 6; FQHEIS Level 10"; 4.2)'),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='inferred: std:doc:qaa-fheq-2024-framework S5 (shared descriptor; Table 1); Part E')])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['front matter', '1.14', '1.19', '1.20', '1.21', '1.22', '1.23', '1.24', '1.25', '1.26', '2.4', '2.8', '3.3', '3.6', '3.7', '4.6', '4.8']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.19', '2.8', '2.9', '2.10', '2.11', '2.12', '2.13', '2.14', '3.20']),
      dict(id='theme:esd', role='carries', carriedIn=['front matter', '1.1', '1.3', '1.11', '1.12', '1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '3.2', '3.6', '3.7', '4.6', '4.8']),
      dict(id='theme:enterprise', role='carries', carriedIn=['front matter', '1.35', '1.36', '1.37', '1.38', '1.39', '1.40', '4.8'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-architectural-technology-2019-benchmarks (not held)', note='the fourth edition, 2019, named in the back matter; earlier editions 2014, 2007 and 2000'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the degree classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees, cited in 4.2 for performance above threshold'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ Level 6 (2.15; 4.2); exit awards CertHE and DipHE (2.17)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS Level 10 (2.15; 4.2); four-year Scottish honours (2.17)'),
      dict(rel='cites', target='std:doc:qaa-advancehe-esd-2021-guidance', note='1.27: the core skills align with its learning outcomes'),
      dict(rel='cites', target='std:doc:qaa-enterprise-2018-guidance', note='1.35: its definitions of enterprise and entrepreneurship education'),
      dict(rel='refersTo', target='CIAT accreditation requirements and Standards of Education (not yet ingested)', note='front matter; 1.20; 1.39; 2.5; 2.25'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance (not yet ingested)', note='front matter'),
      dict(rel='readWith', target='QAA Subject Benchmark Statements for Town and Country Planning; Architecture; Landscape Architecture; Engineering; Land, Construction, Real Estate and Surveying', note='front matter: a suite of built environment subjects; the editions held (std:doc:qaa-town-and-country-planning-2024-benchmarks, std:doc:qaa-architecture-2026-benchmarks, std:doc:qaa-landscape-architecture-2024-benchmarks, std:doc:qaa-engineering-2023-benchmarks, std:doc:qaa-land-construction-real-estate-and-surveying-2024-benchmarks) are later than those current in 2022')]
S8 = dict(published='2022-03', lastReviewed='none-stated', reviewCycle='none-stated',
          consultation='none-stated; the 2022 advisory group is listed (D1, back matter)', replacedBy='none')

SB1 = ['An essential professional design discipline about how buildings are put together and perform (structure, systems, materials, fabric and services), rooted in science and engineering (D1, 1.1, 1.17, 3.1).',
       'The link between design and construction, optimising production and long-term performance across the building life cycle (D1, 1.11, 1.12, 3.2).',
       'Four educational components, theoretical, experiential, professional and ethical, tied to design, technology and practice; four main aspects, design, technology, management and practice (D1, 1.17, 2.3, 4.4).',
       'Shaped now by building and life safety law, the climate emergency, retrofit and data-driven, digital working such as BIM (D1, 1.2, 1.3, 1.6, 1.7, 3.1).',
       'Vocational and competency based: its standards are threshold only, and a lead PSRB, CIAT, accredits courses and confers the protected title (D1, 1.15, 4.1, front matter).',
       'Inclusive design at its heart, with a record of widening participation (D1, 1.19, 1.23, 2.4, 3.3).']
SB2 = [dict(theme='theme:edi', inThisSubject='framed by the discipline\'s own EDI Vision Statement and the Equality Act 2010: wider participation, whole-life care for diverse end-users, inclusive design as a requirement on a par with health and safety; course aims on fairness and unconscious bias, generic skill on EDI at work (D1, 1.19 to 1.26, 3.6, 4.8)',
            statements=['1.23', '3.6.b12', '3.6.b13', '3.7.b1', '3.7.b3', '4.6.b8', '4.8.b15', '4.8.b16']),
       dict(theme='theme:accessibility', inThisSubject='a provider obligation onsite and online; a floor of support services; adjustments for presentation-led design assessment; digital routes for students short of money for models or of data and equipment (D1, 2.8 to 2.14, 3.20)',
            statements=['2.10', '2.12', '2.14', '3.20', '3.20.s2']),
       dict(theme='theme:esd', inThisSubject='headed Sustainability: the discipline\'s key part in a sustainable built environment, the three pillars, UNESCO\'s eight competencies aligned with outcomes, real cases and problem-based learning; carried into the climate-emergency aims and the sustainable design items at both awards (D1, 1.27 to 1.34, 3.6, 3.7, 4.6, 4.8)',
            statements=['1.29', '1.30', '1.33', '1.34', '3.6.b1', '3.6.b2', '3.7.b1', '3.7.b3', '3.7.b4', '3.7.b5', '3.7.b6', '3.7.b7', '4.6.b5', '4.6.b8', '4.8.b16', '4.8.b17']),
       dict(theme='theme:enterprise', inThisSubject='headed Entrepreneurship, enterprise and employment: QAA\'s 2018 definitions, live and community projects, employer engagement required by CIAT accreditation, apprenticeships and the aspirATion network (D1, 1.35 to 1.40)',
            statements=['1.40', '4.8.b16'])]
SB3 = dict(areas=[dict(component='3.1', gloss='the design function: systems, materials and components for new and existing buildings; BIM across the life cycle'),
                  dict(component='3.2', gloss='performance, comfort, energy, waste and carbon; collaboration and social and ethical awareness'),
                  dict(component='3.3', gloss='inclusive design; health, safety and welfare; the needs of all stakeholders'),
                  dict(component='3.4', gloss='identifying and evaluating requirements, social needs and life safety; new materials and modelling'),
                  dict(component='3.5', gloss='whole-life modelling, procurement and services; design, technology, management and practice'),
                  dict(component='3.6', gloss='fourteen honours aims, from sustainable design and detailing to ethics and EDI'),
                  dict(component='3.7', gloss='eight added master\'s abilities centred on sustainable and inclusive design and research')],
           practices=[dict(component='2.18', kind='teaching', gloss='full-time, sandwich, part-time, online, blended, apprenticeship and distance modes'),
                      dict(component='3.8', kind='teaching', gloss='case studies, live sites, project simulations, interdisciplinary projects'),
                      dict(component='3.9', kind='teaching', gloss='studio teaching, team and individual projects, problem-based learning with industry input'),
                      dict(component='3.11', kind='learning', gloss='simulated real projects, practical sessions, problem-based studio learning'),
                      dict(component='3.12', kind='learning', gloss='active and reflective learning; a final collaborative interdisciplinary project'),
                      dict(component='3.14', kind='learning', gloss='master\'s: critical understanding and learner-centred work joining theory and practice'),
                      dict(component='3.16', kind='learning', gloss='master\'s: advanced research, analytical and practical techniques'),
                      dict(component='3.18', kind='assessment', gloss='a wide range of methods suited to a vocational subject'),
                      dict(component='3.19', kind='assessment', gloss='an explicit assessment strategy tied to outcomes'),
                      dict(component='3.20', kind='assessment', gloss='accessible mix, adjustments, practical and portfolio work, formative and peer feedback'),
                      dict(component='3.21', kind='assessment', gloss='indicative list: long design projects, essays, exams, reports, oral and graphical presentations, other media, online tests, portfolios, placement reports'),
                      dict(component='3.22', kind='assessment', gloss='master\'s: the major design or research project as the key assessment')])
SB4 = dict(rungs=[dict(rung='threshold', leadIn='4.6', award=HON, items=10),
                  dict(rung='threshold', leadIn='4.7', award=MAS, items=5),
                  dict(rung='typical', leadIn='none', award='none', items=0),
                  dict(rung='excellent', leadIn='none', award='none', items=0)],
           rungBases=("threshold only (4.1 to 4.3): the standards are the baseline for all honours and master's graduates, apprenticeships included; "
                      "4.2 leaves performance above threshold to Annex D; 4.7's master's items are held in addition to 4.6's honours items. "
                      "Threshold items total 15 (10 honours, 5 master's)."),
           outcomeLists=[dict(leadIn='3.6', gloss='honours course aims: what students should learn how to do', items=14, award=['honours']),
                         dict(leadIn='3.7', gloss="additional subject-specific abilities at master's level", items=8, award=["master's"]),
                         dict(leadIn='4.8', gloss='generic skills of honours graduates', items=17, award=['honours'])],
           outcomes=[])
SB4A_FULL = []
SB5 = [dict(body="Chartered Institute of Architectural Technologists (CIAT)",
            says='the lead PSRB; bases its accreditation of honours and master\'s courses and its standards of education for Chartered Membership on the statement; alone awards the protected title Chartered Architectural Technologist; accredited graduates are exempt from its Standards of Education; Centre of Excellence status for providers offering both awards; uses inclusivity in assessing student work; requires links with the profession; runs the aspirATion network; accredits courses outside the UK (D1, front matter, 1.18, 1.20, 1.39, 2.5, 2.25)',
            requirements='not yet ingested (Part E)')]
SB6 = dict(themes=[dict(id='theme:edi', named='Equality, diversity and inclusion (EDI); the Architectural Technology EDI Vision Statement', carriedIn=S6[0]['carriedIn'], statements=SB2[0]['statements']),
                   dict(id='theme:accessibility', named='Accessibility', carriedIn=S6[1]['carriedIn'], statements=SB2[1]['statements']),
                   dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=S6[2]['carriedIn'], statements=SB2[2]['statements']),
                   dict(id='theme:enterprise', named='Entrepreneurship, enterprise and employment (front matter: employability, entrepreneurship and enterprise education)', carriedIn=S6[3]['carriedIn'], statements=SB2[3]['statements'])],
           frameworks=[dict(framework='fheq', levels=['fheq:6'], citedIn=['2.15', '4.2']),
                       dict(framework='scqf', levels=['fqheis:10'], citedIn=['2.15', '4.2'])],
           bodies=[dict(body='Chartered Institute of Architectural Technologists (CIAT)', citedIn=['front matter', '1.18', '1.20', '1.39', '2.5', '2.25']),
                   dict(body='Office for Students (its regulatory framework)', citedIn=['front matter']),
                   dict(body='Advance HE (co-author of the ESD guidance)', citedIn=['1.27']),
                   dict(body='UNESCO (key competencies for sustainability)', citedIn=['1.29'])],
           sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'], role='descriptions of the four honours classifications, for performance above threshold'),
                            dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='Education for Sustainable Development Guidance (Advance HE and QAA, March 2021)', citedIn=['1.27'], role='the core skills align with its suggested learning outcomes'),
                            dict(document='std:doc:qaa-enterprise-2018-guidance', named='QAA 2018 (Enterprise and Entrepreneurship Education)', citedIn=['1.35'], role='definitions of entrepreneurship education and enterprise'),
                            dict(document='QAA Quality Code, Advice and Guidance (not yet ingested: listed in Part E)', named='Advice and Guidance to support the Quality Code', citedIn=['front matter'], role='course design, teaching, external expertise, monitoring'),
                            dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
                            dict(document='other QAA Subject Benchmark Statements (S7 readWith)', named='Town and Country Planning; Architecture; Landscape Architecture; Engineering; and Land, Construction, Real Estate and Surveying', citedIn=['front matter'], role='a suite of built environment subjects, read for context and shared curricula'),
                            dict(document='Equality Act 2010 (law)', named='Equality Act 2010', citedIn=['1.20'], role='frames the EDI Vision Statement'),
                            dict(document="OfS regulatory framework; Quality Assessment Framework for Wales; Quality Enhancement Framework (Scotland)", named='as named', citedIn=['front matter'], role='the statement\'s regulatory status in each nation')])

B1 = [dict(slug='architectural-technology', definition='a professional design discipline about how buildings are put together and perform, grounded in science and engineering and linking design to construction (D1, 1.1, 1.11, 3.1)',
           beneficiaryDefinition='the field that works out how a building is put together, made and kept performing well', scopeNote='independent of, but beside, the other built environment disciplines', category='unknown', practices=['education']),
      dict(slug='inclusive-design', definition='design that puts people at the centre so every user can have the same experience of a building or place whatever their ability, age, gender or faith (D1, 2.4, 3.3)',
           beneficiaryDefinition='designing so that everyone can use and enjoy a place equally', scopeNote='a requirement of education and practice in the EDI Vision Statement (1.23)', category='unknown', practices=['education']),
      dict(slug='generalist-and-specialist-masters', definition="master's degrees differing in balance: generalist ones broader, specialist ones deeper (D1, 2.7)",
           scopeNote='both covered by the master\'s standards (4.5)', category='unknown', practices=['education']),
      dict(slug='threshold-standard', definition='the baseline performance expected of every honours and master\'s graduate (D1, 4.1, 4.3)',
           scopeNote='the only rung the statement states', category='unknown', practices=['education']),
      dict(slug='chartered-architectural-technologist', definition='the protected professional title only CIAT may award (D1, front matter)',
           scopeNote='reached after practice experience; accredited degrees exempt holders from CIAT\'s Standards of Education', category='unknown', practices=['education'])]
B2A = [dict(concept='architectural-technology', form='architectural technology', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
       dict(concept='inclusive-design', form='inclusive design', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
       dict(concept='generalist-and-specialist-masters', form="'generalist' and 'specialist' master's degrees", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='threshold-standard', form='threshold level of performance', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='chartered-architectural-technologist', form='Chartered Architectural Technologist', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific')]
B4 = []; B5 = []
D3 = [dict(citation='CIAT, Standards of Education and accreditation requirements for honours and master\'s courses', settles=['SB5', 'S7'], asked='2026-10-03', state='wanted')]

E = [
    'Rungs: threshold only, at two awards (4.6 honours, 10 items; 4.7 master\'s, 5 items, "in addition to" 4.6); no typical or excellent lists; above threshold is left to Annex D (4.2). Like Archaeology, unlike Psychology.',
    'Rungs: the lead-ins name the rung only in the headings ("(threshold)"); 4.6 uses plain present ("demonstrate"), 4.7 "can demonstrate". Both recorded with force threshold, from the headings and 4.1; "can" is outside the five force words.',
    'Rungs: 2.15 calls the generic skills "threshold-level", but 4.8\'s lead-in names no rung ("students should be able to"), so its 17 items are an outcome list with rung none and force should; for P3: move them to the threshold rung?',
    'gradeOf: none. The two threshold lists are for different awards, and no typical or excellent rung exists, so no outcome can be linked one rung below.',
    'Force: 3.7\'s master\'s list ("to be demonstrated ... are the ability to") has no modal; recorded force describes and listed here; for Abbott: read as will?',
    'Force: 3.6\'s course aims ("Courses should typically be designed to allow students to understand how to") taken as statements with force should and addressee both, since each item names what students learn; the ben versions keep should.',
    'Force, not taken as statements: 1.19 "Providers have a duty", 2.8 "have an obligation", 1.32 "need to ensure", 1.34 "need to involve" (inside a should paragraph that is taken), 1.13 "it is important", 2.15 "it is expected", 3.12 "is expected", 2.9 "an expectation of such institutions" (its items, as the list 2.10 calls basic services). For Abbott: should duty, obligation and expectation read as must or should?',
    'Force: 3.4 "must also recognise" binds project requirements, not courses or students: read as content (SB3 area), not a statement.',
    'S4: 3.20 split in two: 3.20 (should, the accessible mix) and 3.20.s2 (must, adjustments considered with the student), since one paragraph carries both modals; the id 3.20.s2 is ours, in the issuer\'s numbering.',
    'S4: 2.5 and 3.5 state the same expected outcome; 3.5 adds management. Both kept, each in its own paragraph; 4.4 restates the four aspects.',
    'S4, predictive "will" not taken: 1.14, 1.30 (second sentence, inside a taken should paragraph), 2.18 (courses "will offer" methods), 2.22, 2.23 and 2.24 (providers and examiners "will" use reference points and reviewers): descriptions of practice, not standards.',
    'Skeleton: the spans of 3.7.b8, 4.6.b10 and 4.7.b5 ran on into the next heading ("Teaching and learning"; "Benchmark standards for master\'s degrees (threshold)"; "Generic skills for Architectural Technology graduates"); recut with find. 1.34, 1.40, 2.12, 2.14, 2.19, 3.17 recut to drop trailing headings or to take the obliging sentence.',
    'S3: headings are run into the paragraph text above them by the extraction (for example "Purposes of an Architectural Technology degree" at the end of 1.10); SUB records them by range. A blank line before 3.13 may hide a lost sub-heading on master\'s teaching.',
    'S3: 2.3 repeats 1.17 almost whole and 3.3 repeats 2.4 almost whole: the issuer\'s repetition.',
    'Edition: the cover reads March 2022, the colophon "Fifth edition, September 2022". Recorded as March 2022 (the cover); for P3.',
    'Levels: the statement names FHEQ Level 6 and FQHEIS Level 10 (2.15, 4.2) and no level for master\'s degrees; fheq:7 and fqheis:11 are inferred from the frameworks (std:doc:qaa-fheq-2024-framework S5, 4.17; shared descriptor), as is the crosswalk fheq:7 to fqheis:11.',
    'Levels: 2.17 names exit awards (Certificate and Diploma of Higher Education, fheq:4 and fheq:5) and four-year Scottish honours; not levels the statement covers, so not in levelsCovered.',
    'Subjects: HECoS 100121 architectural technology names the subject; CAH codes follow from it. The master\'s specialisms of 2.16 are recorded in statedSubjects, with HECoS codes only where the term matches (100120 architectural engineering, 100812 project management); Fire Safety (perhaps 100183 fire safety engineering) and Conservation (perhaps 100585 conservation of buildings) are inferred and left out of the front matter, for P3. HECoS 100584 building technology is a close neighbour, not named.',
    'SB5: CIAT\'s own requirements (accreditation, Standards of Education) are not yet ingested (D3).',
    'SB6: named outside the excluded matter but not bodies of the subject: Office for Students, Advance HE and UNESCO recorded in SB6 bodies; the back matter names the Disabled Students\' Commission, the Construction Industry Council, the British Standards Institution, the Institute for Apprenticeships and Technical Education and Skills Development Scotland (excluded matter, not recorded).',
    'SB6: the front matter names the cross-cutting themes as three ("equality, diversity and inclusion", "education for sustainable development", "employability, entrepreneurship and enterprise education"); accessibility is a section of its own (2.8 to 2.14). Building and life safety runs through the text as a subject theme with no shared theme id: a new id (theme:safety?) is for Abbott.',
    'S7: the built environment benchmarks it asks to be read with are held only in later editions than those current in 2022.',
    'Themes on statements: S4 `themes` tags only statements inside a theme\'s own paragraphs (TH); list items that carry a theme are in SB2 and SB6.',
    'S9: not researched in P1.',
    'Pattern against Psychology: threshold only, at two awards, with master\'s standards in the same document (benchmark open point 1); lead-ins without "will"; a should-list of course aims (3.6); a master\'s list with no modal (3.7); generic skills as a separate should list (4.8); the subject\'s own EDI Vision Statement inside section 1.',
]
