#!/usr/bin/env python3
"""L11 p.21 cycle panels derived from the existing stereochemical attack drawing."""
from pathlib import Path
import json,copy
def empty():
 return dict(title='', atoms=[], bonds=[], abbrev=[], captions=[], arrows=[], curved=[], lone_pairs=[])
def append(s,t,dx=0,dy=0):
 n=len(s['atoms'])
 for atom in t['atoms']:
  a=copy.deepcopy(atom);a[1]+=dx;a[2]+=dy;s['atoms'].append(a)
 for b in t['bonds']:s['bonds'].append([b[0]+n,b[1]+n,*b[2:]])
 for label,anchor,indices in t['abbrev']:s['abbrev'].append([label,anchor+n,[i+n for i in indices]])
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'figures/L11'
S=json.loads((OUT/'iminium_attack.json').read_text())
def part(ids):
 s=empty();m={old:i for i,old in enumerate(ids)}
 s['atoms']=[copy.deepcopy(S['atoms'][i]) for i in ids]
 s['bonds']=[[m[b[0]],m[b[1]],*b[2:]] for b in S['bonds'] if b[0] in m and b[1] in m]
 s['abbrev']=[[x[0],m[x[1]],[m[i] for i in x[2]]] for x in S['abbrev'] if x[1] in m]
 return s,m
def freecat():
 s,m=part(list(range(11)));s['atoms'][0][3]=0;i=len(s['atoms']);s['atoms'].append(['H',0,1.85]);s['bonds'].append([0,i,1,'plain']);return s

def adduct(aromatic=False):
 ids=list(range(25,49))+list(range(52,56))
 if aromatic:ids.remove(47)
 s,m=part(ids);s['atoms'][m[46]][3]=0 if aromatic else 1
 if aromatic:
  for b in s['bonds']:
   pair={ids[b[0]],ids[b[1]]}
   if pair=={42,43}:b[2]=2
   if pair=={43,44}:b[2]=1
   if pair=={44,45}:b[2]=2
   if pair=={45,46}:b[2]=1
 return s,m

def save(name,s):
 s['title']='Iminium catalytic cycle: L11 p.21; user-supplied cycle; proton transfers summarized'
 (OUT/(name+'.json')).write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')

s=empty();append(s,freecat());enal,m=part(list(range(11,18)));o=len(enal['atoms']);enal['atoms'].append(['O',0,.8507]);enal['bonds'].append([m[11],o,2,'plain']);append(s,enal,6,-1)
im,m=part(list(range(18)));append(s,im,16,0)
s['arrows']=[[9,1,12.5,1,'forward']];s['captions']=[['+',3.2,.7,'ink',10],['condensation',8,-1.6,'muted'],['-H2O',10,1.5,'muted'],['1. Secondary amine + enal',-2,5,'muted'],['iminium acceptor',14,5,'el'],['catalyst: 20 mol%',-2,6,'muted']];save('iminium_cycle_formation',s)
s=copy.deepcopy(S);s['atoms'][46][3]=1;s['captions']=[c for c in s['captions'] if c[0]!='+'];s['captions'].append(['2. Conjugate addition',-2.4,10.2,'muted']);save('iminium_cycle_addition',s)
s=empty();a,m=adduct();append(s,a,-5,0);a,m=adduct(True);append(s,a,5,0)
s['arrows']=[[6,3,9,3,'forward']];s['captions']=[['-H+',6.7,2,'muted'],['3. Pyrrole rearomatization',0,7.4,'muted'],['enamine; aromatic pyrrole restored',10,7.4,'muted']];save('iminium_cycle_rearomatization',s)
s=empty();a,m=adduct(True);append(s,a,-5,0)
# Released aldehyde: preserve the beta stereocentre and attached pyrrole.
ids=[i for i in range(36,49) if i!=47]+list(range(52,56));p,mp=part(ids)
for b in p['bonds']:
 pair={ids[b[0]],ids[b[1]]}
 if pair=={36,38}:b[2]=1
 if pair=={42,43}:b[2]=2
 if pair=={43,44}:b[2]=1
 if pair=={44,45}:b[2]=2
 if pair=={45,46}:b[2]=1
p['atoms'][mp[46]][3]=0
o=len(p['atoms']);p['atoms'].append(['O',7.8,.8507]);p['bonds'].append([mp[36],o,2,'plain'])
h=len(p['atoms']);p['atoms'].append(['H',6.1,2.85]);p['bonds'].append([mp[38],h,1,'plain','good'])
append(s,p,5,0);append(s,freecat(),23,3)
s['arrows']=[[6,3,9,3,'forward']];s['captions']=[['H2O, H+',6.2,1.7,'muted'],['via iminium',6.5,5.7,'muted'],['+',18.6,3,'ink',10],['4. Product release',0,7.4,'muted'],['aldehyde',12,7.4,'muted'],['catalyst regenerated',20,7.4,'muted']];save('iminium_cycle_hydrolysis',s)
