#!/usr/bin/env python3
"""User supplied enamine scheme, redrawn as native ReShiki specs."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'figures/L11'
def new():return dict(title='L11 p.18-19; generalization of supplied figure; mechanism supplement: Clayden p.608',atoms=[],bonds=[],abbrev=[],captions=[],arrows=[],curved=[],lone_pairs=[])
def atom(s,e,x,y,charge=0,color='ink',label=None):
 i=len(s['atoms']);s['atoms'].append([e,x,y,charge,0,color])
 if label:s['abbrev'].append([label,i,[i]])
 return i
def bond(s,a,b,o=1,c='ink'):s['bonds'].append([a,b,o,'plain',c])
def group(s,x,y,label):return atom(s,'C',x,y,label=label)
def donor(s,x=0,y=0,ketone=False):
 c=atom(s,'C',x,y);a=atom(s,'C',x+.866,y+.5,color='nu');het=atom(s,'O' if ketone else 'N',x,y-1.2,color='ink' if ketone else 'nu',label=None if ketone else 'NR2')
 bond(s,c,a,1 if ketone else 2,'ink' if ketone else 'nu');bond(s,c,het,2 if ketone else 1)
 bond(s,c,group(s,x-.866,y+.5,'R¹'));bond(s,a,group(s,x+.866,y+1.7,'R²'));bond(s,a,atom(s,'H',x+1.732,y))
 if ketone:bond(s,a,atom(s,'H',x+1.732,y+1.0))
 return c,a,het

def adduct(s,x=0,y=0,keto=False):
 chain=[atom(s,'C',x+i*.866,y+(i%2)*.5) for i in range(5)]
 for i in range(4):bond(s,chain[i],chain[i+1],2 if i==3 and not keto else 1,'good' if i==1 else 'ink')
 n=atom(s,'O' if keto else 'N',x,y-1.2,0 if keto else 1,label=None if keto else 'N⁺R2');bond(s,chain[0],n,2)
 o=atom(s,'O',x+3.464,y-1.2,0 if keto else -1);bond(s,chain[4],o,2 if keto else 1)
 bond(s,chain[0],group(s,x-.866,y+.5,'R¹'));bond(s,chain[4],group(s,x+4.33,y+.5,'Z'))
 bond(s,chain[1],group(s,x+.866,y+1.7,'R²'));bond(s,chain[2],group(s,x+1.732,y-1.7,'R³'))
 # H at the reacting donor/acceptor carbons.
 bond(s,chain[1],atom(s,'H',x+.1,y+1.2));bond(s,chain[2],atom(s,'H',x+2.55,y-.65))
 bond(s,chain[3],atom(s,'H',x+2.598,y+1.6))
 if keto:bond(s,chain[3],atom(s,'H',x+3.45,y+1.1),1,'good')
 return chain

def save(n,s):(OUT/(n+'.json')).write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
s=new();donor(s,ketone=True);atom(s,'N',4.5,.4,label='R2NH');donor(s,12,0)
s['arrows']=[[6.5,.2,10.2,.2,'equilibrium']];s['captions']=[['+',3.1,.1,'ink',10],['H+ (cat.)',7,-.8,'muted'],['-H2O',7.5,.6,'muted'],['1. Enamine formation',0,2.7,'muted'],['via iminium; loss of alpha-H',8,2.7,'muted']];save('enamine_general_formation',s)
s=new();c,a,n=donor(s)
b=atom(s,'C',6,.5,color='el');al=atom(s,'C',6.866,1);co=atom(s,'C',7.732,.5);o=atom(s,'O',7.732,-.7)
bond(s,b,al,2,'el');bond(s,al,co);bond(s,co,o,2);bond(s,co,group(s,8.598,1,'Z'));bond(s,b,group(s,6,-.7,'R³'));bond(s,b,atom(s,'H',5.134,1));bond(s,al,atom(s,'H',6.866,2.1))
s['lone_pairs']=[[n,180,7]]
s['curved']=[{'from':{'lp':[n,180]},'to':{'pt':[-.22,-.55],'gap':3},'bend':-.65}, {'from':{'bond':[c,a]},'to':{'atom':b,'gap':7},'bend':.55}, {'from':{'bond':[b,al]},'to':{'bond':[al,co],'gap':3},'bend':.6}, {'from':{'bond':[co,o]},'to':{'atom':o,'gap':3,'dir':340},'bend':-.8}]
s['captions']=[['+',3.4,.6,'ink',10],['2. Carbon-carbon bond formation',0,3.2,'muted'],['donor alpha-C',0,4.1,'nu'],['acceptor beta-C',5.1,4.1,'el']]
s['arrows']=[[10,.5,12.3,.5,'forward']];adduct(s,14.4,0)
s['captions'].extend([['iminium / enolate',14,3.2,'muted'],['net charge = 0',14,4.1,'muted']]);save('enamine_general_addition',s)
s=new();adduct(s,0,0);chain=adduct(s,12,0,keto=True);atom(s,'N',21,.4,label='R2NH')
s['arrows']=[[6,.3,9.5,.3,'forward']];s['captions']=[['H2O',7,-.7,'muted'],['proton transfer,',5.3,1,'muted'],['iminium hydrolysis',5.3,1.8,'muted'],['+',19.5,.2,'ink',10],['3. Aqueous work-up',0,3.4,'muted'],['1,5-dicarbonyl product',11.8,3.4,'muted'],['amine released',20,3.4,'muted']]
for i,c in enumerate(chain):
 a=s['atoms'][c];s['captions'].append([str(i+1),a[1]-.12,2.6,'nu',7])
save('enamine_general_workup',s)
