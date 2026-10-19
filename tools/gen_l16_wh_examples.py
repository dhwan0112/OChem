#!/usr/bin/env python3
"""L16 Woodward–Hoffmann teaching diagrams (qualitative, not optimized TSs).
Sources: Clayden 2e pp.892–893,912–913,920–921; local L16 pp.21–25.
Run with the chem Python environment. Uses the repository's mplfig theme.
"""
from pathlib import Path
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, FancyArrowPatch, Rectangle
from mplfig import C, PX, save

OUT=Path(__file__).resolve().parents[1]/'figures/L16'

def canvas(w,h):
    fig,ax=plt.subplots(figsize=(w/72,h/72),dpi=72)
    fig.subplots_adjust(0,0,1,1);ax.set(xlim=(0,w),ylim=(h,0));ax.axis('off')
    return fig,ax

def text(ax,x,y,s,color='ink',size=None,ha='left'):
    return ax.text(x,y,s,color=C[color],fontsize=size or PX['caption'],ha=ha,va='center')

def line(ax,x1,y1,x2,y2,color='ink',dash=False,lw=None):
    ax.plot([x1,x2],[y1,y2],color=C[color],ls=(0,(4,3)) if dash else '-',lw=lw or PX['stroke'])

def arc(ax,a,b,rad=0,color='good',arrow=False):
    ax.add_patch(FancyArrowPatch(a,b,connectionstyle=f'arc3,rad={rad}',arrowstyle='->' if arrow else '-',
                 mutation_scale=9,color=C[color],lw=PX['stroke'],linestyle='-' if arrow else (0,(4,3))))

def p_orb(ax,x,y,phase=None,scale=1):
    # In WH diagrams both lobes are open: no MO phase is implied.
    for face in (-1,1):
        filled=phase is not None and ((face==-1 and phase==1) or (face==1 and phase==-1))
        ax.add_patch(Ellipse((x,y+face*20*scale),22*scale,36*scale,
                            fc=C['nu'] if filled else C['card'],ec=C['nu'],lw=PX['stroke']))
    ax.add_patch(Circle((x,y),2,fc=C['ink'],ec='none'))

def endpoint(ax,x,y,face,label=None):
    yy=y+face*36;line(ax,x,yy,x,yy+face*20,'good',True)
    ax.add_patch(Circle((x,yy+face*20),3,fc=C['good'],ec='none'))
    if label:text(ax,x,yy+face*38,label,'good',ha='center')

def finish(fig,name):
    p=OUT/(name+'.svg');save(fig,p)
    s=p.read_text();pos=s.index('>')+1
    # The first > may close the XML declaration; insert title at the SVG root.
    import re
    s=re.sub(r'(<svg[^>]*>)',r'\1<title>'+name+'; qualitative orbital/face diagram; Clayden 2e pp.913,920-921</title>',s,count=1)
    p.write_text(s)

def faces_four():
    fig,ax=canvas(600,390)
    for x0,y0,faces,label in [(0,0,(-1,-1),'s: upper / upper'),(300,0,(1,1),'s: lower / lower'),
                              (0,200,(-1,1),'a: upper / lower'),(300,200,(1,-1),'a: lower / upper')]:
        text(ax,x0+20,y0+14,label,'good')
        for x in (x0+80,x0+220):p_orb(ax,x,y0+100)
        line(ax,x0+55,y0+100,x0+245,y0+100,'muted',True)
        for x,f in zip((x0+80,x0+220),faces):endpoint(ax,x,y0+100,f)
        text(ax,x0+150,y0+180,'same local face' if faces[0]==faces[1] else 'opposite local faces','muted',ha='center')
    finish(fig,'wh_faces_four')

def phase_not_face():
    fig,ax=canvas(590,330)
    text(ax,15,16,'Face: where the two contacts occur')
    for x,phase in [(180,1),(390,-1)]:p_orb(ax,x,110,phase);endpoint(ax,x,110,-1)
    line(ax,145,110,425,110,'muted',True)
    text(ax,180,177,'C1',ha='center');text(ax,390,177,'C2',ha='center')
    text(ax,285,208,'two upper contacts = suprafacial','good',ha='center')
    text(ax,20,250,'Phase: filled / open = opposite signs','nu')
    text(ax,20,278,'Example shown: alkene antibonding MO; same face, opposite phase.','muted',PX['small'])
    text(ax,20,304,'Lobe shading does not show electron occupancy.','muted',PX['small'])
    finish(fig,'wh_phase_not_face')

def sigma_four():
    fig,ax=canvas(600,430)
    for x0,y0,L,R in [(0,0,'R','R'),(300,0,'I','I'),(0,210,'R','I'),(300,210,'I','R')]:
        token='s' if L==R else 'a'
        text(ax,x0+20,y0+15,f'{L}/{R}: '+r'$\sigma2\mathrm{'+token+'}$','good')
        y=y0+105
        line(ax,x0+100,y,x0+200,y,'el')
        for x,inside,choice in [(x0+100,1,L),(x0+200,-1,R)]:
            ax.add_patch(Ellipse((x+inside*23,y),42,20,fc='none',ec=C['nu'],lw=PX['stroke']))
            ax.add_patch(Ellipse((x-inside*10,y),16,12,fc='none',ec=C['nu'],lw=PX['stroke']))
            ax.add_patch(Circle((x,y),2,fc=C['ink'],ec='none'))
            contact=x+inside*(31 if choice=='R' else -14)
            line(ax,contact,y,contact,y-45,'good',True)
            text(ax,contact,y-64,choice,'good',ha='center')
        text(ax,x0+150,y0+162,'same response' if L==R else 'different responses','muted',ha='center')
    text(ax,300,415,'R = retention (large lobe); I = inversion (small lobe)','muted',PX['small'],ha='center')
    finish(fig,'wh_sigma_four')

def component_map(n,anti):
    # Unfolded component bookkeeping, not a molecular conformation.
    fig,ax=canvas(610,335)
    pi=n-1;xs=[150+i*310/(pi-1) for i in range(pi)];y=178
    text(ax,15,16,f'[1,{n}]H: thermal '+('antarafacial' if anti else 'suprafacial'))
    text(ax,15,43,'Unfolded component map; contact lines are not electron-pair arrows.','muted',PX['small'])
    text(ax,150,82,'C1',ha='center',size=PX['label']);text(ax,460,82,'H (1s)',ha='center',size=PX['label'])
    line(ax,180,82,410,82,'el');text(ax,295,65,r'$\sigma2\mathrm{s}$'+'  (C1-H)','el',ha='center')
    for i,x in enumerate(xs):p_orb(ax,x,y);text(ax,x,y+57,f'C{i+2}',ha='center',size=PX['small'])
    line(ax,125,y,485,y,'muted',True)
    line(ax,150,100,150,y-36,'good',True)
    if anti:arc(ax,(493,86),(462,y+34),-.85)
    else:line(ax,460,100,460,y-36,'good',True)
    text(ax,70,126,'R at C1','good',PX['small'],ha='center');text(ax,550,240 if anti else 120,'R at H','good',PX['small'],ha='center')
    token=rf'$\pi{pi}\mathrm{{'+('a' if anti else 's')+'}$'
    text(ax,20,270,token+' + '+r'$\sigma2\mathrm{s}$'+' :  count = 1  (odd)','good')
    text(ax,20,303,'Symmetry allowed; '+('short-chain geometry blocks the ordinary pathway.' if n==3 else 'a suitable conformation is still required.'),'muted',PX['small'])
    finish(fig,f'wh_h1{n}_components')

def fmo(n):
    count=n-1;k=count//2+1
    phases=[1 if math.sin(k*(j+1)*math.pi/(count+1))>0 else -1 for j in range(count)]
    fig,ax=canvas(610,340);xs=[130+i*350/(count-1) for i in range(count)];y=150
    text(ax,15,16,f'[1,{n}]H: '+('diene' if n==5 else 'triene')+' LUMO '+rf'$\psi_{k}$')
    text(ax,15,45,'FMO phase diagram; equal lobe sizes simplify coefficient magnitudes.','muted',PX['small'])
    line(ax,105,y,505,y,'muted',True)
    for j,x in enumerate(xs):
        p_orb(ax,x,y,phases[j]);text(ax,x,y+78,f'C{j+2}',ha='center',size=PX['small'])
    for j in range(count-1):
        if phases[j]!=phases[j+1]:line(ax,(xs[j]+xs[j+1])/2,y-42,(xs[j]+xs[j+1])/2,y+40,'arrow',True)
    endpoint(ax,xs[0],y,-1)
    endpoint(ax,xs[-1],y,-1 if n==5 else 1)
    text(ax,20,252,('same-face end lobes: same phase' if n==5 else 'opposite-face end lobes: same phase'),'good')
    text(ax,20,280,f'{k-1} nodes; '+('suprafacial' if n==5 else 'antarafacial')+' matching with occupied C-H sigma orbital','muted',PX['small'])
    text(ax,20,309,'H 1s has one phase throughout: no inversion at hydrogen.','muted',PX['small'])
    finish(fig,f'wh_h1{n}_fmo')

def count33():
    fig,ax=canvas(610,300)
    text(ax,15,15,'[3,3]: compare two consistent connection schemes')
    for y,tokens,score in [(85,[r'$\pi2\mathrm{s}$',r'$\sigma2\mathrm{a}$',r'$\pi2\mathrm{a}$'],[1,0,0]),
                           (205,[r'$\pi2\mathrm{a}$',r'$\sigma2\mathrm{s}$',r'$\pi2\mathrm{a}$'],[0,1,0])]:
        for x,t,s in zip([100,265,430],tokens,score):
            text(ax,x,y,t,'good' if s else 'ink',PX['label'],ha='center')
            text(ax,x,y+32,str(s)+' counted','good' if s else 'muted',ha='center')
        text(ax,538,y+12,'sum = 1','good',ha='center')
    text(ax,20,145,'Changing one connection changes TWO component labels.','muted',PX['small'])
    text(ax,20,278,'Both descriptions: 6 electrons, odd count, thermally allowed.','muted',PX['small'])
    finish(fig,'wh_33_count')

def photo():
    fig,ax=canvas(610,340)
    for y,n,therm,phot in [(85,5,'s','a'),(235,7,'a','s')]:
        text(ax,20,y,f'[1,{n}]H',size=PX['label'])
        for x,face,condition in [(245,therm,'thermal'),(480,phot,'photochemical')]:
            text(ax,x,y-58,condition,'muted',ha='center')
            for px in (x-48,x+48):p_orb(ax,px,y,scale=.65)
            line(ax,x-70,y,x+70,y,'muted',True)
            line(ax,x-48,y-24,x-48,y-40,'good',True)
            sign=-1 if face=='s' else 1
            line(ax,x+48,y+sign*24,x+48,y+sign*40,'good',True)
            text(ax,x,y+66,'suprafacial' if face=='s' else 'antarafacial','good',ha='center')
    finish(fig,'wh_hshift_photo')

if __name__=='__main__':
    faces_four();phase_not_face();sigma_four()
    component_map(5,False);component_map(7,True);component_map(3,True)
    fmo(5);fmo(7);count33();photo()
