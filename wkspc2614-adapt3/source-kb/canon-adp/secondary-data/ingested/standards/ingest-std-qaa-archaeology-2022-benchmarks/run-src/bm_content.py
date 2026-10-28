# bm_content.py: run 0085 (std), QAA Subject Benchmark Statement Archaeology, March 2022. Judgement for tools/bm_build.py.
# Templates: standards 0.8.0-draft, benchmark 0.6.0-draft, run layer 0.7.0-draft; brief BM-BRIEF 0.2.0. Our words throughout except FINDS (the issuer's spans).
# Exact statement texts where the skeleton cut wrongly (trailing headings, a page break, a stray bullet); each occurs once.
FINDS = {
    '1.7': '1.7 In the case of degree courses where archaeology constitutes 50% or less of the total (including joint and combined honours courses, and those cases where archaeology units are taken as optional components within other kinds of modularised courses), the delivery of an appropriate platform of knowledge and understanding should be integral to the design of each individual archaeology module. In such situations, both the knowledge and understanding attained by students, and the teaching environment, will be consistent with the standards expressed in this Subject Benchmark Statement. For those courses that include other subjects alongside archaeology, guidance on appropriate levels of attainment will be articulated in the relevant Subject Benchmark Statement.',
    '1.9': '1.9 Archaeology degrees have a long tradition of being open to people from non- standard academic backgrounds. However, much more remains to be done to ensure the equitable inclusion of under-represented groups, most notably ethnic minority students, students from less affluent backgrounds, and otherwise disadvantaged students, including students with caring responsibilities, neurodiverse students and students with physical and/or mental health considerations. Greater attention should be paid to under-represented groups at all stages from outreach to marketing and recruitment, to education and career\n\n6\nprogression after graduation, in order to provide externally visible role models who can convey the clear message that archaeology is a global and diverse subject of enormous relevance to contemporary society. In addition, robust feedback mechanisms should be in place for students to highlight deficiencies and co-create possible solutions to barriers to participation, including ensuring accessibility for all students, particularly for practical elements of teaching, learning and extracurricular experience.',
    '1.10': '1.10 The core skills provided by all Archaeology degrees align with the learning outcomes suggested by the Education for Sustainable Development Guidance produced by Advance HE and QAA (March 2021). These include critical thinking, self-awareness, collaborative competencies, anticipatory and strategic thinking. Archaeology both encourages and embeds partnerships and interdependence between economic, social and environmental factors. By developing a deep understanding of what life was like in the past for people and non-humans, archaeology can actively contribute to the narratives about how we create a vision of a better world. Indeed, as the only subject that deals with the entirety of the human past, archaeology offers a critical perspective on how we now shape that future. In particular, the discipline is uniquely placed to foster an appreciation of the fragile and finite nature of the archaeological resource and the need for sustainable approaches to its use and conservation. Moreover, archaeology is directly involved with the development of sustainable and ethical heritage and tourism industries across the world. Emphasis should be placed on conveying this value to a wider society, both within local and regional communities and government organisations who are in a position to determine future outcomes.',
    '2.12': '2.12 Archaeological science is the application of scientific techniques to archaeological problems, whose methodologies and innovations are ultimately shared across a broad range of sciences, including physics, chemistry, biochemistry, biology, medicine, forensics and geoscience, alongside environmental, digital and materials science. The use of quantitative approaches, hypothesis testing and an awareness of scientific techniques should be part of the toolkit of every archaeologist. Archaeological science is interdisciplinary and collaborative by nature, contributing to a diverse range of major research themes. These include:',
    '2.19': '2.19 Individual degree courses are located at different points within a triangle drawn between the complementary archaeologies of the humanities, sciences and professional practice. A department teaching single and combined honours degrees will inevitably position the courses it offers at different locations within this range. All courses will nevertheless stress the contexts, interdisciplinarity and overarching practice that departments seek to instil in their students.',
    '2.20': '2.20 The principal learning and teaching methods that an Archaeology student may experience will depend on the aims and objectives of the course, given the wide range of subject-specific and transferable skills being developed. To ensure students who struggle with particular forms of teaching and learning scenarios are not disadvantaged, methods used within an individual course should be as varied as possible. They are likely to comprise an appropriate combination of the following:',
    '2.21': '2.21 While there is a recognition that teaching and assessments may need to be adjusted or tailored to the requirements of individuals to ensure inclusiveness and well- being, different formats should be offered to all students and expectations should be\n\n13\ntransparent. Care must be taken not to create a two-tier system that singles out students with additional requirements. Fieldwork in particular may present practical difficulties for some students and no one-size-fits-all approach is likely to be sufficient; individual circumstances should be taken into account in agreeing adjustments to teaching and learning methods for disabled students. In addition, all practical efforts should be made to ensure equal access to extracurricular activities such as field trips, placements and volunteering opportunities, given the often hidden costs (including opportunity costs) involved. The timing of religious observances and school holidays may be considered when setting deadlines. It should be remembered that perceptions of assessment may differ according to the cultural and experiential backgrounds of both assessors and their students. Clear and accessible guidance outlining assessment criteria at different stages of the degree must be provided.',
    '4.2': "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd.",
    '3.2.b5': 'recognise and communicate the archaeological significance of materi al re mains,\n• landscapes and environmental data',
    '3.2.b17': 'understand the broader legislative and planning content in which archaeological work may be undertaken, now and in the past.',
    '4.3.b16': 'demonstrate awareness of the impact of archaeological practice, interpretation and representation on other communities, including historically marginalised groups,\n\n21\nand appreciate the need to engage with communities thus affected on an equitable basis',
    '4.3.b18': 'demonstrate awareness of the legal and ethical dimensions of archaeology.',
}

HON = "bachelor's with honours"
CITE = 'QAA, 2022, Archaeology Subject Benchmark Statement'

META = dict(
    run='0085', p1='2026-10-03 16:14',
    title='Subject Benchmark Statement Archaeology',
    heading='Subject Benchmark Statement: Archaeology (QAA, March 2022)',
    edition='March 2022 (fourth edition)', published='2022-03',
    status='current',
    supersedes='the third edition (2014), named in the advisory group list (D1, section 6)',
    subjects=[dict(scheme='hecos', code='100299', label='archaeology', basis='stated'),
              dict(scheme='cah', code='CAH20-01-03', label='archaeology', basis='stated'),
              dict(scheme='cah', code='CAH20-01', label='history and archaeology', basis='stated'),
              dict(scheme='hecos', code='100384', label='archaeological sciences', basis='inferred')],
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2022 revision with cross-cutting themes (Archaeology fourth edition, March 2022)',
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    agentDefinition=("This document records what the QAA's 2022 Archaeology statement expects of an honours graduate in archaeology and of the courses "
                     "that lead there. Read S4 for the standards: section 4 gives one rung only, the threshold, in two lists (subject knowledge, "
                     "understanding and skills; generic skills), and section 3 adds two outcome lists of what students will be equipped to do. "
                     "Every standard has a practitioner version, a student version and two instructions for AI agents who write about it or use it "
                     "in conversation. Performance above the threshold is left to Annex D of the 2024 Frameworks, which this document points to and never copies."),
    summary=("Archaeology, bachelor's degree with honours (FHEQ level 6; FQHEIS level 10), fourth edition, March 2022. One rung is stated: the threshold, "
             "with 18 subject items (4.3) and 20 generic items (4.4); no typical or excellent lists, the provider being sent to Annex D for higher "
             "classes (4.2). Two further outcome lists in section 3 give the subject-specific (3.2, 16 items) and generic, transferable and employability "
             "skills (3.3, 19 items) students will be equipped with. Fourteen obliging paragraphs set expectations on courses and the discipline: the "
             "platform of knowledge, inclusion, sustainability, ethics, accessibility, assessment and the use of Annex D. Themes: equality, diversity and "
             "inclusion; accessibility; sustainability (education for sustainable development); enterprise and entrepreneurship. Bodies: the Chartered "
             "Institute for Archaeologists with University Archaeology UK (joint degree accreditation since 2019), BABAO, the Institute of Archaeologists "
             "of Ireland and others in the historic environment sector; the national heritage bodies are named as partners."),
    authority='reference: a sector reference point, not a regulatory requirement; a key reference point in Wales and Scotland and part of the quality requirements in Northern Ireland (D1, front matter)')

S2 = dict(
    governs="what a graduate in archaeology is expected to know, do and understand at the end of an honours degree, and the nature of courses in the subject",
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    statedScope='"This document is a QAA Subject Benchmark Statement for Archaeology that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies." (D1, front matter); 4.1 applies the standards in full only to courses with at least 50% archaeology',
    statedSubjects=[
        dict(name='Archaeology', locator='(D1, title; 1.1)', kind='subject',
             codes=[dict(scheme='hecos', code='100299', label='archaeology'), dict(scheme='cah', code='CAH20-01-03', label='archaeology')]),
        dict(name='joint or combined honours courses (with history, geography, anthropology, classics and cultural heritage, English, natural sciences or forensic science)',
             locator='(D1, 1.4; 1.7; 2.23)', kind='programme title', codes=[dict(scheme='hecos', code='100299', label='archaeology')]),
        dict(name='archaeological science', locator='(D1, 2.12 to 2.17)', kind='specialism',
             codes=[dict(scheme='hecos', code='100384', label='archaeological sciences')]),
        dict(name="integrated master's degrees (MArc)", locator='(D1, 2.24)', kind='programme title',
             codes=[dict(scheme='hecos', code='100299', label='archaeology')]),
    ])

SECTIONS = {'1': 'Context and purposes of an Archaeology degree', '2': 'Distinctive features of an Archaeology degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.4', 'Context'), ('1.5', '1.5', 'Purposes of an Archaeology degree'),
       ('1.6', '1.7', 'Characteristics of an Archaeology degree'), ('1.8', '1.9', 'Equality, diversity and inclusion'),
       ('1.10', '1.10', 'Sustainability'), ('1.11', '1.14', 'Enterprise and entrepreneurship'),
       ('2.1', '2.2', 'Design'), ('2.3', '2.4', 'The social context'), ('2.5', '2.8', 'The ethical and professional context'),
       ('2.9', '2.11', 'The theoretical context'), ('2.12', '2.17', 'The scientific context'),
       ('2.18', '2.19', 'Implications for the design of Archaeology degree courses'), ('2.20', '2.21', 'Accessibility'),
       ('2.22', '2.24', 'Progression'), ('2.25', '2.26', 'Flexibility'), ('2.27', '2.28', 'Partnership'),
       ('2.29', '2.32', 'Monitoring and review'),
       ('3.1', '3.1', 'Content'), ('3.2', '3.2', 'Subject-specific content'), ('3.3', '3.3', 'Generic, transferable and employability content'),
       ('3.4', '3.8', 'Teaching and learning'), ('3.9', '3.11', 'Assessment'),
       ('4.1', '4.2', 'Introduction'), ('4.3', '4.3', 'Threshold level: Subject knowledge, understanding and skills'), ('4.4', '4.4', 'Generic skills')]

G = {
    '1.1': 'a unique view of the whole human past and of being human; time depth for present concerns',
    '1.2': 'interpreting tangible and intangible remains; discovery, stories, debate and many voices',
    '1.3': 'origins in colonial and national contexts; changing methods and theory; a distinct discipline today',
    '1.4': 'between science, arts and professional practice; how it differs from Classics, History and Heritage Management',
    '1.5': 'purposes: foundations in the human past, transferable skills and varied careers',
    '1.6': 'the platform of knowledge any course with at least half archaeology offers',
    '1.7': 'courses with half archaeology or less build the platform into each module',
    '1.8': 'inclusion: barriers to taking part and the duty to widen voices',
    '1.9': 'under-represented groups, from outreach to careers; student feedback on barriers',
    '1.10': 'sustainability: alignment with ESD outcomes and the finite resource',
    '1.11': 'enterprise education and its benefits for careers',
    '1.12': 'the professional body and joint accreditation against occupational standards',
    '1.13': 'the joint governance of accreditation',
    '1.14': 'not only a vocational degree; wide career sectors',
    '2.1': 'research-led, broad and rigorous; students meet primary material and can discover',
    '2.2': 'the four contexts courses are built on',
    '2.3': 'the social context: narratives of past societies through present lenses',
    '2.4': 'contested pasts, identity and the legacy of colonialism; decolonising the subject',
    '2.5': 'institutional ethics approval for any student project',
    '2.6': 'human remains, illicit material, overseas work and the ethics in curricula',
    '2.7': 'professional bodies, heritage protection law and treaties, links with nature heritage',
    '2.8': 'growing employment, public benefit and accreditation since 2019',
    '2.9': 'theory and practice intertwined; paradigm shifts and borrowing from other fields',
    '2.10': 'big questions about being human, resilience and contemporary challenges',
    '2.11': 'four elements: scale, networks, wider context and self-reflexive theory',
    '2.12': 'archaeological science and its ten research themes',
    '2.13': 'artefact study and dating frameworks',
    '2.14': 'conservation science and the care of tangible heritage',
    '2.15': 'biological and environmental science and biomolecular methods',
    '2.16': 'experimental archaeology',
    '2.17': 'digital literacy, creativity and global ethical frameworks for science',
    '2.18': 'the four contexts underpin all degrees; humanities and sciences integrated',
    '2.19': 'courses placed within the humanities, science and practice triangle',
    '2.20': 'a varied mix of teaching and learning methods so no student is disadvantaged',
    '2.21': 'adjustments, transparency, equal access to fieldwork and extras, clear assessment criteria',
    '2.22': 'progression year by year towards the threshold skills; readiness for postgraduate study',
    '2.23': 'joint honours students reach part of the skills and add others',
    '2.24': "integrated master's (MArc), exit awards and the Scottish four-year honours degree",
    '2.25': 'a flexible mix of research-led teaching styles and pedagogic innovation',
    '2.26': 'independent research, project or dissertation, with ethical reflection',
    '2.27': 'partnership with accrediting and national heritage bodies and museums',
    '2.28': 'data services, commercial units, volunteers, community archaeology and European partners',
    '2.29': 'monitoring and periodic review against external reference points',
    '2.30': 'external reviewers in periodic review',
    '2.31': 'external examiners and the security of threshold standards',
    '2.32': 'professional accreditation for vocational courses',
    '3.1': 'content varies with position in the triangle; single and combined honours',
    '3.2': 'what students will be equipped to do in the subject',
    '3.3': 'general, transferable and employability skills of graduates',
    '3.4': 'teaching environments reflect each department\'s position',
    '3.5': 'teaching, research and practice; competent staff',
    '3.6': 'the learning environment and its resources, equipment and laboratories',
    '3.7': 'course documentation, safety and ethics guidance',
    '3.8': 'engagement with the archaeological community; practical work in every course',
    '3.9': 'an explicit assessment strategy tied to outcomes',
    '3.10': 'accessible, mixed assessment; adjustments; formative feedback',
    '3.11': 'the range of assessment methods in current use',
    '4.1': 'the minimum threshold standards and where they apply in full',
    '4.2': 'most students exceed the threshold; Annex D for degree classes',
    '4.3': 'threshold: subject knowledge, understanding and skills',
    '4.4': 'threshold: generic skills',
}

CTYPE = {'1.6': 'area', '2.3': 'area', '2.4': 'area', '2.5': 'area', '2.6': 'area', '2.9': 'area', '2.11': 'area', '2.12': 'area',
         '2.13': 'area', '2.14': 'area', '2.15': 'area', '2.16': 'area', '2.17': 'area',
         '2.20': 'practice', '2.25': 'practice', '2.26': 'practice', '2.28': 'practice', '3.6': 'practice', '3.8': 'practice',
         '3.9': 'practice', '3.10': 'practice', '3.11': 'practice'}

EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='Contents', kind='other: contents list'),
    dict(number='1 to 4', heading='section heading lines', kind='other: headings, recorded in S3 as sections'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for SB5 and SB6'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Archaeology', kind='other: back matter, read for S8 (editions 2000, 2007, 2014, 2022)'),
]

P = {}
def s(i, **k):
    P[i] = k

# ---- obliging or outcome paragraphs (sections 1 to 4)
s('1.6', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='courses with at least 50% archaeology and their students',
  addressee='both', verbs=['offer', 'include', 'recognise'], about='the platform of knowledge and understanding', domain='knowledge', award=HON,
  para=("Any course that is at least half archaeology will give students a common base: where the discipline came from and why it matters now, "
        "its legal and policy setting, and the contexts of investigation; the content should stress that the resource is fragile and cannot be renewed. "
        "Students are expected to know the kinds of evidence, theory and interpretation, to know regions and periods broadly and one or more classes of "
        "material or periods in depth, and to recognise why recovering and managing primary data matters, through fieldwork (adjusted for disabled students) "
        "or work with collections, records or artefacts, including scientific methods and the sources of bias in evidence."),
  prac=("A course that is half archaeology or more will build a shared base: the history and present value of the discipline, its legal and policy "
        "frame, the social, ethical and political settings of fieldwork and interpretation, and care for a finite resource. Plan for broad regional and "
        "period knowledge plus depth in at least one class of material or period, hands-on work with primary data in the field (adjusted where a student "
        "is disabled) or with collections and records, scientific dating and analysis, analogy and experiment, and the causes of bias in evidence."),
  ben=("Your course will give you a broad grounding in how archaeology began, why it matters today and the laws and policies around it. You will be "
       "expected to know many regions and periods in outline and at least one kind of material or period in depth, to handle primary data in the field "
       "(with adjustments if you need them) or through collections, and to understand scientific methods and why some evidence is less reliable than other evidence."),
  aaw=(f"Describe this as an expectation (will, with one should) on any course that is at least half archaeology, at FHEQ level 6 for the honours degree, "
       f"not as one of the threshold items. Cite {CITE}, para 1.6. Set it beside the threshold knowledge items 4.3.b2, 4.3.b3 and 4.3.b11 and the level 6 "
       f"descriptor qaa/fheq-2024/4.15.b1; do not claim it binds a course with less archaeology, which para 1.7 treats separately."),
  aad=("Bring this up when a programme team asks what core content an archaeology degree should cover, or when a student wonders why fieldwork, "
       "theory and science all appear in the course. Put it to staff as a design checklist and to a student as the broad base the course builds. "
       "Ask the team which modules carry depth in one class of material or period, and ask a student which kind of evidence they feel least sure "
       "of; avoid reading the long paragraph out or treating every element as a separate pass requirement."))

s('1.7', type='requirement', rung='none', force='should', level='none', appliesTo='courses where archaeology is 50% or less',
  addressee='provider', verbs=['expressed'], about='the platform in joint, combined and minor routes', domain='none', award=HON,
  para=("Where archaeology is half a course or less, including joint and combined honours and optional modules in other courses, each archaeology "
        "module should be designed to deliver a suitable base of knowledge and understanding; what students attain and the teaching setting will match "
        "the standards of this statement, and other subjects follow their own statements."),
  prac=("In joint, combined or modular routes where archaeology is no more than half the course, design each archaeology module to carry its share of "
        "the core base of knowledge; the attainment and teaching environment will match this statement, while the partner subject is judged against its own statement."),
  ben=('n/a', 'a design duty on the course for joint and combined routes; the student meets its effect, not a standard to reach'),
  aaw=(f"Describe this as a course design duty (should) for routes where archaeology is half the course or less; it states no level of its own. "
       f"Cite {CITE}, para 1.7, and read it with para 1.6 and the scope note at para 4.1. Do not claim that joint honours students must meet every "
       f"threshold item in 4.3 and 4.4; para 2.23 says they reach a proportion and add others."),
  aad=("Raise this with a programme team designing a joint or combined route, or with a teacher of an archaeology option inside another degree. "
       "Frame it for staff as building the core base into each module rather than relying on the full course. Ask which parts of the shared base "
       "each module carries and how the partner subject's statement is being met; avoid putting this to a student as something they must achieve."))

s('1.8', type='expectation', rung='none', force='must', level='none', appliesTo='archaeologists and the discipline, including teaching staff',
  addressee='provider', verbs=['take', 'emphasise', 'reflect', 'engage'], about='widening voices and participation in the discipline', domain='none', award='none',
  themes='theme:edi',
  para=("The subject's deep-time, cross-cultural view could give voice to many groups, but it often does not, and archaeologists must take "
        "responsibility for changing that. Barriers remain around ethnicity, disability, gender and class, a legacy of the discipline's origins. "
        "Archaeology should stress that understanding of the past is fluid, help students see the continuing effects of colonialism, and its "
        "practitioners should reflect on their practice and must engage far more fairly with communities outside the academy, in inclusive language."),
  prac=("Staff and departments must own the work of widening who takes part in and is heard by archaeology: challenge stereotypes, show that views of "
        "the past change, bring the legacy of colonialism into teaching, reflect critically on practice, engage fairly with schools, community groups and "
        "the public, and use language that includes rather than excludes."),
  ben=('n/a', 'a duty on archaeologists and departments as practitioners; the student meets its effect through the curriculum'),
  aaw=(f"Describe this as an obligation (must and should) on archaeologists and departments, not an outcome the student is assessed on. "
       f"Cite {CITE}, para 1.8, under its equality, diversity and inclusion heading, and set it beside the student-facing items 4.3.b16, 4.3.b17 and 4.4.b18. "
       f"Do not claim it sets a level or a legal duty; the statement carries no regulatory requirement."),
  aad=("Raise this with a programme team or teacher reviewing curriculum, fieldwork recruitment or outreach for inclusion. Put it in practitioner terms: "
       "what the department does to widen who takes part and whose pasts are told. Ask which groups the course still struggles to reach and where "
       "colonial legacies are taught; avoid passing this duty to a student or reading the paragraph aloud."))

s('1.9', type='requirement', rung='none', force='should', level='none', appliesTo='departments and courses in archaeology',
  addressee='provider', verbs=['paid', 'provide', 'highlight', 'co-create'], about='under-represented groups and feedback on barriers', domain='none', award='none',
  themes='theme:edi',
  para=("Though open to people from varied academic backgrounds, archaeology must do more to include under-represented students, among them ethnic "
        "minority, less affluent, disadvantaged, caring, neurodiverse and disabled students. Attention should go to them at every stage from outreach to "
        "careers, to give visible role models, and strong feedback routes should let students raise problems and help design fixes, including access to practical work."),
  prac=("Attend to under-represented students at every stage, from outreach and recruitment through teaching to careers, so that they can see role "
        "models; put working feedback routes in place so students can report barriers and help solve them, above all for access to practical and extracurricular activity."),
  ben=('n/a', 'a duty on the department and course; the student meets its effect'),
  aaw=(f"Describe this as a provider expectation (should) on inclusion across the student journey; it carries no level. Cite {CITE}, para 1.9, "
       f"and set it beside para 1.8, the accessibility paragraphs 2.20 and 2.21 and the student items 4.3.b17 and 4.4.b17. Do not present it as a "
       f"student outcome or as a statutory equality duty."),
  aad=("Bring this into a programme team's discussion of recruitment, outreach, student voice or access to fieldwork. Frame it for staff as a "
       "check across the whole journey and on feedback routes. Ask how students can report a barrier and see it acted on, and which groups the "
       "outreach reaches; avoid placing the duty on a student."))

s('1.10', type='expectation', rung='none', force='should', level='none', appliesTo='the discipline and its teaching',
  addressee='provider', verbs=['placed', 'conveying'], about="conveying the value of sustainability and the finite resource", domain='none', award='none',
  themes='theme:esd',
  para=("The core skills of archaeology degrees match the outcomes the 2021 ESD guidance proposes, such as critical, anticipatory and strategic "
        "thinking, self-awareness and collaboration. The subject can shape stories of a better future, teaches that the resource is fragile and finite "
        "and serves sustainable heritage and tourism; emphasis should go on conveying this value to society, communities and government."),
  prac=("Treat the degree's core skills as education for sustainable development and make the case for that value outside the university: to local "
        "and regional communities and to the bodies that decide what happens to the resource and heritage."),
  ben=('n/a', 'an expectation on the discipline and its teaching to make a public case; the student meets the related outcomes in 4.3.b11 and 4.4.b19'),
  aaw=(f"Describe this as an expectation (should) on the discipline to convey the value of sustainable approaches, aligned with the ESD guidance "
       f"std:doc:qaa-advancehe-esd-2021-guidance. Cite {CITE}, para 1.10. Set it beside the student items 4.3.b11, 4.4.b18 and 4.4.b19; do not claim "
       f"it is a learning outcome or that it applies at a stated level."),
  aad=("Raise this when a programme team maps sustainability across the curriculum or plans public engagement. Frame it for staff as both a "
       "curriculum link to the ESD competences and a public-facing task. Ask where students meet the finite nature of the resource and who outside "
       "the university hears the case; avoid turning it into a student requirement."))

s('1.12', type='requirement', rung='none', force='must', level='none', appliesTo='providers seeking professional accreditation of a degree',
  addressee='provider', verbs=['apply', 'demonstrate'], about='accreditation against the occupational standards', domain='none', award='none',
  themes='theme:enterprise',
  para=("The Chartered Institute for Archaeologists sets standards for the profession and, with University Archaeology UK, accredits degrees through a "
        "competency matrix tied to the occupational standards for archaeological practice (NOS); to be accredited, a provider must show that the "
        "core relevant standards are covered by the degree or pathway, and the statement already covers many of them."),
  prac=("If you seek accreditation from the professional body and its university partner, you must show that the degree or pathway covers the core "
        "relevant occupational standards through their competency matrix; mapping to this statement already covers many of them."),
  ben=('n/a', 'a condition for the provider seeking accreditation, not a standard for the student'),
  aaw=(f"Describe this as a condition (must) that the professional body sets for accreditation, reported by the statement, not a QAA requirement on "
       f"every course. Cite {CITE}, para 1.12, and name the accreditation as the scheme run jointly by CIfA and UAUK (see also paras 1.13, 2.8 and 2.27). "
       f"Do not claim that accreditation is compulsory or that the occupational standards are reproduced in this document."),
  aad=("Raise this when a programme team considers or prepares for professional accreditation, or when a student asks whether their degree is "
       "accredited. Frame it for staff as an optional route with its own matrix of competences. Ask whether the team has mapped modules to the core "
       "occupational standards; avoid telling a student it is a standard they must meet."))

s('2.6', type='requirement', rung='none', force='should', level='none', appliesTo='students, staff and curricula in archaeology',
  addressee='both', verbs=['treated', 'embed'], about='ethics of human remains and of archaeological practice', domain='understanding', award=HON,
  para=("Human remains need ethical care: all human and non-human primate remains, hominins included, should always be treated with dignity and "
        "respect, whatever their age or origin, with openness and integrity. Ethical issues also arise with illicit material, personal data, overseas "
        "fieldwork and professional conduct, and curricula should explicitly build in the ethics of practice and of archaeology's real-world uses, "
        "especially for less privileged groups and for fair engagement beyond the profession."),
  prac=("Build the ethics of practice into the curriculum explicitly: dignified and respectful treatment of human and primate remains, illicit trade, "
        "personal data, permits and local partners for work abroad, plagiarism, and the uses of archaeology for less privileged groups, using contextualised examples from around the world."),
  ben=("You should always treat human remains, and the remains of other primates, with dignity and respect, whatever their age or origin. Your course "
       "will help you think through the ethics of fieldwork, research and the way archaeology is used in the world, including its effects on less privileged groups."),
  aaw=(f"Describe this as an expectation (should) on curricula to embed the ethics of practice, and on everyone handling remains to treat them with "
       f"dignity; it states no level. Cite {CITE}, para 2.6, and set it beside the threshold items 4.3.b18 and 3.3.b17 and the professional conduct row "
       f"qaa/fheq-2024/annex-d/professional/r2/3rd-1st. Do not reproduce the CIfA or BABAO guidance or claim it is binding law."),
  aad=("Raise this before a student handles human remains or plans a project with living participants, or when a team reviews where ethics is "
       "taught. To a student, say plainly that remains are treated with dignity and that ethics runs through the course; to staff, frame it as "
       "explicit curriculum content. Ask a student what they would do if material seemed to have been traded illegally; avoid long readings of the guidance."))

s('2.12', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='every archaeologist, students included',
  addressee='learner', verbs=['use'], about='quantitative and scientific approaches in the toolkit', domain='subject-skill', award=HON,
  para=("Archaeological science applies techniques from many sciences to archaeological problems; quantitative methods, hypothesis testing and a "
        "grasp of scientific techniques should belong in every archaeologist's toolkit, in a field that is interdisciplinary and collaborative."),
  prac=("Make sure every student, whatever the course's position in the triangle, learns quantitative methods, how to test hypotheses and what "
        "scientific techniques can and cannot show."),
  ben=("You should come away able to use numbers and statistics, test a hypothesis and understand the scientific techniques archaeologists rely on, "
       "even if your interests lie mainly in the humanities."),
  aaw=(f"Describe this as an expectation (should) that scientific and quantitative skills are part of every archaeologist's equipment, for the "
       f"honours degree at FHEQ level 6. Cite {CITE}, para 2.12. Set it beside 3.2.b9, 3.3.b6 and 4.3.b4 and the descriptor qaa/fheq-2024/4.15.b2; "
       f"do not claim it is itself a threshold item or that it requires laboratory science in every course."),
  aad=("Raise this when a student on a humanities-leaning route doubts they need statistics or science, or when a team reviews methods teaching. "
       "To a student, say plainly that numbers and scientific methods are part of every archaeologist's kit; to staff, frame it as a minimum in "
       "every pathway. Ask a student which quantitative method they could use unaided today; avoid presenting the list of research themes as content they must master."))

s('2.19', type='expectation', rung='none', force='will', level='none', appliesTo='all archaeology courses',
  addressee='provider', verbs=['stress', 'seek'], about='every course stresses the contexts and practice', domain='none', award=HON,
  para=("Courses sit at different points between the humanities, the sciences and professional practice, and a department will place its single "
        "and combined honours courses differently, but all courses will stress the contexts, the interdisciplinarity and the practice that departments want students to take on."),
  prac=("Wherever your course sits between humanities, science and practice, it will still give weight to the four contexts, to working across "
        "disciplines and to the practice of archaeology as a whole."),
  ben=('n/a', 'a design expectation on every course; the student meets its effect'),
  aaw=(f"Describe this as an expectation (will) on course design, with no level of its own. Cite {CITE}, para 2.19, and read it with paras 2.2 and "
       f"2.18 on the four contexts. Do not claim it fixes a course's balance between science and humanities; the statement allows each course its own place."),
  aad=("Raise this with a programme team positioning a new course or reviewing balance between science, humanities and practice. Frame it for "
       "staff as a floor shared by all positions in the triangle. Ask how the course shows all four contexts whatever its emphasis; avoid giving it to a student as an outcome."))

s('2.20', type='expectation', rung='none', force='should', level='none', appliesTo='teaching and learning methods within a course',
  addressee='provider', verbs=['ensure', 'varied'], about='varied teaching methods so no student is disadvantaged', domain='none', award=HON,
  themes='theme:accessibility',
  para=("The methods a student meets depend on the course's aims and the wide range of skills it develops; so that students who find some formats "
        "hard are not disadvantaged, the methods in a course should be as varied as possible, drawn from a list of typical methods with adjustments for access."),
  prac=("Vary teaching and learning methods as far as you can, from lectures, seminars and tutorials to laboratory, field and placement work, so that "
        "no student is held back by one format; build in reasonable adjustments for practical and team work."),
  ben=('n/a', 'a design duty on the course; the student meets its effect'),
  aaw=(f"Describe this as an expectation (should) on teaching design under the accessibility heading; the list that follows is indicative, not "
       f"required. Cite {CITE}, para 2.20, and set it beside para 2.21 and the student item 3.3.b16. Do not claim every listed method must appear in a course."),
  aad=("Raise this when a programme team plans teaching methods or reviews access for disabled or neurodiverse students. Frame it for staff as "
       "variety for fairness, not a checklist. Ask which students a single dominant format would leave behind; avoid reading the list of methods aloud or putting the duty to a student."))

s('2.21', type='requirement', rung='none', force='must', level='none', appliesTo='teaching, assessment and extracurricular activity',
  addressee='provider', verbs=['offered', 'taken', 'agreeing', 'provided'], about='adjustments, equal access and clear assessment criteria', domain='none', award=HON,
  themes='theme:accessibility',
  para=("Teaching and assessment may be tailored for inclusion, but different formats should be open to all and expectations clear; care must be taken "
        "not to single out students with extra needs. Fieldwork adjustments for disabled students should follow individual circumstances, equal access to "
        "trips, placements and volunteering should be pursued given hidden costs, cultural views of assessment should be remembered, and clear, accessible "
        "guidance on assessment criteria at each stage must be provided."),
  prac=("Offer alternative formats to everyone rather than only to those who ask, and make expectations plain; you must avoid a two-tier system. "
        "Agree fieldwork adjustments case by case, work to remove hidden costs from field trips, placements and volunteering, consider religious "
        "observance and school holidays in deadlines, and you must publish clear, accessible assessment criteria for each stage."),
  ben=('n/a', 'a duty on the course and its assessors; the student meets its effect'),
  aaw=(f"Describe this as a provider duty (must, with several shoulds) on inclusive teaching, access and assessment criteria; it states no level. "
       f"Cite {CITE}, para 2.21, and set it beside paras 2.20, 3.10 and 1.9. Do not claim the statement creates a legal duty or that it sets out the adjustments for a given student."),
  aad=("Raise this with a programme team reviewing fieldwork, extracurricular access or assessment information, or with a teacher agreeing an "
       "adjustment. Frame it for staff around the two musts: no two-tier system and clear criteria at each stage. Ask whether alternative formats "
       "are offered to all and whether field trip costs exclude anyone; avoid presenting it to a student as their obligation."))

s('2.23', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='joint honours students with archaeology',
  addressee='learner', verbs=['achieve', 'add'], about='joint honours reach part of the skills and add others', domain='none', award=HON,
  para=("Students on joint honours routes, such as archaeology with anthropology or with classics, will reach only some of the subject-specific and "
        "generic skills and will add others from their partner subject; they usually do less laboratory science and fieldwork, though not where the partner is a STEM or social science subject."),
  prac=("For joint honours, expect students to achieve a share of this statement's specific and generic skills and to add others from the partner "
        "subject; decide which, and expect less laboratory and field work unless the partner is a science or social science."),
  ben=("If you study archaeology jointly with another subject, you will gain some of the archaeological skills and add others from your second "
       "subject; you may do less laboratory and field work, unless your other subject is a science."),
  aaw=(f"Describe this as an expected outcome (will) for joint honours at FHEQ level 6: a proportion of the skills in 3.2, 3.3, 4.3 and 4.4, not all of them. "
       f"Cite {CITE}, para 2.23, and read it with para 1.7. Do not claim it names which skills a joint honours student keeps; the course decides that."),
  aad=("Raise this when a joint honours student asks which archaeology outcomes apply to them, or when a team designs a joint route. To a student, "
       "say plainly that they will cover part of the archaeology skills and gain others from their second subject; to staff, ask which items the route "
       "will evidence. Ask a student which skills they expect from each subject; avoid implying the threshold lists apply in full."))

s('3.9', type='requirement', rung='none', force='will', level='none', appliesTo='each archaeology course',
  addressee='provider', verbs=['contains', 'reflect', 'support', 'enable'], about='an explicit assessment strategy', domain='none', award=HON,
  para=("Every archaeology course has an explicit assessment strategy in its design, which will mirror the outcomes of its components, support "
        "learning, let students show rising levels of attainment and reflect the range of abilities and the teaching methods used."),
  prac=("Write an explicit assessment strategy into the curriculum: it will map to each component's outcomes, support learning, show progression "
        "in attainment and match the skills developed and the teaching methods chosen."),
  ben=('n/a', 'a design duty on the course; the student meets its effect'),
  aaw=(f"Describe this as a course design expectation (will) for assessment; it sets no level. Cite {CITE}, para 3.9, and set it beside para 3.10, the "
       f"indicative list in 3.11 and the classification descriptions in Annex D (std:doc:qaa-fheq-2024-framework, SL6). Do not claim it prescribes particular methods."),
  aad=("Raise this when a programme team reviews its assessment strategy or a validation panel asks how outcomes are assessed. Frame it for staff "
       "as alignment, progression and fit with teaching. Ask where in the course a student's growing attainment becomes visible; avoid giving it to a student as their task."))

s('4.2', type='requirement', rung='none', force='should', level='fheq:6', appliesTo='honours degree-awarding providers',
  addressee='provider', verbs=['perform', 'refer'], about='using Annex D above the threshold', domain='none', award=HON,
  para=("Most students will do much better than the minimum threshold; each provider decides how to evidence this and should refer to Annex D, "
        "which describes the four honours classes (1st, 2:1, 2:2, 3rd) at level 6 of the FHEQ, level 10 in Scotland."),
  prac=("Above the threshold, judge performance with your own method and refer to Annex D's outcome classification descriptions for the four "
        "honours classes; this statement gives no typical or excellent lists of its own."),
  ben=('n/a', 'a duty on the awarding body for judging classes above the threshold'),
  aaw=(f"Describe this as a provider expectation (should) to use Annex D for performance above the threshold at FHEQ level 6 and FQHEIS level 10. "
       f"Cite {CITE}, para 4.2, and point to std:doc:qaa-fheq-2024-framework, Annex D (SL6), for example qaa/fheq-2024/annex-d/summary/r1/3rd. "
       f"Do not claim the statement sets subject-specific typical or excellent standards; it states the threshold only."),
  aad=("Raise this when a team or student asks what separates a first from a third in archaeology. To staff, say the statement stops at the "
       "threshold and points to Annex D for the classes; to a student, explain that most people do much better than the minimum. Ask which "
       "Annex D descriptions the team's marking criteria follow; avoid presenting the threshold as the expected result."))

# ---- 3.2 subject-specific content (lead-in: as appropriate to the course, students will be equipped to)
AAW32 = ("Describe this as an expected subject-specific outcome (will) of the honours degree at FHEQ level 6, scaled to the breadth and depth of "
         "the course: {about}. Cite " + CITE + ", para 3.2 (bullet {k}). Set it beside {nb} and the level 6 descriptor {fw}; do not report it as a "
         "threshold item, which section 4 holds, or as applying in full where archaeology is a minor part (para 1.7).")
AAD32 = ("Raise this when {when}. To a student, put it plainly in the second person as something the course will equip them to do; to staff, frame "
         "it as a subject-specific outcome to evidence across modules. Ask {q} Avoid reading the issuer's bullet aloud or presenting it as a pass "
         "requirement, since the threshold lists sit in section 4.")
def k32(k, verbs, about, domain, para, prac, ben, nb, fw, when, q, find=None):
    r = dict(type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students of the subject, as the course allows',
             addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben,
             aaw=AAW32.format(about=about, k=k, nb=nb, fw=fw), aad=AAD32.format(when=when, q=q))
    if find:
        r['find'] = find
    P['3.2.b%d' % k] = r

k32(1, ['evaluate', 'challenge', 'apply'], 'critical use of scholarly, theoretical and scientific ideas', 'subject-skill',
    "Judge, contest and use suitable scholarly, theoretical and scientific principles when tackling archaeological problems.",
    "Students will weigh, question and apply scholarly, theoretical and scientific concepts to archaeological problems.",
    "You will be able to judge, question and use scholarly, theoretical and scientific ideas when you work on archaeological problems.",
    '4.3.b6 and 4.4.b6', 'qaa/fheq-2024/4.15.b7', 'a student asks how theory connects to the problems they meet in fieldwork or the laboratory',
    'which theory they last applied to a real archaeological problem, and how they tested it?')
k32(2, ['practise', 'observe', 'record', 'interpret'], 'core fieldwork techniques', 'subject-skill',
    "Use the core techniques of fieldwork to observe, record and interpret primary evidence, with adjustments where a disabled student needs them.",
    "Students will practise the main field techniques for observing, recording and interpreting primary evidence; plan reasonable adjustments for disabled students.",
    "You will practise the main fieldwork techniques for observing, recording and interpreting evidence on site, with adjustments if you need them.",
    '4.3.b5 and 4.3.b13', 'qaa/fheq-2024/4.15.b2', 'a student prepares for fieldwork or a team plans field training and its adjustments',
    'which field techniques the student could carry out unsupervised, and what adjustment, if any, would help them take part?')
k32(3, ['practise'], 'post-excavation and post-survey techniques', 'subject-skill',
    "Use the core techniques that follow excavation or survey, such as analysing stratigraphy from field records, phasing and archiving.",
    "Students will practise core post-excavation and post-survey work: stratigraphic analysis of records, phasing and archiving.",
    "You will practise the work that follows excavation or survey, such as working out the sequence of layers from records, phasing a site and preparing an archive.",
    '3.2.b2 and 4.3.b13', 'qaa/fheq-2024/4.15.b2', 'a student asks what happens to finds and records after a dig, or a team reviews post-excavation teaching',
    'whether the student has ever phased a site from its records, and what they found hardest?')
k32(4, ['practise'], 'recording, measuring and analysing material and data', 'subject-skill',
    "Use core techniques to record, measure, analyse and interpret archaeological material and data.",
    "Students will practise core techniques for recording, measuring, analysing and interpreting archaeological material and data.",
    "You will practise recording, measuring, analysing and interpreting archaeological material and data.",
    '4.3.b13 and 4.4.b16', 'qaa/fheq-2024/4.15.b2', 'a student works with finds or datasets in a practical class or project',
    'which recording or measuring method the student trusts most, and why?')
k32(5, ['recognise', 'communicate'], 'the significance of remains, landscapes and environmental data', 'subject-skill',
    "See and explain why material remains, landscapes and environmental data matter archaeologically.",
    "Students will recognise and convey the archaeological importance of material remains, landscapes and environmental evidence.",
    "You will be able to see why remains, landscapes and environmental evidence matter to archaeology, and explain this to others.",
    '4.3.b7 and 3.3.b10', 'qaa/fheq-2024/4.15.b8', 'a student must explain to a non-specialist why a site, landscape or sample matters',
    'how the student would explain the importance of one find or landscape to a visitor in two sentences?', find=FINDS['3.2.b5'])
k32(7, ['interpret', 'integrating'], 'interpreting spatial data', 'subject-skill',
    "Read spatial data by combining theoretical models, the traces left in today's landscapes and the results of excavation.",
    "Students will interpret spatial data, combining theoretical models, surviving landscape traces and excavation results.",
    "You will be able to interpret spatial data by bringing together models, what survives in today's landscape and what excavation shows.",
    '3.2.b5 and 4.3.b9', 'qaa/fheq-2024/4.15.b3.1', 'a student works with maps, survey or GIS data, or a team plans landscape teaching',
    'which kinds of spatial evidence the student has combined so far, and where they disagreed?')
k32(8, ['observe', 'record'], 'describing and recording classes of primary data', 'subject-skill',
    "Look at and describe different kinds of primary data and record their features by set methods.",
    "Students will observe and describe classes of primary data and record their characteristics by defined methods.",
    "You will be able to observe and describe different kinds of primary evidence and record their features using set methods.",
    '4.4.b15 and 4.4.b16', 'qaa/fheq-2024/4.15.b2', 'a student starts handling a class of finds or samples for the first time',
    'which recording system the student used and how they checked their descriptions were consistent?')
k32(9, ['select', 'apply', 'process', 'recognising'], 'choosing qualitative, quantitative and statistical analyses', 'subject-skill',
    "Choose and use suitable qualitative, quantitative and statistical methods to process data, knowing what each can and cannot show.",
    "Students will select and apply qualitative, quantitative and statistical analyses to data and recognise their potential and limits.",
    "You will be able to choose and use the right qualitative, numerical and statistical methods for your data, and know what each method can and cannot tell you.",
    '2.12, 3.3.b6 and 4.3.b4', 'qaa/fheq-2024/4.15.b2', 'a student plans the analysis for a dissertation or a practical report',
    'why the student chose their method, and what it could not show?')
k32(10, ['understand', 'shaped'], 'change in coupled socio-ecological systems', 'understanding',
    "Grasp how social, cultural and environmental factors interact to drive change in linked social and ecological systems, and how people have shaped and been shaped by them through human evolution.",
    "Students will understand how social, cultural and environmental factors combine to cause change, and the two-way relation between people and environment over human evolution.",
    "You will understand how social, cultural and environmental factors work together to bring about change, and how people have both shaped and been shaped by their surroundings over human history.",
    '3.2.b14 and 4.4.b20', 'qaa/fheq-2024/4.15.b1', 'a student links archaeology to climate, environment or long-term change',
    'what example of human and environmental change the student would use, and which factor they think mattered most?')
k32(11, ['understand'], 'human diversity, present and past', 'understanding',
    "Understand the extent and nature of human diversity today and in the past, and some of its causes, from several perspectives.",
    "Students will understand the nature, scope and some causes of human diversity, past and present, from social, cultural, ecological, biological and temporal angles.",
    "You will understand how varied people are and have been, and some of the reasons why, looked at from social, cultural, ecological, biological and long-term points of view.",
    '4.3.b17 and 4.4.b20', 'qaa/fheq-2024/4.15.b1', 'a topic on identity, population or difference comes up in teaching or a project',
    'which perspective on human diversity the student finds most convincing, and which they have not yet used?')
k32(12, ['identify', 'question'], 'questioning cultural assumptions, including colonial legacies', 'subject-skill',
    "Spot and challenge cultural assumptions in varied settings, including those still marked by colonialism.",
    "Students will be able to spot and challenge cultural assumptions in different settings, including those shaped by colonial legacies.",
    "You will be able to notice and challenge cultural assumptions in many settings, including those still shaped by colonialism.",
    '4.3.b15, 4.3.b16 and 4.4.b18', 'qaa/fheq-2024/4.15.b7', 'a student reads an older interpretation, a museum label or a reading list critically',
    'which assumption the student found in a source this term, and where it came from?')
k32(13, ['interpret', 'analyse'], 'interpreting textual, oral, visual and digital forms', 'subject-skill',
    "Interpret and analyse many kinds of sources: written, spoken, visual and digital.",
    "Students will be able to interpret and analyse textual, oral, visual and digital forms of evidence.",
    "You will be able to interpret and analyse written, spoken, visual and digital sources.",
    '4.3.b9 and 4.4.b3', 'qaa/fheq-2024/4.15.b5', 'a student combines documents, oral history, images or digital records with material evidence',
    'which kind of source the student is least used to, and how they would start to analyse it?')
k32(14, [], 'how biology, environment and culture interact in human ecology', 'knowledge',
    "Know how biological, environmental and social or cultural influences interact in human ecology.",
    "Students will know how biological, environmental and social or cultural factors interact in human ecology.",
    "You will know how biology, environment and society and culture affect one another in the way people live in their surroundings.",
    '3.2.b10', 'qaa/fheq-2024/4.15.b1', 'a student meets diet, health or environmental evidence in a module',
    'how the student would show one biological and one cultural influence acting together in a case study?')
k32(15, ['evaluate', 'compare', 'synthesise'], 'weighing and combining different evidence about behaviour', 'subject-skill',
    "Assess, compare and bring together different forms of evidence to interpret human behaviour, past and present.",
    "Students will be able to evaluate, compare and synthesise varied forms of evidence to interpret human behaviour past and present.",
    "You will be able to judge, compare and combine different kinds of evidence to reach interpretations about how people behaved and behave.",
    '4.3.b8, 4.4.b3 and 4.4.b7', 'qaa/fheq-2024/4.15.b3.1', 'a student writes an interpretation that draws on more than one kind of evidence',
    'where two lines of the student\'s evidence pointed different ways, and how they decided?')
k32(16, ['evaluate', 'use'], 'ethics of the discipline and modes of communication', 'understanding',
    "Know the ethical issues around the discipline's legacy and uses, and critically assess and use fitting ways of communicating and engaging.",
    "Students will be aware of ethical issues in the legacy and uses of archaeology and will critically evaluate and use suitable modes of communication and engagement.",
    "You will know the ethical questions raised by archaeology's past and its uses today, and be able to judge and use good ways of communicating and engaging with people.",
    '2.6, 4.3.b18 and 3.3.b10', 'qaa/fheq-2024/4.15.b8', 'a student plans public engagement or writes about a contested site',
    'who could be affected by the student\'s account, and how they would involve them?')
k32(17, ['understand'], 'legislative and planning context', 'knowledge',
    "Understand the wider legal and planning setting in which archaeological work may happen, now and in the past.",
    "Students will understand the legislative and planning context of archaeological work, present and historical.",
    "You will understand the laws and planning rules that shape where and how archaeological work happens, now and in the past.",
    '1.6 and 4.3.b18', 'qaa/fheq-2024/4.15.b1', 'a student asks how development-led or commercial archaeology works, or a team plans professional practice teaching',
    'which law or planning rule the student would need to check before work on a site?', find=FINDS['3.2.b17'])

# ---- 3.3 generic, transferable and employability content (lead-in: graduates will be equipped with)
AAW33 = ("Describe this as an expected generic, transferable skill (will) of honours graduates in archaeology at FHEQ level 6: {about}; it refines "
         "the level 6 descriptor {fw}. Cite " + CITE + ", para 3.3 (bullet {k}). Set it beside {nb}; do not claim it is a threshold item, a skill "
         "only archaeology teaches or a standard at another level.")
AAD33 = ("Raise this when {when}. To a student, say in plain words and the second person that the degree will build this skill and where it shows; "
         "to staff, frame it as a transferable outcome to make visible in modules and placements. Ask {q} Avoid reading the issuer's wording aloud or "
         "turning it into a separate assessed hurdle.")
def k33(k, verbs, about, para, prac, ben, nb, fw, when, q):
    P['3.3.b%d' % k] = dict(type='outcome', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject',
                            addressee='learner', verbs=verbs, about=about, domain='generic-skill', award=HON, para=para, prac=prac, ben=ben,
                            aaw=AAW33.format(about=about, k=k, nb=nb, fw=fw), aad=AAD33.format(when=when, q=q))

k33(1, ['develop', 'drawing'], 'creative problem solving across humanities and sciences',
    "Solve problems by lateral and creative thinking in practical and theoretical settings, using methods from the humanities and sciences.",
    "Graduates will solve problems creatively and laterally in practical and theoretical work, using techniques from both humanities and sciences.",
    "You will be able to solve problems creatively, thinking sideways and using methods from both the humanities and the sciences, in practical and theoretical work.",
    '4.4.b4', 'qaa/fheq-2024/4.15.b9.2', 'a student is stuck on a project problem or a team designs problem-based tasks',
    'which method from outside their usual area the student could try?')
k33(2, ['producing'], 'structured, evidenced argument',
    "Build logical, well-ordered arguments backed by analytical and critical use of relevant evidence.",
    "Graduates will produce logical, structured arguments supported by analytical and critical reference to evidence.",
    "You will be able to build clear, logical arguments that rest on careful, critical use of evidence.",
    '4.4.b11 and 4.3.b8', 'qaa/fheq-2024/4.15.b3.1', 'a student plans an essay or receives feedback on argument',
    'what the strongest objection to the student\'s argument is, and where their evidence answers it?')
k33(3, ['planning', 'designing', 'executing', 'documenting', 'working'], 'designing and carrying out primary research',
    "Plan, design, carry out and record a programme of primary research, alone or with others as fits.",
    "Graduates will plan, design, carry out and document primary research, independently and collaboratively as appropriate.",
    "You will be able to plan, design, carry out and write up your own primary research, working alone or with others as the task needs.",
    '4.3.b12 and 3.3.b4', 'qaa/fheq-2024/4.15.b6', 'a student starts a dissertation or independent project',
    'what the student\'s research question is and how their design will answer it?')
k33(4, ['assembling'], 'coherent research or project designs',
    "Put together coherent designs for research or projects.",
    "Graduates will assemble coherent research and project designs.",
    "You will be able to put together a clear, workable design for a research project.",
    '3.3.b3 and 3.3.b15', 'qaa/fheq-2024/4.15.b6', 'a student drafts a project proposal',
    'whether each part of the student\'s design serves the question, and what they would cut?')
k33(5, ['evaluating'], 'critical evaluation of own and others\' views',
    "Assess one's own and others' views critically, informed by archaeology's changing theoretical, methodological, professional, ethical and social settings.",
    "Graduates will evaluate their own and others' opinions critically in the light of the discipline's changing contexts.",
    "You will be able to judge your own and other people's views critically, aware of how archaeology's theory, methods, ethics and social setting keep changing.",
    '4.4.b6', 'qaa/fheq-2024/4.15.b7', 'a student reviews literature or peer work, or reflects on a debate',
    'which of the student\'s own views has changed during the course, and why?')
k33(6, ['applying'], 'quantitative analysis and digital literacy in practice',
    "Use quantitative analysis and digital skills in practical work.",
    "Graduates will apply quantitative analysis and digital literacy in practical contexts.",
    "You will be able to use numerical analysis and digital skills in practical work.",
    '2.12, 3.2.b9 and 4.4.b12', 'qaa/fheq-2024/annex-d/transferable/r1/3rd', 'a student handles data in a practical or project',
    'which software or numerical method the student used last and how confident they felt?')
k33(7, ['demonstrating'], 'a positive approach to practical problems',
    "Meet practical problems with a confident, positive attitude.",
    "Graduates will show a positive, confident approach to practical problems.",
    "You will meet practical problems with confidence and a positive attitude.",
    '3.3.b1', 'qaa/fheq-2024/4.15.b9.1', 'a student faces a setback in fieldwork or a practical task',
    'how the student responded to the last practical problem that did not go to plan?')
k33(8, ['demonstrating'], 'innovation, creativity, collaboration and risk-taking',
    "Show an inventive approach, creativity, cooperation and a willingness to take risks.",
    "Graduates will show innovation, creativity, collaboration and readiness to take risks.",
    "You will show that you can be inventive and creative, work with others and take sensible risks.",
    '3.3.b1 and 3.3.b16', 'qaa/fheq-2024/4.15.b9.1', 'enterprise, placements or creative assessment come up',
    'where in the course the student has tried something new, and what they learned from it?')
k33(9, ['presenting'], 'presenting to different audiences',
    "Give effective presentations to varied audiences.",
    "Graduates will present effectively to different kinds of audience.",
    "You will be able to give effective presentations to different kinds of audience.",
    '4.4.b13 and 3.3.b10', 'qaa/fheq-2024/4.15.b8', 'a student prepares a talk, poster or public event',
    'who the student\'s audience is and what they would change for a different one?')
k33(10, ['communicating', 'creating'], 'communicating in many media, including visual',
    "Communicate well with many audiences in written, spoken and other media, and produce effective, suitable visual presentation.",
    "Graduates will communicate effectively with wide audiences through written, oral and other media and create suitable visual presentations.",
    "You will be able to communicate well with many kinds of audience in writing, in speech and in other media, and make effective visual material.",
    '4.4.b10 and 3.2.b5', 'qaa/fheq-2024/4.15.b8', 'a student plans how to present findings in more than one format',
    'which medium suits the student\'s findings best, and which they find hardest?')
k33(11, ['making'], 'digital technology and software for digital data',
    "Use relevant digital technology and software well and suitably to handle digital data.",
    "Graduates will make effective and appropriate use of relevant digital technology and software to manipulate digital data.",
    "You will be able to use the right digital tools and software to work with digital data.",
    '3.3.b6 and 4.4.b12', 'qaa/fheq-2024/annex-d/transferable/r1/3rd', 'a student works with GIS, databases, imaging or modelling',
    'which digital tool the student would choose for their data and why?')
k33(12, ['making', 'using'], 'information retrieval from analogue and digital resources',
    "Find information critically and effectively from analogue and digital sources.",
    "Graduates will make critical and effective use of information retrieval skills across analogue and digital resources.",
    "You will be able to find information well and critically, in print and archives as well as online.",
    '4.4.b3', 'qaa/fheq-2024/4.15.b5', 'a student starts a literature search or archival work',
    'how the student judged the reliability of the last source they found?')
k33(13, ['working'], 'method, accuracy and attention to detail',
    "Work methodically and accurately, paying attention to detail.",
    "Graduates will work methodically and accurately with attention to detail.",
    "You will be able to work carefully, accurately and with attention to detail.",
    '4.4.b16 and 3.2.b8', 'qaa/fheq-2024/annex-d/practical/r2/3rd', 'a student records finds, data or references',
    'how the student checks their own records for errors?')
k33(14, ['reflecting', 'accessing'], 'continuing professional and personal development',
    "Reflect on and act early to seek continuing professional and personal development.",
    "Graduates will reflect on and take initiative in seeking continuing professional and personal development.",
    "You will be able to reflect on your own development and take the lead in finding ways to keep learning, personally and professionally.",
    '4.4.b9', 'qaa/fheq-2024/4.15.b9.3', 'careers, placements or personal tutoring come up',
    'what the student wants to learn next and where they will find it?')
k33(15, ['assembling'], 'time management, organisation and planning',
    "Manage time, organise and plan, including putting together coherent research or project designs.",
    "Graduates will manage time, organise and plan, which includes putting together coherent project designs.",
    "You will be able to manage your time, organise yourself and plan work, including designing a research project.",
    '3.3.b4 and 4.4.b8', 'qaa/fheq-2024/annex-d/transferable/r3/3rd', 'a student juggles deadlines or plans a long project',
    'how the student has planned the stages of their project against the deadline?')
k33(16, [], 'teamwork in laboratory, field or project',
    "Work well in a team through group experience in the laboratory, the field or project work, with reasonable adjustments if needed.",
    "Graduates will collaborate effectively in teams through group work in laboratory, field or project settings, with reasonable adjustments if required.",
    "You will be able to work well as part of a team, in the laboratory, in the field or on a project, with adjustments if you need them.",
    '4.4.b2 and 2.20', 'qaa/fheq-2024/annex-d/transferable/r2/3rd', 'a student meets a group task or a team dispute',
    'what role the student took in their last group task and what they would do differently?')
k33(17, [], 'ethics, health and safety and professional frameworks',
    "Value ethical and health and safety procedures and duties, for oneself and others, and wider professional frameworks and policies.",
    "Graduates will appreciate ethical and health and safety procedures and responsibilities, personal and towards others, and broader professional frameworks.",
    "You will understand why ethics and health and safety rules matter, for you and for others, and how wider professional frameworks apply to your work.",
    '2.6, 4.3.b18 and 4.4.b17', 'qaa/fheq-2024/annex-d/professional/r2/3rd-1st', 'a student prepares for fieldwork, laboratory work or a placement',
    'which risk the student would check for first on a site, and who else it affects?')
k33(18, ['taking', 'making'], 'inclusiveness and respect for others and cultures',
    "Value inclusion, respond with sensitivity and act early, owning the duty to see that diverse people and cultures are respected.",
    "Graduates will appreciate the need for inclusiveness and take personal responsibility for respecting diverse people and cultures.",
    "You will value inclusion and take personal responsibility for making sure that people from different backgrounds and cultures are respected.",
    '1.8, 4.3.b17 and 4.4.b17', 'qaa/fheq-2024/4.15.b9.1', 'a group, fieldwork or outreach setting raises questions of respect or exclusion',
    'what the student does when someone in a group is left out?')
k33(19, ['engaging'], 'the wider cultural context of professional practice',
    "Engage with the wider cultural setting of professional practice in any field, such as equality, diversity and inclusion, sustainability, global views, inequality, public engagement, employability, enterprise and creativity.",
    "Graduates will engage with the broader cultural context of professional practice, for example EDI, sustainability, global perspectives, inequality, public engagement, employability, enterprise and creativity.",
    "You will be able to engage with the wider issues that shape professional life in any field, such as inclusion, sustainability, global views, inequality, public engagement, employability and enterprise.",
    '4.4.b18 and 4.4.b20', 'qaa/fheq-2024/4.15.b9.1', 'careers, employability or the cross-cutting themes come up',
    'which of these wider issues the student could speak about in a job interview?')

# ---- 4.3 threshold: subject knowledge, understanding and skills (lead-in: on graduating with honours, students should be able to)
AAW43 = ("Describe this as a threshold standard: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 "
         "(FQHEIS level 10); it covers {about}. Cite " + CITE + ", para 4.3 (bullet {k}). Set it beside {nb}, the descriptor {fw} and the "
         "third-class column of Annex D ({ad}); do not claim it is a regulatory rule, the typical result or a standard at another level.")
AAD43 = ("Raise this when {when}. To a student, put it plainly in the second person as part of the minimum the degree asks by graduation; to staff, "
         "frame it as a threshold their assessments must let every student show. Ask {q} Avoid reading the list aloud or treating this minimum as the "
         "class of degree most students reach.")
def k43(k, verbs, about, domain, para, prac, ben, nb, fw, ad, when, q, find=None):
    r = dict(type='threshold', rung='threshold', force='should', level='fheq:6', appliesTo='honours graduates in archaeology',
             addressee='learner', verbs=verbs, about=about, domain=domain, award=HON, para=para, prac=prac, ben=ben,
             aaw=AAW43.format(about=about, k=k, nb=nb, fw=fw, ad=ad), aad=AAD43.format(when=when, q=q))
    if find:
        r['find'] = find
    P['4.3.b%d' % k] = r

KN, UN, SK = 'knowledge', 'understanding', 'subject-skill'
ADK1, ADK2, ADK3 = ('qaa/fheq-2024/annex-d/knowledge/r%d/3rd' % i for i in (1, 2, 3))
ADP1, ADP4 = 'qaa/fheq-2024/annex-d/practical/r1/3rd', 'qaa/fheq-2024/annex-d/practical/r4/3rd'
ADPRO = 'qaa/fheq-2024/annex-d/professional/r2/3rd-1st'

k43(1, ['appreciate'], 'the time span and conceptual range of the discipline', UN,
    "Grasp how far archaeology reaches in time and in the ideas it works with.",
    "At threshold, graduates appreciate the chronological and conceptual reach of archaeological work.",
    "By graduation you should be able to show that you grasp how far archaeology reaches across time and across ideas.",
    '4.3.b14 and 3.2.b10', 'qaa/fheq-2024/4.15.b1', ADK2, 'a student asks what the degree expects them to know overall',
    'which period or idea the student feels furthest from, and how they would place it in the whole?')
k43(2, ['demonstrate'], 'regional breadth', KN,
    "Show knowledge of the archaeology of several geographical regions.",
    "At threshold, graduates show knowledge of the archaeology of several regions of the world.",
    "By graduation you should be able to show that you know the archaeology of several parts of the world.",
    '4.3.b3 and para 1.6', 'qaa/fheq-2024/4.15.b1', ADK1, 'a student chooses modules or asks if their regional coverage is wide enough',
    'which regions the student could discuss with confidence, and which they have barely met?')
k43(3, ['demonstrate'], 'period breadth', KN,
    "Show knowledge of the archaeology of several chronological periods.",
    "At threshold, graduates show knowledge of the archaeology of several periods.",
    "By graduation you should be able to show that you know the archaeology of several periods of the past.",
    '4.3.b2 and para 1.6', 'qaa/fheq-2024/4.15.b1', ADK1, 'a student chooses modules or asks if their period coverage is wide enough',
    'which periods the student could compare, and on what point?')
k43(4, ['demonstrate', 'acquired', 'analysed'], 'how data are gathered and analysed', UN,
    "Show understanding of the principles and methods for obtaining and analysing archaeological data.",
    "At threshold, graduates understand the principles and methods by which archaeological data are obtained and analysed.",
    "By graduation you should be able to show that you understand how archaeologists collect and analyse their data, and why.",
    '3.2.b9 and 2.12', 'qaa/fheq-2024/4.15.b2', ADK2, 'a student plans data collection or a team checks methods teaching',
    'how the student would explain one method of collecting data and its weaknesses?')
k43(5, ['demonstrate'], 'practical experience of recovering primary data', SK,
    "Show hands-on experience of recovering primary archaeological data.",
    "At threshold, graduates show practical experience of recovering primary data, in the field or (with adjustments, per 1.6) through collections or records.",
    "By graduation you should be able to show hands-on experience of recovering primary archaeological evidence.",
    '3.2.b2 and 4.3.b13', 'qaa/fheq-2024/4.15.b2', ADP1, 'a student cannot take part in standard fieldwork or asks how practical experience is evidenced',
    'what primary data the student has recovered themselves, and in what setting?')
k43(6, ['describe'], 'theoretical and practical approaches to the past', UN,
    "Describe the range of theoretical and practical ways of understanding, constructing and interpreting the past.",
    "At threshold, graduates describe the variety of theoretical and practical approaches to understanding and interpreting the past.",
    "By graduation you should be able to describe the different theoretical and practical ways archaeologists understand and build accounts of the past.",
    '3.2.b1 and 4.3.b14', 'qaa/fheq-2024/4.15.b3.1', ADK2, 'a student studies archaeological theory or compares interpretations',
    'which two approaches the student could contrast, and what each would make of the same site?')
k43(7, ['recognise'], 'the range of data, including other disciplines', KN,
    "Recognise the range of archaeological data and of relevant data from other subjects.",
    "At threshold, graduates recognise the full range of archaeological evidence and useful data from other disciplines.",
    "By graduation you should be able to recognise the many kinds of archaeological evidence, and useful evidence from other subjects.",
    '4.3.b10 and 3.2.b13', 'qaa/fheq-2024/4.15.b1', ADK1, 'a student plans which evidence a project will draw on',
    'which non-archaeological evidence could help the student\'s question?')
k43(8, ['describe', 'understand'], 'the problems, possibilities and limits of evidence', UN,
    "Describe why archaeological evidence is varied and problematic, and understand what it can and cannot show.",
    "At threshold, graduates describe the varied and problematic nature of evidence and understand its possibilities and limits.",
    "By graduation you should be able to explain why archaeological evidence is varied and often difficult, and what it can and cannot tell you.",
    '3.2.b9 and para 1.6 on bias', 'qaa/fheq-2024/4.15.b4', ADK2, 'a student over-reads a find or a dataset',
    'what the student\'s evidence cannot show, and how that limits their conclusion?')
k43(9, ['gather', 'analyse', 'present'], 'working with primary and secondary evidence', SK,
    "Collect, analyse and present archaeological evidence from primary and secondary sources.",
    "At threshold, graduates gather, analyse and present evidence from primary and secondary sources.",
    "By graduation you should be able to collect, analyse and present archaeological evidence from both original and published sources.",
    '4.3.b12 and 3.3.b3', 'qaa/fheq-2024/4.15.b5', ADP4, 'a student starts a project or report',
    'which primary and which secondary sources the student is using, and how they will present them?')
k43(10, ['recognise'], 'the range of archaeological data (repeat of b7)', KN,
    "Recognise the range of archaeological data; this repeats the first half of bullet 7.",
    "At threshold, graduates recognise the range of archaeological data (the issuer repeats this within bullet 7).",
    "By graduation you should be able to recognise the many kinds of archaeological evidence.",
    '4.3.b7, which it repeats', 'qaa/fheq-2024/4.15.b1', ADK1, 'a student lists the kinds of evidence a site might give',
    'which kinds of evidence the student would expect from a site they know?')
k43(11, ['recognise'], 'a finite resource needing sustainable conservation', UN,
    "Recognise that the archaeological resource is finite and needs to be conserved sustainably.",
    "At threshold, graduates recognise that the resource is finite and that it needs sustainable conservation.",
    "By graduation you should be able to recognise that archaeological remains cannot be replaced and must be conserved in a sustainable way.",
    'para 1.10, 4.4.b19 and 3.3.b19', 'qaa/fheq-2024/4.15.b1', ADK2, 'sustainability, conservation or excavation ethics come up',
    'why excavation itself uses up the resource, and what that means for the student\'s choices?')
k43(12, ['research', 'present'], 'an extended piece of research', SK,
    "Carry out and present a substantial piece of archaeological research of one's own.",
    "At threshold, graduates research and present an extended piece of archaeological work, often a dissertation or project (2.26).",
    "By graduation you should be able to carry out and present an extended piece of archaeological research of your own.",
    '3.3.b3, 3.3.b4 and para 2.26', 'qaa/fheq-2024/4.15.b6', ADK3, 'a student plans a dissertation or independent project',
    'what the student\'s question is and how far along their research is?')
k43(13, ['demonstrate'], 'observing, recording and interpreting primary data', SK,
    "Show knowledge of archaeological and practical skills, above all in observing, recording and interpreting primary data.",
    "At threshold, graduates show knowledge of archaeological and practical skills, especially observing, recording and interpreting primary data.",
    "By graduation you should be able to show your practical archaeological skills, especially in observing, recording and interpreting original evidence.",
    '4.3.b5, 3.2.b2 and 3.2.b8', 'qaa/fheq-2024/4.15.b2', ADP1, 'a student prepares a field or laboratory notebook for assessment',
    'how the student would show an assessor that their recording is accurate?')
k43(14, ['describe', 'understand'], 'the development of the discipline', KN,
    "Describe how archaeology developed as a subject and understand what that means for the discipline now and its cultural setting.",
    "At threshold, graduates describe how archaeology developed as a subject and understand what that means for it today and for its cultural setting.",
    "By graduation you should be able to describe how archaeology grew as a subject and what that history means for it today.",
    '4.3.b6 and para 2.11 (fourth element)', 'qaa/fheq-2024/4.15.b1', ADK2, 'a student studies the history of the discipline or its colonial origins',
    'which part of the subject\'s history still shapes practice the student has seen?')
k43(15, ['demonstrate'], 'the social, cultural and political context', UN,
    "Show awareness of the social, cultural and political setting of archaeological interpretation and practice.",
    "At threshold, graduates show awareness of the social, cultural and political context of interpretation and practice.",
    "By graduation you should be able to show that you know how society, culture and politics shape archaeological interpretation and practice.",
    '3.2.b12 and 4.3.b16', 'qaa/fheq-2024/4.15.b4', ADK2, 'a student writes about a contested site or a political use of the past',
    'who gains from a given interpretation of the past the student has studied?')
k43(16, ['demonstrate', 'appreciate', 'engage'], 'impact on communities and fair engagement', UN,
    "Show awareness of how archaeological practice, interpretation and representation affect other communities, including historically marginalised groups, and appreciate the need to engage fairly with those affected.",
    "At threshold, graduates show awareness of the effect of practice and representation on other communities, including marginalised groups, and appreciate the need for equitable engagement with them.",
    "By graduation you should be able to show that you understand how archaeology can affect other communities, including groups pushed to the margins in the past, and why you need to work with them fairly.",
    'para 1.8, 4.3.b15 and 4.3.b17', 'qaa/fheq-2024/4.15.b9.2', ADK2, 'a student plans community work, writes on contested heritage or handles material from another culture',
    'which community the student\'s work might affect, and how they would involve them?', find=FINDS['4.3.b16'])
k43(17, ['understand', 'accord'], 'an inclusive discipline and respect for others', UN,
    "Understand why the discipline must be inclusive and give respect to diverse others inside and outside archaeology.",
    "At threshold, graduates understand why the discipline must be inclusive and show respect to diverse others.",
    "By graduation you should be able to show that you understand why archaeology needs to include everyone, and that you treat people from different backgrounds with respect.",
    '3.3.b18 and 4.4.b17', 'qaa/fheq-2024/4.15.b9.1', ADPRO, 'a group, fieldwork or outreach setting raises questions of inclusion',
    'what the student has seen that made a team or site more or less inclusive?')
k43(18, ['demonstrate'], 'legal and ethical dimensions', UN,
    "Show awareness of the legal and ethical sides of archaeology.",
    "At threshold, graduates show awareness of the law and ethics that bear on archaeology.",
    "By graduation you should be able to show that you know the legal and ethical issues archaeology raises.",
    'para 2.6, 3.2.b17 and 3.3.b17', 'qaa/fheq-2024/4.15.b9.2', ADPRO, 'a student meets human remains, illicit material or planning law',
    'which legal or ethical question the student would ask before starting a piece of work?', find=FINDS['4.3.b18'])

# ---- 4.4 threshold: generic skills (lead-in: on graduating with honours, students should be able to)
AAW44 = ("Describe this as a threshold generic skill: every honours graduate in archaeology should be able to show it at award, at FHEQ level 6 "
         "(FQHEIS level 10); it covers {about} and refines the descriptor {fw}. Cite " + CITE + ", para 4.4 (bullet {k}). Set it beside {nb} and "
         "the third-class column of Annex D ({ad}); do not claim it is a regulatory rule, the typical result or a standard at another level.")
AAD44 = ("Raise this when {when}. To a student, say plainly and in the second person that this is part of the minimum the degree asks by graduation; "
         "to staff, frame it as a threshold skill their assessments must give every student a chance to show. Ask {q} Avoid reading the list aloud or "
         "presenting the minimum as what a good degree looks like.")
def k44(k, verbs, about, para, prac, ben, nb, fw, ad, when, q):
    P['4.4.b%d' % k] = dict(type='threshold', rung='threshold', force='should', level='fheq:6', appliesTo='honours graduates in archaeology',
                            addressee='learner', verbs=verbs, about=about, domain='generic-skill', award=HON, para=para, prac=prac, ben=ben,
                            aaw=AAW44.format(about=about, k=k, nb=nb, fw=fw, ad=ad), aad=AAD44.format(when=when, q=q))

ADT = ['qaa/fheq-2024/annex-d/transferable/r%d/3rd' % i for i in range(6)]
ADC = ['qaa/fheq-2024/annex-d/cognitive/r%d/3rd' % i for i in range(5)]

k44(1, ['demonstrate'], 'using archaeological ideas outside archaeology',
    "Show awareness of relevant archaeological concepts and methods in situations outside archaeology.",
    "At threshold, graduates show they can see where archaeological concepts and methods apply beyond the discipline.",
    "By graduation you should be able to show that you can see where archaeological ideas and methods are useful outside archaeology.",
    '3.3.b19 and para 1.14', 'qaa/fheq-2024/4.15.b6', ADT[4], 'a student considers careers outside archaeology',
    'where the student could use an archaeological method in a job outside the field?')
k44(2, ['participating'], 'teamwork and discussion',
    "Carry out set tasks as a team member, taking part in discussion.",
    "At threshold, graduates perform assigned tasks in a team and take part in discussion.",
    "By graduation you should be able to do your share of a team task and take part in the discussion.",
    '3.3.b16', 'qaa/fheq-2024/4.15.b9.1', ADT[2], 'a group task begins or a team member is not contributing',
    'what the student\'s part in the last team task was?')
k44(3, [], 'bringing together information from different sources',
    "Bring together information and material from different sources.",
    "At threshold, graduates combine information and materials from different sources.",
    "By graduation you should be able to combine information and material from different sources.",
    '3.2.b15 and 3.3.b12', 'qaa/fheq-2024/4.15.b5', ADC[1], 'a student starts a literature review or synthesis',
    'which sources the student has combined and how they reconciled them?')
k44(4, [], 'identifying problems and questions',
    "Identify problems and frame questions.",
    "At threshold, graduates identify problems and questions.",
    "By graduation you should be able to spot problems and turn them into questions.",
    '3.3.b1', 'qaa/fheq-2024/4.15.b7', ADC[3], 'a student struggles to find a project question',
    'what problem the student has noticed in their reading that no one has answered?')
k44(5, ['undertake'], 'analysing factual information',
    "Analyse factual information.",
    "At threshold, graduates undertake analysis of factual information.",
    "By graduation you should be able to analyse factual information.",
    '4.3.b9', 'qaa/fheq-2024/4.15.b7', ADC[1], 'a student handles data or factual sources',
    'what the student\'s analysis of a dataset showed that a summary would miss?')
k44(6, ['recognise'], 'judging others\' arguments',
    "Recognise the strengths and weaknesses of other people's arguments.",
    "At threshold, graduates recognise the strengths and weaknesses of others' arguments.",
    "By graduation you should be able to see the strong and weak points in other people's arguments.",
    '3.3.b5 and 3.2.b1', 'qaa/fheq-2024/4.15.b7', ADC[2], 'a student reviews literature or responds in a seminar',
    'what the weakest point is in an argument the student admires?')
k44(7, ['produce'], 'synthesising the state of knowledge',
    "Produce a synthesis of what is known on a particular subject or topic.",
    "At threshold, graduates produce a synthesis of current knowledge on a topic.",
    "By graduation you should be able to pull together what is currently known about a topic.",
    '3.2.b15 and 4.3.b9', 'qaa/fheq-2024/4.15.b3.2', ADK3, 'a student writes a review essay or dissertation chapter',
    'what the student would say is the current consensus on their topic, and where it is weakest?')
k44(8, [], 'independent work with guidance',
    "Carry out tasks independently, with guidance.",
    "At threshold, graduates undertake tasks independently, with guidance.",
    "By graduation you should be able to carry out tasks on your own, with some guidance.",
    '3.3.b15 and 3.3.b3', 'qaa/fheq-2024/4.15.b5', ADT[3], 'a student moves from taught work to independent study',
    'what guidance the student still needs, and what they now do alone?')
k44(9, ['make'], 'reflecting on progress and using feedback',
    "Reflect on one's own progress and use the feedback given.",
    "At threshold, graduates reflect on their progress and use feedback provided.",
    "By graduation you should be able to reflect on your own progress and act on feedback you receive.",
    '3.3.b14', 'qaa/fheq-2024/4.15.b5', ADT[5], 'feedback is returned or a student meets their personal tutor',
    'what the student changed after their last piece of feedback?')
k44(10, ['express'], 'speaking and writing effectively',
    "Express oneself well in speech and in writing.",
    "At threshold, graduates express themselves effectively orally and in writing.",
    "By graduation you should be able to express yourself clearly in speech and in writing.",
    '3.3.b10 and 4.4.b11', 'qaa/fheq-2024/4.15.b8', ADT[1], 'a student receives feedback on writing or speaking',
    'which form, spoken or written, the student finds harder and why?')
k44(11, ['present'], 'making knowledge or argument understood',
    "Present knowledge or an argument so that others can follow it.",
    "At threshold, graduates present knowledge or argument in a way others can understand.",
    "By graduation you should be able to present what you know, or an argument, so that others can follow it.",
    '3.3.b2 and 3.3.b9', 'qaa/fheq-2024/4.15.b8', ADT[1], 'a student prepares a presentation or essay for a non-specialist reader',
    'how the student would check that someone outside the subject followed them?')
k44(12, ['use', 'collate', 'analyse', 'select', 'present'], 'digital literacy with relevant IT',
    "Use relevant IT to gather, analyse, choose and present information (digital literacy).",
    "At threshold, graduates use suitable IT to gather, analyse, choose and present information.",
    "By graduation you should be able to use the right digital tools to gather, analyse, choose and present information.",
    '3.3.b6 and 3.3.b11', 'qaa/fheq-2024/4.15.b8', ADT[1], 'a student chooses software for a project or presentation',
    'which digital tools the student relies on and which they avoid?')
k44(13, ['make'], 'oral presentation with visual aids',
    "Give oral presentations supported by visual aids.",
    "At threshold, graduates make oral presentations using visual aids.",
    "By graduation you should be able to give a spoken presentation with visual aids.",
    '3.3.b9 and 3.3.b10', 'qaa/fheq-2024/4.15.b8', ADT[1], 'a student prepares for an assessed presentation',
    'what the student\'s visual aids add that their words do not?')
k44(14, ['demonstrate', 'comprehend'], 'taking in new ideas and information',
    "Show the ability to understand new ideas or information when they are presented.",
    "At threshold, graduates show they can understand new ideas or information presented to them.",
    "By graduation you should be able to show that you can understand new ideas or information when you meet them.",
    '4.3.b6', 'qaa/fheq-2024/4.15.b5', ADK2, 'a student meets an unfamiliar method or theory',
    'how the student would check their understanding of a new idea?')
k44(15, ['demonstrate'], 'recognising and describing material',
    "Show skill in recognising and describing material.",
    "At threshold, graduates show skill in recognising and describing archaeological material.",
    "By graduation you should be able to show that you can recognise and describe archaeological material.",
    '3.2.b8 and 4.3.b13', 'qaa/fheq-2024/4.15.b2', ADP1, 'a student handles finds in a practical or identification test',
    'which features the student uses first to identify an object?')
k44(16, ['demonstrate'], 'classifying and collating data',
    "Show skill in classification: describing, sorting into categories and collating data.",
    "At threshold, graduates show classification skills in describing, categorising and collating data.",
    "By graduation you should be able to show that you can describe, sort and organise data into categories.",
    '3.2.b8 and 3.3.b13', 'qaa/fheq-2024/4.15.b2', ADP4, 'a student builds a catalogue, database or typology',
    'how the student decided where one category ends and the next begins?')
k44(17, ['understand'], 'health and safety and EDI at work',
    "Understand why health and safety and equality, diversity and inclusion matter in the workplace.",
    "At threshold, graduates understand why health and safety, and equality, diversity and inclusion, matter at work.",
    "By graduation you should be able to show that you understand why health and safety, and equality, diversity and inclusion, matter at work.",
    '3.3.b17 and 3.3.b18', 'qaa/fheq-2024/4.15.b9.1', ADPRO, 'a student prepares for fieldwork, a placement or a laboratory session',
    'what the student would do if they saw an unsafe or excluding practice on site?')
k44(18, ['appreciate'], 'current debates on sustainability, employability, decolonisation and anti-racism',
    "Appreciate current debates on global sustainability, employability and global perspectives, decolonisation and anti-racism among them.",
    "At threshold, graduates appreciate contemporary debates on global sustainability, employability and global perspectives including decolonisation and anti-racism.",
    "By graduation you should be able to show that you understand current debates on sustainability, employability and global perspectives, including decolonisation and anti-racism.",
    '3.2.b12, 3.3.b19 and 4.4.b20', 'qaa/fheq-2024/4.15.b4', ADK2, 'decolonisation, anti-racism or sustainability come up in teaching or careers',
    'which current debate the student feels archaeology adds most to?')
k44(19, ['appreciate', 'act'], 'acting sustainably',
    "Appreciate the need to act sustainably.",
    "At threshold, graduates appreciate the need to act in a sustainable way.",
    "By graduation you should be able to show that you understand the need to act sustainably.",
    '4.3.b11 and para 1.10', 'qaa/fheq-2024/4.15.b9.1', ADT[4], 'fieldwork travel, resource use or conservation choices come up',
    'what one sustainable choice the student could make in their own practice?')
k44(20, ['appreciate', 'engage'], 'engaging in contemporary debates',
    "Appreciate and take part in current debates, for instance on inequality, sustainability, globalisation and cultural diversity.",
    "At threshold, graduates appreciate and engage in contemporary debates such as inequality, sustainability, globalisation and cultural diversity.",
    "By graduation you should be able to take part in current debates, for example on inequality, sustainability, globalisation and cultural diversity.",
    '4.4.b18 and 3.2.b11', 'qaa/fheq-2024/4.15.b3.2', ADK2, 'a seminar or public event turns to current affairs',
    'what evidence from the past the student would bring to a current debate?')

# paragraph records whose skeleton span ran into the next heading, or whose statement is the stem only
for _i in ('1.7', '1.9', '1.10', '2.12', '2.19', '2.20', '2.21', '4.2'):
    P[_i]['find'] = FINDS[_i]
for _r in P.values():
    _r.pop('themes', None)

GRADE = {}   # one rung only: no gradeOf links

TH = {'1.8': 'theme:edi', '1.9': 'theme:edi', '1.10': 'theme:esd', '1.12': 'theme:enterprise',
      '2.20': 'theme:accessibility', '2.21': 'theme:accessibility'}

S5 = dict(
    levels=[dict(id='fheq:6', role='cites', locator='D1, 2.22; 4.2'),
            dict(id='fqheis:10', role='cites', locator='D1, 2.22; 4.2'),
            dict(id='fheq:7', role='cites', locator="D1, 2.24 (integrated master's, MArc; no standards stated)"),
            dict(id='fqheis:11', role='cites', locator="D1, 2.24 (integrated master's, MArc; no standards stated)"),
            dict(id='spine:6', role='refers', locator='std:ref:uk-framework R2 and R8 (inferred: Part E)')],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.22: "FHEQ Level 6; FQHEIS Level 10"; 4.2, the title of Annex D)'),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.24)'),
                dict(**{'from': 'fheq:6'}, to='spine:6', relation='sameStep', basis='inferred from std:ref:uk-framework R2 (Part E)')])

S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.8', '1.9', '2.4', '3.3', '4.3', '4.4']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.6', '1.9', '2.20', '2.21', '3.2', '3.3', '3.8', '3.10']),
      dict(id='theme:esd', role='carries', carriedIn=['1.1', '1.6', '1.10', '2.7', '2.14', '3.3', '4.3', '4.4']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.11', '1.12', '1.13', '1.14', '3.3', '4.4'])]

S7 = [dict(rel='supersedes', target='std:doc:qaa-archaeology-2014-benchmarks (not yet ingested)', note='the third edition (2014), named in section 6; the front matter lists key changes'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees, for performance above the threshold (4.2); SL6'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='levels 6 and 7 (2.22, 2.24)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='levels 10 and 11 (2.22, 2.24)'),
      dict(rel='cites', target='std:doc:qaa-advancehe-esd-2021-guidance', note='the core skills align with its learning outcomes (1.10)'),
      dict(rel='refersTo', target='CIfA and UAUK degree accreditation and its competency matrix (not yet ingested: Part E)', note='1.12, 1.13, 2.8, 2.27'),
      dict(rel='refersTo', target='National Occupational Standards for Archaeological Practice (not yet ingested: Part E)', note='1.12'),
      dict(rel='readWith', target='the Subject Benchmark Statements of partner subjects in joint honours (collection)', note='1.7, 2.23'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance; QAA Glossary', note='front matter')]

SB1 = [
    'The one subject that covers the whole human past in every period and place, giving the time depth needed for present concerns such as ecosystems, globalisation and sustainability (D1, 1.1, 2.10).',
    'It works with tangible and intangible remains, joins discovery to storytelling and debate, and welcomes many voices and narratives (D1, 1.2, 1.3).',
    'It sits in a triangle of science, arts and professional practice, so teaching and research are often interdisciplinary; it differs from Classics, History and Heritage Management (D1, 1.4, 2.19).',
    'Degrees rest on four contexts: social, ethical and professional, theoretical and scientific (D1, 2.2 to 2.18).',
    'It is self-critical about its colonial origins and contested uses, and works to decolonise its teaching and practice (D1, 1.3, 1.8, 2.4, 2.11).',
    'It is research-led, with undergraduates handling primary material and able to make discoveries of their own (D1, 2.1, 2.25).',
    'Practical work, in the field or with collections, is the main way evidence is made and is part of every course, with adjustments for access (D1, 1.6, 3.8).',
    'Archaeological science, conservation science, biological and environmental science, experimental and digital work run through it (D1, 2.12 to 2.17).',
    'Careers are wide, from commercial archaeology and museums to general graduate work, and a professional accreditation route exists (D1, 1.5, 1.12, 1.14, 2.8).',
]

SB2 = [dict(theme='theme:edi', inThisSubject='the discipline names barriers of ethnicity, disability, gender and class rooted in its origins; it asks for many voices, decolonised teaching, fair engagement with communities and attention to under-represented students at every stage (D1, 1.8, 1.9, 2.4)',
            statements=['1.8', '1.9', '3.3.b18', '3.3.b19', '4.3.b16', '4.3.b17', '4.4.b17', '4.4.b18', '4.4.b20']),
       dict(theme='theme:accessibility', inThisSubject='headed Accessibility in the text: varied teaching methods, adjustments for fieldwork and practical work, no two-tier system, equal access to field trips and placements, clear assessment criteria and accessible assessment (D1, 1.6, 2.20, 2.21, 3.8, 3.10)',
            statements=['2.20', '2.21', '3.2.b2', '3.3.b16']),
       dict(theme='theme:esd', inThisSubject='headed Sustainability in the text: core skills align with the ESD guidance; the archaeological resource is finite and needs sustainable conservation; heritage and tourism can be sustainable (D1, 1.1, 1.6, 1.10, 2.7, 2.14)',
            statements=['1.6', '1.10', '3.3.b19', '4.3.b11', '4.4.b18', '4.4.b19', '4.4.b20']),
       dict(theme='theme:enterprise', inThisSubject='enterprise education for careers, set beside the professional accreditation scheme and a wide range of employment beyond the profession (D1, 1.11 to 1.14)',
            statements=['1.12', '3.3.b8', '3.3.b19', '4.4.b18'])]

SB3 = dict(
    areas=[dict(component='1.6', gloss='the platform of knowledge: origins and value, legal and policy frames, contexts, evidence, theory, regions and periods, primary data, science and bias'),
           dict(component='2.3', gloss='the social context: past societies through present questions (2.3, 2.4)'),
           dict(component='2.5', gloss='the ethical and professional context (2.5 to 2.8)'),
           dict(component='2.9', gloss='the theoretical context and its four elements (2.9 to 2.11)'),
           dict(component='2.12', gloss='archaeological science and ten research themes, from formation processes to climate change'),
           dict(component='2.13', gloss='artefact characterisation and dating'),
           dict(component='2.14', gloss='conservation science'),
           dict(component='2.15', gloss='biological and environmental science, biomolecular methods'),
           dict(component='2.16', gloss='experimental archaeology'),
           dict(component='2.17', gloss='digital data and visualisation')],
    practices=[dict(component='2.20', kind='teaching', gloss='a varied mix: reading, lectures, seminars, tutorials, laboratory and field practicals, site visits, placements, outreach, self-guided and team work'),
               dict(component='2.25', kind='learning', gloss='research-led, experiential and team learning; flipped classroom, problem-based learning, students in curriculum design'),
               dict(component='2.26', kind='learning', gloss='independent research, project or dissertation'),
               dict(component='2.28', kind='learning', gloss='placements, community archaeology, shared fieldwork training and online courses with partners'),
               dict(component='3.6', kind='teaching', gloss='the resources: literature, digital tools, collections, field equipment and laboratories'),
               dict(component='3.8', kind='learning', gloss='practical participation in projects as part of every course'),
               dict(component='3.9', kind='assessment', gloss='an explicit strategy tied to outcomes and progression'),
               dict(component='3.10', kind='assessment', gloss='accessible mixed methods, adjustments, formative and peer feedback'),
               dict(component='3.11', kind='assessment', gloss='indicative methods: research project, essays, exams, notebooks, presentations, practical exams, portfolios, placement reports')])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.3 and 4.4 (under the heading Threshold level)', award=HON, items=38),
           dict(rung='typical', leadIn='none', award=HON, items=0),
           dict(rung='excellent', leadIn='none', award=HON, items=0)],
    rungBases='4.1: the statement sets the minimum threshold only; 4.2: most students perform significantly better, judged by each provider with reference to Annex D (the four honours classes)',
    outcomeLists=[dict(leadIn='3.2', gloss='subject-specific content students will be equipped with, as the course allows', items=16, award=['honours']),
                  dict(leadIn='3.3', gloss='generic, transferable and employability skills graduates will be equipped with', items=19, award=['honours'])],
    outcomes=[])

SB4A_FULL = []

SB5 = [dict(body='Chartered Institute for Archaeologists (CIfA)', says='the leading professional body; sets standards and, with University Archaeology UK, accredits degrees against a competency matrix aligned with the occupational standards (since 2019); publishes guidance on human remains (D1, 1.12, 1.13, 2.6, 2.7, 2.8, 2.27)', requirements='not yet ingested (Part E)'),
       dict(body='University Archaeology UK (UAUK)', says='partner in the joint accreditation scheme and its governance (D1, 1.12, 1.13, 2.8, 2.27)', requirements='not yet ingested (Part E)'),
       dict(body='British Association for Biological Anthropology and Osteoarchaeology (BABAO)', says='publishes guidance on the ethics of human remains (D1, 2.6; section 5)', requirements='not yet ingested (Part E)'),
       dict(body='Institute of Archaeologists of Ireland', says='professional body for archaeologists; links with institutions in Northern Ireland (D1, 2.7, 2.27)', requirements='not yet ingested (Part E)'),
       dict(body='Institute for Historic Building Conservation; Institute for Conservation; Society for Museum Archaeology', says='set standards for the built historic environment and the conservation of cultural heritage (D1, 2.7)', requirements='not yet ingested (Part E)'),
       dict(body='European Association of Archaeologists', says='a continental membership body with its own code of practice and principles of conduct (D1, 2.7)', requirements='not yet ingested (Part E)'),
       dict(body='Historic England; Cadw; Historic Scotland; Department for Communities, Northern Ireland', says='national heritage bodies with long-standing links to departments (D1, 2.27)', requirements='not yet ingested (Part E)')]

SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.8', '1.9', '2.4', '3.3', '4.3', '4.4'],
                 statements=['1.8', '1.9', '3.3.b18', '3.3.b19', '4.3.b16', '4.3.b17', '4.4.b17', '4.4.b18', '4.4.b20']),
            dict(id='theme:accessibility', named='Accessibility', carriedIn=['1.6', '1.9', '2.20', '2.21', '3.2', '3.3', '3.8', '3.10'],
                 statements=['2.20', '2.21', '3.2.b2', '3.3.b16']),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=['1.1', '1.6', '1.10', '2.7', '2.14', '3.3', '4.3', '4.4'],
                 statements=['1.6', '1.10', '3.3.b19', '4.3.b11', '4.4.b18', '4.4.b19', '4.4.b20']),
            dict(id='theme:enterprise', named='Enterprise and entrepreneurship (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['1.11', '1.12', '1.13', '1.14', '3.3', '4.4'],
                 statements=['1.12', '3.3.b8', '3.3.b19', '4.4.b18'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.22', '2.24', '4.2']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.22', '2.24', '4.2'])],
    bodies=[dict(body='Chartered Institute for Archaeologists', citedIn=['1.12', '1.13', '2.6', '2.7', '2.8', '2.27']),
            dict(body='University Archaeology UK', citedIn=['1.12', '1.13', '2.8', '2.27']),
            dict(body='British Association for Biological Anthropology and Osteoarchaeology', citedIn=['2.6']),
            dict(body='Institute of Archaeologists of Ireland', citedIn=['2.7', '2.27']),
            dict(body='Institute for Historic Building Conservation', citedIn=['2.7']),
            dict(body='Institute for Conservation', citedIn=['2.7']),
            dict(body='Society for Museum Archaeology', citedIn=['2.7']),
            dict(body='European Association of Archaeologists', citedIn=['2.7']),
            dict(body='Historic England, Cadw, Historic Scotland, Department for Communities (Northern Ireland)', citedIn=['2.27']),
            dict(body='professional, statutory and regulatory bodies (unnamed)', citedIn=['2.32', '3.8'])],
    sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'], role='the four honours classes, for performance above the threshold'),
                     dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='Education for Sustainable Development Guidance produced by Advance HE and QAA (March 2021)', citedIn=['1.10'], role='the learning outcomes the core skills align with'),
                     dict(document='National Occupational Standards for Archaeological Practice (not yet ingested: Part E)', named='National Occupational Standards for Archaeological Practice (NOS)', citedIn=['1.12'], role='the basis of the accreditation competency matrix'),
                     dict(document='European Association of Archaeologists, Code of Practice and Principles of Conduct (not yet ingested)', named='Code of Practice and Principles of Conduct', citedIn=['2.7'], role='a professional code'),
                     dict(document='Valletta, Faro and World Heritage Conventions (international treaties)', named='the Valletta and Faro Conventions, and the World Heritage Convention', citedIn=['2.7'], role='protection of the archaeological heritage'),
                     dict(document='Profiling the Profession (labour market intelligence; external)', named='Profiling the Profession', citedIn=['2.8'], role='evidence of employment growth'),
                     dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code', citedIn=['front matter'], role='course design, teaching, external expertise, monitoring'),
                     dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms')])

B1 = [dict(slug='archaeological-science', definition='using scientific methods on archaeological questions, with methods shared across many sciences (D1, 2.12)',
           beneficiaryDefinition='applying science, such as chemistry, biology or physics, to questions about the past', scopeNote='includes dating, materials, biomolecular and environmental work (2.13 to 2.15)', category='unknown', practices=['archaeology']),
      dict(slug='conservation-science', definition='the science of what makes sites, monuments and artefacts decay and of how to restore and keep them (D1, 2.14)',
           beneficiaryDefinition='finding out why remains decay and how to preserve them', scopeNote='', category='unknown', practices=['archaeology']),
      dict(slug='experimental-archaeology', definition='reproducing past actions and processes to see how the archaeological record forms (D1, 2.16)',
           beneficiaryDefinition='recreating past activities to understand what they leave behind', scopeNote='', category='unknown', practices=['archaeology'])]
B2A = [dict(concept='archaeological-science', form='Archaeological science', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='conservation-science', form='Conservation science', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='experimental-archaeology', form='Experimental archaeology', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []; B5 = []

D3 = [dict(source='CIfA and UAUK degree accreditation scheme and competency matrix', why='the accreditation route named in 1.12, 1.13, 2.8 and 2.27 (SB5)', status='wanted'),
      dict(source='National Occupational Standards for Archaeological Practice', why='the occupational standards the accreditation matrix aligns with (1.12)', status='wanted')]

E = [
    'Rungs: one only. Section 4 states the threshold (4.3, 18 subject items; 4.4, 20 generic items) and leaves higher performance to Annex D (4.2); no typical or excellent lists, so SB4 `outcomes` is empty and no gradeOf link is drawn. Differs from Psychology (three rungs).',
    'Lead-in wording: "On graduating with an honours degree in Archaeology, students should be able to" (4.3, 4.4) under the heading "Threshold level"; the modal is should, so force is recorded as should, statementType and rung threshold. 4.1 calls these the minimum threshold standards a student "will have demonstrated". P3 to confirm should against threshold as the force.',
    'Outcome lists in section 3 use "will be equipped to" (3.2) and "will be equipped with" (3.3), recorded as type outcome, rung none, force will; 3.2 is qualified "as appropriate to the breadth and depth of the course" and 3.1 says combined honours graduates normally have most of the skills. New lead-in wordings against Psychology.',
    'Skeleton corrections: 3.2.b5 and 3.2.b6 are one item split by a stray bullet ("material remains, / landscapes and environmental data"); recorded as 3.2.b5 with the merged text and 3.2.b6 dropped, so 3.2 has 16 items. 4.3.b16 ran across a page break and lost "and appreciate the need to engage ... equitable basis"; recut with `find`. 3.2.b17 and 4.3.b18 carried the next sub-heading; recut. Paragraph spans for 1.7, 1.9, 1.10, 2.19, 2.21 and 4.2 carried a following heading; recut to the paragraph text. 2.12 and 2.20 are recorded as their stems only; their list items (research themes; teaching methods) are S3 content, not statements.',
    'Duplicate in the issuer\'s text: 4.3.b10 ("recognise the range of archaeological data") repeats the start of 4.3.b7; both kept as issued. Also repeated: two identical tutorial bullets in 2.20 (b4, b11), and "assembling coherent research/project designs" in 3.3.b4 and 3.3.b15.',
    'Broken words in the held text (extraction spacing, such as "perf orm", "bri ng", "identi fy", "undert ake", "re flect", "colla borating", "appreciati ng") mean some verbs cannot be listed as they appear: 4.4.b2, b3, b4, b8, b9, b13 and 3.2.b8, b14, 3.3.b16, b17 list only the intact verbs or none.',
    'Not cut as statements, with reasons: 1.14 ("should not be seen exclusively as a vocational choice") is a view, not a standard; 2.5 and 2.29 to 2.31 use will to describe institutional practice; 2.22 uses "it is expected" and "would" (an obliging word outside the five, for Abbott); 2.26 ("there is a requirement" in most courses) describes practice; 4.1 frames the threshold and is the rung\'s introduction.',
    'Plain-present provider norms not cut (open point 5 of the benchmark template, for P3): 2.25 ("courses in all higher education providers include"), 3.5, 3.6 (providers "facilitate access"), 3.7 (students "are provided with full documentation"; documentation "will refer to" accreditation where appropriate), 3.8 ("participatory experience ... is therefore part of any course") and 3.10 ("aspires to include").',
    '2.21 holds both must (no two-tier system; clear assessment criteria must be provided) and several shoulds; recorded at must, with the should parts paraphrased as should. 1.8 likewise holds must and should; recorded at must. 1.6 holds will and should; recorded at will.',
    '1.12 reports a condition the professional body sets for accreditation (must demonstrate core NOS coverage); recorded as a requirement with addressee provider, but it is the accreditor\'s rule, not the issuer\'s. P3 to confirm it belongs in S4.',
    '1.8, 1.9 and 1.10 address the discipline and its practitioners rather than the student; recorded with addressee provider and the student version not applicable.',
    "Integrated master's (MArc) at FHEQ 7 / FQHEIS 11 is described in 2.24 but no standards are given for it; levelsCovered holds fheq:6 and fqheis:10 only.",
    'Inferred: HECoS 100384 (archaeological sciences) from 2.12 to 2.17; the text names the subject area but no code. The crosswalk fheq:6 to spine:6 is read from std:ref:uk-framework R2.',
    'SB5: no body\'s requirements are ingested; CIfA and UAUK accreditation and the NOS are wanted (D3). The national heritage bodies (2.27) are partners, not regulators of courses; recorded for completeness.',
    'SB6: the front matter also names the Quality Assessment Framework for Wales, the Quality Enhancement Framework (Scotland) and the OfS regulatory framework for England; these are excluded matter and not quality-level frameworks, so they are not in SB6 frameworks.',
    'CQFW: not cited by the statement; not used.',
    'Section order and headings: section 2 is "Distinctive features" with four contexts and design sub-sections (Accessibility, Progression, Flexibility, Partnership, Monitoring and review) where Psychology has its own order; filled by function.',
    'Supersedes: the 2014 third edition is named only in the advisory group list (section 6); its date of withdrawal is not stated.',
    'Licence: QAA copyright notice only; re-use terms not stated in the text.',
]
