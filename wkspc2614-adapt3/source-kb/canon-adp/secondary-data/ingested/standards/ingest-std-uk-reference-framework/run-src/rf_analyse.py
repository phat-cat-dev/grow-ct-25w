import json,re,collections
SP='/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad/'
H='/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/frameworks/'
NORM={'fheq':open(H+'qaa-frameworks-2024.norm.txt').read(),'fqheis':open(H+'qaa-frameworks-2024.norm.txt').read(),'cqfw':open(H+'welsh-government-cqfw-level-descriptors-2009.norm.txt').read()}
SPINE={'cqfw':lambda l:l.split(':')[1], 'fheq':lambda l:l.split(':')[1], 'fqheis':lambda l:{'7':'4','8':'5','9':'6','10':'6','11':'7','12':'8'}[l.split(':')[1]], 'qfehea':lambda l:{'short':'5','1':'6','2':'7','3':'8'}[l.split(':')[1]]}
def strand(r):
    t=(str(r.get('about',''))+' '+str(r.get('paraphrase',''))).lower()
    if re.search(r'communicat|audience|non-specialist|present(s|ing)? (information|ideas|results)',t): return 'M'
    if re.search(r'responsib|autonom|initiative|independen|own learning|training|professional development|employment|work that|accountab|self-direct|\blead|supervis|guidance|direction|decision',t): return 'R'
    if re.search(r'evaluat|analys|critical|argument|judg|problem|assess|interpret|synthes|reflect|weigh',t): return 'C'
    if re.search(r'appl|technique|method|procedure|practice|task|\buse\b|carry out|enquiry|research|investigat|skill',t): return 'A'
    return 'K'
RECS=[]
for fw in ('fheq','fqheis','cqfw'):
    for r in json.load(open(SP+f'ref_{fw}.json')):
        if r.get('statementType')!='descriptor': continue
        lv=r.get('level')
        if isinstance(lv,list): lv=lv[0]
        if not lv or lv=='none': continue
        pre=lv.split(':')[0]
        if pre=='qfehea': src='dublin'
        else: src=fw
        try: step=SPINE[pre](lv)
        except Exception: continue
        sp=r['span']; txt=NORM[fw][sp['start']:sp['end']]
        RECS.append({'id':r['id'],'src':src,'level':lv,'step':step,'dim':r.get('dimension'),'strand':strand(r),'verbs':[v.lower() for v in r.get('verbs',[])],'force':r.get('force'),'text':txt})
json.dump(RECS,open('rf_recs.json','w'))
c=collections.Counter((r['src'],r['step']) for r in RECS); print(sorted(c.items()))
print(collections.Counter((r['src'],r['strand']) for r in RECS))
