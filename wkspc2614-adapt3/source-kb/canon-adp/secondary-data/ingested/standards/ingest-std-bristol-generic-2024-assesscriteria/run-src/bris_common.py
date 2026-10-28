import json, re
S='/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad'
G=json.load(open(S+'/bris-grid.json'))
BANDS={'4':['0-19','20-39','40-49','50-59','60-69','70-79','80-100']}; BANDS['5']=BANDS['6']=BANDS['4']; BANDS['7']=['0-39','40-49','50-59','60-69','70-79','80-100']
slug=lambda s: re.sub(r'[^a-z]+','-',s.lower().replace('self- ','self-')).strip('-')
STOP={'is','an','a','the','able','to','be','are'}
def key(t):
    t=t.replace('‐','-').replace('- ','-').replace('/ ','/').lower()
    t=re.sub(r'[^a-z0-9 ]+',' ',t)
    return ' '.join(w for w in t.split() if w not in STOP)
def cells():
    out=[]
    for L in ['4','5','6','7']:
        for c in G[L]:
            for k,x in enumerate(c['cells']):
                out.append(dict(id=f'l{L}/{slug(c["criterion"])}/{BANDS[L][k]}',level=int(L),criterion=c['criterion'],name=c['criterion'].replace('- ','-'),crit=slug(c['criterion']),category=c['category'],bsp=c['bsp'],band=BANDS[L][k],bi=k,text=x,key=key(x)))
    first={}
    for c in out:
        first.setdefault(c['key'],c['id']); c['first']=first[c['key']]
    return out
