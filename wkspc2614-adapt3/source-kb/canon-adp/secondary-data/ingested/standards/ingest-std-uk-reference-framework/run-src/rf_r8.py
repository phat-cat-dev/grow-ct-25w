# Adds R8 (shared expectations by spine step) to the reference framework after rf_build.py; std, run R-0001
import json,sys
p=sys.argv[1]; s=open(p).read()
R8=[
 ('4','CQFW 4, FHEQ 4, SCQF 7',3,"Knows the underlying concepts of the field coherently; applies them and evaluates information in familiar, often routine settings; communicates results clearly; takes personal responsibility for own work.","You know the basic ideas of your subject and how they fit together, use them on familiar tasks, judge information, explain your results clearly and take responsibility for your own work."),
 ('5','CQFW 5, FHEQ 5, SCQF 8, short cycle',4,"Knows well-established principles and some of their limits; applies them beyond where first met; analyses critically in complex settings; communicates in varied forms; takes responsibility and some initiative.","You know the established ideas in your subject and where they stop working, use them in new places, analyse complex situations critically, explain in different ways and start to take the initiative."),
 ('6','CQFW 6, FHEQ 6, SCQF 9 and 10, first cycle',4,"Understands the field systematically, partly at its forefront; uses its methods of enquiry accurately; evaluates arguments and evidence critically; communicates to specialists and non-specialists; makes decisions in complex, unpredictable settings with initiative and personal responsibility.","You understand your subject in depth, including some of its latest work, use its research methods properly, judge arguments and evidence critically, explain to experts and non-experts, and make decisions in complex, unpredictable situations on your own initiative."),
 ('7','CQFW 7, FHEQ 7, SCQF 11, second cycle',4,"Has a comprehensive, critical grasp of current problems and new insight at the forefront; shows originality in applying knowledge; handles complex issues systematically and creatively; decides soundly without complete information; works autonomously and is self-directed.","You have a full, critical grasp of the current questions in your field, apply what you know in original ways, handle complex issues creatively, make sound decisions without all the facts, and direct your own work."),
 ('8','CQFW 8, FHEQ 8, SCQF 12, third cycle',4,"Creates new knowledge through original research at the forefront; conceptualises and carries out substantial enquiry; makes informed judgements on complex issues, often without complete data; leads and takes responsibility in a field.","You create new knowledge through original research, plan and carry out major enquiries, make informed judgements on complex issues with incomplete data, and lead in your field."),
]
y='\n'.join(f"- {{ step: spine:{st}, levels: {json.dumps(lv)}, sharedBy: {n}, forPractitioner: {json.dumps(p_)}, forBeneficiary: {json.dumps(b)}, status: drafted }}" for st,lv,n,p_,b in R8)
block=f'''### R8 Shared expectations by step (student-facing and practitioner-facing)
<!-- label: both; status: drafted; basis: inferred: each step's statement distils the strands' terms and the three qualifier ladders (R4.3) that the sources at that step share; `sharedBy` counts the sources with a descriptor at the step (CQFW, FHEQ, FQHEIS, Dublin; FQHEIS has none of its own at 7 and 8, sharing the FHEQ's); our words -->

```yaml
{y}
```

'''
s=s.replace('## Part B Terminology',block+'## Part B Terminology',1)
open(p,'w').write(s)
