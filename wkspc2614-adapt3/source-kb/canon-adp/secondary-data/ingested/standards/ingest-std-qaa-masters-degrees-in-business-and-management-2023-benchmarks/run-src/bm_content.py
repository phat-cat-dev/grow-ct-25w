# Judgement file for run 0119, QAA Master's Degrees in Business and Management (March 2023), std.
# Built by tools/bm_build.py under the benchmark template 0.6.0-draft, run layer 0.7.0-draft and BM-BRIEF 0.2.3.
MA = "master's"
L7 = 'fheq:7'

META = dict(
    run='0119', p1='2026-10-03 18:01',
    title="Subject Benchmark Statement Master's Degrees in Business and Management",
    heading="Subject Benchmark Statement: Master's Degrees in Business and Management (QAA, March 2023)",
    edition='March 2023 (fourth edition)', published='2023-03',
    status='current',
    supersedes="the previous Subject Benchmark Statement for this subject (D1, front matter: 'Key changes from the previous'); its edition is not named in the text (the membership lists name review groups of 2015, 2007 and 2000)",
    subjects=[
        dict(scheme='hecos', code='100078', label='business and management', basis='stated'),
        dict(scheme='cah', code='CAH17-01-01', label='business and management (non-specific)', basis='stated'),
        dict(scheme='cah', code='CAH17-01', label='business and management', basis='stated'),
        dict(scheme='cah', code='CAH17', label='business and management', basis='stated'),
        dict(scheme='hecos', code='100089', label='management studies', basis='inferred'),
        dict(scheme='hecos', code='100079', label='business studies', basis='inferred'),
        dict(scheme='hecos', code='100088', label='leadership', basis='inferred'),
        dict(scheme='hecos', code='100090', label='public administration', basis='inferred'),
    ],
    awards=[MA], levels=['fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, the 2022 onward revision with cross-cutting themes (recall, to check)',
    partsB='partial: no glossary in the document; terms it defines in passing (1.9 to 1.12) and its course typology (1.20 to 1.30)',
    agentDefinition="QAA's UK reference point for taught master's study in business and management at FHEQ level 7 (SCQF level 11): what a holder of the award should know, understand and be able to do, set out as one list of minimum threshold standards, with the subject's content areas, skills and a four-type typology of courses (generalist or specialist, for career entry or career development).",
    summary="Published by QAA in March 2023 for the sector, this statement covers every kind of taught master's in business and management, from MSc and MA to MBA, MPA and MRes, and related level 7 awards such as postgraduate certificates and diplomas. It sorts courses into four types, describes their purposes and characteristics, sets out distinctive features of design, progression, flexibility, partnership and review, and lists content areas, subject skills and generic skills. Its standards are a single threshold list in 4.4 (twelve items under knowledge and understanding, skills, critical perspective, application and values); it states no typical or excellent rung and does not cite the degree classification descriptions (Annex D). It treats four cross-cutting themes (equality, diversity and inclusion; accessibility; education for sustainable development; enterprise and entrepreneurship education, joined to employability) and names professional and accrediting bodies such as CMI, CIPD, the Chartered Institute of Marketing and the public administration accreditors.",
    authority='reference: a sector reference point, not a regulatory requirement; a key reference point in Wales and Scotland and part of the quality requirements in Northern Ireland, not a sector-recognised standard in England (D1, front matter)',
)

S2 = dict(
    governs='taught master\'s courses in business and management, generalist and specialist, and other provision at FHEQ level 7 and SCQF level 11 (postgraduate certificates and diplomas; the level 7 part of integrated master\'s)',
    awards=[MA, 'postgraduate diploma', 'postgraduate certificate', "integrated master's (level 7 components)"],
    levels=['fheq:7', 'fqheis:11'],
    statedScope="\"This Subject Benchmark Statement covers all types of master's degrees in Business and Management, including both specialist and generalist degrees for a range of participants, from new graduates to those with considerable work experience.\" (D1, 1.1)",
    statedSubjects=[
        dict(name='Business and Management', locator='(D1, 1.1)', kind='subject', codes=[dict(scheme='hecos', code='100078', label='business and management'), dict(scheme='cah', code='CAH17-01-01', label='business and management (non-specific)')]),
        dict(name='Master of Business Administration (MBA)', locator='(D1, 1.4; 1.24)', kind='programme title', codes=[dict(scheme='hecos', code='100078', label='business and management')]),
        dict(name='Master of Public Administration (MPA)', locator='(D1, 1.25)', kind='programme title', codes=[dict(scheme='hecos', code='100090', label='public administration')]),
        dict(name='specialist master\'s (for example marketing, project management, strategic retailing)', locator='(D1, 1.4; 1.27)', kind='specialism', codes=[]),
    ],
)

SECTIONS = {
    '1': "Context and purposes of a master's degree in Business and Management",
    '2': "Distinctive features of a master's in Business and Management",
    '3': 'Content, structure and delivery',
    '4': 'Benchmark standards',
}
SUB = [
    ('1.1', '1.7', 'Introduction'),
    ('1.8', '1.14', 'Purposes and characteristics of taught master\'s courses: Purposes'),
    ('1.15', '1.30', 'Purposes and characteristics of taught master\'s courses: Characteristics'),
    ('1.31', '1.37', 'Equality, diversity and inclusion'),
    ('1.38', '1.40', 'Accessibility'),
    ('1.41', '1.44', 'Education for Sustainable Development'),
    ('1.45', '1.49', 'Enterprise and entrepreneurship education'),
    ('2.1', '2.7', 'Design'),
    ('2.8', '2.12', 'Progression'),
    ('2.13', '2.15', 'Flexibility'),
    ('2.16', '2.18', 'Partnership'),
    ('2.19', '2.23', 'Monitoring and review'),
    ('3.1', '3.12', 'Content: Knowledge and understanding'),
    ('3.13', '3.17', 'Skills and practice'),
    ('3.18', '3.22', 'Learning and teaching'),
    ('3.23', '3.32', 'Assessment'),
    ('4.1', '4.4', 'Introduction'),
]

G = {
    '1.1': 'covers every kind of taught master\'s in the subject; a typology guides, it does not fix categories',
    '1.2': 'intended users; level 7 and SCQF 11; no national curriculum; joint subjects left to providers',
    '1.3': 'courses differ by content and by career stage; Table 1 typology',
    '1.4': 'typical award titles; the title alone does not fix the type',
    '1.5': 'research-based and taught master\'s; the MRes',
    '1.6': 'also relevant to postgraduate certificates, diplomas and integrated master\'s',
    '1.7': 'documents the statement was written to relate to',
    '1.8': 'purposes a course may serve, one or more',
    '1.9': 'what organisations and business are taken to include',
    '1.10': 'what responsible leadership is taken to include',
    '1.11': 'what career preparation and development is taken to mean',
    '1.12': 'what skills and attributes are taken to include',
    '1.13': 'purposes by course type, 1 to 4',
    '1.14': 'general courses are expected to cover the purposes; balance varies by type',
    '1.15': 'diversity of content, disciplines and perspectives',
    '1.16': 'theory together with practice',
    '1.17': 'the capstone project and methods training',
    '1.18': 'a changing discipline shapes course design',
    '1.19': 'the three new theme sections apply throughout',
    '1.20': 'characteristics follow the course type',
    '1.21': 'Type 1: generalist, career entry',
    '1.22': 'Type 1 with some specialisation; methods of linking theory to practice',
    '1.23': 'Type 1 combined with other subjects',
    '1.24': 'Type 2: generalist, post-experience, such as the MBA',
    '1.25': 'the MPA and its accreditors',
    '1.26': 'MBA and MPA largely generalist; sectoral MBAs allowed',
    '1.27': 'Type 3: specialist, career entry',
    '1.28': 'Type 3 entry, content and links to professional bodies',
    '1.29': 'Type 4: specialist, post-experience',
    '1.30': 'Type 4 entry and emphasis on practice',
    '1.31': 'what EDI covers; embedded in the subject\'s culture',
    '1.32': 'principles for an inclusive learning community',
    '1.33': 'why the subject is taught: EDI and the SDGs',
    '1.34': 'what is taught: EDI in content and perspectives',
    '1.35': 'how the subject is taught: inclusive design and modes',
    '1.36': 'examples of ways to consider EDI',
    '1.37': 'EDI as continuing review with students',
    '1.38': 'what accessibility covers and its minimum',
    '1.39': 'designing out barriers in advance',
    '1.40': 'equal access to work-based, international and digital learning',
    '1.41': 'sustainability, the SDGs and PRME in the subject',
    '1.42': 'sustainable management in the curriculum; example topics',
    '1.43': 'ethics, responsibility and sustainability, dedicated and embedded',
    '1.44': 'core skills that match the ESD guidance outcomes',
    '1.45': 'what EED does for students\' careers',
    '1.46': 'entrepreneurial capacity and theory in courses',
    '1.47': 'theory and practice of enterprise across sectors',
    '1.48': 'experiential learning for venture and portfolio careers',
    '1.49': 'EED beyond employment',
    '2.1': 'design reflects interdisciplinarity and course type',
    '2.2': 'interdisciplinary, specialist or generalist, pre- or post-experience',
    '2.3': 'knowledge joined to skills for responsible work',
    '2.4': 'employability and professional, responsible behaviour',
    '2.5': 'responsible management practice designed in',
    '2.6': 'all kinds of organisation covered',
    '2.7': 'readiness for changing working life',
    '2.8': 'a full master\'s: one year, usually 180 credits',
    '2.9': 'postgraduate certificates and diplomas as stages or exits',
    '2.10': 'integrated master\'s: length and level 7 study',
    '2.11': 'advanced standing with professional bodies; microcredits',
    '2.12': 'a route to research degrees',
    '2.13': 'flexible approaches and inclusive design',
    '2.14': 'kinds of flexibility there may need to be',
    '2.15': 'flexibility kept coherent',
    '2.16': 'partnerships with organisations',
    '2.17': 'recognition by professional bodies',
    '2.18': 'networks, bodies and learned societies',
    '2.19': 'monitoring and periodic review with students',
    '2.20': 'external reviewers in periodic review',
    '2.21': 'the external examining system',
    '2.22': 'advisory boards and employer panels',
    '2.23': 'accreditation of vocational courses',
    '3.1': 'generalist and specialist scope; consistency with the level 7 descriptor',
    '3.2': 'knowledge of organisations, context and management',
    '3.3': 'integrating the three areas',
    '3.4': 'area: the business environment',
    '3.5': 'area: organisations',
    '3.6': 'area: responsible leadership and management',
    '3.7': 'learning outcomes define knowledge and skills by type',
    '3.8': 'broad knowledge, change and integrative links',
    '3.9': 'knowledge differs by course type',
    '3.10': 'areas for generalist courses (Types 1 and 2)',
    '3.11': 'added knowledge for specialist courses (Types 3 and 4)',
    '3.12': 'Types 2 and 4 ground learning in experience',
    '3.13': 'skills tied closely to practice and employability',
    '3.14': 'cognitive, subject, personal and team skills',
    '3.15': 'skills particular to the subject',
    '3.16': 'other generic skills and attributes',
    '3.17': 'skills vary by type; reflection on experience',
    '3.18': 'diverse teaching and learning methods',
    '3.19': 'theory and practice joined through practitioners',
    '3.20': 'inclusive, engaging methods; typical activities',
    '3.21': 'teaching adapted to course type',
    '3.22': 'skills development embedded and assessed',
    '3.23': 'assessment for learning; timely feedback',
    '3.24': 'inclusive assessment design',
    '3.25': 'reliable, varied assessment methods',
    '3.26': 'where and how assessment takes place',
    '3.27': 'authentic assessment',
    '3.28': 'assessment design by learning outcomes and type',
    '3.29': 'group work and its marking',
    '3.30': 'peer review and peer assessment',
    '3.31': 'transparent assessment and co-design',
    '3.32': 'student workload in assessment design',
    '4.1': 'the list sets the minimum threshold for the award',
    '4.2': 'achievement above the threshold; the level 7 descriptor',
    '4.3': 'five factors that mark master\'s achievement',
    '4.4': 'the threshold standards, under five headings',
}
CTYPE = {
    '3.4': 'area', '3.5': 'area', '3.6': 'area', '3.10': 'area', '3.11': 'area',
    '3.18': 'practice', '3.19': 'practice', '3.20': 'practice', '3.21': 'practice', '3.22': 'practice',
    '3.23': 'practice', '3.24': 'practice', '3.25': 'practice', '3.26': 'practice', '3.27': 'practice',
    '3.28': 'practice', '3.29': 'practice', '3.30': 'practice', '3.31': 'practice', '3.32': 'practice',
}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1 and S2'),
    dict(number='none', heading='section heading lines (sections 1 to 4)', kind='other: headings, recorded as sections in S3'),
    dict(number='5', heading='List of references and further resources', kind='other: references, read for SB6 and Part E'),
    dict(number='6', heading="Membership of the Advisory Groups for the Subject Benchmark Statement for Master's Degrees in Business and Management", kind='other: membership lists'),
]

# ---------------------------------------------------------------- helpers for the two agent instructions
CITE = "QAA (2023), Business and Management master's Subject Benchmark Statement, para "
DESC = "qaa/fheq-2024/4.17"

def aaw(n, kind, what, beside, notclaim="that it is a regulatory requirement or that it holds below level 7"):
    return (f"Describe this as {kind} for the {MA} award at FHEQ level 7 (SCQF level 11): {what}. "
            f"Cite it as {CITE}{n}. Do not claim {notclaim}. Set it beside {beside}.")

def aad_l(n, when, ask):
    return (f"Raise this when {when}. Put it in plain words: second person for a student, the course outcome for staff. "
            f"Ask: {ask} Avoid reading paragraph {n} aloud at length or treating the course types as fixed boxes.")

def aad_p(n, when, ask):
    return (f"Raise this with a programme team or teacher when {when}; it is a course duty, so never hand it to a student as a target. "
            f"Frame it in plain words as a design or review question. Ask: {ask} Avoid quoting paragraph {n} at length or calling it a legal rule.")

NA_P = ('n/a', 'a duty on the course and its staff; the student meets its effect, not a standard to reach')

P = {}
def s(i, **k):
    P[i] = k

# ---------------------------------------------------------------- provider duties and obliging paragraphs
PV = dict(rung='none', addressee='provider', domain='none', award=MA, ben=NA_P)

s('1.14', type='expectation', force='should', level='none', appliesTo='general business and management master\'s courses',
  verbs=['cover'], about='covering the purposes of a master\'s', **PV,
  para="General master's courses in the subject should cover the purposes listed in 1.8, though the balance will vary with the course type and any professional recognition sought, and the intended learning outcomes will show it.",
  prac="Check the course against the purposes in 1.8: a general master's should address them, weighting them to its type and to any professional accreditation, and its intended outcomes should make that weighting visible.",
  aaw=aaw('1.14', 'a provider expectation (should)', 'general courses address the listed purposes, weighted by course type', f'the purposes in 1.8, the typology in 1.3 and 1.20 to 1.30, and {DESC}.b1'),
  aad=aad_p('1.14', 'a team is writing or revising course aims', 'Which of the purposes in 1.8 does your course weight most, and where do your outcomes show it?'))
s('1.24', type='expectation', force='should', level='none', appliesTo='Type 2 generalist post-experience courses, including the MBA',
  verbs=['build'], about='building on prior work experience', **PV,
  para="Type 2 generalist courses serve people with substantial work experience, usually at least two years, and learning should build on it; they stress leadership and strategy and use reflective and peer learning, and MBAs differ from other master's in aims, recruitment and teaching.",
  prac="For a post-experience generalist course such as an MBA, design learning that builds on what entrants bring from at least two years of work, with leadership, strategy, reflection and peer exchange at its centre.",
  aaw=aaw('1.24', 'a provider expectation (should) for one course type', 'post-experience generalist learning draws on entrants\' work experience', '1.29 and 1.30 (Type 4), 3.12 and 3.17 (learning from experience) and 3.21', "that every master's must require work experience or that the two-year figure is a fixed rule"),
  aad=aad_p('1.24', 'an MBA or similar post-experience course is being designed or reviewed', 'How does each module draw on what participants already know from work?'))
s('1.28', type='expectation', force='should', level='none', appliesTo='Type 3 specialist career-entry courses',
  verbs=['provide'], about='practice-relevant skills in specialist courses', **PV,
  para="Type 3 specialist courses usually rest on strong theory but should also give a range of skills relevant to practice; they seldom need work experience, and some link to professional body qualifications.",
  prac="In a pre-experience specialist course, pair the theory base with skills students can use in practice, and note any professional body qualification the course connects to.",
  aaw=aaw('1.28', 'a provider expectation (should) for one course type', 'specialist career-entry courses add practice-relevant skills to theory', '1.27, 3.11 (specialist knowledge) and 3.15 (subject skills)'),
  aad=aad_p('1.28', 'a specialist pre-experience course looks heavy on theory', 'Where in the course do students practise skills they will use in the job the course prepares them for?'))
s('1.31', type='expectation', force='should', level='none', appliesTo='the subject area and its courses',
  verbs=['embedded'], about='EDI embedded in the subject', **PV,
  para="Equality, diversity and inclusion reach across many identity characteristics and beyond legal duties to intersections in the student and staff body, and the subject area should make EDI a real concept built into its culture and practice.",
  prac="Treat equality, diversity and inclusion as part of how the subject is taught and practised, not as a compliance add-on, recognising differences that overlap and go beyond the protected characteristics.",
  aaw=aaw('1.31', 'a provider expectation (should) under the EDI theme', 'EDI is to be part of the subject\'s culture and practice', '1.33 to 1.37, 2.13 and theme:edi', 'that it lists every characteristic a course must monitor or that it is a statutory duty in itself'),
  aad=aad_p('1.31', 'a team discusses inclusion in its subject', 'Where would a student see inclusion in the everyday practice of your course, not only in its policies?'))
s('1.33', type='outcome', force='will', level=L7, appliesTo='students of the subject, as future managers and leaders',
  addressee='learner', domain='generic-skill', award=MA, rung='none',
  verbs=['embed'], about='EDI principles carried into management and leadership',
  para="Business and management education can help organisations tackle inequality, in line with the UN SDGs, and studying the subject will build the principles of equality, diversity and inclusion into future managers and leaders.",
  prac="Expect graduates to leave with EDI principles as part of how they will manage and lead; teach the link between inclusion, reflective practice and organisations' work on inequality and the SDGs.",
  ben="Your studies will build the principles of equality, diversity and inclusion into how you manage and lead, so that you can help organisations tackle inequality.",
  aaw=aaw('1.33', 'an expected outcome (will) under the EDI theme', 'study builds EDI principles into future managers and leaders', f'1.10 (responsible leadership), 1.34, 3.16.b8 and {DESC}.b8.2'),
  aad=aad_l('1.33', 'a student asks why inclusion matters in a management course', 'How would you show inclusion in a team you led?'))
s('1.34', type='expectation', force='should', level=L7, appliesTo='postgraduates and the courses they take',
  addressee='both', domain='understanding', award=MA, rung='none',
  verbs=['gain', 'foster', 'ensure'], about='EDI in what is taught',
  para="Courses make sure students understand critically how organisations and leaders promote EDI; postgraduates should know the legal duty not to discriminate and be equipped to build inclusive workplaces, and content should be diverse and critical of dominant approaches.",
  prac="Teach the legal duties on discrimination and the skills to build inclusive workplaces; choose content and cases that draw on varied perspectives, including the Global South and marginalised communities, and examine critically how dominant approaches can exclude.",
  ben="You should come to know the law that protects people from discrimination and gain the skills to build inclusive workplaces, studying a wide range of perspectives and questioning approaches that leave people out.",
  aaw=aaw('1.34', 'an expectation (should) on both students and courses under the EDI theme', 'critical understanding of EDI in organisations, with diverse and critical content', '1.33, 1.35, 3.10.b5 and theme:edi'),
  aad=("Raise this when content choices or inclusive leadership come up with a student or a course team. For a student, ask what perspectives their reading leaves out; for staff, frame it as a curriculum review. "
       "Ask: Which cases in the course come from outside the usual dominant settings? Avoid reading paragraph 1.34 aloud at length or treating it as a legal checklist."))
s('1.35', type='expectation', force='should', level='none', appliesTo='the design of courses and teaching',
  verbs=['designed', 'realise'], about='inclusive design of teaching and assessment', **PV,
  para="Courses should be designed so students from every background can reach their potential and feel represented; teaching, assessment and modes of learning should reflect inclusive principles and pedagogy aware of EDI.",
  prac="Design so every student can reach their potential and see themselves in the course: weigh the effects of each mode of study, plan assessment that lets different students succeed, and take account of people's multiple identities.",
  aaw=aaw('1.35', 'a provider expectation (should) under the EDI theme', 'inclusive design of teaching, modes of study and assessment', '1.38 to 1.40, 2.13, 3.24 and theme:edi'),
  aad=aad_p('1.35', 'a team chooses delivery modes or assessment formats', 'Which students might the current mode or assessment disadvantage, and what would change that?'))
s('1.37', type='expectation', force='should', level='none', appliesTo='course teams',
  verbs=['reflect', 'work'], about='continuing review of EDI with students', **PV,
  para="EDI is continuing work: course teams should reflect regularly on how to strengthen it and, where they can, do so with students; approval of changes may include an equality impact assessment.",
  prac="Put EDI on the regular review cycle, involve students in it where possible, and consider an equality impact assessment when course changes go for approval.",
  aaw=aaw('1.37', 'a provider expectation (should) under the EDI theme', 'regular reflection on EDI, in partnership with students', '2.19 (monitoring and review) and 1.31', 'that an equality impact assessment is required'),
  aad=aad_p('1.37', 'a team plans annual review or a course change', 'When did the team last review inclusion with students, and what changed as a result?'))
s('1.38', type='expectation', force='should', level='none', appliesTo='courses, from pre-application to after graduation',
  verbs=['meet', 'apply'], about='accessibility from application to graduation', **PV,
  para="Accessibility asks whether everyone can understand every part of a course however they meet it; it should at least satisfy regulatory requirements and should run from pre-application information to graduation and beyond, with examples given.",
  prac="Meet the regulatory minimum for accessibility and go further: check information, curriculum, spaces, resources and assessments at every stage, with reasonable adjustments and attention to barriers such as digital poverty and caring duties.",
  aaw=aaw('1.38', 'a provider expectation (should) under the accessibility theme', 'accessibility at least to the regulatory minimum, across the whole student journey', '1.39, 1.40, 2.14 and theme:accessibility', 'that its examples are a complete list'),
  aad=aad_p('1.38', 'a team reviews information, spaces or assessment for access', 'At which stage, from application to graduation, is access least certain for your students?'))
s('1.39', type='expectation', force='should', level='none', appliesTo='the design of courses, modules, teaching and assessment',
  verbs=['build', 'avoid'], about='designing out barriers', **PV,
  para="Courses, modules, teaching and assessment should be designed proactively to build in inclusivity and keep obstacles away from neurodivergent students and those with specific learning difficulties.",
  prac="Anticipate the needs of neurodivergent students and those with specific learning difficulties at design stage rather than waiting for adjustments to be requested.",
  aaw=aaw('1.39', 'a provider expectation (should) under the accessibility theme', 'barriers are designed out in advance', '1.38, 3.24 and theme:accessibility'),
  aad=aad_p('1.39', 'a module is being designed or redesigned', 'What would a neurodivergent student find hardest in this module as it stands?'))
s('1.40', type='expectation', force='should', level='none', appliesTo='courses and their learning opportunities',
  verbs=['include', 'enabling', 'providing'], about='equal access to work, international and digital learning', **PV,
  para="Accessibility should cover giving every student the same chances of workplace and international learning and digital access that is inclusive and free of discrimination.",
  prac="Make placements, international experiences and digital provision open to every student on equal terms.",
  aaw=aaw('1.40', 'a provider expectation (should) under the accessibility theme', 'equal access to workplace, international and digital learning', '1.38, 2.16 and theme:accessibility'),
  aad=aad_p('1.40', 'placements, study abroad or online provision are planned', 'Who on the course could not take up a placement or trip as it is now arranged?'))
s('1.42', type='expectation', force='describes', level='none', appliesTo='the business and management curriculum',
  verbs=['integrated', 'equipped'], about='sustainable management across the curriculum', **PV,
  para="Organisations matter for meeting emissions targets, so future leaders need to be ready to respond to climate challenges; management for economic, social and environmental sustainability is to be built systematically into the curriculum and its functional areas, with example topics.",
  prac="Build sustainability into each functional area of the curriculum, not one module alone, using topics such as sustainable supply chains, carbon literacy, integrated reporting and responsible leadership.",
  aaw=aaw('1.42', 'a provider expectation under the sustainability theme, worded with \'needs to\' and \'imperative\' rather than must or should', 'sustainable management across the curriculum, with example topics', '1.41, 1.43, 3.10.b1 and theme:esd', 'that the example topics are required or complete'),
  aad=aad_p('1.42', 'a team maps sustainability across its modules', 'In which functional areas of the course does climate and sustainability content not yet appear?'))
s('2.13', type='expectation', force='should', level='none', appliesTo='the design of courses',
  verbs=['designed', 'offered'], about='flexible, inclusive design', **PV,
  para="Flexible approaches let students fit study to their circumstances and may widen access; courses should be designed for inclusivity and may offer varied learning modes and assessment.",
  prac="Design with inclusivity in mind and consider offering a choice of study modes and assessment so students can fit learning to their circumstances.",
  aaw=aaw('2.13', 'a provider expectation (should) with permissive options (may)', 'inclusive design and optional flexibility in mode and assessment', '2.14, 2.15, 1.35 and theme:accessibility', 'that any particular mode must be offered'),
  aad=aad_p('2.13', 'a team weighs part-time, blended or block delivery', 'Which students could join the course only if it were offered differently?'))
s('2.19', type='expectation', force='should', level='none', appliesTo='degree-awarding bodies and their partners',
  verbs=['collect', 'analyse', 'form'], about='students in monitoring and review', **PV,
  para="Awarding bodies and partners gather and analyse information and review courses periodically against external reference points, and students should take part in that monitoring and review, which can also cover EDI.",
  prac="Involve students in monitoring and periodic review, use this statement among the external reference points, and include equality, diversity and inclusion in what is reviewed.",
  aaw=aaw('2.19', 'a provider expectation (should) on review', 'students take part in course monitoring and review', '2.20, 2.21, 1.37'),
  aad=aad_p('2.19', 'a team prepares for periodic review', 'How do students shape the evidence and the actions in your review?'))
s('2.20', type='expectation', force='will', level='none', appliesTo='higher education providers',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', **PV,
  para="Externality is essential to UK quality assurance: providers will use external reviewers in periodic review to bring an outside view and to confirm that threshold standards are met and content suits the subject.",
  prac="Include external reviewers in periodic review to test proposed changes, confirm threshold standards and check that content fits the subject.",
  aaw=aaw('2.20', 'a provider expectation (will) on externality', 'periodic review uses external reviewers to confirm threshold standards', '2.21, 4.1 and 4.4'),
  aad=aad_p('2.20', 'a periodic review panel is being set up', 'Who outside the institution will judge whether the threshold in 4.4 is met?'))
s('3.1', type='expectation', force='will', level=L7, appliesTo='generalist and specialist courses',
  verbs=['provide', 'set'], about='scope of generalist and specialist courses', **PV,
  para="Generalist courses are expected to give a broad, analytical and joined-up study of business and management across complex organisations; specialist courses will place the specialism in the wider field; the statement matches the FHEQ level 7 and SCQF level 11 descriptors.",
  prac="In a generalist course, cover organisations broadly, analytically and in an integrated way; in a specialist course, set the specialism in the context of the wider field; read both against the level 7 descriptor.",
  aaw=aaw('3.1', 'a provider expectation (will) on course scope', 'breadth for generalist courses and wider context for specialist ones', f'3.2, 3.8, 3.10, 3.11 and the level 7 descriptor {DESC}.b1'),
  aad=aad_p('3.1', 'a team defines the scope of a generalist or specialist course', 'Where does a specialist student meet the wider field of business and management?'))
s('3.7', type='expectation', force='will', level='none', appliesTo='courses and their learning outcomes',
  verbs=['defined', 'vary'], about='knowledge and skills set in learning outcomes', **PV,
  para="Each course's learning outcomes will set out its subject knowledge, understanding and skills, which may differ with the type of master's.",
  prac="State the course's knowledge, understanding and skills in its learning outcomes, matched to its type in the typology.",
  aaw=aaw('3.7', 'a provider expectation (will) on learning outcomes', 'outcomes set out knowledge, understanding and skills by course type', '1.3, 3.9, 3.17 and 4.4'),
  aad=aad_p('3.7', 'a team writes or revises course learning outcomes', 'Do your outcomes reflect the type of course you run, and could a reader tell which type from them?'))
s('3.23', type='expectation', force='should', level='none', appliesTo='assessment and feedback',
  verbs=['form', 'provided'], about='assessment for learning and timely feedback', **PV,
  para="Assessment should be part of learning, with feedback on formative and summative work that should be timely and usable for development within a module and across the course.",
  prac="Plan assessment as part of learning and return feedback on both formative and summative work quickly enough, and specifically enough, for students to act on it.",
  aaw=aaw('3.23', 'a provider expectation (should) on assessment', 'assessment supports learning through timely, actionable feedback', '3.24, 3.31 and 3.32'),
  aad=aad_p('3.23', 'feedback timing or quality is discussed', 'Can students use the feedback on one task before they submit the next?'))
s('3.29', type='expectation', force='should', level='none', appliesTo='group assessment',
  verbs=['given'], about='group work and its marking', **PV,
  para="Where work is assessed in groups, the amount of group work, its authenticity, its fit to the task and the split between group and individual marks should all be considered with care.",
  prac="Decide deliberately how much assessment is group-based, whether the task suits a group, and how group and individual marks are balanced.",
  aaw=aaw('3.29', 'a provider expectation (should) on assessment', 'group assessment is weighed for extent, authenticity, fit and marking', '3.15.b11 (teamwork), 3.27 and 3.30'),
  aad=aad_p('3.29', 'a team plans group assessment', 'How will one student\'s mark reflect their own contribution to the group?'))
s('3.30', type='expectation', force='should', level='none', appliesTo='peer review and peer assessment',
  verbs=['provided', 'set'], about='guidance and limits for peer assessment', **PV,
  para="Peer review and assessment can engage students; whether formative or summative, students should get clear guidance and the weighting of peer assessment in a module should be capped.",
  prac="When using peer assessment, brief students clearly and cap how much it counts in the module.",
  aaw=aaw('3.30', 'a provider expectation (should) on assessment', 'clear guidance and capped weighting for peer assessment', '3.29 and 3.31', 'that it fixes a particular weighting'),
  aad=aad_p('3.30', 'peer marking is proposed', 'What guidance will students get, and what share of the mark will peers decide?'))
s('3.31', type='expectation', force='should', level='none', appliesTo='assessment information',
  verbs=['shared', 'co-design'], about='transparent assessment and co-design', **PV,
  para="Assessment details should be open and given to students with the marking criteria, and there may be room for students to co-design assessments with tutors or peers.",
  prac="Publish assessment details and marking criteria to students, and consider letting students help design assessments.",
  aaw=aaw('3.31', 'a provider expectation (should) with a permissive option (may)', 'transparent assessment details and criteria; optional co-design', '3.23 and 3.30', 'that co-design is required'),
  aad=aad_p('3.31', 'assessment briefs are prepared', 'Do students see the marking criteria when they start the task?'))
s('3.32', type='expectation', force='should', level='none', appliesTo='assessment design',
  verbs=['designed'], about='student workload', **PV,
  para="Assessment should be planned with the load it places on students in mind.",
  prac="Check the total assessment load on students when designing assessment, across modules as well as within them.",
  aaw=aaw('3.32', 'a provider expectation (should) on assessment', 'assessment design takes account of student workload', '3.23 and 3.25'),
  aad=aad_p('3.32', 'deadlines cluster or a module adds tasks', 'How many assessments fall due in the same fortnight?'))
s('4.2', type='expectation', force='should', level=L7, appliesTo='higher education providers',
  verbs=['perform', 'refer'], about='evidence of achievement above the threshold', **PV,
  para="Many students will go beyond the threshold; each provider decides what evidence shows this and should refer to the qualification frameworks; the standards match the master's descriptor at FHEQ level 7 and SCQF level 11 and can guide postgraduate certificates and diplomas.",
  prac="Use the frameworks' master's descriptor when deciding what evidence shows achievement above the threshold, and treat these standards as a reference for postgraduate certificates and diplomas too.",
  aaw=aaw('4.2', 'a provider expectation (should) on standards above the threshold', 'each provider sets the evidence for achievement beyond the minimum, with reference to the frameworks', f'4.1, 4.4 and the level 7 descriptor {DESC}.b1 to {DESC}.b8.3', 'that the statement grades achievement above the threshold'),
  aad=aad_p('4.2', 'a team discusses merit and distinction criteria', 'How do your merit and distinction criteria go beyond the threshold list in 4.4?'))

# ---------------------------------------------------------------- outcomes stated with will (sections 1 and 3)
LO = dict(rung='none', force='will', level=L7, addressee='learner', award=MA, type='outcome')
s('1.21', appliesTo='students on Type 1 generalist career-entry courses', domain='understanding', **LO,
  verbs=['develop', 'make'], about='understanding of business contexts for early contribution',
  para="Type 1 courses suit graduates of other subjects with little business experience; their postgraduates will develop a sound grasp of business and organisational contexts and so should be able to contribute early and significantly to an employer.",
  prac="On a career-entry generalist course, aim for a sound grasp of how organisations work that lets students add value to an employer quickly.",
  ben="You will build a sound understanding of how businesses and organisations work, so that you can contribute to an employer early on.",
  aaw=aaw('1.21', 'an expected outcome (will) for Type 1 courses', 'a sound understanding of organisational contexts that supports early contribution at work', '3.2, 3.8 and 4.4.b1'),
  aad=aad_l('1.21', 'a student new to business asks what the course will give them', 'Which parts of how an organisation works do you feel least sure about yet?'))
s('3.2', appliesTo='graduates of taught master\'s courses', domain='knowledge', **LO,
  verbs=['demonstrate'], about='knowledge of organisations, context and management',
  para="Graduates will be able to show what they know and understand about organisations, their wider business setting including its environmental and regulatory sides, and how organisations are managed; courses stress change, the future of organisations, risk and impact on society.",
  prac="Ensure graduates can show knowledge of organisations, their environmental and regulatory context and their management, with attention to change, risk, sustainability and social impact.",
  ben="You will be able to show what you know about organisations, the wider business world they operate in, including its environmental and legal sides, and how they are managed.",
  aaw=aaw('3.2', 'an expected outcome (will)', 'knowledge of organisations, their context and their management', f'3.3 to 3.6, 4.4.b1 and {DESC}.b1'),
  aad=aad_l('3.2', 'a student or team asks what core knowledge a master\'s covers', 'Can you explain how an organisation you know is shaped by its environmental and regulatory context?'))
s('3.3', appliesTo='successful master\'s graduates', domain='understanding', **LO,
  verbs=['demonstrated'], about='integrating the areas of knowledge',
  para="How the areas named in 3.2 relate and fit together matters greatly, and successful graduates from every mode of study will show it in what they can do.",
  prac="Teach and assess the links between organisations, their context and their management, not each area alone, whatever the mode of study.",
  ben="You will be able to show how what you know about organisations, their context and their management fits together.",
  aaw=aaw('3.3', 'an expected outcome (will)', 'integration across the areas of knowledge', '3.2, 3.8 and 4.4.b1'),
  aad=aad_l('3.3', 'a student treats modules as separate topics', 'How does what you learned in one module change how you see another?'))
s('3.8', appliesTo='master\'s graduates', domain='understanding', **LO,
  verbs=['demonstrate', 'understand', 'respond', 'make'], about='breadth, change and integrative links',
  para="Graduates are typically able to show broad knowledge and deep understanding of organisations, their external context and their management; they will understand change and respond to it, and will have the breadth to connect areas of an organisation, even on specialist courses.",
  prac="Expect graduates, specialists included, to understand and respond to change and to link the different areas of an organisation, with broad knowledge and deep understanding.",
  ben="You will understand how organisations change and how to respond, and you will be able to connect different parts of an organisation, even if you specialise.",
  aaw=aaw('3.8', 'an expected outcome (will; partly typical)', 'breadth, response to change and integrative links across an organisation', f'3.4 to 3.6, 4.4.b1, 4.4.b6 and {DESC}.b1'),
  aad=aad_l('3.8', 'a specialist student asks why wider organisational topics matter', 'How does your specialism depend on other parts of the organisation?'))
s('3.12', appliesTo='students of Types 2 and 4 career-development courses', domain='understanding', **LO,
  verbs=['ground'], about='new knowledge grounded in professional experience',
  para="On career-development courses of Types 2 and 4, students will be able to root what they newly learn in their own professional experience.",
  prac="On post-experience courses, ask students to connect new theory to their own working experience in teaching and assessment.",
  ben="You will be able to connect what you learn to your own experience at work.",
  aaw=aaw('3.12', 'an expected outcome (will) for Types 2 and 4', 'new knowledge grounded in professional experience', '1.24, 1.29, 3.17 and 3.28'),
  aad=aad_l('3.12', 'an experienced student asks how theory relates to their job', 'Which idea from the course best explains something you have seen at work?'))
s('3.14', appliesTo='graduates of the subject\'s master\'s courses', domain='generic-skill', **LO,
  verbs=['demonstrate'], about='cognitive, subject, personal and team skills',
  para="Graduates will be able to show cognitive and intellectual skills and business and management competencies, with well-developed personal, interpersonal and teamwork skills that go beyond those of a first degree.",
  prac="Develop and assess intellectual skills, subject competencies and strong personal, interpersonal and team skills at a level beyond undergraduate study.",
  ben="You will be able to show strong thinking skills, business and management competencies and well-developed personal and team-working skills, beyond what a first degree asks.",
  aaw=aaw('3.14', 'an expected outcome (will) and the lead-in for the skills lists 3.15 and 3.16', 'a range of intellectual, subject, personal and team skills above undergraduate level', f'3.15, 3.16, 4.4.b3, {DESC}.b6 and spine:7'),
  aad=aad_l('3.14', 'a student asks how master\'s skills differ from a first degree', 'Which of your skills has moved furthest since your first degree?'))
s('3.17', appliesTo='students of Types 2 and 4 career-development courses', domain='generic-skill', **LO,
  verbs=['reflect', 'learn', 'integrate', 'applying', 'acquire'], about='learning from prior experience',
  para="Skills differ with course type; on Types 2 and 4, students will be able to learn from earlier experience by reflecting on it, combine new knowledge with it, apply it to new situations and gain new skills while building existing ones.",
  prac="On career-development courses, build in reflection on prior experience so that students combine it with new knowledge, apply it in new settings and extend their skills.",
  ben="You will be able to reflect on your past experience, combine it with what you learn now, use it in new situations and build both new and existing skills.",
  aaw=aaw('3.17', 'an expected outcome (will) for Types 2 and 4', 'reflection on and learning from prior experience', f'3.12, 3.28, 3.16.b7 and {DESC}.b7'),
  aad=aad_l('3.17', 'an experienced student sets goals for the course', 'What from your past work do you want to test against new ideas?'))

# ---------------------------------------------------------------- 3.10 areas for generalist courses (lead-in: will typically gain deep knowledge and critical understanding)
L310 = dict(rung='none', force='will', level=L7, appliesTo='graduates of generalist courses (Types 1 and 2)', addressee='learner', award=MA, type='outcome')
def k310(b, **k):
    s('3.10.b%d' % b, **L310, **k)
AW310 = lambda b, what: aaw('3.10.b%d' % b, 'an expected outcome (will, typically), one of a list of areas from which generalist courses draw some', what, f'3.2, 3.11, 4.4.b1 and {DESC}.b1', 'that every course must cover every area in the list')
AD310 = lambda b, when, ask: aad_l('3.10.b%d' % b, when, ask)
k310(1, domain='knowledge', verbs=['managing', 'behaving'], about='ethics, responsibility and sustainability',
     para="Will typically gain deep knowledge and critical understanding of ethics, responsibility and sustainability: managing responsibly and leading ethically on social, cultural, legal, economic and environmental questions.",
     prac="Where the course covers it, develop critical understanding of responsible management and ethical leadership across social, legal, economic and environmental issues.",
     ben="You may study ethics, responsibility and sustainability in depth: how to manage responsibly and lead ethically on social, legal, economic and environmental questions.",
     aaw=AW310(1, 'ethics, responsibility and sustainability'), aad=AD310(1, 'ethics or sustainability modules are discussed', 'Where have you seen a manager weigh profit against an environmental or social cost?'))
k310(2, domain='knowledge', verbs=[], about='markets and economies',
     para="Will typically gain deep knowledge and critical understanding of markets and economies: how markets for resources, goods and services form and work, including market failure, externalities and fair trade.",
     prac="Where the course covers it, develop critical understanding of how markets develop and operate, including their failures, externalities and fair trade.",
     ben="You may study markets and economies in depth, including why markets sometimes fail and what fair trade means.",
     aaw=AW310(2, 'markets and economies'), aad=AD310(2, 'economics content is planned or questioned', 'Can you name a market failure that affects a business you know?'))
k310(3, domain='knowledge', verbs=['generating'], about='marketing, sales, negotiation and customers',
     para="Will typically gain deep knowledge and critical understanding of marketing, sales, negotiation and customers: customer relationships, consumer behaviour, segmentation, targeting and positioning, sales and innovation in products and services.",
     prac="Where the course covers it, develop critical understanding of customer relationships, consumer behaviour, segmentation and positioning, selling and product and service innovation.",
     ben="You may study marketing, sales, negotiation and customers in depth, from consumer behaviour to how products and services are positioned and improved.",
     aaw=AW310(3, 'marketing, sales, negotiation and customers'), aad=AD310(3, 'marketing content is planned or questioned', 'How would you decide which customers a new service should target first?'))
k310(4, domain='knowledge', verbs=['managing'], about='finance and accounting',
     para="Will typically gain deep knowledge and critical understanding of finance and accounting: where finance comes from and how it is used and managed, and how accounting and information systems serve planning, control, decisions and financial risk.",
     prac="Where the course covers it, develop critical understanding of sources and uses of finance and of accounting information for planning, control, decisions and risk.",
     ben="You may study finance and accounting in depth: where money comes from, how it is managed and how accounting supports planning, decisions and managing risk.",
     aaw=AW310(4, 'finance and accounting'), aad=AD310(4, 'finance content is planned or a student is anxious about numbers', 'Which financial report would you look at first to judge a business decision?'))
k310(5, domain='knowledge', verbs=[], about='people and organisational behaviour',
     para="Will typically gain deep knowledge and critical understanding of people and organisational behaviour: responsible and inclusive leadership, strategic people management and development, engagement, the legal context, cross-cultural issues and EDI.",
     prac="Where the course covers it, develop critical understanding of inclusive leadership, strategic people management, engagement, employment law, cross-cultural working and EDI.",
     ben="You may study people and organisational behaviour in depth, including inclusive leadership, managing and developing people, employment law and working across cultures.",
     aaw=AW310(5, 'people and organisational behaviour'), aad=AD310(5, 'people management or HR content is discussed', 'How would you build engagement in a team drawn from several cultures?'))
k310(6, domain='knowledge', verbs=['transforming'], about='operations and business innovation',
     para="Will typically gain deep knowledge and critical understanding of operations and business innovation: resources, supply chains, procurement, logistics, outsourcing, quality, service excellence and projects, and turning data into information for analysis and decisions.",
     prac="Where the course covers it, develop critical understanding of operations, supply chains, quality and project management, and of tools that turn data into decision support.",
     ben="You may study operations and innovation in depth, from supply chains and quality to managing projects and using data to support decisions.",
     aaw=AW310(6, 'operations and business innovation'), aad=AD310(6, 'operations content is planned', 'Where would a delay in one supplier hurt an organisation you know most?'))
k310(7, domain='knowledge', verbs=['deliver', 'enable'], about='data analytics, digital business and information systems',
     para="Will typically gain deep knowledge and critical understanding of analytics and statistics, digital business, information systems and business intelligence: setting digital priorities and using information systems to support decisions driven by data.",
     prac="Where the course covers it, develop critical understanding of analytics, statistics, information systems and business intelligence for data-driven decisions.",
     ben="You may study data analytics, digital business and information systems in depth, and how they help organisations decide on the basis of evidence.",
     aaw=AW310(7, 'analytics, statistics, digital business and business intelligence'), aad=AD310(7, 'digital or analytics content is discussed', 'Which decision in your organisation could better data change?'))
k310(8, domain='knowledge', verbs=['maximise'], about='business policy and strategy',
     para="Will typically gain deep knowledge and critical understanding of business policy and strategy: forming policies and strategies for a changing environment and stakeholders, with risk, crisis and continuity management and communication.",
     prac="Where the course covers it, develop critical understanding of strategy and policy making for stakeholders, with risk, crisis and continuity planning.",
     ben="You may study business policy and strategy in depth, including how organisations plan for risk, crises and continuity.",
     aaw=AW310(8, 'business policy and strategy'), aad=AD310(8, 'strategy content is planned', 'How would you test a strategy against a sudden crisis?'))
k310(9, domain='knowledge', verbs=[], about='public and non-profit strategic management',
     para="Will typically gain deep knowledge and critical understanding of public and non-profit strategic management: how public services and the voluntary and community sector work, including governance, finance, leadership, co-production, public value and ethics.",
     prac="Where the course covers it, develop critical understanding of public and voluntary sector governance, finance, leadership, co-production and public value.",
     ben="You may study how public services and charities are run, including their governance, money, leadership and public value.",
     aaw=AW310(9, 'public and non-profit strategic management'), aad=AD310(9, 'a student comes from or aims for the public or voluntary sector', 'How does accountability differ between a charity and a company?'))
k310(10, domain='knowledge', verbs=['taking', 'create', 'generate'], about='entrepreneurship and enterprise development',
     para="Will typically gain deep knowledge and critical understanding of entrepreneurship and enterprise development: turning innovative ideas into new products, services or organisations that earn a return, including identifying and valuing intellectual property.",
     prac="Where the course covers it, develop critical understanding of venture creation and of recognising and valuing intellectual property.",
     ben="You may study entrepreneurship in depth: turning new ideas into products, services or organisations, and protecting and valuing intellectual property.",
     aaw=AW310(10, 'entrepreneurship and enterprise development'), aad=AD310(10, 'a student is interested in starting a venture', 'What would make an idea of yours worth investing in?'))
s('3.10.b11', type='expectation', rung='none', force='will', level='none', appliesTo='MPA courses', addressee='provider', domain='none', award=MA,
  find='MPA courses will have a greater focus on content related to governance, public policy and public management.',
  verbs=['have'], about='MPA content focus',
  para="MPA courses will give more weight to governance, public policy and public management content.",
  prac="In an MPA, weight the content towards governance, public policy and public management.",
  ben=('n/a', 'a statement about MPA course content, not an outcome for the student'),
  aaw=aaw('3.10.b11', 'a provider expectation (will) for MPA courses', 'heavier content on governance, public policy and public management', '1.25, 3.10.b9 and the MPA accreditors in SB5'),
  aad=aad_p('3.10.b11', 'an MPA is designed or reviewed', 'How much of the course addresses governance and public policy directly?'))

# ---------------------------------------------------------------- 3.11 specialist courses (will typically gain; will also acquire knowledge in)
L311 = dict(rung='none', force='will', level=L7, appliesTo='graduates of specialist courses (Types 3 and 4)', addressee='learner', award=MA, type='outcome')
s('3.11.b1', **L311, domain='knowledge', verbs=['placing'], about='the specialist subject in its wider setting',
  para="Will acquire knowledge of the specialist subject and set it within its wider organisational and contextual frame.",
  prac="Develop specialist knowledge and the ability to place the specialism within the wider organisation and its context.",
  ben="You will gain knowledge of your specialist subject and see how it fits into the wider organisation and its setting.",
  aaw=aaw('3.11.b1', 'an expected outcome (will) for specialist courses', 'specialist knowledge set within its wider organisational frame', f'3.1, 3.8 and {DESC}.b1'),
  aad=aad_l('3.11.b1', 'a specialist student focuses only on their field', 'Who else in an organisation depends on your specialism?'))
s('3.11.b2', **L311, domain='knowledge', verbs=[], about='current issues and research techniques in the specialism',
  para="Will acquire knowledge of current issues and thinking in the specialist area and of the research techniques used in it.",
  prac="Cover the specialism's current debates and the research techniques its field uses.",
  ben="You will learn the current issues and debates in your specialism and the research techniques used in it.",
  aaw=aaw('3.11.b2', 'an expected outcome (will) for specialist courses', 'current issues and research techniques in the specialism', f'4.4.b2, 4.4.b4 and {DESC}.b2'),
  aad=aad_l('3.11.b2', 'a student chooses a dissertation topic', 'What is the most debated question in your specialism right now?'))
s('3.11.b3', **L311, domain='subject-skill',
  find='both theoretical and applied perspectives enabling them to apply a range of specialist skills to the organisations (and their context) in which they as specialists may operate.',
  verbs=['apply'], about='theory and application of specialist skills',
  para="Will acquire theoretical and applied perspectives that let them use specialist skills in the organisations and settings where they may work.",
  prac="Combine theory and application so specialists can use their skills in the organisations they are likely to join.",
  ben="You will gain both theory and practice so that you can use your specialist skills in the organisations where you may work.",
  aaw=aaw('3.11.b3', 'an expected outcome (will) for specialist courses', 'theoretical and applied perspectives for using specialist skills', f'1.28, 4.4.b6 and {DESC}.b5'),
  aad=aad_l('3.11.b3', 'a specialist student asks how theory will help at work', 'Which specialist skill have you applied in a real setting so far?'))

# ---------------------------------------------------------------- 3.15 subject-specific skills (force from the lead-in 3.14: graduates will be able to demonstrate)
L315 = dict(rung='none', force='will', forceFrom='3.14', level=L7, appliesTo='graduates of the subject\'s master\'s courses', addressee='learner', award=MA, type='outcome', domain='subject-skill')
def k315(b, verbs, about, para, prac, ben, ask, beside):
    s('3.15.b%d' % b, **L315, verbs=verbs, about=about, para=para, prac=prac, ben=ben,
      aaw=aaw('3.15.b%d' % b, 'an expected subject skill (will, from the lead-in 3.14)', about, beside),
      aad=aad_l('3.15.b%d' % b, 'a student plans their skills development or a team maps skills to modules', ask))
k315(1, ['setting', 'selecting', 'nurturing', 'motivating'], 'people management',
     "Will be able to manage people: building teams, resilience and well-being, leading and motivating, choosing a fitting leadership style, fostering EDI, managing performance, setting objectives, coaching and mentoring.",
     "Develop people-management skills from team building and motivation to choosing leadership styles, managing performance, coaching and fostering inclusion.",
     "You will be able to manage people: build and motivate teams, choose how to lead in different situations, support well-being and inclusion, and coach others.",
     'Which leadership style do you fall back on, and when would another work better?', f'4.4.b12, 3.16.b8 and {DESC}.b6')
k315(2, ['collecting', 'analysing', 'identifying', 'evaluating'], 'problem-solving and critical analysis',
     "Will be able to solve problems and analyse critically: gather information, find causes, weigh and choose sustainable solutions, think critically and creatively, test assumptions and logic, and carry out and review decisions.",
     "Develop structured problem-solving and critical analysis: diagnosing causes, evaluating options, choosing sustainable solutions, checking assumptions and reasoning, and reviewing decisions once made.",
     "You will be able to work out the cause of a problem, weigh possible solutions, choose sustainable ones, test the reasoning behind them and review how they worked.",
     'When did you last check the assumptions behind a decision before acting on it?', f'4.4.b6, 3.16.b4 and {DESC}.b5')
k315(3, ['conduct', 'analysing', 'evaluating', 'evaluate', 'assess'], 'research',
     "Will be able to research business and management issues alone or in teams: design, collect and analyse qualitative and quantitative data, synthesise and report, with strong digital literacy, and judge the rigour and relevance of published research.",
     "Develop research skills across design, mixed data collection and analysis, synthesis and reporting, with digital literacy, and the critical appraisal of published studies for evidence-based decisions.",
     "You will be able to plan and carry out research, analyse numbers and words, report what you find, and judge how sound and relevant published research is.",
     'How would you judge whether a published study applies to your situation?', f'4.4.b2, 4.4.b5, 4.4.b7 and {DESC}.b2')
k315(4, ['providing', 'building'], 'commercial acumen',
     "Will have commercial acumen grounded in knowing what drives business success and failure and why sustainable customer satisfaction and loyalty matter.",
     "Develop commercial awareness of what makes organisations succeed or fail and how they keep customers satisfied and loyal in sustainable ways.",
     "You will understand what makes a business succeed or fail and why keeping customers satisfied and loyal, in sustainable ways, matters.",
     'What would you say is the main driver of success for an organisation you know?', '3.10.b3, 4.4.b6 and spine:7')
k315(5, ['act', 'generate', 'develop', 'communicate'], 'innovation, creativity and enterprise',
     "Will be able to act entrepreneurially: produce, develop and communicate ideas, handle intellectual property, win support and achieve sustainable results.",
     "Develop enterprising behaviour: generating and pitching ideas, managing intellectual property, building support and delivering sustainable results.",
     "You will be able to act in an enterprising way: come up with ideas, develop and share them, protect intellectual property and win support to deliver results.",
     'What idea of yours could you develop and pitch this term?', f'3.10.b10, 1.46 and {DESC}.b6')
k315(6, ['manipulate', 'evaluate', 'estimate', 'model'], 'numeracy',
     "Will be able to use quantitative skills to work with data and to evaluate, estimate and model business problems and processes.",
     "Develop quantitative skills for handling data and for estimating and modelling business problems.",
     "You will be able to use numbers and data to estimate, evaluate and model business problems.",
     'Which business problem could you model with the data you have?', f'3.10.b7 and {DESC}.b5')
k315(7, ['challenge', 'remove', 'handle'], 'managing complexity',
     "Will be able to manage complexity: question preconceptions, cross subject and functional boundaries to deal with complex situations as a whole, and solve unstructured problems systematically and creatively.",
     "Develop the ability to work across functional boundaries and solve complex, unstructured problems both systematically and creatively.",
     "You will be able to handle complex, messy problems by questioning assumptions, looking across functions and solving them in a careful but creative way.",
     'Which problem you face cuts across several departments, and how would you approach it?', f'4.4.b6 and {DESC}.b5')
k315(8, ['cultivating'], 'networking',
     "Will be aware of the interpersonal skills of listening, negotiation, persuasion and presentation and how they build business contacts.",
     "Develop awareness of listening, negotiating, persuading and presenting as the skills that build professional networks.",
     "You will understand how listening, negotiating, persuading and presenting help you build professional contacts.",
     'Who would you most like in your professional network, and how might you reach them?', '3.15.b12 and 3.16.b8')
k315(9, [], 'effective business communication',
     "Will be able to communicate complex ideas and arguments verbally and non-verbally through a range of media and technology, including business reports.",
     "Develop communication of complex ideas across media and technologies, including the writing of business reports.",
     "You will be able to communicate complex ideas clearly in speech, writing and other media, including business reports.",
     'Who is the audience for your next report, and what do they need first?', f'3.16.b2 and {DESC}.b5')
k315(10, [], 'awareness of current issues',
     "Will be aware of current problems and new insights, much of it at or shaped by the forefront of the discipline, a specialism or related professional practice.",
     "Keep students in touch with current problems and new insights from the leading edge of the field and of professional practice.",
     "You will know the current problems and new ideas at the leading edge of business and management and your own specialism.",
     'What new insight in your field has changed how you think this year?', f'4.4.b4 and {DESC}.b1')
k315(11, ['operate', 'recognise', 'negotiate', 'persuade', 'influence'], 'teamwork',
     "Will be able to work well in varied team roles, recognise and use members' contributions, negotiate and influence, and select, delegate to, develop and manage a team.",
     "Develop teamwork across roles: drawing on members' contributions, negotiating and influencing, and selecting, delegating to and developing team members.",
     "You will be able to work well in different team roles, make use of what each person brings, negotiate and influence, and lead and develop a team.",
     'What role do you usually take in a team, and which role do you avoid?', '3.15.b1, 3.16.b1 and 3.29')
k315(12, [], 'relationship-building and influencing',
     "Will be able to build relationships and exert influence across private, public and non-profit organisations.",
     "Develop the ability to build relationships and influence across organisations in all three sectors.",
     "You will be able to build working relationships and influence people in private, public and voluntary organisations.",
     'Which relationship outside your own organisation would help your work most?', '3.15.b8 and 3.10.b9')
k315(13, ['take', 'carry', 'recognise', 'initiate'], 'leadership and managing change',
     "Will be able to take on leadership roles and fulfil them responsibly and well, seeing when change is needed, starting it and managing it.",
     "Develop responsible leadership, including recognising the need for change, initiating it and managing it through.",
     "You will be able to take on leadership roles responsibly, see when change is needed, start it and manage it.",
     'What change would you lead first if you had the authority?', f'4.4.b12, 1.10 and {DESC}.b8.2')

# ---------------------------------------------------------------- 3.16 other generic skills (force from 3.14)
L316 = dict(rung='none', force='will', forceFrom='3.14', level=L7, appliesTo='graduates of the subject\'s master\'s courses', addressee='learner', award=MA, type='outcome', domain='generic-skill')
def k316(b, verbs, about, para, prac, ben, ask, beside):
    s('3.16.b%d' % b, **L316, verbs=verbs, about=about, para=para, prac=prac, ben=ben,
      aaw=aaw('3.16.b%d' % b, 'an expected generic skill (will, from the lead-in 3.14), refining the level 7 descriptor', about, beside),
      aad=aad_l('3.16.b%d' % b, 'a student reflects on transferable skills or a team maps generic skills', ask))
k316(1, ['work'], 'collaborative and inclusive working with stakeholders',
     "Will be able to collaborate inclusively with internal and external stakeholders and with professional integrity.",
     "Develop inclusive collaboration with stakeholders inside and outside the organisation, with professional integrity.",
     "You will be able to work with people inside and outside an organisation inclusively and with integrity.",
     'Which outside stakeholder have you worked with, and how did it go?', f'3.15.b11 and {DESC}.b8.1')
k316(2, [], 'verbal, non-verbal and digital communication',
     "Will be able to communicate verbally, non-verbally and digitally.",
     "Develop communication in speech, in non-verbal forms and through digital channels.",
     "You will be able to communicate in speech, in other non-verbal ways and online.",
     'Which form of communication do you find hardest?', f'3.15.b9 and {DESC}.b5')
k316(3, [], 'digital literacy and etiquette',
     "Will have digital literacy and good digital etiquette.",
     "Develop digital literacy and appropriate conduct in digital settings.",
     "You will be confident with digital tools and know how to behave well online.",
     'Which digital tool would most improve your work?', '3.15.b3 and spine:7')
k316(4, [], 'conceptual, systemic and critical thinking',
     "Will be able to think conceptually, systemically and critically, and to analyse, synthesise and evaluate.",
     "Develop conceptual, systems and critical thinking, with analysis, synthesis and evaluation.",
     "You will be able to think in concepts and systems, think critically, and analyse, combine and judge ideas.",
     'How would you map the system around a problem you face?', f'3.15.b2 and {DESC}.b4.1')
k316(5, [], 'conflict resolution',
     "Will be able to resolve conflict.",
     "Develop the ability to resolve conflict between people and groups.",
     "You will be able to help settle disagreements between people.",
     'How did you handle the last disagreement in a team you were part of?', f'3.15.b11 and {DESC}.b8.2')
k316(6, ['accept', 'tolerate', 'challenge', 'handle'], 'self-management',
     "Will manage themselves: taking responsibility, staying flexible and adaptable, coping with uncertainty and complexity, questioning assumptions, being resilient, self-starting and suitably assertive.",
     "Develop self-management: responsibility, adaptability, tolerance of uncertainty, resilience, initiative and appropriate assertiveness.",
     "You will be able to manage yourself: take responsibility, adapt, cope with uncertainty, bounce back, get started on your own and speak up when needed.",
     'How do you respond when a task has no clear answer?', f'{DESC}.b6 and {DESC}.b8.2')
k316(7, ['develop'], 'self-reflection',
     "Will be able to reflect on themselves, be aware of and sensitive to diversity in people and cultures, keep wanting to develop and take responsibility for building new skills to a higher level.",
     "Develop self-reflection, sensitivity to diversity and a lasting commitment to building new skills to a higher level.",
     "You will be able to reflect on yourself, be aware of differences between people and cultures, and keep taking charge of building your skills further.",
     'What has reflection on your work changed about how you act?', f'3.17 and {DESC}.b7')
k316(8, ['understanding'], 'interpersonal skills',
     "Will have interpersonal skills: understanding and empathising with others' needs, and sensitivity to diversity and inclusion in different settings.",
     "Develop empathy, understanding of others' needs and sensitivity to diversity and inclusion.",
     "You will be able to understand and empathise with what others need and act inclusively in different situations.",
     'How do you find out what a colleague needs from you?', '3.15.b1, 1.33 and theme:edi')
k316(9, [], 'initiative',
     "Will have the qualities and transferable skills for employment that calls for initiative and personal responsibility.",
     "Develop the qualities and transferable skills that roles needing initiative and personal responsibility require.",
     "You will have the qualities and skills to take initiative and personal responsibility at work.",
     'When did you last act without being asked, and what happened?', f'{DESC}.b8.1')
k316(10, ['act', 'planning', 'implementing'], 'independent learning',
     "Will have the learning ability needed for continuing professional development and be able to plan and deliver projects independently at a professional level.",
     "Develop independent learning for continuing professional development and the ability to plan and run projects alone at professional level.",
     "You will be able to keep learning on your own throughout your career and plan and run projects independently at a professional level.",
     'How will you keep learning after the course ends?', f'{DESC}.b8.3 and {DESC}.b6')

# ---------------------------------------------------------------- 4.4 threshold standards (lead-in 4.4; 4.1 defines them as the minimum)
LT = dict(type='threshold', rung='threshold', force='threshold', forceFrom='4.1', level=L7, appliesTo='holders of a master\'s degree in business and management at the threshold', addressee='learner', award=MA)
TB = 'To reach the threshold for the award, '
def kt(b, domain, verbs, about, para, prac, ben, desc, ask, find=None):
    r = dict(**LT, domain=domain, verbs=verbs, about=about, para=para, prac=prac, ben=TB + ben,
             aaw=(f"Describe this as a threshold standard: the minimum every holder of the {MA} award at FHEQ level 7 (SCQF level 11) has shown, here {about}. "
                  f"Cite it as {CITE}4.4 (item {b} of 12). Do not present it as typical or excellent performance, and do not claim it is a regulatory requirement. "
                  f"Set it beside the master's descriptor {desc}, the factor in 4.3 it falls under and spine:7."),
             aad=(f"Raise this when someone asks what passing the {MA} requires, in particular on {about}. "
                  f"Put it plainly as the floor, not the goal: second person for a student, the minimum outcome for staff. "
                  f"Ask: {ask} Avoid reading 4.4 aloud at length or implying that meeting it earns a merit or distinction."))
    if find:
        r['find'] = find
    s('4.4.b%d' % b, **r)
kt(1, 'knowledge', [], 'systematic, deep understanding of organisations and their management',
   "Will have shown a systematic and deep understanding of organisations, their external context and management, and how these relate to each other and to practice.",
   "At threshold, every graduate has shown systematic, deep understanding of organisations, their context and management, and of how these connect and apply in practice.",
   "you will have shown a thorough, organised understanding of organisations, the world around them, how they are run and how all this applies in practice.",
   f'{DESC}.b1', 'Can you explain how an organisation\'s context shapes the way it is run?')
kt(2, 'understanding', ['allow'], 'understanding of techniques for investigation and research',
   "Will have shown full understanding of the techniques needed for detailed investigation, research or advanced scholarship into issues in business and management or a specialism.",
   "At threshold, every graduate has shown comprehensive understanding of techniques for detailed investigation, research or advanced scholarship in the field or a specialism.",
   "you will have shown that you understand the methods needed to investigate and research business and management questions in detail.",
   f'{DESC}.b2', 'Which research method would suit the question you want to investigate, and why?',
   find='Comprehensive understanding of appropriate techniques sufficient to allow detailed investigation, research or advanced scholarship into relevant business and management issues or specialism within business and management.')
kt(3, 'subject-skill', [], 'command of subject and professional skills, with generic skills',
   "Will have shown strong command of the subject's academic and professional skills in the relevant field and steady proficiency in generic skills and attributes.",
   "At threshold, every graduate has shown a high command of subject-specific academic and professional skills and consistent proficiency in generic skills (see 3.15 and 3.16).",
   "you will have shown a strong command of the academic and professional skills of your field and steady ability in wider, transferable skills.",
   f'{DESC}.b7, 3.15 and 3.16', 'Which subject skill and which general skill can you show most clearly?',
   find='An excellent command of subject-specific academic and professional skills relevant to the appropriate field of business and management as well as consistent proficiency in generic skills and attributes.')
kt(4, 'understanding', ['informed'], 'critical awareness of current issues',
   "Will have shown critical awareness of current issues in the field, drawn from leading research and practice and from a proactive, independent approach to learning.",
   "At threshold, every graduate has shown critical awareness of current issues, informed by leading research and practice and by their own proactive, independent learning.",
   "you will have shown that you can think critically about current issues in business and management, drawing on leading research and practice and your own independent study.",
   f'{DESC}.b1', 'Which current issue in your field could you discuss with evidence from recent research?')
kt(5, 'subject-skill', ['evaluate'], 'critical evaluation of current research and scholarship',
   "Will have shown conceptual understanding that allows critical evaluation of current research and advanced scholarship in the field or a specialism.",
   "At threshold, every graduate has shown the conceptual understanding needed to evaluate current research and advanced scholarship critically.",
   "you will have shown that you understand the ideas well enough to judge current research and scholarship in your field critically.",
   f'{DESC}.b4.1', 'How would you judge the strength of a recent study in your area?',
   find='Conceptual understanding that enables students to evaluate critically current research and advanced scholarship in the field of business and management or a specialism within it.')
kt(6, 'subject-skill', ['taking'], 'applying knowledge to complex situations',
   "Will have shown that they can apply relevant knowledge to a range of complex situations, allowing for its links with other parts of the business or organisation.",
   "At threshold, every graduate has applied relevant knowledge to varied complex situations while accounting for links with other parts of the organisation.",
   "you will have shown that you can use what you know in complex situations, taking account of how one part of an organisation affects the others.",
   f'{DESC}.b5', 'Where have you applied what you learned to a complex situation, and what else did it affect?')
kt(7, 'subject-skill', ['used', 'create', 'interpret'], 'originality in applying knowledge and research practice',
   "Will have shown originality and creativity in applying knowledge, with a practical grasp of how established research and enquiry techniques produce and interpret knowledge in the field.",
   "At threshold, every graduate has applied knowledge with originality and creativity and understands in practice how established research techniques create and interpret knowledge.",
   "you will have shown original, creative use of what you know and a practical understanding of how research creates and makes sense of knowledge in your field.",
   f'{DESC}.b3', 'What is original about the way you applied an idea in your recent work?')
kt(8, 'subject-skill', ['evaluate', 'integrate'], 'evaluating and joining theory and practice',
   "Will have shown that they can evaluate and integrate theory and practice across many situations.",
   "At threshold, every graduate has evaluated and integrated theory and practice across a wide range of situations.",
   "you will have shown that you can weigh up theory and practice and bring them together in many different situations.",
   f'{DESC}.b5', 'Which theory has held up, or failed, when you tested it against practice?')
kt(9, 'understanding', ['advanced'], 'how research advances knowledge',
   "Will have shown understanding of how research pushes forward the limits of knowledge.",
   "At threshold, every graduate has shown understanding of how research extends the boundaries of knowledge.",
   "you will have shown that you understand how research moves knowledge forward.",
   f'{DESC}.b3', 'How has a piece of research changed what is known in your field?',
   find='An understanding of how the boundaries of knowledge are advanced through research.')
kt(10, 'generic-skill', ['championing', 'behaving'], 'commitment to global social responsibility and integrity',
   "Will have shown commitment to championing global social responsibility and ethical values and to acting with integrity.",
   "At threshold, every graduate has shown a commitment to global social responsibility and ethical values and has acted with integrity.",
   "you will have shown that you are committed to social responsibility worldwide, to ethical values and to acting with integrity.",
   f'{DESC}.b8.1', 'Where have your values shaped a decision you made in your studies or work?')
kt(11, 'understanding', ['take'], 'an international perspective on globalisation',
   "Will have shown the ability to take an international view, including the effects of globalisation on business, society and the environment and their ethical implications.",
   "At threshold, every graduate has shown an international perspective, understanding how globalisation affects organisations, societies and the environment, with its ethical implications.",
   "you will have shown that you can take an international view, including how globalisation affects business, society and the environment and what that means ethically.",
   f'{DESC}.b5', 'How does globalisation affect an organisation you know, for better and worse?')
kt(12, 'generic-skill', ['manage', 'lead', 'appreciating'], 'managing and leading with global social responsibility',
   "Will have shown they can lead and manage with a firm sense of social responsibility worldwide, aware of the conflicting pressures this brings in complex settings.",
   "At threshold, every graduate has shown they can lead and manage with a firm sense of worldwide social responsibility, recognising the tensions it creates in complex environments.",
   "you will have shown that you can manage and lead with a strong sense of social responsibility, aware of the tensions this creates in complex settings.",
   f'{DESC}.b8.2', 'When might acting responsibly conflict with a business target, and how would you lead through it?')

GRADE = {}   # one rung only: no gradeOf links
TH = {'1.31': 'theme:edi', '1.33': 'theme:edi', '1.34': 'theme:edi', '1.35': 'theme:edi', '1.37': 'theme:edi',
      '1.38': 'theme:accessibility', '1.39': 'theme:accessibility', '1.40': 'theme:accessibility',
      '1.42': 'theme:esd'}

S5 = dict(
    levels=[
        dict(id='fheq:7', role='cites', locator='D1, 1.2; 1.6; 2.8; 2.9; 2.10; 3.1; 4.2', descriptor='std:doc:qaa-fheq-2024-framework, qaa/fheq-2024/4.17.*'),
        dict(id='fqheis:11', role='cites', locator='D1, 1.2; 1.6; 2.8; 2.10; 3.1; 4.2', descriptor='std:doc:qaa-fqheis-2024-framework (shares the FHEQ 4.17 descriptor)'),
        dict(id='fheq:6', role='cites', locator='D1, 1.6 (integrated master\'s combine levels 6 and 7)'),
        dict(id='fqheis:10', role='cites', locator='D1, 1.6 (integrated master\'s combine levels 10 and 11)'),
        dict(id='spine:7', role='refers', locator='std:ref:uk-framework R2 and R8; inferred (Part E)'),
    ],
    crosswalks=[
        dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 1.2; 2.8; 4.2)'),
        dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 1.6)'),
        dict(**{'from': 'fheq:7'}, to='spine:7', relation='sits-at', basis='inferred from std:ref:uk-framework R2 (Part E)'),
    ])
S6 = [
    dict(id='theme:edi', role='carries', carriedIn=['1.19', '1.31', '1.32', '1.33', '1.34', '1.35', '1.36', '1.37', '2.5', '2.13', '2.19', '2.22', '3.10', '3.15', '3.16', '3.20', '3.24']),
    dict(id='theme:accessibility', role='carries', carriedIn=['1.35', '1.36', '1.38', '1.39', '1.40', '2.13', '2.14']),
    dict(id='theme:esd', role='carries', carriedIn=['1.10', '1.19', '1.33', '1.41', '1.42', '1.43', '1.44', '1.49', '2.5', '3.2', '3.4', '3.10']),
    dict(id='theme:enterprise', role='carries', carriedIn=['1.11', '1.19', '1.45', '1.46', '1.47', '1.48', '1.49', '3.10', '3.15', '3.19']),
]
S7 = [
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='the master\'s descriptor, FHEQ level 7 (4.17); cited in 1.6, 1.7, 2.8, 3.1, 4.2 (the statement cites the 2014 edition)'),
    dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='SCQF level 11, sharing the FHEQ 4.17 descriptor'),
    dict(rel='cites', target='std:doc:qaa-advancehe-esd-2021-guidance', note='ESD guidance and its learning outcomes (1.41, 1.44)'),
    dict(rel='cites', target='std:doc:qaa-enterprise-2018-guidance', note='enterprise behaviours, attributes and competencies (1.48)'),
    dict(rel='thresholdAt', target='std:ref:uk-framework', note='the threshold standards sit at spine:7; inferred'),
    dict(rel='relatedTo', target='std:doc:qaa-business-and-management-2023-benchmarks', note='the bachelor\'s statement for the same subject, same year; inferred, not cited in the text'),
]
S8 = dict(published='2023-03', lastReviewed='none-stated', reviewCycle='none-stated', consultation='none-stated', replacedBy='none',
          edition='fourth edition, published 8 March 2023 (D1, back matter)')

SB1 = [
    'Taught master\'s in the subject vary widely in content, in how many disciplines they draw on and in the perspectives they take, and are often fast-paced, broad or specialist (D1, 1.15)',
    'Every course joins theory to the consideration of practice, with theory preparing students to tackle complex issues and act on opportunities (D1, 1.16)',
    'A capstone project, from a dissertation to a consultancy project or white paper, is a defining feature, with methods training to prepare for it (D1, 1.17)',
    'The discipline changes quickly, and course design and delivery are to follow that change (D1, 1.18)',
    'Courses fall into four types by content (generalist or specialist) and by career stage (entry or development), and a title alone does not fix the type (D1, 1.3; 1.4; 1.20 to 1.30)',
    'Courses are interdisciplinary, drawing on social sciences, humanities and sciences, and are designed to join subject knowledge to responsible, effective working (D1, 2.1 to 2.3)',
    'Responsible management, sustainability and inclusion are designed into courses, which cover private, public and non-profit organisations (D1, 2.5; 2.6)',
    'The subject is closely tied to practice and to employability, with skills developed for and assessed through practice (D1, 3.13; 3.22)',
]
SB2 = [
    dict(theme='theme:edi', inThisSubject='Inclusion is framed by why, what and how the subject is taught: future managers and leaders carry EDI into organisations, content draws on diverse and critical perspectives, and teaching, modes and assessment are inclusive (D1, 1.31 to 1.37)',
         statements=['1.31', '1.33', '1.34', '1.35', '1.37', '2.13', '2.19', '3.10.b5', '3.15.b1', '3.16.b7', '3.16.b8']),
    dict(theme='theme:accessibility', inThisSubject='Accessibility runs from pre-application to after graduation, at least to the regulatory minimum, with barriers designed out and equal access to placements, international and digital learning (D1, 1.38 to 1.40)',
         statements=['1.38', '1.39', '1.40', '2.13']),
    dict(theme='theme:esd', inThisSubject='Sustainable management, carbon literacy and responsible leadership are built into every functional area, drawing on the SDGs and PRME, with ethics, responsibility and sustainability as a knowledge area (D1, 1.41 to 1.44; 3.10)',
         statements=['1.42', '3.2', '3.10.b1']),
    dict(theme='theme:enterprise', inThisSubject='Enterprise and entrepreneurship education, joined to employability, builds entrepreneurial mindsets for new ventures and innovation in existing organisations, through theory and experiential learning (D1, 1.45 to 1.49; 3.10; 3.15)',
         statements=['3.10.b10', '3.15.b5']),
]
SB3 = dict(
    areas=[
        dict(component='3.4', gloss='the business environment, local to global, and its effects on organisations'),
        dict(component='3.5', gloss='organisations: functions, structures, governance, behaviour and culture'),
        dict(component='3.6', gloss='responsible leadership and management, theory and ethical decision-making'),
        dict(component='3.10', gloss='ten knowledge areas for generalist courses, plus the MPA focus'),
        dict(component='3.11', gloss='specialist knowledge, current issues and applied perspectives'),
    ],
    practices=[
        dict(component='3.18', kind='teaching', gloss='diverse methods; research methods training in most courses'),
        dict(component='3.19', kind='teaching', gloss='practitioners and stakeholders in teaching and co-creation'),
        dict(component='3.20', kind='learning', gloss='inclusive modes and a range of learning activities'),
        dict(component='3.21', kind='teaching', gloss='teaching adapted to course type'),
        dict(component='3.22', kind='assessment', gloss='skills development embedded and formally assessed'),
        dict(component='3.23', kind='assessment', gloss='assessment for learning; timely feedback'),
        dict(component='3.24', kind='assessment', gloss='inclusive assessment design'),
        dict(component='3.25', kind='assessment', gloss='typical assessment methods, capstone included'),
        dict(component='3.26', kind='assessment', gloss='online, in situ and other settings'),
        dict(component='3.27', kind='assessment', gloss='authentic assessment and integrity'),
        dict(component='3.28', kind='assessment', gloss='reflective assessment on post-experience courses'),
        dict(component='3.29', kind='assessment', gloss='group work and its marks'),
        dict(component='3.30', kind='assessment', gloss='peer assessment guidance and weighting'),
        dict(component='3.31', kind='assessment', gloss='transparent criteria; co-designed assessment'),
        dict(component='3.32', kind='assessment', gloss='assessment workload'),
    ])
SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.4', award=MA, items=12)],
    rungBases='4.1 defines the 4.4 list as the minimum threshold for the award; no typical or excellent rung is stated; 4.2 says many students will exceed the threshold and leaves the evidence for that to each provider with reference to the frameworks',
    outcomeLists=[
        dict(leadIn='3.10', gloss='knowledge areas for generalist courses (will typically gain)', items=10, award=[MA]),
        dict(leadIn='3.11', gloss='added knowledge for specialist courses (will also acquire)', items=3, award=[MA]),
        dict(leadIn='3.14', gloss='subject skills listed in 3.15 (force from 3.14)', items=13, award=[MA]),
        dict(leadIn='3.14', gloss='generic skills listed in 3.16 (force from 3.14)', items=10, award=[MA]),
    ],
    outcomes=[])
SB4A_FULL = []
SB5 = [
    dict(body='Chartered Management Institute (CMI)', says='some courses give advanced standing towards its management and leadership qualifications (D1, 2.11)', requirements='not yet ingested (Part E)'),
    dict(body='Chartered Institute of Personnel and Development (CIPD)', says='specialist post-experience courses often link to its qualifications, and some give accelerated progression to them (D1, 1.29; 2.11)', requirements='not yet ingested (Part E)'),
    dict(body='Chartered Institute of Marketing', says='an example of a professional body whose qualifications Type 4 courses often link to (D1, 1.29)', requirements='not yet ingested (Part E)'),
    dict(body='International Commission on the Accreditation of Public Administration and Training (ICAPA)', says='an academic accreditor an MPA may be accredited by (D1, 1.25)', requirements='not yet ingested (Part E)'),
    dict(body='European Association for Public Administration Accreditation (EAPAA)', says='an academic accreditor an MPA may be accredited by (D1, 1.25)', requirements='not yet ingested (Part E)'),
    dict(body='Network of Schools of Public Policy, Affairs and Administration (NASPA, as the text names it)', says='an academic accreditor an MPA may be accredited by (D1, 1.25)', requirements='not yet ingested (Part E)'),
    dict(body='professional, statutory and regulatory bodies (PSRBs) in general', says='courses may reflect PSRB recognition requirements, which can help learners apply management skills and plan development; vocational courses may need PSRB evaluation and accreditation (D1, 1.14; 2.17; 2.23; front matter)', requirements='not yet ingested (Part E)'),
    dict(body='accrediting bodies (unnamed)', says='some expect ethics, responsibility and sustainability to be integrated into business school curricula (D1, 1.41)', requirements='not yet ingested (Part E)'),
    dict(body='UN Principles for Responsible Management Education (PRME)', says='courses can draw on it to build students\' capacity to create sustainable value (D1, 1.41)', requirements='not yet ingested (Part E)'),
    dict(body='European Quality Link (EQUAL)', says='its MBA guidelines are among the documents the statement was written to relate to (D1, 1.7)', requirements='not yet ingested (Part E)'),
]
SB6 = dict(
    themes=[
        dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.19', '1.31', '1.32', '1.33', '1.34', '1.35', '1.36', '1.37', '2.5', '2.13', '2.19', '2.22', '3.10', '3.15', '3.16', '3.20', '3.24'],
             statements=['1.31', '1.33', '1.34', '1.35', '1.37', '2.13', '2.19', '3.10.b5', '3.15.b1', '3.16.b7', '3.16.b8']),
        dict(id='theme:accessibility', named='Accessibility', carriedIn=['1.35', '1.36', '1.38', '1.39', '1.40', '2.13', '2.14'], statements=['1.38', '1.39', '1.40', '2.13']),
        dict(id='theme:esd', named='Education for Sustainable Development', carriedIn=['1.10', '1.19', '1.33', '1.41', '1.42', '1.43', '1.44', '1.49', '2.5', '3.2', '3.4', '3.10'], statements=['1.42', '3.2', '3.10.b1']),
        dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (with employability in the front matter)', carriedIn=['1.11', '1.19', '1.45', '1.46', '1.47', '1.48', '1.49', '3.10', '3.15', '3.19'], statements=['3.10.b10', '3.15.b5']),
    ],
    frameworks=[
        dict(framework='fheq', levels=['fheq:7', 'fheq:6'], citedIn=['1.2', '1.5', '1.6', '2.8', '2.9', '2.10', '3.1', '4.2']),
        dict(framework='scqf', levels=['fqheis:11', 'fqheis:10'], citedIn=['1.2', '1.5', '1.6', '2.8', '2.10', '3.1', '4.2']),
    ],
    bodies=[
        dict(body='Chartered Management Institute (CMI)', citedIn=['2.11']),
        dict(body='Chartered Institute of Personnel and Development (CIPD)', citedIn=['1.29', '2.11']),
        dict(body='Chartered Institute of Marketing', citedIn=['1.29']),
        dict(body='ICAPA', citedIn=['1.25']),
        dict(body='EAPAA', citedIn=['1.25']),
        dict(body='NASPA (as named)', citedIn=['1.25']),
        dict(body='PSRBs in general', citedIn=['1.14', '2.17', '2.23']),
        dict(body='accrediting bodies (unnamed)', citedIn=['1.41', '3.26']),
        dict(body='UN PRME', citedIn=['1.41']),
        dict(body='European Quality Link (EQUAL)', citedIn=['1.7']),
    ],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework', named="Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies (the references list the 2014 edition)", citedIn=['1.6', '1.7', '2.8', '3.1', '4.2'], role='the level 7 master\'s descriptor and qualification lengths'),
        dict(document="not yet ingested: QAA Characteristics Statement: Master's Degree (2020), listed in Part E", named="Characteristics Statement: Master's Degree(s)", citedIn=['1.4', '1.7', '1.8', '2.8'], role='award titles, purposes and lengths of master\'s'),
        dict(document='not yet ingested: QAA Characteristics Statement: Micro-credentials (2022), listed in Part E', named='Characteristics Statement: Micro-Credentials', citedIn=['2.11'], role='level 7 microcredits'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named="QAA and Advance HE's Education for Sustainable Development Guidance, 2021", citedIn=['1.41', '1.44'], role='sustainability competencies and learning outcomes'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='enterprise behaviours, attributes and competencies (as defined by QAA, 2018)', citedIn=['1.48'], role='enterprise competencies reflected in subject skills'),
    ])

B1 = [
    dict(slug='organisations', definition='Read broadly: public, private, non-profit and social enterprises of every size and structure, from start-ups and micro businesses to global firms; business likewise is read broadly (D1, 1.9)',
         beneficiaryDefinition='Any kind of organisation you might work in, from a start-up or charity to a public body or a global company.', scopeNote='applies throughout the statement', category='unknown', practices=['business and management']),
    dict(slug='responsible-leadership', definition='Leadership that is authentic, driven by values, inclusive, ethical, sustainable, systemic and transformative, weighing stakeholders now and in future and addressing climate change and fair, inclusive net zero (D1, 1.10)',
         beneficiaryDefinition='Leading in a way that is ethical, inclusive and sustainable, and that thinks about everyone affected, now and later.', scopeNote='used in 1.8, 3.6, 3.10 and 4.4', category='unknown', practices=['business and management']),
    dict(slug='career-preparation-and-development', definition='Building professional-level knowledge and skills, or preparing for research and further study, with self-awareness, personal development and a positive stance on change and enterprise (D1, 1.11)',
         beneficiaryDefinition='Getting ready for, or moving on in, a business career, or preparing for research.', scopeNote='one of the purposes in 1.8', category='unknown', practices=['business and management']),
    dict(slug='skills-and-attributes', definition='Transferable academic and professional skills suited to a business career but not limited to it, with continuing reflection, self-awareness, lifelong learning and regard for others\' well-being (D1, 1.12)',
         beneficiaryDefinition='The skills and qualities you build that are useful in business and beyond it.', scopeNote='one of the purposes in 1.8', category='unknown', practices=['business and management']),
    dict(slug='course-typology', definition='Four course types: Type 1 generalist for career entry, Type 2 generalist for career development (MBA, MPA), Type 3 specialist for career entry, Type 4 specialist for career development (D1, 1.3; 1.20 to 1.30)',
         beneficiaryDefinition='Whether a course is broad or specialist, and whether it is for people starting a career or already working.', scopeNote='the statement treats the types as guidance, not strict categories (1.1)', category='unknown', practices=['business and management']),
    dict(slug='capstone-project', definition='A substantial final piece of independent work involving research, such as a dissertation, thesis, consultancy project, white paper or business project (D1, 1.17)',
         beneficiaryDefinition='A large final project of your own, such as a dissertation or a consultancy report.', scopeNote='a characteristic of the taught master\'s', category='unknown', practices=['business and management']),
]
B2A = [
    dict(concept='organisations', form="'Organisations'", lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='responsible-leadership', form="'responsible leadership'", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='career-preparation-and-development', form="'Preparation for, and/or further development of, a career in business and management'", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='skills-and-attributes', form="'Skills and attributes'", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='course-typology', form='Type 1 to Type 4', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='capstone-project', form='capstone project', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
]
B4 = []; B5 = []
D3 = [
    dict(source="QAA (2020) Characteristics Statement: Master's Degree", why='cited for award titles, purposes and length (1.4; 1.7; 1.8; 2.8)'),
    dict(source='QAA (2022) Characteristics Statement: Micro-credentials', why='cited for level 7 microcredits (2.11)'),
    dict(source='European Quality Link (2014) Equal MBA Guidelines', why='cited as a document the statement relates to (1.7)'),
]
E = [
    'Master\'s only: the whole statement is at FHEQ level 7 and SCQF level 11; every learner statement carries award "master\'s" and level fheq:7 (no `.masters` suffix, since no bachelor\'s standards are present). Differs from Psychology.',
    'Rungs: one only. 4.4 is the threshold list, defined by 4.1 as the minimum ("minimum threshold standards that a student will have demonstrated"); no typical or excellent rung; 4.2 leaves achievement above the threshold to each provider. The skeleton counted no rungs. Force recorded as `threshold`, forceFrom 4.1. No gradeOf links.',
    'Rung lead-in wording: "On graduating with a master\'s degrees in the Business and Management field, students will have demonstrated:" with five sub-headings (Knowledge and understanding; Skills; Critical perspective; Application; Values) run into the list in the held text. A new lead-in shape.',
    'Skeleton cuts corrected by `find`: 4.4.b2, 4.4.b3, 4.4.b5 and 4.4.b9 carried the next sub-heading at their end; 3.10.b11 and 3.11.b3 carried the next typology heading. The spans now end at the item.',
    'Threshold item 4.4.b3 uses the word "excellent" ("An excellent command of ..."): this is the threshold rung, not the excellent rung (P3 to confirm).',
    'The 4.4 items follow the FHEQ master\'s descriptor closely (4.4.b2 with qaa/fheq-2024/4.17.b2; 4.4.b5 with 4.17.b4.1; 4.4.b7 and 4.4.b9 with 4.17.b3); the pointers in each author-agent-written instruction are inferred.',
    '4.3 ("factors that distinguish a master\'s level of achievement can be articulated in the demonstration of") is read as a framing list naming the five dimensions of 4.4, not as statements; P3 to confirm.',
    'Skill lists 3.15 ("Skills particular to ... include the following") and 3.16 ("Other generic skills and attributes include") have no modal of their own; they are recorded as outcome statements with force will from the lead-in 3.14 ("Graduates ... will be able to demonstrate a range of ... competencies specific to business and management"), forceFrom 3.14. An inference for P3.',
    'Outcome lists 3.10 and 3.11 are typical ("will typically gain ... in some of the following areas"): no course need cover every area. Recorded as force will, rung none.',
    'Definitional "should" in 1.9 to 1.12 ("should be understood", "should be taken to mean", "should incorporate") read as definitions for Part B, not statements.',
    'Obliging words outside the five, recorded as `describes` or not as statements: 1.42 "needs to be integrated" and "It is therefore imperative" (recorded, force describes); 3.20 and 3.25 "need to" (not statements, provider norms); 1.24 "are expected to" (MBA differences; the record takes the paragraph\'s "should"); 1.41 "There is an expectation by some accrediting bodies" (description of others\' expectations); 1.32, 3.24 "It is important that" (not statements).',
    'Plain-present provider norms not recorded as statements (template open point 5): 1.8 purposes list; 1.13 purposes by type (with descriptive "will include" and "will also instil" about course purposes); 1.17 capstone ("It will involve independent research"); 1.30 Type 4 ("will normally require", "will have an emphasis on practice"); 1.36 examples ("could consider"); 2.1 to 2.7 design; 2.14 ("there may need to be"); 2.16 partnerships; 2.21 external examiners; 3.18 to 3.22; 3.25 methods; 3.28 ("will be determined"). Abbott\'s P3 decides.',
    'Provider expectations with "will" recorded as statements: 2.20 (external reviewers), 3.1 (course scope), 3.7 (learning outcomes), 3.10.b11 (MPA focus). P3 to confirm they count.',
    '1.34 records one paragraph with two addressees (postgraduates should be aware ...; courses should ensure ...): addressee both.',
    'Themes: the front matter names four cross-cutting themes, the fourth as "employability, entrepreneurship and enterprise education"; recorded under theme:enterprise, with employability not given its own id (a new id would go here). Employability also appears in 1.8, 1.21, 2.4, 2.22, 3.13, 3.27.',
    'No generative AI section and no mention of artificial intelligence.',
    'Annex D (degree classification descriptions) is not cited: the statement is at master\'s level and has no honours classes. The skeleton\'s doc:annex-d hits were empty.',
    'CQFW not cited; Wales appears only in the front matter (Quality Assessment Framework for Wales). SCQF is cited as "SCQF Level 11 on the FQHEIS".',
    'The statement cites the Frameworks in the 2014 edition (references list) and refers to "Section 4.17" for the level 7 descriptor; it is linked to the 2024 ingested edition, where 4.17 is the same descriptor. Inferred.',
    'S5 spine:7 and S7 thresholdAt std:ref:uk-framework are inferred from the reference framework (R2).',
    'S7 relatedTo std:doc:qaa-business-and-management-2023-benchmarks (the bachelor\'s statement) is inferred; the text does not cite it.',
    'Inferred subject codes, held back from lookup until P3: hecos 100089 management studies, hecos 100079 business studies, hecos 100088 leadership, hecos 100090 public administration (from the MPA in 1.25 and 3.10.b9).',
    'Bodies not yet ingested: CMI, CIPD, Chartered Institute of Marketing, ICAPA, EAPAA, NASPA (named so in 1.25; recall suggests NASPAA, to check), PRME, EQUAL. The references list (excluded matter) also names AACSB, CABS and EFMD, not in the body of the text.',
    'Shared documents not yet ingested: QAA Characteristics Statement: Master\'s Degree (2020) and Characteristics Statement: Micro-credentials (2022) (D3). The front matter also names QAA\'s Advice and Guidance and Glossary (excluded matter).',
    'Section order differs from Psychology: a long typology of four course types (1.20 to 1.30) and a section 2 on distinctive features (design, progression, flexibility, partnership, monitoring and review).',
    'Typing slips in the held text kept as found in `source`: "heathcare" (1.2), "a master\'s degrees" (4.4), "Section 4.17 of the Frameworks" for the descriptor, "paragraphs 1.31-37" (2.5).',
]
