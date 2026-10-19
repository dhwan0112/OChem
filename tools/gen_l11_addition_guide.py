#!/usr/bin/env python3
"""L11 p.9,13 teaching panels; render JSON with chemfig.py/ReShiki.
CN addition arrows are adapted from the existing mvk_cn_12_vs_14 spec.
"""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'figures/L11'

def empty():return dict(title='L11 p.9,13: staged 1,2/1,4 comparison; intermediate detail is explanatory',atoms=[],bonds=[],abbrev=[],lone_pairs=[],curved=[],captions=[],arrows=[])
def save(name,s): (OUT/(name+'.json')).write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
def append(s,t,dx=0,dy=0):
 n=len(s['atoms'])
 for a in t['atoms']:
  a=copy.deepcopy(a);a[1]+=dx;a[2]+=dy;s['atoms'].append(a)
 for b in t.get('bonds',[]):s['bonds'].append([b[0]+n,b[1]+n,*b[2:]])
 for label,i,inds in t.get('abbrev',[]):s['abbrev'].append([label,i+n,[v+n for v in inds]])
 for lp in t.get('lone_pairs',[]):s['lone_pairs'].append([lp[0]+n,*lp[1:]])
 for c in t.get('captions',[]):s['captions'].append([c[0],c[1]+dx,c[2]+dy,*c[3:]])
 for curve in t.get('curved',[]):
  c=copy.deepcopy(curve)
  for key in ['from','to']:
   e=c[key]
   if 'atom' in e:e['atom']+=n
   if 'bond' in e:e['bond']=[v+n for v in e['bond']]
   if 'lp' in e:e['lp'][0]+=n
   if 'pt' in e:e['pt']=[e['pt'][0]+dx,e['pt'][1]+dy]
  s['curved'].append(c)
 return n

def model(kind):
 # Same carbon skeleton in every panel: beta, alpha, carbonyl C, O, methyl.
 s=empty();s['atoms']=[['C',0,0],['C',.866,.5],['C',1.732,0],['O',1.732,-1,0,0],['C',2.598,.5],['H',.24,1.64]]
 s['bonds']=[[0,1,2,'plain'],[1,2,1,'plain'],[2,3,2,'plain'],[2,4,1,'plain'],[1,5,1,'plain']]
 s['abbrev']=[['H2C',0,[0]],['CH3',4,[4]]]
 if kind=='start':return s
 is12=kind.startswith('12');enolate=kind in ['12_alkoxide','14_enolate'];enol=kind=='14_enol';keto=kind=='14_keto'
 s['atoms'][3][3]=-1 if enolate else 0
 if is12:
  s['bonds'][2][2]=1
  s['atoms'] += [['C',1.732,1.45,0,0,'good'],['N',1.732,2.45]]
  s['bonds'] += [[2,6,1,'plain','good'],[6,7,3,'plain']]
 else:
  s['bonds'][0][2]=1;s['bonds'][1][2]=1 if keto else 2;s['bonds'][2][2]=2 if keto else 1
  # Extend CN to the left, leaving the right-hand skeleton unchanged.
  s['atoms'] += [['C',-1.25,.72,0,0,'good'],['N',-2.116,1.22]]
  s['bonds'] += [[0,6,1,'plain','good'],[6,7,3,'plain']]
  s['abbrev']=[['CH3',4,[4]]]
  # beta remains CH2 after attachment: show both H explicitly.
  s['atoms'] += [['H',-.8,-.65],['H',.25,-1.0]]
  s['bonds'] += [[0,8,1,'plain'],[0,9,1,'plain']]
 s['abbrev'].append(['C',6,[6]])  # Explicit nitrile carbon at a linear junction.
 if kind=='12_alcohol' or enol:
  h=len(s['atoms']);s['atoms'].append(['H',2.8,-1.55,0,0,'good']);s['bonds'].append([3,h,1,'plain','good'])
 if keto:
  h=len(s['atoms']);s['atoms'].append(['H',1.55,1.45,0,0,'good']);s['bonds'].append([1,h,1,'plain','good'])
 return s

old=json.loads((OUT/'mvk_cn_12_vs_14.json').read_text())
def attack(which):
 ids=([0,1,2,3,4,5,6,14] if which==12 else [7,8,9,10,11,12,13,15]);mp={v:i for i,v in enumerate(ids)};dx=0 if which==12 else -8.5
 s=empty();s['atoms']=[copy.deepcopy(old['atoms'][i]) for i in ids]
 for a in s['atoms']:a[1]+=dx
 s['bonds']=[[mp[b[0]],mp[b[1]],*b[2:]] for b in old['bonds'] if b[0] in mp and b[1] in mp]
 s['abbrev']=[[a[0],mp[a[1]],[mp[i] for i in a[2]]] for a in old['abbrev'] if a[1] in mp]
 s['lone_pairs']=[[mp[a[0]],*a[1:]] for a in old['lone_pairs'] if a[0] in mp]
 for curve in old['curved'][:2] if which==12 else old['curved'][2:]:
  c=copy.deepcopy(curve)
  for k in ['from','to']:
   e=c[k]
   if 'atom'in e:e['atom']=mp[e['atom']]
   if 'bond'in e:e['bond']=[mp[i] for i in e['bond']]
   if 'lp'in e:e['lp'][0]=mp[e['lp'][0]]
  s['curved'].append(c)
 if which==14:s['curved'][1]['bend']=0.65
 return s

s=empty();append(s,model('start'),1,0)
s['captions']=[['1',2.55,-2.1,'muted',7],['2',3.0,-.65,'muted',7],['3',2.15,1.05,'muted',7],['4',.7,-1.05,'muted',7],['1 = O; 2 = carbonyl C',5,-.8,'muted'],['3 = alpha C; 4 = beta C',5,.2,'muted'],['Addition numbering, not IUPAC locants',.2,2.45,'muted']]
save('guide_addition_numbering',s)
for which,label in [(12,'alkoxide'),(14,'enolate')]:
 s=empty();append(s,attack(which),1,0);append(s,model(f'{which}_{label}'),11 if which==14 else 9,0)
 s['arrows']=[[5.2,.2,7.8,.2,'forward']]
 s['captions']=[[f'1,{2 if which==12 else 4}: first C-C bond',.2,3.35,'muted'],[label,9,3.35,'muted'],['before protonation',8.3,4.25,'muted']]
 save(f'guide_{which}_attack',s)
for name,left,right,cond,sub in [
 ('guide_12_protonation','12_alkoxide','12_alcohol','proton donor','C=C retained; C=O becomes C-OH'),
 ('guide_14_protonation','14_enolate','14_enol','O-protonation','enol: not the final ketone'),
 ('guide_14_tautomerization','14_enol','14_keto','tautomerization','C=O restored; original C=C consumed')]:
 s=empty();append(s,model(left),2.8,0);append(s,model(right),13,0)
 s['arrows']=[[6.7,.2,9.8,.2,'equilibrium' if 'tautomer' in name else 'forward']]
 s['captions']=[[cond,6.1,-.9,'muted'],[sub,2,3.35,'muted']]
 save(name,s)
s=empty();append(s,model('12_alcohol'),3,0);append(s,model('14_keto'),3,6)
s['captions']=[['1,2 product: cyanohydrin',7,.1,'muted'],['CN at original carbonyl C',7,1.1,'muted'],['1,4 product: beta-cyano ketone',7,5.8,'muted'],['CN at original beta C',7,6.8,'muted']]
save('guide_products_compare',s)
