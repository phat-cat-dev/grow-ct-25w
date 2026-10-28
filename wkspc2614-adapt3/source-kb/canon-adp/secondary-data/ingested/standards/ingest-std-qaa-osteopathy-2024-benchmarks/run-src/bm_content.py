# bm_content.py: judgement for run 0123, QAA Subject Benchmark Statement: Osteopathy (April 2024). std, 3 October 2026.
# Built by tools/bm_build.py (brief BM-BRIEF.md 0.2.3; benchmark template 0.6.0-draft; run layer 0.7.0-draft).
# Keys are S4 ids under qaa/osteopathy-2024/. The 3.6 list is flattened in the held text: its items are cut here by `find`
# in the issuer's numbering, 3.6.<letter>.<roman>. Paragraph statements take `find` to drop trailing page numbers and the
# flattened sub-headings that follow them.

HON = "bachelor's with honours"
IM = "integrated master's"
CITE = 'QAA, 2024, Osteopathy Subject Benchmark Statement, para '
SID = 'qaa/osteopathy-2024/'

META = dict(
    run='0123', p1='2026-10-03 18:11',
    title='Subject Benchmark Statement Osteopathy',
    heading='Subject Benchmark Statement: Osteopathy (QAA, April 2024)',
    edition='April 2024 (fifth edition)', published='2024-04',
    status='current',
    supersedes='the previous Osteopathy statement (not named in the text; the text dates the third edition 2019, the second 2014 and the original 2007: Part E)',
    subjects=[dict(scheme='hecos', code='100243', label='osteopathy', basis='stated'),
              dict(scheme='cah', code='CAH02-06-06', label='complementary and alternative medicine', basis='inferred'),
              dict(scheme='cah', code='CAH02-06', label='allied health', basis='inferred'),
              dict(scheme='cah', code='CAH02', label='subjects allied to medicine', basis='inferred')],
    awards=[HON, IM], levels=['fheq:6', 'fheq:7', 'fqheis:11'],
    nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
    series='QAA Subject Benchmark Statements, revision with cross-cutting themes (fifth edition of this statement, April 2024)',
    partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in passing',
    agentDefinition=("QAA's UK reference point for what a graduate of a pre-registration osteopathy course should know, understand and be able to do: "
                     "a short profile of the graduate (3.4), 83 detailed outcomes in fourteen lettered groups (3.6) and a single threshold list for the honours award (6.10), "
                     "with typical and higher achievement left to each provider and Annex D. Reach for it when designing, reviewing or describing an osteopathy course, its outcomes or its assessment. "
                     "It is not the regulator's standard: registration rests on the General Osteopathic Council's Osteopathic Practice Standards and its Recognised Qualification process, which the statement reports but does not hold."),
    summary=("Published by QAA in April 2024 as the fifth edition, the statement covers osteopathy as a primary healthcare profession regulated by the General Osteopathic Council. "
             "It sets out the context and purposes of the degree, education and training and the awarding level (bachelor's with honours at FHEQ level 6 and integrated master's at level 7; SCQF level 11 named), "
             "a broad curriculum and 83 graduate outcomes in fourteen groups, teaching and learning, assessment against the Osteopathic Practice Standards and benchmark standards stated at the threshold only (13 items), "
             "with achievement above it referred to Annex D. It carries the four cross-cutting themes (equality, diversity and inclusion; accessibility; education for sustainable development; enterprise and entrepreneurship), "
             "names the regulator, the Professional Standards Authority, the Privy Council, NCOR, NICE and CEN, and cites the FHEQ, the FQHEIS and the Quality Code."),
    authority="reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of current quality arrangements in Northern Ireland (D1, front matter: Relationship to legislation)")

S2 = dict(
    governs='what a graduate of a pre-registration osteopathy course is expected to know, understand and be able to do, and the threshold standards for the honours award',
    awards=[HON, IM, "pre-registration master's (named at 2.8)"], levels=['fheq:6', 'fheq:7', 'fqheis:11'],
    statedScope='"This document is a QAA Subject Benchmark Statement for Osteopathy that defines what can be expected of a graduate in the subject" (D1, front matter); "pre-registration osteopathic courses currently satisfy bachelor\'s ( Level 6) and integrated master\'s (Level 7) degree levels" (D1, 6.9)',
    statedSubjects=[dict(name='Osteopathy', locator='(D1, front matter; 1.1; 6.10)', kind='subject', codes=[dict(scheme='hecos', code='100243', label='osteopathy')])])

SECTIONS = {'1': 'Context and purposes of an Osteopathy degree', '2': 'Education and training', '3': 'Knowledge, understanding and skills',
            '4': 'Teaching and learning', '5': 'Assessment', '6': 'Benchmark Standards'}
SUB = [('1.1', '1.4', 'Context'), ('1.5', '1.10', 'Purposes and characteristics of an Osteopathy degree'), ('1.11', '1.12', 'Osteopathic practice'),
       ('1.13', '1.19', 'Equality, diversity and inclusion'), ('1.20', '1.22', 'Accessibility'), ('1.23', '1.25', 'Education for Sustainable Development (ESD)'),
       ('1.26', '1.39', 'Enterprise and entrepreneurship education'), ('2.7', '2.8', 'Awarding level'),
       ('3.4', '3.6', 'The key characteristics of graduates in Osteopathy'), ('6.1', '6.9', 'Introduction'), ('6.10', '6.10', 'Standards')]

G = {
    '1.1': 'osteopaths as primary healthcare practitioners; an Allied Health Profession in England',
    '1.2': 'the range of management strategies osteopaths use',
    '1.3': 'settings of practice and the scope of a first consultation; referral',
    '1.4': 'clinical training in institutional clinics; the kinds of institution that teach the subject',
    '1.5': 'regulation by the GOsC; Recognised Qualifications must deliver the OPS',
    '1.6': 'preparing students for autonomous practice from graduation',
    '1.7': 'employment patterns: self-employed, salaried, NHS and other roles',
    '1.8': 'osteopathy in independent clinical guidance, notably on back pain',
    '1.9': 'NCOR and the osteopathic evidence base',
    '1.10': 'osteopathy as a global profession; the CEN standard',
    '1.11': 'what osteopathic practice blends: knowledge, skills and principles',
    '1.12': 'seven features that characterise osteopathic practice',
    '1.13': 'a collective responsibility for equity and inclusion beyond legal minimums',
    '1.14': 'an inclusive learning community that counters systemic disadvantage',
    '1.15': 'critical interrogation of dominant thought; equity as a right',
    '1.16': 'core values to run through the whole curriculum',
    '1.17': 'critical theory across the curriculum; anticipatory design',
    '1.18': 'anticipatory design and caring for self and others',
    '1.19': 'questions to test how a course takes account of EDI',
    '1.20': 'how students first meet osteopathy; widening access',
    '1.21': 'part-time and full-time modes and parity of experience',
    '1.22': 'accessibility across all modes of teaching, learning and assessment',
    '1.23': 'whole-person training and critical study of the profession for sustainability',
    '1.24': 'the eight UNESCO sustainability competencies in the learning environment',
    '1.25': 'contextualising learning; personal and social responsibility as an aim',
    '1.26': 'growing demand for osteopathy across sectors',
    '1.27': 'graduates articulating the value of their skills; enterprising self-awareness',
    '1.28': 'what an entrepreneurial mindset involves',
    '1.29': 'EEE and its part in an ethical career',
    '1.30': 'enterprising behaviours',
    '1.31': 'enterprising attributes',
    '1.32': 'competencies for employed or self-employed practice',
    '1.33': 'digital competency used creatively and accessibly',
    '1.34': 'employability and enterprise in curriculum design',
    '1.35': 'external speakers and alumni recommended',
    '1.36': 'assignments that build business and evaluative skill',
    '1.37': 'initiatives with placement providers, employers and stakeholders',
    '1.38': 'supervised clinic practice as a bridge to an entrepreneurial mindset',
    '1.39': 'career pathways and the can-do confidence EEE builds',
    '2.1': 'a common approach to the regulator\'s capabilities',
    '2.2': 'evidence-based pedagogy; feed-forward feedback and self-assessment',
    '2.3': 'progressive levels, clinical reasoning, supervised experience and autonomy in learning',
    '2.4': 'technical skill integrated with closely supervised clinical work',
    '2.5': 'core sciences, communication and patient-centred teaching',
    '2.6': 'clinical reasoning frameworks for critical awareness',
    '2.7': 'training reflects the degree-level descriptors of the FHEQ and FQHEIS',
    '2.8': 'awarding levels and course lengths',
    '3.1': 'the broad curriculum of an osteopathy degree',
    '3.2': 'the OPS combined with the curriculum to prepare graduates',
    '3.3': 'integrating knowledge and skills for safe practice and learner autonomy',
    '3.4': 'six key characteristics of the osteopathy graduate',
    '3.5': 'competent students graduate as safe, rounded practitioners',
    '3.6': 'the detailed graduate outcomes in fourteen lettered groups',
    '4.1': 'teaching and learning towards GO-SET and the OPS themes',
    '4.2': 'progressive, critical and reflective learning; skills students gain',
    '4.3': 'evolving, innovative and research-informed teaching',
    '4.4': 'supervised clinical learning across diverse patient groups',
    '5.1': 'assessment towards meeting the OPS; the condition to graduate',
    '5.2': 'authentic assessment shaped by practitioners and patients',
    '5.3': 'varied, valid and reliable assessment tools',
    '5.4': 'assessment that tracks growing complexity towards autonomy',
    '6.1': 'the standards are the minimum threshold for the honours award',
    '6.2': 'most students exceed the threshold; Annex D for higher achievement',
    '6.3': 'osteopathy\'s holistic, person-centred approach',
    '6.4': 'pre-registration courses with supervised clinical practice and the OPS themes',
    '6.5': 'the scientific and clinical foundation of training',
    '6.6': 'evidence-informed practice and research skills',
    '6.7': 'reflective practice and CPD after graduation',
    '6.8': 'Recognised Qualification approval and the OPS',
    '6.9': 'the capabilities map to framework levels 6 and 7 and SCQF 11',
    '6.10': 'the thirteen threshold standards for the honours award',
}
CTYPE = {'3.1': 'area', '6.5': 'area', '2.2': 'practice', '2.4': 'practice', '4.3': 'practice', '4.4': 'practice',
         '1.36': 'practice', '1.38': 'practice'}
EXCLUDED = [
    dict(number='none', heading='About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points', kind='other: front matter, read for S1, S2 and SB6'),
    dict(number='section headings', heading='the six numbered section heading lines', kind='other: headings, recorded in SECTIONS'),
    dict(number='7', heading='List of references and further resources', kind='other: back matter, references'),
    dict(number='8', heading='Membership of the Advisory Group', kind='other: back matter, membership; read for S8'),
]

# ---- exact texts for the cut items (from the held text; 3.6 is flattened)
FIND36 = {
  '3.6.a.i': 'A detailed and integrated knowledge of human structure and function, with emphasis on the neuro-musculoskeletal system, sufficient to recognise, identify and critically differentiate between normal diversity and abnormal anatomical structures and processes in the living body.',
  '3.6.a.ii': 'Contemporary scientific and medical knowledge of human disease sufficient to inform clinical judgement regarding clinical examination and palpatory findings, and to recognise disorders that require referral for more investigation or additional professional support.',
  '3.6.a.iii': 'Knowledge of human psychology and sociology, relevant to the acquisition and maintenance of health, and appreciation of individual needs, values and beliefs, sufficient to provide a context for clinical decision-making and patient management.',
  '3.6.a.iv': 'Knowledge of pain neurophysiology and psychosocial influences and the impact these have on the patient and their clinical presentation.',
  '3.6.a.v': 'Understand the role of touch within treatment and how this can influence patients’ responses to the application of osteopathic techniques.',
  '3.6.a.vi': 'Recognise that the presenting problem may mask underlying health concerns that involve physical and behavioural aspects.',
  '3.6.a.vii': 'Knowledge to select, effectively apply and monitor an appropriate range of osteopathic techniques and management approaches specific to the needs of the patient, acknowledging any relative and absolute contraindications.',
  '3.6.a.viii': 'Knowledge and understanding of concepts relating to research methodologies, demonstrating the ability to critically appraise and evaluate the quality of quantitative and qualitative clinical research sufficient to inform clinical decision-making and patient management.',
  '3.6.b.i': 'A critical understanding of principles and concepts of osteopathy and how these may inform rational clinical decision-making activities.',
  '3.6.b.ii': 'An understanding of models of health, disease and illness and how these inform a critical consideration of practical patient care and management.',
  '3.6.b.iii': 'A critical awareness and adaptation of principles, perspectives and practice of other relevant healthcare professions.',
  '3.6.b.iv': 'An understanding of how osteopathic principles are applied through different osteopathic treatment and management approaches and how to select or modify techniques to meet the needs and preferences of an individual patient.',
  '3.6.c.i': 'Understand different models relating to therapeutic relationships.',
  '3.6.c.ii': 'Demonstrate the elements and boundaries of a therapeutic relationship with the appropriate skills to form an appropriate partnership with the patient.',
  '3.6.c.iii': 'Show self-awareness to identify potential boundary issues, and to manage these effectively, ensuring ongoing standards of care for the patient.',
  '3.6.c.iv': 'Deal with unfamiliar situations or uncertainty effectively and efficiently, applying duty of candour and the self-awareness to manage the case with integrity.',
  '3.6.c.v': 'Justify acceptable management strategies to cope with ethical issues likely to confront a practitioner.',
  '3.6.c.vi': 'Maintain patient confidentiality and act only with the informed consent of the patient or other individual able to consent on the patient’s behalf, except in cases where safeguarding concerns would override this.',
  '3.6.c.vii': 'Adopt appropriate strategies for physical and psychological self-care during interactions with patients to maintain a high standard of professional effectiveness.',
  '3.6.d.i': 'Understand the range and forms of human communication and their strengths and limitations with the skill to move between these different approaches with patients and colleagues, adapting appropriately to the individual they are dealing with.',
  '3.6.d.ii': 'Skilled in relating, integrating and responding to information and data acquired by verbal and non-verbal means, either face-to-face or using telehealth and online meetings.',
  '3.6.d.iii': 'Developing a comprehensive vocabulary to translate palpatory experiences to appropriate language to clearly communicate with colleagues, other professionals and patients.',
  '3.6.d.iv': 'Speak with a critical reasoned perspective about osteopathy, its relative limitations, strengths and potential, appraising research, opinion and anecdote to make sense of therapeutic claims to further inform patients.',
  '3.6.d.v': 'Skilled in digital literacy consistent with the efficient management of a modern osteopathic practice, including:\n- the ability to interact with other healthcare professionals\n- the production of written reports and presentations of high quality for referral and related purposes\n- the ability to use information technology for research and clinic-related purposes\n- the ability to manage and present financial and other data needed for compliance with legal requirements\n- the ability to analyse quantitative and qualitative data for audit and related purposes.',
  '3.6.e.i': "Demonstrate effective and efficient completion of a detailed case history of the patient and an analysis of the patient's presenting complaint.",
  '3.6.e.ii': "Recognise the relative importance of the psychosocial context of the patient's presenting complaint and the role of shared decision making in treatment planning.",
  '3.6.e.iii': 'Identify the needs of the patient and facilitate specific clinical investigations or other referrals as required.',
  '3.6.e.iv': 'Conduct a thorough and ongoing evaluation of the patient, which may include a biomechanical, psychosocial, attitudinal, palpatory and clinical examination, as appropriate and sensitive to the individual’s presentation.',
  '3.6.e.v': "Generate several hypotheses to explain the patient's presenting complaint, to aid the formulation of a treatment plan or onward referral, including an accessible explanation of the working diagnosis.",
  '3.6.e.vi': "Recognise the characteristics and consequences of non-verbal communication and issues around protected characteristics and socioeconomic status as they may impact on the patient's health.",
  '3.6.e.vii': 'Generate complete and accurate records of the outcomes of the patient evaluation.',
  '3.6.f.i': 'A critical appraisal of the therapeutic value of touch and palpatory influence within diagnosis and treatment.',
  '3.6.f.ii': 'Awareness of the need for ongoing communication with the patient around the use of touch and palpation for confirmation of findings and to ensure patient consent and comfort.',
  '3.6.f.iii': 'The relevant use of criticality to recognise and understand the structure and function of the tissues during palpation as part of the evaluation process.',
  '3.6.f.iv': 'The use of palpation both as a complementary diagnostic, and therapeutic technique to provide reassurance to patients.',
  '3.6.f.v': 'Demonstrate a sensitivity in using palpatory skill, with an awareness of its limitations and recognise ongoing opportunities for enhancing development of these practical skills.',
  '3.6.f.vi': 'Make accurate, consistent and appropriate records of palpatory findings in parallel with objective measures and patient reported outcomes.',
  '3.6.f.vii': 'Use palpation in conjunction with other evaluation methods to inform a working diagnostic hypothesis and ongoing treatment plan.',
  '3.6.g.i': 'Perform a detailed analysis and reflection on information gathered during patient history taking and evaluation.',
  '3.6.g.ii': "Generate and justify a set of hypotheses for the aetiology of the patient's presenting complaint.",
  '3.6.g.iii': 'Establish how to inform the patient or person with parental responsibility or guardianship of findings and discuss potential courses of action.',
  '3.6.g.iv': 'Consider appropriate courses of action based on a rational and shared decision- making process which includes a critical consideration of personal limits of competence and the likely effects of osteopathic treatment.',
  '3.6.g.v': 'With the consent of the patient, or person who can consent on their behalf, make referrals to other healthcare professionals for further investigations if required.',
  '3.6.g.vi': 'Formulate a treatment plan and prognosis that includes monitoring the effect of treatment during and after its application over the course of planned interventions.',
  '3.6.g.vii': 'Identify and reflect on the obstacles to progress and to plan and take appropriate action.',
  '3.6.h.i': 'Demonstrate an awareness of, and ability to select from, the wide range of indirect and direct osteopathic technical approaches as appropriate to the patient and informed by available best evidence.',
  '3.6.h.ii': 'Demonstrate awareness and application of a range of patient management approaches developed in conjunction with the patient, considering individual preferences and needs.',
  '3.6.h.iii': 'Rationalise indications and contraindications of using specific osteopathic techniques or their modification.',
  '3.6.h.iv': 'Adapt osteopathic approaches and justify or amend its mode of use further in relation to the feedback received as a patient-centred intervention.',
  '3.6.i.i': 'Monitor spontaneous changes to recognise and record adverse reactions to osteopathic treatment, and initiate appropriate responses, including referral when appropriate.',
  '3.6.i.ii': 'Maintain an open-minded and inquiring approach to treatment outcomes.',
  '3.6.i.iii': 'Record evaluation findings and their interpretation accurately, legibly and accessibly in the case notes of an individual patient.',
  '3.6.i.iv': 'Gather and organise a comprehensive range of qualitative and quantitative data, outcome measures and evidence relevant to the response of an individual patient to an osteopathic intervention.',
  '3.6.j.i': 'Operate with a critical appreciation of the key concepts and organisation of health education and health promotion in the UK and overseas.',
  '3.6.j.ii': 'An understanding of the significance and potential effect of psychosocial, cultural, and socioeconomic factors in helping patients to make informed choices about their personal healthcare maintenance.',
  '3.6.j.iii': 'Work in partnership with the patient to identify self-care activities, that may include dietary advice, exercise and lifestyle adjustments.',
  '3.6.j.iv': 'Offer realistic advice concerning the location and effective use of local healthcare promoting activities consistent with community, cultural and ethnic values.',
  '3.6.j.v': 'Care for their own health and well-being and follow due diligence with the appropriate procedures to manage communicable diseases.',
  '3.6.j.vi': 'Identify potential benefits and limitations of referring an individual patient to other healthcare practitioners or processes.',
  '3.6.k.i': 'Be committed to lifelong learning through reflective and active approaches to skills and knowledge acquisition.',
  '3.6.k.ii': 'Be critically aware of the level of practical skills and clinical knowledge required to deliver the expected standards of care.',
  '3.6.k.iii': 'Be able to reflect on personal and professional strengths and limitations to plan and enact ongoing self-directed professional development and learning.',
  '3.6.k.iv': 'Be able to record reflective activities around clinical practice, evidenced through a professional portfolio, sufficient to demonstrate continuing professional development for the professional statutory body.',
  '3.6.k.v': 'Evidence of critical problem-solving skills to a level that informs and guides the interpretation of clinical and other data and contributes to effective clinical reasoning and decision-making.',
  '3.6.k.vi': 'Evidence of engagement in peer-review, facilitating respectful feedback and discussion with colleagues that enables collaboration in group activities relevant to the development of the individual and the profession.',
  '3.6.k.vii': 'Self-care and self-awareness sufficient to consistently maintain an acceptable standard of care for a patient.',
  '3.6.k.viii': 'The attitudes and skills necessary to comply fully with continuing fitness to practise standard requirements to maintain registered status.',
  '3.6.k.ix': 'The ability to contribute to and/or understand research and other scholarly activities to support personal and professional development.',
  '3.6.l.i': 'Understand the concept and significance of statutory regulation authorised by Parliament.',
  '3.6.l.ii': 'Abide by the professional standards outlined in the OPS and other guidance issued by the General Osteopathic Council and other appropriate bodies.',
  '3.6.l.iii': 'Practise osteopathy safely, competently, and effectively in accordance with the law. This includes, for example, compliance with consent, safeguarding, equality, diversity and inclusivity, data protection and health and safety legislation.',
  '3.6.l.iv': "Act quickly to prevent harm. Appropriate action may include managing the situation by oneself, discussing with a colleague, or reporting to another appropriate authority or body. Acting in all circumstances where patient safety may be at risk will include, for example:\n- disclosing and apologising to patients and discussing and agreeing how to make things better\n- being aware of and complying with the legislative framework and principles in relation to safeguarding vulnerable adults and children\n- acting in circumstances where colleagues' actions may be putting patients at risk of harm or financial loss\n- taking appropriate action where practitioner health may impact on the ability to practise safely\n\n17\n- reporting relevant and appropriate information about conduct or competence to the regulator.",
  '3.6.l.v': 'Respect and uphold patient dignity, autonomy and confidentiality.',
  '3.6.l.vi': 'Disclose and justify actions to others when appropriate.',
  '3.6.l.vii': 'Take responsibility for maintaining professional boundaries and uphold high standards of personal and professional conduct, and the integrity of the profession.',
  '3.6.m.i': 'A critical understanding of the delivery of healthcare provision in the UK and overseas and the contribution of osteopathy within the context of one of the Allied Health Professions in NHS England and as primary healthcare practitioners.',
  '3.6.m.ii': 'A critical understanding of the specific claims of a range of conventional and non- conventional healthcare professions and how these relate to the practice of osteopathy.',
  '3.6.m.iii': 'Demonstrate a critical evaluation of the current claims of osteopathic practice in the UK and overseas.',
  '3.6.n.i': 'Understand financial and practice management operational details in accordance with legal and ethical requirements, including health and safety standards, and employment legislation and any other relevant guidance or applicable laws.',
  '3.6.n.ii': 'Understand the role of audit in monitoring the quality of practice and the ability to contribute to the generation of operational and strategic plans.',
  '3.6.n.iii': 'Maintain patient records and information in compliance with legal and ethical requirements of confidentiality and peer support.',
  '3.6.n.iv': 'Generate effective and high standards of contact with external agencies, including referrals to other healthcare professionals within and outside of the NHS, insurance companies and public service organisations.',
  '3.6.n.v': 'Demonstrate knowledge of business skills necessary to establish a viable osteopathic business that prioritises patients over profit.',
}
FINDP = {
  '1.5': "1.5 Osteopathic students follow an extended degree course, combining academic and hands-on clinical work. The General Osteopathic Council (GOsC) regulates the practice of osteopathy in the UK. By law (the Osteopaths Act 1993), only those registered with the GOsC are entitled to call themselves osteopaths and practise osteopathy in the UK. A student wishing to study in the UK to become an osteopath must gain a qualification recognised by the GOsC and approved by the Privy Council. All Recognised Qualifications (RQs) must deliver the GOsC's Osteopathic Practice Standards (OPS) . RQs should also align with the GOsC's guidance, including the Graduate Outcomes and Standards for Education and Training which sets out the outcomes that will help graduates to demonstrate that they meet the OPS. The Professional Standards Authority oversees the GOsC as well as nine other health professional regulatory bodies.",
  '1.6': '1.6 Once qualified and registered with GOsC, osteopaths can practise independently. Thus, it is critical that throughout pre-registration education osteopaths are prepared for autonomous practice at the point of graduation. This requires them to develop both the skills\n\n4\nand criticality to integrate into the osteopathic and wider health community to provide effective patient care, and the reflexivity, insight and ability to keep themselves up to date with evidence (including clinical guidelines) and fit to practise.',
  '1.13': "1.13 Osteopathy, as an inclusive learning community, has a collective responsibility to embed equity, equality, diversity and inclusion within all institutions, processes, curricula, and pedagogies. This responsibility to go beyond the minimum expectations of equality ensures an equitable community that recognises learners’ difference in prior experience and opportunity and can help to remedy systemic disadvantages in the subject, for example: through widening participation agendas to ensure economic disadvantage does not hinder a student's access, experience or outcome; countering the underrepresentation of marginalised groups inclusive of, and beyond, those with protected characteristics as defined by the Equality Act 2010 ; adopting a zero-tolerance approach to discrimination and harassment, including everyday microaggressions; ensuring access for neurodiverse community members; and closing structural awarding gaps. All participants in the community will need to engage, reflect and change to uphold this responsibility and duty, which will impact education, student participation, population health, and patient care perspectives.",
  '1.14': '1.14 All involved in osteopathy should foster an inclusive learning community encompassing a range of participants, such as students, academics, professional staff, patients, visitors and external partners to counter systemic disadvantage. Equity , diversity and inclusion require a strong commitment and concerted action to build an inclusive environment where opportunities are open to all and where everybody can reach their full potential without fear of harassment, prejudice or discrimination. Contemporary legacies of systemic disadvantage, for example, racism, classism, ablism, homophobia and patriarchy, must therefore be acknowledged and countered by fostering an inclusive learning community encompassing a range of participants, such as students, academics, professional staff, patients, visitors and external partners. This could include, for example, the provision of diverse osteopathic educational methods to address the challenges of EDI and access.',
  '1.15': '1.15 Osteopathic undergraduate and postgraduate studies should continually critically interrogate the language, perceptions, and entrenchment of dominant systems of thought, within concepts of knowledge and power. Recognition and commitment to agency, equal rights and inherent dignity of all humans form the foundation of social justice. Equity is positioned as an ethical consideration of each person’s multiple identities and experiences and a fundamental human right in relation to supporting and advocating for anti-oppressive knowledge generation and practice.',
  '1.16': '1.16 The following core values underpin osteopathy’s inclusive learning community: an ethics of care towards patients, students, educational faculty and members of the public embracing and valuing plurality of knowledges and experiences; respect for a range of perspectives and lifestyles; attentiveness to the opportunities and challenges raised by decolonial imperatives; and solidarity in recognising and addressing injustice. These values should be integrated throughout the curriculum and not be siloed within individual modules and/or sub-disciplines. This will enhance the contribution that studying osteopathy can make to realising transformative justice across education and healthcare, and supporting osteopathic students to engage with health inequalities, social determinants, and varied patient populations (Office for Health Improvement and Disparities 2022; Bambra et al. 2023; NIHR 2021; Versus Arthtritis 2019; Rashbrook 2019).',
  '1.17': '1.17 The core values underpinning osteopathy’s inclusive learning community aligns with, and encourages, curricula design principles that stimulate critical thinking informed by a variety of progressive theoretical perspectives and educational research. These include, but are not limited to, theoretical perspectives from critical theory, critical race theory, decoloniality, disability studies, feminist, queer, and science and technology studies. The application of critical theory is relevant to, and should be applied across, the osteopathic discipline and curricula content. The core values also promote anticipatory design and practices, which are considerate of the particularities associated with sites of learning, for example, online, face-to-face, in technique class, in the clinic, paying close attention to those that may have historically been less inclusive.',
  '1.18': '1.18 Effective anticipatory design and practice in osteopathy acknowledges the importance of providing a supportive cultural and institutional context for teaching, learning and research, within which participants are encouraged to embrace intellectual, methodological, and practical challenges. Effective anticipatory design and practice also enhance the individual and collective capability to work with the discomfort associated with encountering alternative perspectives, learning new knowledge, and gaining new skills. This requires osteopathy’s inclusive learning community to develop and promote techniques to care for the self and others, as part of a sustained consideration for emotional, mental and physical wellbeing.',
  '1.22': "1.22 The combined use of digital/virtual, face-to-face, synchronous, or asynchronous teaching and learning can provide opportunities for knowledge sharing and skills acquisition that are fair and accessible to all. Students' engagement with face-to-face or online learning environments and teaching activities (including assessment) will not always be equal or consistent due to several factors. For example, students may have personal commitments, such as caring responsibilities, that prevent them from attending scheduled lectures. Alternatively, they may need to make reasonable adjustments to ensure that they can access and engage with learning materials, for example if they have specific disabilities, special educational needs or limited access to digital resources or bandwidth due to geographical or economic conditions. Wherever possible, all modes of teaching, learning and assessment will be underpinned by a concern for accessibility, which can be achieved in a variety of ways. These include captioning of recorded lectures, recording of synchronous content, accessible design of virtual learning environments; it is for subject specialists to determine the most appropriate means of promoting fair and equitable access to learning and removing barriers to success. Supportive measures have to be enacted without compromising the regulatory framework that supports patient safety and well- being.",
  '1.24': '1.24 All eight of the UNESCO sustainability competencies (systems thinking; anticipatory; normative; strategic; collaboration; critical thinking; self-awareness; integrated problem- solving) are considered essential for the sustainability of osteopathy. The qualified osteopath within their professional and working context requires the practical operation of all the competencies in the delivery of their professional services. The learning environment for osteopathy therefore requires these competencies to be manifested and exemplified within the learning facilities and course curricula.',
  '1.25': '1.25 To develop learning environments that promote sustainable development, undergraduate osteopathic training aims to contextualise theoretical learning and professional provision at a practice level within the social, economic and political arena, and promote the employability of their graduates. Engendering personal and social responsibility for the well-being of others and themselves should be a developmental aim. More\n\n8\ninformation on education for sustainable development can be found in the QAA and Advance HE guidance.',
  '1.27': '1.27 Osteopathy graduates can collect, analyse and manipulate a range of quantitative and qualitative data and should understand the commercial as well as practical value of their skillsets and be able to articulate and demonstrate them to potential employers and in plans for self-employment, private practice or further study. They should also be encouraged to develop self-awareness of their own enterprising and entrepreneurial capabilities in osteopathy, as well as the motivation and self-discipline to apply these flexibly in different ways and in changing contexts. This might include recognising themselves as being creative or resourceful; translating ideas into actions; prepared to challenge assumptions through critical investigation and research.',
  '1.33': '1.33 Developing digital competency and transferable skills should include using digital technology to communicate ideas creatively, innovatively and accessibly to enhance academic success and employability.',
  '1.34': '1.34 The development of such professional knowledge, skills and competencies in osteopathy should be a key aspect of curriculum design and might be achieved across the duration of a training programme. Learning outcomes, teaching, and learning activities and authentic assessment for employability, enterprise and entrepreneurship may be explicit within dedicated modules and embedded across modules.',
  '1.35': '1.35 The engagement of external speakers or representation from the profession and alumni to enrich teaching and offer first-hand experience is recommended. Exposure to a variety of osteopaths will develop awareness of the working context and could enhance the competencies of graduates to deal with market forces and promote themselves ethically as an osteopath upon graduation.',
  '2.3': '2.3 This approach combines academic and theoretical learning framed around progressive levels aligned to the UK Quality Code for Higher Education (Quality Code ), including procedural, propositional and psychomotor knowledge centred in an osteopathic clinical framework. The applied practical and clinical reasoning skills should robustly support osteopathic clinical decision-making and safe, effective practice ensuring continuing student fitness to practise. Furthermore, supervised clinical experience is essential to the development of osteopathic skills. Autonomy in learning is also required to enable and ensure lifelong learning and reflective practice. Knowledge of the healthcare environment in the UK, business and regulatory requirements are sufficient to enable graduates to work independently.',
  '2.5': '2.5 As befits a primary healthcare profession, it is important that osteopathic students graduate with comprehensive knowledge and demonstrate understanding of anatomy, physiology and pathology, as well as acquiring excellent communication and interpersonal skills to liaise with both patients and other health professionals. Osteopathic teaching and learning should emphasise patient-centred care, including a comprehensive understanding of psychosocial factors, to support and guide the patient journey.',
  '3.5': '3.5 Competent students will develop core knowledge, understanding and skills and will have capability to apply these to patient evaluation and management, graduating as safe and rounded practitioners. The following outcomes describe the more detailed clinical, academic and practical expectations of the osteopathic graduate. They are designed to demonstrate the professional capabilities that are needed to become registered as an osteopath in the UK as set out in the OPS and accompanying Graduate Outcomes and\n\n12\nStandards for Education and Training provided by GOsC.',
  '4.2': '4.2 Knowledge, skills and experience are progressively accumulated throughout the duration of the course. The teaching and learning experience will be a critical and reflective approach to osteopathy with consideration of osteopathic concepts and principles and personalised care for patients. Students will be equipped with reflective, leadership, peer review and lifelong learning skills. The integration of theoretical and practical knowledge and skills prepares students to work autonomously as an osteopath in professional practice. Teaching and learning methods reflect the diverse learning styles of students, delivered in a sustainable and inclusive way.',
  '5.1': '5.1 Assessment strategies should support students in their development as practitioners and ultimately should enable students to demonstrate that they have met the OPS. Only students who meet these standards are permitted to graduate.',
  '5.2': '5.2 Assessment strategies should reflect the range and depth of competence required to meet the OPS and relate to real-life situations and practice where possible, to better prepare students for postgraduation and lifelong learning. Experienced and qualified educators and practitioners should play a central role in developing assessment strategies, which should also be supported by the patient voice.',
  '5.3': '5.3 A diverse range of assessment tools should be utilised, to support students in their learning and development, and to support a range of learning styles and differences. These should be valid and reliable, providing a transparent and supportive pathway for student progression and achievement. Central to assessment strategies should be the use of formative and summative assessments, and the involvement of peers, patients, educators and external expertise where appropriate.',
  '5.4': '5.4 Assessment of students should reflect the increasing complexity of their studies and responsibilities, and the requirements of meeting the OPS. This should support students as they move from novice to competent practitioner, where they will need to be able to manage clinical uncertainty and demonstrate the qualities and competence of an autonomous healthcare practitioner, capable of working in a range of environments.',
  '6.2': '6.2 Most students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies.',
  '6.6': '6.6 Students develop skills to critically engage with the three components of evidence- informed practice (clinical experience, research, and patient expectations). They are expected to be able to evaluate the clinical relevance of published research both within and outside of the profession, conduct audits, service evaluation and research for improving the quality of osteopathic practice and patient care, as well as for current professional issues. Osteopaths are expected to support and develop an effective evidenced-informed approach for patient care regardless of practice setting.',
  '6.8': '6.8 Osteopathic education courses are approved by the professional regulator, the General Osteopathic Council, through gaining Recognised Qualification (RQ) status which is reviewed regularly. This requires observing the General Osteopathic Council’s Graduate Outcomes and Standards for Education and Training (September 2022) as well as demonstrating the effective delivery of the OPS which graduating students and registered osteopaths are required to meet throughout their careers.',
  '6.10.b7': 'an appreciation of the value of osteopaths’ abilities to support patients’ well-being throughout their lifespan and through changing public health considerations. This also includes the value of osteopathic care even when the patient may have a lifelong\n\n22\nillness or disability but can benefit from advice and treatment which supports palliation or well-being',
}

P = {}
def s(i, **k):
    if i in FINDP:
        k['find'] = FINDP[i]
    P[i] = k
NA_PROV = ('n/a', 'a duty on the course or provider; the student meets its effect, not a standard to reach')

# ---- obliging or outcome paragraphs (sections 1, 2, 4, 5 and 6)
s('1.5', type='requirement', rung='none', force='must', level='none', appliesTo='anyone seeking to practise as an osteopath in the UK',
  addressee='learner', verbs=['regulates', 'gain', 'deliver', 'align'], about='registration, Recognised Qualifications and the OPS', domain='none', award='none',
  para="Osteopathy courses are extended and mix academic with hands-on clinical work; the General Osteopathic Council regulates the profession and by law only its registrants may use the title or practise; anyone who trains here as an osteopath must gain a qualification the regulator recognises and the Privy Council approves; every Recognised Qualification must deliver the Osteopathic Practice Standards and should align with the regulator's guidance on graduate outcomes; the Professional Standards Authority oversees the regulator.",
  prac="Courses that lead to registration must hold Recognised Qualification status from the GOsC with Privy Council approval, must deliver the Osteopathic Practice Standards and should align with the regulator's guidance, including its graduate outcomes and education standards.",
  ben="If you want to practise as an osteopath in the UK, you must gain a qualification recognised by the professional regulator, because by law only registered osteopaths may use the title or practise.",
  aaw="Treat this as a legal and regulatory requirement the statement reports, not as a graduate outcome: entry to the register depends on a Recognised Qualification approved by the regulator and the Privy Council, and such a qualification must deliver the regulator's practice standards. It applies to the qualification whatever its level (bachelor's at FHEQ 6, integrated master's at FHEQ 7). Cite it as " + CITE + "1.5, and cite the regulator's own documents for the detail. Set it beside " + SID + "6.8 and 2.1, and do not claim the statement itself sets or confers registration.",
  aad="Raise it when a prospective or current student asks whether the course leads to practice as an osteopath. Tell a student plainly that you must hold a recognised qualification and register with the regulator before you can use the title; with a programme team, frame it as the condition the course's recognition rests on. Ask whether the person knows if their course holds Recognised Qualification status and what registration involves. Avoid reciting the legislation at length or suggesting the statement itself grants the right to practise.")
s('1.6', type='requirement', rung='none', force='must', level='fheq:6', appliesTo='students on pre-registration courses',
  addressee='learner', verbs=['prepared', 'requires', 'develop'], about='readiness for autonomous practice at graduation', domain='generic-skill', award=[HON, IM],
  para="Once qualified and registered, osteopaths may practise on their own, so pre-registration education must ready them for autonomous practice by graduation; this requires them to develop the skills and criticality to join the osteopathic and wider health community and care well for patients, and the reflexivity and insight to keep abreast of evidence and stay fit to practise.",
  prac="Because registered osteopaths may practise independently, the course must prepare students for autonomous practice by graduation: the skills and criticality to work within the osteopathic and wider health community, and the reflexivity to keep abreast of evidence and remain fit to practise.",
  ben="Because you may work on your own as soon as you register, your course must prepare you for independent practice by the time you graduate: you will need the skills and critical thinking to work with other health professionals, and the habit of keeping up with evidence and staying fit to practise.",
  aaw="Treat this as a requirement the statement places on pre-registration education: graduates must be ready for autonomous practice at the point of graduation, at FHEQ level 6 for the honours award and level 7 for integrated master's. The issuer's words are 'it is critical' and 'requires', recorded here as must (Part E). Cite it as " + CITE + "1.6. Set it beside the threshold standards " + SID + "6.10.b9, 6.10.b10 and 6.10.b13 and the level 6 descriptor qaa/fheq-2024/4.15.b9.2, and do not claim it adds a registration condition of its own.",
  aad="Raise it when a student or team asks why the course stresses independence, reflection and keeping up with evidence. Tell a student plainly that you could be practising alone soon after you graduate, so the course aims to make you ready for that; with staff, frame it as the design goal behind clinic autonomy and reflective tasks. Ask how ready the person feels to make decisions without a tutor in the room, and how they keep up with new evidence. Avoid presenting it as a separate test or quoting the paragraph at length.")
s('1.12.b1', type='expectation', rung='none', force='should', level='none', appliesTo='osteopathic practice and its teaching',
  addressee='both', verbs=['inform', 'involves', 'viewing'], about='care centred on the person, not the condition', domain='understanding', award='none',
  para="Focusing on the person rather than the condition is a long-held principle of osteopathy and should shape the osteopathic approach to care; it means seeing the person as a combined mix of influences that together affect health.",
  prac="Teach and model care that centres on the person rather than the condition: this long-held tenet should shape the approach to care, treating health as the product of many interacting influences.",
  ben="You should centre your care on the person, not just their condition, seeing their health as the result of many influences working together.",
  aaw="Treat this as an expectation (should) about the osteopathic approach to care, given as the first of the features of practice listed in 1.12; it holds for practice and teaching at every level and sets no award outcome. Cite it as " + CITE + "1.12, first bullet. Set it beside the person-centred outcomes " + SID + "3.4.b2, 3.6.h.ii and 6.10.b4, and do not present it as a measurable threshold or as the regulator's standard.",
  aad="Raise it when a student's case discussion narrows to the tissue or the diagnosis and loses the person. Put it to a student as advice on how you should approach every patient; to staff, as a principle to model in clinic teaching. Ask what else in the patient's life might be shaping their health, and how that changed the plan. Avoid lecturing on osteopathic philosophy or quoting the passage at length.")
s('1.13', type='expectation', rung='none', force='will', level='none', appliesTo='everyone in the osteopathic learning community',
  addressee='both', verbs=['embed', 'engage', 'reflect', 'change', 'uphold'], about='shared responsibility for equity and inclusion', domain='none', award='none',
  para="The osteopathic learning community holds a shared responsibility, going past the legal minimum, to build equity, equality, diversity and inclusion into institutions, processes, curricula and teaching, for example by widening participation, countering under-representation, refusing all discrimination and harassment, securing access for neurodiverse members and closing awarding gaps; everyone in it will need to engage, reflect and change to meet this duty.",
  prac="Embed equity, equality, diversity and inclusion across institutions, processes, curricula and pedagogy as a collective responsibility that goes past legal minimums: widen participation, counter under-representation, tolerate no discrimination or microaggression, secure access for neurodiverse members and close awarding gaps; all participants will need to engage, reflect and change.",
  ben="You, like everyone in the osteopathic community, will be expected to engage, reflect and be open to change so that learning is fair and inclusive for all.",
  aaw="Treat this as an expectation (will) on everyone in the osteopathic learning community, staff and students alike, under the equality, diversity and inclusion theme; it is not a level outcome and holds across the course. Cite it as " + CITE + "1.13. Say that the issuer frames it as a collective responsibility and duty, not as a legal requirement beyond the Equality Act it names. Set it beside " + SID + "1.14 to 1.18 and the threshold standard 6.10.b4 on equality and diversity needs in treatment planning.",
  aad="Raise it when equity, access, awarding gaps or discrimination come up in course review or student discussion. With a student, say in plain words that you are part of a community expected to reflect and change to make learning fair; with staff, frame it as a shared duty that reaches past legal minimums. Ask what one change the person or team could make, and what the data on progression and attainment show. Avoid treating it as a student's sole burden or reading the paragraph aloud.")
s('1.14', type='requirement', rung='none', force='must', level='none', appliesTo='everyone involved in osteopathy and its learning community',
  addressee='both', verbs=['foster', 'require', 'build', 'acknowledged', 'countered'], about='an inclusive community that counters systemic disadvantage', domain='none', award='none',
  para="Everyone in osteopathy should build an inclusive learning community of students, staff, patients, visitors and partners that works against systemic disadvantage; inclusion needs strong commitment and joint action so that all can reach their potential free of harassment, prejudice or discrimination; present-day legacies such as racism, classism, ableism, homophobia and patriarchy must be acknowledged and countered, for instance through varied teaching methods.",
  prac="Foster an inclusive community of students, academics, professional staff, patients, visitors and partners; act with commitment so all can reach their potential without harassment or discrimination; acknowledge and counter the legacies of systemic disadvantage, for example with diverse teaching methods. The countering is a must; the fostering a should.",
  ben="You should help build a learning community where everyone, patients and visitors included, belongs, and where racism, ableism, homophobia and other prejudice must be named and challenged.",
  aaw="Treat this as mixed in force: the community should foster inclusion, and legacies of systemic disadvantage must be acknowledged and countered; it is recorded at must, with the should part noted in Part E. It applies to the whole learning community, not to a level or award. Cite it as " + CITE + "1.14. Set it beside " + SID + "1.13 and 1.15 to 1.18, and do not present it as a statutory duty beyond what the Equality Act cited at 1.13 imposes.",
  aad="Raise it when a team plans inclusive teaching or responds to harassment or discrimination, or when a student raises a concern. With a student, say plainly that you belong to a community that should include everyone and must challenge prejudice; with staff, frame it as an obligation on the institution and its people. Ask who is not yet included in the community and what would change that. Avoid reading lists of prejudices aloud or putting the institution's duty on an individual student.")
s('1.15', type='expectation', rung='none', force='should', level='none', appliesTo='undergraduate and postgraduate osteopathic study',
  addressee='provider', verbs=['interrogate'], about='critical interrogation of dominant thought', domain='none', award='none',
  para="Osteopathic study at every level should keep questioning critically the language, perceptions and entrenched dominant systems of thought within ideas of knowledge and power; social justice rests on agency, equal rights and human dignity, and equity is treated as an ethical matter and a basic right that supports anti-oppressive knowledge and practice.",
  prac="Build continual critical interrogation of the discipline's language, perceptions and dominant systems of thought into undergraduate and postgraduate study, framing equity as an ethical matter and a human right that supports anti-oppressive knowledge and practice.",
  ben=('n/a', 'a duty on courses in shaping the curriculum; the student meets its effect'),
  aaw="Treat this as an expectation (should) on undergraduate and postgraduate osteopathic curricula, under the equality, diversity and inclusion theme; it is a curriculum duty, not a student outcome at a set level. Cite it as " + CITE + "1.15. Set it beside " + SID + "1.16 and 1.17 on core values and critical theory, and do not present it as a learning outcome students must evidence.",
  aad="Raise it with a programme team reviewing curriculum content, reading lists or the language used about patients and bodies of knowledge. Frame it for staff as a standing invitation to question whose knowledge the course privileges. Ask which accepted ideas in the course have not been questioned recently, and whose voices are missing. Avoid presenting it to students as a requirement on them.")
s('1.16', type='expectation', rung='none', force='should', level='none', appliesTo='the osteopathy curriculum',
  addressee='provider', verbs=['underpin', 'integrated', 'siloed'], about='core values across the curriculum', domain='none', award='none',
  para="An ethics of care, valuing plural knowledges and experiences, respect for different perspectives and lifestyles, attention to decolonial imperatives and solidarity against injustice underpin the inclusive community; these values should run through the whole curriculum rather than sit in single modules, helping students engage with health inequalities and varied patient groups.",
  prac="Integrate the community's core values (an ethics of care, plural knowledges, respect, decolonial attention and solidarity) across the curriculum, not in isolated modules, so that students engage with health inequalities, social determinants and diverse patients.",
  ben=('n/a', 'a duty on course design; the student meets its effect in the curriculum'),
  aaw="Treat this as an expectation (should) on curriculum design under the equality, diversity and inclusion theme: the named core values are to run through the whole curriculum, not sit in one module; it sets no level outcome. Cite it as " + CITE + "1.16. Set it beside " + SID + "1.15, 1.17 and the outcomes that touch patient diversity, 3.6.e.vi and 6.10.b4, and do not claim the health-inequality sources it cites as part of the standard.",
  aad="Raise it when a team maps where equality, diversity and inclusion appear in the course. Frame it for staff as a test of spread: are the values present across modules or confined to one? Ask where in the clinical modules health inequalities and social determinants are discussed. Avoid giving it to students as a duty of theirs.")
s('1.17', type='expectation', rung='none', force='should', level='none', appliesTo='the osteopathy curriculum and its design',
  addressee='provider', verbs=['stimulate', 'applied', 'promote'], about='critical theory and anticipatory design', domain='none', award='none',
  para="The core values support curriculum design that encourages critical thinking drawn from progressive theories and educational research, drawing on critical and critical race theory, decolonial thought, disability, feminist and queer studies and the study of science and technology; critical theory should be applied across the discipline and its content, and the values also favour anticipatory design suited to each site of learning, with care for those that have been less inclusive.",
  prac="Apply critical theory across the discipline and curriculum (critical race theory, decoloniality, disability, feminist, queer and science and technology studies among others) and design anticipatorily for each learning site, whether online, face to face, technique class or clinic.",
  ben=('n/a', 'a duty on course design; the student meets its effect'),
  aaw="Treat this as an expectation (should) on the curriculum under the equality, diversity and inclusion theme: critical theory applied across the discipline, and anticipatory design for each site of learning. It is a design duty and sets no student level. Cite it as " + CITE + "1.17. Set it beside " + SID + "1.16 and 1.18, and name the listed perspectives as examples, not a required syllabus.",
  aad="Raise it when a team designs teaching for technique classes, clinic or online learning, or chooses theoretical perspectives for the curriculum. Frame it for staff as an expectation that critical perspectives reach clinical teaching, not only theory modules. Ask which learning sites have been least inclusive in the past and what anticipatory changes would help. Avoid presenting the perspectives as mandatory content or as a student requirement.")
s('1.18', type='requirement', rung='none', force='must', level='none', appliesTo="osteopathy's inclusive learning community",
  addressee='both', verbs=['acknowledges', 'requires', 'develop', 'promote'], about='anticipatory design and care for self and others', domain='none', award='none',
  para="Effective anticipatory design gives a supportive cultural and institutional setting for teaching, learning and research in which people are encouraged to take on challenges, and builds the capacity to work with the discomfort of new perspectives, knowledge and skills; this requires the learning community to develop and promote ways of caring for self and others, with sustained attention to emotional, mental and physical wellbeing.",
  prac="Provide a supportive cultural and institutional context that helps people stay with the discomfort of new perspectives and skills; this requires the community to develop and promote ways of caring for self and others and to attend to emotional, mental and physical wellbeing.",
  ben="You will be part of a community that is required to develop ways of caring for yourself and others, so that you can cope with the discomfort of meeting new ideas and learning new skills.",
  aaw="Treat this as a requirement (the issuer's word is requires, recorded as must) on the osteopathic learning community to develop and promote care for self and others; it is a community and design duty under the equality, diversity and inclusion theme, with no level outcome. Cite it as " + CITE + "1.18. Set it beside " + SID + "1.17 and the self-care outcomes 3.6.c.vii and 3.6.k.vii, and do not present it as a standard for a wellbeing service.",
  aad="Raise it when students or staff talk about the discomfort of challenging ideas, hands-on learning or difficult clinic encounters. With a student, say plainly that feeling unsettled when learning something new is expected and that the community should help you look after yourself and others; with staff, frame it as a design obligation. Ask what support would help the person stay with a difficult learning moment. Avoid reading it aloud or turning it into a counselling referral by default.")
s('1.22', type='expectation', rung='none', force='will', level='none', appliesTo='all modes of teaching, learning and assessment',
  addressee='provider', verbs=['underpinned', 'achieved', 'determine', 'enacted'], about='accessibility in every mode of teaching, learning and assessment', domain='none', award='none',
  para="Blended digital and face-to-face, live and recorded teaching can make learning fair and accessible, though students' engagement varies with caring duties, disabilities, special educational needs or poor digital access; wherever possible all teaching, learning and assessment will rest on a concern for accessibility, such as captions, recordings and accessible virtual environments, with subject specialists choosing the means; supportive measures have to be put in place without weakening the regulation that keeps patients safe.",
  prac="Wherever possible, underpin every mode of teaching, learning and assessment with a concern for accessibility (captioning, recording live sessions, accessible VLE design), choose the means as subject specialists and put supportive measures in place without weakening the regulation that keeps patients safe.",
  ben=('n/a', 'a duty on course delivery; the student meets its effect and arranges adjustments with the course'),
  aaw="Treat this as an expectation (will, wherever possible) that every mode of teaching, learning and assessment rests on a concern for accessibility, under the accessibility theme; it is a provider duty, not a student outcome, and holds at every level. Cite it as " + CITE + "1.22. State the limit the issuer sets: support must not compromise the regulation that protects patient safety. Set it beside " + SID + "1.20 and 1.21 and the access points of the equality theme at 1.13 and 1.14.",
  aad="Raise it when a student needs adjustments or cannot attend live sessions, or a team plans recorded, online or clinic-based delivery. With staff, frame it as a standing duty to design for access and to choose the means as subject specialists; with a student, explain only that the course should make learning accessible and how to ask for support. Ask which parts of the course are hardest to reach for students with caring duties, disabilities or poor connections. Avoid promising an adjustment that would affect patient safety in clinic.")
s('1.24', type='requirement', rung='none', force='must', level='none', appliesTo='the osteopathic learning environment',
  addressee='provider', verbs=['considered', 'requires', 'manifested', 'exemplified'], about='UNESCO sustainability competencies in the learning environment', domain='none', award='none',
  para="All eight UNESCO sustainability competencies are held essential to the sustainability of osteopathy; qualified osteopaths need to use them all in practice, so the osteopathic learning environment requires them to be shown and modelled in learning facilities and curricula.",
  prac="Make all eight UNESCO sustainability competencies visible and modelled in learning facilities and curricula: the issuer says practice needs them all and the learning environment therefore requires them.",
  ben=('n/a', 'a duty on the learning environment and curriculum; the student meets its effect'),
  aaw="Treat this as a requirement on the learning environment (the issuer's word is requires, recorded as must; Part E) under education for sustainable development: the eight UNESCO competencies are to be shown and modelled in facilities and curricula. It sets no level outcome. Cite it as " + CITE + "1.24, and the guidance named at 1.25 as std:doc:qaa-advancehe-esd-2021-guidance. Set it beside " + SID + "1.23 and 1.25, and do not claim the statement lists the competencies as assessed graduate outcomes.",
  aad="Raise it when a team maps sustainability across the curriculum or the estate. Frame it for staff as a requirement to make the eight competencies (systems thinking through to integrated problem-solving) visible in teaching and clinic. Ask which of the eight the course currently models least, and where it could. Avoid presenting the list to students as a checklist they must pass.")
s('1.25', type='expectation', rung='none', force='should', level='none', appliesTo='undergraduate osteopathic training',
  addressee='both', verbs=['contextualise', 'promote', 'engendering'], about='personal and social responsibility as a developmental aim', domain='none', award='none',
  para="To build learning environments that advance sustainable development, undergraduate training aims to set theory and professional provision in their social, economic and political context and to promote graduates' employability; growing a sense of responsibility, personal and social, for one's own and others' well-being should be a developmental aim, and guidance from QAA and Advance HE gives more on education for sustainable development.",
  prac="Set theoretical learning and professional provision in their social, economic and political context and promote employability; treat personal and social responsibility for others' and one's own well-being as a developmental aim (should).",
  ben="You should grow in your sense of responsibility for your own and other people's well-being, and see your future practice in its social, economic and political setting.",
  aaw="Treat this as an expectation (should) that personal and social responsibility for well-being is a developmental aim, under education for sustainable development; it holds across undergraduate training, not at a single level. Cite it as " + CITE + "1.25, and the QAA and Advance HE guidance it names as std:doc:qaa-advancehe-esd-2021-guidance. Set it beside " + SID + "1.23 and 1.24 and the self-care outcomes 3.6.j.v and 3.6.k.vii, and do not present it as an assessed threshold.",
  aad="Raise it when sustainability, social responsibility or students' own well-being is discussed as part of becoming a professional. With a student, say in plain words that the course aims to grow your sense of responsibility for others and yourself; with staff, frame it as a developmental aim to plan for. Ask how the person's practice could affect the well-being of their community, and how they look after themselves. Avoid treating it as a pass or fail requirement.")
s('1.27', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='osteopathy graduates',
  addressee='learner', verbs=['collect', 'analyse', 'manipulate', 'understand', 'articulate', 'demonstrate', 'encouraged', 'develop', 'apply'], about='enterprising skills and their value', domain='generic-skill', award=HON,
  para="Osteopathy graduates can collect, analyse and handle varied data and should understand the commercial and practical worth of their skills and be able to explain and show them to employers and when planning self-employment, private practice or more study; they should also be encouraged to become aware of their own enterprising capabilities and to apply them flexibly as contexts change.",
  prac="Graduates should understand the commercial and practical value of their skills and be able to articulate and show it to employers and in plans for their own practice or further study; courses should encourage awareness of their enterprising and entrepreneurial capabilities and the motivation to apply them flexibly.",
  ben="You should understand what your skills are worth, commercially and practically, and be able to explain and show them to employers or when planning your own practice or further study; you should also come to recognise your own enterprising strengths and use them flexibly.",
  aaw="Treat this as an expectation (should) of osteopathy graduates under the enterprise and entrepreneurship theme: understanding and articulating the value of their skills, and being encouraged towards enterprising self-awareness; it sits at FHEQ level 6 for the honours award. Cite it as " + CITE + "1.27. Set it beside " + SID + "1.28 to 1.32 on the entrepreneurial mindset, the outcomes 3.6.n.v and 3.6.d.v and the level descriptor qaa/fheq-2024/4.15.b9.1, and do not present the examples that follow it in 1.28 to 1.32 as required.",
  aad="Raise it when a student talks about careers, self-employment, opening a practice or further study. Put it plainly: you should be able to say what your skills are worth and show them to an employer or in a business plan. Ask what the person would say if a clinic owner asked what they bring, and which enterprising strengths they see in themselves. Avoid turning it into a sales pitch or implying every graduate must run a business.")
s('1.33', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='students developing digital and transferable skills',
  addressee='both', verbs=['include', 'using', 'communicate', 'enhance'], about='digital competency used creatively and accessibly', domain='generic-skill', award=HON,
  para="Building digital competence and transferable skills should take in the use of digital technology to share ideas creatively, innovatively and accessibly, to support academic success and employability.",
  prac="Develop digital competency and transferable skills through using digital tools to get ideas across creatively, innovatively and accessibly, for academic success and employability.",
  ben="You should use digital tools to share your ideas creatively and accessibly, which will help both your studies and your career.",
  aaw="Treat this as an expectation (should) about how digital competency and transferable skills are developed, under the enterprise and employability theme with an accessibility element; it holds across the course and refines the communication strand at FHEQ level 6. Cite it as " + CITE + "1.33. Set it beside " + SID + "3.6.d.v (digital literacy for practice) and the level 6 descriptor qaa/fheq-2024/4.15.b8, and do not present it as a named digital qualification.",
  aad="Raise it when a student prepares presentations, online content or patient materials, or a team plans digital skills teaching. Tell a student plainly that you should be able to use digital tools to get ideas across in creative and accessible ways; with staff, frame it as an expectation for where digital work sits in the course. Ask whether a piece of the person's recent work would reach someone using a screen reader or captions. Avoid reducing it to software training.")
s('1.34', type='expectation', rung='none', force='should', level='none', appliesTo='curriculum design',
  addressee='provider', verbs=['achieved', 'embedded'], about='employability and enterprise in curriculum design', domain='none', award='none',
  para="Developing these professional knowledge, skills and competencies should be a central part of curriculum design and can be spread across the training; outcomes, teaching and authentic assessment for employability and enterprise may sit in dedicated modules and be embedded across others.",
  prac="Make professional, employability and enterprise development a key part of curriculum design across the programme, with outcomes, activities and authentic assessment in dedicated modules and embedded in others.",
  ben=('n/a', 'a duty on curriculum design; the student meets its effect'),
  aaw="Treat this as an expectation (should) on curriculum design under the enterprise and entrepreneurship theme: employability, enterprise and entrepreneurship are to be a key aspect, with their placement left open (may). It is a design duty with no level of its own. Cite it as " + CITE + "1.34. Set it beside " + SID + "1.27, 1.35 to 1.38 and the outcome 3.6.n.v, and do not claim it requires a dedicated module.",
  aad="Raise it with a programme team mapping employability and enterprise across modules. Frame it for staff as a design expectation with freedom over where it sits. Ask where students now meet authentic assessment of their business and career skills, and whether it is spread or concentrated. Avoid presenting it to students as a duty of theirs.")
s('1.35', type='expectation', rung='none', force='describes', level='none', appliesTo='teaching on osteopathy courses',
  addressee='provider', verbs=['recommended', 'enrich', 'offer'], about='external speakers and alumni in teaching', domain='none', award='none',
  para="Bringing in external speakers, members of the profession and alumni to enrich teaching and share first-hand experience is recommended; meeting a range of osteopaths builds awareness of the working context and can strengthen graduates' ability to handle market forces and promote themselves ethically.",
  prac="Involve external speakers, practitioners and alumni in teaching (the issuer recommends it), so students meet varied osteopaths and grow ready to handle the market and present themselves ethically.",
  ben=('n/a', 'a recommendation to the course on its teaching'),
  aaw="Treat this as a recommendation to courses under the enterprise theme; the issuer's word is recommended, outside the five force words, so it is recorded as describes (Part E) and should not be written up as a must or a should. It holds for teaching across the course, not at a level. Cite it as " + CITE + "1.35. Set it beside " + SID + "1.34 and 1.36 to 1.38.",
  aad="Raise it when a team plans guest teaching, alumni links or careers input. Frame it for staff as a recommendation, not a requirement, and as a way to show students varied working lives. Ask which kinds of practice students currently never hear about first-hand. Avoid presenting it to students as an obligation.")
s('2.3', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='osteopathy courses and their students',
  addressee='both', verbs=['support', 'ensuring', 'required', 'enable'], about='clinical reasoning, supervised experience and autonomy in learning', domain='subject-skill', award=[HON, IM],
  para="Academic and theoretical learning progresses through levels in line with the Quality Code and spans procedural, propositional and psychomotor knowledge within a clinical framework; practical and clinical reasoning skills should firmly support clinical decisions and safe, effective practice that keeps students fit to practise; supervised clinical experience is essential and autonomy in learning is required for lifelong learning and reflection; enough knowledge of UK healthcare, business and regulation lets graduates work independently.",
  prac="Design progression aligned to the Quality Code across procedural, propositional and psychomotor knowledge; make applied and clinical reasoning robustly support safe, effective decisions and continuing fitness to practise; provide supervised clinical experience and require autonomy in learning.",
  ben="Your practical and clinical reasoning skills should firmly support safe, effective decisions about patients and keep you fit to practise; supervised clinic work is central, and you will need to take charge of your own learning.",
  aaw="Treat this as an expectation (should) that applied and clinical reasoning robustly support safe decision-making, joined by two plain statements that supervised clinical experience is essential and autonomy in learning is required; it applies across the course up to FHEQ level 6 or 7. Cite it as " + CITE + "2.3. Set it beside " + SID + "3.6.g.iv, 3.6.k.iii, the threshold standard 6.10.b5 and the level 6 descriptor qaa/fheq-2024/4.15.b5, and do not claim it sets hours of clinical practice (the figure is in 6.4).",
  aad="Raise it when a student asks why clinic matters so much or struggles to take charge of their own learning, or a team reviews clinical progression. Put it plainly to a student: your reasoning should support safe decisions, clinic experience is essential and you are expected to direct your own learning; for staff, frame it as how progression and supervision are designed. Ask how the person reasons from findings to a decision, and what they do to learn between clinic sessions. Avoid quoting the paragraph at length.")
s('2.5', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='osteopathy courses and their graduates',
  addressee='both', verbs=['graduate', 'demonstrate', 'acquiring', 'emphasise', 'support', 'guide'], about='core sciences, communication and patient-centred teaching', domain='knowledge', award=[HON, IM],
  para="As a primary healthcare profession, osteopathy needs students to graduate with full knowledge and understanding of anatomy, physiology and pathology and excellent communication and interpersonal skills for working with patients and other professionals; teaching and learning should stress patient-centred care, including a full grasp of psychosocial factors, to support the patient's journey.",
  prac="Ensure graduates leave with comprehensive anatomy, physiology and pathology and excellent communication and interpersonal skills; teaching and learning should emphasise patient-centred care, psychosocial factors included.",
  ben="You will need a thorough knowledge of anatomy, physiology and pathology and excellent communication skills, and your teaching should put the patient, with their psychological and social circumstances, at the centre.",
  aaw="Treat this as an expectation (should) that osteopathic teaching emphasises patient-centred care, set beside a statement that graduates need comprehensive anatomy, physiology and pathology and excellent communication; it bears on the honours award at FHEQ level 6. Cite it as " + CITE + "2.5. Set it beside " + SID + "3.6.a.i, 3.6.d.i and the threshold standards 6.10.b1 and 6.10.b3, and the level descriptor qaa/fheq-2024/4.15.b1; do not present the word excellent here as a rung above threshold.",
  aad="Raise it when a team weighs the balance of basic science, communication and patient-centred teaching. With staff, frame it as an expectation about emphasis in teaching; with a student, say plainly that you will need strong science and people skills and that care starts from the patient. Ask where in the course patient-centred care is taught and practised, not only described. Avoid treating the word excellent as the minimum standard.")
s('3.5', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='competent students on graduation',
  addressee='learner', verbs=['develop', 'apply', 'graduating'], about='core capability for safe practice', domain='subject-skill', award=[HON, IM],
  para="Competent students will build core knowledge, understanding and skill and be able to apply them to evaluating and managing patients, graduating as safe, rounded practitioners; the outcomes in 3.6 set out the detail and are designed to show the capabilities needed to register as an osteopath in the UK under the OPS and the regulator's graduate outcomes.",
  prac="Competent students will build core knowledge, understanding and skill and be able to use them in evaluating and managing patients, graduating as safe, rounded practitioners; 3.6 sets out the detail against the registration requirements.",
  ben="You will build the core knowledge, understanding and skills of osteopathy and be able to use them to assess and care for patients, so that you graduate as a safe, all-round practitioner ready to register.",
  aaw="Treat this as an outcome statement (will) that introduces the detailed outcomes in 3.6: competent students develop core capability and graduate as safe, rounded practitioners, at FHEQ level 6 for the honours award. Cite it as " + CITE + "3.5. Say that the outcomes are designed to show the capabilities registration needs, not that meeting them registers anyone. Set it beside " + SID + "3.4, the 3.6 outcomes and the threshold list 6.10, and the level descriptor qaa/fheq-2024/4.15.b6.",
  aad="Raise it when a student asks what the course expects of them by the end, or a team introduces the outcome framework. Put it plainly to a student: you will build the core knowledge and skills to assess and care for patients safely; for staff, frame it as the purpose of the 3.6 outcomes. Ask which parts of patient evaluation and management the person feels least ready for. Avoid listing all the 3.6 outcomes at once.")
s('4.2', type='outcome', rung='none', force='will', level='fheq:6', appliesTo='students of osteopathy',
  addressee='learner', verbs=['accumulated', 'equipped', 'prepares', 'reflect'], about='reflective, leadership, peer review and lifelong learning skills', domain='generic-skill', award=[HON, IM],
  para="Knowledge, skills and experience build up across the course; teaching and learning will take a critical, reflective approach to osteopathy with attention to its concepts, principles and personalised care; students will gain reflective, leadership, peer review and lifelong learning skills; joining theory and practice prepares them to work autonomously, and methods suit diverse learning styles and are delivered sustainably and inclusively.",
  prac="Teaching and learning will be critical and reflective about osteopathic concepts, principles and personalised care; students will gain reflective, leadership, peer-review and lifelong learning skills, and methods suit diverse learners and are delivered sustainably and inclusively.",
  ben="You will learn in a critical, reflective way and gain skills in reflection, leadership, peer review and lifelong learning that prepare you to practise on your own.",
  aaw="Treat this as an expectation (will) about the teaching and learning experience and the skills students gain from it (reflection, leadership, peer review, lifelong learning), at FHEQ level 6 for the honours award. Cite it as " + CITE + "4.2. Set it beside " + SID + "3.6.k.i, 3.6.k.vi, the threshold standard 6.10.b13 on leadership and the level descriptor qaa/fheq-2024/4.15.b9.3; its mention of sustainable and inclusive delivery links it to the cross-cutting themes without making it a theme statement.",
  aad="Raise it when a student asks what kind of learning to expect or how leadership and peer review fit an osteopathy course. Tell a student plainly that you will be asked to reflect, give and take peer feedback and lead, because you will practise on your own; for staff, frame it as what teaching should build. Ask where the person has practised leadership or peer review so far. Avoid presenting it as a list of assessed units.")
s('5.1', type='expectation', rung='none', force='should', level='none', appliesTo='assessment on pre-registration courses',
  addressee='both', verbs=['support', 'enable', 'demonstrate', 'met', 'permitted'], about='assessment towards the OPS; the condition to graduate', domain='none', award='none',
  para="Assessment strategies should support students' development as practitioners and in the end let them show they meet the OPS; only students who meet those standards may graduate.",
  prac="Design assessment that supports development and finally enables students to demonstrate they meet the OPS; only those who meet them graduate.",
  ben="Your assessments should help you develop as a practitioner and let you show that you meet the professional standards; you will only graduate once you have met them.",
  aaw="Treat this as an expectation (should) on assessment strategy, with a plain condition attached: only students who meet the OPS are permitted to graduate. It holds for the pre-registration award at FHEQ level 6 or 7, not for a single module. Cite it as " + CITE + "5.1, and the regulator's OPS for the standards themselves. Set it beside " + SID + "5.2 to 5.4 and 6.8, and do not claim the statement defines the OPS.",
  aad="Raise it when a student asks what they must show to graduate or a team designs final assessments. Tell a student plainly that assessment is there to help you develop and that you graduate only when you have shown you meet the professional standards; for staff, frame it as a design expectation with a firm condition at the end. Ask how the person's assessments so far map to the professional standards. Avoid reading out the standards or implying a grade alone decides it.")
s('5.2', type='expectation', rung='none', force='should', level='none', appliesTo='assessment strategies',
  addressee='provider', verbs=['reflect', 'relate', 'prepare', 'play', 'supported'], about='authentic assessment shaped by practitioners and patients', domain='none', award='none',
  para="Assessment strategies should match the range and depth of competence the OPS requires and relate, where possible, to real situations and practice; experienced, qualified educators and practitioners should lead their design, with the patient voice in support.",
  prac="Make assessment reflect the range and depth of OPS competence and real practice where possible; involve experienced educators and practitioners centrally, supported by the patient voice.",
  ben=('n/a', 'a duty on the course in designing assessment'),
  aaw="Treat this as an expectation (should) on how assessment strategies are designed: authentic, matched to OPS competence and shaped by practitioners and the patient voice; it is a provider duty with no level of its own. Cite it as " + CITE + "5.2. Set it beside " + SID + "5.1, 5.3 and 5.4, and do not claim it requires patients to mark students.",
  aad="Raise it when a team reviews assessment design, patient involvement or authenticity. Frame it for staff as an expectation that assessment mirrors real practice and draws on practitioners and patients. Ask where patients now shape assessment and how close the tasks are to real clinic. Avoid giving it to students as their responsibility.")
s('5.3', type='expectation', rung='none', force='should', level='none', appliesTo='assessment tools',
  addressee='provider', verbs=['utilised', 'support', 'providing'], about='varied, valid and reliable assessment', domain='none', award='none',
  para="A varied range of assessment tools should be used to support learning and development and different learning styles and differences; they should be valid and reliable and give a clear, supportive path to progression, with formative and summative assessment and the involvement of peers, patients, educators and outside experts where suitable at the centre.",
  prac="Use varied, valid and reliable assessment tools that support different learners and give a transparent path to progression, centred on formative and summative assessment and involving peers, patients, educators and external expertise where suitable.",
  ben=('n/a', 'a duty on the course in choosing assessment'),
  aaw="Treat this as an expectation (should) on the assessment toolset: varied, valid, reliable and centred on formative and summative assessment with peer, patient and external involvement; a provider duty with no level of its own. Cite it as " + CITE + "5.3. Set it beside " + SID + "5.2 and 5.4 and the inclusive design paragraphs 1.17 and 1.22, and do not claim it names particular tools.",
  aad="Raise it when a team reviews the assessment mix or a concern arises about fairness for different learners. Frame it for staff as an expectation of variety, validity and transparency. Ask whether students can see how each assessment leads to the next stage, and where formative feedback sits. Avoid presenting it to a student as their duty.")
s('5.4', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='assessment and the students it serves',
  addressee='both', verbs=['reflect', 'support', 'move', 'manage', 'demonstrate'], about='assessment that tracks growing complexity towards autonomy', domain='generic-skill', award=[HON, IM],
  para="Assessment should mirror the rising complexity and responsibility of study and the demands of the OPS, supporting students from novice to competent practitioner, when they will need to manage clinical uncertainty and show the qualities and competence of an autonomous practitioner able to work in many settings.",
  prac="Assessment should track rising complexity and responsibility and the OPS requirements, supporting the move from novice to competent practitioner able to handle clinical uncertainty and act autonomously across settings.",
  ben="Your assessments should grow more demanding as you progress, helping you move from beginner to competent practitioner who can handle clinical uncertainty and work independently in different settings.",
  aaw="Treat this as an expectation (should) on assessment progression, with the outcome it serves stated in will: by the end students need to manage clinical uncertainty and show the competence of an autonomous practitioner, at FHEQ level 6 for the honours award. Cite it as " + CITE + "5.4. Set it beside " + SID + "5.1, the threshold standard 6.10.b13 and the level 6 descriptor qaa/fheq-2024/4.15.b9.2, and do not claim it sets level 7 outcomes for integrated master's courses.",
  aad="Raise it when a student asks why assessment gets harder or a team designs progression across years. Tell a student plainly that assessment grows with you, towards handling uncertainty on your own; for staff, frame it as the progression assessment should follow. Ask what clinical uncertainty the person has handled recently and how. Avoid presenting the end point as something expected in the first year.")
s('6.2', type='expectation', rung='none', force='should', level='fheq:6', appliesTo='each higher education provider',
  addressee='provider', verbs=['perform', 'refer'], about='achievement above threshold and Annex D', domain='none', award=HON,
  para="Most students will do well above the minimum threshold standards; each provider has its own way of deciding what counts as evidence of this and should refer to Annex D of the UK qualifications frameworks.",
  prac="Expect most students to exceed the threshold; set your own method for judging evidence of higher achievement and refer to Annex D of the Frameworks for Higher Education Qualifications.",
  ben=('n/a', 'a duty on the provider in judging achievement above the threshold; the student-facing point is the threshold list at 6.10'),
  aaw="Treat this as an expectation (should) on providers: judge achievement above the threshold by their own method, with reference to Annex D, the degree classification descriptions. It holds for the honours award at FHEQ level 6. Cite it as " + CITE + "6.2, and Annex D as std:doc:qaa-fheq-2024-framework (for example qaa/fheq-2024/annex-d/summary/r1/3rd for the threshold class). Set it beside " + SID + "6.1 and the 6.10 list, and do not claim the statement itself defines typical or excellent rungs.",
  aad="Raise it when a team sets classification criteria or a student asks how a first differs from a pass. With staff, frame it as the provider's own judgement, anchored in Annex D; with a student, explain only that the 6.10 list is the floor and that classes above it are described elsewhere. Ask how the course's marking criteria line up with Annex D's descriptions. Avoid treating the classification descriptions as part of this statement.")
s('6.6', type='expectation', rung='none', force='describes', level='fheq:6', appliesTo='students and osteopaths',
  addressee='learner', verbs=['engage', 'evaluate', 'conduct', 'support', 'develop'], about='evidence-informed practice and research skills', domain='subject-skill', award=[HON, IM],
  para="Students develop the skills to engage critically with evidence-informed practice in its three parts, namely research, clinical experience and what patients expect; they are expected to judge how clinically relevant published research is and to carry out audits, service evaluations and research to improve practice, care and current professional issues; in any setting osteopaths are expected to back and build an evidence-informed approach.",
  prac="Students develop critical engagement with research, clinical experience and patient expectations; they are expected to judge the clinical relevance of published research and to conduct audit, service evaluation and research that improve practice and care.",
  ben="You will build the skills to weigh research, clinical experience and what patients expect, and you are expected to judge how relevant published research is and to take part in audit and research that improves care.",
  aaw="Treat this as an expectation the issuer words as 'are expected to', outside the five force words and recorded as describes (Part E): students judge the relevance of research and conduct audit, service evaluation and research, at FHEQ level 6 for the honours award. Cite it as " + CITE + "6.6. Set it beside the threshold standard " + SID + "6.10.b11, the outcomes 3.6.a.viii and 3.6.k.ix and the level 6 descriptor qaa/fheq-2024/4.15.b3.2, and do not write it up as a must.",
  aad="Raise it when a student plans an audit or research project or asks how research fits clinical work. Tell a student plainly that you are expected to weigh research, experience and what patients want, and to help improve care through audit and research; for staff, frame it as the expectation behind research teaching. Ask which recent study has changed, or should change, how the person treats patients. Avoid presenting it as a requirement to publish.")
s('6.8', type='requirement', rung='none', force='must', level='none', appliesTo='osteopathy courses, graduating students and registered osteopaths',
  addressee='both', verbs=['approved', 'reviewed', 'requires', 'observing', 'demonstrating', 'required', 'meet'], about='Recognised Qualification approval and the OPS', domain='none', award='none',
  para="Osteopathy courses are approved by the regulator, the General Osteopathic Council, through Recognised Qualification status that is reviewed regularly; this requires following its graduate outcomes and education standards of September 2022 and showing that the OPS are delivered well; those graduating and those registered must meet the OPS for the whole of their careers.",
  prac="Courses gain and keep Recognised Qualification status from the GOsC through regular review, which requires following its graduate outcomes and education standards (September 2022) and delivering the OPS effectively; graduates and registrants must meet the OPS throughout their careers.",
  ben="Throughout your career, from graduation onwards, you must meet the regulator's professional practice standards; your course is approved and regularly reviewed to make sure it prepares you for this.",
  aaw="Treat this as a requirement (required, recorded as must) reported from the regulator's system: courses hold Recognised Qualification status under regular review, and graduates and registrants must meet the OPS throughout their careers. It is not a level outcome. Cite it as " + CITE + "6.8, and the regulator's documents for the standards. Set it beside " + SID + "1.5, 5.1 and 6.9, and do not claim that the statement's own standards are the regulator's approval criteria.",
  aad="Raise it when a student asks what happens after graduation or a team prepares for regulatory review. Tell a student plainly that you must keep meeting the professional standards for as long as you practise; for staff, frame it as the condition of the course's recognition. Ask whether the person knows how the standards will apply to them in their first year of practice. Avoid reading the standards aloud or confusing course approval with the student's own registration.")

# ---- 3.4 key characteristics (lead-in: "An osteopathic graduate can demonstrate the qualities of ... practitioner who:")
def k34(n, verbs, about, domain, para, prac, ben, near, fw, when, q):
    s('3.4.b%d' % n, type='outcome', rung='none', force='will', forceFrom='3.4', level='fheq:6', appliesTo='graduates of pre-registration osteopathy courses',
      addressee='learner', verbs=verbs, about=about, domain=domain, award=[HON, IM], para=para, prac=prac, ben=ben,
      aaw=("Treat this as one of six key characteristics the statement expects an osteopathy graduate to be able to show (" + about + "); the lead-in at 3.4 says a graduate can demonstrate it, recorded here as will, at FHEQ level 6 for the honours award. "
           "Cite it as " + CITE + "3.4, bullet " + str(n) + ". Do not present it as a separate threshold: it summarises qualities that the outcomes in 3.6 and the threshold list in 6.10 spell out. "
           "Set it beside " + near + " and the level descriptor " + fw + " (spine:6)."),
      aad=("Raise it when " + when + ". With a student, put it in plain second-person words as part of the practitioner you are becoming; with staff, frame it as a quality the whole course builds and the clinic shows. "
           "Ask: " + q + " Avoid reading the list aloud or treating one bullet as the whole picture of a graduate."))

k34(1, ['support'], 'practical competence and problem-solving', 'subject-skill',
    "Will be able to show they are a competent practitioner with strong practical skills (manual therapy among them) and the problem-solving to draw on varied approaches for different presentations.",
    "Graduates will be competent, with highly developed practical and manual therapy skills and problem-solving across approaches for different presentations.",
    "You will be a competent practitioner with strong hands-on and manual therapy skills, able to solve problems using a range of approaches for different patients.",
    SID + '6.10.b6 and 3.6.h.i', 'qaa/fheq-2024/4.15.b2', 'a student asks what kind of practitioner the course aims to produce',
    "Which kinds of patient presentation do you feel least equipped to handle with your current range of approaches?")
k34(2, ['demonstrates', 'allow', 'integrate'], 'integrating many factors in whole-person care', 'subject-skill',
    "Will be able to show a developed knowledge base and clinical ability that lets them bring many factors together in a full, overall approach to a person's health needs.",
    "Graduates will have a developed knowledge base and the clinical ability to integrate multiple factors into a comprehensive approach to each person's health needs.",
    "You will have the knowledge and clinical ability to bring many factors together and look at a patient's health needs as a whole.",
    SID + '6.10.b4 and 1.12.b1', 'qaa/fheq-2024/4.15.b1', 'a case discussion needs to pull several factors together',
    "In your last complex case, which factors did you bring together, and which did you leave out?")
k34(3, ['work'], 'a caring partnership with the patient', 'subject-skill',
    "Will be able to show they are caring, empathetic and trustworthy and can work as the patient's partner.",
    "Graduates will be caring, empathetic and trustworthy and able to work in partnership with patients.",
    "You will be caring, empathetic and trustworthy, and work with patients as partners.",
    SID + '3.6.c.ii and 3.6.j.iii', 'qaa/fheq-2024/4.15.b9.1', 'the therapeutic relationship or patient trust comes up',
    "How would a patient you treated describe working with you?")
k34(4, [], 'professional attitudes, values and behaviour', 'subject-skill',
    "Will be able to show professional attitudes, values and behaviour fitting a healthcare practitioner, including on consent, safeguarding and candour.",
    "Graduates will hold the attitudes, values and behaviours of a healthcare practitioner, including consent, safeguarding and candour.",
    "You will act with the attitudes, values and behaviour expected of a health professional, including on consent, safeguarding and honesty when things go wrong.",
    SID + '3.6.l.iii and 6.10.b12', 'qaa/fheq-2024/4.15.b9.1', 'professional behaviour, consent or safeguarding is in question',
    "When did consent or safeguarding shape what you did in clinic?")
k34(5, [], 'reflection, self-awareness and lifelong learning', 'generic-skill',
    "Will be able to show they are reflective, self-aware and enquiring, and committed to learning throughout life.",
    "Graduates will be reflective, self-aware and enquiring and committed to lifelong learning.",
    "You will be reflective, self-aware and curious, and committed to learning throughout your career.",
    SID + '3.6.k.i and 6.10.b10', 'qaa/fheq-2024/4.15.b9.3', 'a student plans their development or reflects on their learning',
    "What has reflection changed in how you practise this year?")
k34(6, ['appreciates'], 'the scope and limits of osteopathy and of oneself', 'understanding',
    "Will be able to show they value osteopathy's role in treating patients of every age while knowing the limits of its scope, above all in relation to their own knowledge and abilities.",
    "Graduates will appreciate osteopathy's role across all ages and know the limits of its scope, especially those set by their own knowledge and capability.",
    "You will value what osteopathy can do for patients of all ages and know where its limits lie, especially the limits of your own knowledge and skill.",
    SID + '6.10.b9 and 3.6.j.vi', 'qaa/fheq-2024/4.15.b4', 'a student considers treating a patient outside their experience, such as a child or an older adult with complex needs',
    "Which patients would you refer on at this stage, and why?")

# ---- 3.6 graduate outcomes (lead-in: "On successful completion of their studies, students will have developed the following ...")
GRP = {  # letter: (heading gloss, threshold neighbour, FHEQ level 6 descriptor, when to raise)
    'a': ('knowledge for safe, competent practice', '6.10.b3', 'qaa/fheq-2024/4.15.b1', 'a student asks what science they need, or a team reviews the knowledge base of the course'),
    'b': ('concepts and principles of osteopathy', '6.10.b2', 'qaa/fheq-2024/4.15.b7', 'talk turns to osteopathic principles and how they guide clinical reasoning'),
    'c': ('professionalism and therapeutic relationships', '6.10.b12', 'qaa/fheq-2024/4.15.b9.1', 'a student reflects on a therapeutic relationship, a boundary or an ethical problem'),
    'd': ('communication', '6.10.b1', 'qaa/fheq-2024/4.15.b8', 'communication with patients or colleagues, in person or online, comes up'),
    'e': ("identifying and evaluating the patient's needs", '6.10.b4', 'qaa/fheq-2024/4.15.b7', 'a student is learning to assess a new patient or a team reviews clinical assessment'),
    'f': ('palpation', '6.10.b4', 'qaa/fheq-2024/4.15.b2', 'palpation, touch or consent in hands-on work is the subject'),
    'g': ('planning, justifying and monitoring treatment', '6.10.b5', 'qaa/fheq-2024/4.15.b7', 'treatment planning, hypotheses or referral decisions are being discussed'),
    'h': ('conducting treatment and patient management', '6.10.b6', 'qaa/fheq-2024/4.15.b2', 'a student is choosing or adapting techniques and management'),
    'i': ('evaluating progress after treatment', '6.10.b6', 'qaa/fheq-2024/4.15.b6', "a student reviews a patient's response to treatment"),
    'j': ('advice and support for healthy living', '6.10.b7', 'qaa/fheq-2024/4.15.b6', 'advice on healthy living or referral to other services is in question'),
    'k': ('personal and professional development', '6.10.b10', 'qaa/fheq-2024/4.15.b5', 'a student plans their learning, reflection or continuing development'),
    'l': ('professional identity, accountability and ethics', '6.10.b12', 'qaa/fheq-2024/4.15.b9.1', 'professional conduct, regulation or patient safety comes up'),
    'm': ('collaboration across professions', '6.10.b8', 'qaa/fheq-2024/4.15.b3.2', "osteopathy's place in wider healthcare or its claims are discussed"),
    'n': ('running a practice', '6.10.b13', 'qaa/fheq-2024/4.15.b9.2', 'a student thinks about running or working in a practice'),
}
def o36(i, verbs, about, domain, para, prac, ben, q):
    letter, roman = i.split('.')[2:4]
    head, near, fw, when = GRP[letter]
    s(i, find=FIND36[i], type='outcome', rung='none', force='will', forceFrom='3.6', level='fheq:6',
      appliesTo='students on successful completion of a pre-registration osteopathy course', addressee='learner',
      verbs=verbs, about=about, domain=domain, award=[HON, IM], para=para, prac=prac, ben=ben,
      aaw=("Treat this as a graduate outcome the statement expects on completing a pre-registration osteopathy course, under the group on " + head + "; its force is will, from the lead-in at 3.6, and it sits at FHEQ level 6 for the honours award. "
           "Cite it as " + CITE + "3.6 " + letter + ") " + roman + ". Do not claim it is a regulatory requirement in itself or a level 7 outcome, although integrated master's courses also work to it. "
           "Set it beside the threshold standard " + SID + near + ", the other items in group " + letter + ") and the level 6 descriptor " + fw + " (spine:6)."),
      aad=("Raise it when " + when + ". With a student, put it plainly in the second person as something you will be able to do by graduation; with staff, frame it as an outcome the course teaches and assesses. "
           "Ask: " + q + " Avoid reading the issuer's wording aloud at length or suggesting that meeting it alone entitles anyone to register."))

# a) knowledge relevant to safe and competent practice
o36('3.6.a.i', ['recognise', 'identify', 'differentiate'], 'human structure and function', 'knowledge',
    "Will have a detailed, joined-up knowledge of how the human body is built and works, centred on the neuromusculoskeletal system, enough to tell normal variation from abnormal structure and process in living people.",
    "Graduates will know human anatomy and physiology in integrated detail, above all the neuromusculoskeletal system, well enough to tell normal variation from pathology in a living patient.",
    "You will know in detail how the body is built and how it works, especially muscles, bones, joints and nerves, so that you can tell normal variation from something abnormal in a living person.",
    "Could you explain how you would tell a normal anatomical variant from an abnormal finding in a patient you examined?")
o36('3.6.a.ii', ['inform', 'recognise'], 'disease knowledge for judgement and referral', 'knowledge',
    "Will know enough current science and medicine about human disease to guide clinical judgement on examination and palpation findings and to spot conditions that need referral for further tests or other professional help.",
    "Graduates will hold current scientific and medical knowledge of disease, enough to support judgement about examination and palpatory findings and to identify when a patient needs referring on.",
    "You will know enough about disease to make sense of what you find when you examine and palpate a patient, and to notice when someone needs referring for tests or other professional help.",
    "Which findings in a recent case would make you stop and refer the patient on, and why?")
o36('3.6.a.iii', ['provide'], 'psychology and sociology of health', 'knowledge',
    "Will know the psychology and sociology that bear on gaining and keeping health, and appreciate each person's needs, values and beliefs, enough to frame clinical decisions and patient management.",
    "Graduates will know the psychology and sociology relevant to health and appreciate individual needs, values and beliefs, as context for their clinical decisions and management of patients.",
    "You will understand the psychological and social side of health and respect each patient's needs, values and beliefs, so that they shape the decisions you make about care.",
    "How did a patient's beliefs or circumstances change the plan you agreed with them?")
o36('3.6.a.iv', [], 'pain neurophysiology and psychosocial influence', 'knowledge',
    "Will know the neurophysiology of pain and the psychosocial influences on it, and how both affect the patient and the way their problem presents.",
    "Graduates will know pain neurophysiology and the psychosocial factors in pain, and how these shape the patient's experience and clinical picture.",
    "You will understand how pain works in the nervous system, how psychological and social factors affect it, and how both change what a patient experiences and shows you.",
    "What would you say to a patient about why their pain has lasted longer than the tissue injury?")
o36('3.6.a.v', ['understand', 'influence'], 'the role of touch in treatment', 'understanding',
    "Will understand what touch does within treatment and how it can affect the way patients respond to osteopathic techniques.",
    "Graduates will understand the place of touch in treatment and how it can shape patients' responses to techniques.",
    "You will understand the part touch plays in treatment and how it can change the way a patient responds to what you do.",
    "How might the way you touch a patient change how they respond to a technique?")
o36('3.6.a.vi', ['recognise', 'mask', 'involve'], 'concerns hidden behind the presenting problem', 'understanding',
    "Will recognise that the problem a patient brings may hide other health concerns, physical and behavioural.",
    "Graduates will recognise that a presenting complaint can conceal underlying physical or behavioural health issues.",
    "You will be alert to the chance that the problem a patient comes with may be hiding another health issue, physical or behavioural.",
    "In your last few new patients, what else could have lain behind the complaint they described?")
o36('3.6.a.vii', ['select', 'apply', 'monitor', 'acknowledging'], 'choosing and monitoring techniques safely', 'knowledge',
    "Will know how to choose, use well and monitor a suitable range of osteopathic techniques and management approaches for each patient, taking account of relative and absolute contraindications.",
    "Graduates will know how to select, apply and monitor osteopathic techniques and management suited to the individual, alert to relative and absolute contraindications.",
    "You will know how to pick, carry out and keep track of the right osteopathic techniques and ways of managing care for each patient, and when a technique should not be used.",
    "Which contraindications did you check before choosing your techniques for that patient?")
o36('3.6.a.viii', ['demonstrating', 'appraise', 'evaluate', 'inform'], 'research methods and critical appraisal', 'subject-skill',
    "Will know and understand research methodology and be able to appraise critically how good numerical and qualitative clinical studies are, enough to guide clinical decisions and patient management.",
    "Graduates will understand research methodologies and critically judge the quality of clinical studies of either kind, numerical or qualitative, so that evidence informs their decisions and care.",
    "You will understand how clinical research is done and be able to judge how good a study is, whether numerical or qualitative, so that evidence guides your decisions about patients.",
    "Take one study you have read recently: how would you judge whether its findings should change what you do?")

# b) concepts and principles of osteopathy
o36('3.6.b.i', ['inform'], 'osteopathic principles in clinical reasoning', 'understanding',
    "Will understand critically the principles and concepts of osteopathy and how they can guide rational clinical decisions.",
    "Graduates will have a critical grasp of osteopathic principles and concepts and how they can support reasoned clinical decision-making.",
    "You will understand the principles and ideas of osteopathy critically and know how they can guide sound clinical decisions.",
    "Which osteopathic principle shaped a recent decision you made, and how would you defend that choice?")
o36('3.6.b.ii', ['inform'], 'models of health, disease and illness', 'understanding',
    "Will understand models of health, disease and illness and how they shape critical thinking about practical care and management of patients.",
    "Graduates will understand models of health, disease and illness and use them to think critically about patient care and management.",
    "You will understand different ways of thinking about health, disease and illness and use them to think critically about how you care for patients.",
    "Which model of health best explains your approach to a patient you are seeing now?")
o36('3.6.b.iii', [], 'principles of other health professions', 'understanding',
    "Will be critically aware of the principles, perspectives and practice of other relevant health professions and able to adapt them.",
    "Graduates will be critically aware of how other relevant health professions think and work, and will adapt what is useful from them.",
    "You will know, critically, how other health professions think and work, and be able to adapt what is useful from them in your own practice.",
    "What could you learn from how a physiotherapist or GP would approach the same patient?")
o36('3.6.b.iv', ['applied', 'select', 'modify', 'meet'], 'applying principles through treatment approaches', 'understanding',
    "Will understand how osteopathic principles are put into practice through different treatment and management approaches, and how to choose or adapt techniques to suit an individual patient's needs and preferences.",
    "Graduates will understand how principles translate into varied osteopathic treatment and management, and how to choose or adapt techniques for the individual's needs and preferences.",
    "You will understand how osteopathic principles show up in different treatments, and how to choose or adjust techniques to suit each patient's needs and wishes.",
    "How did you adapt a technique last week to fit what a patient needed or preferred?")

# c) professionalism and therapeutic relationships
o36('3.6.c.i', ['understand'], 'models of the therapeutic relationship', 'understanding',
    "Will understand the different models of the therapeutic relationship.",
    "Graduates will understand a range of models of the therapeutic relationship.",
    "You will understand the different ways of thinking about the relationship between practitioner and patient.",
    "Which model of the therapeutic relationship best describes how you worked with a recent patient?")
o36('3.6.c.ii', ['demonstrate', 'form'], 'elements and boundaries of the therapeutic relationship', 'subject-skill',
    "Will show the parts and limits of a therapeutic relationship, with the skills to build a fitting partnership with the patient.",
    "Graduates will demonstrate what a therapeutic relationship involves and where its boundaries lie, with the skills to build a proper partnership with each patient.",
    "You will be able to show what a good therapeutic relationship involves and where its limits lie, and build a proper partnership with each patient.",
    "Where would you draw the line with a patient who wants more than clinical care from you?")
o36('3.6.c.iii', ['show', 'identify', 'manage', 'ensuring'], 'recognising and managing boundary issues', 'subject-skill',
    "Will show the self-awareness to spot possible boundary problems and handle them well, so that care stays at a proper standard.",
    "Graduates will show the self-awareness to identify and manage potential boundary issues effectively, keeping standards of care intact.",
    "You will be self-aware enough to notice when a boundary issue might be arising and deal with it well, so your patient's care does not suffer.",
    "Can you think of a moment in clinic when a boundary felt unclear, and what did you do?")
o36('3.6.c.iv', ['deal', 'applying', 'manage'], 'uncertainty, candour and integrity', 'subject-skill',
    "Will cope well and promptly with the unfamiliar or uncertain, being open with patients when things go wrong and aware enough of themselves to manage the case honestly.",
    "Graduates will deal effectively with unfamiliar situations and uncertainty, apply the duty of candour and manage the case with integrity and self-awareness.",
    "You will be able to handle situations that are new or uncertain, be open and honest with patients when something goes wrong, and manage the case with integrity.",
    "Tell me about a time you were unsure what was going on with a patient: what did you do, and what did you tell them?")
o36('3.6.c.v', ['justify', 'cope', 'confront'], 'ethical issues in practice', 'subject-skill',
    "Will be able to defend sound strategies for handling the ethical problems a practitioner is likely to meet.",
    "Graduates will justify acceptable strategies for managing the ethical issues practitioners commonly face.",
    "You will be able to explain and defend how you would handle the ethical problems you are likely to meet in practice.",
    "What ethical dilemma have you met in clinic, and how would you justify the way you handled it?")
o36('3.6.c.vi', ['maintain', 'act', 'override'], 'confidentiality and informed consent', 'subject-skill',
    "Will keep patient information confidential and act only with informed consent from the patient or someone able to consent for them, unless safeguarding concerns take precedence.",
    "Graduates will maintain confidentiality and act only on informed consent from the patient or an authorised person, save where safeguarding overrides it.",
    "You will keep patients' information confidential and act only with their informed consent, or that of someone who can consent for them, except where a safeguarding concern comes first.",
    "When would a safeguarding concern lead you to share information without a patient's agreement?")
o36('3.6.c.vii', ['adopt', 'maintain'], 'self-care during patient contact', 'generic-skill',
    "Will use suitable ways of looking after their own physical and psychological well-being while working with patients, to stay professionally effective.",
    "Graduates will use suitable physical and psychological self-care strategies in patient work to sustain professional effectiveness.",
    "You will look after your own physical and mental well-being while treating patients, so that you can keep working at your best.",
    "What do you do to look after yourself during a demanding clinic session?")

# d) communication skills
o36('3.6.d.i', ['understand', 'move', 'adapting'], 'forms of communication and adapting them', 'generic-skill',
    "Will understand the kinds of human communication and what each does well and badly, and be able to switch between them with patients and colleagues to suit the person.",
    "Graduates will understand the forms of communication and their strengths and limits, and shift between them with patients and colleagues to fit the individual.",
    "You will understand different ways people communicate, what each does well and less well, and switch between them to suit the patient or colleague in front of you.",
    "How did you change the way you explained something for a patient who was not following you?")
o36('3.6.d.ii', ['relating', 'integrating', 'responding', 'acquired'], 'verbal, non-verbal and remote information', 'generic-skill',
    "Will be skilled at linking, combining and acting on information gathered by verbal and non-verbal means, in person or through telehealth and online meetings.",
    "Graduates will relate, integrate and respond to information gathered verbally and non-verbally, face to face or by telehealth and online.",
    "You will be good at picking up, combining and responding to what patients tell you and show you, in person or online.",
    "What did you notice in a remote consultation that you might have missed, or caught, in person?")
o36('3.6.d.iii', ['developing', 'translate', 'communicate'], 'language for palpatory findings', 'subject-skill',
    "Will be building a full vocabulary that turns what is felt in palpation into suitable language for clear communication with colleagues, other professionals and patients.",
    "Graduates will be developing a full vocabulary to put palpatory findings into words suited to colleagues, other professionals and patients.",
    "You will be building the vocabulary to put what you feel with your hands into clear words for patients, colleagues and other professionals.",
    "How would you describe a palpatory finding to a GP, and how would you describe it to the patient?")
o36('3.6.d.iv', ['speak', 'appraising', 'make', 'inform'], 'speaking critically about osteopathy and its claims', 'subject-skill',
    "Will talk about osteopathy from a critical, reasoned standpoint, covering its limits, strengths and potential, weighing research, opinion and anecdote to judge therapeutic claims and better inform patients.",
    "Graduates will discuss osteopathy critically, including its limits, strengths and potential, weighing research against opinion and anecdote to assess therapeutic claims for patients.",
    "You will be able to talk about osteopathy critically, including what it cannot do as well as what it can, and weigh research against opinion and anecdote when telling patients what to expect.",
    "If a patient asked whether osteopathy can cure their condition, how would you answer honestly?")
o36('3.6.d.v', ['interact', 'use', 'manage', 'present', 'analyse'], 'digital literacy for running a practice', 'generic-skill',
    "Will be digitally literate enough to run a modern osteopathic practice efficiently: working with other health professionals, writing good reports and presentations for referral, using technology for research and clinic tasks, handling financial and other data for legal compliance and analysing data of both kinds for audit.",
    "Graduates will have the digital literacy to run a modern practice: liaising with other professionals, producing high-quality referral reports and presentations, using technology for research and clinical work, managing financial and compliance data and analysing data for audit.",
    "You will be confident with the digital side of running a practice: working with other health professionals, writing good referral reports, using technology for research and clinic work, keeping financial and legal records and analysing data for audit.",
    "Which parts of running a practice's records and data do you feel ready for, and which not yet?")

# e) identification and evaluation of the needs of the patient
o36('3.6.e.i', ['demonstrate'], 'case history and analysis of the complaint', 'subject-skill',
    "Will show effective, efficient taking of a detailed case history and analysis of the presenting complaint.",
    "Graduates will demonstrate effective, efficient detailed case-history taking and analysis of the presenting complaint.",
    "You will be able to take a detailed case history efficiently and analyse the problem the patient has come with.",
    "What questions in your case history most often change your thinking about the complaint?")
o36('3.6.e.ii', ['recognise'], 'psychosocial context and shared decisions', 'subject-skill',
    "Will recognise how much the psychosocial setting of the complaint matters and the part shared decision-making plays in planning treatment.",
    "Graduates will recognise the weight of a complaint's psychosocial context and the part shared decisions play in planning treatment.",
    "You will recognise how much a patient's life and circumstances matter to their problem, and how deciding together shapes the treatment plan.",
    "How did the patient take part in deciding their treatment plan last time?")
o36('3.6.e.iii', ['identify', 'facilitate'], 'identifying needs and arranging investigations', 'subject-skill',
    "Will identify the patient's needs and arrange specific clinical investigations or other referrals where needed.",
    "Graduates will identify patients' needs and arrange specific investigations or referrals as needed.",
    "You will be able to work out what a patient needs and arrange tests or referrals when they are called for.",
    "When did you last decide a patient needed an investigation, and how did you arrange it?")
o36('3.6.e.iv', ['conduct', 'include'], 'thorough, ongoing evaluation', 'subject-skill',
    "Will carry out a thorough, continuing evaluation of the patient, possibly including biomechanical, psychosocial, attitudinal, palpatory and clinical examination, as suits and respects the person's presentation.",
    "Graduates will evaluate patients thoroughly and continuously, using biomechanical, psychosocial, attitudinal, palpatory and clinical examination as the presentation warrants.",
    "You will examine each patient thoroughly and keep reassessing them, using physical, psychological, hands-on and clinical tests as fits their situation.",
    "How did you decide which parts of the examination to use with your last new patient?")
o36('3.6.e.v', ['generate', 'explain', 'aid'], 'hypotheses and the working diagnosis', 'subject-skill',
    "Will produce several hypotheses for the presenting complaint to support a treatment plan or onward referral, with an explanation of the working diagnosis the patient can follow.",
    "Graduates will generate several hypotheses for the complaint to inform a plan or referral, and explain the working diagnosis accessibly.",
    "You will be able to come up with several possible explanations for a patient's problem, use them to plan treatment or refer on, and explain your working diagnosis in words they understand.",
    "What were your competing hypotheses for a recent case, and how did you explain the working one to the patient?")
o36('3.6.e.vi', ['recognise', 'impact'], 'non-verbal cues, protected characteristics and socioeconomic status', 'subject-skill',
    "Will recognise the features and effects of non-verbal communication, and how protected characteristics and socioeconomic status may bear on the patient's health.",
    "Graduates will recognise what non-verbal communication shows and how protected characteristics and socioeconomic status can affect health.",
    "You will notice what patients communicate without words and understand how things like their background, identity and income can affect their health.",
    "How might a patient's circumstances or identity have shaped their health and how they spoke to you?")
o36('3.6.e.vii', ['generate'], 'records of the evaluation', 'subject-skill',
    "Will produce full, accurate records of what the patient evaluation found.",
    "Graduates will generate complete, accurate records of evaluation outcomes.",
    "You will keep full and accurate records of what you find when you assess a patient.",
    "Would another practitioner reading your notes understand exactly what you found and why?")

# f) palpation
o36('3.6.f.i', [], 'the therapeutic value of touch and palpation', 'subject-skill',
    "Will appraise critically what touch and palpation contribute to diagnosis and treatment.",
    "Graduates will critically appraise the therapeutic value of touch and palpation in diagnosis and treatment.",
    "You will be able to judge critically what touch and palpation add to diagnosing and treating patients.",
    "What do you think palpation added to your diagnosis in a recent case, and what could it not tell you?")
o36('3.6.f.ii', ['ensure'], 'talking with patients about touch and consent', 'subject-skill',
    "Will be aware that one must keep talking with the patient about touch and palpation, to confirm findings and to secure consent and comfort.",
    "Graduates will be aware of the need for continuing dialogue with patients about touch and palpation, to confirm findings and keep consent and comfort.",
    "You will keep talking with patients about how and why you are touching them, to check your findings and make sure they consent and are comfortable.",
    "How do you check, during treatment, that a patient is still comfortable and consenting?")
o36('3.6.f.iii', ['recognise', 'understand'], 'critical palpation of tissues', 'subject-skill',
    "Will use criticality to recognise and understand tissue structure and function when palpating during evaluation.",
    "Graduates will apply criticality in palpation to recognise and understand tissue structure and function during evaluation.",
    "You will think critically about what you feel when you palpate, recognising how the tissues are built and working.",
    "How confident are you that what you feel matches what is there, and how do you check?")
o36('3.6.f.iv', ['provide'], 'palpation as diagnostic and therapeutic technique', 'subject-skill',
    "Will use palpation both to help diagnosis and as a therapeutic technique that reassures patients.",
    "Graduates will use palpation as a complementary diagnostic tool and as a reassuring therapeutic technique.",
    "You will use palpation both to help work out what is wrong and as a way of treating and reassuring patients.",
    "When has palpation reassured a patient as well as informing you?")
o36('3.6.f.v', ['demonstrate', 'using', 'recognise'], 'sensitive palpation and its limits', 'subject-skill',
    "Will show sensitivity in palpation, knowing its limits and seeing continuing chances to develop the skill.",
    "Graduates will palpate with sensitivity, aware of its limits and of continuing ways to develop the skill.",
    "You will palpate with sensitivity, know the limits of what it tells you and keep looking for ways to improve.",
    "Where are the limits of your palpation skill at the moment, and how are you working on them?")
o36('3.6.f.vi', ['make'], 'recording palpatory findings', 'subject-skill',
    "Will record palpatory findings accurately, consistently and suitably alongside objective measures and outcomes reported by patients.",
    "Graduates will record palpatory findings accurately and consistently, alongside objective measures and patient-reported outcomes.",
    "You will record what you find by palpation accurately and consistently, next to objective measures and what the patient reports.",
    "How do you record a palpatory finding so that you can compare it next session?")
o36('3.6.f.vii', ['use', 'inform'], 'palpation combined with other methods', 'subject-skill',
    "Will combine palpation with other evaluation methods to shape a working diagnostic hypothesis and a continuing treatment plan.",
    "Graduates will use palpation with other assessment methods to inform a working diagnosis and ongoing plan.",
    "You will combine palpation with other ways of assessing a patient to form a working diagnosis and plan.",
    "How did your palpation findings fit, or clash with, the rest of your assessment?")

# g) planning, justifying and monitoring treatment
o36('3.6.g.i', ['perform', 'gathered'], 'analysing history and evaluation', 'subject-skill',
    "Will analyse and reflect in detail on what history taking and evaluation have produced.",
    "Graduates will analyse and reflect in detail on information from history taking and evaluation.",
    "You will analyse and reflect carefully on what you learned from the case history and examination.",
    "What did reflecting on your notes after the session change about your view of the case?")
o36('3.6.g.ii', ['generate', 'justify'], 'hypotheses on the cause of the complaint', 'subject-skill',
    "Will generate and justify a set of hypotheses about the cause of the presenting complaint.",
    "Graduates will generate and justify hypotheses for the aetiology of the presenting complaint.",
    "You will be able to put forward and justify possible causes for the patient's problem.",
    "Which cause did you rank first for a recent complaint, and what evidence supported it?")
o36('3.6.g.iii', ['establish', 'inform', 'discuss'], 'telling patients or guardians about findings', 'subject-skill',
    "Will work out how to tell the patient, or a person with parental responsibility or guardianship, about findings and talk through possible courses of action.",
    "Graduates will establish how to share findings with the patient or a parent or guardian and discuss the options.",
    "You will know how to explain your findings to a patient, or to a parent or guardian, and talk through the options.",
    "How would you explain your findings and options to the parent of a young patient?")
o36('3.6.g.iv', ['consider', 'includes'], 'shared, reasoned choice of action', 'subject-skill',
    "Will weigh suitable courses of action through rational, shared decision-making that critically considers the limits of their own competence and the likely effects of treatment.",
    "Graduates will consider options through rational, shared decision-making, critically weighing their own limits of competence and treatment's likely effects.",
    "You will weigh up options with the patient in a reasoned way, thinking critically about the limits of your own competence and what treatment is likely to do.",
    "When did the limits of your competence shape the option you and a patient chose?")
o36('3.6.g.v', ['consent', 'make'], 'referral for investigation with consent', 'subject-skill',
    "Will, with consent from the patient or someone who can consent for them, refer to other health professionals for further investigation where needed.",
    "Graduates will refer patients to other health professionals for further investigation when needed, with proper consent.",
    "You will refer patients to other health professionals for further tests when needed, with their consent or that of someone who can consent for them.",
    "How do you gain consent for a referral, and what do you do if the patient declines?")
o36('3.6.g.vi', ['formulate', 'includes', 'monitoring'], 'treatment plan, prognosis and monitoring', 'subject-skill',
    "Will draw up a treatment plan and prognosis that tracks the effect of treatment during and after each session across the planned course of care.",
    "Graduates will formulate a plan and prognosis that monitors treatment effects during and after application over the planned course.",
    "You will draw up a treatment plan and prognosis and keep checking how treatment is working, during and after each session.",
    "How did you decide on the prognosis you gave, and how will you know if treatment is on track?")
o36('3.6.g.vii', ['identify', 'reflect', 'plan', 'take'], 'obstacles to progress', 'subject-skill',
    "Will identify and reflect on what is holding back progress and plan and act on it.",
    "Graduates will identify and reflect on obstacles to progress and plan and take suitable action.",
    "You will spot and think about what is getting in the way of a patient's progress, then plan and act on it.",
    "What has slowed a patient's progress recently, and what did you change?")

# h) conducting treatment and patient management
o36('3.6.h.i', ['demonstrate', 'select', 'informed'], 'choosing among technical approaches', 'subject-skill',
    "Will show awareness of, and the ability to choose from, the wide range of direct and indirect osteopathic techniques to suit the patient, guided by the best evidence available.",
    "Graduates will demonstrate knowledge of, and choice among, the full range of direct and indirect techniques, matched to the patient and guided by best evidence.",
    "You will know the wide range of direct and indirect osteopathic techniques and be able to choose the right ones for each patient, guided by the best evidence.",
    "Why did you choose a direct or an indirect approach with your last patient?")
o36('3.6.h.ii', ['demonstrate', 'developed', 'considering'], 'patient management agreed with the patient', 'subject-skill',
    "Will show awareness and use of a range of management approaches agreed with the patient, taking account of their preferences and needs.",
    "Graduates will demonstrate a range of patient management approaches developed with the patient and responsive to their preferences and needs.",
    "You will use a range of ways of managing a patient's care, worked out with them and shaped by what they need and prefer.",
    "How did a patient's preferences change the management approach you agreed?")
o36('3.6.h.iii', ['rationalise'], 'indications and contraindications', 'subject-skill',
    "Will reason through the indications and contraindications for specific techniques or their modification.",
    "Graduates will rationalise indications and contraindications for specific techniques and their adaptations.",
    "You will be able to explain when a particular technique, or a changed version of it, is or is not suitable.",
    "What made a technique unsuitable for a patient you saw, and what did you do instead?")
o36('3.6.h.iv', ['adapt', 'justify', 'amend'], 'adapting approaches to feedback', 'subject-skill',
    "Will adapt osteopathic approaches and justify or change how they are used in response to the patient's feedback, as person-centred care.",
    "Graduates will adapt approaches and justify or amend their use in response to patient feedback, as person-centred intervention.",
    "You will adjust your approach in response to how the patient reacts, and be able to explain why.",
    "When did a patient's feedback make you change a technique mid-treatment?")

# i) evaluation of post-treatment progress and change
o36('3.6.i.i', ['monitor', 'recognise', 'record', 'initiate'], 'adverse reactions to treatment', 'subject-skill',
    "Will watch for spontaneous changes so as to spot and record adverse reactions to treatment, and respond suitably, referring on where needed.",
    "Graduates will monitor for and record adverse reactions to treatment and respond suitably, including by referral.",
    "You will watch for and record any unwanted reactions to treatment and respond properly, including referring the patient on if needed.",
    "What would you do if a patient reported feeling worse after treatment?")
o36('3.6.i.ii', ['maintain'], 'an open mind about outcomes', 'subject-skill',
    "Will keep an open, enquiring mind about the results of treatment.",
    "Graduates will maintain an open-minded, enquiring stance towards treatment outcomes.",
    "You will stay open-minded and curious about how your treatments turn out.",
    "When did an outcome surprise you, and what did you learn from it?")
o36('3.6.i.iii', ['record'], 'recording evaluation findings', 'subject-skill',
    "Will write down evaluation findings and what they mean accurately, legibly and accessibly in each patient's notes.",
    "Graduates will write evaluation findings and what they mean into case notes accurately, legibly and accessibly.",
    "You will write up what you found and what you think it means clearly and accurately in each patient's notes.",
    "Could a colleague act safely on your notes if you were absent?")
o36('3.6.i.iv', ['gather', 'organise'], "outcome data for an individual patient", 'subject-skill',
    "Will collect and organise a full range of data, outcome measures and evidence of both kinds on how an individual patient responds to treatment.",
    "Graduates will gather and organise qualitative and quantitative data, outcome measures and evidence on a patient's response to treatment.",
    "You will collect and organise numbers, measures and patients' own accounts to show how someone is responding to treatment.",
    "Which outcome measures do you use to show a patient's progress?")

# j) advice and support for healthy living
o36('3.6.j.i', ['operate'], 'health education and health promotion', 'understanding',
    "Will work with a critical grasp of the main ideas behind health education and promotion and how they are organised in the UK and abroad.",
    "Graduates will work with a critical appreciation of the concepts and organisation of health education and promotion at home and abroad.",
    "You will understand critically how health education and health promotion work, in the UK and elsewhere.",
    "How does what you advise patients fit with national health promotion messages?")
o36('3.6.j.ii', ['helping', 'make'], 'social and cultural factors in health choices', 'understanding',
    "Will understand how far psychosocial, cultural and socioeconomic factors matter in helping patients make informed choices about looking after their health.",
    "Graduates will understand the bearing of psychosocial, cultural and socioeconomic factors on patients' informed choices about their own health maintenance.",
    "You will understand how people's circumstances, culture and income affect the choices they make about their health, and use this to help them choose well.",
    "What got in the way of a patient following your advice, and how could you have helped?")
o36('3.6.j.iii', ['work', 'identify', 'include'], 'self-care planned with the patient', 'subject-skill',
    "Will work with the patient to agree self-care, which may cover diet, exercise and changes to lifestyle.",
    "Graduates will work in partnership with patients to identify self-care, such as dietary advice, exercise and lifestyle change.",
    "You will work with patients to agree what they can do for themselves, such as diet, exercise and changes to daily life.",
    "What self-care did you agree with a patient, and how did you check it suited them?")
o36('3.6.j.iv', ['offer'], 'advice on local health-promoting activity', 'subject-skill',
    "Will give realistic advice on where to find local health-promoting activities and how to use them well, in keeping with community, cultural and ethnic values.",
    "Graduates will offer realistic advice on local health-promoting activities that respects community, cultural and ethnic values.",
    "You will be able to point patients to realistic local activities that support their health, in ways that respect their community and culture.",
    "What local activities could you recommend to a patient, and would they fit that patient's life?")
o36('3.6.j.v', ['care', 'follow', 'manage'], 'own health and infection control', 'generic-skill',
    "Will look after their own health and well-being and carefully follow the procedures for managing communicable disease.",
    "Graduates will care for their own health and follow due diligence and procedures for communicable disease.",
    "You will look after your own health and follow infection-control procedures carefully.",
    "What infection-control steps do you take between patients?")
o36('3.6.j.vi', ['identify', 'referring'], 'benefits and limits of referral', 'subject-skill',
    "Will identify what referring a patient to other practitioners or services could gain and where it falls short.",
    "Graduates will identify the potential benefits and limits of referring patients to other practitioners or services.",
    "You will be able to weigh up what a patient could gain from being referred elsewhere, and what the drawbacks might be.",
    "For a patient you referred, what did you expect them to gain and what were the risks?")

# k) personal and professional skills development
o36('3.6.k.i', ['be committed'], 'commitment to lifelong learning', 'generic-skill',
    "Will be committed to learning throughout life, building skills and knowledge through reflection and active approaches.",
    "Graduates will commit to lifelong learning, gaining skills and knowledge through reflective and active approaches.",
    "You will be committed to learning throughout your career, using reflection and active practice to keep building your skills and knowledge.",
    "What have you learned recently outside the set curriculum, and how did you go about it?")
o36('3.6.k.ii', ['deliver'], 'awareness of what safe care demands', 'subject-skill',
    "Will be critically aware of the practical skill and clinical knowledge needed to give the expected standard of care.",
    "Graduates will be critically aware of the level of practical skill and clinical knowledge the expected standards of care require.",
    "You will know, critically, what level of practical skill and clinical knowledge good care demands of you.",
    "Where does your current skill fall short of what safe care needs, and what is your plan?")
o36('3.6.k.iii', ['reflect', 'plan', 'enact'], 'self-directed development', 'generic-skill',
    "Will be able to weigh up their own strengths and weaknesses, personal and professional, so as to plan and carry out continuing self-directed development and learning.",
    "Graduates will reflect on their strengths and limits and plan and carry out ongoing self-directed development.",
    "You will be able to reflect on your strengths and weaknesses, plan how to develop and follow your plan through.",
    "What is the next thing you want to develop, and how will you know you have?")
o36('3.6.k.iv', ['record', 'evidenced', 'demonstrate'], 'a reflective portfolio for CPD', 'subject-skill',
    "Will be able to record reflection on clinical practice in a professional portfolio, enough to show continuing professional development to the statutory regulator.",
    "Graduates will record reflective activity on clinical practice in a portfolio that evidences CPD for the statutory regulator.",
    "You will be able to record your reflections on clinical practice in a portfolio that shows your professional development to the regulator.",
    "What entry from your portfolio best shows your development this year?")
o36('3.6.k.v', ['informs', 'guides', 'contributes'], 'critical problem-solving in clinical reasoning', 'generic-skill',
    "Will show critical problem-solving skill at a level that guides the reading of clinical and other data and supports sound clinical reasoning and decisions.",
    "Graduates will evidence critical problem-solving that informs interpretation of clinical and other data and supports clinical reasoning and decisions.",
    "You will be able to solve problems critically, so that you read clinical information well and reason soundly about what to do.",
    "Walk me through how you solved a puzzling case: where did your reasoning change direction?")
o36('3.6.k.vi', ['facilitating', 'enables'], 'peer review and respectful feedback', 'generic-skill',
    "Will show engagement in peer review, giving respectful feedback and discussion that lets colleagues work together for their own and the profession's development.",
    "Graduates will evidence peer review and respectful feedback that supports collaborative group work for individual and professional development.",
    "You will take part in peer review, giving and receiving feedback respectfully so that you and your colleagues improve together.",
    "What feedback from a peer changed how you practise?")
o36('3.6.k.vii', ['maintain'], 'self-care and self-awareness for safe care', 'generic-skill',
    "Will have the self-care and self-awareness to keep giving patients an acceptable standard of care consistently.",
    "Graduates will show self-care and self-awareness enough to sustain an acceptable standard of patient care.",
    "You will look after yourself and know yourself well enough to keep your care of patients at a good standard.",
    "How do you notice when tiredness or stress might affect your care?")
o36('3.6.k.viii', ['comply', 'maintain'], 'continuing fitness to practise', 'subject-skill',
    "Will have the attitudes and skills needed to meet continuing fitness to practise requirements in full and keep their registration.",
    "Graduates will have the attitudes and skills to comply fully with continuing fitness to practise requirements and stay registered.",
    "You will have the attitudes and skills to keep meeting fitness to practise requirements, so you can stay on the register.",
    "What would put your fitness to practise at risk, and how would you guard against it?")
o36('3.6.k.ix', ['contribute', 'understand', 'support'], 'research and scholarship', 'generic-skill',
    "Will be able to contribute to or understand research and other scholarship in support of personal and professional growth.",
    "Graduates will contribute to, or understand, research and scholarly activity that supports their personal and professional development.",
    "You will be able to take part in, or make sense of, research and other scholarly work to help you grow personally and professionally.",
    "How has a piece of research you took part in or read shaped your practice?")

# l) professional identity, accountability, ethics and responsibilities
o36('3.6.l.i', ['understand', 'authorised'], 'statutory regulation', 'understanding',
    "Will understand what statutory regulation, as authorised by Parliament, is and why it matters.",
    "Graduates will understand the concept and importance of statutory regulation of the profession.",
    "You will understand what it means for your profession to be regulated by law, and why that matters.",
    "Why do you think osteopathy is regulated by law, and what does that mean for you?")
o36('3.6.l.ii', ['abide', 'outlined', 'issued'], 'professional standards and guidance', 'subject-skill',
    "Will keep to the professional standards in the OPS and the other guidance from the General Osteopathic Council and other relevant bodies.",
    "Graduates will abide by the OPS and other guidance from the GOsC and other appropriate bodies.",
    "You will follow the regulator's professional standards and other guidance for osteopaths.",
    "Which part of the professional standards do you find hardest to apply in practice?")
o36('3.6.l.iii', ['practise', 'includes'], 'safe, competent and lawful practice', 'subject-skill',
    "Will practise safely, competently and effectively within the law, for example complying with legislation on consent, safeguarding, equality, diversity and inclusion, data protection and health and safety.",
    "Graduates will practise safely, competently and effectively within the law, including consent, safeguarding, equality, data protection and health and safety legislation.",
    "You will practise safely, competently and effectively within the law, including the rules on consent, safeguarding, equality, data protection and health and safety.",
    "Which legal duty do you feel least sure about, and how could you check it?")
o36('3.6.l.iv', ['act', 'prevent', 'include'], 'acting to prevent harm', 'subject-skill',
    "Will act promptly to prevent harm, whether by managing the situation alone, consulting a colleague or reporting to a suitable authority; acting where patient safety may be at risk covers candour with patients, safeguarding law, colleagues putting patients at risk, practitioner health and reporting conduct or competence to the regulator.",
    "Graduates will act quickly to prevent harm, alone, with a colleague or by reporting, covering candour, safeguarding, reports to the regulator and concerns about colleagues or their own health.",
    "You will act quickly to prevent harm: dealing with it yourself, talking to a colleague or reporting it, including being open with patients, safeguarding, raising concerns about colleagues or your own health and reporting to the regulator.",
    "If you saw a colleague putting a patient at risk, what would you do first?")
o36('3.6.l.v', ['respect', 'uphold'], 'dignity, autonomy and confidentiality', 'subject-skill',
    "Will respect and protect patients' dignity, autonomy and confidentiality.",
    "Graduates will respect and uphold patient dignity, autonomy and confidentiality.",
    "You will respect and protect each patient's dignity, independence and privacy.",
    "How do you protect a patient's dignity during examination?")
o36('3.6.l.vi', ['disclose', 'justify'], 'disclosing and justifying actions', 'subject-skill',
    "Will be open about their actions to others and justify them when appropriate.",
    "Graduates will disclose and justify their actions to others when appropriate.",
    "You will be open about what you have done and be able to explain why, when that is called for.",
    "When have you had to explain a clinical decision to someone else?")
o36('3.6.l.vii', ['take', 'maintaining', 'uphold'], 'boundaries, conduct and integrity', 'subject-skill',
    "Will take responsibility for keeping professional boundaries and maintain high personal and professional conduct and the profession's integrity.",
    "Graduates will take responsibility for professional boundaries and uphold high standards of conduct and the profession's integrity.",
    "You will take responsibility for keeping professional boundaries and for behaving well, personally and professionally, so the profession can be trusted.",
    "What does professional conduct outside clinic mean for you?")

# m) intra- and inter-professional collaboration
o36('3.6.m.i', [], "healthcare delivery and osteopathy's place in it", 'understanding',
    "Will critically understand how healthcare is delivered in the UK and abroad and what osteopathy contributes, as an Allied Health Profession in NHS England and as primary healthcare.",
    "Graduates will critically understand UK and overseas healthcare delivery and osteopathy's contribution, as an Allied Health Profession in NHS England and as primary care.",
    "You will understand critically how healthcare is organised in the UK and elsewhere, and where osteopathy fits, including as an allied health profession and in primary care.",
    "Where does osteopathy fit in the care pathway for back pain in your area?")
o36('3.6.m.ii', ['relate'], 'claims of other health professions', 'understanding',
    "Will critically understand what a range of conventional and non-conventional health professions claim and how this relates to osteopathic practice.",
    "Graduates will critically understand the claims of conventional and non-conventional health professions and their relation to osteopathy.",
    "You will understand critically what other health professions, mainstream and not, claim to do and how that relates to osteopathy.",
    "How do the claims of a neighbouring profession compare with what osteopathy can show?")
o36('3.6.m.iii', ['demonstrate'], "evaluating osteopathy's claims", 'subject-skill',
    "Will show critical evaluation of what osteopathic practice currently claims, in the UK and abroad.",
    "Graduates will demonstrate critical evaluation of current claims made for osteopathic practice at home and abroad.",
    "You will be able to judge critically what osteopathy currently claims to achieve, in the UK and elsewhere.",
    "Which claim made for osteopathy would you want stronger evidence for?")

# n) operating an efficient and effective practice environment
o36('3.6.n.i', ['understand'], 'financial and practice management within the law', 'understanding',
    "Will understand the financial and operational detail of managing a practice within legal and ethical requirements, including health and safety, employment law and other relevant guidance or law.",
    "Graduates will understand financial and operational practice management within legal and ethical requirements, including health and safety and employment law.",
    "You will understand the money and day-to-day running of a practice within the law and ethics, including health and safety and employment rules.",
    "What would you need to have in place, legally and financially, before opening your own clinic?")
o36('3.6.n.ii', ['understand', 'contribute'], 'audit and planning', 'understanding',
    "Will understand audit's part in checking the quality of practice and be able to help produce operational and strategic plans.",
    "Graduates will understand audit's role in monitoring practice quality and contribute to operational and strategic planning.",
    "You will understand how audit checks the quality of a practice and be able to help plan how a practice runs and develops.",
    "What would you audit first in a clinic you worked in, and why?")
o36('3.6.n.iii', ['maintain'], 'compliant patient records', 'subject-skill',
    "Will keep patient records and information in line with what law and ethics require on confidentiality and peer support.",
    "Graduates will maintain records and information that meet the legal and ethical duties of confidentiality and of peer support.",
    "You will keep patient records and information in a way that meets legal and ethical rules on confidentiality.",
    "How do you store and share patient records safely?")
o36('3.6.n.iv', ['generate'], 'contact with external agencies', 'generic-skill',
    "Will keep effective, high-standard contact with outside agencies, including referrals to health professionals in and beyond the NHS, insurers and public services.",
    "Graduates will generate effective, high-standard contact with external agencies, including referrals within and outside the NHS, insurers and public services.",
    "You will deal effectively and professionally with outside organisations, such as the NHS, other health professionals, insurers and public services.",
    "How would you write to a GP about a patient you were concerned about?")
o36('3.6.n.v', ['demonstrate', 'establish', 'prioritises'], 'business skills for a viable practice', 'generic-skill',
    "Will show knowledge of the business skills needed to set up a viable osteopathic business that puts patients before profit.",
    "Graduates will demonstrate the business knowledge needed to establish a viable practice that puts patients ahead of profit.",
    "You will know the business skills needed to set up a practice that works financially while putting patients before profit.",
    "How would you keep a new practice viable without letting income drive clinical decisions?")

# ---- 6.10 threshold standards (lead-in: "To be awarded an honours degree in Osteopathy, a student will have demonstrated:";
#      6.1 defines them as the minimum threshold for the honours award)
def t610(n, verbs, about, domain, para, prac, ben, near, fw, when, q):
    s('6.10.b%d' % n, type='threshold', rung='threshold', force='threshold', forceFrom='6.1', level='fheq:6',
      appliesTo='students awarded an honours degree in osteopathy', addressee='learner', verbs=verbs, about=about, domain=domain, award=HON,
      para=para, prac=prac, ben=ben,
      aaw=("Treat this as a threshold standard: the minimum the statement says a student will have demonstrated to be awarded an honours degree in osteopathy (6.1, 6.10), at FHEQ level 6 (" + about + "). "
           "Cite it as " + CITE + "6.10, bullet " + str(n) + ". Do not describe it as typical achievement or as the regulator's requirement: 6.2 says most students do significantly better, judged against Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd). "
           "Set it beside the outcomes " + near + " and the level 6 descriptor " + fw + " (spine:6)."),
      aad=("Raise it when " + when + ". With a student, say in plain second-person words that this is the floor for the award, not the target; with a programme team, frame it as the minimum every route through assessment must secure. "
           "Ask: " + q + " Do not quote the bullet at length or present the higher classification descriptions as the minimum."))

t610(1, ['interact', 'communicate'], 'interpersonal and communication skills', 'generic-skill',
     "Will have developed strong interpersonal and communication skills for dealing professionally, ethically and effectively, from an informed position, with diverse patients, peers and other health professionals; this is the minimum for the honours award.",
     "At threshold, graduates will have developed highly effective interpersonal and communication skills for professional, ethical dealings with diverse patients, peers and other health professionals.",
     "To reach the threshold for the award, you will have developed strong people and communication skills, so that you deal professionally, ethically and effectively with a wide range of patients, fellow students and other health professionals.",
     SID + '3.6.d.i and 3.6.d.ii', 'qaa/fheq-2024/4.15.b8', 'a student asks how well they need to communicate to pass, or a team sets communication assessment',
     "Where have you had to communicate with a patient or professional whose needs were unlike your own?")
t610(2, ['inform'], 'osteopathic philosophy and principles in decisions', 'understanding',
     "Will have shown a critical grasp of the philosophy, principles and concepts of osteopathy and how they can guide reasoned clinical decisions.",
     "At threshold, graduates will have shown critical understanding of osteopathy's philosophy and principles and how these can guide rational clinical decisions.",
     "To reach the threshold, you will understand the philosophy and principles of osteopathy critically and how they can guide sound clinical decisions.",
     SID + '3.6.b.i and 3.6.b.iv', 'qaa/fheq-2024/4.15.b1', 'osteopathic principles are being tied to clinical decisions',
     "Can you show how an osteopathic principle led you to a clinical decision you could defend?")
t610(3, ['underpin'], 'the sciences underpinning practice across the lifespan', 'knowledge',
     "Will have gained coherent, detailed knowledge and understanding of how the biological, physical and behavioural sciences behind osteopathy interrelate and apply clinically across a patient's life.",
     "At threshold, graduates will have coherent, detailed knowledge of the interplay of biological, physical and behavioural sciences that underpin practice, and of their clinical use across the lifespan.",
     "To reach the threshold, you will have a clear, detailed understanding of how the biological, physical and behavioural sciences behind osteopathy link together and apply to patients at every stage of life.",
     SID + '3.6.a.i to 3.6.a.iv', 'qaa/fheq-2024/4.15.b1', 'a team checks the science base of the course or a student asks how much science is enough',
     "How would you explain a patient's problem using more than one of the biological, physical and behavioural sciences?")
t610(4, ['undertake', 'assess', 'make', 'formulate', 'taking'], 'safe assessment, working diagnosis and shared planning', 'subject-skill',
     "Will have shown the ability to carry out a clinical and osteopathic assessment that lets them assess a patient safely and effectively, reach a working diagnosis and, with the patient through shared decisions, form a treatment plan that allows for physical, biopsychosocial, cultural, equality and diversity needs and the person's values, preferences and expectations.",
     "At threshold, graduates will be able to assess a patient safely and effectively, reach a working diagnosis and agree a treatment plan through shared decision-making that respects the person's physical, psychosocial, cultural and diversity needs and their values and preferences.",
     "To reach the threshold, you will be able to assess a patient safely and effectively, reach a working diagnosis and agree a treatment plan with them that takes account of their whole situation, values and wishes.",
     SID + '3.6.e.i to 3.6.e.v and 3.6.g.iv', 'qaa/fheq-2024/4.15.b6', 'a student prepares for a clinical assessment or a team designs one',
     "Talk me through how you reached a working diagnosis and agreed a plan with your last new patient.")
t610(5, ['using', 'draws', 'inform'], 'critical clinical reasoning with incomplete knowledge', 'subject-skill',
     "Will have shown a critical approach to clinical and osteopathic assessment, using problem-solving and clinical reasoning that draws on what they know, including where it may be incomplete, complex or unpredictable, to shape treatment and management plans.",
     "At threshold, graduates will assess critically, using problem-solving and clinical reasoning drawn from their knowledge, including incomplete, complex or unpredictable areas, to plan treatment and management.",
     "To reach the threshold, you will approach assessment critically, using problem-solving and clinical reasoning, even where what you know is incomplete or the picture is complex, to plan treatment.",
     SID + '3.6.g.i, 3.6.g.ii and 3.6.k.v', 'qaa/fheq-2024/4.15.b7', 'a student meets a case that does not fit what they were taught',
     "What did you do when your knowledge ran out in a recent case?")
t610(6, ['select', 'apply', 'justify', 'monitor', 'evaluate', 'guide', 'educate', 'support'], 'selecting, applying and evaluating treatment', 'subject-skill',
     "Will have shown the ability to choose critically, apply and justify osteopathic treatment suited to a patient's needs, to monitor and judge its effect over the treatment plan and to guide and educate the patient as needed to help progress.",
     "At threshold, graduates will critically select, apply and justify treatment for the individual, monitor and evaluate its effect across the plan and guide and educate the patient to support progress.",
     "To reach the threshold, you will be able to choose, carry out and justify treatment that suits each patient, check and judge how well it is working and guide and teach the patient to help them progress.",
     SID + '3.6.h.i to 3.6.h.iv and 3.6.i.i to 3.6.i.iv', 'qaa/fheq-2024/4.15.b6', 'treatment choice and monitoring are assessed or discussed',
     "How do you know whether the treatment you chose for a patient is working?")
t610(7, ['support', 'benefit'], 'supporting well-being across the lifespan, including long-term illness', 'understanding',
     "Will have shown they appreciate how osteopaths can support patients' well-being across the lifespan and as public health priorities change, including care that eases or supports well-being when a patient lives with lifelong illness or disability.",
     "At threshold, graduates will appreciate osteopathy's value for well-being over the lifespan and in changing public health contexts, including palliative and supportive care for lifelong illness or disability.",
     "To reach the threshold, you will appreciate how osteopathy can support people's well-being throughout life and as public health needs change, including helping people who live with long-term illness or disability.",
     SID + '3.6.j.i to 3.6.j.iv', 'qaa/fheq-2024/4.15.b1', 'a student wonders what osteopathy offers someone who will not get better',
     "What could you offer a patient whose condition is lifelong?")
t610(8, ['collaborate', 'ensure'], "osteopathy's distinctiveness for collaboration", 'understanding',
     "Will have shown understanding of what is distinctive about osteopathic treatment, so as to work well with other health professions when needed and secure the best outcomes for patients and populations.",
     "At threshold, graduates will understand osteopathy's distinctive approach well enough to collaborate effectively with other professions for the best patient and population outcomes.",
     "To reach the threshold, you will understand what makes osteopathy distinctive, so you can work well with other health professions for the best results for patients and communities.",
     SID + '3.6.m.i, 3.6.m.ii and 3.6.b.iii', 'qaa/fheq-2024/4.15.b8', 'working with other professions or referral pathways comes up',
     "How would you explain what osteopathy adds to a GP or physiotherapist you were working with?")
t610(9, ['seek'], 'knowing the limits of one\'s own competence', 'generic-skill',
     "Will have shown awareness of the limits of their own competence, skill, knowledge and experience in practice, education and research, and will seek development through CPD, mentoring and shadowing or refer the patient to another osteopath or health professional as fitting.",
     "At threshold, graduates will know the limits of their competence across practice, education and research and respond by seeking CPD, mentoring or shadowing, or by referring on.",
     "To reach the threshold, you will know the limits of your own skills, knowledge and experience, and respond by seeking more training, mentoring or shadowing, or by referring the patient to someone better placed.",
     SID + '3.6.k.ii, 3.6.j.vi and 3.4.b6', 'qaa/fheq-2024/4.15.b4', 'a student is unsure whether to treat or refer, or plans their next learning',
     "Where are the edges of your competence right now, and what do you do when a patient takes you there?")
t610(10, ['informs', 'monitors', 'develops', 'draws'], 'self-directed professional learning', 'generic-skill',
     "Will have shown understanding of, and commitment to, continuing self-directed professional learning that shapes practice, tracks and improves the quality of care and uses current advice and research.",
     "At threshold, graduates will show commitment to ongoing self-directed professional learning that informs practice, monitors and improves care quality and draws on current advice and research.",
     "To reach the threshold, you will be committed to directing your own learning throughout your career, using current advice and research to keep improving the care you give.",
     SID + '3.6.k.i, 3.6.k.iii and 3.6.k.iv', 'qaa/fheq-2024/4.15.b9.3', 'a student plans continuing development or a team designs reflective assessment',
     "What have you changed in your practice because of something you chose to learn?")
t610(11, ['support', 'evaluate'], 'evidence-informed practice', 'subject-skill',
     "Will have shown awareness and effective use of clinically relevant research, clinical experience and patient expectations to support and judge evidence-informed practice critically, for the development of practice standards and patients' care.",
     "At threshold, graduates will apply relevant research, clinical experience and patient expectations to support and critically evaluate evidence-informed practice.",
     "To reach the threshold, you will combine research, clinical experience and what patients expect to judge and improve the care you give, critically and on good evidence.",
     SID + '3.6.a.viii, 3.6.k.ix and 6.6', 'qaa/fheq-2024/4.15.b3.2', 'research use or evidence-informed practice is assessed or discussed',
     "How did research, your experience and the patient's wishes each shape a recent decision?")
t610(12, ['evaluate'], 'professional integrity, probity and candour', 'generic-skill',
     "Will have shown understanding and the ability to judge critically their own professional integrity, with attention to probity, respect, self-care and the duty of candour in practice.",
     "At threshold, graduates will critically evaluate their own professional integrity, attending to probity, respect, self-care and the duty of candour.",
     "To reach the threshold, you will be able to judge your own professional integrity critically, paying attention to honesty, respect, looking after yourself and being open when things go wrong.",
     SID + '3.6.l.vii, 3.6.c.iv and 3.6.c.vii', 'qaa/fheq-2024/4.15.b9.1', 'professional integrity, honesty or a mistake is discussed',
     "When did you last have to be open with a patient or tutor about something that went wrong?")
t610(13, ['make', 'drawing'], 'decisions in complex, unpredictable situations', 'generic-skill',
     "Will have shown they can make decisions in unfamiliar, complex and unpredictable professional settings, using leadership, resilience, commitment and accountability.",
     "At threshold, graduates will make decisions in unfamiliar, complex and unpredictable professional settings, showing leadership, resilience, commitment and accountability.",
     "To reach the threshold, you will be able to make decisions in situations that are new, complex or unpredictable, showing leadership, resilience, commitment and accountability.",
     SID + '3.6.c.iv and 3.6.n.iv', 'qaa/fheq-2024/4.15.b9.2 (and, for integrated master\'s, qaa/fheq-2024/4.17.b5)', 'a student faces an unfamiliar or uncertain clinical situation',
     "Describe a decision you made without all the information: what did you weigh, and who did you tell?")

# ---- links, themes and the variant's sections
GRADE = {}   # one rung only (threshold): no gradeOf links
TH = {'1.13': 'theme:edi', '1.14': 'theme:edi', '1.15': 'theme:edi', '1.16': 'theme:edi', '1.17': 'theme:edi', '1.18': 'theme:edi',
      '1.22': 'theme:accessibility', '1.24': 'theme:esd', '1.25': 'theme:esd',
      '1.27': 'theme:enterprise', '1.33': 'theme:enterprise', '1.34': 'theme:enterprise', '1.35': 'theme:enterprise'}

S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.7; 2.8; 6.9', note="bachelor's (Level 6); the descriptors are cited as the FHEQ's degree-level qualification descriptors"),
                  dict(id='fheq:7', role='cites', locator='D1, 2.8; 6.9', note="integrated master's and pre-registration master's (Level 7)"),
                  dict(id='fqheis:11', role='cites', locator='D1, 6.9', note='"Level 11 of the Scottish Credit and Qualifications Framework" on the FQHEIS'),
                  dict(id='fqheis:10', role='inferred', locator='not named; the FQHEIS honours level beside fheq:6 (std:doc:qaa-fheq-2024-framework, Table 1)', note='Part E')],
          crosswalks=[dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='shared-descriptor', basis='inferred: the statement names both at 6.9 but states no equivalence; the FHEQ document gives one descriptor for both (std:doc:qaa-fheq-2024-framework, 4.8, 4.17)'),
                      dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='inferred from std:doc:qaa-fheq-2024-framework, Table 1 (honours); the statement names no SCQF level 10 (Part E)')])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['front matter', '1.13', '1.14', '1.15', '1.16', '1.17', '1.18', '1.19', '3.6', '4.2', '4.4', '6.10']),
      dict(id='theme:accessibility', role='carries', carriedIn=['front matter', '1.20', '1.21', '1.22', '1.33']),
      dict(id='theme:esd', role='carries', carriedIn=['front matter', '1.23', '1.24', '1.25', '4.2']),
      dict(id='theme:enterprise', role='carries', carriedIn=['front matter', '1.26', '1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '1.35', '1.36', '1.37', '1.38', '1.39', '3.6'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-osteopathy-<previous year>-benchmarks (not yet ingested)', note='the text calls this the fifth edition and dates the third 2019, the second 2014 and the original 2007; the fourth is not dated: Part E'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='degree classification descriptions for achievement above the threshold (6.2)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework', note='degree-level qualification descriptors (2.7); Levels 6 and 7 (2.8, 6.9)'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='named at 2.7 and 6.9; SCQF Level 11 (6.9)'),
      dict(rel='refersTo', target='std:doc:qaa-advancehe-esd-2021-guidance', note='"the QAA and Advance HE guidance" on education for sustainable development (1.25)'),
      dict(rel='refersTo', target='GOsC Osteopathic Practice Standards (not yet ingested: Part E)', note='1.5, 3.2, 3.5, 3.6 l) ii, 4.1, 5.1 to 5.4, 6.4, 6.8'),
      dict(rel='refersTo', target='GOsC Graduate Outcomes and Standards for Education and Training, September 2022 (not yet ingested: Part E)', note='1.5, 2.1, 3.5, 4.1, 4.4, 6.8'),
      dict(rel='refersTo', target='QAA Quality Code for Higher Education and its Advice and Guidance (not yet ingested)', note='front matter; 2.3'),
      dict(rel='refersTo', target='CEN European Standard on Osteopathic Healthcare Provision (not ingested)', note='1.10'),
      dict(rel='refersTo', target='Office for Students sector-recognised standards (not ingested)', note='front matter; 6.9')]
S8 = dict(published='2024-04', lastReviewed='none-stated', reviewCycle='none-stated',
          consultation='an Advisory Group chaired from NCOR, with GOsC, QAA, the Osteopathic Alliance, the Institute of Osteopathy, the Council for Osteopathic Education Institutions and providers (D1, section 8)',
          replacedBy='none')

SB1 = [
    'A primary healthcare profession that diagnoses, manages, treats and prevents a range of disorders, and an Allied Health Profession in England (D1, 1.1, 1.3).',
    'Care centres on the person, not the condition, and supports the body\'s own capacity to keep and restore health, with biopsychosocial factors always in view (D1, 1.12, 6.3).',
    'Its methods combine person-centred tools, hands-on technique, palpation, rehabilitation exercise and self-help advice, with diagnosis built from case history and examination and guided by clinical reasoning (D1, 1.2, 1.12, 6.5).',
    'It is a regulated profession: only those registered with the General Osteopathic Council may practise or use the title, and graduates may practise autonomously from registration (D1, 1.5, 1.6).',
    'Training joins academic study with extensive supervised clinical work in teaching clinics, at least 1,000 hours (D1, 1.4, 2.4, 6.4).',
    'It is evidence-informed and self-critical, weighing research, clinical experience and patient expectations and appraising its own claims (D1, 1.9, 6.6, 3.6 d) iv, 3.6 m) iii).',
    'Most osteopaths are self-employed, so business, enterprise and practice management sit inside the curriculum (D1, 1.7, 1.26 to 1.39, 3.6 n)).',
]
SB2 = [
    dict(theme='theme:edi', inThisSubject='framed as a collective responsibility of an inclusive learning community that reaches past legal minimums: critical theory and decolonial perspectives across the curriculum, anticipatory design for each learning site (technique class, clinic, online), care for self and others and questions for reviewing a course; in practice, attention to protected characteristics, socioeconomic status and diverse patient groups (D1, 1.13 to 1.19, 3.6 e) vi, 4.4, 6.10)',
         statements=['1.13', '1.14', '1.15', '1.16', '1.17', '1.18', '3.6.e.vi', '3.6.l.iii', '6.10.b4']),
    dict(theme='theme:accessibility', inThisSubject='part-time and full-time modes, blended and recorded delivery and reasonable adjustments, always bounded by the regulation that protects patient safety in clinic (D1, 1.20 to 1.22); accessible communication with digital tools (D1, 1.33)',
         statements=['1.22', '1.33']),
    dict(theme='theme:esd', inThisSubject='whole-person training, critical study of the profession\'s structures and discourses, the eight UNESCO competencies modelled in facilities and curricula and personal and social responsibility for well-being (D1, 1.23 to 1.25); sustainable delivery of teaching (D1, 4.2)',
         statements=['1.24', '1.25', '4.2']),
    dict(theme='theme:enterprise', inThisSubject='named employability, enterprise and entrepreneurship education (EEE): most osteopaths are self-employed, so the entrepreneurial mindset, career planning, marketing, legal and financial skills, external speakers and clinic placements prepare graduates for private practice (D1, 1.26 to 1.39); a viable business that puts patients before profit (D1, 3.6 n) v)',
         statements=['1.27', '1.33', '1.34', '1.35', '3.6.n.v']),
]
SB3 = dict(
    areas=[dict(component='3.1', gloss='the broad curriculum: cognitive and perceptual learning, manual and palpatory skills, generic skills, problem-solving, reflective practice, ICT, practice management and leadership, research and critical reasoning'),
           dict(component='3.6', gloss='fourteen outcome groups from the knowledge base (a) to running a practice (n); also the stem of 83 statements'),
           dict(component='6.5', gloss='anatomy, biomechanics, physiology, pathology and behavioural sciences as the foundation for assessment and management')],
    practices=[dict(component='2.2', kind='teaching', gloss='evidence-based pedagogy; feed-forward feedback and self-assessment'),
               dict(component='2.4', kind='learning', gloss='technical skill integrated with closely supervised outpatient clinical work'),
               dict(component='4.3', kind='teaching', gloss='innovative, research-informed methods chosen by each institution'),
               dict(component='4.4', kind='learning', gloss='supervised clinical learning in institutional and satellite clinics across diverse patient groups'),
               dict(component='1.36', kind='assessment', gloss='assignments on contemporary practice, marketing and the law of private practice'),
               dict(component='1.38', kind='learning', gloss='supervised clinic placements as a bridge to an entrepreneurial mindset'),
               dict(component='5.3', kind='assessment', gloss='varied, valid and reliable tools; formative and summative assessment with peers, patients and external expertise')])
SB4 = dict(
    rungs=[dict(rung='threshold', leadIn='6.10', award=HON, items=13)],
    rungBases='6.1 defines the 6.10 list as the minimum threshold standards for an honours degree; 6.2 says most students perform significantly better and leaves the evidence of this to each provider with reference to Annex D. No typical or excellent lists.',
    outcomeLists=[dict(leadIn='3.4', gloss='six key characteristics a graduate can demonstrate', items=6, award=[HON, IM]),
                  dict(leadIn='3.6', gloss='83 outcomes in fourteen lettered groups, developed on successful completion', items=83, award=[HON, IM])],
    outcomes=[])
SB4A_FULL = []
SB5 = [
    dict(body='General Osteopathic Council (GOsC)', says='the statutory regulator: only its registrants may practise or use the title; it recognises qualifications (Recognised Qualification status, reviewed regularly), which must deliver its Osteopathic Practice Standards and align with its Graduate Outcomes and Standards for Education and Training; graduates and registrants must meet the OPS throughout their careers (D1, 1.5, 1.6, 2.1, 3.5, 3.6 l) ii, 4.1, 6.8, 6.9)',
         requirements='not yet ingested: the OPS and GO-SET (Part E; D3)'),
    dict(body='Professional Standards Authority', says='oversees the GOsC and nine other health regulators (D1, 1.5)', requirements='not-applicable-by-design: named only as the regulator\'s overseer'),
    dict(body='Privy Council', says='approves the qualifications the GOsC recognises (D1, 1.5)', requirements='not-applicable-by-design: approval role only'),
    dict(body='National Council for Osteopathic Research (NCOR)', says='works to strengthen the evidence base and research capacity of the profession (D1, 1.9); chairs the advisory group (D1, section 8)', requirements='not-applicable-by-design: sets no requirements on courses'),
    dict(body='National Institute for Health and Care Excellence (NICE)', says='its low back pain guideline (NG59) is among the independent assessments that include osteopathy (D1, 1.8; the text gives its older name)', requirements='not-applicable-by-design: clinical guidance, not a course requirement'),
    dict(body='European Committee for Standardisation (CEN)', says='publishes a European Standard on Osteopathic Healthcare Provision for countries without regulation (D1, 1.10)', requirements='not yet ingested (Part E)'),
]
SB6 = dict(
    themes=[dict(id='theme:edi', named='Equality, diversity and inclusion (front matter: equality, diversity, and inclusion)', carriedIn=['front matter', '1.13', '1.14', '1.15', '1.16', '1.17', '1.18', '1.19', '3.6', '4.2', '4.4', '6.10'],
                 statements=[SID + x for x in ('1.13', '1.14', '1.15', '1.16', '1.17', '1.18', '3.6.e.vi', '3.6.l.iii', '6.10.b4')]),
            dict(id='theme:accessibility', named='Accessibility (front matter: accessibility and the needs of disabled students)', carriedIn=['front matter', '1.20', '1.21', '1.22', '1.33'],
                 statements=[SID + '1.22', SID + '1.33']),
            dict(id='theme:esd', named='Education for Sustainable Development (ESD)', carriedIn=['front matter', '1.23', '1.24', '1.25', '4.2'],
                 statements=[SID + '1.24', SID + '1.25', SID + '4.2']),
            dict(id='theme:enterprise', named='Enterprise and entrepreneurship education (front matter: employability, entrepreneurship, and enterprise education; EEE at 1.29)', carriedIn=['front matter', '1.26', '1.27', '1.28', '1.29', '1.30', '1.31', '1.32', '1.33', '1.34', '1.35', '1.36', '1.37', '1.38', '1.39', '3.6'],
                 statements=[SID + x for x in ('1.27', '1.33', '1.34', '1.35', '3.6.n.v')])],
    frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.7', '2.8', '6.9']),
                dict(framework='scqf', levels=['fqheis:11'], citedIn=['2.7', '6.9']),
                dict(framework='other: Office for Students sector-recognised standards', levels=[], citedIn=['front matter', '6.9'])],
    bodies=[dict(body='General Osteopathic Council', citedIn=['1.5', '1.6', '2.1', '3.5', '3.6', '4.1', '6.8', '6.9']),
            dict(body='Professional Standards Authority', citedIn=['1.5']),
            dict(body='Privy Council', citedIn=['1.5']),
            dict(body='National Council for Osteopathic Research', citedIn=['1.9']),
            dict(body='National Institute for Health and Clinical Excellence (NICE)', citedIn=['1.8']),
            dict(body='European Committee for Standardisation (CEN)', citedIn=['1.10']),
            dict(body='PSRBs (generic)', citedIn=['front matter'])],
    sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies', citedIn=['6.2'], role='how each provider evidences achievement above the threshold'),
                     dict(document='std:doc:qaa-fheq-2024-framework', named='the degree-level qualification descriptors in the FHEQ; Qualifications Frameworks', citedIn=['2.7', '6.9'], role='the levels training reflects and the capabilities map to'),
                     dict(document='std:doc:qaa-fqheis-2024-framework', named='the Framework for Qualifications of Higher Education Institutions in Scotland', citedIn=['2.7', '6.9'], role='the Scottish framework, Level 11 named'),
                     dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='the QAA and Advance HE guidance', citedIn=['1.25'], role='more information on education for sustainable development'),
                     dict(document='QAA Quality Code for Higher Education and Advice and Guidance (not yet ingested: Part E)', named='Quality Code; Advice and Guidance', citedIn=['front matter', '2.3'], role='course design and progressive levels'),
                     dict(document="QAA Glossary (not ingested)", named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms')])

# ---- Part B: terms the statement defines in passing
B1 = [
    dict(slug='recognised-qualification', definition='a qualification the regulator recognises, with Privy Council approval, as leading to registration; it must deliver the OPS and is reviewed regularly (D1, 1.5, 6.8)', beneficiaryDefinition='a course the regulator has approved, which you need to complete before you can register', scopeNote='the regulator\'s term; abbreviated RQ', category='unknown', practices=['healthcare education']),
    dict(slug='osteopathic-practice-standards', definition='the regulator\'s professional standards, in four themes, that registrants must meet and courses must deliver (D1, 1.5, 6.4, 6.8)', beneficiaryDefinition='the standards you will have to meet as a registered osteopath', scopeNote='abbreviated OPS; a separate document, not ingested', category='unknown', practices=['healthcare education']),
    dict(slug='evidence-informed-practice', definition='practice drawing on three parts: clinical experience, research and patient expectations (D1, 6.6)', beneficiaryDefinition='practice that weighs research, your experience and what the patient wants', scopeNote='', category='unknown', practices=['healthcare']),
    dict(slug='employability-enterprise-entrepreneurship-education', definition='education for the behaviours, attributes and competencies of employed or self-employed practice (D1, 1.29 to 1.32)', beneficiaryDefinition='learning that prepares you for work, including running your own practice', scopeNote='abbreviated EEE', category='unknown', practices=['education']),
    dict(slug='anticipatory-design', definition='design of teaching and practice that plans ahead for the needs of each learning site and those it has served badly (D1, 1.17, 1.18)', beneficiaryDefinition='courses planned in advance so that everyone can take part', scopeNote='', category='unknown', practices=['education']),
]
B2A = [dict(concept='recognised-qualification', form='Recognised Qualification (RQ)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='osteopathic-practice-standards', form="Osteopathic Practice Standards (OPS)", lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='evidence-informed-practice', form='evidence-informed practice', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='employability-enterprise-entrepreneurship-education', form='employability, enterprise, and entrepreneurship education (EEE)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='anticipatory-design', form='anticipatory design', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = []; B5 = []

D3 = [dict(source='General Osteopathic Council, Osteopathic Practice Standards (current edition)', why='the standards every Recognised Qualification must deliver; cited throughout (1.5, 5.1, 6.8)'),
      dict(source='General Osteopathic Council, Graduate Outcomes and Standards for Education and Training (September 2022)', why='the regulator\'s graduate outcomes the 3.6 outcomes are designed to show (3.5, 6.8)'),
      dict(source='QAA, Subject Benchmark Statement: Osteopathy, previous edition', why='the edition this one supersedes; the text does not name or date it')]

E = [
    'Rungs: one rung only. 6.10 lists 13 threshold standards for the honours degree; 6.1 calls them the minimum threshold; 6.2 leaves higher achievement to each provider and Annex D (std:doc:qaa-fheq-2024-framework). No typical or excellent lists, so no gradeOf links (as Archaeology).',
    'Pattern: the threshold lead-in (6.10) is "To be awarded an honours degree in Osteopathy, a student will have demonstrated:"; force recorded as threshold, with forceFrom 6.1, which defines the list as the minimum.',
    'Pattern: two outcome lists outside the rungs: 3.4 (six key characteristics, lead-in "can demonstrate", recorded as will; for P3) and 3.6 (83 outcomes in fourteen lettered groups a) to n), lead-in "will have developed").',
    'Skeleton correction: 3.6 is flattened in the held text (lettered groups with roman-numbered items run into one paragraph). The skeleton cut it into 12 wrong items (3.6.b1 to 3.6.b12); this run cuts 83 items by find, with ids 3.6.<letter>.<roman> in the issuer\'s numbering. Placements are by the markers a) to n) and i to ix; all 83 texts are unique in the held text. For P3: the builder reads only numeric ids, so these 83 records sort after section 6 and show stem none and a blank sub-heading; their stem is 3.6 and their group heading is the letter\'s (a) to n)).',
    'Skeleton correction: 6.10.b7 crosses a page break; its span is extended by find to the end of the bullet, page number 22 included in source. 3.6 d) v and l) iv each hold an unnumbered dash list, kept inside the one record; l) iv crosses page break 17.',
    'Skeleton correction: paragraph spans trimmed by find to drop trailing page numbers and the flattened sub-headings that follow 1.22 ("Education for Sustainable Development (ESD)") and 1.25 ("Enterprise and entrepreneurship education"). Other sub-headings sit at the end of 1.4, 1.10, 1.12, 2.6, 3.3 and 6.9 (not statements).',
    'Awards: the statement covers pre-registration courses at bachelor\'s (Level 6) and integrated master\'s (Level 7), and names pre-registration master\'s (Level 7) at 2.8; the outcome lists are not split by award. Outcome records carry both awards at level fheq:6; the threshold list is for the honours degree (fheq:6). Whether integrated master\'s needs fheq:7 records is for P3. No master\'s column, so no .masters ids.',
    'Levels: 6.9 names SCQF "Level 11" on the FQHEIS but not SCQF 10, the honours level beside FHEQ 6. fqheis:10 and both crosswalks in S5 are inferred from std:doc:qaa-fheq-2024-framework (Table 1; 4.8 and 4.17). The CQFW is not named, though the statement applies in Wales.',
    'Force, outside the five: 1.6 ("it is critical that"; "requires") recorded as must; 1.18 and 1.24 ("requires") recorded as must; 6.8 ("required") recorded as must; 1.35 ("is recommended") recorded as describes; 6.6 ("are expected to") recorded as describes; 1.13 ("will need to"; "responsibility and duty") recorded as will. For Abbott.',
    'Force, mixed in one paragraph: 1.14 has should (foster) and must (acknowledge and counter), recorded as must; 1.5 has must and should, recorded as must; 2.3 has should with "essential" and "required", recorded as should; 2.5 has "it is important that" and should, recorded as should; 5.1 and 5.4 have should with a will or a plain condition, recorded as should.',
    'Plain-present provider norms, not statements (template open point 5): 1.4, 2.2, 2.4, 3.1 (the curriculum "include"s eight areas), 4.1, 4.3, 4.4 and 6.4 (courses integrate "at least 1,000 hours of supervised clinical practice"), 6.5, 6.7. 6.4 also says graduates "understand and can demonstrate" the OPS themes in plain present. For P3: 6.4\'s 1,000 hours is the one quantified course requirement in the text.',
    'Not statements: 1.12 bullets 2 to 7 (features of practice, descriptive; bullet 1 has should and is a statement); 1.19 (review questions); 1.28 (the entrepreneurial mindset defined); 1.30 to 1.32 ("can include"); 1.23, 1.29, 1.36, 1.39 (will in a descriptive or predictive sense); 6.1 (the rung definition, in SB4 rungBases); 6.9 (level mapping).',
    'Codes: HECoS 100243 osteopathy is stated by subject name. CAH02-06-06 (complementary and alternative medicine), CAH02-06 and CAH02 are inferred from HECoS\'s own mapping; the text calls osteopathy an Allied Health Profession (1.1) and never complementary or alternative. For P3.',
    'Themes: ESD skeleton hits at 1.22 (the flattened heading) and 6.4 ("sustainability and development of practice life", a business sense) are not ESD and are not cited. 4.2 ("sustainable and inclusive way") is cited for ESD and EDI. Accessibility at 1.33 ("accessibly") and EDI at 3.6, 4.4 and 6.10 are cited by what the paragraph says.',
    'Bodies: the GOsC\'s OPS and GO-SET (September 2022) are not ingested (D3). CEN\'s European Standard is not ingested. 1.8 names NICE by an older name ("National Institute for Health and Clinical Excellence").',
    'Shared documents: the Quality Code and its Advice and Guidance (front matter, 2.3) are not ingested. Legislation named (Osteopaths Act 1993 at 1.5; Equality Act 2010 at 1.13) is recorded only in the statements that carry it.',
    'Supersedes: the back matter calls this the fifth edition and dates the third (2019), the second (2014, by membership) and the original (2007); the fourth edition is not dated. The edition superseded is not named.',
    'Typos in the held text, left as held: "Versus Arthtritis" (1.16), "make decision" (6.10 b13), "ones\' own" (6.10 b12), "A bout" and "O steopathy" from extraction.',
    'Generic-skill records carry fheq:6, the level they refine (S5); their aaw points to the matching FHEQ 4.15 item and spine:6. For integrated master\'s, the 4.17 items are the counterpart (named at 6.10.b13 only).',
    'S9 commentary not researched in P1.',
]
