# Judgement fields for run 0130, QAA Social Work 2026 (std). Keys are S4 ids under qaa/social-work-2026/.
# Read whole from wkspc2601-library/txt/qaa-2026-social-work-subject-benchmark-statement-standard.norm.txt; versions written fresh from the held text alone.
HON = "bachelor's with honours"
IMA = "integrated master's"
MA = "master's"
SID = 'qaa/social-work-2026/'
CITE = 'QAA (2026), Social Work Subject Benchmark Statement, para '

def sid(*ids):
    return ', '.join(SID + i for i in ids)

META = dict(
    run='0130', p1='2026-10-03 18:42',
    title='Subject Benchmark Statement Social Work',
    heading='Subject Benchmark Statement: Social Work (QAA, April 2026)',
    edition='April 2026 (fifth edition)', published='2026-04',
    status='current', supersedes='Subject Benchmark Statement: Social Work, fourth edition (2019; minor update of the 2016 statement)',
    subjects=[dict(scheme='hecos', code='100503', label='social work', basis='stated'),
              dict(scheme='cah', code='CAH15-04-01', label='social work', basis='stated')],
    awards=[HON, IMA, MA], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, 2026 revision with five cross-cutting themes (EEDI; accessibility; ESD; EEE; generative AI)',
    partsB='partial: no glossary in the document (it sends readers to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what a social work student must have shown by the end of an honours degree, an integrated "
                     "master's or a taught master's: one rung only, the minimum threshold, set out for honours as four categories (knowledge "
                     "and understanding, demonstrable skills, values and ethics, the regulator's requirements) with 34 lettered outcomes, and "
                     "for the two master's awards as stronger headline statements that point back to those outcomes. Reach for it when designing, "
                     "approving, reviewing or describing a social work course. It sits under the four UK regulators, whose approval and "
                     "registration rules are separate, and it is not a regulatory requirement in England."),
    summary=("Published by QAA on 16 April 2026 as the fifth edition, the statement sets social work in the IFSW global definition, describes "
             "the subject's purposes and distinctive features, the regulators of the four nations and their approval and registration "
             "rules, content, teaching, learning and assessment, and minimum threshold standards for bachelor's degrees with honours (FHEQ 6, "
             "SCQF 10), integrated master's and postgraduate taught master's degrees (FHEQ 7, SCQF 11). It states no typical or excellent "
             "lists: it maps threshold to a third, typical to a 2.2 or 2.1 and excellent to a first and refers to Annex D of the Frameworks "
             "for the classes. It treats five cross-cutting themes: equity, equality, diversity and inclusion; accessibility and the needs "
             "of disabled students; education for sustainable development; employability, entrepreneurship and enterprise education; and "
             "generative artificial intelligence. Bodies named: Social Care Wales, Social Work England, the Northern Ireland Social Care "
             "Council, the Scottish Social Services Council, the Professional Standards Authority and the IFSW."),
    authority=("reference: a sector-owned reference point (D1, front matter); in England not a sector-recognised standard under the Office "
               "for Students' framework; part of the quality arrangements in Scotland, Wales and Northern Ireland (D1, front matter: "
               "Relationship to legislation). Approval and registration rest with the four regulators (D1, 1.4, 2.9 to 2.22)"))

S2 = dict(
    governs=("what a Social Work graduate can be expected to know, do and understand at the end of their studies, and the nature of awards in "
             "the subject, as minimum threshold standards for honours, integrated master's and postgraduate taught master's degrees "
             "(D1, front matter: About this Statement; 4.3)"),
    awards=["bachelor's degrees with honours", "integrated master's degrees", "postgraduate taught master's degrees",
            "postgraduate certificates and diplomas (the master's standards can also apply, 4.15)", "degree apprenticeships (named, 2.24)"],
    levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
    statedScope=('"This Subject Benchmark Statement sets out the minimum threshold standards that a Social Work student will have '
                 'demonstrated when they are awarded: a bachelor\'s degree with honours, an integrated master\'s degree, a postgraduate '
                 'taught master\'s degree." (D1, 4.3)'),
    statedSubjects=[
        dict(name='Social Work', locator='(D1, title; 1.1; 4.1)', kind='subject',
             codes=[dict(scheme='hecos', code='100503', label='social work'), dict(scheme='cah', code='CAH15-04-01', label='social work')]),
        dict(name="Bachelor of Science (BSc) or Arts (BA) degree ... postgraduate conversion course ... postgraduate diploma (PgDip) ... Master of Science (MSc or MSci) or Arts (MA) ... degree apprenticeship",
             locator='(D1, 2.24)', kind='programme title', codes=[dict(scheme='hecos', code='100503', label='social work')]),
        dict(name='honours-level degree in Social Work (the professional qualification for social workers, probation officers and education welfare officers in Northern Ireland)',
             locator='(D1, 2.18)', kind='programme title', codes=[dict(scheme='hecos', code='100503', label='social work')]),
        dict(name='generic honours degree in Social Work, or an equivalent postgraduate award (Scotland)', locator='(D1, 2.21)',
             kind='programme title', codes=[dict(scheme='hecos', code='100503', label='social work')]),
    ])

SECTIONS = {'1': 'Context and purposes of a Social Work degree', '2': 'Distinctive features of a Social Work course',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.1', '1.6', 'Context and purposes of a Social Work degree'),
       ('1.7', '1.11', 'Purposes and characteristics of a Social Work degree'),
       ('1.12', '1.21', 'Equity, equality, diversity and inclusion'),
       ('1.22', '1.25', 'Accessibility and the needs of disabled students'),
       ('1.26', '1.33', 'Education for sustainable development'),
       ('1.34', '1.44', 'Employability, entrepreneurship and enterprise education'),
       ('1.45', '1.48', 'Generative artificial intelligence'),
       ('2.1', '2.8', 'Design'),
       ('2.9', '2.9', 'Regulatory bodies'),
       ('2.10', '2.12', 'Regulatory bodies: Cymru/Wales'),
       ('2.13', '2.15', 'Regulatory bodies: England'),
       ('2.16', '2.19', 'Regulatory bodies: Northern Ireland'),
       ('2.20', '2.22', 'Regulatory bodies: Scotland'),
       ('2.23', '2.27', 'Progression'),
       ('2.28', '2.32', 'Flexibility'),
       ('2.33', '2.37', 'Partnership'),
       ('2.38', '2.42', 'Monitoring and review'),
       ('3.1', '3.5', 'Content'),
       ('3.6', '3.7', 'Teaching and learning'),
       ('3.8', '3.9', 'Assessment'),
       ('4.1', '4.5', 'Introduction'),
       ('4.6', '4.8', 'Classification'),
       ('4.9', '4.11', "Bachelor's degree with honours: Minimum standards"),
       ('4.12', '4.14', "Integrated master's degree: Threshold level (3rd class degree)"),
       ('4.15', '4.15', "Postgraduate master's degree benchmark standards"),
       ('4.16', '4.17', "Postgraduate master's degree: Threshold level (pass degree)")]

G = {
    '1.1': 'the IFSW global definition of the profession as the frame for UK social work',
    '1.2': 'the statement as a route map for education grounded in social justice, inclusion and ethical, reflective practice',
    '1.3': 'professional qualification tied to an academic level; honours as the minimum route into the profession',
    '1.4': 'statutory registration since 2000; the protected title and the four national regulators (listed)',
    '1.5': 'regulators approve courses and regulate practitioners to protect the public',
    '1.6': 'regulators\' standards shape curriculum and assessment',
    '1.7': 'an academic discipline applied through practice; integrated knowledge, skills, values and research',
    '1.8': 'complex, uncertain settings; what social workers must be equipped for and expected to do (S4)',
    '1.9': 'interagency and multi-agency working and knowledge of other roles',
    '1.10': 'practice as core learning, in placements and other experiential settings',
    '1.11': 'regulators\' stipulations inform design, content and practice learning',
    '1.12': 'the scope of EEDI and intersectionality; EEDI central to the subject',
    '1.13': 'inclusive learning communities and reference points for equality (listed)',
    '1.14': 'the duty to make reasonable adjustments, linked to IFSW principles (S4)',
    '1.15': 'self-identity and intersectionality; widening access; awarding gaps; cross-cutting topics for curricula (listed)',
    '1.16': 'a diverse workforce and staff; reflecting on one\'s own privileges and barriers',
    '1.17': 'the legal duty on courses and placements to adjust (S4); QAA guidance on inclusive communities',
    '1.18': 'examples of how courses address EEDI (listed)',
    '1.19': 'anti-oppressive and anti-racist values built into design, content, teaching and assessment (listed)',
    '1.20': 'dismantling oppression and racism, with a commitment against anti-Black racism',
    '1.21': 'examples of anti-racist and decolonising course practice (listed)',
    '1.22': 'equality and Welsh-language law across the four nations; a proactive approach to access',
    '1.23': 'accessible environments as legal duty and professional value',
    '1.24': 'accessible design and the expectation of anticipatory adjustments (S4)',
    '1.25': 'how courses secure equitable access while keeping standards (listed)',
    '1.26': 'social work\'s part in sustainable development and climate impacts; three generations of rights',
    '1.27': 'graduates as global citizens aware of climate and environmental effects',
    '1.28': 'a value-based profession; reflecting on social and environmental impacts',
    '1.29': 'ESD and the UN SDGs as shared social work goals',
    '1.30': 'UNESCO key competencies for the SDGs, embedded in course design and assessment',
    '1.31': 'ESD content and action-oriented, transformative pedagogy',
    '1.32': 'IFSW support for the SDGs; ESD as a lens, citing the QAA and Advance HE ESD guidance',
    '1.33': 'inclusion and leaving no-one behind; applying skills to sustainability problems',
    '1.34': 'employability, enterprise and entrepreneurship education and its benefits',
    '1.35': 'practice-based learning and links with outside organisations',
    '1.36': 'entrepreneurship education for a self-directed professional life',
    '1.37': 'the entrepreneurial mindset in social work (listed)',
    '1.38': 'what course experiences offer for careers and enterprise (listed)',
    '1.39': 'enterprise behaviours',
    '1.40': 'enterprise attributes',
    '1.41': 'skills for professional practice',
    '1.42': 'digital competence and transferable skills',
    '1.43': 'benefits of enterprise learning for confidence and career pathways',
    '1.44': 'enterprise skills employers prize; the aim of competent, confident entrants',
    '1.45': 'AI and generative AI in society and practice; procedures for authenticity (S4)',
    '1.46': 'engaging with technologies in many spaces; the need to navigate them (S4)',
    '1.47': 'what engagement with generative AI includes (listed)',
    '1.48': 'values guide technology use; technology does not replace human relationships (S4)',
    '2.1': 'distinctive focus on practice in complex situations; partnership with employers, people with lived experience and students',
    '2.2': 'integrated study of knowledge, skills, values and research; analytic and practical understanding',
    '2.3': 'preparing for work with many people and groups; including care-experienced students',
    '2.4': 'values and ethics, difficult decisions and the study of dilemmas as a core requirement (S4)',
    '2.5': 'the subject\'s heritage and its contested scope',
    '2.6': 'different and changing welfare contexts in the UK and internationally',
    '2.7': 'competing views of social work: justice, care and order',
    '2.8': 'a changing profession; qualified workers need to understand and lead change (S4)',
    '2.9': 'regulators\' standards shape design and assessment',
    '2.10': 'the Welsh regulator, its history and the protected title',
    '2.11': 'approval by Social Care Wales; the Welsh qualification framework and context (S4)',
    '2.12': 'student registration with Social Care Wales and its Code (S4)',
    '2.13': 'the regulator for England and the protected title',
    '2.14': 'approval by Social Work England against its standards (S4); oversight by the Professional Standards Authority',
    '2.15': 'registration after an approved course; post-qualifying statements and the supported first year',
    '2.16': 'the Northern Ireland regulator and the protected title',
    '2.17': 'the Northern Ireland framework specification; learning on political violence and integrated care (S4)',
    '2.18': 'honours as the professional qualification in Northern Ireland; student registration; the assessed year (S4)',
    '2.19': 'standards of conduct and practice for registrants and students',
    '2.20': 'the Scottish regulator and the protected title',
    '2.21': 'SSSC approval, codes and registers; the honours or postgraduate award needed to qualify (S4)',
    '2.22': 'registration with the SSSC after an approved programme',
    '2.23': 'progression through levels to the threshold skills (FHEQ 6 and 7; SCQF 10 and 11) (S4)',
    '2.24': 'routes and awards, including apprenticeships; integrated practice learning in all (S4)',
    '2.25': 'design flexibility within the broad base of the discipline',
    '2.26': 'seminal and contemporary theory and culturally diverse viewpoints',
    '2.27': 'ethics central to design; students apply ethics to themselves and judge others (S4)',
    '2.28': 'duration and level of honours in England, Wales and Northern Ireland',
    '2.29': 'Scottish ordinary and honours degrees and the Scottish MA',
    '2.30': 'integrated master\'s: length and the two levels it meets',
    '2.31': 'part-time credit equivalence',
    '2.32': 'flexible delivery modes (listed)',
    '2.33': 'delivery with partners; the statement\'s role for partners',
    '2.34': 'partnership with people with lived or living experience (S4)',
    '2.35': 'partnership with practice learning providers; written agreements; stakeholder views in design (S4)',
    '2.36': 'courses aligned with the relevant regulator\'s standards (S4)',
    '2.37': 'partnership benefits and the student voice',
    '2.38': 'routine monitoring and periodic review by awarding bodies',
    '2.39': 'externality and external reviewers (S4)',
    '2.40': 'external examining and its use of the statement',
    '2.41': 'stakeholders in monitoring and review',
    '2.42': 'approval and ongoing monitoring by regulators (S4)',
    '3.1': 'frameworks in design; principles for content; co-production and decolonised content (S4)',
    '3.2': 'knowledge, skills, values and behaviours for reflective practitioners',
    '3.3': 'typical content: research, theory, methods, values, policy, law and leadership',
    '3.4': 'practice-based learning and the integration of knowledge into practice (S4)',
    '3.5': 'sequencing for incremental learning by level',
    '3.6': 'scaffolded teaching, growing responsibility and a range of facilitators (S4)',
    '3.7': 'five learning themes and the methods that carry them',
    '3.8': 'principles and purposes of assessment; readiness and fitness for practice (S4)',
    '3.9': 'a diverse range of assessment methods and assessors',
    '4.1': 'a professional qualification at undergraduate or postgraduate level; academic and practice requirements (S4)',
    '4.2': 'threshold standards are not competence standards; equality guidance for providers (S4)',
    '4.3': 'lead-in: the three awards for which minimum threshold standards are set (scope, not an outcome list)',
    '4.4': 'standards shown over time show the expected range of attainment',
    '4.5': 'practice requirements common to all routes; academic levels 6 and 7; regulators\' outcomes also apply (S4)',
    '4.6': 'most students exceed the threshold; providers decide the evidence',
    '4.7': 'Annex D for honours classes; threshold, typical and excellent mapped to degree classes',
    '4.8': 'classes for integrated master\'s and merit and distinction for master\'s; marking schemes (S4)',
    '4.9': 'honours graduates must reach at least threshold across four categories (S4)',
    '4.10': 'threshold criteria follow marking schemes; practice days set by the regulator (S4)',
    '4.11': 'lead-in: the honours threshold in four categories, with 34 lettered outcomes (S4, 38 records)',
    '4.12': 'what an integrated master\'s adds, meeting both undergraduate and master\'s standards (S4)',
    '4.13': 'integrated master\'s graduates must reach at least threshold, as in 4.11 (S4)',
    '4.14': 'lead-in: the integrated master\'s threshold in four categories (S4, 6 records)',
    '4.15': 'the master\'s standards also apply to postgraduate certificates and diplomas',
    '4.16': 'master\'s graduates must reach at least threshold across outcome categories (S4)',
    '4.17': 'lead-in: the postgraduate master\'s threshold in four categories (S4, 8 records)',
}
CTYPE = {'3.1': 'area', '3.2': 'area', '3.3': 'area', '3.4': 'practice', '3.6': 'practice', '3.7': 'practice', '3.8': 'practice', '3.9': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points',
         kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='none', heading='Contents', kind='contents'),
    dict(number='5', heading='List of references and further resources', kind='references'),
    dict(number='6', heading='Membership of the Advisory Group', kind='acknowledgements'),
    dict(number='none', heading='Fifth Edition; publication date; copyright notice', kind='other: back matter, read for S1 and S8'),
]

P = {}
def s(i, **k):
    P[i] = k

# ---------------------------------------------------------------- obliging and outcome paragraphs (sections 1 to 4)
s('1.8', type='expectation', rung='none', force='must', level='none', appliesTo='social workers, and so those qualifying',
  addressee='learner', verbs=['equipped', 'engage', 'demonstrate', 'analyse', 'manage', 'lead'], about='equipped for complexity and able to lead change',
  domain='understanding', award='none',
  para=("Because the work takes place amid uncertainty, complexity and ambiguity, social workers must have the knowledge and skills to cope with it; "
        "they are also expected to take a critical part in debate about what the profession is for and to show they can analyse, adjust to, "
        "manage and in time lead change."),
  prac=("Courses prepare students for settings marked by uncertainty and ambiguity: social workers must hold the knowledge and skills these demand, "
        "and are expected to debate the purpose of the profession critically and to show they can handle and eventually lead change."),
  ben=("As a social worker you must be ready for situations that are uncertain, complex and unclear. You will be expected to question what "
       "social work is for and to show you can make sense of change, adapt to it, manage it and, later on, lead it."),
  aaw=("Treat this as a statement of what the profession must equip people for, not as a numbered outcome of any award. Cite it as " + CITE + "1.8. "
       "Do not turn it into a threshold outcome or claim it sets a level. Set it beside " + sid('2.8', '4.11.x', '4.11.cc') + " and spine:6 in std:ref:uk-framework."),
  aad=("Raise it when a student or team talks about uncertainty in practice or about leading change. With a student, put it as 'you'; "
       "with staff, as what the course must prepare people for. Ask: 'Where have you had to act without a clear answer, and what helped?' "
       "Avoid quoting the paragraph at length or treating leadership of change as something a new graduate must already show."))

s('1.14', type='requirement', rung='none', force='describes', level='none', appliesTo='course providers', addressee='provider',
  verbs=['make', 'provide'], about='duty to make reasonable adjustments', domain='none', award='none',
  para=("Course providers carry a duty to adjust reasonably for students so the learning environment is accessible to everyone, those with "
        "protected characteristics included, in keeping with the IFSW principles of justice, rights, shared responsibility and respect for difference."),
  prac=("Make reasonable adjustments so that every student, including those with protected characteristics, can learn in an accessible setting; "
        "the statement ties this duty to the profession's own principles as well as to law."),
  ben=('n/a', 'a duty on the provider; the student meets its effect, not a standard to reach'),
  aaw=("Describe this as a duty on the course provider, worded by the issuer as a 'duty' (recorded here as describes, Part E). Cite it as " + CITE + "1.14. "
       "Do not present it as a student outcome or as the statement creating a legal duty of its own. Set it beside " + sid('1.17', '1.24') + "."),
  aad=("Raise it with a programme team reviewing access or adjustments. Frame it as the provider's duty, in plain terms. Ask: 'How would a student "
       "with a protected characteristic find out what adjustments are open to them?' Do not put this duty to a student as something they must do."))

s('1.17', type='requirement', rung='none', force='describes', level='none', appliesTo='course providers and practice placements', addressee='provider',
  verbs=['make', 'provide'], about='legal duty to adjust, on courses and placements', domain='none', award='none',
  para=("Both course providers and practice placements hold a legal duty to adjust reasonably so the learning environment is open and accessible "
        "to all students, including those with protected characteristics; QAA guidance on inclusive subject communities gives more."),
  prac=("The legal duty to make reasonable adjustments reaches placements as well as the university: agree with placement partners how adjustments "
        "made on campus carry over into practice settings."),
  ben=('n/a', 'a duty on the provider and placements; the student meets its effect'),
  aaw=("Describe this as a legal duty on courses and on placement settings alike, recorded as describes because the issuer uses 'duty' (Part E). "
       "Cite it as " + CITE + "1.17. Do not claim the statement adds to the law. Set it beside " + sid('1.14', '1.24', '2.35') + "."),
  aad=("Raise it when a team plans placements or a student's adjustments need to follow them into practice. Frame it for staff as a shared "
       "duty with placement partners. Ask: 'Who in the placement knows about this student's agreed adjustments, and how?' "
       "Avoid telling a student that arranging adjustments is their job."))

s('1.24', type='expectation', rung='none', force='describes', level='none', appliesTo='course providers', addressee='provider',
  verbs=['make', 'enable'], about='anticipatory reasonable adjustments in every setting', domain='none', award='none',
  para=("Courses can be built to accommodate individual needs with access designed in, and providers are expected to make adjustments in advance "
        "to teaching, learning and assessment, on campus, online and in practice, so that every student can reach and show the intended outcomes."),
  prac=("Anticipate adjustments rather than waiting for requests, across campus, online and practice settings, so that all students can meet and "
        "evidence the outcomes; build accessibility into the curriculum itself."),
  ben=('n/a', 'an expectation of the provider; the student meets its effect'),
  aaw=("Describe this as an expectation placed on providers ('expected to', recorded as describes, Part E). Cite it as " + CITE + "1.24. "
       "Do not claim it lowers the outcomes; it concerns how students reach them. Set it beside " + sid('1.14', '1.17', '3.8') + "."),
  aad=("Raise it with a programme team designing teaching or assessment. Put it as planning ahead for access, including in practice settings. "
       "Ask: 'Which assessment in this module would a disabled student find hardest, and what could you change now?' Do not give this to a student as their task."))

s('1.45', type='expectation', rung='none', force='will', level='none', appliesTo='course providers', addressee='provider',
  verbs=['ensure'], about='procedures for authenticity and integrity with generative AI', domain='none', award='none',
  para=("AI, generative AI included, now shapes society and practice; students and social workers engage with it critically to support people in "
        "line with social work values, providers can help them use it competently, critically, lawfully and ethically, and procedures will be in "
        "place to protect authenticity and academic integrity."),
  prac=("Have procedures that protect authenticity and academic integrity where students use generative AI, and support students to use these "
        "tools competently, critically, lawfully and ethically for the good of people and communities."),
  ben=('n/a', 'an expectation of the provider; the student meets its effect'),
  aaw=("Describe this as an expectation that providers will have integrity procedures for AI use. Cite it as " + CITE + "1.45. "
       "Do not claim it bans or endorses particular tools. Set it beside " + sid('1.46', '1.48', '4.11.w') + "."),
  aad=("Raise it when a team reviews assessment design or integrity rules in the light of AI. Frame it for staff as procedures plus support. "
       "Ask: 'Would your students know which uses of AI are allowed in this assessment and why?' Avoid presenting it to a student as a rule they must police."))

s('1.46', type='expectation', rung='none', force='describes', level='none', appliesTo='students and educators', addressee='both',
  verbs=['navigate'], about='navigating technologies and their risks', domain='generic-skill', award='none',
  para=("Technologies are met in many places and at many scales, with unequal access; students and educators need to handle them from varied "
        "angles, keep up with change and use them to improve learning, research and practice, while recognising and challenging the harm and "
        "discrimination they can create."),
  prac=("Staff and students alike need to keep pace with changing technologies, use them to strengthen learning and practice, and recognise and "
        "challenge the risks and discrimination they can bring for individuals and groups."),
  ben=("You need to be able to find your way around changing technologies from different points of view, keep up to date, use them to help "
       "your learning and practice, and notice and push back on the harm or unfairness they can cause."),
  aaw=("Describe this as a need shared by students and staff, worded 'need to' and recorded as describes (Part E); it is not a numbered outcome. "
       "Cite it as " + CITE + "1.46. Do not claim it sets a level. Set it beside " + sid('1.45', '1.48', '4.11.w') + " and qaa/fheq-2024/annex-d/transferable/r1/3rd."),
  aad=("Raise it when someone asks how they should use digital tools or AI in study or practice. With a student say 'you'; with staff, note it "
       "applies to them too. Ask: 'Which technology you use could put someone at a disadvantage, and how would you spot it?' "
       "Avoid reading the paragraph aloud or treating it as a test students must pass."))

s('1.48', type='expectation', rung='none', force='describes', level='none', appliesTo='students and educators', addressee='both',
  verbs=['guide', 'replace'], about='values guide technology; it never replaces relationships', domain='understanding', award='none',
  para=("Social work values are expected to steer how students and staff use technology throughout learning, and technology and digital options "
        "should not stand in for human relationships or contact."),
  prac=("Expect values to steer every use of technology in the course, and keep digital options from replacing the human contact that the "
        "profession depends on."),
  ben=("You are expected to let social work values guide how you use technology, and to make sure digital tools never take the place of real "
       "human relationships with the people you work with."),
  aaw=("Describe this as an expectation ('it is expected', recorded as describes, Part E) for students and staff. Cite it as " + CITE + "1.48. "
       "Do not claim it forbids digital delivery. Set it beside " + sid('1.45', '1.46', '4.11.z') + "."),
  aad=("Raise it when a student or team considers using technology with people who use services. Put it plainly: relationships come first. "
       "Ask: 'In this case, what would be lost if the contact happened only through a screen or a tool?' Avoid lecturing or quoting at length."))

s('2.4', type='requirement', rung='none', force='must', level='none', appliesTo='Social Work courses', addressee='provider',
  verbs=['involve'], about='ethics and dilemmas as a core requirement', domain='none', award='none',
  para=("Social work education rests on values and ethics that ask practitioners to respect individual dignity yet also to take and carry out hard "
        "decisions, liberty included, where benefit and harm are both possible; courses therefore require the study, use of and critical "
        "reflection on ethical principles and dilemmas, which the regulators of all four nations reflect."),
  prac=("Make ethical principles and professional dilemmas a core, required part of the course: their study, their application and critical "
        "reflection on them, including decisions that restrict liberty."),
  ben=('n/a', 'a requirement on course design; the student-facing outcome is in 4.11 aa and 2.27'),
  aaw=("Describe this as a core requirement of course design, recorded as must from 'core requirement'. Cite it as " + CITE + "2.4. "
       "Do not present it as a student outcome in its own right. Set it beside " + sid('2.27', '4.11.u', '4.11.aa', '4.11.ve') + "."),
  aad=("Raise it when a programme team maps where ethics and dilemmas are taught and assessed. Frame it as a required strand of the course. "
       "Ask: 'Where do students first practise reasoning through a decision that limits someone's liberty?' Do not hand this to a student as their duty."))

s('2.8', type='expectation', rung='none', force='describes', level='none', appliesTo='qualified social workers, and so those qualifying',
  addressee='learner', verbs=['understand', 'work', 'analyse', 'manage', 'lead'], about='working within contested debate and leading change',
  domain='understanding', award='none',
  para=("Social work changes with social, political and economic pressures and with policy and law; qualified social workers need to be ready to "
        "understand and work within argument over the profession's nature and purpose, and to analyse, adapt to, manage and finally lead change."),
  prac=("Prepare students to work inside a contested profession: they need to grasp the debate about what social work is for and to build the "
        "capacity to handle change and, over time, lead it."),
  ben=("You need to understand that people disagree about what social work is for, be able to work within that debate, and build your ability "
       "to cope with change, manage it and eventually lead it."),
  aaw=("Describe this as a need ('need to', recorded as describes, Part E) for qualified practitioners, which courses prepare for. Cite it as " + CITE + "2.8. "
       "Do not claim graduates must already lead change at the award. Set it beside " + sid('1.8', '4.11.cc', '4.11.k') + " and qaa/fheq-2024/4.15.b9.2."),
  aad=("Raise it when a student is unsettled by conflicting views of the profession's role. Put it plainly and in the second person. "
       "Ask: 'Which view of social work's purpose do you lean towards, and what would someone who disagrees say?' Avoid settling the debate for them."))

s('2.11', type='requirement', rung='none', force='must', level='none', appliesTo='Social Work courses in Wales', addressee='provider',
  verbs=['approved', 'informed'], about='approval by Social Care Wales and the Welsh context', domain='none', award='none',
  para=("In Wales, courses must have Social Care Wales approval; the professional requirements sit in its qualifications framework and the award "
        "draws on the National Occupational Standards, the Welsh code of practice for social care and this statement; degrees run through "
        "partnerships with local authority employers and must reflect current Welsh law, policy and regulation."),
  prac=("For a Welsh course, secure Social Care Wales approval, meet its qualifications framework, deliver through partnership with local authority "
        "employers, and keep content current with Welsh legislation, social policy and regulation."),
  ben=('n/a', 'a requirement on the course in Wales; the student-facing rule is in 2.12'),
  aaw=("Describe this as a requirement on Welsh courses (must), set by Social Care Wales, not by QAA. Cite it as " + CITE + "2.11. "
       "Do not claim the statement approves courses. Set it beside " + sid('2.12', '2.36', '2.42') + "."),
  aad=("Raise it with a team running or planning a course in Wales. Frame it as the regulator's approval route. Ask: 'Which Welsh legislation or "
       "policy changed this year, and where does the course pick it up?' Do not present it to a student as their obligation."))

s('2.12', type='requirement', rung='none', force='must', level='none', appliesTo='Social Work students in Wales', addressee='learner',
  verbs=['register', 'demonstrate', 'adhere'], about='registering with Social Care Wales and following its Code', domain='none', award='none',
  para=("Students in Wales must register with Social Care Wales and show that they understand and keep to its Code of Professional Practice "
        "for Social Care, during their studies and on into practice."),
  prac=("Students on Welsh courses must register with Social Care Wales and show they understand and follow its Code of Professional Practice "
        "while studying and after qualifying."),
  ben=("If you study in Wales, you must register with Social Care Wales and show that you understand its Code of Professional Practice and follow "
       "it, both while you study and once you qualify."),
  aaw=("Describe this as a must on students in Wales that comes from the Welsh regulator. Cite it as " + CITE + "2.12. "
       "Do not claim it applies in England, Scotland or Northern Ireland. Set it beside " + sid('2.11', '2.18', '4.11.v') + "."),
  aad=("Raise it with a student starting a course in Wales, or one unsure about conduct rules. Say it plainly in the second person. "
       "Ask: 'Have you registered yet, and which part of the Code do you find hardest to keep in placement?' Avoid reading the Code out at length."))

s('2.14', type='requirement', rung='none', force='must', level='none', appliesTo='Social Work courses in England', addressee='provider',
  verbs=['approved', 'meet', 'demonstrate'], about='approval by Social Work England against its standards', domain='none', award='none',
  para=("In England, courses must have Social Work England approval, meeting its Education and Training Standards and producing graduates who can "
        "show they meet its Professional Standards; approved courses also reflect wider curriculum guidance and this statement, and the "
        "Professional Standards Authority oversees the regulator."),
  prac=("For a course in England, secure Social Work England approval against the Education and Training Standards, and make sure graduates can "
        "evidence the Professional Standards; reflect the regulator's knowledge, skills and behaviours guidance too."),
  ben=('n/a', 'a requirement on the course in England; the student meets its effect at registration'),
  aaw=("Describe this as a must on English courses that comes from Social Work England. Cite it as " + CITE + "2.14. "
       "Do not claim the statement is one of the regulator's standards. Set it beside " + sid('2.36', '2.42', '4.11.e') + "."),
  aad=("Raise it with a team preparing for approval or review in England. Frame it as the regulator's route, with the statement as one input. "
       "Ask: 'Where in your mapping does each Professional Standard get evidenced by a graduate?' Do not put this to a student as their duty."))

s('2.17', type='requirement', rung='none', force='must', level='none', appliesTo='Social Work students in Northern Ireland', addressee='learner',
  verbs=['understand', 'consider'], about='political violence and integrated care in Northern Ireland', domain='understanding', award='none',
  para=("Northern Ireland's framework specification, written jointly by the regulator and the health department, gives one set of learning "
        "requirements and outcomes, with some particular to the region, where students are required to grasp how its political "
        "violence bears on their practice and to consider their place in integrated health and social care after conflict."),
  prac=("On a Northern Ireland course, students are required to understand the effect of political violence on practice and their role in "
        "joined-up health and social care bodies in a society emerging from conflict."),
  ben=("If you study in Northern Ireland, you are required to understand how its history of political violence affects your practice and to think "
       "about your role in joined-up health and social care in a society after conflict."),
  aaw=("Describe this as a requirement ('required', recorded as must) on students in Northern Ireland, drawn from its framework specification. "
       "Cite it as " + CITE + "2.17. Do not claim it applies elsewhere in the UK. Set it beside " + sid('2.18', '4.11.k', '4.11.a') + "."),
  aad=("Raise it with a student or team on a Northern Ireland course, especially before placement. Say it plainly and with care. "
       "Ask: 'How might the legacy of the conflict shape what a family expects of you as a social worker?' Avoid lecturing on the history."))

s('2.18', type='requirement', rung='none', force='must', level='none', appliesTo='Social Work students and social workers in Northern Ireland',
  addressee='learner', verbs=['register', 'undertake'], about='registration and the assessed year in Northern Ireland', domain='none', award=HON,
  para=("Since 2004 an honours degree in Social Work is the recognised qualification there for social workers, for probation officers and for "
        "education welfare officers; since protection of title in 2005 every student and qualified social worker is required to register with "
        "the Social Care Council, and graduates register on condition of an Assessed Year in Employment."),
  prac=("In Northern Ireland, students must register with the Social Care Council, honours is the professional qualification, and new graduates "
        "are registered on condition that they complete an Assessed Year in Employment."),
  ben=("If you study in Northern Ireland, you must register with the Social Care Council as a student, and once you graduate your registration "
       "depends on completing an assessed first year in work."),
  aaw=("Describe this as a requirement ('required', recorded as must) from the Northern Ireland regulator. Cite it as " + CITE + "2.18. "
       "Do not claim the assessed year is part of the degree. Set it beside " + sid('2.12', '2.21', '4.11.psrb') + "."),
  aad=("Raise it with a student in Northern Ireland asking about registration or the first job. Say it plainly in the second person. "
       "Ask: 'What support will you look for in your assessed year?' Avoid reading out the dates and acts."))

s('2.21', type='requirement', rung='none', force='must', level='none', appliesTo='Social Work students in Scotland', addressee='learner',
  verbs=['achieve'], about='the qualifying award and SSSC registration in Scotland', domain='none', award=[HON, MA],
  para=("The SSSC approves all qualifying courses, keeps registers, sets codes and regulates training; practising in Scotland needs a recognised "
        "qualification and SSSC registration, and to qualify professionally students must gain a generic Social Work honours degree or a postgraduate "
        "award of equal standing."),
  prac=("In Scotland, to qualify, students must hold a generic Social Work honours degree or a postgraduate award of equal standing, and practice needs "
        "SSSC registration; courses work to the SSSC's revised standards and requirements."),
  ben=("If you study in Scotland, to qualify you must gain a generic Social Work honours degree or a postgraduate award of equal standing, and you "
       "will need to register with the SSSC to practise."),
  aaw=("Describe this as a must on students in Scotland, set by the Scottish regulator's route to qualification. Cite it as " + CITE + "2.21. "
       "Do not claim an ordinary degree qualifies. Set it beside " + sid('2.22', '2.18', '4.9') + " and fqheis:10 (qaa/fqheis-2024/4.16.b1)."),
  aad=("Raise it with a student in Scotland weighing routes into the profession. Say it plainly in the second person. Ask: 'Is the route you are on "
       "an honours or postgraduate award approved by the SSSC?' Avoid reading out the history of the regulator."))

s('2.23', type='expectation', rung='none', force='will', level='none', appliesTo='students progressing through a course', addressee='both',
  verbs=['progress', 'include'], about='progression through levels to the threshold skills', domain='none', award=[HON, IMA],
  para=("Across an honours degree (FHEQ 6; SCQF 10) or an integrated master's (FHEQ 7; SCQF 11), students move from level to level under each "
        "institution's rules; each level is expected to build towards meeting the threshold subject and generic skills, usually with credit "
        "gained for all learning and assessment, practice included."),
  prac=("Design each level so that it builds towards the threshold subject-specific and generic skills, and expect students to complete and gain "
        "credit for every element, practice components included."),
  ben=("As you move from one level of your course to the next, each stage builds towards the minimum skills you need by the end, and you will "
       "usually need to pass everything, including your practice learning."),
  aaw=("Describe this as an expectation of how levels build towards the threshold, with 'will usually include' for credit. Cite it as " + CITE + "2.23. "
       "Do not claim it sets outcomes for earlier levels. Set it beside " + sid('4.9', '4.11.ku', '3.5') + " and spine:4 to spine:6 in std:ref:uk-framework."),
  aad=("Raise it when a student asks how earlier years count or a team plans level outcomes. With a student, say 'you'; with staff, talk about "
       "staged design. Ask: 'What from your first year are you still using now?' Avoid suggesting earlier levels must meet the final threshold."))

s('2.24', type='requirement', rung='none', force='will', level='none', appliesTo='all Social Work routes', addressee='provider',
  verbs=['include', 'apply', 'develop'], about='practice learning integrated into every route', domain='none', award='none',
  para=("Social work can be taken as a BA or BSc, a postgraduate conversion, a PgDip, an MSc, MSci or MA, or a degree apprenticeship, and every "
        "one of these routes will build in practice learning so students can use and grow their skills in real situations."),
  prac=("Whatever the route, from BA to MA or apprenticeship, build practice learning into the programme so that students apply and develop "
        "their skills in real situations."),
  ben=('n/a', 'a requirement on course design; the student meets its effect'),
  aaw=("Describe this as a will on every route: practice learning is part of all of them. Cite it as " + CITE + "2.24. "
       "Do not claim it sets a number of practice days; the regulators do (4.10). Set it beside " + sid('3.4', '4.10', '4.11.psrb') + "."),
  aad=("Raise it when a team designs a new route, such as an apprenticeship. Frame it for staff as integration, not an add-on. "
       "Ask: 'How does what students do in practice feed back into the taught modules?' Do not present it to a student as their responsibility."))

s('2.27', type='outcome', rung='none', force='will', level='none', appliesTo='students of the subject', addressee='learner',
  verbs=['apply', 'evaluating'], about='applying ethics to oneself and judging others', domain='subject-skill', award='none',
  para=("Ethics, social justice and professional values sit at the centre of design, with activities that carry values into research, practice and "
        "daily conduct; students will be able to bring this to bear on their own values and behaviour and to judge critically how others behave ethically."),
  prac=("Build activities that apply values and ethics to research, practice and conduct; students will be able to apply them to their own value "
        "base and critically evaluate the ethical conduct of others."),
  ben=("You will be able to apply social work values and ethics to your own beliefs and behaviour, and to judge critically how ethically other "
       "people act."),
  aaw=("Describe this as an expected outcome (will) for students, not tied to one award. Cite it as " + CITE + "2.27. "
       "Do not claim it is one of the lettered threshold outcomes, though it echoes them. Set it beside " + sid('4.11.u', '4.11.ve', '2.4') + "."),
  aad=("Raise it when a student reflects on a value conflict in placement. Say it plainly in the second person. Ask: 'Where did your own values "
       "pull against what you were asked to do, and how did you judge it?' Avoid moralising or reading the paragraph aloud."))

s('2.34', type='expectation', rung='none', force='describes', level='none', appliesTo='Social Work courses', addressee='provider',
  verbs=['work', 'promote'], about='partnership with people with lived experience', domain='none', award='none',
  para=("Courses are expected to work alongside people with lived or living experience to build understanding, empathy and good practice, so "
        "students hear many perspectives, test their assumptions and reflect more widely."),
  prac=("Partner with people who have lived or living experience so that students hear a wide range of voices, question their own "
        "perceptions and reflect more broadly."),
  ben=('n/a', 'an expectation of the course; the student meets its effect'),
  aaw=("Describe this as an expectation on courses ('expected to', recorded as describes, Part E). Cite it as " + CITE + "2.34. "
       "Do not claim it specifies a model of involvement. Set it beside " + sid('2.35', '3.6', '4.11.p') + "."),
  aad=("Raise it when a team reviews how people with lived experience take part. Frame it as partnership, not consultation alone. "
       "Ask: 'Where in the course do people with lived experience shape what is taught, not just tell their story?' Do not give this to a student as a duty."))

s('2.35', type='requirement', rung='none', force='will', level='none', appliesTo='Social Work courses and practice partners', addressee='provider',
  verbs=['ensure'], about='written practice agreements and stakeholder views in design', domain='none', award='none',
  para=("Courses partner with practice learning providers and stakeholders; practice-based learning will rest on a written agreement among "
        "practice educators, supervisors, course and placement providers and students, and courses are expected to bring in the views of employers, "
        "practitioners and those with lived experience when designing and reviewing the curriculum."),
  prac=("Put every practice placement under a written collaborative agreement among all parties, and bring employers', practitioners' and lived "
        "experience views into curriculum design, development and review."),
  ben=('n/a', 'a requirement on the course and its partners; the student is a party to the agreement but the duty is the course\'s'),
  aaw=("Describe this as a will on placement agreements and an expectation ('expected to', Part E) on stakeholder involvement. Cite it as "
       + CITE + "2.35. Do not claim it sets the agreement's content. Set it beside " + sid('2.34', '1.17', '2.36') + "."),
  aad=("Raise it when a team sets up or reviews placement arrangements. Frame it as shared written agreement and shared design. Ask: 'Does every "
       "placement have a written agreement that the student has seen and signed?' Avoid presenting the agreement as the student's job to arrange."))

s('2.36', type='requirement', rung='none', force='should', level='none', appliesTo='Social Work courses', addressee='provider',
  verbs=['written'], about='alignment with the relevant regulator\'s standards', domain='none', award='none',
  para="Courses should be written to align with the standards of the regulator in the nation where they run.",
  prac="Write the course so that it lines up with the standards of the regulator for the nation where it is delivered.",
  ben=('n/a', 'a duty on course design'),
  aaw=("Describe this as a should on course design. Cite it as " + CITE + "2.36. Do not claim the statement can stand in for the regulator's "
       "standards. Set it beside " + sid('2.11', '2.14', '2.42') + "."),
  aad=("Raise it with a team writing or revising a course. Frame it as aligning to the national regulator. Ask: 'Which regulator's standards "
       "is this course mapped against, and when was that mapping last checked?' Do not put this to a student."))

s('2.39', type='requirement', rung='none', force='will', level='none', appliesTo='providers', addressee='provider',
  verbs=['use', 'gain', 'ensure'], about='external reviewers in periodic review', domain='none', award='none',
  para=("Externality is essential to UK quality assurance: providers will bring in external reviewers in periodic review for an independent view "
        "of proposed changes and to make sure threshold standards are met and content suits the subject."),
  prac="Include external reviewers in periodic review to test proposed changes independently and confirm threshold standards and subject content.",
  ben=('n/a', 'a duty on the provider'),
  aaw=("Describe this as a will on providers in periodic review. Cite it as " + CITE + "2.39. Do not claim it describes external examining, which "
       "2.40 covers. Set it beside " + sid('2.42', '4.9') + "."),
  aad=("Raise it with a team preparing a periodic review. Frame it as external challenge. Ask: 'Who outside the institution will test whether "
       "the threshold is secure?' Do not raise it with students."))

s('2.42', type='requirement', rung='none', force='will', level='none', appliesTo='Social Work courses', addressee='provider',
  verbs=['require'], about='regulatory approval and ongoing monitoring', domain='none', award='none',
  para="Courses will need regulators' approval and continuing monitoring, usually through a mix of visits and desk review.",
  prac="Expect regulatory approval and continued monitoring of the course, normally by site visits combined with desk-based review.",
  ben=('n/a', 'a requirement on the course'),
  aaw=("Describe this as a will on courses: regulators approve and monitor them. Cite it as " + CITE + "2.42. "
       "Do not claim QAA approves social work courses. Set it beside " + sid('2.11', '2.14', '2.36') + "."),
  aad=("Raise it with a team planning for a regulator's visit. Frame it as ongoing, not one-off. Ask: 'What evidence would a desk review ask for "
       "first?' Do not put this to a student."))

s('3.1', type='expectation', rung='none', force='describes', level='none', appliesTo='Social Work courses', addressee='provider',
  verbs=['use', 'based'], about='principles for course content', domain='none', award='none',
  para=("Providers design at set levels using the national frameworks of their nation; content is expected to be relevant, up to date, evidence "
        "informed, current and coherent, and co-production, responsiveness and inclusive, decolonised content are welcomed."),
  prac=("Base content on relevance, currency, evidence and coherence; design at the right framework level for your nation; co-produce with "
        "stakeholders where you can and make content inclusive and decolonised."),
  ben=('n/a', 'an expectation of the course'),
  aaw=("Describe this as an expectation ('it is expected', recorded as describes, Part E) on course content. Cite it as " + CITE + "3.1. "
       "Do not claim it names a particular framework; it refers to the national frameworks in general. Set it beside " + sid('2.26', '3.4', '1.21') + "."),
  aad=("Raise it when a team refreshes content. Frame it for staff as five tests of content. Ask: 'Which topic in this module is least current, "
       "and whose perspectives are missing from it?' Do not hand this to a student."))

s('3.4', type='expectation', rung='none', force='describes', level='none', appliesTo='students and courses', addressee='both',
  verbs=['engage'], about='practice-based learning and integration of knowledge into practice', domain='subject-skill', award='none',
  para=("Practical learning is fundamental: in work settings it means taking part directly with people with lived experience, families, carers, "
        "communities and other professionals, alongside observation, shadowing, supervision, reflection and research, and knowledge is expected "
        "to be clearly integrated into practice."),
  prac=("Make practice learning central, with direct work alongside people with lived experience and professionals, and expect students to show "
        "clearly how they bring knowledge into practice."),
  ben=("Learning in practice is a core part of your course: you will work directly with people and other professionals, and you are expected to "
       "show clearly how you put what you know into practice."),
  aaw=("Describe this as an expectation on integration ('there is an expectation', recorded as describes, Part E). Cite it as " + CITE + "3.4. "
       "Do not claim it sets the length or type of placement. Set it beside " + sid('2.24', '4.11.n', '4.11.l') + " and qaa/fheq-2024/4.15.b6."),
  aad=("Raise it when a student struggles to link theory with what they do on placement. Say it plainly in the second person. "
       "Ask: 'Which idea from your reading did you actually use this week, and how?' Avoid quoting the paragraph's list at length."))

s('3.6', type='expectation', rung='none', force='describes', level='none', appliesTo='Social Work courses', addressee='provider',
  verbs=['facilitated'], about='scaffolded teaching and a range of facilitators', domain='none', award='none',
  para=("Teaching is staged, starting with induction and orientation at each level, students take more responsibility as they progress, and "
        "learning is expected to be led by a range of people, including academics, researchers, practitioners and people with lived experience."),
  prac=("Scaffold teaching from induction onward, hand students more responsibility over time, and involve academics, researchers, practitioners "
        "and people with lived experience in facilitating learning."),
  ben=('n/a', 'an expectation of the course'),
  aaw=("Describe this as an expectation ('it is expected', recorded as describes, Part E) on who teaches. Cite it as " + CITE + "3.6. "
       "Do not claim it fixes a ratio of contributors. Set it beside " + sid('2.34', '3.8') + "."),
  aad=("Raise it with a team planning teaching across levels. Frame it as scaffolding plus a range of voices. Ask: 'Where does responsibility "
       "for learning visibly shift to students?' Do not put it to a student as a duty."))

s('3.8', type='requirement', rung='none', force='will', level='none', appliesTo='Social Work courses', addressee='provider',
  verbs=['incorporate'], about='assessment principles and readiness for practice', domain='none', award='none',
  para=("Assessment rests on inclusion, accessibility and integrity and will build in feedback and feed forward; it measures learning, checks "
        "professional standards and supports reflection, with clear criteria linked to outcomes, and it judges readiness for practice, progress "
        "and the final award."),
  prac=("Ground assessment in inclusion, accessibility and integrity, build in feedback and feed forward, link criteria to outcomes and use "
        "assessment to judge readiness and fitness for practice."),
  ben=('n/a', 'a requirement on the course\'s assessment'),
  aaw=("Describe this as a will on assessment design (feedback and feed forward). Cite it as " + CITE + "3.8. "
       "Do not claim it prescribes methods; 3.9 lists examples. Set it beside " + sid('1.24', '4.11.ee', '4.10') + "."),
  aad=("Raise it with a team reviewing assessment. Frame it as principles plus readiness for practice. Ask: 'How does feedback on this task "
       "help the student with the next one?' Do not put this to a student."))

s('4.1', type='requirement', rung='none', force='must', level='none', appliesTo='Social Work students and graduates', addressee='learner',
  verbs=['demonstrate', 'met', 'meet'], about='academic and practice requirements, and regulators\' standards', domain='none', award=[HON, IMA, MA],
  para=("Social work is a professional qualification at undergraduate or postgraduate level; students must show they have met both the academic "
        "and the practice requirements of their course, and graduates are also expected to meet any standards of the regulator in their nation."),
  prac=("Assess both academic and practice requirements, since students must show they meet both; graduates also face the national regulator's "
        "own standards."),
  ben=("You must show that you have met both the academic and the practice requirements of your course, and you will also be expected to meet "
       "the standards of the regulator in the nation where you study."),
  aaw=("Describe this as a must on students for both academic and practice requirements, at every award covered. Cite it as " + CITE + "4.1. "
       "Do not claim the statement sets the regulator's standards. Set it beside " + sid('4.9', '4.13', '4.16', '4.11.psrb') + "."),
  aad=("Raise it when a student is strong in one side, academic or practice, and weak in the other. Say it plainly in the second person. "
       "Ask: 'Which side of your course feels less secure right now, and what is the evidence?' Avoid suggesting one side can make up for the other."))

s('4.2', type='requirement', rung='none', force='should', level='none', appliesTo='providers developing competence standards', addressee='provider',
  verbs=['follow'], about='threshold standards are not competence standards', domain='none', award='none',
  para=("The minimum threshold standards are not meant as universal competence standards; a provider that sets competence standards under equality "
        "law may draw on the statement and PSRB requirements, and in that case should follow the latest Equality and Human Rights Commission guidance."),
  prac=("Do not treat the threshold standards as competence standards in the equality-law sense; if you write competence standards, follow the "
        "latest EHRC guidance."),
  ben=('n/a', 'a duty on the provider'),
  aaw=("Describe this as a should on providers that write competence standards, and as a limit on how the threshold is used. Cite it as " + CITE + "4.2. "
       "Do not claim the threshold outcomes are competence standards. Set it beside " + sid('4.9', '1.14') + "."),
  aad=("Raise it when a team proposes using the outcomes to bar a disabled student. Frame it for staff with care. Ask: 'Is this a competence "
       "standard you have justified under equality law, or a learning outcome?' Do not raise it with students as their concern."))

s('4.5', type='requirement', rung='none', force='will', level='none', appliesTo='Social Work courses', addressee='provider',
  verbs=['designed', 'assessed', 'apply'], about='academic level 6 or 7 and regulator outcomes', domain='none', award=[HON, IMA, MA],
  para=("Practice requirements are the same across undergraduate and postgraduate routes, but academic study will be designed and assessed at the "
        "right level, 6 (SCQF 10) or 7 (SCQF 11); every degree is accredited by a regulator, whose outcomes for registration will also apply."),
  prac=("Keep practice requirements common across routes while pitching academic modules at Level 6 (SCQF 10) or Level 7 (SCQF 11), and apply "
        "the regulator's learning outcomes for registration as well."),
  ben=('n/a', 'a requirement on course design'),
  aaw=("Describe this as a will on course design: academic level differs, practice does not. Cite it as " + CITE + "4.5. "
       "Do not claim practice expectations rise at master's level. Set it beside " + sid('4.9', '4.12', '4.16') + ", qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1."),
  aad=("Raise it with a team running both undergraduate and postgraduate routes. Frame it as one practice standard, two academic levels. "
       "Ask: 'What makes an assignment on your master's route a level 7 task rather than a level 6 one?' Do not put this to a student."))

s('4.8', type='expectation', rung='none', force='will', level='none', appliesTo='providers classifying awards', addressee='provider',
  verbs=[], about='classes above threshold follow the provider\'s marking schemes', domain='none', award=[IMA, MA],
  para=("Integrated master's degrees use similar classes (2:2, 2:1 and first), master's degrees give merit and distinction above the threshold, "
        "and for every award the criteria above threshold will follow the provider's common or generic marking schemes."),
  prac="Classify achievement above the threshold through your institution's common or generic marking schemes, for every award covered.",
  ben=('n/a', 'a provider duty in classification'),
  aaw=("Describe this as a will on providers: grading above threshold comes from their own schemes, not from the statement. Cite it as " + CITE + "4.8. "
       "Do not claim the statement defines merit or distinction. Set it beside " + sid('4.10') + " and qaa/fheq-2024/annex-d/summary/r1/2.1."),
  aad=("Raise it when someone asks what a merit or a 2:1 looks like in social work. Frame it as the institution's marking scheme. Ask: 'Which "
       "marking descriptors does your institution use above the pass?' Avoid inventing subject criteria for higher classes."))

s('4.9', type='requirement', rung='none', force='must', level='fheq:6', appliesTo='honours graduates', addressee='learner',
  verbs=['demonstrate'], about='at least threshold across four categories', domain='none', award=HON,
  para=("Honours graduates in Social Work must show at least threshold attainment in every category of four areas: what they know and "
        "understand, the skills they show, values and ethics, and PSRB requirements."),
  prac=("Make sure every honours graduate reaches at least the threshold in all four areas: knowledge and understanding, skills, values and ethics, "
        "and the regulator's requirements."),
  ben=("To gain your honours degree you must reach at least the minimum standard in all four areas: what you know and understand, the skills "
       "you show, your values and ethics, and the regulator's requirements."),
  aaw=("Describe this as the must that makes 4.11 a threshold for the honours award at FHEQ level 6 (SCQF 10). Cite it as " + CITE + "4.9. "
       "Do not claim a strong area can offset a weak one. Set it beside " + sid('4.11.ku', '4.11.ds', '4.11.ve', '4.11.psrb') + " and qaa/fheq-2024/annex-d/summary/r1/3rd."),
  aad=("Raise it when a student asks what they must pass to qualify. Say it plainly in the second person. Ask: 'Which of the four areas do you "
       "have the least evidence for so far?' Avoid presenting the minimum as what a good degree looks like."))

s('4.10', type='requirement', rung='none', force='will', level='none', appliesTo='providers and regulators', addressee='provider',
  verbs=['determined'], about='threshold criteria and practice days', domain='none', award=HON,
  para=("Threshold criteria will follow the provider's common or generic undergraduate marking schemes and the sector standards used in each UK "
        "nation, and the regulator will also set the threshold, including the required number of mandatory practice days."),
  prac=("Set threshold criteria in line with your undergraduate marking scheme and the sector standards of your nation, and take the number of "
        "practice days from the regulator."),
  ben=('n/a', 'a provider and regulator matter'),
  aaw=("Describe this as a will on how the honours threshold is set: by marking schemes and by the regulator. Cite it as " + CITE + "4.10. "
       "Do not state a number of practice days from the statement. Set it beside " + sid('4.9', '4.11.psrb', '4.13', '4.16') + "."),
  aad=("Raise it when a team asks how many practice days are needed or how the pass is set. Frame it as the regulator's figure and the "
       "institution's scheme. Ask: 'Which regulator sets your practice days, and where is that written down?' Do not put this to a student as their task."))

s('4.12', type='requirement', rung='none', force='must', level='fheq:7', appliesTo="integrated master's courses", addressee='provider',
  verbs=['add', 'include', 'meet'], about="integrated master's meets both levels", domain='none', award=IMA,
  para=("Integrated master's degrees usually add a further full-time year to honours, with about a year at master's level, often research, and "
        "are required to satisfy the standards for undergraduate and for master's social work degrees alike."),
  prac=("Design an integrated master's so that it meets both the honours threshold and the master's threshold, with around a year of master's-level "
        "study, often including research."),
  ben=('n/a', 'a requirement on course design'),
  aaw=("Describe this as a requirement ('required', recorded as must) on integrated master's design at FHEQ 7 (SCQF 11). Cite it as " + CITE + "4.12. "
       "Do not claim the integrated master's escapes the honours outcomes. Set it beside " + sid('4.13', '4.14.ku', '4.17.ku') + " and qaa/fheq-2024/4.17.b1."),
  aad=("Raise it with a team designing an integrated master's. Frame it as meeting two sets of standards. Ask: 'Which modules carry the master's-level "
       "year, and how is it different from the honours years?' Do not put this to a student."))

s('4.13', type='requirement', rung='none', force='must', level='fheq:7', appliesTo="integrated master's graduates", addressee='learner',
  verbs=['demonstrate'], about="integrated master's: at least threshold, as in 4.11", domain='none', award=IMA,
  para=("Integrated master's graduates must show at least threshold attainment across all categories of 4.11; threshold often maps to a third, and "
        "the regulator also sets it, including mandatory practice days."),
  prac=("Ensure integrated master's graduates reach at least the 4.11 threshold in every category; the regulator sets the practice days."),
  ben=("To gain an integrated master's in social work you must reach at least the minimum standard in every area set for the honours degree, "
       "including the practice days your regulator requires."),
  aaw=("Describe this as the must that applies the honours threshold to the integrated master's. Cite it as " + CITE + "4.13; the reference to 4.11 is a "
       "cross-reference, not a new list. Do not claim a third is the expected outcome. Set it beside " + sid('4.11.ku', '4.12', '4.14.ku') + "."),
  aad=("Raise it when an integrated master's student asks what they must pass. Say it plainly in the second person. Ask: 'Have you checked your "
       "evidence against the honours areas as well as the master's ones?' Avoid presenting the minimum as the target."))

s('4.16', type='requirement', rung='none', force='must', level='fheq:7', appliesTo="postgraduate master's graduates", addressee='learner',
  verbs=['demonstrate'], about="master's: at least threshold across categories", domain='none', award=MA,
  para=("Master's graduates in Social Work must show at least threshold attainment in all relevant outcome categories; threshold usually maps to a "
        "pass, and the regulator also sets it, including mandatory practice days."),
  prac=("Ensure master's graduates reach at least the threshold in every relevant category; a pass corresponds to threshold and the regulator "
        "sets the practice days."),
  ben=("To gain your master's in social work you must reach at least the minimum standard in every relevant area, including the practice days your "
       "regulator requires."),
  aaw=("Describe this as the must that makes 4.17 a threshold for the master's award at FHEQ level 7 (SCQF 11). Cite it as " + CITE + "4.16. "
       "Do not claim it describes merit or distinction. Set it beside " + sid('4.17.ku', '4.17.ds', '4.8') + " and qaa/fheq-2024/4.17.b1."),
  aad=("Raise it when a master's student asks what they need to pass. Say it plainly in the second person. Ask: 'Which outcome area do you have "
       "least evidence for so far?' Avoid treating the pass as the expected standard."))

# ---------------------------------------------------------------- the threshold rung
LV = {HON: 'FHEQ level 6 (SCQF level 10 in Scotland)', IMA: "FHEQ level 7 (SCQF level 11), on top of the honours outcomes", MA: 'FHEQ level 7 (SCQF level 11)'}
AWN = {HON: 'honours', IMA: "integrated master's", MA: "master's"}
FW = {HON: 'qaa/fheq-2024/4.15', IMA: 'qaa/fheq-2024/4.17', MA: 'qaa/fheq-2024/4.17'}

def rung(i, award, cite, about, nb, fw, when, q, **k):
    lead = i.rsplit('.', 1)[0]
    P[i] = dict(type='threshold', rung='threshold', force='threshold', forceFrom=lead, level='fheq:6' if award == HON else 'fheq:7',
                appliesTo='graduates of the subject at threshold', addressee='learner', award=award, about=about, **k)
    P[i]['aaw'] = ("Present this as a threshold outcome: the minimum every " + AWN[award] + " graduate in social work must have shown at " + LV[award]
                   + ", here on " + about + ". Cite it as " + CITE + cite + ". Do not claim it is a regulator's standard, a mark of a higher class, "
                   "or that it holds at another level. Set it beside " + nb + " and the framework descriptor " + fw + ".")
    P[i]['aad'] = ("Bring it up when " + when + ". With a student, say it plainly as 'you'; with staff, frame it as the minimum the award asks the course "
                   "to secure. Ask: " + q + " Do not read the issuer's wording aloud at length or present this minimum as what a good degree reaches.")

def hon(letter, about, para, prac, ben, q, nb, fw, when=None, **k):
    i = '4.11.' + letter
    lab = {'ku': 'knowledge and understanding', 'ds': 'demonstrable skills', 've': 'values and ethics', 'psrb': 'PSRB requirements'}
    cite = '4.11 (' + lab[letter] + ')' if letter in lab else '4.11 ' + letter + ')'
    rung(i, HON, cite, about, nb, fw, when or ('a student or programme team looks at ' + about), q,
         para='Will have shown ' + para, prac='At threshold, honours graduates will have shown ' + prac,
         ben='To reach the minimum for your honours degree, you will have shown ' + ben, **k)

F = {}
F['ku'] = "a coherent knowledge and understanding of the context of professional social work, the knowledge base of social work and its practical application"
F['a'] = "awareness of the role of social work across the globe and in the UK and its constituent nations"
F['b'] = "understanding of social work across statutory, independent, voluntary and third sectors"
F['c'] = "the ability to identify, assess and critically apply research to support a strong evidence base to inform and guide professional practice"
F['d'] = "a critical understanding of theory, policy, legislative context, methods and skills, and awareness of how they apply to practice"
F['e'] = "evidence and demonstration of knowledge, skills and wider behaviours or professional competencies required by regulatory bodies"
F['f'] = "engagement with contemporary cultural and societal debates, such as those concerning inequality, power and oppression"
F['g'] = ("understanding of the relevance of climate change, social, ecological and environmental justice, conflict and diminishing democracy, and the "
          "role of social work in addressing the impact on individuals, families and communities, environmental hazards in terms of their impacts on "
          "fulfilling individuals' and communities' human rights and the disproportionate burden on those already facing hardship or inequality such "
          "as poverty, racism or ableism")
F['h'] = "the ability to understand, identify and appropriately respond to need and risk"
F['i'] = "recognition of intersectional issues that might impact on need and risk, and to respond and challenge where required"
F['j'] = "understanding of the knowledge base and values of social work, and their integrated application and use when working across disciplines"
F['k'] = "critical awareness of contested political and societal contexts and commitment to anti- discriminatory, anti-oppressive and anti-racist practice"
F['l'] = "an ability to use knowledge and understanding to effectively relate to people with lived experience and other professionals to improve outcomes"
F['m'] = "continuous learning, reflection on experience and use of feedback, with the ability to incorporate this in future learning and practice"
F['ds'] = ("a consistent application of social work skills. Reflective application of a range of social work methods, underpinned by critical thinking, "
           "evidence-informed decision-making, and understanding of diverse practice context")
F['n'] = "use knowledge, understanding and critical thinking to inform practice, drawing on theory, policy, legislative context, methods and skills"
F['o'] = "use and evaluate research and wider evidence to inform practice and decisions"
F['p'] = "build relationships and work in partnership with individuals with lived or living experience, and other professionals across agencies"
F['q'] = "practice in environmentally sustainable ways"
F['r'] = "communicate effectively verbally, non-verbally and in writing with individuals with lived or living experience, and other professionals across contexts and levels"
F['s'] = "work within teams, systems and processes, gathering, processing and analysing information to enable understanding and interventions"
F['t'] = "work across and with other agencies and disciplines"
F['u'] = "demonstrate the application of social work values and ethics, including cultural humility and anti-discriminatory, anti-oppressive and anti-racist practice"
F['v'] = "maintain appropriate standards of personal and professional conduct, drawing on relevant codes of practice and/or standards"
F['w'] = "critically engage with digital technology to collate, analyse, select, record and present information"
F['x'] = "exercise an appropriate level of autonomy and decision-making within the context of organisations to ensure safe and effective practice"
F['y'] = "support people to improve outcomes, and manage and reduce risk"
F['z'] = "recognise the dignity of the individual, working in a strengths-based and empowering way"
F['aa'] = "make and implement difficult decisions (including the restriction of liberty) in human situations that involve the potential for benefit while understanding harm"
F['bb'] = "confidently defend decisions made, drawing on a wide evidence base"
F['cc'] = "demonstrate professional leadership and advocacy skills"
F['dd'] = "maintain professional boundaries, working within the limits of the role, identifying sources of support where needed"
F['ee'] = "critically reflect on their performance, using feedback and evidence"
F['ff'] = "engage in continuous professional development, identifying gaps in knowledge and ways to resolve them"
F['gg'] = "use support and supervision effectively, to maintain safe, effective, accountable and sustainable practice in a demanding working environment"
F['hh'] = "take responsibility for their own wellbeing, including by taking appropriate action and seeking support"
F['ve'] = "a commitment to professional social work practice, guided by the core values of the profession, ethical principles and a sense of global social responsibility"
F['psrb'] = "Demonstration of the minimum requirements set by the professional regulator, including the required number of days in practice"

H6 = 'qaa/fheq-2024/4.15'
hon('ku', "joined-up knowledge of the profession's context, knowledge base and its use", find=F['ku'], verbs=[], domain='knowledge',
    para="a joined-up knowledge and understanding of where professional social work takes place, of what the profession knows and of how that knowledge is used, across items a to m.",
    prac="a coherent grasp of the setting of professional social work, of its knowledge base and of how that knowledge is applied, as items a to m set out.",
    ben="a joined-up grasp of where social work happens, what the profession knows and how that knowledge is used in practice.",
    q="'Which part of social work's knowledge base can you link to something you did in practice?'",
    nb=sid('4.11.a', '4.11.m', '4.14.ku', '4.17.ku'), fw=H6 + '.b1, qaa/fqheis-2024/4.16.b1 and spine:6')
hon('a', "social work's role worldwide and across the UK nations", find=F['a'], verbs=[], domain='knowledge',
    para="an awareness of what social work does internationally, in the UK and in each of the four UK nations.",
    prac="awareness of the profession's role internationally, across the UK and within each of its four nations.",
    ben="that you know what social work does around the world, across the UK and in each of the four UK nations.",
    q="'How does social work differ between the nation you train in and another nation or country?'",
    nb=sid('4.11.b', '2.6'), fw=H6 + '.b1')
hon('b', 'social work across the sectors', find=F['b'], verbs=[], domain='knowledge',
    para="an understanding of how social work operates in statutory, independent and voluntary bodies and the wider third sector.",
    prac="understanding of how the profession works in statutory, independent and voluntary organisations and the third sector.",
    ben="that you understand how social work is done in statutory services, independent and voluntary organisations and the third sector.",
    q="'What changes for a social worker moving from a local authority to a charity?'",
    nb=sid('4.11.a', '4.11.t'), fw=H6 + '.b1')
hon('c', 'research as the evidence base for practice', find=F['c'], verbs=['identify', 'assess', 'apply'], domain='subject-skill',
    para="the ability to find, judge and critically use research so that professional practice rests on sound evidence.",
    prac="the ability to locate, appraise and critically apply research so that it grounds and steers practice.",
    ben="that you can find research, judge how good it is and use it critically so your practice rests on sound evidence.",
    q="'Can you name a study that changed how you would act in a case, and say how far you trusted it?'",
    nb=sid('4.11.o', '4.11.bb'), fw=H6 + '.b3.2 and ' + H6 + '.b2')
hon('d', 'theory, policy, law, methods and skills in practice', find=F['d'], verbs=['apply'], domain='understanding',
    para="a critical understanding of theory, policy, the legal framework, methods and skills, and of how each bears on practice.",
    prac="critical understanding of theory, policy, law, methods and skills, and of how each applies in practice.",
    ben="that you understand theory, policy, the law, methods and skills critically, and see how each one shapes what you do in practice.",
    q="'Which law or policy most shaped a decision you saw on placement, and what theory would explain it?'",
    nb=sid('4.11.n', '4.11.j'), fw=H6 + '.b1 and ' + H6 + '.b3.1')
hon('e', "the regulators' required knowledge, skills and behaviours", find=F['e'], verbs=[], domain='subject-skill',
    para="evidence of the knowledge, skills, broader behaviours or professional competences that the regulators require.",
    prac="evidence of the knowledge, skills, behaviours or competences that the relevant regulator requires.",
    ben="evidence that you have the knowledge, skills and professional behaviours your regulator asks for.",
    q="'Where in your portfolio is the evidence for each of your regulator's standards?'",
    nb=sid('4.11.psrb', '2.14', '4.1'), fw='qaa/fheq-2024/annex-d/professional/r1/3rd-1st')
hon('f', 'current debates on inequality, power and oppression', find=F['f'], verbs=[], domain='understanding',
    para="engagement with current cultural and social debates, for instance about inequality, power and oppression.",
    prac="engagement with present-day cultural and social debates, inequality, power and oppression among them.",
    ben="that you engage with today's cultural and social debates, for example about inequality, power and oppression.",
    q="'Which current debate about power or inequality affects the people you work with, and where do you stand?'",
    nb=sid('4.11.k', '4.11.i'), fw=H6 + '.b4')
hon('g', "climate and environmental justice and social work's part", find=F['g'], verbs=[], domain='understanding',
    para=("an understanding of why climate change, environmental and social justice, conflict and weakening democracy matter, of social work's part in "
          "meeting their effects on people and communities, and of how environmental harm and its threat to human rights fall hardest on those already "
          "facing poverty, racism, ableism or other disadvantage."),
    prac=("understanding of why climate change, environmental and social justice, conflict and democratic decline matter to the profession, of its role "
          "in responding to their effects, and of how environmental harm lands hardest on those already disadvantaged."),
    ben=("that you understand why climate change, environmental and social justice, conflict and threats to democracy matter for social work, what "
         "social workers can do about their effects, and why environmental harm hits people already facing poverty, racism or ableism hardest."),
    q="'How could a flood, a heatwave or rising energy bills change the needs of a family you work with?'",
    nb=sid('4.11.q', '1.26', '1.27'), fw=H6 + '.b4')
hon('h', 'need and risk', find=F['h'], verbs=['understand', 'identify', 'respond'], domain='subject-skill',
    para="the ability to recognise and make sense of need and risk and to respond to them fittingly.",
    prac="the ability to understand, identify and respond appropriately to need and risk.",
    ben="that you can recognise need and risk, make sense of them and respond in the right way.",
    q="'In your last assessment, what told you this was a risk and not just a need?'",
    nb=sid('4.11.i', '4.11.y'), fw=H6 + '.b9.2')
hon('i', 'intersecting factors in need and risk', find=F['i'], verbs=['respond', 'challenge'], domain='understanding',
    para="recognition of how overlapping parts of identity and disadvantage can shape need and risk, with the ability to respond and to challenge when needed.",
    prac="recognition of intersecting factors that bear on need and risk, and the ability to respond and challenge where required.",
    ben="that you can see how different parts of someone's identity and situation combine to affect need and risk, and that you respond and challenge when you need to.",
    q="'Whose combined circumstances did you nearly overlook, and what made you see them?'",
    nb=sid('4.11.h', '4.11.f', '4.11.k'), fw=H6 + '.b7')
hon('j', 'knowledge base and values across disciplines', find=F['j'], verbs=[], domain='understanding',
    para="an understanding of the profession's knowledge base and values and of how to apply them together when working with other disciplines.",
    prac="understanding of social work's knowledge and values and how to use them together in interdisciplinary work.",
    ben="that you understand what social work knows and values, and how to use both together when you work with other professions.",
    q="'What did you bring to a meeting with health or education colleagues that only social work could?'",
    nb=sid('4.11.t', '4.11.ku'), fw=H6 + '.b1')
hon('k', 'contested contexts and a commitment against oppression', find=F['k'], verbs=[], domain='understanding',
    para="critical awareness of disputed political and social contexts, with a commitment to practice that opposes discrimination, oppression and racism.",
    prac="critical awareness of contested political and social contexts and a commitment to practice that challenges discrimination, oppression and racism.",
    ben="that you are critically aware of disputed political and social contexts and committed to practice that stands against discrimination, oppression and racism.",
    q="'Where have you seen discrimination built into a system, and what could you do about it?'",
    nb=sid('4.11.u', '4.11.f', '1.20'), fw=H6 + '.b4')
hon('l', 'relating to people with lived experience and professionals', find=F['l'], verbs=['use', 'relate'], domain='subject-skill',
    para="the ability to draw on knowledge and understanding to work effectively with people who have lived experience and with other professionals, so that outcomes improve.",
    prac="the ability to use knowledge to build effective relationships with people with lived experience and with professionals, to improve outcomes.",
    ben="that you can use what you know to build good working relationships with people who use services and with other professionals, so that things get better for people.",
    q="'What did you do to build trust with someone who was wary of social workers?'",
    nb=sid('4.11.p', '4.11.r'), fw=H6 + '.b6')
hon('m', 'continuous learning, reflection and feedback', find=F['m'], verbs=['incorporate'], domain='generic-skill',
    para="continuing learning, reflection on experience and use of feedback, carried forward into later study and practice.",
    prac="ongoing learning, reflection on what they have experienced and use of feedback, built into later learning and practice.",
    ben="that you keep learning, reflect on your experience and use feedback, and carry what you learn into your next piece of study or practice.",
    q="'What feedback did you act on last term, and what changed because of it?'",
    nb=sid('4.11.ee', '4.11.ff'), fw=H6 + '.b5 and qaa/fheq-2024/annex-d/summary/r3/3rd')
hon('ds', 'consistent, reflective use of social work skills and methods', find=F['ds'], verbs=[], domain='subject-skill',
    para="consistent use of social work skills and reflective use of a range of methods, grounded in critical thinking, decisions informed by evidence and an understanding of varied practice settings, across items n to hh.",
    prac="a consistent use of social work skills and a reflective use of varied methods, resting on critical thinking, evidence-based decisions and understanding of different practice settings, as items n to hh set out.",
    ben="that you use social work skills consistently and choose and reflect on a range of methods, thinking critically and basing decisions on evidence.",
    q="'Which method did you choose for a recent piece of work, and why that one?'",
    nb=sid('4.11.n', '4.11.hh', '4.14.ds', '4.17.ds'), fw=H6 + '.b2 and spine:6')
hon('n', 'critical thinking informing practice', find=F['n'], verbs=['use', 'inform', 'drawing'], domain='subject-skill',
    para="the capacity to bring knowledge, understanding and critical thinking to bear on practice, using theory, policy, law, methods and skills.",
    prac="the capacity to let knowledge and critical thinking shape practice, drawing on theory, policy, law, methods and skills.",
    ben="that you can use your knowledge and critical thinking to shape your practice, drawing on theory, policy, the law, methods and skills.",
    q="'What did critical thinking change in a plan you made recently?'",
    nb=sid('4.11.d', '3.4'), fw=H6 + '.b3.1')
hon('o', 'research and evidence for decisions', find=F['o'], verbs=['use', 'evaluate', 'inform'], domain='subject-skill',
    para="the capacity to use and weigh research and other evidence when shaping practice and decisions.",
    prac="the capacity to use and evaluate research and wider evidence in practice and decision-making.",
    ben="that you can use and weigh up research and other evidence when you decide what to do.",
    q="'What evidence did you lean on for your last decision, and what would have made you doubt it?'",
    nb=sid('4.11.c', '4.11.bb'), fw=H6 + '.b7')
hon('p', 'relationships and partnership working', find=F['p'], verbs=['build', 'work'], domain='subject-skill',
    para="the capacity to form relationships and partnerships with people with lived or living experience and with professionals from other agencies.",
    prac="the capacity to build relationships and partnerships with people with lived experience and with professionals across agencies.",
    ben="that you can build relationships and work in partnership with people who use services and with professionals from other agencies.",
    q="'What did partnership look like in practice with someone you supported?'",
    nb=sid('4.11.l', '4.11.t', '2.34'), fw=H6 + '.b9.1')
hon('q', 'environmentally sustainable practice', find=F['q'], verbs=['practice'], domain='subject-skill',
    para="the capacity to work in ways that are environmentally sustainable.",
    prac="the capacity to practise in environmentally sustainable ways.",
    ben="that you can work in ways that look after the environment.",
    q="'What one change would make your practice more sustainable without costing the people you support?'",
    nb=sid('4.11.g', '1.28'), fw=H6 + '.b6')
hon('r', 'communication with people and professionals', find=F['r'], verbs=['communicate'], domain='generic-skill',
    para="the capacity to communicate well in speech, without words and in writing with people with lived experience and with professionals in many settings and at many levels.",
    prac="the capacity to communicate effectively, spoken, non-verbal and written, with people with lived experience and with professionals at all levels.",
    ben="that you can communicate well, by speaking, writing and through body language, with people who use services and with professionals in many settings.",
    q="'How did you adapt a written record so the person it was about could read it?'",
    nb=sid('4.11.l', '4.11.w'), fw=H6 + '.b8 and qaa/fheq-2024/annex-d/transferable/r1/3rd')
hon('s', 'teamwork and handling information', find=F['s'], verbs=['work', 'gathering', 'processing', 'analysing'], domain='generic-skill',
    para="the capacity to work inside teams, systems and processes, collecting, handling and analysing information to inform understanding and action.",
    prac="the capacity to work within teams and organisational systems, gathering and analysing information to support understanding and intervention.",
    ben="that you can work within teams and organisational systems, collecting and analysing information so you understand a situation and can act on it.",
    q="'What information did you gather that changed your team's view of a case?'",
    nb=sid('4.11.t', '4.11.w'), fw='qaa/fheq-2024/annex-d/transferable/r2/3rd')
hon('t', 'working across agencies and disciplines', find=F['t'], verbs=['work'], domain='subject-skill',
    para="the capacity to work across and alongside other agencies and disciplines.",
    prac="the capacity to work with and across other agencies and professions.",
    ben="that you can work with other agencies and professions and across the boundaries between them.",
    q="'When did another agency see a case differently from you, and how did you work it out?'",
    nb=sid('4.11.j', '4.11.p', '1.9'), fw=H6 + '.b9.1')
hon('u', 'values, ethics and anti-oppressive practice', find=F['u'], verbs=['demonstrate'], domain='subject-skill',
    para="the capacity to show social work values and ethics in action, with cultural humility and practice that opposes discrimination, oppression and racism.",
    prac="the capacity to apply the profession's values and ethics, including cultural humility and practice that counters discrimination, oppression and racism.",
    ben="that you can put social work values and ethics into action, with cultural humility and in ways that stand against discrimination, oppression and racism.",
    q="'What did cultural humility mean in a conversation you had with a family?'",
    nb=sid('4.11.k', '4.11.ve', '2.27'), fw=H6 + '.b9.1')
hon('v', 'personal and professional conduct', find=F['v'], verbs=['maintain', 'drawing'], domain='subject-skill',
    para="the capacity to keep fitting standards of personal and professional conduct, guided by the relevant codes and standards.",
    prac="the capacity to maintain proper personal and professional conduct, using the relevant codes of practice or standards.",
    ben="that you keep to proper standards of personal and professional behaviour, guided by the codes and standards that apply to you.",
    q="'Which part of your code of conduct is hardest to keep outside work, for example online?'",
    nb=sid('4.11.dd', '2.12', '2.19'), fw='qaa/fheq-2024/annex-d/professional/r2/3rd-1st')
hon('w', 'digital technology and information', find=F['w'], verbs=['engage', 'collate', 'analyse', 'select', 'record', 'present'], domain='generic-skill',
    para="the capacity to use digital technology critically to gather, analyse, choose, record and present information.",
    prac="the capacity to engage critically with digital tools to collate, analyse, select, record and present information.",
    ben="that you can use digital technology critically to gather, analyse, choose, record and present information.",
    q="'What did you leave out of a digital case record, and why?'",
    nb=sid('1.45', '1.46', '4.11.s'), fw='qaa/fheq-2024/annex-d/transferable/r1/3rd')
hon('x', 'autonomy and decisions within organisations', find=F['x'], verbs=['exercise', 'ensure'], domain='generic-skill',
    para="the capacity to use a suitable degree of independence and judgement within organisations so that practice stays safe and effective.",
    prac="the capacity to exercise suitable autonomy and decision-making within organisations, keeping practice safe and effective.",
    ben="that you can act with the right amount of independence and make decisions within your organisation so your practice stays safe and effective.",
    q="'Which decision did you take on your own last week, and which did you rightly take to a supervisor?'",
    nb=sid('4.11.aa', '4.11.dd'), fw=H6 + '.b9.2 and spine:6')
hon('y', 'improving outcomes and managing risk', find=F['y'], verbs=['support', 'manage', 'reduce'], domain='subject-skill',
    para="the capacity to help people improve their outcomes and to manage and lessen risk.",
    prac="the capacity to support people towards better outcomes and to manage and reduce risk.",
    ben="that you can help people improve their situation and manage and reduce risk.",
    q="'How did you balance someone's wishes against the risk in their situation?'",
    nb=sid('4.11.h', '4.11.aa'), fw=H6 + '.b9.2')
hon('z', 'dignity and strengths-based practice', find=F['z'], verbs=['recognise', 'working'], domain='subject-skill',
    para="the capacity to respect each person's dignity and to work in ways that build on strengths and empower.",
    prac="the capacity to recognise individual dignity and to practise in a strengths-based, empowering way.",
    ben="that you respect each person's dignity and work in ways that build on their strengths and give them more control.",
    q="'What strength did you find in someone that changed the plan you made with them?'",
    nb=sid('4.11.u', '1.48'), fw=H6 + '.b9.1')
hon('aa', 'difficult decisions, including restricting liberty', find=F['aa'], verbs=['make', 'implement', 'understanding'], domain='subject-skill',
    para="the capacity to take and carry out hard decisions, liberty-restricting ones included, in human situations that may bring benefit while understanding the harm involved.",
    prac="the capacity to make and carry out difficult decisions, including those that restrict liberty, weighing possible benefit against harm.",
    ben="that you can make and carry out hard decisions, including ones that limit someone's freedom, while weighing up the good and the harm they may do.",
    q="'What would you need to know before agreeing to a decision that limits someone's freedom?'",
    nb=sid('4.11.bb', '2.4', '4.11.x'), fw=H6 + '.b9.2')
hon('bb', 'defending decisions with evidence', find=F['bb'], verbs=['defend', 'drawing'], domain='subject-skill',
    para="the capacity to defend decisions with confidence, using a broad range of evidence.",
    prac="the capacity to justify decisions confidently on a wide evidence base.",
    ben="that you can explain and defend your decisions confidently, using a wide range of evidence.",
    q="'If a manager or a court questioned your last decision, what evidence would you point to?'",
    nb=sid('4.11.o', '4.11.aa'), fw=H6 + '.b3.1')
hon('cc', 'leadership and advocacy', find=F['cc'], verbs=['demonstrate'], domain='generic-skill',
    para="the capacity to show professional leadership and skill in advocacy.",
    prac="the capacity to show professional leadership and advocacy skills.",
    ben="that you can show leadership as a professional and speak up for the people you work with.",
    q="'When did you speak up for someone whose voice was not being heard?'",
    nb=sid('1.8', '2.8'), fw=H6 + '.b9.1 and qaa/fheq-2024/annex-d/transferable/r2/3rd')
hon('dd', 'professional boundaries', find=F['dd'], verbs=['maintain', 'working', 'identifying'], domain='subject-skill',
    para="the capacity to keep professional boundaries, stay within the limits of the role and find support when needed.",
    prac="the capacity to hold professional boundaries, work within the role's limits and identify support where needed.",
    ben="that you keep professional boundaries, stay within the limits of your role and know where to get support when you need it.",
    q="'Where was the edge of your role in a recent case, and who did you turn to?'",
    nb=sid('4.11.v', '4.11.gg'), fw=H6 + '.b9.1')
hon('ee', 'critical reflection on performance', find=F['ee'], verbs=['reflect', 'using'], domain='generic-skill',
    para="the capacity to reflect critically on one's own performance, drawing on feedback and evidence.",
    prac="the capacity to reflect critically on their own performance using feedback and evidence.",
    ben="that you can reflect critically on how you are doing, using feedback and evidence.",
    q="'What does the evidence say about your last piece of direct work, beyond how it felt?'",
    nb=sid('4.11.m', '4.11.ff'), fw='qaa/fheq-2024/annex-d/transferable/r5/3rd')
hon('ff', 'continuing professional development', find=F['ff'], verbs=['engage', 'identifying', 'resolve'], domain='generic-skill',
    para="the capacity to take part in continuing professional development, spotting gaps in knowledge and how to close them.",
    prac="the capacity to pursue continuing professional development, identifying knowledge gaps and how to address them.",
    ben="that you keep developing as a professional, noticing gaps in what you know and finding ways to fill them.",
    q="'What gap in your knowledge did you notice this month, and what is your plan for it?'",
    nb=sid('4.11.m', '4.11.ee'), fw=H6 + '.b9.3')
hon('gg', 'support and supervision', find=F['gg'], verbs=['use', 'maintain'], domain='subject-skill',
    para="the capacity to make good use of support and supervision so that practice stays safe, effective, accountable and sustainable under heavy demands.",
    prac="the capacity to use support and supervision well, keeping practice safe, effective, accountable and sustainable under pressure.",
    ben="that you make good use of support and supervision so that your work stays safe, effective, accountable and sustainable when the pressure is on.",
    q="'What did you bring to your last supervision, and what did you take away?'",
    nb=sid('4.11.dd', '4.11.hh'), fw=H6 + '.b9.1')
hon('hh', 'own wellbeing', find=F['hh'], verbs=['take', 'taking', 'seeking'], domain='generic-skill',
    para="the capacity to take responsibility for one's own wellbeing, acting appropriately and seeking support.",
    prac="the capacity to take responsibility for their own wellbeing, acting appropriately and seeking support.",
    ben="that you look after your own wellbeing, taking sensible action and asking for support when you need it.",
    q="'What tells you that you need to step back and ask for support?'",
    nb=sid('4.11.gg', '4.11.dd'), fw=H6 + '.b9.1')
hon('ve', 'commitment to professional values and ethics', find=F['ve'], verbs=['guided'], domain='subject-skill',
    para="a commitment to professional social work practice steered by the profession's core values, ethical principles and a sense of responsibility to the wider world.",
    prac="a commitment to professional practice led by the profession's core values and ethics and by a sense of global social responsibility.",
    ben="that you are committed to professional social work practice, guided by its core values, its ethics and a sense of responsibility to people everywhere.",
    q="'Which core value of the profession did you find hardest to hold to this year?'",
    nb=sid('4.11.u', '2.27', '4.14.ve', '4.17.ve'), fw=H6 + '.b9.1')
hon('psrb', "the regulator's minimum requirements, including practice days", find=F['psrb'], verbs=[], domain='subject-skill',
    para="that the professional regulator's minimum requirements are met, the required number of practice days included.",
    prac="that the regulator's minimum requirements are met, including the set number of practice days.",
    ben="that you meet the minimum requirements of your regulator, including the number of days in practice it sets.",
    q="'How many practice days does your regulator require, and how many have you logged?'",
    nb=sid('4.10', '4.11.e', '4.14.psrb', '4.17.psrb'), fw='qaa/fheq-2024/annex-d/professional/r1/3rd-1st')

# ---- integrated master's (4.14): lead-in "graduates will have demonstrated the following"
H7 = 'qaa/fheq-2024/4.17'
def ima(key, cite, about, para, prac, ben, q, nb, fw, **k):
    rung('4.14.' + key, IMA, '4.14 (' + cite + ')', about, nb, fw, "an integrated master's student or team looks at " + about, q,
         para='Will have shown ' + para, prac="At threshold, integrated master's graduates will have shown " + prac,
         ben="To reach the minimum for your integrated master's, you will have shown " + ben, **k)
ima('ku', 'knowledge and understanding', "broad, critical knowledge of the profession's context and knowledge base",
    find="a broad and critical knowledge and understanding of the context of professional social work, the knowledge base of social work and its practical application (paragraph 4.11 a-m)",
    verbs=[], domain='knowledge',
    para="a wide and critical knowledge and understanding of where social work takes place, what it knows and how that is used, across the areas of 4.11 a to m.",
    prac="a broad, critical command of the setting, knowledge base and use of social work knowledge, covering 4.11 a to m.",
    ben="a wide and critical grasp of where social work happens, what the profession knows and how that knowledge is used.",
    q="'Where does your knowledge now go beyond what an honours graduate would know?'",
    nb=sid('4.11.ku', '4.17.ku', '4.12'), fw=H7 + '.b1 and spine:7')
ima('inquiry', 'knowledge and understanding', 'a self-directed inquiry project',
    find="Evidence of achievement in completion of an element of self-directed study, involving personal inquiry, for example a research project or synoptic project.",
    verbs=['involving'], domain='subject-skill',
    para="evidence of completing a piece of self-directed study built on personal inquiry, such as a research or synoptic project.",
    prac="evidence of a completed self-directed element of personal inquiry, such as a research or synoptic project.",
    ben="that you have completed a piece of independent study driven by your own inquiry, such as a research project or a project that draws your learning together.",
    q="'What question did your project set out to answer, and who chose it?'",
    nb=sid('4.17.inquiry', '4.11.c'), fw=H7 + '.b2 and ' + H7 + '.b6')
ima('ds', 'demonstrable skills', 'consistent use of social work skills',
    find="a consistent application of social work skills (paragraph 4.11 n-hh)", verbs=[], domain='subject-skill',
    para="consistent use of the social work skills of 4.11 n to hh.",
    prac="a consistent use of the skills listed at 4.11 n to hh.",
    ben="that you use the core social work skills consistently.",
    q="'Which of the core skills do you use least confidently, and where could you practise it?'",
    nb=sid('4.11.ds', '4.14.methods'), fw=H7 + '.b5')
ima('methods', 'demonstrable skills', 'consistent, reflective methods with nuanced understanding of settings',
    find=("The consistent and reflective application of a range of social work methods, underpinned by critical thinking, evidence-informed "
          "decision-making, and a nuanced understanding of diverse practice context"), verbs=[], domain='subject-skill',
    para="consistent and reflective use of a range of social work methods, resting on critical thinking, evidence-based decisions and a finely judged grasp of varied practice settings.",
    prac="consistent, reflective use of varied methods, grounded in critical thinking, evidence-informed decisions and a nuanced reading of different practice settings.",
    ben="that you use a range of social work methods consistently and reflectively, think critically, base decisions on evidence and read different practice settings with care.",
    q="'How did the setting change the method you chose in a recent piece of work?'",
    nb=sid('4.11.ds', '4.17.practice'), fw=H7 + '.b5 and ' + H7 + '.b6')
ima('ve', 'values and ethics', 'commitment to and critical understanding of values',
    find="a commitment to and critical understanding of professional social work practice, guided by the core values of the profession, ethical principles, and a sense of global social responsibility",
    verbs=['guided'], domain='subject-skill',
    para="a commitment to, and a critical understanding of, professional practice led by the profession's core values, ethics and a sense of global social responsibility.",
    prac="commitment to and critical understanding of professional practice shaped by core values, ethics and global social responsibility.",
    ben="that you are committed to professional social work practice and understand critically how its values, ethics and responsibility to people everywhere shape it.",
    q="'Where would you challenge how a core value is usually applied, and why?'",
    nb=sid('4.11.ve', '4.17.ve'), fw=H7 + '.b8.1')
ima('psrb', 'PSRB requirements', "the regulator's minimum requirements, including practice days",
    find=F['psrb'], after="a nuanced understanding of diverse practice context", verbs=[], domain='subject-skill',
    para="that the professional regulator's minimum requirements are met, the required practice days included.",
    prac="that the regulator's minimum requirements, including practice days, are met.",
    ben="that you meet your regulator's minimum requirements, including the number of practice days.",
    q="'Which regulator's requirements apply to your course, and are your practice days complete?'",
    nb=sid('4.11.psrb', '4.13'), fw='qaa/fheq-2024/annex-d/professional/r1/3rd-1st')

# ---- postgraduate master's (4.17): lead-in "graduates will have demonstrated the following"
def mas(key, cite, about, para, prac, ben, q, nb, fw, **k):
    rung('4.17.' + key, MA, '4.17 (' + cite + ')', about, nb, fw, "a master's student or team looks at " + about, q,
         para='Will have shown ' + para, prac="At threshold, master's graduates will have shown " + prac,
         ben="To reach the minimum for your master's, you will have shown " + ben, **k)
mas('ku', 'knowledge and understanding', "critically informed understanding of contexts and a sophisticated grasp of the knowledge base",
    find="A critically informed understanding of the contexts shaping professional social work, alongside a sophisticated grasp of its knowledge base (paragraph 4.11 a-m)",
    verbs=[], domain='knowledge',
    para="a critically informed understanding of what shapes professional social work and a sophisticated command of its knowledge base, across 4.11 a to m.",
    prac="critically informed understanding of the forces shaping the profession and a sophisticated grasp of its knowledge base, covering 4.11 a to m.",
    ben="a critical understanding of what shapes social work and a sophisticated grasp of what the profession knows.",
    q="'Which part of social work's knowledge base would you now question, and on what grounds?'",
    nb=sid('4.11.ku', '4.14.ku', '4.17.concepts'), fw=H7 + '.b1 and spine:7')
mas('concepts', 'knowledge and understanding', 'interrogating and applying complex concepts',
    find="the capacity to interrogate and apply complex concepts to practice with intellectual rigour and reflexivity",
    verbs=['interrogate', 'apply'], domain='understanding',
    para="the capacity to question and apply complex concepts in practice with rigour and reflexivity.",
    prac="the capacity to interrogate complex concepts and apply them to practice rigorously and reflexively.",
    ben="that you can question complex ideas and apply them to practice with rigour, while staying aware of your own part in what you see.",
    q="'Which concept did you have to adapt to make sense of a real case?'",
    nb=sid('4.17.ku', '4.17.practice'), fw=H7 + '.b4.1 and ' + H7 + '.b3')
mas('inquiry', 'knowledge and understanding', 'self-directed inquiry with original insight',
    find="Evidence of achievement in completion of an element of self-directed study, involving personal inquiry, for example a research project or synoptic project and the ability to generate original insights",
    verbs=['involving', 'generate'], domain='subject-skill',
    para="evidence of completing self-directed study built on personal inquiry, such as a research or synoptic project, and the ability to reach original insights.",
    prac="evidence of a completed self-directed inquiry, such as a research or synoptic project, and the ability to produce original insights.",
    ben="that you have completed a piece of independent study driven by your own inquiry and can come up with insights of your own.",
    q="'What did your project show that you could not have found in the existing literature?'",
    nb=sid('4.14.inquiry', '4.11.c'), fw=H7 + '.b3 and ' + H7 + '.b6')
mas('ds', 'demonstrable skills', 'consistent use of social work skills and methods',
    find="a consistent application of social work skills and methods (paragraph\n4.11 n-hh)", verbs=[], domain='subject-skill',
    para="consistent use of the skills and methods of 4.11 n to hh.",
    prac="a consistent use of the skills and methods set out at 4.11 n to hh.",
    ben="that you use the core social work skills and methods consistently.",
    q="'Which core skill do you rely on most, and which do you avoid?'",
    nb=sid('4.11.ds', '4.14.ds'), fw=H7 + '.b5')
mas('practice', 'demonstrable skills', 'practice grounded in critical thinking and evidence',
    find="Practice is underpinned by critical thinking, evidence-informed decision-making, and understanding of the complexities inherent in diverse practice environments",
    verbs=['underpinned'], domain='subject-skill',
    para="practice that rests on critical thinking, decisions informed by evidence and an understanding of the complexity of different practice environments.",
    prac="practice grounded in critical thinking, evidence-informed decisions and a grasp of the complexity of varied practice environments.",
    ben="that your practice rests on critical thinking and evidence, and that you understand how complex different practice settings can be.",
    q="'What made the setting of your last placement complex, and how did that shape your decisions?'",
    nb=sid('4.14.methods', '4.17.judgement'), fw=H7 + '.b5')
mas('judgement', 'demonstrable skills', 'professional judgement in ethically hard situations',
    find="Exercise professional judgement in ethically challenging situations", verbs=['exercise'], domain='subject-skill',
    para="professional judgement in situations that are ethically difficult.",
    prac="sound professional judgement in ethically challenging situations.",
    ben="that you can make sound professional judgements when a situation is ethically difficult.",
    q="'What made a recent situation ethically hard, and how did you reach your judgement?'",
    nb=sid('4.11.aa', '4.17.ve'), fw=H7 + '.b5 and ' + H7 + '.b8.2')
mas('ve', 'values and ethics', 'commitment to, critical understanding and application of values',
    find="a commitment to and critical understanding and application of professional social work practice, guided by the core values of the profession, ethical principles, and a critical understanding of global social responsibility",
    verbs=['guided'], domain='subject-skill',
    para="a commitment to, and critical understanding and use of, professional practice led by core values, ethics and a critical view of global social responsibility.",
    prac="commitment to professional practice, with critical understanding and use of it, shaped by core values, ethics and a critical grasp of global social responsibility.",
    ben="that you are committed to professional social work practice, understand and apply its values and ethics critically, and think critically about responsibility to people everywhere.",
    q="'How would you explain global social responsibility to a colleague who thinks it is not part of the job?'",
    nb=sid('4.11.ve', '4.14.ve'), fw=H7 + '.b8.1')
mas('psrb', 'PSRB requirements', "the regulator's minimum requirements, including practice days",
    find=F['psrb'], after="a critical understanding of global social responsibility", verbs=[], domain='subject-skill',
    para="that the professional regulator's minimum requirements are met, the required practice days included.",
    prac="that the regulator's minimum requirements, including practice days, are met.",
    ben="that you meet your regulator's minimum requirements, including the number of practice days.",
    q="'Which regulator's requirements apply to your course, and are your practice days complete?'",
    nb=sid('4.11.psrb', '4.16'), fw='qaa/fheq-2024/annex-d/professional/r1/3rd-1st')

GRADE = {}   # one rung only (threshold): no same-outcome link one rung below
TH = {'1.14': 'theme:edi', '1.17': 'theme:edi', '1.24': 'theme:accessibility',
      '1.45': 'theme:generative-ai', '1.46': 'theme:generative-ai', '1.48': 'theme:generative-ai'}

S5 = dict(
    levels=[dict(id='fheq:6', role='cites', locator='D1, 2.23; 2.28; 2.30; 4.5; 4.7'),
            dict(id='fheq:7', role='cites', locator='D1, 2.23; 2.30; 4.5; 4.15'),
            dict(id='fqheis:9', role='cites', locator='D1, 2.29 (ordinary degree and Scottish MA)'),
            dict(id='fqheis:10', role='cites', locator='D1, 2.23; 2.29; 2.30; 4.5; 4.7'),
            dict(id='fqheis:11', role='cites', locator='D1, 2.23; 2.30; 4.5')],
    crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent',
                     basis='stated (D1, 2.23; 2.30; 4.5: honours at FHEQ Level 6, SCQF Level 10 in Scotland); agrees with std:doc:qaa-fheq-2024-framework S5 (Table 1)'),
                dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent',
                     basis="stated (D1, 2.23; 2.30; 4.5: integrated master's and master's at FHEQ Level 7, SCQF Level 11); agrees with std:doc:qaa-fheq-2024-framework S5 (shared descriptor 4.17)")])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['front matter', '1.12', '1.13', '1.14', '1.15', '1.16', '1.17', '1.18', '1.19', '1.20', '1.21', '1.47', '3.1', '3.9']),
      dict(id='theme:accessibility', role='carries', carriedIn=['front matter', '1.14', '1.17', '1.22', '1.23', '1.24', '1.25', '1.46', '2.32', '3.6', '3.8']),
      dict(id='theme:esd', role='carries', carriedIn=['front matter', '1.26', '1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33', '1.37', '2.32']),
      dict(id='theme:enterprise', role='carries', carriedIn=['front matter', '1.34', '1.35', '1.36', '1.37', '1.38', '1.39', '1.40', '1.41', '1.42', '1.43', '1.44']),
      dict(id='theme:generative-ai', role='carries', carriedIn=['front matter', '1.45', '1.46', '1.47', '1.48'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-social-work-2019-benchmarks (not yet ingested)',
           note='the fourth edition, 2019, a minor update of the 2016 statement (D1, section 6); this is the fifth edition (back matter)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D',
           note="the degree classification descriptions for honours (4.7); threshold maps to a third, typical to a 2.2 or 2.1, excellent to a first"),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='FHEQ Levels 6 and 7 (2.23, 2.28, 2.30, 4.5, 4.15)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='SCQF/FQHEIS Levels 9, 10 and 11 (2.23, 2.29, 2.30, 4.5, 4.7)'),
      dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='quoted on ESD as a lens (1.32)'),
      dict(rel='refersTo', target='QAA Quality Code (2024 update) and QAA Glossary (not ingested)', note='front matter'),
      dict(rel='refersTo', target="QAA, Creating Inclusive Subject Learning Communities (not ingested)", note='1.17'),
      dict(rel='refersTo', target='QAA advice and resources on Generative AI (not ingested)', note='1.46'),
      dict(rel='refersTo', target='Social Care Wales requirements: framework for Social Work Qualifications, National Occupational Standards, Code of Professional Practice for Social Care (not yet ingested)', note='2.11, 2.12'),
      dict(rel='refersTo', target='Social Work England: Education and Training Standards, Professional Standards, knowledge, skills and behaviours (not yet ingested)', note='2.14, 2.15'),
      dict(rel='refersTo', target='Northern Ireland Framework Specification for the Degree in Social Work (2015); Standards of Conduct and Practice (not yet ingested)', note='2.17, 2.19'),
      dict(rel='refersTo', target='SSSC: Standards in Social Work Education and Ethical Principles; Scottish Requirements for Social Work Education (not yet ingested)', note='2.21'),
      dict(rel='readWith', target='std:doc:qaa-social-policy-2026-benchmarks', note='inferred: a neighbouring 2026 social science statement; no citation in the text')]
S8 = {'published': '2026-04', 'lastReviewed': 'none-stated', 'reviewCycle': 'none-stated',
      'consultation': 'none-stated (advisory group named, section 6)', 'replacedBy': 'none', 'other': 'Fifth Edition, published 16 April 2026 (back matter)'}

SB1 = [
    'A practice-based profession and an academic discipline, framed by the IFSW global definition: social change, cohesion, empowerment and liberation, on principles of social justice, human rights, collective responsibility and respect for diversity (D1, 1.1, 2.1).',
    'An academic subject applied through professional practice, marked by work in complex social situations to protect and promote individual and collective wellbeing (D1, 1.7, 2.1).',
    'Integrated study of knowledge, skills and values with critical use of research, so that practice is central to learning, in placements and in other experiential settings (D1, 1.10, 2.2, 3.4).',
    'Values and ethics at its root, including hard decisions that may restrict liberty, and a commitment against discrimination, oppression and racism (D1, 1.20, 2.4).',
    'A regulated profession with a protected title in each UK nation; regulators approve courses and register students and practitioners (D1, 1.4, 1.5, 2.9 to 2.22).',
    'Its nature and scope are themselves contested and keep changing with social, political and economic pressures (D1, 2.5, 2.7, 2.8).',
    'People with lived or living experience take part in teaching, design, assessment and review (D1, 2.1, 2.34, 2.35, 2.41, 3.6).']
SB2 = [
    dict(theme='theme:edi', inThisSubject="headed equity, equality, diversity and inclusion (EEDI): central to the subject's practice; intersectionality, anti-oppressive and anti-racist values across design, content, teaching and assessment, a named commitment against anti-Black racism, decolonising the curriculum and the legal duty to adjust (D1, 1.12 to 1.21)",
         statements=['1.14', '1.17', '4.11.f', '4.11.i', '4.11.k', '4.11.u']),
    dict(theme='theme:accessibility', inThisSubject='headed accessibility and the needs of disabled students: equality and Welsh-language law across the four nations, anticipatory adjustments in practice settings as well as on campus, and access support such as bursaries and lent laptops (D1, 1.22 to 1.25)',
         statements=['1.14', '1.17', '1.24']),
    dict(theme='theme:esd', inThisSubject="social work's place in sustainable development and climate impacts, three generations of rights, the SDGs and UNESCO competencies, and an outcome on environmentally sustainable practice (D1, 1.26 to 1.33; 4.11 g, q)",
         statements=['4.11.g', '4.11.q']),
    dict(theme='theme:enterprise', inThisSubject='headed employability, entrepreneurship and enterprise education: an entrepreneurial mindset read as professional identity, behaviours, attributes and skills for practice, and careers beyond statutory settings (D1, 1.34 to 1.44)',
         statements=[]),
    dict(theme='theme:generative-ai', inThisSubject='critical, lawful and ethical use of AI in learning and practice, integrity procedures, and values that keep human relationships first (D1, 1.45 to 1.48)',
         statements=['1.45', '1.46', '1.48', '4.11.w'])]
SB3 = dict(
    areas=[dict(component='3.1', gloss='principles for content: relevant, current, evidence-informed and coherent; inclusive and decolonised'),
           dict(component='3.2', gloss='theoretical, factual (research) and practice knowledge'),
           dict(component='3.3', gloss='research, theory, skills, methods, values and ethics, social policy, law, service leadership and delivery, UK and global contexts')],
    practices=[dict(component='3.4', kind='learning', gloss='practice-based learning in work settings: direct work, observation, shadowing, supervision and reflection'),
               dict(component='3.6', kind='teaching', gloss='scaffolded teaching from induction, with academics, researchers, practitioners and people with lived experience'),
               dict(component='3.7', kind='teaching', gloss='five learning themes carried by lectures, workshops, problem-based learning, simulation, role play and practice'),
               dict(component='3.8', kind='assessment', gloss='inclusive, accessible assessment with feedback and feed forward; judging readiness for practice'),
               dict(component='3.9', kind='assessment', gloss='a diverse range of methods and assessors, including people with lived experience')])
SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='4.11 (requirement 4.9)', award=HON, items=38),
           dict(rung='threshold', leadIn='4.14 (requirement 4.13)', award=IMA, items=6),
           dict(rung='threshold', leadIn='4.17 (requirement 4.16)', award=MA, items=8),
           dict(rung='typical', leadIn='none', award=HON, items=0),
           dict(rung='excellent', leadIn='none', award=HON, items=0)],
    rungBases=("4.7: threshold maps to a third, typical to a 2.2 or 2.1 and excellent to a first, by reference to Annex D (qaa/fheq-2024/annex-d/summary/*); "
               "4.8: classes above threshold for integrated master's and merit and distinction for master's follow the provider's marking schemes. "
               "Threshold items total 52, by award as above"),
    outcomeLists=[],
    outcomes=[dict(outcome="knowledge and understanding headline", threshold='4.11.ku', typical='none', excellent='none', basis='stated', domain='knowledge', award=HON),
              dict(outcome="demonstrable skills headline", threshold='4.11.ds', typical='none', excellent='none', basis='stated', domain='subject-skill', award=HON),
              dict(outcome="values and ethics", threshold='4.11.ve', typical='none', excellent='none', basis='stated', domain='subject-skill', award=HON),
              dict(outcome="regulator's requirements", threshold='4.11.psrb', typical='none', excellent='none', basis='stated', domain='subject-skill', award=HON)])
SB4A_FULL = []
SB5 = [
    dict(body='Social Care Wales', says='the Welsh regulator (replacing the Care Council for Wales); approves courses, sets the qualifications framework and Code of Professional Practice, and registers students (D1, 1.4, 2.10, 2.11, 2.12)', requirements='not yet ingested (Part E)'),
    dict(body='Social Work England', says="the regulator for England; approves courses against its Education and Training Standards and Professional Standards and registers graduates; post-qualifying Knowledge and Skills Statements and the supported first year (D1, 1.4, 2.13, 2.14, 2.15)", requirements='not yet ingested (Part E)'),
    dict(body='Northern Ireland Social Care Council', says='the Northern Ireland regulator; with the Department of Health produced the framework specification; registers students and graduates, the latter subject to an Assessed Year in Employment; standards of conduct (D1, 1.4, 2.16 to 2.19)', requirements='not yet ingested (Part E)'),
    dict(body='Scottish Social Services Council (SSSC)', says='the Scottish regulator; approves all qualifying courses, keeps registers, sets codes and regulates training; the honours or postgraduate route to qualify (D1, 1.4, 2.20, 2.21, 2.22)', requirements='not yet ingested (Part E)'),
    dict(body='Professional Standards Authority', says='oversees Social Work England and eight other health and care regulators (D1, 2.14)', requirements='not-applicable-by-design'),
    dict(body='International Federation of Social Workers (IFSW)', says='source of the global definition and principles framing the subject; supports the UN SDGs (D1, 1.1, 1.14, 1.26, 1.32, 2.1)', requirements='not-applicable-by-design'),
    dict(body='Equality and Human Rights Commission; Equality Commission for Northern Ireland', says='equality reference points; providers writing competence standards should follow the EHRC guidance (D1, 1.13, 4.2)', requirements='not-applicable-by-design'),
    dict(body='Department of Health (Northern Ireland); Northern Ireland Assembly', says='co-author of the framework specification; oversight of education and health and social care in Northern Ireland (D1, 2.17)', requirements='not-applicable-by-design')]
SB6 = dict(
    themes=[dict(id='theme:edi', named='Equity, equality, diversity and inclusion (EEDI)', carriedIn=S6[0]['carriedIn'], statements=[SID + x for x in SB2[0]['statements']]),
            dict(id='theme:accessibility', named='Accessibility and the needs of disabled students', carriedIn=S6[1]['carriedIn'], statements=[SID + x for x in SB2[1]['statements']]),
            dict(id='theme:esd', named='Education for sustainable development (ESD)', carriedIn=S6[2]['carriedIn'], statements=[SID + x for x in SB2[2]['statements']]),
            dict(id='theme:enterprise', named='Employability, entrepreneurship and enterprise education (EEE)', carriedIn=S6[3]['carriedIn'], statements=[]),
            dict(id='theme:generative-ai', named='Generative artificial intelligence (GenAI)', carriedIn=S6[4]['carriedIn'], statements=[SID + x for x in SB2[4]['statements']])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.23', '2.28', '2.30', '4.5', '4.7', '4.15']),
                dict(framework='scqf', levels=['fqheis:9', 'fqheis:10', 'fqheis:11'], citedIn=['2.23', '2.29', '2.30', '4.5', '4.7'])],
    bodies=[dict(body='Social Care Wales', citedIn=['1.4', '2.10', '2.11', '2.12']),
            dict(body='Social Work England', citedIn=['1.4', '2.13', '2.14', '2.15']),
            dict(body='Northern Ireland Social Care Council', citedIn=['1.4', '2.16', '2.17', '2.18', '2.19']),
            dict(body='Scottish Social Services Council', citedIn=['1.4', '2.20', '2.21', '2.22']),
            dict(body='Professional Standards Authority', citedIn=['2.14']),
            dict(body='International Federation of Social Workers', citedIn=['1.1', '1.14', '1.26', '1.32', '2.1']),
            dict(body='Equality and Human Rights Commission', citedIn=['1.13', '4.2']),
            dict(body='professional, statutory and regulatory bodies (PSRBs), named generically', citedIn=['front matter', '4.2', '4.9', '4.11', '4.13', '4.14', '4.17'])],
    sharedDocuments=[
        dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['4.7'],
             role='common descriptions of the four honours classes; the statement maps threshold, typical and excellent onto them'),
        dict(document='std:doc:qaa-fheq-2024-framework', named='FHEQ (Level 6, Level 7); the Qualifications Frameworks', citedIn=['2.23', '2.28', '2.30', '4.5', '4.15'], role='levels of the awards'),
        dict(document='std:doc:qaa-fqheis-2024-framework', named='SCQF/FQHEIS (Levels 9, 10, 11)', citedIn=['2.23', '2.29', '2.30', '4.5', '4.7'], role='Scottish levels of the awards'),
        dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='QAA/Advance HE Guidance on ESD (2021)', citedIn=['1.32'], role='quoted on ESD as a lens'),
        dict(document='QAA Quality Code, 2024 update (not ingested)', named='the Quality Code', citedIn=['front matter'], role='a further reference point'),
        dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
        dict(document='QAA Creating Inclusive Subject Learning Communities (not ingested)', named="QAA's Creating Inclusive Subject Learning Communities", citedIn=['1.17'], role='further guidance on inclusion'),
        dict(document='QAA advice and resources on Generative AI (not ingested)', named='QAA advice and resources on Generative AI', citedIn=['1.46'], role='further guidance on AI'),
        dict(document='Equality Act 2010 (law)', named='The Equality Act 2010', citedIn=['1.13', '1.22', '4.2'], role='equality duties and competence standards'),
        dict(document='Welsh Language (Wales) Measure 2011 (law)', named='The Welsh Language (Wales) Measure 2011', citedIn=['1.22'], role='Welsh language in education and social care'),
        dict(document='Special Educational Needs and Disability (Northern Ireland) Order 2005 (law)', named='The Special Educational Needs and Disability (Northern Ireland) Order 2005', citedIn=['1.22'], role='the Northern Ireland access duty'),
        dict(document='UN Sustainable Development Goals (external)', named="United Nation's Sustainable Development Goals (SDGs)", citedIn=['1.29', '1.30', '1.32', '1.33'], role='frame of the ESD theme'),
        dict(document='IFSW Global Definition of the Social Work Profession, 2014 (external)', named='Global Definition of the Social Work Profession (IFSW 2014)', citedIn=['1.1', '2.1'], role='definition framing the subject')])

B1 = [
    dict(slug='practice-social-work-education', definition="learning in professional work-based settings (placement) and in other experiential settings, classroom activity included, sometimes supported by people with lived experience (D1, 1.10)",
         beneficiaryDefinition='the part of your course where you learn by doing, on placement and in other hands-on settings', scopeNote="the statement's own sense of 'practice'", category='unknown', practices=['education']),
    dict(slug='threshold-level-attainment', definition="the minimum standard a student must show for the award, which the statement maps to a third (honours) or a pass (master's) (D1, 4.3, 4.7, 4.13, 4.16)",
         beneficiaryDefinition='the minimum you must reach to gain your award', scopeNote="typical maps to a 2.2 or 2.1 and excellent to a first (4.7); no lists for them", category='unknown', practices=['education']),
    dict(slug='intersectionality', definition='the interconnected nature of social categories such as race or ethnicity, class and gender (D1, 1.15)',
         beneficiaryDefinition='how different parts of who someone is combine to shape their experience', scopeNote='used in 1.12, 1.15 and 4.11 i', category='unknown', practices=['social work', 'education']),
    dict(slug='eedi', definition='equity, equality, diversity and inclusion, covering a wide range of identity characteristics (D1, 1.12)',
         beneficiaryDefinition='fairness, equal treatment, diversity and inclusion', scopeNote="the statement's name for the EDI theme", category='unknown', practices=['education']),
    dict(slug='generations-of-rights', definition='first generation civil and political rights; second socio-economic and cultural rights; third rights to the natural world, biodiversity and fairness between generations (D1, 1.26)',
         beneficiaryDefinition='three kinds of human rights: freedoms, living standards and a healthy planet', scopeNote='after the IFSW', category='unknown', practices=['social work'])]
B2A = [
    dict(concept='practice-social-work-education', form='practice', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
    dict(concept='practice-social-work-education', form='placement', lang='en', partOfSpeech='noun', termStatus='admitted', register='discipline-specific'),
    dict(concept='threshold-level-attainment', form='threshold level', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='intersectionality', form='intersectionality', lang='en', partOfSpeech='noun', termStatus='preferred', register='discipline-specific'),
    dict(concept='eedi', form='equity, equality, diversity and inclusion (EEDI)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
    dict(concept='generations-of-rights', form='first, second and third generation rights', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific')]
B4 = []; B5 = []
D3 = [dict(source="the regulators' requirement documents (Social Care Wales, Social Work England, NISCC, SSSC) named in 2.11 to 2.21 and section 5", why='SB5 requirements, to ingest as standards documents of their own'),
      dict(source='QAA Subject Benchmark Statement: Social Work, fourth edition (2019)', why='S7 supersedes; a comparison of editions')]

E = [
    'Rungs: one only. The statement gives threshold lists for three awards (honours 4.11, integrated master\'s 4.14, master\'s 4.17) and no typical or excellent lists; 4.7 maps threshold to a third, typical to a 2.2 or 2.1 and excellent to a first through Annex D. SB4 records typical and excellent as stated by name only (items 0). Pattern differs from Psychology (three listed rungs) and matches the threshold-only shape (Archaeology).',
    'Skeleton correction: 4.11 was one candidate (4.11.b1) holding the whole list; it is cut here by the issuer\'s letters a) to hh) as 4.11.a to 4.11.hh (34 records), plus four category headlines 4.11.ku (knowledge and understanding), 4.11.ds (demonstrable skills), 4.11.ve (values and ethics) and 4.11.psrb (PSRB requirements). The letter ids keep the issuer\'s numbering, which 4.14 and 4.17 cite ("4.11 a-m", "4.11 n-hh"). The builder\'s heading path is empty for the letter ids a to z (it reads only numeric parts); cosmetic, for P3.',
    'Skeleton correction: 4.3.b1 to 4.3.b3 (marked threshold) are the three awards the standards cover, not outcomes; not recorded as statements. 4.3 is a lead-in to section 4 (S3 gloss).',
    'Skeleton correction: 4.14 and 4.17 were single paragraphs with no candidates; cut into 6 and 8 records by category and sentence, each with `find`. The references "(paragraph 4.11 a-m)" and "(paragraph 4.11 n-hh)" are kept inside the headline spans as cross-references and never made statements (DPN-1); in 4.17 "(paragraph" is split across a page break in the held text.',
    'Pattern: master\'s standards are separate paragraphs for two further awards (integrated master\'s, postgraduate master\'s), recorded as rung threshold with award and level fheq:7 by the convention; the `.masters` id suffix is not used because the paragraph number already separates the award. The master\'s statements are stronger headlines over the same lettered outcomes, not new lists. 4.12 says integrated master\'s degrees must meet both the undergraduate and the master\'s standards, so 4.11 a to hh also hold for them (not duplicated as records).',
    'Pattern: the honours threshold is a lead-in ("graduates will have demonstrated the following") followed by four category headings, two of them with lettered lists run inline (a) to hh)) rather than bullets. Force is `threshold` from 4.3 and 4.9 (minimum standards; "must demonstrate at least a threshold-level"), with forceFrom the lead-in paragraph.',
    'Pattern: a fourth category of threshold outcome, "PSRB requirements", recorded as a rung item (4.11.psrb, 4.14.psrb, 4.17.psrb); the number of practice days is left to the regulator (4.10, 4.13, 4.16).',
    'No gradeOf links: a single rung, and the master\'s headlines are other awards, not a rung below. SB4 `outcomes` lists only the four honours category headlines.',
    'Verbs empty: the knowledge items a), b), e), f), g), j), k) and the category headlines are noun phrases with no action verb in the span; `verbs: []`.',
    'Obliging words outside the five, recorded as describes for Abbott: "duty" (1.14), "legal duty" (1.17), "expected to" (1.24, 2.34, 2.35 second sentence), "need to" (1.46, 2.8), "it is expected" (1.48, 3.1, 3.6), "there is an expectation" (3.4). Recorded as must where the meaning is plain: "required" (2.17, 2.18, 4.12), "core requirement" (2.4).',
    'Not recorded as statements (descriptive, legal fact or plain-present provider norms, template open point 5): 1.4 ("illegal" to use the title unless registered; legal fact), 1.9 ("graduates possess"), 1.15 ("course providers are committed"; "will be useful to include"), 1.19 ("course providers make explicit and embed"), 1.22 (statute places a duty), 1.23 ("legal obligation", "responsibility"), 1.25 and 1.38 (lists of what courses do), 1.27 ("courses develop graduates"), 1.44 ("required professional knowledge", an aim), 2.30, 2.38 ("will form part" of review), 2.40 (external examiners "will be asked"), 4.4 and 4.6 (predictions with "will").',
    'Codes: HECoS 100503 social work and CAH15-04-01 social work, both stated by the subject name. Related codes not added: probation/after-care 100662 (probation officers named as a role in 2.18, not a subject), youth and community work 100466, community work 100655.',
    'Frameworks: the CQFW is not named; Wales is placed at FHEQ Level 6 (2.28). 3.1 refers to "the relevant national qualifications frameworks" without naming one; not counted in SB6. FHEQ and SCQF/FQHEIS levels match the ingested frameworks (std:doc:qaa-fheq-2024-framework S5; std:doc:qaa-fqheis-2024-framework S5); the SCQF Level 9 ordinary degree and Scottish MA (2.29) are cited but not covered by the standards.',
    'Annex D: 4.7 cites Annex D for honours and also, as worded, "postgraduate awards at Level 6 (SCQF Level 10 in Scotland)"; recorded as cited. The master\'s classes (merit, distinction) are left to providers\' schemes (4.8).',
    'Bodies: BASW and the regulators\' documents appear only in section 5 (excluded) and are not counted in SB6 bodies; BASW\'s Shades of Bias is named in 1.21 as an example tool (not a body citation). The 2016 group listed the HCPC and the Care Council for Wales (section 6, excluded).',
    'Theme naming: the statement names five cross-cutting themes in its front matter and section 1 headings, the fifth being generative AI (theme:generative-ai, convention). Its EDI theme is named EEDI, with equity added.',
    'Integrated master\'s headline 4.14.inquiry and master\'s 4.17.inquiry sit under the knowledge and understanding heading in the issuer\'s layout but are recorded with domain subject-skill (an inquiry project); for P3.',
    'S9 commentary not researched in P1.']
