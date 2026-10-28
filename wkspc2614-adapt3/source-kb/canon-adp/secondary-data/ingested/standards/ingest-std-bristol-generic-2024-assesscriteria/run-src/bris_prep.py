import pdfplumber, glob, re, json
U='/root/.claude/uploads/378bff94-17ab-5a5d-8465-bd8449aca2a6/'
F={4:'23927037-university-marking-criteria-level4.pdf',5:'5ddac833-university-marking-criteria-level5.pdf',6:'fa378a48-university-marking-criteria-level6.pdf',7:'882842aa-university-marking-criteria-level7.pdf'}
BANDS={4:['0-19','20-39','40-49','50-59','60-69','70-79','80-100']}; BANDS[5]=BANDS[6]=BANDS[4]; BANDS[7]=['0-39','40-49','50-59','60-69','70-79','80-100']
J=lambda c: ' '.join((c or '').split())
out={}
for L,f in F.items():
    crit=[]; cat=None
    with pdfplumber.open(U+f) as pdf:
        for pg in pdf.pages[1:]:
            for t in pg.extract_tables():
                if len(t[0])<6: continue
                for r in t:
                    nn=[c for c in r if c is not None]
                    if nn and J(nn[0]).startswith('Marks'): continue
                    vals=[J(c) for c in nn]
                    if len([v for v in vals if v])==1 and len(vals)<=2 or (len(nn)==1):
                        v=[x for x in vals if x][0] if any(vals) else ''
                        if re.fullmatch(r'[\d, ]+',v): continue
                        cat=v; continue
                    if len(nn)==1: continue
                    if re.fullmatch(r'[\d, ]+',vals[0] or 'x') and len(vals)<8: continue
                    nb=len(BANDS[L])
                    if len(vals)!=nb+1:
                        print('ODD',L,len(vals),vals[:2]); continue
                    if vals[0]=='':
                        for k in range(nb):
                            if vals[k+1]: crit[-1]['cells'][k]=(crit[-1]['cells'][k]+' '+vals[k+1]).strip()
                    else:
                        m=re.match(r'(.*?)\s*(BSP .*)$',vals[0])
                        name,bsp=(m.group(1),m.group(2)) if m else (vals[0],'')
                        crit.append({'category':cat,'criterion':name,'bsp':bsp,'cells':vals[1:]})
    out[L]=crit
    print('Level',L,len(crit),'criteria:',[ (c['category'][:12],c['criterion'],c['bsp']) for c in crit])
json.dump(out,open('bris-grid.json','w'),indent=1)
