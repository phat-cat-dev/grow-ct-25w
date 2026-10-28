# bm_content.py: the judgement file for run 0107, QAA Subject Benchmark Statement: Forensic Science (March 2022). std, run agent.
# Read by tools/bm_build.py (brief BM-BRIEF.md 0.2.3; benchmark template 0.6.0-draft; run layer 0.7.0-draft).
# Every text field below is our own words; the issuer's words reach the document only through `source` (from each span).
HON = "bachelor's with honours"
MA = "master's"
IMA = "integrated master's"
BOTH = [HON, MA]
SID = 'qaa/forensic-science-2022/'

META = dict(
  run='0107', p1='2026-10-03 17:33',
  title='Subject Benchmark Statement Forensic Science',
  heading='Subject Benchmark Statement: Forensic Science (QAA, March 2022)',
  edition='March 2022', published='2022-03',
  status='current', supersedes='the earlier Forensic Science statement (the back matter lists a 2012 advisory group and calls this the second edition; the front matter names key changes from the previous statement)',
  subjects=[dict(scheme='hecos', code='100388', label='forensic science', basis='stated'),
            dict(scheme='cah', code='CAH07-04-02', label='forensic and archaeological sciences', basis='stated'),
            dict(scheme='cah', code='CAH07-04', label='general, applied and forensic sciences', basis='stated'),
            dict(scheme='hecos', code='100386', label='forensic biology', basis='stated'),
            dict(scheme='hecos', code='100385', label='computer forensics', basis='inferred'),
            dict(scheme='hecos', code='101222', label='crime scene investigation', basis='inferred')],
  awards=[HON, MA, IMA], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
  nations=['England', 'Wales', 'Scotland', 'Northern Ireland'],
  series='QAA Subject Benchmark Statements, the 2022 revisions with cross-cutting themes (second edition of this subject)',
  partsB='partial: no glossary in the document (it points to QAA\'s Glossary); terms it defines in its text',
  agentDefinition=("QAA's UK reference point for what a Forensic Science graduate should know, understand and be able to do at the end of an "
    "honours degree, and at master's and integrated master's level: course aims, outcome lists for knowledge and skills, and benchmark "
    "standards at three rungs (threshold, typical, excellent), each split into generic standards and area standards for scene "
    "investigation, laboratory analysis and digital forensics, with a separate master's list. Reach for it when designing, reviewing or "
    "describing a forensic science course or its outcomes. It is not a curriculum, not the Chartered Society of Forensic Sciences' "
    "accreditation standard and not a regulatory requirement."),
  summary=("Published by QAA in March 2022 with a foreword from the Forensic Science Regulator, the statement defines forensic science as "
    "science serving the law and organises the subject round three integrated components: scene investigation, laboratory analysis, and "
    "the interpretation, evaluation and presentation of evidence. It sets out course aims (honours and master's), distinctive features "
    "(accessibility, progression, flexibility, employer partnership, monitoring), content in the underpinning sciences, digital forensics "
    "and law, skills lists with master's additions, and benchmark standards at threshold (3rd), typical (2:2 or 2:1) and excellent (1st) "
    "for honours, plus one master's list. It carries the cross-cutting themes of equality, diversity and inclusion, accessibility, "
    "sustainability and enterprise; it cites the FHEQ and FQHEIS levels and Annex D, and names the Chartered Society of Forensic Sciences "
    "and the Forensic Science Regulator."),
  authority='reference: a sector reference point, not a regulatory requirement; in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of the quality requirements in Northern Ireland (D1, front matter: Relationship to legislation and regulation)')

S2 = dict(
  governs="what can be expected of a Forensic Science graduate at the end of an honours degree, a master's degree or an integrated master's degree, and the nature of courses in the subject, including the forensic parts of courses based in other subjects (D1, front matter: About this Statement; 1.1; 1.2)",
  awards=[HON, MA, IMA], levels=['fheq:6', 'fheq:7', 'fqheis:10', 'fqheis:11'],
  statedScope='"This Statement sets out academic standards for courses at bachelor\'s degree with honours and master\'s degree levels (including integrated master\'s) in Forensic Science." (D1, 1.1)',
  statedSubjects=[
    dict(name='Forensic Science', locator='(D1, title; 1.1)', kind='subject', codes=[dict(scheme='hecos', code='100388', label='forensic science'), dict(scheme='cah', code='CAH07-04-02', label='forensic and archaeological sciences')]),
    dict(name='Chemistry with Forensic Science', locator='(D1, 1.2)', kind='programme title', codes=[dict(scheme='hecos', code='100417', label='chemistry'), dict(scheme='hecos', code='100388', label='forensic science')]),
    dict(name='Forensic Biology', locator='(D1, 1.2)', kind='programme title', codes=[dict(scheme='hecos', code='100386', label='forensic biology')]),
    dict(name='digital forensics', locator='(D1, 1.9; 3.19; 4.1; 4.5)', kind='specialism', codes=[dict(scheme='hecos', code='100385', label='computer forensics')]),
    dict(name='scene investigation', locator='(D1, 1.14; 1.15; 3.11; 4.5)', kind='specialism', codes=[dict(scheme='hecos', code='101222', label='crime scene investigation')]),
    dict(name='laboratory analysis', locator='(D1, 1.14; 1.16; 3.12; 4.5)', kind='specialism', codes=[]),
    dict(name='joint honours', locator='(D1, 2.6)', kind='programme title', codes=[dict(scheme='hecos', code='100388', label='forensic science')])])

SECTIONS = {'1': 'Context and purposes of a Forensic Science degree', '2': 'Distinctive features of a Forensic Science degree',
            '3': 'Content, structure and delivery', '4': 'Benchmark standards'}
SUB = [('1.3', '1.4', 'Context'), ('1.5', '1.8', 'Purposes of a Forensic Science degree'), ('1.9', '1.18', 'Characteristics of a Forensic Science degree'),
       ('1.19', '1.22', 'Equality, diversity and inclusion (EDI)'), ('1.23', '1.24', 'Sustainability'), ('1.25', '1.27', 'Enterprise and entrepreneurship'),
       ('2.2', '2.3', 'Accessibility'), ('2.4', '2.8', 'Progression'), ('2.9', '2.10', 'Flexibility'), ('2.11', '2.13', 'Partnership and employer engagement'),
       ('2.14', '2.18', 'Monitoring and review'), ('3.3', '3.7', 'Teaching and learning'), ('3.8', '3.20', 'Knowledge and understanding'),
       ('3.21', '3.21', 'Skills and employability'), ('3.22', '3.23', 'Scientific, laboratory and research skills'), ('3.24', '3.25', 'Forensic science skills'),
       ('3.26', '3.27', 'Generic graduate skills'), ('3.28', '3.28', 'Ethical behaviour'), ('3.29', '3.33', 'Assessment'),
       ('4.1', '4.3', 'Introduction'), ('4.4', '4.5', 'Threshold level (3rd class)'), ('4.6', '4.7', 'Typical level (2:2 or 2:1)'),
       ('4.8', '4.9', 'Excellent level (1st class)'), ('4.10', '4.11', "Master's degrees (including integrated master's)")]
# ---- spans: exact texts where the skeleton cut carried a flattened heading, a page number or a list (run 0107)
FIND = {
  '1.4': "1.4 Over the past 20 years there has been an increasing realisation that all forensic testimony presented to the court needs to be underpinned by sound, peer-reviewed science (National Research Council, 2009; President's Council of Advisors on Science and Technology, 2016; House of Lords Science and Technology Select Committee, 2019). Over this same period, many universities both in the UK and in other countries have developed and delivered degree courses encompassing forensic science and its associated sub- disciplines. Such courses have appealed strongly to potential students looking for a science degree within a motivating and purposeful context and have provided employers, working within the criminal justice system and beyond, with a pool of potential graduate employees. To ensure degrees are fit for purpose within the professional context, the Educational Accreditation scheme set up by the Chartered Society of Forensic Sciences continues to support most higher education providers in the UK and some overseas with ongoing accreditation and surveillance activities. This scheme ensures productive close interaction between the profession, higher education providers and their students. Furthermore, the importance of equity of opportunity through inclusive practices is established within the field and should be supported and promoted by higher education institutions through accessible programmes and positive actions.",
  '1.8': "1.8 All degree courses should accord with the qualification descriptions in national qualification frameworks. QAA has published additional guidance on different kinds of master's degrees , which may also be helpful to providers.",
  '1.17': "1.17 Interpretation and evaluation of evidence involves the reliable recording of evidential materials, experimentation, analysis and interpretation within the context of the case and data management. It also requires the clear and impartial presentation (written and oral) of the forensic examination and findings with an understanding of the significance of its outcomes within a legal context, including uncertainties. A report or witness statement must be robust, transparent, logical and unbiased and should distinguish between factual and expert reporting. It should be noted that admissible 'evidence' can only be decided by the courts and therefore, up to that point in the process, the items and findings are only 'potential evidence'. For the purpose of this document, the term evidence implies both evidence and potential evidence.",
  '1.19': "1.19 This Subject Benchmark Statement is to be interpreted in the context of the Equality Act 2010 and seeks to embed equality, diversity and inclusivity across all educational practices within a Forensic Science course. The Equality Duty (section 149 of the Act) supports good decision-making by ensuring public bodies consider how different people will be affected by their activities, helping them to deliver policies and services which are efficient and effective, accessible to all and which meet different people's needs. In this section we pose some reflective questions, and set out aims and objectives which might help when reviewing and reflecting on course provision, to ensure everyone is treated equally with dignity and respect. All staff and students within Forensic Science courses have a responsibility to ensure equal opportunity for all regardless of background, ability, culture, gender or identity.",
  '1.23': "1.23 Education for Sustainable Development (ESD) is defined as 'the process of creating curriculum structures and subject-relevant content to support sustainable development' by aligning teaching practices, where possible, to the UN Sustainable Development Goals. ESD should be embedded in teaching and learning practices to ensure students are aware of social, economic and ecological well-being factors, now and in the future. ESD can be used to empower students and staff to change the way they think and work towards a sustainable future using transdisciplinary, holistic and values-driven relevant material. For Forensic Science students this includes developing practices for lifelong learning through engagement with continual professional development to ensure their future practitioner skills and knowledge base are current. Staff should be equipped with tools and inspiration to mainstream sustainable development across a student's learning environment. Critical thinking, problem-solving skills and competencies related to ESD should be embedded in a student's learning process to ensure they can manage complexities such as uncertainty and risk. This invites the use of informed student-centred and inquiry-based teaching approaches within the programme.",
  '1.24': '1.24 ESD should be interpreted in the context of the Advance HE and QAA Education for Sustainable Development Guidance.',
  '1.25': '1.25 Education activities in enterprise and entrepreneurship may also contribute to Forensic Science courses by supporting behaviours, attributes and competencies that are likely to have a significant impact on the individual student in terms of successful careers. Enterprise activities should be ambitious and require students to develop creative, innovative, resilient and critical approaches to provide solutions, generate ideas and communicate issues aligned with forensic practice. Through entrepreneurship activities students learn to organise and manage business risk and associated business profit. Such activities prepare students for changing environments, and provide enhanced impact through placements and activities that build links between academic institutions and external organisations.',
  '1.27': '1.27 Enterprise thinking and entrepreneurship will drive the future of forensic science. Students should be able to identify opportunities for business development or process improvement whether this be through studies, partnerships or placements. The grounding of entrepreneurial thought is in making decisions, acting on ideas and individual creativity to support wider commercial or organisational interests.',
  '2.1': '2.1 The course and thus its curriculum should be designed to enable students to demonstrate the attainment of the stated learning outcomes of the course, and the assessment strategies should align to these outcomes. The course outcomes and content (section 3) should reflect the contemporary knowledge and skills required by relevant graduate employers. Therefore, course design should be frequently updated with developments in pedagogical and scientific research and collaboration or partnership with appropriate key stakeholders - for example, with forensic science providers, police forces, other investigative agencies and the judiciary. Students should be supported to progressively acquire subject knowledge and skills, gradually advancing towards more independent learning.',
  '2.3': '2.3 Digital accessibility is the inclusive practice of ensuring that all people can equally access and navigate digital information and platforms, such as websites, electronic documents and mobile phone applications, irrespective of physical, situational or socio- economical impairments (W3C , 2018). The content, which will include text, images and sound, should be accessible and comprehensible without discrimination.',
  '2.6': '2.6 Joint honours undergraduates will achieve core elements of the specific and generic skills for the subject, and will add others according to the subjects covered in joint courses. Additionally, they may explore the overlap between their two subject areas, creating further opportunities for interdisciplinary study.',
  '2.9': '2.9 Degree providers are encouraged to consider a range of learning modes to offer flexibility within their courses with the aim of meeting diverse learner needs including assisted learning including communication skills. Where possible, full-time, part-time and distanced learning options should be offered and within each of these modes, there are a variety of options. To enable wider participation, providers might consider a combination of classroom-based, online and employer-based learning or a blended approach to all of these such as the HyFlex (hybrid-flexible) delivery approach, blending online and on-site participation. Not only does this increase inclusivity and equity, but it empowers students by providing choices, where possible and appropriate, relating to the how, what, when and where they learn.',
  '2.10': "2.10 Flexibility should also encompass a plan of action for those with protected characteristics and, where there is a change in a student's circumstances, to support them to complete their course. In addition, it is important that providers have a plan in place for the sudden need to change content delivery mode, such as the need to move entirely to online and digital delivery to ensure continuation of learning. This flexibility may include altering the practical/theory content and may even involve the practical being concentrated into blocks. Certain aspects, particularly related to practical skills, may need to be considered in a particular way to ensure the required skill development.",
  '2.11': '2.11 Degree providers should be encouraged to develop partnerships and engagement with forensic science employers (law enforcement agencies and private sector forensic service providers) and other wider organisations where degree activities can be related to the work environment. This will help prepare the students for the demands and expectations of the workplace while developing their workplace skills which are likely to include self- reliance, critical thinking, interpersonal, problem-solving and teamworking skills. For\n\n12\nemployers this helps resolve workplace skills shortages, grows a pipeline for recruitment, improves recruitment success and increases retention of staff.',
  '2.14': '2.14 A major feature of academic quality assurance and enhancement at a higher education institution is having in place monitoring and regular review processes for the courses it delivers. Degree-awarding bodies routinely collect and analyse information and undertake periodic course review according to their own needs. They will draw on a range of external reference points, including this Statement, to ensure that their provision aligns with sector norms. Monitoring and evaluation is a periodic assessment of a course, conducted internally or by external independent evaluators. Evaluation uses information from both current and historic monitoring to develop an understanding of student achievement or inform future course planning.',
  '2.15': '2.15 Forensic Science degrees will work collaboratively with external examiners, student cohorts and external partners to enhance the educational experience. Close alignment with external bodies such as, but not limited to, the Chartered Society of Forensic Sciences and the Forensic Science Regulator ensure that the content as set out below remains relevant.',
  '2.16': '2.16 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.',
  '2.18': '2.18 Forensic science has professional and vocational outcomes that may also require evaluation and accreditation from professional and regulatory bodies as outlined above. These are usually done through a combination of site visits and desk-based reviews. Monitoring and evaluation processes should identify appropriate stakeholders and ensure dissemination of findings with regards to learning, teaching and assessment at various levels to reflect changes in cohorts, experience and pedagogic practice.',
  '3.4': '3.4 Practical classes, for example in laboratories and/or computer rooms, should support the taught curriculum, and in particular allow the student to acquire transferable technical and practical skills. This will include familiarity with a variety of forensic experimental methods and their scientific basis, and with methods to deal with uncertainties in their outcomes, such as data handling and statistics to carry out probabilistic inference (expanded upon in paragraph 3.19). The contemporaneous preparation of records and reports is likely to be emphasised.',
  '3.5': "3.5 At master's level, experience of research methods and of reading and interpreting research publications is expected, as is extended project work, including the preparation of an independent original report, for example, in the style of a journal article or thesis.",
  '3.6': '3.6 As previously outlined in section 2, the programme of teaching and learning should be designed to enable students to demonstrate the attainment of the stated learning outcomes of the course using assessment strategies that align to these outcomes and the skills required by relevant graduate employers. As a result, the teaching and learning strategies suggested above should be reviewed and updated with advances in pedagogy,\n\n15\nandragogy and educational and professional information technology, although the balance between different methods may vary between institutions and courses. Teaching staff will need to maintain their knowledge of forensic science to remain current by suitable and regular continuous professional development engagement. Subject-specific content should also be underpinned and updated based on the latest research, innovation, practice and regulation within the sector. Overarching considerations will be the demonstrable acquisition by the student of a clear appreciation of the scientific approach, and of the knowledge and skills needed for the practice of forensic science.',
  '3.7': '3.7 Depending on the course type, learning outcomes or learner demographics, the taught curriculum may be delivered using synchronous (live) and/or asynchronous approaches, on campus and/or from a distance (remote). Wherever possible, sessions should be designed to be student-centred and utilise active learning strategies to promote inclusivity, application and engagement. Design and delivery should also consider the use of technology, hardware and/or software, to enhance the learning experience and provide further opportunities to apply knowledge in problem-solving.',
  '3.9': '3.9 Students should also be expected to develop a knowledge of the criminal justice and legal systems within the UK and an appreciation of systems that operate globally in different jurisdictions. This should include an understanding of both the adversarial and inquisitorial approaches from the global perspective and, in particular, how forensic science and the role of the expert witness, including defence scientists operate within these systems. They should have an understanding of prevailing legal standards and legislation applicable to the recovery, storage, retention, analysis and disposal of evidence.',
  '3.10': '3.10 Within the three main themes of forensic science outlined in paragraph 1.14, different degree schemes may have different emphases, however, a basic knowledge of all three themes, appropriate to that degree, is a minimum expectation for all students. The content of these themes is expanded on as follows.',
  '3.11': '3.11 Scene investigation encompasses knowledge of the principles and effective safe working practical application of the relevant techniques needed for the formulation of scene examination strategies which involve understanding the potential significance of various materials in a given context. This includes understanding the importance of the recognition, priority processing, recording, preservation, recovery, storage, scientific analysis and interpretation of evidence at the scene, including strategies for dealing with contamination issues throughout the process. Students will acquire, as appropriate, an understanding of the forensic principles and practices when using a range of imaging techniques, in particular (crime) scene photography together with a clear understanding of the responsibilities, roles\n\n16\nand liabilities of the individuals and agencies involved in a (crime) scene, and of information exchange between them.',
  '3.12': '3.12 Laboratory examination and analysis requires competence in the selection and application of a range of methods used in the location, identification, recovery, examination, comparison (including mark comparison), extraction and scientific analysis of commonly encountered physical, chemical, biological and digital evidential materials, including appropriate storage practices, as appropriate. This is underpinned by safe working practices and knowledge of the theory, application and limitations of the principal laboratory methods used routinely in forensic science together with an understanding of the importance of validation, calibration and the use of accepted examination or analytical methods for all laboratory work, where appropriate. Students will also have a knowledge of the principles and application of control and reference samples, and the use of databases for the identification of materials.',
  '3.13': '3.13 Interpretation, evaluation and presentation of evidence encompasses the management and interpretation of the results from the examination of physical or digital evidence, in the context of casework. Fundamental to this is the understanding and application of accepted methods of interpretation and evaluation, in particular that of logical evaluation using likelihood ratio, and other appropriate statistical analysis, including the use of appropriate interpretive databases, together with an understanding of factors affecting the interpretation process that may contribute to uncertainty in the outcome and consequent expert opinion. Students will be able to interpret and assign conclusions to forensic findings and to distinguish between factual and expert reporting. They will be able to formulate expert opinion and have the knowledge and skills to write impartial, comprehensive and appropriate reports in a variety of formats and for a variety of audiences, including for both investigators and for the court. They will acquire the skills and expertise to convey and defend, both orally and in writing, a written report in the context of the court.',
  '3.14': '3.14 The three core components of forensic science above are underpinned by scientific knowledge and understanding drawn principally from chemistry, biology, physics, mathematics, computer science and law topics, but the list is not intended to be exhaustive and may include aspects of digital forensics. Again, different degree schemes may have different emphases, but a basic knowledge of these underpinning sciences appropriate to that degree course is expected. For courses in digital forensics, appropriate scientific and mathematical underpinning is expected.',
  '3.15': '3.15 In chemistry, students should be able to select, utilise and interpret data from appropriate analytical and microscopic techniques, to determine analytes in a sample, identify and compare materials and determine their composition within a forensic science context. The student should appreciate the underlying theoretical and operating principles of analytical and microscopic techniques and the limitations of the techniques, as well as chemical interactions that may be taking place.',
  '3.16': '3.16 In biology, the course should include practical microscopy, and molecular biology and biochemistry (with particular emphasis on body fluid identification and detection, nucleic acids, proteins, enzymes and biochemical processes, molecular genetics, genomics and principles of inheritance), forensic genetic techniques such as Short Tandem Repeat (STR) and may include anatomy, organ systems, some forensic medicine and other areas such as entomology, microbiology, palynology, botany and anthropology.',
  '3.17': '3.17 In physics, the course should include elementary optics (including principles of microscopy), the mechanics principles that underpin projectiles, ballistics, explosions and blood dynamics, aspects of the physical properties of materials, and an understanding of electromagnetism, atomic structure and radiation needed for an appreciation of the\n\n17\ntheoretical aspects of chemical instrumental analysis, forensic photography and other imaging techniques.',
  '3.18': '3.18 In mathematics, there should be sufficient knowledge and facility in functions, algebra and trigonometry to cover the mathematical aspects of the physics, chemistry and biology in the course. Appropriate statistics would be a working knowledge of the basis and application of statistical methods and probability for analysis of experimental data and their uncertainties, including sampling methods and determining method uncertainty. This should also include an understanding of the principles and application of the likelihood ratio approach to the evaluation of evidence for the court, including the retrieval and use of frequency of occurrence information and the use of databases.',
  '3.19': '3.19 Digital forensics builds upon principles based in computer science. Such principles are likely to include knowledge in data representation schemes (such as binary and hexadecimal), coding in a least one language (for example, Python), the different types of networks and the basic protocols in use, the principles of computer security, and an understanding of relational databases. From these principles, the course should develop to include reverse engineering techniques to understand the structure of unfamiliar data, linking artefacts from disparate data sources to develop a timeline of user activity and distinguishing between circumstantial and probative evidence.',
  '3.20': '3.20 In law, the course would be expected to include an awareness of criminal law, appropriate range of legislation, jurisdiction and procedures for working within a justice system. This includes the role of the expert witness as well as a working knowledge of the legislation that governs professional practice, such as the Police and Criminal Evidence Act 1984, the Data Protection Act 2018, and the Criminal Procedural Rules and Practice Directions 2020.',
  '3.30': "3.30 Assessment will test the successful achievement of subject knowledge, and the acquisition of generic and subject-specific skills embedded in the learning outcomes for the course. It is appropriate that some assessment elements will test a student's ability to organise and complete work, and to communicate effectively, under constraints of time and pressure. Elements of the assessment should also allow students the opportunity to demonstrate reflection, originality, creativity and integration of their knowledge into practice.",
  '3.31': '3.31 Assessments should be shared with students via an assessment brief with associated marking criteria mapped against the specific learning outcomes of the module or course. However, there may also be opportunities for students to design or co-create assessments with their tutors and/or peers as part of the learning process and these may or may not form part of the marking criteria. Assessments should be designed to be inclusive of all students, for example by using digital accessibility best practices, and meet learning support requirements, such as hearing impairments and colour blindness. While it still may be necessary on occasion to provide an alternative assessment to meet a specific learning support requirement, good assessment design should aim to anticipate such needs as much as possible. It is also important that alternative assessments enable students to demonstrate that they meet the expected learning outcome(s).',
  '3.33': '3.33 To encourage students to engage with feedback, it should be provided in a timely manner. It is also suggested that the curriculum contains embedded, visible opportunities for students to create and implement their action plans to further promote personal development.',
  '4.2': "4.2 In each case, the standards are divided into 'threshold', 'typical' and 'excellent'. These standards are intended to reflect the performance of the individual student. The threshold level is the core of the Subject Benchmark Statement and is achieved by anyone obtaining an honours degree. Many students will perform significantly better than the threshold standard, and it is expected that most should achieve the typical standard. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd.",
  '4.10': "4.10 An integrated master's degree is a combination of both bachelor's degree studies and master's level; students are therefore expected to have developed the graduate outcomes for Forensic Science associated with a degree to at least a typical level (paragraph 4.6) but will have extended their knowledge, skills and understanding into outcomes associated with aspects of a master's degree.",
  '2.2': '2.2 Accessibility considerations should apply to all aspects of the course. This relates to physical access but also includes cultural awareness, language and sensitivity to victims of crime. Accessibility should consider whether all aspects of the course can be understood or used by people however it is encountered. This includes the recognition for curricula, tuition and assessment being accessible and reasonable adjustments being put in place. To ensure students who struggle with particular forms of teaching and learning scenarios are not disadvantaged, methods used within an individual course should be as varied as possible. There are many forms of delivery, too many to include all, but some examples are likely to comprise an appropriate combination of the following:',
  '2.13': '2.13 If students choose a work placement opportunity as part of their degree this should have a clear programme of learning. The typical activities a student may undertake as part of their placement could be quality assurance activities, data analysis, basic examination processes, administration of evidence and specific project work. In order to successfully secure a work placement, the student would likely need to display:',
  '3.3': '3.3 Utilising a combination of teaching and learning practices (pedagogy and andragogy) should enable learners to develop their knowledge and understanding along with academic and professional skills. Teaching methods may include:',
  '3.28': '3.28 Students should fully appreciate that to fabricate, falsify, misrepresent or wilfully misinterpret evidence, data or the results of experiments is unethical and unacceptable. This should be referred to within the course material. They should also:',
  '3.29': "3.29 Within the multidisciplinary curriculum of forensic science, a diverse selection of assessment formats is expected to provide opportunities for students to develop a broad and contemporary skillset for the range of careers they may wish to pursue post-graduation. Assessments may be a combination of formative and summative to enhance students' skills and gain confidence, and may be delivered through in-person and/or online mechanisms. Reasonable adjustments for disabled students should be made to all assessment practices according to the student requirements. Assessment types could include some or all of the following elements at various levels of the curriculum:",
  '3.23.b4': 'independently plan, design, conduct and report an independent research project.',
  '3.25.b3': 'an understanding of the moral and ethical issues involved in the practice of forensic science.',
  '3.27.b4': 'the independent learning ability required for continuing professional development.',
  '3.28.b6': "be aware of ethical issues, legal requirements and procedures involved in the conduct of research, particularly when working with animals and humans, and/or using an individual's data.",
  '4.4.b16': 'communication skills to an understandable level, verbally and in writing.',
  '4.4.b23': 'the ability to adhere to contamination avoidance procedures including the handling of digital data.',
  '4.5.b2': 'an understanding of the responsibilities, roles and liabilities of those involved in a scene investigation, including when to call upon specialist personnel and an ability to work safely, effectively and contribute positively within such a team.',
  '4.5.b4': 'an ability in the selection and use of a wide range of methods used in the location, identification, recovery, extraction and scientific analysis of commonly encountered physical, digital, chemical and biological materials and marks, including trace materials such as DNA.',
  '4.5.b9': 'the ability to construct and manage a forensic strategy, with regards to the search of multiple sites and the subsequent analysis of digital data.',
  '4.6.b23': 'the ability to effectively construct, manage and deliver case-appropriate forensic strategies, including the Case Assessment and Interpretation framework.',
  '4.7.b2': 'a thorough understanding of the responsibilities, roles and liabilities of those involved in a (crime) scene investigation, and an ability to work effectively and contribute positively within such a team.',
  '4.7.b4': 'consistent ability in the selection and use of a wide range of methods used in the location, identification, recovery, extraction and scientific analysis of commonly encountered physical, digital, chemical and biological materials and marks, including trace materials such as DNA.',
  '4.8.b16': 'communication skills to an accomplished level, verbally and in writing.',
  '4.8.b23': 'the ability to consistently and effectively construct, manage and deliver case- appropriate forensic strategies, including the Case Assessment and Interpretation framework.',
  '4.9.b2': 'a comprehensive and critical understanding of the responsibilities, roles and liabilities of those involved in a (crime) scene investigation, and a consistent ability to work effectively and contribute positively within such a team.',
  '4.9.b4': 'consistent ability in the critical selection, use and development of a wide range of methods used in the location, identification, recovery, extraction and scientific analysis of commonly encountered physical, digital, chemical and biological materials and marks, including trace materials such as DNA.',
  '4.5.b5': 'knowledge and understanding of the principal techniques and skills required for the searching, identification, preservation, transport, handling, and continuity of\n\n23\ncommonly encountered physical devices likely or known to contain digital data from a range of scenes',
}
AFTER = {
  '1.4': '1.4 Over the past 20 year',
  '1.8': '1.8 All degree courses sh',
  '1.17': '1.17 Interpretation and e',
  '1.19': '1.19 This Subject Benchma',
  '1.23': '1.23 Education for Sustai',
  '1.24': '1.24 ESD should be interp',
  '1.25': '1.25 Education activities',
  '1.27': '1.27 Enterprise thinking ',
  '2.1': '2.1 The course and thus i',
  '2.3': '2.3 Digital accessibility',
  '2.6': '2.6 Joint honours undergr',
  '2.9': '2.9 Degree providers are ',
  '2.10': '2.10 Flexibility should a',
  '2.11': '2.11 Degree providers sho',
  '2.14': '2.14 A major feature of a',
  '2.15': '2.15 Forensic Science deg',
  '2.16': '2.16 Externality is an es',
  '2.18': '2.18 Forensic science has',
  '3.4': '3.4 Practical classes, fo',
  '3.5': "3.5 At master's level, ex",
  '3.6': '3.6 As previously outline',
  '3.7': '3.7 Depending on the cour',
  '3.9': '3.9 Students should also ',
  '3.10': '3.10 Within the three mai',
  '3.11': '3.11 Scene investigation ',
  '3.12': '3.12 Laboratory examinati',
  '3.13': '3.13 Interpretation, eval',
  '3.14': '3.14 The three core compo',
  '3.15': '3.15 In chemistry, studen',
  '3.16': '3.16 In biology, the cour',
  '3.17': '3.17 In physics, the cour',
  '3.18': '3.18 In mathematics, ther',
  '3.19': '3.19 Digital forensics bu',
  '3.20': '3.20 In law, the course w',
  '3.30': '3.30 Assessment will test',
  '3.31': '3.31 Assessments should b',
  '3.33': '3.33 To encourage student',
  '4.2': '4.2 In each case, the sta',
  '4.10': '4.10 An integrated master',
  '2.2': '2.2 Accessibility conside',
  '2.13': '2.13 If students choose a',
  '3.3': '3.3 Utilising a combinati',
  '3.28': '3.28 Students should full',
  '3.29': '3.29 Within the multidisc',
  '3.23.b4': '3.23 In addition to the a',
  '3.25.b3': '3.25 In addition to the a',
  '3.27.b4': '3.27 In addition to the a',
  '3.28.b6': '3.28 Students should full',
  '4.4.b16': '4.4 Students graduating w',
  '4.4.b23': '4.4 Students graduating w',
  '4.5.b2': '4.5 Students graduating w',
  '4.5.b4': '4.5 Students graduating w',
  '4.5.b9': '4.5 Students graduating w',
  '4.6.b23': '4.6 Students graduating w',
  '4.7.b2': '4.7 Students graduating w',
  '4.7.b4': '4.7 Students graduating w',
  '4.8.b16': '4.8 Students graduating w',
  '4.8.b23': '4.8 Students graduating w',
  '4.9.b2': '4.9 Students graduating w',
  '4.9.b4': '4.9 Students graduating w',
  '4.5.b5': '4.5 Students graduating w',
}
# the issuer's action verbs, each present in its span
VERBS = {
  '1.4': ['have', 'select', 'support', 'provided', 'reviewed', 'underpinned'],
  '1.8': ['accord'],
  '1.17': ['report', 'distinguish'],
  '1.19': ['have', 'deliver', 'embed', 'interpreted', 'consider', 'respect'],
  '1.23': ['developing', 'use', 'manage', 'work', 'support', 'embedded'],
  '1.24': ['interpreted'],
  '1.25': ['develop', 'have', 'organise', 'communicate', 'prepare', 'manage'],
  '1.27': ['identify', 'support', 'drive'],
  '2.1': ['demonstrate', 'acquire', 'design', 'reflect', 'designed', 'updated'],
  '2.3': ['include', 'access'],
  '2.6': ['achieve', 'add', 'explore'],
  '2.9': ['meeting', 'offered', 'encouraged', 'consider', 'enable', 'learn'],
  '2.10': ['have', 'plan', 'support', 'include'],
  '2.11': ['develop', 'developing', 'prepare', 'work', 'include', 'encouraged'],
  '2.14': ['develop', 'review', 'undertake', 'draw', 'analyse'],
  '2.15': ['work', 'collaboratively'],
  '2.16': ['use', 'gain', 'review'],
  '2.18': ['identify', 'reflect'],
  '3.4': ['acquire', 'carry', 'support', 'include', 'allow', 'deal'],
  '3.5': ['work', 'report'],
  '3.6': ['demonstrate', 'designed', 'reviewed', 'updated', 'maintain', 'underpinned'],
  '3.7': ['use', 'utilise', 'apply', 'design', 'promote', 'designed'],
  '3.9': ['develop', 'have', 'include'],
  '3.10': ['have'],
  '3.11': ['acquire', 'includes'],
  '3.12': ['use', 'have', 'work', 'underpinned'],
  '3.13': ['acquire', 'use', 'have', 'interpret', 'formulate', 'report'],
  '3.14': ['have', 'include', 'underpinned'],
  '3.15': ['utilise', 'select', 'interpret', 'appreciate', 'identify'],
  '3.16': ['include'],
  '3.17': ['include'],
  '3.18': ['use', 'include'],
  '3.19': ['develop', 'use', 'include', 'understand'],
  '3.20': ['include', 'includes'],
  '3.30': ['demonstrate', 'organise', 'communicate', 'work', 'embedded', 'test'],
  '3.31': ['demonstrate', 'design', 'support', 'shared', 'designed', 'enable'],
  '3.33': ['encourage', 'promote', 'embedded', 'engage', 'provided', 'implement'],
  '4.2': ['reflect', 'perform', 'achieve', 'refer'],
  '4.10': ['have'],
  '2.2': ['apply', 'include', 'includes', 'consider', 'access'],
  '2.13': ['have', 'work', 'undertake', 'display'],
  '3.3': ['develop', 'include', 'enable'],
  '3.28': ['appreciate', 'fabricate', 'falsify', 'misrepresent', 'misinterpret'],
  '3.29': ['develop', 'gain', 'include', 'made'],
  '1.6.b1': ['develop'],
  '1.6.b2': ['have'],
  '1.6.b3': ['acquire'],
  '1.6.b4': ['develop'],
  '1.6.b5': ['acquire'],
  '1.6.b6': ['acquire', 'present', 'justify'],
  '1.6.b7': ['demonstrate', 'use', 'respect'],
  '1.6.b8': ['develop'],
  '1.6.b9': ['become', 'record'],
  '1.6.b10': ['acquire'],
  '1.6.b11': ['demonstrate', 'recognise'],
  '1.6.b12': ['develop', 'support'],
  '1.6.b13': ['develop'],
  '1.6.b14': ['develop'],
  '1.6.b15': ['encourage', 'review', 'critically'],
  '1.6.b16': ['gain', 'access', 'understand'],
  '1.6.b17': ['gain'],
  '1.6.b18': ['gain'],
  '1.7.b1': [],
  '1.7.b2': [],
  '1.7.b3': ['carry', 'present', 'plan', 'devise'],
  '1.7.b4': [],
  '1.7.b5': ['work'],
  '1.7.b6': [],
  '1.7.b7': [],
  '3.8.b1': ['conduct'],
  '3.8.b2': ['conduct', 'respect'],
  '3.8.b3': [],
  '3.8.b4': ['implement'],
  '3.22.b1': ['work', 'includes'],
  '3.22.b2': ['use'],
  '3.22.b3': ['carry', 'understand'],
  '3.22.b4': ['interpret', 'present', 'evaluate', 'plan', 'identify', 'critically'],
  '3.22.b5': ['evaluate', 'plan', 'execute', 'report', 'analyse', 'critically'],
  '3.22.b6': ['construct', 'apply', 'design', 'tackle', 'test'],
  '3.22.b7': ['use', 'organise', 'analyse'],
  '3.23.b1': ['work'],
  '3.23.b2': ['apply', 'adapt'],
  '3.23.b3': ['plan', 'execute', 'design'],
  '3.23.b4': ['plan', 'report', 'design', 'conduct'],
  '3.24.b1': ['conduct', 'appreciate'],
  '3.24.b2': ['work'],
  '3.24.b3': ['undertake'],
  '3.24.b4': ['construct'],
  '3.24.b5': [],
  '3.24.b6': ['use'],
  '3.24.b7': ['comply'],
  '3.24.b8': ['have'],
  '3.24.b9': ['possess'],
  '3.24.b10': ['appreciate'],
  '3.25.b1': [],
  '3.25.b2': [],
  '3.25.b3': [],
  '3.26.b1': ['developing'],
  '3.26.b2': ['carry'],
  '3.26.b3': ['present', 'communicate', 'interact'],
  '3.26.b4': ['use', 'construct'],
  '3.26.b5': ['use'],
  '3.26.b6': ['organise', 'work', 'plan', 'perform', 'meeting'],
  '3.26.b7': ['identify', 'reflect'],
  '3.26.b8': ['apply', 'respect'],
  '3.27.b1': [],
  '3.27.b2': [],
  '3.27.b3': ['interpret', 'communicate'],
  '3.27.b4': [],
  '3.28.b1': ['appreciate'],
  '3.28.b2': ['work'],
  '3.28.b3': ['recognise', 'acknowledge'],
  '3.28.b4': ['recognise'],
  '3.28.b5': [],
  '3.28.b6': ['conduct'],
  '4.4.b1': [],
  '4.4.b2': [],
  '4.4.b3': ['carry'],
  '4.4.b4': ['use', 'carry', 'select'],
  '4.4.b5': [],
  '4.4.b6': [],
  '4.4.b7': ['interpret'],
  '4.4.b8': [],
  '4.4.b9': [],
  '4.4.b10': ['record', 'organise', 'make', 'present'],
  '4.4.b11': ['made'],
  '4.4.b12': [],
  '4.4.b13': ['respect'],
  '4.4.b14': [],
  '4.4.b15': [],
  '4.4.b16': [],
  '4.4.b17': ['interpret', 'communicate'],
  '4.4.b18': ['formulate', 'justify'],
  '4.4.b19': ['appraise', 'quantify', 'communicate'],
  '4.4.b20': ['prepare', 'deliver'],
  '4.4.b21': [],
  '4.4.b22': ['deliver', 'construct', 'manage'],
  '4.4.b23': ['adhere'],
  '4.5.b1': [],
  '4.5.b2': ['work', 'contribute', 'call'],
  '4.5.b3': [],
  '4.5.b4': ['use'],
  '4.5.b5': [],
  '4.5.b6': ['use', 'select', 'justify'],
  '4.5.b7': ['carry', 'understand'],
  '4.5.b8': ['review', 'validate', 'verify'],
  '4.5.b9': ['construct', 'manage'],
  '4.6.b1': [],
  '4.6.b2': [],
  '4.6.b3': ['carry'],
  '4.6.b4': ['use', 'carry', 'select'],
  '4.6.b5': ['apply', 'identify'],
  '4.6.b6': [],
  '4.6.b7': ['interpret'],
  '4.6.b8': [],
  '4.6.b9': [],
  '4.6.b10': ['record', 'organise', 'make', 'present'],
  '4.6.b11': ['made'],
  '4.6.b12': [],
  '4.6.b13': ['respect'],
  '4.6.b14': [],
  '4.6.b15': [],
  '4.6.b16': [],
  '4.6.b17': ['interpret', 'communicate', 'manage', 'critically'],
  '4.6.b18': ['formulate', 'justify'],
  '4.6.b19': ['appraise', 'quantify', 'communicate'],
  '4.6.b20': ['prepare', 'deliver'],
  '4.6.b21': [],
  '4.6.b22': ['adhere'],
  '4.6.b23': ['deliver', 'construct', 'manage'],
  '4.7.b1': [],
  '4.7.b2': ['work', 'contribute'],
  '4.7.b3': [],
  '4.7.b4': ['use'],
  '4.7.b5': [],
  '4.7.b6': ['use', 'select', 'justify'],
  '4.7.b7': ['carry', 'understand'],
  '4.7.b8': ['review', 'validate', 'verify'],
  '4.7.b9': ['construct', 'manage'],
  '4.8.b1': [],
  '4.8.b2': [],
  '4.8.b3': ['carry'],
  '4.8.b4': ['develop', 'use', 'carry', 'select', 'critically'],
  '4.8.b5': ['apply', 'identify', 'critically'],
  '4.8.b6': [],
  '4.8.b7': ['interpret'],
  '4.8.b8': [],
  '4.8.b9': [],
  '4.8.b10': ['record', 'organise', 'make', 'present', 'critically'],
  '4.8.b11': ['made'],
  '4.8.b12': [],
  '4.8.b13': ['respect'],
  '4.8.b14': [],
  '4.8.b15': [],
  '4.8.b16': [],
  '4.8.b17': ['interpret', 'communicate', 'manage', 'critically'],
  '4.8.b18': ['formulate', 'justify'],
  '4.8.b19': ['appraise', 'quantify', 'communicate', 'critically'],
  '4.8.b20': ['prepare', 'deliver'],
  '4.8.b21': [],
  '4.8.b22': ['develop', 'adhere'],
  '4.8.b23': ['deliver', 'construct', 'manage'],
  '4.9.b1': [],
  '4.9.b2': ['work', 'contribute'],
  '4.9.b3': [],
  '4.9.b4': ['use'],
  '4.9.b5': [],
  '4.9.b6': ['use', 'select', 'justify', 'critically'],
  '4.9.b7': ['carry', 'understand'],
  '4.9.b8': ['review', 'validate', 'verify', 'critically'],
  '4.9.b9': ['construct', 'manage'],
  '4.11.b1': [],
  '4.11.b2': [],
  '4.11.b3': [],
  '4.11.b4': ['carry', 'plan', 'report', 'devise'],
  '4.11.b5': [],
  '4.11.b6': [],
  '4.11.b7': ['plan', 'execute'],
  '4.11.b8': [],
  '4.11.b9': ['interpret', 'communicate'],
  '4.11.b10': [],
}

G = {
  '1.1': "scope: honours, master's and integrated master's courses; the working definition is in 1.3",
  '1.2': 'also covers the forensic parts of courses based in other benchmarked subjects; even-handed across the investigative process',
  '1.3': 'forensic science as science in the service of law; differences between jurisdictions; the UK aim of ISO accreditation for scene, examination and reporting by 2025',
  '1.4': 'testimony resting on sound science; the growth of degrees; accreditation by the professional society; equity of opportunity (S4)',
  '1.5': 'a broad science degree with a vocational focus on investigation and justice',
  '1.6': 'eighteen aims a course should pursue (S4, one record per item)',
  '1.7': "seven further aims for master's courses (S4)",
  '1.8': "courses to match the national qualification descriptors (S4); QAA's guidance on master's degrees",
  '1.9': 'most courses are laboratory-based analytical science; others lean towards digital forensics or investigation',
  '1.10': 'employers: justice-system bodies and forensic science providers; wider science, quality and communication roles',
  '1.11': 'a regulated field: quality standards, validation, law, codes; awareness of bias and ethics',
  '1.12': 'practitioners need relevant law and procedure, civil and criminal, in the UK and abroad',
  '1.13': 'multidisciplinary grounding in chemistry, biology, physics, mathematics and statistics',
  '1.14': 'three integrated components: scene, laboratory, and interpretation and presentation',
  '1.15': 'scene investigation read broadly: physical and digital scenes, safety, contamination, civil and coroner work, fieldwork',
  '1.16': 'laboratory work read broadly: chemical, biological, physical and digital examination; safety; many kinds of laboratory',
  '1.17': 'interpreting and evaluating evidence; what a report must be (S4); evidence and potential evidence',
  '1.18': 'techniques change fast; practitioners keep up with research',
  '1.19': 'the Equality Act 2010 and the equality duty; a shared responsibility for equal opportunity (S4)',
  '1.20': 'reflective questions on equality in courses (not statements)',
  '1.21': "commitment to equality and the Act's three aims (not statements)",
  '1.22': 'practices an equality review may cover (not statements)',
  '1.23': 'education for sustainable development defined and embedded; lifelong learning; staff equipped (S4)',
  '1.24': 'sustainable development read through the Advance HE and QAA guidance (S4)',
  '1.25': 'enterprise education; ambitious enterprise activities (S4)',
  '1.26': 'entrepreneurship education beyond employment',
  '1.27': 'enterprise thinking; spotting openings for business or process improvement (S4)',
  '2.1': 'curriculum aligned to outcomes and employers, renewed with research and partners (S4)',
  '2.2': 'accessibility across the course, with examples of varied delivery (S4)',
  '2.3': 'digital accessibility (S4)',
  '2.4': 'the UK frameworks and their numbered levels',
  '2.5': 'honours at FHEQ 6 and FQHEIS 10; yearly progress towards the threshold; second-class graduates ready for postgraduate study',
  '2.6': 'joint honours students reach the core skills (S4)',
  '2.7': "integrated master's at FHEQ 7 and FQHEIS 11, and its length",
  '2.8': 'exit awards; four-year honours in Scotland',
  '2.9': 'flexible study modes, blended and HyFlex delivery (S4)',
  '2.10': 'support plans and contingency for a change of delivery (S4)',
  '2.11': 'partnerships with employers (S4)',
  '2.12': 'research partnerships with organisations',
  '2.13': 'placements need a programme of learning (S4); attributes a placement asks for (not statements)',
  '2.14': 'monitoring and periodic review against external reference points (S4)',
  '2.15': 'working with examiners, students, partners and professional bodies (S4)',
  '2.16': 'external reviewers in periodic review (S4)',
  '2.17': 'external examining',
  '2.18': 'professional accreditation; monitoring that involves stakeholders (S4)',
  '3.1': "the professional society's accreditation as a source of curriculum standards",
  '3.2': 'core and optional curriculum areas',
  '3.3': 'teaching and learning methods (S4)',
  '3.4': 'practical classes (S4)',
  '3.5': "research experience at master's level (S4)",
  '3.6': 'design for outcomes; staff kept current; research-led content (S4)',
  '3.7': 'delivery modes; student-centred, active learning (S4)',
  '3.8': 'knowledge across the whole process from scene to court (S4, four items)',
  '3.9': 'justice and legal systems (S4)',
  '3.10': 'all three components as a minimum (S4)',
  '3.11': 'scene investigation content (S4)',
  '3.12': 'laboratory examination and analysis content (S4)',
  '3.13': 'interpretation, evaluation and presentation content (S4)',
  '3.14': 'the underpinning sciences (S4)',
  '3.15': 'chemistry (S4)',
  '3.16': 'biology (S4)',
  '3.17': 'physics (S4)',
  '3.18': 'mathematics and statistics (S4)',
  '3.19': 'digital forensics (S4)',
  '3.20': 'law (S4)',
  '3.21': 'four groups of skills: scientific, forensic, generic and ethical',
  '3.22': 'scientific, laboratory and research skills (S4, seven items)',
  '3.23': "master's additions to those skills (S4, four items)",
  '3.24': 'forensic science skills (S4, ten items)',
  '3.25': "master's additions to those skills (S4, three items)",
  '3.26': 'generic graduate skills (S4, eight items)',
  '3.27': "master's additions to those skills (S4, four items)",
  '3.28': 'ethical behaviour (S4, stem and six items)',
  '3.29': 'varied assessment; reasonable adjustments (S4); kinds of assessment (not statements)',
  '3.30': 'what assessment tests (S4)',
  '3.31': 'briefs, criteria and inclusive design of assessment (S4)',
  '3.32': 'feedback mechanisms (not statements)',
  '3.33': 'prompt feedback; action plans (S4)',
  '4.1': 'two groups of standards: generic, and specific to three areas',
  '4.2': 'the three rungs; the threshold is reached by every honours graduate; Annex D (S4)',
  '4.3': "the master's standard comes at the end",
  '4.4': 'threshold rung, generic standards (23 items)',
  '4.5': 'threshold rung, area standards (9 items)',
  '4.6': 'typical rung, generic standards (23 items)',
  '4.7': 'typical rung, area standards (9 items)',
  '4.8': 'excellent rung, generic standards (23 items)',
  '4.9': 'excellent rung, area standards (9 items)',
  '4.10': "integrated master's: at least typical honours, then master's outcomes (S4)",
  '4.11': "master's standards (10 items)",
}
CTYPE = {'3.2': 'area', '3.11': 'area', '3.12': 'area', '3.13': 'area', '3.14': 'area', '3.15': 'area', '3.16': 'area', '3.17': 'area',
         '3.18': 'area', '3.19': 'area', '3.20': 'area',
         '2.13': 'practice', '3.3': 'practice', '3.4': 'practice', '3.5': 'practice', '3.7': 'practice', '3.29': 'practice',
         '3.30': 'practice', '3.31': 'practice', '3.32': 'practice', '3.33': 'practice'}
EXCLUDED = [
  dict(number='none', heading='Contents; About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points', kind='other: front matter, read for S1, S2 and SB6'),
  dict(number='none', heading='Foreword from the Forensic Science Regulator', kind='other: front matter, read for SB1 and SB5'),
  dict(number='1, 2, 3, 4', heading='section heading lines', kind='other: headings, recorded in SECTIONS'),
  dict(number='5', heading='List of references and further resources', kind='other: back matter, read for SB6 and D3'),
  dict(number='6', heading='Membership of the Advisory Groups for the Subject Benchmark Statement for Forensic Science', kind='other: back matter, read for S8 (second edition; 2012 group)')]

# ---------------------------------------------------------------- statements
P = {}
def s(i, **k):
    k.setdefault('verbs', VERBS.get(i, []))
    if i in FIND:
        k['find'] = FIND[i]; k['after'] = AFTER[i]
    k.setdefault('type', 'expectation')
    k.setdefault('rung', 'none')
    P[i] = k

def you(t):
    for a, b in ((' themselves', ' yourself'), (' their ', ' your '), (' them ', ' you '), (' them.', ' you.'), (' them,', ' you,'), (' they ', ' you ')):
        t = t.replace(a, b)
    return t

NA_P = ('n/a', 'a duty on the course and its team; the student meets its effect, not a standard to reach')

# ---- section 1: purposes, themes
s('1.4', force='should', level='none', appliesTo='higher education institutions teaching the subject', addressee='provider',
  about='equity of opportunity through inclusive practice', domain='none', award=BOTH,
  para="Forensic testimony needs to rest on sound, peer-reviewed science; forensic degrees have spread in the UK and abroad; the professional society's accreditation scheme covers most UK courses; and institutions should support and promote equity of opportunity through accessible courses and positive action.",
  prac="Support and promote equity of opportunity: make the course accessible and take positive action. The paragraph also records that the professional society's accreditation scheme covers most UK courses.",
  ben=NA_P, nb=['1.19', '2.2'])

A16 = dict(force='should', level='fheq:6', appliesTo='courses in the subject and their students', addressee='both', award=HON, type='expectation', forceFrom='1.6')
def a16(n, vp, **k):
    s('1.6.b%d' % n, **A16, para='Courses should aim to help students %s.' % vp, prac='Aim to help students %s.' % vp,
      ben='Your course should aim to help you %s.' % you(' ' + vp).strip(), **k)
a16(1, 'build an enthusiasm for forensic science', about='enthusiasm for the subject', domain='none')
a16(2, 'have learning that stretches them intellectually and does them good', about='a stimulating, worthwhile learning experience', domain='none')
a16(3, 'gain the scientific knowledge and skills that competent forensic practice rests on, useful also to bodies that gather or analyse physical or digital evidence', about='science underpinning practitioner competence', domain='knowledge')
a16(4, 'gain a sound grounding in science and laboratory and transferable skills valued in forensic work and in any organisation built on analysis, digital content or quality assurance', about='sound science and transferable laboratory skills', domain='knowledge')
a16(5, 'understand why ISO quality standards exist and what working under them involves, and why high professional and ethical standards matter at every moment if miscarriages of justice are to be avoided', about='quality standards and professional ethics', domain='understanding')
a16(6, 'set out data, explain scientific reasoning and defend their conclusions to expert and lay audiences', about='communicating science to varied audiences', domain='generic-skill')
a16(7, 'learn independently, grow professionally, and show initiative and flexibility as needs and techniques change, perhaps by keeping a structured record of their personal development', about='independent learning and professional development', domain='generic-skill', fw='qaa/fheq-2024/4.15.b5')
a16(8, 'understand how evidence stays continuous from scene to court and beyond, why laboratory findings depend on good sampling at the scene, and how to avoid and detect contamination and cognitive bias at each stage', about='continuity of evidence, contamination and bias', domain='understanding')
a16(9, 'become familiar with the justice system and what police, expert witnesses and lawyers need from forensic work (records, admissibility, disclosure), and with how legal systems differ in the UK and elsewhere', about='the justice system and its demands', domain='knowledge')
a16(10, 'build problem-solving and research skills fit for degree study and keep aware of current and emerging forensic research', about='problem-solving, research and current research', domain='subject-skill')
a16(11, 'see why sustainability and equality, diversity and inclusion matter in forensic science, as a subject and as a profession, and commit to those values', about='sustainability and inclusion as professional values', domain='generic-skill')
a16(12, 'grasp the forensic opportunities in a case and how they serve a forensic strategy, thinking impartially and investigating so that an enquiry moves forward', about='forensic opportunities and strategy', domain='subject-skill')
a16(13, 'see what digital forensics can offer and how the forensic specialisms together get the most from the evidence', about='digital forensic opportunities', domain='understanding')
a16(14, 'build investigative skills, such as finding lines of enquiry, sources of evidence and artefacts and seeing how they connect', about='investigative skills', domain='subject-skill')
a16(15, 'review information critically, published science above all', about='critical review of information and literature', domain='subject-skill')
a16(16, 'understand the scientific method and the worth of experiment, and judge findings', about='the scientific method', domain='understanding')
a16(17, 'see how evidence from a scene, the investigation, the analysis and the court case link together', about='from scene to court', domain='understanding')
a16(18, "understand a forensic professional's duty to the court and what an expert witness does", about='duty to the court and the expert witness', domain='understanding')

A17 = dict(force='should', level='fheq:7', appliesTo="master's courses and their students", addressee='both', award=MA, type='expectation', forceFrom='1.7')
def a17(n, vp, **k):
    s('1.7.b%d' % n, **A17, para="A master's course should also aim to help students %s." % vp, prac="At master's level, aim also to help students %s." % vp,
      ben="If you take a master's, your course should also aim to help you %s." % you(' ' + vp).strip(), **k)
a17(1, 'gain deep knowledge and hands-on experience of forensic examination and analytical techniques and their use in chosen specialisms', about='deep knowledge of techniques in a specialism', domain='knowledge')
a17(2, 'engage critically with the research methods and techniques in use today', about='critical engagement with research methods', domain='understanding')
a17(3, 'conceive, plan, conduct and report a sizeable original research project in an academic setting', about='an extended original research project', domain='subject-skill')
a17(4, 'see clearly what limits and what opens up professional forensic science today', about='the professional setting, its limits and openings', domain='understanding')
a17(5, 'work within a quality standards framework', about='working to a quality standards framework', domain='subject-skill')
a17(6, 'be better prepared to enter professional work or doctoral study', about='readiness for employment or doctoral study', domain='generic-skill')
a17(7, 'keep learning on their own for continuing professional development', about='independent learning for professional development', domain='generic-skill', fw='qaa/fheq-2024/4.17.b7')

s('1.8', force='should', level='none', appliesTo='all degree courses in the subject', addressee='provider', about='matching national qualification descriptors',
  domain='none', award=[HON, MA, IMA],
  para="Every degree course should match the qualification descriptions in the national frameworks; QAA's guidance on kinds of master's degree may also help.",
  prac="Check the course against the qualification descriptors of the national framework that applies (the FHEQ, or the FQHEIS in Scotland); for master's courses, QAA's guidance on master's degree types may help.",
  ben=NA_P, nb=['2.5', '2.7', '4.2'], fwp='qaa/fheq-2024/4.15.i1 and qaa/fheq-2024/4.17.i1')
s('1.17', type='requirement', force='must', level='fheq:6', appliesTo='anyone reporting forensic findings, students included', addressee='learner',
  about='standards for forensic reports and witness statements', domain='subject-skill', award=BOTH,
  para="Interpreting and evaluating evidence means reliable recording, experiment, analysis and interpretation within the case, and clear, impartial written and oral presentation that explains significance and uncertainty; reports and witness statements must be robust, transparent, logical and free of bias, and should separate fact from expert opinion. Only a court decides what counts as evidence.",
  prac="Teach that reports and witness statements must be robust, transparent, logical and free of bias, and should keep factual reporting apart from expert opinion, as part of reliable recording, case-based interpretation and impartial presentation of findings and their uncertainty.",
  ben="Any report or witness statement you write must be robust, transparent, logical and free of bias, and should keep the facts apart from your expert opinion.",
  nb=['3.13', '4.4.b20', '4.4.b18'], when='a student is writing a report, a case file or a mock witness statement')
s('1.19', force='describes', level='none', appliesTo='all staff and students on courses in the subject', addressee='both',
  about='a shared responsibility for equal opportunity', domain='none', award=BOTH,
  para="The statement is to be read in the light of the Equality Act 2010 and its equality duty, and aims to embed equality, diversity and inclusion in all teaching; every member of staff and every student carries a responsibility to secure equal opportunity whatever a person's background, ability, culture, gender or identity.",
  prac="Read the course against the Equality Act 2010 and the public sector equality duty; staff and students alike carry a responsibility to secure equal opportunity for everyone.",
  ben="You share, with staff and other students, a responsibility to make sure everyone has an equal chance, whatever their background, ability, culture, gender or identity.",
  nb=['1.4', '3.26.b8', '3.28.b5'])
s('1.23', force='should', level='none', appliesTo='courses in the subject and their staff', addressee='provider',
  about='embedding education for sustainable development', domain='none', award=BOTH,
  para="Education for sustainable development should be built into teaching and learning so students grasp social, economic and ecological well-being now and later; for forensic students it includes lifelong learning through professional development; staff should be equipped to mainstream it; and critical thinking, problem-solving and related competencies should be embedded so students can handle uncertainty and risk.",
  prac="Build education for sustainable development into teaching, equip staff to mainstream it, and embed critical thinking and problem-solving so students can handle uncertainty and risk; for forensic students it also means keeping skills current through professional development. Student-centred, inquiry-based teaching suits it.",
  ben=('n/a', 'a duty on the course and its staff; the student-facing aim is 1.6, item 11'), nb=['1.24', '1.6.b11'])
s('1.24', force='should', level='none', appliesTo='courses in the subject', addressee='provider', about='reading sustainability through the national guidance',
  domain='none', award=BOTH,
  para="Education for sustainable development should be read through the Advance HE and QAA guidance on it.",
  prac="Interpret education for sustainable development through the Advance HE and QAA guidance (std:doc:qaa-advancehe-esd-2021-guidance).",
  ben=NA_P, nb=['1.23', 'std:doc:qaa-advancehe-esd-2021-guidance'])
s('1.25', force='should', level='none', appliesTo='enterprise activities in courses', addressee='provider', about='ambitious enterprise activities',
  domain='none', award=BOTH,
  para="Enterprise and entrepreneurship education can add to forensic courses; enterprise activities should be ambitious and should require students to be creative, innovative, resilient and critical in solving problems, generating ideas and communicating issues tied to forensic practice, with placements and partnerships adding to their effect.",
  prac="Make enterprise activities ambitious: they should require students to tackle forensic problems creatively, innovatively, resiliently and critically, to generate ideas and to communicate issues; tie them to placements and outside organisations.",
  ben=('n/a', 'a duty on course design; the student-facing outcome is 1.27'), nb=['1.27', '1.26'])
s('1.27', type='outcome', force='should', level='fheq:6', appliesTo='students of the subject', addressee='learner', about='spotting openings for business or process improvement',
  domain='generic-skill', award=BOTH,
  para="Enterprise and entrepreneurial thinking will shape where forensic science goes; students should be able to spot chances to develop a business or improve a process, through study, partnerships or placements.",
  prac="Equip students to spot openings to develop a business or improve a process, whether in their studies, through partnerships or on placement.",
  ben="You should be able to spot chances to develop a business or improve how things are done, in your studies, partnerships or placements.",
  nb=['1.25', '2.11'], fw='qaa/fheq-2024/4.15.b9.1')

# ---- section 2: distinctive features
def prov(i, force, about, para, prac, nb, ben=NA_P, **k):
    k.setdefault('award', BOTH)
    s(i, force=force, level='none', appliesTo='courses in the subject and the teams that run them', addressee='provider', about=about,
      domain='none', para=para, prac=prac, ben=ben, nb=nb, **k)

prov('2.1', 'should', 'curriculum aligned to outcomes, employers and research',
  "The curriculum should let students show they have met the course's stated outcomes, with assessment aligned to them; outcomes and content should reflect what graduate employers need now; design should be refreshed often with pedagogical and scientific research and with partners such as forensic providers, police and the judiciary; and students should be supported to build knowledge and skills step by step towards independence.",
  "Align curriculum and assessment with the stated outcomes; keep outcomes and content current with what employers need, with research, and with input from partners such as police forces, forensic science providers, other investigators and the judiciary; and scaffold learning towards independence.",
  ['3.6', '2.11'])
prov('2.2', 'should', 'accessibility across the whole course',
  "Accessibility should cover every part of the course, from physical access to awareness of culture and language, and sensitivity towards victims of crime; curricula, tuition and assessment should be accessible with reasonable adjustments in place; and teaching methods should vary as widely as possible so that no student is put at a disadvantage.",
  "Make every part of the course accessible, including physical access, awareness of culture and language, and sensitivity towards victims of crime; build in reasonable adjustments; and vary teaching widely, for instance practicals with adjustments, individual risk assessments, accessible facilities, peer support and placements.",
  ['2.3', '3.29', '3.31'])
prov('2.3', 'should', 'digital accessibility of course content',
  "Digital accessibility means everyone can reach and use digital information and platforms equally, whatever their impairment; course content in text, image and sound should be accessible and understandable without discrimination.",
  "Make all digital course content, text, images and sound alike, accessible and understandable to everyone, following W3C guidance.",
  ['2.2', '3.31'])
s('2.6', type='outcome', force='will', level='fheq:6', appliesTo='joint honours students', addressee='learner', about='joint honours: the core skills of the subject',
  domain='subject-skill', award=HON,
  para="Joint honours students will achieve the core subject-specific and generic skills of forensic science, add others from their second subject, and may explore where the two overlap.",
  prac="Joint honours students will reach the core of the subject's specific and generic skills and add others from the partner subject; leave room for interdisciplinary work where they meet.",
  ben="If you study forensic science as part of a joint honours degree, you will achieve its core specific and generic skills, add others from your other subject, and may explore where the two meet.",
  nb=['4.4', '2.5'])
prov('2.9', 'should', 'flexible modes of study',
  "Providers are encouraged to offer a range of learning modes; where possible full-time, part-time and distance options should be offered, perhaps blending classroom, online and employer-based learning such as HyFlex, to widen participation and give students choice over how, what, when and where they learn.",
  "Where you can, offer full-time, part-time and distance routes and consider blended or HyFlex delivery that mixes classroom, online and workplace learning, so that more people can take part and students have choice.",
  ['2.10', '3.7'])
prov('2.10', 'should', 'support plans and delivery contingency',
  "Flexibility should include a plan to support students with protected characteristics, or whose circumstances change, to finish the course, and a plan for sudden changes of delivery such as moving wholly online; practical teaching may then be reshaped, for example into blocks.",
  "Plan how to support students with protected characteristics or changed circumstances to complete, and keep a contingency for an abrupt move to online delivery, which may mean regrouping practical work into blocks.",
  ['2.9', '1.19'])
prov('2.11', 'should', 'partnerships with forensic employers',
  "Providers should be encouraged to build partnerships with forensic employers and wider organisations so that course activities connect with real work, preparing students for the workplace and its skills while helping employers recruit and keep staff.",
  "Build links with forensic employers (police and other law enforcement, private forensic service providers) and other organisations, so course work connects with real workplaces and students develop self-reliance, critical thinking, teamwork and problem-solving.",
  ['2.12', '2.13', '1.27'])
s('2.13', force='should', level='none', appliesTo='work placements taken as part of a course', addressee='both', about='a clear programme of learning on placement',
  domain='none', award=BOTH,
  para="A work placement that a student chooses should have a clear programme of learning; typical tasks include quality assurance, data analysis, basic examinations, administering evidence and project work.",
  prac="Give any placement a clear programme of learning; typical placement work includes quality assurance, data analysis, basic examination, administering evidence and set projects.",
  ben="If you choose a work placement, it should come with a clear programme of learning, often covering tasks such as quality checks, data analysis, basic examinations and handling evidence.",
  nb=['2.11', '2.12'], when='a student is weighing up a placement or a programme team is setting one up')
prov('2.14', 'will', 'external reference points in review',
  "Monitoring and periodic review are central to quality assurance; degree-awarding bodies will draw on external reference points, this statement among them, to keep their provision in line with sector norms.",
  "Use this statement, with the other external reference points, in monitoring and periodic review to keep the course in line with sector norms.",
  ['2.16', '2.17', '2.18'])
prov('2.15', 'will', 'collaboration with examiners, students and professional bodies',
  "Forensic science degrees will work with external examiners, students and outside partners to improve the learning experience; close links with bodies such as the Forensic Science Regulator and the Chartered Society of Forensic Sciences keep content relevant.",
  "Work with external examiners, student cohorts and partners, and stay close to bodies such as the Forensic Science Regulator and the Chartered Society of Forensic Sciences, so that content stays relevant.",
  ['2.14', '3.1'])
prov('2.16', 'will', 'external reviewers in periodic review',
  "Providers will use external reviewers in periodic review to bring an outside view of proposed changes, confirm threshold standards are met and check that content suits the subject.",
  "Bring external reviewers into periodic review to test proposed changes, confirm threshold standards and check that content suits the subject.",
  ['2.14', '2.17', '4.2'])
prov('2.18', 'should', 'stakeholders and findings in monitoring',
  "Forensic science's professional outcomes may also need evaluation and accreditation by professional and regulatory bodies, usually through visits and desk review; monitoring and evaluation should identify the right stakeholders and share findings on learning, teaching and assessment so courses respond to changing cohorts, experience and practice.",
  "Identify the right stakeholders in monitoring and evaluation, share what you learn about learning, teaching and assessment, and expect professional accreditation through visits and desk review.",
  ['2.14', '2.15', '1.4'])

# ---- section 3: content and delivery (paragraphs)
prov('3.3', 'should', 'a mix of teaching and learning practices',
  "A mix of teaching and learning practices should let learners grow in knowledge, understanding and academic and professional skill; methods may run from lectures and practicals to simulations, fieldwork, problem-based learning and learning at work.",
  "Combine approaches (pedagogy and andragogy) so learners grow in knowledge and in academic and professional skill: lectures, practicals, seminars, mock scenes and courtrooms, case studies, debates, fieldwork, problem-based and work-based learning among them.",
  ['3.4', '3.7'])
prov('3.4', 'should', 'practical classes and their purpose',
  "Practicals in laboratories or computer rooms should back up the taught curriculum and build transferable technical and practical skills, including forensic experimental methods, their scientific basis and ways of handling uncertainty through data handling and statistics; contemporaneous records and reports are likely to be stressed.",
  "Use practicals to support taught content and build transferable technical skill: forensic experimental methods and their basis, data handling and statistics for probabilistic inference, and contemporaneous records and reports.",
  ['3.3', '3.18', '3.22.b1'])
s('3.5', force='describes', level='fheq:7', appliesTo="master's students", addressee='learner', about="research methods and an extended project at master's level",
  domain='subject-skill', award=MA,
  para="At master's level students are expected to gain research-methods experience, read and interpret published research, and to complete extended project work ending in an independent original report, such as a journal-style article or thesis.",
  prac="At master's level, expect experience of research methods, reading and interpreting research publications, and an extended project written up as an independent original report, for example as a journal article or a thesis.",
  ben="On a master's course, you can expect to use research methods, read and interpret research papers, and complete an extended project written up as your own original report.",
  nb=['1.7.b3', '3.23.b4', '4.11.b4'])
prov('3.6', 'should', 'design for outcomes; current staff and content',
  "Teaching and learning should be designed so students can show they meet the stated outcomes, with aligned assessment and the skills employers need; strategies should be reviewed as pedagogy and technology move on; teaching staff will need regular professional development to stay current; and subject content should rest on the latest research, practice and regulation.",
  "Design teaching around the stated outcomes and aligned assessment, review it as pedagogy and technology advance, keep teaching staff current through regular professional development, and ground content in current research, innovation, practice and regulation.",
  ['2.1', '3.7'])
prov('3.7', 'should', 'student-centred, active delivery',
  "Delivery may be live or recorded, on campus or remote; wherever possible sessions should be student-centred and use active learning for inclusion, application and engagement, and design should consider technology that enriches learning and problem-solving.",
  "Make sessions student-centred and active where you can, and use hardware and software to give students more chances to apply what they know to problems, whatever the mode of delivery.",
  ['2.9', '3.3'])

# ---- 3.8: knowledge across the process (lead-in: students should be expected to work safely and demonstrate)
def k38(n, vp, **k):
    s('3.8.b%d' % n, type='outcome', force='should', forceFrom='3.8', level='fheq:6', appliesTo='students of the subject', addressee='learner', award=BOTH,
      para='Throughout the process from scene to court, students should work safely and show %s.' % vp,
      prac='Across the whole process from scene to court, students should work safely and show %s.' % vp,
      ben='From scene to court, you should work safely and show %s.' % you(' ' + vp).strip(), **k)
k38(1, "an understanding of current ISO standards, the law and the Forensic Science Regulator's codes and guidance, impartiality and disclosure included", about='standards, law and the Regulator\'s codes', domain='knowledge', nb=['1.6.b5', '4.4.b21'])
k38(2, 'familiarity with professional ethics: respect for the codes of practice and conduct, the standards and rules, and their responsibilities', about='professional ethics and codes', domain='understanding', nb=['3.28', '4.4.b12'])
k38(3, 'knowledge and understanding of the kinds of cognitive bias, what they lead to (cumulative effects included) and how to reduce them', about='cognitive bias and its mitigation', domain='understanding', nb=['4.4.b5', '1.6.b8'])
k38(4, 'an understanding of approaches such as Case Assessment and Interpretation and the ability to use them in building and delivering a forensic strategy', about='Case Assessment and Interpretation in forensic strategy', domain='subject-skill', nb=['4.4.b22', '3.24.b4'])

def lrn(i, force, about, domain, para, prac, ben, nb, **k):
    k.setdefault('award', BOTH); k.setdefault('level', 'fheq:6'); k.setdefault('type', 'outcome')
    s(i, force=force, appliesTo='students of the subject', addressee='learner', about=about, domain=domain, para=para, prac=prac, ben=ben, nb=nb, **k)

lrn('3.9', 'should', 'criminal justice and legal systems', 'knowledge',
  "Students should be expected to know the UK's criminal justice and legal systems and appreciate those elsewhere, including adversarial and inquisitorial approaches, how forensic science and expert witnesses (defence scientists among them) work within them, and the legal standards for recovering, storing, keeping, analysing and disposing of evidence.",
  "Students should come to know the UK criminal justice and legal systems and appreciate systems abroad: adversarial and inquisitorial models, the place of forensic science and the expert witness (defence scientists included), and the legal standards that govern evidence from recovery to disposal.",
  "You should come to know how the UK's criminal justice and legal systems work and how others differ, how forensic scientists and expert witnesses fit into them, and the legal rules for handling evidence from recovery to disposal.",
  ['1.6.b9', '3.20', '4.4.b8'])
lrn('3.10', 'threshold', 'basic knowledge of all three components', 'knowledge',
  "Courses may weight the three components (scene investigation, laboratory analysis, and interpretation, evaluation and presentation) differently, but every student is expected, as a minimum, to have a basic knowledge of all three at a level fitting the degree.",
  "Whatever the course's emphasis, make sure every student gains at least a basic knowledge of all three components: scene investigation, laboratory analysis, and interpreting, evaluating and presenting evidence.",
  "Whatever your course focuses on, you will need at least a basic knowledge of all three areas: scene investigation, laboratory analysis, and interpreting, evaluating and presenting evidence.",
  ['1.14', '3.11', '3.12', '3.13'], type='expectation')
lrn('3.11', 'will', 'scene investigation: imaging, roles and information exchange', 'knowledge',
  "Scene investigation covers the principles and safe practice of the techniques for planning scene examinations, from recognising, prioritising, recording and preserving evidence to recovering, storing and interpreting it and controlling contamination; students will gain, as their course requires, an understanding of imaging, scene photography above all, and of the roles, duties and liabilities of the people and agencies at a scene and how they share information.",
  "Students will come to understand, as suits the course, imaging and scene photography and the roles, duties and liabilities of everyone at a scene and how they exchange information, within safe, contamination-aware scene strategy.",
  "You will learn, as your course requires, how imaging and scene photography work, who does what at a scene, what each is responsible and liable for, and how they share information.",
  ['4.5.b1', '4.5.b2', '3.24.b3'])
lrn('3.12', 'will', 'laboratory methods, control samples and databases', 'knowledge',
  "Laboratory work needs competence in choosing and applying methods to find, identify, recover, examine, compare, extract and analyse common physical, chemical, biological and digital materials, with proper storage and safe practice, knowledge of each method's theory and limits, and attention to validation and calibration; students will also know the principles and use of control and reference samples and of databases for identifying materials.",
  "Students will know the principles and use of control and reference samples and of identification databases, alongside competent, safe, validated and calibrated use of the main laboratory methods.",
  "You will understand how control and reference samples work and how databases help identify materials, alongside using the main laboratory methods safely, with proper validation and calibration.",
  ['4.5.b3', '4.5.b4', '3.22.b1'])
lrn('3.13', 'will', 'interpreting, reporting and defending findings', 'subject-skill',
  "Interpretation, evaluation and presentation rest on accepted methods, logical evaluation by the likelihood ratio above all, suitable statistics and databases, and an understanding of what makes outcomes uncertain; students will be able to interpret findings and reach conclusions, keep factual apart from expert reporting, form expert opinion, write impartial and complete reports in formats fit for investigators and courts, and explain and defend a report in court, orally and in writing.",
  "Students will be able to interpret findings and reach conclusions, separate factual from expert reporting, form expert opinion, write impartial reports for investigators and the court in different formats, and defend a report orally and in writing, using likelihood-ratio evaluation and an understanding of uncertainty.",
  "You will be able to interpret findings and draw conclusions, keep the facts apart from expert opinion, write impartial reports for investigators and courts, and explain and defend your report in court, in speech and in writing.",
  ['1.17', '4.4.b17', '4.4.b18', '4.4.b20'])
lrn('3.14', 'describes', 'the underpinning sciences', 'knowledge',
  "The three core components rest on science drawn mainly from chemistry, biology, physics, mathematics and computer science, and from law, the list being open; courses may weight these differently, but basic knowledge of the underpinning sciences fitting the course is expected, and digital forensics courses are expected to have suitable scientific and mathematical grounding.",
  "Make sure students gain basic knowledge of the sciences the course rests on (chemistry, biology, physics, mathematics, computer science, law); digital forensics courses need their own scientific and mathematical grounding.",
  "You can expect to gain a basic knowledge of the sciences your course rests on, such as chemistry, biology, physics, mathematics, computing and law.",
  ['3.15', '3.16', '3.17', '3.18', '3.19', '3.20', '4.4.b1'])
lrn('3.15', 'should', 'chemistry: analytical and microscopic techniques', 'subject-skill',
  "In chemistry, students should be able to choose, use and interpret analytical and microscopic techniques to find analytes and to identify, compare and characterise materials in forensic work, and should understand how those techniques work, their limits and the chemistry that may be going on.",
  "Students should be able to choose, apply and interpret analytical and microscopic techniques for forensic samples, and understand how the techniques work, where their limits lie and what chemical interactions are involved.",
  "In chemistry, you should be able to choose and use analytical and microscope techniques, interpret their data to identify and compare materials, and understand how the techniques work and where their limits lie.",
  ['3.14', '4.4.b4', '4.5.b4'])
prov('3.16', 'should', 'biology in the curriculum',
  "The biology taught should include practical microscopy, molecular biology and biochemistry (body fluids, nucleic acids, proteins, enzymes, molecular genetics, genomics, inheritance) and forensic genetic techniques such as STR profiling, and may include anatomy, forensic medicine, entomology, microbiology, palynology, botany and anthropology.",
  "Include in biology practical microscopy, molecular biology and biochemistry with stress on body fluid identification and genetics, and STR profiling; anatomy, forensic medicine and fields such as entomology or palynology are options.",
  ['3.14', '3.15', '3.17'], ben=('n/a', 'a content duty on the course; the student meets it as curriculum'))
prov('3.17', 'should', 'physics in the curriculum',
  "Physics should include elementary optics and microscopy, the mechanics behind projectiles, ballistics, explosions and blood dynamics, the physical properties of materials, and enough electromagnetism, atomic structure and radiation to understand instrumental analysis, forensic photography and imaging.",
  "Teach the physics forensic work draws on: optics and microscopy, mechanics for ballistics, explosions and bloodstain dynamics, material properties, and the electromagnetism, atomic structure and radiation that instrumental analysis and imaging rely on.",
  ['3.14', '3.16', '3.18'], ben=('n/a', 'a content duty on the course; the student meets it as curriculum'))
prov('3.18', 'should', 'mathematics and statistics in the curriculum',
  "Mathematics should give enough skill with functions, algebra and trigonometry for the course's science; statistics should give a working grasp of statistical methods and probability for experimental data and its uncertainty, sampling and method uncertainty, and the likelihood ratio approach to evaluating evidence for court, with frequency data and databases.",
  "Teach enough functions, algebra and trigonometry for the science, and working statistics: probability, experimental uncertainty, sampling and method uncertainty, and likelihood-ratio evaluation of evidence for court using frequency data and databases.",
  ['3.14', '4.4.b1', '4.4.b18'], ben=('n/a', 'a content duty on the course; the student meets it as curriculum'))
prov('3.19', 'should', 'digital forensics in the curriculum',
  "Digital forensics builds on computer science principles such as data representation, coding in at least one language, networks and protocols, security and relational databases; the course should go on to reverse engineering of unfamiliar data, linking artefacts from separate sources into a timeline of user activity, and telling circumstantial from probative evidence.",
  "Ground digital forensics in computer science (data representation, a programming language such as Python, networks and protocols, security, relational databases) and build up to reverse engineering unfamiliar data, timelines from linked artefacts, and weighing circumstantial against probative evidence.",
  ['3.14', '4.5.b5', '4.5.b6', '4.5.b8'], ben=('n/a', 'a content duty on the course; the student meets it as curriculum'))
prov('3.20', 'describes', 'law in the curriculum',
  "The law taught would be expected to cover criminal law, relevant legislation, jurisdiction and procedure within a justice system, the expert witness, and the statutes governing practice, such as the Data Protection Act 2018, the Police and Criminal Evidence Act 1984 and the criminal procedure rules and practice directions of 2020.",
  "Cover criminal law, jurisdiction and procedure, the expert witness's role, and the legislation that governs practice, such as the Data Protection Act 2018, PACE 1984 and the criminal procedure rules.",
  ['3.9', '3.14', '4.4.b8'], ben=('n/a', 'a content duty on the course; the student meets it as curriculum'))

# ---- outcome lists 3.22 to 3.27 (lead-ins: a course should be designed to enable students to ...)
def ol(stem, n, vp, domain, about, ma=False, **k):
    if ma:
        s('%s.b%d' % (stem, n), type='outcome', force='should', forceFrom=stem, level='fheq:7', appliesTo="master's students", addressee='learner', award=MA,
          para="A master's course should also be designed so that students can %s." % vp,
          prac="Design the master's course so that, beyond the honours abilities, students can %s." % vp,
          ben="If you take a master's, your course should also help you %s." % you(' ' + vp).strip(), domain=domain, about=about, **k)
    else:
        s('%s.b%d' % (stem, n), type='outcome', force='should', forceFrom=stem, level='fheq:6', appliesTo='students of the subject', addressee='learner', award=BOTH,
          para='A course should be designed so that students can %s.' % vp,
          prac='Design the course so that students can %s.' % vp,
          ben='Your course should help you %s.' % you(' ' + vp).strip(), domain=domain, about=about, **k)

ol('3.22', 1, 'work safely and well in a laboratory: assessing risk competently, following written procedures, calibrating where needed and recording methods and results reliably', 'subject-skill', 'safe, effective laboratory work', nb=['4.4.b3', '4.4.b14'])
ol('3.22', 2, 'use advanced laboratory equipment with confidence where it applies, learn new facilities, and understand the principles behind the instruments', 'subject-skill', 'advanced equipment and instrument principles', nb=['4.4.b4'])
ol('3.22', 3, 'see why tasks must be done consistently, reproducibly and traceably', 'understanding', 'consistent, reproducible, traceable work', nb=['4.4.b15', '3.24.b2'])
ol('3.22', 4, 'evaluate and critically interpret results by solving problems: finding the relevant scientific principles, planning how to solve them and presenting conclusions as text, tables or graphs', 'subject-skill', 'interpreting results through problem-solving', nb=['4.4.b7'])
ol('3.22', 5, 'plan, carry out and report a scientific investigation, analysing the data critically and judging how uncertain it is', 'subject-skill', 'planning and reporting an investigation', nb=['4.4.b19', '4.4.b10'])
ol('3.22', 6, 'use scientific method on scientific problems, forming a hypothesis and designing experiments to test it', 'subject-skill', 'hypotheses and experimental design', nb=['1.6.b16', '4.4.b4'])
ol('3.22', 7, 'analyse and organise data with ICT, using the software that goes with instruments and working with databases', 'generic-skill', 'ICT for data analysis', nb=['3.26.b5'])
ol('3.23', 1, 'work safely and well in a laboratory with little direct supervision', 'subject-skill', 'laboratory work with minimal supervision', ma=True, nb=['3.22.b1', '4.11.b7'])
ol('3.23', 2, 'apply and adapt problem-solving to situations that are unfamiliar, complex, poorly defined and open-ended', 'generic-skill', 'problem-solving in unfamiliar, open-ended situations', ma=True, nb=['4.11.b6', '3.27.b1'])
ol('3.23', 3, 'plan, design and run new experimental procedures on their own', 'subject-skill', 'designing new experimental procedures', ma=True, nb=['4.11.b7'])
ol('3.23', 4, 'plan, design, conduct and report a research project on their own', 'subject-skill', 'an independent research project', ma=True, nb=['4.11.b4', '3.5'])
ol('3.24', 1, 'see why standards and codes of conduct are needed and why keeping to them matters', 'understanding', 'why standards and codes matter', nb=['3.8.b1', '4.4.b15'])
ol('3.24', 2, 'work well in a team and inside a formal system, following the relevant quality assurance procedures', 'subject-skill', 'teamwork within a quality system', nb=['4.5.b2', '4.4.b15'])
ol('3.24', 3, 'record, recover, analyse, evaluate, interpret, preserve and present potential evidence', 'subject-skill', 'the handling of potential evidence from record to presentation', nb=['4.5.b1', '4.4.b17'])
ol('3.24', 4, 'build efficient strategies for examining a case', 'subject-skill', 'case-examination strategies', nb=['4.4.b22', '3.8.b4'])
ol('3.24', 5, 'apply competent procedures that keep evidence intact and its continuity unbroken', 'subject-skill', 'integrity and continuity of evidence', nb=['4.4.b23', '1.6.b8'])
ol('3.24', 6, 'present impartially, in writing and in speech, in ways suited to legal, court and policing settings', 'subject-skill', 'impartial presentation for legal settings', nb=['4.4.b20', '1.17'])
ol('3.24', 7, 'keep to safe working practice, for themselves and others', 'subject-skill', 'safe working practice', nb=['4.4.b14'])
ol('3.24', 8, 'appreciate the particular issues, legal framework and practice for digital evidence and trace materials, human and other biological tissue and DNA included, with reference to the Human Tissue Act 2004', 'understanding', 'digital evidence, trace materials and the Human Tissue Act', nb=['4.4.b13'])
ol('3.24', 9, 'be aware of what modern technology, databases and digital forensics (such as data taken from phones and computers) mean for the field', 'understanding', 'implications of technological advances', nb=['1.6.b13', '4.5.b5'])
ol('3.24', 10, "appreciate a forensic practitioner's ethical, legal and commercial responsibilities and the quality assurance and validation that professional competence requires", 'understanding', 'practitioner responsibilities, quality and validation', nb=['4.4.b12', '4.4.b15'])
ol('3.25', 1, 'gain deep experience of an apt range of forensic methods and take a critical approach to them', 'subject-skill', "deep, critical experience of forensic methods", ma=True, nb=['4.11.b1', '1.7.b1'])
ol('3.25', 2, 'be open and inventive towards new and emerging forensic procedures and techniques', 'subject-skill', 'openness to new procedures and techniques', ma=True, nb=['4.11.b7'])
ol('3.25', 3, 'understand the moral and ethical questions forensic practice raises', 'understanding', 'moral and ethical issues in practice', ma=True, nb=['4.11.b8', '3.28'])
ol('3.26', 1, 'build personal and academic resilience by paying attention to their own well-being and that of others', 'generic-skill', 'resilience and well-being', nb=['4.4.b16'], fw='qaa/fheq-2024/4.15.b9.1')
ol('3.26', 2, 'investigate on their own, drawing on many sources of information and using critical judgement', 'generic-skill', 'independent investigation from many sources', nb=['4.5.b7', '1.6.b14'], fw='qaa/fheq-2024/4.15.b7')
ol('3.26', 3, 'communicate complex ideas and information concisely and well, orally and in writing, and interact effectively across many professional settings', 'generic-skill', 'communication across professional settings', nb=['4.4.b16', '4.4.b20'])
ol('3.26', 4, 'analyse with attention to detail, build logical arguments from incomplete data and use technical language correctly', 'generic-skill', 'analytical skills', nb=['4.4.b10', '4.4.b18'], fw='qaa/fheq-2024/4.15.b7')
ol('3.26', 5, 'use ICT well, including databases, software packages and modern means of communication', 'generic-skill', 'ICT skills', nb=['3.22.b7'], fw='qaa/fheq-2024/4.15.b8')
ol('3.26', 6, 'work alone and in a team, and plan, organise and complete work efficiently, conscientiously and on time', 'generic-skill', 'independent and team working; managing time', nb=['3.24.b2'], fw='qaa/fheq-2024/4.15.b9.1')
ol('3.26', 7, 'see where further training or new skills would help them improve, and reflect on it', 'generic-skill', 'reflective personal development', nb=['1.6.b7'], fw='qaa/fheq-2024/4.15.b5')
ol('3.26', 8, 'understand how to put good practice in equality, diversity and inclusion into effect', 'generic-skill', 'applying good practice in equality, diversity and inclusion', nb=['1.19', '3.28.b5'], fw='qaa/fheq-2024/4.15.b9.1')
ol('3.27', 1, 'solve problems with self-direction and originality', 'generic-skill', 'self-directed, original problem-solving', ma=True, nb=['4.11.b6', '3.23.b2'])
ol('3.27', 2, 'take a self-critical approach to planning, doing and reporting investigations', 'generic-skill', 'a self-critical approach to investigation', ma=True, nb=['4.11.b3'])
ol('3.27', 3, 'interpret complex technical information with competence and convey it across a wide variety of professional settings', 'generic-skill', 'interpreting and conveying complex information', ma=True, nb=['4.11.b9'], fw='qaa/fheq-2024/4.17.b5')
ol('3.27', 4, 'keep learning on their own for continuing professional development', 'generic-skill', 'independent learning for professional development', ma=True, nb=['4.11.b10', '1.7.b7'], fw='qaa/fheq-2024/4.17.b7')

# ---- 3.28: ethical behaviour (stem and items)
lrn('3.28', 'should', 'fabrication and misrepresentation are unethical', 'understanding',
  "Students should fully understand that inventing, falsifying, misrepresenting or wilfully misreading evidence, data or experimental results is unethical and unacceptable, and course materials should say so.",
  "Make sure students fully understand, and course materials state, that fabricating, falsifying, misrepresenting or wilfully misreading evidence, data or results is unethical and unacceptable.",
  "You should fully understand that making up, falsifying, misrepresenting or deliberately misreading evidence, data or experimental results is unethical and never acceptable.",
  ['3.28.b2', '4.4.b12', '1.6.b5'])
def e28(n, vp, domain, about, **k):
    s('3.28.b%d' % n, type='outcome', force='should', forceFrom='3.28', level='fheq:6', appliesTo='students of the subject', addressee='learner', award=BOTH,
      para='Students should also %s.' % vp, prac='Expect students, and help them, to %s.' % vp, ben='You should also %s.' % you(' ' + vp).strip(), domain=domain, about=about, **k)
e28(1, 'understand how serious the results of careless or poor practice can be', 'understanding', 'consequences of careless practice', nb=['4.4.b14', '4.4.b23'])
e28(2, 'be objective, impartial and honest in every part of their work', 'generic-skill', 'objectivity and honesty', nb=['4.4.b20', '3.24.b6'], fw='qaa/fheq-2024/4.15.b9.1')
e28(3, 'recognise and admit where their knowledge ends', 'generic-skill', 'the limits of one\'s knowledge', nb=['4.4.b7'], fw='qaa/fheq-2024/4.15.b4')
e28(4, 'recognise plagiarism as unethical conduct', 'understanding', 'plagiarism as unethical', nb=['3.28'])
e28(5, 'know the law on equality and diversity', 'knowledge', 'equality and diversity legislation', nb=['1.19', '3.26.b8'])
e28(6, "know the ethical questions, legal rules and procedures in research, especially with animals or people or with a person's data", 'understanding', 'research ethics and data', nb=['3.24.b8', '4.4.b13'])

# ---- assessment and the rungs' introduction
prov('3.29', 'should', 'varied assessment and reasonable adjustments',
  "A forensic curriculum is expected to use varied assessment that builds a broad, current set of skills for later careers; assessment may be formative or summative, in person or online; and reasonable adjustments for disabled students should be made across all assessment as each student needs.",
  "Use a wide mix of assessment formats, formative and summative, in person or online, and make reasonable adjustments for disabled students across all assessment, as their needs require.",
  ['3.31', '2.2'])
prov('3.30', 'will', 'what assessment tests',
  "Assessment will test subject knowledge and the generic and subject-specific skills in the course outcomes; some will test organising and completing work and communicating under time pressure, and some should let students show reflection, originality, creativity and the integration of knowledge into practice.",
  "Assess knowledge and both kinds of skill named in the outcomes; include some timed tasks testing organisation and communication under pressure, and some that let students show reflection, originality, creativity and knowledge put into practice.",
  ['3.29', '3.31', '4.2'])
prov('3.31', 'should', 'briefs, criteria and inclusive assessment design',
  "Students should receive each assessment through a brief with marking criteria mapped to the outcomes, and may co-create some assessments; assessment should be inclusive, using good digital accessibility practice and meeting needs such as hearing impairment and colour blindness, anticipating needs rather than relying on alternatives, and it matters that any alternative still lets students show the outcomes.",
  "Issue a brief with criteria mapped to the outcomes; design assessments inclusively from the start, with digital accessibility good practice and attention to needs such as hearing impairment and colour blindness; and make sure any alternative still lets students show the outcomes.",
  ['3.29', '2.2', '2.3'])
prov('3.33', 'should', 'prompt feedback and action planning',
  "Feedback should come promptly so that students engage with it, and the statement suggests the curriculum give students visible chances to make and act on their own development plans.",
  "Return feedback promptly, and build in visible points where students make and carry out action plans for their development.",
  ['3.32', '3.26.b7'])
prov('4.2', 'should', 'the three rungs and Annex D',
  "Each set of standards is split into threshold, typical and excellent and describes individual performance; the threshold is the core, reached by anyone gaining an honours degree, and most students are expected to reach the typical rung; each provider decides what counts as evidence of achievement and should refer to Annex D, which describes the degree classes at FHEQ level 6 and FQHEIS level 10.",
  "Read the three rungs as individual performance: the threshold is what every honours graduate reaches and typical is where most should land; set your own evidence of achievement and refer to Annex D of the frameworks for the four classes (1st, 2:1, 2:2, 3rd).",
  ['4.4', '4.6', '4.8'], award=HON, fwp='qaa/fheq-2024/annex-d/summary/r1/3rd and SL6 of std:doc:qaa-fheq-2024-framework')
s('4.10', force='will', level='fheq:7', appliesTo="integrated master's students", addressee='learner', about="integrated master's: typical honours and beyond",
  domain='none', award=IMA,
  para="An integrated master's joins bachelor's and master's study, so its students are expected to have reached at least the typical rung of the honours outcomes and will have taken their knowledge, skills and understanding on into master's-level outcomes.",
  prac="Integrated master's students will reach at least the typical honours rung (4.6 and 4.7) and go beyond it into master's outcomes (4.11).",
  ben="On an integrated master's, you are expected to reach at least the typical level of the honours outcomes and then go further, into master's-level knowledge and skills.",
  nb=['4.6', '4.7', '4.11'])

# ---------------------------------------------------------------- the rungs: 4.4 to 4.9 (honours) and 4.11 (master's)
# Each outcome once, with our noun phrase at each rung; ids by rung list. Generic items 22 and 23 swap places between 4.4 and 4.6/4.8.
RUNGW = {'threshold': ('the threshold (third-class honours)', 'To reach the threshold for honours (a third),'),
         'typical': ('the typical rung (a 2:2 or 2:1)', 'At the typical level (a 2:2 or 2:1),'),
         'excellent': ('the excellent rung (first-class honours)', 'At the excellent level (a first),')}
GEN = [  # (outcome, domain, about, threshold, typical, excellent)
 ('the sciences behind forensic work', 'knowledge', 'the sciences, mathematics and statistics behind forensic work',
  'knowledge and understanding of the sciences that forensic investigation draws on, mathematics and statistics among them, with Bayesian reasoning and likelihood ratios',
  'strong knowledge and understanding of the sciences behind forensic investigation, mathematics and statistics included, with Bayesian reasoning',
  'consistent, detailed command of the sciences behind forensic investigation, mathematics, statistics and Bayesian reasoning included'),
 ('forensic techniques', 'knowledge', 'forensic techniques',
  'knowledge of the techniques forensic science uses', 'thorough knowledge of the techniques forensic science uses', 'detailed and thorough command of the techniques forensic science uses'),
 ('laboratory skills and autonomy', 'subject-skill', 'laboratory skills and autonomy',
  'laboratory skills for a range of tasks and technical processes, done with some autonomy',
  'laboratory skills for every kind of task and technical process, done largely on their own',
  'the confidence and laboratory skill for every kind of task and technical process, done with a high degree of autonomy'),
 ('practical laboratory experiments', 'subject-skill', 'choosing and running laboratory experiments',
  'choosing and running practical laboratory experiments for forensic investigations, using suitable equipment',
  'effective choice and running of such experiments, with confident use of the right equipment',
  'critical choice, development and running of such experiments, with confident use of the right equipment'),
 ('cognitive bias', 'understanding', 'cognitive bias in forensic processes',
  'knowledge of the kinds of cognitive bias and how they can distort forensic processes',
  'strong knowledge of cognitive bias and its effects on forensic processes, and the skill to spot it and apply ways to reduce it across a range of cases',
  'detailed knowledge of cognitive bias and its effects, and critical skill in spotting it and applying ways to reduce it across a wide range of cases'),
 ('scene investigation issues and techniques', 'knowledge', 'scene investigation issues and techniques',
  'a range of knowledge of the broad issues and methods of scene investigation', 'thorough knowledge of the broad issues and methods of scene investigation',
  'wide-ranging, critical knowledge of the broad issues and methods of scene investigation'),
 ('interpreting results and their limits', 'subject-skill', 'interpreting results within their limits',
  'interpretation of laboratory and other results with a sense of their limits, with the hierarchy of propositions and hypotheses at activity level',
  'interpretation of laboratory and other results with a thorough sense of their limits',
  'consistent interpretation of laboratory and other results with a thorough, critical sense of their limits'),
 ('legal and policing settings', 'knowledge', 'legal and law enforcement settings of practice',
  'knowledge of the legal and policing settings in which forensic science is practised, work across jurisdictions included',
  'strong knowledge of the legal and policing settings in which forensic science is practised, work across jurisdictions included',
  'extensive knowledge of the legal and policing settings in which forensic science is practised, work across jurisdictions included'),
 ('intelligence and evidential value', 'understanding', 'intelligence value against evidential value',
  'understanding of how the intelligence value of a forensic finding differs from its evidential value',
  'thorough understanding of how the intelligence value of a forensic finding differs from its evidential value',
  'exceptional understanding of how the intelligence value of a forensic finding differs from its evidential value'),
 ('recording, deduction and presentation', 'subject-skill', 'recording, deducing and presenting results for legal audiences',
  'accurate recording of results, orderly data, sound deductions and clear written and spoken presentation of findings in a form legal, policing or court audiences can take in',
  'accurate recording, orderly data, rational deductions and clear written and spoken presentation of complex investigations for legal, policing or court audiences',
  'consistently accurate recording, critically organised data, rational deductions and clear written and spoken presentation of complex investigations for legal, policing or court audiences'),
 ('how the discipline advances', 'understanding', 'how progress is made in the discipline',
  'an appreciation of how the discipline advances', 'a strong appreciation of how the discipline advances', 'an exceptional, critical appreciation of how the discipline advances'),
 ('ethical and legal duties', 'understanding', 'the ethical and legal duties of forensic science',
  'knowledge of the ethical and legal duties that bind science, forensic science above all, and commitment to meeting them',
  'thorough knowledge of the ethical and legal duties that bind science, forensic science above all, and a consistent commitment to meeting them',
  'extensive knowledge of the ethical and legal duties that bind science, forensic science above all, and a consistent commitment to meeting them'),
 ('human tissue, DNA, digital data and trace material', 'understanding', 'handling human tissue, DNA, digital data and trace material',
  'knowledge, understanding and respect for what handling, storing and examining human tissue, DNA, digital data and other trace material involves',
  'strong knowledge, understanding and respect for what handling, storing and examining human tissue, DNA, digital data and other trace material involves',
  'advanced knowledge, critical understanding and respect for what handling, storing and examining human tissue, DNA, digital data and other trace material involves'),
 ('safe working', 'subject-skill', 'safe working at scenes and in the laboratory',
  'competent safe working at scenes and in the laboratory, for themselves and others',
  'consistent, well-developed competence in safe working at scenes and in the laboratory, for themselves and others',
  'consistent, exemplary competence in safe working at scenes and in the laboratory, for themselves and others'),
 ('quality assurance', 'understanding', 'quality assurance procedures',
  'an appreciation of quality assurance procedures in forensic science', 'a thorough appreciation of quality assurance procedures in forensic science',
  'a critical appreciation of quality assurance procedures in forensic science'),
 ('communication', 'generic-skill', 'spoken and written communication',
  'spoken and written communication that others can follow', 'highly proficient spoken and written communication', 'accomplished spoken and written communication'),
 ('interpreting and communicating evidence in casework', 'subject-skill', 'interpreting and communicating evidence in casework',
  'interpretation and communication of forensic evidence and experimental results in casework, expert opinion included',
  'management, critical interpretation and clear communication of forensic evidence and results in casework, expert opinion included',
  'consistent, effective management, critical interpretation and clear communication of forensic evidence and results in casework, expert opinion included'),
 ('expert opinion', 'subject-skill', 'forming and justifying expert opinion',
  'expert opinion formed and justified through transparent argument, using the likelihood ratio where it fits',
  'consistent forming and justifying of expert opinion through transparent argument, using the likelihood ratio where it fits',
  'exceptional skill in forming and justifying expert opinion through transparent argument, using the likelihood ratio where it fits'),
 ('uncertainty', 'subject-skill', 'appraising and conveying uncertainty',
  'appraising, quantifying and clearly reporting the uncertainty in expert opinion or the data behind it',
  'consistent appraisal, quantification and clear reporting of the uncertainty in expert opinion or the data behind it',
  'critical appraisal, quantification and consistently clear reporting of the uncertainty in expert opinion or the data behind it'),
 ('reports', 'subject-skill', 'impartial oral and written reports',
  'impartial, clear and complete oral and written reports fit for a wide variety of legal and policing settings, those involving the public included',
  'impartial, clear and complete oral and written reports of high quality across legal and policing settings, those involving the public included',
  'consistently impartial, clear and complete oral and written reports of exceptional quality across legal and policing settings, those involving the public included'),
 ('best practice and legal standards for evidence', 'knowledge', 'best practice and legal standards for evidence',
  'working knowledge of current industry best practice and the legal standards for evidence, digital data included',
  'strong working knowledge of current industry best practice and the legal standards for evidence, digital data included',
  'comprehensive working knowledge of current industry best practice and the legal standards for evidence, digital data included'),
 ('forensic strategies', 'subject-skill', 'case-appropriate forensic strategies',
  'building, managing and delivering forensic strategies suited to the case, using the Case Assessment and Interpretation framework',
  'effective building, managing and delivering of forensic strategies suited to the case, using the Case Assessment and Interpretation framework',
  'consistent, effective building, managing and delivering of forensic strategies suited to the case, using the Case Assessment and Interpretation framework'),
 ('contamination avoidance', 'subject-skill', 'avoiding contamination',
  'following procedures that avoid contamination, in handling digital data too',
  'consistently following procedures that avoid contamination, in handling digital data too',
  'consistent, exceptional adherence to procedures that avoid contamination, and their development, in handling digital data too'),
]
AREA = [
 ('scene techniques', 'knowledge', 'scene investigation: techniques for evidence at a scene',
  'knowledge and appreciation of the skills and techniques for recording (photography included), preserving, collecting, processing and interpreting evidence at a scene',
  'thorough knowledge and appreciation of the skills and techniques for collecting, processing, recording (with suitable photography), preserving and interpreting evidence at a scene',
  'extensive knowledge and critical appreciation of the skills and techniques for collecting, processing, recording (with suitable photography), preserving and interpreting evidence at a scene'),
 ('scene roles and teamwork', 'understanding', 'scene investigation: roles, liabilities and teamwork',
  'understanding of the duties, roles and liabilities of everyone in a scene investigation, knowing when to call in specialists, and the ability to work safely and well and contribute within that team',
  'thorough understanding of the duties, roles and liabilities of everyone in a scene investigation and the ability to work well and contribute within that team',
  'comprehensive, critical understanding of the duties, roles and liabilities of everyone in a scene investigation and a consistent ability to work well and contribute within that team'),
 ('laboratory method theory', 'knowledge', 'laboratory analysis: theory and application of methods',
  'knowledge and appreciation of the theory and use of forensic laboratory methods',
  'thorough knowledge and appreciation of the theory and use of forensic laboratory methods',
  'extensive, critical knowledge and appreciation of the theory and use of forensic laboratory methods'),
 ('laboratory method use', 'subject-skill', 'laboratory analysis: choosing and using methods',
  'choosing and using many methods to locate, identify, recover, extract and analyse common physical, digital, chemical and biological materials and marks, trace materials such as DNA included',
  'consistent skill in choosing and using many methods to locate, identify, recover, extract and analyse common physical, digital, chemical and biological materials and marks, trace materials such as DNA included',
  'consistent skill in critically choosing, using and developing many methods to locate, identify, recover, extract and analyse common physical, digital, chemical and biological materials and marks, trace materials such as DNA included'),
 ('digital devices', 'knowledge', 'digital forensics: devices that hold digital data',
  'knowledge and understanding of the main techniques and skills for searching for, identifying, preserving, moving, handling and keeping continuity of common devices that hold or may hold digital data',
  'thorough knowledge and understanding of the main techniques and skills for searching for, identifying, preserving, moving, handling and keeping continuity of common devices that hold or may hold digital data',
  'advanced knowledge and critical understanding of the main techniques and skills for searching for, identifying, preserving, moving, handling and keeping continuity of common devices that hold or may hold digital data'),
 ('digital acquisition methods', 'subject-skill', 'digital forensics: choosing and justifying acquisition and analysis methods',
  'choosing, and fully justifying, a range of methods for acquiring and analysing digital data',
  'consistent choice, fully justified, of a range of methods for acquiring and analysing digital data',
  'consistent, critical choice, fully justified, of a range of methods for acquiring and analysing digital data'),
 ('investigating to establish the truth', 'subject-skill', 'digital forensics: investigating facts from many sources',
  'an investigation that examines facts from varied sources, some needing extra reading or testing to understand, to find out the truth of an incident or allegation',
  'an effective investigation that examines facts from varied sources, some needing extra reading or testing to understand, to find out the truth of an incident or allegation',
  'an exceptional investigation that examines facts from varied sources, some needing extra reading or testing to understand, to find out the truth of an incident or allegation'),
 ('validating digital tools', 'subject-skill', 'digital forensics: reviewing, validating and verifying tools',
  'reviewing, validating and verifying the methods and tools that process digital data',
  'consistently reviewing, validating and verifying the methods and tools that process digital data',
  'consistently and critically reviewing, validating and verifying the methods and tools that process digital data'),
 ('digital forensic strategy', 'subject-skill', 'digital forensics: strategy across multiple sites',
  'building and managing a forensic strategy for searching several sites and then analysing the digital data',
  'building and managing an effective forensic strategy for searching several sites and then analysing the digital data',
  'exceptional building and managing of a forensic strategy for searching several sites and then analysing the digital data'),
]
LIST = {'threshold': ('4.4', '4.5'), 'typical': ('4.6', '4.7'), 'excellent': ('4.8', '4.9')}
GRADE = {}
OUTCOMES = []
FWG = {'knowledge': ('qaa/fheq-2024/4.15.b1', 'knowledge/r1'), 'understanding': ('qaa/fheq-2024/4.15.b4', 'knowledge/r2'),
       'subject-skill': ('qaa/fheq-2024/4.15.b2', 'practical/r1'), 'generic-skill': ('qaa/fheq-2024/4.15.b8', 'transferable/r1')}
BAND = {'threshold': ['3rd'], 'typical': ['2.2', '2.1'], 'excellent': ['1st']}
def rung_rec(i, rung, o, np_, area):
    name, dom, about = o[0], o[1], o[2]
    force = 'threshold' if rung == 'threshold' else 'will'
    lab, lead = RUNGW[rung]
    s(i, type=rung, rung=rung, force=force, forceFrom=i.split('.b')[0], level='fheq:6', appliesTo='honours graduates at %s' % lab + (' with emphasis on one area' if area else ''),
      addressee='learner', about=about, domain=dom, award=HON,
      para='Will be able to show %s.' % np_,
      prac='At %s, graduates will be able to show %s.' % (lab, np_),
      ben='%s you will be able to show %s.' % (lead, you(' ' + np_).strip()),
      outcome=name)
for gi, o in enumerate(GEN, 1):
    ids = {}
    for rung in ('threshold', 'typical', 'excellent'):
        n = gi
        if rung != 'threshold' and gi in (22, 23):
            n = 45 - gi   # 4.6 and 4.8 list contamination 22nd and strategies 23rd
        i = '%s.b%d' % (LIST[rung][0], n); ids[rung] = i
        rung_rec(i, rung, o, o[{'threshold': 3, 'typical': 4, 'excellent': 5}[rung]], False)
    GRADE[ids['typical']] = ids['threshold']; GRADE[ids['excellent']] = ids['typical']
    OUTCOMES.append(dict(outcome=o[0], threshold=ids['threshold'], typical=ids['typical'], excellent=ids['excellent'], basis='inferred', domain=o[1], award=HON))
for ai, o in enumerate(AREA, 1):
    ids = {}
    for rung in ('threshold', 'typical', 'excellent'):
        i = '%s.b%d' % (LIST[rung][1], ai); ids[rung] = i
        rung_rec(i, rung, o, o[{'threshold': 3, 'typical': 4, 'excellent': 5}[rung]], True)
    GRADE[ids['typical']] = ids['threshold']; GRADE[ids['excellent']] = ids['typical']
    OUTCOMES.append(dict(outcome=o[0], threshold=ids['threshold'], typical=ids['typical'], excellent=ids['excellent'], basis='inferred', domain=o[1], award=HON))
# neighbours for the rung records: the same outcome at the other rungs
for oc in OUTCOMES:
    trio = [oc['threshold'], oc['typical'], oc['excellent']]
    for i in trio:
        P[i]['nb'] = [x for x in trio if x != i]

# master's list 4.11 (another award, not another rung: recorded as its threshold, per the batch 1 convention)
MAS = [
 ('knowledge', 'deep specialist or broad critical knowledge', 'either deep specialist knowledge and experience of techniques in one area of forensic science, or a broad, critical view of the discipline as a whole', 'qaa/fheq-2024/4.17.b1', ['1.7.b1', '3.25.b1']),
 ('understanding', 'engagement with current research', 'active familiarity with recent and current research, its methods, findings and publications', 'qaa/fheq-2024/4.17.b4.1', ['1.7.b2', '3.5']),
 ('generic-skill', 'a self-critical approach to investigation', 'a self-critical approach to planning, doing and reporting investigations', 'qaa/fheq-2024/4.17.b6', ['3.27.b2']),
 ('subject-skill', 'an original investigation or research project', 'the capability to conceive, plan and conduct original research or investigation and report on it', 'qaa/fheq-2024/4.17.b3', ['1.7.b3', '3.23.b4', '3.5']),
 ('understanding', 'the professional setting', 'a clear view of what limits and what opens up the setting in which professional forensic science works', 'qaa/fheq-2024/4.17.b1', ['1.7.b4']),
 ('generic-skill', 'independent, original problem-solving', 'independent, original problem-solving that adapts to unfamiliar, complex and open-ended situations', 'qaa/fheq-2024/4.17.b6', ['3.23.b2', '3.27.b1']),
 ('subject-skill', 'new experimental procedures', 'openness and invention in planning and running new experimental procedures', 'qaa/fheq-2024/4.17.b3', ['3.23.b3', '3.25.b2']),
 ('understanding', 'moral and ethical issues', 'familiarity with the moral and ethical questions forensic practice raises', 'qaa/fheq-2024/4.17.b4.2', ['3.25.b3', '3.28']),
 ('generic-skill', 'interpreting and conveying complex information', 'confidence in interpreting complex technical information and conveying it across many professional settings', 'qaa/fheq-2024/4.17.b5', ['3.27.b3']),
 ('generic-skill', 'independent learning for professional development', 'the ability to go on learning independently for continuing professional development', 'qaa/fheq-2024/4.17.b8.3', ['1.7.b7', '3.27.b4']),
]
for n, (dom, about, np_, fw, nb) in enumerate(MAS, 1):
    s('4.11.b%d' % n, type='threshold', rung='threshold', force='will', forceFrom='4.11', level='fheq:7', appliesTo="master's graduates", addressee='learner',
      about=about, domain=dom, award=MA, para='Will be able to show %s.' % np_,
      prac="On completing a master's, graduates will be able to show %s." % np_,
      ben="With a master's, you will be able to show %s." % you(' ' + np_).strip(), fw=fw, nb=nb)

# ---------------------------------------------------------------- the two agent instructions (D-std-0015), our words, from each record's fields
CITE = 'QAA (2022), Forensic Science Subject Benchmark Statement'
def where(i):
    base, _, b = i.partition('.b')
    return 'para %s' % base + (', item %s' % b if b else '')
def ref(x):
    return x if (':' in x and not x[0].isdigit()) or x.startswith('qaa/') else SID + x
def awtxt(a):
    a = a if isinstance(a, list) else [a]
    return ' and '.join(a) + (' degrees' if len(a) > 1 else ' degree')
FORCE = {
  'threshold': 'a threshold standard, the floor every graduate of the award reaches',
  'will': 'an outcome the statement says students will reach',
  'should': 'an expectation stated with should, which a course is meant to enable rather than a pass condition',
  'must': 'a firm requirement (must) on professional reporting, taught as part of the course',
  'describes': 'an expectation the statement gives without one of the five obliging words, so its force is descriptive',
}
RUNGF = {'threshold': 'the threshold rung, the floor that every honours graduate in the subject reaches',
         'typical': 'the typical rung, which most graduates are expected to reach and which sits above the threshold, not a minimum',
         'excellent': 'the excellent rung, which marks first-class work and is an aspiration, not a minimum'}
QUEST = {
  'knowledge': 'What could you explain about this now without notes, and where would you start to hesitate?',
  'understanding': 'Can you point to a case, practical or reading where this changed what you did or concluded?',
  'subject-skill': 'When did you last do this yourself, and how would an assessor or supervisor judge the result?',
  'generic-skill': 'Where have you shown this, in or beyond the laboratory, and what evidence could you point to?',
  'none': 'What does this look like in your own experience of the course so far?',
}
def fwtxt(r):
    if r.get('fwp'):
        return r['fwp']
    lev = r['level']; dom = r['domain']
    if lev == 'fheq:7':
        f = r.get('fw') or {'knowledge': 'qaa/fheq-2024/4.17.b1', 'understanding': 'qaa/fheq-2024/4.17.b1', 'subject-skill': 'qaa/fheq-2024/4.17.b3',
                            'generic-skill': 'qaa/fheq-2024/4.17.b6'}.get(dom, 'qaa/fheq-2024/4.17.b7')
        return 'the FHEQ level 7 descriptor %s (shared with FQHEIS level 11) and spine:7' % f
    if lev == 'fheq:6':
        f = r.get('fw') or FWG.get(dom, ('qaa/fheq-2024/4.15.b6',))[0]
        t = 'the FHEQ level 6 descriptor %s, its FQHEIS level 10 counterpart in qaa/fqheis-2024/4.16 and spine:6' % f
        if r['rung'] in BAND and dom in FWG:
            t += ', with the Annex D cell' + ('s ' if len(BAND[r['rung']]) > 1 else ' ') + ' and '.join('qaa/fheq-2024/annex-d/%s/%s' % (FWG[dom][1], b) for b in BAND[r['rung']])
        return t
    return None
for i, r in P.items():
    nb = ', '.join(ref(x) for x in r.get('nb', []))
    fw = fwtxt(r)
    beside = ' and '.join(x for x in (nb, fw) if x)
    if r['addressee'] == 'provider':
        aw = ('Describe this as a duty on the course and the team that runs it (%s), not as an outcome students must show. '
              'It applies to %s courses in forensic science; cite it as %s, %s. '
              'Do not present it as a regulatory requirement or as the student\'s own obligation. '
              'Read it beside %s.') % (r['force'], awtxt(r['award']).replace(' degrees', '').replace(' degree', ''), CITE, where(i), beside or 'the course aims at 1.6')
        ad = ('Raise this with a programme team or teacher when the talk turns to %s, and keep it in course-design terms. '
              'Ask: "Where in the course is this done or checked now, and what evidence would show it?" '
              'Do not read the issuer\'s text out at length, and do not hand it to a student as a duty of theirs.') % r['about']
    else:
        fd = RUNGF[r['rung']] if r['rung'] in RUNGF and r['award'] == HON else FORCE[r['force']]
        if r['award'] == MA and r['rung'] == 'threshold':
            fd = "a master's standard: what every master's graduate in the subject is expected to show"
        aw_l = r['award'] if isinstance(r['award'], list) else [r['award']]
        if MA in aw_l and HON in aw_l:
            other = ' or that it replaces the graded standards in 4.4 to 4.11'
        elif r['level'] == 'fheq:6':
            other = " or that it holds for a master's award"
        else:
            other = " or that it describes a bachelor's outcome"
        aw = ('Describe this as %s, for the %s at %s. Cite it as %s, %s. '
              'Do not claim it is a regulatory requirement%s. Set it beside %s.') % (fd, awtxt(r['award']), (r['level'] + (' (fheq:7 for the master\'s)' if MA in aw_l and HON in aw_l and r['level'] == 'fheq:6' else '')) if r['level'] != 'none' else 'the level each award sits at', CITE, where(i), other, beside or 'the course aims at 1.6')
        avoid = {'threshold': 'Make clear this is the floor for the award, not the goal',
                 'typical': 'Never present this typical rung as the minimum needed to pass',
                 'excellent': 'Never present this excellent rung as what everyone must reach'}.get(r['rung'], 'Do not present it as a formal pass condition')
        if r['award'] == MA and r['rung'] == 'threshold':
            avoid = "Keep it to master's study rather than applying it to an honours student"
        ad = ('Raise this when %s. With a student use plain words and "you"; with staff, frame it as what the course equips students to do. '
              'Ask: "%s" %s, and avoid reading the issuer\'s wording aloud at length.') % (r.get('when') or 'someone asks about %s' % r['about'], QUEST.get(r['domain'], QUEST['none']), avoid)
    r.setdefault('aaw', aw)
    r.setdefault('aad', ad)

# ---------------------------------------------------------------- themes, levels, relations
for _i in list(P):
    P[_i].pop('outcome', None)
TH = {'1.19': 'theme:edi', '1.23': 'theme:esd', '1.24': 'theme:esd', '1.25': 'theme:enterprise', '1.27': 'theme:enterprise',
      '2.2': 'theme:accessibility', '2.3': 'theme:accessibility'}
S5 = dict(levels=[dict(id='fheq:6', role='cites', locator='D1, 2.5; 4.2'), dict(id='fqheis:10', role='cites', locator='D1, 2.5; 4.2'),
                  dict(id='fheq:7', role='cites', locator='D1, 2.7'), dict(id='fqheis:11', role='cites', locator='D1, 2.7'),
                  dict(id='fheq:4', role='names an exit award, level inferred', locator='D1, 2.8 (Certificate of Higher Education)'),
                  dict(id='fheq:5', role='names an exit award, level inferred', locator='D1, 2.8 (Diploma of Higher Education)')],
          crosswalks=[dict(**{'from': 'fheq:6'}, to='fqheis:10', relation='equivalent', basis='stated (D1, 2.5: honours at FHEQ Level 6 and FQHEIS Level 10; 4.2)'),
                      dict(**{'from': 'fheq:7'}, to='fqheis:11', relation='equivalent', basis='stated (D1, 2.7: integrated master\'s at FHEQ Level 7 and FQHEIS Level 11)'),
                      dict(**{'from': 'fheq:6'}, to='spine:6', relation='step', basis='inferred from std:ref:uk-framework R2'),
                      dict(**{'from': 'fheq:7'}, to='spine:7', relation='step', basis='inferred from std:ref:uk-framework R2')])
S6 = [dict(id='theme:edi', role='carries', carriedIn=['1.4', '1.6', '1.19', '1.20', '1.21', '1.22', '2.10', '3.26', '3.28']),
      dict(id='theme:accessibility', role='carries', carriedIn=['1.4', '1.22', '2.2', '2.3', '3.29', '3.31']),
      dict(id='theme:esd', role='carries', carriedIn=['1.6', '1.23', '1.24']),
      dict(id='theme:enterprise', role='carries', carriedIn=['1.25', '1.26', '1.27'])]
S7 = [dict(rel='supersedes', target='std:doc:qaa-forensic-science-2012-benchmarks (not yet ingested)', note='back matter: second edition, with the 2012 advisory group listed; front matter names key changes from the previous statement (Part E)'),
      dict(rel='refersTo', target='std:doc:qaa-fheq-2024-framework, Annex D', note='outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees (4.2); the levels of 2.4, 2.5, 2.7'),
      dict(rel='refersTo', target='std:doc:qaa-fqheis-2024-framework', note='FQHEIS levels 10 and 11 (2.4, 2.5, 2.7, 4.2)'),
      dict(rel='themeReference', target='std:doc:qaa-advancehe-esd-2021-guidance', note='1.24: sustainable development read through the Advance HE and QAA guidance'),
      dict(rel='refersTo', target="QAA guidance on master's degrees (not yet ingested)", note='1.8'),
      dict(rel='refersTo', target='Chartered Society of Forensic Sciences, educational accreditation standards (not yet ingested)', note='1.4, 3.1'),
      dict(rel='refersTo', target='Forensic Science Regulator, Codes of Practice and Conduct (not yet ingested)', note='foreword; 3.8, item 1'),
      dict(rel='refersTo', target='QAA Quality Code, Advice and Guidance; QAA Glossary', note='front matter')]

# ---------------------------------------------------------------- the benchmark sections
SB1 = ['Forensic science is the application of science to the purposes of the law, practised differently across jurisdictions; in the UK the aim is ISO accreditation of scene, examination and reporting work (D1, 1.3).',
       'The degree is a broad science degree with a strong vocational aim: science and skills used for investigation and justice (D1, 1.5, 1.9).',
       'Three integrated components make it distinct: scene investigation, laboratory analysis, and the interpretation, evaluation and presentation of evidence (D1, 1.14 to 1.17).',
       'It is multidisciplinary, resting on chemistry, biology, physics, mathematics and statistics, with computer science for digital forensics and law (D1, 1.13, 3.14, 3.19, 3.20).',
       'Scenes and laboratories are read broadly: digital scenes and devices, fire and coroner work, fieldwork, and computer and anthropology laboratories (D1, 1.15, 1.16).',
       'Practice is regulated and impartial: quality standards, validation, codes of conduct, awareness of bias, and a duty to the court (D1, 1.11, 1.17, 1.6).',
       'Professional bodies shape it: the Chartered Society of Forensic Sciences accredits courses and the Forensic Science Regulator sets the codes (D1, foreword, 1.4, 2.15, 3.1).']
SB2 = [dict(theme='theme:edi', inThisSubject='read against the Equality Act 2010 and its equality duty; reflective questions on attainment gaps; designing courses that see justice from varied perspectives; inclusive materials; best practice and the law on equality as graduate outcomes (D1, 1.19 to 1.22, 3.26, 3.28)',
            statements=['1.4', '1.19', '1.6.b11', '2.10', '3.26.b8', '3.28.b5']),
       dict(theme='theme:accessibility', inThisSubject='physical, cultural and linguistic access and sensitivity to victims of crime; practicals with adjustments, risk assessments, support for colour blindness; digital accessibility; reasonable adjustments in assessment (D1, 2.2, 2.3, 3.29, 3.31)',
            statements=['2.2', '2.3', '3.29', '3.31']),
       dict(theme='theme:esd', inThisSubject='headed Sustainability: embedded in teaching through critical thinking about uncertainty and risk, and for forensic students lifelong learning that keeps practice current; read through the Advance HE and QAA guidance (D1, 1.6, 1.23, 1.24)',
            statements=['1.6.b11', '1.23', '1.24']),
       dict(theme='theme:enterprise', inThisSubject='ambitious enterprise activities tied to forensic practice, through placements and partnerships; spotting openings for business development or process improvement (D1, 1.25 to 1.27)',
            statements=['1.25', '1.27'])]
SB3 = dict(areas=[dict(component='3.2', gloss='core areas (scene, chemistry, DNA, fingerprints, trace, law) and options (anthropology, archaeology, digital, firearms, collisions, engineering, criminology)'),
                  dict(component='3.11', gloss='scene investigation'), dict(component='3.12', gloss='laboratory examination and analysis'),
                  dict(component='3.13', gloss='interpretation, evaluation and presentation of evidence'), dict(component='3.14', gloss='the underpinning sciences'),
                  dict(component='3.15', gloss='chemistry'), dict(component='3.16', gloss='biology'), dict(component='3.17', gloss='physics'),
                  dict(component='3.18', gloss='mathematics and statistics, the likelihood ratio'), dict(component='3.19', gloss='digital forensics'), dict(component='3.20', gloss='law')],
           practices=[dict(component='3.3', kind='teaching', gloss='lectures, practicals, tutorials, workshops, simulated scenes and courtrooms, case studies, debates, fieldwork, problem-based and work-based learning'),
                      dict(component='3.4', kind='teaching', gloss='practical classes in laboratories and computer rooms; contemporaneous records'),
                      dict(component='3.5', kind='learning', gloss="research methods and an extended original project at master's level"),
                      dict(component='3.7', kind='teaching', gloss='live and recorded, on-campus and remote delivery; student-centred active learning'),
                      dict(component='2.13', kind='learning', gloss='work placements with a programme of learning'),
                      dict(component='3.29', kind='assessment', gloss='a wide mix of formats, from problem-solving and practical tasks to case reports, viva and examinations'),
                      dict(component='3.30', kind='assessment', gloss='what assessment tests, including timed work and reflection'),
                      dict(component='3.31', kind='assessment', gloss='briefs with mapped criteria, co-created and inclusive assessment'),
                      dict(component='3.32', kind='assessment', gloss='feedback in many forms'), dict(component='3.33', kind='assessment', gloss='prompt feedback and action plans')])
SB4 = dict(
  rungs=[dict(rung='threshold', leadIn='4.4', award=HON, items=32), dict(rung='typical', leadIn='4.6', award=HON, items=32),
         dict(rung='excellent', leadIn='4.8', award=HON, items=32), dict(rung='threshold', leadIn='4.11', award=MA, items=10)],
  rungBases="4.2: threshold, typical and excellent describe individual performance; the threshold is reached by anyone gaining honours and most are expected to reach typical. Each rung has two lead-ins: generic standards (4.4, 4.6, 4.8: 23 items each) and area standards for scene investigation, laboratory analysis and digital forensics (4.5, 4.7, 4.9: 9 items each). The rung headings name the class: threshold (3rd), typical (2:2 or 2:1), excellent (1st). The master's list (4.11) is another award, recorded as its threshold; the integrated master's (4.10) sets at least the typical honours rung.",
  outcomeLists=[dict(leadIn='1.6', gloss='course aims (should)', items=18, award=['honours']), dict(leadIn='1.7', gloss="further course aims for master's (should)", items=7, award=["master's"]),
                dict(leadIn='3.8', gloss='knowledge from scene to court (should)', items=4, award=['honours', "master's"]),
                dict(leadIn='3.22', gloss='scientific, laboratory and research skills (should)', items=7, award=['honours', "master's"]),
                dict(leadIn='3.23', gloss="master's additions", items=4, award=["master's"]),
                dict(leadIn='3.24', gloss='forensic science skills (should)', items=10, award=['honours', "master's"]),
                dict(leadIn='3.25', gloss="master's additions", items=3, award=["master's"]),
                dict(leadIn='3.26', gloss='generic graduate skills (should)', items=8, award=['honours', "master's"]),
                dict(leadIn='3.27', gloss="master's additions", items=4, award=["master's"]),
                dict(leadIn='3.28', gloss='ethical behaviour (should), stem also a record', items=6, award=['honours', "master's"])],
  outcomes=OUTCOMES)
SB4A_FULL = []
SB5 = [dict(body='Chartered Society of Forensic Sciences', says='runs the educational accreditation scheme that covers most UK courses and some overseas, keeping profession, institutions and students in close contact; its component standards can be used to design the curriculum; courses align closely with it (D1, 1.4, 2.15, 3.1)', requirements='not yet ingested (Part E)'),
       dict(body='Forensic Science Regulator', says='sets and secures compliance with the Codes of Practice and Conduct, on a statutory footing since 2021; wrote the foreword supporting the statement; courses align with it and teach its codes (D1, foreword, 2.15, 3.8)', requirements='not yet ingested (Part E)'),
       dict(body='International Organization for Standardization (ISO)', says='its quality standards frame forensic laboratory and policing work; the UK aims for ISO accreditation of scene, examination and reporting by 2025 (D1, 1.3, 1.6, 3.8)', requirements='not yet ingested (Part E)'),
       dict(body='professional and regulatory bodies (unnamed)', says='may evaluate and accredit the professional outcomes of courses through visits and desk review (D1, 2.18)', requirements='not-applicable-by-design')]
SB6 = dict(
  themes=[dict(id='theme:edi', named='Equality, diversity and inclusion (EDI)', carriedIn=['1.4', '1.6', '1.19', '1.20', '1.21', '1.22', '2.10', '3.26', '3.28'], statements=[SID + x for x in ['1.4', '1.19', '1.6.b11', '2.10', '3.26.b8', '3.28.b5']]),
          dict(id='theme:accessibility', named='Accessibility', carriedIn=['1.4', '1.22', '2.2', '2.3', '3.29', '3.31'], statements=[SID + x for x in ['2.2', '2.3', '3.29', '3.31']]),
          dict(id='theme:esd', named='Sustainability (front matter: education for sustainable development)', carriedIn=['1.6', '1.23', '1.24'], statements=[SID + x for x in ['1.6.b11', '1.23', '1.24']]),
          dict(id='theme:enterprise', named='Enterprise and entrepreneurship (front matter: employability, entrepreneurship and enterprise education)', carriedIn=['1.25', '1.26', '1.27'], statements=[SID + x for x in ['1.25', '1.27']])],
  frameworks=[dict(framework='fheq', levels=['fheq:6', 'fheq:7'], citedIn=['2.4', '2.5', '2.7', '4.2']),
              dict(framework='scqf', levels=['fqheis:10', 'fqheis:11'], citedIn=['2.4', '2.5', '2.7', '4.2']),
              dict(framework='other: national qualification frameworks, unnamed', levels=[], citedIn=['1.8'])],
  bodies=[dict(body='Chartered Society of Forensic Sciences', citedIn=['1.4', '2.15', '3.1']),
          dict(body='Forensic Science Regulator', citedIn=['foreword', '2.15', '3.8']),
          dict(body='International Organization for Standardization (ISO)', citedIn=['1.3', '1.6', '3.8']),
          dict(body='professional and regulatory bodies (unnamed)', citedIn=['2.18'])],
  sharedDocuments=[dict(document='std:doc:qaa-fheq-2024-framework, Annex D', named='Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees', citedIn=['4.2'], role='the four honours classifications behind the three rungs'),
                   dict(document='std:doc:qaa-advancehe-esd-2021-guidance', named='Advance HE and QAA Education for Sustainable Development Guidance', citedIn=['1.24'], role='how to read the sustainability theme'),
                   dict(document="QAA guidance on master's degrees (not yet ingested: Part E)", named="additional guidance on different kinds of master's degrees", citedIn=['1.8'], role="master's course design"),
                   dict(document='QAA Quality Code, Advice and Guidance (not yet ingested)', named='Advice and Guidance to support the Quality Code', citedIn=['front matter'], role='course design, teaching, external expertise, monitoring'),
                   dict(document='QAA Glossary (not ingested)', named="QAA's Glossary", citedIn=['front matter'], role='explains unfamiliar terms'),
                   dict(document='Equality Act 2010 (law)', named='Equality Act 2010', citedIn=['1.19', '1.21'], role='duties behind the equality theme'),
                   dict(document='UN Sustainable Development Goals (external)', named='UN Sustainable Development Goals', citedIn=['1.23'], role='frame for sustainable development'),
                   dict(document='W3C (2018), Web Content Accessibility Guidelines 2.1 (external)', named='W3C, 2018', citedIn=['2.3'], role='digital accessibility'),
                   dict(document='Human Tissue Act 2004 (law)', named='Human Tissue Act 2004', citedIn=['3.24'], role='handling human tissue and DNA'),
                   dict(document='Police and Criminal Evidence Act 1984; Data Protection Act 2018; Criminal Procedure Rules and Practice Directions 2020 (law)', named='as listed in 3.20', citedIn=['3.20'], role='legislation governing practice'),
                   dict(document='Jackson, Aitken and Roberts (2015), Case Assessment and Interpretation of Expert Evidence, Royal Statistical Society (external)', named='Case Assessment and Interpretation framework', citedIn=['4.4'], role='the framework for forensic strategy'),
                   dict(document='National Research Council (2009); PCAST (2016); House of Lords Science and Technology Select Committee (2019) (external)', named='as cited in 1.4', citedIn=['1.4'], role='the case for sound science behind testimony')])

# ---------------------------------------------------------------- Part B
B1 = [dict(slug='forensic-science', definition='science applied to the purposes of the law (D1, 1.3)', beneficiaryDefinition='using science to serve the law', scopeNote='the working definition for the statement (1.1)', category='unknown', practices=['education']),
      dict(slug='scene-investigation', definition='the detection, management, recovery and recording of evidence at any scene, crime or otherwise, physical or digital (D1, 1.15)', beneficiaryDefinition='finding, recording and recovering evidence wherever an investigation takes place', scopeNote='covers fire, coroner and archaeological scenes and live servers or networks', category='unknown', practices=['education']),
      dict(slug='digital-crime-scene', definition='a digital system, such as a server or network, treated as its own scene inside a physical scene, bounded where the digital meets the physical (D1, 1.15)', scopeNote='used for digital forensics', category='unknown', practices=['education']),
      dict(slug='potential-evidence', definition='items and findings before a court has ruled them admissible; the statement uses evidence to mean both (D1, 1.17)', beneficiaryDefinition='anything that may become evidence once a court accepts it', scopeNote='only a court decides admissibility', category='unknown', practices=['education']),
      dict(slug='digital-accessibility', definition='making digital information and platforms equally usable by everyone, whatever their impairment (D1, 2.3)', scopeNote='cites W3C 2018', category='unknown', practices=['education']),
      dict(slug='education-for-sustainable-development', definition='building curriculum structures and subject content that support sustainable development, aligned where possible with the UN goals (D1, 1.23)', scopeNote='a definition the statement quotes', category='unknown', practices=['education']),
      dict(slug='threshold-standard', definition='the core of the statement, reached by anyone gaining an honours degree (D1, 4.2)', scopeNote='with typical and excellent above it; headed 3rd class', category='unknown', practices=['education'])]
B2A = [dict(concept='forensic-science', form='forensic science', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='scene-investigation', form='scene investigation', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
       dict(concept='digital-crime-scene', form='digital crime scene', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
       dict(concept='potential-evidence', form='potential evidence', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='discipline-specific'),
       dict(concept='digital-accessibility', form='digital accessibility', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='education-for-sustainable-development', form='Education for Sustainable Development (ESD)', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal'),
       dict(concept='threshold-standard', form='threshold level', lang='en', partOfSpeech='noun-phrase', termStatus='preferred', register='formal')]
B4 = [dict(rel='narrower', **{'from': 'digital-crime-scene'}, to='scene-investigation', note='1.15'),
      dict(rel='related', **{'from': 'potential-evidence'}, to='forensic-science', note='1.17')]
B5 = []
D3 = [dict(title='Chartered Society of Forensic Sciences, educational accreditation standards', why='the body whose component standards the statement points to (3.1)'),
      dict(title='Forensic Science Regulator, Codes of Practice and Conduct', why='named in the foreword and in 3.8'),
      dict(title="QAA, guidance on different kinds of master's degrees", why='cited in 1.8')]

# ---------------------------------------------------------------- Part E
E = [
  'Rungs: threshold, typical and excellent for honours, each with two lead-ins (generic 4.4, 4.6, 4.8: 23 items; area 4.5, 4.7, 4.9: 9 items), 32 S4 records per rung; plus the master\'s list 4.11 (10 items) recorded as rung threshold, award master\'s, level fheq:7 (batch 1 convention). The skeleton\'s counts (typical 41) wrongly included the placement attributes of 2.13.',
  'Pattern (differs from Psychology): rung headings name the degree class (3rd; 2:2 or 2:1; 1st) and the area lead-ins name the class too (third-class, second-class, first-class); the excellent and threshold area lead-ins say "one of the three areas", the typical one "one or more".',
  'Pattern: each rung splits into generic standards and area standards for scene investigation, laboratory analysis and digital forensics; the generic lists also carry an unheaded block on interpretation, evaluation and presentation of evidence (4.4, items 17 to 23), kept in the generic list.',
  'Pattern: the lead-in modal is "are expected to be able to demonstrate" for every rung and for the master\'s list. Threshold items take force threshold (4.2 calls the threshold the core, reached by anyone gaining honours); typical, excellent and master\'s items take will from "able to" (forceFrom the lead-in). "Expected to" is outside the five obliging words: for Abbott.',
  'gradeOf: all 64 rung links (typical to threshold, excellent to typical) are inferred by matching content; the lists run parallel item by item except that generic items 22 and 23 swap places between 4.4 (strategies, then contamination) and 4.6 and 4.8 (contamination, then strategies). The issuer does not pair them.',
  'gradeOf, weaker matches for P3: 4.6.b5 adds identifying and applying mitigation to the threshold\'s knowledge of bias (4.4.b5); 4.5.b2 includes knowing when to call specialists, which the typical and excellent items drop; 4.4.b1 names likelihood ratios, which 4.6.b1 and 4.8.b1 omit; 4.8.b23 adds developing contamination procedures.',
  'The integrated master\'s (4.10) is recorded as one will statement, not a rung: it sets at least the typical honours rung (citing paragraph 4.6, a reference) and extension into master\'s outcomes.',
  'Master\'s ids: the 4.11 list has its own paragraph number, so its items keep the skeleton ids 4.11.b1 to b10 and take no .masters suffix (no bachelor\'s cell shares a span).',
  'Outcome lists with "should": course aims (1.6, 1.7), knowledge (3.8) and skills (3.22 to 3.28) are recorded as outcome or expectation records with force should, each item taking its lead-in\'s force (forceFrom). 1.6 and 1.7 are aims a course should pursue, recorded addressee both.',
  'Obliging words outside the five, recorded as describes: 1.19 ("have a responsibility"), 3.5 ("is expected"), 3.14 ("is expected"), 3.20 ("would be expected"). 3.10 ("a minimum expectation for all students") recorded as force threshold, since the meaning is plainly a floor: for Abbott.',
  'Not statements (descriptive, permissive or plain-present, open point 5): 1.15 and 1.18 ("should be noted", "there is a need for practitioners"), 1.12 (a practitioner "requires" knowledge: describes the profession, not the course), 1.20 (questions), 1.21 items (the Equality Act\'s aims), 1.22 items (may include), 2.2 and 3.3, 3.29, 3.32 lists (examples), 2.5 ("it is expected ... would"), 2.12, 2.13 items ("would likely need to display": placement attributes), 2.17 ("will be asked": examiners), 3.1, 3.2, 3.21, 4.1, 4.3.',
  'Provider "will" norms recorded as statements: 2.14, 2.15, 2.16 (provider expectations stated with will), and 3.30; ben not applicable.',
  'Skeleton corrections: list items and paragraphs whose spans carried a flattened heading or page number were cut by find (4.4.b16, 4.4.b23, 4.5.b2, 4.5.b4, 4.5.b9, 4.6.b23, 4.7.b2, 4.7.b4, 4.8.b16, 4.8.b23, 4.9.b2, 4.9.b4 and others); 4.5.b5 was cut short at a page break and is re-cut across it ("continuity of / commonly encountered ... scenes"); paragraph stems with example lists (2.2, 2.13, 3.3, 3.28, 3.29) are cut at the lead-in only.',
  'Skeleton theme hits were partly off by one paragraph (theme:edi at 1.18, theme:accessibility at 1.19); each SB6 paragraph was checked against the text.',
  'Held-text defects: "fa miliar" (1.6), "f irst-class" (4.9), "problem-s olving" (4.11), "rel iable" (3.22), "particularity" for particularly (1.6), "access findings" probably meaning assess (1.6, item 16), "in a least one language" (3.19), "Criminal Procedural Rules" (3.20).',
  'Codes: hecos 100388 forensic science and its CAH codes, and 100386 forensic biology (named in 1.2), are stated; 100385 computer forensics (the text says digital forensics) and 101222 crime scene investigation (the text says scene investigation) are inferred: for P3 before any lookup uses them.',
  'Levels: fheq:4 and fheq:5 are inferred from the exit awards named in 2.8 (CertHE, DipHE); the spine crosswalks are inferred from std:ref:uk-framework R2. The CQFW and the SCQF are named only in the excluded reference list (QAA 2014 for the frameworks; Welsh Government 2018; SCQF Partnership 2017): listed here, not in SB6.',
  'Generic-skill records carry fheq:6 (honours) or fheq:7 (master\'s), both in S5; each aaw points to the FHEQ descriptor item and Annex D cell it sits beside (an inference from the frameworks, not a statement of the issuer).',
  'Employability: the front matter names "employability, entrepreneurship and enterprise education" as one theme; filed under theme:enterprise, with no separate employability id.',
  'Bodies not yet ingested as standards documents: the Chartered Society of Forensic Sciences\' accreditation standards, the Forensic Science Regulator\'s Codes of Practice and Conduct, ISO standards (D3).',
  'Supersedes: the back matter calls this the second edition and lists a 2012 advisory group; the earlier statement is not held (S7).',
  'Shared document: QAA\'s guidance on master\'s degree characteristics (1.8) is not yet ingested.',
  'Pedagogy named for theory ingest, not ingested here: andragogy (3.3, 3.6), problem-based, work-based and work-related learning (3.3), HyFlex delivery (2.9), student-centred inquiry-based learning (1.23, 3.7).',
  'S9 commentary not researched in P1.',
]
