# Judgement file for run 0134, QAA Veterinary Nursing 2024 (std). Built by tools/bm_build.py (BM-BRIEF 0.2.3).
# Keys are S4 ids under qaa/veterinary-nursing-2024/. Our words everywhere except `find` (the issuer's cell text, located in the held text).
import re as _re

_NORM_PATH = '/home/claude/wkspc2601-library/txt/qaa-2024-veterinary-nursing-subject-benchmark-statement-standard.norm.txt'
_norm = open(_NORM_PATH, encoding='utf-8').read()

def _exact(text):
    pat = _re.escape(text).replace("'", "['\u2019]").replace('\\ ', r'\s+')
    return _re.compile(pat).search(_norm).group(0)

FD = 'foundation degree'
HON = "bachelor's with honours"
MA = "master's"
SID = 'qaa/veterinary-nursing-2024'
CITE = 'QAA (2024), Veterinary Nursing Subject Benchmark Statement'

META = dict(
    run='0134', p1='2026-10-03 18:44',
    title='Subject Benchmark Statement Veterinary Nursing',
    heading='Subject Benchmark Statement: Veterinary Nursing (QAA, April 2024)',
    edition='April 2024 (third edition)', published='2024-04',
    status='current', supersedes='the second edition, 2019 (D1, section 6); first edition 2015',
    subjects=[dict(scheme='hecos', code='100532', label='veterinary nursing', basis='stated'),
              dict(scheme='cah', code='CAH05-01-02', label='others in veterinary sciences', basis='inferred')],
    awards=[FD, HON, MA], levels=['fheq:5', 'fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2024 revision (third edition for this subject)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=('This document records what the 2024 Veterinary Nursing statement expects of graduates at three awards: '
                     'a foundation degree (FHEQ level 5), a bachelor\'s degree with honours (FHEQ level 6, SCQF level 10) and a master\'s '
                     'degree (FHEQ level 7, SCQF level 11). Its standards are all threshold standards, set out in four tables with one column per award, '
                     'beside the duties on course design that sections 1 to 3 place on providers. An agent should use the statement ids here when it '
                     'writes or talks about a veterinary nursing course, keep each award\'s column to that award, and read the RCVS requirements '
                     'as separate documents.'),
    summary=('A science-based, strongly vocational subject whose courses should prepare graduates to register as veterinary nurses with the RCVS '
             'on graduating. The statement sets threshold standards only (no typical or excellent rungs), for three awards side by side in four '
             'tables: generic skills; principles and concepts in application; subject knowledge, understanding and skills; and working as a '
             'professional veterinary nurse. Sections 1 to 3 add course duties on the RCVS Day One Competences, Skills and Professional '
             'Behaviours, placements, partnership, assessment and minimum content. Themes: equality, diversity and inclusion; accessibility; '
             'sustainability; enterprise and entrepreneurship education. Bodies: the RCVS (PSRB) and the Office for Students. '
             'Annex D of the FHEQ is cited for honours classification.'),
    authority='reference: a sector reference point, not a regulatory requirement; a key reference point in Wales and Scotland and part of quality requirements in Northern Ireland, not a sector-recognised standard in England (D1, front matter)')

S2 = dict(
    governs=('what a Veterinary Nursing graduate can be expected to know, do and understand at the end of a foundation degree, a bachelor\'s '
             'degree with honours or a master\'s degree, and the nature of awards in the subject (D1, front matter; 1.6; 1.9; 4.1)'),
    awards=['foundation degree', "bachelor's degree with honours", "master's degree"],
    levels=['fheq:5', 'fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    howUsed=['design', 'approval', 'review', 'other: external examining; PSRBs; information for prospective students and employers'],
    doesNot='it does not prescribe teaching, learning or assessment, does not interpret legislation and carries no statutory or regulatory requirement (D1, front matter)',
    statedScope='"The purpose of this Subject Benchmark Statement is to make explicit the nature and the academic standards of degrees in Veterinary Nursing." (D1, 1.6)',
    statedSubjects=[
        dict(name='Veterinary Nursing', locator='(D1, 1.6)', kind='subject', codes=[dict(scheme='hecos', code='100532', label='veterinary nursing')]),
        dict(name='small animal Veterinary Nursing', locator='(D1, 3.3)', kind='specialism', codes=[dict(scheme='hecos', code='100532', label='veterinary nursing')]),
        dict(name='equine Veterinary Nursing', locator='(D1, 3.4)', kind='specialism', codes=[dict(scheme='hecos', code='100532', label='veterinary nursing')]),
    ])

SECTIONS = {'1': 'Context and purposes of a Veterinary Nursing degree', '2': 'Distinctive features of a Veterinary Nursing degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.5', 'Context'), ('1.6', '1.10', 'Purposes and characteristics of a Veterinary Nursing degree'),
       ('1.11', '1.13', 'Equality, diversity and inclusion'), ('1.14', '1.16', 'Accessibility'), ('1.17', '1.19', 'Sustainability'),
       ('1.20', '1.22', 'Enterprise and entrepreneurship education'), ('2.1', '2.5', 'Design'), ('2.6', '2.6', 'Progression'),
       ('2.7', '2.7', 'Flexibility'), ('2.8', '2.12', 'Partnership'), ('2.13', '2.15', 'Monitoring and review'), ('3.1', '3.1', 'Content'),
       ('3.2', '3.6', 'Research and evidence-based practice'), ('3.7', '3.8', 'Clinical and technical skills'),
       ('3.9', '3.10', 'Personal and professional skills and behaviours'), ('3.11', '3.13', 'Teaching and learning'),
       ('3.14', '3.18', 'Assessment'), ('4.1', '4.2', 'Introduction')]

G = {
    '1.1': 'what veterinary nurses do and where they work',
    '1.2': 'the aims of veterinary nursing: health, welfare, comfort',
    '1.3': 'the scope of a registered veterinary nurse\'s role',
    '1.4': 'RCVS registration, code and accountability',
    '1.5': 'the five principles in the code of conduct',
    '1.6': 'purpose of the statement; a vocational science degree leading to registration',
    '1.7': 'licence to practise courses and the Day One requirements',
    '1.8': 'what the statement describes and which awards it covers',
    '1.9': 'awards and framework levels covered',
    '1.10': 'room for variety in course design',
    '1.11': 'the statement\'s stance on equity and diversity',
    '1.12': 'inclusive learning and placement environments',
    '1.13': 'programmes that build personal responsibility for inclusion',
    '1.14': 'accessibility across the whole course, with examples',
    '1.15': 'flexible, inclusive design that avoids barriers',
    '1.16': 'equal workplace learning and inclusive digital access',
    '1.17': 'the profession and sustainable development; ethics, responsibility and sustainability',
    '1.18': 'climate action and sustainable management in the curriculum',
    '1.19': 'example sustainability topics for courses',
    '1.20': 'what enterprise education offers students',
    '1.21': 'entrepreneurial competencies beyond employment',
    '1.22': 'designing enterprise education with employers and others',
    '2.1': 'minimum subject areas a course should include',
    '2.2': 'meeting the Day One requirements as a condition of accreditation',
    '2.3': 'how the focus differs by award',
    '2.4': 'extensive practical teaching across the Day One skills',
    '2.5': 'clinical placement time in approved training practices',
    '2.6': 'progression through the levels and on to postgraduate study',
    '2.7': 'modes, formats and credit',
    '2.8': 'partnership with the RCVS on accreditation',
    '2.9': 'partnerships with further education colleges and their oversight',
    '2.10': 'students as partners; the student voice',
    '2.11': 'partnership with placement providers; written agreements',
    '2.12': 'approving training practices and training clinical supervisors',
    '2.13': 'monitoring, evaluation and periodic review',
    '2.14': 'external reviewers in periodic review',
    '2.15': 'the role of external examiners',
    '3.1': 'areas of knowledge across species',
    '3.2': 'research and evidence-based practice activities',
    '3.3': 'species for small animal nursing degrees',
    '3.4': 'equine nursing degrees',
    '3.5': 'farm animal husbandry in some curricula',
    '3.6': 'the range of skills students build',
    '3.7': 'clinical and technical skills developed',
    '3.8': 'skills learned in class and on placement',
    '3.9': 'ethics, culture, law and professional duties in course design',
    '3.10': 'personal and professional abilities to develop',
    '3.11': 'teaching and assessment set locally with the RCVS',
    '3.12': 'reflective, critical, student-centred learning',
    '3.13': 'skills teaching should build; the research project',
    '3.14': 'aligned assessment that separates threshold from higher achievement',
    '3.15': 'progressive, varied, authentic and inclusive assessment',
    '3.16': 'formative and summative assessment',
    '3.17': 'assessing competence and fitness to practise; clinical placement',
    '3.18': 'emphasis at postgraduate level on applied evidence and research skills',
    '4.1': 'threshold standards for the three awards',
    '4.2': 'performance above threshold; Annex D; then the four standards tables',
}
CTYPE = {'3.1': 'area', '3.2': 'area', '3.5': 'area', '3.7': 'area', '3.9': 'area',
         '3.8': 'practice', '3.11': 'practice', '3.12': 'practice', '3.16': 'practice', '3.17': 'practice'}
EXCLUDED = [
    dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2, SB5 and SB6'),
    dict(number='section headings 1 to 4', heading='the section heading lines', kind='other: headings, recorded in SECTIONS'),
    dict(number='5', heading='List of references and further resources', kind='other: references, read for SB6 and D3'),
    dict(number='6', heading='Membership of the Advisory Group', kind='other: authorship and edition history, read for S8'),
]

P = {}
def s(i, **k):
    P[i] = k

def aw(nature, holds, para, notc, beside):
    return (f"Present this as {nature}, holding for {holds}. Cite it as {CITE}, para {para}. "
            f"Do not claim {notc}. Set it beside {beside}.")

def ad(when, how, q, avoid):
    return f"Raise it when {when}. {how} Ask: \"{q}\" Avoid {avoid}."

HOW_L = 'Put it plainly, in the second person to a student, and as a teaching and assessment question to staff.'
HOW_P = 'Put it to the programme team as a design question; with a student, say only what it means for their course.'
AV_L = 'reading the paragraph aloud at length or making it sound stricter than it is'
AV_P = 'presenting this duty to a student as something they must do, or reading the paragraph aloud at length'
NA_P = 'a duty on the course and its provider; the student meets its effect, not a standard to reach'

# ------------------------------------------------------------------ sections 1 to 3: obliging paragraphs and outcome lists
s('1.4', type='requirement', rung='none', force='must', level='none', appliesTo='veterinary nurses who wish to practise in the UK',
  addressee='learner', verbs=['registered', 'agree', 'adhere'], about='registration, the code of conduct and accountability', domain='none', award='none',
  para='Anyone who wants to practise as a veterinary nurse in the UK must be on the RCVS register and must commit to its code of conduct, answering for their actions and keeping their knowledge current through reflective continuing professional development; fitness to practise procedures hold them to account.',
  prac='Practice in the UK must rest on RCVS registration, a commitment to its code, accountability and regular reflective CPD; the course is where students first meet these professional obligations.',
  ben='To work as a veterinary nurse in the UK you must join the RCVS register, keep to its code of conduct, answer for what you do and keep your skills current through professional development that you reflect on.',
  aaw=aw('a condition of professional practice that the statement reports (a must, set by the RCVS, not by the statement)', 'anyone entering practice after any of the three awards', '1.4',
         'that the degree alone confers registration or that the statement itself imposes this duty', '1.7 and 2.2 on the Day One requirements and qaa/fheq-2024/4.12.b8 and 4.15.b9.1 on personal responsibility'),
  aad=ad('a student asks what they need beyond the degree to work as a veterinary nurse', HOW_L,
         'What do you understand about registering with the RCVS and keeping up your professional development once you qualify?', AV_L))
s('1.6', type='expectation', rung='none', force='should', level='none', appliesTo='Veterinary Nursing courses', addressee='provider',
  verbs=['equip'], about='courses that prepare graduates for registration on graduating', domain='none', award=[FD, HON, MA],
  para='The statement sets out the nature and academic standards of veterinary nursing degrees: a science-based, strongly vocational course that should prepare graduates to register as veterinary nurses on graduating.',
  prac='Design the course as science-based and strongly vocational so that it should leave graduates ready to register as veterinary nurses on the day they graduate.',
  ben=('n/a', NA_P),
  aaw=aw('a course aim with the force of should', 'courses at all three awards', '1.6', 'that every award listed leads to registration or that the statement sets accreditation rules',
         '1.7, 2.2 and 2.5 on accreditation and placement, and the RCVS requirements recorded in SB5'),
  aad=ad('a programme team asks what the overall purpose of a veterinary nursing course should be', HOW_P,
         'How does your course leave graduates ready to register at the point they finish?', AV_P))
s('1.7', type='expectation', rung='none', force='should', level='none', appliesTo='licence to practise courses accredited by the RCVS',
  addressee='both', verbs=['designed', 'acquire', 'evidence', 'meet'], about='the Day One Competences, Skills and Professional Behaviours', domain='none', award=[FD, HON],
  para='An RCVS-accredited licence to practise course should be built so that graduates can gain and show the Day One Competences, the Day One Skills List and the Professional Behaviours and Attributes, the RCVS minimum that every student veterinary nurse must meet to join its register.',
  prac='Build an accredited licence to practise course so that students should be able to gain and evidence the Day One Competences, Skills and Professional Behaviours; the RCVS sets these as the minimum for joining its register.',
  ben='Your course should be set up so that you can gain and show the Day One Competences, the Day One Skills and the professional behaviours; the RCVS requires you to meet them before you can join its register.',
  aaw=aw('a course design expectation (should) resting on an RCVS minimum (must)', 'licence to practise courses', '1.7',
         'that the statement defines the Day One requirements; they are the RCVS\'s and are recorded as a separate document (SB5)', '2.2, 2.5, 2.11 and 1.14 on the same requirements'),
  aad=ad('a student or team asks what the Day One requirements are and how the course covers them', HOW_L,
         'Which of the Day One Competences and Skills have you already evidenced, and which are still to come?', AV_L))
s('1.12', type='expectation', rung='none', force='should', level='none', appliesTo='course design', addressee='provider',
  verbs=['designed', 'ensure'], about='equitable access through proactive, flexible design', domain='none', award=[FD, HON, MA],
  para='Learning settings, placements included, should be inclusive; courses should be designed proactively and flexibly for equitable access, and providers, staff and students share responsibility for promoting equity and challenging bias.',
  prac='Design the course, placements included, proactively and flexibly so that access to learning should be equitable; staff and students share the work of promoting equity and challenging stereotypes.',
  ben=('n/a', NA_P),
  aaw=aw('a provider duty (should) under the equality, diversity and inclusion theme', 'courses at all three awards', '1.12',
         'that it sets a legal standard; it is a sector expectation', '1.13, the inclusion rows of the generic skills table (4.2.b8 to 4.2.b10) and 4.2.b43'),
  aad=ad('a programme team reviews whether its course and placements are inclusive by design', HOW_P,
         'Where might a student meet a barrier in your course or placements, and how is the design meant to remove it?', AV_P))
s('1.13', type='expectation', rung='none', force='should', level='none', appliesTo='veterinary nursing programmes and their students',
  addressee='both', verbs=['designed', 'considered'], about='personal responsibility for equity and inclusive practice', domain='none', award=[FD, HON, MA],
  para='Programmes should be designed to encourage openness and participation and to build each person\'s sense of responsibility for equity and inclusive practice, as a student and as a registered nurse; this should be treated as a professional responsibility in teams and with the public.',
  prac='Design the programme so that it should foster openness and each student\'s responsibility for equity and inclusion, framed as a professional duty in teamwork and in educating owners and the public.',
  ben='Your course should help you see equity and inclusion as part of your own professional responsibility, in your team and when you advise animal owners and the public.',
  aaw=aw('an expectation (should) on programme design with a student-facing aim', 'all three awards', '1.13',
         'that it is a competence assessed in its own right; the tables carry the assessed forms', '1.12, 4.2.b8 to 4.2.b10 and 4.2.b43'),
  aad=ad('a student asks why inclusion matters in a clinical role, or a team plans how to teach it', HOW_L,
         'Can you think of a time at work or on placement when you made sure a client or colleague was treated fairly?', AV_L))
s('1.14', type='expectation', rung='none', force='should', level='none', appliesTo='all stages of the course', addressee='provider',
  verbs=['meet', 'apply'], about='accessibility from pre-application to graduation', domain='none', award=[FD, HON, MA],
  para='Accessibility asks whether everything in a course can be understood by everyone; it should meet any regulatory requirement as a minimum and should run from pre-application information to graduation and beyond, for example through accessible curricula, safe learning spaces and adjustable assessment that lets every student meet the RCVS requirements.',
  prac='Make every stage accessible: as a minimum it should meet regulatory requirements and should cover information before application through to after graduation, including the curriculum, learning spaces and adjustable assessment.',
  ben=('n/a', NA_P),
  aaw=aw('a provider duty (should) under the accessibility theme', 'courses at all three awards', '1.14',
         'that the listed examples are a complete or required set; the paragraph says it may include them', '1.15, 1.16 and 3.15 on adjusted assessment'),
  aad=ad('a team checks accessibility across the student journey', HOW_P,
         'Which stage of your course, from application to graduation, is hardest for a disabled student to use, and what changes would help?', AV_P))
s('1.15', type='expectation', rung='none', force='should', level='none', appliesTo='course, module, teaching and assessment design', addressee='provider',
  verbs=['taken', 'build', 'avoid'], about='flexible, inclusive design for specific learning differences', domain='none', award=[FD, HON, MA],
  para='Proactive and innovative approaches should be used in designing courses, modules, teaching and assessment so that flexibility and inclusion are built in and students with specific learning differences meet no needless barriers.',
  prac='Use proactive, innovative design for courses, modules, teaching and assessment that should build in flexibility and inclusion from the start and avoid barriers for students with specific learning differences.',
  ben=('n/a', NA_P),
  aaw=aw('a provider duty (should) under the accessibility theme', 'courses at all three awards', '1.15',
         'that it requires any particular method', '1.14, 1.16 and 3.15'),
  aad=ad('a team designs or revises a module or assessment', HOW_P,
         'If a student with dyslexia took this module, where would they first struggle, and what would you change?', AV_P))
s('1.16', type='expectation', rung='none', force='should', level='none', appliesTo='workplace learning and digital provision', addressee='provider',
  verbs=['include', 'enabling', 'providing'], about='equal workplace learning and inclusive digital access', domain='none', award=[FD, HON, MA],
  para='Accessibility should give every student the same chance of workplace learning and inclusive digital access free of discrimination.',
  prac='Accessibility should extend to placements, so every student has the same workplace learning opportunities, and to digital provision that is inclusive and free of discrimination.',
  ben=('n/a', NA_P),
  aaw=aw('a provider duty (should) under the accessibility theme', 'courses at all three awards', '1.16',
         'that it guarantees any particular placement', '1.14, 1.15, 2.5 and 2.11 on placements'),
  aad=ad('a team plans placements or digital learning', HOW_P,
         'Do all your students get the same quality of placement and digital access, and how do you know?', AV_P))
s('1.17', type='expectation', rung='none', force='describes', level='none', appliesTo='the Veterinary Nursing curriculum', addressee='provider',
  verbs=['contribute', 'draw', 'develop', 'integrated'], about='ethics, responsibility and sustainability in the curriculum', domain='none', award=[FD, HON, MA],
  para='The profession can support sustainable development as the UN goals frame it, through content and method; courses can use the UN principles for responsible management education, and the statement sets an expectation that ethics, responsibility and sustainability are woven into the curriculum.',
  prac='Weave ethics, responsibility and sustainability through the curriculum, as the statement expects, drawing if useful on the UN principles for responsible management education so students can help sustain the profession.',
  ben=('n/a', NA_P),
  aaw=aw('an expectation on the curriculum stated as "an expectation", outside the five modal words (recorded as describes)', 'courses at all three awards', '1.17',
         'that it is a must or a should', '1.18, the sustainability row 4.2.b11 and the ESD guidance std:doc:qaa-advancehe-esd-2021-guidance'),
  aad=ad('a team asks how sustainability should feature in a veterinary nursing course', HOW_P,
         'Where in your curriculum do students meet the ethics and sustainability of veterinary work?', AV_P))
s('1.18', type='expectation', rung='none', force='should', level='none', appliesTo='veterinary nurses and the curriculum', addressee='both',
  verbs=['equipped', 'engage', 'embed', 'integrated'], about='climate action and sustainable management', domain='none', award=[FD, HON, MA],
  para='Sustainable management is needed for the planet, and organisations including practices will help meet emission targets; veterinary nurses should be equipped to act on climate challenges in their work, and sustainability management should be built into the curriculum.',
  prac='The curriculum should cover economic, social and environmental sustainability management, and should equip students to take on climate challenges and build climate solutions into veterinary processes.',
  ben='You should leave your course ready to take on climate challenges and to build greener ways of working into everyday veterinary tasks.',
  aaw=aw('an expectation (should) under the sustainability theme, with a student-facing aim', 'all three awards', '1.18',
         'that it sets targets for practices or students', '1.17, 1.19\'s example topics and 4.2.b11'),
  aad=ad('a student asks what sustainability has to do with veterinary nursing', HOW_L,
         'What is one change in a clinic you know that would cut waste or emissions without risking patient care?', AV_L))
s('1.22', type='expectation', rung='none', force='should', level='none', appliesTo='enterprise and entrepreneurship education', addressee='provider',
  verbs=['designed', 'encouraged'], about='enterprise education designed with stakeholders', domain='none', award=[FD, HON, MA],
  para='Employer involvement helps employability; enterprise education should be designed together with employers, professional bodies, service users and other stakeholders, and collaborative student work should be encouraged to build teamwork, negotiation and leadership.',
  prac='Design enterprise and entrepreneurship education with employers, professional bodies and service users, as it should be, and encourage group work that develops teamwork, negotiation and leadership.',
  ben=('n/a', NA_P),
  aaw=aw('a provider duty (should) under the enterprise theme', 'courses at all three awards', '1.22',
         'that it requires any particular enterprise module', '1.20, 1.21, the teamwork rows 4.2.b4 and 4.2.b23, and std:doc:qaa-enterprise-2018-guidance'),
  aad=ad('a team plans employability or enterprise content', HOW_P,
         'Which employers or service users helped shape your enterprise teaching, and what did they change?', AV_P))

AREAS21 = ['communication', 'animal physiology', 'husbandry', 'welfare and behaviour', 'infection control', 'anaesthesia',
           'surgical nursing and theatre practice', 'pharmacology', 'laboratory and diagnostic techniques', 'ethics', 'principles of evidence-based practice']
for _n, _a in enumerate(AREAS21, 1):
    s('2.1.b%d' % _n, type='requirement', rung='none', force='should', level='none', appliesTo='Veterinary Nursing courses', addressee='provider',
      verbs=[], about='minimum content: ' + _a, domain='knowledge', award=[FD, HON, MA],
      para=f'As a minimum, a veterinary nursing course should include the subject area of {_a}.',
      prac=f'Include {_a} in the curriculum; it is one of the subject areas a course should cover at the least.',
      ben=('n/a', 'a minimum of course content set for the course, not an outcome for the student'),
      aaw=aw(f'one of the minimum subject areas a course should include ({_a}), a duty on the course rather than a student outcome', 'every award the statement covers', '2.1',
             'that it sets the depth, hours or level of the topic, or that the list is complete', '3.1, the content areas the course aims to develop, and the outcomes in the four section 4 tables'),
      aad=ad('a programme team checks its curriculum against the minimum content', HOW_P,
             f'Where in your course is {_a} taught and assessed, and at what depth for each award?', AV_P))

s('2.2', type='requirement', rung='none', force='must', level='none', appliesTo='courses seeking RCVS accreditation', addressee='provider',
  verbs=['affords', 'meet'], about='meeting the Day One requirements as a condition of accreditation', domain='none', award=[FD, HON],
  para='Teaching and assessing these subject areas lets graduates meet the RCVS Day One requirements, which a course is required to do to gain RCVS accreditation as a licence to practise and let its graduates apply to the register.',
  prac='For RCVS accreditation, a course is required to give every graduate the chance to meet the Day One Competences, Skills and Professional Behaviours through the subject areas it teaches and assesses.',
  ben=('n/a', 'a condition on the course\'s accreditation; the student-facing point is in 1.7'),
  aaw=aw('a condition of accreditation that the statement reports (required: recorded as must)', 'licence to practise courses', '2.2',
         'that the statement itself accredits courses', '1.7, 2.5 and the RCVS requirements in SB5'),
  aad=ad('a team prepares for RCVS accreditation', HOW_P,
         'Can you map each Day One requirement to where your course teaches and assesses it?', AV_P))
s('2.3', type='expectation', rung='none', force='will', level='none', appliesTo='courses at each award', addressee='provider',
  verbs=['focus', 'incorporate', 'build'], about='the focus of content at each award', domain='none', award=[FD, HON, MA],
  para='Foundation degree courses will concentrate on content that supports the Day One requirements; honours courses will add subjects reflecting the wider clinical role and running a practice as a business; master\'s courses should build further on these specialisms.',
  prac='Pitch content by award: foundation degrees will centre on the Day One requirements, honours degrees will add the wider clinical and business side of practice, and master\'s courses should deepen chosen specialisms.',
  ben=('n/a', NA_P),
  aaw=aw('an expectation on content by award (will for foundation and honours, should for master\'s)', 'each of the three awards in turn', '2.3',
         'that one award\'s content is required at another', '2.1, 3.1 and the three columns of the section 4 tables'),
  aad=ad('a team compares what its foundation, honours and master\'s courses cover', HOW_P,
         'What does your honours course add to the foundation degree, and what does the master\'s build on?', AV_P))
s('2.4', type='expectation', rung='none', force='will', level='none', appliesTo='all Veterinary Nursing courses', addressee='provider',
  verbs=['require', 'cover'], about='extensive practical teaching across the Day One skills', domain='none', award=[FD, HON, MA],
  para='Because the subject is vocational, every course will need extensive practical teaching that covers all the Day One skills.',
  prac='Plan extensive practical teaching: every course will need it to cover the full Day One Skills List.',
  ben=('n/a', NA_P),
  aaw=aw('an expectation (will) on how courses teach', 'courses at all three awards', '2.4',
         'that it fixes any number of hours', '2.5, 3.7 and 3.8'),
  aad=ad('a team plans practical classes and skills sessions', HOW_P,
         'Which Day One skills get the least hands-on practice in your course now?', AV_P))
s('2.5', type='requirement', rung='none', force='must', level='none', appliesTo='licence to practise courses', addressee='provider',
  verbs=['built', 'complete'], about='clinical placement hours in approved training practices', domain='none', award=[FD, HON],
  para='Enough placement time in an approved training practice must be built into any licence to practise course for students to complete the RCVS pre-registration hours before graduating; that time lets them practise and refine the Day One requirements so they will be ready for the role.',
  prac='Build enough clinical placement in approved training practices into the course to let every student complete the RCVS pre-registration hours before graduating, as must be done; use the time to practise and refine the Day One requirements.',
  ben=('n/a', 'a duty on the course; the student meets its effect through placement'),
  aaw=aw('a provider requirement (must) for licence to practise courses', 'foundation and honours licence to practise courses', '2.5',
         'a number of hours; the RCVS sets them', '2.11, 2.12, 1.16 on equal workplace learning and 3.17'),
  aad=ad('a team plans the placement pattern or a student asks why placement is so long', HOW_P,
         'Does your placement plan let every student finish the required hours before the exam board?', AV_P))
s('2.6', type='outcome', rung='none', force='will', level='fheq:7', appliesTo="holders of a master's degree in Veterinary Nursing",
  addressee='learner', verbs=['progress', 'contribute', 'develop', 'demonstrate'], about='progression and the master\'s contribution to the profession', domain='subject-skill', award=MA,
  para='Students progress level by level towards the threshold standards; a second-class honours graduate would be expected to be ready for postgraduate study; postgraduate students will be expected to advance the profession through innovation, and master\'s holders will build the knowledge base and show excellence in research and practice.',
  prac='Plan progression so each level builds towards the threshold; at master\'s level graduates will add to the knowledge base and show excellence in research and practice, advancing the profession within legal and professional limits.',
  ben='If you take a master\'s in veterinary nursing, you will add to what the profession knows and show excellence in both research and practice.',
  aaw=aw('an expected outcome (will) for master\'s holders, inside a paragraph on progression', "the master's degree (FHEQ level 7, SCQF level 11)", '2.6',
         'that a second-class degree guarantees entry to postgraduate study; entry is for each provider', "the master's column of the tables, 3.18 and qaa/fheq-2024/4.17.b3 and 4.17.b7 (spine:7)"),
  aad=ad('a student weighs up a master\'s or asks what it adds', HOW_L,
         'What question from your practice would you most like to research, and how would it change care?', AV_L))
s('2.8', type='expectation', rung='none', force='should', level='none', appliesTo='higher education providers', addressee='provider',
  verbs=['work', 'ensure'], about='partnership with the RCVS on accreditation', domain='none', award=[FD, HON, MA],
  para='Providers should work with the RCVS so that accreditation and quality requirements are met and completing students can register as veterinary nurses or with the advanced certificate.',
  prac='Work in partnership with the RCVS, as the provider should, so that accreditation and quality assurance requirements are met and completing students are eligible to register.',
  ben=('n/a', NA_P),
  aaw=aw('a provider duty (should)', 'courses at all three awards', '2.8', 'that the statement sets RCVS requirements', '2.2, 2.9 and SB5'),
  aad=ad('a team plans its accreditation relationship', HOW_P, 'Who in your team owns the RCVS relationship, and how often do you meet?', AV_P))
s('2.9', type='expectation', rung='none', force='describes', level='none', appliesTo='providers working with further education colleges', addressee='provider',
  verbs=['operate', 'develop', 'ensure'], about='oversight of partner colleges', domain='none', award=[FD, HON, MA],
  para='Providers may partner with further education colleges, widening access; they are expected to set up oversight so that partners meet all academic and RCVS standards.',
  prac='Where you deliver with further education colleges, set up oversight processes, as the statement expects, so that partners meet every academic and RCVS standard.',
  ben=('n/a', NA_P),
  aaw=aw('an expectation on providers stated as "are expected to", outside the five modal words (recorded as describes)', 'courses delivered in partnership', '2.9',
         'that it is a must or a should', '2.8, 2.11 and 2.12'),
  aad=ad('a team delivers through a partner college', HOW_P, 'How do you check that your partner college meets the same RCVS standards you do?', AV_P))
s('2.10', type='expectation', rung='none', force='should', level='none', appliesTo='students and their course teams', addressee='both',
  verbs=['work', 'play'], about='students as partners; the student voice', domain='none', award=[FD, HON, MA],
  para='Students should work in partnership with their provider and course team, and their voice should count for much in course development, delivery, review and experience.',
  prac='Treat students as partners: they should work with the course team, and their views should carry real weight in developing, delivering and reviewing the course.',
  ben='You should work with your course team as a partner, and your views should help shape how the course is built, taught and reviewed.',
  aaw=aw('an expectation (should) on students and course teams', 'all three awards', '2.10', 'that students carry responsibility for course quality', '2.13 and 1.12'),
  aad=ad('a student asks how they can influence their course', HOW_L, 'What is one thing about your course you would change, and who could you raise it with?', AV_L))
s('2.11', type='expectation', rung='none', force='should', level='none', appliesTo='course providers, placement providers, supervisors and students', addressee='provider',
  verbs=['work', 'complete'], about='written placement agreements', domain='none', award=[FD, HON],
  para='Course providers partner with placement providers for access to clinical cases and practice settings, needed for the Day One requirements and placement hours; there should be a written collaborative agreement among supervisors, course and placement providers and students.',
  prac='Put in place a written collaborative agreement, as there should be, between clinical supervisors, the course, placement providers and students, so that placements give the access to cases the Day One requirements need.',
  ben=('n/a', NA_P),
  aaw=aw('a provider duty (should); the first sentence is a plain-present norm', 'licence to practise courses', '2.11', 'that the statement sets the content of the agreement', '2.5, 2.12 and 1.16'),
  aad=ad('a team sets up or reviews placement agreements', HOW_P, 'Does every student on placement have a signed agreement that names their supervisor\'s role?', AV_P))
s('2.12', type='expectation', rung='none', force='should', level='none', appliesTo='course providers', addressee='provider',
  verbs=['undertaken', 'ensure'], about='approving training practices and training supervisors', domain='none', award=[FD, HON],
  para='Course providers should approve and monitor training practices and auxiliary training practices so that clinical learning settings are and stay fit for purpose, and should ensure clinical supervisors are trained and standardised.',
  prac='Approve and monitor training practices, as the course provider should, so placements stay suitable, and train and standardise clinical supervisors.',
  ben=('n/a', NA_P),
  aaw=aw('a provider duty (should)', 'licence to practise courses', '2.12', 'that it replaces RCVS approval rules', '2.5, 2.11 and 3.17'),
  aad=ad('a team reviews placement quality', HOW_P, 'When did you last check a training practice, and how are new supervisors prepared?', AV_P))
s('2.14', type='expectation', rung='none', force='will', level='none', appliesTo='providers in periodic review', addressee='provider',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award=[FD, HON, MA],
  para='Externality is central to UK quality assurance; providers will use external reviewers in periodic review to gain an outside view of changes and to make sure threshold standards are reached and content suits the subject.',
  prac='Use external reviewers in periodic review, as providers will, for an outside view of planned changes and to confirm that threshold standards are met and content is right for the subject.',
  ben=('n/a', NA_P),
  aaw=aw('a provider expectation (will) about review', 'courses at all three awards', '2.14', 'that it sets a review cycle', '2.13, 2.15 and 4.1'),
  aad=ad('a team prepares for periodic review', HOW_P, 'Who will act as your external reviewer, and which proposed change do you most want them to test?', AV_P))
s('3.3', type='outcome', rung='none', force='describes', level='none', appliesTo='holders of degrees in small animal Veterinary Nursing',
  addressee='learner', verbs=['delivering'], about='nursing cats, dogs and exotic species', domain='subject-skill', award=[FD, HON],
  para='Holders of small animal veterinary nursing degrees are expected (the issuer says anticipated) to be proficient in nursing a range of species, including cats, dogs and exotics.',
  prac='Prepare small animal graduates to nurse cats, dogs and exotic species proficiently, which the statement anticipates of them.',
  ben='On a small animal course you are expected to become skilled at nursing cats, dogs and exotic species.',
  aaw=aw('an expected outcome stated as "anticipated", outside the five modal words (recorded as describes)', 'small animal veterinary nursing degrees', '3.3',
         'that it is a must, or that the species list is complete', '3.4, 3.1 and 3.7'),
  aad=ad('a student asks which species their course covers', HOW_L, 'Which species do you feel least confident nursing, and how could you get more practice?', AV_L))
s('3.4', type='outcome', rung='none', force='describes', level='none', appliesTo='holders of degrees in equine Veterinary Nursing',
  addressee='learner', verbs=['delivering'], about='nursing horses', domain='subject-skill', award=[FD, HON],
  para='Holders of equine veterinary nursing degrees are expected (anticipated) to be proficient in nursing horses.',
  prac='Prepare equine graduates to nurse horses proficiently, which the statement anticipates of them.',
  ben='On an equine course you are expected to become skilled at nursing horses.',
  aaw=aw('an expected outcome stated as "anticipated" (recorded as describes)', 'equine veterinary nursing degrees', '3.4', 'that it is a must', '3.3 and 3.7'),
  aad=ad('a student on an equine route asks what is expected of them', HOW_L, 'Which equine nursing tasks have you done on placement so far?', AV_L))

L310 = dict(type='outcome', rung='none', force='should', level='fheq:5', appliesTo='students of the subject', addressee='learner', award=[FD, HON])
def k310(i, **k):
    s('3.10.b%d' % i, **L310, **k)
k310(1, verbs=['work', 'deliver', 'maintain'], about='multidisciplinary teamwork and professional relationships', domain='generic-skill',
     para='Should be able to work in a multidisciplinary team to care for patients and clients, which calls for excellent communication and steady professional relationships with clients, colleagues, the public and others, even under emotional and financial strain.',
     prac='Students should develop the ability to work in multidisciplinary teams, with strong communication and professional relationships that hold up under emotional and economic pressure.',
     ben='You should become able to work in a team of different professionals, communicate very well and keep professional relationships with clients, colleagues and the public, even when things are emotionally or financially tense.',
     aaw=aw('an outcome students should develop (should)', 'foundation and honours study', '3.10',
            'that it is a separate threshold from the tables', '4.2.b4, 4.2.b23 and 4.2.b27 and qaa/fheq-2024/4.12.b6 (spine:5, strand:communication)'),
     aad=ad('a student reflects on teamwork or a hard client conversation', HOW_L, 'When did you last keep a conversation professional under pressure, and what helped?', AV_L))
k310(2, verbs=['respond', 'recognising', 'utilising'], about='ethical judgement and legislation', domain='subject-skill',
     para='Should be able to respond fittingly to situations that call for an ethical and moral stance, seeing the risks and using relevant law where needed.',
     prac='Students should develop the ability to respond to ethical situations appropriately, recognising risk and applying the relevant legislation.',
     ben='You should become able to handle situations that need an ethical stance, seeing the risks and using the relevant law when you need to.',
     aaw=aw('an outcome students should develop (should)', 'foundation and honours study', '3.10', 'that it is a legal competence', '4.2.b24 and 4.2.b36 (spine:5, strand:thinking)'),
     aad=ad('a student meets an ethical dilemma in practice', HOW_L, 'What made that situation an ethical one, and which law or rule applied?', AV_L))
k310(3, verbs=['act', 'maintaining'], about='advocacy with confidentiality', domain='subject-skill',
     para='Should be able to speak up for patients and clients while always keeping confidentiality.',
     prac='Students should develop the ability to advocate for patients and clients while always keeping matters confidential.',
     ben='You should become able to speak up for patients and clients while always keeping their information confidential.',
     aaw=aw('an outcome students should develop (should)', 'foundation and honours study', '3.10', 'that advocacy overrides confidentiality', '4.2.b6 and 4.2.b41 (spine:5)'),
     aad=ad('a student asks how to advocate for an animal when the owner disagrees', HOW_L, 'How would you speak up for this patient without sharing anything you should not?', AV_L))
k310(4, verbs=['use', 'inform', 'take'], about='evidence-informed decisions and responsibility', domain='generic-skill',
     para='Should be able to use research and current data in decisions and take personal responsibility for what they do.',
     prac='Students should develop the ability to base decisions on research and current data and to own their actions.',
     ben='You should become able to base your decisions on research and up-to-date data and take responsibility for what you do.',
     aaw=aw('an outcome students should develop (should)', 'foundation and honours study', '3.10', 'that it is a research competence', '4.2.b17 and 4.2.b37 and qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)'),
     aad=ad('a student explains a clinical decision', HOW_L, 'What evidence did you use for that decision, and would you make it again?', AV_L))
k310(5, verbs=['maintain', 'identify'], about='reflective practice', domain='generic-skill',
     para='Should be able to keep reflecting on their professional practice to find what to improve and develop.',
     prac='Students should develop the ability to reflect on their practice to identify areas for improvement.',
     ben='You should become able to keep reflecting on your own practice to see what to improve next.',
     aaw=aw('an outcome students should develop (should)', 'foundation and honours study', '3.10', 'that a single reflective log meets it', '4.2.b12, 4.2.b31 and 4.2.b44 (spine:5, strand:autonomy)'),
     aad=ad('a student writes a reflection or plans development', HOW_L, 'What is one thing you would do differently after your last shift, and why?', AV_L))

s('3.13', type='expectation', rung='none', force='should', level='none', appliesTo='teaching and learning', addressee='both',
  verbs=['enable', 'acquire', 'develop'], about='skills teaching and the research project', domain='none', award=[FD, HON],
  para='Teaching and learning should let students gain skills in communication, information technology, teamwork, problem-solving and evidence-based practice; where fitting, students will have the chance to build research method skills, and honours courses typically include a short research project or dissertation.',
  prac='Teaching should give students communication, IT, teamwork, problem-solving and evidence-based practice skills; where suitable, students will be able to develop research method skills, often through an honours project.',
  ben='Your course should help you build skills in communication, IT, teamwork, problem-solving and using evidence, and where it fits you will get the chance to learn research methods.',
  aaw=aw('an expectation (should) on teaching, with a will on research opportunity', 'foundation and honours study', '3.13',
         'that every course must include a dissertation; the statement says typically', 'the generic skills table (4.2.b1 to 4.2.b13) and 4.2.b42'),
  aad=ad('a student asks what skills the course builds beyond clinical ones', HOW_L, 'Which of these skills do you use most on placement, and which least?', AV_L))
s('3.14', type='expectation', rung='none', force='should', level='none', appliesTo='assessment strategies', addressee='provider',
  verbs=['ensure', 'discriminate', 'help'], about='aligned assessment that separates threshold from higher achievement', domain='none', award=[FD, HON, MA],
  para='Assessment strategies should align outcomes, teaching and competencies and should tell threshold achievement apart from higher; varied assessment may be used, and methods should prepare students for their first day in practice.',
  prac='Align assessment with outcomes, teaching and competencies, as it should be, and make it discriminate between threshold and higher achievement; methods should prepare students for day one in practice.',
  ben=('n/a', NA_P),
  aaw=aw('a provider duty (should) on assessment', 'courses at all three awards', '3.14', 'that the statement defines grades above threshold; it points to Annex D (4.2)', '3.15, 4.1, 4.2 and qaa/fheq-2024 Annex D (SL6)'),
  aad=ad('a team designs an assessment strategy', HOW_P, 'How does this assessment tell a threshold performance apart from a strong one?', AV_P))
s('3.15', type='expectation', rung='none', force='should', level='none', appliesTo='assessment and course teams', addressee='provider',
  verbs=['progressive', 'diversify', 'permit'], about='progressive, varied, authentic and inclusive assessment', domain='none', award=[FD, HON, MA],
  para='Assessment should progress in level and content and give useful feedback, building transferable skills including critical digital literacy; course teams should vary methods so students of every background can show their learning, make assessment authentic where possible, and allow reasonable adjustments while students still show every competence a registered nurse needs.',
  prac='Make assessment progressive with useful feedback; vary methods so all students can show what they have learned; make tasks authentic where possible; and allow reasonable adjustments, as assessment should, without lowering the competences a registered nurse needs.',
  ben=('n/a', NA_P),
  aaw=aw('a provider duty (should) on assessment', 'courses at all three awards', '3.15', 'that adjustments may waive a competence', '1.14, 1.15, 3.14 and 4.2.b5'),
  aad=ad('a team reviews feedback, variety or adjustments in assessment', HOW_P, 'Could a student with an adjustment still show every competence through this task?', AV_P))
s('3.18', type='expectation', rung='none', force='should', level='fheq:7', appliesTo='postgraduate courses', addressee='provider',
  verbs=['apply', 'requiring'], about='applied evidence and research skills at postgraduate level', domain='none', award=MA,
  para='At postgraduate level there should be strong weight on requiring students to apply evidence-based subject knowledge to decisions and to complex, unfamiliar problems; assessing research skills is held crucial in judging whether postgraduate outcomes are met.',
  prac='At postgraduate level, teaching and assessment should stress applying evidence-based knowledge to complex, unfamiliar problems and should assess research skills.',
  ben=('n/a', NA_P),
  aaw=aw('a provider expectation (should) on postgraduate assessment', "postgraduate study, including the master's (FHEQ level 7)", '3.18',
         'that it applies to foundation or honours courses', "2.6, the master's column of the tables and qaa/fheq-2024/4.17.b5 (spine:7)"),
  aad=ad('a postgraduate team designs assessment', HOW_P, 'Where do your students meet a complex, unfamiliar case, and how are their research skills assessed?', AV_P))
s('4.2', find=_exact("4.2 The vast majority of students who graduate with a bachelor's degree with honours will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies . This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd."),
  type='expectation', rung='none', force='should', level='fheq:6', appliesTo='higher education providers', addressee='provider',
  verbs=['refer'], about='judging achievement above threshold with Annex D', domain='none', award=HON,
  para='Most honours graduates will do much better than the threshold; each provider decides how to evidence this and should refer to Annex D of the qualifications frameworks, which describes the four honours classifications.',
  prac='When judging achievement above threshold for honours, use your own method and refer to Annex D of the Frameworks, as you should, for the shared descriptions of the four classes.',
  ben=('n/a', NA_P),
  aaw=aw('a provider expectation (should) pointing to a shared document', 'the honours degree (FHEQ level 6, SCQF level 10)', '4.2',
         'that the statement defines classification bands itself', 'std:doc:qaa-fheq-2024-framework Annex D (qaa/fheq-2024/annex-d/..., SL6) and 3.14'),
  aad=ad('a team sets classification criteria', HOW_P, 'How do your marking criteria line up with the Annex D descriptions of each class?', AV_P))

# ------------------------------------------------------------------ section 4: four tables, one row per outcome, three award columns
# Each cell is a threshold standard (4.1: the minimum for the award), lead-in "Graduates should be able to:".
AW = {
    'foundation': dict(award=FD, level='fheq:5', lvl='FHEQ level 5', short='foundation degree', col='Foundation degree (FHEQ Level 5)', spine='spine:5', who='a foundation degree student or tutor'),
    'honours': dict(award=HON, level='fheq:6', lvl='FHEQ level 6, SCQF level 10', short='honours degree', col="Bachelor's degree with honours (FHEQ Level 6 / SCQF Level 10)", spine='spine:6', who='an honours student or tutor'),
    'masters': dict(award=MA, level='fheq:7', lvl='FHEQ level 7, SCQF level 11', short="master's degree", col="Master's degree (FHEQ Level 7)", spine='spine:7', who="a master's student or tutor"),
}
DESC = {  # framework descriptor items by strand and award level (std:doc:qaa-fheq-2024-framework; FQHEIS 4.16 for SCQF 10)
    'knowledge':     {'foundation': 'qaa/fheq-2024/4.12.b1', 'honours': 'qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1', 'masters': 'qaa/fheq-2024/4.17.b1'},
    'thinking':      {'foundation': 'qaa/fheq-2024/4.12.b5', 'honours': 'qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b6', 'masters': 'qaa/fheq-2024/4.17.b5'},
    'application':   {'foundation': 'qaa/fheq-2024/4.12.b2', 'honours': 'qaa/fheq-2024/4.15.b6 and qaa/fqheis-2024/4.16.b4', 'masters': 'qaa/fheq-2024/4.17.b3'},
    'communication': {'foundation': 'qaa/fheq-2024/4.12.b6', 'honours': 'qaa/fheq-2024/4.15.b8 and qaa/fqheis-2024/4.16.b7', 'masters': 'qaa/fheq-2024/4.17.b5'},
    'autonomy':      {'foundation': 'qaa/fheq-2024/4.12.b8', 'honours': 'qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2', 'masters': 'qaa/fheq-2024/4.17.b8.2'},
    'research':      {'foundation': 'qaa/fheq-2024/4.12.b3', 'honours': 'qaa/fheq-2024/4.15.b3.2 and qaa/fqheis-2024/4.16.b5', 'masters': 'qaa/fheq-2024/4.17.b4.1'},
}
STRAND_ID = {'knowledge': 'strand:knowledge', 'thinking': 'strand:thinking', 'application': 'strand:application',
             'communication': 'strand:communication', 'autonomy': 'strand:autonomy', 'research': 'strand:application'}

def _fmt(x, you):
    return x.replace('{p}', 'your' if you else 'their').replace('{s}', 'yourself' if you else 'themselves')

_cursor = _norm.find('Generic skills Graduates should be able to:')
def _locate(text):
    """Find a cell's text from the cursor on; spaces match any whitespace, straight quotes match curly ones."""
    global _cursor
    pat = _re.escape(text).replace("'", "['’]").replace('\\ ', r'\s+')
    m = _re.compile(pat).search(_norm, _cursor)
    if not m:
        raise SystemExit('cell not found after %d: %s' % (_cursor, text[:60]))
    _cursor = m.end()
    return m.group(0), m.start()

TABLES = []   # (table name, first row number, last row number)
OUTCOMES = []
_row = 0
def table(name):
    TABLES.append([name, _row + 1, _row])

def row(topic, domain, strand, q, cells):
    """cells: three (issuer's text, our infinitive phrase, verbs) for foundation, honours, master's, in column order."""
    global _row
    _row += 1
    TABLES[-1][2] = _row
    base = '4.2.b%d' % _row
    ids = {'foundation': base + '.foundation', 'honours': base, 'masters': base + '.masters'}
    for (col, (text, x, verbs)) in zip(('foundation', 'honours', 'masters'), cells):
        a = AW[col]
        found, at = _locate(text)
        others = ', '.join(ids[c] for c in ('foundation', 'honours', 'masters') if c != col)
        P[ids[col]] = dict(
            find=found, after=at, forceFrom='4.1',
            type='threshold', rung='threshold', force='threshold', level=a['level'],
            appliesTo='%s graduates (section 4 table: %s)' % (a['short'], TABLES[-1][0]),
            addressee='learner', verbs=verbs, about='%s (%s)' % (topic, a['short']), domain=domain, award=a['award'],
            para='Graduates of a %s should be able to %s, as the minimum for the award.' % (a['short'], _fmt(x, False)),
            prac='The minimum for a %s (%s): teach and assess so that every graduate should be able to %s.' % (a['short'], a['lvl'], _fmt(x, False)),
            ben='As the minimum for your %s, you should be able to %s.' % (a['short'], _fmt(x, True)),
            aaw=('Treat this as a threshold standard: the minimum a %s in veterinary nursing asks at %s, on %s. '
                 'Cite it as %s, section 4, table "%s", %s column. '
                 'Do not present it as an RCVS or regulatory requirement, or as holding for another award. '
                 'Set it beside the same row\'s other columns (%s) and the framework descriptor %s (%s, %s).'
                 % (a['short'], a['lvl'], topic, CITE, TABLES[-1][0], a['short'], others, DESC[strand][col], a['spine'], STRAND_ID[strand])),
            aad=('Raise it when %s asks what %s should look like by the end of the %s. '
                 'Put it plainly: to a student, that by the end you should be able to %s; to staff, as where the course teaches and assesses it. '
                 'Ask: "%s" '
                 'Avoid reading the table aloud and holding anyone to another award\'s column as if it were their minimum.'
                 % (a['who'], topic, a['short'], _fmt(x, True), q)))
    OUTCOMES.append(dict(outcome=topic, threshold=ids['honours'], typical='none', excellent='none',
                         foundation=SID + '/' + ids['foundation'], masters=SID + '/' + ids['masters'],
                         basis='stated: one table row, columns placed by reading the flattened row', domain=domain, award=[FD, HON, MA]))

T1, T2, T3, T4 = ('Generic skills', 'Principles and concepts: application',
                  'Subject knowledge, understanding and associated skills', 'Working as a professional veterinary nurse: expectations')

table(T1)
row('arguing a case for the patient', 'generic-skill', 'communication', 'When did you last make the case for a patient to a vet or colleague, and how did it go?', [
    ('Articulate opinions and formulate arguments effectively both verbally and in writing',
     'put forward views and build sound arguments, in speech and on paper', ['articulate', 'formulate']),
    ("Articulate opinions and formulate arguments effectively both verbally and in writing to provide compelling debate with other professionals as the patient's advocate",
     "put forward views and build arguments in speech and writing strong enough to carry a debate with other professionals on the patient's behalf", ['articulate', 'formulate', 'provide']),
    ("Debate effectively both verbally and in writing as the patient's advocate with other professionals",
     'hold {p} own in spoken and written debate with fellow professionals, speaking up for the patient', ['debate'])])
row('independent learning and problem-solving', 'generic-skill', 'autonomy', 'What did you last learn on your own, and how did you tackle the problem it helped with?', [
    ('Learn independently and utilise problem-solving skills', 'study on {p} own and use problem-solving skills', ['learn', 'utilise']),
    ('Learn independently and demonstrate an analytical approach to problem-solving', 'study on {p} own and show an analytical way of solving problems', ['learn', 'demonstrate']),
    ('Learn independently and implement an analytical approach to problem-solving', 'study on {p} own and put an analytical way of solving problems into action', ['learn', 'implement'])])
row('evidence-based practice', 'generic-skill', 'thinking', 'Which piece of evidence has most changed how you nurse, and how did you judge it?', [
    ('Demonstrate the principles of evidence- based practice', 'show what evidence-based practice rests on', ['demonstrate']),
    ('Apply the concept of evidence-based practice in the clinical environment. Critically evaluate arguments, assumptions, abstract concepts and data',
     'use evidence-based practice in the clinic and weigh up arguments, assumptions, abstract ideas and data critically', ['apply', 'evaluate']),
    ('Create and critique evidence to establish best practice in the clinical environment',
     'generate and critique evidence that sets the best clinical practice', ['create', 'critique'])])
row('teamwork', 'generic-skill', 'autonomy', 'What part did you play in your team this week, and what would you take on next?', [
    ('Collaborate and contribute to the work of the team', 'work with others and play a part in what the team does', ['collaborate', 'contribute']),
    ('Contribute proactively to the aims and organisation of a team', "take an active part in setting a team's goals and organising it", ['contribute']),
    ('Lead the development of the aims and organisation of a team', "lead the shaping of a team's goals and how it is organised", ['lead'])])
row('digital skills', 'generic-skill', 'communication', 'Which digital tool do you rely on most, and how do you keep data use within the law?', [
    ('Use digital skills competently and effectively to include information gathering in line with legal and ethical requirements',
     'use digital tools capably, including to find information, within legal and ethical limits', ['use']),
    ('Use digital skills to enhance presentations and to facilitate data analysis in line with legal and ethical requirements',
     'use digital tools to strengthen presentations and support data analysis, within legal and ethical limits', ['use']),
    ('Create digitally enhanced presentations and use digital skills to facilitate data analysis in line with legal and ethical requirements',
     'produce digitally enriched presentations and analyse data with digital tools, within legal and ethical limits', ['create', 'use'])])
row('confidential information', 'generic-skill', 'autonomy', 'What would you do if a colleague shared a client\'s details where they should not?', [
    ('Demonstrate management of confidential information in an appropriate manner', 'handle confidential information properly', ['demonstrate']),
    ('Demonstrate management of confidential information in line with legal requirements, guiding colleagues where necessary',
     'handle confidential information as the law requires and guide colleagues when needed', ['demonstrate']),
    ('Manage confidential information in line with legal requirements, supporting colleagues in maintaining this ethos',
     'manage confidential information as the law requires and help colleagues keep to that standard', ['manage'])])
row('self-awareness and confidence in the clinic', 'generic-skill', 'autonomy', 'Where in the clinic do you feel most and least sure of yourself, and why?', [
    ('Demonstrate self-awareness and self-confidence in the clinical environment', 'show self-awareness and self-assurance in clinical settings', ['demonstrate']),
    ('Demonstrate self-awareness and self- confidence in the clinical environment', 'show self-awareness and self-assurance in clinical settings', ['demonstrate']),
    ('Demonstrate self-awareness and self- confidence in the clinical environment', 'show self-awareness and self-assurance in clinical settings', ['demonstrate'])])
_X8 = 'know about and promote respect for the variety of cultures, values, outlooks and beliefs, and model the behaviours that anti-discriminatory practice depends on'
_T8 = 'Demonstrate knowledge of, and advocate respect for, diverse cultures, values, views and beliefs. Role model behaviours that underpin anti-discriminatory practices'
row('respect for diversity and anti-discriminatory behaviour', 'generic-skill', 'autonomy', 'How do you show respect for a client whose views on animal care differ from yours?', [
    (_T8, _X8, ['demonstrate', 'advocate']), (_T8, _X8, ['demonstrate', 'advocate']), (_T8, _X8, ['demonstrate', 'advocate'])])
row('barriers for people with protected characteristics', 'generic-skill', 'thinking', 'What barrier might a disabled client or colleague face in your clinic, and what could change?', [
    ('Recognise barriers for those with protected characteristics and understand how to minimise these',
     'spot the barriers facing people with protected characteristics and know how to reduce them', ['recognise', 'understand', 'minimise']),
    ('Analyse and take action to address any identified barriers to those with protected characteristics',
     'analyse barriers found for people with protected characteristics and act to remove them', ['analyse', 'take', 'address']),
    ('Evaluate potential barriers to those with protected characteristics and identify appropriate actions',
     'evaluate possible barriers for people with protected characteristics and decide on fitting actions', ['evaluate', 'identify'])])
_X10 = 'stay non-judgemental in all {p} work and avoid stigmatising any group of clients, team members or the public'
_T10 = 'Maintain a non-judgmental position in all aspects of work and avoid stigmatising any category of veterinary client, members of the team or the public'
row('non-judgemental practice', 'generic-skill', 'autonomy', 'Can you recall a moment when you caught yourself judging a client, and what you did next?', [
    (_T10, _X10, ['maintain', 'avoid']), (_T10, _X10, ['maintain', 'avoid']), (_T10, _X10, ['maintain', 'avoid'])])
row('sustainable practice', 'generic-skill', 'application', 'What is one practice in your clinic you could make more sustainable without harming care?', [
    ('Adopt a sustainable approach to all aspects of Veterinary Nursing practice', 'take a sustainable approach across every part of veterinary nursing work', ['adopt']),
    ('Develop a sustainable approach to all aspects of Veterinary Nursing practice', 'build a sustainable approach across every part of veterinary nursing work', ['develop']),
    ('Innovate and develop a sustainable approach to all aspects of Veterinary Nursing practice', 'innovate and build a sustainable approach across every part of veterinary nursing work', ['innovate', 'develop'])])
row('reflective practice', 'generic-skill', 'autonomy', 'What did your last reflection change in how you or your team work?', [
    ('Adopt a reflective approach to professional practice, including the identification of opportunities to improve individual and team- working practices',
     'reflect on professional practice and find chances to improve both individual and team working', ['adopt']),
    ('Adopt a reflective approach to professional practice in both self and others within the team, including improvement of patient care practices and the management of the clinical environment',
     "reflect on professional practice, {p} own and that of team members, to improve patient care and how the clinical setting is run", ['adopt']),
    ('Lead a reflective approach to professional practice in both self and others within the team, including improvement of patient care practices and the management of the clinical environment',
     "lead reflection on professional practice, {p} own and the team's, to improve patient care and how the clinical setting is run", ['lead'])])
row('well-being and fitness to practise', 'generic-skill', 'autonomy', 'How do you notice when you or a colleague needs more support, and who would you turn to?', [
    ('Adopt well-being practices to maintain fitness to practise, recognising where additional support is required',
     'use well-being habits to stay fit to practise, knowing when to seek more support', ['adopt', 'recognising']),
    ('Adopt well-being practices to maintain fitness to practise in self and others, recognising where additional support is required',
     'use well-being habits to keep {s} and others fit to practise, knowing when more support is needed', ['adopt', 'recognising']),
    ('Adopt well-being practices to maintain fitness to practise in self and others, recognising where additional support is required',
     'use well-being habits to keep {s} and others fit to practise, knowing when more support is needed', ['adopt', 'recognising'])])

table(T2)
row('theory in holistic care', 'subject-skill', 'application', 'Which theory or model shaped the last care plan you wrote, and why that one?', [
    ('Select and apply theories, concepts and principles to deliver holistic veterinary healthcare',
     'choose and use theories, concepts and principles to give holistic veterinary care', ['select', 'apply']),
    ('Select and apply theories, concepts and principles, evaluating the most appropriate frameworks to deliver holistic veterinary healthcare',
     'choose and use theories, concepts and principles, judging which frameworks best support holistic veterinary care', ['select', 'apply', 'evaluating']),
    ('Select and apply advanced theories, concepts and principles that incorporate other relevant disciplines in providing holistic care in complex and unpredictable situations',
     'choose and use advanced theory, drawing on other relevant disciplines, to give holistic care in complex, unpredictable situations', ['select', 'apply', 'incorporate'])])
row('managing clinical risk', 'subject-skill', 'thinking', 'What risk did you spot early on a recent case, and what did you do about it?', [
    ('Recognise potential risk and appropriate interventions to prevent complications occurring, where possible',
     'recognise possible risks and the interventions that can head off complications', ['recognise', 'prevent']),
    ('Recognise potential risk, appropriate interventions, and the need to develop protocols to minimise risk while providing quality veterinary healthcare',
     'recognise possible risks, suitable interventions and the need for protocols that reduce risk in good-quality care', ['recognise', 'develop', 'minimise']),
    ('Critically evaluate and enhance current protocols of the management of risk in the veterinary practice, while informing strategic level and direction',
     "critically evaluate and improve a practice's risk-management protocols while shaping its strategy and direction", ['evaluate', 'enhance', 'informing'])])
row('promoting animal health and welfare', 'subject-skill', 'application', 'What health message do owners most need from you, and how do you know it works?', [
    ('Analyse and interpret relevant educational/promotional information and use this knowledge to promote animal health and welfare',
     'analyse and interpret educational and promotional material and draw on it to advance the health and welfare of animals', ['analyse', 'interpret', 'use', 'promote']),
    ('Critically analyse contemporary issues in animal health and welfare', 'critically analyse current issues in the health and welfare of animals', ['analyse']),
    ('Develop innovative strategies to promote animal health and welfare in line with evidenced-based practice',
     'devise new strategies, grounded in evidence-based practice, to advance the health and welfare of animals', ['develop', 'promote'])])
row('evidence behind clinical decisions', 'subject-skill', 'thinking', 'Talk me through a decision you made with only part of the information: what did you weigh?', [
    ('Use appropriate research and suitable evidence to underpin and justify clinical decisions',
     'draw on suitable research and evidence to support and justify clinical decisions', ['use', 'underpin', 'justify']),
    ('Articulate and justify decision-making and problem-solving processes associated with Veterinary Nursing practice even where there is incomplete data',
     'explain and justify the decisions and problem-solving behind veterinary nursing practice, even when the data are incomplete', ['articulate', 'justify']),
    ('Systematically synthesise advanced and specialist information to develop innovative proposals to address complex patient care',
     'bring advanced, specialist information together systematically to propose new ways of meeting complex patient care needs', ['synthesise', 'develop', 'address'])])
row('nursing assessment', 'subject-skill', 'application', 'What did your last nursing assessment miss at first, and how did you find it?', [
    ('Undertake and document a systematic nursing assessment considering the needs of the patient and, where applicable, their owner',
     "carry out and record a systematic nursing assessment that takes account of the patient's needs and, where relevant, the owner's", ['undertake', 'document']),
    ('Use relevant theoretical and research evidence to undertake and document a comprehensive, systematic nursing assessment considering the needs of the patient and, where applicable, their owner',
     "use theory and research to carry out and record a full, systematic nursing assessment that takes account of the patient's needs and, where relevant, the owner's", ['use', 'undertake', 'document']),
    ('Develop a systematic and evidence-based framework to assess the needs of the patient and owner (regardless of their cultural and socioeconomic background)',
     'build a systematic, evidence-based framework for assessing what patient and owner need, whatever their cultural or socioeconomic background', ['develop', 'assess'])])
row('priorities and care delivery', 'subject-skill', 'autonomy', 'On a busy shift, how do you decide what comes first, and who do you tell?', [
    ('Assess priorities in nursing practice and deliver care competently to meet identified needs',
     'judge nursing priorities and give competent care that meets the needs found', ['assess', 'deliver']),
    ('Evaluate evolving priorities within a complex and changing environment and communicate appropriately',
     'evaluate shifting priorities in a complex, changing setting and communicate suitably', ['evaluate', 'communicate']),
    ('Facilitate team development, demonstrating leadership skills to ensure the team delivers the care required',
     'develop the team and show leadership so that the team gives the care needed', ['facilitate', 'demonstrating', 'delivers'])])
row('care planning and research', 'subject-skill', 'research', 'Which research finding would you use to change a care plan, and how would you check it worked?', [
    ('Formulate and document a plan of care with the collaboration of the veterinary team and consent of clients in the best interest of the patient',
     "draw up and record a care plan with the veterinary team and the client's consent, in the patient's best interest", ['formulate', 'document']),
    ('Critically evaluate research findings and use these to inform changes to planned care',
     'critically evaluate research findings and use them to change planned care', ['evaluate', 'use', 'inform']),
    ('Create research and contribute and add to the evidence base', 'produce research that adds to the evidence base', ['create', 'contribute', 'add'])])
row('accountability and the context of care', 'subject-skill', 'autonomy', 'Which outside factor, such as cost or culture, most shaped care you gave recently?', [
    ('Demonstrate accountability for veterinary healthcare delivered, considering social, cultural, spiritual, legal, political, economic and welfare factors',
     'show accountability for the care given, weighing the social, cultural, spiritual, legal, political and economic factors and animal welfare', ['demonstrate']),
    ('Demonstrate an ability to critically challenge the veterinary healthcare delivered, considering dynamic social, cultural, spiritual, legal, political, economic and welfare factors',
     'challenge critically the care delivered, weighing the shifting social, cultural, spiritual, legal, political and economic factors and animal welfare', ['demonstrate', 'challenge']),
    ('Act autonomously to make strategic decisions and develop appropriate practice guidelines, taking responsibility for outcomes in abstract and unpredictably complex contexts',
     'act autonomously in making strategic decisions and setting practice guidelines, owning the results in abstract, highly complex and unpredictable settings', ['act', 'make', 'develop', 'taking'])])
row('outcomes of interventions', 'subject-skill', 'thinking', 'How did you know whether your last intervention worked, and what did you change?', [
    ('Accurately document and evaluate the outcomes of professional interventions', 'record accurately and evaluate the results of professional interventions', ['document', 'evaluate']),
    ('Critically evaluate outcomes of professional interventions, adjusting Veterinary Nursing care accordingly',
     'critically evaluate the results of professional interventions and adjust nursing care to match', ['evaluate', 'adjusting']),
    ('Use outcomes of interventions to inform development of self and others and disseminate/lead as part of clinical governance',
     'use the results of interventions to develop {s} and others, and share findings or lead within clinical governance', ['use', 'inform', 'disseminate', 'lead'])])
row('multidisciplinary teamwork', 'subject-skill', 'communication', 'Whose contribution in the team do you rely on most, and how do you make use of it?', [
    ('Participate in teamwork that respects and uses the contributions of colleagues in a variety of veterinary healthcare situations',
     "take part in teamwork that values and makes use of colleagues' contributions across veterinary care settings", ['participate', 'respects', 'uses']),
    ('Contribute with skill and confidence to effective multidisciplinary working, providing direction as necessary',
     'contribute skilfully and confidently to multidisciplinary work, giving direction where needed', ['contribute', 'providing']),
    ('Apply and develop advanced interpersonal, team and networking skills to strategically enhance team performance in unpredictably complex contexts and contribute to specialist professional communities',
     'use and grow advanced interpersonal, team and networking skills to lift team performance strategically in highly complex settings and to take part in specialist professional communities', ['apply', 'develop', 'enhance', 'contribute'])])
row('ethics in patient care', 'subject-skill', 'thinking', 'What ethical question came up on a recent case, and how was it settled?', [
    ('Recognise the moral and ethical issues that relate to veterinary patient care', 'recognise the moral and ethical questions in caring for veterinary patients', ['recognise']),
    ('Critically evaluate the moral and ethical issues that relate to veterinary patient care and advocate for animal welfare',
     'critically evaluate the moral and ethical questions in caring for veterinary patients and speak up for animal welfare', ['evaluate', 'advocate']),
    ('Systematically apply an advanced awareness of ethical and professional values and codes of conduct, to personal and strategic decisions, actions, responsibilities, outcomes and dilemmas, while working proactively with others to suggest and advocate appropriate solutions in unpredictably complex contexts',
     'apply an advanced grasp of ethical and professional values and codes systematically to personal and strategic decisions and dilemmas, working with others to propose and argue for solutions in highly complex settings', ['apply', 'working', 'suggest', 'advocate'])])

table(T3)
row('core subject knowledge', 'knowledge', 'knowledge', 'Which underpinning subject do you find hardest to use on the ward, and why?', [
    ('Demonstrate a sound knowledge of the fundamental subjects which underpin Veterinary Nursing, and apply the knowledge and skills required of a veterinary nurse in everyday practice',
     "show sound knowledge of the core subjects behind veterinary nursing and use a veterinary nurse's knowledge and skills in daily practice", ['demonstrate', 'apply']),
    ('Demonstrate a robust knowledge of the fundamental subjects which underpin Veterinary Nursing, apply the knowledge and skills required of a veterinary nurse in everyday practice, and continually evaluate nursing care provision to inform the enhancement of professional practise',
     "show robust knowledge of the core subjects behind veterinary nursing, use a veterinary nurse's knowledge and skills in daily practice and keep evaluating nursing care to improve professional practice", ['demonstrate', 'apply', 'evaluate']),
    ('Be cognisant of the knowledge, skills and behaviours aligned to professional practitioners',
     'be aware of the knowledge, skills and behaviours expected of professional practitioners', ['be'])])
row('cultural awareness and anti-discriminatory practice', 'subject-skill', 'thinking', 'How might a client\'s background shape what they need from you, and how would you find out?', [
    ('Demonstrate the skills of cultural awareness and role modelling behaviours that underpin anti-discriminatory practice',
     'show cultural awareness and model the behaviours that anti-discriminatory practice depends on', ['demonstrate']),
    ('Critically analyse the diversity of experience and values of groups and individuals to advance anti-discriminatory practice',
     'critically analyse how experience and values differ across groups and individuals to further anti-discriminatory practice', ['analyse', 'advance']),
    ('Apply the skills of inclusivity and adaptation in the pursuit of anti-discriminatory practice',
     'apply inclusive and adaptive skills in pursuing anti-discriminatory practice', ['apply'])])
row('communication and evidence-based decisions', 'generic-skill', 'communication', 'How would you explain this decision to an owner, and how to a vet?', [
    ('Communicate effectively with others in a clear and articulate manner, to a wide variety of audiences, using a range of media',
     'communicate clearly and articulately with many kinds of audience through a range of media', ['communicate']),
    ('Articulately present robust evidence in written and verbal format, using technology which supports sound decision-making',
     'present strong evidence clearly in writing and speech, using technology that supports sound decisions', ['present', 'using', 'supports']),
    ('Demonstrate decision-making using evidence, criticality and originality in thought',
     'show decision-making that uses evidence and is critical and original in its thinking', ['demonstrate'])])
row('therapeutic client relationships', 'subject-skill', 'communication', 'What helps an anxious owner trust you, and what gets in the way?', [
    ('Develop and maintain therapeutic interpersonal relationships with clients considering diversity, environments and other impacting factors',
     'build and keep therapeutic relationships with clients, taking account of diversity, settings and other influences', ['develop', 'maintain']),
    ('Enhance therapeutic interpersonal relationships with a diverse range of clients through creative use of concepts and theories and critical reflection',
     'strengthen therapeutic relationships with a wide range of clients by creative use of concepts and theory and by critical reflection', ['enhance']),
    ('Demonstrate inclusive and adaptive behaviours aligned with professional interrelationships',
     'show inclusive, adaptive behaviour in professional relationships', ['demonstrate'])])
row('contemporary evidence-based nursing', 'subject-skill', 'application', 'What part of your nursing have you updated because of newer evidence?', [
    ('Reflect upon and provide modern, contemporary and evidence-based Veterinary Nursing through practical skills and application of knowledge',
     'reflect on and give up-to-date, evidence-based veterinary nursing through practical skill and applied knowledge', ['reflect', 'provide']),
    ('Demonstrate robust and evidence-based modern and contemporary Veterinary Nursing using critical judgement to evaluate, inform decision-making and synthesise new approaches to enhance quality of care',
     'show robust, up-to-date, evidence-based veterinary nursing, using critical judgement to evaluate, guide decisions and combine new approaches that raise the quality of care', ['demonstrate', 'using', 'evaluate', 'inform', 'synthesise', 'enhance']),
    ('Articulate judgements using thoughtful, evidence-based and critical reasoning as a reflective base',
     'express judgements through careful, evidence-based, critical reasoning grounded in reflection', ['articulate', 'using'])])
row('evidence and data in judgement', 'subject-skill', 'thinking', 'Which data do you trust most when judging a patient\'s progress, and why?', [
    ('Use evidence, data and a range of technology to inform judgements and enhance veterinary healthcare',
     'use evidence, data and technology to inform judgements and improve veterinary care', ['use', 'inform', 'enhance']),
    ('Apply the skills of critical analysis and syntheses, using robust evidence and data in the creation of new theory, in the pursuit of healthcare excellence',
     'apply critical analysis and synthesis, using strong evidence and data to build new theory in pursuit of excellent care', ['apply', 'using']),
    ('Apply the skills of evaluation to apply critical reasoning to justify evidence-based judgements in the advancement of health care excellence',
     'apply evaluation and critical reasoning to justify evidence-based judgements that advance excellent care', ['apply', 'justify'])])
row('reflection for self-improvement', 'generic-skill', 'autonomy', 'What feedback has most changed your practice, and how did you act on it?', [
    ('Apply skills of introspection and reflection to improve professional practice', 'use introspection and reflection to improve professional practice', ['apply', 'improve']),
    ('Adopt a reflective approach to self- improvement using critical evaluation and analysis with consideration to the impact on colleagues, to enhance professional practice',
     'reflect on {p} own improvement through critical evaluation and analysis, weighing the effect on colleagues, to strengthen professional practice', ['adopt', 'using', 'enhance']),
    ('Consider an evaluative and critically reflective approach to self-improvement to professional practice',
     'take an evaluative, critically reflective approach to improving {s} in professional practice', ['consider'])])

table(T4)
row('managing self and others under the code', 'subject-skill', 'autonomy', 'Where are the limits of what you can safely do on your own, and how do you know?', [
    ('Manage themselves, their own professional practise and that of others, in accordance with the Code of Professional Conduct, recognising their own abilities and limitations',
     'manage {s}, {p} practice and that of others in line with the professional code of conduct, knowing {p} own strengths and limits', ['manage', 'recognising']),
    ('Manage themselves, their own professional practise and that of others in accordance with the Code of Professional Conduct, and critically evaluate and reflect on their own abilities and limitations',
     'manage {s}, {p} practice and that of others in line with the professional code of conduct, and weigh up critically, and reflect on, {p} own strengths and limits', ['manage', 'evaluate', 'reflect']),
    ('Manage themselves, their own professional practise and that of others in accordance with the Code of Professional Conduct. Critically evaluate and reflect on the importance of educating and promoting these expectations',
     'manage {s}, {p} practice and that of others in line with the professional code of conduct, and critically evaluate and reflect on why teaching and promoting those expectations matters', ['manage', 'evaluate', 'reflect'])])
row('applying knowledge across clinical settings', 'subject-skill', 'application', 'What happened the last time a case went off script, and what did you draw on?', [
    ('Select and apply knowledge and skills to a variety of clinical settings and unexpected situations',
     'choose and apply knowledge and skills across different clinical settings and unforeseen situations', ['select', 'apply']),
    ('Select and apply knowledge and skills to a variety of clinical settings and unexpected situations',
     'choose and apply knowledge and skills across different clinical settings and unforeseen situations', ['select', 'apply']),
    ('Develop knowledge and skills through contribution to evidence-based Veterinary Nursing to a variety of clinical settings and unexpected situations',
     'extend knowledge and skills by contributing to evidence-based veterinary nursing across different clinical settings and unforeseen situations', ['develop'])])
row('collaborative therapeutic and preventive care', 'subject-skill', 'application', 'How do you bring the client into decisions about preventive care?', [
    ('Work in collaboration with clients and colleagues to identify and provide the therapeutic and preventative veterinary healthcare requirements to meet the needs of patients',
     'work with clients and colleagues to identify and give the therapeutic and preventive care patients need', ['work', 'identify', 'provide']),
    ('Implement strategies to promote and evaluate collaborative working with patients, clients and colleagues to identify and provide therapeutic and preventative veterinary healthcare requirements of patients',
     'put in place strategies that promote and evaluate collaboration with patients, clients and colleagues in identifying and giving therapeutic and preventive care', ['implement', 'promote', 'evaluate']),
    ('Synthesise strategies to promote and evaluate collaborative working with patients, clients and colleagues to identify and provide therapeutic and preventative veterinary healthcare requirements of patients',
     'synthesise strategies that promote and evaluate collaboration with patients, clients and colleagues in identifying and giving therapeutic and preventive care', ['synthesise', 'promote', 'evaluate'])])
row('empathy in challenging situations', 'subject-skill', 'autonomy', 'Think of a hard conversation with an owner: what did you do that helped?', [
    ('Provide empathetic support to patients, clients and colleagues in changing and potentially challenging situations',
     'give empathetic support to patients, clients and colleagues when situations change or become difficult', ['provide']),
    ('Anticipate and deal with challenging situations, involving patients, clients and colleagues, in an empathetic manner while minimising risk where necessary',
     'foresee and handle difficult situations with patients, clients and colleagues with empathy, reducing risk where needed', ['anticipate', 'deal', 'minimising']),
    ('Lead and support colleagues through a diverse range of challenging situations, involving patients, clients and colleagues, in an empathetic manner while minimising risk, where appropriate',
     'lead and support colleagues through many kinds of difficult situation with patients, clients and colleagues, with empathy and with risk kept low where fitting', ['lead', 'support'])])
row('the professional, ethical and legal framework', 'subject-skill', 'thinking', 'Which rule or law most often shapes what you can do for a patient?', [
    ('Practise in accordance with the professional, ethical and legal framework', 'practise within the professional, ethical and legal framework', ['practise']),
    ('Recognise the complexity of the professional, ethical and legal framework and its impact on decision-making and practise accordingly',
     'recognise how complex the professional, ethical and legal framework is and how it bears on decisions, and practise to match', ['recognise', 'practise']),
    ('Appraise the complexity of the professional, ethical and legal frameworks. Provide guidance and leadership to colleagues in relation to the impacts of decision-making',
     'appraise how complex the professional, ethical and legal frameworks are, and guide and lead colleagues on what decisions entail', ['appraise', 'provide'])])
row('responsibility and impartial decisions', 'subject-skill', 'autonomy', 'When did you last have to stay impartial, and how did you manage it?', [
    ('Uphold personal responsibility and impartial decision-making across a range of situations', 'uphold personal responsibility and impartial decisions in many situations', ['uphold']),
    ('Critically reflect on personal responsibility and decision-making across a range of situations', 'reflect critically on personal responsibility and decision-making in many situations', ['reflect']),
    ('Critically reflect and evaluate on both personal and interprofessional responsibility and decision-making across a range of situations',
     'reflect critically on, and evaluate, personal and interprofessional responsibility and decision-making in many situations', ['reflect', 'evaluate'])])
row('a safe clinical environment', 'subject-skill', 'application', 'What hazard in your clinic worries you most, and what would reduce it?', [
    ('Contribute to public protection by creating and maintaining a safe clinical environment', 'help protect the public by creating and keeping a safe clinical environment', ['contribute', 'creating', 'maintaining']),
    ('Select and implement a range of risk management strategies to create and maintain a safe clinical environment for protection',
     'choose and put in place several risk-management strategies that create and keep a safe clinical environment', ['select', 'implement', 'create', 'maintain']),
    ('Analyse and inform processes to improve a range of risk and management strategies to create and maintain a safe clinical environment, taking into account one health',
     'analyse and shape processes that improve risk-management strategies for a safe clinical environment, with one health in view', ['analyse', 'inform', 'improve'])])
row('guidance, role-modelling and mentorship', 'subject-skill', 'autonomy', 'Who have you helped learn something recently, and how did you go about it?', [
    ('Provide guidance, role-modelling and support to others in the veterinary environment', 'guide, set an example for and support others in the veterinary setting', ['provide']),
    ('Provide guidance, role-modelling, mentorship and support to others in the veterinary environment, ensuring effective supervision and monitoring',
     'guide, set an example for, mentor and support others in the veterinary setting, making sure supervision and monitoring work', ['provide', 'ensuring']),
    ('Inspire self and others to act as ambassadors to uphold the reputation of the profession both in and out of the veterinary environment',
     "inspire {s} and others to act as ambassadors who uphold the profession's reputation inside and outside the veterinary setting", ['inspire', 'act', 'uphold'])])
row('roles, delegation and supervision', 'subject-skill', 'autonomy', 'What would you delegate, and what would you never delegate, and why?', [
    ('Understand the role of self and of others, including when delegation, supervision and seeking advice is appropriate',
     "understand {p} own role and others', including when to delegate, supervise or ask for advice", ['understand']),
    ('Critically analyse roles of self and of others, including appropriate delegation, supervision and seeking advice',
     "critically analyse {p} own role and others', including suitable delegation, supervision and advice-seeking", ['analyse']),
    ('Critically evaluate and reflect upon roles of self and of others, providing guidance on appropriate delegation, supervision and when to seek advice',
     "critically evaluate and reflect on {p} own role and others', guiding others on suitable delegation, supervision and when to seek advice", ['evaluate', 'reflect', 'providing'])])
row('advocacy, advice and well-being', 'subject-skill', 'communication', 'When you advise an owner, how do you speak up for the animal while looking after yourself?', [
    ('Demonstrate empathy with patients and clients and act as an advocate for them, when appropriate, with an appreciation for their own mental and physical health and well-being',
     'show empathy with patients and clients and advocate for them where fitting, mindful of {p} own mental and physical health', ['demonstrate', 'act']),
    ('Provide advice to clients and act as an advocate for them and the patient, when appropriate, with an appreciation for their own mental and physical health and well-being',
     'advise clients and advocate for them and the patient where fitting, mindful of {p} own mental and physical health', ['provide', 'act']),
    ('Awareness of factors that impact on mental and physical health and well-being. Implement strategies to support others to provide advice to clients and act as an advocate for them and the patient, when appropriate',
     'be aware of what affects mental and physical health, and put in place strategies that help others advise clients and advocate for them and the patient', ['implement', 'support', 'provide', 'act'])])
row('research and the evidence base', 'subject-skill', 'research', 'What clinical question would you most like answered by research, and how would you start?', [
    ('Participate in the development of an evidence base in clinical practice and understand the importance of such work',
     'take part in building an evidence base in clinical practice and understand why that work matters', ['participate', 'understand']),
    ('Plan and execute research and development work, including the development of an evidence base for clinical practice',
     'plan and carry out research and development, including building an evidence base for clinical practice', ['plan', 'execute']),
    ('Propose new approaches to the continual development of evidence- based Veterinary Nursing. Evaluate the impact of their research and dissemination of concepts',
     'propose new approaches to keep developing evidence-based veterinary nursing and evaluate the impact of {p} research and of sharing its ideas', ['propose', 'evaluate'])])
_X42 = 'take up and promote equality, diversity and inclusion in the veterinary setting and beyond it'
_T42 = 'Adopt and promote equality, diversity and inclusion within the veterinary environment and beyond'
row('equality, diversity and inclusion in practice', 'subject-skill', 'autonomy', 'What have you done, or seen done, to make your workplace more inclusive?', [
    (_T42, _X42, ['adopt', 'promote']), (_T42, _X42, ['adopt', 'promote']), (_T42, _X42, ['adopt', 'promote'])])
row('professional development', 'generic-skill', 'autonomy', 'What new competence do you want next, and how will you get it?', [
    ('Reflect on own skills and recognise the opportunities to develop and acquire new competences in line with professional development requirements',
     'reflect on {p} own skills and see chances to develop and gain new competences as professional development requires', ['reflect', 'recognise']),
    ('Critically evaluate own skills and recognise and engage with the opportunities to develop and acquire new competences in line with professional development requirements',
     'critically evaluate {p} own skills and see and take chances to develop and gain new competences as professional development requires', ['evaluate', 'recognise', 'engage']),
    ('Support and lead colleagues to recognise and engage with the opportunities to develop and acquire new competences in line with professional development requirements',
     'support and lead colleagues in seeing and taking chances to develop and gain new competences as professional development requires', ['support', 'lead', 'recognise', 'engage'])])

_NCELL = 3 * _row

GRADE = {}   # no typical or excellent rungs: the columns are awards, not rungs
TH = {'1.12': 'theme:edi', '1.13': 'theme:edi', '1.14': 'theme:accessibility', '1.15': 'theme:accessibility', '1.16': 'theme:accessibility',
      '1.17': 'theme:esd', '1.18': 'theme:esd', '1.22': 'theme:enterprise'}

def _cells(*rows):
    out = []
    for r in rows:
        out += ['4.2.b%d.foundation' % r, '4.2.b%d' % r, '4.2.b%d.masters' % r]
    return out

S5 = dict(levels=[dict(id='fheq:5', role='cites', locator='D1, 1.9; 2.6; 4.2 (column headings)'),
                  dict(id='fheq:6', role='cites', locator='D1, 1.9; 2.6; 4.2 (column headings)'),
                  dict(id='fheq:7', role='cites', locator='D1, 1.9; 4.2 (column headings)'),
                  dict(id='fqheis:10', role='cites', locator='D1, 1.9 (SCQF Level 10); 2.6 (FQHEIS Level 10); 4.2 (SCQF Level 10)'),
                  dict(id='fqheis:11', role='cites', locator='D1, 1.9 (SCQF Level 11)')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 1.9; 2.6; the honours column heading in 4.2: FHEQ Level 6 / SCQF Level 10)'),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 1.9: master\'s level courses at Level 7 on the FHEQ and Level 11 on the SCQF)')])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.11', '1.12', '1.13', '1.15', '1.19', '2.13', '3.1', '3.15', '4.2']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.14', '1.15', '1.16', '2.9']),
      dict(id='theme:esd', role='carries', carriedIn=['1.17', '1.18', '1.19', '1.22', '4.2']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.20', '1.21', '1.22', '3.15'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-veterinary-nursing-2019-benchmarks (not yet ingested)', note='the second edition, 2019, revised by QAA to align with the 2018 Quality Code; the first edition was 2015 (section 6)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='degree classification descriptions for honours, cited in 4.2'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='levels 5, 6 and 7 (1.9, 2.6, 4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='SCQF levels 10 and 11 (1.9, 2.6, 4.2)'),
      dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='Education for Sustainable Development Guidance (1.17)'),
      dict(rel='refersTo', target='std:doc:qaa-enterprise-2018-guidance', note='Enterprise and Entrepreneurship Education guidance (section 5 references only)'),
      dict(rel='refersTo', target='RCVS Day One Competences, Skills and Professional Behaviours for Veterinary Nurses (not yet ingested)', note='1.7, 1.14, 2.2, 2.3, 2.4, 2.5, 2.11'),
      dict(rel='refersTo', target='RCVS Code of Professional Conduct for Veterinary Nurses (not yet ingested)', note='1.4, 1.5, 3.9; the professional expectations table'),
      dict(rel='refersTo', target='RCVS Standards Framework for Veterinary Nurse Education and Training (not yet ingested)', note='front matter'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance', note='front matter')]

SB1 = [
    'A science-based degree with a strong vocational focus, meant to make graduates ready to register as veterinary nurses when they graduate (D1, 1.6)',
    'Veterinary nurses give professional care grounded in knowledge of each patient\'s condition, across many settings and every life stage, mindful of the owner or keeper (D1, 1.1)',
    'The work aims at animal health, welfare and quality of life with as little pain and suffering as possible, and can be proactive or reactive, autonomous or collaborative (D1, 1.2)',
    'Registered nurses may give medical treatment and minor surgery that does not enter a body cavity, under a veterinary surgeon\'s direction, and educate owners and the public (D1, 1.3)',
    'Practice is regulated through RCVS registration, a code of conduct with five principles, continuing development and fitness to practise (D1, 1.4, 1.5)',
    'Licence to practise courses are built around the RCVS Day One Competences, Skills and Professional Behaviours and long clinical placements in approved training practices (D1, 1.7, 2.4, 2.5)',
    'Courses cover a range of species, with small animal and equine routes and, in some places, farm animal husbandry (D1, 3.1, 3.3 to 3.5)',
    'The statement covers three awards side by side: foundation degree, honours degree and master\'s degree (D1, 1.8, 1.9, 4.1)',
]
SB2 = [
    dict(theme='theme:edi', inThisSubject='inclusive learning and placement settings; equity treated as a professional duty towards teams, owners and the public; respect for cultures and anti-discriminatory practice at every award, with barriers for people with protected characteristics analysed (D1, 1.11 to 1.13; 3.1; 4.2 tables)',
         statements=['1.12', '1.13'] + _cells(8, 9, 10, 26, 43)),
    dict(theme='theme:accessibility', inThisSubject='accessibility from pre-application to after graduation, including equal workplace learning on placement and adjustable assessment that still lets every student meet the RCVS requirements (D1, 1.14 to 1.16; 2.9)',
         statements=['1.14', '1.15', '1.16']),
    dict(theme='theme:esd', inThisSubject='animal welfare as a sustainability goal; climate action, antimicrobial resistance, zoonoses and clinical waste; a sustainable approach to practice at every award (D1, 1.17 to 1.19; 4.2 table)',
         statements=['1.17', '1.18'] + _cells(11)),
    dict(theme='theme:enterprise', inThisSubject='enterprise education designed with employers, professional bodies and service users, with group work building teamwork, negotiation and leadership, and authentic assessment for employability (D1, 1.20 to 1.22; 3.15)',
         statements=['1.22']),
]
SB3 = dict(
    areas=[dict(component='3.1', gloss='knowledge areas across species, from anatomy to legislation and anti-discriminatory practice'),
           dict(component='3.2', gloss='appraising, applying and producing research'),
           dict(component='3.5', gloss='basic farm animal husbandry in some curricula'),
           dict(component='3.7', gloss='clinical and technical skills, from handling to maintaining anaesthesia'),
           dict(component='3.9', gloss='ethics, cultural diversity, law and the professional code in course design')],
    practices=[dict(component='3.8', kind='learning', gloss='nursing skills learned in class and on placement'),
               dict(component='3.11', kind='teaching', gloss='methods chosen locally with the RCVS requirements'),
               dict(component='3.12', kind='learning', gloss='student-centred, reflective and critical learning for lifelong learning'),
               dict(component='3.16', kind='assessment', gloss='formative, self and peer assessment beside summative'),
               dict(component='3.17', kind='assessment', gloss='competence and fitness to practise judged by academic and clinical staff together')])
SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.1', award=[FD, HON, MA], items=_NCELL)],
    rungBases=('4.1 sets the minimum threshold standards for all three awards; each of the four tables (%s) carries the lead-in "Graduates should be able to:" '
               'and one column per award, so one row is one outcome at three awards. No typical or excellent rung is stated; 4.2 leaves achievement above threshold '
               'to each provider with Annex D. Rows by table: %s.') % ('; '.join(t[0] for t in TABLES), '; '.join('%s 4.2.b%d to 4.2.b%d' % (t[0], t[1], t[2]) for t in TABLES)),
    outcomeLists=[dict(leadIn='3.10', gloss='personal and professional abilities students should develop', items=5, award=[FD, HON])],
    outcomes=OUTCOMES)
SB4A_FULL = []
SB5 = [dict(body='Royal College of Veterinary Surgeons (RCVS)',
            says='the PSRB for the subject; keeps the non-statutory register of veterinary nurses and its code of conduct; sets the Standards Framework for Veterinary Nurse Education and the Day One Competences, Skills and Professional Behaviours; accredits licence to practise courses, training practices and post-registration qualifications; registered nurses use RVN or Cert AVN (D1, front matter; 1.4; 1.7; 1.14; 2.2 to 2.5; 2.8; 2.9; 2.11; 3.9; 3.11; 3.17)',
            requirements='not yet ingested (Part E)'),
       dict(body='Office for Students',
            says='in England, Subject Benchmark Statements are not sector-recognised standards under its regulatory framework (D1, front matter)',
            requirements='not yet ingested (Part E)')]
SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=['1.11', '1.12', '1.13', '1.15', '1.19', '2.13', '3.1', '3.15', '4.2'],
                 statements=['1.12', '1.13'] + _cells(8, 9, 10, 26, 43)),
            dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=['1.14', '1.15', '1.16', '2.9'],
                 statements=['1.14', '1.15', '1.16']),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=['1.17', '1.18', '1.19', '1.22', '4.2'],
                 statements=['1.17', '1.18'] + _cells(11)),
            dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)',
                 carriedIn=['1.20', '1.21', '1.22', '3.15'], statements=['1.22'])],
    frameworks=[dict(framework='fheq', levels=['fheq:5', 'fheq:6', 'fheq:7'], citedIn=['1.9', '2.6', '4.2']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['1.9', '2.6', '4.2'])],
    bodies=[dict(body='Royal College of Veterinary Surgeons', citedIn=['front matter', '1.4', '1.7', '1.14', '2.2', '2.3', '2.5', '2.8', '2.9', '3.9', '3.11', '3.17']),
            dict(body='Office for Students', citedIn=['front matter'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.2'],
             role='common descriptions of the four honours classifications, for judging achievement above threshold'),
        dict(document='std:doc:qaa-fheq-2024-framework', named='The Frameworks for Higher Education Qualifications (FHEQ; FQHEIS; SCQF levels)', citedIn=['1.9', '2.6', '4.2'], role='the levels of the three awards'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named="QAA and Advance HE's Education for Sustainable Development Guidance, 2021", citedIn=['1.17'], role='the frame for the sustainability theme'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (2018)', citedIn=['section 5'], role='listed as a further resource for the enterprise theme'),
        dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code', citedIn=['front matter'], role='course design, teaching, external expertise, monitoring'),
        dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='Quality Assessment Framework for Wales; Quality Enhancement Framework (Scotland) (not ingested)', named='Quality Assessment Framework for Wales; Quality Enhancement Framework', citedIn=['front matter'], role='the statement\'s status in Wales and Scotland'),
        dict(document='RCVS documents (not yet ingested: Part E, D3)', named='Day One Competences, Day One Skills List, Professional Behaviours and Attributes; Code of Professional Conduct for Veterinary Nurses; Standards Framework for Veterinary Nurse Education; Veterinary Nurse Registration Rules 2017; Post-registration Framework for Veterinary Nursing',
             citedIn=['front matter', '1.4', '1.5', '1.7', '1.14', '2.2', '2.3', '2.5', '3.9'], role='the professional body\'s requirements for registration and accreditation'),
        dict(document='UN Sustainable Development Goals; UN Principles for Responsible Management Education (external)', named='UN Sustainable Development Goals; PRME', citedIn=['1.17', '1.18'], role='the frame of sustainable development and responsible management'),
        dict(document='IPCC (2022) (external)', named='IPCC, 2022', citedIn=['1.18'], role='the emissions target'),
        dict(document='Vet Sustain (2020) (external)', named='Vet Sustain 2020', citedIn=['1.19'], role='source of the example sustainability topics')])

B1 = [
    dict(slug='day-one-competences', definition='the RCVS list of competences a student veterinary nurse must gain and evidence to join the register, abbreviated DOC (D1, 1.7)',
         beneficiaryDefinition='the abilities you must show before you can register as a veterinary nurse', scopeNote='set by the RCVS; with DOS and PB', category='unknown', practices=['education']),
    dict(slug='day-one-skills-list', definition='the RCVS list of practical skills a student veterinary nurse must meet to register, abbreviated DOS (D1, 1.7, 2.4)',
         beneficiaryDefinition='the hands-on skills you must master before you can register', scopeNote='set by the RCVS', category='unknown', practices=['education']),
    dict(slug='professional-behaviours-and-attributes', definition='the RCVS professional behaviours required for registration, abbreviated PB (D1, 1.7)',
         beneficiaryDefinition='how you are expected to behave as a professional before you can register', scopeNote='set by the RCVS', category='unknown', practices=['education']),
    dict(slug='registered-veterinary-nurse', definition='a veterinary nurse on the RCVS register, entitled to the postnominals RVN (D1, front matter; 1.6)',
         beneficiaryDefinition='a qualified veterinary nurse on the professional register', scopeNote='Cert AVN marks an accredited post-registration qualification', category='unknown', practices=['education']),
    dict(slug='licence-to-practise-qualification', definition='a course fully accredited by the RCVS whose graduates may apply to the register (D1, front matter; 1.7; 2.2)',
         beneficiaryDefinition='a course that lets you apply to register when you finish', scopeNote='the issuer spells it Licence and License', category='unknown', practices=['education']),
    dict(slug='training-practice', definition='a veterinary practice approved for clinical placement, abbreviated TP, with auxiliary training practices beside it (D1, 2.5, 2.12)',
         beneficiaryDefinition='the approved clinic where you do your placement', scopeNote='approved and monitored by course providers (2.12)', category='unknown', practices=['education']),
    dict(slug='accessibility', definition='whether every part of a course, however met, can be understood by everyone (D1, 1.14)',
         beneficiaryDefinition='whether every part of your course works for you, whatever your needs', scopeNote='a cross-cutting theme', category='unknown', practices=['education']),
]
B2A = [
    dict(concept='day-one-competences', form='Day One Competences', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
    dict(concept='day-one-competences', form='DOC', lang='en', partOfSpeech='noun', termStatus='admitted', register='discipline-specific'),
    dict(concept='day-one-skills-list', form='Day One Skills List', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
    dict(concept='day-one-skills-list', form='DOS', lang='en', partOfSpeech='noun', termStatus='admitted', register='discipline-specific'),
    dict(concept='professional-behaviours-and-attributes', form='Professional Behaviours and Attributes', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
    dict(concept='professional-behaviours-and-attributes', form='PB', lang='en', partOfSpeech='noun', termStatus='admitted', register='discipline-specific'),
    dict(concept='registered-veterinary-nurse', form='registered veterinary nurse', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='registered-veterinary-nurse', form='RVN', lang='en', partOfSpeech='noun', termStatus='admitted', register='discipline-specific'),
    dict(concept='licence-to-practise-qualification', form='License to Practise Qualification', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
    dict(concept='training-practice', form='training practice', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
    dict(concept='training-practice', form='TP', lang='en', partOfSpeech='noun', termStatus='admitted', register='discipline-specific'),
    dict(concept='accessibility', form='accessibility', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
]
B4 = []; B5 = []
D3 = [dict(citation='Royal College of Veterinary Surgeons, Day One Competences, Skills and Professional Behaviours for Veterinary Nurses', settles=['SB5', 'S7'], asked='2026-10-03', state='wanted'),
      dict(citation='Royal College of Veterinary Surgeons, Code of Professional Conduct for Veterinary Nurses', settles=['SB5', 'S7'], asked='2026-10-03', state='wanted'),
      dict(citation='Royal College of Veterinary Surgeons, Standards Framework for Veterinary Nurse Education and Training', settles=['SB5', 'S7'], asked='2026-10-03', state='wanted'),
      dict(citation='Royal College of Veterinary Surgeons, Post Registration Framework for Veterinary Nursing; Veterinary Nurse Registration Rules 2017', settles=['SB5'], asked='2026-10-03', state='wanted'),
      dict(citation='QAA, Subject Benchmark Statement: Veterinary Nursing, second edition (2019)', settles=['S7'], asked='2026-10-03', state='wanted')]

E = [
    'SB4, rungs: no typical or excellent rung. 4.1 states minimum threshold standards for three awards; the four section 4 tables give one column per award (foundation degree, FHEQ 5; honours, FHEQ 6 / SCQF 10; master\'s, FHEQ 7), not per rung. Recorded as rung threshold throughout, %d cells in %d rows (pattern differs from Psychology).' % (_NCELL, _row),
    'S4, ids: the tables carry no issuer numbers and sit after 4.2 under their own headings. Rows are numbered 4.2.b1 to 4.2.b%d in held-text order (tables listed in SB4 rungBases); the honours cell keeps the base id, the master\'s cell takes .masters (brief convention) and the foundation cell takes .foundation, a new suffix for a third award column: for std to confirm.' % _row,
    'S4, force: each table cell is recorded as threshold with forceFrom 4.1 (the minimum for the award); the tables\' own lead-in is "Graduates should be able to:", kept in every version as should.',
    'S4, flattened tables: cells placed by reading each row in column order. Doubtful placements for P3: generic skills row 3 (4.2.b3), where "Critically evaluate arguments, assumptions, abstract concepts and data" is read as the second sentence of the honours cell, not a cell of its own; professional expectations row 10 (4.2.b41), where "Awareness of factors that impact on mental and physical health and well-being." is read as the start of the master\'s cell; subject knowledge row 6 (4.2.b30), where the honours cell (creating new theory) reads as more advanced than the master\'s cell (evaluation), kept as placed.',
    'S4, identical cells: rows 4.2.b7, 4.2.b8, 4.2.b10, 4.2.b13 (honours and master\'s), 4.2.b33 (foundation and honours) and 4.2.b43 repeat the same wording in more than one column; each column is still its own record with the same paraphrase.',
    'SB4, outcomes: each row links its three award cells (foundation, masters keys beside threshold) with basis stated, since the issuer\'s table rows pair them; gradeOf is not used because the columns are awards, not rungs. No GRADE links.',
    'S4, held text: the issuer spells "practise" as a noun in "professional practise" (4.2.b25, honours; all three cells of 4.2.b32) and "evidenced-based" in 4.2.b16; kept in source, corrected in our words.',
    'S4, statements taken from sections 1 to 3 (D-std-0002 (a)): obliging paragraphs 1.4, 1.6, 1.7, 1.12 to 1.16, 1.18, 1.22, 2.2 to 2.5, 2.8, 2.10 to 2.12, 2.14, 3.13 to 3.15, 3.18 and 4.2\'s first part; the 2.1 minimum content list (11 items); the 3.10 outcome list (5 items); 2.6 for its master\'s outcome in will.',
    'S4, obliging words outside the five, recorded as describes for Abbott: 1.17 "There is an expectation that" ERS are integrated; 2.9 "Providers are expected to" set up oversight; 3.3 and 3.4 "It is anticipated that" holders are proficient. 2.6 also uses "it is expected that" and "would be expected", taken with its will sentence.',
    'S4, required read as must: 2.2 ("This is a requirement for ... accreditation").',
    'S4, mixed force: 2.3 is will for foundation and honours and should for master\'s, recorded as will; 1.7 is should on the course, must from the RCVS on the student, recorded as should.',
    'S4, not statements: 1.3 ("Veterinary nurses are able to") describes the registered profession, not graduates; 1.5 lists the code\'s principles; 1.8 and 1.9 describe the statement; 1.19 lists topics that "could usefully be incorporated"; 2.15 describes external examining; 3.2 ("can cover") and 3.5 describe content; 4.1 is the threshold lead-in.',
    'S4, plain-present provider norms not taken as statements (template open point 5): 2.7, 2.11\'s first sentence, 2.13 ("will form part" of review), 3.1 ("aim to develop"), 3.6, 3.7, 3.8, 3.9 ("Courses are designed to ensure"), 3.11, 3.12, 3.16, 3.17.',
    'S4, items under a may: 1.14\'s three examples follow "It may include", so 1.14 is one record over its whole span, not three item records.',
    'S4, 3.3 is one record over the stem and its species list (cats, dogs, exotic species), since the items are species, not outcomes.',
    'S4, levels inferred: 3.10\'s items take fheq:5 and the awards foundation and honours, because section 3 frames content for foundation and honours courses (3.1, 3.11); the list names no award.',
    'S4, 4.2: recorded by find over its own paragraph only; the skeleton\'s 4.2 span ran to the end of the tables.',
    'S3, headings: the four table headings (Generic skills; Principles and concepts: application; Subject knowledge, understanding and associated skills; Working as a professional veterinary nurse: expectations) are not numbered components; the builder shows 4.2\'s heading, Introduction, in each cell\'s headingPath. Each cell names its table in appliesTo.',
    'S3, skeleton: the 3.3 to 3.6 paragraphs fall under the issuer\'s heading Research and evidence-based practice although they concern species and skills; recorded as the issuer places them.',
    'Subjects: HECoS 100532 veterinary nursing matches the stated subject; CAH05-01-02 (others in veterinary sciences) is inferred from the HECoS mapping, held back from lookups until P3.',
    'S5: no Scottish level is stated for the foundation degree (the FHEQ\'s Table 1 has none); fqheis:11 for master\'s is stated in 1.9 only, not in the table heading.',
    'SB5, SB6: the RCVS requirements (Day One Competences, Skills and Professional Behaviours; the code of conduct; the Standards Framework; the registration rules; the post-registration framework) are not yet ingested (D3). The Office for Students\' regulatory framework is not ingested.',
    'SB6, themes: generative AI and other themes are not named. Mental health and well-being appear (1.19; the tables) but no shared theme id exists for them; not tagged.',
    'SB6: the enterprise guidance (2018) is cited only in section 5\'s list of references, twice.',
    'Front matter: the edition line reads "Third edition, April 2024"; section 6 dates the earlier editions 2019 and 2015.',
    'S1, licence: the text gives a copyright notice and no re-use terms.',
    'S9: not researched in P1.',
    'Patterns that differ from Psychology: threshold only, three awards in table columns (foundation, honours, master\'s); a PSRB (RCVS) whose Day One requirements run through the design sections; many provider duties in should; no rung lists in prose.',
]
