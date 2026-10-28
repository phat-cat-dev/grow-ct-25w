# Judgement fields for run 0095, QAA Subject Benchmark Statement: Computing (March 2022). std run agent. Built by tools/bm_build.py.
# Keys are S4 ids under qaa/computing-2022/. Two rung tables, both unnumbered:
#   the undergraduate table follows 4.6 (threshold, typical, excellent; six outcome categories): threshold cells 4.6.b<n>,
#   the others 4.6.b<n>.typical and 4.6.b<n>.excellent;
#   the postgraduate table follows 4.14 (typical and excellent only): 4.14.b<n>.typical and 4.14.b<n>.excellent.
# Cells that a page break splits (4.6.b4, 4.14.b5) share one span covering the whole row.
import os as _os

_ST = '/home/claude/wkspc2601-library/ingested/standards'   # moved to the source library (std N-0119)
_NORM = open(_os.path.join('/home/claude', 'wkspc2601-library/txt/qaa-2022-computing-subject-benchmark-statement-standard.norm.txt'), encoding='utf-8').read()


def cut(a, b, frm=0):
    """the held text from the first `a` at or after `frm` to the end of the next `b`: a `find` and its offset."""
    s = _NORM.index(a, frm)
    e = _NORM.index(b, s) + len(b)
    return dict(find=_NORM[s:e], after=s)


HON = "bachelor's with honours"
IM = "integrated master's"
MA = "master's"
ALL = [HON, IM, MA]
CITE = 'QAA (2022), Computing Subject Benchmark Statement'

META = dict(
    run='0095', p1='2026-10-03 16:57',
    title='Subject Benchmark Statement Computing',
    heading='Subject Benchmark Statement: Computing (QAA, March 2022)',
    edition='March 2022 (fifth edition)', published='2022-03',
    status='current',
    supersedes=("the fourth edition, Computing (2019), and the separate Computing (Master's) statement (2019), which this edition "
                "brings together in one statement (D1, front matter; 1.2; back matter)"),
    subjects=[
        dict(scheme='cah', code='CAH11-01', label='computing', basis='inferred'),
        dict(scheme='hecos', code='100366', label='computer science', basis='inferred'),
        dict(scheme='hecos', code='100162', label='computer systems engineering', basis='inferred'),
        dict(scheme='hecos', code='100374', label='software engineering', basis='inferred'),
        dict(scheme='hecos', code='100367', label='computing and information technology', basis='inferred'),
        dict(scheme='hecos', code='100371', label='information systems', basis='inferred'),
        dict(scheme='hecos', code='100376', label='computer and information security', basis='inferred'),
    ],
    awards=[HON, IM, MA], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series="QAA Subject Benchmark Statements, the 2022 revision with cross-cutting themes; this statement's fifth edition (D1, back cover)",
    partsB="partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing",
    agentDefinition=("QAA's UK reference point for what graduates in computing should know, understand and be able to do, in one "
        "statement for three awards: bachelor's degrees with honours, integrated undergraduate master's degrees and taught "
        "postgraduate master's degrees, degree apprenticeships included. Reach for it when designing, approving, reviewing or "
        "describing a computing course or its outcomes, when placing a student's work against the threshold, typical and excellent "
        "rungs or when building employability, inclusion, accessibility or sustainability into a computing curriculum. It is a "
        "sector reference point, not a syllabus, a regulation or a professional body's accreditation standard."),
    summary=("Published by QAA in March 2022 as the fifth edition, the statement joins the earlier bachelor's and master's computing "
        "statements. It sets out the context and purposes of a computing degree with the cross-cutting themes of equality, diversity "
        "and inclusion, sustainability (education for sustainable development) and entrepreneurship and enterprise education, read "
        "as employability, with a long list of employability skills; the distinctive features of course design (seven discipline "
        "areas built on computer science and seven fundamental requirements), accessibility, progression, flexibility, partnership "
        "and review; and content, teaching and assessment. The benchmark standards are two tables: an undergraduate table of six "
        "outcome categories at threshold, typical and excellent, mapped to third, second and first-class honours; and a master's "
        "table of six categories at typical and excellent only, mapped to Pass/Merit and Distinction, with the master's threshold "
        "required by reference. Integrated master's graduates meet the threshold at both levels. It cites the FHEQ and FQHEIS levels "
        "6 and 7 (10 and 11), Annex D, the ESD and enterprise guidance, and names the British Computer Society, the Institute for "
        "Apprenticeships and Technical Education, the Engineering Council and the ACM and IEEE."),
    authority=('reference: a sector-owned reference point, not a regulatory requirement; a key reference point in Wales and Scotland '
               'and part of the quality requirements in Northern Ireland, not a sector-recognised standard in England (D1, front matter)'))

S2 = dict(
    governs=("what graduates in computing can be expected to know, understand and do on bachelor's honours, integrated master's and "
             "taught master's courses, at threshold, typical and excellent rungs, with employability skills and the context for "
             "course design, teaching and assessment"),
    awards=[HON, IM, MA], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    statedScope=('"This Subject Benchmark Statement refers to courses of study in Computing, including: bachelor\'s degrees with honours; '
                 'integrated undergraduate master\'s degrees; postgraduate degrees that are generalist in nature; postgraduate degrees '
                 'that are specialist in nature; courses designed to be studied in part-time mode at both undergraduate and postgraduate '
                 'levels; undergraduate and postgraduate degree apprenticeships." (D1, 1.1)'),
    statedSubjects=[
        dict(name='Computing', locator='(D1, 1.1; 1.5; 3.1)', kind='subject',
             codes=[dict(scheme='cah', code='CAH11-01', label='computing')]),
        dict(name='computer science', locator='(D1, 2.1; Appendix 3)', kind='discipline area',
             codes=[dict(scheme='hecos', code='100366', label='computer science')]),
        dict(name='computer engineering', locator='(D1, 2.1; Appendix 3)', kind='discipline area',
             codes=[dict(scheme='hecos', code='100162', label='computer systems engineering')]),
        dict(name='software engineering', locator='(D1, 2.1; Appendix 3)', kind='discipline area',
             codes=[dict(scheme='hecos', code='100374', label='software engineering')]),
        dict(name='information technology', locator='(D1, 2.1; Appendix 3)', kind='discipline area',
             codes=[dict(scheme='hecos', code='100367', label='computing and information technology')]),
        dict(name='information systems', locator='(D1, 2.1; Appendix 3)', kind='discipline area',
             codes=[dict(scheme='hecos', code='100371', label='information systems')]),
        dict(name='cybersecurity', locator='(D1, 2.1; Appendix 3)', kind='discipline area',
             codes=[dict(scheme='hecos', code='100376', label='computer and information security')]),
        dict(name='data science', locator='(D1, 2.1; Appendix 3)', kind='discipline area', codes=[]),
        dict(name='computer networking; games; multimedia; artificial intelligence; health informatics', locator='(D1, 2.3)', kind='specialism',
             codes=[dict(scheme='hecos', code='100365', label='computer networks'), dict(scheme='hecos', code='101267', label='computer games'),
                    dict(scheme='hecos', code='100737', label='multimedia computing science'), dict(scheme='hecos', code='100359', label='artificial intelligence'),
                    dict(scheme='hecos', code='100994', label='health informatics')]),
    ])

SECTIONS = {
    '1': 'Context and purposes of a Computing degree',
    '2': 'Distinctive features of a Computing degree',
    '3': 'Content, structure and delivery',
    '4': 'Benchmark standards',
}
SUB = [('1.1', '1.3', 'Context'), ('1.4', '1.4', 'Purposes of a Computing degree'), ('1.5', '1.10', 'Characteristics of a Computing degree'),
       ('1.11', '1.14', 'Equality, diversity and inclusion'), ('1.15', '1.18', 'Sustainability'),
       ('1.19', '1.19', 'Entrepreneurship and enterprise education'),
       ('2.1', '2.6', 'Design'), ('2.7', '2.9', 'Accessibility'), ('2.10', '2.12', 'Progression'), ('2.13', '2.14', 'Flexibility'),
       ('2.15', '2.17', 'Partnership'), ('2.18', '2.22', 'Monitoring and review'),
       ('3.1', '3.4', 'Content'), ('3.5', '3.16', 'Teaching and learning'), ('3.17', '3.20', 'Assessment'),
       ('4.1', '4.3', 'Introduction'), ('4.4', '4.6', 'Undergraduate standards: threshold, typical and excellent descriptors'),
       ('4.7', '4.14', 'Postgraduate degrees'), ('4.15', '4.17', "Integrated undergraduate master's degrees")]

G = {
    '1.1': 'the courses covered, from honours to degree apprenticeships',
    '1.2': 'a merged review of earlier statements; ACM and IEEE curricula for detail',
    '1.3': 'a reference point for joint courses with a large computing core',
    '1.4': 'why people study computing; equity and the SDGs',
    '1.5': 'what the discipline is concerned with and does',
    '1.6': 'innovation, disciplined problem-solving and abstraction',
    '1.7': 'innovation from theory as well as technology',
    '1.8': 'varied course titles; other sources a provider may need',
    '1.9': 'graduate outcomes rather than a core curriculum',
    '1.10': 'placements and early professional competence',
    '1.11': 'a culturally responsive curriculum and unbiased technology',
    '1.12': 'representing all students; the gender imbalance',
    '1.13': 'how course structure affects students; reasonable adjustments',
    '1.14': 'an auditable list of EDI practices for courses to consider',
    '1.15': 'sustainable development in computing courses; the ESD guidance',
    '1.16': 'the broad sense of sustainability in the curriculum',
    '1.17': 'the SDGs and four common ways of teaching sustainability',
    '1.18': 'graduates appreciate sustainability issues in their field',
    '1.19': 'employability and enterprise skills for computing courses',
    '2.1': 'computing degrees and their seven discipline areas',
    '2.2': 'no syllabus; the ACM and IEEE curricula inform design',
    '2.3': 'specialist degrees count when a discipline area informs them',
    '2.4': 'joint and interdisciplinary courses',
    '2.5': 'course titles and the dominant discipline area',
    '2.6': 'the fundamental requirements of every computing degree',
    '2.7': "computing's responsibility to disabled people",
    '2.8': 'universal access in teaching and practice',
    '2.9': 'accessible curriculum design; the statutory minimum',
    '2.10': 'progression through honours; readiness for postgraduate study',
    '2.11': 'skills for joint honours students',
    '2.12': "integrated master's structure, exit awards, Scottish honours",
    '2.13': 'flexible education and wider access',
    '2.14': 'kinds of flexibility in delivery, study, assessment and entry',
    '2.15': 'work-based learning and study abroad through partnership',
    '2.16': 'a pointer to further guidance on partnerships',
    '2.17': 'collaboration with outside organisations; advisory boards',
    '2.18': 'monitoring and periodic review',
    '2.19': 'external reviewers in periodic review',
    '2.20': 'external examiners and threshold standards',
    '2.21': 'accreditation by professional bodies',
    '2.22': 'learners in monitoring and review',
    '3.1': 'computing defined; talent-based recruitment',
    '3.2': 'degrees and micro-credentials for learner-earners',
    '3.3': 'stakeholders, international bodies and future skills',
    '3.4': 'balance of skills; capstone and teamwork encouraged',
    '3.5': 'evidencing competence in applied contexts',
    '3.6': 'learner agency, reflection and personalised assessment',
    '3.7': 'teaching for capability and competence',
    '3.8': 'competence through practical work at scale',
    '3.9': 'teaching that builds reflective, adaptable learners',
    '3.10': 'research-informed, inclusive curriculum design',
    '3.11': "from breadth to focus; generalist and specialist master's",
    '3.12': 'curriculum, outcomes and individual competence',
    '3.13': 'resources and staff development',
    '3.14': "legitimacy for integrated specialist master's",
    '3.15': 'grounding knowledge and applying it for lifelong learning',
    '3.16': 'applied learning, team projects and industry partners',
    '3.17': 'varied, authentic assessment',
    '3.18': 'academic integrity and assessment design',
    '3.19': 'the capstone activity',
    '3.20': "capstone formats; research literature at master's level",
    '4.1': 'the minimum threshold standards and the awards they cover',
    '4.2': 'standards set against FHEQ and FQHEIS levels; accreditors',
    '4.3': 'most exceed threshold; Annex D for degree classes',
    '4.4': 'three levels of attainment',
    '4.5': 'honours: threshold required; rungs linked to classes',
    '4.6': "a pointer to the master's paragraphs; the undergraduate rung table",
    '4.7': 'kinds of postgraduate computing degree',
    '4.8': "what all master's graduates have",
    '4.9': "research, specialist and professional master's graduates",
    '4.10': "where master's graduates go next",
    '4.11': 'not every category fits every postgraduate course',
    '4.12': 'postgraduate content aligned to level 7 or 11',
    '4.13': 'postgraduate threshold required; Pass',
    '4.14': "typical and excellent for master's; the postgraduate rung table",
    '4.15': "integrated master's build on honours; their length",
    '4.16': "the master's characteristics apply",
    '4.17': "integrated master's: threshold at both levels",
}
CTYPE = {'2.1': 'area', '2.2': 'area', '2.3': 'area',
         '1.10': 'practice', '2.15': 'practice', '3.4': 'practice', '3.5': 'practice', '3.6': 'practice', '3.7': 'practice',
         '3.8': 'practice', '3.9': 'practice', '3.16': 'practice', '3.17': 'practice', '3.18': 'practice', '3.19': 'practice',
         '3.20': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points', kind='other: front matter, read for S1 and S2'),
    dict(number='section headings 1 to 4', heading='the four section heading lines', kind='other: heading lines'),
    dict(number='5', heading='List of references and further resources', kind='other: back matter, read for S7 and SB6'),
    dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Computing', kind='other: back matter, read for S8 (editions)'),
    dict(number='Appendix 1', heading='Mapping and audit templates', kind='other: blank EDI mapping and audit templates, read for SB2'),
    dict(number='Appendix 2', heading='Examples of ESD approaches', kind='other: illustrative examples, read for SB2 and SB6'),
    dict(number='Appendix 3', heading='Foundations of computer science courses', kind='other: the discipline areas and ACM curricula, read for SB1 and SB3'),
]

P = {}


def s(i, **k):
    P[i] = k


NA_P = ('n/a', 'a duty on the course team or institution; the student meets its effect, not a standard to reach')

# ------------------------------------------------------------------ section 1: EDI and sustainability paragraphs
s('1.11', type='expectation', rung='none', force='should', level='none', appliesTo='computing curricula', addressee='provider',
  verbs=['speak', 'engage', 'ensuring'], about='a culturally responsive curriculum', domain='none', award=ALL,
  para=("Because computing reaches everywhere, a curriculum can be authentic, tied to real problems and a force for social justice; it "
        "should matter to every student and be valued by them, and should give students culturally grounded practical work in a "
        "welcoming, collaborative setting, so that the technology they build carries no unintended bias."),
  prac=("Build a curriculum every student can see themselves in: draw practical tasks from varied cultures, keep the setting welcoming "
        "and collaborative and teach students to check what they build for bias."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on the curriculum and the course team, not a student outcome: a culturally "
       f"responsive curriculum that every student values and that guards against biased technology. It holds for all three awards "
       f"the statement covers. Cite it as {CITE}, para 1.11. Do not present it as a legal duty; set it beside 1.12, 3.9 and 3.10 here "
       f"and the professional practice rungs 4.6.b6, 4.6.b6.typical and 4.6.b6.excellent."),
  aad=("Raise this when a programme team reviews its curriculum, case studies or practical tasks for inclusion. Frame it for staff "
       "as a test of whether every student finds the work relevant and the setting welcoming. Ask: 'Whose experiences do your "
       "practical tasks draw on, and whose are missing?' Do not hand it to a student as a standard they must meet."))
s('1.12', type='expectation', rung='none', force='should', level='none', appliesTo='computing curricula', addressee='provider',
  verbs=['represent'], about='a curriculum that represents all students', domain='none', award=ALL,
  para=("Curricula should therefore represent every student, recognising and removing the biases already present and supporting all "
        "students equally; the gender imbalance in computer science, partly the product of gendered terms, teaching habits and "
        "history, is the example given."),
  prac=("Look through terminology, teaching approaches and examples for bias, gendered language included, remove what you find and "
        "support every student on equal terms."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on curricula: represent all students and remove existing bias, with gender "
       f"imbalance as the worked example. Cite it as {CITE}, para 1.12. Do not claim it sets quotas or a legal test; set it beside "
       f"1.11 and 3.9 here and the EDI practices listed in 1.14."),
  aad=("Raise this when a team looks at recruitment or attainment by gender, or reviews the language of its modules. Frame it for "
       "staff as removing barriers that are already built in. Ask: 'Which terms, examples or teaching habits in your modules might "
       "tell some students that computing is not for them?' Avoid presenting it to a student as their task."))
s('1.15', type='expectation', rung='none', force='should', level='none', appliesTo='computing courses', addressee='provider',
  verbs=['address', 'enable'], about='sustainable development in computing courses', domain='none', award=ALL,
  para=("Computing courses should take up the sustainable development agenda by pointing to the economic, social and environmental "
        "issues the discipline affects for good or ill, and should help students build the personal and professional competencies "
        "to meet the challenges named in the UN Sustainable Development Goals in their later careers; the QAA and Advance HE ESD "
        "guidance sets out teaching approaches."),
  prac=("Show students where computing helps or harms economically, socially and environmentally, and build the competencies they "
        "will need to act on the SDGs at work; use the ESD guidance for methods."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on computing courses to address sustainable development and build students' "
       f"competencies for the SDGs. Cite it as {CITE}, para 1.15. Do not claim it prescribes particular goals (1.17 says it does "
       f"not); set it beside 1.16 to 1.18 here, std:doc:qaa-advancehe-esd-2021-guidance and the professional practice rungs from 4.6.b6."),
  aad=("Raise this when a team maps sustainability content or writes outcomes about it. Frame it for staff as showing both the "
       "good and the harm computing does, and building students' capacity to act. Ask: 'Where in your course do students weigh the "
       "environmental or social cost of a system they build?' Avoid presenting a list of SDGs as compulsory."))
s('1.16', type='expectation', rung='none', force='should', level='none', appliesTo='the computing subject community and its teachers', addressee='provider',
  verbs=['considering'], about='the broad sense of sustainable development', domain='none', award=ALL,
  para=("The subject community should take sustainable development in its broad sense, economic and social as well as environmental, "
        "and think how its teaching links to it: data centre energy use, the cost of making hardware and e-waste are environmental "
        "examples, and the link with EDI brings in social justice, prosperity and a global, inclusive approach to lifelong learning."),
  prac=("Use the broad meaning of sustainability when planning the curriculum: alongside environmental topics such as data centre "
        "energy and e-waste, bring in social justice and economic prosperity."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation addressed to the subject community and its teachers: sustainability in its "
       f"economic, social and environmental senses, linked to EDI. Cite it as {CITE}, para 1.16. Do not narrow it to green IT or "
       f"present it as a student outcome; set it beside 1.15, 1.17, 1.18 and 3.10 in this document."),
  aad=("Raise this when a lecturer treats sustainability as only an environmental topic. Frame it for staff as a wider lens on "
       "material they already teach. Ask: 'Which topic in your module could carry a social or economic sustainability question as "
       "well as an environmental one?' Avoid lecturing on the SDGs at length."))
s('1.18', **cut('1.18 Irrespective', 'might be addressed.'), type='outcome', rung='none', force='should', level='fheq:6',
  appliesTo='computing graduates at every award covered', addressee='learner',
  verbs=['have'], about='appreciating sustainability issues in computing', domain='understanding', award=ALL,
  para=("Whatever approach a course takes, computing graduates should appreciate the sustainable development issues that bear on "
        "their field and the ways those issues are starting to be tackled."),
  prac=("Whichever ESD approach the course takes, check that every graduate can recognise the sustainability issues in their area "
        "of computing and how they are starting to be addressed."),
  ben=("By the end of your course, you should appreciate the sustainability issues that matter in your area of computing and how "
       "people are beginning to tackle them."),
  aaw=(f"Treat this as a should-level outcome for computing graduates at all three awards (FHEQ levels 6 and 7; FQHEIS 10 and 11). "
       f"Cite it as {CITE}, para 1.18. Do not claim it requires specialist sustainability science or a set list of SDGs; set it "
       f"beside 1.15, 1.19.b3 and the professional practice rungs from 4.6.b6, the FHEQ descriptors qaa/fheq-2024/4.15.b4 and "
       f"qaa/fheq-2024/4.17.b1 and the reference step spine:6."),
  aad=("Raise this when a student plans a project or asks why sustainability belongs in a computing degree. To a student, say "
       "plainly that you should be able to name the sustainability issues in your own area; to staff, frame it as a graduate "
       "outcome their modules must give evidence of. Ask: 'What sustainability issue does your project raise, and how is your "
       "field starting to respond to it?' Avoid treating it as a test of specialist environmental knowledge."))

# ------------------------------------------------------------------ 1.19: employability skills (lead-in "imperative ... acting as a guide")
FH7 = {'4.15.b1': '4.17.b1', '4.15.b2': '4.17.b2', '4.15.b3.1': '4.17.b5', '4.15.b3.2': '4.17.b4.1', '4.15.b4': '4.17.b1',
       '4.15.b5': '4.17.b8.3', '4.15.b6': '4.17.b6', '4.15.b7': '4.17.b4.1', '4.15.b8': '4.17.b5', '4.15.b9.1': '4.17.b8.1',
       '4.15.b9.2': '4.17.b8.2', '4.15.b9.3': '4.17.b8.3'}
GROUP = [(1, 11, 'Generic skills'), (12, 15, 'Agile working'), (16, 17, 'Remote working'), (18, 20, 'Resilience'),
         (21, 24, 'Entrepreneurship and enterprise education'), (25, 28, 'Subject-specific skills in computing (common core)')]


def group_of(n):
    for a, b, h in GROUP:
        if a <= n <= b:
            return h


TRIM = {11: ('Communicate with confidence', 'virtual meetings.'),
        15: ('Ability to identify problems and desired', 'acceptable solutions.'),
        17: ('Ability to act confidently', 'own initiative.'),
        20: ('The ability to succinctly present', 'or in writing).'),
        24: ('Recognise factors in environmental', 'human activities.'),
        27: ('Application of computing knowledge', 'will be working in.'),
        28: ('Ability to continuously plan', 'professional development.')}
# n: (domain, verbs, about, Y (our words, third person), Yb (second person), FHEQ honours id, Annex D id, question)
GS = 'generic-skill'
SKILLS = {
 1: (GS, ['work'], 'professional integrity', "acting with integrity in professional conduct and behaviour", "acting with integrity in your professional conduct and behaviour",
     '4.15.b9.1', 'transferable/r4', "Think of a time on a project when cutting a corner was tempting: what did you do, and why?"),
 2: (GS, [], 'legal and ethical awareness', "awareness of the legal and ethical principles that govern professional computing work", "an awareness of the legal and ethical principles that govern computing work",
     '4.15.b9.2', 'transferable/r4', "Which law or ethical principle shaped a design decision in your last project?"),
 3: (GS, [], 'sustainability awareness', "awareness of the sustainability issues that computing raises as a discipline and a profession", "an awareness of the sustainability issues computing raises",
     '4.15.b4', 'knowledge/r2', "What sustainability issue would you raise about the system you are building now?"),
 4: (GS, [], 'computing as a global profession', "an evident understanding that computing is practised as a global profession", "an understanding that computing is a global profession",
     '4.15.b1', 'knowledge/r2', "How would your work change if your team or your users were in another country?"),
 5: (GS, ['include'], 'professional use of social media', "using social media responsibly at work, including professional online communication, email conduct and building an online presence", "the habit of using social media responsibly at work, including how you write online and by email and how you present yourself",
     '4.15.b8', 'transferable/r1', "What would an employer learn about you from your public online profile today?"),
 6: (GS, ['communicate'], 'critical reflection and communication', "critical reflection and clear communication in writing, in speech and online", "critical reflection and clear communication in writing, in speech and online",
     '4.15.b8', 'transferable/r5', "What did your last piece of feedback tell you, and how did you explain your response to it?"),
 7: (GS, ['apply'], 'numeracy and literacy', "a high standard of numeracy and literacy", "a high standard of numeracy and literacy",
     '4.15.b8', 'transferable/r1', "Where did your last report depend on getting the numbers and the wording exactly right?"),
 8: (GS, ['interact'], 'respectful professional interaction', "dealing with others professionally and with respect", "the ability to deal with others professionally and with respect",
     '4.15.b9.1', 'transferable/r2', "How did you handle a disagreement in your last team project?"),
 9: (GS, ['understand', 'demonstrate'], 'respect for equality and diversity', "understanding and showing respect for equality and diversity across the many sectors where computing professionals work", "respect for equality and diversity, understood and shown, across the many sectors where computing is practised",
     '4.15.b9.2', 'transferable/r2', "Where have you seen a team or a product leave some people out, and what would you change?"),
 10: (GS, ['understand'], 'the role of a leader', "understanding what a leader does in setting direction and owning actions and decisions", "an understanding of what a leader does in setting direction and owning decisions",
      '4.15.b9.1', 'transferable/r4', "When have you set the direction for a group, and what did you take responsibility for?"),
 11: (GS, ['communicate'], 'confident communication in meetings', "communicating confidently in meetings held in person or online", "the confidence to speak up in meetings, in person or online",
      '4.15.b8', 'transferable/r1', "In your last online or face-to-face meeting, what did you contribute and how was it received?"),
 12: (GS, ['work'], 'agility and flexibility', "working with agility and flexibility as situations and priorities change", "the ability to adapt quickly as situations and priorities change",
      '4.15.b9.2', 'transferable/r3', "When a project's priorities changed suddenly, how did you adjust your plan?"),
 13: (GS, ['interpret'], 'timely interpretation of data', "interpreting data and information promptly in academic and professional settings", "the ability to make sense of data and information promptly, in study and at work",
      '4.15.b7', 'cognitive/r1', "How quickly could you tell what the data in your last project showed, and how sure were you?"),
 14: (GS, ['recognise', 'make', 'collaborate'], "drawing on others' strengths to collaborate", "recognising and drawing on other people's skills and knowledge in order to collaborate", "the ability to spot and use other people's skills and knowledge when you work together",
      '4.15.b9.1', 'transferable/r2', "In your last group task, whose strengths did you rely on, and how did you find them?"),
 15: (GS, ['identify', 'negotiate', 'achieve'], 'negotiating solutions', "identifying problems and wanted outcomes and negotiating with colleagues towards solutions all can accept", "the ability to pin down a problem and the outcome wanted and to negotiate a solution your colleagues accept",
      '4.15.b7', 'cognitive/r3', "Describe a solution you reached with others that was not your first choice: how did you agree on it?"),
 16: (GS, ['work', 'plan', 'meet'], 'working unsupervised to deadlines', "working without supervision, planning well and meeting deadlines", "the ability to work without supervision, plan well and meet deadlines",
      '4.15.b9.1', 'transferable/r3', "How did you plan your last piece of independent work, and did you meet the deadline?"),
 17: (GS, ['act'], 'acting on own initiative', "acting with confidence on their own initiative", "the confidence to act on your own initiative",
      '4.15.b9.1', 'transferable/r4', "When did you last act without being asked, and what happened?"),
 18: (GS, ['build', 'apply'], 'networking and social capital', "building social capital and using professional networking skills", "a professional network and the skills to grow it",
      '4.15.b9.3', 'transferable/r2', "Who in the profession could you ask for advice today, and how did you meet them?"),
 19: (GS, ['maintain'], 'keeping up with the profession', "keeping a current, critical understanding of developments, challenges and opportunities in the profession, at home and worldwide", "a current, critical view of what is changing in the profession, at home and worldwide",
      '4.15.b3.2', 'cognitive/r1', "What development in computing this year matters most for your area, and why?"),
 20: (GS, ['present', 'address'], 'presenting reasoned arguments', "presenting rational, reasoned arguments concisely on a given problem or opportunity to varied audiences, orally, online or in writing", "the ability to make a short, reasoned case on a problem or opportunity to different audiences, in speech, online or in writing",
      '4.15.b8', 'cognitive/r2', "Could you make the case for your project's approach in two minutes to a non-specialist?"),
 21: (GS, [], 'continuing professional development', "active engagement in continuing professional development", "an active habit of continuing professional development",
      '4.15.b9.3', 'transferable/r3', "What have you learned outside your modules this term, and how did you choose it?"),
 22: (GS, ['contribute', 'apply'], 'enterprise and contribution to the profession', "contributing to the development of the profession and bringing an enterprising, challenging approach", "an enterprising, questioning approach and a part in developing your profession",
      '4.15.b9.1', 'transferable/r4', "Where have you challenged an accepted way of doing something, and what did you propose instead?"),
 23: (GS, ['locate', 'retrieve', 'ensure'], 'finding and communicating ideas', "finding and retrieving relevant ideas and making sure they can be communicated well in varied formats to varied audiences", "the ability to find relevant ideas and share them well in different formats with different audiences",
      '4.15.b8', 'transferable/r1', "How did you find the key sources for your last assignment, and how did you present them?"),
 24: (GS, ['recognise', 'present'], 'opportunities and challenges in context', "recognising environmental and social factors that open opportunities or pose challenges for computing systems across human activity", "the ability to see how environmental and social factors create openings or problems for computing systems",
      '4.15.b7', 'cognitive/r3', "What social or environmental factor could make or break the system you are working on?"),
 27: ('subject-skill', ['solve'], 'applying computational thinking to complex problems', "using what they know of computing, with computational thinking, to crack complex problems for the benefit of the organisation the graduate works in", "the ability to use what you know of computing, with computational thinking, to crack complex problems for the organisation you work in",
      '4.15.b3.1', 'cognitive/r3', "What complex problem have you broken down with computational thinking, and who gained from the result?"),
 28: ('subject-skill', ['plan', 'record'], 'planning and recording self-learning', "planning and recording their own learning in core computing skills and technologies throughout, as a basis for lifelong learning and CPD", "the habit of planning and recording your own learning in core computing skills, as a basis for lifelong learning",
      '4.15.b5', 'transferable/r3', "How do you keep track of what you are learning in computing, and what is next on your list?"),
}
for n, (dom, verbs, about, Y, Yb, fh, ad, qn) in SKILLS.items():
    i = '1.19.b%d' % n
    grp = group_of(n)
    extra = cut(*TRIM[n]) if n in TRIM else {}
    s(i, **extra, type='outcome', rung='none', force='describes', level='fheq:6', appliesTo='computing graduates at every award covered',
      addressee='learner', verbs=verbs, about=about, domain=dom, award=ALL,
      para=f"A skill listed under {grp} for computing courses to build in as part of employability: {Y}.",
      prac=f"Give students chances to develop and evidence {Y} ({grp.lower()}), as one of the employability skills the course builds in.",
      ben=f"Your course is meant to help you develop {Yb}.",
      aaw=(f"Treat this as one of the employability skills the statement lists for computing courses to build in ({grp}); the list is "
           f"offered as a guide with no modal of its own, so describe it as an expected skill, not a requirement. It applies to "
           f"computing graduates at every award covered (FHEQ levels 6 and 7). Cite it as {CITE}, para 1.19. Do not present it as a "
           f"rung or a regulatory requirement; set it beside the FHEQ descriptors qaa/fheq-2024/{fh} and qaa/fheq-2024/{FH7[fh]}, "
           f"the Annex D descriptions qaa/fheq-2024/annex-d/{ad}/3rd to 1st and the reference steps spine:6 and spine:7."),
      aad=(f"Bring this up when a student or team talks about {about}, in study, placements or careers planning. To a student, put it "
           f"in plain words as a skill employers look for that the course helps you build; to staff, as an employability outcome to "
           f"design in and give evidence of. Ask: '{qn}' Avoid reading the issuer's list aloud or treating it as one of the rungs in "
           f"section 4."))

s('1.19.b25', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='computing graduates at every award covered', addressee='learner',
  verbs=['form', 'use', 'apply'], about='subject knowledge employers can rely on', domain='subject-skill', award=ALL,
  para=("The computing knowledge and skills set out across the statement will make up the body of knowledge an employer can fairly "
        "expect a computing graduate to use and apply."),
  prac=("Treat the subject knowledge and skills of the whole statement, above all section 4, as the base an employer will expect "
        "graduates to put to use."),
  ben=("The computing knowledge and skills you build on your course will be what an employer expects you to be able to use and "
       "apply at work."),
  aaw=(f"Treat this as a will-level statement linking the subject standards to employers' expectations: the statement's subject "
       f"knowledge and skills will form the base employers expect graduates to apply. Cite it as {CITE}, para 1.19. Do not claim it "
       f"adds new outcomes or guarantees employment; set it beside the rungs 4.6.b1 to 4.6.b4 and 4.14.b1.typical to "
       f"4.14.b4.typical and the FHEQ descriptors qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.17.b2."),
  aad=("Raise this when a student asks whether what they learn will matter to employers. To a student, say that the subject "
       "knowledge in the course is what an employer will expect you to use; to staff, frame it as the link between the rungs and "
       "employability. Ask: 'Which part of your course would you expect to use in your first month at work?' Avoid promising "
       "particular jobs."))
s('1.19.b26', type='outcome', rung='none', force='should', level='fheq:6', appliesTo='computing graduates at every award covered', addressee='learner',
  verbs=['link', 'discussing'], about='linking computing to business and industry', domain='subject-skill', award=ALL,
  para=("Graduates should be able to connect their computing knowledge to business and industry, discussing examples and case "
        "studies of how organisations put it to use."),
  prac=("Use examples and case studies of organisations using computing so that graduates can explain how their subject knowledge "
        "serves business and industry."),
  ben=("You should be able to show how your computing knowledge is used by organisations, talking through examples and case "
       "studies."),
  aaw=(f"Treat this as a should-level outcome for computing graduates at every award covered (FHEQ levels 6 and 7): relating "
       f"subject knowledge to business and industry through examples. Cite it as {CITE}, para 1.19. Do not claim it requires "
       f"business management knowledge; set it beside 1.19.b25 and 1.19.b27 here, the FHEQ descriptor qaa/fheq-2024/4.15.b3.1 and "
       f"the reference step spine:6."),
  aad=("Raise this when a student prepares for placements or interviews, or a team plans case-study teaching. To a student, put it "
       "as being able to explain how a real organisation uses what you know; to staff, as an outcome case studies should build. "
       "Ask: 'Name an organisation that uses something you have learned, and explain how.' Avoid making it a test of business "
       "jargon."))
s('1.19.b30', **cut('Interdisciplinary teamwork and creative', 'problem-solving in other disciplines.'), type='outcome', rung='none', force='should',
  level='fheq:6', appliesTo='computing graduates at every award covered', addressee='learner',
  verbs=['apply'], about='applying computing in other disciplines', domain='subject-skill', award=ALL,
  para=("Interdisciplinary teamwork and creative thinking are valued employability skills that foster innovation and open minds; "
        "since computing is interdisciplinary, graduates should be able to bring computer science, data science and digital "
        "technology to bear on problems in other fields."),
  prac=("Give students interdisciplinary problems so that, by graduation, they can bring computer science, data science and digital "
        "technology to bear on questions from other fields."),
  ben=("You should be able to use computer science, data science and digital technology to help solve problems in other subjects, "
       "working with people from those fields."),
  aaw=(f"Treat this as a should-level outcome for computing graduates (FHEQ levels 6 and 7): applying computing to problem-solving "
       f"in other disciplines, set in a paragraph on interdisciplinary teamwork. Cite it as {CITE}, para 1.19. Do not claim it "
       f"requires expertise in a second subject; set it beside 2.4 here, the FHEQ descriptor qaa/fheq-2024/4.15.b6 and the reference "
       f"strand strand:application."),
  aad=("Raise this when a student joins an interdisciplinary project or a joint course. To a student, put it as using your computing "
       "to help with someone else's problem; to staff, as an outcome interdisciplinary projects can show. Ask: 'What problem from "
       "another subject could your computing skills help with?' Avoid suggesting the student must master the other subject."))
s('1.19.b32', type='outcome', rung='none', force='should', level='fheq:6', appliesTo='computing graduates at every award covered', addressee='learner',
  verbs=['build', 'match'], about='understanding career pathways', domain=GS, award=ALL,
  para=("Computing graduates can follow many routes across organisation types and roles; they should build an understanding of "
        "those routes and their differing skill demands, know their own technical and wider employability skills and see how to "
        "match these to their career aims."),
  prac=("Help students map the range of computing careers, the skills each asks for and their own skills, so they can plan towards "
        "the roles they want."),
  ben=("You should get to know the many careers open to you in computing, what each asks for and what your own skills are, so you "
       "can match them to what you want to do."),
  aaw=(f"Treat this as a should-level outcome for computing graduates (FHEQ levels 6 and 7): understanding employment pathways and "
       f"matching personal skills to them. Cite it as {CITE}, para 1.19. Do not claim it guarantees a role or sets out a careers "
       f"service duty; set it beside 1.19.b33 and 1.19.b34 here, the FHEQ descriptor qaa/fheq-2024/4.15.b9.3 and the Annex D "
       f"description qaa/fheq-2024/annex-d/transferable/r3/3rd."),
  aad=("Raise this when a student is unsure what to do after the course. To a student, put it plainly: look at the routes open to "
       "you and at what you already offer; to staff, frame it as career awareness the course should build. Ask: 'Which two roles "
       "interest you, and which skills do you still need for them?' Avoid steering the student towards one career."))
s('1.19.b33', type='outcome', rung='none', force='should', level='fheq:6', appliesTo='computing graduates at every award covered', addressee='learner',
  verbs=['communicate'], about='articulating strengths to employers', domain=GS, award=ALL,
  para=("Graduates should be able to show employers how their study and experience evidence their strengths and skills, using "
        "social media to build a professional profile among other means."),
  prac=("Have students practise turning their study and experience into evidence of strengths for employers, including through a "
        "professional online profile."),
  ben=("You should be able to explain to an employer how your study and experience show your strengths and skills, including "
       "through a professional online profile."),
  aaw=(f"Treat this as a should-level outcome for computing graduates (FHEQ levels 6 and 7): communicating to employers how study "
       f"and experience evidence their strengths. Cite it as {CITE}, para 1.19. Do not claim it requires a social media presence; "
       f"set it beside 1.19.b5 and 1.19.b32 here and the FHEQ descriptor qaa/fheq-2024/4.15.b8."),
  aad=("Raise this when a student writes a CV, a portfolio or an online profile. To a student, put it as being able to tell an "
       "employer what your work shows about you; to staff, as an outcome placements and portfolios can build. Ask: 'Which piece of "
       "your work best shows a strength an employer wants, and how would you describe it?' Avoid writing the student's profile for "
       "them."))
s('1.19.b34', type='expectation', rung='none', force='should', level='none', appliesTo='computing courses', addressee='provider',
  verbs=['encourage', 'explore'], about='continuing professional development in career planning', domain='none', award=ALL,
  para=("Computing careers depend heavily on continuing professional development, so courses should encourage students to find out "
        "how to access CPD and to plan it into their careers."),
  prac="Show students where CPD comes from in computing and help them build it into their career plans.",
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on computing courses to encourage students to explore CPD and plan for it. Cite "
       f"it as {CITE}, para 1.19. Do not present it as a student outcome on its own; set it beside 1.19.b21 and 1.19.b28 here and "
       f"the FHEQ descriptor qaa/fheq-2024/4.15.b9.3."),
  aad=("Raise this when a team plans careers or professional development content. Frame it for staff as making CPD visible and "
       "part of career planning. Ask: 'Where in your course do students learn how professionals in computing keep their skills "
       "current?' Avoid presenting it to a student as their duty alone."))
s('1.19.b35', **cut('Course planning and development should include', 'assessment opportunities.'), type='expectation', rung='none', force='should',
  level='none', appliesTo='course planning and development', addressee='provider',
  verbs=['include', 'identify'], about='working with employers on course planning', domain='none', award=ALL,
  para=("Course planning and development should involve employers wherever it can, to find co-curricular activities such as "
        "bootcamps, hackathons and master classes and to develop authentic assessment."),
  prac="Involve employers when planning courses, to set up co-curricular activities and to design authentic assessments.",
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on course teams to work with employers where possible. Cite it as {CITE}, para "
       f"1.19. Do not claim it requires an employer on every course or module; set it beside 2.17 and 3.17 in this document."),
  aad=("Raise this when a team plans a revalidation or new assessments. Frame it for staff as using employers to make activities "
       "and assessment authentic. Ask: 'Which employer has shaped an assessment on your course, and how?' Avoid presenting it to "
       "students as their task."))
s('1.19.b36', type='expectation', rung='none', force='should', level='none', appliesTo='computing courses', addressee='provider',
  verbs=['encourage', 'explore', 'apply'], about='digital technologies in the workplace', domain='none', award=ALL,
  para=("Courses should encourage students to explore what digital technologies can do in the workplace and how to apply suitable "
        "technologies, techniques and principles to raise digital capability."),
  prac="Give students room to explore workplace uses of digital technology and to practise applying it to improve digital capability.",
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on computing courses: encouraging students to explore and apply digital "
       f"technologies at work. Cite it as {CITE}, para 1.19. Do not present it as a student outcome; set it beside 1.19.b37 and "
       f"1.19.b42 here and the FHEQ descriptor qaa/fheq-2024/4.15.b6."),
  aad=("Raise this when a team plans placements, projects or work-related modules. Frame it for staff as giving students real "
       "workplace problems for digital technology. Ask: 'Where do students try out digital technology on a workplace problem in "
       "your course?' Avoid presenting it to students as an obligation."))
s('1.19.b37', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='computing graduates and courses', addressee='both',
  verbs=['expect', 'demonstrate', 'included'], about='core digital skills employers expect', domain=GS, award=ALL,
  para=("Employers will expect graduates to show the core skills needed to apply and advance digital technologies at work, and "
        "courses should include the development of those skills."),
  prac=("Build the core skills for applying and advancing digital technology at work into the course; employers will expect "
        "graduates to show them."),
  ben=("Employers will expect you to show the core skills needed to use and improve digital technology at work, and your course "
       "should help you build them."),
  aaw=(f"Treat this as a will-level statement of employers' expectations of graduates, with a should-level duty on courses to "
       f"develop the skills; the core skills follow as 1.19.b38 to 1.19.b42. Cite it as {CITE}, para 1.19. Do not weaken the will or "
       f"turn the should into a must; set it beside 1.19.b36 here, the FHEQ descriptors qaa/fheq-2024/4.15.b9.1 and "
       f"qaa/fheq-2024/4.17.b8.1 and the reference step spine:6."),
  aad=("Raise this when a student asks what employers look for, or a team reviews its employability outcomes. To a student, put it "
       "as the core skills employers will expect you to show; to staff, as skills the course should develop. Ask: 'Which of the "
       "five core skills that follow could you show an employer today, and with what evidence?' Avoid reading the list aloud."))
CORE = {
 38: (['work', 'achieve'], 'teamwork across cultures', "work with people from a range of cultures towards shared goals, as in group work, group projects and group presentations",
      "work with people from many cultures towards shared goals, as you do in group projects and presentations", '4.15.b9.1', 'transferable/r2',
      "In your last group project, what did you do to help a mixed team reach a shared goal?"),
 39: (['accept', 'plan', 'organise', 'manage'], 'self-management', "take responsibility, be flexible and resilient, start things themselves, assert themselves fittingly and plan, organise and manage their time",
      "take responsibility, stay flexible and resilient, get started without being asked, speak up when it is right to and plan and manage your time", '4.15.b9.1', 'transferable/r3',
      "How do you plan your week when several deadlines fall together?"),
 40: (['showing'], 'self-reflection and empathy', "analyse themselves and show awareness of and sensitivity to diversity among people and cultures, with emotional intelligence and empathy",
      "look honestly at yourself and show awareness of different people and cultures, with emotional intelligence and empathy", '4.15.b9.2', 'transferable/r5',
      "When did you last change how you worked because you understood a colleague's point of view?"),
 41: (['produce'], 'communication and listening', "listen and produce clear, well-structured communications in varied media",
      "listen well and produce clear, well-organised communications in different media", '4.15.b8', 'transferable/r1',
      "Which medium did you choose for your last piece of communication, and why?"),
 42: (['identify', 'advance', 'create'], 'capability advancement', "network with peers and scan the horizon for chances to advance digital capability and improve the future",
      "network with peers and watch for chances to push digital capability forward and improve the future", '4.15.b9.3', 'transferable/r4',
      "What new technology have you spotted that could change your field, and how did you hear about it?"),
}
for n, (verbs, about, Y, Yb, fh, ad, qn) in CORE.items():
    i = '1.19.b%d' % n
    s(i, type='outcome', rung='none', force='will', forceFrom='1.19.b37', level='fheq:6', appliesTo='computing graduates at every award covered',
      addressee='learner', verbs=verbs, about=about, domain=GS, award=ALL,
      para=f"A core skill employers will expect computing graduates to show: the capability to {Y}.",
      prac=f"Develop, and give students ways to evidence, the capability to {Y}; employers will expect it of graduates.",
      ben=f"Employers will expect you to be able to {Yb}.",
      aaw=(f"Treat this as one of the core skills that employers will expect computing graduates to show (the will comes from its "
           f"lead-in, 1.19.b37), at every award covered (FHEQ levels 6 and 7). Cite it as {CITE}, para 1.19, under Employers' "
           f"perspective. Do not present it as a rung or a regulatory requirement; set it beside the FHEQ descriptors "
           f"qaa/fheq-2024/{fh} and qaa/fheq-2024/{FH7[fh]}, the Annex D descriptions qaa/fheq-2024/annex-d/{ad}/3rd to 1st and the "
           f"reference step spine:6."),
      aad=(f"Bring this up when a student prepares for placements or interviews, or a team reviews employability outcomes on "
           f"{about}. To a student, say plainly that employers will expect this of you; to staff, frame it as a skill to build and "
           f"assess. Ask: '{qn}' Avoid reading the issuer's list aloud or presenting it as one of the section 4 rungs."))

# ------------------------------------------------------------------ section 2
s('2.2', type='expectation', rung='none', force='should', level='none', appliesTo='course design and curriculum content', addressee='provider',
  verbs=['used', 'inform'], about='ACM and IEEE curricula to inform design', domain='none', award=ALL,
  para=("The statement gives no syllabus or body of knowledge; the ACM, with the IEEE and other societies, keeps curricula for "
        "several discipline areas up to date, and these should be used to inform course design and content."),
  prac="Use the current ACM and IEEE curriculum guidelines for your discipline area when designing the course and its content.",
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on course design: draw on the ACM and IEEE curricula, since the statement sets "
       f"no syllabus. Cite it as {CITE}, para 2.2. Do not claim the ACM or IEEE curricula are UK requirements; set it beside 1.2 and "
       f"2.1 here and the curricula listed in Appendix 3 (relatedTo in S7)."),
  aad=("Raise this when a team designs a new computing course or asks what content it must cover. Frame it for staff as the "
       "statement deferring content to the professional curricula. Ask: 'Which ACM or IEEE guideline matches your course, and "
       "where does your content depart from it?' Avoid presenting the guidelines as a checklist for students."))
REQ = {
 1: ('describes', ['identified', 'defined', 'captured'], 'clear outcomes reflected in the award title',
     "The topic and learning outcomes are clearly set out, and the award title captures how they relate to computing and its applications.",
     "Make the topic and learning outcomes explicit and choose an award title that shows how they relate to computing."),
 2: ('describes', ['designed', 'accommodate'], 'design for varied entry qualifications',
     "Courses are designed with care to suit students entering with a wide range of accepted qualifications.",
     "Design the course so that students arriving with any of the accepted entry qualifications can succeed."),
 3: ('should', ['identified', 'result'], 'theory that lasts despite rapid change',
     "The relevant theory, mathematical or not, is identified and should lead to emphasis on the fundamentals of the subject that stay stable while technology changes fast.",
     "Identify the theoretical foundations of the course and give most weight to the fundamentals that outlast changes in technology."),
 4: ('describes', ['demonstrates'], 'integrating theory and practice',
     "The curriculum joins theory and practice and plans how students' attitudes develop and how they come to appreciate a range of applications and their effect on users.",
     "Plan the curriculum so theory and practice meet, and so students build attitudes and an appreciation of applications and their effect on users."),
 5: ('describes', ['demonstrates'], 'a cohesive set of classes',
     "The classes fit together, cohesive in content and planned as an approach to the topic of the course.",
     "Make sure the modules form a cohesive, planned whole rather than a loose collection."),
 6: ('describes', ['requires', 'provides', 'demonstrate'], 'a substantial individual or team activity',
     "A major part of the course is a substantial individual activity, or a team activity carrying substantial individual responsibility, that draws on material from across the modules and lets students show a range of abilities and achievements.",
     "Include a major individual activity, or a team one with real individual responsibility, that draws on the whole course and lets students show a range of abilities."),
}
for n, (fw, verbs, about, para, prac) in REQ.items():
    i = '2.6.b%d' % n
    s(i, type='requirement', rung='none', force=fw, forceFrom='2.6', level='none', appliesTo='all computing degree courses', addressee='provider',
      verbs=verbs, about=about, domain='none', award=ALL, para=para, prac=prac, ben=NA_P,
      aaw=(f"Treat this as one of the fundamental requirements the statement sets for every computing degree course (2.6): a duty "
           f"on course design, not a student outcome; the lead-in calls it a requirement but uses none of must, should or will"
           f"{', and the item itself says should' if fw == 'should' else ''}. Cite it as {CITE}, para 2.6. Do not present it as a "
           f"regulatory condition; set it beside the other items 2.6.b1 to 2.6.b7 and the FHEQ statement on meeting the descriptor "
           f"in full, qaa/fheq-2024/4.15.i1."),
      aad=(f"Raise this when a programme team designs, approves or reviews a computing course and checks it against the fundamental "
           f"requirements. Frame it for staff as a design test on {about}. Ask: 'Where in your course documents could a reviewer "
           f"see this, and what would they find?' Avoid presenting it to a student as their responsibility."))
s('2.6.b7', **cut("all undergraduate and master's degree courses will meet", 'Degree-Awarding Bodies.'), type='requirement', rung='none', force='will',
  level='none', appliesTo="all undergraduate and master's computing courses", addressee='provider',
  verbs=['meet'], about='meeting the FHEQ qualification descriptors', domain='none', award=ALL,
  para=("Every undergraduate and master's computing course will meet the outcomes of the qualification descriptors in the UK "
        "qualifications frameworks."),
  prac="Check each award against its level's qualification descriptor in the UK frameworks; the course will meet those outcomes.",
  ben=NA_P,
  aaw=(f"Treat this as a will-level requirement on courses: every award meets the outcomes of its qualification descriptor in "
       f"the Frameworks (std:doc:qaa-fheq-2024-framework), at FHEQ level 6 for honours and 7 for master's. Cite it as {CITE}, para "
       f"2.6. Do not claim the statement replaces the descriptors; set it beside qaa/fheq-2024/4.15.i1 and qaa/fheq-2024/4.17.i1 "
       f"and 4.2 here."),
  aad=("Raise this when a team maps outcomes for approval or review. Frame it for staff as a check against the national "
       "descriptor before the subject rungs. Ask: 'Which of your programme outcomes meets each part of the level descriptor?' "
       "Avoid presenting it to students."))
s('2.7', type='expectation', rung='none', force='should', level='none', appliesTo='computing education', addressee='provider',
  verbs=['recognise', 'taken', 'ensure'], about="computing's responsibility to disabled people", domain='none', award=ALL,
  para=("Computing has a particular responsibility to disabled people: technology can make once hard or impossible tasks routine, "
        "but it can also raise barriers, so care should be taken that it enables rather than disables."),
  prac="Teach and practise computing so that technology removes barriers for disabled people and does not create new ones.",
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on computing education: care that technology enables disabled people. Cite it "
       f"as {CITE}, para 2.7. Do not present it as a full statement of legal duties; set it beside 2.8 and 2.9 here and the "
       f"professional practice rungs from 4.6.b6."),
  aad=("Raise this when a team discusses accessibility in the curriculum or in student projects. Frame it for staff as the "
       "subject's own responsibility, not only a support service matter. Ask: 'Which of your students' projects would a screen "
       "reader user struggle with, and does the course teach them why?' Avoid presenting it to a student as their sole duty."))
s('2.8', type='requirement', rung='none', force='must', level='none', appliesTo='computing education and curricula', addressee='provider',
  verbs=['encompass', 'treated', 'embedded'], about='universal access in teaching and practice', domain='none', award=ALL,
  para=("Accessibility in computing education must cover both teaching and practising universal access, following standards and "
        "working with assistive technologies; in curricula it should be a standard part of computing, embedded, for example, beside "
        "quality testing wherever software lifecycles are taught."),
  prac=("Teach universal access and practise it, with standards and assistive technologies; make accessibility a normal concern in "
        "the curriculum, for example wherever software lifecycles are taught."),
  ben=NA_P,
  aaw=(f"Treat this as a must-level requirement that accessibility in computing education covers teaching and practice, with "
       f"should-level expectations to embed it in curricula. Cite it as {CITE}, para 2.8. Do not weaken the must or strengthen the "
       f"should; set it beside 2.7 and 2.9 here and the practical skills rungs from 4.6.b4."),
  aad=("Raise this when a team reviews where accessibility appears in the curriculum. Frame it for staff as both content to teach "
       "and practice to model. Ask: 'In which module do students first test their software for accessibility, and is it assessed?' "
       "Avoid presenting it to students as their obligation."))
s('2.9', **cut('2.9 In terms of practice', 'barriers in the way of some students.'), type='expectation', rung='none', force='should', level='none',
  appliesTo='curriculum design', addressee='provider',
  verbs=['designed', 'meeting'], about='accessible curriculum design', domain='none', award=ALL,
  para=("Curricula should be designed with accessibility in mind and meet statutory requirements at the least; putting access first "
        "lets students study who otherwise could not, and a requirement to attend campus regularly is an example of a barrier."),
  prac=("Design the course with access as a primary concern, treating legal requirements as the floor; question anything, such as "
        "compulsory regular attendance, that shuts some students out."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on curriculum design, with statutory requirements as the minimum. Cite it as "
       f"{CITE}, para 2.9. Do not claim it sets out the law; set it beside 1.13, 2.8 and 2.14 in this document."),
  aad=("Raise this when a team designs delivery patterns or attendance rules. Frame it for staff as design for access first. Ask: "
       "'Which part of your course would a student who cannot come to campus every week be unable to complete?' Avoid placing the "
       "duty on the student."))
s('2.10', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='honours students in computing', addressee='learner',
  verbs=['progress'], about='progression towards the threshold', domain='none', award=HON,
  para=("An honours student will move from year to year under their institution's rules; each year is expected to add knowledge, "
        "expertise and experience towards meeting all the threshold subject and generic skills, and a graduate with a second-class "
        "degree or better is expected to be ready for postgraduate study in computing or a related subject."),
  prac=("Plan each year so that it builds towards all the threshold subject and generic skills; a 2:2 or better is expected to fit "
        "a graduate for postgraduate study."),
  ben=("Each year of your course builds towards the minimum subject and general skills you need at the end, and with a "
       "second-class result or better you can expect to be ready for postgraduate study."),
  aaw=(f"Treat this as a will-level description of progression through an honours degree (FHEQ level 6; FQHEIS level 10, as the "
       f"paragraph states): each year builds towards the threshold rungs. Cite it as {CITE}, para 2.10. Do not claim it sets entry "
       f"rules for postgraduate courses; set it beside 4.5 and the threshold rungs 4.6.b1 to 4.6.b6, the FHEQ descriptor "
       f"qaa/fheq-2024/4.15.b9.3 and the reference step spine:6."),
  aad=("Raise this when a student asks whether every year counts or whether their result will let them go on to a master's. To a "
       "student, say that each year builds towards the final minimum and that a second-class result usually opens postgraduate "
       "study; to staff, frame it as year-by-year design. Ask: 'Which threshold skills has this year moved you towards?' Avoid "
       "promising entry to a particular course."))
s('2.11', type='expectation', rung='none', force='will', level='fheq:6', appliesTo='joint honours students', addressee='learner',
  verbs=['achieve', 'add'], about='joint honours skills', domain='none', award=HON,
  para="Joint honours students will gain part of the subject and generic skills of computing and add others from their other subject.",
  prac="On joint honours, secure the core computing skills and let the other subject add its own.",
  ben="If you study computing with another subject, you will gain part of the computing skills and add others from your second subject.",
  aaw=(f"Treat this as a will-level expectation for joint honours: elements of the computing skills plus those of the other "
       f"subject. Cite it as {CITE}, para 2.11. Do not claim joint students must meet every rung in full; set it beside 2.4 and the "
       f"rungs 4.6.b1 to 4.6.b6 here and the FHEQ statement qaa/fheq-2024/4.15.i1."),
  aad=("Raise this when a joint honours student or their team asks which computing standards apply. To a student, say you will "
       "cover part of the computing skills and add your other subject's; to staff, frame it as a core set rather than the whole "
       "table. Ask: 'Which computing outcomes does your joint pathway cover, and where?' Avoid implying they must meet everything."))
s('2.19', type='expectation', rung='none', force='will', level='none', appliesTo='providers in periodic review', addressee='provider',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award=ALL,
  para=("Externality is essential to UK quality assurance; providers will bring external reviewers into periodic review for an "
        "outside view of proposed changes and to make sure threshold standards are met and content suits the subject."),
  prac="Include external reviewers in periodic review to test proposed changes, confirm the threshold standards and check the content.",
  ben=NA_P,
  aaw=(f"Treat this as a will-level statement of provider practice: external reviewers in periodic review, partly to confirm "
       f"threshold standards. Cite it as {CITE}, para 2.19. Do not confuse it with external examining (2.20) or present it as a "
       f"student outcome; set it beside 2.18 and 2.20 here and 4.5."),
  aad=("Raise this with a team preparing a periodic review. Frame it for staff as the outside check that the threshold rungs are "
       "met. Ask: 'Which external reviewer will see your threshold evidence, and what will they compare it with?' Avoid presenting "
       "it to students."))
s('2.22', type='expectation', rung='none', force='should', level='none', appliesTo='computing courses', addressee='provider',
  verbs=['consider'], about='learners in monitoring and review', domain='none', award=ALL,
  para="Courses should also consider involving learners in monitoring and review as part of their partnership with students.",
  prac="Bring students into course monitoring and review as partners.",
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation that courses consider including learners in monitoring and review. Cite it as "
       f"{CITE}, para 2.22. Do not claim it requires student members on every panel; set it beside 2.18 and 2.19 in this document."),
  aad=("Raise this when a team plans an annual monitoring or periodic review. Frame it for staff as partnership, not consultation "
       "after the event. Ask: 'Where did students shape your last course review?' Avoid presenting it to a student as an "
       "obligation."))

# ------------------------------------------------------------------ section 3
s('3.4', type='expectation', rung='none', force='should', level='none', appliesTo='those who teach and design computing courses', addressee='provider',
  verbs=['consider', 'encouraged'], about='balancing skills; capstone and teamwork', domain='none', award=ALL,
  para=("Teachers should weigh subject-specific against transferable skills in curriculum and assessment, personalised learning and "
        "evidence of individual capability, as well as education against workforce needs; the value of learning should be clear, problem-"
        "solving and building artefacts are core, and capstone work and teamwork are encouraged."),
  prac=("Balance subject and transferable skills, individual evidence and employer needs as you develop the course; make the value "
        "of learning clear and use capstone work and teamwork."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on those who design and teach courses, with capstone activity and teamwork "
       f"encouraged rather than required. Cite it as {CITE}, para 3.4. Do not turn the encouragement into a requirement; set it "
       f"beside 3.19 and 3.20 here and the team working rungs from 4.6.b5."),
  aad=("Raise this when a team designs assessment or the shape of the final year. Frame it for staff as balancing kinds of skill "
       "and making learning visible to students. Ask: 'How can a student evidence their own contribution in your team projects?' "
       "Avoid presenting it to students as a rule."))
s('3.7', type='expectation', rung='none', force='should', level='none', appliesTo='teaching methods in computing courses', addressee='provider',
  verbs=['employed', 'deliver', 'ensure'], about='teaching for capability and competence', domain='none', award=ALL,
  para=("Computing teaching is varied, which is a strength; the methods used should deliver learning shown through the learning "
        "outcomes, as evidence of capability, and should make sure learners gain competence in particular areas, which needs the "
        "ability to work independently in them."),
  prac=("Choose teaching methods that let students show capability through the outcomes and also build competence, with independent "
        "work, in specific areas."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on teaching methods: capability shown through outcomes and competence in "
       f"specific areas. Cite it as {CITE}, para 3.7. Do not claim it prescribes particular methods; set it beside 3.8 and 3.12 here "
       f"and the FHEQ descriptor qaa/fheq-2024/4.15.b2."),
  aad=("Raise this when a team aligns teaching methods with outcomes. Frame it for staff as the difference between showing "
       "capability and building competence. Ask: 'In which area does your course give students enough independent practice to "
       "become competent?' Avoid presenting it to students."))
s('3.9', type='expectation', rung='none', force='should', level='none', appliesTo='teaching in computing courses', addressee='provider',
  verbs=['encourage', 'prepare', 'exposed', 'minimised', 'considered'], about='teaching for reflective, adaptable learners', domain='none', award=ALL,
  para=("Teaching should get students to reflect, evaluate, select, justify, communicate and innovate in solving problems, and "
        "prepare them to be adaptable, independent learners for life; students should meet a range of bespoke, open source and "
        "commercial tools; varied prior learning should be understood and accommodated, barriers minimised and EDI carefully "
        "considered."),
  prac=("Teach so that students reflect, justify and innovate in problem-solving; use bespoke, open source and commercial tools; "
        "accommodate varied backgrounds and remove barriers to learning."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on teaching, with several parts: reflective problem-solving, a range of tools, "
       f"accommodating prior learning, removing barriers and attending to EDI. Cite it as {CITE}, para 3.9. Do not present it as a "
       f"student outcome; set it beside 1.11 to 1.14 and 3.10 here and the FHEQ descriptor qaa/fheq-2024/4.15.b5."),
  aad=("Raise this when a team reviews its teaching approaches or support for students with varied backgrounds. Frame it for staff "
       "as a checklist of teaching aims. Ask: 'Which barrier to learning in your module could you remove this year?' Avoid placing "
       "the duty on students."))
s('3.10', type='expectation', rung='none', force='should', level='none', appliesTo='curriculum design', addressee='provider',
  verbs=['reflect', 'use', 'include', 'developed'], about='research-informed, inclusive curriculum design', domain='none', award=ALL,
  para=("Curriculum design should reflect research, scholarship and current industry practice and the ability to choose the right "
        "approach for a context; teaching sits within computing's legal, ethical, social, professional, economic and environmental "
        "setting; the curriculum should use inclusive design and cover sustainability and EDI, and graduates' attitudes and values "
        "should be developed for a diverse, fast-changing subject."),
  prac=("Ground the curriculum in research and industry practice, set teaching in its legal, ethical and wider context, design it "
        "inclusively and cover sustainability and EDI."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on curriculum design: research-informed, set in its professional context, "
       f"inclusively designed and covering sustainability and EDI. Cite it as {CITE}, para 3.10. Do not present it as a student "
       f"outcome; set it beside 1.11, 1.15 and 3.9 here and the professional practice rungs from 4.6.b6."),
  aad=("Raise this when a team revalidates a course or adds new content. Frame it for staff as checking the curriculum's context "
       "and inclusiveness as well as its technical content. Ask: 'Where does your curriculum place security, ethics and "
       "sustainability side by side with technical topics?' Avoid presenting it to students."))
s('3.11', type='expectation', rung='none', force='should', level='none', appliesTo='undergraduate and master\'s computing courses', addressee='provider',
  verbs=['expose', 'reflect'], about='from breadth to focus across levels', domain='none', award=ALL,
  para=("Undergraduate courses typically start broad and narrow in the final year; generalist master's usually aim at the minimum "
        "subject knowledge of a computing graduate, broadly or in a niche, and specialist master's and integrated master's final "
        "years focus more closely; progression through levels should also move from general foundations towards current research "
        "and the state of the art, with growing independence in learning."),
  prac=("Plan progression from broad foundations to focus, and from general knowledge towards current research, with students "
        "taking more charge of their own learning at each level."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on how courses progress through levels (FHEQ 6 to 7), with typical patterns for "
       f"undergraduate, generalist and specialist master's courses. Cite it as {CITE}, para 3.11. Do not present the typical "
       f"patterns as rules; set it beside 2.10, 4.12 and the FHEQ descriptors qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/4.17.b6."),
  aad=("Raise this when a team plans the shape of a course across years or designs a generalist master's. Frame it for staff as "
       "progression in focus, currency and independence. Ask: 'How does your final year bring students closer to current "
       "research than your first?' Avoid presenting it to students as a rule."))
s('3.12', type='expectation', rung='none', force='will', level='none', appliesTo='computing curricula and students', addressee='both',
  verbs=['define', 'gain', 'indicate'], about='curriculum, outcomes and individual competence', domain='none', award=ALL,
  para=("The curriculum will define what students learn and the outcomes show where graduates will have knowledge, competence or "
        "capability; each student is expected to have the chance to build deeper competence in some areas, through applied "
        "contexts, the capstone or optional modules, and may show it in a portfolio, through badges or in a CV."),
  prac=("Use the curriculum and outcomes to define what all graduates know and can do, and give each student room to build deeper "
        "competence in chosen areas and to evidence it."),
  ben=("Your course sets out what you will learn, and you will also have the chance to build deeper competence in some areas you "
       "choose, which you can show in a portfolio, through badges or in your CV."),
  aaw=(f"Treat this as a will-level statement of what the curriculum and outcomes do, with an expectation that each student can "
       f"deepen competence in some areas. Cite it as {CITE}, para 3.12. Do not claim every student must specialise or hold "
       f"micro-credentials; set it beside 3.5, 3.7 and 3.19 here and the FHEQ descriptor qaa/fheq-2024/4.15.b1."),
  aad=("Raise this when a student chooses options or a capstone topic, or asks how to show what they are best at. To a student, "
       "say you will have room to go deeper in some areas and show it; to staff, frame it as designing for individual depth. Ask: "
       "'Which area of computing do you want to be strongest in, and how will you show it?' Avoid presenting badges as required."))
s('3.13', type='expectation', rung='none', force='should', level='none', appliesTo='institutions and staff delivering computing courses', addressee='provider',
  verbs=['facilitate', 'demonstrate', 'supported'], about='resources and staff development', domain='none', award=ALL,
  para=("Hardware and software resources should support practical delivery; staff should show ongoing development in the subject and "
        "in pedagogy, supported by their institution, and would normally hold qualifications above the level they teach and a "
        "teaching qualification for higher education, held or in progress."),
  prac=("Provide hardware and software for practical work, support staff development in computing and in teaching and expect "
        "staff to be qualified beyond the level they teach."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on institutions and staff: practical resources, continuing development and, "
       f"normally, qualifications above the level taught. Cite it as {CITE}, para 3.13. Do not present 'normally' as a must; set it "
       f"beside 3.14 here and, for staff development, std:doc:advancehe-psf-dimensions-2023-framework."),
  aad=("Raise this when a team plans staffing, resources or staff development. Frame it for staff as institutional support for "
       "practical teaching and for their own development. Ask: 'What development in computing or pedagogy have you done this "
       "year, and who supported it?' Avoid presenting it to students."))
s('3.14', type='requirement', rung='none', force='must', level='fheq:7', appliesTo="institutions offering integrated specialist master's courses", addressee='provider',
  verbs=['articulate'], about="legitimacy for integrated specialist master's", domain='none', award=IM,
  para=("An institution that offers an integrated specialist master's must be able to show why it is well placed "
        "to teach the topic, which often means staff at its forefront and engaged in advanced scholarship."),
  prac=("If you offer an integrated specialist master's, be ready to justify your standing in the topic, usually through staff "
        "active at its forefront."),
  ben=NA_P,
  aaw=(f"Treat this as a must-level requirement on institutions offering integrated specialist master's courses (FHEQ level 7). "
       f"Cite it as {CITE}, para 3.14. Do not extend it to other awards or present it as a student outcome; set it beside 3.13 and "
       f"4.15 to 4.17 here and the FHEQ master's descriptor qaa/fheq-2024/4.17.i1."),
  aad=("Raise this when a team proposes an integrated specialist master's. Frame it for staff as a firm duty to justify the "
       "course's topic. Ask: 'Which staff work at the forefront of this topic, and what is their recent scholarship?' Avoid "
       "presenting it to students."))
s('3.15', type='outcome', rung='none', force='describes', level='fheq:6', appliesTo='computing graduates at every award covered', addressee='learner',
  verbs=['acquired', 'apply', 'demonstrate'], about='grounding knowledge and applying it to new technology', domain='knowledge', award=ALL,
  para=("Computing graduates need a firm grounding in core knowledge and the ability to apply it to keep learning and to become "
        "competent in new technologies as they appear; students would usually show they can learn and apply a new approach, often in "
        "the major activity near the end of the course."),
  prac=("Secure a strong base of core knowledge and test students' ability to learn and apply something new, often in the final "
        "major activity."),
  ben=("You need a firm base of core computing knowledge and the ability to use it to learn new technologies as they appear, "
       "which you would usually show in your final major project."),
  aaw=(f"Treat this as a graduate outcome stated with 'need to', a word outside must, should and will, so describe it as an "
       f"expectation without strengthening it; it holds at every award covered (FHEQ levels 6 and 7). Cite it as {CITE}, para 3.15. "
       f"Do not present it as a must; set it beside 3.19, 1.19.b28 and the FHEQ descriptors qaa/fheq-2024/4.15.b5 and "
       f"qaa/fheq-2024/4.17.b7."),
  aad=("Raise this when a student plans a final project or asks how to keep up with new technology. To a student, put it as "
       "having a firm base and showing you can learn something new on your own; to staff, as an outcome the capstone can test. "
       "Ask: 'What new technique or tool have you taught yourself, and how did you apply it?' Avoid presenting it as a hard rule."))
s('3.16', type='expectation', rung='none', force='should', level='none', appliesTo='course delivery', addressee='provider',
  verbs=['incorporate'], about='applied learning and team projects', domain='none', award=ALL,
  para=("Course delivery should offer learning applied in real or simulated workplaces, such as placements or "
        "apprenticeships; sizeable team projects simulate real-world complexity, and projects set with industry or research partners "
        "can strengthen learning, self-regulation and awareness of legal and ethical issues."),
  prac="Build in placements or simulated work, sizeable team projects and projects set with industry or research partners.",
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on course delivery: applied learning in authentic or simulated work contexts. "
       f"Cite it as {CITE}, para 3.16. Do not claim placements are compulsory; set it beside 1.10, 2.15 and 3.17 here and the team "
       f"working rungs from 4.6.b5."),
  aad=("Raise this when a team plans placements, live projects or group work. Frame it for staff as giving students authentic "
       "work contexts. Ask: 'Where do students meet a real client or an industry-set problem in your course?' Avoid presenting it "
       "to students as their obligation."))
s('3.17', type='expectation', rung='none', force='should', level='none', appliesTo='assessment in computing courses', addressee='provider',
  verbs=['tied', 'demonstrate'], about='varied, authentic assessment', domain='none', award=ALL,
  para=("Assessment in computing should be varied, fitting and engaging and, above all, authentic, tied to real contexts and "
        "constraints and letting students show their skills in practice."),
  prac="Design varied, engaging assessment that mirrors real contexts and lets students show their skills practically.",
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on assessment design: varied and authentic, with practical demonstration of "
       f"skills. Cite it as {CITE}, para 3.17. Do not claim it bans examinations; set it beside 3.18 to 3.20 and 1.19.b35 here."),
  aad=("Raise this when a team reviews its assessment strategy. Frame it for staff as authenticity and practical demonstration. "
       "Ask: 'Which of your assessments would a working developer recognise as real work?' Avoid presenting it to students as a "
       "rule for them."))
s('3.18', type='expectation', rung='none', force='should', level='none', appliesTo='assessment design', addressee='provider',
  verbs=['afford', 'showcase', 'ensure'], about='academic integrity in assessment design', domain='none', award=ALL,
  para=("Academic integrity matters and assessment design is central to every student succeeding: assessment should let students "
        "show what they can do, not only write about it, with checkpoints so that only students' own work is assessed, for example "
        "by following QAA's contract cheating guidance."),
  prac=("Design assessments where students show what they can do, with checkpoints that confirm the work is their own; use the "
        "contract cheating guidance."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on assessment design: chances to show practical ability, with checkpoints for "
       f"authorship. Cite it as {CITE}, para 3.18. Do not present it as an academic misconduct regulation; set it beside 3.17 here "
       f"and QAA's contract cheating guidance (not yet ingested)."),
  aad=("Raise this when a team redesigns assessments for integrity. Frame it for staff as design that makes authorship visible. "
       "Ask: 'At which checkpoint in your project would you see that the work is the student's own?' Avoid accusing students or "
       "presenting it as their obligation."))
s('3.20', type='expectation', rung='none', force='should', level='fheq:7', appliesTo="capstone activities at master's level", addressee='provider',
  verbs=['drawing'], about="capstone formats; research literature at master's level", domain='none', award=[IM, MA],
  para=("A written dissertation may not suit every computing course, so a capstone may include academic papers, a professional "
        "portfolio or entrepreneurial work; at master's level such activities should focus more on research literature."),
  prac=("Offer capstone formats beyond the dissertation where they fit; at master's level, make research literature central to "
        "them."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on capstone design at master's level (FHEQ level 7), with permission for "
       f"varied formats at any level. Cite it as {CITE}, para 3.20. Do not apply the master's should to honours capstones; set it "
       f"beside 3.19 here, the master's rungs from 4.14.b1.typical and the FHEQ descriptor qaa/fheq-2024/4.17.b4.1."),
  aad=("Raise this when a master's team designs its capstone or a student asks about formats. Frame it for staff as room for "
       "varied formats with a stronger research base at master's level. Ask: 'How does your capstone brief require students to "
       "engage with research literature?' Avoid presenting it to a student as their duty."))

# ------------------------------------------------------------------ section 4: requirements and expectations
s('4.3', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='providers judging achievement', addressee='provider',
  verbs=['perform', 'refer'], about='evidence of achievement and Annex D', domain='none', award=HON,
  para=("Most students will perform well above the minimum threshold; each provider sets what counts as evidence of this and should "
        "refer to Annex D, which describes the four honours classes; the standards are expected to underpin awards, and any "
        "departure from them is to be identified and justified."),
  prac=("Use Annex D's descriptions of the 1st, 2:1, 2:2 and 3rd as the common reference when deciding how to evidence achievement "
        "above threshold, and record and justify any departure from the standards."),
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on providers to refer to Annex D (std:doc:qaa-fheq-2024-framework, Annex D) when "
       f"judging achievement, with the statement that most students exceed threshold. Cite it as {CITE}, para 4.3. Do not claim the "
       f"statement sets the classification algorithm; set it beside 4.5 here and the Annex D summary descriptions from "
       f"qaa/fheq-2024/annex-d/summary/r1/3rd to qaa/fheq-2024/annex-d/summary/r1/1st."),
  aad=("Raise this when a team sets marking criteria or links the rungs to classes. Frame it for staff as a pointer to Annex D and "
       "a duty to justify departures. Ask: 'How do your marking bands relate to the Annex D descriptions?' Avoid telling a student "
       "their class follows mechanically from the rungs."))
s('4.5', type='requirement', rung='none', force='must', level='fheq:6', appliesTo='honours graduates in computing', addressee='learner',
  verbs=['demonstrate'], about='threshold in every category; rungs and classes', domain='none', award=HON,
  para=("Honours graduates in computing must show at least threshold attainment in every outcome category; threshold usually "
        "corresponds to a third, typical to a 2:1 or 2:2 and excellent to a first, and a first does not need excellence in every "
        "category."),
  prac=("Make sure every honours graduate reaches at least the threshold in all six categories; use the typical and excellent rungs "
        "to describe second and first-class work."),
  ben=("To gain an honours degree in computing, you must reach at least the minimum level in every outcome area; a first does not "
       "mean being excellent in all of them."),
  aaw=(f"Treat this as a must-level requirement: every honours graduate meets the threshold in all outcome categories, with the "
       f"issuer's own mapping of rungs to classes (threshold to third, typical to 2:1 or 2:2, excellent to first). Cite it as "
       f"{CITE}, para 4.5. Do not claim the mapping is fixed for every provider; set it beside the rungs 4.6.b1 to 4.6.b6, their "
       f"typical and excellent records and the Annex D summary descriptions qaa/fheq-2024/annex-d/summary/r1/3rd to 1st."),
  aad=("Raise this when a student asks what they must do to pass, or whether a first means excellence everywhere. To a student, "
       "say plainly that you must reach the minimum in every area and that a first does not need excellence in all of them; to "
       "staff, frame it as the rule assessment must secure. Ask: 'In which outcome area are you least sure you have reached the "
       "minimum?' Avoid presenting the typical rung as the pass mark."))
s('4.8', type='outcome', rung='none', force='will', level='fheq:7', appliesTo="all master's graduates in computing", addressee='learner',
  verbs=['include', 'reflect'], about="what all master's graduates have", domain='knowledge', award=[IM, MA],
  para=("Every master's graduate has deep, advanced knowledge and understanding of their subject or profession, shaped by practice, "
        "scholarship and research; this will include critical awareness of current issues and developments, critical skills, "
        "an understanding of professional ethics, integrity and responsibility and the capacity to reflect on how they are progressing as learners."),
  prac=("Make sure master's graduates leave with advanced, current knowledge, critical skills, a grasp of professional ethics and "
        "the habit of reflecting on their own learning."),
  ben=("At master's level, you will have advanced, up-to-date knowledge of your subject or profession, critical skills, an "
       "understanding of professional responsibility and ethics and the habit of reflecting on how you are progressing."),
  aaw=(f"Treat this as a will-level outcome for all master's graduates (FHEQ level 7; FQHEIS level 11), drawn from QAA's master's "
       f"characteristics. Cite it as {CITE}, para 4.8. Do not apply it to honours graduates; set it beside 4.9, the master's rungs "
       f"4.14.b1.typical and 4.14.b6.typical, the FHEQ descriptor qaa/fheq-2024/4.17.b1 and the reference step spine:7."),
  aad=("Raise this when a master's student or team asks what sets master's work apart. To a student, say you will have advanced, "
       "current knowledge, critical skills, a grasp of ethics and the habit of reflection; to staff, frame it as the shared core "
       "of every master's. Ask: 'Which recent development in your field could you critique, and how has your view of your own "
       "learning changed?' Avoid presenting it as the honours standard."))
s('4.9', type='outcome', rung='none', force='will', level='fheq:7', appliesTo="graduates of research, specialist and professional master's", addressee='learner',
  verbs=['study', 'use', 'complete', 'apply'], about="what each kind of master's graduate can do", domain='subject-skill', award=MA,
  para=("Research master's graduates are likely also to study independently and use advanced research methods; specialist or "
        "advanced study master's graduates are likely to complete a research project, sometimes with a critical literature review; "
        "and professional or practice master's graduates are able to bring research and critical perspectives to professional "
        "situations and use methods suited to their practice."),
  prac=("Match outcomes to the kind of master's: independent study and research methods for research master's, a research project "
        "for specialist ones and research applied to practice for professional ones."),
  ben=("Depending on your master's, you are likely to study independently with advanced research methods, complete a research "
       "project, or, on a professional master's, bring research and critical thinking to real work situations."),
  aaw=(f"Treat this as an outcome statement for three kinds of master's (FHEQ level 7): 'likely' for research and specialist "
       f"master's, 'are able to' for professional or practice master's. Cite it as {CITE}, para 4.9. Do not turn 'likely' into a "
       f"requirement; set it beside 4.8 and 4.10 here, the FHEQ descriptors qaa/fheq-2024/4.17.b2 and qaa/fheq-2024/4.17.b4.2 and "
       f"the reference step spine:7."),
  aad=("Raise this when a student chooses between master's types or a team designs one. To a student, explain what each type "
       "usually leads you to do; to staff, frame it as matching outcomes to the course's kind. Ask: 'Is your master's mainly "
       "research, specialist or professional, and do your outcomes show it?' Avoid presenting the likely outcomes as fixed rules."))
s('4.12', type='expectation', rung='none', force='should', level='fheq:7', appliesTo='postgraduate computing courses', addressee='provider',
  verbs=['align'], about='postgraduate content aligned to level 7 or 11', domain='none', award=MA,
  para="In every case, a postgraduate course's content should align with the specification for FHEQ level 7 or SCQF level 11.",
  prac="Check that the content of each postgraduate course matches the FHEQ level 7 (SCQF level 11) descriptor.",
  ben=NA_P,
  aaw=(f"Treat this as a should-level expectation on postgraduate courses to align with FHEQ level 7 or SCQF level 11 (fqheis:11). "
       f"Cite it as {CITE}, para 4.12. Do not claim it requires every undergraduate category to apply (4.11 says not); set it beside "
       f"4.13 and the FHEQ master's descriptor qaa/fheq-2024/4.17.i1."),
  aad=("Raise this when a team designs or reviews a taught master's. Frame it for staff as a level check before the subject rungs. "
       "Ask: 'Which modules carry the level 7 demands for originality and judgement without complete data?' Avoid presenting it "
       "to students."))
s('4.13', type='requirement', rung='none', force='must', level='fheq:7', appliesTo="postgraduate master's graduates in computing", addressee='learner',
  verbs=['demonstrate'], about="threshold for postgraduate master's; Pass", domain='none', award=MA,
  para=("With reference to the undergraduate descriptors, postgraduate computing graduates must show at least threshold attainment "
        "in every relevant outcome category; threshold usually corresponds to a Pass."),
  prac=("Make sure every master's graduate reaches at least the threshold in each category that applies to the course; a Pass "
        "usually marks it."),
  ben=("To gain a postgraduate degree in computing, you must reach at least the minimum level in every outcome area that applies "
       "to your course, which usually means a Pass."),
  aaw=(f"Treat this as a must-level requirement for postgraduate computing graduates (FHEQ level 7; SCQF level 11): threshold in "
       f"all relevant categories, usually a Pass. The postgraduate table gives no threshold column, so the threshold is read by "
       f"reference to the undergraduate descriptors. Cite it as {CITE}, para 4.13. Do not invent a master's threshold text; set it "
       f"beside 4.11, 4.14, the master's rungs from 4.14.b1.typical and the FHEQ descriptor qaa/fheq-2024/4.17.i1."),
  aad=("Raise this when a master's student asks what they need to pass. To a student, say plainly that you must reach the minimum "
       "in every area your course covers, which usually means a Pass; to staff, frame it as the floor and note that the table "
       "only describes typical and excellent. Ask: 'Which outcome area applies to your course, and where are you least sure of "
       "the minimum?' Avoid presenting the typical column as the pass standard."))
s('4.17', type='requirement', rung='none', force='must', level='fheq:7', appliesTo="integrated master's graduates in computing", addressee='learner',
  verbs=['demonstrate'], about="integrated master's: threshold at both levels", domain='none', award=IM,
  para=("Integrated master's graduates in computing must show at least threshold attainment against every descriptor at both FHEQ "
        "levels 6 and 7 (FQHEIS 10 and 11)."),
  prac=("Make sure integrated master's graduates reach the threshold at both the honours and the master's level across all "
        "descriptors."),
  ben=("On an integrated master's in computing, you must reach at least the minimum at both the honours and the master's level in "
       "every outcome area."),
  aaw=(f"Treat this as a must-level requirement for integrated master's graduates: threshold across all descriptors at FHEQ "
       f"levels 6 and 7 (FQHEIS 10 and 11). Cite it as {CITE}, para 4.17. Do not read its pointer to 'paragraphs 4.2 and 4.3' as "
       f"statements; set it beside 4.5, 4.13, the rungs 4.6.b1 to 4.6.b6, the master's rungs from 4.14.b1.typical and the FHEQ "
       f"descriptors qaa/fheq-2024/4.15.i1 and qaa/fheq-2024/4.17.i1."),
  aad=("Raise this when an integrated master's student asks what they must reach, or a team plans its final year. To a student, "
       "say you must reach the minimum at both levels; to staff, frame it as two thresholds, honours then master's. Ask: 'Which "
       "master's-level outcome is your final year built to secure?' Avoid presenting either typical column as the minimum."))

# ------------------------------------------------------------------ 4.6: the undergraduate rung table (threshold, typical, excellent)
T0 = _NORM.index('Threshold Typical Excellent Subject')
K, U, SK = 'knowledge', 'understanding', 'subject-skill'
UG = [
 # (category, domain, about, FHEQ id, Annex D id, spans (T, Ty, E) or 'row', verbs (T, Ty, E), paras, bens, questions)
 ('Subject knowledge, understanding and skills', K, 'the main body of subject knowledge', '4.15.b1', 'knowledge/r1',
  (('Demonstrate a requisite understanding', 'knowledge for their subject'), ('Demonstrate a sound understanding', 'in the use of that knowledge'),
   ('Demonstrate an exceptional understanding', 'taught in classes')),
  (['demonstrate'], ['demonstrate', 'exercise'], ['demonstrate', 'exercise', 'go']),
  ("show the understanding of the core body of computing knowledge that their subject needs",
   "show a sound grasp of the core body of knowledge in their subject and use critical judgement in applying it",
   "show an exceptional grasp of the core body of knowledge with insightful critical judgement in using it, apply what the curriculum covers creatively and with innovation and reach past what was taught"),
  ("show that you understand the core knowledge of your area of computing well enough for what it needs",
   "show a sound grasp of the core knowledge of your area and use critical judgement in applying it",
   "show an exceptional grasp of the core knowledge of your area, judge insightfully how to use it, apply it creatively and go beyond what you were taught"),
  ("Which core topics of your subject could you explain without your notes?",
   "Where did you have to judge which part of your knowledge fitted a problem, and why?",
   "What have you learned beyond the taught material, and how did you use it?")),
 ('Intellectual skills', U, 'applying concepts, principles and practices', '4.15.b7', 'cognitive/r2',
  (('Understand and apply essential concepts', 'application of tools and techniques'), ('Critically analyse and apply concepts', 'use of tools and techniques'),
   ('Critically analyse and apply a wide range', 'use of tools and techniques')),
  (['understand', 'apply', 'showing'], ['analyse', 'apply', 'showing'], ['analyse', 'apply', 'showing']),
  ("understand and use the subject's essential concepts, principles and practices in clearly defined scenarios, choosing and applying tools and techniques with judgement",
   "analyse critically and apply the subject's ideas, principles and practices where scenarios are only loosely defined, choosing and using tools and techniques with effective judgement and adaptability",
   "analyse critically and apply a wide range of the subject's ideas, principles and practices in open scenarios, choosing and using tools and techniques with refined judgement and adaptability"),
  ("understand and use the essential ideas and methods of your subject on clearly set problems, choosing suitable tools with care",
   "analyse critically and apply your subject's ideas and methods to loosely defined problems, choosing tools well and adapting as you go",
   "analyse critically and apply a wide range of ideas and methods to open problems, choosing tools with refined judgement and adapting readily"),
  ("For your last assignment, why did you choose the tools you used?",
   "When a brief was vague, how did you decide which approach and tools to use?",
   "Faced with an open problem, how did you weigh several approaches before choosing one?")),
 ('Computational problem-solving', SK, 'computational problem-solving', '4.15.b3.1', 'cognitive/r3',
  (('Be able to demonstrate judgement, critical thinking and problem-solving', 'with a degree of independence'),
   ('Be able to demonstrate detailed judgement', 'appropriate computational artefacts'),
   ('Be able to demonstrate sophisticated judgement', 'unpredictable circumstances')),
  (['demonstrate', 'solve', 'create'], ['demonstrate', 'solve', 'create'], ['demonstrate', 'create']),
  ("use judgement, critical thinking and problem-solving to solve clearly specified problems and build computational artefacts with some independence",
   "use detailed judgement, critical thinking and problem-solving to solve both clearly specified and loosely defined problems and build suitable computational artefacts",
   "bring sophisticated judgement and critical thinking, research design and strong problem-solving to bear with considerable autonomy, building highly effective computational artefacts where circumstances are complex and unpredictable"),
  ("use judgement and critical thinking to solve clearly set problems and build working software or other artefacts with some independence",
   "use detailed judgement and critical thinking to solve both clearly set and loosely defined problems and build suitable artefacts",
   "bring sophisticated judgement, research design and strong problem-solving to complex, unpredictable problems with real independence, building highly effective artefacts"),
  ("What part of your last program or system did you work out on your own?",
   "How did you turn a loosely defined problem into something you could build?",
   "Which complex problem have you tackled with little guidance, and how did you design your approach?")),
 ('Practical skills across the computing lifecycle', SK, 'practical skills across the lifecycle', '4.15.b6', 'practical/r1',
  'row',
  (['undertake', 'design', 'develop', 'test', 'integrate', 'deploy', 'understand'], ['undertake', 'design', 'deploy', 'understand', 'demonstrate'],
   ['undertake', 'design', 'deploy', 'understand', 'demonstrate']),
  ("identify and analyse a problem, then suitably design, build, test, integrate or deploy a computing system with its related artefacts, understanding how the stages connect",
   "identify and analyse a problem, then suitably design, build, test, integrate or deploy a complex computing system with its related artefacts, understanding how the stages connect and applying problem-solving and evidence-informed evaluation",
   "identify and analyse a problem, then suitably design, build, test, integrate or deploy a highly complex computing system with its related artefacts, understanding in depth how the stages connect and applying sophisticated problem-solving and evidence-informed evaluation"),
  ("identify and analyse a problem and then design, build, test, integrate or deploy a system to solve it, knowing how the stages fit together",
   "do the same for a complex system, knowing how the stages fit together and judging your work on evidence",
   "do the same for a highly complex system, with a deep grasp of how the stages fit together and sophisticated, evidence-based evaluation"),
  ("Walk me through the stages of your last project, from the problem to the working system.",
   "How did evidence from testing change your design on a complex system?",
   "On your most complex system, how did a decision at one stage affect the others, and how did you evaluate it?")),
 ('Interpersonal and team working skills', GS, 'teamwork and project working', '4.15.b9.1', 'transferable/r2',
  (('Demonstrate the ability to work in an effective manner', 'plan projects under guidance'), ('Demonstrate the ability to work in a proactive', 'with minimum guidance'),
   ('Demonstrate the ability to work in a highly proactive', 'with minimum guidance')),
  (['work', 'communicate', 'manage', 'plan'], ['work', 'communicate', 'manage', 'plan'], ['work', 'communicate', 'manage', 'plan']),
  ("work effectively, including in a team, using tools and techniques suitably to communicate, organise tasks and plan projects with guidance",
   "work proactively and effectively, including in a team, using tools and techniques well to communicate clearly, organise tasks and plan projects with little guidance",
   "work in a highly proactive, accomplished way, including leading within a team, using tools and techniques excellently to communicate, organise tasks and plan projects proficiently with little guidance"),
  ("work well, including in a team, using suitable tools to communicate, organise tasks and plan projects with some guidance",
   "work proactively and well in a team, using tools to communicate, organise tasks and plan projects with little guidance",
   "work in a highly proactive, accomplished way, taking a lead in your team and using tools excellently to plan and run projects with little guidance"),
  ("Which tools did your team use to share tasks, and what was your part?",
   "Where did you step in without being asked to keep a team project on track?",
   "When have you led a team, and how did you plan and run the work?")),
 ('Professional practice', GS, 'professional, legal and ethical practice', '4.15.b9.2', 'transferable/r4',
  (('Identify appropriate practices and perform work', 'in the work that they undertake'), ('Identify appropriate practices and effect principled', 'in the work that they undertake'),
   ('Identify best-of-kind practices', 'in the work that they undertake')),
  (['identify', 'perform'], ['identify', 'effect', 'address'], ['identify', 'effect', 'address']),
  ("identify suitable practices and carry out their own work inside a professional, legal and ethical framework that covers data management and use, security, EDI and sustainability",
   "identify suitable practices and reach principled solutions inside a professional, legal and ethical framework that deal with the core considerations, such as data management and use, security, EDI and sustainability, in their own work",
   "identify the best practices of their kind and reach highly principled solutions inside a professional, legal and ethical framework that deal consistently with a wide range of relevant considerations, such as data management and use, security, EDI and sustainability, in their own work"),
  ("choose suitable practices and work within professional, legal and ethical limits, including on data, security, equality and sustainability",
   "choose suitable practices and reach principled solutions that deal with the main professional, legal and ethical issues in your work, from data and security to equality and sustainability",
   "choose the best practices available and reach highly principled solutions that deal consistently with a wide range of professional, legal and ethical issues in your work"),
  ("What legal or ethical rule applied to the data in your last project, and how did you follow it?",
   "Which principled choice did you make about security, data or inclusion in a recent project?",
   "Where have you weighed several ethical, legal and sustainability issues at once and reached a sound solution?")),
]
UG_OUT = []
GRADE = {}
ROW4 = cut('Demonstrate the ability to undertake problem identification', 'sophisticated problem-solving and evidence-informed evaluative skills', T0)
for n, (cat, dom, about, fh, ad, spans, verbs, paras, bens, qs) in enumerate(UG, 1):
    th, ty, ex = '4.6.b%d' % n, '4.6.b%d.typical' % n, '4.6.b%d.excellent' % n
    fh7 = FH7[fh]
    finds = [dict(ROW4), dict(ROW4), dict(ROW4)] if spans == 'row' else [cut(a, b, T0) for (a, b) in spans]
    base = dict(level='fheq:6', addressee='learner', about=about, domain=dom, award=HON)
    s(th, **finds[0], **base, type='threshold', rung='threshold', force='threshold', forceFrom='4.5', verbs=verbs[0],
      appliesTo='honours graduates in computing, at the threshold rung',
      para=f"At threshold, honours graduates will {paras[0]}.",
      prac=f"Every honours graduate must reach this in {cat.lower()}: they {paras[0]}. Teaching and assessment need to secure it for all.",
      ben=f"To reach the minimum for an honours degree, you will {bens[0]}.",
      aaw=(f"Treat this as the threshold rung for honours graduates in computing: the minimum the award requires in {cat} ({about}), "
           f"at FHEQ level 6 (FQHEIS level 10 in Scotland). Cite it as {CITE}, para 4.6, undergraduate table, {cat} row, threshold "
           f"column. Do not present it as a regulatory requirement or as a master's standard, which has its own table after 4.14. "
           f"Set it beside {ty} and {ex}, the FHEQ honours descriptor qaa/fheq-2024/{fh} and the Annex D third-class description "
           f"qaa/fheq-2024/annex-d/{ad}/3rd, which 4.5 says the threshold usually maps onto."),
      aad=(f"Raise this when a student asks what they must show in {about} to pass, or when a team checks the minimum every graduate "
           f"reaches. To a student, say plainly that this is the floor for an honours degree; to staff, frame it as what the course "
           f"must secure for everyone. Ask: '{qs[0]}' Do not read the table aloud, and do not present the typical or excellent "
           f"columns as the minimum."))
    s(ty, **finds[1], **base, type='typical', rung='typical', force='will', forceFrom='4.1', verbs=verbs[1],
      appliesTo='honours graduates in computing, at the typical rung',
      para=f"At the typical rung, honours graduates will {paras[1]}.",
      prac=f"Most honours graduates reach this in {cat.lower()}: they {paras[1]}. Design teaching and assessment so it is the usual result.",
      ben=f"At the typical level, you will {bens[1]}.",
      aaw=(f"Treat this as the typical rung: what most honours graduates in computing show in {cat} ({about}), above the threshold, "
           f"at FHEQ level 6 (FQHEIS level 10). Cite it as {CITE}, para 4.6, undergraduate table, {cat} row, typical column. Do not "
           f"present it as the pass standard; 4.5 links it to 2:1 or 2:2 performance, so set it beside {th} and {ex}, the FHEQ "
           f"descriptor qaa/fheq-2024/{fh} and the Annex D descriptions qaa/fheq-2024/annex-d/{ad}/2.2 and qaa/fheq-2024/annex-d/{ad}/2.1."),
      aad=(f"Raise this when a student who meets the basics in {about} asks what a solid result looks like, or a team calibrates "
           f"marking. To a student, describe it as the level most people reach, linked to an upper or lower second; to staff, as the "
           f"expected standard above the floor. Ask: '{qs[1]}' Avoid presenting it as the pass mark."))
    s(ex, **finds[2], **base, type='excellent', rung='excellent', force='will', forceFrom='4.1', verbs=verbs[2],
      appliesTo='honours graduates in computing, at the excellent rung',
      para=f"At the excellent rung, honours graduates will {paras[2]}.",
      prac=f"First-class work in {cat.lower()} usually shows this: graduates {paras[2]}. Leave room in tasks for the strongest students to show it.",
      ben=f"At the excellent level, you will {bens[2]}.",
      aaw=(f"Treat this as the excellent rung, an aspiration rather than a requirement: what first-class work in {cat} ({about}) "
           f"usually shows, at FHEQ level 6 (FQHEIS level 10). Cite it as {CITE}, para 4.6, undergraduate table, {cat} row, excellent "
           f"column. Do not claim every first-class student must reach it in every category (4.5 says not) or that it is master's "
           f"work. Set it beside {th} and {ty}, the FHEQ descriptor qaa/fheq-2024/{fh} and the Annex D first-class description "
           f"qaa/fheq-2024/annex-d/{ad}/1st."),
      aad=(f"Raise this with a student aiming for a first, or a team designing stretch tasks in {about}. To a student, describe it "
           f"as what the strongest work shows; to staff, as the room assessment must leave at the top. Ask: '{qs[2]}' Avoid implying "
           f"that everyone must reach it or that a first needs it in every category."))
    GRADE[ty] = th + '|stated'
    GRADE[ex] = ty + '|stated'
    UG_OUT.append(dict(outcome=about, threshold=th, typical=ty, excellent=ex, basis='stated', domain=dom, award=HON))

# ------------------------------------------------------------------ 4.14: the postgraduate rung table (typical and excellent only)
P0 = _NORM.index('4.14 The typical level descriptor')
PG = [
 ('Subject knowledge, understanding and skills', K, 'systematic knowledge at the forefront', '4.17.b1',
  (('Demonstrate a systematic understanding', 'interpret knowledge in the discipline.'), ('Demonstrate a deep and systematic', 'interpret knowledge in the discipline.')),
  (['demonstrate', 'create', 'interpret'], ['demonstrate', 'create', 'interpret']),
  ("show systematic understanding of knowledge in their area of study, much of it at or shaped by the forefront of the discipline or of professional practice, critical awareness of current problems or recent developments, some originality in applying knowledge and a practical understanding of how established research and enquiry techniques create and interpret knowledge",
   "show deep, systematic understanding of knowledge in their area, much of it at or shaped by the forefront, with critical awareness and advanced understanding of current problems or recent developments, originality in applying knowledge and a practical and reflective grasp of how research and enquiry techniques, both established and state-of-the-art, create and interpret knowledge"),
  ("show a systematic understanding of your area, much of it close to the leading edge, a critical awareness of its current problems, some originality in using what you know and a practical grasp of how research builds knowledge",
   "show a deep, systematic understanding of your area, much of it close to the leading edge, an advanced and critical view of its current problems, originality in using what you know and a reflective grasp of how established and the newest research methods build knowledge"),
  ("Which current problem in your field could you explain and critique?", "Where have you applied knowledge in a way that was genuinely your own?")),
 ('Intellectual skills', U, 'critical evaluation at the forefront', '4.17.b4.1',
  (('Be able to analyse, apply and critically evaluate', 'the area of study.'), ('Be able to deeply analyse', 'as appropriate.')),
  (['analyse', 'apply', 'evaluate'], ['analyse', 'apply', 'evaluate', 'demonstrating']),
  ("critically evaluate, analyse and apply the concepts, principles and practices found at the leading edge of their area of study",
   "analyse in depth, apply and critically evaluate leading-edge concepts, principles and practices, showing insight and innovation and applying these skills where they fit"),
  ("analyse, apply and critically judge the ideas and practices at the leading edge of your area",
   "analyse in depth, apply and critically judge leading-edge ideas and practices, with insight and innovation"),
  ("Which leading-edge idea in your area have you evaluated critically, and what did you conclude?", "Where did your analysis of a new idea lead you to something innovative?")),
 ('Computational problem-solving', SK, 'computational problem-solving with autonomy', '4.17.b5',
  (('Be able to demonstrate judgement, critical thinking, research design', 'complex or open constraints.'), ('Be able to demonstrate innovation', 'complex or open constraints.')),
  (['demonstrate', 'create'], ['demonstrate', 'create']),
  ("bring judgement, critical thinking, research design and strong problem-solving to bear with considerable autonomy, building effective computational artefacts under complex or open constraints",
   "show innovation or originality with sophisticated judgement, critical thinking, research design and strong problem-solving, working with considerable autonomy to build comprehensive, highly effective computational artefacts under complex or open constraints"),
  ("use judgement, critical thinking and research design to solve problems largely on your own, building effective artefacts when the constraints are complex or open",
   "bring innovation or originality and sophisticated judgement to problems you tackle largely on your own, building comprehensive, highly effective artefacts under complex or open constraints"),
  ("How did you design your approach to a problem whose constraints were open?", "What was original in the way you solved your hardest problem this year?")),
 ('Practical computing skills', SK, 'applying computing techniques in complex scenarios', '4.17.b2',
  (('Demonstrate the ability to apply computing techniques', 'incomplete or missing data.'), ('Demonstrate the ability to apply state-of-the-art', 'incomplete or missing data.')),
  (['apply', 'making'], ['apply', 'making']),
  ("apply computing techniques suited to their area systematically in complex or unpredictable scenarios, making sound decisions when data are incomplete or missing",
   "apply state-of-the-art computing techniques suited to their area systematically and creatively in highly complex or unpredictable scenarios, making insightful decisions when data are incomplete or missing"),
  ("apply suitable computing techniques systematically in complex, unpredictable situations and make sound decisions when data are missing",
   "apply the newest computing techniques systematically and creatively in highly complex situations and make insightful decisions when data are missing"),
  ("When data were missing, how did you decide what to do next?", "Which state-of-the-art technique have you used, and why did it fit?")),
 ('Self-directed learning and attainment', GS, 'self-direction', '4.17.b6',
  'row',
  (['tackling', 'solving', 'approaching', 'implementing'], ['tackling', 'solving', 'approaching', 'implementing']),
  ("show some self-direction in tackling and solving problems and approach and carry out tasks proactively and effectively",
   "show self-direction in tackling and solving complex problems and approach and carry out tasks in a highly proactive, effective way"),
  ("direct yourself to some extent in tackling problems and carry out tasks proactively and well",
   "direct yourself in tackling complex problems and carry out tasks in a highly proactive, effective way"),
  ("Which problem did you take on without being directed, and how did you see it through?", "What complex task did you plan and complete on your own initiative?")),
 ('Professional practice', GS, 'communication and professional practice', '4.17.b8.2',
  (('Ability to communicate their work to specialist and a diverse', 'in the work that they undertake.'),
   ('Ability to communicate their work to specialist and non-specialist', 'in the work they undertake.')),
  (['communicate', 'identify', 'perform'], ['communicate', 'identify', 'effect', 'address']),
  ("communicate their work to specialists and to a wide range of non-specialist audiences, and identify suitable practices and work inside a professional, legal and ethical framework, covering data management and use, security, EDI and sustainability, in complex, unpredictable professional settings",
   "communicate their work accessibly and with impact to specialist and non-specialist audiences, and identify and reach the best, highly principled solutions inside a professional, legal and ethical framework, dealing consistently with a wide range of considerations such as data management and use, security, EDI and sustainability, in complex, unpredictable professional settings"),
  ("explain your work to specialists and to many kinds of non-specialist, and work within professional, legal and ethical limits, including on data, security, equality and sustainability, in complex settings",
   "explain your work clearly and with impact to any audience, and reach the best, highly principled solutions to a wide range of professional, legal and ethical issues in complex settings"),
  ("How would you explain your project to a non-specialist manager, and what professional issues would you raise?", "Where have you balanced several legal, ethical and sustainability issues in a complex professional setting?")),
]
PG_OUT = []
ROW5 = cut('Demonstrate elements of self- direction', 'in a highly proactive and effective manner.', P0)
for n, (cat, dom, about, fh, spans, verbs, paras, bens, qs) in enumerate(PG, 1):
    ty, ex = '4.14.b%d.typical' % n, '4.14.b%d.excellent' % n
    finds = [dict(ROW5), dict(ROW5)] if spans == 'row' else [cut(a, b, P0) for (a, b) in spans]
    base = dict(level='fheq:7', addressee='learner', about=about, domain=dom, award=MA, force='will', forceFrom='4.1')
    s(ty, **finds[0], **base, type='typical', rung='typical', verbs=verbs[0],
      appliesTo="postgraduate master's graduates in computing, at the typical rung",
      para=f"At the typical rung, master's graduates will {paras[0]}.",
      prac=f"Most master's graduates reach this in {cat.lower()}: they {paras[0]}.",
      ben=f"At the typical level on a master's, you will {bens[0]}.",
      aaw=(f"Treat this as the typical rung for taught master's graduates in computing in {cat} ({about}), at FHEQ level 7 "
           f"(FQHEIS and SCQF level 11); 4.14 links it to a Pass/Merit or Commendation. Cite it as {CITE}, para 4.14, postgraduate "
           f"table, {cat} row, typical column. The table has no threshold column, so do not invent one and do not apply this rung "
           f"to honours awards. Set it beside {ex}, the threshold requirement 4.13, the FHEQ master's descriptor qaa/fheq-2024/{fh} "
           f"and the reference step spine:7."),
      aad=(f"Raise this when a master's student asks what a solid result looks like in {about}, or a team calibrates master's "
           f"marking. To a student, describe it as the level most master's students reach; to staff, as the expected standard, "
           f"with the floor set by 4.13. Ask: '{qs[0]}' Avoid presenting it as the bare pass standard or reading the table aloud."))
    s(ex, **finds[1], **base, type='excellent', rung='excellent', verbs=verbs[1],
      appliesTo="postgraduate master's graduates in computing, at the excellent rung",
      para=f"At the excellent rung, master's graduates will {paras[1]}.",
      prac=f"Distinction-level work in {cat.lower()} usually shows this: graduates {paras[1]}.",
      ben=f"At the excellent level on a master's, you will {bens[1]}.",
      aaw=(f"Treat this as the excellent rung for taught master's graduates in {cat} ({about}), usually linked to a Distinction "
           f"(4.14), at FHEQ level 7 (FQHEIS and SCQF level 11). Cite it as {CITE}, para 4.14, postgraduate table, {cat} row, "
           f"excellent column. Do not claim every Distinction must show it in every category; 4.14 says not. Set it beside {ty}, "
           f"the FHEQ master's descriptor qaa/fheq-2024/{fh} and the reference step spine:7."),
      aad=(f"Raise this with a master's student aiming for a Distinction, or a team designing stretch tasks in {about}. To a "
           f"student, describe it as what the strongest master's work shows; to staff, as room assessment must leave at the top. "
           f"Ask: '{qs[1]}' Avoid implying that everyone must reach it."))
    GRADE[ex] = ty + '|stated'
    PG_OUT.append(dict(outcome=about + " (master's)", threshold='none', typical=ty, excellent=ex, basis='stated', domain=dom, award=MA))

# ------------------------------------------------------------------ themes, levels, relations
TH = {'1.11': 'theme:edi', '1.12': 'theme:edi', '1.15': 'theme:esd', '1.16': 'theme:esd', '1.18': 'theme:esd',
      '2.7': 'theme:accessibility', '2.8': 'theme:accessibility', '2.9': 'theme:accessibility'}
for _i in P:
    if _i.startswith('1.19.'):
        TH[_i] = 'theme:enterprise'

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.10; 4.2 (honours)'),
                  dict(id='fheq:7', role='cites', locator="D1, 2.12; 4.2; 4.12; 4.17 (integrated and taught master's)"),
                  dict(id='fqheis:10', role='cites', locator='D1, 2.10; 4.2; 4.3 (Annex D title); 4.17'),
                  dict(id='fqheis:11', role='cites', locator='D1, 2.12; 4.2; 4.17; 4.12 (as SCQF Level 11)')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent',
                           basis="stated (D1, 2.10: 'FHEQ Level 6; FQHEIS Level 10'; 4.2; 4.17); agrees with std:doc:qaa-fheq-2024-framework, Table 1"),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent',
                           basis="stated (D1, 2.12; 4.2; 4.12: 'FHEQ Level 7/SCQF Level 11'; 4.17); agrees with std:doc:qaa-fheq-2024-framework, S5 (shared descriptor)")])

EDI_P = ['1.4', '1.11', '1.12', '1.13', '1.14', '1.16', '1.19', '3.9', '3.10', '4.6', '4.14']
ACC_P = ['1.13', '1.14', '2.7', '2.8', '2.9']
ESD_P = ['1.4', '1.15', '1.16', '1.17', '1.18', '1.19', '3.10', '4.6', '4.14']
ENT_P = ['1.19', '2.17', '3.20', '4.6']
S6 = [dict(id='theme:edi', role='carries', carriedIn=EDI_P), dict(id='theme:accessibility', role='carries', carriedIn=ACC_P),
      dict(id='theme:esd', role='carries', carriedIn=ESD_P), dict(id='theme:enterprise', role='carries', carriedIn=ENT_P)]

S7 = [
    dict(rel='supersedes', target='std:doc:qaa-computing-2019-benchmarks (not yet ingested)', note='the fourth edition (2019), named in the back matter'),
    dict(rel='supersedes', target="std:doc:qaa-computing-masters-2019-benchmarks (not yet ingested)", note="the separate Computing (Master's) statement, merged here (front matter; 1.2)"),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='the degree outcome classification descriptions for honours (4.3)'),
    dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='the Frameworks and their qualification descriptors (2.6; 4.15, cited as the 2014 edition; references)'),
    dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS levels 10 and 11 (2.10; 2.12; 4.2; 4.17)'),
    dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='Education for Sustainable Development Guidance (1.15)'),
    dict(rel='refersTo', target='std:doc:qaa-enterprise-2018-guidance', note='Enterprise and Entrepreneurship Education guidance, to be read with 1.19'),
    dict(rel='refersTo', target="QAA Master's Degree Characteristics Statement (not yet ingested)", note='4.7; 4.16'),
    dict(rel='refersTo', target='QAA contract cheating guidance, Contracting to Cheat in Higher Education (not yet ingested)', note='3.18'),
    dict(rel='refersTo', target='QAA Advice and Guidance: Partnerships and Work-based Learning (not yet ingested)', note='2.16'),
    dict(rel='relatedTo', target='ACM and IEEE Computing Curricula 2020 and the discipline curriculum guidelines', note='1.2; 2.2; Appendix 3'),
    dict(rel='refersTo', target='British Computer Society accreditation requirements (not yet ingested)', note='4.2'),
    dict(rel='refersTo', target='United Nations, Sustainable Development Goals', note='1.4; 1.15; 1.17'),
    dict(rel='refersTo', target='OECD, Future of Education and Skills 2030', note='3.3'),
    dict(rel='refersTo', target='York University, Decolonising the Curriculum', note='1.14'),
]

SB1 = [
    'Computing studies how computation and computer technologies are understood, designed and exploited, joining elegant theory drawn from mathematics, engineering, psychology and design with the solving of practical problems (D1, 1.5).',
    "It underpins secure, reliable and usable systems of every size, is pervasive and often invisible and serves people's daily lives and careers (D1, 1.5).",
    'Its ways of working: disciplined problem-solving, design by choosing among alternatives with argued justification and control of complexity by abstraction and simplification and then integration (D1, 1.6).',
    'Innovation comes as much from foundational areas such as algorithmics and cryptography as from new technology (D1, 1.7).',
    'Seven discipline areas rest on computer science: computer science, computer engineering, software engineering, information technology, information systems, cybersecurity and data science; one degree may draw on several (D1, 2.1; Appendix 3).',
    'Specialist degrees such as networking, games, multimedia, AI or health informatics count as computing when a discipline area informs their content; merely using computers in a field does not (D1, 2.3).',
    'The statement sets graduate outcomes, not a syllabus; the ACM and IEEE curricula give detailed content (D1, 1.2; 1.9; 2.2).',
    'Problem-solving and the making of artefacts are core, learned through practical, team and capstone work and through placements (D1, 1.10; 3.4; 3.8; 3.19).',
    'Computing carries a particular responsibility to disabled people, since technology can remove barriers or raise them (D1, 2.7).',
]
_ENT_S = [i for i in P if i.startswith('1.19.')]
SB2 = [
    dict(theme='theme:edi', inThisSubject='a culturally responsive curriculum that represents all students, tackles the gender imbalance and guards against biased systems; an auditable list of EDI practices for courses to consider; EDI written into professional practice at every rung (D1, 1.11 to 1.14; 3.9; 3.10; 4.6; 4.14)',
         statements=['1.11', '1.12', '1.19.b9', '1.19.b40', '3.9', '3.10', '4.6.b6', '4.6.b6.typical', '4.6.b6.excellent', '4.14.b6.typical', '4.14.b6.excellent']),
    dict(theme='theme:accessibility', inThisSubject="computing's own responsibility to disabled people: universal access taught and practised, accessibility built into the software lifecycle and curricula designed for access beyond the statutory minimum (D1, 1.13; 1.14; 2.7 to 2.9)",
         statements=['2.7', '2.8', '2.9']),
    dict(theme='theme:esd', inThisSubject='the SDGs (4, 5 and 8 above all), the environmental cost of data centres, hardware and e-waste, social and economic sustainability, four ways of embedding ESD and sustainability written into professional practice at every rung (D1, 1.4; 1.15 to 1.18; 3.10; 4.6; 4.14; Appendix 2)',
         statements=['1.15', '1.16', '1.18', '1.19.b3', '1.19.b24', '3.10', '4.6.b6', '4.6.b6.typical', '4.6.b6.excellent', '4.14.b6.typical', '4.14.b6.excellent']),
    dict(theme='theme:enterprise', inThisSubject="read as employability in its widest sense: generic, agile, remote working, resilience and enterprise skills, a common core of subject skills, interdisciplinary thinking, career planning and employers' expected core skills; entrepreneurial capstones; teamwork at every rung (D1, 1.19; 2.17; 3.20; 4.6)",
         statements=_ENT_S + ['3.20', '4.6.b5', '4.6.b5.typical', '4.6.b5.excellent']),
]
SB3 = dict(
    areas=[dict(component='2.1', gloss='the seven discipline areas, outlined in Appendix 3, from computer science to data science'),
           dict(component='2.2', gloss='content informed by the ACM and IEEE curricula rather than a syllabus here'),
           dict(component='2.3', gloss='specialist foci such as networking, games, multimedia, AI and health informatics')],
    practices=[dict(component='1.10', kind='learning', gloss='placements and internships'),
               dict(component='2.15', kind='learning', gloss='apprenticeships, placements, live projects and study abroad through partnership'),
               dict(component='3.4', kind='teaching', gloss='balanced skills, personalised learning, capstone activity and teamwork'),
               dict(component='3.5', kind='learning', gloss='evidencing competence in applied, often work-based, contexts'),
               dict(component='3.6', kind='learning', gloss='reflection, portfolios and personalised assessment for learner agency'),
               dict(component='3.7', kind='teaching', gloss='varied approaches building capability and competence'),
               dict(component='3.8', kind='learning', gloss='repeated practical coursework of real scale'),
               dict(component='3.9', kind='teaching', gloss='reflective, innovative problem-solving with varied tools'),
               dict(component='3.16', kind='learning', gloss='applied learning, team projects and industry or research partners'),
               dict(component='3.17', kind='assessment', gloss='varied, authentic, practical assessment'),
               dict(component='3.18', kind='assessment', gloss='academic integrity by design, with authorship checkpoints'),
               dict(component='3.19', kind='assessment', gloss='a capstone bringing the course together'),
               dict(component='3.20', kind='assessment', gloss="capstone formats beyond the dissertation; research literature at master's level")])

SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.5', award=HON, items=6),
           dict(rung='typical', leadIn='4.5', award=HON, items=6),
           dict(rung='excellent', leadIn='4.5', award=HON, items=6),
           dict(rung='threshold', leadIn='4.13', award=MA, items=0),
           dict(rung='typical', leadIn='4.14', award=MA, items=6),
           dict(rung='excellent', leadIn='4.14', award=MA, items=6),
           dict(rung='threshold', leadIn='4.17', award=IM, items=0)],
    rungBases=("Two unnumbered tables. Undergraduate (after 4.6): six outcome categories, each a row with a threshold, typical and "
               "excellent cell; 4.5 requires threshold in every category and maps threshold to a third, typical to a 2:1 or 2:2 and "
               "excellent to a first. Postgraduate (after 4.14): six categories with typical and excellent cells only; 4.13 requires "
               "threshold in every relevant category by reference to the undergraduate descriptors (no master's threshold text), "
               "mapped to a Pass; typical maps to Pass/Merit or Commendation, excellent to a Distinction. Integrated master's (4.17): "
               "threshold at both levels, no table of its own. Threshold items: 6 in all; typical 12; excellent 12."),
    outcomeLists=[dict(leadIn='1.19', gloss="employability skills: generic, agile working, remote working, resilience, enterprise, a common core of subject skills, interdisciplinary thinking, careers and employers' expected core skills",
                       items=len(_ENT_S), award=ALL)],
    outcomes=UG_OUT + PG_OUT)
SB4A_FULL = []
SB5 = [
    dict(body='British Computer Society (BCS, The Chartered Institute for IT)', says='accredits many computing degrees, so its professional competency standards will often apply (D1, 4.2)', requirements='not yet ingested: listed in Part E'),
    dict(body='Institute for Apprenticeships and Technical Education', says='named among the bodies whose competency standards apply to accredited courses and apprenticeships (D1, 4.2)', requirements='not yet ingested: listed in Part E'),
    dict(body='Engineering Council and its recognised accreditors', says='other accreditors recognised by the Engineering Council may accredit computing degrees, with their standards applying (D1, 4.2)', requirements='not yet ingested: listed in Part E'),
    dict(body='sector skills bodies (unnamed)', says='named in general terms among accrediting bodies (D1, 4.2)', requirements='not yet ingested: no body named (Part E)'),
    dict(body='Association for Computing Machinery (ACM) and Institute of Electrical and Electronics Engineers (IEEE)', says='maintain the curricula (Computing Curricula 2020 and discipline guidelines) to be used for detailed content and course design (D1, 1.2; 2.2; Appendix 3)', requirements='not yet ingested: listed in Part E'),
    dict(body='professional, statutory and regulatory bodies (PSRBs), unnamed', says='may evaluate and accredit courses with professional or vocational outcomes, by site visits and desk review (D1, 2.21; front matter)', requirements='not yet ingested: no body named (Part E)'),
]
SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion', carriedIn=EDI_P, statements=SB2[0]['statements']),
            dict(id='theme:accessibility', named='Accessibility (a section 2 heading; not among the front matter themes)', carriedIn=ACC_P, statements=SB2[1]['statements']),
            dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=ESD_P, statements=SB2[2]['statements']),
            dict(id='theme:enterprise', named='Entrepreneurship and enterprise education (front matter: employability, entrepreneurship and enterprise education)', carriedIn=ENT_P, statements=SB2[3]['statements'])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.6', '2.10', '2.12', '4.2', '4.3', '4.12', '4.15', '4.17']),
                dict(framework='other: FQHEIS', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.10', '2.12', '4.2', '4.3', '4.17']),
                dict(framework='scqf', levels=['fqheis:11'], citedIn=['4.12'])],
    bodies=[dict(body='British Computer Society', citedIn=['4.2']),
            dict(body='Institute for Apprenticeships and Technical Education', citedIn=['4.2']),
            dict(body='Engineering Council', citedIn=['4.2']),
            dict(body='sector skills bodies', citedIn=['4.2']),
            dict(body='ACM', citedIn=['1.2', '2.2']),
            dict(body='IEEE', citedIn=['1.2', '2.2']),
            dict(body='professional and regulatory bodies, unnamed', citedIn=['2.21'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.3'],
             role='common descriptions of the four honours classes (1st, 2:1, 2:2, 3rd), for judging achievement above threshold'),
        dict(document='std:doc:qaa-fheq-2024-framework', named='The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies (cited in its 2014 edition)', citedIn=['2.6', '4.15'],
             role="qualification descriptors every course meets; the length of integrated master's"),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='The Education for Sustainable Development Guidance (QAA and Advance HE, 2021)', citedIn=['1.15'],
             role='teaching approaches for sustainable development'),
        dict(document='std:doc:qaa-enterprise-2018-guidance', named='Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (QAA, 2018)', citedIn=['1.19'],
             role='to be read with the employability skills'),
        dict(document='not yet ingested: listed in Part E', named="QAA characteristics statement on master's degrees", citedIn=['4.7', '4.16'], role="kinds of master's and the integrated master's characteristics"),
        dict(document='not yet ingested: listed in Part E', named="QAA's contract cheating guidance", citedIn=['3.18'], role='assessment integrity'),
        dict(document='not yet ingested: listed in Part E', named='Partnerships and Work-based Learning (QAA Advice and Guidance)', citedIn=['2.16'], role='further advice on partnerships'),
        dict(document='not yet ingested: listed in Part E', named='other Subject Benchmark Statements (unnamed)', citedIn=['1.8', '2.4'], role='joint and interdisciplinary courses'),
    ])

B1 = [
    dict(slug='computing', definition='any purposeful activity that uses, exploits or creates computing equipment and services (D1, 3.1)',
         beneficiaryDefinition='anything you do on purpose that uses, makes or exploits computers and computing services', scopeNote='the statement\'s working definition of its subject', category='unknown', practices=['computing']),
    dict(slug='computing-competence', definition='the application of computing capabilities in applied contexts, often work-based, as distinct from capability shown through learning outcomes (D1, 3.5; 3.7)',
         beneficiaryDefinition='being able to use your computing skills in real settings, such as at work', scopeNote='competency; capability is the related term', category='unknown', practices=['computing', 'education']),
    dict(slug='capstone-activity', definition='a culminating activity that brings together the knowledge and practical and analytical skills of the course, as a project, end-point assessment, paper, portfolio or entrepreneurial work (D1, 3.19; 3.20)',
         beneficiaryDefinition='a final major piece of work that pulls together what you have learned', scopeNote='often near the end of the course', category='unknown', practices=['education']),
    dict(slug='learner-earner', definition='a person moving between study and work through life, building on achievements without repeating study (D1, 3.1; 3.2; 3.6)',
         beneficiaryDefinition='someone who keeps learning and working at the same time or in turns through life', scopeNote='used with micro-credentials and lifelong learning', category='unknown', practices=['education']),
    dict(slug='entrepreneurship-and-enterprise-education', definition='in this statement, read as employability in its widest sense (D1, 1.18 to 1.19)',
         beneficiaryDefinition='learning that prepares you for work and for making things happen', scopeNote='a cross-cutting theme', category='unknown', practices=['education']),
    dict(slug='externality', definition='the use of people from outside the provider, such as external reviewers and examiners, to check standards and content (D1, 2.19; 2.20)',
         beneficiaryDefinition='outside experts checking that your course meets the standards', scopeNote='quality assurance', category='unknown', practices=['education']),
]
B2A = [
    dict(concept='computing', form='Computing', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='computing-competence', form='computing competencies', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='capstone-activity', form='capstone activity', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='learner-earner', form='learner-earners', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
    dict(concept='entrepreneurship-and-enterprise-education', form='entrepreneurship and enterprise education', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='externality', form='Externality', lang='en', partOfSpeech='noun', termStatus='preferred', register='formal'),
]
B4 = []
B5 = []
D3 = []

E = [
    'Rung shape (new against Psychology): the rungs are two unnumbered tables, each listing six outcome categories in rows with one cell per rung. The undergraduate table follows 4.6 and has threshold, typical and excellent columns; its cells take the ids 4.6.b<n> (threshold), 4.6.b<n>.typical and 4.6.b<n>.excellent, our ids hung on the nearest issuer paragraph (4.6 is only a cross-reference). The postgraduate table follows 4.14 and has typical and excellent columns only; its cells take 4.14.b<n>.typical and 4.14.b<n>.excellent, with no bare id because there is no threshold cell. For P3.',
    "The postgraduate table has no threshold column: 4.13 requires threshold attainment 'with reference to the descriptors outlined in Undergraduate standards', so the master's threshold is read against the honours table; and 4.14 says the typical descriptor goes with 'the typical threshold performance', an unclear phrase. SB4 records the master's threshold rung with items 0. For Abbott.",
    'Integrated master\'s (4.17): threshold required at both FHEQ 6 and 7 (FQHEIS 10 and 11) across "all descriptors ... in paragraphs 4.2 and 4.3"; 4.2 and 4.3 hold no descriptors, so the pointer looks like a slip carried from an earlier edition (perhaps the old sections 4.2 and 4.3 or the two tables). Not a statement (rule 3); SB4 records the rung with items 0.',
    'gradeOf: 18 links (each typical to its threshold, each excellent to its typical, in both tables), recorded as stated because the issuer pairs the cells in one row by category (batch 1 convention, paired cells). No link runs across the two tables.',
    'Rungs mapped to classes by the issuer (4.5; 4.13; 4.14): threshold to a third, typical to a 2:1 or 2:2, excellent to a first; for master\'s, threshold to a Pass, typical to Pass/Merit or Commendation, excellent to a Distinction. The agent instructions use these as stated; the Annex D pairings by strand (knowledge, cognitive, practical, transferable) are ours, inferred.',
    'Force: threshold cells take force threshold, since 4.5 defines the threshold as the minimum for honours (forceFrom 4.5). Typical and excellent cells in both tables take will from 4.1 ("will have demonstrated"; benchmark standards defined for all awards), as in Psychology and Agriculture; the issuer\'s own lead-ins for these rungs are descriptive ("defines outcomes usually associated with"). For P3.',
    'Split cells: a page break splits the practical skills row of the undergraduate table (4.6.b4) and the self-directed learning row of the postgraduate table (4.14.b5); each rung record in those rows takes one span covering the whole row, so its source holds its own words with its neighbours\' interleaved.',
    '1.19 employability skills: the lead-in says it is "imperative" that employability skills are embedded, with the list "acting as a guide"; the 26 skill items under Generic skills, Agile working, Remote working, Resilience, Entrepreneurship and enterprise education and the last two of the common core (1.19.b1 to b24, b27, b28) have no modal of their own and are recorded with force describes. "Imperative" is an obliging word outside the five: for Abbott whether it makes these must.',
    "1.19 under Employers' perspective: the five core skills 1.19.b38 to b42 take will from their lead-in 1.19.b37 (\"Employers will expect graduates to be able to demonstrate core skills\"), given as forceFrom.",
    '2.6: the lead-in calls its items "fundamental requirements associated with all degree courses"; "requirements" reads as must, but it is none of the five and the builder\'s force check matches only must and required, so items b1, b2, b4, b5 and b6 (plain present) are recorded as describes with forceFrom 2.6; b3 has its own should and b7 its own will. For Abbott: whether "requirements" counts as must; if so the check needs widening before the force can be raised.',
    '3.15: "Computing graduates need to have acquired ..." ("need to", outside the five) recorded as describes. 3.3 ("it is important ... to consider"), 1.13 ("is key"), 2.17 and 3.11\'s "it is important that progression reflects" are obliging words outside the five, not recorded as force.',
    'Not recorded as statements: the 14 items of 1.14 (the issuer calls them "EDI statements" for audit against Appendix 1, but their lead-in is "could consider", which obliges nothing); the 8 items of 2.14 ("there may need to be"); 1.17\'s list of common ESD approaches; 1.19.b29 and 1.19.b31 (descriptive, "may", "could"). 1.14 especially is for Abbott\'s P3.',
    'Plain-present provider norms and descriptive will, not recorded (template open point 5): 1.9 and 3.2 (predictions with "will continue"), 2.18 ("will draw on" external reference points, routine practice), 2.20 ("typically, external examiners will be asked"), 4.2 ("all professional competency standards will apply in many instances", context), 4.10 (master\'s graduates "are equipped"), 4.15 and 4.16 (descriptive).',
    'Levels: fheq:6, fheq:7, fqheis:10 and fqheis:11 are all stated (2.10, 2.12, 4.2, 4.17); 4.12 names "SCQF Level 11", recorded as fqheis:11 under a separate scqf entry in SB6. CQFW is not cited. Statements in sections 1 to 3 that apply to all three awards take level fheq:6 (the lowest award\'s level) with award listing all three; their agent instructions name FHEQ 6 and 7.',
    'Awards: the statement covers bachelor\'s with honours, integrated master\'s and taught postgraduate master\'s; degree apprenticeships and part-time courses (1.1; 4.1) are modes of those awards, not separate awards. Research master\'s are mentioned only in 4.9.',
    'Subject codes: the statement states none; all seven in front matter (CAH11-01; HECoS 100366, 100162, 100374, 100367, 100371, 100376) are basis inferred, as are the specialism codes in S2 (100365, 101267, 100737, 100359, 100994). Computer engineering maps to computer systems engineering (100162, CAH10-01-08, an engineering code); data science has no HECoS term found. For P3.',
    'Themes: accessibility is a section 2 heading, not one of the front matter themes. Employability is named with enterprise in the front matter and in 1.18/1.19 and recorded under theme:enterprise. The heading and first sentence of the enterprise section fall at the end of component 1.18 in the skeleton; 1.18\'s record is cut by find to its own sentence. No generative AI section.',
    'Skeleton theme hits not kept: theme:edi in 1.10 and 2.22 and theme:accessibility in 2.6, 1.14 and theme:esd in 1.14 come only from the next sub-heading caught at the end of those components; theme:accessibility in 4.14 is "communicate ... in an accessible and impactful way", not the theme.',
    'Bodies: BCS, the Institute for Apprenticeships and Technical Education, the Engineering Council (and its recognised accreditors) and sector skills bodies (4.2); ACM and IEEE (1.2; 2.2); PSRBs in general (2.21; front matter). Not bodies of this kind, and not recorded in SB5: the United Nations (1.4; 1.15; 1.17), the OECD, UNESCO, the World Bank and the International Labour Organization (3.3), the Office for Students (front matter) and the Disabled Students\' Commission (back matter). None of the bodies\' requirements is ingested.',
    'Shared documents not yet ingested: QAA\'s Master\'s Degree Characteristics Statement (4.7; 4.16), the contract cheating guidance (3.18), the Partnerships and Work-based Learning advice (2.16), the Characteristics Statement: Higher Education in Apprenticeships (references list only), the two 2019 statements superseded and the ACM and IEEE curricula. The Frameworks are cited in their 2014 edition; we point to std:doc:qaa-fheq-2024-framework (inferred as the current edition).',
    'Appendices 1 to 3 fall inside the skeleton\'s back-matter component (membership of the advisory groups); they are read for SB1, SB2 and SB3 and cited as (D1, Appendix n). Appendix 1\'s templates are blank in the held text.',
    'Text faults noted, not acted on: 4.6 cites "paragraphs 4.7-4.17", though 4.15 to 4.17 are on integrated master\'s; 4.14 "the typical threshold performance"; 1.14.b12 "Decolonising of curriculum" (the reference list says "Decolonising the Curriculum"); 3.3 "twenty-f irst" and 3.17 "Assessment f or" (extraction spacing).',
    'Patterns that differ from Psychology: one statement for three awards; a master\'s table with no threshold column; rung tables rather than lists; a long employability skills list in section 1 with no modal; "fundamental requirements" (2.6) and "imperative" (1.19) as obliging words outside the five; a must on accessibility (2.8) and on integrated specialist master\'s (3.14).',
    'S9 commentary not researched in P1.',
]
