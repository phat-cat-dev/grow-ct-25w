# bm_content.py: run 0101, QAA Subject Benchmark Statement: Earth Sciences, Environmental Sciences and Environmental Studies (March 2022).
# std run agent. Templates: standards 0.8.0-draft, benchmark 0.6.0-draft, run layer 0.7.0-draft; brief BM-BRIEF 0.2.2.
# Every judgement for tools/bm_build.py. Written fresh from the held text alone (benchmark rule 6).

HON = "bachelor's with honours"
IMS = "integrated master's"
PGT = "master's"
SUBJ = 'Earth Sciences, Environmental Sciences and Environmental Studies'
def CITE(n):
    return f'QAA, 2022, {SUBJ} (ES3) Subject Benchmark Statement, para {n}'

# Exact text of each paragraph statement, trimmed of the sub-heading or page number the skeleton span ran on into.
F = {}
F['1.2'] = 'The wider context for this Subject Benchmark Statement is the ongoing climate emergency and biodiversity crisis, as well as other threats to the natural environment. These require action at every level, from global and national political commitment to practical measures at a local level. Graduates in ES3 subjects will be required to ensure actions and decisions are based on sound science, and that they take into account equity, equality, diversity and inclusivity to deliver long-term, sustainable solutions.'
F['1.5'] = 'Note that the term ‘environment’ as used throughout this document should be interpreted as inclusive in its scope and should be taken to include all livings things, both human and non-human.'
F['1.8'] = 'Equality, diversity and inclusivity (EDI) are integral to the ES3 disciplines, not only informing pedagogical practice but also as subject knowledge. Inclusion of diverse groups is critical to the development of subject learning communities, yet these groups may encounter multiple barriers to engagement. ES3 communities have a duty to confront and encourage the dismantling of all barriers to engagement and participation in our disciplines. Equality Impact Assessments may be a useful mechanism to explore these issues. ES3 communities can commit to creating safe, inclusive and supportive environments that value diversity and encourage discussion, learning and the co-production of ES3 curricula.'
F['1.9'] = 'EDI can be explored in discipline contexts and by challenging discipline identities and stereotypes, including the impact of colonialism, embedding diverse representation within curriculums, broadening interdisciplinary and cross-disciplinary perspectives and particularly valuing different cultural perspectives, ways of knowing and lived experience. The ES3 subjects are a route to justice through delivery of the UN Sustainable Development Goals and diverse perspectives are essential to confronting global grand challenges. To achieve this, academic programmes in ES3 disciplines cultivate graduates who are culturally aware, show ethical behaviour, consideration and respect and who can reflect on equality in the context of their discipline. They will also be proficient in systems thinking, flexibility, interdisciplinarity and open to different ways of thinking and practising.'
F['1.12'] = 'To support the inclusion of sustainable development within the ES3 disciplines, users should refer to the QAA and Advance HE Education for Sustainable Development Guidance to address teaching and learning for sustainable development, key competencies, learning outcomes and assessment within the curricula.'
F['1.16'] = 'To support the inclusion of employability, entrepreneurship and enterprise within the ES3 disciplines, users should refer to the QAA document Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers.'
F['2.2'] = 'In this Statement, we approach accessibility as the inclusive design of curriculum and pedagogy that does not exclude any individual from participation. Individuals and marginalised groups experience a variety of barriers to participation, many of which are intersectional. These barriers are purposefully addressed in the ES3 subjects so that all learners can equally access and thrive, with inclusive practices a pedagogical norm. While inclusive curriculum design should enable all learners to participate fully, flexibility is required, and reasonable adjustments may be needed in practice. The ES3 subjects are visual and graphic subjects traditionally underpinned by laboratory and field-based approaches, which can sometimes be exclusionary. Ensuring that all students can participate in such activities may require a mix of strategies, including careful design of curricula and field programmes and leveraging accessible technologies. Health, safety and well-being of participants should be included in risk assessments, including any specific risks a student with protected characteristics may face. A choice of blended learning through online learning and practical exercises can enable a wide range of learners to engage, making for effective teams and group work rather than reinforcing otherness.'
F['2.3'] = 'Over the course of a bachelor’s degree with honours (FHEQ Level 6; FQHEIS SCQF Level 10), a student studying for a degree in the ES3 subject area will progress from one year of study to the next, in line with the regulations and processes for each institution. However, it is expected that in each year, the attainment of certain levels of knowledge, expertise and experience are achieved. These will build towards the final achievement of meeting all of the threshold-level subject-specific and generic skills listed in this Statement. Integrated master’s degrees (FHEQ Level 7; FQHEIS SCQF Level 11) require one further academic year of study and it is expected that at the end of this further year, students are able to demonstrate increased critical thinking, evaluation skills and independence. In a standard three-year undergraduate honours degree course, students may exit earlier and be eligible for a Certificate of Higher Education, a Diploma of Higher Education or an honours degree, depending upon the levels of study completed to a satisfactory standard. Scottish bachelor’s degrees with honours are typically designed to include four years of study, which relates to the structure of Scottish primary and secondary education.'
F['2.4'] = 'Where relevant, upon graduation from an undergraduate degree, it would normally be expected that a student who had achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in Earth Science, Environmental Science, Environmental Studies or associated sustainability disciplines and would also be equipped for entering courses that cross and combine disciplines.'
F['2.5'] = 'Joint honours undergraduates will achieve elements of the specific and generic skills for the subject but will add others according to the subjects covered in a joint programme.'
F['3.14'] = 'This Subject Benchmark Statement does not specify which methods of teaching or learning should be employed in relevant courses; however, learning outcomes should be achievable through the methods utilised and clearly articulated to the learners.'
F['3.15'] = 'Teaching and learning are interlinked as part of the curriculum design process and methods chosen should be inclusive and appropriate to develop the knowledge and skills identified in sections 1 and 2. Research-led and enquiry-based courses may develop specific subject-based knowledge and skills.'
F['3.16'] = 'The ES3 subjects are characterised by the integration of practical work, especially field-based activities, with theoretical studies. Courses therefore offer all students opportunities for significant field-based learning and teaching to foster skills such as the ability to visualise and extrapolate data in three dimensions or understand the application of practical methodologies. Much advancement in knowledge and understanding in these subject areas is founded on accurate observation and recording in the field and the collection of empirical data for analysis. Developing field-related practical and research skills is therefore important for students wishing to pursue careers in ES3-related sectors. Field- based studies allow students to develop and enhance many graduate attributes and transferable skills, for example leadership, team working, problem-solving, self-management and interpersonal relationships, which are of value to their employability, entrepreneurship and active citizenship. Activities should be designed to be inclusive to all students. If required, reasonable adjustments should be arranged in order to enable all students to take part in practical work and fieldwork activities.'
F['3.17'] = 'ES3 subjects have sustainability at their core. Teaching and learning should be clearly underpinned by education for sustainable development to achieve positive graduate outcomes and teaching and learning methods should embody sustainability principles and solutions.'
F['4.2'] = "The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd."
F['4.7'] = 'In addition to the competencies developed over the course of their programme, graduates of integrated master’s courses will have gained significant specialism in a specific subject area through developing and leading an independent research project. Graduates of integrated master’s courses will demonstrate the ability to independently interrogate the relevant literature, applying ideas, techniques and data to a range of questions, demonstrating key skills and working independently to design and carry out a project to address important practical questions.'
F['4.8'] = 'At postgraduate (MSc or MA) level it is expected that students will build on the competencies listed above that are developed in their undergraduate studies but focus in greater depth on a specific aspect of the subject area, achieving knowledge and skills to enhance their employability.'

META = dict(
    run='0101', p1='2026-10-03 17:09',
    title='Subject Benchmark Statement Earth Sciences, Environmental Sciences and Environmental Studies',
    heading='Subject Benchmark Statement: Earth Sciences, Environmental Sciences and Environmental Studies (QAA, March 2022)',
    edition='March 2022 (fifth edition)', published='2022-03',
    status='current',
    supersedes='the fourth edition (2019), which QAA revised from the third (2014); the back matter names both',
    subjects=[
        dict(scheme='hecos', code='100394', label='earth sciences', basis='stated'),
        dict(scheme='hecos', code='100381', label='environmental sciences', basis='stated'),
        dict(scheme='hecos', code='100469', label='environmental management', basis='inferred'),
        dict(scheme='hecos', code='100395', label='geology', basis='inferred'),
        dict(scheme='cah', code='CAH26-01-06', label='earth sciences', basis='stated'),
        dict(scheme='cah', code='CAH26-01-04', label='environmental sciences', basis='stated'),
        dict(scheme='cah', code='CAH26-01-03', label='human geography', basis='inferred'),
        dict(scheme='cah', code='CAH26-01', label='geography, earth and environmental studies', basis='stated'),
        dict(scheme='cah', code='CAH26', label='geography, earth and environmental studies', basis='stated'),
    ],
    awards=[HON, IMS, PGT],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2022 revision with cross-cutting themes (this statement\'s fifth edition)',
    partsB='partial: no glossary of its own (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what a graduate in Earth sciences, environmental sciences or environmental studies (ES3) "
                     "knows and can do at the end of an honours degree, with shorter notes for integrated master's and taught master's awards. "
                     "It sets one rung only, the threshold, as four skill lists, and pairs it with content lists for each subject. "
                     "Reach for it when designing, reviewing or describing an ES3 course or its outcomes. It is not a curriculum, "
                     "not a professional body's accreditation standard and not a regulatory requirement in England."),
    summary=("Published by QAA in March 2022 as the fifth edition, the statement treats Earth sciences, environmental sciences and environmental "
             "studies together as ES3. It sets out the context (the climate and biodiversity crises), the common character of the subjects, "
             "their distinctive features, the content of each subject and its applications, teaching, learning and assessment, and threshold "
             "standards for honours graduates in four groups: intellectual skills, practical skills, communication skills and personal and professional skills. "
             "It states no typical or excellent rung and sends providers to Annex D for performance above the threshold. Integrated master's "
             "and taught master's graduates are described in two paragraphs. It carries the cross-cutting themes of equality, diversity and "
             "inclusion, accessibility, sustainability (ESD) and employability, entrepreneurship and enterprise, cites the FHEQ and the "
             "FQHEIS at levels 6 and 7 (10 and 11) and names five professional bodies."),
    authority=("reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised "
               "standard under the OfS framework; a key reference point in Wales and Scotland; part of quality requirements in Northern Ireland "
               "(D1, front matter: Relationship to legislation and regulation)"),
)

S2 = dict(
    governs=("what a graduate in Earth sciences, environmental sciences or environmental studies can be expected to know, do and understand "
             "at the end of their studies, and the nature of awards in the subjects (D1, front matter: About this Statement; 4.1)"),
    awards=["bachelor's degrees with honours (BSc, sometimes BA), placement years included", "integrated master's degrees (MSci)",
            "taught postgraduate degrees (MSc, sometimes MA)", "foundation degrees (FdSc): may find it useful, not covered as such"],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    statedScope=('"This Subject Benchmark Statement covers the subjects as delivered at bachelor\'s degree with honours level (including '
                 'degrees with placement years and generally leading to the award of BSc or sometimes BA), integrated master\'s degrees and '
                 'taught postgraduate degrees (generally leading to the award of MSci, MSc or sometimes MA)." (D1, front matter: About this Statement)'),
    statedSubjects=[
        dict(name='Earth Sciences', locator='(D1, title; 1.1; 3.1)', kind='subject',
             codes=[dict(scheme='hecos', code='100394', label='earth sciences'), dict(scheme='cah', code='CAH26-01-06', label='earth sciences')]),
        dict(name='Environmental Sciences', locator='(D1, title; 1.1; 3.4; 3.7)', kind='subject',
             codes=[dict(scheme='hecos', code='100381', label='environmental sciences'), dict(scheme='cah', code='CAH26-01-04', label='environmental sciences')]),
        dict(name='Environmental Studies', locator='(D1, title; 1.1; 3.4; 3.10)', kind='subject',
             codes=[dict(scheme='hecos', code='100469', label='environmental management')]),
        dict(name='ES3', locator='(D1, 1.1)', kind='subject', codes=[]),
        dict(name="joint honours", locator='(D1, 2.5)', kind='programme title', codes=[]),
        dict(name="integrated master's (MSci); postgraduate (MSc or MA)", locator='(D1, front matter; 2.3; 4.7; 4.8)', kind='programme title', codes=[]),
    ],
)

SECTIONS = {
    '1': 'Context and characteristics of an Earth Sciences, Environmental Sciences and Environmental Studies degree',
    '2': 'Distinctive features of an Earth Sciences, Environmental Sciences and Environmental Studies degree',
    '3': 'Content, structure and delivery',
    '4': 'Benchmark standards',
}
SUB = [
    ('1.1', '1.5', 'Context'), ('1.6', '1.7', 'Characteristics of an ES3 degree'), ('1.8', '1.9', 'Equality, diversity and inclusion'),
    ('1.10', '1.12', 'Sustainability'), ('1.13', '1.16', 'Employability, entrepreneurship and enterprise'),
    ('2.1', '2.1', 'Design'), ('2.2', '2.2', 'Accessibility'), ('2.3', '2.5', 'Progression'), ('2.6', '2.6', 'Flexibility'),
    ('2.7', '2.7', 'Partnership'), ('2.8', '2.10', 'Monitoring and review'),
    ('3.1', '3.3', 'Earth Sciences'), ('3.4', '3.6', 'Environmental Sciences and Environmental Studies'),
    ('3.7', '3.9', 'Environmental Sciences only content'), ('3.10', '3.12', 'Environmental Studies only content'),
    ('3.13', '3.17', 'Teaching and learning'), ('3.18', '3.22', 'Assessment'),
    ('4.1', '4.2', 'Introduction'), ('4.3', '4.3', 'Threshold level: Intellectual skills (knowledge and understanding)'),
    ('4.4', '4.4', 'Practical skills'), ('4.5', '4.5', 'Communication skills'), ('4.6', '4.8', 'Personal and professional skills'),
]
G = {
    '1.1': 'the three subjects named together as ES3',
    '1.2': 'climate and biodiversity crises as the setting; graduates base decisions on sound science and fairness',
    '1.3': 'why one statement serves several subjects',
    '1.4': 'environmental sciences and studies merged where possible; Earth science content unchanged',
    '1.5': 'environment read broadly, human and non-human life included',
    '1.6': 'nine shared traits of ES3 study',
    '1.7': 'professional bodies in the field and the five named',
    '1.8': 'EDI as subject matter and practice; a duty to remove barriers',
    '1.9': 'ways to explore EDI; graduates culturally aware and ethical',
    '1.10': 'sustainability as more than environment, central to ES3',
    '1.11': 'ESD defined, with the UNESCO vision and the SDGs',
    '1.12': 'users pointed to the joint ESD guidance',
    '1.13': 'employability and entrepreneurship defined; links with employers',
    '1.14': 'what Earth science employers seek',
    '1.15': 'what environmental employers seek',
    '1.16': 'users pointed to the enterprise guidance',
    '2.1': 'design: rooted in sustainability, practical, research-informed, decolonising',
    '2.2': 'accessibility as inclusive design; field and lab barriers; risk assessment',
    '2.3': 'yearly progression to the threshold; integrated master\'s year; exit awards; Scottish four-year degree',
    '2.4': 'second-class graduates ready for postgraduate study',
    '2.5': 'joint honours graduates reach part of the skills',
    '2.6': 'modes of study and possible specialisms',
    '2.7': 'students and external bodies as partners; work-based learning; apprenticeships',
    '2.8': 'monitoring, periodic review and awarding gaps',
    '2.9': 'external reviewers in periodic review',
    '2.10': 'external examiners and the statement\'s part in their advice',
    '3.1': 'Earth sciences: knowledge every graduate is anticipated to hold (18 items)',
    '3.2': 'Earth sciences: typical components',
    '3.3': 'Earth sciences: applications',
    '3.4': 'environmental sciences and studies: shared knowledge (20 items)',
    '3.5': 'environmental sciences and studies: typical components',
    '3.6': 'environmental sciences and studies: applications',
    '3.7': 'environmental sciences only: further knowledge (6 items)',
    '3.8': 'environmental sciences only: further components',
    '3.9': 'environmental sciences only: further applications',
    '3.10': 'environmental studies only: further knowledge (3 items)',
    '3.11': 'environmental studies only: further components',
    '3.12': 'environmental studies only: further applications',
    '3.13': 'teaching and learning defined',
    '3.14': 'methods open; outcomes reachable and made clear',
    '3.15': 'inclusive methods; research-led and enquiry-based courses',
    '3.16': 'fieldwork at the heart; inclusive activities and adjustments',
    '3.17': 'ESD to underpin teaching and learning',
    '3.18': 'assessment strategy; authentic assessment',
    '3.19': 'inclusive assessment linked to outcomes',
    '3.20': 'feedback, reflection, peer and self-assessment',
    '3.21': 'examples of authentic assessment',
    '3.22': 'multidisciplinary assessment grounded in ESD',
    '4.1': 'the threshold standards for honours defined',
    '4.2': 'most students exceed the threshold; Annex D for classes',
    '4.3': 'threshold: intellectual skills (9 items)',
    '4.4': 'threshold: practical skills (7 items)',
    '4.5': 'threshold: communication skills (5 items)',
    '4.6': 'threshold: personal and professional skills (13 items)',
    '4.7': 'integrated master\'s graduates: a specialism through an independent research project',
    '4.8': 'taught postgraduate students: greater depth in one aspect',
}
CTYPE = {
    '3.2': 'area', '3.3': 'area', '3.5': 'area', '3.6': 'area', '3.8': 'area', '3.9': 'area', '3.11': 'area', '3.12': 'area',
    '3.13': 'practice', '3.14': 'practice', '3.15': 'practice', '3.16': 'practice', '3.17': 'practice',
    '3.18': 'practice', '3.19': 'practice', '3.20': 'practice', '3.21': 'practice', '3.22': 'practice',
}
EXCLUDED = [
    dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional reference points',
         kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='section headings 1 to 4', heading='the four section heading lines', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: references, read for SB6 and D3'),
    dict(number='6', heading='Membership of the Advisory Groups (2022, 2019, 2014, 2007, 2000)', kind='other: back matter, read for S8 and supersedes'),
]

P = {}
def s(i, **k):
    P[i] = k

# ------------------------------------------------------------------ paragraph statements
def aaw_prov(n, about, force, nb):
    return (f"Treat para {n} as a duty on the course or provider, in '{force}' terms, about {about}; it is not an outcome a student has to show. "
            f"Cite it as {CITE(n)}. Do not call it statutory or regulatory, and do not rewrite it as a student learning outcome. "
            f"Set it beside {nb}.")
def aad_prov(about, q):
    return (f"Raise it with a programme team or teacher when {about} comes up in design, approval or review, framed for staff as something the course "
            f"ought to do. Ask: {q} Do not hand it to a student as something they must achieve, and do not read the paragraph out at length.")

s('1.2', find=F['1.2'], type='expectation', rung='none', force='will', level='none', appliesTo='graduates in ES3 subjects', addressee='learner',
  verbs=['ensure', 'deliver'], about='decisions grounded in sound science and fairness', domain='generic-skill', award=[HON, IMS, PGT],
  para=("Set against the climate emergency, biodiversity loss and other pressures on nature, which call for action from global policy to local practice, "
        "ES3 graduates will be required to make sure that actions and decisions rest on good science and weigh equity, equality, diversity and inclusion, "
        "so that solutions last and are sustainable."),
  prac=("Prepare students for a working world in which they will be required to ground decisions in sound science and to weigh equity and inclusion, "
        "so that the solutions they propose last; the climate and biodiversity crises are the setting for the whole course."),
  ben=("You will be expected, in your working life, to make sure that the decisions you take part in rest on sound science and treat people fairly, "
       "so that the solutions you help to build last."),
  aaw=(f"Treat para 1.2 as a stated expectation of ES3 graduates across all the awards covered, in 'will be required' terms: decisions grounded in sound science "
       f"that weigh fairness and inclusion and aim at lasting solutions. Cite it as {CITE('1.2')}. Do not present it as a threshold outcome from section 4 "
       "or as a professional licensing rule. Set it beside the threshold items 4.6.b13 and 4.3.b5 and the honours descriptor qaa/fheq-2024/4.15.b9.2 (spine:6)."),
  aad=("Raise it when a student or a programme team asks why the subjects matter now or what graduates are trusted to do. For a student, say plainly that you "
       "will be expected to base decisions on evidence and fairness; for staff, frame it as the purpose the course serves. Ask: Where in your work have you had "
       "to weigh evidence and fairness together before reaching a decision? Avoid reading the paragraph aloud or treating it as a graded outcome."))

s('1.5', find=F['1.5'], type='expectation', rung='none', force='should', level='none', appliesTo='readers and users of the statement', addressee='provider',
  verbs=['interpreted', 'include'], about='reading environment broadly', domain='none', award='none',
  para="The word environment, wherever the statement uses it, should be read broadly, so that it covers every living thing, human and non-human.",
  prac="Read environment, in every part of the statement, as covering all living things, people and other species alike, and carry that breadth into course documents.",
  ben=('n/a', 'a note to readers on how to read a term in the document, not a standard for the student'),
  aaw=(f"Treat para 1.5 as a reading instruction in 'should' terms: wherever the statement says environment, it means all living things, human and non-human. "
       f"Cite it as {CITE('1.5')} when you define the term in a course document. Do not narrow environment to the physical or natural world alone. "
       "Set it beside para 1.10, which says sustainability is not only about the environment."),
  aad=("Raise it when a programme team drafts outcomes or a teacher frames a topic and the word environment is doing a lot of work. Put it plainly to staff as "
       "a broad reading that takes in people and other species. Ask: Does your course use environment to include people, or only the natural world? "
       "Do not present it to a student as an outcome."))

s('1.8', find=F['1.8'], type='expectation', rung='none', force='describes', level='none', appliesTo='ES3 academic communities', addressee='provider',
  verbs=['confront', 'encourage', 'commit'], about='removing barriers to taking part in the disciplines', domain='none', award='none',
  para=("EDI belongs to the ES3 subjects both as how they are taught and as knowledge in its own right; diverse groups matter to learning communities "
        "but face many barriers, which ES3 communities have a duty to challenge and help take down, perhaps using equality impact assessments, "
        "and they can commit to safe, inclusive settings that welcome diversity and co-produced curricula."),
  prac=("Treat equality, diversity and inclusion as subject content and as practice; your teaching community carries a duty to challenge and help remove "
        "barriers to taking part, for example through equality impact assessments, and to build safe, inclusive spaces where curricula can be co-produced with students."),
  ben=('n/a', 'a duty on the academic community and the course, not a standard for the student'),
  aaw=(f"Treat para 1.8 as a duty on ES3 academic communities to challenge and help dismantle barriers to taking part; the word is duty, recorded here as "
       f"descriptive force because it is none of must, should, may or will. Cite it as {CITE('1.8')}. Do not call it a legal duty or a student outcome. "
       "Set it beside para 1.9, the student-facing outcome 4.6.b12 and para 2.2 on accessibility."),
  aad=aad_prov('barriers to taking part in ES3, equality impact assessments or co-produced curricula',
               'Which barriers to fieldwork, labs or class discussion have you identified, and what has the team done about them?'))

s('1.9', find=F['1.9'], type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of ES3 programmes', addressee='learner',
  verbs=['cultivate', 'reflect'], about='cultural awareness, ethics and openness to other ways of knowing', domain='generic-skill', award=[HON, IMS, PGT],
  para=("EDI can be explored by challenging the disciplines' identities and stereotypes, colonial legacies included, diversifying curricula and valuing other "
        "cultures' knowledge and lived experience; the subjects serve justice through the SDGs, so programmes develop graduates who are culturally aware, "
        "ethical and respectful and can reflect on equality; they will also think in systems, adapt, work across disciplines and stay open to other ways of thinking."),
  prac=("Use the discipline itself to explore EDI, by questioning its stereotypes and colonial history and valuing other knowledge systems; graduates will be "
        "culturally aware, ethical and respectful and able to reflect on equality in the subject; they will also think in systems, adapt and work across disciplines."),
  ben=("You will become culturally aware, act ethically and with respect, reflect on equality in your subject, think in terms of whole systems, adapt to change "
       "and stay open to ways of knowing that differ from your own."),
  aaw=(f"Treat para 1.9 as a stated outcome in 'will' terms for ES3 graduates generally, read here at honours level (FHEQ level 6, FQHEIS level 10). "
       f"Cite it as {CITE('1.9')}. Do not present it as one of the section 4 threshold items, though it overlaps them. "
       "Set it beside 4.6.b10, 4.6.b12 and 4.5.b3, and beside qaa/fheq-2024/4.15.b9.1 and spine:6 in std:ref:uk-framework."),
  aad=("Raise it when a student reflects on fieldwork with communities, on colonial history in the subject or on working with people from other disciplines. "
       "For a student, put it in plain words as qualities you will grow; for staff, as outcomes the curriculum should make room for. "
       "Ask: When did another culture's knowledge change how you read an environmental problem? Avoid reading the paragraph out or treating it as a checklist."))

s('1.12', find=F['1.12'], type='expectation', rung='none', force='should', level='none', appliesTo='users of the statement designing ES3 curricula', addressee='provider',
  verbs=['support', 'refer', 'address'], about='using the joint ESD guidance', domain='none', award='none',
  para="Those building sustainable development into ES3 courses should consult the joint QAA and Advance HE guidance on ESD for teaching, competencies, outcomes and assessment.",
  prac="When you build sustainable development into an ES3 curriculum, you should use the joint QAA and Advance HE ESD guidance for teaching, key competencies, outcomes and assessment.",
  ben=('n/a', 'a pointer for course designers, not a standard for the student'),
  aaw=aaw_prov('1.12', 'using the joint ESD guidance when building sustainable development into the curriculum', 'should',
               'std:doc:qaa-advancehe-esd-2021-guidance, paras 1.10 and 1.11 and the content items 3.1.b1 and 3.4.b1'),
  aad=aad_prov('education for sustainable development', 'Which of the ESD key competencies do your module outcomes and assessments already cover?'))

s('1.16', find=F['1.16'], type='expectation', rung='none', force='should', level='none', appliesTo='users of the statement designing ES3 curricula', addressee='provider',
  verbs=['support', 'refer'], about='using the enterprise and entrepreneurship guidance', domain='none', award='none',
  para="Those building employability, entrepreneurship and enterprise into ES3 courses should consult QAA's guidance on enterprise and entrepreneurship education.",
  prac="When you build employability, enterprise and entrepreneurship into an ES3 course, you should use QAA's enterprise and entrepreneurship education guidance.",
  ben=('n/a', 'a pointer for course designers, not a standard for the student'),
  aaw=aaw_prov('1.16', 'using the enterprise and entrepreneurship guidance', 'should', 'std:doc:qaa-enterprise-2018-guidance and paras 1.13 to 1.15'),
  aad=aad_prov('employability, enterprise or links with employers',
               'Where do students meet enterprise or employer-set tasks, and have you checked them against the guidance?'))

s('2.2', find=F['2.2'], type='expectation', rung='none', force='should', level='none', appliesTo='course and field programme design', addressee='provider',
  verbs=['addressed', 'enable', 'included'], about='accessible design, adjustments and inclusive risk assessment', domain='none', award='none',
  para=("Accessibility means designing curriculum and teaching so nobody is shut out; barriers, often overlapping, are tackled deliberately so all learners can "
        "take part and do well; inclusive design should let everyone take part, though flexibility and reasonable adjustments may still be needed; field and "
        "laboratory work can exclude, so courses may need several strategies and accessible technology; risk assessments should cover health, safety and "
        "well-being, including risks to students with protected characteristics; blended options help a wide range of learners."),
  prac=("Design curricula and field programmes so that no one is excluded: inclusive design should let all learners take part, with flexibility and reasonable "
        "adjustments where needed; plan for the barriers labs and fieldwork can raise and use accessible technology; make risk assessments cover health, "
        "safety and well-being, including risks a student with protected characteristics may face."),
  ben=('n/a', 'a duty on the course and provider; the student meets its effect, not a standard to reach'),
  aaw=aaw_prov('2.2', 'accessible curriculum and field design, reasonable adjustments and inclusive risk assessment', 'should',
               'para 3.16 on inclusive fieldwork, para 3.19 on inclusive assessment and the student-facing items 4.4.b4 and 4.6.b11'),
  aad=aad_prov('fieldwork, laboratory work or blended options for disabled students or students with protected characteristics',
               'Does your field programme risk assessment name the specific risks a student with protected characteristics might face?'))

s('2.3', find=F['2.3'], type='expectation', rung='none', force='will', level='fheq:6', appliesTo="honours and integrated master's students", addressee='learner',
  verbs=['progress', 'build', 'demonstrate'], about="progression to the threshold and the integrated master's year", domain='none', award=[HON, IMS],
  para=("Across an honours degree (at FHEQ level 6, or SCQF level 10 in Scotland) each student moves up year by year under each institution's rules, reaching set levels of "
        "knowledge, expertise and experience each year that build towards meeting every threshold subject-specific and generic skill; an integrated master's "
        "(FHEQ level 7; SCQF level 11) adds a year, after which students are able to show stronger critical thinking, evaluation and independence; early exit "
        "awards are possible, and Scottish honours degrees usually last four years."),
  prac=("Plan each year so attainment builds towards every threshold skill by the end of the honours degree (FHEQ level 6; SCQF level 10); in an integrated "
        "master's (FHEQ level 7; SCQF level 11), the extra year will leave students able to show stronger critical thinking, evaluation and independence."),
  ben=("Each year of your honours degree will build your knowledge and experience towards the full set of skills expected at graduation; if you take an "
       "integrated master's, your extra year will leave you thinking more critically, evaluating more sharply and working more independently."),
  aaw=(f"Treat para 2.3 as a stated expectation of progression in 'will' and 'are able to' terms: year-on-year attainment that builds to all the threshold "
       f"skills at honours (FHEQ level 6, FQHEIS level 10), and a further step at integrated master's (FHEQ level 7, FQHEIS level 11). Cite it as {CITE('2.3')}. "
       "Do not claim it fixes what each year must contain or that it sets a separate master's standard. Set it beside 4.1, 4.7, qaa/fheq-2024/4.15.b1, "
       "qaa/fheq-2024/4.17.b6 and the steps spine:6 and spine:7."),
  aad=("Raise it when a student asks how their years add up or a team maps outcomes across levels. For a student, explain in plain words that each year "
       "builds towards what you need by graduation; for staff, frame it as a progression design question. Ask: Which threshold skills does each year of the "
       "course build, and where does the master's year add independence? Do not read out the paragraph or treat its exit awards as targets."))

s('2.4', find=F['2.4'], type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='undergraduates with a second-class degree or above', addressee='learner',
  verbs=['equipped', 'undertaking', 'entering'], about='readiness for postgraduate and cross-disciplinary study', domain='none', award=HON,
  para=("Where it applies, a graduate with at least a second-class degree would normally be expected to be able and ready to go on to postgraduate study in "
        "ES3 or related sustainability fields, and to enter courses that combine disciplines."),
  prac=("A graduate with a second-class honours degree or better would normally be expected to be capable of and ready for postgraduate study in ES3 or "
        "related sustainability fields, including cross-disciplinary courses."),
  ben=("If you graduate with a second-class degree or higher, you would normally be ready to go on to postgraduate study in your subject, in a related "
       "sustainability field or on a course that combines disciplines."),
  aaw=(f"Treat para 2.4 as an expectation the statement words as 'would normally be expected', recorded as descriptive force: readiness for postgraduate "
       f"study for honours graduates at a 2:2 or above (FHEQ level 6). Cite it as {CITE('2.4')}. Do not present it as an entry rule for any postgraduate "
       "course or as a promise. Set it beside Annex D (qaa/fheq-2024/annex-d/summary) and qaa/fheq-2024/4.15.b9.3."),
  aad=("Raise it when a student asks whether their likely classification opens postgraduate study. In plain words and the second person, say that a "
       "second-class result or above normally leaves you ready, and that each course sets its own entry terms. Ask: Which postgraduate field are you "
       "looking at, and what does it ask for? Avoid treating it as a guarantee of entry."))

s('2.5', find=F['2.5'], type='outcome', rung='none', force='will', level='fheq:6', appliesTo='joint honours undergraduates', addressee='learner',
  verbs=['achieve', 'add'], about='joint honours and the skill lists', domain='none', award=HON,
  para="Students on joint honours will reach part of the subject-specific and generic skills for ES3 and add further skills from their other subject.",
  prac="Joint honours students will achieve some of the ES3 subject-specific and generic skills, with others drawn from the partner subject; map which ones each route covers.",
  ben="If you study ES3 in a joint honours degree, you will gain some of its subject and general skills and add others from your second subject.",
  aaw=(f"Treat para 2.5 as a stated outcome in 'will' terms for joint honours students at FHEQ level 6: they reach some, not all, of the ES3 skills. "
       f"Cite it as {CITE('2.5')}. Do not claim that joint honours graduates meet every threshold item in 4.3 to 4.6. "
       "Set it beside 4.1 and qaa/fheq-2024/4.15.i1 (honours meets the descriptor in full)."),
  aad=("Raise it when a joint honours student or team asks which ES3 skills apply. For a student, say plainly that you will gain part of the ES3 skills "
       "and others from your second subject; for staff, frame it as a mapping task. Ask: Which of the threshold skills in sections 4.3 to 4.6 does your "
       "ES3 half cover? Avoid implying they fall short of honours."))

s('3.14', find=F['3.14'], type='expectation', rung='none', force='should', level='none', appliesTo='ES3 courses', addressee='provider',
  verbs=['achievable', 'articulated'], about='outcomes reachable by the methods used and made clear', domain='none', award='none',
  para="The statement does not choose teaching or learning methods, but the outcomes should be reachable through the methods a course uses and set out clearly for learners.",
  prac="Choose your own teaching and learning methods, but check that students can reach the outcomes through them and that the outcomes are stated clearly to students.",
  ben=('n/a', 'a duty on the course; the student meets its effect, not a standard to reach'),
  aaw=aaw_prov('3.14', 'matching teaching methods to outcomes and stating outcomes clearly', 'should', 'paras 3.15, 3.19 and qaa/fheq-2024/4.15'),
  aad=aad_prov('module outcomes and teaching methods', 'Can a student reach each outcome through the methods the module actually uses, and is each outcome written so a student understands it?'))

s('3.15', find=F['3.15'], type='expectation', rung='none', force='should', level='none', appliesTo='ES3 courses', addressee='provider',
  verbs=['interlinked', 'develop'], about='inclusive, fitting teaching methods', domain='none', award='none',
  para="Teaching and learning link within curriculum design, and the methods chosen should be inclusive and fit to build the knowledge and skills in sections 1 and 2; courses led by research or enquiry may build subject-based knowledge and skills.",
  prac="Pick teaching and learning methods that are inclusive and fit to develop the knowledge and skills sections 1 and 2 describe; research-led and enquiry-based designs are one option.",
  ben=('n/a', 'a duty on the course; the student meets its effect, not a standard to reach'),
  aaw=aaw_prov('3.15', 'choosing inclusive teaching methods fit for the subject knowledge and skills', 'should', 'paras 3.14, 3.16 and 2.2'),
  aad=aad_prov('choosing teaching methods', 'Which methods in your module would exclude some students, and what would an inclusive alternative look like?'))

s('3.16', find=F['3.16'], type='expectation', rung='none', force='should', level='none', appliesTo='ES3 courses and their field and practical activities', addressee='provider',
  verbs=['designed', 'arranged'], about='fieldwork for all, inclusively designed with adjustments', domain='none', award='none',
  para=("Practical work, above all fieldwork, is woven through the subjects, so courses give every student substantial field-based learning that builds "
        "skills such as visualising data in three dimensions and applying practical methods; field skills matter for ES3 careers and build transferable "
        "attributes; activities should be inclusive, and reasonable adjustments should be arranged where needed so all can take part."),
  prac=("Give every student substantial fieldwork, integrated with theory; design field and practical activities to be inclusive, and arrange reasonable "
        "adjustments where required so that all students can take part in practical work and fieldwork."),
  ben=('n/a', 'a duty on the course; the student meets its effect, not a standard to reach'),
  aaw=aaw_prov('3.16', 'inclusive field and practical work, with reasonable adjustments', 'should', 'para 2.2 and the threshold items 4.4.b1, 4.4.b2 and 4.4.b4'),
  aad=aad_prov('fieldwork, field trips or practical classes', 'For each field activity, what reasonable adjustment is ready if a student cannot take part as planned?'))

s('3.17', find=F['3.17'], type='expectation', rung='none', force='should', level='none', appliesTo='ES3 courses', addressee='provider',
  verbs=['underpinned', 'embody'], about='teaching grounded in ESD', domain='none', award='none',
  para="Sustainability is central to ES3, so teaching and learning should rest plainly on education for sustainable development and its methods should live out sustainable principles and solutions.",
  prac="Ground teaching and learning in education for sustainable development, and choose methods that themselves practise sustainable principles and solutions.",
  ben=('n/a', 'a duty on the course; the student meets its effect, not a standard to reach'),
  aaw=aaw_prov('3.17', 'grounding teaching and learning in ESD', 'should', 'para 3.22, para 1.12 and std:doc:qaa-advancehe-esd-2021-guidance'),
  aad=aad_prov('how sustainability shows in teaching', 'How do the module\'s own teaching methods practise sustainability, not only teach about it?'))

s('4.2', find=F['4.2'], type='expectation', rung='none', force='should', level='fheq:6', appliesTo='higher education providers awarding ES3 honours degrees', addressee='provider',
  verbs=['perform', 'refer'], about='Annex D for performance above the threshold', domain='none', award=HON,
  para=("Most students will do much better than the threshold; each provider decides what evidence shows this and should use Annex D, QAA's descriptions of "
        "the four honours classifications (1st, 2:1, 2:2, 3rd) at FHEQ level 6 and FQHEIS level 10."),
  prac=("Expect most students to go well beyond the threshold; set your own evidence for this and use Annex D's descriptions of first, upper second, lower "
        "second and third-class honours (FHEQ level 6; FQHEIS level 10)."),
  ben=('n/a', 'a duty on the provider in judging classifications'),
  aaw=(f"Treat para 4.2 as a provider duty in 'should' terms: judge performance above the threshold against Annex D at FHEQ level 6 (FQHEIS level 10). "
       f"Cite it as {CITE('4.2')}. Do not claim the statement sets its own typical or excellent rung, and do not read Annex D as subject-specific. "
       "Set it beside 4.1 and qaa/fheq-2024/annex-d/summary (SL6 in std:doc:qaa-fheq-2024-framework)."),
  aad=aad_prov('classification or what earns a 2:1 or a first', 'Where do your marking criteria draw on the Annex D class descriptions for the ES3 threshold skills?'))

s('4.7', find=F['4.7'], type='outcome', rung='none', force='will', level='fheq:7', appliesTo="graduates of integrated master's courses", addressee='learner',
  verbs=['gained', 'demonstrate', 'interrogate', 'applying', 'design', 'carry'], about="specialism and an independent research project", domain='subject-skill', award=IMS,
  para=("Beyond the skills built over the course, integrated master's graduates will have gained a substantial specialism by developing and leading an "
        "independent research project, and will show they can probe the literature on their own, apply ideas, techniques and data to varied questions and "
        "design and run a project on a significant practical question."),
  prac=("Integrated master's graduates will have built a significant specialism through an independent research project they develop and lead, and will "
        "show they can interrogate the literature alone and design and carry out a project on an important practical question."),
  ben=("In an integrated master's, you will build a real specialism by planning and leading your own research project, and you will show that you can "
       "search the literature independently, apply ideas, methods and data to different questions and design and run a project that tackles a practical problem."),
  aaw=(f"Treat para 4.7 as a stated outcome in 'will' terms for integrated master's graduates at FHEQ level 7 (FQHEIS level 11), on top of the honours threshold. "
       f"Cite it as {CITE('4.7')}. Do not present it as a typical or excellent rung for honours, nor as a standard for taught MSc courses (para 4.8). "
       "Set it beside 4.3.b7, para 2.3, qaa/fheq-2024/4.17.b3, qaa/fheq-2024/4.17.b6 and spine:7."),
  aad=("Raise it when an integrated master's student plans the final-year project or a team designs the master's year. For a student, put it plainly: "
       "you will lead your own research and work independently; for staff, frame it as the step up from 4.3.b7. Ask: What practical question will your "
       "project tackle, and which parts of it did you design yourself? Avoid treating it as an honours requirement."))

s('4.8', find=F['4.8'], type='expectation', rung='none', force='will', level='fheq:7', appliesTo='taught postgraduate (MSc or MA) students', addressee='learner',
  verbs=['build', 'focus', 'achieving', 'enhance'], about='postgraduate depth in one aspect of the subject', domain='none', award=PGT,
  para=("At taught postgraduate level (MSc or MA), students are expected to build on the competencies from their first degree and go deeper into one "
        "aspect of the subject, gaining knowledge and skills that make them more employable."),
  prac=("Taught MSc or MA students will build on the undergraduate competencies above and focus in more depth on one aspect of the subject, gaining "
        "knowledge and skills that improve their employability."),
  ben=("On a taught master's, you will build on what you learned as an undergraduate and go deeper into one area of the subject, gaining knowledge and "
       "skills that strengthen your career prospects."),
  aaw=(f"Treat para 4.8 as a stated expectation in 'will' terms for taught master's students at FHEQ level 7 (FQHEIS level 11): depth in one aspect, building "
       f"on the honours threshold. Cite it as {CITE('4.8')}. Do not claim it sets detailed master's outcomes; the statement gives none. "
       "Set it beside 4.3 to 4.6, para 4.7, qaa/fheq-2024/4.17.b1 and spine:7."),
  aad=("Raise it when a taught master's student or team asks what the statement says about postgraduate study. Say plainly that you will build on your "
       "first-degree skills and go deeper in one area; for staff, frame it as a reason to use the FHEQ master's descriptor for detail. Ask: Which aspect "
       "of the subject will you specialise in, and which of your undergraduate skills will it stretch? Avoid inventing master's outcomes the text does not state."))

# ------------------------------------------------------------------ content lists 3.1, 3.4, 3.7, 3.10 (outcome lists: knowledge every graduate is anticipated to hold)
CONTENT_NB = {
    '3.1': 'the threshold item 4.3.b1 and the Environmental Sciences and Studies list in 3.4',
    '3.4': 'the threshold item 4.3.b1 and the Earth sciences list in 3.1',
    '3.7': 'the shared list in 3.4 and the threshold item 4.3.b1',
    '3.10': 'the shared list in 3.4 and the threshold item 4.3.b1',
}
CONTENT_SUBJ = {'3.1': 'Earth sciences', '3.4': 'environmental sciences or environmental studies', '3.7': 'environmental sciences', '3.10': 'environmental studies'}
def content(stem, k, about, verbs, domain, para, prac, ben, q, force='describes', addressee='learner'):
    i = f'{stem}.b{k}'
    subj = CONTENT_SUBJ[stem]
    lvl = 'fheq:6'
    if force == 'should':
        fdesc = ("its force is descriptive for the knowledge, with a 'should' on how the topic aligns with the ESD guidance")
    elif stem in ('3.7', '3.10'):
        fdesc = "its force is descriptive: the course is normally expected to include it, a word outside must, should, may and will"
    else:
        fdesc = "its force is descriptive: content the statement anticipates, not a requirement"
    P[i] = dict(type='outcome', rung='none', force=force, level=lvl, appliesTo=f'honours graduates in {subj}', addressee=addressee,
                verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben,
                aaw=(f"Treat {stem}, item {k} ({about}) as knowledge the statement expects an honours graduate in {subj} to hold; {fdesc}. "
                     f"Name it as content covered at FHEQ level 6 (FQHEIS level 10), citing {CITE(stem)}, item {k}. "
                     f"Do not present it as a mandatory national curriculum item, a threshold skill from section 4 or a master's standard. "
                     f"Set it beside {CONTENT_NB[stem]} and qaa/fheq-2024/4.15.b1 (spine:6)."),
                aad=(f"Raise it when a student or a programme team checks whether a course covers {about}. "
                     f"Put it plainly, in the second person for a student and as content coverage for staff, noting that courses treat topics in different depth. "
                     f"Ask: {q} Do not read the whole list aloud or treat one item as a pass condition."))

# 3.1 Earth sciences
content('3.1', 1, 'sustainable development and systems thinking', [], 'knowledge',
        "Knowledge of the ideas and uses of sustainable development and systems thinking, taught in a way that should match the joint QAA and Advance HE guidance on ESD.",
        "Teach what sustainable development and systems thinking are and how they are put to use; this should line up with the joint ESD guidance from QAA and Advance HE.",
        "You can expect to learn what sustainable development and systems thinking mean and how they are used in Earth science.",
        'Where in the course do students apply systems thinking to a sustainability problem?', force='should', addressee='both')
content('3.1', 2, 'how the Earth and planets formed', [], 'knowledge',
        "Knowledge of how the Earth and the other planets came into being and where they sit in the solar system.",
        "Cover the origin of the Earth and other planets and their position in the solar system.",
        "You can expect to learn how the Earth and the other planets formed and how they fit into the solar system.",
        'Where does the course teach planetary formation and the solar system?')
content('3.1', 3, 'the central paradigms of the Earth sciences', [], 'understanding',
        "Understanding of the field's core paradigms: uniformitarianism, the span of geological time, evolution and plate tectonics.",
        "Teach the field's core paradigms, from uniformitarianism and deep time to evolution and plate tectonics.",
        "You can expect to understand the big ideas of Earth science: that present processes explain the past, how vast geological time is, how life evolved and how plates move.",
        'Can you explain how plate tectonics and uniformitarianism shape the way you read a rock sequence?')
content('3.1', 4, 'geological time and Earth history', [], 'knowledge',
        "Knowledge of geological time: stratigraphic principles and the column, the fossil record, dating methods, how fast processes run and the major events of Earth history.",
        "Cover stratigraphy and the stratigraphic column, the fossil record, geochronology, process rates and major events in Earth history.",
        "You can expect to learn how geological time is measured and divided, what the fossil record shows and which major events shaped Earth's history.",
        'Which dating methods have you used, and how confident are you in the ages they gave?')
content('3.1', 5, 'Earth spheres and the cycling of matter and energy', [], 'knowledge',
        "Knowledge of the make-up of the solid Earth, oceans and waters, air, ice and living world, the processes acting in each and how matter and energy cycle through them.",
        "Teach how the solid Earth, hydrosphere, atmosphere, cryosphere and biosphere are built and composed and the processes and cycles linking them.",
        "You can expect to learn what the solid Earth, oceans, atmosphere, ice and living world are made of and how matter and energy move between them.",
        'Can you trace one element or form of energy through several Earth spheres?')
content('3.1', 6, 'processes behind Earth and planetary systems', [], 'understanding',
        "Understanding of the biological, chemical and physical processes on which knowledge of Earth and planetary systems rests.",
        "Teach the biological, chemical and physical processes that explain how Earth and planetary systems work.",
        "You can expect to understand the biological, chemical and physical processes that explain how the Earth and other planets work.",
        'Which processes, biological, chemical or physical, do you find hardest to connect?')
content('3.1', 7, 'variation in time and space at fitting scales', [], 'understanding',
        "Understanding of structures, materials and processes with attention to how they vary over time and space at suitable scales.",
        "Teach structures, materials and processes so students appreciate how they vary in time and space at appropriate scales.",
        "You can expect to study structures, materials and processes and how they change across time and place, from small to large scales.",
        'How does the scale you work at change what you can say about a process?')
content('3.1', 8, 'formation of the main rock types', [], 'knowledge',
        "Knowledge of how igneous, metamorphic and sedimentary rocks form.",
        "Cover the formation of igneous, metamorphic and sedimentary rocks.",
        "You can expect to learn how igneous, metamorphic and sedimentary rocks form.",
        'Can you explain how each main rock type forms and give a field example?')
content('3.1', 9, 'identifying rocks, minerals, fossils and structures', [], 'subject-skill',
        "Recognising rocks, minerals, fossils and geological structures and using the right terms, names and classifications for them.",
        "Teach students to identify rocks, minerals, fossils and geological structures and to use the field's terminology, nomenclature and classification.",
        "You can expect to learn to identify rocks, minerals, fossils and geological structures and to name and classify them correctly.",
        'How reliably can you identify common rocks and minerals in hand specimen?')
content('3.1', 10, 'collecting and modelling Earth data in four dimensions', [], 'subject-skill',
        "Gathering and analysing data from the surface and subsurface, then presenting, handling, modelling and extrapolating these often incomplete data across space and time.",
        "Teach collection and analysis of surface and subsurface data and their presentation, manipulation, modelling and extrapolation in four dimensions, including incomplete data.",
        "You can expect to learn to collect and analyse data from above and below ground and to model and extend them across space and time, even when they are incomplete.",
        'Where have you had to extrapolate from incomplete subsurface data, and how did you handle the gaps?')
content('3.1', 11, 'interpreting field data from first principles', [], 'subject-skill',
        "Observing and interpreting field data, gathered in person or virtually, by reasoning from first principles.",
        "Train students to observe and interpret field data, in situ or virtual, from first principles.",
        "You can expect to learn to observe in the field, in person or virtually, and to interpret what you see by reasoning from first principles.",
        'Which field observation have you interpreted without a model answer to lean on?')
content('3.1', 12, 'surveying and measuring in the field and laboratory', [], 'subject-skill',
        "Surveying and measuring in the field and the laboratory with quantitative and instrumental methods.",
        "Teach surveying and measurement in field and laboratory using quantitative and instrumental techniques.",
        "You can expect to learn to survey and take measurements in the field and the laboratory with numerical methods and instruments.",
        'Which instruments have you used, and how did you check their readings?')
content('3.1', 13, 'data use, quality and uncertainty', ['assess'], 'subject-skill',
        "Working with qualitative and quantitative data and datasets, and knowing how to assess data quality and uncertainty.",
        "Teach the use of qualitative and quantitative data and datasets and how to assess data quality and uncertainty.",
        "You can expect to learn to work with both qualitative and numerical data and to judge how good and how certain your data are.",
        'How do you decide how much to trust a dataset?')
content('3.1', 14, 'Earth sciences in resources, hazards and climate change', [], 'understanding',
        "Understanding why the Earth sciences matter for managing resources and for reducing and adapting to environmental hazards, climate change among them.",
        "Teach the role of the Earth sciences in resource management and in mitigating and adapting to environmental hazards, including climate change.",
        "You can expect to understand how Earth science helps manage natural resources and lessen and adapt to hazards such as climate change.",
        'Can you give an example where Earth science changed how a resource or hazard was managed?')
content('3.1', 15, 'the wider socioeconomic and environmental context', ['considered'], 'understanding',
        "Awareness that the subject's knowledge and its uses are weighed within a broader social, economic and environmental setting.",
        "Develop students' awareness that the subject and its application sit within a wider socioeconomic and environmental context.",
        "You can expect to become aware that what you learn and how it is used sit within wider social, economic and environmental concerns.",
        'Who else, beyond scientists, has a stake in the problem you are studying?')
content('3.1', 16, 'ethics, legacy and decolonisation of the discipline', ['engaging', 'appreciating'], 'understanding',
        "Understanding the ethical questions raised by the discipline's history and uses, taking part in current debates and seeing why decolonisation is needed.",
        "Teach the ethics of the discipline's legacy and uses, engage students in current debates and help them see the case for decolonisation.",
        "You can expect to explore the ethical questions raised by Earth science's past and present uses, join current debates and understand why decolonising the subject matters.",
        'Which part of the subject\'s history raises ethical questions for you?')
content('3.1', 17, 'EDI in the practice of the discipline', [], 'understanding',
        "Understanding why equality, diversity and inclusivity matter in how the discipline is practised.",
        "Teach why equality, diversity and inclusivity matter in Earth science practice.",
        "You can expect to understand why equality, diversity and inclusion matter in how Earth science is done.",
        'Who is missing from fieldwork and research in your area, and why?')
content('3.1', 18, 'fieldwork codes and risk assessment', ['complete'], 'subject-skill',
        "Awareness of codes of practice for fieldwork and the ability to complete health and safety risk assessments with confidence.",
        "Teach fieldwork codes of practice and have students complete health and safety risk assessments confidently.",
        "You can expect to learn the codes of practice for fieldwork and to complete health and safety risk assessments with confidence.",
        'Have you written a field risk assessment yourself, and what did it make you change?')

# 3.4 Environmental Sciences and Environmental Studies (shared)
content('3.4', 1, 'sustainable development and systems thinking', [], 'knowledge',
        "Knowledge of the ideas and uses of sustainable development and systems thinking, taught in a way that should match the joint QAA and Advance HE guidance on ESD.",
        "Teach what sustainable development and systems thinking are and how they are put to use; this should line up with the joint ESD guidance from QAA and Advance HE.",
        "You can expect to learn what sustainable development and systems thinking mean and how they are used in environmental work.",
        'Where in the course do students apply systems thinking to a sustainability problem?', force='should', addressee='both')
content('3.4', 2, 'a holistic view of Earth systems', [], 'understanding',
        "Studying Earth's systems and processes as a whole, with their complexity and links.",
        "Take a holistic approach to the complexity and interconnections of Earth's systems and processes.",
        "You can expect to study the Earth's systems and processes as a connected whole.",
        'Can you show how a change in one Earth system spreads to others?')
content('3.4', 3, 'sustainability principles and resource cycles', [], 'knowledge',
        "Knowledge of sustainability principles and of sustainable ways to manage natural and human-driven cycles of resource use.",
        "Teach the principles of sustainability and sustainable approaches to managing natural and human-induced resource cycles.",
        "You can expect to learn the principles of sustainability and how to manage the use of resources sustainably.",
        'Which resource cycle have you analysed, and where could it be made more sustainable?')
content('3.4', 4, 'timescale and impacts on ecosystems', [], 'understanding',
        "Understanding how the timescale considered, from geological to future, shapes the effects of natural and human activity on ecosystems.",
        "Teach why timescale, geological, present, short and long term and future, matters to the impacts of natural and human activities on ecosystems.",
        "You can expect to understand how looking over different timescales, from geological to future, changes how you judge effects on ecosystems.",
        'How would your conclusion change if you looked over a century instead of a decade?')
content('3.4', 5, 'spatial scale of human impacts', [], 'understanding',
        "Understanding the spatial scale, global to local, of human effects on the environment and of responses to change.",
        "Teach how human effects on the environment, and responses to change, differ from the global scale down to the local.",
        "You can expect to understand how human effects on the environment, and responses to change, play out from global to local scales.",
        'Which local issue you know links to a global pattern?')
content('3.4', 6, 'interdependence of organisms in ecosystems', [], 'knowledge',
        "Knowledge of how all organisms in natural and managed ecosystems connect with and depend on each other.",
        "Teach the interconnections and interdependencies of organisms in natural and managed ecosystems.",
        "You can expect to learn how living things in natural and managed ecosystems depend on each other.",
        'Can you map the dependencies in one ecosystem you have studied?')
content('3.4', 7, 'impacts of development and tools to manage them', ['addressing'], 'knowledge',
        "Knowledge of the good and harmful effects of development on the environment and of the management tools for dealing with them.",
        "Teach the positive and negative environmental impacts of development and the management tools that address them.",
        "You can expect to learn how development helps and harms the environment and which tools can manage those effects.",
        'Which management tool would you choose for a development you know, and why?')
content('3.4', 8, 'effects of environmental change on people, other species and infrastructure', [], 'knowledge',
        "Knowledge of how environmental change affects people, other species and infrastructure.",
        "Teach how environmental change affects people, other species and built infrastructure.",
        "You can expect to learn how environmental change affects people, other species and the things we build.",
        'Which group, species or structure is most exposed in a case you have studied?')
content('3.4', 9, 'monitoring, modelling and managing environmental change', ['monitoring', 'modelling', 'managing'], 'subject-skill',
        "Monitoring, modelling and managing environmental change and behaviour, natural and human-induced.",
        "Teach monitoring, modelling and management of natural and human-induced environmental change and behaviour.",
        "You can expect to learn to monitor, model and manage environmental change, whether natural or caused by people.",
        'Which monitoring or modelling method have you used, and what did it miss?')
content('3.4', 10, 'predicting and managing environmental risk', ['understand', 'predict', 'mitigate', 'manage'], 'subject-skill',
        "Knowing how to forecast, reduce and manage the risks posed by a changing environment and human pressure.",
        "Teach how to predict, mitigate and manage risks from environmental change and human pressures.",
        "You can expect to learn how to forecast, reduce and manage risks from a changing environment and from human pressure.",
        'How did you weigh likelihood against impact in a risk you assessed?')
content('3.4', 11, 'uncertainty in decision-making', ['applies'], 'understanding',
        "Understanding uncertainty and how it bears on decisions now and in future.",
        "Teach what uncertainty is and how it affects present and future decisions.",
        "You can expect to understand uncertainty and how it affects decisions now and later.",
        'How did you communicate uncertainty in your last piece of advice or report?')
content('3.4', 12, 'institutions and governance of human impacts', ['managing', 'regulating'], 'knowledge',
        "Knowledge of the part institutions, organisations, governance and other stakeholders play in managing and regulating human effects on the environment.",
        "Teach how institutions, organisations, governance structures and stakeholders manage and regulate what people do to the environment.",
        "You can expect to learn how institutions, organisations, governments and other stakeholders manage and regulate human effects on the environment.",
        'Which body regulates the issue you are studying, and how well does it work?')
content('3.4', 13, 'the subjects in resources, hazards and climate change', [], 'understanding',
        "Understanding why environmental sciences and studies matter for managing resources and for reducing and adapting to environmental hazards, climate change among them.",
        "Teach why environmental science and environmental studies matter for managing resources and for reducing and adapting to hazards, climate change included.",
        "You can expect to understand how your subject helps manage resources and lessen and adapt to hazards such as climate change.",
        'Can you give an example where environmental evidence changed how a hazard was managed?')
content('3.4', 14, 'interpreting field data from first principles', [], 'subject-skill',
        "Observing and interpreting field data, gathered in person or virtually, by reasoning from first principles.",
        "Train students to observe and interpret field data, in situ or virtual, from first principles.",
        "You can expect to learn to observe in the field, in person or virtually, and to interpret what you see by reasoning from first principles.",
        'Which field observation have you interpreted without a model answer to lean on?')
content('3.4', 15, 'data use, quality and uncertainty', ['assess'], 'subject-skill',
        "Working with qualitative and quantitative data and datasets, and knowing how to assess data quality and uncertainty.",
        "Teach the use of qualitative and quantitative data and datasets and how to assess data quality and uncertainty.",
        "You can expect to learn to work with both qualitative and numerical data and to judge how good and how certain your data are.",
        'How do you decide how much to trust a dataset?')
content('3.4', 16, 'digital skills and technology', ['developing'], 'generic-skill',
        "Building digital skills and technology use that are relevant and fit for purpose.",
        "Develop relevant, appropriate digital skills and use of technology.",
        "You can expect to build the digital skills and confidence with technology your field needs.",
        'Which digital tools will you need in the job you want, and which can you already use?')
content('3.4', 17, 'the wider socioeconomic and environmental context', ['considered'], 'understanding',
        "Awareness that the subject's knowledge and its uses are weighed within a broader social, economic and environmental setting.",
        "Develop students' awareness that the subject and its application sit within a wider socioeconomic and environmental context.",
        "You can expect to become aware that what you learn and how it is used sit within wider social, economic and environmental concerns.",
        'Who else, beyond scientists, has a stake in the problem you are studying?')
content('3.4', 18, 'ethics, legacy and decolonisation of the discipline', ['understand', 'engage', 'appreciate'], 'understanding',
        "Understanding the ethical questions raised by the discipline's history and uses, taking part in current debates and seeing why decolonisation is needed.",
        "Teach the ethics of the discipline's legacy and uses, engage students in current debates and help them see the case for decolonisation.",
        "You can expect to explore the ethical questions raised by your subject's past and present uses, join current debates and understand why decolonising it matters.",
        'Which part of the subject\'s history raises ethical questions for you?')
content('3.4', 19, 'EDI in the practice of the discipline', [], 'understanding',
        "Understanding why equality, diversity and inclusivity matter in how the discipline is practised.",
        "Teach why equality, diversity and inclusivity matter in environmental practice.",
        "You can expect to understand why equality, diversity and inclusion matter in how your subject is practised.",
        'Who is missing from environmental decision-making in your area, and why?')
content('3.4', 20, 'fieldwork codes and risk assessment', ['complete'], 'subject-skill',
        "Awareness of codes of practice for fieldwork and the ability to complete health and safety risk assessments with confidence.",
        "Teach fieldwork codes of practice and have students complete health and safety risk assessments confidently.",
        "You can expect to learn the codes of practice for fieldwork and to complete health and safety risk assessments with confidence.",
        'Have you written a field risk assessment yourself, and what did it make you change?')

# 3.7 Environmental Sciences only
content('3.7', 1, 'scientific study of processes acting on ecosystems', [], 'knowledge',
        "Knowledge, from scientific study, of the physical, chemical, biological and human-driven processes that act on ecosystems.",
        "Include scientific study of the physical, chemical, biological and human-made processes that act on ecosystems.",
        "You can expect to study scientifically the physical, chemical, biological and human processes that act on ecosystems.",
        'Which process acting on an ecosystem have you measured directly?')
content('3.7', 2, 'environmental processes from global to atomic scale', [], 'knowledge',
        "Knowledge of the main environmental processes at scales from the planet to the organism and, where it fits, down to molecules and atoms.",
        "Include major environmental processes across scales from global to organismal and, where relevant, to molecular and atomic levels.",
        "You can expect to learn the main environmental processes from the global scale down to single organisms and, where useful, molecules and atoms.",
        'At which scale do you feel least confident explaining a process?')
content('3.7', 3, "a scientific approach to Earth's structure, processes and ecosystems", ['identifying', 'understanding', 'managing'], 'understanding',
        "A scientific, multidisciplinary way to recognise, understand and manage the structure, processes and ecosystems of the Earth.",
        "Include a scientific, multidisciplinary approach to identifying, understanding and managing Earth's structure, processes and ecosystems.",
        "You can expect to learn a scientific approach, drawing on several disciplines, to recognising, understanding and managing the structure, processes and ecosystems of the Earth.",
        'Which disciplines did you draw on in your last environmental investigation?')
content('3.7', 4, 'scientific information and tools for decisions', ['inform'], 'subject-skill',
        "Using scientific and technical information and tools to support decisions and environmental management.",
        "Include using scientific and technical information and tools to support decisions and environmental management.",
        "You can expect to learn to use scientific information and technical tools to support decisions and environmental management.",
        'Which tool or dataset have you used to support an environmental decision?')
content('3.7', 5, 'interpreting field data from first principles', [], 'subject-skill',
        "Observing and interpreting field data, gathered in person or virtually, by reasoning from first principles.",
        "Include observation and interpretation of field data, in situ or virtual, from first principles.",
        "You can expect to learn to observe in the field, in person or virtually, and to interpret what you see from first principles.",
        'Which field observation have you interpreted without a model answer to lean on?')
content('3.7', 6, 'surveying and measuring in the field and laboratory', [], 'subject-skill',
        "Surveying and measuring in the field and the laboratory with quantitative and instrumental methods.",
        "Include surveying and measurement in field and laboratory using quantitative and instrumental techniques.",
        "You can expect to learn to survey and take measurements in the field and the laboratory with numerical methods and instruments.",
        'Which instruments have you used, and how did you check their readings?')

# 3.10 Environmental Studies only
content('3.10', 1, 'history and evidence of environmental change', [], 'knowledge',
        "Knowledge of the history of environmental change, natural and human-driven, and the evidence for it now.",
        "Include the history and present evidence of natural and human-induced environmental change.",
        "You can expect to learn the history of environmental change, both natural and caused by people, and the evidence for it today.",
        'What evidence would you use to separate natural from human-caused change in a case you know?')
content('3.10', 2, 'social, political and economic implications', [], 'understanding',
        "Understanding the social, political and economic consequences of how people interact with the environment.",
        "Include the social, political and economic consequences of how people interact with the environment.",
        "You can expect to understand the social, political and economic consequences of how people treat the environment.",
        'Which political or economic factor most shaped the environmental issue you are studying?')
content('3.10', 3, 'environment, culture and values', [], 'understanding',
        "Understanding how the environment relates to human cultures and values.",
        "Include how the environment relates to human cultures and their values.",
        "You can expect to understand how the environment and human cultures and values shape each other.",
        'How do different communities value the same landscape you have studied?')

# ------------------------------------------------------------------ threshold rung, 4.3 to 4.6 (lead-in 4.1: minimum threshold standards for honours)
FHQ = {
    '4.15.b1': 'qaa/fheq-2024/4.15.b1', '4.15.b2': 'qaa/fheq-2024/4.15.b2', '4.15.b3.1': 'qaa/fheq-2024/4.15.b3.1',
    '4.15.b3.2': 'qaa/fheq-2024/4.15.b3.2', '4.15.b4': 'qaa/fheq-2024/4.15.b4', '4.15.b5': 'qaa/fheq-2024/4.15.b5',
    '4.15.b6': 'qaa/fheq-2024/4.15.b6', '4.15.b7': 'qaa/fheq-2024/4.15.b7', '4.15.b8': 'qaa/fheq-2024/4.15.b8',
    '4.15.b9.1': 'qaa/fheq-2024/4.15.b9.1', '4.15.b9.2': 'qaa/fheq-2024/4.15.b9.2', '4.15.b9.3': 'qaa/fheq-2024/4.15.b9.3',
}
GROUP = {'4.3': 'intellectual skills', '4.4': 'practical skills', '4.5': 'communication skills', '4.6': 'personal and professional skills'}
def th(stem, k, about, verbs, domain, fh, nb, para, prac, ben, q, find=None):
    i = f'{stem}.b{k}'
    r = dict(type='threshold', rung='threshold', force='threshold', forceFrom='4.1', level='fheq:6', appliesTo='honours graduates in ES3 at the threshold',
             addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben,
             aaw=(f"Treat {stem}, item {k} ({about}) as a threshold standard among the {GROUP[stem]}: the least every ES3 honours graduate will have shown, "
                  f"at FHEQ level 6 (FQHEIS level 10). Cite it as {CITE(stem)}, item {k}. "
                  f"Do not call it regulatory, do not treat it as a typical or excellent level and do not apply it to a master's award; the statement leaves grades above the threshold to Annex D. "
                  f"Set it beside {nb} and the honours descriptor {FHQ[fh]} (spine:6)."),
             aad=(f"Raise it when a student or a programme team asks what an honours graduate must be able to show about {about}. "
                  f"For a student, say in plain words and the second person that this is the floor of the degree; for staff, frame it as an outcome every student must reach and evidence. "
                  f"Ask: {q} Avoid reading the issuer's wording aloud at length or suggesting that meeting it earns more than a pass-level honours result."))
    if find:
        r['find'] = find
    P[i] = r

# 4.3 Intellectual skills (knowledge and understanding)
th('4.3', 1, 'subject theories, paradigms, concepts and principles', ['have'], 'knowledge', '4.15.b1', '3.1.b3 and 3.4.b2',
   "Know and understand the theories, paradigms, concepts and principles particular to the subject.",
   "At threshold, graduates know and understand the subject's own theories, paradigms, concepts and principles.",
   "By the time you graduate with honours, you will know and understand the main theories, paradigms, concepts and principles of your subject.",
   'Which core idea of your subject could you explain to a first-year student?')
th('4.3', 2, 'testing findings against several sources of evidence', ['integrate', 'test'], 'subject-skill', '4.15.b7', '4.3.b4 and 4.3.b6',
   "Bring together evidence from varied sources to check findings and hypotheses.",
   "At threshold, graduates combine evidence from several sources to test findings and hypotheses.",
   "By graduation, you will be able to combine evidence from different sources to test findings and hypotheses.",
   'When did evidence from a second source change a finding you were sure of?')
th('4.3', 3, 'looking at issues across disciplines', ['consider', 'appraise'], 'understanding', '4.15.b3.1', '4.3.b2 and 1.9',
   "Weigh up and judge issues from several multidisciplinary and interdisciplinary angles.",
   "At threshold, graduates weigh up and judge issues from several multidisciplinary and interdisciplinary viewpoints.",
   "By graduation, you will be able to look at an issue from the viewpoints of several disciplines and judge them.",
   'Which other discipline has changed how you see an environmental issue?')
th('4.3', 4, 'analysing and critically evaluating information', ['analyse', 'synthesise', 'summarise', 'appraise', 'evaluate'], 'generic-skill', '4.15.b7', '4.3.b8 and 4.5.b4',
   "Analyse, combine, summarise, judge and critically evaluate information.",
   "At threshold, graduates analyse, synthesise, summarise, appraise and critically evaluate information.",
   "By graduation, you will be able to analyse, pull together, summarise and critically judge information.",
   'Where have you had to weigh conflicting information and reach a view of your own?')
th('4.3', 5, 'defining complex problems and weighing solutions', ['define', 'develop', 'evaluate'], 'generic-skill', '4.15.b7', '1.2 and 4.3.b9',
   "Set out complex problems clearly, then work up and judge possible solutions.",
   "At threshold, graduates set out complex problems and work up and judge possible solutions.",
   "By graduation, you will be able to define a complex problem and come up with and judge possible solutions.",
   'Which complex problem have you framed yourself, and how did you compare the options?')
th('4.3', 6, 'hypotheses that shape investigations', ['develop', 'test', 'inform', 'design'], 'subject-skill', '4.15.b6', '4.3.b2 and 4.3.b7',
   "Form and test hypotheses that guide the design of investigations and experiments.",
   "At threshold, graduates form and test hypotheses and use them to shape and design investigations, experiments included.",
   "By graduation, you will be able to form and test hypotheses and use them to design investigations and experiments.",
   'How did your hypothesis shape the way you designed your last investigation?')
th('4.3', 7, 'an independent project with guidance', ['plan', 'conduct', 'present'], 'subject-skill', '4.15.b6', '4.3.b6 and 4.7',
   "Plan, carry out and present an independent project, with suitable guidance.",
   "At threshold, graduates plan, carry out and present an independent project, with suitable guidance.",
   "By graduation, you will have planned, carried out and presented a project of your own, with suitable support.",
   'Which decisions in your project were yours, and where did you need guidance?')
th('4.3', 8, 'a critical approach to literature and data', ['take'], 'generic-skill', '4.15.b5', '4.3.b4 and qaa/fheq-2024/4.15.b3.2',
   "Approach academic writing, data and other information critically.",
   "At threshold, graduates read academic literature, data and other information sources critically.",
   "By graduation, you will read academic work, data and other sources critically.",
   'How do you decide whether a published source is reliable?')
th('4.3', 9, 'handling uncertainty in data and systems', ['have'], 'subject-skill', '4.15.b4', '3.4.b11 and 3.1.b13',
   "Deal with uncertainty in data and in how systems respond, with confidence and competence.",
   "At threshold, graduates deal confidently and competently with uncertainty in data and in system responses.",
   "By graduation, you will be able to work confidently with uncertainty in data and in how systems behave.",
   'How did you handle uncertainty in your last dataset or model?',
   find='have confidence and competence in dealing with uncertainty in data and systems response.')

# 4.4 Practical skills
th('4.4', 1, 'competent field and laboratory investigation', ['conduct'], 'subject-skill', '4.15.b2', '4.4.b2 and 3.16',
   "Carry out field and laboratory investigations competently, as fits the course.",
   "At threshold, graduates conduct fieldwork and laboratory investigations competently, as appropriate to the course.",
   "By graduation, you will be able to carry out fieldwork and laboratory investigations competently.",
   'Which field or lab investigation could you now run without supervision?')
th('4.4', 2, 'recording observations in field and laboratory', ['describe', 'record'], 'subject-skill', '4.15.b2', '4.4.b1 and 3.1.b11',
   "Describe and record observations well in the field and the laboratory.",
   "At threshold, graduates describe and record observations effectively in field and laboratory.",
   "By graduation, you will be able to describe and record what you observe clearly in the field and the lab.",
   'Could someone else repeat your work from your field or lab notes?')
th('4.4', 3, 'logical interpretation of practical results', ['interpret', 'evaluate'], 'subject-skill', '4.15.b7', '4.4.b5 and 4.3.b2',
   "Interpret and judge practical results logically.",
   "At threshold, graduates interpret and evaluate practical results logically.",
   "By graduation, you will be able to interpret and judge practical results logically.",
   'How did you check that your interpretation of a result followed from the data?')
th('4.4', 4, 'ethical and safe practical work', ['undertake'], 'subject-skill', '4.15.b2', '3.1.b18, 3.4.b20 and 4.6.b11',
   "Do laboratory and fieldwork ethically and safely, aware of the relevant codes of conduct and legal requirements.",
   "At threshold, graduates carry out lab and field work ethically and safely, aware of the codes of conduct and the law that apply.",
   "By graduation, you will carry out lab and field work ethically and safely, knowing the codes of conduct and the law that apply.",
   'Which code of conduct or legal requirement shaped your last fieldwork?')
th('4.4', 5, 'gathering and processing data', ['gather', 'prepare', 'process', 'interpret'], 'subject-skill', '4.15.b2', '4.4.b6 and 3.1.b10',
   "Collect, prepare, process and interpret data with suitable methods.",
   "At threshold, graduates collect, prepare, process and interpret data with suitable techniques.",
   "By graduation, you will be able to collect, prepare, process and interpret data with the right methods.",
   'Which step of handling your data was hardest to get right?')
th('4.4', 6, 'numerical, statistical and qualitative techniques', ['use'], 'subject-skill', '4.15.b2', '4.4.b5 and 3.1.b13',
   "Apply suitable numerical, statistical and qualitative methods.",
   "At threshold, graduates use appropriate numerical, statistical and qualitative techniques.",
   "By graduation, you will be able to use suitable numerical, statistical and qualitative methods.",
   'Which statistical test would you pick for your data, and why that one?')
th('4.4', 7, 'technologies for solving problems', ['use'], 'generic-skill', '4.15.b6', '3.4.b16 and 4.3.b5',
   "Use fitting technologies to tackle problems well.",
   "At threshold, graduates use appropriate technologies to address problems effectively.",
   "By graduation, you will be able to use the right technologies to tackle problems well.",
   'Which technology has most helped you solve a problem in your subject?')

# 4.5 Communication skills
th('4.5', 1, 'communicating with varied audiences and media', ['communicate'], 'generic-skill', '4.15.b8', '4.5.b5 and 3.21',
   "Communicate well with different audiences in a range of formats and media.",
   "At threshold, graduates communicate effectively with varied audiences across formats and media.",
   "By graduation, you will be able to communicate well with different audiences in different formats and media.",
   'Who was the least specialist audience you have explained your work to, and how did you adapt?')
th('4.5', 2, 'interpersonal skills for teamwork', ['have', 'enable'], 'generic-skill', '4.15.b9.1', '4.6.b5 and 3.16',
   "Have sound interpersonal communication skills that make teamwork effective.",
   "At threshold, graduates have good interpersonal communication skills for effective team working.",
   "By graduation, you will communicate well with others so that the teams you work in function effectively.",
   'What did you do the last time a team you were in stopped communicating well?')
th('4.5', 3, 'recognising different perspectives', ['acknowledge', 'understand'], 'generic-skill', '4.15.b8', '4.6.b10 and 1.9',
   "Recognise and understand viewpoints other than one's own.",
   "At threshold, graduates acknowledge and understand different perspectives.",
   "By graduation, you will recognise and understand points of view that differ from yours.",
   'Which view you disagreed with did you come to understand better?')
th('4.5', 4, 'building and expressing an argument', ['articulate', 'synthesise'], 'generic-skill', '4.15.b8', '4.3.b4 and 4.5.b5',
   "Put an argument together and express it clearly.",
   "At threshold, graduates articulate and synthesise an argument effectively.",
   "By graduation, you will be able to build an argument and express it clearly.",
   'Can you state the main line of your last essay or report in two sentences?')
th('4.5', 5, 'making a persuasive case', ['present'], 'generic-skill', '4.15.b3.1', '4.5.b1 and 4.5.b4',
   "Present a case persuasively, so that it influences others.",
   "At threshold, graduates present a case in an influential, persuasive way.",
   "By graduation, you will be able to present a case in a way that persuades others.",
   'When did you change someone\'s mind with evidence, and how did you present it?',
   find='present a case in an influential and persuasive manner.')

# 4.6 Personal and professional skills
th('4.6', 1, 'reflecting on learning and own strengths', ['reflect', 'evaluate'], 'generic-skill', '4.15.b5', '4.6.b9 and 3.20',
   "Reflect on how one learns and judge one's own strengths and weaknesses.",
   "At threshold, graduates reflect on their learning process and evaluate their own strengths and weaknesses.",
   "By graduation, you will reflect on how you learn and judge your own strengths and weaknesses.",
   'What has your last piece of feedback told you about how you learn?')
th('4.6', 2, 'skills for autonomous learning', ['develop'], 'generic-skill', '4.15.b5', '4.6.b1 and qaa/fheq-2024/4.15.b9.3',
   "Build the skills to learn independently.",
   "At threshold, graduates develop the skills for autonomous learning.",
   "By graduation, you will have built the skills to learn on your own.",
   'What did you last teach yourself without a class, and how?')
th('4.6', 3, 'planning workloads and managing projects', ['plan', 'organise'], 'generic-skill', '4.15.b9.1', '4.3.b7',
   "Plan and organise workloads, project management included.",
   "At threshold, graduates plan and organise workloads, including project management.",
   "By graduation, you will be able to plan and organise your workload and manage a project.",
   'How did you plan your time on your last large piece of work?')
th('4.6', 4, 'leadership', ['develop'], 'generic-skill', '4.15.b9.1', '4.6.b5 and 3.16',
   "Grow qualities of leadership.",
   "At threshold, graduates develop leadership qualities.",
   "By graduation, you will have developed qualities that let you lead others.",
   'When have you led a group, and what would you do differently?')
th('4.6', 5, 'working well in a team', ['work'], 'generic-skill', '4.15.b9.1', '4.5.b2 and 4.6.b4',
   "Contribute well as a member of a team.",
   "At threshold, graduates work effectively as team members.",
   "By graduation, you will work well as a member of a team.",
   'What part do you usually play in a team, and how well does it work?')
th('4.6', 6, 'working online, remotely and in person', ['work'], 'generic-skill', '4.15.b9.1', '2.6 and 4.6.b5',
   "Work online and at a distance as well as face to face.",
   "At threshold, graduates work online and at a distance as well as face to face.",
   "By graduation, you will be able to work online and remotely as well as face to face.",
   'What changes in how you work when a team meets only online?')
th('4.6', 7, 'professional behaviour', ['demonstrate'], 'generic-skill', '4.15.b9.1', '4.6.b13 and 1.7',
   "Show professional conduct.",
   "At threshold, graduates demonstrate professional behaviours.",
   "By graduation, you will behave professionally.",
   'What does professional behaviour look like on a field trip or placement?')
th('4.6', 8, 'graduate skills for career pathways', ['display'], 'generic-skill', '4.15.b9.3', '4.6.b9 and 1.13',
   "Show awareness of building graduate skills that fit possible careers.",
   "At threshold, graduates show they value building the graduate skills that suit their possible careers.",
   "By graduation, you will understand which graduate skills matter for the careers you are considering and be building them.",
   'Which skills does the career you are considering need, and which do you already have?')
th('4.6', 9, 'planning personal, career and professional development', ['recognise'], 'generic-skill', '4.15.b9.3', '4.6.b1 and 4.6.b8',
   "See why planning for personal, career and professional growth matters, including setting and working towards targets.",
   "At threshold, graduates recognise the importance of planning their personal, career and professional development, including setting and working towards targets.",
   "By graduation, you will see why planning your personal and career development matters, and you will set targets and work towards them.",
   'What development target have you set yourself this year?')
th('4.6', 10, 'respecting the views of others', ['recognise', 'respect'], 'generic-skill', '4.15.b8', '4.5.b3 and 1.9',
   "Recognise and respect other people's views.",
   "At threshold, graduates recognise and respect the views of others.",
   "By graduation, you will recognise and respect other people's views.",
   'How do you respond when a teammate holds a view you think is wrong?')
th('4.6', 11, 'risk assessment and health and safety law', ['demonstrate'], 'generic-skill', '4.15.b9.2', '4.4.b4, 3.1.b18 and 2.2',
   "Show understanding of why risk assessment and the related health, safety and well-being law matter.",
   "At threshold, graduates demonstrate understanding of the importance of risk assessment and related health, safety and well-being legislation.",
   "By graduation, you will understand why risk assessment and the law on health, safety and well-being matter.",
   'Which risk did your last risk assessment catch that you might have missed?')
th('4.6', 12, 'EDI and inclusive behaviour', ['recognise', 'develop', 'support'], 'generic-skill', '4.15.b9.1', '1.8, 1.9, 3.1.b17 and 3.4.b19',
   "See why equality, diversity and inclusivity matter and develop behaviour that supports EDI.",
   "At threshold, graduates see why equality, diversity and inclusivity matter and build behaviours that support EDI.",
   "By graduation, you will understand why equality, diversity and inclusion matter and act in ways that support them.",
   'What have you done to make a group you worked in more inclusive?')
th('4.6', 13, 'acting ethically, sustainably and lawfully', ['appreciate', 'act', 'work'], 'generic-skill', '4.15.b9.2', '1.2, 3.17 and 4.4.b4',
   "Appreciate the need to act and work ethically and sustainably and within the relevant law.",
   "At threshold, graduates appreciate the need to act and work ethically, sustainably and in compliance with relevant legislation.",
   "By graduation, you will understand why you need to act and work ethically, sustainably and within the law.",
   'Where has an ethical or sustainability concern changed what you did in your work?')

GRADE = {}       # one rung only: no gradeOf links
TH = {
    '1.2': 'theme:edi', '1.8': 'theme:edi', '1.9': 'theme:edi', '1.12': 'theme:esd', '1.16': 'theme:enterprise',
    '2.2': 'theme:accessibility', '3.16': 'theme:accessibility', '3.17': 'theme:esd',
}

S5 = dict(
    levels=[dict(id='fheq:6', role='cites', locator='D1, 2.3; 4.2'), dict(id='fheq:7', role='cites', locator='D1, 2.3'),
            dict(id='fqheis:10', role='cites', locator='D1, 2.3; 4.2'), dict(id='fqheis:11', role='cites', locator='D1, 2.3')],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis="stated (D1, 2.3: honours at FHEQ Level 6, FQHEIS SCQF Level 10; 4.2)"),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis="stated (D1, 2.3: integrated master's at FHEQ Level 7, FQHEIS SCQF Level 11)")],
)
S6 = [
    dict(id='theme:edi', role='carries', carriedIn=['front matter', '1.2', '1.4', '1.8', '1.9', '3.1', '3.4', '3.19', '4.6']),
    dict(id='theme:accessibility', role='carries', carriedIn=['2.2', '3.16', '3.19']),
    dict(id='theme:esd', role='carries', carriedIn=['front matter', '1.4', '1.6', '1.10', '1.11', '1.12', '2.1', '3.1', '3.3', '3.4', '3.6', '3.17', '3.22', '4.6']),
    dict(id='theme:enterprise', role='carries', carriedIn=['front matter', '1.6', '1.13', '1.14', '1.15', '1.16', '3.16', '3.18', '4.8']),
]
S7 = [
    dict(rel='supersedes', target='std:doc:qaa-earth-sciences-environmental-sciences-and-environmental-studies-2019-benchmarks (not yet ingested)',
         note='the fourth edition, 2019, named in the back matter; this is the fifth edition'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the honours classification descriptions, cited as QAA 2019 (4.2; section 5)'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='levels 6 and 7 (2.3; 4.2)'),
    dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='SCQF levels 10 and 11 (2.3; 4.2)'),
    dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='1.12; 3.1.b1; 3.4.b1; section 5'),
    dict(rel='refersTo', target='std:doc:qaa-enterprise-2018-guidance', note='1.16; section 5'),
    dict(rel='refersTo', target='QAA Characteristics Statement: Higher Education in Apprenticeships (not yet ingested)', note='2.7; section 5'),
    dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance (not yet ingested)', note='front matter'),
]
SB1 = [
    'Earth sciences, environmental sciences and environmental studies are treated together as ES3, with enough overlap for one statement (D1, 1.1, 1.3).',
    'The setting is the climate emergency, biodiversity loss and wider threats to nature; graduates act on sound science with fairness in view (D1, 1.2).',
    'Environment is read broadly, covering human and non-human life (D1, 1.5).',
    'The subjects study physical, chemical and biological Earth systems to learn from the past and shape the future, across scales of space and time, through systems thinking (D1, 1.6).',
    'They are practical and field-based, with observation and analysis to support decisions under uncertainty (D1, 1.6, 3.16).',
    'They are multidisciplinary and interdisciplinary, overlapping with biology, chemistry, geography, informatics and physics (D1, 1.6, 2.1).',
    'Sustainability is at their root and at their core (D1, 2.1, 3.17).',
    'EDI is subject matter as well as practice, with attention to colonial legacies and other ways of knowing (D1, 1.8, 1.9, 2.1).',
]
SB2 = [
    dict(theme='theme:edi', inThisSubject=("EDI as subject knowledge and practice: removing barriers to field and lab participation, decolonising the curriculum, valuing "
                                            "other ways of knowing, and a route to justice through the SDGs (D1, 1.2, 1.8, 1.9, 2.1)"),
         statements=['1.2', '1.8', '1.9', '3.1.b17', '3.4.b19', '4.6.b12']),
    dict(theme='theme:accessibility', inThisSubject=("inclusive design of curricula and field programmes, accessible technology, reasonable adjustments for practical work and "
                                                      "fieldwork, and risk assessments that cover students with protected characteristics (D1, 2.2, 3.16, 3.19)"),
         statements=['2.2', '3.16']),
    dict(theme='theme:esd', inThisSubject=("headed Sustainability: the subjects are rooted in it; ESD defined with UNESCO's vision and the SDGs; content, applications, teaching "
                                            "and assessment all grounded in it, with the joint ESD guidance as the reference (D1, 1.10 to 1.12, 2.1, 3.17, 3.22)"),
         statements=['1.12', '3.1.b1', '3.4.b1', '3.4.b3', '3.17', '4.6.b13']),
    dict(theme='theme:enterprise', inThisSubject=("headed Employability, entrepreneurship and enterprise: employability defined, what Earth science and environmental employers look "
                                                   "for, employer links, field skills that build graduate attributes, and authentic assessment (D1, 1.13 to 1.16, 3.16, 3.18)"),
         statements=['1.16', '4.6.b8', '4.8']),
]
SB3 = dict(
    areas=[
        dict(component='3.1', gloss='Earth sciences: anticipated knowledge from planetary formation and geological time to field data, ethics and risk'),
        dict(component='3.2', gloss='Earth sciences: 29 typical components, from Earth materials and geochemistry to volcanology and urban geoscience'),
        dict(component='3.3', gloss='Earth sciences: applications in the SDGs, resources, energy transition, past climates, engineering geology and geohazards'),
        dict(component='3.4', gloss='environmental sciences and studies: shared anticipated knowledge of systems, scales, impacts, risk, governance and data'),
        dict(component='3.5', gloss='environmental sciences and studies: 28 typical components, from air quality and biodiversity to waste and water'),
        dict(component='3.6', gloss='environmental sciences and studies: applications in the SDGs, energy, greening industry, modelling, policy and cities'),
        dict(component='3.7', gloss='environmental sciences only: scientific study of processes and scales, field data and measurement'),
        dict(component='3.8', gloss='environmental sciences only: biogeochemical cycles, environmental engineering, principles of environmental science'),
        dict(component='3.9', gloss='environmental sciences only: contamination, future impacts, carbon footprints, corporate practice, biodiversity loss'),
        dict(component='3.10', gloss='environmental studies only: history of change, social and political implications, culture and values'),
        dict(component='3.11', gloss='environmental studies only: conflict, environmental justice, philosophies, indigenous knowledge, values-based ethics'),
        dict(component='3.12', gloss='environmental studies only: philosophies and ethics in practice; indigenous communities in managing the environment'),
    ],
    practices=[
        dict(component='3.13', kind='teaching', gloss='teaching and learning defined, inclusive of all students'),
        dict(component='3.14', kind='teaching', gloss='methods left open; outcomes reachable and clearly stated'),
        dict(component='3.15', kind='teaching', gloss='inclusive methods; research-led and enquiry-based courses'),
        dict(component='3.16', kind='learning', gloss='substantial fieldwork for every student, inclusive, with adjustments'),
        dict(component='3.17', kind='teaching', gloss='teaching and learning grounded in ESD'),
        dict(component='3.18', kind='assessment', gloss='assessment strategy in course design; authentic assessment for employability'),
        dict(component='3.19', kind='assessment', gloss='inclusive assessment tied to outcomes, with adjustments'),
        dict(component='3.20', kind='assessment', gloss='formative feedback, reflection, peer and self-assessment'),
        dict(component='3.21', kind='assessment', gloss='authentic assessment examples: practical investigations, case studies, case reports, presentations'),
        dict(component='3.22', kind='assessment', gloss='multidisciplinary assessment grounded in ESD'),
    ],
)
SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.1', award=HON, items=34)],
    rungBases=("4.1 defines the threshold as the minimum an honours graduate will have demonstrated; the heading 'Threshold level' (before 4.3) "
               "opens four lists, 4.3 intellectual (9), 4.4 practical (7), 4.5 communication (5) and 4.6 personal and professional (13), each with a lead-in "
               "and no modal; 4.2 sends performance above the threshold to Annex D; no typical or excellent rung is stated"),
    outcomeLists=[
        dict(leadIn='3.1', gloss='Earth sciences knowledge all graduates are anticipated to hold', items=18, award=['honours']),
        dict(leadIn='3.4', gloss='environmental sciences and studies knowledge all graduates are anticipated to hold', items=20, award=['honours']),
        dict(leadIn='3.7', gloss='environmental sciences only: further knowledge graduates are expected to demonstrate', items=6, award=['honours']),
        dict(leadIn='3.10', gloss='environmental studies only: further knowledge graduates are expected to demonstrate', items=3, award=['honours']),
    ],
    outcomes=[],
)
SB4A_FULL = []
SB5 = [
    dict(body='Chartered Institution of Water and Environmental Management', says='a notable PSRB in the ES3 field (D1, 1.7)', requirements='not yet ingested (Part E)'),
    dict(body='Geological Society of London', says='a notable PSRB in the ES3 field (D1, 1.7)', requirements='not yet ingested (Part E)'),
    dict(body='Institution of Environmental Sciences', says='a notable PSRB in the ES3 field (D1, 1.7)', requirements='not yet ingested (Part E)'),
    dict(body='Chartered Institute of Ecology and Environmental Management', says='a notable PSRB in the ES3 field (D1, 1.7)', requirements='not yet ingested (Part E)'),
    dict(body='Institute of Environmental Management and Assessment', says='a notable PSRB in the ES3 field (D1, 1.7)', requirements='not yet ingested (Part E)'),
    dict(body='PSRBs in general', says=("several cover the ES3 range, some accrediting programmes and CPD and offering membership up to chartered status; the list changes "
                                        "over time; they and external experts can partner with courses through guidance, accreditation and standards (D1, front matter, 1.7, 2.7)"),
         requirements='not-applicable-by-design'),
]
SB6 = dict(
    themes=[
        dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['front matter', '1.2', '1.4', '1.8', '1.9', '3.1', '3.4', '3.19', '4.6'],
             statements=['1.2', '1.8', '1.9', '3.1.b17', '3.4.b19', '4.6.b12']),
        dict(id='theme:accessibility', named='Accessibility', carriedIn=['2.2', '3.16', '3.19'], statements=['2.2', '3.16']),
        dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)',
             carriedIn=['front matter', '1.4', '1.6', '1.10', '1.11', '1.12', '2.1', '3.1', '3.3', '3.4', '3.6', '3.17', '3.22', '4.6'],
             statements=['1.12', '3.1.b1', '3.4.b1', '3.4.b3', '3.17', '4.6.b13']),
        dict(id='theme:enterprise', named='Employability, entrepreneurship and enterprise (front matter: employability, entrepreneurship and enterprise education)',
             carriedIn=['front matter', '1.6', '1.13', '1.14', '1.15', '1.16', '3.16', '3.18', '4.8'], statements=['1.16', '4.6.b8', '4.8']),
    ],
    frameworks=[
        dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.3', '4.2']),
        dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.3', '4.2']),
    ],
    bodies=[
        dict(body='Chartered Institution of Water and Environmental Management', citedIn=['1.7']),
        dict(body='Geological Society of London', citedIn=['1.7']),
        dict(body='Institution of Environmental Sciences', citedIn=['1.7']),
        dict(body='Chartered Institute of Ecology and Environmental Management', citedIn=['1.7']),
        dict(body='Institute of Environmental Management and Assessment', citedIn=['1.7']),
        dict(body='PSRBs (general)', citedIn=['front matter', '1.7', '2.7']),
    ],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees',
             citedIn=['4.2'], role='descriptions of the four honours classes, for judging performance above the threshold'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='QAA and Advance HE Education for Sustainable Development Guidance',
             citedIn=['1.12', '3.1', '3.4'], role='the reference for ESD in teaching, competencies, outcomes and assessment'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers',
             citedIn=['1.16'], role='the reference for employability, enterprise and entrepreneurship'),
        dict(document='QAA Characteristics Statement: Higher Education in Apprenticeships (not yet ingested: Part E)', named="QAA's Higher Education in Apprenticeships Characteristics Statement",
             citedIn=['2.7'], role='describes apprenticeship degrees'),
        dict(document='QAA Quality Code, Advice and Guidance (not yet ingested: Part E)', named='Advice and Guidance to support the Quality Code',
             citedIn=['front matter'], role='course design, teaching, external expertise, monitoring'),
        dict(document='QAA Glossary (not ingested: Part E)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='UN Sustainable Development Goals (external)', named='UN Sustainable Development Goals', citedIn=['1.9', '1.11', '3.3', '3.6'], role='frame of the sustainability theme'),
        dict(document='UNESCO 2019 definition of ESD (external)', named='the UNESCO 2019 definition', citedIn=['1.11'], role='defines ESD'),
        dict(document='OfS regulatory framework; Quality Assessment Framework for Wales; Quality Enhancement Framework (regulatory, external)',
             named="Office for Students' regulatory framework; Quality Assessment Framework for Wales; Quality Enhancement Framework", citedIn=['front matter'],
             role='the statement\'s regulatory status in each nation'),
    ],
)
B1 = [
    dict(slug='es3', definition='the shorthand the statement uses for Earth sciences, environmental sciences and environmental studies taken together (D1, 1.1)',
         beneficiaryDefinition='the name for the three subjects as one family', scopeNote='used throughout', category='unknown', practices=['education']),
    dict(slug='employability', definition='the competencies, shown through knowledge, skills and behaviours, that make people likelier to gain work and succeed in it (D1, 1.13)',
         beneficiaryDefinition='what makes you likely to find work and do well in it', scopeNote='linked to entrepreneurship and enterprise', category='unknown', practices=['education']),
    dict(slug='accessibility', definition='inclusive design of curriculum and teaching so that no one is excluded from taking part (D1, 2.2)',
         beneficiaryDefinition='courses designed so that you can take full part', scopeNote='with reasonable adjustments where needed', category='unknown', practices=['education']),
    dict(slug='education-for-sustainable-development', definition='building curriculum structures and subject content that support and put sustainable development into practice (D1, 1.11)',
         beneficiaryDefinition='learning that prepares you to help make development sustainable', scopeNote='abbreviated ESD; UNESCO 2019 quoted', category='unknown', practices=['education']),
    dict(slug='authentic-assessment', definition='assessment based on tasks likely to arise at work (D1, 3.18)',
         beneficiaryDefinition='assessment that looks like the work you may do after graduating', scopeNote='examples in 3.21', category='unknown', practices=['education']),
    dict(slug='threshold-standard', definition='the minimum an honours graduate in ES3 will have demonstrated (D1, 4.1)',
         beneficiaryDefinition='the least you need to show to gain the degree', scopeNote='the only rung the statement sets', category='unknown', practices=['education']),
]
B2A = [
    dict(concept='es3', form='ES3', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
    dict(concept='employability', form='employability', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='accessibility', form='accessibility', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='education-for-sustainable-development', form='Education for Sustainable Development', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='education-for-sustainable-development', form='ESD', lang='en', partOfSpeech='noun', termStatus='admitted', register='formal'),
    dict(concept='authentic-assessment', form='authentic assessment', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='threshold-standard', form='minimum threshold standards', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
]
B4 = []
B5 = []
D3 = [
    dict(citation='QAA (2019) Characteristics Statement: Higher Education in Apprenticeships', settles=['SB6', 'S7'], asked='2026-10-03', state='wanted'),
    dict(citation='QAA (2019) Subject Benchmark Statement: Earth Sciences, Environmental Sciences and Environmental Studies, fourth edition', settles=['S7'], asked='2026-10-03', state='wanted'),
]
E = [
    'SB4, rungs: the statement sets one rung only, the threshold (4.1, the heading "Threshold level" and the lists 4.3 to 4.6, 34 items); no typical or excellent rung; 4.2 sends performance above it to Annex D. Same shape as Archaeology (run 0085). No gradeOf links.',
    'SB4, lead-ins: the four threshold lists have lead-ins with no modal ("Graduates with an honours degree in ES3:", "Graduates of an honours degree in ES3:"); force recorded as threshold from 4.1 (forceFrom 4.1).',
    'S4, skeleton correction: std_prep marked 3.2, 3.5, 3.8 and 3.11 ("Typical components may include") as typical-rung lists (65 items). They are lists of typical course components, not a rung: recorded as S3 areas (SB3), not statements.',
    'S4, skeleton correction: 4.3.b9 and 4.5.b5 ran on into the next sub-heading ("Practical skills", "Personal and professional skills"); the paragraph statements 1.5, 1.9, 1.12, 2.2, 2.5 and 4.2 ran on into their next sub-heading, and 1.16, 2.3, 3.17 and 4.8 into a page number. All re-cut with find.',
    'S4, outcome lists in other words: 3.1 and 3.4 say "it is anticipated that all graduates have appropriate knowledge and skills" of the listed items, and 3.7 and 3.10 that a programme "is normally expected to include" them "with graduates expected to demonstrate knowledge and understanding". Taken as outcome lists (47 records) with force describes, as "anticipated" and "expected" are outside the five; for Abbott: should they read as will or should?',
    'S4, 3.1.b1 and 3.4.b1 carry their own "should" (consistency with the ESD guidance); force recorded as should, addressee both.',
    'S4, 3.7 and 3.10 point to "the combined content in paragraph 3.2"; the combined environmental content is 3.4 (3.2 is Earth science components). The issuer\'s slip, kept; read as 3.4.',
    'S4, 1.8 obliges with "a duty to confront and encourage the dismantling of all barriers" (ES3 communities): an obliging word outside the five, recorded as describes, addressee provider; for Abbott.',
    'S4, 1.2 "Graduates in ES3 subjects will be required to ensure..." taken as a will statement about graduates (expectation, all awards); "required" here describes their future working duty, not a condition of the award.',
    'S4, 2.4 "it would normally be expected that a student who had achieved a second-class degree or higher would be capable of" postgraduate study: an obliging phrase outside the five, recorded as describes.',
    'S4, 1.5 (should, how to read "environment") taken as a statement under the obliging-paragraph rule, though it binds readers, not courses or students; student version not applicable. For Abbott at P3.',
    'S4, not taken as statements (plain-present provider norms or descriptions, template open point 5): 2.1 ("Courses are focused...", "Courses allow students to reflect..."); 3.16\'s "Courses therefore offer all students opportunities for significant field-based learning" (the paragraph is a statement by its should); 3.19 ("Assessment is inclusive for all students"); 3.22 ("assessments take multidisciplinary and interdisciplinary approaches").',
    'S4, not taken as statements (predictive or descriptive will): 1.13 ("will contribute positively to graduate employability"); 1.14 and 1.15 ("employers will be looking for competence..."): employer demand, not an outcome; 2.8 to 2.10 (degree-awarding bodies, providers and external examiners "will" review and examine): descriptions of quality assurance. For Abbott at P3: 1.14 and 1.15 could be read as expected competences.',
    'S4, not taken as statements: 1.6, nine shared traits ("ES3 is characterised by"), descriptive with no modal; recorded in SB1. 2.6 and 2.7 use "may" for options only.',
    'S4, 2.3 holds two outcomes, honours progression and the integrated master\'s year; kept as one record by the issuer\'s numbering, level fheq:6, award honours and integrated master\'s.',
    'S4, 4.7 and 4.8 (integrated master\'s, taught MSc or MA) sit under the heading "Personal and professional skills" with no heading of their own; recorded rung none, level fheq:7.',
    'S2, statedScope: the scope also says foundation degrees (FdSc) may find the guidance useful and that research degrees are not addressed.',
    'Subjects: HECoS has no preferred term "environmental studies"; it is a non-preferred term of 100469 environmental management (CAH26-01-03 human geography): entered as inferred. Geology (100395) inferred: the statement names Earth sciences, not geology, as the subject. CAH26-01-03 inferred with it.',
    'SB5: five bodies named in 1.7 as notable PSRBs; the statement says nothing more of each; their own requirements are not yet ingested. The Disabled Students\' Commission, the Environment Agency, the British Geological Survey and others appear only in the back matter (excluded).',
    'SB6, sharedDocuments: section 5 also lists HEA (2016) Framework for embedding employability in higher education, cited nowhere in the body; not tagged. The Apprenticeships Characteristics Statement and the Quality Code Advice and Guidance are not yet ingested (D3).',
    'SB6, themes: the front matter names three cross-cutting themes (EDI; ESD; employability, entrepreneurship and enterprise education); accessibility has its own heading (2.2) as a fourth. Tags follow what each paragraph says; 1.14 and 1.15 tagged enterprise for employer expectations.',
    'S5: no CQFW level cited; FQHEIS levels cited as "FQHEIS SCQF Level 10" and "11" (2.3) and "FQHEIS Level 10" (4.2).',
    'S7, supersedes: the back matter names the fourth edition (2019) and the third (2014); the 2019 document is not yet ingested (D3).',
    'S9: not researched in P1.',
    'Patterns that differ from Psychology: threshold only, no typical or excellent rung; threshold lead-ins with no modal; subject content lists phrased as "anticipated" and "normally expected" knowledge; three subjects in one statement with shared and subject-only lists; integrated master\'s and taught master\'s covered in one paragraph each; no glossary; 4.2 cites Annex D as QAA 2019.',
]
