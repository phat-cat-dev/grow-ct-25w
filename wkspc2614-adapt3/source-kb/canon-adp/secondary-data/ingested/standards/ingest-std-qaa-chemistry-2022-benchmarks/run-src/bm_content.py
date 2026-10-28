# bm_content.py: run 0092 (std), QAA Subject Benchmark Statement Chemistry, March 2022 (fifth edition). Judgement for tools/bm_build.py.
# Templates: standards 0.8.0-draft, benchmark 0.6.0-draft, run layer 0.7.0-draft; brief BM-BRIEF 0.2.1. Our words throughout; the issuer's
# words reach the document only through `source` (the span) and the `find` texts below.
# Rung tables: Table 1 (honours) gives each outcome a threshold cell and an excellent cell with their own text; the threshold cell is
# 4.6.b<n>, the excellent cell 4.6.b<n>.excellent, each on its own span. Table 2 (master's) gives one threshold and one excellent cell,
# read as applying to all five outcomes (Part E); both records sit on the outcome's span: 4.7.b<n> and 4.7.b<n>.excellent.
import json as _json, os as _os

SLUG = 'chemistry-2022'
_DIR = _os.path.join(_os.getcwd(), 'ingest-std-qaa-chemistry-2022-benchmarks')
_SK = _json.load(open(_os.path.join(_DIR, 'run-src/bm-skel.json'), encoding='utf-8'))
_NORM = open(_os.path.join(_os.getcwd(), 'stan/core/qaa/benchmarks', SLUG + '.norm.txt'), encoding='utf-8').read()
_SPAN = {c['id'].split('/')[-1]: c['span'] for c in _SK['candidateStatements']}

HON = "bachelor's with honours"
MAS = "master's"
CITE = 'QAA, 2022, Chemistry Subject Benchmark Statement'
SID = 'qaa/chemistry-2022'
NA_P = ('n/a', 'a duty on the provider or course team; the student meets its effect, not a standard to reach')

def trim(i, heading):
    """the skeleton span less a trailing sub-heading the extraction ran on to"""
    sp = _SPAN[i]
    t = _NORM[sp['start']:sp['end']].rstrip()
    assert t.endswith(heading), (i, t[-60:])
    return dict(find=t[:-len(heading)].rstrip(), after=sp['start'])

META = dict(
    run='0092', p1='2026-10-03 16:36',
    title='Subject Benchmark Statement Chemistry',
    heading='Subject Benchmark Statement: Chemistry (QAA, March 2022)',
    edition='March 2022 (fifth edition)', published='2022-03',
    status='current',
    supersedes='the fourth edition (2019), named in the advisory group list (D1, section 6); this is the fifth edition (D1, back cover)',
    subjects=[dict(scheme='hecos', code='100417', label='chemistry', basis='stated'),
              dict(scheme='cah', code='CAH07-02-01', label='chemistry', basis='stated'),
              dict(scheme='cah', code='CAH07-02', label='chemistry', basis='stated'),
              dict(scheme='hecos', code='101045', label='environmental chemistry', basis='inferred'),
              dict(scheme='hecos', code='100420', label='medicinal chemistry', basis='inferred')],
    awards=[HON, MAS], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2022 revision with cross-cutting themes (Chemistry fifth edition, March 2022)',
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    agentDefinition=("This document records what QAA's 2022 Chemistry statement expects of a graduate in chemistry and of the courses that lead there, "
                     "for the bachelor's degree with honours and for master's degrees, integrated and standalone. Read S4 for the standards: two tables "
                     "in section 4 grade each outcome at two rungs, threshold and excellent, and section 3 adds four outcome lists (core chemistry content, "
                     "optional specialist content, enabling skills for honours and further skills for integrated master's). Every standard has a "
                     "practitioner version, a student version and two instructions for AI agents that write about it or use it in conversation. Classes "
                     "between the two rungs are left to Annex D of the 2024 Frameworks, which this document points to and never copies."),
    summary=("Chemistry, bachelor's degree with honours (FHEQ level 6; FQHEIS level 10) and master's degrees (FHEQ level 7; FQHEIS level 11), fifth "
             "edition, March 2022. Two rungs are stated, threshold and excellent, with no typical rung: Table 1 grades 14 honours outcomes at both "
             "rungs and Table 2 adds five master's outcomes, graded by support at threshold and independence at excellent. Section 3 holds four outcome "
             "lists: 14 core content outcomes for all undergraduates, three optional specialist outcomes, nine enabling skills for honours and six further "
             "skills for integrated master's. Some 30 obliging paragraphs set expectations on courses: breadth, laboratory competence, inclusion, "
             "accessibility, progression, placements, monitoring, the project and assessment. Themes: equality, diversity and inclusion; accessibility; "
             "education for sustainable development; employability, enterprise and entrepreneurship. Body: the Royal Society of Chemistry, which accredits "
             "courses towards Chartered Chemist. Shared documents: Annex D, the ESD guidance, the enterprise guidance and the apprenticeships "
             "characteristics statement."),
    authority='reference: a sector reference point, not a regulatory requirement; not a sector-recognised standard in England, a key reference point in Wales and Scotland and part of the quality requirements in Northern Ireland (D1, front matter)')

S2 = dict(
    governs=("what a graduate in chemistry is expected to know, understand and be able to do at the end of a bachelor's degree with honours or a "
             "master's degree, at threshold and excellent rungs, with the context for course design, teaching and assessment"),
    awards=[HON, MAS], levels=['fheq:6', 'fqheis:10', 'fheq:7', 'fqheis:11'],
    statedScope='"This document is a QAA Subject Benchmark Statement for Chemistry that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies." (D1, front matter)',
    statedSubjects=[
        dict(name='Chemistry', locator='(D1, title; 1.1)', kind='subject',
             codes=[dict(scheme='hecos', code='100417', label='chemistry'), dict(scheme='cah', code='CAH07-02-01', label='chemistry')]),
        dict(name="integrated master's degrees with honours (MChem, MSci) and standalone master's (MSc, MRes)", locator='(D1, 2.3; 4.7)', kind='programme title',
             codes=[dict(scheme='hecos', code='100417', label='chemistry')]),
        dict(name='applications such as biological, computational, environmental, materials or medicinal chemistry', locator='(D1, 2.1)', kind='specialism',
             codes=[dict(scheme='hecos', code='101045', label='environmental chemistry'), dict(scheme='hecos', code='100420', label='medicinal chemistry')]),
        dict(name='sub-branches such as green and sustainable chemistry, cheminformatics or chemistry education', locator='(D1, 3.4)', kind='specialism',
             codes=[dict(scheme='hecos', code='100417', label='chemistry')]),
        dict(name='interdisciplinary single honours, joint and combined honours courses with chemistry', locator='(D1, 1.7; 1.14)', kind='programme title',
             codes=[dict(scheme='hecos', code='100417', label='chemistry')]),
    ])

SECTIONS = {'1': 'Context and purposes of a Chemistry degree', '2': 'Distinctive features of a Chemistry degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.1', 'Context'), ('1.2', '1.5', 'Purposes of a Chemistry degree'), ('1.6', '1.9', 'Characteristics of a Chemistry degree'),
       ('1.10', '1.11', 'Equality, diversity and inclusion'), ('1.12', '1.12', 'Education for sustainable development'),
       ('1.13', '1.15', 'Employability, enterprise and entrepreneurship'),
       ('2.1', '2.6', 'Design'), ('2.7', '2.8', 'Accessibility'), ('2.9', '2.12', 'Progression'), ('2.13', '2.13', 'Flexibility'),
       ('2.14', '2.14', 'Partnership'), ('2.15', '2.20', 'Monitoring and review'),
       ('3.1', '3.2', 'Content, structure and delivery'), ('3.3', '3.4', 'Subject knowledge and understanding'),
       ('3.5', '3.9', 'Underpinning and enabling knowledge and skills'), ('3.10', '3.14', 'Project and dissertation'),
       ('3.15', '3.20', 'Teaching and learning'), ('3.21', '3.25', 'Assessment'), ('4.1', '4.7', 'Introduction')]

G = {
    '1.1': 'chemistry as the central science; its part in global challenges',
    '1.2': 'the aims read within an inclusive, representative curriculum',
    '1.3': 'general aims of chemistry courses',
    '1.4': "aims of honours courses",
    '1.5': "aims of master's courses",
    '1.6': 'each provider sets its own content and organisation',
    '1.7': 'a broad discipline; specialist, joint and combined routes',
    '1.8': 'practical work as essential; a spiral towards independent lab work',
    '1.9': 'theory underpinned by enabling skills',
    '1.10': 'EDI built in; a shared duty to promote equality',
    '1.11': 'an inclusive view of the history and uses of chemistry',
    '1.12': 'sustainable development as part of studying chemistry; the SDGs',
    '1.13': 'employability: subject and wider attributes',
    '1.14': 'enterprise and entrepreneurship defined',
    '1.15': 'topics in enterprise education; the QAA guidance',
    '2.1': 'many course designs; theory and application combined',
    '2.2': 'routes in, foundation years and prior qualifications',
    '2.3': "honours and integrated master's degrees and their levels; standalone master's",
    '2.4': 'placements and study abroad; integrating credit-bearing placements',
    '2.5': 'a common core with later options',
    '2.6': 'degree apprenticeships follow this statement',
    '2.7': 'accessible learning and assessment by inclusive design and adjustment',
    '2.8': 'fully accessible curricula, pedagogy, assessment and practicals',
    '2.9': 'progression from defined to open-ended problems',
    '2.10': 'methods that build independence; strategies that support progression',
    '2.11': 'progression rules and the threshold for each level',
    '2.12': 'resits and exit awards; Scottish four-year honours',
    '2.13': 'modes of delivery, credit transfer and flexibility to change',
    '2.14': 'partnerships with colleges, overseas providers and industry',
    '2.15': 'monitoring and periodic review against external reference points',
    '2.16': 'external reviewers in periodic review',
    '2.17': 'external examiners and threshold standards',
    '2.18': 'several external examiners for the breadth of the subject',
    '2.19': 'continuous evaluation with students, graduates and employers',
    '2.20': 'accreditation by the Royal Society of Chemistry towards CChem',
    '3.1': 'each provider defines its own content',
    '3.2': 'the content as a foundation, developed later',
    '3.3': 'core chemistry content and what it lets graduates do',
    '3.4': 'optional specialist and supplementary content',
    '3.5': 'the wider characteristics of chemistry graduates',
    '3.6': 'making development opportunities explicit; support into work or study',
    '3.7': 'skills embedded in content; resilience through practical work',
    '3.8': "enabling content for honours graduates",
    '3.9': "further skills for integrated master's graduates",
    '3.10': 'the independent investigative project; originality at master\'s',
    '3.11': "supervision and greater ownership at master's",
    '3.12': 'industry and team projects; individual master\'s projects',
    '3.13': 'training that underpins the project',
    '3.14': 'typical share of credit for the project',
    '3.15': 'teaching methods left open but explicit, inclusive and reviewed',
    '3.16': 'student-centred, visual and practical teaching in many formats',
    '3.17': 'synchronous learning activities',
    '3.18': 'asynchronous materials and activities',
    '3.19': 'blended and multimodal activities',
    '3.20': 'responsive strategies; development for all teaching staff',
    '3.21': 'assessment aligned with outcomes and varied',
    '3.22': 'digital literacy, coding and varied assessment formats',
    '3.23': 'the kinds of evidence assessed',
    '3.24': 'assessment for subject and employability skills; the skills map',
    '3.25': "master's assessment: unfamiliar problems and research skills",
    '4.1': 'the standards as what an honours graduate has shown',
    '4.2': 'most exceed threshold; Annex D for the classes',
    '4.3': 'the two rungs defined: threshold and excellent',
    '4.4': 'the tables cover the main content; no checklist or weighting',
    '4.5': 'achievement across outcomes; compensation by algorithm',
    '4.6': 'reading the tables with sections 1 and 3; Table 1 for honours',
    '4.7': "master's build on Table 1; Table 2",
}
CTYPE = {'3.3': 'area', '3.4': 'area', '3.13': 'area',
         '3.15': 'practice', '3.16': 'practice', '3.17': 'practice', '3.18': 'practice', '3.19': 'practice', '3.20': 'practice',
         '3.21': 'practice', '3.22': 'practice', '3.23': 'practice', '3.24': 'practice', '3.25': 'practice', '3.10': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional reference points', kind='other: front matter, read for S1 and S2'),
    dict(number='section headings 1 to 4', heading='the four section heading lines', kind='other: heading lines'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for S7 and SB6'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Chemistry', kind='other: back matter, read for S8 (editions)'),
]

P = {}
def s(i, **k):
    P[i] = k

# ------------------------------------------------------------------ obliging paragraphs, section 1
s('1.2', type='expectation', rung='none', force='should', level='none', appliesTo='chemistry courses', addressee='provider',
  verbs=['providing', 'creating'], about='representative material and an inclusive setting', domain='none', award=[HON, MAS],
  para="The aims that follow should be read as part of giving every chemistry student relevant, representative material and a welcoming, inclusive setting where all feel valued and can come to enjoy the subject.",
  prac="Read the course aims through an inclusion lens: choose material that is relevant and representative for every student, and build a setting where all feel welcome and valued.",
  ben=NA_P,
  aaw=f"Treat this as a should-level framing of the course aims: relevant, representative material and an inclusive environment for every student, for honours and master's courses. Cite it as {CITE}, para 1.2. Do not present it as a student outcome or a legal duty; set it beside 1.10, 1.11 and 2.7 in this document.",
  aad="Raise this when a team reviews its curriculum or induction and asks whether the material speaks to all its students. Frame it for staff as a test applied to every aim, not a separate module. Ask: 'Whose work and examples appear in your first-year material, and who might not see themselves there?' Avoid presenting it to a student as their task.")
s('1.7', type='expectation', rung='none', force='should', level='none', appliesTo='chemistry courses', addressee='provider',
  verbs=['reflect'], about='breadth in content and methods', domain='none', award=[HON, MAS],
  para="Because chemistry is very broad, courses should show that breadth in what they cover and in how they teach, learn and assess; some courses cover the whole field, others let students specialise or combine chemistry with other subjects.",
  prac="Let the breadth of chemistry show in both the topics covered and the variety of teaching, learning and assessment methods, whether the course is broad, specialist, joint or combined.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation that courses reflect the breadth of chemistry in content and in methods. It applies to all chemistry courses, broad or specialist. Cite it as {CITE}, para 1.7. Do not claim it requires every course to cover the whole field; set it beside 2.1, 3.2 and 3.21 in this document.",
  aad="Raise this when a team designs a specialist, joint or combined chemistry course and asks how broad it must be. Put it to staff as breadth in methods as well as topics. Ask: 'Which parts of chemistry, and which kinds of assessment, does your course leave out, and is that a choice you can defend?' Avoid presenting it to a student as their duty.")
s('1.8', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='chemistry graduates; final-year students', addressee='learner',
  verbs=['work', 'solving'], about='safe, accurate laboratory work', domain='subject-skill', award=[HON, MAS],
  para="Practical work is essential to every chemistry course: all graduates will be competent and able to work safely and accurately in a laboratory, and by the final year students work precisely with little supervision, sorting out problems as they come; courses build this in a spiral, from detailed instructions to independence.",
  prac="Plan practical work as a spiral: detailed instructions and forgiving experiments early, then less support, so that final-year students work precisely with little supervision and every graduate is safe and accurate in the laboratory.",
  ben="By the end of your course you will be able to work safely and accurately in a laboratory, and in your final year you will work precisely with little supervision, solving problems as they come up.",
  aaw=f"Treat this as a will-level expectation that every chemistry graduate is competent at safe, accurate laboratory work, with final-year students working precisely under minimal supervision, for honours (FHEQ level 6) and integrated master's courses. Cite it as {CITE}, para 1.8. Do not claim it sets a professional licence or a fixed number of laboratory hours; set it beside 3.3.b2, 4.6.b3 and 4.6.b4 in this document and the FHEQ honours descriptor qaa/fheq-2024/4.15.b2.",
  aad="Raise this when a student asks how much practical work matters or why early labs are so tightly scripted, or when a team plans its laboratory programme. To a student, explain that support is reduced step by step until you can work alone; to staff, frame it as the spiral the course should build. Ask: 'Which experiment could you now run with no script, and where do you still need one?' Avoid suggesting that early mistakes in the laboratory count against them.")
s('1.11', **trim('1.11', 'Education for sustainable development'), type='requirement', rung='none', force='must', level='none', appliesTo='chemistry curricula and teaching', addressee='provider',
  verbs=['viewed', 'taught', 'recognise', 'acknowledge', 'evaluate'], about='an inclusive account of chemistry and its uses', domain='none', award=[HON, MAS],
  para="Though chemistry rests on objective observation, its history and its uses in society must be presented and taught inclusively; curricula should credit chemists of diverse backgrounds, accept that other cultures bring other insights, let learners explore topics that matter to them and encourage them to weigh both the good and harm that chemical discoveries can do.",
  prac="Teach the history and applications of chemistry inclusively as a must; as shoulds, credit chemists from diverse backgrounds, give learners room to follow topics tied to their own experience, and ask them to weigh benefits and harms of discoveries.",
  ben=NA_P,
  aaw=f"Treat this as a must-level duty to view and teach the history and applications of chemistry inclusively, with should-level expectations on curricula and learner choice. It applies to all chemistry courses. Cite it as {CITE}, para 1.11. Do not weaken the must or strengthen the shoulds, and do not present it as a student outcome; set it beside 1.2, 1.10 and 3.4.b1 in this document.",
  aad="Raise this when a team reviews whose discoveries its teaching names or plans a module on the history or impact of chemistry. Frame it for staff as a firm duty with shoulds attached. Ask: 'Which chemists from under-represented backgrounds appear in your course, and where do students judge the harms as well as the benefits of chemistry?' Avoid presenting it to students as their responsibility.")
s('1.12', **trim('1.12', 'Employability, enterprise and entrepreneurship'), type='expectation', rung='none', force='should', level='none', appliesTo='chemistry courses', addressee='provider',
  verbs=['inspire', 'engage'], about='sustainable development in chemistry courses', domain='none', award=[HON, MAS],
  para="Chemistry is central to solving problems, so courses should inspire chemists to take part in tackling personal, human and global challenges; topics may come from the UN Sustainable Development Goals, and ESD is part of studying chemistry, equipping graduates to devise new answers to complex challenges.",
  prac="Inspire students to engage with global challenges through chemistry; draw topics where useful from the SDGs, such as health, energy, clean water and the environment, and use the QAA and Advance HE ESD guidance.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation that chemistry courses inspire engagement with personal, human and global challenges, with the SDGs as an optional source of topics. Cite it as {CITE}, para 1.12. Do not present the SDGs as a mandatory checklist; set it beside 3.3.b3, 3.3.b13 and 4.6.b9 in this document and the ESD guidance std:doc:qaa-advancehe-esd-2021-guidance.",
  aad="Raise this when a team maps sustainability content or asks how to make it more than one module. Frame it for staff as inspiration through chemistry's own problems, such as clean energy or water. Ask: 'Where in the course do students use chemistry on a real sustainability problem?' Avoid reading the issuer's text on the SDGs aloud at length.")
s('1.13', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='chemistry courses and their graduates', addressee='both',
  verbs=['equip', 'prepare', 'enable'], about='employability: subject skills and wider attributes', domain='generic-skill', award=[HON, MAS],
  para="All chemistry courses should prepare students for life after graduation in a complex, changing world and for a useful contribution to society; graduates should have both the subject knowledge and professional skills for chemical careers and the wider attributes for careers elsewhere.",
  prac="Build both subject-specific professional skills and wider attributes into the course, so graduates can work in the chemical sciences or in other sectors; 3.8 lists the wider skills.",
  ben="Your course should prepare you for work in chemistry and beyond it, giving you both subject expertise and the wider skills employers in other sectors value.",
  aaw=f"Treat this as a should-level expectation with two sides: courses equip students for life after graduation, and graduates hold both subject and wider attributes (honours, FHEQ level 6). Cite it as {CITE}, para 1.13. Do not claim it guarantees employment; set it beside 3.5, 3.6 and the enabling skills 3.8.b1 to 3.8.b9 in this document and the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3.",
  aad="Raise this when a student asks what the degree prepares them for beyond the laboratory, or when a team reviews employability. To a student, put it as subject skills plus wider attributes that travel to other careers; to staff, as a course duty. Ask: 'Which of your skills would an employer outside chemistry value, and where did you build them?' Avoid promising particular jobs.")

# ------------------------------------------------------------------ section 2
s('2.1', type='expectation', rung='none', force='should', level='none', appliesTo='chemistry courses', addressee='provider',
  verbs=['include'], about='theory and application combined', domain='none', award=[HON, MAS],
  para="Chemistry courses across the UK are designed in many ways, by traditional branches, by synthesis, measurement and application, or around applied fields; whichever lead they take, all courses should include a suitable mix of fundamental theory and application.",
  prac="Whatever structure the course takes, branches or applications, make sure it combines fundamental theory and application in suitable proportion.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation that every chemistry course combines theory and application, whatever its structure. Cite it as {CITE}, para 2.1. Do not claim it prescribes the traditional branches or any one structure; set it beside 1.7 and 3.2 in this document.",
  aad="Raise this when a team chooses how to organise its course. Frame it for staff as freedom of structure with a fixed need for both theory and application. Ask: 'If your course leads with applications, where do students meet the underlying theory?' Avoid presenting it to students.")
s('2.3', type='expectation', rung='none', force='should', level='fheq:6', appliesTo="bachelor's degrees with honours in chemistry", addressee='provider',
  verbs=['provide', 'prepare'], about="what honours degrees provide; the integrated master's", domain='none', award=[HON, MAS],
  para="Undergraduates may take a bachelor's degree with honours (FHEQ 6; FQHEIS 10) or an integrated master's with honours (FHEQ 7; FQHEIS 11), each with its own outcomes; bachelor's degrees should give subject knowledge, understanding and skills plus wider transferable skills for many careers, while integrated master's degrees cover both sets of outcomes and go deeper.",
  prac="Give honours students subject knowledge, understanding and skills together with wider transferable skills; in an integrated master's, meet the honours outcomes and add the depth, specialist knowledge and project work of master's level.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation of what the honours degree provides, with a statement of the two undergraduate awards and their levels (FHEQ 6 and FQHEIS 10; FHEQ 7 and FQHEIS 11). Cite it as {CITE}, para 2.3. Do not claim standalone MSc or MRes courses carry the honours outcomes; set it beside 3.8, 3.9 and 4.7 in this document and std:doc:qaa-fheq-2024-framework, Table 1.",
  aad="Raise this when a student weighs a bachelor's against an integrated master's, or a team designs both. For staff, frame it as two awards with distinct outcomes at two levels. Ask: 'What does your integrated master's add beyond the honours outcomes, and where?' Avoid treating it as a student standard.")
s('2.4', type='expectation', rung='none', force='should', level='none', appliesTo='credit-bearing placements', addressee='provider',
  verbs=['integrated', 'relate', 'use'], about='integrating placements into the course', domain='none', award=[HON, MAS],
  para="Courses may include placements or study abroad, often in the third or fourth year and of varied length and credit; credit-bearing placements should be built into the course so students can link their experience and skills to their academic study.",
  prac="Where a placement carries credit, integrate it with the rest of the course so students connect what they do on placement with their academic work.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation that credit-bearing placements are integrated with academic study. It applies to bachelor's and integrated master's courses that offer placements. Cite it as {CITE}, para 2.4. Do not claim every course must offer a placement; set it beside 2.13 and 3.19 in this document.",
  aad="Raise this when a team designs or reviews a placement year. Frame it for staff as a link students should be able to draw between placement and study. Ask: 'How do students bring what they learn on placement back into their final-year work?' Avoid presenting it to a student as a requirement.")
s('2.6', **trim('2.6', 'Accessibility'), type='expectation', rung='none', force='should', level='none', appliesTo='degree apprenticeships in chemistry', addressee='provider',
  verbs=['follow'], about='degree apprenticeships follow this statement', domain='none', award=[HON, MAS],
  para="The academic part of chemistry degree apprenticeships should follow this statement; apprenticeships in general are described in QAA's characteristics statement on higher education in apprenticeships.",
  prac="Design the academic component of a chemistry degree apprenticeship to the same outcomes as other chemistry degrees, reading the apprenticeships characteristics statement alongside.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation that the academic component of chemistry degree apprenticeships follows this statement. Cite it as {CITE}, para 2.6. Do not claim it covers the work-based or end-point parts of an apprenticeship; set it beside the Characteristics Statement for Higher Education in Apprenticeships (not yet ingested) and 2.14 in this document.",
  aad="Raise this when a team builds a degree apprenticeship in chemistry. Frame it for staff as the same academic standards in a different delivery model. Ask: 'Where does your apprenticeship meet the outcomes of Table 1?' Avoid presenting it to apprentices as an extra duty.")
s('2.7', type='requirement', rung='none', force='must', level='none', appliesTo='chemistry courses', addressee='provider',
  verbs=['ensure', 'offered'], about='equally accessible learning and assessment', domain='none', award=[HON, MAS],
  para="Equal opportunity means access for people with differing needs and removing needless barriers; chemistry courses must make learning and assessment equally accessible to all, by inclusive design where possible and reasonable adjustment where needed, and learning and assessment should be varied to reflect the subject and widen access.",
  prac="As a must, design learning and assessment inclusively so they are equally accessible, adding reasonable individual adjustments where needed; as a should, vary the experiences to reflect the subject and widen access.",
  ben=NA_P,
  aaw=f"Treat this as a must-level duty on chemistry courses: learning and assessment equally accessible to all, by inclusive design and reasonable adjustment, with a should on varied experiences. Cite it as {CITE}, para 2.7. Do not weaken the must or present it as a student outcome; set it beside 2.8, 2.13 and 3.15 in this document.",
  aad="Raise this when a team plans assessment or laboratory work, or a disabled student asks what to expect. Frame it for staff as a duty met first by design, then by adjustment; to a student, only as what they can expect. Ask: 'Which assessment in your course would a student with a visual impairment find hardest, and what would you redesign?' Avoid placing the duty on the student.")
s('2.8', **trim('2.8', 'Progression'), type='requirement', rung='none', force='must', level='none', appliesTo='chemistry course teams', addressee='provider',
  verbs=['pay', 'ensuring', 'designed', 'supported'], about='fully accessible curricula and practicals', domain='none', award=[HON, MAS],
  para="Course teams must take care that curricula, teaching, assessments and practical work are built for full accessibility, and that every learner gets support to develop the verbal, spatial, numerical and other skills chemical problems call for.",
  prac="Check every element, curriculum, pedagogy, assessment and practicals, for full accessibility, and support all learners in the verbal, spatial and numerical skills chemistry needs.",
  ben=NA_P,
  aaw=f"Treat this as a must-level duty on course teams: fully accessible design of curricula, pedagogy, assessment and practicals, and support for all learners in the skills chemical problems need. Cite it as {CITE}, para 2.8. Do not present it as a student outcome; set it beside 2.7 and 3.15 in this document.",
  aad="Raise this with a team reviewing its practical classes or spatial-reasoning tasks. Frame it for staff as a design duty covering practicals as well as lectures. Ask: 'How would a student who cannot stand at a bench complete your laboratory course?' Avoid presenting it to students as theirs to solve.")
s('2.9', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='chemistry courses and their students', addressee='both',
  verbs=['designed', 'promote', 'solve', 'applying'], about='progression from defined to open problems', domain='none', award=[HON, MAS],
  para="Courses should be designed to foster academic and personal growth: students first use simple concepts on well-defined problems, then link harder concepts to tackle ill-defined, open problems, and on graduating will have the range of knowledge, experience and skills for a career in chemistry or elsewhere.",
  prac="Sequence the course so students move from simple concepts and well-defined problems to complex concepts and open-ended ones, ending with the competence a chemistry career needs.",
  ben="Your course should take you from using simple ideas on clear-cut problems to connecting harder ideas on open-ended ones, so that you finish ready for a career in chemistry or another field.",
  aaw=f"Treat this as a should-level expectation on course design, with a will-level account of where students arrive, for honours (FHEQ level 6) and integrated master's courses. Cite it as {CITE}, para 2.9. Do not claim it sets the outcomes for each year; set it beside 2.10, 2.11 and 4.6.b2 in this document and the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1.",
  aad="Raise this when a student finds later problems much less defined than earlier ones, or a team plans the sequence of problem types. To a student, explain that the shift to open problems is intended; to staff, frame it as a progression to design. Ask: 'Can you name a problem you solved this year that had no single right answer?' Avoid suggesting struggle with open problems means failure.")
s('2.10.b1', type='expectation', rung='none', force='should', level='none', appliesTo='progression strategies', addressee='provider',
  verbs=['recognise'], about='diverse prior experience and transition', domain='none', award=[HON, MAS],
  para="Strategies for progression should take account of how varied students' prior experience is and how hard transition can be.",
  prac="Plan induction and early teaching around the range of prior experience in the cohort and the difficulty of moving into higher education.",
  ben=NA_P,
  aaw=f"Treat this as one of four should-level strategies that support progression from guided study to independence. Cite it as {CITE}, para 2.10, first item. Do not present it as a student outcome; set it beside 2.10.b2 to 2.10.b4 and 2.2 in this document.",
  aad="Raise this when a team plans induction or first-year support. Frame it for staff as planning for varied starting points. Ask: 'What do you know about the routes your students took into the course, and how does first year allow for them?' Avoid presenting it to students.")
s('2.10.b2', type='expectation', rung='none', force='should', level='none', appliesTo='progression strategies', addressee='provider',
  verbs=['allow', 'achieve', 'realise'], about='every student reaching their potential', domain='none', award=[HON, MAS],
  para="Strategies for progression should let every student reach their potential and ambitions, whatever their background or reasons for studying chemistry.",
  prac="Check that progression arrangements let students of any background or motivation reach their potential.",
  ben=NA_P,
  aaw=f"Treat this as a should-level strategy for progression with an inclusion aim. Cite it as {CITE}, para 2.10, second item. Do not present it as a student outcome; set it beside 2.10.b1, 1.2 and 2.7 in this document.",
  aad="Raise this when a team studies who progresses and who does not. Frame it for staff as a question of equal chances. Ask: 'Do progression rates in your course differ by background, and what would explain it?' Avoid presenting it to students.")
s('2.10.b3', type='expectation', rung='none', force='should', level='none', appliesTo='progression strategies', addressee='provider',
  verbs=['support'], about='academic and personal development', domain='none', award=[HON, MAS],
  para="Strategies for progression should support personal and academic growth as well as learning.",
  prac="Give personal development a place beside academic learning in the support that moves students through the course.",
  ben=NA_P,
  aaw=f"Treat this as a should-level strategy for progression. Cite it as {CITE}, para 2.10, third item. Do not present it as a student outcome; set it beside 2.9 and 3.6 in this document.",
  aad="Raise this when a team reviews personal tutoring or skills support. Frame it for staff as development beyond content. Ask: 'Where does your course support personal development, not only knowledge?' Avoid presenting it to students.")
s('2.10.b4', type='expectation', rung='none', force='should', level='none', appliesTo='progression strategies', addressee='provider',
  verbs=['matched'], about='strategies tied to each level\'s outcomes', domain='none', award=[HON, MAS],
  para="Strategies for progression should fit the stated learning outcomes or competencies for each level.",
  prac="Align progression strategies with the documented outcomes or competencies at each level of the course.",
  ben=NA_P,
  aaw=f"Treat this as a should-level strategy for progression. Cite it as {CITE}, para 2.10, fourth item. Do not claim it sets level outcomes itself; set it beside 2.11 in this document and the FHEQ level descriptors qaa/fheq-2024/4.10, 4.12 and 4.15.",
  aad="Raise this when a team writes level outcomes. Frame it for staff as alignment between support and outcomes. Ask: 'Does your second-year support match what level 5 asks of students?' Avoid presenting it to students.")
s('2.11', type='requirement', rung='none', force='must', level='none', appliesTo="institutions' progression regulations", addressee='provider',
  verbs=['require', 'demonstrate'], about='the threshold for each level as the condition of progression', domain='none', award=[HON, MAS],
  para="Students progress between years by meeting their institution's rules, which must require them to show they have met the overall threshold for the level; this will usually mean completing and gaining credit for all learning and assessment, practicals included, and more may be asked for specialist titles, placements or an integrated master's.",
  prac="Write progression rules that require students to show the overall threshold for each level, usually with credit for every element including practical courses; set any extra criteria for specialist titles, placements or the integrated master's.",
  ben=NA_P,
  aaw=f"Treat this as a must-level duty on institutions: progression rules require evidence that the overall threshold for the level has been met. Cite it as {CITE}, para 2.11. Do not claim it sets the threshold for each year's content; set it beside 2.10.b4 and 4.6.b1 in this document and the FHEQ level descriptors.",
  aad="Raise this when a team writes or reviews progression regulations, or a student asks why a failed practical blocks progression. To staff, frame it as a firm duty; to a student, explain only that each level has a threshold. Ask: 'Does your regulation let a student progress without passing the practical course?' Avoid presenting the duty as the student's.")
s('2.13', **trim('2.13', 'Partnership'), type='expectation', rung='none', force='should', level='none', appliesTo='chemistry courses', addressee='provider',
  verbs=['respond', 'anticipate', 'take', 'make'], about='flexibility to change and reasonable adjustments', domain='none', award=[HON, MAS],
  para="Courses differ in mode, from full-time to part-time and distance study, abroad and in industry; they need to be flexible enough to meet and foresee changes in the subject and in graduates' and employers' needs, and should take account of learners' needs, making reasonable adjustments as required.",
  prac="Keep the course flexible to change in the subject and in employers' needs, and make reasonable adjustments for learners as required.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation that courses take account of learners' needs with reasonable adjustments, alongside an unmodalled call for flexibility. Cite it as {CITE}, para 2.13. Do not claim it requires part-time or distance routes; set it beside 2.7 and 2.8 in this document.",
  aad="Raise this when a team reviews modes of study or responds to a change in the field. Frame it for staff as responsiveness to the subject and to learners. Ask: 'When did your course last change because of a shift in chemistry or in employers' needs?' Avoid presenting it to students.")
s('2.16', type='expectation', rung='none', force='will', level='none', appliesTo='higher education providers in periodic review', addressee='provider',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award=[HON, MAS],
  para="Externality is essential to UK quality assurance; providers will use external reviewers in periodic review to get an outside view of planned changes and to make sure threshold standards are met and content suits the subject.",
  prac="Bring external reviewers into periodic review to test changes, confirm the threshold standards and check that content fits chemistry.",
  ben=NA_P,
  aaw=f"Treat this as a will-level statement of provider practice: external reviewers in periodic review, partly to confirm threshold standards. Cite it as {CITE}, para 2.16. Do not confuse it with external examining (2.17); set it beside 2.15, 2.17 and 2.19 in this document.",
  aad="Raise this with a team preparing for periodic review. Frame it for staff as the outside check on the threshold column of Table 1. Ask: 'Which external reviewer will see your threshold evidence, and what will they compare it with?' Avoid presenting it to students.")
s('2.19', type='expectation', rung='none', force='should', level='none', appliesTo='programme and course teams', addressee='provider',
  verbs=['conduct', 'integrated', 'involved'], about='continuous evaluation with stakeholders', domain='none', award=[HON, MAS],
  para="Programme and course teams should evaluate regularly with independent evaluators; student data, feedback and voice should be combined with expert review, external examiners' included, to keep curricula current, engaging and accessible, and students, graduates, employers and professional bodies should help design and deliver improvements.",
  prac="Run regular evaluation that combines performance data, student feedback and expert review, and involve students, graduates, employers and professional bodies in improving the course.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation on teams to monitor and evaluate continuously and to involve stakeholders in enhancement. Cite it as {CITE}, para 2.19. Do not present it as a student outcome; set it beside 2.15 to 2.17 in this document.",
  aad="Raise this when a team plans an annual review or a curriculum change. Frame it for staff as evaluation with students and employers at the table. Ask: 'Which change to your course in the past year came from student or employer input?' Avoid presenting it to students as a duty.")

# ------------------------------------------------------------------ section 3, paragraphs
s('3.2', **trim('3.2', 'Subject knowledge and understanding'), type='expectation', rung='none', force='should', level='none', appliesTo='undergraduate chemistry curricula', addressee='provider',
  verbs=['regarded', 'developed'], about='the content as a foundation to build on', domain='none', award=[HON, MAS],
  para="No undergraduate course can cover every part of chemistry equally; the content that follows should be treated as the foundation of a good curriculum, with parts developed further later on in line with staff research and teaching interests.",
  prac="Treat the 3.3 content as the foundation, then develop parts of it further in later years according to your staff's specialisms.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation on how to read the core content of 3.3: as foundational, to be developed further. Cite it as {CITE}, para 3.2. Do not claim the 3.3 list is a complete syllabus; set it beside 3.3.b1 to 3.3.b14 and 4.4 in this document.",
  aad="Raise this when a team asks whether 3.3 is a syllabus to cover in full. Frame it for staff as a foundation they build on in their own direction. Ask: 'Which parts of the core does your course take furthest, and why?' Avoid presenting it to students.")
s('3.5', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='chemistry graduates', addressee='learner',
  verbs=['develop', 'support', 'refute'], about='logical, analytical use of evidence', domain='generic-skill', award=[HON, MAS],
  para="Chemistry is a creative discipline and its graduates tend to be innovative, resilient, self-motivated team players; they should be logical and analytical and confident in using evidence to build, back or rebut arguments, and courses let them develop these wider traits.",
  prac="Give students repeated practice in building and testing arguments from evidence, alongside the creativity, resilience and teamwork the course develops.",
  ben="You should become logical and analytical, and confident in using evidence to build, support or knock down an argument.",
  aaw=f"Treat this as a should-level expectation of chemistry graduates' reasoning, set within a plain-present account of their wider character, for honours (FHEQ level 6) and integrated master's courses. Cite it as {CITE}, para 3.5. Do not turn the plain-present traits into requirements; set it beside 3.8.b2, 3.9.b2 in this document and the FHEQ honours descriptor qaa/fheq-2024/4.15.b7.",
  aad="Raise this when a student asks what makes a good chemistry argument or how to handle criticism of their ideas. To a student, put it as using evidence to support or challenge a claim; to staff, as a habit to build across modules. Ask: 'What evidence would make you change your mind about your last conclusion?' Avoid presenting the other traits in the paragraph as tests a student must pass.")
s('3.6', type='expectation', rung='none', force='should', level='none', appliesTo='chemistry courses', addressee='provider',
  verbs=['made', 'reflect', 'given'], about='making development explicit; support into work or study', domain='none', award=[HON, MAS],
  para="Students should be shown clearly the chances for academic and personal growth the course offers, so they can reflect on strengths and next steps and improve their employability, and should get support, in or beyond the curriculum, in applying for and moving on to further study or work.",
  prac="Make development opportunities visible and give structured support for applications and interviews, in the curriculum or through extracurricular activity.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation on courses: make development explicit and support transition to further study or employment. Cite it as {CITE}, para 3.6. Do not present it as a student outcome; set it beside 1.13 and 3.24 in this document.",
  aad="Raise this when a team reviews careers support or personal tutoring. Frame it for staff as making the hidden development visible. Ask: 'Where does a student in your course learn to describe their skills to an employer?' Avoid presenting it to students as their obligation.")
s('3.10', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='honours and master\'s students in chemistry', addressee='learner',
  verbs=['engage', 'include'], about='the independent investigative project', domain='subject-skill', award=[HON, MAS],
  para="Every honours student is expected to carry out some independent, open-ended investigation through a project or research assignment, usually in the final year; at master's level the project is expected to show some originality, and the presentation and critical evaluation in its written report should match the quality of a peer-reviewed publication.",
  prac="Give every honours student an open-ended investigative project, usually in the final year; at master's level expect originality, and judge the report's quality against that of a peer-reviewed paper.",
  ben="You will undertake an open-ended investigation of your own, usually in your final year. At master's level, your project should show some original thinking, and your written report should be as good as a published, peer-reviewed paper in quality, though not in format.",
  aaw=f"Treat this as an expectation that every honours student undertakes independent investigative work, with a should-level standard for the master's report equal in quality to a peer-reviewed publication. It holds for honours (FHEQ level 6) and master's (FHEQ level 7). Cite it as {CITE}, para 3.10. Do not claim the format of a paper is required, and record the obliging words outside the five ('expected to') as written; set it beside 4.6.b8, 4.7.b5 and 3.13 in this document and the FHEQ descriptors qaa/fheq-2024/4.15.b6 and 4.17.b3.",
  aad="Raise this when a student plans a final-year or master's project, or a team sets project assessment. To a student, explain that the project is the place to investigate on your own, and that at master's level the report is judged as if for publication. Ask: 'What open question will your project try to answer, and what would make the answer new?' Avoid suggesting that an honours project needs originality.")
s('3.15', type='requirement', rung='none', force='must', level='none', appliesTo='teaching and learning in chemistry courses', addressee='provider',
  verbs=['made', 'paid', 'support'], about='explicit, reviewed, inclusive teaching methods', domain='none', award=[HON, MAS],
  para="The statement does not prescribe teaching methods; whatever methods are used must be explained to students and reviewed regularly inside and outside the institution, and the design should make sure they support the outcomes and are inclusive and accessible.",
  prac="Tell students how and why you teach as you do, review methods internally and externally, and design them to support the outcomes and to be inclusive and accessible.",
  ben=NA_P,
  aaw=f"Treat this as a must-level duty to make teaching methods explicit to students and subject them to regular review, with a should on alignment and inclusion. Cite it as {CITE}, para 3.15. Do not claim it prescribes any method; set it beside 2.7, 3.16 and 3.20 in this document.",
  aad="Raise this when a team writes a module handbook or plans a review of teaching. Frame it for staff as a duty to explain and review methods. Ask: 'Could a student in your module say why it is taught the way it is?' Avoid presenting it to students as their task.")
s('3.20', **trim('3.20', 'Assessment'), type='expectation', rung='none', force='should', level='none', appliesTo='teaching strategies and teaching staff', addressee='provider',
  verbs=['contribute', 'have'], about='responsive strategies; development for all teaching staff', domain='none', award=[HON, MAS],
  para="Teaching strategies should change with technology and with research on pedagogy, so everyone who teaches or assesses, technical demonstrators and visiting lecturers as well as academics, should have access to subject and educational development.",
  prac="Keep teaching responsive to new technology and pedagogic research, and give every member of teaching staff, demonstrators and visiting lecturers included, access to subject and educational development.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation on providers: responsive strategies and professional development for all who teach or assess. Cite it as {CITE}, para 3.20. Do not present it as a student outcome; where staff development is the subject, set it beside std:doc:advancehe-psf-dimensions-2023-framework and 3.15 in this document.",
  aad="Raise this when a team plans staff development or reviews how demonstrators are trained. Frame it for staff as access for everyone who teaches, not only academics. Ask: 'What development have your technical demonstrators had in the past year?' Avoid presenting it to students.")
s('3.21', type='expectation', rung='none', force='should', level='none', appliesTo='assessment in chemistry courses', addressee='provider',
  verbs=['aligns', 'reflect'], about='assessment aligned and varied', domain='none', award=[HON, MAS],
  para="Assessment is tied to the learning outcomes and to the knowledge and skills the course builds, and the range of assessment used should reflect that.",
  prac="Align assessment with the outcomes and vary it enough to cover the knowledge, abilities and professional skills the course develops.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation that the diversity of assessment reflects the outcomes and skills a course develops. Cite it as {CITE}, para 3.21. Do not present it as a student outcome; set it beside 3.22 to 3.24 in this document.",
  aad="Raise this when a team reviews its assessment pattern. Frame it for staff as a check that variety matches the range of outcomes. Ask: 'Which of your outcomes is assessed only by examination, and would another format test it better?' Avoid presenting it to students.")
s('3.22', type='expectation', rung='none', force='should', level='none', appliesTo='chemistry courses and their assessment', addressee='provider',
  verbs=['provided', 'engage', 'demonstrate'], about='digital literacy, coding and varied formats', domain='none', award=[HON, MAS],
  para="A digital world asks students to be ready for the future through IT literacy and coding, and students should be given chances to engage with them; assessments are strongly encouraged to use a range of formats so all students can show their learning, though some tasks still call for hand-drawn formulae and schemes.",
  prac="Give students opportunities to build IT literacy and coding, and use a wide range of assessment formats, digital and handwritten, so every student can show what they have learned.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation that students get opportunities to develop IT literacy and coding, with a strong encouragement towards varied assessment formats. Cite it as {CITE}, para 3.22. Do not claim coding is a required outcome; set it beside 3.8.b4, 4.6.b12 and 3.21 in this document.",
  aad="Raise this when a team plans where coding sits in the course or reviews assessment formats. Frame it for staff as opportunity and variety. Ask: 'Where in your course does a student first write code, and is it assessed?' Avoid presenting it to students as a duty.")
s('3.24', type='expectation', rung='none', force='should', level='none', appliesTo='assessment in chemistry courses', addressee='provider',
  verbs=['support', 'enhance'], about='assessment that builds subject and employability skills', domain='none', award=[HON, MAS],
  para="Assessment drives learning and, where it can, should build both the skills and concepts a chemistry career needs and wider skills for employability; a map links skills such as communication, teamwork, numeracy and IT literacy to the assessment types that call on them.",
  prac="Use assessment to build both chemistry-specific and wider employability skills; the skills map shows which assessment types exercise which skills.",
  ben=NA_P,
  aaw=f"Treat this as a should-level expectation that assessment supports both career-specific and wider skills, with an illustrative skills map. Cite it as {CITE}, para 3.24. Do not present the map as a required pattern; set it beside 3.23, 1.13 and 3.6 in this document.",
  aad="Raise this when a team audits which skills its assessments exercise. Frame it for staff as using the map as a prompt. Ask: 'Which of the mapped skills, such as teamwork, does none of your assessments require?' Avoid presenting it to students.")

# ------------------------------------------------------------------ section 4, paragraphs
s('4.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='honours degree-awarding providers', addressee='provider',
  verbs=['perform', 'refer'], about='Annex D for achievement above threshold', domain='none', award=HON,
  para="Most students will do much better than the minimum threshold; each provider decides what evidence shows this and should refer to Annex D, the common descriptions of the four honours classes.",
  prac="When deciding what evidence shows achievement above threshold, use Annex D's descriptions of first, upper second, lower second and third.",
  ben=NA_P,
  aaw=f"Treat this as a should-level pointer for providers to Annex D when judging achievement above threshold in the honours degree (FHEQ level 6; FQHEIS level 10). Cite it as {CITE}, para 4.2. Do not claim the statement sets its own class bands; set it beside 4.3, the rungs 4.6.b1 to 4.6.b14 and their excellent forms, and qaa/fheq-2024/annex-d (SL6 of std:doc:qaa-fheq-2024-framework).",
  aad="Raise this when a team aligns its marking with degree classes. Frame it for staff as Annex D filling the space between the two rungs. Ask: 'How do your criteria for a 2:1 differ from those for a first, and do they draw on Annex D?' Avoid presenting it to a student as their duty.")
s('4.6', find='4.6 The standards in these tables should be read in conjunction with Sections 1 and 3, and paragraphs 4.1 to 4.5.',
  type='expectation', rung='none', force='should', level='none', appliesTo='readers of the tables: course teams and examiners', addressee='provider',
  verbs=['read'], about='reading the tables with their context', domain='none', award=[HON, MAS],
  para="The standards in the two tables should be read together with sections 1 and 3 and with the introductory paragraphs of section 4.",
  prac="Read Tables 1 and 2 with the context, content and enabling skills of sections 1 and 3 and the framing of 4.1 to 4.5, not as standalone lists.",
  ben=NA_P,
  aaw=f"Treat this as a should-level instruction on how to read Tables 1 and 2. Cite it as {CITE}, para 4.6. Do not quote a table row without its context; set it beside 4.4 (no checklist, no weighting) and the outcome lists 3.3 and 3.8 in this document.",
  aad="Raise this when a team or examiner lifts a table row out of context. Frame it for staff as reading the tables with sections 1 and 3. Ask: 'Which paragraph of section 3 explains the row you are using?' Avoid presenting it to students.")
s('4.7', find="4.7 There are a range of master's courses (integrated and standalone), but all students should have attained the thresholds in Table 1. Master's courses further develop transferable skills and depth of knowledge, in particular, mastery of one or more specialist areas or applications of chemistry and independence in project-based work.",
  type='expectation', rung='none', force='should', level='fheq:7', appliesTo="master's students in chemistry, integrated and standalone", addressee='learner',
  verbs=['attained', 'develop'], about="Table 1 thresholds as the base for master's", domain='none', award=MAS,
  para="Whatever kind of master's course, integrated or standalone, all students should have reached the Table 1 thresholds; master's courses then deepen knowledge and transferable skills, above all mastery of a specialism and independence in project work.",
  prac="Check that master's students hold the Table 1 thresholds, then build specialist mastery, transferable skills and independence in projects on top.",
  ben="On a master's course you should already meet the minimum honours outcomes; the course then deepens your knowledge in a specialism and makes you more independent in project work.",
  aaw=f"Treat this as a should-level expectation that every master's student in chemistry, integrated or standalone, has attained the Table 1 thresholds, with Table 2 adding master's outcomes (FHEQ level 7; FQHEIS level 11). Cite it as {CITE}, para 4.7. Do not claim it makes Table 1's excellent column the master's standard; set it beside 4.6.b1 to 4.6.b14, 4.7.b1 to 4.7.b5 in this document, the FHEQ master's descriptor qaa/fheq-2024/4.17.b1 and spine:7.",
  aad="Raise this when a master's applicant or student asks what they are expected to know already, or a team admits students to a standalone MSc. To a student, explain that the honours minimum is the starting point; to staff, frame it as an entry check. Ask: 'Which Table 1 outcome do you feel least secure in, and how will you close that gap?' Avoid treating the excellent column as an entry requirement.")

# ------------------------------------------------------------------ outcome lists: 3.3 (core content), 3.4 (optional), 3.8 (honours), 3.9 (integrated master's)
K, U, SS, GS = 'knowledge', 'understanding', 'subject-skill', 'generic-skill'
def you(t):
    return t.replace('{their}', 'your')
def them(t):
    return t.replace('{their}', 'their')

# n: (domain, verbs, about, X, fheq, table row, question)
CORE = {
 1: (K, ['describe', 'discuss'], 'key chemical concepts', "describe and discuss the key concepts across the whole of chemistry with confidence, accuracy and detail, in the right terms", '4.15.b1', '4.6.b1', "Which key concept could you explain in detail without notes, and which would you struggle with?"),
 2: (SS, ['describe', 'document', 'enact'], 'safe working practices', "describe, record and follow safe practice, managing toxicity, stability and reactivity through knowledge-led risk assessment and practical work", '4.15.b2', '4.6.b3', "How did you decide the controls in your last risk assessment?"),
 3: (SS, ['consider', 'apply', 'deploy'], 'waste reduction and safe disposal', "cut waste in practical work and use disposal methods that protect people in the laboratory and the environment", '4.15.b2', '4.6.b3', "What did you do to reduce or safely dispose of waste in your last experiment?"),
 4: (U, ['explain', 'rationalise', 'apply'], 'thermodynamics, kinetics, quantum mechanics and spectroscopy', "explain and justify how thermodynamics (classical and statistical), kinetics, quantum mechanics and spectroscopy work, and use them on problems in theory and in the laboratory", '4.15.b3.1', '4.6.b2', "Can you use thermodynamics or kinetics to explain why a reaction you ran behaved as it did?"),
 5: (SS, ['predict', 'use', 'suggest', 'design'], 'predicting reactions and planning synthesis', "predict likely products, bond-forming reactions, mechanisms, stereochemistry and reactivity, and use those predictions to propose routes to target compounds and to design experiments that test them", '4.15.b2', '4.6.b4', "For a target compound, could you propose a route and say which step is most likely to fail?"),
 6: (SS, ['explain', 'design', 'deploy'], 'purification, isolation and characterisation', "explain, plan and use ways to purify, isolate and characterise substances, guided by the physical and chemical properties and periodic trends of the elements and their compounds", '4.15.b2', '4.6.b4', "Why would you choose one purification method over another for a given product?"),
 7: (U, ['discuss', 'explain', 'apply'], 'periodic trends', "discuss trends across the periodic table, explain what they mean for how elements react and behave and for their physical properties, and use this on problems in theory and practice", '4.15.b1', '4.6.b2', "Which periodic trend best explains a reaction you have studied, and how?"),
 8: (K, ['describe'], 'atomic and molecular orbitals', "describe atomic and molecular orbitals and how they help explain structure, bonding and the paths reactions take", '4.15.b1', '4.6.b1', "Could you sketch the orbitals involved in a bond you know well and explain what they show?"),
 9: (SS, ['design', 'develop', 'carry'], 'sample preparation, measurement and analysis', "plan, develop and carry out qualitative and quantitative preparation and purification of samples, measurement, metrology and analysis, attending to accuracy, precision, traceability, complex matrices and sample size", '4.15.b2', '4.6.b5', "How did you check the accuracy and precision of your last quantitative analysis?"),
 10: (SS, ['explain', 'undertake', 'communicate'], 'analytical techniques and their limits', "explain the theory behind classical and instrumental analytical techniques and their limits, carry out analyses and measurements and report them in the right terms and notation", '4.15.b2', '4.6.b5', "What are the limits of an instrumental technique you have used, and how did they affect your result?"),
 11: (SS, ['use'], 'computational methods', "use computational methods and software to understand chemical structure, bonding and reactivity better", '4.15.b2', '4.6.b6', "What has a computational model shown you about a molecule that you could not easily see otherwise?"),
 12: (K, ['gain'], 'inorganic and organic substances and their uses', "know many organic and inorganic compounds, substances and materials and what each is for", '4.15.b1', '4.6.b1', "Can you name a material you have studied and explain what makes it fit for its use?"),
 13: (U, ['appreciate'], "chemistry's part in innovation and future challenges", "recognise how chemistry has fed the innovations of the modern world and how chemists can help meet present and future challenges", '4.15.b7', '4.6.b9', "Which modern innovation depends on chemistry, and which challenge could chemists help with next?"),
 14: (U, ['recognise', 'operate'], 'chemistry and other subjects', "see how chemistry relates to and meets other subjects, so as to work well in multidisciplinary settings", '4.15.b1', '4.6.b10', "When have you used chemistry alongside another subject, and what did each bring?"),
}
for n, (dom, verbs, about, X, fheq, row, qn) in CORE.items():
    s('3.3.b%d' % n, type='outcome', rung='none', force='should', level='fheq:6', appliesTo="undergraduates in chemistry (honours and integrated master's)", addressee='learner',
      verbs=verbs, about=about, domain=dom, award=[HON, MAS],
      para=f"Undergraduate courses should include chemistry content that lets graduates {them(X)}.",
      prac=f"Cover this in the core chemistry content so every undergraduate can {them(X)}; it is foundational content to build on later (3.2).",
      ben=f"By the end of your course you should be able to {you(X)}.",
      aaw=(f"Treat this as a should-level outcome of the core chemistry content: graduates able to work with {about}, for undergraduate courses (honours at FHEQ level 6 and FQHEIS level 10; integrated master's, which include these outcomes). "
           f"Cite it as {CITE}, para 3.3, item {n}. "
           f"Do not present it as a regulatory requirement or a complete syllabus. "
           f"Set it beside the graded row {row} and {row}.excellent in Table 1, the FHEQ honours descriptor qaa/fheq-2024/{fheq} and spine:6."),
      aad=(f"Raise this when a student asks what core chemistry they need on {about}, or when a team maps modules against the core content. "
           f"To a student, put it plainly as something you should be able to do by the end; to staff, as content the curriculum should cover. "
           f"Ask: '{qn}' "
           f"Avoid reading the list aloud or treating it as a checklist of equal weight (4.4)."))

OPT = {
 1: (U, ['consider', 'discuss'], "the culture and history of chemistry and its social impact", "think about and discuss where and how chemistry grew as a culture and what it has done to society", "How has chemistry changed the society you live in, for better and worse?"),
 2: (K, ['specialise'], 'specialising in a branch of chemistry', "focus on one or more specialist branches, for example sustainable (green) chemistry, cheminformatics or the teaching of chemistry", "Which branch of chemistry would you most like to specialise in, and why?"),
 3: (U, ['integrate', 'situate', 'relate'], 'chemistry within other subjects and vocations', "place {their} chemistry within another honours subject, such as biology, physics or the environmental and pharmaceutical sciences, or link it to vocational fields such as business and law", "How does your chemistry connect with the other subject or field you are studying?"),
}
for n, (dom, verbs, about, X, qn) in OPT.items():
    i = '3.4.b%d' % n
    extra = trim(i, 'Underpinning and enabling knowledge and skills') if n == 3 else {}
    s(i, **extra, type='outcome', rung='none', force='may', level='fheq:6', appliesTo="undergraduates on courses with specialist or supplementary content", addressee='learner',
      verbs=verbs, about=about, domain=dom, award=[HON, MAS],
      para=f"Undergraduate courses may add specialist or supplementary content that lets graduates {them(X)}.",
      prac=f"Optionally, add specialist or supplementary content so graduates can {them(X)}; it is a choice for the course, not a requirement.",
      ben=f"Your course may also give you the chance to {you(X)}.",
      aaw=(f"Treat this as an optional outcome (may) of specialist or supplementary content on {about}, for undergraduate courses at FHEQ level 6. "
           f"Cite it as {CITE}, para 3.4, item {n}. "
           f"Do not present it as a requirement of every chemistry course. "
           f"Set it beside the core outcomes 3.3.b1 to 3.3.b14 in this document and spine:6."),
      aad=(f"Raise this when a student asks about options, specialisms or joint study, or a team considers adding specialist content. "
           f"To a student, describe it as a possible opportunity, not a must; to staff, as an option the statement allows. "
           f"Ask: '{qn}' "
           f"Avoid implying that a course lacking it falls short."))

ENABLE = {
 1: (['navigate', 'utilise', 'collate'], 'digital information tools', "use digital tools to find, gather and organise information and data", '4.15.b5', 'cognitive/r1', '4.6.b7', "Which database or search tool do you use to find chemical information, and how do you organise what you find?"),
 2: (['select', 'examine', 'critique'], 'critical use of the literature', "choose, examine and criticise research papers and other sources so as to keep {their} knowledge current, learn further and help solve set problems", '4.15.b5', 'cognitive/r1', '4.6.b7', "How do you judge whether a paper you found is reliable enough to use?"),
 3: (['deploy', 'solve', 'evaluate'], 'mathematics for chemistry', "apply mathematical ideas and tools, such as rearranging equations, calculus and graphical and statistical methods, to chemical problems and data", '4.15.b3.1', 'transferable/r1', '4.6.b11', "Which mathematical tool do you rely on most in chemistry, and where does it still trip you up?"),
 4: (['choose', 'deploy'], 'data analysis, coding and scripting', "pick and apply methods for analysing and handling data, which may include coding or scripting, to present, communicate and solve problems", '4.15.b3.1', 'practical/r4', '4.6.b12', "Have you written code or a script to handle data, and what did it let you do?"),
 5: (['collaborate', 'work'], 'teamwork', "work well with others in a group, contributing constructively and adaptably to shared outputs", '4.15.b9.1', 'transferable/r2', '4.6.b13', "What did you bring to the last team task, and how did you adapt when plans changed?"),
 6: (['communicate', 'selecting'], 'communication for audience and purpose', "communicate well, choosing content, medium and method to suit the audience, purpose and topic", '4.15.b8', 'transferable/r1', '4.6.b14', "How would you present the same result to a lab group and to a school class?"),
 7: (['comprehend', 'discriminate', 'recognising'], 'kinds of published information and peer review', "tell apart different kinds of published information and understand how peer review shapes the scientific literature", '4.15.b5', 'cognitive/r1', '4.6.b7', "What is the difference between a peer-reviewed article, a preprint and a press release?"),
 8: (['realise'], 'intellectual property and academic integrity', "understand what {their} own and others' intellectual property is and is worth, and why academic integrity matters", '4.15.b9.1', 'professional/r2', 'none', "When would you need to credit someone else's idea in your own work?"),
 9: (['act', 'modelling', 'promotes'], 'professional, ethical conduct', "behave professionally, mindful of legal, ethical and social duties, setting an example that reflects well on chemistry and chemists", '4.15.b9.2', 'professional/r2', 'none', "Which ethical or legal question have you met in chemistry, and how did you handle it?"),
}
for n, (verbs, about, X, fheq, ann, row, qn) in ENABLE.items():
    rowtxt = f"the graded row {row} and {row}.excellent in Table 1, " if row != 'none' else ("Table 1's last row, which repeats it without rung cells (Part E), " if n == 9 else '')
    s('3.8.b%d' % n, type='outcome', rung='none', force='should', level='fheq:6', appliesTo='honours graduates in chemistry', addressee='learner',
      verbs=verbs, about=about, domain=GS, award=HON,
      para=f"Honours courses should include enabling content so graduates can {them(X)}.",
      prac=f"Build enabling content into the honours course so every graduate can {them(X)}; it may sit inside the chemistry content (3.7).",
      ben=f"By the end of your honours degree you should be able to {you(X)}.",
      aaw=(f"Treat this as a should-level generic skill for honours graduates in chemistry, on {about}, at FHEQ level 6 (FQHEIS level 10). "
           f"Cite it as {CITE}, para 3.8, item {n}. "
           f"Do not present it as a regulatory requirement or as a master's outcome. "
           f"Set it beside {rowtxt}the FHEQ honours descriptor qaa/fheq-2024/{fheq}, the Annex D third-class description qaa/fheq-2024/annex-d/{ann}/{'3rd-1st' if ann.startswith('professional') else '3rd'} and spine:6."),
      aad=(f"Raise this when a student asks which wider skills the degree builds on {about}, or when a team checks where those skills are taught and assessed. "
           f"To a student, put it plainly in the second person; to staff, as enabling content the course should include. "
           f"Ask: '{qn}' "
           f"Avoid reading the issuer's list aloud or treating every item as a separate module."))

FURTHER = {
 1: (['develop', 'solving'], 'new approaches to advanced problems', "devise new ways to tackle advanced problems, at times without full information", '4.17.b5', '4.7.b1', "Describe a problem you tackled without all the information: how did you proceed?"),
 2: (['develop', 'articulate', 'synthesising', 'provide'], 'persuasive argument', "build persuasive arguments and state {their} position, drawing knowledge and skills together into a convincing case for {their} ideas", '4.17.b4.2', 'none', "What is the strongest objection to your current research idea, and how would you answer it?"),
 3: (['interrogate', 'integrate', 'design', 'develop'], 'literature to design methods', "question and combine varied scientific literature and other information to design methods of investigation and analysis, also beyond {their} specialism", '4.17.b4.1', '4.7.b2', "Which sources outside your specialism shaped the method you are using?"),
 4: (['develop', 'solving'], 'strategies for problems without a single answer', "build general strategies for problems with more than one answer, including finding the extra information needed", '4.17.b5', 'none', "When a problem has several possible answers, how do you decide what information you still need?"),
 5: (['plan', 'manage'], 'planning own and group work', "plan and manage {their} own work and a group's work well", '4.17.b8.1', '4.7.b3', "How do you plan your project week by week, and how do you share work in a group?"),
 6: (['demonstrate'], 'readiness for research or doctoral study', "show readiness for research, a doctorate or employment at a similar level", '4.17.b7', 'none', "What would you need to show a doctoral supervisor or research employer that you are ready?"),
}
for n, (verbs, about, X, fheq, row, qn) in FURTHER.items():
    i = '3.9.b%d' % n
    extra = trim(i, 'Project and dissertation') if n == 6 else {}
    rowtxt = f"the Table 2 outcome {row} and {row}.excellent, " if row != 'none' else ''
    s(i, **extra, type='outcome', rung='none', force='should', level='fheq:7', appliesTo="integrated master's graduates in chemistry", addressee='learner',
      verbs=verbs, about=about, domain=GS, award=MAS,
      para=f"Integrated master's courses should build on the honours skills so graduates can {them(X)}.",
      prac=f"Building on the honours enabling skills, make sure integrated master's graduates can {them(X)}.",
      ben=f"By the end of your integrated master's you should be able to {you(X)}.",
      aaw=(f"Treat this as a should-level generic skill for integrated master's graduates in chemistry, on {about}, at FHEQ level 7 (FQHEIS level 11). "
           f"Cite it as {CITE}, para 3.9, item {n}. "
           f"Do not apply it to the bachelor's degree with honours or present it as regulation. "
           f"Set it beside {rowtxt}the honours skills 3.8.b1 to 3.8.b9, the FHEQ master's descriptor qaa/fheq-2024/{fheq} and spine:7."),
      aad=(f"Raise this when an integrated master's student asks how the final year differs from honours, or a team plans master's-level teaching on {about}. "
           f"To a student, put it as the extra step beyond honours, in plain words; to staff, as an outcome the master's year should secure. "
           f"Ask: '{qn}' "
           f"Avoid holding a bachelor's student to it."))

# ------------------------------------------------------------------ Table 1: honours rungs (lead-in in the table caption, after 4.6)
# k: (domain, name, related, T text, E text, verbs T, verbs E, Xt, Xe, fheq, annex row, strand, question T, question E)
T1 = {
 1: (K, 'core chemical concepts', '3.3.b1',
     "Recall basic knowledge and theories in chemistry based on the course contents and use these in the discussion or explanation of familiar concepts with appropriate terminology.",
     "Use and apply in-depth knowledge of concepts and theories in chemistry to discuss and predict outcomes covering most essential aspects of the course and show evidence of enquiry beyond this.",
     ['Recall', 'use'], ['Use', 'apply', 'discuss', 'predict', 'show'],
     "remember the basic knowledge and theory taught on the course and draw on it, with the right terms, to discuss or explain familiar ideas",
     "apply deep knowledge of chemical concepts and theory to discuss and predict outcomes across most core parts of the course, and show enquiry that goes further",
     '4.15.b1', 'knowledge/r1', 'strand:knowledge',
     "Could you explain a familiar idea from your course, such as a reaction type, using the correct terms?",
     "Can you predict what would happen in a case the course did not cover, and justify it?"),
 2: (SS, 'solving chemical problems', '3.3.b4',
     "Adequately define and solve routine problems, applying a range of methods and concepts taught within the course.",
     "Devise and evaluate solutions to solve both routine and unfamiliar problems using a range of methods.",
     ['define', 'solve', 'applying'], ['Devise', 'evaluate', 'solve', 'using'],
     "set out and work through routine problems adequately, using a variety of the methods and ideas taught",
     "devise and judge solutions to problems, familiar or new, drawing on several methods",
     '4.15.b3.1', 'cognitive/r3', 'strand:thinking',
     "Take a routine problem from your course: can you state it clearly and solve it without a worked example?",
     "Faced with a problem unlike any you have practised, how would you choose and test an approach?"),
 3: (SS, 'safe practice and risk assessment', '3.3.b2',
     "Produce and follow risk assessments f or completing practical work in a safe and reliable manner with significant reliance on guidance.",
     "Produce and follow risk assessments f or completing practical work in a safe and reliable manner with limited reliance on guidance.",
     ['Produce', 'follow'], ['Produce', 'follow'],
     "write and work to risk assessments so practical work is done safely and reliably, leaning heavily on guidance",
     "write and work to risk assessments so practical work is done safely and reliably, with little need for guidance",
     '4.15.b2', 'practical/r2', 'strand:application',
     "When did you last write a risk assessment, and what guidance did you need?",
     "Could you assess the hazards of a new procedure on your own and justify your controls?"),
 4: (SS, 'synthesis, purification and characterisation', '3.3.b6',
     "Suggest and attempt synthesis, purification, isolation and characterisation strategies accurately with a degree of independence and justify choice/use of technique.",
     "Design, evaluate and complete synthesis, purification, isolation and characterisation strategies accurately with a high degree of autonomy and efficiency.",
     ['Suggest', 'attempt', 'justify'], ['Design', 'evaluate', 'complete'],
     "propose and try out accurate approaches to making, purifying, isolating and characterising compounds with some independence, and give reasons for the techniques chosen",
     "design, assess and carry through accurate approaches to making, purifying, isolating and characterising compounds, working efficiently and largely on {their} own",
     '4.15.b2', 'practical/r1', 'strand:application',
     "For a compound you made recently, why did you choose that purification method?",
     "Could you plan a full route from synthesis to characterisation for a new target and defend each step?"),
 5: (SS, 'chemical measurement and analysis', '3.3.b9',
     "Suggest, carry out and report qualitative and quantitative sample preparation and purification, chemical measurement, metrology and appropriate analysis accurately with a degree of independence.",
     "Design, optimise, carry out and report qualitative and quantitative sample preparation and purification, chemical measurement, metrology and appropriate analysis accurately with a high degree of autonomy and efficiency.",
     ['Suggest', 'carry', 'report'], ['Design', 'optimise', 'carry', 'report'],
     "propose, perform and write up accurate sample preparation, measurement and analysis, qualitative and quantitative, with some independence",
     "design, refine, perform and write up accurate sample preparation, measurement and analysis, efficiently and with a high level of autonomy",
     '4.15.b2', 'practical/r4', 'strand:application',
     "Which analytical method have you run from preparation to report, and how confident are you in its accuracy?",
     "How would you improve the precision of a measurement you have made, and how would you show it?"),
 6: (SS, 'computational chemistry', '3.3.b11',
     "Use computational techniques and tools to investigate familiar chemical concepts covered in course content",
     "Select and use appropriate computational techniques and tools to investigate complex chemical concepts and evaluate and",
     ['Use', 'investigate'], ['Select', 'use', 'investigate', 'evaluate'],
     "use computational methods and software to explore familiar chemical ideas from the course, reporting what is found in the right terms",
     "choose and use suitable computational methods and software to explore complex chemical ideas, judging and reporting the results in the right terms",
     '4.15.b2', 'practical/r1', 'strand:application',
     "Which computational tool have you used to look at a structure or reaction, and what did it show you?",
     "How would you decide which computational method suits a complex system, and how would you check the result?"),
 7: (GS, 'using the chemical literature', '3.8.b2',
     "Identify and select appropriate resources and sources of chemical information.",
     "Identify and select appropriate resources and sources of chemical information with a high degree of independence.",
     ['Identify', 'select'], ['Identify', 'select'],
     "track down and choose fitting sources of chemical information",
     "track down and choose fitting sources of chemical information, largely unaided",
     '4.15.b5', 'cognitive/r1', 'strand:application',
     "Where would you look first for reliable data on a compound, and why there?",
     "How do you find what has been published on a topic you have not studied before?"),
 8: (SS, 'the independent project', '3.10',
     "Complete an open-ended investigative project/ research-based assignment.",
     "Complete an open-ended investigative project/ research-based assignment with a high level of independence.",
     ['Complete'], ['Complete'],
     "carry an open-ended investigation or research-based assignment through to completion",
     "carry an open-ended investigation or research-based assignment through to completion, working very independently",
     '4.15.b6', 'transferable/r3', 'strand:autonomy',
     "What stage of your project needs the most help from your supervisor?",
     "Which decisions in your project did you take on your own, and how did you justify them?"),
 9: (U, 'chemistry and global challenges', '3.3.b13',
     "Identify and discuss application of chemistry in solving current and future challenges in the world.",
     "Explain and suggest ways in which chemistry can contribute to solving current and future challenges in the world.",
     ['Identify', 'discuss'], ['Explain', 'suggest'],
     "name and discuss how chemistry is applied to present and future problems facing the world",
     "explain how chemistry can help with present and future world problems and propose ways it might do so",
     '4.15.b7', 'cognitive/r2', 'strand:thinking',
     "Which global problem do you know chemistry is helping with, and how?",
     "Could you propose a way chemistry might help with a challenge such as clean energy, and weigh its limits?"),
 10: (U, 'chemistry and other subjects', '3.3.b14',
     "Identify and explain relationships between chemistry and other subjects as relevant to course content.",
     "Evaluate and explain contribution of chemistry to multidisciplinary issues.",
     ['Identify', 'explain'], ['Evaluate', 'explain'],
     "point out and explain links between chemistry and other subjects met on the course",
     "assess and explain what chemistry brings to issues that cross several disciplines",
     '4.15.b1', 'knowledge/r2', 'strand:knowledge',
     "Where has your chemistry met another subject, such as biology or physics, on your course?",
     "For a problem that crosses disciplines, what does chemistry add that the others cannot?"),
 11: (GS, 'mathematics in chemistry', '3.8.b3',
     "Select and use mathematical concepts, processes and tools to solve familiar chemical problems and evaluate chemical data, usually accurately.",
     "Consistently and accurately select and use mathematical concepts, processes and tools to solve familiar chemical problems and evaluate chemical data.",
     ['Select', 'use', 'solve', 'evaluate'], ['select', 'use', 'solve', 'evaluate'],
     "pick and apply mathematical ideas and tools to familiar chemistry problems and to judging data, accurately most of the time",
     "pick and apply mathematical ideas and tools to familiar chemistry problems and to judging data, with consistent accuracy",
     '4.15.b3.1', 'transferable/r1', 'strand:application',
     "Which calculation in your course do you still find hardest to get right?",
     "How do you check that your data analysis is correct before you rely on it?"),
 12: (GS, 'data analysis methods', '3.8.b4',
     "Select and correctly use methods for data analysis and manipulation with some guidance.",
     "Select, evaluate and correctly use methods for data analysis and manipulation in complex and unpredictable situations.",
     ['Select', 'use'], ['Select', 'evaluate', 'use'],
     "choose and apply data-handling and analysis methods correctly, with some guidance",
     "choose, assess and apply data-handling and analysis methods correctly in complex, unpredictable situations",
     '4.15.b3.1', 'practical/r4', 'strand:thinking',
     "Which data analysis method do you use most, and when do you still need help with it?",
     "When data are messy or incomplete, how do you decide which method to trust?"),
 13: (GS, 'teamwork', '3.8.b5',
     "Provide useful contributions to team outputs.",
     "Provide clear and valuable contributions to team outputs exhibiting teamwork and/or leadership skills.",
     ['Provide'], ['Provide', 'exhibiting'],
     "make useful contributions to what a team produces",
     "make clear, valuable contributions to what a team produces, showing teamwork, leadership or both",
     '4.15.b9.1', 'transferable/r2', 'strand:autonomy',
     "What did you contribute to the last group task, and how did the team use it?",
     "When have you helped a team work better, or led part of it?"),
 14: (GS, 'communication', '3.8.b6',
     "Communicate information, ideas, problems and solutions verbally, electronically and in writing, with clear expression and style.",
     "Communicate information, ideas, problems and solutions to an accomplished level verbally, electronically and in writing, in an accurate, fluent and sophisticated style, at a level consistently appropriate for audience.",
     ['Communicate'], ['Communicate'],
     "get information, ideas, problems and solutions across clearly in speech, in writing and electronically",
     "get information, ideas, problems and solutions across to a high standard in speech, writing and electronic forms, accurately, fluently and with sophistication, always pitched to the audience",
     '4.15.b8', 'transferable/r1', 'strand:communication',
     "Who was the audience for your last presentation, and how did you adapt it for them?",
     "Could you explain the same result to a specialist and to a member of the public?"),
}
GRADE = {}
OUTCOMES = []
T1START = _NORM.find('Table 1: Benchmark standards')
for k, (dom, name, rel, tt, te, vt, ve, xt, xe, fheq, ann, strand, qt, qe) in T1.items():
    it, ie = '4.6.b%d' % k, '4.6.b%d.excellent' % k
    base = dict(level='fheq:6', addressee='learner', domain=dom, award=HON, appliesTo='honours graduates in chemistry')
    s(it, find=tt, after=T1START, type='threshold', rung='threshold', force='threshold', verbs=vt, about=name, **base,
      para=f"At the threshold for the honours degree, the graduate can {them(xt)}.",
      prac=f"Threshold: make sure every honours graduate can at least {them(xt)}; teaching and assessment need to evidence this floor.",
      ben=f"As a minimum, by the end of your honours degree you can {you(xt)}.",
      aaw=(f"Treat this as a threshold standard, the least every honours graduate in chemistry shows on {name} (FHEQ level 6; FQHEIS level 10). "
           f"Cite it as {CITE}, Table 1, row {k}, threshold column. "
           f"Do not present it as regulation, a mark scheme or the master's standard. "
           f"Set it beside its excellent form {ie}, the related outcome {rel}, the FHEQ honours descriptor qaa/fheq-2024/{fheq} and the Annex D third-class description qaa/fheq-2024/annex-d/{ann}/3rd ({strand}, spine:6)."),
      aad=(f"Raise this when a student asks what they must at least manage on {name}, or when a team checks a module against the floor. "
           f"To a student, say it in plain second-person words; to staff, frame it as the minimum the course has to evidence. "
           f"Ask: '{qt}' "
           f"Do not read the table aloud, and never offer the excellent column as the pass standard."))
    s(ie, find=te, after=T1START, type='excellent', rung='excellent', force='describes', verbs=ve, about=name, **base,
      para=f"At the excellent standard, the level of a first-class degree, the graduate can {them(xe)}.",
      prac=f"Excellent: for first-class work, look for evidence that the student can {them(xe)}; set tasks that leave room to show it.",
      ben=f"For excellent, first-class work, you would {you(xe)}.",
      aaw=(f"Treat this as the excellent standard on {name}: a description of first-class performance in the honours degree (FHEQ level 6), not a requirement for the award. "
           f"Cite it as {CITE}, Table 1, row {k}, excellent column. "
           f"Do not present it as the minimum or as a master's standard. "
           f"Set it beside its threshold form {it}, the FHEQ honours descriptor qaa/fheq-2024/{fheq} and the Annex D first-class description qaa/fheq-2024/annex-d/{ann}/1st."),
      aad=(f"Raise this with a student who meets the minimum on {name} and asks how to reach the top band, or with a team designing stretch tasks. "
           f"Present it as a step above the threshold, in plain words to a student and as a design aim to staff. "
           f"Ask: '{qe}' "
           f"Avoid implying that every student has to reach it."))
    GRADE[ie] = it + '|stated'
    OUTCOMES.append(dict(outcome=name, threshold=it, typical='none', excellent=ie, basis='stated', domain=dom, award=HON))

# ------------------------------------------------------------------ Table 2: master's (one threshold cell and one excellent cell, read as applying to every outcome)
T2 = {
 1: (U, 'applying advanced understanding to complex problems',
     "Develop, integrate, synthesise and apply the systematic and broad understanding of relevant and state-of-the-art chemical concepts to solve more complex problems.",
     ['Develop', 'integrate', 'synthesise', 'apply', 'solve'],
     "build up, combine and apply a broad, systematic grasp of current chemical concepts to harder problems", '4.17.b1', '3.9.b1',
     "Which complex problem have you tackled by combining ideas from different areas of chemistry?"),
 2: (GS, 'using the literature to design methods',
     "Interrogate and integrate diverse sources of scientific literature alongside other information sources, in order to design and develop methods for investigation and analysis, including in areas at the forefront of knowledge and outside their current specialist knowledge.",
     ['Interrogate', 'integrate', 'design', 'develop'],
     "question and combine varied scientific literature and other information to design methods of investigation, at the forefront and beyond {their} specialism", '4.17.b4.1', '3.9.b3',
     "Which recent papers shaped the method you are using, and what did you take from each?"),
 3: (SS, 'project planning',
     "Project planning, including, as appropriate, evaluation of ethics, hazards and environmental effects and appreciation of costs.",
     [], "plan a project, weighing ethics, hazards, environmental effects and costs where relevant", '4.17.b6', '3.9.b5',
     "What ethical, safety, environmental and cost questions did you weigh in planning your project?"),
 4: (SS, 'advanced experimental skills',
     "Development of advanced experimental and investigative skills as appropriate for project.",
     [], "develop the advanced practical and investigative skills a project calls for", '4.17.b2', '3.13',
     "Which advanced technique did your project need, and how did you learn it?"),
 5: (GS, 'discussing a research project',
     "Discussion of the background, context, methods, results and potential impact of a significant research project.",
     [], "discuss the background, context, methods, results and likely impact of a substantial research project", '4.17.b3', '3.10',
     "How would you explain why your project's results matter, and to whom?"),
}
T2START = _NORM.find("Table 2: Benchmark standards")
for k, (dom, name, text, verbs, X, fheq, rel, qn) in T2.items():
    it, ie = '4.7.b%d' % k, '4.7.b%d.excellent' % k
    base = dict(find=text, after=T2START, level='fheq:7', addressee='learner', domain=dom, award=MAS, verbs=verbs, about=name,
                appliesTo="master's graduates in chemistry, integrated and standalone")
    s(it, type='threshold', rung='threshold', force='threshold', **base,
      para=f"At the threshold for a master's degree, beyond Table 1, the graduate can {them(X)}, with substantial support and guidance.",
      prac=f"Threshold: every master's graduate can {them(X)}, though with a good deal of support and guidance from staff.",
      ben=f"As a minimum on a master's course you can {you(X)}, with plenty of support and guidance.",
      aaw=(f"Treat this as a master's threshold standard on {name}: reached with considerable support (FHEQ level 7; FQHEIS level 11), in addition to the honours thresholds. "
           f"Cite it as {CITE}, Table 2, row {k}, threshold column. "
           f"Do not apply it to the honours degree or use Annex D for it, since Annex D covers honours classes only. "
           f"Set it beside its excellent form {ie}, the related outcome {rel}, the FHEQ master's descriptor qaa/fheq-2024/{fheq} and spine:7."),
      aad=(f"Raise this when a master's student asks what the minimum is on {name}, or a team sets master's assessment. "
           f"To a student, say that support and guidance are expected at the minimum; to staff, frame it as the floor for the award. "
           f"Ask: '{qn}' "
           f"Do not present the excellent column's independence as the minimum."))
    s(ie, type='excellent', rung='excellent', force='describes', **base,
      para=f"At the excellent standard for a master's degree, the graduate can {them(X)} largely independently and autonomously.",
      prac=f"Excellent: look for master's students who can {them(X)} on their own initiative, needing little direction.",
      ben=f"For excellent work on a master's course, you would {you(X)} largely on your own initiative.",
      aaw=(f"Treat this as the excellent standard for master's graduates on {name}: the same outcome reached with a high degree of independence (FHEQ level 7), not a requirement for the award. "
           f"Cite it as {CITE}, Table 2, row {k}, excellent column. "
           f"Do not present it as the minimum or as a doctoral standard. "
           f"Set it beside its threshold form {it}, the FHEQ master's descriptor qaa/fheq-2024/4.17.b6 on self-direction and spine:7."),
      aad=(f"Raise this with a master's student aiming high on {name}, or a team designing work that rewards independence. "
           f"Put it as doing the same work with little direction, in plain words to a student and as a design aim to staff. "
           f"Ask: 'Which parts of this could you now do without asking your supervisor?' "
           f"Avoid implying that needing guidance means failing."))
    GRADE[ie] = it + ('|stated' if k == 1 else '')
    OUTCOMES.append(dict(outcome=name, threshold=it, typical='none', excellent=ie, basis='stated' if k == 1 else 'inferred', domain=dom, award=MAS))

# ------------------------------------------------------------------ themes, levels, relations
TH = {'1.2': 'theme:edi', '1.11': 'theme:edi', '1.12': 'theme:esd', '1.13': 'theme:enterprise', '2.7': 'theme:accessibility',
      '2.8': 'theme:accessibility', '2.10.b2': 'theme:edi', '3.6': 'theme:enterprise', '3.24': 'theme:enterprise', '3.15': 'theme:accessibility'}

S5 = dict(
    levels=[dict(id='fheq:6', role='cites', locator='D1, 2.3; 4.2'),
            dict(id='fqheis:10', role='cites', locator='D1, 2.3; 4.2'),
            dict(id='fheq:7', role='cites', locator="D1, 2.3 (integrated master's); Table 2 and 4.7 (level inferred for standalone master's)"),
            dict(id='fqheis:11', role='cites', locator="D1, 2.3 (integrated master's)"),
            dict(id='spine:6', role='refers', locator='std:ref:uk-framework R2 and R8 (inferred: Part E)'),
            dict(id='spine:7', role='refers', locator='std:ref:uk-framework R2 and R8 (inferred: Part E)')],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.3: "FHEQ Level 6; FQHEIS Level 10"; 4.2, the title of Annex D)'),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis="stated (D1, 2.3: integrated master's, \"FHEQ Level 7; FQHEIS Level 11\")"),
                dict(**{'from': 'fheq:6'}, to='spine:6', relation='sameStep', basis='inferred from std:ref:uk-framework R2 (Part E)'),
                dict(**{'from': 'fheq:7'}, to='spine:7', relation='sameStep', basis='inferred from std:ref:uk-framework R2 (Part E)')])

EDI_P = ['1.2', '1.10', '1.11', '2.7', '2.10', '3.5', '3.15', '3.22']
ACC_P = ['2.7', '2.8', '2.13', '2.19', '3.15', '3.16']
ESD_P = ['1.1', '1.3', '1.12', '1.15', '3.3', '3.4', '3.13', '4.7']
ENT_P = ['1.13', '1.14', '1.15', '3.5', '3.6', '3.24']
S6 = [dict(id='theme:edi', role='carries', carriedIn=EDI_P), dict(id='theme:accessibility', role='carries', carriedIn=ACC_P),
      dict(id='theme:esd', role='carries', carriedIn=ESD_P), dict(id='theme:enterprise', role='carries', carriedIn=ENT_P)]

S7 = [
    dict(rel='supersedes', target='std:doc:qaa-chemistry-2019-benchmarks (not yet ingested)', note='the fourth edition (2019), named in the advisory group list; key changes listed in the front matter'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the degree classification descriptions for honours (4.2); cited as the 2019 Annex D in the reference list, now in the 2024 Frameworks'),
    dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='Education for Sustainable Development guidance (1.12)'),
    dict(rel='refersTo', target='std:doc:qaa-enterprise-2018-guidance', note='Enterprise and Entrepreneurship Education guidance (1.15)'),
    dict(rel='refersTo', target='QAA (2019) Characteristics Statement: Higher Education in Apprenticeships (not yet ingested)', note='2.6'),
    dict(rel='refersTo', target='United Nations, Sustainable Development Goals', note='1.12'),
    dict(rel='refersTo', target='Royal Society of Chemistry accreditation criteria for Chartered Chemist (not yet ingested)', note='2.20'),
    dict(rel='refersTo', target='HEA (2016) Framework for embedding employability in higher education (not yet ingested)', note='reference list only'),
    dict(rel='refersTo', target='QAA Quality Code Advice and Guidance; QAA Glossary (not ingested)', note='front matter'),
]

SB1 = [
    'Chemistry is the central science, describing, explaining and changing the material world, with large effects on society and a key part in sustainable development and global challenges (D1, 1.1).',
    'A very broad discipline, organised in many ways: the traditional inorganic, organic, physical and analytical branches; synthesis, measurement and application; or applied fields such as biological, computational, environmental, materials or medicinal chemistry (D1, 1.7; 2.1).',
    'Hands-on practical work is essential, built up in a spiral from scripted experiments to independent, precise work by the final year (D1, 1.8).',
    'Theory is underpinned by mathematical, spatial, information, planning, communication and problem-solving skills; the subject has a strong visual and practical side (D1, 1.9; 3.16).',
    'An inherently creative, multidisciplinary subject whose graduates combine subject expertise with wider attributes valued by employers in and beyond science (D1, 1.3; 3.5).',
    "Two undergraduate routes, the bachelor's with honours and the integrated master's (MChem, MSci), plus standalone MSc and MRes courses; accreditation by the Royal Society of Chemistry towards Chartered Chemist (D1, 2.3; 2.20).",
]
SB2 = [
    dict(theme='theme:edi', inThisSubject='relevant, representative material; an inclusive account of the history and uses of chemistry crediting diverse chemists; learner choice of topics tied to their lives; progression that lets all reach their potential (D1, 1.2; 1.10; 1.11; 2.10; 3.5)',
         statements=['1.2', '1.11', '2.10.b2']),
    dict(theme='theme:accessibility', inThisSubject='inclusive design and reasonable adjustment for learning, assessment and practical work, support for verbal, spatial and numerical skills, recorded and simulcast sessions (D1, 2.7; 2.8; 2.13; 3.15; 3.16)',
         statements=['2.7', '2.8', '2.13', '3.15']),
    dict(theme='theme:esd', inThisSubject="chemistry as a toolkit for the SDGs, from health to clean energy and water; waste reduction and safe disposal; green and sustainable chemistry as a specialism; environmental effects weighed in project planning (D1, 1.1; 1.12; 3.3; 3.4; 3.13; Table 2)",
         statements=['1.12', '3.3.b3', '3.4.b2', '4.7.b3', '4.7.b3.excellent']),
    dict(theme='theme:enterprise', inThisSubject='employability through subject and wider skills, enterprise as creativity and problem-solving central to chemistry, enterprise education topics such as business plans and intellectual property, assessment that builds employability (D1, 1.13 to 1.15; 3.5; 3.6; 3.24)',
         statements=['1.13', '3.6', '3.24', '3.8.b8']),
]
SB3 = dict(
    areas=[dict(component='3.3', gloss='core content: concepts, safe practice and waste, physical chemistry, synthesis and reactivity, purification, periodic trends, orbitals, measurement and analysis, computation, substances and materials, chemistry in innovation and with other subjects'),
           dict(component='3.4', gloss='optional content: culture and history of chemistry, specialist branches, chemistry within other subjects and vocations'),
           dict(component='3.13', gloss='project training: advanced experimental skills, literature, planning, communication, the research community, impact')],
    practices=[dict(component='3.10', kind='learning', gloss='an independent open-ended project, usually in the final year; originality at master\'s'),
               dict(component='3.15', kind='teaching', gloss='methods left open, explained to students, reviewed, inclusive and accessible'),
               dict(component='3.16', kind='teaching', gloss='student-centred, visual and practical; remote, face-to-face and recorded sessions; pre-sessional work'),
               dict(component='3.17', kind='teaching', gloss='synchronous: lectures, problem classes, labs, computer workshops, case studies, peer learning, presentations, fieldwork'),
               dict(component='3.18', kind='learning', gloss='asynchronous: texts, digital media, recordings, simulations, virtual experiments, practice tests, pre-lab exercises'),
               dict(component='3.19', kind='learning', gloss='blended: team projects, placements, reflective portfolios, research projects'),
               dict(component='3.20', kind='teaching', gloss='responsive strategies and development for all teaching staff'),
               dict(component='3.21', kind='assessment', gloss='assessment aligned with outcomes and varied'),
               dict(component='3.22', kind='assessment', gloss='IT literacy and coding; digital and handwritten formats'),
               dict(component='3.23', kind='assessment', gloss='sixteen kinds of evidence, from invigilated exams to practical skills assessed on yield and precision'),
               dict(component='3.24', kind='assessment', gloss='assessment building subject and employability skills, with a skills-by-assessment map'),
               dict(component='3.25', kind='assessment', gloss="master's: unfamiliar problems and the full range of research skills")])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.6', award=HON, items=14),
           dict(rung='excellent', leadIn='4.6', award=HON, items=14),
           dict(rung='threshold', leadIn='4.7', award=MAS, items=5),
           dict(rung='excellent', leadIn='4.7', award=MAS, items=5)],
    rungBases=("4.3 defines two rungs, threshold (the minimum for an honours degree) and excellent (the level for a first); no typical rung, Annex D "
               "covering the classes between (4.2). Table 1, after 4.6 (caption: on graduating with honours, graduates should be able to), gives 15 "
               "benchmark standards, 14 with a threshold cell and an excellent cell of their own text, recorded on their own spans; the first column "
               "names the outcome. Table 2, in 4.7, adds five master's outcomes with one threshold cell (significant support and guidance) and one "
               "excellent cell (high independence and autonomy), read as applying to all five; each outcome is recorded at both rungs on its span."),
    outcomeLists=[dict(leadIn='3.3', gloss="core chemistry content for all undergraduates", items=14, award=[HON, MAS]),
                  dict(leadIn='3.4', gloss='optional specialist and supplementary content (may)', items=3, award=[HON, MAS]),
                  dict(leadIn='3.8', gloss='enabling content for honours graduates', items=9, award=[HON]),
                  dict(leadIn='3.9', gloss="further skills for integrated master's graduates", items=6, award=[MAS])],
    outcomes=OUTCOMES)
SB4A_FULL = []
SB5 = [dict(body='Royal Society of Chemistry',
            says="may accredit chemistry courses; bachelor's and multidisciplinary courses are usually accredited as partly meeting the academic criteria for Chartered Chemist (CChem) and integrated master's as fully meeting them, through site visits and desk review (D1, 2.20)",
            requirements='not yet ingested: listed in Part E'),
       dict(body='professional bodies, unnamed',
            says='should be involved with students, graduates and employers in enhancing courses; multidisciplinary courses may be accredited by more than one (D1, 2.19; 2.20)',
            requirements='not yet ingested: no body named (Part E)')]
SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=EDI_P, statements=SB2[0]['statements']),
            dict(id='theme:accessibility', named='Accessibility', carriedIn=ACC_P, statements=SB2[1]['statements']),
            dict(id='theme:esd', named='Education for sustainable development', carriedIn=ESD_P, statements=SB2[2]['statements']),
            dict(id='theme:enterprise', named='Employability, enterprise and entrepreneurship (front matter: employability, entrepreneurship and enterprise education)', carriedIn=ENT_P, statements=SB2[3]['statements'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.3', '4.2']),
                dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.3', '4.2'])],
    bodies=[dict(body='Royal Society of Chemistry', citedIn=['2.20']),
            dict(body='professional bodies, unnamed', citedIn=['2.19', '2.20'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'],
             role='common descriptions of the four honours classes, for evidence of achievement above threshold'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='the QAA and Advance HE guidance Education for Sustainable Development', citedIn=['1.12'], role='further information on ESD'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers', citedIn=['1.15'], role='further information on enterprise education'),
        dict(document='not yet ingested: listed in Part E', named='the Characteristics Statement for Higher Education in Apprenticeships', citedIn=['2.6'], role='general characteristics of apprenticeships'),
    ])

B1 = [
    dict(slug='threshold-standard', definition='the least needed to gain an honours degree in the subject, shown by an acceptable level of ability and skill (D1, 4.3)',
         beneficiaryDefinition='the minimum you need to reach to be awarded an honours degree', scopeNote='one of the two rungs of Tables 1 and 2', category='unknown', practices=['education']),
    dict(slug='excellent-standard', definition='the level needed for a first-class degree, shown by consistently advanced knowledge, understanding and skill (D1, 4.3)',
         beneficiaryDefinition='the level of work that earns a first-class degree', scopeNote='the upper rung of Tables 1 and 2', category='unknown', practices=['education']),
    dict(slug='enterprise', definition='generating and developing ideas, drawing on creativity, innovation, adaptability, reflection, problem-solving and communication (D1, 1.14)',
         beneficiaryDefinition='coming up with ideas and turning them into something', scopeNote='with entrepreneurship, a cross-cutting theme', category='unknown', practices=['education']),
    dict(slug='entrepreneurship', definition='applying enterprise to create social, cultural or economic value, in private, public or third sectors and not only for profit (D1, 1.14)',
         beneficiaryDefinition='using your ideas to create value for people, culture or the economy', scopeNote='not limited to commercial activity', category='unknown', practices=['education']),
    dict(slug='integrated-masters-degree', definition="an extended undergraduate award with honours, such as MChem or MSci, covering both honours and master's outcomes at greater depth (D1, 2.3)",
         beneficiaryDefinition="a longer first degree that takes you to master's level", scopeNote='FHEQ level 7; FQHEIS level 11', category='unknown', practices=['education', 'chemistry']),
    dict(slug='monitoring-and-evaluation', definition='periodic internal or external assessment of a course, using current and past data to understand achievement and plan ahead (D1, 2.15)',
         beneficiaryDefinition='how your course is checked and improved over time', scopeNote='with periodic review and external examining', category='unknown', practices=['education']),
]
B2A = [
    dict(concept='threshold-standard', form='threshold standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='excellent-standard', form='excellent standard', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='enterprise', form='Enterprise', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='entrepreneurship', form='Entrepreneurship', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='integrated-masters-degree', form="integrated master's degree", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='monitoring-and-evaluation', form='Monitoring and evaluation', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
]
B4 = []; B5 = []

D3 = [dict(citation='QAA (2022) Subject Benchmark Statement: Chemistry, the PDF as published', settles=['S4', 'SB4'], asked='2026-10-03',
           state="wanted: to check Table 1's last row (no rung cells in the extraction), the page-break split of row 6 and the layout of Table 2's two cells"),
      dict(citation='Royal Society of Chemistry, accreditation criteria for degree programmes (Chartered Chemist)', settles=['SB5', 'S7'], asked='2026-10-03', state='wanted'),
      dict(citation='QAA (2019) Characteristics Statement: Higher Education in Apprenticeships', settles=['SB6', 'S7'], asked='2026-10-03', state='wanted')]

E = [
    "Rung shape (new against Psychology): two rungs only, threshold and excellent, defined in 4.3; no typical rung, Annex D covering the classes between (4.2). The rungs sit in two tables, not separate lists.",
    "Table 1 (honours, caption after 4.6: 'graduates should be able to') has three columns: benchmark standard, threshold, excellent. Each of 14 rows has its own threshold and excellent text; recorded as 4.6.b<n> (threshold) and 4.6.b<n>.excellent, each on its own span, our ids under 4.6 where the table sits (rule 3: for P3). The first column is read as the row's outcome name, not a separate statement: rows 1, 3 to 6 and 9 to 14 restate 3.3 and 3.8 items, which are recorded there; rows 2, 7 and 8 reword them (3.3.b4, 3.8.b2, 3.10).",
    "Table 1's last row ('Act professionally ...') has no threshold or excellent cell in the held text; it repeats 3.8.b9 word for word and is not recorded again. Whether the PDF has cells there is for P2 (D3).",
    "Table 1 row 6 runs across a page break: the threshold cell ends '... covered in course content' and the excellent cell '... evaluate and'; each continues after the page number with 'and report outcomes using appropriate terminology.' The spans stop at the break; the paraphrases include the reporting. Extraction fault, for P2.",
    "Table 1 row 3 holds 'f or' (an extraction split of 'for') in both cells; kept as held.",
    "Table 2 (master's, in 4.7) has five outcomes but only row 1 carries threshold ('With significant support and guidance.') and excellent ('With a high degree of independence and autonomy.') cells. Read as merged cells qualifying all five outcomes, so each outcome is recorded at both rungs on its own span (4.7.b<n>, 4.7.b<n>.excellent). The reading is ours: gradeOf is stated for row 1 and inferred for rows 2 to 5. For P2 against the PDF.",
    "Force: threshold cells take force threshold (the column heading and 4.3); excellent cells take describes (4.3 defines excellent as the level for a first, not a requirement), as in run 0084's tables. The caption's 'should be able to' governs the outcome column. P3 to rule whether excellent cells take should.",
    "gradeOf: 19 links, each excellent cell to the threshold cell in its row; 15 stated (paired cells in one row: Table 1's 14 and Table 2 row 1) and four inferred (Table 2 rows 2 to 5).",
    "Outcome lists: 3.3 (14, should, all undergraduates), 3.4 (3, may, optional content: recorded as outcomes with force may; P3 to rule whether a may list is a standard), 3.8 (9, should, honours), 3.9 (6, should, integrated master's). The aims lists 1.3, 1.4 and 1.5 ('the aims ... are to') state course aims, not outcomes or obligations: not cut; S3 components.",
    "Levels: honours stated at FHEQ 6 and FQHEIS 10, integrated master's at FHEQ 7 and FQHEIS 11 (2.3). Standalone master's (MSc, MRes) are given no level; Table 2 records take fheq:7 by std:doc:qaa-fheq-2024-framework Table 1 (inferred). spine:6 and spine:7 are inferred from std:ref:uk-framework R2. No CQFW reference.",
    "Awards: 3.3 and 3.4 say 'undergraduate courses', recorded for both honours and integrated master's; 3.9 says master's degrees with honours (integrated master's); Table 2 and 4.7 cover integrated and standalone master's.",
    "Subject codes: HECoS 100417 and CAH07-02-01 and CAH07-02 marked stated, as the statement names Chemistry, though it gives no code (as run 0085); 101045 environmental chemistry and 100420 medicinal chemistry are inferred from 2.1. For P3.",
    "Obliging words outside the five, not cut as statements: 1.10 ('responsibility for, promoting equality'); 2.14 ('Providers are expected to develop processes for oversight'); 3.11 and 3.12 ('expected to take more ownership'; master's projects 'expected to be individual'). In 3.10 'expected to' sits beside a should, which is recorded; 2.13 'need to' sits beside a should. 3.22 'strongly encouraged'; 3.25 'considered crucial'.",
    "Not cut, with reasons: 2.12, 2.15, 2.17, 3.13 and 3.16 use will for routine practice (resits, review, examining, project training, session formats); 4.1 frames the tables (as run 0085); 4.3 defines the rungs (the skeleton's 4.3.b1 and 4.3.b2 rung candidates are definitions, recorded in B1); 4.5 and 2.20 describe.",
    "Plain-present provider norms not cut (template open point 5): 1.6, 2.5, 3.1, 3.15 first sentences ('Teaching and learning strategies are designed'), 3.21 first sentence, 4.4 ('Courses include the full range of content and skills'), 4.5.",
    "Skeleton corrections: 1.11, 1.12, 2.6, 2.8, 2.13, 3.2, 3.4.b3, 3.9.b6 and 3.20 carried a following sub-heading and are recut; 4.6 and 4.7 spans covered the tables and are recut to their own sentences; skeleton rung counts (threshold 2) replaced by the table counts.",
    "Paragraphs with two forces: 1.11 (must and should), 2.7 (must and should), 3.15 (must and should): one record each at must, the shoulds in paraphrase and versions. 2.9 (should and will) and 3.10 (expected to, should) recorded at should.",
    "Themes: the four in the front matter, with section 1 headings for three (EDI; ESD; employability, enterprise and entrepreneurship) and section 2 for accessibility. Employability recorded under theme:enterprise.",
    "Bodies: the Royal Society of Chemistry is the only body named in the body text (2.20); PSRBs and the Office for Students appear only in the front matter, the Disabled Students' Commission only in the back matter. The RSC accreditation criteria are not yet ingested (D3).",
    "Shared documents: Annex D is cited as the 2019 standalone annex (reference list) and is now in the 2024 Frameworks (std:doc:qaa-fheq-2024-framework); the apprenticeships characteristics statement is not yet ingested. The HEA (2016) employability framework is in the reference list only.",
    "Agent instructions pair the excellent cells with the Annex D first-class descriptions because 4.3 defines excellent as the level of a first; the choice of Annex D row for each outcome and the FHEQ descriptor ids are ours and inferred.",
    "Text faults noted, not acted on: 'under standing' in the contents; 'f irst' in 4.3; 'tacking unfamiliar problems' in 3.7; 'other's intellectual property' in 3.8.b8; 'honour's subjects' in 3.4.b3.",
    "S9 commentary not researched in P1.",
]
