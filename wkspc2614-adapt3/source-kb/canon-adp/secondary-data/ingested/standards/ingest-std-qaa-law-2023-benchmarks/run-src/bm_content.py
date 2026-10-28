# bm_content.py: run 0116 (std), QAA Subject Benchmark Statement Law, March 2023. Judgement for tools/bm_build.py.
# Templates: standards 0.8.0-draft, benchmark 0.6.0-draft, run layer 0.7.0-draft; brief BM-BRIEF 0.2.3. Our words throughout except FINDS (the issuer's spans).
# Exact statement texts where the skeleton cut wrongly (trailing headings, page breaks) or gave component spans; each occurs once.
FINDS = {
    '1.4': '1.4 The study of law is both national and global in outlook, relevance, and application. Therefore, the study of law may focus on one or more jurisdictions. This Statement requires knowledge of the main features and principles of whichever legal system is (or systems are) being considered. Areas covered may include the relationships between individuals, between individuals and other entities, individuals and the state, as well as sources of law. The subject of law is shaped by and in turn impacts on, among other things, the ethical, social, political, environmental, and economic norms of different jurisdictions. Such impact may also be reflected in the curriculum.',
    '1.8': '1.8 The interaction of law with equality, diversity and inclusion will therefore be highlighted, given that the law is involved in regulating these issues while more generally being linked with concerns of justice and fairness. Legal study may thus encourage reflective engagement with the history, politics and impacts of law and legal knowledge with respect to these issues. This includes the actual and potential uses and limitations of legal understanding in managing equalities in culture and society, highlighting the shifting role of law and legal institutions with respect to different forms of systemic injustice.',
    '1.9': '1.9 Providers demonstrate their commitment to widening access and inclusive participation to ensure that each Law student can thrive and reach their full potential regardless of their background or disability. Providers anticipate and take responsibility for the provision of inclusive teaching, learning and assessment methods underpinned by a desire for accessibility for all marginalised groups. They will also have responsibilities for making reasonable adjustments and taking on proactive preventive duties and obligations.',
    '1.11': '1.11 In meeting the needs of disabled students, consideration could be given to creating inclusive learning environments. There are multiple disabled identities and disability in the context of studying law, and they should be understood in all its various forms. Disabled Law students can experience a complex transition through law school where identities are constructed and reconstructed on multiple occasions in different contexts.',
    '1.12': '1.12 Flexibility of assessment methods needs to be considered by providers to meet the needs of different students and demonstrate that learning is possible in a variety of ways.',
    '2.2': '2.2 Over the course of a degree with honours (FHEQ Level 6; FQHEIS Level 10) Law students will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the progressive attainment of knowledge, skills, expertise and experience that build towards the final achievement of meeting the threshold level subject skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components. Upon graduation from an undergraduate degree, it would be expected that a student who had achieved a second- class degree or higher would be capable of, and equipped for, undertaking postgraduate study in Law or an associated discipline. Entry requirements to postgraduate courses are, however, determined by individual providers and may require specified levels of achievement at undergraduate level.',
    '2.3': '2.3 Undergraduates studying a combined, joint or major-minor route will achieve core elements of the specific and generic skills for the subject, and will add others according to the requirements of the relevant joint courses. Additionally, they may explore the overlap between their two subject areas via interdisciplinary study.',
    '2.6': '2.6 Providers will consider holistically the learning, teaching and assessment of a Law course to ensure that it offers learning in creative ways across different modalities of delivery\n- to include online, blended or face-to-face - to widen access and ensure that all students can achieve their full potential within an inclusive and supportive learning environment. Practical learning opportunities - for example, through clinical education, work placements, mentoring schemes and via other experiential and/or innovative routes - can be considered\n\n7\nacross all modalities of learning. Where appropriate, the flexibility of digital tools will be used to build the digital confidence and fluency of students within the context of some of the complex and challenging changes brought about by technologically mediated practices. This fluency is likely to include knowing what technology works best in a given situation and developing digital literacies grounded in authentic disciplinary and professional values and identities.',
    '2.7': '2.7 Providers will seek to harness potential solutions, using different technological mediums, for flexible delivery methods which facilitate student learning in accessible, meaningful and impactful ways. These will present opportunities for knowledge exchange and skills acquisition that are fair and accessible for all in ways that will afford increased opportunities. For example, offering courses as a work-based learning route, a theoretical route, a skills-focused route, or a route for those who have already acquired a degree and experience in a different discipline.',
    '2.12': '2.12 Qualifying Law degrees in the UK with professional and vocational outcomes will also require evaluation and accreditation from relevant PSRBs. Institutions should be explicit to potential and current students about their routes to professional qualification.',
    '3.2': '3.2 Law degrees provide opportunities for developing proficiency in legal understanding. This means knowledge and comprehension of, and the capacity to question and apply, theories, concepts, values, principles and rules of public and private laws within a range of contexts. They include, but are not limited to, individual, regional, national and global contexts, as well as institutional, normative, social, political, economic, cultural, historical, ethical, philosophical, technological and ecological contexts. Legal understanding also includes the ability to recognise ambiguity and deal with legal uncertainty. It involves offering evidenced conclusions via the application of knowledge to address actual or hypothetical problems in different contexts, and developing the capacity to produce syntheses of relevant doctrinal, policy and contextual issues, present reasoned choices between alternative solutions, and make critical judgements on the merits of particular arguments. No particular legal subjects or areas of regulation are required for legal understanding to be developed, although it is expected that legal study will include detailed engagement with substantive areas of law in order to demonstrate and provide opportunities for students to develop this understanding. Individual courses may differ in their content and may focus on one or more jurisdictions. Providers intending a course to operate as part of a pathway into legal or other professional practice will be aware of the requirements of relevant PSRBs.',
    '3.5': '3.5 The teaching and learning environments developed by different providers will reflect their respective approaches to legal study. Learning and teaching methods are designed to best fit the subject matter at hand and the learning outcomes set, considering the needs of different learners. Innovation in teaching methodology and engagement with innovative approaches could drive curriculum design and development. Learning and teaching methods will embrace principles of sustainability, inclusion and diversity as well as accessibility. This may include synchronous and asynchronous methods of delivery, using technology- enhanced learning as appropriate, along with in-person, classroom-based learning and teaching opportunities (both curricular and extracurricular). As far as possible, providers will ensure digital inclusivity for students (for example, equal access to Wi-Fi and digital equipment).',
    '3.6': '3.6 The interactions between teaching, research and professional practice are key elements of the environment in which Law is taught. Staff will be given opportunities for development and may have opportunities to interact with learned societies in law and broader external networks. Staff teaching on Law courses may have obtained, or may be supported towards obtaining, a postgraduate qualification in learning and teaching or an equivalent recognition - such as Advance HE’s PSF . Students studying for a Law degree are taught within an environment that is conducive to learning, intellectually stimulating and embraces intellectual and/or neurological diversity. Students will have access to, and be appropriately trained in the identification, retrieval and use of, legal sources and sources of academic commentary. They will have access to relevant published literature, digital technologies, databases and associated software and computing resources. To ensure development of digital literacy skills, students will be supported to use these resources effectively in group and individual learning environments.',
    '3.7': '3.7 An education in law might involve active engagement with the legal and wider community. Students may have opportunities to participate in legal projects within and/or outside the higher education provider in which they are studying, and will be made aware of relevant learned societies and/or professional bodies. These projects may include experiential or simulated activities such as clinical legal education, public legal education, outreach, academic research, professional placements and other suitable opportunities.',
    '3.8': '3.8 A provider’s assessment strategy will reflect the skills and understanding developed within the curriculum, constructively aligned to the methods of teaching and learning adopted by the particular course at both course and modular levels. This strategy will clearly and directly reflect the defined learning outcomes of the course components, support student learning and enable students to demonstrate progressive levels of attainment. In this way,\n\n11\nassessment as and for learning (as opposed to assessment merely of learning) will be promoted and developed.',
    '3.9': '3.9 The assessment of Law courses will include a mix of methods that are accessible to all students. Providers can ensure transparency of inclusive and authentic assessment strategies to avoid disadvantage. Where individual students may be disadvantaged by particular assessment methods, adjustments to those assessments will be considered in discussion with the student concerned, while ensuring fairness across the full cohort.',
    '3.10': '3.10 Law students will encounter a range of assessment methods during their course. There will be differentiation between assessment that identifies a wide range of diverse learner needs and assessment that focuses on subsequent academic performance. Providers will design assessments to ensure that the overall assessment burden is considered, including the impact on wellbeing and accessibility.',
    '3.12': '3.12 Feedback will be given to students on both formative and summative work in a way that allows them to ‘feed forward’ and make changes to their learning practices with respect to future assessments. To develop feedback literacy and self-efficacy skills, providers may give opportunities for peer and self-assessment of their work, for example by engaging with marking criteria or providing exemplars of previous student work and the feedback given on\n\n12\nthat work. To ensure equality and inclusion with respect to diverse student cohorts, a variety of feedback methods could be used, such as written, audio, multimedia, screencast and ‘viva voce’ style formats.',
    '4.2': "4.2 The majority of students will perform significantly better than the minimum threshold standards articulated below. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be, and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.",
    '4.3.b15': 'develop employability skills and awareness of career opportunities, professional\n\n14\nrequirements and of the need for future planning',
}

HON = "bachelor's with honours"
CITE = 'QAA, 2023, Law Subject Benchmark Statement'

META = dict(
    run='0116', p1='2026-10-03 17:45',
    title='Subject Benchmark Statement Law',
    heading='Subject Benchmark Statement: Law (QAA, March 2023)',
    edition='March 2023 (fifth edition)', published='2023-03',
    status='current',
    supersedes='the fourth edition (2019), named in the advisory group list (D1, section 5)',
    subjects=[dict(scheme='hecos', code='100485', label='law', basis='stated'),
              dict(scheme='cah', code='CAH16-01-01', label='law', basis='stated'),
              dict(scheme='cah', code='CAH16-01', label='law', basis='stated')],
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2023 revision with cross-cutting themes (Law fifth edition, March 2023)',
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    agentDefinition=("This document records what the QAA's 2023 Law statement expects of an honours graduate in law and of the courses that lead "
                     "there. Read S4 for the standards: section 4 states one rung only, the threshold, in two lists (subject knowledge, understanding "
                     "and skills; generic skills and qualities of mind), and section 3 adds one outcome list of general skills graduates will be equipped "
                     "with. Every standard has a practitioner version, a student version and two instructions for AI agents who write about it or use "
                     "it in conversation. Performance above the threshold is left to Annex D of the 2024 Frameworks, which this document points to and never copies."),
    summary=("Law, bachelor's degree with honours (FHEQ level 6; FQHEIS level 10), fifth edition, March 2023. One rung is stated: the threshold, with "
             "16 subject items (4.3) and 16 generic items (4.4); no typical or excellent lists, the provider being sent to Annex D for higher classes "
             "(4.2). An outcome list in section 3 gives 12 general and widely applicable skills graduates will be equipped with (3.4). Nineteen paragraphs "
             "set requirements or expectations: knowledge of the legal system studied, legal understanding through substantive law, progression, joint "
             "routes, inclusion and access, flexible delivery, resources, assessment, feedback, professional routes and the use of Annex D. Themes: "
             "equality, diversity and inclusion; accessibility; sustainability (education for sustainable development); entrepreneurship and enterprise "
             "education with employability; artificial intelligence in legal services. Bodies: PSRBs, unnamed in the body of the text, govern routes to "
             "legal practice and accredit qualifying Law degrees; Advance HE's PSF is named for staff recognition; UNESCO for ESD."),
    authority='reference: a sector reference point, not a regulatory requirement; a key reference point in Wales and Scotland and part of the quality arrangements in Northern Ireland (D1, front matter)')

S2 = dict(
    governs="what a graduate in law is expected to know, do and understand at the end of an honours degree, and the nature of courses in the subject",
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    statedScope='"This document is a QAA Subject Benchmark Statement for Law that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies." (D1, front matter); 4.1 applies the standards in full only to courses with at least 50% Law',
    statedSubjects=[
        dict(name='Law', locator='(D1, title; 1.1)', kind='subject',
             codes=[dict(scheme='hecos', code='100485', label='law'), dict(scheme='cah', code='CAH16-01-01', label='law')]),
        dict(name='combined, joint or major-minor routes', locator='(D1, 2.3)', kind='programme title',
             codes=[dict(scheme='hecos', code='100485', label='law')]),
        dict(name="integrated master's degrees in Law (MLaw)", locator='(D1, 2.4)', kind='programme title',
             codes=[dict(scheme='hecos', code='100485', label='law')]),
        dict(name='Qualifying Law degrees', locator='(D1, 2.12)', kind='programme title',
             codes=[dict(scheme='hecos', code='100485', label='law')]),
    ])

SECTIONS = {'1': 'Context and purposes of a Law degree', '2': 'Distinctive features of a Law degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.5', 'Purposes and characteristics of a Law degree'), ('1.6', '1.8', 'Equality, diversity and inclusion'),
       ('1.9', '1.12', 'Accessibility'), ('1.13', '1.14', 'Sustainability'), ('1.15', '1.18', 'Entrepreneurship and enterprise education'),
       ('2.2', '2.5', 'Progression'), ('2.6', '2.7', 'Flexibility'), ('2.8', '2.8', 'Partnership'), ('2.9', '2.12', 'Monitoring and review'),
       ('3.1', '3.4', 'Content'), ('3.5', '3.7', 'Teaching and learning'), ('3.8', '3.12', 'Assessment and feedback'),
       ('4.3', '4.3', 'Threshold level: Subject knowledge, understanding and skills'), ('4.4', '4.4', 'Threshold level: Generic skills and qualities of mind')]

G = {
    '1.1': 'law as an academic study: knowledge, intellectual and subject skills, values and ethics',
    '1.2': 'the degree alone gives no right to practise; PSRB routes to qualification differ by nation',
    '1.3': 'methods from the humanities and social sciences; professional behaviours, well-being and citizenship',
    '1.4': 'national and global outlook; knowledge of the main features of the system or systems studied',
    '1.5': 'careers in and well beyond regulated legal practice',
    '1.6': 'law as authority and power; a critical approach to law and equality',
    '1.7': 'substantive equality and students seeing themselves in the curriculum',
    '1.8': 'the curriculum brings out how law meets equality, diversity and inclusion',
    '1.9': 'widening access, inclusive methods and reasonable adjustments',
    '1.10': 'the many dimensions of access, from digital literacy to extracurricular life',
    '1.11': 'disabled identities in law school and inclusive environments',
    '1.12': 'flexible assessment for varied student needs',
    '1.13': 'law and sustainable development; ESD, the SDGs and UNESCO competencies',
    '1.14': 'teaching and content can take up sustainability; the joint ESD guidance',
    '1.15': 'enterprise education for careers, placements and external links',
    '1.16': 'entrepreneurship education for a self-directed working life',
    '1.17': 'legal technology, a networked society and access to justice',
    '1.18': 'artificial intelligence, digital justice and the changing role of lawyers',
    '2.1': 'a critical, expansive study of law, justice and a changing society',
    '2.2': 'progression through the levels to the threshold; readiness for postgraduate study',
    '2.3': 'joint, combined and major-minor routes',
    '2.4': "integrated master's (MLaw) and other master's routes",
    '2.5': 'course length by nation, exit awards and part-time study',
    '2.6': 'whole-course design across delivery modes; practical learning; digital fluency',
    '2.7': 'technology for flexible routes and fair access',
    '2.8': 'partnerships with employers and social enterprises; law clinics and access to justice',
    '2.9': 'monitoring and periodic review against external reference points',
    '2.10': 'external reviewers in periodic review',
    '2.11': 'external examiners and threshold standards',
    '2.12': 'qualifying Law degrees, PSRB accreditation and clarity on professional routes',
    '3.1': 'the scope of legal study: rules, ethics, justice, the rule of law and other disciplines',
    '3.2': 'legal understanding built through substantive areas of law; no set subjects',
    '3.3': 'subject-specific skills: interpreting, finding and interrogating legal sources',
    '3.4': 'the general skills graduates will be equipped with',
    '3.5': 'teaching methods suited to the subject; themes built in; digital inclusivity',
    '3.6': 'teaching, research and practice; staff development; resources and training in sources',
    '3.7': 'engagement with the legal community; clinics, outreach and placements',
    '3.8': 'an assessment strategy aligned with teaching and outcomes',
    '3.9': 'accessible mixed assessment and adjustments agreed with the student',
    '3.10': 'a range of assessment; diagnostic and later assessment; overall burden',
    '3.11': 'indicative assessment practices, from dissertation to mooting and portfolios',
    '3.12': 'feedback that feeds forward; peer and self-assessment; varied formats',
    '4.1': 'the minimum threshold standards and where they apply in full',
    '4.2': 'most students exceed the threshold; Annex D for degree classes',
    '4.3': 'threshold: subject knowledge, understanding and skills',
    '4.4': 'threshold: generic skills and qualities of mind',
}

CTYPE = {'1.4': 'area', '3.1': 'area', '3.2': 'area', '3.3': 'area',
         '2.6': 'practice', '2.8': 'practice', '3.5': 'practice', '3.6': 'practice', '3.7': 'practice',
         '3.8': 'practice', '3.9': 'practice', '3.10': 'practice', '3.11': 'practice', '3.12': 'practice'}

EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='Contents', kind='other: contents list'),
    dict(number='1 to 4', heading='section heading lines', kind='other: headings, recorded in S3 as sections'),
    dict(number='5', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Law', kind='other: back matter, read for S8 (editions 2000, 2007, 2015, 2019, 2023)'),
]

P = {}
def s(i, **k):
    P[i] = k

# ---- obliging or outcome paragraphs (sections 1 to 4)
s('1.4', type='requirement', rung='none', force='must', level='fheq:6', appliesTo='Law courses and their students',
  addressee='both', verbs=['requires', 'considered'], about='knowledge of the legal system or systems studied', domain='knowledge', award=HON,
  para=("Law may be studied in one jurisdiction or several, with a national and a global outlook; whichever system or systems a course covers, the "
        "statement asks that students know its main features and principles. Coverage may take in relations among people, organisations and the state "
        "and the sources of law, and law's two-way link with ethical, social, political, environmental and economic norms may show in the curriculum."),
  prac=("Whatever jurisdiction or jurisdictions the course covers, make sure students gain knowledge of that system's main features and principles; the "
        "statement requires this. Consider covering relations between persons, bodies and the state, the sources of law and how law shapes and is shaped by wider norms."),
  ben=("Whichever legal system or systems your course covers, you must come to know their main features and principles, which may include how people, "
       "organisations and the state relate in law and where law comes from."),
  aaw=(f"Describe this as a requirement (requires, recorded as must) that students know the main features and principles of the legal system or systems "
       f"their course covers, at FHEQ level 6 for the honours degree. Cite {CITE}, para 1.4. Set it beside the threshold items 4.3.b11 and 4.3.b12 and the "
       f"level 6 descriptor qaa/fheq-2024/4.15.b1; do not claim it names a required jurisdiction or list of subjects, which para 3.2 rules out."),
  aad=("Raise this when a programme team asks whether a course must cover a particular jurisdiction, or a student studying several systems asks what they "
       "need to know. Tell staff the requirement is that students know the core features and principles of the system taught; tell a student plainly what "
       "that means for them. Ask which system the course centres on and where its sources of law are taught; avoid implying that any one jurisdiction is compulsory."))

s('1.8', type='expectation', rung='none', force='will', level='none', appliesTo='Law courses',
  addressee='provider', verbs=['highlighted', 'encourage'], about="law's interaction with equality, diversity and inclusion in the curriculum", domain='none', award='none',
  para=("Because law regulates equality, diversity and inclusion and is tied to justice and fairness, courses will bring out how law interacts with these "
        "issues; study may prompt reflection on law's history, politics and effects here, including what legal understanding can and cannot do against systemic injustice."),
  prac=("Bring the relationship between law and equality, diversity and inclusion to the fore in the curriculum, inviting students to reflect on the history, "
        "politics and effects of law in this area and on the reach and limits of legal tools for tackling systemic injustice."),
  ben=('n/a', 'a curriculum expectation on the course; the student meets it through what is taught'),
  aaw=(f"Describe this as a curriculum expectation (will) on Law courses under the equality, diversity and inclusion heading; it sets no level of its own. "
       f"Cite {CITE}, para 1.8, and read it with paras 1.6 and 1.7. Set it beside the student items 4.4.b13 and 4.4.b16; do not present it as a student "
       f"outcome or as a legal equality duty."),
  aad=("Raise this with a programme team reviewing where equality, diversity and inclusion appear in a Law curriculum. Frame it for staff as making law's "
       "part in equality and injustice visible in teaching. Ask which modules examine how law can entrench or challenge inequality; avoid handing this to a "
       "student as a requirement or reading the paragraph aloud."))

s('1.9', type='expectation', rung='none', force='will', level='none', appliesTo='providers of Law courses',
  addressee='provider', verbs=['demonstrate', 'anticipate', 'take'], about='widening access, inclusive methods and reasonable adjustments', domain='none', award='none',
  para=("Providers show commitment to widening access and inclusive participation so every Law student can thrive whatever their background or disability; "
        "they plan ahead for inclusive teaching, learning and assessment aimed at access for marginalised groups, and will carry duties for reasonable "
        "adjustments and proactive prevention."),
  prac=("Commit to widening access and inclusive participation, plan inclusive teaching, learning and assessment in advance with marginalised groups in mind, "
        "and meet your duties to make reasonable adjustments and to act preventively rather than only in response."),
  ben=('n/a', 'a duty on the provider; the student meets its effect in access and adjustments'),
  aaw=(f"Describe this as a provider duty (will) on access and inclusion in Law, under the accessibility heading; it carries no level. Cite {CITE}, para 1.9, "
       f"and set it beside paras 1.10 to 1.12, 2.6 and 3.9. Do not present it as a student outcome or as a restatement of statutory disability duties, which "
       f"the statement says it does not interpret."),
  aad=("Bring this into a programme team's discussion of widening participation, inclusive design or reasonable adjustments. Put it to staff as planning "
       "access in from the start rather than adding it later. Ask how the course anticipates the needs of disabled and marginalised students before they "
       "arrive; avoid putting this duty to a student."))

s('1.11', type='expectation', rung='none', force='should', level='none', appliesTo='Law courses and their staff',
  addressee='provider', verbs=['understood'], about='understanding disability in its many forms', domain='none', award='none',
  para=("To meet disabled students' needs, inclusive learning environments could be built; disability in the context of studying law takes many forms and "
        "identities and should be understood in all of them, since disabled Law students may see their identities remade several times during their studies."),
  prac=("Treat disability among Law students as many identities, not one, and understand it in all its forms; consider building inclusive learning "
        "environments, knowing that a disabled student's sense of identity may shift repeatedly through law school."),
  ben=('n/a', 'a duty on the course and its staff; the student meets its effect'),
  aaw=(f"Describe this as a provider expectation (should) on understanding disability in all its forms, with inclusive environments offered as one option "
       f"(could); it carries no level. Cite {CITE}, para 1.11. Set it beside paras 1.9, 1.12 and 3.11; do not present it as a student outcome or as a legal duty."),
  aad=("Raise this with staff designing support or teaching for disabled Law students. Frame it as recognising many disabled identities and the changes "
       "students may go through. Ask how the team learns what different disabled students need at different points; avoid placing this on a student or "
       "treating disability as one category."))

s('1.12', type='expectation', rung='none', force='describes', level='none', appliesTo='providers of Law courses',
  addressee='provider', verbs=['considered', 'meet', 'demonstrate'], about='flexible assessment for different students', domain='none', award='none',
  para="Providers need to consider flexible assessment methods so that different students' needs are met and learning can be shown in several ways.",
  prac="Consider flexibility in how students are assessed, so that varied needs are met and students can show their learning in more than one way.",
  ben=('n/a', 'a duty on the provider in designing assessment'),
  aaw=(f"Describe this as a provider expectation on flexible assessment, worded with need to (recorded as describes; Part E); it carries no level. Cite "
       f"{CITE}, para 1.12, and read it with paras 3.9 to 3.11. Do not strengthen it to a must, or present it as a student outcome."),
  aad=("Raise this when a programme team reviews its assessment mix for accessibility. Frame it for staff as offering more than one way to show the same "
       "learning. Ask which outcomes can currently be shown in only one format; avoid giving this duty to a student."))

s('2.2', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='Law students across the honours degree',
  addressee='learner', verbs=['progress', 'build', 'include'], about='progression across the levels towards the threshold', domain='none', award=HON,
  para=("Across an honours degree at FHEQ level 6 (FQHEIS level 10), students of Law will move from level to level under each institution's rules, with "
        "knowledge, skills, expertise and experience growing at each stage towards the threshold subject skills; this will usually mean completing and "
        "gaining credit for all learning and assessment, practical parts included. A graduate with a second-class degree or better would be expected to be "
        "ready for postgraduate study in Law or a related subject, though entry is for each provider to set."),
  prac=("Plan each level so that knowledge, skills and experience build steadily towards the threshold subject skills by the end of the honours degree, with "
        "credit awarded for all learning and assessment, including practical work. Expect students with a second-class degree or better to be equipped for "
        "postgraduate study, while postgraduate entry rules remain your own."),
  ben=("As you move through each year of your honours degree you will build knowledge, skills and experience towards the minimum the subject sets for "
       "graduation, usually by passing all your learning and assessment, including any practical parts. With a second-class degree or better you would "
       "normally be ready for postgraduate study, though each course sets its own entry rules."),
  aaw=(f"Describe this as an expectation (will) about progression through the honours degree at FHEQ level 6 (FQHEIS level 10), with readiness for "
       f"postgraduate study expected of second-class graduates. Cite {CITE}, para 2.2. Set it beside the threshold lists 4.3 and 4.4, the level 6 "
       f"descriptor qaa/fheq-2024/4.15.b9.3 and the step spine:6 in std:ref:uk-framework R8; do not claim it fixes postgraduate entry, which each provider decides."),
  aad=("Raise this when a student asks how each year builds to graduation or whether their degree will let them go on to a master's in Law. Say in plain "
       "words that each level builds towards the minimum set for graduation and that a second-class result or better usually signals readiness for "
       "postgraduate study. Ask what the student plans after graduating and which part of the course they find hardest to build on; avoid promising entry "
       "to any particular postgraduate course."))

s('2.3', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students on combined, joint or major-minor routes',
  addressee='learner', verbs=['achieve', 'add', 'explore'], about='joint, combined and major-minor routes', domain='none', award=HON,
  para=("Students on combined, joint or major-minor routes will reach the core of the subject's specific and generic skills and add others as their joint "
        "course requires; they may also study where their two subjects overlap."),
  prac=("On joint, combined or major-minor routes, make sure students will reach the core subject-specific and generic Law skills, add the rest the partner "
        "subject requires and, where useful, offer interdisciplinary study of the overlap."),
  ben=("If you study Law with another subject, you will gain the core Law skills, both specific and general, and add others your joint course asks for; "
       "you may also explore where your two subjects meet."),
  aaw=(f"Describe this as an expected outcome (will) for students on combined, joint or major-minor routes at FHEQ level 6: they reach core elements, not "
       f"every item, of the Law skills. Cite {CITE}, para 2.3, and read it with para 4.1, which applies the standards in full only where Law is at least half "
       f"the course. Do not claim that joint honours students must meet every item in 4.3 and 4.4."),
  aad=("Raise this when a joint honours student or programme team asks how much of the Law standards applies to a combined route. Explain that the core Law "
       "skills are expected and the rest depends on the joint course. Ask which Law skills the route covers in full and where the partner subject adds its "
       "own; avoid presenting the full threshold lists as binding on every joint route."))

s('2.6', type='expectation', rung='none', force='will', level='none', appliesTo='providers of Law courses',
  addressee='provider', verbs=['consider', 'ensure', 'widen', 'used', 'build'], about='flexible, inclusive delivery and digital fluency', domain='none', award='none',
  para=("Providers will look at a Law course's learning, teaching and assessment as a whole so that it offers creative learning across online, blended or "
        "in-person delivery, widens access and lets every student reach their potential in an inclusive, supportive setting; practical learning such as "
        "clinics, placements and mentoring can be considered in any mode, and digital tools will be used where suitable to build students' digital "
        "confidence and fluency, including knowing which technology suits a task."),
  prac=("Design learning, teaching and assessment as a whole so the course works creatively across online, blended and face-to-face delivery, widens access "
        "and supports every student inclusively. Consider practical learning, such as clinical legal education, placements and mentoring, in any mode, and "
        "use digital tools where suitable to build students' digital confidence and fluency grounded in the discipline's values."),
  ben=('n/a', 'a duty on the provider in designing delivery; the student meets its effect'),
  aaw=(f"Describe this as a provider expectation (will) on flexible, inclusive delivery and the growth of digital fluency, under the flexibility heading; it "
       f"sets no level. Cite {CITE}, para 2.6. Set it beside para 2.7 and the student items 3.4.b6, 4.3.b13 and 4.4.b9; do not present it as a requirement "
       f"to teach online or as a student outcome."),
  aad=("Raise this with a programme team planning delivery modes, clinical or placement learning, or digital skills. Frame it for staff as designing the "
       "whole course for access and digital fluency, not module by module. Ask where students meet practical legal work and how digital tools build their "
       "confidence; avoid passing the design duty to a student."))

s('2.7', type='expectation', rung='none', force='will', level='none', appliesTo='providers of Law courses',
  addressee='provider', verbs=['seek', 'harness', 'facilitate'], about='technology for flexible, accessible routes', domain='none', award='none',
  para=("Providers will try to use different technologies for flexible delivery that supports learning in accessible, meaningful and effective ways, opening "
        "fair access to knowledge exchange and skills, for instance through work-based, theoretical, skills-focused or graduate-entry routes."),
  prac=("Look for technological means of flexible delivery that make learning accessible and meaningful, and consider offering varied routes, such as "
        "work-based, theoretical, skills-focused or graduate-entry courses, that widen fair access."),
  ben=('n/a', 'a duty on the provider in planning routes and delivery'),
  aaw=(f"Describe this as a provider expectation (will seek) on using technology for flexible and accessible routes; it carries no level. Cite {CITE}, "
       f"para 2.7, and read it with para 2.6. Do not claim it requires any particular route or technology; the routes named are examples."),
  aad=("Raise this when a programme team considers new routes into Law study, such as work-based or graduate-entry courses, or new delivery technology. "
       "Frame it as widening fair access through flexible design. Ask which learners the current routes leave out; avoid presenting the examples as required."))

s('2.12', type='requirement', rung='none', force='should', level='none', appliesTo='institutions offering qualifying Law degrees',
  addressee='provider', verbs=['require'], about='qualifying Law degrees and routes to professional qualification', domain='none', award=HON,
  para=("Qualifying Law degrees with professional and vocational outcomes will also need assessment and accreditation by the relevant PSRBs, and "
        "institutions should tell prospective and current students plainly which routes to professional qualification their courses offer."),
  prac=("Where the course is a qualifying Law degree, secure the relevant PSRB accreditation, and be clear with applicants and current students about which "
        "professional qualification routes the course does and does not open."),
  ben=('n/a', 'a duty on the institution to inform students; the student is its audience, not its subject'),
  aaw=(f"Describe this as a provider expectation (should) to be clear with students about routes to professional qualification, alongside the statement "
       f"that qualifying degrees also need PSRB accreditation (will); it carries no level. Cite {CITE}, para 2.12, and read it with paras 1.2 and 3.2. Do not "
       f"claim the statement itself confers or regulates professional qualification; the accreditation rules are the PSRBs' own (SB5)."),
  aad=("Raise this when a student asks whether their Law degree leads to practice as a solicitor, barrister or advocate, or a team prepares course "
       "information. To staff, frame it as a duty to be explicit about routes; to a student, explain that the degree alone does not entitle them to practise "
       "and point them to the course's stated route. Ask what the course information says about professional routes; avoid giving regulatory advice on qualification."))

s('3.2', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='Law courses and their students',
  addressee='both', verbs=['include', 'demonstrate', 'develop'], about='legal understanding through substantive law; awareness of PSRB requirements', domain='understanding', award=HON,
  para=("Law degrees give chances to build legal understanding: knowing, comprehending, questioning and applying the theories, concepts, values, rules and "
        "principles of public and private law across many contexts, recognising ambiguity and handling uncertainty, reaching evidenced conclusions on real "
        "or hypothetical problems, synthesising doctrine, policy and context, choosing reasoned solutions and judging arguments critically. No set subjects "
        "are required, but legal study is expected to engage in detail with substantive areas of law; courses may differ in content and jurisdiction, and "
        "providers designing a route into practice will know the relevant PSRB requirements."),
  prac=("Give students the means to build legal understanding through detailed work on substantive areas of law of your choosing: questioning and applying "
        "the doctrine and theory of public and private law in varied contexts, handling ambiguity and uncertainty, reaching evidenced conclusions and weighing "
        "arguments. If the course is meant as a route into practice, take account of the relevant PSRB requirements."),
  ben=("Your course will help you build legal understanding by working in detail on real areas of law: you learn to question and apply legal ideas and rules "
       "in different settings, cope with uncertainty, reach conclusions backed by evidence and judge arguments. No particular law subjects are compulsory for this."),
  aaw=(f"Describe this as an expectation (will, is expected) that Law courses develop legal understanding through detailed engagement with substantive law, "
       f"at FHEQ level 6, with no prescribed subjects. Cite {CITE}, para 3.2. Set it beside the threshold items 4.3.b3, 4.3.b5, 4.3.b10 and 4.3.b11 and the "
       f"level 6 descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b4; do not claim it lists compulsory subjects or that PSRB requirements are part of the statement."),
  aad=("Raise this when a team debates which areas of law a course must teach, or a student asks why the degree is built around particular subjects. Explain "
       "that understanding grows through depth in substantive law, whichever areas are chosen. Ask which modules give the deepest engagement with doctrine, "
       "policy and context, and where students practise reaching evidenced conclusions; avoid suggesting any subject is required by the statement."))

s('3.5', type='expectation', rung='none', force='will', level='none', appliesTo='providers of Law courses',
  addressee='provider', verbs=['reflect', 'designed', 'embrace', 'ensure'], about='inclusive, sustainable and accessible teaching; digital inclusivity', domain='none', award='none',
  para=("Each provider's teaching and learning environment will reflect its own approach to legal study, with methods suited to the subject, the outcomes and "
        "learners' needs; innovation could shape the curriculum. Methods will take in sustainability, inclusion, diversity and accessibility, may mix live and "
        "recorded, technology-enhanced and in-person teaching, and providers will secure digital inclusivity as far as they can, such as fair access to Wi-Fi and devices."),
  prac=("Choose teaching and learning methods that fit the material, the intended outcomes and your learners, and build in sustainability, inclusion, diversity "
        "and accessibility. Mix synchronous, asynchronous, technology-enhanced and classroom teaching as suits, and do what you can to secure equal digital "
        "access, such as Wi-Fi and equipment."),
  ben=('n/a', 'a duty on the provider in designing teaching'),
  aaw=(f"Describe this as a provider expectation (will) on teaching methods that embrace sustainability, inclusion, diversity and accessibility and on digital "
       f"inclusivity; it carries no level. Cite {CITE}, para 3.5. Set it beside paras 2.6 and 3.6; do not claim it prescribes any method, which the "
       f"statement says it does not."),
  aad=("Raise this when a team reviews its teaching methods or digital access for students. Frame it for staff as aligning methods with content, outcomes "
       "and learner needs while building in the cross-cutting themes. Ask how the team knows every student has the equipment and connection they need; avoid "
       "assigning this to a student."))

s('3.6', type='expectation', rung='none', force='will', level='none', appliesTo='providers of Law courses',
  addressee='provider', verbs=['given', 'taught', 'have', 'trained', 'supported'], about='staff development, learning resources and training in legal sources', domain='none', award='none',
  para=("Teaching, research and professional practice interact in the Law learning environment. Staff will be given development opportunities and may hold "
        "or work towards a teaching qualification or recognition such as Advance HE's PSF. Students learn in a stimulating setting that welcomes intellectual "
        "and neurological diversity; they will have access to legal and academic sources, literature, databases, software and computing, will be trained to "
        "find and use legal sources, and will be supported to use these resources well, alone and in groups."),
  prac=("Give staff development opportunities and support towards a teaching qualification or recognition such as the PSF. Make sure students can reach legal "
        "and academic sources, databases, software and computing, train them to identify, retrieve and use legal sources, and support them to use these "
        "resources in group and individual work."),
  ben=('n/a', 'a duty on the provider for staff and resources; the student meets its effect'),
  aaw=(f"Describe this as a provider expectation (will) on staff development and on students' access to, and training in, legal sources and digital "
       f"resources; it carries no level. Cite {CITE}, para 3.6. Set it beside the student items 4.3.b1, 3.4.b6 and 4.3.b13; mention the PSF "
       f"(std:doc:advancehe-psf-dimensions-2023-framework) only as the statement's example of staff recognition, not as a requirement."),
  aad=("Raise this when a team reviews library, database and digital provision, or staff development for Law teaching. Frame it for staff as the resources "
       "and training students need to work with legal sources. Ask how and when students are trained to find and use primary legal materials; avoid putting "
       "a provider's resourcing duty to a student."))

s('3.7', type='expectation', rung='none', force='will', level='none', appliesTo='providers of Law courses',
  addressee='provider', verbs=['made', 'participate', 'involve'], about='engagement with the legal community; awareness of professional bodies', domain='none', award='none',
  para=("Legal education might engage actively with the legal and wider community; students may join legal projects inside or outside their provider, such "
        "as clinics, public legal education, outreach, research or placements, and will be told about relevant learned societies or professional bodies."),
  prac=("Consider giving students chances to take part in legal projects within or beyond the institution, such as clinical or public legal education, "
        "outreach, research or placements, and make sure they are told about the learned societies and professional bodies relevant to them."),
  ben=('n/a', 'a duty on the provider to inform students and offer opportunities'),
  aaw=(f"Describe this as a provider expectation (will) that students are made aware of relevant learned societies or professional bodies, beside optional "
       f"engagement with the legal community (might, may); it carries no level. Cite {CITE}, para 3.7. Set it beside para 2.8 and the student item "
       f"4.3.b15; do not present clinics or placements as required."),
  aad=("Raise this when a student asks about law clinics, pro bono or placements, or a team plans community engagement. To staff, frame the one firm "
       "expectation as telling students about relevant societies and bodies; to a student, describe the kinds of projects that may be on offer. Ask which "
       "bodies students currently hear about and when; avoid suggesting every course must run a clinic."))

s('3.8', type='expectation', rung='none', force='will', level='none', appliesTo='providers of Law courses',
  addressee='provider', verbs=['reflect', 'support', 'enable', 'promoted', 'developed'], about='an aligned assessment strategy', domain='none', award='none',
  para=("A provider's assessment strategy will mirror the skills and understanding the curriculum builds, aligned with the course's teaching and learning at "
        "course and module level; it will follow the stated learning outcomes, support learning and let students show progressing attainment, so that "
        "assessment for and as learning is fostered."),
  prac=("Set an assessment strategy aligned with teaching and learning at course and module level, tied directly to the learning outcomes, supporting "
        "learning and letting students show attainment that grows over the course, so that assessment serves learning, not only measurement."),
  ben=('n/a', 'a duty on the provider in setting assessment strategy'),
  aaw=(f"Describe this as a provider expectation (will) for a constructively aligned assessment strategy; it carries no level of its own. Cite {CITE}, "
       f"para 3.8. Set it beside paras 3.9 to 3.12 and the progression expectation in para 2.2; do not present it as a student outcome."),
  aad=("Raise this when a team reviews its assessment strategy or module outcomes. Frame it for staff as tying each assessment to outcomes and to progression "
       "across levels. Ask which assessments also teach, not only measure; avoid placing this duty on a student."))

s('3.9', type='expectation', rung='none', force='will', level='none', appliesTo='providers of Law courses',
  addressee='provider', verbs=['include', 'ensure', 'avoid', 'considered'], about='accessible assessment and adjustments', domain='none', award='none',
  para=("Law assessment will use a mix of methods accessible to every student; providers can make inclusive, authentic strategies transparent to prevent "
        "disadvantage, and where a method disadvantages a student, adjustments will be considered with that student, keeping the whole cohort fair."),
  prac=("Use a mix of assessment methods that all students can access, be open about inclusive and authentic strategies, and where a method disadvantages an "
        "individual, consider adjustments with that student while keeping fairness for the cohort."),
  ben=('n/a', 'a duty on the provider; the student takes part in discussing adjustments but does not carry the duty'),
  aaw=(f"Describe this as a provider expectation (will) for accessible, mixed assessment and for adjustments agreed with the student; it carries no level. "
       f"Cite {CITE}, para 3.9. Set it beside paras 1.9, 1.12 and 3.11; do not present it as a statutory duty or as a student outcome."),
  aad=("Raise this when a student says an assessment format disadvantages them, or a team reviews its assessment mix. To a student, explain that "
       "adjustments can be discussed with them; to staff, frame it as accessible design first and adjustments second. Ask what about the format causes the "
       "difficulty; avoid promising a particular adjustment."))

s('3.10', type='expectation', rung='none', force='will', level='none', appliesTo='providers of Law courses',
  addressee='provider', verbs=['encounter', 'design', 'considered'], about='a range of assessment and the overall burden', domain='none', award='none',
  para=("Law students will meet a range of assessment methods; assessment that identifies diverse learner needs will be told apart from assessment of later "
        "academic performance, and providers will design assessment with the overall load, wellbeing and accessibility in mind."),
  prac=("Give students a range of assessment methods, distinguish assessment that identifies learners' needs from assessment of their later performance, and "
        "design the whole assessment load with wellbeing and accessibility in view."),
  ben=('n/a', 'a duty on the provider in designing assessment'),
  aaw=(f"Describe this as a provider expectation (will) on varied assessment and the overall assessment burden; it carries no level. Cite {CITE}, para 3.10, "
       f"and read it with paras 3.9 and 3.11. Do not present it as a student outcome or as setting a limit on assessment volume."),
  aad=("Raise this when a team maps assessment deadlines and loads across a year or a student reports overload. Frame it for staff as weighing the whole "
       "burden and its effect on wellbeing. Ask where assessments cluster and which ones diagnose needs rather than grade; avoid giving this duty to a student."))

s('3.12', type='expectation', rung='none', force='will', level='none', appliesTo='providers of Law courses',
  addressee='provider', verbs=['given', 'feed', 'make', 'develop', 'used'], about='feedback that feeds forward', domain='none', award='none',
  para=("Students will receive feedback on formative and summative work that lets them carry it forward into later assessments; providers may build "
        "feedback literacy and self-efficacy through peer and self-assessment, marking criteria and exemplars, and could use varied feedback formats for "
        "equality and inclusion."),
  prac=("Give feedback on formative and summative work that students can act on in later assessments; consider peer and self-assessment, work with marking "
        "criteria and exemplars to build feedback literacy, and vary feedback formats, written, audio, screencast or oral, for inclusion."),
  ben=('n/a', 'a duty on the provider to give feedback; the student uses it (see 4.4.b15)'),
  aaw=(f"Describe this as a provider expectation (will) that feedback on formative and summative work helps students feed forward; the peer, "
       f"self-assessment and format suggestions are permissive (may, could). Cite {CITE}, para 3.12. Set it beside the student items 3.4.b7 and 4.4.b15 "
       f"and the Annex D row on managing learning, qaa/fheq-2024/annex-d/transferable/r3/3rd; do not claim it requires any particular feedback format."),
  aad=("Raise this when a student says feedback does not help them, or a team reviews feedback practice. To staff, frame it as feedback designed to be used "
       "next time; to a student, ask how they used their last feedback. Ask which feedback the student found most usable and why; avoid reading the format "
       "list aloud or treating suggestions as requirements."))

s('4.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='higher education providers awarding honours degrees in Law',
  addressee='provider', verbs=['perform', 'refer'], about='performance above the threshold: Annex D', domain='none', award=HON,
  para=("Most students will do considerably better than the minimum; each provider decides what evidence shows this and should refer to Annex D, which "
        "describes the four honours classes (1st, 2.1, 2.2, 3rd) at FHEQ level 6 and FQHEIS level 10."),
  prac=("Above the threshold, judge achievement by your own method and refer to Annex D's descriptions of the four honours classes; this statement gives no "
        "typical or excellent lists of its own."),
  ben=('n/a', 'a duty on the awarding body for judging classes above the threshold'),
  aaw=(f"Describe this as a provider expectation (should) to refer to Annex D when judging performance above the threshold at FHEQ level 6 and FQHEIS "
       f"level 10. Cite {CITE}, para 4.2, and point to std:doc:qaa-fheq-2024-framework, Annex D (SL6), for example qaa/fheq-2024/annex-d/summary/r1/3rd. "
       f"Do not claim the statement sets subject-specific typical or excellent standards; it states the threshold only."),
  aad=("Raise this when a team or student asks what separates a first from a third in Law. To staff, say the statement stops at the threshold and points "
       "to Annex D for the classes; to a student, explain that most people do much better than the minimum. Ask which Annex D descriptions the team's "
       "marking criteria follow; avoid presenting the threshold as the expected result."))

# ---- 3.4 general skills (lead-in: Law graduates will be equipped with the following general and widely applicable skills)
AAW34 = ("Describe this as an expected generic skill (will) that Law graduates are equipped with at FHEQ level 6 (FQHEIS level 10): {about}; it refines "
         "the descriptor {fw}. Cite " + CITE + ", para 3.4 (bullet {k}). Set it beside {nb}; do not report it as a threshold item, which section 4 holds, "
         "or as a standard at another level.")
AAD34 = ("Raise this when {when}. To a student, say plainly and in the second person that the degree will equip them with this skill and where it shows; "
         "to staff, frame it as a transferable outcome to evidence across modules. Ask {q} Avoid reading the issuer's bullet aloud or treating it as a pass requirement.")
def k34(k, verbs, about, para, prac, ben, nb, fw, when, q):
    P['3.4.b%d' % k] = dict(type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates in Law',
                            addressee='learner', verbs=verbs, about=about, domain='generic-skill', award=HON, para=para, prac=prac, ben=ben,
                            aaw=AAW34.format(about=about, k=k, nb=nb, fw=fw), aad=AAD34.format(when=when, q=q))

k34(1, ['ask', 'answer', 'identify', 'acquire', 'engage'], 'intellectual independence and critical enquiry',
    "Think independently: pose and answer sharp questions, spot and fill gaps in what they know, and analyse and evaluate critically.",
    "Graduates will be equipped to think for themselves: to frame and answer pointed questions, notice and close gaps in their knowledge, and analyse and evaluate critically.",
    "You will be able to think for yourself: ask and answer sharp questions, spot what you do not yet know and learn it, and analyse and evaluate critically.",
    '4.4.b2 and 4.4.b10', 'qaa/fheq-2024/4.15.b7', 'a student asks what independent thinking looks like in a Law degree',
    'what gap in their knowledge the student found most recently and how they filled it?')
k34(2, ['solving'], 'problem solving and adaptability',
    "Solve problems and adapt to change.",
    "Graduates will be equipped to solve problems and to adapt when circumstances change.",
    "You will be able to solve problems and adapt when things change.",
    '4.3.b14 and 4.4.b5', 'qaa/fheq-2024/4.15.b9.2', 'a student meets an unfamiliar legal problem or a change of plan',
    'how the student responded the last time a problem did not fit the method they knew?')
k34(3, ['conducting'], 'independent research and use of information',
    "Carry out independent research well: identify the issues accurately, find, retrieve and evaluate accurate, current and relevant information from many suitable sources, and apply it properly.",
    "Graduates will be equipped to research on their own: to pin down the issues, locate and judge reliable, up-to-date information from varied sources and use it appropriately.",
    "You will be able to research independently: pin down the issue, find and judge reliable, up-to-date information from a wide range of sources and use it well.",
    '4.3.b1, 4.3.b9 and 4.4.b10', 'qaa/fheq-2024/4.15.b5', 'a student begins a research essay or dissertation',
    'how the student decides whether a source is current and authoritative?')
k34(4, ['work'], 'working with textual, numerical and statistical data',
    "Work with varied data, whether textual, numerical or statistical.",
    "Graduates will be equipped to handle textual, numerical and statistical data.",
    "You will be able to work with different kinds of data, such as text, numbers and statistics.",
    '4.4.b8', 'qaa/fheq-2024/4.15.b6', 'a student meets empirical or statistical material in legal research',
    'which kind of data the student is least comfortable with?')
k34(5, ['responding'], 'clear communication responsive to other views',
    "Communicate clearly, effectively and precisely, in speech or other forms, responding fittingly and with sensitivity to differing views and arguments.",
    "Graduates will be equipped to communicate precisely and effectively, verbally or otherwise, and to respond with care to positions they may not share.",
    "You will be able to communicate clearly and precisely, in speech or other ways, and respond with care to views different from your own.",
    '4.3.b8, 4.4.b6 and 4.4.b7', 'qaa/fheq-2024/4.15.b8', 'a student prepares a moot, presentation or debate',
    'how the student would answer an argument they disagree with?')
k34(6, ['finding', 'managing', 'creating', 'communicating'], 'digital literacy with information',
    "Use digital skills to find, organise, create and share information.",
    "Graduates will be equipped with digital literacy for locating, organising, producing and sharing information.",
    "You will be able to use digital tools to find, organise, create and share information.",
    '4.3.b13 and 4.4.b9', 'qaa/fheq-2024/4.15.b5', 'a student uses legal databases or digital tools',
    'which digital tools the student relies on to manage sources?')
k34(7, ['reflect', 'make', 'listen', 'acknowledge', 'correct'], 'self-management and use of feedback',
    "Manage themselves: reflect on their learning, use feedback well, take advice and own and fix their mistakes.",
    "Graduates will be equipped to manage their own learning, reflecting on it, acting on feedback and advice, and admitting and correcting errors.",
    "You will be able to manage your own learning: reflect on it, act on feedback and advice, and own and correct your mistakes.",
    '4.4.b12 and 4.4.b15', 'qaa/fheq-2024/4.15.b5', 'a student receives feedback or makes a mistake in an assessment',
    'what the student changed after their last piece of feedback?')
k34(8, ['work'], 'collaborative work',
    "Be willing and able to work with others.",
    "Graduates will be equipped and willing to collaborate.",
    "You will be willing and able to work well with others.",
    '4.4.b11', 'qaa/fheq-2024/4.15.b9.1', 'group work begins',
    'what the student contributed to their last group task?')
k34(9, [], 'personal and professional development and academic integrity',
    "Engage with their own personal and professional growth, academic integrity included.",
    "Graduates will be equipped to take charge of their personal and professional development, including acting with academic integrity.",
    "You will be able to take charge of your own personal and professional growth, including working with academic integrity.",
    '4.4.b12 and 4.3.b15', 'qaa/fheq-2024/4.15.b9.3', 'a student plans their development or asks about academic integrity',
    'what professional development step the student is planning next?')
k34(10, ['arise', 'make', 'resolve'], 'resolving ethical conflicts',
    "Understand ethical conflicts that may come up and how to settle them through reasoned, balanced judgement.",
    "Graduates will be equipped to recognise ethical conflicts and resolve them by weighed, reasoned judgement.",
    "You will be able to recognise ethical conflicts when they arise and resolve them through careful, balanced reasoning.",
    '4.4.b13 and para 1.1', 'qaa/fheq-2024/4.15.b9.2', 'a case study or placement raises an ethical dilemma',
    'how the student would weigh two duties that pull in different directions?')
k34(11, [], 'integrity and ethical awareness in decisions',
    "Develop personal integrity and awareness of the ethical effects decisions may have.",
    "Graduates will be equipped with personal integrity and an awareness of what their decisions may mean ethically.",
    "You will develop personal integrity and an awareness of the ethical effects your decisions can have.",
    '4.4.b13 and 3.4.b10', 'qaa/fheq-2024/4.15.b9.2', 'a discussion turns to professional ethics or conduct',
    'what decision the student has made where ethics weighed on the outcome?')
k34(12, ['enhance'], 'professional reflection',
    "Develop professional reflective capacity to improve their own practice.",
    "Graduates will be equipped with professional reflective skills to improve their own practice.",
    "You will develop the habit of professional reflection to improve how you work.",
    '4.4.b12', 'qaa/fheq-2024/4.15.b9.3', 'a student writes a reflective account or returns from a placement',
    'what the student would do differently next time and why?')

# ---- 4.3 threshold: subject knowledge, understanding and skills (lead-in: on graduating with an honours degree in Law, students should be able to)
AAW43 = ("Describe this as a threshold standard: every honours graduate in Law should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); "
         "it covers {about}. Cite " + CITE + ", para 4.3 (bullet {k}). Set it beside {nb}, the descriptor {fw} and the third-class column of Annex D ({ad}); "
         "do not claim it is a regulatory rule, the typical result or a standard at another level.")
AAD43 = ("Raise this when {when}. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, frame "
         "it as a threshold their assessments must let every student show. Ask {q} Avoid reading the list aloud or treating this minimum as the class of "
         "degree most students reach.")
def k43(k, verbs, about, domain, para, prac, ben, nb, fw, ad, when, q, find=None):
    r = dict(type='threshold', rung='threshold', force='should', level='fheq:6', appliesTo='honours graduates in Law',
             addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben,
             aaw=AAW43.format(about=about, k=k, nb=nb, fw=fw, ad=ad), aad=AAD43.format(when=when, q=q))
    if find:
        r['find'] = find
    P['4.3.b%d' % k] = r

KN, UN, SK, GS = 'knowledge', 'understanding', 'subject-skill', 'generic-skill'
AD = 'qaa/fheq-2024/annex-d/'
ADK = [AD + 'knowledge/r%d/3rd' % i for i in (0, 1, 2, 3)]
ADC = [AD + 'cognitive/r%d/3rd' % i for i in (0, 1, 2, 3, 4)]
ADP = [AD + 'practical/r%d/3rd' % i for i in (0, 1, 2, 3, 4)]
ADT = [AD + 'transferable/r%d/3rd' % i for i in (0, 1, 2, 3, 4, 5)]

k43(1, ['identify', 'locate', 'retrieve'], 'finding standard legal materials', SK,
    "Find and obtain standard legal materials for the relevant jurisdictions, in print and online.",
    "At threshold, graduates find, locate and retrieve standard legal materials in print and electronic form for the jurisdictions they study.",
    "By graduation you should be able to find and obtain the standard legal materials for the jurisdictions you study, in print and online.",
    '3.4.b3 and para 3.6', 'qaa/fheq-2024/4.15.b5', ADP[1], 'a student starts research on an unfamiliar area of law',
    'where the student would look first for a statute or case and why?')
k43(2, ['synthesise', 'appreciate', 'achieve'], 'synthesising primary and secondary legal sources', SK,
    "Bring together information from several primary and secondary legal sources, judge their relative weight and so gain knowledge and understanding of complex legal issues.",
    "At threshold, graduates combine primary and secondary legal sources, weigh their relative value and reach an understanding of complex legal issues.",
    "By graduation you should be able to combine information from primary and secondary legal sources, judge how much weight each carries and use them to understand complex legal issues.",
    '4.4.b4 and 4.3.b7', 'qaa/fheq-2024/4.15.b1', ADC[1], 'a student writes an essay drawing on cases, statutes and commentary',
    'how the student decides which source carries most authority?')
k43(3, ['apply', 'draw'], 'applying law to problem scenarios', SK,
    "Apply legal knowledge to problem scenarios and reach reasoned conclusions backed by legal authority.",
    "At threshold, graduates use their legal knowledge on problem questions and reach conclusions reasoned from legal authority.",
    "By graduation you should be able to use your legal knowledge on problem questions and reach conclusions you can support with legal authority.",
    '4.4.b5 and para 3.2', 'qaa/fheq-2024/4.15.b3.1', ADC[3], 'a student prepares for problem questions or a moot',
    'what authority the student would rely on for their conclusion?')
k43(4, ['identify'], 'possible outcomes grounded in authority and research', SK,
    "Set out several possible outcomes to a problem, grounded in legal authority and drawing on current research and advanced scholarship.",
    "At threshold, graduates map out several possible outcomes to a problem, each grounded in authority and drawing on current research and scholarship.",
    "By graduation you should be able to set out several possible outcomes to a legal problem, each backed by authority and by current research and scholarship.",
    '4.3.b3 and 4.3.b5', 'qaa/fheq-2024/4.15.b3.2', ADC[2], 'a student gives only one answer to a problem question',
    'what other outcome a court might reach and on what authority?')
k43(5, ['make'], 'judging arguments and choosing solutions', SK,
    "Judge critically how strong particular arguments are and choose between alternative solutions with reasons.",
    "At threshold, graduates critically weigh the merits of arguments and choose, with reasons, between competing solutions.",
    "By graduation you should be able to judge critically how strong an argument is and choose between different solutions, giving your reasons.",
    '4.4.b10 and para 3.2', 'qaa/fheq-2024/4.15.b7', ADC[2], 'a student must decide between competing arguments in an essay',
    'which argument the student finds weakest and why?')
k43(6, ['demonstrate'], 'legal citation and reasoning', SK,
    "Show suitable legal citation and reasoning in written work and communication.",
    "At threshold, graduates cite legal authority correctly and reason soundly in writing and other communication.",
    "By graduation you should be able to cite legal sources correctly and reason clearly in your writing and other work.",
    '4.4.b7 and 3.4.b5', 'qaa/fheq-2024/4.15.b8', ADT[1], 'a student asks about referencing cases and statutes or loses marks for citation',
    'which citation convention the student uses and where they check it?')
k43(7, ['analyse', 'evaluate', 'interpret'], 'the primary sources of law', SK,
    "Analyse, evaluate and interpret the primary materials of law, such as statutes, law reports, treaties and directives.",
    "At threshold, graduates analyse, assess and interpret statutes, law reports, treaties, directives and other primary legal materials.",
    "By graduation you should be able to analyse, assess and interpret primary legal materials such as statutes, law reports, treaties and directives.",
    '4.3.b2 and 4.3.b1', 'qaa/fheq-2024/4.15.b2', ADK[2], 'a student reads a statute or judgment closely for the first time',
    'how the student would explain what a section or judgment decides?')
k43(8, ['understand', 'use', 'convey', 'explain'], 'legal terminology', SK,
    "Understand and use legal terminology, in speech, other forms and writing, to put across and explain technical legal information.",
    "At threshold, graduates understand legal terms and use them, orally, in writing and in other forms, to convey technical legal points.",
    "By graduation you should be able to understand legal terms and use them in speech and writing to explain technical legal points.",
    '4.4.b6 and 3.4.b5', 'qaa/fheq-2024/4.15.b8', ADK[1], 'a student struggles with legal vocabulary or must explain law to a non-lawyer',
    'how the student would explain a technical term to a client?')
k43(9, ['demonstrate'], 'legal research techniques, including from other disciplines', SK,
    "Show a range of legal research techniques, drawing where suitable on methods from other humanities and social science disciplines.",
    "At threshold, graduates use several techniques of legal research, including, where it fits, methods borrowed from the humanities and social sciences.",
    "By graduation you should be able to use several legal research techniques, including methods from other humanities and social science subjects where they help.",
    '3.4.b3 and para 3.3', 'qaa/fheq-2024/4.15.b6', ADK[3], 'a student plans a dissertation or research project',
    "which research method suits the student's question, doctrinal or empirical?")
k43(10, ['exhibit'], 'uncertainty and the limits of knowledge in law', UN,
    "Show some awareness of the uncertainties, ambiguities and limits of knowledge built into law and how they affect understanding and applying it.",
    "At threshold, graduates show some awareness that law carries uncertainty, ambiguity and limits to knowledge, and how these shape its understanding and use.",
    "By graduation you should be able to show some awareness that law is often uncertain or ambiguous, and how that affects how it is understood and applied.",
    'para 3.2 and 4.3.b4', 'qaa/fheq-2024/4.15.b4', ADK[2], 'a student is frustrated that a legal question has no single answer',
    'where the student has seen the law left genuinely unsettled?')
k43(11, ['show'], 'the contexts of law', UN,
    "Show understanding of law in its many settings, from the individual to the global, and in its institutional, normative, economic, political, social, cultural, historical, ethical, ecological, technological and philosophical dimensions.",
    "At threshold, graduates show they understand law across settings from local to global and across its wider dimensions, such as social, economic, ethical and ecological.",
    "By graduation you should be able to show that you understand law in settings from the personal to the global and in its wider dimensions, such as social, economic, ethical and environmental.",
    'para 1.4 and para 3.2', 'qaa/fheq-2024/4.15.b1', ADK[2], 'a student treats law as rules alone, apart from society',
    'what social or economic context shaped a rule the student has studied?')
k43(12, ['demonstrate', 'enable', 'reach', 'studied'], 'legal skills for reaching unfamiliar branches of law', SK,
    "Show a range of legal skills, such as critical analysis and problem-solving, enough to reach a basic grasp of any branch of the relevant jurisdictions, including ones not yet studied.",
    "At threshold, graduates have legal skills, such as critical analysis and problem-solving, that let them gain a basic grasp of any branch of law in their jurisdictions, studied or not.",
    "By graduation you should be able to use legal skills such as critical analysis and problem-solving to get a basic grasp of any area of law, even one you have not studied.",
    'para 1.4 and 4.3.b3', 'qaa/fheq-2024/4.15.b5', ADP[1], 'a student worries about areas of law their course did not cover',
    'how the student would start to learn a branch of law they have never studied?')
k43(13, ['develop'], 'digital literacy', GS,
    "Build digital literacy for finding, organising, creating and sharing information.",
    "At threshold, graduates have built digital literacy in locating, managing, producing and sharing information.",
    "By graduation you should be able to use digital skills to find, organise, create and share information.",
    '3.4.b6 and 4.4.b9', 'qaa/fheq-2024/4.15.b5', ADT[1], 'a student uses legal databases or digital tools',
    'which digital tool the student would use to keep track of sources?')
k43(14, ['participate'], 'taking part in problem-solving exercises', GS,
    "Take part in problem-solving exercises.",
    "At threshold, graduates have taken part in problem-solving exercises.",
    "By graduation you should be able to take part in problem-solving exercises.",
    '3.4.b2 and 4.3.b3', 'qaa/fheq-2024/4.15.b9.2', ADC[3], 'a student joins a group problem exercise or moot',
    'what role the student played in the last problem-solving exercise?')
k43(15, ['develop'], 'employability and career awareness', GS,
    "Build employability skills and awareness of careers, professional requirements and the need to plan ahead.",
    "At threshold, graduates have built employability skills and know about career options, professional requirements and the value of planning.",
    "By graduation you should be able to show employability skills and know about your career options, the professional requirements that apply and why you need to plan ahead.",
    'paras 1.5 and 2.12 and 3.4.b9', 'qaa/fheq-2024/4.15.b9.3', ADT[4], 'a student asks about careers in or beyond the law',
    'which careers the student is considering and what each requires?', find=FINDS['4.3.b15'])
k43(16, ['develop'], 'the changing legal profession', UN,
    "Become aware of where the legal profession is heading and how it keeps changing.",
    "At threshold, graduates are aware of the direction of the legal profession and of its continual change.",
    "By graduation you should be aware of where the legal profession is heading and how it keeps changing.",
    'paras 1.17 and 1.18 and 4.3.b15', 'qaa/fheq-2024/4.15.b9.3', ADK[2], 'a student asks how technology or AI will change legal work',
    'what change in legal practice the student expects to matter most in their career?')

# ---- 4.4 threshold: generic skills and qualities of mind (lead-in: on graduating with an honours degree in Law, students should be able to demonstrate)
AAW44 = ("Describe this as a threshold generic skill: every honours graduate in Law should be able to show it at award, at FHEQ level 6 (FQHEIS level 10); "
         "it covers {about} and refines the descriptor {fw}. Cite " + CITE + ", para 4.4 (bullet {k}). Set it beside {nb} and the third-class column of "
         "Annex D ({ad}); do not claim it is a regulatory rule, the typical result or a standard at another level.")
AAD44 = ("Raise this when {when}. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; to "
         "staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask {q} Avoid reading the list aloud or presenting "
         "the minimum as what a good degree looks like.")
def k44(k, verbs, about, para, prac, ben, nb, fw, ad, when, q):
    P['4.4.b%d' % k] = dict(type='threshold', rung='threshold', force='should', level='fheq:6', appliesTo='honours graduates in Law',
                            addressee='learner', verbs=verbs, about=about, domain='generic-skill', award=HON, para=para, prac=prac, ben=ben,
                            aaw=AAW44.format(about=about, k=k, nb=nb, fw=fw, ad=ad), aad=AAD44.format(when=when, q=q))

k44(1, ['identify'], 'identifying issues and problems',
    "Pick out the issues, questions and problems in a situation.",
    "At threshold, graduates spot the issues, questions and problems a situation raises.",
    "By graduation you should be able to spot the issues, questions and problems in a situation.",
    '4.3.b3 and 3.4.b1', 'qaa/fheq-2024/4.15.b7', ADC[3], 'a student misses the point of a problem question',
    'what the student sees as the central issue before they start writing?')
k44(2, ['identify', 'acquire'], 'gaps in knowledge',
    "Recognise what they do not yet know and learn it.",
    "At threshold, graduates recognise the gaps in their knowledge and fill them.",
    "By graduation you should be able to see what you do not yet know and go and learn it.",
    '3.4.b1', 'qaa/fheq-2024/4.15.b5', ADT[3], 'a student starts a new topic or revision',
    'what the student knows least about in the current module?')
k44(3, ['understand', 'analyse'], 'understanding and analysing information',
    "Grasp and break down knowledge and information.",
    "At threshold, graduates make sense of knowledge and information and analyse it.",
    "By graduation you should be able to make sense of information and analyse it.",
    '4.3.b7', 'qaa/fheq-2024/4.15.b7', ADK[2], 'a student summarises rather than analyses',
    'what the student would say a source shows, beyond what it says?')
k44(4, ['synthesise'], 'synthesising the state of knowledge',
    "Draw together what is known on a given topic.",
    "At threshold, graduates synthesise current knowledge on a topic.",
    "By graduation you should be able to bring together what is known about a topic.",
    '4.3.b2', 'qaa/fheq-2024/4.15.b3.2', ADC[1], 'a student begins a literature review',
    'what the main positions on the topic are and where they meet?')
k44(5, ['apply', 'provide'], 'evidenced conclusions to problems',
    "Use knowledge and understanding to reach evidenced conclusions, including on complex real or hypothetical problems.",
    "At threshold, graduates apply what they know to reach evidenced conclusions, including on complex real or imagined problems.",
    "By graduation you should be able to use what you know to reach conclusions backed by evidence, including on complex real or imagined problems.",
    '4.3.b3 and para 3.2', 'qaa/fheq-2024/4.15.b3.1', ADC[3], "a student's conclusion is unsupported",
    "what evidence the student's conclusion rests on?")
k44(6, ['communicate'], 'effective communication',
    "Communicate effectively and suitably, in speech or in other forms.",
    "At threshold, graduates communicate effectively and appropriately, orally or otherwise.",
    "By graduation you should be able to communicate clearly and appropriately, in speech or in other ways.",
    '3.4.b5 and 4.3.b8', 'qaa/fheq-2024/4.15.b8', ADT[1], 'a student prepares a presentation or moot',
    'who the audience is and what they need to understand?')
k44(7, ['present'], 'presenting knowledge and argument comprehensibly',
    "Present knowledge or an argument so that others can follow it.",
    "At threshold, graduates present knowledge or argument in a form others can understand.",
    "By graduation you should be able to present knowledge or an argument so others can follow it.",
    '4.3.b6 and 3.4.b5', 'qaa/fheq-2024/4.15.b8', ADT[1], "a student's writing is hard to follow",
    "how a non-lawyer would summarise the student's argument?")
k44(8, ['work'], 'working with qualitative and quantitative data',
    "Handle varied data, including qualitative and quantitative empirical data.",
    "At threshold, graduates work with a range of data, qualitative and quantitative.",
    "By graduation you should be able to work with different kinds of data, including qualitative and quantitative evidence.",
    '3.4.b4', 'qaa/fheq-2024/4.15.b6', ADP[4], 'a student meets empirical research on how law works in practice',
    'what kind of data would test a claim about how a law operates?')
k44(9, ['engage', 'collate', 'analyse', 'select', 'present'], 'digital technology for handling information',
    "Use varied digital technologies to gather, analyse, select and present information.",
    "At threshold, graduates use different digital technologies to gather, analyse, choose and present information.",
    "By graduation you should be able to use different digital tools to gather, analyse, choose and present information.",
    '3.4.b6 and 4.3.b13', 'qaa/fheq-2024/4.15.b5', ADT[1], 'a student chooses tools for research or presentation',
    'which digital tool helped the student most in their last assignment?')
k44(10, ['undertaking', 'conducting', 'demonstrating'], 'intellectual independence',
    "Show intellectual independence: work on tasks alone with suitable guidance and support, carry out self-directed research and judge critically.",
    "At threshold, graduates work independently with fitting support, direct their own research and exercise critical judgement.",
    "By graduation you should be able to work on your own, with the right guidance, direct your own research and make critical judgements.",
    '3.4.b1 and 3.4.b3', 'qaa/fheq-2024/4.15.b9.1', ADT[3], 'a student moves to a dissertation or independent project',
    'what support the student still needs and what they can now do alone?')
k44(11, ['work', 'undertaking', 'participating'], 'collaborative work',
    "Work with others, in a group or team or by taking part in discussion.",
    "At threshold, graduates collaborate in groups or teams and contribute to discussion.",
    "By graduation you should be able to work with others in a group or team and take part in discussion.",
    '3.4.b8', 'qaa/fheq-2024/4.15.b9.1', ADT[2], 'group work begins or a seminar discussion is quiet',
    'how the student contributed to the last group discussion?')
k44(12, ['reflect'], 'reflection on progress and academic integrity',
    "Reflect on their own progress, including matters of academic integrity.",
    "At threshold, graduates reflect on their progress, taking in questions of integrity in their academic work.",
    "By graduation you should be able to reflect on your own progress, including how you keep your work honest and properly referenced.",
    '3.4.b7 and 3.4.b9', 'qaa/fheq-2024/4.15.b9.3', ADT[5], 'a student asks about academic integrity or reviews their progress',
    'what the student has learned about their own progress this year?')
k44(13, ['identify', 'examine'], 'values and ethics in law, society and the self',
    "Identify and examine the values and ethics underlying law, culture and society, and their own.",
    "At threshold, graduates examine the values and ethics beneath law, culture and society and in their own lives.",
    "By graduation you should be able to identify and question the values and ethics behind law, culture and society, and your own.",
    '3.4.b10, 3.4.b11 and para 1.1', 'qaa/fheq-2024/4.15.b9.2', ADK[2], "a topic raises questions of values or the student's own ethics",
    'what value the student thinks a rule they have studied protects?')
k44(14, ['understand'], 'well-being, emotions and learning',
    "Understand why well-being, mental health and emotions matter and how they bear on learning.",
    "At threshold, graduates understand how well-being, mental health and emotion relate to learning.",
    "By graduation you should understand why your well-being, mental health and emotions matter and how they affect your learning.",
    'para 1.3 and 3.4.b7', 'qaa/fheq-2024/4.15.b9.1', ADT[3], 'a student talks about stress or how they feel about their studies',
    'what helps the student learn well when under pressure?')
k44(15, ['make'], 'using feedback',
    "Make good use of feedback to advance their intellectual development.",
    "At threshold, graduates use the feedback they receive to develop intellectually.",
    "By graduation you should be able to use the feedback you get to develop your thinking.",
    '3.4.b7 and para 3.12', 'qaa/fheq-2024/4.15.b5', ADT[3], 'a student receives marked work back',
    'what the student did with their last feedback?')
k44(16, ['appreciate', 'engage'], 'contemporary debates on law and society',
    "Appreciate and join current debates on law, individuals, culture and society, such as inequality and sustainability.",
    "At threshold, graduates follow and take part in current debates on law and society, for example on inequality and sustainability.",
    "By graduation you should be able to follow and take part in current debates about law and society, such as on inequality and sustainability.",
    'paras 1.8 and 1.13', 'qaa/fheq-2024/4.15.b3.2', ADK[2], 'a seminar turns to current affairs or law reform',
    'which current debate the student would most want to see change the law?')

# paragraph records recut to the paragraph text (skeleton spans ran into the next heading or page)
for _i in ('1.4', '1.8', '1.9', '1.11', '1.12', '2.2', '2.3', '2.6', '2.7', '2.12', '3.2', '3.5', '3.6', '3.7', '3.8', '3.9', '3.10', '3.12', '4.2'):
    P[_i]['find'] = FINDS[_i]

GRADE = {}   # one rung only: no gradeOf links

TH = {'1.8': 'theme:edi', '1.9': 'theme:accessibility', '1.11': 'theme:accessibility', '1.12': 'theme:accessibility'}

S5 = dict(
    levels=[dict(id='fheq:6', role='cites', locator='D1, 2.2; 4.2'),
            dict(id='fqheis:10', role='cites', locator='D1, 2.2; 4.2'),
            dict(id='fheq:7', role='cites', locator="D1, 2.4 (integrated master's, MLaw; no standards stated)"),
            dict(id='fqheis:11', role='cites', locator="D1, 2.4 (integrated master's, MLaw; no standards stated)"),
            dict(id='spine:6', role='refers', locator='std:ref:uk-framework R2 and R8 (inferred: Part E)')],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.2: "FHEQ Level 6; FQHEIS Level 10"; 4.2, the title of Annex D)'),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.4: "FHEQ Level 7; FQHEIS Level 11")'),
                dict(**{'from': 'fheq:6'}, to='spine:6', relation='sameStep', basis='inferred from std:ref:uk-framework R2 (Part E)')])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.3', '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '1.17', '2.1', '2.6', '3.5', '3.6', '3.9', '3.12', '4.4']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.3', '1.9', '1.10', '1.11', '1.12', '1.17', '2.6', '2.7', '3.5', '3.9', '3.10', '3.11']),
      dict(id='theme:esd', role='carries', carriedIn=['1.3', '1.13', '1.14', '3.5', '4.4']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.5', '1.10', '1.15', '1.16', '1.17', '1.18', '3.4', '4.3']),
      dict(id='theme:generative-ai', role='carries', carriedIn=['1.18'])]

S7 = [dict(rel='supersedes', target='std:doc:qaa-law-2019-benchmarks (not yet ingested)', note='the fourth edition (2019), named in section 5; the front matter lists key changes'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees, for performance above the threshold (4.2); SL6'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='levels 6 and 7 (2.2, 2.4)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='levels 10 and 11 (2.2, 2.4)'),
      dict(rel='cites', target='std:doc:qaa-advancehe-esd-2021-guidance', note='the QAA/Advance HE guidance on sustainable development in legal studies (1.14)'),
      dict(rel='refersTo', target='std:doc:advancehe-psf-dimensions-2023-framework', note="Advance HE's PSF, named as a recognition staff may hold (3.6)"),
      dict(rel='refersTo', target='PSRB requirements for routes to legal practice and qualifying Law degree accreditation (not yet ingested: Part E)', note='1.2, 2.12, 3.2'),
      dict(rel='readWith', target='the Subject Benchmark Statements of partner subjects in joint routes (collection)', note='2.3'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance; QAA Glossary', note='front matter')]

SB1 = [
    'Law is studied as an academic subject joining legal knowledge, general intellectual skills and skills particular to law, with values and ethics in theory and practice (D1, 1.1).',
    'The degree alone does not license practice, though it prepares for regulated legal work; routes to qualification differ across the UK nations and are set by PSRBs (D1, 1.2, 2.12).',
    'It borrows methods from the humanities and social sciences and attends to professional behaviours, well-being, the affective domain and citizenship (D1, 1.3, 3.1).',
    'Its outlook is both national and global; a course may cover one jurisdiction or several (D1, 1.4, 3.2).',
    'Law is treated as a system of power that can sustain or challenge inequality, so its study is critical and concerned with justice and fairness (D1, 1.6 to 1.8, 2.1).',
    'Legal understanding is built through detailed work on substantive law, with no compulsory subjects set by the statement (D1, 3.2).',
    'Technology and artificial intelligence are changing legal services and the role of lawyers, and access to justice is a recurring concern (D1, 1.17, 1.18).',
    'Practical and experiential learning, such as law clinics, public legal education, mooting and placements, sits alongside academic study (D1, 2.6, 2.8, 3.7, 3.11).',
    'Graduates go into regulated practice and into many other skilled roles at home and abroad (D1, 1.5).',
]

SB2 = [dict(theme='theme:edi', inThisSubject='law is read as a source of both inequality and challenge to it; courses bring out law and equality, aim for substantive equality in the curriculum and inclusive assessment and feedback, and students engage with debates on inequality (D1, 1.3, 1.6 to 1.8, 2.1, 3.5, 3.9, 3.12)',
            statements=['1.8', '2.6', '3.5', '3.9', '3.12', '4.4.b13', '4.4.b16']),
       dict(theme='theme:accessibility', inThisSubject='headed Accessibility in the text: widening access, anticipatory inclusive design, reasonable adjustments, many disabled identities in law school, flexible assessment and digital inclusivity (D1, 1.9 to 1.12, 2.6, 2.7, 3.5, 3.9 to 3.11)',
            statements=['1.9', '1.11', '1.12', '2.6', '2.7', '3.5', '3.9', '3.10']),
       dict(theme='theme:esd', inThisSubject='headed Sustainability in the text: law has a part in securing sustainable development; the SDGs and the UNESCO competencies are named, and students engage with debates on sustainability (D1, 1.3, 1.13, 1.14, 3.5, 4.4)',
            statements=['3.5', '4.4.b16']),
       dict(theme='theme:enterprise', inThisSubject='headed Entrepreneurship and enterprise education in the text, with employability: careers in and beyond practice, enterprise education for change, legal technology and new models of legal services (D1, 1.5, 1.15 to 1.18, 3.4, 4.3)',
            statements=['3.4.b9', '4.3.b15', '4.3.b16']),
       dict(theme='theme:generative-ai', inThisSubject='artificial intelligence tools change the role of lawyers in decisions; courses may explore digital justice, AI in legal reasoning and its ethical issues (D1, 1.18)',
            statements=['4.3.b16'])]

SB3 = dict(
    areas=[dict(component='1.4', gloss='the main features and principles of the legal system or systems studied; sources of law; relations of persons and the state'),
           dict(component='3.1', gloss='legal rules and concepts, ethics, justice and the rule of law, with methods from the humanities and social sciences'),
           dict(component='3.2', gloss='legal understanding of public and private law in many contexts, through substantive areas of law'),
           dict(component='3.3', gloss='subject-specific skills: interpreting, finding and interrogating legal and academic sources')],
    practices=[dict(component='2.6', kind='teaching', gloss='whole-course design across online, blended and face-to-face delivery; practical learning; digital fluency'),
               dict(component='2.8', kind='learning', gloss='partnerships with employers and social enterprises; law clinics, volunteering and policy work'),
               dict(component='3.5', kind='teaching', gloss='methods suited to subject and learners; synchronous, asynchronous and in-person teaching'),
               dict(component='3.6', kind='teaching', gloss='staff development; resources and training in legal sources and digital tools'),
               dict(component='3.7', kind='learning', gloss='clinical and public legal education, outreach, research and placements'),
               dict(component='3.8', kind='assessment', gloss='a strategy aligned with teaching and outcomes, for and as learning'),
               dict(component='3.9', kind='assessment', gloss='accessible mixed methods and adjustments agreed with the student'),
               dict(component='3.10', kind='assessment', gloss='a range of methods; diagnostic and later assessment; overall burden'),
               dict(component='3.11', kind='assessment', gloss='indicative methods: dissertation, essays and legal writing, examinations, mooting, visual and media work, group work, reflection, portfolios'),
               dict(component='3.12', kind='assessment', gloss='feedback that feeds forward; peer and self-assessment; varied formats')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.3 and 4.4 (under the heading Threshold level)', award=HON, items=32),
           dict(rung='typical', leadIn='none', award=HON, items=0),
           dict(rung='excellent', leadIn='none', award=HON, items=0)],
    rungBases='4.1: the statement sets the minimum threshold standards for the honours degree, in full where Law is at least half the course; 4.2: most students perform significantly better, judged by each provider with reference to Annex D (the four honours classes)',
    outcomeLists=[dict(leadIn='3.4', gloss='general and widely applicable skills Law graduates will be equipped with', items=12, award=['honours'])],
    outcomes=[])

SB4A_FULL = []

SB5 = [dict(body='professional, statutory and regulatory bodies (PSRBs), unnamed in the body of the text',
            says='set the specific requirements of routes to qualification in each branch of the profession in England and Wales, Scotland and Northern Ireland; accredit qualifying Law degrees; courses meant as a pathway to practice take account of their requirements (D1, 1.2, 2.12, 3.2)',
            requirements='not yet ingested (Part E)'),
       dict(body='Advance HE', says="its PSF is named as a recognition staff teaching Law may hold or be supported towards (D1, 3.6)",
            requirements='std:doc:advancehe-psf-dimensions-2023-framework'),
       dict(body='UNESCO', says='its account of education for sustainable development is quoted and its eight sustainability competencies are named (D1, 1.13)',
            requirements='not yet ingested (Part E)'),
       dict(body='learned societies in law and professional bodies (unnamed)', says='staff may interact with them and students will be made aware of the relevant ones (D1, 3.6, 3.7)',
            requirements='not yet ingested (Part E)')]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.3', '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '1.17', '2.1', '2.6', '3.5', '3.6', '3.9', '3.12', '4.4'],
                 statements=['1.8', '2.6', '3.5', '3.9', '3.12', '4.4.b13', '4.4.b16']),
            dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=['1.3', '1.9', '1.10', '1.11', '1.12', '1.17', '2.6', '2.7', '3.5', '3.9', '3.10', '3.11'],
                 statements=['1.9', '1.11', '1.12', '2.6', '2.7', '3.5', '3.9', '3.10']),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=['1.3', '1.13', '1.14', '3.5', '4.4'],
                 statements=['3.5', '4.4.b16']),
            dict(id='theme:enterprise', named='Entrepreneurship and enterprise education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['1.5', '1.10', '1.15', '1.16', '1.17', '1.18', '3.4', '4.3'],
                 statements=['3.4.b9', '4.3.b15', '4.3.b16']),
            dict(id='theme:generative-ai', named='artificial intelligence tools and software', carriedIn=['1.18'], statements=['4.3.b16'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.2', '2.4', '4.2']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.2', '2.4', '4.2'])],
    bodies=[dict(body='professional, statutory and regulatory bodies (PSRBs, unnamed)', citedIn=['1.2', '2.12', '3.2']),
            dict(body='Advance HE', citedIn=['1.14', '3.6']),
            dict(body='UNESCO', citedIn=['1.13']),
            dict(body='learned societies and professional bodies (unnamed)', citedIn=['3.6', '3.7'])],
    sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'], role='the four honours classes, for performance above the threshold'),
                     dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='the QAA/Advance HE Guidance on this topic', citedIn=['1.14'], role='ways of bringing sustainable development into legal studies'),
                     dict(document='std:doc:advancehe-psf-dimensions-2023-framework', named="Advance HE's PSF", citedIn=['3.6'], role='a recognition for staff who teach'),
                     dict(document='UNESCO, Education for Sustainable Development (external; not ingested)', named='Education for Sustainable Development (unesco.org)', citedIn=['1.13'], role='the definition of ESD quoted'),
                     dict(document='UN Sustainable Development Goals (external; not ingested)', named='the UN Sustainable Development Goals', citedIn=['1.13'], role='goals law is relevant to'),
                     dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code', citedIn=['front matter'], role='course design, teaching, external expertise, monitoring'),
                     dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms')])

B1 = [dict(slug='legal-understanding', definition='knowing, questioning and applying the theory, concepts, values and rules of public and private law in many contexts, including handling ambiguity and reaching evidenced conclusions (D1, 3.2)',
           beneficiaryDefinition='being able to question and use legal ideas and rules in different settings and reach well-supported conclusions', scopeNote='built through substantive areas of law; no subjects prescribed', category='unknown', practices=['law']),
      dict(slug='professional-behaviours', definition='individual or group conduct and identity in study, work and wider society, possibly including the legal profession (D1, 1.3)',
           beneficiaryDefinition='how you act and see yourself in study, work and society', scopeNote='may touch sustainability, EDI, digital and interpersonal skills, well-being and reflection', category='unknown', practices=['law']),
      dict(slug='substantive-equality', definition='equality that makes room for people of different backgrounds by removing barriers, challenging stereotypes and building agency, beyond formal legal statement (D1, 1.7)',
           beneficiaryDefinition='equality in practice, not only on paper', scopeNote='', category='unknown', practices=['law'])]
B2A = [dict(concept='legal-understanding', form='legal understanding', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='professional-behaviours', form='professional behaviours', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='substantive-equality', form='Substantive equality', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []; B5 = []

D3 = [dict(source='PSRB requirements for qualifying Law degrees and routes to legal practice in each UK jurisdiction', why='named in 1.2, 2.12 and 3.2 (SB5); the bodies are named only in the excluded back matter', status='wanted')]

E = [
    'Rungs: one only. Section 4 states the threshold (4.3, 16 subject items; 4.4, 16 generic items) and leaves higher performance to Annex D (4.2); no typical or excellent lists, so SB4 `outcomes` is empty and no gradeOf link is drawn. Differs from Psychology (three rungs).',
    'Lead-in wording: "On graduating with an honours degree in Law, students should be able to" (4.3) and "... should be able to demonstrate the following generic skills alongside qualities of mind articulated in paragraph 1.3" (4.4; "paragraph 1.3" is a reference, DPN-1). The modal is should, so force is recorded as should, statementType and rung threshold; 4.1 calls these the minimum threshold standards a student "will have demonstrated". P3 to confirm should against threshold as the force.',
    'The heading "Threshold level Subject knowledge, understanding and skills" is flattened onto the end of 4.2 in the held text; 4.2 is recut to end at its last sentence. 4.4 sits under "Generic skills and qualities of mind", a new sub-heading wording against Psychology.',
    'Outcome list in section 3: "Law graduates will be equipped with the following general and widely applicable skills" (3.4), recorded as type outcome, rung none, force will, domain generic-skill. Its items are noun phrases, so 3.4.b9 and 3.4.b11 list no verbs.',
    'Domains our reading: 4.3.b13 (digital literacy), 4.3.b14 (problem-solving exercises) and 4.3.b15 (employability) are recorded generic-skill though the issuer lists them under subject knowledge, understanding and skills; 4.3.b10, 4.3.b11 and 4.3.b16 understanding; the rest of 4.3 subject-skill. P3 to confirm.',
    'Near repeats in the issuer\'s text: 3.4.b6 and 4.3.b13 (digital literacy in finding, managing, creating and communicating information); 3.4.b4 and 4.4.b8 (working with a range of data); 3.4.b8 and 4.4.b11 (working collaboratively); 3.4.b1 and 4.4.b10 (intellectual independence). All kept as issued.',
    'Skeleton corrections: 4.3.b15 ran across a page break and lost "requirements and of the need for future planning"; recut with `find` (the span holds the page number 14). 2.6 is one paragraph, not a stem with a list: its skeleton item 2.6.b1 ("- to include online, blended or face-to-face - ...") is a dash inside the sentence; recorded as 2.6 whole across the page break, and 2.6.b1 dropped. Paragraph spans for 1.8, 1.12, 2.7, 3.7 and 4.2 carried the following sub-heading; every paragraph record is recut to its own text with `find`.',
    'Sub-headings flattened onto the end of the preceding paragraph in the held text: Accessibility (1.8), Sustainability (1.12), Entrepreneurship and enterprise education (1.14), Progression (2.1), Flexibility (2.5), Partnership (2.7), Monitoring and review (2.8), Assessment and feedback (3.7). SUB records them by their paragraph ranges.',
    'Not cut as statements, with reasons: 1.13.b1 to b3 name the UNESCO competencies under "might be recognised", not an outcome list; 3.11.b1 to b8 are indicative assessment practices (S3 practice); 1.2, 1.3 and 1.17 use will descriptively; 1.18 is permissive (may); 2.1 ("the study of law will apply principles of justice", "a Law degree will empower students") describes the discipline (SB1); 2.9 and 2.10 ("Providers will use external reviewers") and 2.11 describe quality assurance practice, as Archaeology 2.29 to 2.31; 4.1 frames the threshold and is the rung\'s introduction.',
    'Obliging words outside the five, for Abbott: 1.4 "This Statement requires knowledge of ..." recorded must (the meaning is plain); 1.12 "needs to be considered by providers" recorded describes; 1.9 "take responsibility" and "will also have responsibilities" recorded will; 2.2 "it is expected" and "would be expected" recorded will (the paragraph\'s own modal); 3.2 "it is expected that legal study will include" recorded will.',
    'Plain-present provider norms not cut (benchmark template open point 5, for P3): 1.2 ("Higher education providers keep these requirements in mind"), 1.9 (first two sentences, "Providers demonstrate ... anticipate and take responsibility"; the paragraph is cut for its will), 3.3 ("legal study involves"), 3.5 ("Learning and teaching methods are designed"), 3.6 ("Students ... are taught within an environment").',
    'Mixed modals: 2.12 holds will (accreditation) and should (be explicit to students), recorded at should; 3.7 holds might, may and one will, recorded at will; 3.12 holds will, may and could, recorded at will; 1.11 holds could and should, recorded at should.',
    '1.8, 1.9, 1.11, 1.12, 2.6, 2.7, 2.12 and 3.5 to 3.12 address providers rather than the student; recorded with addressee provider and the student version not applicable. 1.4 and 3.2 are recorded addressee both, with a student version.',
    "Integrated master's (MLaw) at FHEQ 7 / FQHEIS 11 is described in 2.4 but no standards are given for it; levelsCovered holds fheq:6 and fqheis:10 only. 2.5 names exit awards (CertHE, DipHE) without standards.",
    'Theme: 1.18 names artificial intelligence tools in legal services, not generative AI by name; tagged theme:generative-ai as the one AI id (BM-BRIEF conventions). P3 to confirm or to set a wider AI id.',
    'Theme: the front matter bundles employability with entrepreneurship and enterprise education; employability in 1.10, 3.4 and 4.3 is carried under theme:enterprise. 1.5 (careers) is carried there too.',
    'Inferred: the crosswalk fheq:6 to spine:6 is read from std:ref:uk-framework R2. No inferred subject codes: HECoS 100485 and CAH16-01-01 (law) follow the stated subject.',
    'SB5: the PSRBs are unnamed in sections 1 to 4; the Bar Standards Board, the Solicitors Regulation Authority, the Chartered Institute of Legal Executives and the Law Society of Scotland appear only in the advisory group lists (section 5, excluded matter) and are not in SB6. Their requirements are wanted (D3).',
    'SB6: the front matter also names the Quality Assessment Framework for Wales, the Quality Enhancement Framework (Scotland) and the OfS regulatory framework for England; these are excluded matter and not qualification frameworks, so they are not in SB6 frameworks. Advance HE is cited in 1.14 (the joint ESD guidance) and 3.6 (the PSF).',
    'SB6 carriers by heading: 1.12 (Accessibility), 1.17 and 1.18 (Entrepreneurship and enterprise education) are recorded under the sub-heading they sit in, though their own words do not name the theme; 2.8 "social enterprises" and "access to justice" (1.17, 2.8) are not counted as the enterprise or accessibility themes.',
    'CQFW: not cited by the statement; not used.',
    'Section order and headings match Psychology\'s 2023 pattern (context and purposes, distinctive features, content, structure and delivery, benchmark standards); the cross-cutting themes sit inside section 1 under their own sub-headings.',
    '4.2 writes the classes as "1st, 2.1, 2.2 and 3rd" (points, not colons).',
    'Supersedes: the 2019 fourth edition is named only in the advisory group list (section 5); the 2015, 2007 and 2000 editions are listed there too.',
    'Licence: QAA copyright notice only; re-use terms not stated in the text.',
]
