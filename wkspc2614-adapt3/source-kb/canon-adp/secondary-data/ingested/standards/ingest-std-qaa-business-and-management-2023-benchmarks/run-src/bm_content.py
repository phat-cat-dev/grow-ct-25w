# Judgement for run 0091, QAA Subject Benchmark Statement: Business and Management (March 2023). std run agent.
# Built by tools/bm_build.py business-and-management-2023 --check. Brief BM-BRIEF.md 0.2.1; benchmark template 0.6.0-draft; run layer 0.7.0-draft.
HON = "bachelor's with honours"
CITE = 'QAA, 2023, Business and Management Subject Benchmark Statement, para '

META = dict(
    run='0091', p1='2026-10-03 16:33',
    title='Subject Benchmark Statement Business and Management',
    heading='Subject Benchmark Statement: Business and Management (QAA, March 2023)',
    edition='March 2023 (fifth edition)', published='2023-03',
    status='current',
    supersedes='the fourth edition (2019), named in the membership section (section 6)',
    subjects=[
        dict(scheme='hecos', code='100078', label='business and management', basis='stated'),
        dict(scheme='cah', code='CAH17-01-01', label='business and management (non-specific)', basis='stated'),
        dict(scheme='cah', code='CAH17-01', label='business and management', basis='stated'),
        dict(scheme='cah', code='CAH17', label='business and management', basis='stated'),
        dict(scheme='hecos', code='100079', label='business studies', basis='inferred'),
        dict(scheme='hecos', code='100089', label='management studies', basis='inferred'),
    ],
    awards=[HON], levels=['fheq:6', 'fqheis:10'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, the 2022 onward revision with cross-cutting themes (fifth edition of this statement)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what a graduate of a broad, general Business and Management honours degree "
                     "should know and be able to do, with its standards at three rungs (threshold, typical, excellent) tied to the "
                     "degree classes. Reach for it when designing, approving, reviewing or describing a general business or management "
                     "course, its outcomes or its marking. It is not a curriculum, not an accrediting body's standard and not a "
                     "regulatory requirement in England; function- or sector-specific courses may use it for their broad business content."),
    summary=("Published by QAA in March 2023 as the fifth edition, the statement sets out the purposes and characteristics of a "
             "Business and Management degree, its distinctive features (design, progression, flexibility, partnership, monitoring "
             "and review), its content, skills, teaching, learning and assessment, and benchmark standards for the honours degree "
             "at threshold (any honours degree), typical (second class) and excellent (first class) rungs, each in five categories "
             "(knowledge and understanding, skills, critical perspective, application, values). It carries four cross-cutting "
             "themes (equality, diversity and inclusion; accessibility; education for sustainable development; enterprise and "
             "entrepreneurship education), points to Annex D for the degree classes, and names professional, statutory and "
             "regulatory bodies in general and sector bodies (CABS, BAM, AACSB, EFMD, PRME) in particular."),
    authority=("reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a "
               "sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of quality "
               "requirements in Northern Ireland (D1, front matter: Relationship to legislation)"))

S2 = dict(
    governs='what a graduate of a broad, general Business and Management honours degree is expected to know, do and understand, and the standards at threshold, typical and excellent',
    awards=[HON, "integrated master's (first-degree elements only)", 'degree apprenticeships in business and management'],
    levels=['fheq:6', 'fqheis:10'],
    statedScope='"The Statement is for Business and Management degree courses which are broad based and general in their scope rather than being oriented towards a particular business function (for example, marketing or finance) or sector (for example, tourism or construction management)." (D1, 1.2)',
    statedSubjects=[
        dict(name='Business and Management', locator='(D1, title; 1.1; 1.2)', kind='subject',
             codes=[dict(scheme='hecos', code='100078', label='business and management'), dict(scheme='cah', code='CAH17-01-01', label='business and management (non-specific)')]),
        dict(name='Degree Apprenticeships in business and management', locator='(D1, 1.2)', kind='programme title',
             codes=[dict(scheme='hecos', code='100078', label='business and management')]),
        dict(name='marketing (a business function, named as outside the main scope)', locator='(D1, 1.2)', kind='specialism',
             codes=[dict(scheme='hecos', code='100075', label='marketing')]),
        dict(name='tourism (a sector, named as outside the main scope)', locator='(D1, 1.2)', kind='specialism',
             codes=[dict(scheme='hecos', code='100100', label='tourism management')]),
    ])

SECTIONS = {
    '1': 'Context and purposes of a Business and Management degree',
    '2': 'Distinctive features of a Business and Management degree',
    '3': 'Content, structure and delivery',
    '4': 'Benchmark standards',
}
SUB = [
    ('1.1', '1.3', 'Context'),
    ('1.4', '1.9', 'Purposes'),
    ('1.10', '1.14', 'Characteristics'),
    ('1.15', '1.21', 'Equality, diversity and inclusion'),
    ('1.22', '1.24', 'Accessibility'),
    ('1.25', '1.28', 'Education for Sustainable Development'),
    ('1.29', '1.33', 'Enterprise and entrepreneurship education'),
    ('2.1', '2.6', 'Design'),
    ('2.7', '2.10', 'Progression'),
    ('2.11', '2.13', 'Flexibility'),
    ('2.14', '2.16', 'Partnership'),
    ('2.17', '2.21', 'Monitoring and review'),
    ('3.1', '3.7', 'Content: knowledge and understanding'),
    ('3.8', '3.13', 'Skills and practice'),
    ('3.14', '3.17', 'Teaching and learning'),
    ('3.18', '3.26', 'Assessment'),
    ('4.1', '4.4', 'Introduction'),
    ('4.5', '4.5', 'Threshold level'),
    ('4.6', '4.6', 'Typical level'),
    ('4.7', '4.7', 'Excellent level'),
]

G = {
    '1.1': 'what the statement sets out: graduate expectations and three rungs',
    '1.2': 'scope: broad general courses; use by function and sector courses; integrated master\'s and apprenticeships; allied statements',
    '1.3': 'a broad frame that keeps innovation and diversity in course design',
    '1.4': 'the four purposes of a degree in the subject',
    '1.5': 'organisations and business read broadly, every type and size',
    '1.6': 'what responsible leadership takes in',
    '1.7': 'what career preparation means: knowledge, skills, self-awareness, enterprise',
    '1.8': 'skills and attributes as transferable, beyond business careers',
    '1.9': 'courses balance the purposes differently, shown in their outcomes',
    '1.10': 'breadth, interdisciplinarity and variety of perspective',
    '1.11': 'theory and practice together',
    '1.12': 'a changing discipline reflected in course design',
    '1.13': 'a broad base for careers and further study',
    '1.14': 'the new theme sections and their reach across the statement',
    '1.15': 'EDI defined broadly and built into the subject',
    '1.16': 'principles for an inclusive learning community',
    '1.17': 'why the subject is taught: EDI and the SDGs',
    '1.18': 'what is taught: EDI content, diverse perspectives',
    '1.19': 'how the subject is taught: inclusive design and modes of learning',
    '1.20': 'examples of EDI in the learning community',
    '1.21': 'EDI as ongoing review with students',
    '1.22': 'accessibility across the whole course, with examples',
    '1.23': 'designing out barriers in advance',
    '1.24': 'equal access to work-based, international and digital learning',
    '1.25': 'the subject and sustainable development: SDGs, PRME, ERS',
    '1.26': 'sustainable management as a curriculum duty, with example topics',
    '1.27': 'ERS taught in dedicated spaces and throughout',
    '1.28': 'core skills match the ESD guidance competencies',
    '1.29': 'enterprise and entrepreneurship education defined',
    '1.30': 'entrepreneurial capacity and mindset',
    '1.31': 'enterprise theory and practice across sectors',
    '1.32': 'experiential learning for ventures and innovation',
    '1.33': 'enterprise for a self-directed working life',
    '2.1': 'interdisciplinary and adaptable course design',
    '2.2': 'knowledge joined with skills; vocational to theoretical',
    '2.3': 'employability and a responsible professional mindset',
    '2.4': 'responsible management practice built into courses',
    '2.5': 'every kind of organisation covered',
    '2.6': 'preparing for changing working life',
    '2.7': 'progression through the levels to threshold and beyond',
    '2.8': 'joint and combined routes',
    '2.9': 'course length, placements and exit awards',
    '2.10': 'integrated master\'s degrees in the subject',
    '2.11': 'flexible approaches for access and inclusion',
    '2.12': 'forms flexibility may take',
    '2.13': 'coherence kept in flexible routes',
    '2.14': 'partnerships with organisations',
    '2.15': 'recognition by professional bodies',
    '2.16': 'networks and sector bodies',
    '2.17': 'monitoring and periodic review',
    '2.18': 'external reviewers in periodic review',
    '2.19': 'external examiners and threshold standards',
    '2.20': 'advisory boards and employer panels',
    '2.21': 'accreditation of professional and vocational courses',
    '3.1': 'broad, analytical, integrated study of business',
    '3.2': 'knowledge of organisations, environment and governance',
    '3.3': 'integration across areas of understanding',
    '3.4': 'area: the business environment',
    '3.5': 'area: organisations',
    '3.6': 'area: responsible leadership and management',
    '3.7': 'ten areas of knowledge, understanding and critical evaluation',
    '3.8': 'practice-related courses link skills to employability',
    '3.9': 'cognitive, intellectual, personal and interpersonal skills',
    '3.10': 'eight skills of particular relevance to the subject',
    '3.11': 'seven other generic skills and attributes',
    '3.12': 'national and international contexts',
    '3.13': 'languages and cultural awareness before going abroad',
    '3.14': 'varied qualifications; emphasis shown in outcomes',
    '3.15': 'theory and practice joined; inputs from practitioners',
    '3.16': 'inclusive methods, modes and typical learning activities',
    '3.17': 'defined skills development and assessment',
    '3.18': 'assessment for learning and timely feedback',
    '3.19': 'inclusive assessment design',
    '3.20': 'reliable, inclusive, varied assessment methods',
    '3.21': 'online and in-person assessment',
    '3.22': 'authentic assessment',
    '3.23': 'group assessment and its weighting',
    '3.24': 'peer review and assessment',
    '3.25': 'transparent assessment and shared criteria',
    '3.26': 'assessment and student workload',
    '4.1': 'what the standards are and where content sits',
    '4.2': 'most go beyond threshold; Annex D for classes',
    '4.3': 'three categories; threshold as minimum, typical as the norm',
    '4.4': 'five bases that separate the categories',
    '4.5': 'threshold rung, honours degree',
    '4.6': 'typical rung, second class honours',
    '4.7': 'excellent rung, first class honours',
}
CTYPE = {
    '3.4': 'area', '3.5': 'area', '3.6': 'area',
    '3.15': 'practice', '3.17': 'practice', '3.18': 'practice', '3.19': 'practice', '3.21': 'practice',
    '3.22': 'practice', '3.23': 'practice', '3.24': 'practice', '3.25': 'practice', '3.26': 'practice',
}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='section headings (1 to 4)', kind='other: heading lines'),
    dict(number='5', heading='List of references and further resources', kind='other: references, read for S7 and SB6'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Business and Management',
         kind='other: membership, read for S7 (earlier editions)'),
]

P = {}
def s(i, **k):
    P[i] = k

FW6 = 'qaa/fheq-2024/4.15 (FHEQ level 6 honours descriptor) and qaa/fqheis-2024/4.16 (FQHEIS level 10)'

# ------------------------------------------------------------- section 1: obliging and outcome paragraphs
s('1.3', type='expectation', rung='none', force='should', level='none', appliesTo='courses in the subject', addressee='provider',
  verbs=['maintained', 'develop', 'deliver'], about='keeping innovation and variety in course design', domain='none', award=HON,
  para="The statement is a broad, non-prescriptive frame for building and running courses; innovation, adaptability and variety mark the subject's courses, and that quality should be kept.",
  prac="Use the statement as a broad frame rather than a template: when you design or revise a course, the innovation, adaptability and variety typical of the subject should be kept.",
  ben=('n/a', 'a duty on those who design courses; it sets no outcome for the student'),
  aaw="Describe this as an expectation (should) on course teams at bachelor's honours level: that innovation, adaptability and variety in course design be kept. Cite it as (" + CITE + "1.3) and read it with para 2.2, to which it points, and the design features in paras 2.1 to 2.6. Do not claim that it sets a curriculum or a regulatory rule.",
  aad="Raise it with a programme team that worries the statement will force a standard course. Put it as both permission and expectation: their course should stay distinctive. Ask what makes the course different and whether a planned change would remove that. Do not bring it to students as something they have to meet.")

s('1.8', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='graduates of the subject', addressee='learner',
  verbs=['equip'], about='transferable skills for any career', domain='generic-skill', award=HON,
  para="Skills and attributes here mean transferable academic and professional skills, suited to business careers but not confined to them; these skills will also prepare students to work well and responsibly as employees, colleagues, leaders and citizens of the world.",
  prac="Read skills and attributes as transferable academic and professional skills: they serve a business career and any other, and they will ready students to act effectively and responsibly at work, as leaders and as global citizens.",
  ben="You will build academic and professional skills that carry over to any career, not only business, and that ready you to be an effective, responsible employee, colleague, leader and citizen of the world.",
  aaw="Present this as a stated expectation (will) for honours graduates at FHEQ level 6: the subject's skills transfer beyond business careers. Cite it as (" + CITE + "1.8) and set it beside the generic skills in paras 3.11.b1 to 3.11.b7 and the employment qualities in qaa/fheq-2024/4.15.b9.1 to 4.15.b9.3. Do not claim that every graduate goes into business or management, which the paragraph itself rules out.",
  aad="Bring it up when a student doubts the degree's worth outside business, or when staff plan careers support. Tell a student plainly that these skills travel, then ask which two skills they would point to for a role outside business. Avoid suggesting the degree leads only to management jobs.")

s('1.9', type='expectation', rung='none', force='should', level='none', appliesTo='each course in the subject', addressee='provider',
  verbs=['vary', 'reflect'], about='the balance of purposes, shown in learning outcomes', domain='none', award=HON,
  para="Courses cover the purposes in differing balance, which may follow what professional bodies ask for recognition; whatever balance a course strikes should be explainable and shown through its stated learning outcomes.",
  prac="Decide how your course weights the four purposes in 1.4, noting any professional recognition that shapes it, and make that weighting explainable and visible in its specified learning outcomes.",
  ben=('n/a', 'a duty on the course team in writing outcomes'),
  aaw="Describe this as an expectation (should) on each honours course: the mix of purposes it delivers should be explainable through its learning outcomes. Cite it as (" + CITE + "1.9) and set it beside the purposes listed in paras 1.4.b1 to 1.4.b4. Do not claim the statement fixes the balance; it leaves the mix to the course and asks only that it be shown.",
  aad="Raise it when a programme team writes or revises its learning outcomes. Ask which of the purposes in 1.4 the course leans towards, and where in the outcomes a reader could see that. Keep it for staff; it is a design duty, not a student standard.")

s('1.10', type='expectation', rung='none', force='should', level='none', appliesTo='courses in the subject', addressee='both',
  verbs=['give', 'applied'], about='broad insight across business areas', domain='none', award=HON,
  para="The subject's courses are marked by variety of content, interdisciplinarity and range of view; they are broad and should give insight into many areas of business, knowledge that carries into many settings.",
  prac="Keep the course broad: it should give students insight into a wide spread of business areas, drawing on varied content and disciplines so that what they learn carries into many settings.",
  ben="Your course should give you a view across many areas of business, not just one, so that what you learn can be used in many settings.",
  aaw="Describe this as an expectation (should) that an honours course in the subject gives insight across many business areas. Cite it as (" + CITE + "1.10) and set it beside the area list in paras 3.7.b1 to 3.7.b10 and the scope note in para 1.2. Do not claim it bars a course with a particular emphasis; para 2.1 allows that.",
  aad="Raise it when a student asks why they study areas outside their interest, or when staff narrow a course. For a student, explain that breadth is part of the subject and ask which area outside their favourite has surprised them. For staff, ask which business areas the course leaves out. Avoid treating breadth as a list of compulsory modules.")

s('1.13', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students of the subject', addressee='learner',
  verbs=['prepared', 'provide'], about='a broad base for careers and further study', domain='none', award=HON,
  para="The subject's courses lay a broad base from which students will be ready for many future careers and roles across organisations of every kind, and may lead on to postgraduate study in many specialisms.",
  prac="Design the course as a broad base: students will be ready for varied careers and roles in many kinds of organisation, and the course may also lead to specialist postgraduate study.",
  ben="Your studies will give you a broad base for many kinds of career and role, in many kinds of organisation, and may lead on to postgraduate study in a specialism.",
  aaw="State it as an expectation (will) about honours graduates at FHEQ level 6: a broad base for many careers, with further study possible (may). Cite it as (" + CITE + "1.13) and set it beside para 2.7 on readiness for postgraduate study and qaa/fheq-2024/4.15.b9.3. Do not turn the 'may' about postgraduate study into a promise.",
  aad="Bring it up when a student is unsure where the degree leads. Ask them which kinds of organisation they could picture working in, and whether a specialist master's appeals. Avoid promising entry to further study, which each institution decides.")

s('1.15', type='expectation', rung='none', force='should', level='none', appliesTo='the subject area and its courses', addressee='provider',
  verbs=['embedded', 'recognise'], about='EDI built into the culture and practice of the subject', domain='none', award=HON,
  para="EDI covers many identity characteristics and kinds of difference, reaching past legal duties to intersections across students and staff; it should be a real concept built into the subject's culture and practice.",
  prac="Treat EDI as more than legal compliance: it should be a real presence in how the subject is taught and practised, attentive to intersecting identities among students and staff.",
  ben=('n/a', 'a duty on the subject community and course teams'),
  aaw="Describe this as an expectation (should) on the subject community and its course teams: EDI built into culture and practice, not only met as a legal duty. Cite it as (" + CITE + "1.15) and set it beside paras 1.18, 1.19 and 1.21, which say what is taught, how it is taught and how it is reviewed. Do not present it as a student outcome or as a legal requirement in its own right.",
  aad="Raise it with a programme team reviewing culture, curriculum or teaching. Ask where EDI shows in day-to-day practice beyond policy, and whose differences the course has not yet noticed. Do not hand it to a student as a standard they must meet.")

s('1.17', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='future managers and leaders studying the subject', addressee='learner',
  verbs=['embed', 'equips', 'support'], about='EDI principles in future managers and leaders', domain='generic-skill', award=HON,
  para="A focus on EDI lets business education help organisations tackle inequality and disadvantage, in line with the SDGs; joined with reflective practice it readies students for a diverse, global world, and study of the subject will instil EDI principles in future managers and leaders.",
  prac="Teach the subject so that EDI and reflective practice prepare students to work in a diverse, global world and to help organisations reduce inequality; the study will instil EDI principles in those who go on to manage and lead.",
  ben="Your studies will build equality, diversity and inclusion into how you manage and lead, so that you can help organisations reduce inequality and do well in a diverse, global world.",
  aaw="Present this as an expected outcome (will) of honours study at FHEQ level 6: EDI principles held by future managers and leaders. Cite it as (" + CITE + "1.17), noting its link to responsible leadership in para 1.6, and set it beside paras 3.10.b1 and 3.11.b3 and the decision-making quality in qaa/fheq-2024/4.15.b9.2. Do not claim it is a measured rung outcome; it states why the subject is taught.",
  aad="Raise it when a student asks why EDI appears in a business degree, or when staff link teaching to the SDGs. With a student, ask how they would make a team they led more inclusive. Avoid lecturing; let the student connect it to work they know.")

s('1.18', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='graduates and courses in the subject', addressee='both',
  verbs=['ensure', 'gain', 'equipped', 'offers'], about='what is taught on EDI: law, inclusive workplaces, diverse content', domain='understanding', award=HON,
  para="Courses make sure students critically grasp how organisations and their leaders advance EDI; graduates should know the legal duty to prevent discrimination and have the knowledge and skills to build inclusive workplaces; courses should also offer diverse content that questions dominant approaches, drawing on perspectives such as the Global South and marginalised communities.",
  prac="Teach a critical understanding of organisations' role in EDI; graduates should know anti-discrimination law and be able to foster inclusive workplaces; and the course content should be diverse, question dominant approaches and use cases that reflect the cohort and society.",
  ben="You should come to understand the law against discrimination and gain the knowledge and skills to build inclusive workplaces; your course should also show you a wide range of perspectives and question the dominant ways the subject has been taught.",
  aaw="Describe this as an expectation (should) at honours level with two parts: what graduates should know and be able to do on EDI, and what course content should offer. Cite it as (" + CITE + "1.18) and set it beside para 3.7.b5 (people and organisational behaviour), para 3.10.b1 and the level 6 understanding in qaa/fheq-2024/4.15.b1. Do not claim the course alone must satisfy legal compliance training; the text asks for awareness and capability.",
  aad="Raise it when a student asks what they should know about inclusion at work, or when a team reviews reading lists and cases. Ask a student whether they could explain an employer's duty not to discriminate and name one way to make a workplace more inclusive; ask staff whose voices their cases leave out. Avoid reading the paragraph out; choose the part that fits the person.")

s('1.19', type='requirement', rung='none', force='should', level='none', appliesTo='course design and teaching', addressee='provider',
  verbs=['designed', 'enable', 'considered'], about='inclusive design, teaching and modes of learning', domain='none', award=HON,
  para="Courses should be built so that students of every background can reach their potential and feel represented; teaching and assessment should follow inclusive principles, with modes of learning chosen with care, and teaching should show awareness of EDI in its pedagogy.",
  prac="Design the course so students from all backgrounds can succeed and feel included; choose modes of learning and assessment designs with their different opportunities and barriers in mind, and let teaching approaches draw on the cohort's diversity.",
  ben=('n/a', 'a duty on course design and teaching'),
  aaw="Describe this as a provider expectation (should) for honours courses: inclusive design, inclusive teaching and assessment, and careful choice of learning mode. Cite it as (" + CITE + "1.19) and set it beside paras 1.22 to 1.24 on accessibility and para 3.19 on inclusive assessment. Do not present it as a student outcome.",
  aad="Raise it when a team chooses delivery modes or redesigns assessment. Ask which students a planned mode would help and which it would hinder, and what assessment choice would widen success. Keep it for staff; a student meets its effect, not the duty.")

s('1.21', type='requirement', rung='none', force='should', level='none', appliesTo='course teams', addressee='provider',
  verbs=['reflect', 'work'], about='EDI review as an ongoing process with students', domain='none', award=HON,
  para="Attention to EDI is continuous: course teams should reflect regularly on improving it and, where they can, do so in partnership with students; changes to courses may include an equality impact assessment.",
  prac="Build EDI into regular course review: reflect on how to strengthen it, involve students as partners where possible, and consider an equality impact assessment when approving changes.",
  ben=('n/a', 'a duty on course teams; students may take part as partners'),
  aaw="Describe this as an expectation (should) on course teams: regular reflection on EDI, with students where possible. Cite it as (" + CITE + "1.21) and set it beside para 2.17 on monitoring and review. Do not state that an equality impact assessment is required; the text says it can be considered.",
  aad="Raise it at annual review or course approval. Ask when the team last looked at EDI in the course and which students took part. Avoid giving students the duty itself; invite them only as partners.")

s('1.22', type='requirement', rung='none', force='should', level='none', appliesTo='every stage of the course', addressee='provider',
  find='Accessibility should, as a minimum, meet regulatory requirements and will apply to all stages of the course, from providing pre-application information through to graduation and beyond.',
  verbs=['meet', 'apply'], about='accessibility meets regulation and covers the whole course', domain='none', award=HON,
  para="At the least, accessibility should satisfy what regulation requires, and it will reach every stage of the course, from information before application to graduation and after.",
  prac="Make accessibility at least compliant with regulation and apply it end to end: pre-application information, teaching, assessment, graduation and beyond.",
  ben=('n/a', 'a duty on the provider; the student meets its effect'),
  aaw="Describe this as a provider expectation (should, with will for its reach) that accessibility meets regulatory requirements at minimum and runs through every stage of the course. Cite it as (" + CITE + "1.22) and set it beside paras 1.23, 1.24 and 3.19. Do not present the paragraph's examples as required actions; they are given as what accessibility may include.",
  aad="Raise it when a team reviews information, spaces, resources or assessment. Ask where in the student journey, from applying to graduating, access is weakest. Do not put this duty to a student; if a student raises a barrier, point them to support.")

s('1.24', type='requirement', rung='none', force='should', level='none', appliesTo='courses in the subject', addressee='provider',
  verbs=['include', 'enabling', 'providing'], about='equal access to work and international learning, and digital access', domain='none', award=HON,
  para="Accessibility should give every student the same chances of workplace and international learning, and digital access that is inclusive and free of discrimination.",
  prac="Check that placements, work-based learning and study abroad are open to every student on equal terms, and that digital provision is inclusive and accessible.",
  ben=('n/a', 'a duty on the provider; the student meets its effect'),
  aaw="Describe this as a provider expectation (should) that work-based, international and digital learning are open to all students alike. Cite it as (" + CITE + "1.24) and set it beside paras 1.22 and 2.14 on partnerships and placements. Do not present it as a student standard.",
  aad="Raise it when a team plans placements, study abroad or online delivery. Ask which students might be unable to take up a placement or trip, and what would change that. Keep the duty with staff.")

s('1.26', type='requirement', rung='none', force='describes', level='none', appliesTo='the curriculum of the subject', addressee='provider',
  find='Management for economic, social and environmental sustainability needs to be integrated systematically within the Business and Management curriculum and across functional areas.',
  verbs=['integrated'], about='sustainability built into the curriculum across functions', domain='none', award=HON,
  para="Managing for economic, social and environmental sustainability needs to run systematically through the curriculum and across business functions (the issuer's 'needs to', recorded as describes).",
  prac="Weave sustainability through the curriculum, in every functional area rather than one module, covering its economic, social and environmental sides.",
  ben=('n/a', 'a duty on curriculum design'),
  aaw="Describe this as a curriculum expectation stated with 'needs to', recorded here as describes because the word is outside the five modals. Cite it as (" + CITE + "1.26) and set it beside paras 1.25, 1.27, 1.28 and the area in para 3.7.b1, and the guidance std:doc:qaa-advancehe-esd-2021-guidance. Do not claim the example topics listed after it are required; the text calls the list not exhaustive.",
  aad="Raise it when a team maps where sustainability sits in the course. Ask which functional modules, such as finance or operations, touch it at all. Do not give it to students as a duty.")

# ------------------------------------------------------------- section 2
s('2.7', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students progressing through the degree', addressee='learner',
  verbs=['progress', 'build', 'undertaking'], about='progression to threshold and readiness for postgraduate study', domain='none', award=HON,
  para="An honours student will move from level to level under each institution's rules, each level building toward the threshold standards; a student reaching the typical standard or above would be expected to be ready for postgraduate study, though entry is for each provider to decide.",
  prac="Plan each level so attainment builds towards the threshold standards at FHEQ level 6 (FQHEIS level 10); students at typical or above would be expected to be ready for further study in the subject or a cognate one.",
  ben="You will move up level by level, building towards at least the minimum standard for your honours degree; if you reach the typical standard or higher, you should be ready for postgraduate study, though each institution sets its own entry rules.",
  aaw="Present this as an expectation (will, with 'it is expected') on progression through an honours degree at FHEQ level 6 and FQHEIS level 10, as the paragraph states both. Cite it as (" + CITE + "2.7) and set it beside the rungs in paras 4.5 to 4.7 and qaa/fheq-2024/4.15. Do not claim it guarantees postgraduate entry; the text leaves entry to each provider.",
  aad="Raise it when a student asks how their current level relates to the final degree or to a master's. Ask where they think they sit now against the minimum and the typical standard. Avoid presenting the typical standard as the pass mark.")

s('2.8', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='students on joint, combined or major-minor routes', addressee='learner',
  verbs=['achieve', 'add', 'explore'], about='core skills on joint and combined routes', domain='subject-skill', award=HON,
  para="Students on combined, joint or major-minor routes will gain the core elements of the subject's specific and generic skills and add others from their second subject, possibly exploring where the two overlap.",
  prac="On joint and combined routes, ensure students will still reach the core specific and generic skills of the subject, and use the overlap with the second subject for interdisciplinary work.",
  ben="If you study business and management alongside another subject, you will still gain its core skills, add skills from your other subject and may explore where the two meet.",
  aaw="Present this as an expectation (will) for joint, combined and major-minor honours routes at FHEQ level 6: the core of the subject's skills is still reached. Cite it as (" + CITE + "2.8) and set it beside paras 3.10 and 3.11. Do not claim joint students must meet every item of the single-subject lists; the text says core elements.",
  aad="Raise it when a joint-honours student worries they are missing out, or a team designs a joint route. Ask which core skills the route secures and which come from the other subject. Avoid implying a joint degree is a lesser award.")

s('2.18', type='expectation', rung='none', force='will', level='none', appliesTo='higher education providers', addressee='provider',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award=HON,
  para="Externality is central to UK quality assurance: providers will bring in external reviewers during periodic review to gain an outside view of proposed changes and confirm that threshold standards are met and content suits the subject.",
  prac="Include external reviewers in periodic review so that proposed changes get an outside view and threshold standards and content are confirmed.",
  ben=('n/a', 'a duty on the provider in review'),
  aaw="Describe this as a provider expectation (will) about periodic review. Cite it as (" + CITE + "2.18) and set it beside paras 2.17 and 2.19 on review and external examining. Do not present it as a student outcome.",
  aad="Raise it with a team preparing periodic review. Ask who their external reviewer is and what they will be asked to confirm about threshold standards. Keep it with staff.")

# ------------------------------------------------------------- section 3: content outcomes
s('3.2', type='outcome', rung='none', force='should', level='fheq:6', appliesTo='graduates of the subject', addressee='learner',
  verbs=['demonstrate', 'emphasise'], about='knowledge of organisations, their environment and governance', domain='knowledge', award=HON,
  para="Graduates should reasonably be able to show knowledge and understanding of varied organisations, their wider business setting and communities, and how they are governed and managed; courses stress the changing nature of work, the future of organisations globally, risk and their effect on society.",
  prac="Graduates should be able to show they know and understand a range of organisations, their environment and governance; teach the changing nature of work, risk and organisations' impact on society.",
  ben="You should be able to show that you know and understand many kinds of organisation, the wider business world and communities around them, and how they are run and governed, including risk and their effect on society.",
  aaw="State it as an outcome graduates should reasonably be expected to show at FHEQ level 6 (FQHEIS level 10): knowledge of organisations, environment and governance. Cite it as (" + CITE + "3.2) and set it beside the areas in paras 3.4 to 3.7 and qaa/fheq-2024/4.15.b1. Do not claim it holds at a lower level of study or as a standalone module.",
  aad="Raise it when a student asks what they should know by the end of the degree. Ask them to name an organisation unlike the ones they know best and explain how it is governed. Avoid reading out the paragraph; use one example.")

s('3.3', type='outcome', rung='none', force='should', level='fheq:6', appliesTo='successful graduates from every mode of learning', addressee='both',
  verbs=['demonstrated'], about='integrating areas of understanding', domain='understanding', award=HON,
  para="How areas of understanding relate and fit together matters greatly in the learning experience and should show in what successful graduates can do, whatever their mode of study.",
  prac="Build integration across areas into the course and its assessment; successful graduates from every mode should be able to show it.",
  ben="You should be able to show how the different areas of business you study connect and work together, whichever way you study.",
  aaw="Describe this as an outcome (should) for successful honours graduates at FHEQ level 6 in every mode of study: integration across areas. Cite it as (" + CITE + "3.3) and set it beside the rung items on relationships between areas, paras 4.5.b1, 4.6.b1 and 4.7.b1. Do not claim it applies only to full-time or in-person students.",
  aad="Raise it when a student treats modules as separate boxes, or a team plans synoptic assessment. Ask the student how a decision in marketing would affect finance or operations. Avoid making integration sound like an extra topic.")

AREA = dict(rung='none', type='outcome', force='should', level='fheq:6', appliesTo='graduates of the subject', addressee='learner',
            domain='knowledge', award=HON)
def area(k, name, verbs, about, para, prac, ben, nb, q):
    s('3.7.b%d' % k, verbs=verbs, about=about, para=para, prac=prac, ben=ben,
      aaw=("Treat this as a knowledge area in which honours graduates should be able to show knowledge, understanding and critical evaluation at FHEQ level 6 (FQHEIS level 10): " + name + ". Cite it as (" + CITE + "3.7), naming the area. "
           "Do not claim every course must teach it as a separate module, or that it holds below honours level. Set it beside " + nb + " and the level 6 knowledge descriptors qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b2."),
      aad=("Raise it when a student or a team asks what a broad business degree should cover in " + name + ". With a student, ask: " + q + " With staff, ask where this area is taught and assessed. Avoid reading the whole list aloud; take the one area in question."),
      **AREA)
area(1, 'ethics, responsibility and sustainability', ['managing', 'behaving'], 'ethics, responsibility and sustainability',
     "Should show knowledge and critical evaluation of managing responsibly and acting ethically, above all on social, cultural, legal, economic and environmental questions.",
     "Graduates should be able to show and critically evaluate responsible management and ethical conduct across social, cultural, legal, economic and environmental issues.",
     "You should be able to show you understand, and can critically judge, what it means to manage responsibly and act ethically on social, cultural, legal, economic and environmental questions.",
     'paras 1.25 to 1.28', 'what would a responsible choice look like in a decision you have studied?')
area(2, 'markets and economies', [], 'markets and economies',
     "Should show knowledge and critical evaluation of how markets for resources, goods and services form, are reached and work, including market failure, externalities and fair trade.",
     "Graduates should be able to show and critically evaluate how markets develop and operate, with market failure, externalities and fair trade.",
     "You should be able to show you understand how markets for resources, goods and services grow and work, including when they fail, their side effects and fair trade.",
     'para 3.4 on the business environment', 'can you explain one market failure and who bears its cost?')
area(3, 'marketing, sales, negotiation and customers', ['generating'], 'marketing, sales, negotiation and customers',
     "Should show knowledge and critical evaluation of managing customer relationships, consumer behaviour, segmenting, targeting and positioning, selling and innovating in products and services.",
     "Graduates should be able to show and critically evaluate customer relationship management, consumer behaviour, segmentation, targeting and positioning, sales and product and service innovation.",
     "You should be able to show you understand, and can judge critically, how organisations manage customers, how consumers behave, how markets are segmented and targeted, how sales are made and why products need innovation.",
     'paras 3.10.b4 (commercial acumen) and 3.10.b7 (networking)', 'how would you decide which customers a product is for?')
area(4, 'finance and accounting', [], 'finance and accounting',
     "Should show knowledge and critical evaluation of where finance comes from, how it is managed, and how accounting and other information systems support planning, control, decisions and financial risk.",
     "Graduates should be able to show and critically evaluate where finance comes from and how it is managed, and how accounting and information systems serve planning, control, decisions and financial risk.",
     "You should be able to show you understand where money for an organisation comes from, how it is managed, and how accounts and information systems help plan, control, decide and manage financial risk.",
     'para 3.10.b6 (numeracy)', 'what would the accounts tell you about the risk in a decision?')
area(5, 'people and organisational behaviour', ['grounded'], 'people, organisational behaviour and EDI',
     "Should show knowledge and critical evaluation of responsible, inclusive and ethical leadership, managing and developing people and organisations, employee engagement and employment law, grounded in cross-cultural understanding and EDI.",
     "Graduates should be able to show and critically evaluate inclusive, ethical leadership, people management and development, engagement and the legal context, with cross-cultural and EDI understanding.",
     "You should be able to show you understand, and can judge critically, how people are led, managed and developed in organisations, how staff are engaged, what the law requires, and how culture and inclusion shape this.",
     'paras 1.6 and 1.15 to 1.20, to which the item points', 'how would you keep a diverse team engaged?')
area(6, 'operations and business innovation', [], 'operations and business innovation',
     "Should show knowledge and critical evaluation of managing resources, supply chains, procurement, logistics, outsourcing, quality systems, service excellence and projects.",
     "Graduates should be able to show and critically evaluate operations: resources, supply chain, procurement, logistics, outsourcing, quality, service and project management.",
     "You should be able to show you understand, and can judge critically, how organisations manage resources, supply chains, buying, logistics, outsourcing, quality, service and projects.",
     'para 1.26.b1 (sustainable supply chains, as an example topic)', 'where would you look first to improve how an organisation delivers its service?')
area(7, 'data analytics, digital business and information systems', ['deliver', 'enable'], 'data, digital business and information systems',
     "Should show knowledge and critical evaluation of setting strategic priorities for fast delivery through managing and applying information systems, their effect on organisations, and data-led decisions.",
     "Graduates should be able to show and critically evaluate data analytics, statistics, digital business and information systems, their organisational impact and data-driven decision-making.",
     "You should be able to show you understand, and can judge critically, how data, statistics and information systems are used in business and how they help organisations make decisions.",
     'paras 3.10.b3 (research), 3.10.b6 (numeracy) and 3.11.b4 (digital literacy)', 'what data would you want before making a decision in your project?')
area(8, 'business policy and strategy', [], 'business policy and strategy',
     "Should show knowledge and critical evaluation of forming policies and strategies for a changing setting and stakeholder interests, with risk and crisis management, continuity planning and communication used to reach strategic aims.",
     "Graduates should be able to show and critically evaluate how policies and strategies are developed for changing environments, with risk, crisis, continuity and communication methods.",
     "You should be able to show you understand, and can judge critically, how organisations set policy and strategy in a changing world, manage risk and crises, keep going through disruption and communicate their plans.",
     'para 3.2 on risk and para 3.4 on the business environment', 'how would a strategy you know change if a crisis hit?')
area(9, 'public and non-profit management', [], 'public and non-profit management',
     "Should show knowledge and critical evaluation of what is distinct in public service bodies and the voluntary and community sector: governance, finance, public leadership, community empowerment, coproduction, public value and hybrid delivery.",
     "Graduates should be able to show and critically evaluate public and non-profit management: governance, finance, leadership, empowerment, coproduction, public values and hybrid service delivery.",
     "You should be able to show you understand, and can judge critically, how public services and voluntary and community organisations are run, funded, led and governed, and how they work with communities.",
     'para 1.5 on organisations read broadly and para 2.5', 'how does running a charity differ from running a company?')
s('3.7.b10', find='entrepreneurship and enterprise development: taking innovative business ideas to create or co-create new products, services or organisations that will generate a return on financial and/or social investment - this includes, but is not limited to, the identification of intellectual property and appreciation of its value (see also paragraphs 1.29-1.33).',
  verbs=['taking', 'create', 'generate'], about='entrepreneurship and enterprise development',
  para="Should show knowledge and critical evaluation of turning new business ideas into products, services or organisations that return financial or social value, including spotting intellectual property and valuing it.",
  prac="Graduates should be able to show and critically evaluate how new ventures, products and services are created for financial or social return, including intellectual property.",
  ben="You should be able to show you understand, and can judge critically, how new business ideas become products, services or organisations that pay back financially or socially, and why intellectual property matters.",
  aaw=("Treat this as a knowledge area in which honours graduates should be able to show knowledge, understanding and critical evaluation at FHEQ level 6 (FQHEIS level 10): entrepreneurship and enterprise development. Cite it as (" + CITE + "3.7), naming the area. "
       "Do not claim every course must teach it as a separate module, or that it holds below honours level. Set it beside paras 1.29 to 1.33, para 3.10.b5 and std:doc:qaa-enterprise-2018-guidance, and the level 6 descriptor qaa/fheq-2024/4.15.b1."),
  aad=("Raise it when a student is thinking about a venture or a team plans enterprise teaching. With a student, ask: who would pay for your idea, and what part of it could you protect? With staff, ask where this area is taught and assessed. Avoid treating it as only for students who want to start a business."),
  **AREA)

s('3.9', type='outcome', rung='none', force='should', level='fheq:6', appliesTo='graduates of the subject', addressee='learner',
  verbs=['demonstrate'], about='cognitive, subject-specific, personal and interpersonal skills', domain='subject-skill', award=HON,
  para="Graduates should be able to show cognitive and intellectual skills with competencies particular to business and management, and also personal and interpersonal skills, both subject-specific and generic.",
  prac="Graduates should be able to show intellectual skills and business competencies, and personal and interpersonal skills; plan for subject-specific and generic skills alike (listed in 3.10 and 3.11).",
  ben="You should be able to show thinking skills and business competencies, and personal and interpersonal skills, both specific to business and useful anywhere.",
  aaw="Describe this as an outcome (should) for honours graduates at FHEQ level 6: the skill set that paras 3.10 and 3.11 then list. Cite it as (" + CITE + "3.9) and set it beside the rung items on skills, paras 4.5.b2, 4.6.b2 and 4.7.b2, and qaa/fheq-2024/4.15.b6 to 4.15.b9.3. Do not claim each listed skill is a separate threshold requirement; the lists name skills, the rungs set the standard.",
  aad="Raise it when a student is mapping their skills for a placement or CV. Ask them to sort their skills into business-specific and general, and to give one example of each. Avoid presenting the lists in 3.10 and 3.11 as a checklist they must tick off.")

SK = dict(rung='none', type='outcome', force='describes', level='fheq:6', appliesTo='graduates of the subject', addressee='learner', award=HON)
def skill(n, k, dom, name, verbs, about, para, prac, ben, nb, q):
    lead = 'a skill of particular relevance to the subject' if n == '3.10' else 'one of the other generic skills and attributes'
    s('%s.b%d' % (n, k), verbs=verbs, about=about, para=para, prac=prac, ben=ben, domain=dom,
      aaw=("Present this as " + lead + " (" + name + "), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (" + CITE + n + "), naming the skill. "
           "Do not claim it is a threshold requirement on its own; set it beside " + nb + "."),
      aad=("Raise it when a student reflects on " + name + " or a team plans where it is developed. Ask: " + q + " Avoid reading the list out or treating it as a checklist."),
      **SK)
skill('3.10', 1, 'subject-skill', 'people management', ['nurturing'], 'people management',
      "People management: communicating, building teams, resilience and well-being, leading and motivating, and fostering EDI.",
      "Develop people management: communication, team building, resilience and well-being, leading and motivating others, and nurturing EDI.",
      "You develop skills in managing people: communicating, building teams, looking after resilience and well-being, leading and motivating others, and making teams inclusive.",
      'paras 3.7.b5 and 1.18, and the employment qualities in qaa/fheq-2024/4.15.b9.1', 'when did you last motivate someone, and what worked?')
skill('3.10', 2, 'subject-skill', 'problem-solving and critical analysis', ['analysing', 'determine', 'selecting'], 'problem-solving and critical analysis',
      "Problem-solving and critical analysis: examining facts and circumstances to find a problem's cause, then deciding on fitting, sustainable solutions.",
      "Develop problem-solving and critical analysis: diagnosing causes from facts and circumstances, then deciding on sustainable solutions.",
      "You develop skills in solving problems and analysing critically: working out what caused a problem, making decisions and choosing sustainable solutions.",
      'qaa/fheq-2024/4.15.b3.1 and 4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r3/3rd', 'how did you find the real cause of a problem you faced?')
s('3.10.b3', find='research: the ability to analyse and evaluate a range of data, sources of information and appropriate methodologies, which includes the need for strong digital literacy,\n\n15\nand to use that research for evidence-based, responsible and ethical decision- making',
  verbs=['analyse', 'evaluate', 'use'], about='research and evidence-based decisions', domain='subject-skill',
  para="Research: analysing and judging data, information sources and suitable methods, with strong digital literacy, and using the findings for decisions that are evidence-based, responsible and ethical.",
  prac="Develop research skills: analysing and evaluating data, sources and methods, with strong digital literacy, and applying findings to responsible, ethical, evidence-based decisions.",
  ben="You develop research skills: analysing and weighing up data, sources and methods, using digital tools well, and basing responsible, ethical decisions on the evidence.",
  aaw=("Present this as a skill of particular relevance to the subject (research), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (" + CITE + "3.10), naming the skill. "
       "Do not claim it requires a dissertation; set it beside para 3.7.b7, qaa/fheq-2024/4.15.b3.2 and 4.15.b6, and qaa/fqheis-2024/4.16.b5."),
  aad=("Raise it when a student plans a project or a team designs research teaching. Ask: what evidence would change your mind about your recommendation? Avoid reading the list out or treating it as a checklist."),
  **SK)
skill('3.10', 4, 'subject-skill', 'commercial acumen', ['based'], 'commercial acumen',
      "Commercial acumen: grounded in awareness of what drives business success and failure, and why customer satisfaction and loyalty matter, pursued sustainably.",
      "Develop commercial acumen: awareness of the drivers of success, causes of failure, and sustainable customer satisfaction and loyalty.",
      "You develop commercial sense: knowing what makes businesses succeed or fail and why keeping customers satisfied and loyal, in sustainable ways, matters.",
      'para 3.7.b3 and the threshold application item 4.5.b4', 'what would you say drives success in a business you know?')
skill('3.10', 5, 'subject-skill', 'innovation, creativity and enterprise', ['act', 'generate', 'develop', 'communicate', 'manage', 'exploit', 'gain', 'deliver'], 'innovation, creativity and enterprise',
      "Innovation, creativity and enterprise: acting entrepreneurially to produce, develop and share ideas, handle and use intellectual property, win support and achieve sustainable results.",
      "Develop innovation, creativity and enterprise: entrepreneurial action to generate and communicate ideas, manage intellectual property, gain backing and deliver sustainable outcomes.",
      "You develop enterprise skills: coming up with and sharing ideas, protecting and using intellectual property, winning support and delivering lasting results.",
      'paras 1.29 to 1.33, para 3.7.b10 and std:doc:qaa-enterprise-2018-guidance', 'which of your ideas could you turn into something real, and who would back it?')
skill('3.10', 6, 'subject-skill', 'numeracy', ['manipulate', 'evaluate', 'estimate', 'model'], 'numeracy and quantitative skills',
      "Numeracy: using quantitative skills to work with data and to judge, estimate and model the problems and functions of a business.",
      "Develop numeracy: quantitative skills to handle data and to evaluate, estimate and model business problems.",
      "You develop number skills: working with data and estimating, evaluating and modelling business problems.",
      'para 3.7.b4 and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd', 'how confident are you building a simple model of a business problem?')
skill('3.10', 7, 'subject-skill', 'networking', ['cultivating'], 'networking and interpersonal skills',
      "Networking: awareness of listening, negotiating, persuading and presenting, and using them to build business contacts.",
      "Develop networking: listening, negotiation, persuasion and presentation used to cultivate business contacts.",
      "You develop networking skills: listening well, negotiating, persuading and presenting, and using these to build business contacts.",
      'para 3.7.b3 and qaa/fheq-2024/4.15.b8', 'who in your field would you most like to meet, and how would you approach them?')
skill('3.10', 8, 'subject-skill', 'leadership', ['including'], 'boundary-spanning and collaborative leadership',
      "Leadership: spanning boundaries, influencing, relating and collaborating, including partnership working across organisations and sectors.",
      "Develop leadership: boundary-spanning, influence, relational and collaborative work and partnership across organisations and sectors.",
      "You develop leadership skills: working across boundaries, influencing others, building relationships and partnering with other organisations and sectors.",
      'paras 1.6 and 1.26 and qaa/fheq-2024/4.15.b9.2', 'when have you had to lead people who did not report to you?')

skill('3.11', 1, 'generic-skill', 'collaborative and inclusive working', [], 'collaborative and inclusive working',
      "Working together, inclusively, with stakeholders inside and outside the organisation.",
      "Develop collaborative, inclusive working with internal and external stakeholders.",
      "You learn to work with others inclusively, both inside your organisation and beyond it.",
      'Annex D qaa/fheq-2024/annex-d/transferable/r2/3rd and spine:6', 'how do you make sure everyone in a group can contribute?')
skill('3.11', 2, 'generic-skill', 'communication', [], 'verbal, non-verbal and digital communication',
      "Communicating in speech, without words and through digital means.",
      "Develop verbal, non-verbal and digital communication.",
      "You learn to communicate well in speech, through body language and online.",
      'qaa/fheq-2024/4.15.b8 and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd', 'which audience do you find hardest to communicate with?')
skill('3.11', 3, 'generic-skill', 'empathy and inclusivity', [], 'empathy and inclusivity',
      "Empathy and inclusivity.",
      "Develop empathy and inclusivity.",
      "You learn to understand how others feel and to include them.",
      'paras 1.17 and 1.18 and spine:6', 'how do you notice when someone feels left out?')
skill('3.11', 4, 'generic-skill', 'digital literacy and etiquette', [], 'digital literacy and etiquette',
      "Using digital tools capably and behaving appropriately online.",
      "Develop digital literacy and appropriate digital conduct.",
      "You learn to use digital tools well and to behave appropriately online.",
      'paras 3.7.b7 and 3.10.b3 and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd', 'which digital tools do you rely on, and which would you like to master?')
skill('3.11', 5, 'generic-skill', 'conceptual, systemic and critical thinking', [], 'conceptual, systemic and critical thinking',
      "Conceptual, systems and critical thinking, with analysis, synthesis and evaluation.",
      "Develop thinking that is conceptual, systemic and critical, with analysis, synthesis and evaluation.",
      "You learn to think in concepts and systems, and critically: analysing, bringing ideas together and judging them.",
      'qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/3rd', 'can you trace how one change ripples through a whole organisation?')
skill('3.11', 6, 'generic-skill', 'self-management', ['accept', 'tolerate', 'handle', 'challenge', 'use'], 'self-management and independent learning',
      "Self-management: growing as an independent learner, ready to take responsibility, be flexible, live with uncertainty, handle complexity, question assumptions, think critically from evidence, and be resilient, self-starting and suitably assertive.",
      "Develop self-management: independent learning, responsibility, flexibility, tolerance of uncertainty, handling complexity, challenging assumptions, evidence-led critical thinking, resilience and appropriate assertiveness.",
      "You learn to manage yourself: learning independently, taking responsibility, staying flexible, coping with uncertainty and complexity, questioning assumptions, using evidence, bouncing back and speaking up when you need to.",
      'qaa/fheq-2024/4.15.b5 and 4.15.b9.1 and Annex D qaa/fheq-2024/annex-d/transferable/r3/3rd', 'when did you last cope well with not knowing the answer?')
skill('3.11', 7, 'generic-skill', 'self-reflection', [], 'self-reflection and sensitivity to diversity',
      "Self-reflection: analysing oneself, awareness of and sensitivity to differences between people and cultures, and a lasting wish to develop.",
      "Develop self-reflection: self-analysis, sensitivity to diversity in people and cultures, and continuing appetite for development.",
      "You learn to reflect on yourself, to be aware of and sensitive to differences between people and cultures, and to keep wanting to grow.",
      'Annex D qaa/fheq-2024/annex-d/transferable/r5/3rd and spine:6', 'what have you learned about yourself from working with people unlike you?')

# ------------------------------------------------------------- section 3: assessment expectations
s('3.18', type='requirement', rung='none', force='should', level='none', appliesTo='assessment in the course', addressee='provider',
  verbs=['form', 'provided', 'enabling'], about='assessment for learning and timely, usable feedback', domain='none', award=HON,
  para="Assessment should be part of learning, helped by feedback on formative and summative work; feedback should come in good time and be usable, supporting development within a module and across the course.",
  prac="Make assessment part of learning: give feedback on formative and summative work, promptly and in a form students can act on within the module and across the course.",
  ben=('n/a', 'a duty on those who set and mark assessment'),
  aaw="Describe this as an expectation (should) on assessment design and feedback in honours courses. Cite it as (" + CITE + "3.18) and set it beside paras 3.19, 3.20 and 3.25. Do not present it as a student outcome.",
  aad="Raise it when a team reviews feedback turnaround or format. Ask whether students can act on the feedback before their next assessment. Keep the duty with staff.")

s('3.20', type='requirement', rung='none', force='describes', level='none', appliesTo='assessment methods', addressee='provider',
  find='While assessment methods need to be a reliable means of assessing the intended learning outcomes and be inclusive in design, they can be diverse, innovative and assist in developing skills in their own right.',
  verbs=['assessing', 'developing'], about='reliable, inclusive and varied assessment methods', domain='none', award=HON,
  para="Assessment methods need to assess the intended outcomes reliably and be inclusively designed (the issuer's 'need to', recorded as describes), and may also be varied, new and skill-building in themselves.",
  prac="Choose assessment methods that reliably test the intended outcomes and are inclusive by design; they can also be varied and innovative and build skills in their own right.",
  ben=('n/a', 'a duty on those who design assessment'),
  aaw="Describe this as an expectation on assessment design stated with 'need to', recorded as describes. Cite it as (" + CITE + "3.20) and set it beside paras 3.18, 3.19 and 3.22. Do not present the list of typical methods that follows as required.",
  aad="Raise it when a team chooses or changes assessment methods. Ask how a method shows the outcome reliably and who might be disadvantaged by it. Keep it for staff.")

s('3.23', type='requirement', rung='none', force='should', level='none', appliesTo='group assessment', addressee='provider',
  verbs=['given'], about='extent, fit and marking of group work', domain='none', award=HON,
  para="When assessment is done in groups, care should go into how much group work a course has, how authentic and suited to its task it is, and how marks are split between group and individual.",
  prac="Weigh the amount of group assessment across the course, its authenticity and fit to the task, and how group and individual marks are attributed.",
  ben=('n/a', 'a duty on assessment design'),
  aaw="Describe this as an expectation (should) on group assessment design. Cite it as (" + CITE + "3.23) and set it beside paras 3.24 on peer assessment and 3.10.b8 on collaborative working. Do not present it as a student standard.",
  aad="Raise it when a team adds or reviews group assessment. Ask how individual contribution is recognised in the mark. Keep it for staff; a student worried about group marks can be pointed to the course's rules.")

s('3.24', type='requirement', rung='none', force='should', level='none', appliesTo='peer review and assessment', addressee='provider',
  verbs=['provided', 'set'], about='guidance and weighting limits for peer assessment', domain='none', award=HON,
  para="Peer review and assessment can engage students in assessment and learning; whether formative or summative, students should get clear guidance and the weight of peer marks in a unit or module should be capped.",
  prac="When using peer assessment, give students clear guidance and cap the weight of peer marks in a module.",
  ben=('n/a', 'a duty on assessment design'),
  aaw="Describe this as an expectation (should) on peer assessment: clear guidance and limited weighting. Cite it as (" + CITE + "3.24) and set it beside paras 3.23 and 3.25. Do not present it as a student standard.",
  aad="Raise it when a team plans peer assessment. Ask what share of the module mark peer marks would carry and what guidance students get. Keep it with staff.")

s('3.25', type='requirement', rung='none', force='should', level='none', appliesTo='assessment information', addressee='provider',
  verbs=['shared', 'co-design'], about='transparent assessment and shared marking criteria', domain='none', award=HON,
  para="Assessment details should be open and given to students with the marking criteria; students may also co-design assessments with tutors or peers.",
  prac="Share assessment details and marking criteria with students openly, and consider co-designing assessments with them.",
  ben=('n/a', 'a duty on the course team; students meet its effect'),
  aaw="Describe this as an expectation (should) that assessment details and criteria are shared, with co-design as an option (may). Cite it as (" + CITE + "3.25) and set it beside para 3.18. Do not claim co-design is required.",
  aad="Raise it when students say they do not know how they are marked. With staff, ask where the criteria are published and when students see them. Do not put the duty on students.")

s('3.26', type='requirement', rung='none', force='should', level='none', appliesTo='assessment design', addressee='provider',
  verbs=['designed'], about='assessment designed with workload in mind', domain='none', award=HON,
  para="Assessment design should take account of how much work students carry.",
  prac="Plan assessment with the student's whole workload in view, across modules and deadlines.",
  ben=('n/a', 'a duty on assessment design'),
  aaw="Describe this as an expectation (should) on assessment design. Cite it as (" + CITE + "3.26) and set it beside paras 3.18 to 3.25. Do not present it as a student standard.",
  aad="Raise it when deadlines cluster or a team adds assessment. Ask what a student's weeks look like at peak assessment. Keep it with staff.")

# ------------------------------------------------------------- section 4
s('4.2', type='requirement', rung='none', force='should', level='fheq:6', appliesTo='higher education providers', addressee='provider',
  verbs=['perform', 'refer'], about='most exceed threshold; refer to Annex D for degree classes', domain='none', award=HON,
  para="Most students will do much better than the minimum threshold; each provider decides what evidence shows achievement and should refer to Annex D, which describes the four honours classes (1st, 2.1, 2.2, 3rd) for FHEQ level 6 and FQHEIS level 10.",
  prac="Set your own evidence of achievement, but refer to Annex D's descriptions of the four honours classes; expect most students to perform well above the threshold.",
  ben=('n/a', 'a duty on the provider in setting classification evidence'),
  aaw="Describe this as a provider expectation (should) to refer to Annex D, with a stated expectation (will) that most students exceed the threshold, at FHEQ level 6 and FQHEIS level 10. Cite it as (" + CITE + "4.2) and set it beside qaa/fheq-2024/annex-d/summary/r1/3rd to r1/1st and the FHEQ document's SL6 bands. Do not claim the statement itself sets the class boundaries.",
  aad="Raise it when a team aligns its marking criteria to degree classes. Ask how their criteria for a 2.1 compare with Annex D's description. Keep it with staff.")

s('4.3', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='honours graduates of the subject', addressee='both',
  verbs=['differentiate', 'achieve', 'describe'], about='threshold as minimum, typical as the expected norm', domain='none', award=HON,
  para="Three categories, threshold, typical and excellent, set apart graduates' achievement and rest on perceived national norms in the subject; threshold is the minimum for all honours graduates, and most students should reach typical.",
  prac="Use the three categories for individual performance: threshold is the floor for every honours graduate, and most students should reach the typical standard.",
  ben="If you complete an honours degree you will have reached at least the minimum standard, and, like most students, you should reach the typical standard.",
  aaw="Describe this as the statement's own reading of its rungs at FHEQ level 6: threshold the minimum for every honours graduate, typical what most should reach (should). Cite it as (" + CITE + "4.3) and set it beside paras 4.5 to 4.7 and the Annex D bands qaa/fheq-2024/annex-d/summary/r1/3rd to r1/1st. Do not claim typical is a pass requirement.",
  aad="Raise it when a student asks what is expected of them or whether the minimum is enough. Ask them which standard they are aiming for and why. Never present the typical or excellent standard as the minimum.")

# ------------------------------------------------------------- rungs 4.5 threshold, 4.6 typical, 4.7 excellent
RUNG = {'threshold': '4.5', 'typical': '4.6', 'excellent': '4.7'}
CLASS = {'threshold': 'any honours degree (the 3rd class marks the threshold in Annex D)', 'typical': 'a second class honours degree', 'excellent': 'a first class honours degree'}
BAND = {'threshold': '3rd', 'typical': '2.2 and 2.1', 'excellent': '1st'}
CAT = {
    1: dict(name='knowledge and understanding', dom='knowledge', fw='qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1', ad='knowledge/r1',
            q='how many areas of business can you explain, and how do they connect in practice?'),
    2: dict(name='skills', dom='subject-skill', fw='qaa/fheq-2024/4.15.b2 and 4.15.b6', ad='practical/r1',
            q='which subject skills could you show an employer evidence for today?'),
    3: dict(name='critical perspective', dom='understanding', fw='qaa/fheq-2024/4.15.b7 and 4.15.b5', ad='cognitive/r2',
            q='whose view of business do you rely on most, and when did you last question it?'),
    4: dict(name='application', dom='subject-skill', fw='qaa/fheq-2024/4.15.b3.1 and 4.15.b9.2', ad='cognitive/r3',
            q='when did you last apply theory to a real organisation, and what did it show you?'),
    5: dict(name='values', dom='generic-skill', fw='qaa/fheq-2024/4.15.b9.1 and spine:6 (strand:autonomy)', ad='transferable/r4',
            q='where in your work have you acted on global social responsibility, not only discussed it?'),
}
BL = {'threshold': 'To reach the minimum standard, ', 'typical': 'To reach the typical standard, ', 'excellent': 'To reach the excellent standard, '}
def kr(rung, k, verbs, about, para, prac, ben):
    c = CAT[k]; n = RUNG[rung]
    below = {'threshold': None, 'typical': '4.5.b%d' % k, 'excellent': '4.6.b%d' % k}[rung]
    above = {'threshold': '4.6.b%d' % k, 'typical': '4.7.b%d' % k, 'excellent': None}[rung]
    nb = ' and '.join(x for x in (below, above) if x)
    force_txt = {'threshold': 'the threshold every honours graduate will have shown (will)',
                 'typical': 'the typical standard most graduates will have shown (will typically), above the minimum',
                 'excellent': 'the excellent standard shown at first class (will), an aspiration rather than a requirement'}[rung]
    avoid = {'threshold': 'Do not present it as the expected standard, since most students go well beyond it (para 4.2).',
             'typical': 'Do not present it as the minimum for an honours degree; that is the threshold item.',
             'excellent': 'Do not present it as the minimum or as expected of most students.'}[rung]
    avoid_d = {'threshold': 'Avoid suggesting the minimum is the goal most students should settle for.',
               'typical': 'Never treat this as the pass standard.',
               'excellent': 'Never present this as what everyone must reach.'}[rung]
    s('%s.b%d' % (n, k), type=rung, rung=rung, force='will', level='fheq:6', appliesTo='honours graduates at the %s rung' % rung,
      addressee='learner', award=HON, verbs=verbs, about=about, domain=c['dom'], para=para, prac=prac, ben=BL[rung] + ben,
      aaw=("Treat this as " + force_txt + " for " + c['name'] + ", for " + CLASS[rung] + " in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (" + CITE + n + ", " + c['name'] + "). "
           + avoid + " Set it beside " + nb + " (the same category at the next rung), the level descriptors " + c['fw'] + ", and Annex D qaa/fheq-2024/annex-d/" + c['ad'] + " at the " + BAND[rung] + " band."),
      aad=("Raise it when a student asks what " + rung + " work looks like in " + c['name'] + ", or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: " + c['q'] + " " + avoid_d))

kr('threshold', 1, [], 'key areas, their relationships and application',
   "Will have shown knowledge and understanding of the main areas of business and management, how they relate and how they are applied.",
   "At threshold, graduates will have shown they know and understand the key areas of the subject, how they interrelate and how they apply.",
   "you will have shown that you know and understand the main areas of business and management, how they link and how they are used.")
kr('threshold', 2, [], 'competence across subject-specific and generic skills',
   "Will have shown competence across the subject's own skills and its generic skills and attributes.",
   "At threshold, graduates will have shown competence across the subject-specific and generic skills and attributes.",
   "you will have shown that you are competent in the range of business skills and general skills.")
kr('threshold', 3, ['influenced'], 'a mainly guided view with some critical perspective',
   "Will have shown a view of the subject shaped mostly by guided learning, with some sign of a critical stance.",
   "At threshold, graduates will hold a view of the subject formed largely through guided learning, with some evidence of critical perspective.",
   "your view of business will come mostly from what you have been guided to learn, with some signs that you question it.")
kr('threshold', 4, ['apply'], 'applying knowledge in a current organisational setting',
   "Will have shown the skills and abilities to use knowledge in a present-day organisational setting.",
   "At threshold, graduates will have shown they can apply their knowledge in a contemporary organisation.",
   "you will have shown that you can use what you know in a present-day organisation.")
kr('threshold', 5, ['practise'], 'practising global social responsibility',
   "Will have shown the capacity to act on the values of global social responsibility.",
   "At threshold, graduates will have shown a capacity to practise global social responsibility.",
   "you will have shown that you can put the values of global social responsibility into practice.")

kr('typical', 1, [], 'solid knowledge of a broad range and complex relationships',
   "Will typically have shown solid, substantial knowledge and understanding across a broad range of business and management areas, the complex links between them and how they are applied in practice.",
   "At the typical rung, graduates will usually have shown solid, substantial knowledge across many areas, their complex interrelations and their use in practice.",
   "you will usually have shown solid, substantial knowledge across a broad range of business areas, the complex ways they link and how they work in practice.")
kr('typical', 2, [], 'command of subject skills, proficiency in generic skills',
   "Will typically have shown command of subject-specific skills and proficiency in generic skills and attributes.",
   "At the typical rung, graduates will usually have shown command of the subject's skills and proficiency in generic ones.",
   "you will usually have shown command of business skills and real proficiency in general skills.")
kr('typical', 3, ['influenced'], 'a view drawn from wide sources, with independence and critical evaluation',
   "Will typically have shown a view of the subject drawn from a wide range of fitting sources, with evidence of independent learning and critical evaluation.",
   "At the typical rung, graduates will usually have a view informed by wide, appropriate sources, showing independent learning and critical evaluation.",
   "your view of business will usually draw on many suitable sources, showing that you learn independently and judge critically.")
kr('typical', 4, ['apply', 'develop', 'deal', 'explore', 'demonstrate', 'integrate'], 'applying knowledge in complex settings, with own perspectives',
   "Will typically have shown the ability to use knowledge in complex, current organisational settings, and some capacity to form and use their own views, handle uncertainty and complexity, look at alternative answers, evaluate critically and bring theory in.",
   "At the typical rung, graduates will usually apply knowledge in complex organisations and show some capacity for their own perspective, coping with uncertainty, weighing alternatives, critical evaluation and integrating theory.",
   "you will usually be able to use what you know in complex organisations, and show some ability to form your own views, cope with uncertainty, weigh up alternatives, judge critically and draw on theory.")
kr('typical', 5, ['integrate'], 'integrating global social responsibility',
   "Will typically have shown the ability to build the values of global social responsibility into their work.",
   "At the typical rung, graduates will usually have shown they can integrate the values of global social responsibility.",
   "you will usually have shown that you can build the values of global social responsibility into what you do.")
P['4.6.b5']['find'] = 'values: an ability to integrate the values of global social responsibility.'

kr('excellent', 1, [], 'advanced, critical knowledge and detailed relationships',
   "Will have shown advanced knowledge and critical understanding across a broad range of business and management areas, the detailed links between them and their application in practice.",
   "At the excellent rung, graduates will have shown advanced knowledge and critical understanding of many areas, their detailed interrelations and their use in practice.",
   "you will have shown advanced knowledge and a critical grasp of a broad range of business areas, the detailed ways they link and how they apply in practice.")
kr('excellent', 2, [], 'excellent command of subject skills, proficiency in generic skills',
   "Will have shown excellent command of subject-specific skills and proficiency in generic skills and attributes.",
   "At the excellent rung, graduates will have shown excellent command of the subject's skills and proficiency in generic ones.",
   "you will have shown excellent command of business skills and real proficiency in general skills.")
kr('excellent', 3, ['influenced', 'challenging', 'questioning'], 'a proactive, independent view that challenges assumptions',
   "Will have shown a view of the subject built from analysing wide sources, through proactive, independent learning that challenges assumptions and questions the status quo.",
   "At the excellent rung, graduates will hold a view formed by analysing wide sources, learning proactively and independently, challenging assumptions and questioning accepted practice.",
   "your view of business will come from analysing many sources, learning on your own initiative, challenging assumptions and questioning the way things are done.")
kr('excellent', 4, ['develop', 'apply', 'deal', 'explore', 'demonstrate', 'integrate'], 'exceptional own perspective and integration of theory and practice',
   "Will have shown exceptional ability to form and use their own views, handle uncertainty and complexity, look at alternative answers, evaluate critically and join theory with practice in many situations.",
   "At the excellent rung, graduates will have shown exceptional capacity for their own perspective, for uncertainty and complexity, alternatives, critical evaluation and integrating theory and practice widely.",
   "you will have shown an exceptional ability to form your own views, cope with uncertainty and complexity, weigh up alternatives, judge critically and join theory with practice in many situations.")
kr('excellent', 5, ['challenge', 'champion', 'appreciating'], 'championing global social responsibility while weighing its debates',
   "Will have shown the ability to challenge assumptions and champion global social responsibility while recognising the debates and conflicting views it raises in complex business settings.",
   "At the excellent rung, graduates will have shown they can challenge assumptions and champion global social responsibility while appreciating its debates and tensions in complex settings.",
   "you will have shown that you can challenge assumptions and champion global social responsibility, while seeing the debates and disagreements it raises in complex business settings.")

# gradeOf: the issuer labels each item with the same category at every rung (knowledge and understanding, skills,
# critical perspective, application, values), so the pairing is stated.
GRADE = {}
for _k in range(1, 6):
    GRADE['4.6.b%d' % _k] = '4.5.b%d|stated' % _k
    GRADE['4.7.b%d' % _k] = '4.6.b%d|stated' % _k

TH = {'1.15': 'theme:edi', '1.17': 'theme:edi', '1.18': 'theme:edi', '1.19': 'theme:edi', '1.21': 'theme:edi',
      '1.22': 'theme:accessibility', '1.24': 'theme:accessibility', '1.26': 'theme:esd'}

S5 = dict(
    levels=[
        dict(id='fheq:6', role='cites', locator='D1, 2.7; 4.2'),
        dict(id='fqheis:10', role='cites', locator='D1, 2.7; 4.2'),
        dict(id='fheq:7', role='cites', locator='D1, 2.10 (integrated master\'s)'),
        dict(id='fqheis:11', role='cites', locator='D1, 2.10 (integrated master\'s)'),
        dict(id='fheq:4', role='inferred: CertHE named as an exit award (D1, 2.9); level from std:doc:qaa-fheq-2024-framework S5', locator='D1, 2.9'),
        dict(id='fheq:5', role='inferred: DipHE named as an exit award (D1, 2.9); level from std:doc:qaa-fheq-2024-framework S5', locator='D1, 2.9'),
        dict(id='spine:6', role='inferred: the reference framework step for the honours standards (std:ref:uk-framework R2, R8)', locator='D1, 4.5 to 4.7'),
    ],
    crosswalks=[
        dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.7: "(FHEQ Level 6; FQHEIS Level 10)"; 4.2)'),
        dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.10)'),
        dict(**{'from': 'fheq:6'}, to='cqfw:6', relation='compares-with', basis='inferred from std:doc:qaa-fheq-2024-framework S5 (its 2.24); the statement does not name the CQFW (Part E)'),
    ])

S6 = [
    dict(id='theme:edi', role='carries', carriedIn=['1.6', '1.14', '1.15', '1.16', '1.17', '1.18', '1.19', '1.20', '1.21', '1.23', '2.4', '2.11', '2.17', '2.20', '3.7', '3.10', '3.11', '3.16', '3.19', '3.20']),
    dict(id='theme:accessibility', role='carries', carriedIn=['1.19', '1.20', '1.22', '1.23', '1.24', '2.11', '2.12', '3.19']),
    dict(id='theme:esd', role='carries', carriedIn=['1.6', '1.14', '1.17', '1.25', '1.26', '1.27', '1.28', '1.33', '2.4', '3.4', '3.7', '3.10']),
    dict(id='theme:enterprise', role='carries', carriedIn=['1.7', '1.14', '1.29', '1.30', '1.31', '1.32', '1.33', '3.7', '3.10', '3.16']),
]

S7 = [
    dict(rel='supersedes', target='std:doc:qaa-business-and-management-2019-benchmarks (not held)', note='the fourth edition, 2019, named in section 6; earlier editions 2015, 2007 and 2000 are named there too'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the degree outcome classification descriptions for FHEQ level 6 and FQHEIS level 10, cited as QAA 2019 (4.2; section 5); now part of the 2024 Frameworks'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ levels 6 and 7 (2.7, 2.10, 4.2)'),
    dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS levels 10 and 11 (2.7, 2.10, 4.2)'),
    dict(rel='themeReference', target='std:doc:qaa-advancehe-esd-2021-guidance', note='Education for Sustainable Development Guidance, QAA and Advance HE 2021 (1.25, 1.28)'),
    dict(rel='themeReference', target='std:doc:qaa-enterprise-2018-guidance', note='Enterprise and Entrepreneurship Education guidance, QAA 2018 (1.32)'),
    dict(rel='refersTo', target='QAA Characteristics Statement: Higher Education in Apprenticeships, 2022 (not yet ingested)', note='1.2'),
    dict(rel='refersTo', target='QAA Characteristics Statement: Micro-Credentials (not yet ingested)', note='2.12'),
    dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance; QAA Glossary (not ingested)', note='front matter'),
    dict(rel='relatedTo', target='the allied Subject Benchmark Statements for Accounting, Economics, Finance, and Events, Hospitality, Leisure, Sport and Tourism', note='named in 1.2 without editions; held: std:doc:qaa-accounting-2025-benchmarks, std:doc:qaa-economics-2023-benchmarks, std:doc:qaa-finance-2025-benchmarks (inferred editions, Part E)'),
    dict(rel='refersTo', target='UN Sustainable Development Goals; UN Principles for Responsible Management Education; UN Curriculum on Governance for the SDGs; IPCC 2022 (not standards documents)', note='1.17, 1.25, 1.26, 1.27'),
]

SB1 = [
    "A broad, general study of organisations, their cultures, structures and management in economic, environmental and social context, rather than one function or sector (D1, 1.2, 1.4).",
    "Organisations and business are read widely: public, private, non-profit, community and social enterprises of every size, from start-ups to global firms (D1, 1.5, 2.5).",
    "Responsible leadership runs through it: values-led, inclusive, ethical and sustainable, with attention to climate change and net zero (D1, 1.6, 3.6).",
    "Interdisciplinary and varied, drawing on the social sciences, humanities and sciences, with theory always set beside practice (D1, 1.10, 1.11, 2.1).",
    "Courses range from vocational study for business to research-oriented study of business, most combining the two (D1, 2.2, 3.14).",
    "Strongly tied to practice and employability, through partnerships, placements, live projects and practitioner input (D1, 2.14, 3.8, 3.15).",
    "A dynamic, changing discipline whose courses are expected to keep innovating (D1, 1.3, 1.12, 2.6).",
]

SB2 = [
    dict(theme='theme:edi', inThisSubject="framed through why, what and how the subject is taught: business education as a lever against inequality (with the SDGs), anti-discrimination law and inclusive workplaces as content, diverse cases including the Global South, and inclusive modes and assessment; reviewed with students (D1, 1.15 to 1.21)",
         statements=['1.15', '1.17', '1.18', '1.19', '1.21', '3.7.b5', '3.10.b1', '3.11.b1', '3.11.b3']),
    dict(theme='theme:accessibility', inThisSubject="regulatory minimum and whole-journey reach, reasonable adjustments in assessment, mindfulness of digital poverty and caring duties, and equal access to placements and international learning (D1, 1.22 to 1.24, 2.11, 2.12)",
         statements=['1.22', '1.24']),
    dict(theme='theme:esd', inThisSubject="sustainable management as a condition of planetary survival, the SDGs and PRME, ethics, responsibility and sustainability (ERS) expected by some accreditors, carbon literacy and sustainable supply chains as example topics (D1, 1.25 to 1.28, 2.4)",
         statements=['1.26', '3.7.b1']),
    dict(theme='theme:enterprise', inThisSubject="entrepreneurship as a subject area and enterprise as a set of behaviours: venture creation, innovation inside established organisations, social enterprise and experiential learning; the front matter joins it with employability (D1, 1.29 to 1.33, 3.7, 3.10)",
         statements=['3.7.b10', '3.10.b5']),
]

SB3 = dict(
    areas=[
        dict(component='3.4', gloss='the business environment: local to international factors acting on organisations'),
        dict(component='3.5', gloss='organisations: internal functions, structures, governance, cultures'),
        dict(component='3.6', gloss='responsible leadership and management: theories, models and roles'),
        dict(component='3.7', gloss='ten areas, from ethics, responsibility and sustainability to entrepreneurship and enterprise development'),
    ],
    practices=[
        dict(component='3.15', kind='teaching', gloss='theory joined with practice; inputs from managers, entrepreneurs and stakeholders'),
        dict(component='3.16', kind='learning', gloss='inclusive methods and modes; lectures, seminars, workshops, placements, live projects, simulations, mentoring, start-up'),
        dict(component='3.17', kind='assessment', gloss='skills development defined and assessed, as process or product'),
        dict(component='3.18', kind='assessment', gloss='assessment for learning with timely feedback'),
        dict(component='3.19', kind='assessment', gloss='inclusive assessment design that anticipates needs'),
        dict(component='3.20', kind='assessment', gloss='reliable, inclusive, varied methods: reports, exams, presentations, dissertations, portfolios'),
        dict(component='3.22', kind='assessment', gloss='authentic assessment'),
        dict(component='3.23', kind='assessment', gloss='group work: extent, fit and attribution of marks'),
        dict(component='3.24', kind='assessment', gloss='peer assessment with guidance and capped weighting'),
        dict(component='3.25', kind='assessment', gloss='transparent criteria; co-designed assessment'),
    ])

SB4 = dict(
    rungs=[
        dict(rung='threshold', leadIn='4.5', award=HON, items=5),
        dict(rung='typical', leadIn='4.6', award=HON, items=5),
        dict(rung='excellent', leadIn='4.7', award=HON, items=5),
    ],
    rungBases="4.4: the categories differ by range and consistency in showing breadth, depth, integration and application of knowledge; competence in subject-specific, academic and professional skills; depth of critical perspective; ability to apply knowledge and skills; capacity to practise global social responsibility. 4.3: threshold is the minimum for all honours graduates; most should reach typical. The lead-ins tie the rungs to degree classes: honours (threshold), second class (typical), first class (excellent).",
    outcomeLists=[
        dict(leadIn='3.7', gloss='ten areas of knowledge, understanding and critical evaluation (should)', items=10, award=['honours']),
        dict(leadIn='3.10', gloss='eight skills of particular relevance to the subject (describes; 3.9 carries should)', items=8, award=['honours']),
        dict(leadIn='3.11', gloss='seven other generic skills and attributes (describes; 3.9 carries should)', items=7, award=['honours']),
    ],
    outcomes=[
        dict(outcome='knowledge and understanding', threshold='4.5.b1', typical='4.6.b1', excellent='4.7.b1', basis='stated', domain='knowledge', award=HON),
        dict(outcome='skills', threshold='4.5.b2', typical='4.6.b2', excellent='4.7.b2', basis='stated', domain='subject-skill', award=HON),
        dict(outcome='critical perspective', threshold='4.5.b3', typical='4.6.b3', excellent='4.7.b3', basis='stated', domain='understanding', award=HON),
        dict(outcome='application', threshold='4.5.b4', typical='4.6.b4', excellent='4.7.b4', basis='stated', domain='subject-skill', award=HON),
        dict(outcome='values', threshold='4.5.b5', typical='4.6.b5', excellent='4.7.b5', basis='stated', domain='generic-skill', award=HON),
    ])
SB4A_FULL = []

SB5 = [
    dict(body='professional, statutory and regulatory bodies (PSRBs), in general', says='the statement supports PSRBs on academic standards; courses may reflect their requirements for recognition, which helps learners apply management skills at work; vocational courses may need their accreditation (D1, front matter, 1.9, 2.15, 2.21)', requirements='not-applicable-by-design: no body named'),
    dict(body='accrediting bodies (unnamed)', says='some expect ethics, responsibility and sustainability to be integrated into business school curricula (D1, 1.25)', requirements='not-applicable-by-design: no body named'),
    dict(body='Principles for Responsible Management Education (PRME)', says='a UN initiative courses can draw on to build students\' capacity to create sustainable value; one of the networks providers may engage with (D1, 1.25, 2.16)', requirements='not yet ingested (Part E)'),
    dict(body='Chartered Association of Business Schools (CABS)', says='a network providers may engage with for good practice and development (D1, 2.16 and its footnote)', requirements='not yet ingested (Part E)'),
    dict(body='British Academy of Management (BAM)', says='a learned society providers may engage with (D1, 2.16 and its footnote)', requirements='not yet ingested (Part E)'),
    dict(body='Association to Advance Collegiate Schools of Business (AACSB)', says='an accreditation body for business schools providers may engage with (D1, 2.16 and its footnote)', requirements='not yet ingested (Part E)'),
    dict(body='European Foundation for Management Development (EFMD)', says='a body providers may engage with (D1, 2.16 and its footnote); its EQUIS and programme accreditation are listed in section 5', requirements='not yet ingested (Part E)'),
    dict(body='Chartered Management Institute (CMI)', says='named only in the references (its professional standards for management and leadership) and the advisory group, not in the numbered text (D1, section 5)', requirements='not yet ingested (Part E)'),
]

SB6 = dict(
    themes=[
        dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['front matter', '1.6', '1.14', '1.15', '1.16', '1.17', '1.18', '1.19', '1.20', '1.21', '1.23', '2.4', '2.11', '2.17', '2.20', '3.7', '3.10', '3.11', '3.16', '3.19', '3.20'],
             statements=['1.15', '1.17', '1.18', '1.19', '1.21', '3.7.b5', '3.10.b1', '3.11.b1', '3.11.b3']),
        dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=['front matter', '1.19', '1.20', '1.22', '1.23', '1.24', '2.11', '2.12', '3.19'],
             statements=['1.22', '1.24']),
        dict(id='theme:esd', named='Education for Sustainable Development', carriedIn=['front matter', '1.6', '1.14', '1.17', '1.25', '1.26', '1.27', '1.28', '1.33', '2.4', '3.4', '3.7', '3.10'],
             statements=['1.26', '3.7.b1']),
        dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['front matter', '1.7', '1.14', '1.29', '1.30', '1.31', '1.32', '1.33', '3.7', '3.10', '3.16'],
             statements=['3.7.b10', '3.10.b5']),
    ],
    frameworks=[
        dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.7', '2.10', '4.2']),
        dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.7', '2.10', '4.2']),
    ],
    bodies=[
        dict(body='professional, statutory and regulatory bodies (PSRBs)', citedIn=['front matter', '1.9', '2.15', '2.21']),
        dict(body='accrediting bodies (unnamed)', citedIn=['1.25']),
        dict(body='Principles for Responsible Management Education (PRME)', citedIn=['1.25', '2.16']),
        dict(body='Chartered Association of Business Schools (CABS)', citedIn=['2.16']),
        dict(body='British Academy of Management (BAM)', citedIn=['2.16']),
        dict(body='Association to Advance Collegiate Schools of Business (AACSB)', citedIn=['2.16']),
        dict(body='European Foundation for Management Development (EFMD)', citedIn=['2.16']),
        dict(body='Office for Students (regulatory framework, England)', citedIn=['front matter']),
    ],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'], role='descriptions of the four honours classes (1st, 2.1, 2.2, 3rd) that providers should refer to when setting evidence of achievement'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named="QAA and Advance HE's Education for Sustainable Development Guidance, 2021", citedIn=['1.25', '1.28'], role='the competencies the subject\'s core skills align with; disciplinary method for sustainability'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='enterprise behaviours, attributes and competencies (as defined by QAA, 2018)', citedIn=['1.32'], role='source of the enterprise competencies reflected in the skills of 3.9'),
        dict(document='QAA Characteristics Statement: Higher Education in Apprenticeships, 2022 (not yet ingested: Part E)', named='Higher Education in Apprenticeships Characteristic Statement, QAA, 2022', citedIn=['1.2'], role='for degree apprenticeships in the subject'),
        dict(document="QAA Characteristics Statement: Micro-Credentials (not yet ingested: Part E)", named="QAA's Characteristics Statement: Micro-Credentials", citedIn=['2.12'], role='flexible credit alongside modular credit'),
        dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code', citedIn=['front matter'], role='course design, teaching, external expertise, monitoring and evaluation'),
        dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
    ])

B1 = [
    dict(slug='organisations', definition='read broadly: public, private, non-profit, community-based and social enterprises of every size and structure, from start-ups to global firms (D1, 1.5)', beneficiaryDefinition='every kind of organisation, from a small charity or start-up to a global company or public body', scopeNote='business is read just as broadly (1.5)', category='unknown', practices=['business and management']),
    dict(slug='responsible-leadership', definition='leadership that is values-led, inclusive, ethical, sustainable, systemic and transformative, weighing stakeholders now and in future and addressing climate change (D1, 1.6)', beneficiaryDefinition='leading in a way that is ethical, inclusive and sustainable and thinks about everyone affected, now and later', scopeNote='used in 1.4, 3.6 and 3.7', category='unknown', practices=['business and management']),
    dict(slug='preparation-for-a-career-in-business-and-management', definition='building knowledge and skills for career readiness, self-awareness and personal development, and a constructive attitude to change and enterprise (D1, 1.7)', beneficiaryDefinition='getting ready for work in any organisation, knowing yourself and being open to change', scopeNote='', category='unknown', practices=['business and management']),
    dict(slug='skills-and-attributes', definition='transferable academic and professional skills suited to, but not limited to, business careers (D1, 1.8)', beneficiaryDefinition='skills you can carry into any career', scopeNote='', category='unknown', practices=['business and management']),
    dict(slug='ethics-responsibility-and-sustainability', definition='ERS: the triad some accrediting bodies expect business school curricula to integrate (D1, 1.25, 1.27)', beneficiaryDefinition='acting ethically, responsibly and sustainably in business', scopeNote='also the first area in 3.7', category='unknown', practices=['business and management']),
    dict(slug='enterprise-and-entrepreneurship-education', definition='EED: education building the behaviours, attributes and competencies for successful careers, venture creation and innovation (D1, 1.29)', beneficiaryDefinition='learning to spot opportunities and turn ideas into value, in a new venture or an existing organisation', scopeNote='', category='unknown', practices=['business and management']),
    dict(slug='threshold-typical-excellent', definition='the three categories of graduate achievement: threshold the minimum for every honours graduate, typical what most should reach, excellent the highest (D1, 4.3)', beneficiaryDefinition='the minimum, the usual and the highest standard for your honours degree', scopeNote='tied to honours, second class and first class in 4.5 to 4.7', category='unknown', practices=['education']),
]
B2A = [
    dict(concept='organisations', form="'Organisations'", lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='responsible-leadership', form="'responsible leadership'", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='preparation-for-a-career-in-business-and-management', form="'Preparation for a career in business and management'", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='skills-and-attributes', form="'skills and attributes'", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='ethics-responsibility-and-sustainability', form='ethics, responsibility and sustainability (ERS)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='enterprise-and-entrepreneurship-education', form='Enterprise and entrepreneurship education (EED)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='threshold-typical-excellent', form="'Threshold', 'Typical', 'Excellent'", lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
]
B4 = []; B5 = []

D3 = [
    dict(source='QAA Characteristics Statement: Higher Education in Apprenticeships (2022)', why='cited in 1.2 for degree apprenticeships; not ingested'),
    dict(source='QAA Characteristics Statement: Micro-Credentials', why='cited in 2.12; not ingested'),
    dict(source='QAA Subject Benchmark Statement: Business and Management (2019, fourth edition)', why='the edition this one supersedes, for the change comparison'),
]

E = [
    'Rungs: three, each a lead-in with five items in five named categories (knowledge and understanding, skills, critical perspective, application, values); the lead-ins tie each rung to a degree class (honours, second class, first class), which Psychology does not do. gradeOf recorded as stated, since the issuer labels each item with the same category at every rung; P3 to confirm that the shared label counts as pairing.',
    'Typical lead-in (4.6) reads "will typically have demonstrated" and names "a second class honours degree" without splitting 2.1 and 2.2; recorded as force will and set beside Annex D at both 2.2 and 2.1.',
    'Domains on the rungs: the "skills" items (4.5.b2, 4.6.b2, 4.7.b2) cover subject-specific and generic skills together; recorded as subject-skill. "Critical perspective" recorded as understanding, "application" as subject-skill, "values" (global social responsibility) as generic-skill at fheq:6. All inferred: P3.',
    'Outcome list 3.7 (lead-in "should reasonably be expected to be able to demonstrate"): ten areas, force should; a new lead-in wording against Psychology ("are able to").',
    'Lists 3.10 and 3.11 have no modal in their lead-ins ("include"); recorded as outcome items with force describes, since 3.9 ("should be able to demonstrate") governs them; P3 to rule whether they take 3.9\'s should.',
    'Obliging words outside the five, recorded as describes: 1.26 "needs to be integrated" (also "imperative", "a requirement for planetary survival"); 3.20 "need to be a reliable means". Not cut: 3.16 "They need to take account" (across a page break, a plain-present teaching norm), 3.19 "It is important that", 1.16 "It is important that", 2.7 "it is expected that" (recorded with will), 4.3 "it is expected that most students should".',
    'Plain-present provider norms, not statements (template open point 5): 1.4 the four purposes ("are to"), 1.11, 2.1 to 2.6, 2.17, 3.1, 3.8, 3.12 ("the course enables graduates to develop and demonstrate"), 3.14, 3.15, 3.16, 3.17, 3.21, 3.22.',
    'Not statements, judged: 1.5 and 1.7 ("should be understood", definitions, to Part B); 1.6 ("will incorporate", a definition); 1.20, 1.22 items, 1.26 items, 2.12 items, 2.14 items, 3.16 items and 3.20 items (examples or options with may, could or typically); 2.19 (describes external examining); 4.1 (introduces the rungs); 4.4 (rung bases, in SB4).',
    '1.22 cut by find to its obliging sentence only; its list (taking actions, ensuring access, confirming assessments, remaining mindful) follows "It may include" and is not cut.',
    'Skeleton corrections: 3.7.b10 ended in the heading "Skills and practice" and 4.6.b5 in "Excellent level"; both recut by find. 3.10.b3 was cut at a page break; recut by find to include its second half (the span holds the page number 15). 4.4.b5 holds the heading "Threshold level" but 4.4 is not a statement.',
    'Skeleton candidate 2.16.b1 is the tail of 2.16 after a footnote marker, not a list item; 2.16 is descriptive (may).',
    'Repeated numbers: the footnote marker "1" after 2.16 and its text (the expansions of CABS, BAM, AACSB, EFMD, PRME) sit inside 2.16 and 2.19 in the held text; not statements.',
    'Inferred subject codes (P3 to confirm; held back from lookup): hecos 100079 business studies, hecos 100089 management studies.',
    'Awards: honours is the award of the rungs; 1.2 extends use to the first-degree elements of integrated master\'s (FHEQ 7, FQHEIS 11, 2.10) and to degree apprenticeships; awardsCovered keeps honours only. CertHE and DipHE (2.9) are exit awards; fheq:4 and fheq:5 inferred.',
    'CQFW: not named in the text, though the statement is a key reference point in Wales; fheq:6 to cqfw:6 recorded as inferred from the FHEQ document.',
    'Annex D is cited as QAA 2019 (section 5); linked to its current home in std:doc:qaa-fheq-2024-framework (recall that the 2024 Frameworks carry it: confirmed in that document\'s SL6).',
    'Allied statements in 1.2 are named without editions; the held editions (accounting 2025, economics 2023, finance 2025) may postdate this statement. No events, hospitality, leisure, sport and tourism statement is held.',
    'Masters Degrees in Business and Management (2023) is a separate statement, not named in this text; any link is inferred and left for P3.',
    'Theme: employability is named in the front matter with enterprise ("employability, entrepreneurship and enterprise education"); recorded under theme:enterprise as Psychology did. No generative AI section.',
    'Bodies: PRME, CABS, BAM, AACSB and EFMD are named in 2.16 and its footnote; CMI appears only in section 5 and the advisory group; the Office for Students only in the front matter. Accrediting bodies (1.25) and PSRBs are unnamed. None of their requirements is ingested.',
    'S9 commentary not researched in P1.',
    'Licence: QAA copyright; the document gives no re-use terms in its text.',
]
