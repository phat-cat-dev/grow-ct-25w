# Judgement fields for run 0089, QAA Subject Benchmark Statement: Biomedical Science and Biomedical Sciences (March 2023). std.
# Built by tools/bm_build.py. Keys are S4 ids under qaa/<slug>/.
# Section 4's two tables sit inside the skeleton's component 4.5. Table 1 rows are 4.5.b1 to 4.5.b16, Table 2 rows 4.5.b17 and 4.5.b18.
# Each row's first column (the benchmark outcome) keeps the base id; its threshold and excellent cells are <id>.threshold and <id>.excellent.
import json as _json, os as _os

HON = "bachelor's with honours"
MAS = "master's"
BOTH = [HON, MAS]
SLUG = 'biomedical-science-and-biomedical-sciences-2023'
SID = 'qaa/' + SLUG
_DIR = _os.path.join(_os.getcwd(), 'ingest-std-qaa-biomedical-science-and-biomedical-sciences-2023-benchmarks')
_NORM = open(_os.path.join(_os.getcwd(), 'stan/core/qaa/benchmarks', SLUG + '.norm.txt'), encoding='utf-8').read()

CITE = 'QAA (2023), Biomedical Science and Biomedical Sciences Subject Benchmark Statement'

def F(a, b, mark=None):
    """The exact held text from phrase a to the end of phrase b (searching after `mark` if given); returns (text, offset)."""
    k0 = _NORM.find(mark) if mark else 0
    s = _NORM.find(a, k0)
    assert s >= 0, a
    e = _NORM.find(b, s)
    assert e >= 0, b
    return _NORM[s:e + len(b)], s

META = dict(
    run='0089', p1='2026-10-03 16:39',
    title='Subject Benchmark Statement Biomedical Science and Biomedical Sciences',
    heading='Subject Benchmark Statement: Biomedical Science and Biomedical Sciences (QAA, March 2023)',
    edition='March 2023', published='2023-03',
    status='current',
    supersedes='the fourth edition, Biomedical Sciences (2019), as the back matter states; this is the fifth edition, published 8 March 2023',
    subjects=[
        dict(scheme='cah', code='CAH02-05-03', label='biomedical sciences (non-specific)', basis='inferred'),
        dict(scheme='hecos', code='100265', label='biomedical sciences', basis='inferred'),
        dict(scheme='hecos', code='100260', label='healthcare science', basis='inferred'),
        dict(scheme='hecos', code='100250', label='pharmacology', basis='inferred'),
        dict(scheme='hecos', code='100247', label='nutrition', basis='inferred'),
        dict(scheme='hecos', code='100262', label='physiology', basis='inferred'),
    ],
    awards=[HON, MAS], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series="QAA Subject Benchmark Statements, the revision with cross-cutting themes; this statement's fifth edition (D1, front matter; back cover)",
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    agentDefinition=("QAA's UK reference point for what a graduate in Biomedical Science (singular: the IBMS-accredited route to HCPC registration "
        "as a Biomedical Scientist) or Biomedical Sciences (plural: the broader human biology degrees, including Pharmacology, Human Nutrition "
        "and Physiology) should know, understand and be able to do. Reach for it when designing, approving, reviewing or describing an honours or "
        "master's course in these subjects, when placing a student's work against its threshold and excellent standards, or when explaining how "
        "an accredited degree leads to registration. It is a sector reference point, not a regulation, and not the IBMS's accreditation criteria "
        "or the HCPC's standards of proficiency."),
    summary=("Published by QAA in March 2023 as the fifth edition, the statement separates Biomedical Science (accredited by the Institute of "
        "Biomedical Science, leading with clinical training to registration with the Health and Care Professions Council) from the broader "
        "Biomedical Sciences. It sets out context and purposes, with the four cross-cutting themes (equality, diversity and inclusion; "
        "accessibility; sustainability; enterprise and entrepreneurship education); distinctive features of design, progression, flexibility, "
        "partnership and review; and content, teaching and assessment, including outcome lists for the nine clinical pathology specialisms of "
        "an accredited degree and for Pharmacology, Human Nutrition and Physiology courses. Its benchmark standards are two tables: Table 1, "
        "sixteen outcomes for the honours degree, fifteen of them graded at threshold and excellent; Table 2, master's outcomes in addition, "
        "graded only by the support or independence they are shown with. It cites the FHEQ and FQHEIS levels, Annex D for degree classes, the "
        "QAA and Advance HE ESD guidance and QAA's enterprise guidance, and names IBMS, HCPC, the Royal Society of Biology, the Association "
        "for Nutrition and the British Pharmacological Society. An appendix of draft threshold suggestions drawn from the HCPC standards of "
        "proficiency is held but not ingested as statements."),
    authority='reference: a sector-owned reference point, not a regulatory requirement; a key reference point in Wales and Scotland and part of the quality arrangements in Northern Ireland, not a sector-recognised standard in England (D1, front matter)')

S2 = dict(
    governs=("what honours graduates in Biomedical Science and Biomedical Sciences, and master's graduates in addition, can be expected to "
             "know, understand and do, at threshold and excellent standards; the clinical pathology content of an IBMS-accredited degree; core "
             "content for Pharmacology, Human Nutrition and Physiology courses; and the context for course design, teaching and assessment"),
    awards=[HON, MAS], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    statedScope=('"This Subject Benchmark Statement offers clarification between Biomedical Science (singular) and Biomedical Sciences '
                 '(plural) courses." (D1, 1.1)'),
    statedSubjects=[
        dict(name='Biomedical Science', locator='(D1, front matter; 1.2; 1.6; 3.2 to 3.4)', kind='subject',
             codes=[dict(scheme='hecos', code='100265', label='biomedical sciences')]),
        dict(name='Biomedical Sciences', locator='(D1, front matter; 1.3; 2.1)', kind='subject',
             codes=[dict(scheme='hecos', code='100265', label='biomedical sciences')]),
        dict(name='Healthcare Science', locator='(D1, 2.6; 3.2; 3.4)', kind='programme title',
             codes=[dict(scheme='hecos', code='100260', label='healthcare science')]),
        dict(name='Pharmacology', locator='(D1, 1.3; 2.5; 3.5; 3.6)', kind='specialism',
             codes=[dict(scheme='hecos', code='100250', label='pharmacology')]),
        dict(name='Human Nutrition', locator='(D1, 2.5; 3.7 to 3.9)', kind='specialism',
             codes=[dict(scheme='hecos', code='100247', label='nutrition')]),
        dict(name='Human/Medical Physiology', locator='(D1, 2.5; 3.10; 3.11)', kind='specialism',
             codes=[dict(scheme='hecos', code='100262', label='physiology')]),
    ])

SECTIONS = {
    '1': 'Context and purposes of Biomedical Science and Biomedical Sciences degrees',
    '2': 'Distinctive features of Biomedical Science/Biomedical Sciences degrees',
    '3': 'Content, structure and delivery',
    '4': 'Benchmark standards',
}
SUB = [('1.1', '1.5', 'Context and purposes'), ('1.6', '1.12', 'Purposes and characteristics of Biomedical Science/Biomedical Sciences degrees'),
       ('1.13', '1.15', 'Registration and protected title'), ('1.16', '1.19', 'Equality, diversity and inclusion'),
       ('1.20', '1.22', 'Accessibility'), ('1.23', '1.25', 'Sustainability'), ('1.26', '1.31', 'Enterprise and entrepreneurship education'),
       ('2.1', '2.8', 'Design'), ('2.9', '2.12', 'Progression'), ('2.13', '2.15', 'Flexibility'), ('2.16', '2.19', 'Partnership'),
       ('2.20', '2.28', 'Monitoring and review'),
       ('3.1', '3.1', 'Content common to Biomedical Science and/or Biomedical Sciences courses'),
       ('3.2', '3.4', 'Content specific to Biomedical Science courses - clinical pathology subjects'),
       ('3.5', '3.6', 'Content specific to other courses in the Biomedical Sciences area; Content in Pharmacology courses'),
       ('3.7', '3.9', 'Content in Human Nutrition courses'), ('3.10', '3.11', 'Content in Human/Medical Physiology courses'),
       ('3.12', '3.14', 'Approaches to study in all courses'), ('3.15', '3.18', 'Teaching and learning'), ('3.19', '3.24', 'Assessment'),
       ('4.1', '4.5', 'Benchmark standards; Table 1 and Table 2')]

G = {
    '1.1': 'the statement tells the singular and plural degrees apart',
    '1.2': 'the singular degree covers every clinical laboratory specialism, the academic basis for registration',
    '1.3': 'the plural degree is broader; top-up modules and clinical time as a route to registration',
    '1.4': 'honours courses give a broad scientific basis for health and disease and qualities for demanding work',
    '1.5': 'who the statement is meant for',
    '1.6': 'accreditation, approval and close work with practising scientists',
    '1.7': 'lifelong learning and further qualifications after the degree',
    '1.8': 'the accredited degree aims at diagnostic pathology laboratories',
    '1.9': 'graduate career paths, listed',
    '1.10': 'hands-on laboratory work as an essential part of every course',
    '1.11': 'research skills and what they prepare students for',
    '1.12': 'interpreting clinical test results; the training portfolio and registration',
    '1.13': 'the protected title and what the role involves',
    '1.14': 'registration by statute; the standards of proficiency',
    '1.15': 'the professional body awards the certificate of competence',
    '1.16': 'a commitment to equity and inclusive practice',
    '1.17': 'inclusion throughout; course teams, awareness and global healthcare',
    '1.18': 'confronting the history of the field and its biases',
    '1.19': 'diverse contributors, lived experience and the misuse of knowledge',
    '1.20': 'equity of access, based on potential',
    '1.21': 'fully accessible curricula, assessment and practical work',
    '1.22': 'anticipating access needs, including fieldwork, laboratories and placements',
    '1.23': 'sustainability in the subject, in the laboratory and in the curriculum',
    '1.24': 'ESD as defined by UNESCO; the SDGs',
    '1.25': 'the ESD guidance as the reference for teaching sustainability',
    '1.26': 'employability and entrepreneurship as competencies; employer links',
    '1.27': 'what enterprise education does for careers',
    '1.28': 'entrepreneurship beyond employment',
    '1.29': 'co-creating enterprise education; topics and real examples',
    '1.30': 'visiting speakers, teamwork and taking charge of one\'s own development',
    '1.31': 'where to find the enterprise guidance',
    '2.1': 'the variety of courses; checking accreditation before applying',
    '2.2': 'routes into the degree, including foundation years',
    '2.3': 'the awards and their levels, bachelor\'s and integrated master\'s',
    '2.4': 'placements, the training portfolio and integrating credit-bearing placements',
    '2.5': 'common cores across related courses and late choice of award',
    '2.6': 'degree apprenticeships follow the statement',
    '2.7': 'equally accessible learning and assessment',
    '2.8': 'accessible design and support for the full range of skills',
    '2.9': 'progression from simple concepts to graduate competence',
    '2.10': 'progressive acquisition of knowledge and skills; strategies to support it',
    '2.11': 'progressing between levels by meeting at least the threshold',
    '2.12': 're-sits, exit awards and length of study',
    '2.13': 'diverse modes of delivery and credit transfer',
    '2.14': 'practical skills, at the bench and virtually',
    '2.15': 'flexible and resilient courses',
    '2.16': 'partnership delivery and oversight of partners',
    '2.17': 'employment-focused learning and inclusive placements',
    '2.18': 'student societies and learned bodies',
    '2.19': 'students as partners; student voice',
    '2.20': 'monitoring and periodic review by degree-awarding bodies',
    '2.21': 'feedback that feeds review',
    '2.22': 'review checks ESD and EDI across the curriculum',
    '2.23': 'performance data and expert review together',
    '2.24': 'external reviewers in periodic review',
    '2.25': 'the external examining system',
    '2.26': 'more than one external examiner may be needed',
    '2.27': 'regular monitoring and enhancement with students and others',
    '2.28': 'the bodies that accredit courses in the area',
    '3.1': 'scientific content common to all the courses',
    '3.2': 'the clinical specialisms the accredited degree must cover',
    '3.3': 'integrating specialisms through a systems-led approach',
    '3.4': 'the clinical pathology subject areas and what graduates know in each',
    '3.5': 'other specialisms; what pharmacology is',
    '3.6': 'core outcomes for Pharmacology graduates',
    '3.7': 'Human Nutrition courses and the professional body\'s competencies',
    '3.8': 'nutrition careers and registration',
    '3.9': 'core outcomes for Human Nutrition graduates',
    '3.10': 'physiology as an integrative science, with disease as context',
    '3.11': 'core outcomes for Physiology graduates',
    '3.12': 'approaches to study common to all the courses',
    '3.13': 'graduate attributes and the changing state of knowledge',
    '3.14': 'the graduate attributes, listed',
    '3.15': 'scaffolded, progressive teaching strategies',
    '3.16': 'adaptive, inclusive strategies; staff development; modes of delivery',
    '3.17': 'synchronous learning activities',
    '3.18': 'asynchronous learning activities',
    '3.19': 'assessment strategy: progressive, varied, authentic and inclusive',
    '3.20': 'principles for designing assessment',
    '3.21': 'themes for authentic assessment',
    '3.22': 'formats for examining the themes',
    '3.23': 'integrated master\'s: unfamiliar problems and research skills',
    '3.24': 'qualities of good feedback',
    '4.1': 'the minimum standards for the honours degree, with excellence indicated',
    '4.2': 'most students exceed the minimum; Annex D for classes',
    '4.3': 'why the standards are broad and generic',
    '4.4': 'standards for the accredited degree link to the regulator\'s proficiency standards',
    '4.5': 'master\'s standards; the two tables of benchmark outcomes',
}
CTYPE = {'3.1': 'area', '3.4': 'area', '3.5': 'area', '3.6': 'area', '3.7': 'area', '3.9': 'area', '3.10': 'area', '3.11': 'area', '3.12': 'area',
         '3.15': 'practice', '3.16': 'practice', '3.17': 'practice', '3.18': 'practice', '3.19': 'practice', '3.20': 'practice',
         '3.21': 'practice', '3.22': 'practice', '3.23': 'practice', '3.24': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='section headings 1 to 4', heading='the four section heading lines', kind='other: heading lines'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for S7 and SB6'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement', kind='other: back matter, read for S8 (editions)'),
    dict(number='Appendix 1', heading='Draft suggestions for threshold levels of achievement for Biomedical Science degrees based on HCPC standards of proficiency', kind='other: a draft drawn from a body\'s standards (HCPC SoP via the IBMS portfolio); not the statement\'s own standards; read for SB5 and Part E'),
]

P = {}
def s(i, **k):
    P[i] = k

NA = ('n/a', 'a duty on the course team or provider; the student meets its effect, not a standard to reach')

def prov(i, txt, force, gist, nbrs, when, ask, **k):
    """A provider norm: agent instructions from a gist, neighbours, a moment to raise it and a question."""
    text, off = txt
    word = {'should': 'should-level expectation', 'must': 'must-level requirement', 'will': 'stated expectation (will)',
            'describes': 'stated expectation, worded outside the five force words'}[force]
    d = dict(find=text, after=off, type=k.pop('type', 'expectation'), rung='none', force=force, level=k.pop('level', 'none'),
             appliesTo=k.pop('appliesTo', 'courses in the subject area'), addressee=k.pop('addressee', 'provider'),
             domain=k.pop('domain', 'none'), award=k.pop('award', BOTH), ben=k.pop('ben', NA))
    d.update(k)
    d.setdefault('aaw', f"Treat this as a {word} on the course team or provider, not a student outcome: {gist}. It holds across the courses the statement covers, honours and master's alike, at no one level. Cite it as {CITE}, para {i}. Do not present it as regulation or as a legal duty; set it beside {nbrs}.")
    d.setdefault('aad', f"Raise this {when}. Put it to staff as something the course should show in its design and evidence, not as a target for students. Ask: '{ask}' Do not hand it to a student as a standard they must reach.")
    P[i] = d

# ------------------------------------------------------------------ section 1: obliging and outcome paragraphs
s('1.2', find=F('A Biomedical Science degree will include', '(protected title).')[0], after=F('A Biomedical Science degree will include', '(protected title).')[1],
  type='expectation', rung='none', force='will', level='fheq:6', appliesTo='Biomedical Science (singular) degrees', addressee='provider',
  verbs=['include', 'enabling', 'achieve', 'apply'], about='all the clinical laboratory specialisms in the singular degree', domain='none', award=HON,
  para="A Biomedical Science degree will take in every key clinical laboratory specialism, so that graduates meet the academic part of what they need to seek registration as a Biomedical Scientist, a protected title.",
  prac="Cover every one of the key clinical laboratory specialisms (microbiology with virology, clinical biochemistry, haematology and transfusion, immunology, cellular pathology and clinical genetics) so the degree gives the academic basis for registration.",
  ben=NA,
  aaw=f"Treat this as a stated expectation (will) on the content of the singular Biomedical Science honours degree (FHEQ level 6): every key clinical laboratory specialism is taught. Cite it as {CITE}, para 1.2. Do not claim it makes graduates registered or that it binds Biomedical Sciences (plural) courses; set it beside 3.2 and the specialism outcomes at 3.4.b2 to 3.4.b47 in this document.",
  aad="Raise this with a team planning or reviewing an accredited Biomedical Science degree, or with a student unsure which degree leads to registration. For staff, frame it as complete coverage of the specialisms; for a student, explain that this degree is the academic step, with clinical training still to come. Ask: 'Which specialism is thinnest in your course at present?' Avoid suggesting the degree alone gives the protected title.")
s('1.4', find=F('Graduates from these courses will develop', 'unpredictable circumstances.')[0], after=F('Graduates from these courses will develop', 'unpredictable circumstances.')[1],
  type='outcome', rung='none', force='will', level='fheq:6', appliesTo='honours graduates of either degree', addressee='learner',
  verbs=['develop', 'require'], about='qualities for demanding professional work', domain='generic-skill', award=HON,
  para="Honours graduates of either degree will build the qualities that work calls for where professionalism, independent critical thinking, personal responsibility and decisions in complex, unpredictable settings are needed.",
  prac="Design the course so that graduates will leave with professionalism, critical independent judgement, personal responsibility and the ability to decide well in complex and unpredictable work.",
  ben="By the end of your honours degree you will have built the professionalism, independent critical thinking and sense of personal responsibility needed to make decisions at work when situations are complex and unpredictable.",
  aaw=f"Treat this as a stated outcome (will) for honours graduates of both the singular and plural degree, at FHEQ level 6 (FQHEIS level 10 in Scotland). Cite it as {CITE}, para 1.4. Do not claim it as a professional body competence or as a master's outcome. Set it beside the FHEQ honours descriptors qaa/fheq-2024/4.15.b9.1 and qaa/fheq-2024/4.15.b9.2, spine:6 and 4.5.b16 in this document.",
  aad="Raise this when a student asks what employers expect of a graduate, or when a team reviews how the course builds independence. To a student, put it as the professional habits you will be trusted with; to staff, as qualities the course has to grow over the years. Ask: 'Can you describe a time on the course when you had to make a decision without a clear right answer?' Avoid reading the issuer's text aloud.")
s('1.12', find=F('Graduates from Biomedical Science courses will develop', 'approaches to healthcare.')[0], after=F('Graduates from Biomedical Science courses will develop', 'approaches to healthcare.')[1],
  type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of Biomedical Science (singular) courses', addressee='learner',
  verbs=['develop', 'enable'], about='interpreting clinical laboratory and near-patient results', domain='subject-skill', award=HON,
  para="Biomedical Science graduates will build the skills and knowledge to interpret results from clinical laboratory and near-patient tests, through their modules, the registration training portfolio and registration, so they can contribute to multidisciplinary healthcare.",
  prac="Through taught modules, and with the training portfolio and registration, singular-degree graduates will be able to interpret clinical laboratory and point-of-care test results and take part in multidisciplinary care.",
  ben="On a Biomedical Science degree you will learn to interpret the results of clinical laboratory tests and tests done near the patient, so that you can play your part in a healthcare team.",
  aaw=f"Treat this as a stated outcome (will) for graduates of the singular Biomedical Science honours degree (FHEQ level 6), reached through modules together with the training portfolio and registration. Cite it as {CITE}, para 1.12. Do not claim that the degree alone makes a graduate registered or that it holds for Biomedical Sciences (plural). Set it beside 3.4.b39 to 3.4.b41 (near-patient testing), 1.2 and qaa/fheq-2024/4.15.b2.",
  aad="Raise this when a student on the accredited route asks what the degree prepares them to do in a laboratory, or when a team plans interpretation tasks. To a student, put it as reading test results with understanding and explaining them to colleagues. Ask: 'Given an abnormal result, what would you check before reporting it?' Do not tell a Biomedical Sciences (plural) student this is required of them.")
prov('1.16', F('This Subject Benchmark Statement expects', 'community members.'), 'describes',
     'learning communities commit to equity, inclusive access and practice that anticipates diverse needs',
     '1.17 to 1.19 and the accessibility paragraphs 1.20 to 1.22', 'when a team sets out its approach to equity and inclusion',
     'How does the course find out about students\' needs before they become barriers?',
     verbs=['expects', 'commit', 'anticipate'], about='a commitment to equity and inclusion',
     para="The statement looks to the learning communities in these subjects to commit to equity, inclusive access and practice that foresees the varied needs of their members.",
     prac="Commit the course community to equity and inclusive access, and plan for members' different needs in advance rather than waiting for requests.")
prov('1.17', F('This Statement asks the learning community', 'government guidance.'), 'should',
     'inclusion throughout, an open and respectful environment, awareness raised through integrated activity, and global healthcare inequality addressed',
     '1.16, 1.18, 1.19 and 2.22', 'with a team reviewing its curriculum or the climate of its labs and classes',
     'Where in the curriculum do students meet questions of access to diagnosis and treatment across the world?',
     verbs=['address', 'create', 'raise', 'designed'], about='an inclusive environment and awareness of equality',
     para="Inclusion runs through the whole statement; course teams should build an open, participative and respectful environment, courses should raise awareness of equality, equity, diversity and inclusion through integrated activity and address global healthcare issues, and everyone shares responsibility for promoting equality and challenging bias.",
     prac="Create a setting where everyone feels respected and knows their part in inclusive practice; weave equality and diversity into activities and discussion, address unequal access to diagnosis and treatment worldwide, and keep this under review.")
prov('1.18', F('Biomedical Science and/or Biomedical Sciences are subjects whose', 'biases and stereotypes.'), 'should',
     'the field\'s history, its links with social injustice and its present practices examined critically, with diverse sources and regular review of materials',
     '1.17, 1.19 and the ethics row 4.5.b14 with its threshold and excellent cells', 'when a team reviews reading lists, case studies or the history taught in a module',
     'Which scientists and cases does the course hold up as examples, and whose work is missing?',
     verbs=['engage', 'consider', 'reviewed'], about='confronting the history and biases of the field',
     para="Though the subjects rest on objective observation, courses should engage critically with how the field has gained from and added to social injustice, encourage students to consider how bias, culture and society shape the science, draw on under-represented sources and diverse case studies, and review materials regularly for bias.",
     prac="Present a balanced history of the field, including the prejudice some influential scientists held or benefited from; have students examine how bias shapes what science is done and how data are read; use diverse sources and cases, and check teaching materials regularly.")
prov('1.19', F('Curricula should recognise the discoveries', 'other inequalities.'), 'should',
     'diverse contributors recognised, students free to connect topics with their own experience, and the misuse of discoveries weighed',
     '1.17, 1.18 and 4.5.b8', 'when a team plans how students choose topics or discuss the uses of research',
     'Do students get to choose topics that connect with their own background, and how is that supported?',
     verbs=['recognise', 'explore', 'evaluate', 'reflect'], about='diverse contributors and the uses of knowledge',
     para="Curricula should credit the work of biologists and Biomedical Scientists from varied backgrounds; learners should be able to explore topics that inspire them in the light of their own experience, and students should be encouraged to weigh the good and harm of applying discoveries, including uses that deepen inequality.",
     prac="Recognise discoveries by scientists of diverse identities; give students room to explore topics linked to their lived experience; ask them to judge how discoveries, such as drug development and targeting, can be turned to ends that widen inequality.")
prov('1.20', F('Equity involves enabling access', 'Sciences course.'), 'should',
     'equitable access to the course, based on each person\'s potential to complete it, with needless barriers removed',
     '1.21, 1.22 and 2.7', 'when a team reviews admissions or the barriers students meet',
     'Which of your entry or course requirements could stop someone who could complete the course?',
     verbs=['enabling', 'eliminating', 'complete'], about='equitable access based on potential',
     para="Equity means opening the course to people with different needs and removing arbitrary barriers to success; access should be fair and rest on a person's potential to complete the course.",
     prac="Base access on each applicant's potential to finish the course, and remove barriers that serve no purpose.")
prov('1.21', F('Biomedical Science and/or Biomedical Sciences course teams must pay attention', 'accessibility for all.'), 'must',
     'curricula, teaching, assessment and practical work designed to be fully accessible, with inclusive design and reasonable adjustments, and varied learning and assessment',
     '1.20, 1.22, 2.7, 2.8 and the assessment principle 3.20.b3', 'when a team designs practical classes or assessments',
     'Which practical or assessment task in the course would be hardest for a disabled student, and what has been done about it?',
     verbs=['pay', 'designed', 'offered'], about='fully accessible curricula and assessment',
     para="Course teams must make sure curricula, teaching, assessment and practical work are designed to be fully accessible and flexible; all students should have equally accessible learning and assessment, by inclusive design where possible and individual adjustment where needed, and both should be varied.",
     prac="Design curricula, teaching, assessment and practical work to be fully accessible from the start; use inclusive design first and reasonable adjustments where needed; vary learning and assessment to reflect the subject and widen access.")
prov('1.22', F('Equitable access to the course for all students', 'accessible to all students.'), 'should',
     'access planned ahead and flexibly, fieldwork, laboratories and placements included, with barriers removed in response to feedback and close work with student support',
     '1.20, 1.21 and 2.17', 'when a team plans fieldwork, laboratory work or placements',
     'How would the course find out, before term, that a student needs a different arrangement for laboratory work?',
     verbs=['considered', 'addressed', 'prevent', 'refine', 'improve', 'work'], about='anticipating access in practical work and placements',
     para="Equitable access for every student should be considered in advance and flexibly, including fieldwork, laboratory work and placements; teams should build flexibility into teaching and assessment, keep personal characteristics from limiting access to the curriculum, act on feedback, and work with student support.",
     prac="Plan access ahead for fieldwork, laboratories and placements; build flexibility into teaching and assessment; let no characteristic, such as disability, neurodiversity or social capital, limit access; act on feedback and work with student support so staff and students are both supported.")
prov('1.25', F('To support the inclusion of sustainable development', 'within the curricula.'), 'should',
     'the QAA and Advance HE ESD guidance used for teaching, competencies, outcomes and assessment in sustainability',
     '1.23, 1.24 and std:doc:qaa-advancehe-esd-2021-guidance', 'when a team plans where sustainability sits in its outcomes or assessment',
     'Which learning outcomes in the course mention sustainability, and how are they assessed?',
     verbs=['refer', 'address'], about='using the ESD guidance',
     para="Those building sustainable development into these courses should use the QAA and Advance HE guidance on Education for Sustainable Development for teaching, key competencies, outcomes and assessment.",
     prac="Use the QAA and Advance HE ESD guidance when writing sustainability into teaching, competencies, learning outcomes and assessment.")
s('1.30', find=F('The student will take responsibility', 'as appropriate.')[0], after=F('The student will take responsibility', 'as appropriate.')[1],
  type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students of the subjects', addressee='learner',
  verbs=['take', 'demonstrating', 'supporting'], about='continuing personal and professional development', domain='generic-skill', award=BOTH,
  para="Students will take charge of their own continuing personal and professional development, showing commitment to learning and self-improvement and, where fitting, helping others develop.",
  prac="Expect students to take responsibility for their continuing development: plan for reflection, goal setting and peer support so they can show commitment to learning and help others where appropriate.",
  ben="You will take charge of your own personal and professional development, keep learning and improving, and help others to develop where it fits.",
  aaw=f"Treat this as a stated outcome (will) for students on these courses, read at FHEQ level 6 for honours (inferred: the paragraph names no level). Cite it as {CITE}, para 1.30. Do not present it as a registration requirement. Set it beside qaa/fheq-2024/4.15.b9.3, spine:6 and 4.5.b15 in this document.",
  aad="Raise this when a student asks how to plan their development or what reflection is for, or when a team designs personal tutoring. To a student, frame it as owning your own learning and helping peers; to staff, as a habit the course should build. Ask: 'What is one skill you want to improve this year, and how will you know you have?' Avoid turning it into a checklist read out from the text.")

# ------------------------------------------------------------------ section 2
s('2.1', find=F('Students should confirm the accreditation status', 'before they apply.')[0], after=F('Students should confirm the accreditation status', 'before they apply.')[1],
  type='expectation', rung='none', force='should', level='none', appliesTo='prospective students', addressee='learner',
  verbs=['confirm', 'apply'], about='checking accreditation before applying', domain='none', award=HON,
  para="Applicants should check whether a course is accredited before applying.",
  prac="Make the accreditation status of the course clear in admissions material, since applicants are advised to check it before they apply.",
  ben="Before you apply, check whether the course is accredited by the professional body, especially if you want to register as a Biomedical Scientist.",
  aaw=f"Treat this as a should-level expectation addressed to prospective students: confirm a course's accreditation before applying. It sets no level. Cite it as {CITE}, para 2.1. Do not claim it puts a duty on the course; set it beside 1.2, 1.3 and 3.2 in this document, which explain why accreditation matters.",
  aad="Raise this when a prospective student asks about routes to registration or compares courses. In plain words, explain that only an accredited Biomedical Science degree gives the academic basis for registration. Ask: 'Do you want to work in a hospital diagnostic laboratory, and does the course you are considering hold the accreditation for that?' Avoid implying an unaccredited course is a lesser degree.")
prov('2.4', F('Credit-bearing placements should, however,', 'their academic study.'), 'should',
     'credit-bearing placements integrated with the programme so students link the experience to their academic study',
     '2.17, 1.12 and 2.11', 'when a team designs or reviews a placement year or module',
     'How does a student\'s placement work come back into their final-year study?',
     verbs=['integrated', 'relate', 'use'], about='integrating credit-bearing placements',
     para="Where placements carry credit, they should be woven into the programme so students can connect what they experience with their academic work and use the skills they built there.",
     prac="Integrate credit-bearing placements with the programme, with tasks that make students relate the placement to their study and use its skills.")
prov('2.6', F('The academic component of degree apprenticeships', 'Subject Benchmark Statement.'), 'should',
     'the academic part of Biomedical Science or Healthcare Science Practitioner degree apprenticeships follows this statement',
     '2.21 and the Characteristics Statement for Higher Education in Apprenticeships (not yet ingested, Part E)', 'with a team designing a degree apprenticeship in the area',
     'Which outcomes in Table 1 does the apprenticeship\'s academic part cover, and where?',
     verbs=['follow'], about='degree apprenticeships follow the statement', award=HON,
     para="The academic part of Biomedical Science or Healthcare Science Practitioner degree apprenticeships should follow this statement.",
     prac="Design the academic component of the apprenticeship to the same standards as the degree.")
prov('2.7', F('All degree courses covered in this Statement can ensure', 'accessibility for all.', '2.7 All degree'), 'should',
     'equally accessible learning and assessment through inclusive design and reasonable adjustment, with varied experiences',
     '1.21, 2.8 and 3.20.b3', 'when a team reviews its learning and assessment for accessibility',
     'Which adjustments are made so often that they could be built into the design for everyone?',
     verbs=['ensure', 'incorporated', 'reflect', 'increase'], about='equally accessible learning and assessment',
     para="Courses can offer all students equally accessible learning and assessment; this should come through inclusive design where possible and reasonable adjustment where needed, and learning and assessment should be varied.",
     prac="Make learning and assessment equally accessible, by inclusive design first and individual adjustment where necessary, and vary them to reflect the subject and widen access.")
prov('2.8', F('Biomedical Science and/or Biomedical Sciences course teams can also ensure', 'complete their course.'), 'should',
     'accessible design, and support for every learner in verbal, spatial and numerical skills',
     '1.21, 2.7 and the mathematics row 4.5.b10', 'when a team plans support for numeracy or study skills',
     'Where do students who arrive with weaker numerical skills get help, and is it timely?',
     verbs=['ensure', 'supported'], about='support for verbal, spatial and numerical skills',
     para="Course teams can make the course fully accessible, and all learners should be supported to develop the verbal, spatial and numerical skills, and other approaches, they need to complete it.",
     prac="Support every learner in the verbal, spatial and numerical skills the course depends on, alongside accessible design.")
prov('2.9', F('Biomedical Science and/or Biomedical Sciences degree course should be designed', 'variety of other sectors.'), 'should',
     'design that promotes academic and personal development, moving students from simple concepts to graduate competence',
     '2.10, 3.15, 4.1 and spine:6', 'when a team maps how demand rises across the years of a course',
     'What can a student do in their final year that they could not do in their first, and where is it assessed?',
     verbs=['designed', 'promote', 'apply', 'develop', 'analyse', 'evaluate'], about='progression from simple concepts to graduate competence',
     addressee='both', level='fheq:6', award=HON,
     ben="Your course is designed to move you from using what you know on simple, well-defined problems towards handling complex ideas, analysing and evaluating data and solving problems with confidence, so that by graduation you are competent across knowledge, understanding, experience and skills.",
     para="Degree courses should be designed to foster academic and personal growth: students will move from applying simple ideas to well-defined problems to linking complex concepts, analysing and evaluating data and solving problems, and will be competent across knowledge, understanding, experience and skills on graduating.",
     prac="Plan progression explicitly: early tasks apply simple concepts to defined problems; later ones ask students to connect complex concepts and analyse and evaluate data; by graduation students will be competent across the range.")
P['2.9']['aad'] = ("Raise this when a student asks why the course gets harder or what is expected by the final year, or when a team maps progression. To a student, put it as moving from simple, defined tasks to complex ones you handle with confidence; to staff, as the design of rising demand. Ask: 'Which task this year asked you to link ideas from different modules?' Avoid presenting the graduate end point as what is expected in the first year.")

# 2.10 strategies (lead-in: progression should be reinforced by strategies that)
L210 = {1: (['recognise'], 'diverse prior experience and transition', "take account of how varied students' earlier experience is and how hard the move into university can be"),
        2: (['allow', 'achieve', 'realise'], 'every student reaching their potential', 'let every student reach their potential and ambitions, whatever their background or reasons for studying'),
        3: (['support'], 'academic and personal development', 'support academic and personal growth as well as learning'),
        4: (['matched'], 'matched to outcomes at each level', "fit the course's learning outcomes or competencies at each level of study")}
for n, (verbs, about, X) in L210.items():
    i = '2.10.b%d' % n
    P[i] = dict(type='expectation', rung='none', force='should', level='none', appliesTo='learning, teaching and assessment methods', addressee='provider',
                verbs=verbs, about=about, domain='none', award=BOTH, ben=NA,
                para=f"Progression should be reinforced by strategies that {X}.",
                prac=f"Back the progressive design of teaching and assessment with strategies that {X}.",
                aaw=f"Treat this as a should-level expectation on the course's teaching and assessment strategies: they {X}. It applies across the courses the statement covers, at every level of study. Cite it as {CITE}, para 2.10 (item {n}). Do not present it as a student outcome; set it beside the other 2.10 items, 2.9 and 3.15.",
                aad=f"Raise this when a team reviews how students are supported through the transitions of the course. Frame it for staff as part of how progression is built: strategies that {X}. Ask: 'What evidence shows that this strategy works for students who arrive with less preparation?' Do not give it to a student as their own task.")
prov('2.11', F('Students on a Biomedical Science and/or Biomedical Sciences degree course will progress', 'than that for a bachelor’s course.'), 'will',
     'progression from one level to the next by meeting the institution\'s regulations, which require at least the threshold standard for the level',
     '4.1, 4.5.b1 to 4.5.b16 and qaa/fheq-2024/annex-d/summary/lead/3rd', 'when a student asks what they need to progress, or when a team reviews progression rules',
     'Do the progression rules say which components, such as practical work or core clinical specialisms, must each be passed?',
     verbs=['progress', 'demonstrate', 'met'], about='progressing by meeting at least the threshold',
     type='requirement', addressee='learner', level='fheq:6', domain='none',
     ben="To move from one year or level to the next you will need to meet your university's rules, which ask you to show at least the threshold standard for that level; on an accredited Biomedical Science course you may also need to pass every core clinical specialism.",
     para="Students will progress between levels by meeting their institution's regulations, which require them to show at least the threshold standard for the level, usually with credit for all learning and assessment, practical work included; extra criteria may apply, such as passing every core clinical specialism on an accredited degree, and integrated master's courses may set a higher standard.",
     prac="State progression rules plainly: at least the threshold for the level, credit across all components including practicals, any extra rules such as passing each core clinical specialism, and any higher standard for the integrated master's.")
P['2.11']['aad'] = ("Raise this when a student asks what they need to progress or worries about a failed component. To a student, say plainly that you must meet at least the minimum standard for your level and that some courses ask you to pass every core specialism; to staff, frame it as rules that must be clear and published. Ask: 'Do you know which of your modules must each be passed before you can move on?' Avoid presenting the excellent standard as what progression needs.")
prov('2.14', F('Given that Biomedical Science and/or Biomedical Sciences courses must contain', 'range of environments.'), 'must',
     'practical skills are a required part of every course, with teams planning how bench and virtual practice develop them',
     '1.10, 4.5.b4 and its cells, and 4.5.b3', 'when a team plans the balance of bench and virtual practicals',
     'Which practical skills can only be learned at the bench, and how much bench time do they get?',
     verbs=['contain', 'consider', 'support'], about='practical skills in every course',
     para="Since the courses must include gaining practical skills, course teams need to plan how they will develop them, using bench practicals backed by online tutorials and virtual practice that can happen in various settings.",
     prac="Include practical skills in every course and plan how to develop them, combining bench sessions with online tutorials and virtual practicals.")
prov('2.15', F('Courses also need to be sufficiently flexible', 'arise in the future.'), 'should',
     'courses flexible enough to respond to change in the subject and in employers\' needs, and resilient enough to adapt to disruption',
     '2.13 and 2.27', 'when a team reviews how quickly its curriculum can change',
     'How long would it take the course to add a new technique that has become standard in practice?',
     verbs=['respond', 'anticipate', 'adapt'], about='flexible and resilient courses',
     para="Courses need enough flexibility to respond to and anticipate change in the subject, its links with other disciplines and the needs of graduates and employers, and should be resilient enough to adapt to disruption such as a pandemic.",
     prac="Keep the course able to change with the subject and with employers' needs, and plan for disruption so teaching can adapt.")
prov('2.16', F('Providers are expected to develop processes', 'employers’ needs.'), 'should',
     'oversight of partners in degree delivery, with effective communication and regular consultation so courses keep meeting employers\' needs',
     '2.17 and 2.21', 'with a team delivering a course with a college, an overseas partner or an NHS or industry partner',
     'How does the course know that a partner meets the same standards, and how often is that checked?',
     verbs=['develop', 'ensure', 'meet'], about='oversight of delivery partners',
     para="Providers are expected to set up oversight so partners in degree delivery meet the relevant standards; this should include good communication and regular consultation so courses keep meeting employers' needs.",
     prac="Put oversight in place for every delivery partner, with clear communication and regular consultation, including with employers.")
prov('2.17', F('Courses should work with relevant stakeholders', 'accessible to all.'), 'should',
     'work-based or work-like learning with stakeholders, extensive engagement with employment sectors, a clear employability strategy and placements made inclusive',
     '1.26 to 1.30, 2.4 and 3.21.b1', 'when a team reviews its employability strategy or its placements',
     'Which students miss out on placements now, and would funding or payment change that?',
     verbs=['work', 'incorporate', 'develop', 'engage', 'considered'], about='employability and inclusive placements',
     para="Courses should bring in work-based or work-like learning with stakeholders, engage widely with employers, and have a clear strategy for employment-focused skills; funding or payment should be considered so placements are open to all.",
     prac="Work with employers and other stakeholders on work-based learning, set out an employability strategy, and consider funding or paying placements so that every student can take one.")
prov('2.19', F('Students should expect to be embraced as partners', 'may be established.'), 'should',
     'students treated as partners, with student voice playing a large part in course development, delivery and review, and students involved in quality review',
     '2.21 and 2.27', 'when a team plans how students take part in course review or design',
     'Which decision about the course last year changed because of what students said?',
     verbs=['expect', 'embraced', 'play', 'involved'], about='students as partners in their courses', addressee='both',
     ben="You can expect to be treated as a partner in your course: your views should shape how it is developed, taught and reviewed, through representatives, surveys and other routes, and you should be able to take part in reviewing its quality.",
     para="Students should expect to be partners in their courses; student voice should shape course development, delivery and review, through representatives, surveys and other channels, and students should take part in quality review and the design of new courses.",
     prac="Treat students as partners: give student voice real weight in developing, delivering and reviewing the course, and involve students in quality review and new course design, for example through steering groups.")
P['2.19']['aad'] = ("Raise this when a student asks how they can influence their course, or when a team plans review. To a student, explain plainly that your views count and how to raise them; to staff, frame it as partnership with evidence of change. Ask: 'Have you had a chance to say what should change in your course, and did anything happen?' Avoid treating partnership as only filling in surveys.")
prov('2.21', F('Monitoring and review should include feedback', 'degree apprenticeships.'), 'should',
     'monitoring and review drawing on current students, employers, placement providers and alumni, and on employers and apprentices for apprenticeships',
     '2.19, 2.23 and 2.27', 'when a team plans its periodic review',
     'Whose feedback is missing from the last review of the course?',
     verbs=['include', 'influence'], about='feedback that informs review',
     para="Monitoring and review should draw on feedback from current students, employers, placement providers and alumni, and for degree apprenticeships from employers and apprentices, to shape the curriculum, its content and delivery.",
     prac="Collect feedback from students, employers, placement providers and alumni, and from apprentices and their employers where relevant, and show how it shaped the course.")
prov('2.23', F('Evaluation of student performance data and various measures', 'external examiners.'), 'should',
     'student performance data and measures of experience integrated with expert review, external examiners included',
     '2.21, 2.25 and 2.27', 'when a team prepares its annual monitoring',
     'How are external examiners\' comments read alongside the course\'s own data?',
     verbs=['integrated'], about='data and expert review together',
     para="Evaluation of student performance and experience data should be combined with expert review, including external examiners' views.",
     prac="Bring performance and experience data together with expert and external examiner review when evaluating the course.")
prov('2.24', F('Higher education providers will use external reviewers', 'appropriate for the subject.'), 'will',
     'external reviewers used in periodic review to give an outside view and check that threshold standards are met and content suits the subject',
     '2.25, 4.1 and 4.5.b1 to 4.5.b16', 'when a team prepares for periodic review',
     'Which external reviewer will look at the course, and what will they check it against?',
     verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review',
     para="Providers will use external reviewers in periodic review to gain an outside view of proposed changes and to make sure threshold standards are met and content suits the subject.",
     prac="Involve external reviewers in periodic review to test proposed changes, threshold standards and the fit of content to the subject.")
prov('2.27', F('Programme and course teams should also conduct', 'courses of study.'), 'should',
     'regular monitoring and evaluation with independent evaluators and student feedback, data integrated with expert review, and students, graduates, employers, service users and professional bodies involved in enhancement',
     '2.21 and 2.23', 'when a team sets its enhancement plan',
     'Have service users or professional bodies had any part in the last change to the course?',
     verbs=['conduct', 'ensure', 'integrated', 'involved'], about='regular monitoring and enhancement',
     para="Programme and course teams should monitor and evaluate regularly, with independent evaluators and student feedback, combining performance data and student voice with expert review so curricula stay current, engaging and accessible; students, graduates, employers, service users and professional bodies should help design and deliver enhancements.",
     prac="Monitor and evaluate the course regularly with independent and student input, use data trends to spot issues, and involve students, graduates, employers, service users and professional bodies in improving it.")

# ------------------------------------------------------------------ section 3: paragraphs
prov('3.2', F('Biomedical Science courses are required to cover all', 'as Biomedical Scientists.'), 'must',
     'the singular degree covers every clinical laboratory specialism in the professional body\'s accreditation criteria and must hold that accreditation so its graduates satisfy the academic conditions for registration',
     '1.2, 3.4 and its items 3.4.b2 to 3.4.b47', 'with a team seeking or renewing accreditation of a Biomedical Science or Healthcare Science degree',
     'Can you show where each specialism in the accreditation criteria is taught and assessed?',
     verbs=['required', 'cover', 'accredited', 'meet'], about='full specialism coverage and accreditation', type='requirement', award=HON, level='fheq:6',
     para="Biomedical Science courses must cover all the clinical laboratory specialisms set out in the professional body's accreditation criteria, and such degrees, whether called Biomedical Science or Healthcare Science, must hold that body's accreditation so their graduates satisfy the academic conditions for registration.",
     prac="Cover every clinical laboratory specialism the IBMS accreditation criteria list, and hold IBMS accreditation, so graduates meet the academic requirements for HCPC registration.")
s('3.3', find=F('Through a systems-led approach, students will integrate', 'intervention strategies.')[0], after=F('Through a systems-led approach, students will integrate', 'intervention strategies.')[1],
  type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students and graduates of Biomedical Science (singular) courses', addressee='learner',
  verbs=['integrate'], about='integrating the specialisms by body system', domain='understanding', award=HON,
  para="Working system by system, students will bring the clinical laboratory specialisms together with the underlying science of disease processes, investigation and treatment; graduates know the current laboratory methods for studying, diagnosing and monitoring health and disease, and how new methods and therapies are developed and evaluated.",
  prac="Teach through a systems-led approach so students will join up the specialisms with the science of investigation and treatment of particular diseases, and know current laboratory methods and how new ones are developed and evaluated.",
  ben="You will learn to join up what you know from each laboratory specialism, disease by disease and system by system, and you will know the current laboratory methods used to investigate, diagnose and monitor health and disease, and how new methods and treatments are tested.",
  aaw=f"Treat this as a stated outcome (will) for students on the singular Biomedical Science honours degree (FHEQ level 6). Cite it as {CITE}, para 3.3. Do not claim it holds for Biomedical Sciences (plural) or that it is an HCPC standard. Set it beside 3.4.b2 to 3.4.b47, 4.5.b9 and the FHEQ honours descriptor qaa/fheq-2024/4.15.b1.",
  aad="Raise this when a student asks how the separate specialisms fit together, or when a team designs integrated case studies. To a student, put it as following one patient's disease across several laboratories; to staff, as the systems-led design. Ask: 'For a patient with suspected kidney disease, which laboratory specialisms would be involved, and what would each add?' Avoid reading the paragraph aloud.")
s('3.4', find=F('IBMS-accredited Biomedical Science or Healthcare Science courses will contain', 'IBMS Registration Training Portfolio.')[0],
  after=F('IBMS-accredited Biomedical Science or Healthcare Science courses will contain', 'IBMS Registration Training Portfolio.')[1],
  type='requirement', rung='none', force='must', level='fheq:6', appliesTo='IBMS-accredited Biomedical Science or Healthcare Science courses and their graduates', addressee='both',
  verbs=['contain', 'required', 'studied', 'passed', 'meet'], about='the clinical pathology subject areas, all studied and passed', domain='knowledge', award=HON,
  para="Accredited Biomedical Science or Healthcare Science courses will include the clinical pathology subject areas below, beyond the common content, and graduates are required to have studied and passed every specialism to meet the education standards for registration, once both the degree and the training portfolio are complete.",
  prac="Include every listed clinical pathology area in the accredited course, and make sure each graduate has studied and passed every specialism: this, with the verified training portfolio, meets the education standards for registration.",
  ben="On an accredited Biomedical Science course you will study all the clinical pathology specialisms, and you must pass every one of them, as well as completing your training portfolio, to meet the education standards for registration.",
  aaw=f"Treat this as a requirement (required, recorded as must) for IBMS-accredited Biomedical Science or Healthcare Science honours degrees (FHEQ level 6): the clinical pathology areas are taught, and every graduate has studied and passed each one. Cite it as {CITE}, para 3.4. Do not claim it holds for Biomedical Sciences (plural) courses or that passing the degree alone gives registration. Set it beside its items 3.4.b2 to 3.4.b47, 3.2 and 1.2.",
  aad="Raise this when a student on the accredited route asks whether a weak result in one specialism matters, or when a team sets its progression and award rules. Say plainly to a student that every specialism has to be passed for the route to registration; to staff, frame it as a rule to build into regulations. Ask: 'Which specialism do you feel least sure of, and when is it assessed?' Avoid applying it to students on a broader Biomedical Sciences course.")

# 3.4 clinical pathology outcome lists (lead-ins: "A Biomedical Science graduate will have knowledge of:")
SPEC = [('cellular pathology', [2, 3, 4, 5]), ('clinical biochemistry', [7, 8, 9, 10]), ('clinical immunology', [12, 13, 14]),
        ('haematology', [16, 17, 18, 19, 20]), ('transfusion science', [22, 23, 24, 25, 26, 27]), ('clinical genetics', [29, 30, 31, 32]),
        ('medical microbiology', [34, 35, 36, 37]), ('near-patient testing', [39, 40, 41]), ('laboratory quality', [43, 44, 45, 46, 47])]
SPEC_OF = {n: sp for sp, ns in SPEC for n in ns}
I34 = {
    2: ([], 'normal and diseased cell and tissue structure', 'how normal cells and tissues are built, at gross and fine scale, and how disease alters that structure'),
    3: ([], 'reproductive science', 'reproductive science, with infertility and the study of embryos'),
    4: ([], 'preparing cells and tissues for microscopy', 'how cells and tissues are prepared for examination under the microscope'),
    5: ([], 'visualisation and imaging in diagnosis', 'the principles and uses of imaging and visualisation methods, microscopy among them, in supporting diagnosis and the choice of treatment'),
    7: ([], 'collecting and analysing clinical samples', 'the common methods for collecting clinical samples and analysing them'),
    8: ([], 'investigating major organ systems', 'how the main body and organ systems are investigated, for example through kidney, liver, bone profile and tumour marker tests'),
    9: ([], 'biochemical investigations across the course of disease', 'the principles and uses of biochemical tests in screening for disease, diagnosing it, treating it and following its course'),
    10: ([], 'drug monitoring and substance misuse', 'monitoring of therapeutic drugs and the investigation of substance misuse'),
    12: ([], 'immune effectors and their measurement', 'how the effectors of the immune response work and how they are measured'),
    13: ([], 'abnormal immune function and its management', 'why immune function goes wrong and what follows, neoplastic disease and transplant reactions included, and how these are detected, diagnosed, treated and followed'),
    14: ([], 'immunological techniques', 'the principles and practice of immunological methods in screening, diagnosis, treatment and follow-up, with prophylaxis and immunotherapy'),
    16: ([], 'blood cells', 'how blood cells are formed, built and work'),
    17: ([], 'normal haemostasis', 'how normal haemostasis is regulated'),
    18: ([], 'blood cell morphology', 'the appearance of blood cells: recognising normal white cells and the usual red cell abnormalities'),
    19: ([], 'anaemias, malignancies and bleeding and clotting disorders', 'the nature and diagnosis of anaemias, blood cancers and disorders of bleeding and thrombosis'),
    20: ([], 'haematological techniques', 'the principles and practice of haematology methods in screening, diagnosis, treatment and follow-up'),
    22: ([], 'blood grouping and antibody screening', 'interpreting blood groups, the causes of grouping anomalies, and screening for antibodies'),
    23: ([], 'red cell antigens', 'the genetics, inheritance, structure and role of antigens on red cells'),
    24: ([], 'immune destruction of blood cells', 'the destruction of blood cells by the immune system'),
    25: ([], 'blood components', 'how blood components are prepared, stored and used'),
    26: ([], 'patient blood management', 'patient blood management'),
    27: ([], 'selecting components for transfusion', 'choosing suitable blood components for transfusion, and the adverse effects that can follow'),
    29: ([], 'omic methods for chromosomes and DNA', 'genomic, transcriptomic and proteomic methods for analysing human chromosomes and DNA'),
    30: ([], 'molecular biology and bioinformatics in medicine', 'how molecular biology and bioinformatics are applied in medicine'),
    31: ([], 'pharmacogenetics', 'pharmacogenetics and personalised medicine'),
    32: ([], 'genetic testing', 'the principles and practice of genetic testing in screening, diagnosis and follow-up, and the ethical questions it raises'),
    34: ([], 'how microorganisms cause disease', 'the mechanisms by which a range of microorganisms cause disease'),
    35: ([], 'public health microbiology', 'public health microbiology, the epidemiology and control of infection, and the One Health concept'),
    36: ([], 'detecting and controlling infection', 'the principles and practice of methods for screening, diagnosing, treating and following infectious diseases, for detecting and identifying microorganisms, and for preventing and controlling infection, vaccination and environmental and vector control included'),
    37: ([], 'antimicrobials and resistance', 'antimicrobial chemotherapy and resistance to antibiotics, antivirals, antifungals and anti-parasitic drugs'),
    39: ([], 'near-patient investigations', 'the principles and uses of investigations run on near-patient testing equipment for screening, diagnosis, treatment and follow-up'),
    40: ([], 'near-patient testing in patient pathways', 'how near-patient testing fits into patient pathways'),
    41: ([], 'quality assurance in near-patient testing', 'the quality assurance points that bear on near-patient testing'),
    43: ([], 'quality control standards', 'how to interpret quality control standards'),
    44: ([], 'quality assurance and pre-analytical variables', 'why quality assurance and pre-analytical variables matter'),
    45: ([], 'external quality assessment', 'why external quality assessment matters'),
    46: ([], 'quality management', 'quality management at a basic level: quality policy, audit, standard operating procedures, training and competency records, error and incident reporting, validation and verification, and reagent stock'),
    47: ([], 'laboratory accreditation', 'laboratory accreditation, with a basic awareness of UKAS and ISO standards'),
}

def outcome_item(i, para_n, course, short, verbs, about, X, domain, fheq, nbrs, force='will', award=HON, applies=None):
    P[i] = dict(type='outcome', rung='none', force=force, level='fheq:6', appliesTo=applies or f'graduates of {course} courses', addressee='learner',
                verbs=verbs, about=about, domain=domain, award=award,
                para=f"{short} graduates will know {X}." if force == 'will' else f"Graduates acquire {X}.",
                prac=(f"Teach and assess {about} so that every {short} graduate will know {X}." if force == 'will'
                      else f"Plan the course so students acquire {X}, and show where it is developed and evidenced."),
                ben=(f"On this course you will come to know {X}." if force == 'will' else f"Your course aims to help you build {X}."),
                aaw=(f"Treat this as a stated outcome (will) for every {short} honours graduate (FHEQ level 6; FQHEIS level 10 in Scotland): knowledge of {about}. "
                     f"Cite it as {CITE}, para {para_n}. Do not claim it holds for other courses in the area, or that it is a professional body's own requirement. "
                     f"Set it beside {nbrs}, the FHEQ honours descriptor {fheq} and spine:6.") if force == 'will' else
                    (f"Treat this as a graduate attribute the statement describes, in plain present with no modal, for all its courses at honours (FHEQ level 6, inferred): {about}. "
                     f"Cite it as {CITE}, para {para_n}. Do not present it as a threshold every graduate must show or as a regulatory requirement. "
                     f"Set it beside {nbrs}, the FHEQ honours descriptor {fheq} and spine:6."),
                aad=(f"Raise this when a {short} student asks what they need to know about {about}, or when a team checks its modules against the core content. "
                     f"To a student, say plainly that by the end you need a working command of it; to staff, frame it as core content to teach and assess. "
                     f"Ask: 'Where in your course have you met {about}, and could you explain it to a colleague?' "
                     f"Do not read the list aloud or suggest it applies to every course in the area.") if force == 'will' else
                    (f"Raise this when a student asks what kind of graduate the course aims to produce, or when a team reviews its graduate attributes. "
                     f"To a student, put it plainly as a strength you can build and show; to staff, as an attribute to plan for and evidence. "
                     f"Ask: 'Where have you shown {about} on your course so far?' "
                     f"Avoid presenting it as a pass requirement or reading the list aloud."))

for n, (verbs, about, X) in I34.items():
    sp = SPEC_OF[n]
    outcome_item('3.4.b%d' % n, f'3.4 ({sp})', 'IBMS-accredited Biomedical Science', 'Biomedical Science', verbs, about, X, 'knowledge',
                 'qaa/fheq-2024/4.15.b1', f'the other {sp} items in 3.4, the lead-in 3.4 and 3.2',
                 applies='graduates of IBMS-accredited Biomedical Science or Healthcare Science courses')

# 3.6 Pharmacology
I36 = {
    2: ([], 'molecular drug targets', 'the molecular targets drugs act on, such as receptors, enzymes, ion channels and transporters', 'knowledge'),
    3: ([], 'drug-receptor relationships', 'how drugs relate to receptors, covering agonism and antagonism, specificity and selectivity, potency, desensitisation and tolerance', 'knowledge'),
    4: ([], 'main drug targets and how drugs alter them', 'the structure and function of the main drug targets and how drugs change that function at molecular level', 'knowledge'),
    5: ([], 'drug effects on organ systems and cells', 'how drugs act on the major organ systems and on cell function, proliferation and death', 'knowledge'),
    6: ([], 'pharmacokinetics', 'pharmacokinetics, what the body does to drugs: their absorption, distribution, biotransformation and excretion', 'knowledge'),
    7: ([], 'individual variation and personalised medicine', 'why people differ in drug response and toxicity, through ethnicity, gender, age, pregnancy, genes, disease and drug interactions, and the emerging technologies of personalised medicine', 'knowledge'),
    9: ([], 'concentration-response relationships', 'how drug concentration or dose relates to response', 'subject-skill'),
    10: ([], 'experimental methods in pharmacology', 'experimental methods used in pharmacology, such as bioassays, receptor binding and cloning, therapeutic recombinant proteins, animal disease models and genetic manipulation', 'subject-skill'),
    11: ([], 'animals in research', 'the ethics and law of using animals in research, and ways to replace, refine and reduce that use', 'understanding'),
    12: ([], 'drug discovery, development and regulation', 'how drugs are discovered and developed, toxicology included, and the regulation that oversees their quality, safety and effectiveness', 'knowledge'),
    13: ([], 'clinical trials', 'the principles of clinical trials (bias, sample size, the placebo effect, therapeutic index) and the ethics of using human participants and tissues', 'understanding'),
}
for n, (verbs, about, X, dom) in I36.items():
    outcome_item('3.6.b%d' % n, '3.6', 'Pharmacology', 'Pharmacology', verbs, about, X, dom,
                 'qaa/fheq-2024/4.15.b2' if dom == 'subject-skill' else 'qaa/fheq-2024/4.15.b1', 'the other 3.6 items and 3.5')

# 3.9 Human Nutrition
I39 = {
    2: ([], 'nutrients, metabolism and the cellular basis of disease', 'the chemistry of life, how nutrients work in the main metabolic pathways, and the cellular and molecular roots of disease, gene expression included'),
    3: ([], 'clinical biochemistry of disease and nutrition', 'the clinical biochemistry of human disease and how it is managed, weighted towards nutritional factors'),
    4: ([], 'assessing nutritional status across the life cycle', 'how nutritional status is assessed, the main nutritional issues at each life stage, and how socio-demographic, economic and environmental factors shape diet'),
    5: ([], 'food science and safety', 'the ideas and processes of food science, safety, storage, processing and microbiology'),
    6: ([], 'clinical nutrition and health promotion', 'clinical nutrition, diet therapy, health promotion and nutrition education'),
    7: ([], 'sport and exercise nutrition', 'nutrition for sport and exercise performance'),
    8: ([], 'gene-nutrient interactions', 'how genes and nutrients interact and what that may mean for preventing diet-related disease'),
    9: ([], 'nutrition and the nature of disease', 'how nutritional status bears on disease, and a core theoretical sense that human disease and its care draw on many disciplines'),
}
for n, (verbs, about, X) in I39.items():
    outcome_item('3.9.b%d' % n, '3.9', 'Human Nutrition', 'Human Nutrition', verbs, about, X, 'knowledge', 'qaa/fheq-2024/4.15.b1', 'the other 3.9 items, 3.7 and 3.8')

# 3.11 Physiology
I311 = {
    2: ([], 'levels of organisation and regulation', 'the levels of organisation from chemical to whole organism, and the internal and external factors that regulate body systems'),
    3: ([], 'structure and function of body systems', 'how structure relates to function in each body system, what each system fundamentally does and how the systems interrelate'),
    4: ([], 'life processes', 'the processes of life: metabolism, responsiveness, movement, growth, differentiation and reproduction'),
    5: ([], 'cell-cell communication', 'the systems by which cells communicate with each other'),
    7: ([], 'homeostasis', 'homeostasis, both self-regulation and regulation from outside the organ'),
    8: ([], 'the nervous system', 'neural tissue, the spinal cord, spinal nerves and reflexes, the brain, cranial nerves and neural integration'),
    9: ([], 'fluid, electrolyte and acid-base balance', 'the balance of fluids, electrolytes, acids and bases, its control, its disturbances and their effect on health'),
    10: ([], 'the endocrine system', 'the endocrine system: how hormones are secreted and distributed and how they act'),
    11: ([], 'stress responses', 'how the body responds to internal and external stressors'),
    12: ([], 'coordination of body systems', 'how neuronal, hormonal and chemical signals coordinate and integrate the work of body systems'),
    13: ([], 'adaptation and survival', 'how physiological responses and regulation allow adaptation and survival as the environment changes'),
    15: ([], 'cell components and transport', 'the main parts of a human cell, its chief transport processes and how it keeps itself intact'),
    16: ([], 'cell differentiation and diversity', 'how cells differentiate and cycle, the variety of cell types, and the intracellular chemistry that sustains life and drives cell responses'),
    18: ([], 'tissues, injury and repair', 'the structure and function of epithelial and connective tissues and membranes, and how tissues are injured and repaired'),
    19: ([], 'skin, bone and joints', 'the basics of skin, bone structure, the skeleton and joints'),
    20: ([], 'muscle', 'skeletal muscle and the other kinds of muscle tissue'),
    21: ([], 'exercise physiology', 'exercise physiology, the effects of exercise and the nutrition linked to it'),
    23: ([], 'the cardiovascular system', 'the cardiovascular system: blood and haemostasis, the heartbeat and cardiodynamics, and cardiovascular physiology and its regulation'),
    24: ([], 'the lymphatic system', 'the lymphatic system, its organisation, defences and immunity'),
    26: ([], 'respiration', 'the respiratory system and its physiology'),
    27: ([], 'digestion and the hepatobiliary system', 'the digestive and hepatobiliary systems: their organs and the processes of digestion, absorption, detoxification and elimination'),
    28: ([], 'metabolism and energetics', 'metabolism and energetics'),
    29: ([], 'the urinary system', 'the urinary system and the principles of kidney physiology'),
    31: ([], 'reproductive systems', 'the reproductive systems and how they integrate with other systems'),
    32: ([], 'development and inheritance', 'development and inheritance, from fertilisation and pregnancy through prenatal development to foetal growth'),
    33: ([], 'inheritance, development and ageing', 'features of human inheritance, development and ageing'),
    35: ([], 'ethics and law of human and animal research', 'the ethics and law of using people, animals or tissues in research and elsewhere'),
    36: ([], 'core physiological techniques', 'the core techniques and practical skills of physiology: experimental design, measurement, data handling and statistical analysis'),
}
for n, (verbs, about, X) in I311.items():
    dom = 'subject-skill' if n == 36 else ('understanding' if n == 35 else 'knowledge')
    outcome_item('3.11.b%d' % n, '3.11', 'Physiology', 'Physiology', verbs, about, X, dom,
                 'qaa/fheq-2024/4.15.b2' if dom == 'subject-skill' else 'qaa/fheq-2024/4.15.b1', 'the other 3.11 items and 3.10')

# 3.13 and the attributes list 3.14
s('3.13', find=F('Graduate attributes integrated in all courses', 'continuing scientific advances.')[0], after=F('Graduate attributes integrated in all courses', 'continuing scientific advances.')[1],
  type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students of all the courses in the area', addressee='learner',
  verbs=['facilitate', 'acquire', 'recognise'], about='graduate attributes and the provisional state of knowledge', domain='generic-skill', award=BOTH,
  para="Graduate attributes built into every course help students gain the graduate and professional attributes fitting their subject, and students will recognise that much of what they learn is likely to change as science advances.",
  prac="Build graduate and professional attributes into the course, and make sure students will understand that much of what they are taught is provisional and will change.",
  ben="Your course will help you develop the attributes of a graduate and a professional in your subject, and you will come to see that much of what you learn now is likely to change as science moves on.",
  aaw=f"Treat this as a stated outcome (will) for students across all the courses in the area, read at FHEQ level 6 for honours (inferred). Cite it as {CITE}, para 3.13. Do not claim the attributes are a fixed or exhaustive list. Set it beside 3.14.b1 to 3.14.b8, 4.5.b15, qaa/fheq-2024/4.15.b4 and spine:6.",
  aad="Raise this when a student is unsettled that a textbook account has been overturned, or when a team reviews its graduate attributes. To a student, put it plainly: much of what you learn will change, so learning how to update it matters. Ask: 'Can you think of something in your subject that was taught differently ten years ago?' Avoid suggesting current knowledge is unreliable.")

I314 = {
    1: ([], 'the complexity of human processes', 'an appreciation of how complex and varied human processes are in health and disease', 'understanding', 'qaa/fheq-2024/4.15.b1'),
    2: (['read', 'evaluate'], 'reading and evaluating literature', 'the ability to read and judge relevant literature critically and in full, from its aims and design to its methods, data interpretation and use', 'generic-skill', 'qaa/fheq-2024/4.15.b5'),
    3: (['give', 'discuss', 'debate'], 'explaining and debating the subject', 'the capacity to explain the subject clearly, currently and accurately, and to discuss and debate it critically with specialists and non-specialists in suitable scientific language', 'generic-skill', 'qaa/fheq-2024/4.15.b8'),
    4: (['tested'], 'critical and analytical skills', 'critical and analytical skills, with the recognition that claims and hypotheses need testing and evidence needs weighing', 'generic-skill', 'qaa/fheq-2024/4.15.b7'),
    5: (['apply'], 'methods of study', 'the ability to use a variety of study methods to investigate, record and analyse material', 'generic-skill', 'qaa/fheq-2024/4.15.b2'),
    6: (['think', 'work', 'solve'], 'independent thinking and problem solving', 'the ability to think for themselves, work autonomously and solve problems', 'generic-skill', 'qaa/fheq-2024/4.15.b9.1'),
    7: (['identify', 'protect', 'exploit'], 'intellectual property', 'an understanding of how intellectual property is identified, protected and exploited in scientific innovation', 'understanding', 'qaa/fheq-2024/4.15.b1'),
    8: (['application'], 'global reach, impact and ethics', "an appreciation of the subject's global reach, its effects on human life and the environment, and the ethics of applying it", 'understanding', 'qaa/fheq-2024/4.15.b4'),
}
for n, (verbs, about, X, dom, fheq) in I314.items():
    outcome_item('3.14.b%d' % n, '3.14', 'all the', 'any', [v for v in verbs if v != 'application'], about, X, dom, fheq,
                 '3.13 and the other 3.14 items', force='describes', award=BOTH, applies='graduates of all the courses in the area')

prov('3.16', F('In this context, there is an expectation that all staf f', 'professional development opportunities.'), 'should',
     'everyone who teaches, demonstrators and visiting lecturers included, has access to educational professional development',
     '3.15 and the PSF dimensions std:doc:advancehe-psf-dimensions-2023-framework', 'when a team plans staff development or the use of demonstrators',
     'What development in teaching do demonstrators and visiting lecturers get before they work with students?',
     verbs=['contribute'], about='professional development for all teaching staff',
     para="All staff who contribute to student learning, temporary and visiting staff and demonstrators as well as permanent academics, should be able to draw on a range of development in teaching and learning.",
     prac="Offer educational development to everyone who teaches on the course, demonstrators and visiting lecturers as well as permanent staff.")
prov('3.19', F('Assessments should be authentic', 'ensure inclusivity.'), 'should',
     'authentic assessment with real-world application, allowing reasonable adjustments for inclusivity',
     '3.20, 3.21 and 1.21', 'when a team designs or reviews an assessment',
     'Which assessment in the course looks most like a task done at work, and which least?',
     verbs=['enhance', 'allow', 'ensure'], about='authentic and inclusive assessment',
     para="Assessments should be authentic, applied to real-world tasks that build employability and professional growth, and should allow reasonable adjustments so they are inclusive.",
     prac="Set authentic, work-related assessment that builds professional skills, and allow reasonable adjustments to keep it inclusive.")

# 3.20 principles for designing assessment (lead-in: "The following principles should be considered")
L320 = {1: (['associated'], 'assessment of and for learning', 'assessment serves learning as well as measuring it, and comes with effective feedback'),
        2: (['provide', 'demonstrate'], 'valid, reliable, consistent assessment', 'assessments are valid, reliable and consistent, and let students show mastery of a topic'),
        3: (['consider'], 'accessibility and EDI in assessment', 'assessment and feedback take explicit account of accessibility and EDI'),
        4: ([], 'clear assessment information', 'information on assessment and feedback is explicit, accessible and transparent'),
        5: (['planned', 'manage'], 'manageable workloads', 'assessment and feedback are planned so that students and staff can manage their workloads'),
        6: (['relate'], 'integral, aligned assessment', 'assessment and feedback are part of the course and plainly tied to its learning outcomes'),
        7: (['give', 'validate'], 'confirming knowledge through assessment', 'assessment and feedback give students a chance to confirm what they know and understand'),
        8: (['align'], 'alignment with accreditation', 'assessment and feedback meet accreditation and approval requirements where needed'),
        9: (['provided'], 'balancing formative and summative assessment', 'formative and summative assessment are balanced and usefully linked')}
for n, (verbs, about, X) in L320.items():
    i = '3.20.b%d' % n
    P[i] = dict(type='expectation', rung='none', force='should', level='none', appliesTo='assessment design', addressee='provider',
                verbs=verbs, about=about, domain='none', award=BOTH, ben=NA,
                para=f"In designing assessment, teams should consider the principle that {X}.",
                prac=f"Design assessment so that {X}.",
                aaw=f"Treat this as a should-level principle for those designing assessment: {X}. It applies across the courses the statement covers, at every level. Cite it as {CITE}, para 3.20 (principle {n}). Do not present it as a student outcome or a regulation; set it beside the other 3.20 principles, 3.19 and 3.24.",
                aad=f"Raise this when a team designs, reviews or moderates assessment. Frame it for staff as a design check: {X}. Ask: 'How would you show an external examiner that this principle holds for your module?' Do not give it to a student as something they must do.")
prov('3.24', F('Feedback should be personal/individual', 'clear in advance.'), 'should',
     'feedback that is personal, understandable, empowering, manageable, developmental, timely and relevant, with support to interpret it and its timing made clear in advance',
     '3.20.b1 and 3.19', 'when a team sets its feedback policy or a student asks what feedback to expect',
     'Do students know, before they submit, when and in what form their feedback will come?',
     verbs=['allow', 'made'], about='qualities of good feedback',
     para="Feedback should be personal, understandable, empowering, manageable and developmental, timely and relevant to the brief, with access to help in interpreting it; it should support reflection, and its nature, extent and timing should be made clear in advance.",
     prac="Give feedback that is individual, clear, timely and tied to the brief, help students interpret it, and tell them in advance what form it will take and when it will arrive.")

# ------------------------------------------------------------------ section 4: 4.2
prov('4.2', F('Each higher education provider has its own method', 'FQHEIS Level 10 degrees.'), 'should',
     'each provider sets its own way of judging achievement above the minimum, referring to Annex D for the honours classes',
     'std:doc:qaa-fheq-2024-framework, Annex D (qaa/fheq-2024/annex-d/summary/lead/1st to 3rd), 4.1 and the Table 1 cells 4.5.b1.threshold to 4.5.b15.excellent',
     'when a team writes marking criteria or class descriptors for the honours degree',
     'How do your marking criteria show the difference between a 2.1 and a first for the outcomes in Table 1?',
     verbs=['refer'], about='using Annex D for degree classes', award=HON, level='fheq:6',
     para="Most students will do much better than the minimum; each provider decides how to evidence that, and should refer to Annex D, which describes the honours classes for degrees at FHEQ Level 6 and FQHEIS Level 10.",
     prac="Use Annex D's class descriptions when setting how achievement above threshold is judged in the honours degree.")

# ------------------------------------------------------------------ section 4: Table 1 (honours) and Table 2 (master's)
# Columns: Benchmark outcome | Threshold standard | Excellent standard. Each row is cut into its cells; row 11 is interleaved
# across a page break by extraction, so its three records share the whole row's span (Part E).
_T1 = _NORM.find('Table 1: On graduating')
_T2 = _NORM.find('Table 2: Benchmark standards')
_pos = [_T1]
def C(a, b):
    s0 = _NORM.find(a, _pos[0]); assert s0 >= 0, a
    e0 = _NORM.find(b, s0); assert e0 >= 0, b
    _pos[0] = s0 + 1
    return _NORM[s0:e0 + len(b)], s0

AD = 'qaa/fheq-2024/annex-d/'
ROWS = [
 # (row, about, domain, fheq, annex row, (O start, O end, O verbs, XO), (T ...), (E ...))
 (1, 'key concepts across the subject', 'knowledge', '4.15.b1', 'knowledge/r2',
  ('Describe and discuss the key concepts', 'from health to disease.', ['describe', 'discuss'], "describe and discuss the main concepts and phenomena of the course accurately, confidently and in depth, in the right technical language, aware of the whole range of the subject from molecules to cells and from health to disease"),
  ('Recall basic knowledge', 'appropriate terminology.', ['recall', 'explain'], "recall the basics of the main concepts and phenomena met on the course and explain them in suitable technical terms"),
  ('Apply a comprehensive knowledge', 'enquiry beyond this.', ['apply', 'discuss', 'explain', 'show'], "apply a wide-ranging grasp of the subject's concepts to discuss and explain the core of the course, and show enquiry that goes past it")),
 (2, 'experimental design and problem solving', 'subject-skill', '4.15.b3.1', 'cognitive/r3',
  ('Apply knowledge and understanding of human biological', 'ethics and sustainability.', ['apply', 'design', 'solve'], "use knowledge of human biological systems and methods to plan experiments and solve problems in theory and practice, alert to controls, bias, ethics and sustainability"),
  ('Demonstrate an understanding of basic experimental', 'ethics and sustainability.', ['demonstrate', 'solve'], "show an understanding of basic experimental design and use methods on routine course problems, with some alertness to controls, bias, ethics and sustainability"),
  ('Devise and evaluate solutions', 'ethics and sustainability.', ['devise', 'evaluate', 'solve'], "devise and evaluate solutions to routine and unfamiliar problems by a range of methods, alert to controls, bias, ethics and sustainability")),
 (3, 'safe working and risk assessment', 'subject-skill', '4.15.b2', 'practical/r2',
  ('Describe, document and enact', 'practical activities.', ['describe', 'document', 'enact'], "describe, record and practise safe working, managing biological, chemical, laboratory and sample risks through risk assessment and practical work"),
  ('Produce and follow risk', 'with support.', ['produce', 'follow'], "write and follow risk assessments so that practical work is done safely and reliably, with support"),
  ('Independently produce and apply', 'reliable manner.', ['produce', 'apply'], "write and apply risk assessments independently so that practical work is done safely and reliably")),
 (4, 'practical laboratory techniques', 'subject-skill', '4.15.b2', 'practical/r1',
  ('Select and carry out appropriate', 'limitations of various techniques.', ['select', 'carry'], "choose and use suitable quantitative and qualitative practical techniques on course problems, weighing the theory behind each and its limits"),
  ('Suggest and demonstrate competence', 'relevant to the course.', ['suggest', 'demonstrate'], "propose, and show competence in, a broad range of suitable practical techniques, qualitative and quantitative, for the course"),
  ('Design, optimise and demonstrate', 'autonomy and efficiency.', ['design', 'optimise', 'demonstrate'], "design, refine and show competence in a broad range of suitable practical techniques, working with much autonomy and efficiency")),
 (5, 'databases and computational tools', 'subject-skill', '4.15.b2', 'practical/r1',
  ('Use appropriate databases', 'Sciences processes.', ['use'], "use suitable databases and computational techniques and tools to deepen understanding of biomedical processes"),
  ('Apply computational techniques and tools to investigate familiar', 'appropriate terminology.', ['apply', 'investigate', 'report'], "use computational techniques and tools to investigate familiar course concepts and report the results in suitable terms"),
  ('Select and apply appropriate computational', 'appropriate terminology.', ['select', 'apply', 'investigate', 'evaluate', 'report'], "choose and use suitable computational techniques and tools to investigate complex concepts, then evaluate and report the results in suitable terms")),
 (6, 'engaging with the literature', 'generic-skill', '4.15.b5', 'cognitive/r1',
  ('Engage with literature', 'insight into the subject.', ['engage', 'develop'], "read the literature of the subject to gain insight into it"),
  ('Assess the evidence base', 'interpretation therein.', ['assess', 'accessing', 'commenting'], "judge the evidence behind scientific claims by going to primary literature and commenting on how adequate its methods, data and interpretation are"),
  ('Identify and select appropriate sources', 'high degree of independence.', ['identify', 'select', 'appraise', 'evaluate'], "find and choose suitable sources of biological information, primary literature among them, and judge the adequacy of their methods, data and interpretation with much independence")),
 (7, 'an independent investigative project', 'subject-skill', '4.15.b6', 'transferable/r3',
  ('Complete independent open-ended', 'relevant to the course.', ['complete'], "complete open-ended investigative work independently through a project or research assignment"),
  ('Demonstrate planning, execution', 'problem solving and independence.', ['demonstrate', 'demonstrating'], "plan, carry out and present a piece of independent work that analyses or evaluates data within a supported framework, showing some time management, problem solving and independence"),
  ('Demonstrate highly independent', 'problem solving and independence.', ['demonstrate', 'demonstrating'], "plan, carry out and present a piece of independent work with marked independence and competence, analysing and critically evaluating data and showing strong time management, problem solving and independence")),
 (8, "the subject's contribution to world challenges", 'understanding', '4.15.b7', 'cognitive/r2',
  ('Appreciate the contribution', 'current and future challenges.', ['appreciate', 'develop'], "value what the subject brings to the innovations of the modern world and what its graduates can offer to present and future challenges"),
  ('Identify and discuss application', 'research scientists in this.', ['identify', 'discuss', 'demonstrate'], "identify and discuss how the subject is applied to present and future world challenges, with some understanding of the part biomedical and research scientists play"),
  ('Explain, suggest and critique', 'future world challenges.', ['explain', 'suggest', 'critique'], "explain, propose and critique ways in which the subject and its scientists can help solve present and future world challenges")),
 (9, 'links with other subjects', 'understanding', '4.15.b1', 'knowledge/r2',
  ('Recognise the relationships and interfaces', 'multidisciplinary environment.', ['recognise', 'enabling'], "recognise how the subject relates to and meets other subjects, so as to work well in a multidisciplinary setting"),
  ('Identify and explain relationships', 'relevant to the course content.', ['identify', 'explain'], "identify and explain how the subject relates to other subjects relevant to the course"),
  ('Explain and evaluate the contribution', 'solving scientific problems.', ['explain', 'evaluate'], "explain and evaluate what the subject contributes to interdisciplinary challenges and how interdisciplinary thinking helps solve scientific problems")),
 (10, 'mathematics and statistics', 'generic-skill', '4.15.b2', 'transferable/r1',
  ('Deploy mathematical and statistical', 'evaluate data.', ['deploy', 'solve', 'evaluate'], "use mathematical and statistical ideas, processes and tools, such as rearranging equations, graphs and statistical tests, for problem solving or data evaluation"),
  ('Use mathematical and statistical concepts', 'evaluate data.', ['use', 'solve', 'evaluate'], "use mathematical and statistical tools on familiar problems or to evaluate data"),
  ('Select, use and evaluate appropriate mathematical', 'evaluate data.', ['select', 'use', 'evaluate'], "choose, use and evaluate suitable mathematical and statistical tools for problem solving or data evaluation")),
 (11, 'collecting and analysing data', 'subject-skill', '4.15.b7', 'practical/r4',
  ('Collect qualitative and quantitative data', 'within the field.', ['collect', 'analyse', 'interpret'], "gather qualitative and quantitative data from course investigations, then analyse and interpret them to test hypotheses, set findings in context, present them and propose further lines of enquiry"),
  None,
  None),
 (12, 'teamwork', 'generic-skill', '4.15.b9.1', 'transferable/r2',
  ('Collaborate and work successf ully', 'team outputs.', ['collaborate', 'work', 'contributing'], "work well with others in a group, contributing positively and flexibly to what the team produces"),
  ('Effectively participate', 'contributions to the work.', ['participate', 'demonstrating'], "take an effective part in group and team work, with clear contributions"),
  ('Identify and apply effective strategies', 'leadership skills.', ['identify', 'apply', 'provide', 'demonstrating'], "find and use effective strategies for group work and make clear, valuable contributions to team outputs, showing good teamwork or leadership")),
 (13, 'communication', 'generic-skill', '4.15.b8', 'transferable/r1',
  ('Communicate effectively, selecting', 'audience, purpose and subject.', ['communicate', 'selecting'], "communicate well, choosing content, media and methods to suit audience, purpose and subject"),
  ('Communicate information, ideas, problems and solutions verbally and/or', 'clear expression and style.', ['communicate'], "convey information, ideas, problems and solutions in speech or other forms, expressed clearly"),
  ('Communicate information, ideas, problems and solutions to an accomplished', 'appropriate for the audience.', ['communicate'], "convey information, ideas, problems and solutions to a high standard in speech and other forms, accurately, fluently and with sophistication, always pitched to the audience")),
 (14, 'ethics, history and societal impact', 'understanding', '4.15.b4', 'professional/r2',
  ('Apply ethical awareness', 'advances in the Biomedical Science and/or Biomedical Sciences.', ['apply', 'appreciate'], "bring ethical awareness to work in the subject and appreciate its history and the effects its advances have on society"),
  ('Describe some of the ethical issues', 'historical context of the subject.', ['describe'], "describe some ethical issues and social effects of advances in the subject, with some acknowledgement of its history"),
  ('Understand and evaluate ethical issues', 'historical context of the subject.', ['understand', 'evaluate'], "understand and evaluate the ethical issues and social effects of advances in the subject, with some understanding of its history")),
 (15, 'keeping up with advances', 'generic-skill', '4.15.b9.3', 'transferable/r3',
  ('Stay up to date', 'new findings emerge.', ['stay', 'appreciate'], "keep up with advances in the subject and appreciate that knowledge shifts as new findings appear"),
  ('Awareness of how new findings', 'up to date with new findings.', ['change', 'demonstrate'], "show awareness that new findings may change how topics are understood and that much in the subject is not yet understood, with some ability to keep up to date"),
  ('Clear appreciation of the fluid', 'understanding of various topics.', ['incorporate'], "show a clear grasp that knowledge in the subject is fluid, with the ability to fold new findings into earlier understanding")),
 (16, 'professional conduct', 'generic-skill', '4.15.b9.1', 'professional/r1',
  ('Act professionally', 'and Biomedical Scientists.', ['act', 'modelling', 'promotes'], "act professionally, mindful of legal, ethical and social responsibilities, and model good practice that gives a positive view of the subject and its scientists"),
  None, None),
]
R11T = (['demonstrate'], "collect data accurately, choosing suitable analysis, interpreting findings to test hypotheses, considering further enquiry and handling data to present them well")
R11E = (['demonstrate'], "collect data accurately and independently, with the same choices of analysis, interpretation, further enquiry and presentation, and a thorough sense of where the investigation sits in the field")

GRADE = {}
OUTCOMES = []
def adid(row, band):
    return AD + row + ('/3rd-1st' if row.startswith('professional') else '/' + band)

for (r, about, dom, fheq, adrow, O, T, E_) in ROWS:
    i = '4.5.b%d' % r
    fq = 'qaa/fheq-2024/' + fheq
    otext, ooff = C(O[0], O[1])
    base = dict(level='fheq:6', addressee='learner', about=about, domain=dom, award=HON)
    nb = (f"its threshold and excellent cells {i}.threshold and {i}.excellent" if T or r == 11 else "1.4 and 2.9 in this document")
    P[i] = dict(find=otext, after=ooff, type='outcome', rung='none', force='threshold', verbs=O[2],
                appliesTo='honours graduates in Biomedical Science or Biomedical Sciences', **base,
                para=f"On graduating with honours, graduates will {O[3]}.",
                prac=f"Every honours graduate in either degree will {O[3]}. Teach and assess this across the course" + (", grading it by the threshold and excellent cells beside it." if T or r == 11 else "."),
                ben=f"By the time you graduate with honours, you will {O[3]}.",
                aaw=(f"Treat this as a benchmark outcome every honours graduate in Biomedical Science or Biomedical Sciences will have (FHEQ level 6; FQHEIS level 10 in Scotland): {about}. "
                     f"Cite it as {CITE}, Table 1, row {r}, benchmark outcome column. Do not present it as a regulatory requirement or as a master's outcome. "
                     f"Set it beside {nb}, the FHEQ honours descriptor {fq} and spine:6."),
                aad=(f"Raise this when a student asks what an honours graduate should be able to do about {about}, or when a team maps its modules to the table. "
                     f"To a student, put it plainly as what you will be able to do by the end; to staff, as the outcome the course has to build. "
                     f"Ask: 'Where in your course have you practised {about}, and what did you produce?' Avoid reading the table aloud."))
    if r == 11:
        T = ('', '', R11T[0], R11T[1]); E_ = ('', '', R11E[0], R11E[1])
        ttext, toff, etext, eoff = otext, ooff, otext, ooff
    elif T:
        ttext, toff = C(T[0], T[1]); etext, eoff = C(E_[0], E_[1])
    if not T:
        continue
    P[i + '.threshold'] = dict(find=ttext, after=toff, type='threshold', rung='threshold', force='threshold', verbs=T[2],
                appliesTo='honours graduates, at the threshold standard', **base,
                para=f"At threshold, honours graduates will {T[3]}.",
                prac=f"This is the floor: every honours graduate will at least {T[3]}. Teaching and assessment need to secure it for all.",
                ben=f"To reach the minimum standard, you will {T[3]}.",
                aaw=(f"Treat this as the threshold standard, the minimum every honours graduate will have shown for {about} (FHEQ level 6; FQHEIS level 10 in Scotland). "
                     f"Cite it as {CITE}, Table 1, row {r}, threshold standard. Do not present it as a regulatory requirement, a mark scheme or a master's standard. "
                     f"Set it beside the benchmark outcome {i} and the excellent cell {i}.excellent in this document, the FHEQ honours descriptor {fq} and the Annex D third-class description {adid(adrow, '3rd')}."),
                aad=(f"Raise this when a student asks what they must show about {about} to pass, or when a team checks that every graduate meets the minimum. "
                     f"To a student, say plainly what the floor is; to staff, frame it as the standard the course has to secure for everyone. "
                     f"Ask: 'Could you show me a piece of your work where you did this, and how much support you had?' Do not present the excellent cell as the minimum or read the table aloud."))
    P[i + '.excellent'] = dict(find=etext, after=eoff, type='excellent', rung='excellent', force='describes', verbs=E_[2],
                appliesTo='honours graduates, at the excellent standard', **base,
                para=f"At an excellent level, graduates {E_[3]}.",
                prac=f"Use this to recognise excellent work: graduates who {E_[3]} are at the top of the range. Design tasks that give the strongest students room to show it.",
                ben=f"At an excellent level, you {E_[3]}.",
                aaw=(f"Treat this as the excellent standard, which describes achievement well above the minimum rather than requiring it: {about}, for honours graduates (FHEQ level 6; FQHEIS level 10 in Scotland). "
                     f"Cite it as {CITE}, Table 1, row {r}, excellent standard. Do not present it as expected of every graduate, as regulation or as master's work. "
                     f"Set it beside {i}.threshold and {i} in this document, the FHEQ honours descriptor {fq} and, as an inferred reading only, the Annex D first-class description {adid(adrow, '1st')}."),
                aad=(f"Raise this with a student aiming for the top of the range in {about}, or with a team designing stretch tasks. "
                     f"To a student, describe what excellent work looks like here; to staff, frame it as what the strongest work shows. "
                     f"Ask: 'What would your next piece of work on this need to show more independence or depth?' Avoid implying that everyone has to reach this or that falling short means failing."))
    GRADE[i + '.excellent'] = i + '.threshold|stated'
    OUTCOMES.append(dict(outcome=about, threshold=i + '.threshold', typical='none', excellent=i + '.excellent', basis='stated', domain=dom, award=HON))

# Table 2: master's, in addition to Table 1 (lead-in: graduates should be able to)
_pos[0] = _T2
t17, o17 = C('Develop, integrate, synthesise', 'complex problems.')
t17t, o17t = C('With significant support and guidance.', '.')
t17e, o17e = C('With a high degree of independence and autonomy.', '.')
t18, o18 = C('Interrogate and integrate diverse', 'significant research project.')
MB = dict(level='fheq:7', addressee='learner', award=MAS)
P['4.5.b17'] = dict(find=t17, after=o17, type='outcome', rung='none', force='should', verbs=['develop', 'integrate', 'synthesise', 'apply', 'solve'],
    appliesTo="master's graduates in Biomedical Science or Biomedical Sciences", about='applying leading-edge understanding to complex problems', domain='understanding', **MB,
    para="In addition to the honours outcomes, master's graduates should be able to develop, combine, synthesise and apply a systematic, broad understanding of current and leading-edge biomedical concepts to solve complex problems.",
    prac="At master's level, students should be able to bring a systematic, broad and current understanding of biomedical concepts to bear on complex problems, on top of the honours outcomes.",
    ben="On a master's course you should become able to pull together a broad, systematic understanding of current and cutting-edge biomedical ideas and use it to solve complex problems.",
    aaw=(f"Treat this as a should-level outcome for master's graduates, added to the honours outcomes of Table 1 (FHEQ level 7; FQHEIS level 11 in Scotland). Cite it as {CITE}, Table 2, row 1. "
         f"Do not claim it holds at honours level or that it is regulation. Set it beside 4.5.b17.threshold and 4.5.b17.excellent, 3.23, the FHEQ master's descriptors qaa/fheq-2024/4.17.b1 and qaa/fheq-2024/4.17.b5, and spine:7."),
    aad=("Raise this when a master's student asks how the step up from honours shows, or when a team writes level 7 outcomes. To a student, put it as using leading-edge understanding on problems with no ready answer; to staff, as the master's addition to the honours outcomes. "
         "Ask: 'Which complex problem in your project needed ideas from more than one area, and how did you combine them?' Avoid reading the table aloud."))
P['4.5.b17.threshold'] = dict(find=t17t, after=o17t, type='threshold', rung='threshold', force='threshold', verbs=[],
    appliesTo="master's graduates, at the threshold standard", about='leading-edge understanding, with support', domain='understanding', **MB,
    para="At threshold, the master's graduate does this with considerable support and guidance.",
    prac="The master's minimum: students meet the first Table 2 outcome while still relying on substantial support and guidance.",
    ben="To reach the minimum on a master's course, you can do this with a good deal of support and guidance.",
    aaw=(f"Treat this as the master's threshold for the first Table 2 outcome: it is met with considerable support and guidance (FHEQ level 7; FQHEIS level 11). Cite it as {CITE}, Table 2, row 1, threshold standard. "
         f"Do not apply it at honours level or treat it as a mark scheme; Part E notes the cell may span every Table 2 row. Set it beside 4.5.b17 and 4.5.b17.excellent, and qaa/fheq-2024/4.17.b6."),
    aad=("Raise this when a master's student worries about how much help they are getting, or when a team sets its pass descriptors. To a student, explain that needing guidance is acceptable at the minimum; to staff, frame it as the support the floor allows. "
         "Ask: 'Which decisions in your project did you take yourself, and which with your supervisor?' Do not present the excellent cell as the minimum."))
P['4.5.b17.excellent'] = dict(find=t17e, after=o17e, type='excellent', rung='excellent', force='describes', verbs=[],
    appliesTo="master's graduates, at the excellent standard", about='leading-edge understanding, independently', domain='understanding', **MB,
    para="At an excellent level, the master's graduate does this with much independence and autonomy.",
    prac="Excellent master's work meets the first Table 2 outcome with a high degree of independence and autonomy.",
    ben="At an excellent level on a master's course, you do this largely on your own, directing the work yourself.",
    aaw=(f"Treat this as the master's excellent standard for the first Table 2 outcome, which describes rather than requires: it is met with much independence and autonomy (FHEQ level 7; FQHEIS level 11). Cite it as {CITE}, Table 2, row 1, excellent standard. "
         f"Do not present it as expected of every master's graduate; Part E notes the cell may span every Table 2 row. Set it beside 4.5.b17.threshold, 4.5.b17 and qaa/fheq-2024/4.17.b6."),
    aad=("Raise this with a master's student aiming high or a team designing distinction descriptors. To a student, describe excellent work as directing your own enquiry; to staff, as autonomy shown in the work. "
         "Ask: 'Where did you change the direction of your project on your own judgement?' Avoid implying that every student must reach it."))
GRADE['4.5.b17.excellent'] = '4.5.b17.threshold|stated'
OUTCOMES.append(dict(outcome='applying leading-edge understanding to complex problems', threshold='4.5.b17.threshold', typical='none', excellent='4.5.b17.excellent', basis='stated', domain='understanding', award=MAS))
P['4.5.b18'] = dict(find=t18, after=o18, type='outcome', rung='none', force='should', verbs=['interrogate', 'integrate', 'design', 'develop'],
    appliesTo="master's graduates in Biomedical Science or Biomedical Sciences", about='research from the literature to a significant project', domain='subject-skill', **MB,
    para="Master's graduates should be able to interrogate and combine varied scientific literature and other information to design and develop methods of investigation and analysis, at the forefront and beyond their own specialism; this takes in planning a project (ethics, hazards, environmental effects, sustainability and costs, as fits), building advanced experimental and investigative skills, and discussing the background, context, methods, results and likely impact of a substantial research project.",
    prac="At master's level, students should be able to design investigations from a critical synthesis of the literature, plan a project with its ethics, hazards, environmental and cost aspects, develop advanced experimental skills and discuss a substantial research project in full.",
    ben="On a master's course you should become able to draw on a wide range of scientific literature to design your own methods, plan a substantial research project with its ethical, safety, environmental and cost aspects, build advanced laboratory and investigative skills, and discuss your project's background, methods, results and impact.",
    aaw=(f"Treat this as a should-level outcome for master's graduates, added to Table 1 (FHEQ level 7; FQHEIS level 11 in Scotland): research from the literature through to a significant project. Cite it as {CITE}, Table 2, rows 2 to 5. "
         f"Do not claim it holds at honours level, and note that the statement grades it only through the support or independence cells of row 1 (Part E). Set it beside 4.5.b17, 3.23, 4.5.b7, the FHEQ master's descriptors qaa/fheq-2024/4.17.b2 and qaa/fheq-2024/4.17.b4.2, and spine:7."),
    aad=("Raise this when a master's student is planning their research project, or when a team designs the project module. To a student, put it as owning the whole arc of a research project, from reading to discussing impact; to staff, as the master's research outcome. "
         "Ask: 'What did the literature leave open that your methods are designed to answer, and what are the costs and risks?' Avoid reading the table aloud."))

# ------------------------------------------------------------------ themes, levels, relations
TH = {'1.16': 'theme:edi', '1.17': 'theme:edi', '1.18': 'theme:edi', '1.19': 'theme:edi',
      '1.20': 'theme:accessibility', '1.21': 'theme:accessibility', '1.22': 'theme:accessibility',
      '1.25': 'theme:esd', '1.30': 'theme:enterprise'}

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.3; 4.2 ("FHEQ Level 6" for the bachelor\'s degree with honours)'),
                  dict(id='fqheis:10', role='cites', locator='D1, 2.3; 4.2 ("FQHEIS Level 10")'),
                  dict(id='fheq:7', role='cites', locator='D1, 2.3 ("FHEQ Level 7" for the integrated master\'s degree with honours); Table 2 (master\'s)'),
                  dict(id='fqheis:11', role='cites', locator='D1, 2.3 ("FQHEIS Level 11")')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent',
                           basis='stated (D1, 2.3: "FHEQ Level 6; FQHEIS Level 10"; 4.2); matches std:doc:qaa-fheq-2024-framework Table 1'),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent',
                           basis='stated (D1, 2.3: "FHEQ Level 7; FQHEIS Level 11"); matches std:doc:qaa-fheq-2024-framework 4.17 (one descriptor shared) and Table 1'),
                      dict(**{'from': 'fheq:6'}, to='spine:6', relation='equivalent', basis='inferred from std:ref:uk-framework R2'),
                      dict(**{'from': 'fheq:7'}, to='spine:7', relation='equivalent', basis='inferred from std:ref:uk-framework R2')])

EDI_P = ['1.16', '1.17', '1.18', '1.19', '1.20', '1.21', '1.22', '2.7', '2.10', '2.17', '2.22', '3.16', '3.19', '3.20']
ACC_P = ['1.19', '1.20', '1.21', '1.22', '2.7', '2.8', '2.17', '2.27', '3.16', '3.19', '3.20']
ESD_P = ['1.23', '1.24', '1.25', '1.29', '2.22', '3.12', '4.5']
ENT_P = ['1.26', '1.27', '1.28', '1.29', '1.30', '1.31', '2.17', '3.12', '3.14', '3.19']
S6 = [dict(id='theme:edi', role='carries', carriedIn=EDI_P), dict(id='theme:accessibility', role='carries', carriedIn=ACC_P),
      dict(id='theme:esd', role='carries', carriedIn=ESD_P), dict(id='theme:enterprise', role='carries', carriedIn=ENT_P)]

S7 = [
    dict(rel='supersedes', target='std:doc:qaa-biomedical-sciences-2019-benchmarks (not yet ingested)', note='the fourth edition (2019), named in the back matter; key changes listed in the front matter'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the honours classification descriptions (4.2); FHEQ and FQHEIS levels for the awards (2.3)'),
    dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS Levels 10 and 11 (2.3, 4.2)'),
    dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='Education for Sustainable Development Guidance (1.25)'),
    dict(rel='refersTo', target='std:doc:qaa-enterprise-2018-guidance', note='Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (1.31)'),
    dict(rel='refersTo', target='QAA Characteristics Statement: Higher Education in Apprenticeships (not yet ingested)', note='2.6'),
    dict(rel='refersTo', target='HCPC Standards of Proficiency for Biomedical Scientists (not yet ingested)', note='1.14, 1.15, 4.4; the source of Appendix 1'),
    dict(rel='refersTo', target='IBMS accreditation criteria and Registration Training Portfolio (not yet ingested)', note='1.2, 1.15, 2.4, 3.2, 3.4'),
    dict(rel='refersTo', target='Association for Nutrition competency requirements for course accreditation (not yet ingested)', note='3.7'),
    dict(rel='refersTo', target='UNESCO (2019), Education for Sustainable Development', note='the ESD definition quoted (1.24)'),
    dict(rel='refersTo', target='United Nations, Sustainable Development Goals', note='1.24'),
    dict(rel='refersTo', target='QAA Quality Code for Higher Education, Advice and Guidance (not yet ingested)', note='front matter; references'),
    dict(rel='refersTo', target='QAA Glossary (not ingested)', note='front matter'),
    dict(rel='refersTo', target='HEA (2016) Framework for embedding employability in higher education (not yet ingested)', note='list of references only'),
]

SB1 = [
    'Two related degrees told apart: Biomedical Science (singular), built to the professional body\'s accreditation requirements and covering every clinical laboratory specialism, and Biomedical Sciences (plural), broader and reaching into other human biology, including named awards such as pharmacology, molecular or cell biology (D1, front matter; 1.1 to 1.3).',
    'Its object is the scientific basis of human health and disease, from molecules and cells to whole systems (D1, 1.4; 3.12; Table 1).',
    'The singular degree is the academic step towards registration as a Biomedical Scientist, a protected title; with verified clinical training, it leads to work in NHS and private diagnostic pathology laboratories (D1, 1.2; 1.6; 1.8; 1.12 to 1.15).',
    'Hands-on laboratory work is essential, giving technical skill and safe, accurate practice in clinical, industrial and research laboratories (D1, 1.10; 2.14).',
    'Research skills, critical appraisal and independent investigation run through the courses and prepare for employment or research degrees (D1, 1.11; Table 1).',
    'Related courses in the area, Pharmacology, Human Nutrition and Physiology, share a common core and have their own content and accrediting bodies (D1, 2.5; 2.28; 3.5 to 3.11).',
    'A systems-led approach integrates the clinical specialisms with the underlying science of investigation and treatment (D1, 3.3; 3.10).',
]
SB2 = [
    dict(theme='theme:edi', inThisSubject='inclusion throughout the course; confronting the field\'s history of injustice and the biases in what science is done and how data are read; diverse contributors and case studies; global inequality in access to diagnosis and treatment; misuse of discoveries for unequal ends (D1, 1.16 to 1.19; 2.10; 2.22; 3.20)',
         statements=['1.16', '1.17', '1.18', '1.19', '2.10.b2', '3.20.b3', '4.5.b14', '4.5.b14.threshold', '4.5.b14.excellent']),
    dict(theme='theme:accessibility', inThisSubject='fully accessible curricula, assessment and practical work, anticipating needs in laboratories, fieldwork and placements, with inclusive design and reasonable adjustments, and placements funded so all can take part (D1, 1.20 to 1.22; 2.7; 2.8; 2.17; 3.19; 3.20)',
         statements=['1.20', '1.21', '1.22', '2.7', '2.8', '2.17', '3.19', '3.20.b3', '3.20.b4']),
    dict(theme='theme:esd', inThisSubject='sustainable laboratory practice (reducing paper and plastics, safer chemicals, the LEAF initiative), environmental impact and the SDGs, with ethics and sustainability a consideration in experimental design and project planning (D1, 1.23 to 1.25; 2.22; Table 1 row 2; Table 2)',
         statements=['1.25', '4.5.b2', '4.5.b2.threshold', '4.5.b2.excellent', '4.5.b18']),
    dict(theme='theme:enterprise', inThisSubject='employability and entrepreneurship as competencies, employer links, placements, intellectual property and commercialisation, and taking charge of one\'s own professional development (D1, 1.26 to 1.31; 2.17; 3.12; 3.14)',
         statements=['1.30', '2.17', '3.14.b7', '3.19', '4.5.b8', '4.5.b8.threshold', '4.5.b8.excellent']),
]
SB3 = dict(
    areas=[dict(component='3.1', gloss='content common to all the courses: anatomy and physiology, cell biology, biochemistry, microbiology, immunology, developmental biology, supporting physics and chemistry, genetics and genomics, molecular biology, pathology of disease, bioinformatics, pharmacology'),
           dict(component='3.4', gloss='the clinical pathology areas of the accredited degree: cellular pathology, clinical biochemistry, clinical immunology, haematology, transfusion science, clinical genetics, medical microbiology, near-patient testing, laboratory quality'),
           dict(component='3.5', gloss='other specialisms in the area; pharmacology defined'),
           dict(component='3.6', gloss='Pharmacology: pharmacodynamics, pharmacokinetics, individual variation, pharmacological methods'),
           dict(component='3.7', gloss='Human Nutrition: nutritional science and its application to health'),
           dict(component='3.9', gloss='Human Nutrition outcomes: metabolism, clinical biochemistry, nutritional assessment, food science, clinical nutrition'),
           dict(component='3.10', gloss='Physiology as an integrative science'),
           dict(component='3.11', gloss='Physiology outcomes, system by system, with experimentation and data'),
           dict(component='3.12', gloss='approaches to study common to all the courses')],
    practices=[dict(component='3.15', kind='teaching', gloss='scaffolded teaching moving towards independent study; integration across the programme'),
               dict(component='3.16', kind='teaching', gloss='student-centred, accessible strategies; synchronous, asynchronous and blended delivery; staff development'),
               dict(component='3.17', kind='learning', gloss='synchronous activities: lectures, laboratory classes, problem-based learning, workshops, fieldwork, peer learning'),
               dict(component='3.18', kind='learning', gloss='asynchronous activities: self-study, recordings, virtual experiments, research projects, reflective portfolios, placements'),
               dict(component='3.19', kind='assessment', gloss='progressive, varied and authentic assessment, discriminating threshold from higher achievement'),
               dict(component='3.20', kind='assessment', gloss='principles for designing assessment'),
               dict(component='3.21', kind='assessment', gloss='themes for authentic assessment: practical, collaborative, integrative, communication, professional'),
               dict(component='3.22', kind='assessment', gloss='examination formats and coursework'),
               dict(component='3.23', kind='assessment', gloss='integrated master\'s assessment: unfamiliar problems and the full range of research skills'),
               dict(component='3.24', kind='assessment', gloss='qualities of feedback')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.1; Table 1 lead-in', award=HON, items=15),
           dict(rung='threshold', leadIn='4.5; Table 2 lead-in', award=MAS, items=1),
           dict(rung='typical', leadIn='none', award='none', items=0),
           dict(rung='excellent', leadIn='4.1; Table 1 lead-in', award=HON, items=15),
           dict(rung='excellent', leadIn='4.5; Table 2 lead-in', award=MAS, items=1)],
    rungBases=('Two tables, each with three columns: Benchmark outcome, Threshold standard and Excellent standard. Table 1 (honours) has 16 rows: '
               '15 graded at threshold and excellent, the last (acting professionally) an outcome only. Table 2 (master\'s, "in addition to Table 1") '
               'grades its first outcome only by support (threshold: with significant support and guidance) and independence (excellent: with a high '
               'degree of independence and autonomy). The benchmark outcome column is recorded as rung none, outcome; each threshold and excellent cell '
               'is its own S4 record, paired by row (gradeOf stated). No typical rung; 4.2 points to Annex D for the classes.'),
    outcomeLists=[dict(leadIn='Table 1', gloss='benchmark outcomes for the honours degree (first column)', items=16, award=[HON]),
                  dict(leadIn='Table 2', gloss="master's outcomes in addition to Table 1 (rows 2 to 5 recorded as one)", items=2, award=[MAS]),
                  dict(leadIn='3.4', gloss='clinical pathology knowledge for graduates of the accredited degree, in nine specialisms', items=38, award=[HON]),
                  dict(leadIn='3.6', gloss='core outcomes for Pharmacology graduates', items=11, award=[HON]),
                  dict(leadIn='3.9', gloss='core outcomes for Human Nutrition graduates', items=8, award=[HON]),
                  dict(leadIn='3.11', gloss='core outcomes for Physiology graduates', items=28, award=[HON]),
                  dict(leadIn='3.14', gloss='graduate attributes for all courses (plain present; force describes)', items=8, award=[HON, MAS])],
    outcomes=OUTCOMES)
SB4A_FULL = []
SB5 = [
    dict(body='Institute of Biomedical Science (IBMS)', says='the professional body that accredits Biomedical Science degrees and approves training laboratories, sets the clinical specialisms the degree must cover, runs the Registration Training Portfolio and awards the Certificate of Competence that makes graduates eligible to apply for registration; it also advises Biomedical Sciences graduates on top-up modules (D1, front matter; 1.2; 1.3; 1.6 to 1.8; 1.15; 2.4; 2.11; 2.28; 3.2; 3.4; 4.4)',
         requirements='not yet ingested: IBMS accreditation criteria and Registration Training Portfolio (Part E)'),
    dict(body='Health and Care Professions Council (HCPC)', says='the statutory regulator under the Health Act 1999 that holds the register and protects the title Biomedical Scientist; registration rests on its Standards of Proficiency, which the standards of the accredited degree are linked to; it may also approve degrees with integrated placements directly, and registers dietitians (D1, 1.2; 1.3; 1.6; 1.12 to 1.15; 2.1; 2.4; 2.9; 3.2; 3.4; 3.8; 4.4; Appendix 1)',
         requirements='not yet ingested: HCPC Standards of Proficiency for Biomedical Scientists (Part E)'),
    dict(body='Royal Society of Biology', says='accredits Biomedical Science and Biomedical Sciences programmes and Human Physiology programmes (D1, 2.28)', requirements='not yet ingested (Part E)'),
    dict(body='Association for Nutrition (AfN)', says='accredits Nutrition courses against its competency requirements and holds a voluntary register for nutritionists (D1, 2.28; 3.7; 3.8)', requirements='not yet ingested: AfN competency requirements (Part E)'),
    dict(body='British Pharmacological Society', says='accredits Pharmacology programmes (D1, 2.28)', requirements='not yet ingested (Part E)'),
    dict(body='professional, statutory and regulatory bodies (PSRBs) and professional bodies, in general', says='the statement supports them with academic standards; they may add requirements, accredit other specialisms, help co-create enterprise education, and take part in course enhancement (D1, front matter; 1.29; 2.18; 2.27; 3.5)', requirements='not applicable: no one body'),
]
SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=EDI_P, statements=SB2[0]['statements']),
            dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=ACC_P, statements=SB2[1]['statements']),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=ESD_P, statements=SB2[2]['statements']),
            dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=ENT_P, statements=SB2[3]['statements'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.3', '4.2']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.3', '4.2'])],
    bodies=[dict(body='Institute of Biomedical Science (IBMS)', citedIn=['1.2', '1.3', '1.6', '1.7', '1.8', '1.12', '1.15', '2.1', '2.4', '2.9', '2.11', '2.28', '3.2', '3.4', '4.4']),
            dict(body='Health and Care Professions Council (HCPC)', citedIn=['1.2', '1.3', '1.6', '1.12', '1.13', '1.14', '1.15', '2.1', '2.4', '2.9', '3.2', '3.4', '3.8', '4.4']),
            dict(body='Royal Society of Biology', citedIn=['2.28']),
            dict(body='Association for Nutrition (AfN)', citedIn=['2.28', '3.7', '3.8']),
            dict(body='British Pharmacological Society', citedIn=['2.28']),
            dict(body='professional, statutory and regulatory bodies, unnamed', citedIn=['1.29', '2.18', '2.27', '3.5'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'],
             role='common descriptions of the four honours classes (1st, 2.1, 2.2, 3rd), for judging achievement above the minimum'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='the QAA and Advance HE Education for Sustainable Development Guidance', citedIn=['1.25'],
             role='teaching, key competencies, learning outcomes and assessment for sustainability'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers', citedIn=['1.31'],
             role='more information on enterprise and entrepreneurship education'),
        dict(document='not yet ingested: listed in Part E', named='Characteristics Statement for Higher Education in Apprenticeships', citedIn=['2.6'], role='the general features of degree apprenticeships'),
    ])

B1 = [
    dict(slug='biomedical-scientist', definition='the protected title, given by the regulator, for those who carry out laboratory investigations on tissue and fluid samples to help diagnose and monitor disease, judge how well treatments work and advise on treatment and prevention (D1, 1.13)',
         beneficiaryDefinition='a registered professional who runs laboratory tests on patient samples to help diagnose and monitor disease', scopeNote='protected title; use requires registration (1.14)', category='unknown', practices=['health', 'biomedical science']),
    dict(slug='certificate-of-competence', definition="the professional body's award showing that a person meets the regulator's proficiency standards and is fit to practise, making them eligible to apply for registration (D1, 1.15)",
         beneficiaryDefinition='the certificate you get after verified clinical training that lets you apply for registration', scopeNote='awarded after the Registration Training Portfolio', category='unknown', practices=['health', 'biomedical science']),
    dict(slug='near-patient-testing', definition='analytical testing done for a patient by health professionals outside the usual laboratory (D1, 3.4)',
         beneficiaryDefinition='tests done close to the patient, such as on a ward or in a clinic, rather than in the main laboratory', scopeNote='NPT; also point-of-care testing', category='unknown', practices=['health', 'biomedical science']),
    dict(slug='education-for-sustainable-development', definition='after UNESCO (2019), holistic and transformational education covering content, outcomes, pedagogy and environment; in higher education, curriculum structures and content that support sustainable development (D1, 1.24)',
         beneficiaryDefinition='learning that helps you understand and act on sustainability', scopeNote='ESD; a cross-cutting theme', category='unknown', practices=['education']),
    dict(slug='employability', definition='a set of competencies, combining knowledge, skills and behaviours, that make people more likely to gain work and succeed in it, to their own, society\'s and the economy\'s benefit (D1, 1.26)',
         beneficiaryDefinition='the knowledge, skills and behaviours that help you get work and do well in it', scopeNote='paired with entrepreneurship in 1.26', category='unknown', practices=['education']),
    dict(slug='equity', definition='opening access to study for people with differing needs while removing arbitrary and needless barriers to success (D1, 1.20)',
         beneficiaryDefinition='making sure everyone with the potential to succeed can take part on fair terms', scopeNote='used with accessibility', category='unknown', practices=['education']),
    dict(slug='pharmacology', definition='the science of drugs: their chemical and physical properties, their actions on living tissues and systems and their effects on health and disease (D1, 3.5)',
         beneficiaryDefinition='the study of drugs and how they act on the body', scopeNote='also pharmacodynamics and pharmacokinetics, 3.6', category='unknown', practices=['biomedical science']),
]
B2A = [
    dict(concept='biomedical-scientist', form='Biomedical Scientist', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='certificate-of-competence', form='Certificate of Competence', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='near-patient-testing', form='Near-patient testing (NPT)/point-of-care testing', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='education-for-sustainable-development', form='Education for Sustainable Development (ESD)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='employability', form='Employability', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='equity', form='Equity', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='pharmacology', form='Pharmacology', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
]
B4 = []; B5 = []
D3 = [dict(citation='HCPC, Standards of Proficiency: Biomedical Scientists', settles=['SB5', 'S7', 'Appendix 1'], asked='2026-10-03', state='wanted'),
      dict(citation='IBMS, accreditation criteria for Biomedical Science degrees and the Registration Training Portfolio', settles=['SB5', 'S7'], asked='2026-10-03', state='wanted'),
      dict(citation='QAA (2019) Characteristics Statement: Higher Education in Apprenticeships', settles=['SB6', 'S7'], asked='2026-10-03', state='wanted'),
      dict(citation='QAA (2019) Subject Benchmark Statement: Biomedical Sciences (fourth edition)', settles=['S7'], asked='2026-10-03', state='wanted')]

E = [
    'SB4, rung shape: two three-column tables (Benchmark outcome; Threshold standard; Excellent standard), not separate rung lists as in Psychology. Table 1 (honours, 16 rows): 15 rows graded at threshold and excellent; row 16 (act professionally) has an outcome cell only. Table 2 (master\'s, "in addition to Table 1", lead-in "should be able to"): one outcome graded by support (threshold) and independence (excellent). No typical rung. The tables sit inside the skeleton\'s component 4.5 (after 4.5\'s own sentence); their rows are given ids 4.5.b1 to 4.5.b18, cells <id>.threshold and <id>.excellent.',
    'S4, the benchmark outcome column is recorded as its own record (type outcome, rung none), because its text differs from both graded cells. Its force is the table lead-in\'s "will have"; recorded as threshold (from 4.1, "minimum threshold standards that a student will have demonstrated"), since the builder\'s force check reads only 600 characters before a span and the lead-in is out of reach for most rows. For P3: whether the column should carry will.',
    'S4, force: threshold cells take threshold from 4.1; excellent cells take describes (4.1: the standards "indicate excellent levels of achievement"), as in Anthropology (run 0084). Table 2 rows take should from the lead-in; its threshold and excellent cells as Table 1\'s.',
    'S4, gradeOf: 16 links, each excellent cell to the threshold cell in the same row, basis stated (the issuer pairs them by row); the builder\'s S4 line reads them from GRADE with |stated.',
    'Text fault: Table 1 row 11 (data collection) is interleaved across a page break by extraction (outcome, threshold and excellent cells each split in two). Its three records share the whole row\'s span, so each `source` holds all three cells. For P3 or a re-extraction.',
    'Table 2 layout lost in extraction: after row 1 come "Interrogate and integrate ...", then three verbless noun phrases (project planning; development of advanced experimental and investigative skills; discussion of a significant research project). Read as one research outcome and recorded as one record, 4.5.b18. The threshold and excellent cells ("With significant support and guidance"; "With a high degree of independence and autonomy") are placed on row 1 only; they may be merged cells spanning every Table 2 row. For P3.',
    'Table 2 award: the lead-in says "master\'s degree"; 2.3 says integrated master\'s for Biomedical Sciences only (FHEQ 7, FQHEIS 11) and names standalone MSc and MRes courses; 3.23 speaks of integrated master\'s. Award recorded as master\'s; which master\'s awards Table 2 serves is for P3.',
    'Appendix 1 (draft threshold suggestions drawn from the HCPC Standards of Proficiency through the IBMS portfolio, 28 items under "Registered biomedical scientists must") is excluded as the body\'s requirements and a draft, though 4.4 says the standards for the accredited degree "are detailed in Appendix 1". Its items cite HCPC SoP numbers. For P3: ingest as a separate standards document from the HCPC SoP (D3).',
    'Outcome lists outside section 4 (new against Psychology): 3.4 (nine clinical pathology specialisms, 38 items under "A Biomedical Science graduate will have knowledge of"), 3.6 Pharmacology (11), 3.9 Human Nutrition (8), 3.11 Physiology (28), all "will have". Group headings that end in a colon (3.4.b1, b6, b11, b15, b21, b28, b33, b38, b42, each a definition plus lead-in; 3.6.b1, b8; 3.9.b1; 3.11.b1, b6, b14, b17, b22, b25, b30, b34) are not recorded as statements: they are stems for the items beneath. 3.6.b6 and b7 and 3.9.b9 have no sub-items and are recorded.',
    '3.14 (graduate attributes, 8 items) has a plain-present lead-in ("These acquired attributes include"); recorded as outcome items with force describes, since they state what graduates acquire (3.13, "will recognise", is recorded on its own). For P3 with open point 5.',
    'Skeleton corrections: rung counts (excellent 7 for the 1.9 list) wrong: 1.9 is a list of career paths, not a rung list or a statement; the tables were not cut at all (all inside 4.5); 3.4 stem span runs to the end of the clinical lists; component spans for 1.12, 1.15, 1.19, 1.22, 1.25, 2.8, 2.12, 2.15, 2.19, 3.1, 3.5, 3.6, 3.9, 3.11, 3.14, 3.18 carry the next sub-heading at their end. Paragraph statements are cut by `find` to the obliging or outcome sentences.',
    'Plain-present or descriptive paragraphs not recorded (open point 5): 1.3 (top-up route; "will advise" of the body), 1.5 to 1.11, 1.13, 1.23, 1.24, 1.26 to 1.29, 1.31, 2.2, 2.3, 2.5, 2.12 ("will usually be offered"), 2.13, 2.18, 2.20, 2.22 ("A review ensures"), 2.25, 2.26, 2.28 ("will hold accreditation"), 3.1 (content "generally includes"), 3.5, 3.7, 3.10, 3.12 (approaches "likely to be common"), 3.15, 3.17, 3.18, 3.21 to 3.23, 4.1, 4.3 to 4.5 (4.5\'s own sentence).',
    'Statutory duties on practitioners, not course or student standards, recorded in SB5 not S4: 1.14 ("required by statute to register"), 3.8 (dietitians "must undertake statutory registration").',
    'Obliging words beyond the five: 1.16 "expects" (force describes); 2.15 "need to" (recorded with the paragraph\'s should); 2.16 "are expected to" (recorded with its should); 3.4 "are required" (recorded as must); 3.2 "are required" with "must"; 3.10 and 3.5 "are encouraged" and 3.3 "are encouraged" (not force); 3.16 "there is an expectation that ... should"; 3.23 "requiring", "considered crucial" (not recorded); 2.11 "require" (institutional regulations; recorded with the paragraph\'s will).',
    '2.9 mixes a provider should (course design) with learner wills (progression to graduate competence): one record, addressee both, force should. 2.19 is addressed to students ("should expect") and to courses: addressee both.',
    'Levels: honours and integrated master\'s levels are stated in 2.3 (FHEQ 6, FQHEIS 10; FHEQ 7, FQHEIS 11) and checked against std:doc:qaa-fheq-2024-framework (Table 1; 4.17 shared with FQHEIS 11). Outcome-list items and attributes take fheq:6 from the honours award (3.4\'s "honours" route; inferred for 3.6 to 3.14). No CQFW name appears (the front matter names the Quality Assessment Framework for Wales, not the CQFW).',
    'Subject codes: the statement states none; all six (CAH02-05-03; HECoS 100265, 100260, 100250, 100247, 100262) are basis inferred. Biomedical Science and Biomedical Sciences both map to 100265 (its non-preferred term is biomedical science); Healthcare Science (100260) as the alternative title in 2.6, 3.2 and 3.4. For P3.',
    'The agent instructions read threshold cells against the Annex D third-class description and excellent cells against the first-class description, by the Annex D row nearest in content; this pairing is ours and inferred: the statement maps no cell to a class. Professional rows have one Annex D cell (3rd-1st).',
    'Bodies named in content but not as PSRBs: UKAS and ISO standards (3.4.b47, laboratory accreditation); NHS, Blood Transfusion Services and Public Health Wales (1.8) as employers. The advisory group lists further bodies only in the excluded back matter; not recorded as cited.',
    'Shared documents not yet ingested: Characteristics Statement for Higher Education in Apprenticeships (2.6); the 2019 fourth edition (supersedes); the Quality Code Advice and Guidance and QAA Glossary (front matter); the HEA employability framework (references only).',
    'Text faults noted, not acted on: extraction splits words ("successf ully", "saf e", "staf f", "f acts"); "an honour\'s degree" in the Table 1 lead-in and 2.2; "fungi protozoa" (3.4, medical microbiology); "agonism, antagonism specificity" (3.6.b3).',
    'S9 commentary not researched in P1.',
]
