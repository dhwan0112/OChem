#!/usr/bin/env python3
"""L16 notation diagrams. Clayden pp.910,913,917-919; figures/STYLE.md."""
import json
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from mplfig import C, PX, save

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'figures/L16'


def numbered(source, count, name, tags, newbond, title, side, pairs=None):
    original=json.loads((OUT/(source+'.json')).read_text())
    spec={'title':title,'atoms':original['atoms'][:count],
          'bonds':[b for b in original['bonds'] if max(b[:2])<count],
          'abbrev':[x for x in original.get('abbrev',[]) if x[1]<count],
          'lone_pairs':pairs if pairs is not None else [x for x in original.get('lone_pairs',[]) if x[0]<count],
          'captions':[t+[7] if len(t)==4 else t for t in tags]+side,
          'shapes':[{'line':[*newbond,'good','dash']}]}
    (OUT/(name+'.json')).write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')


def canvas(w,h):
    fig,ax=plt.subplots(figsize=(w/72,h/72),dpi=72)
    fig.subplots_adjust(0,0,1,1);ax.set(xlim=(0,w),ylim=(h,0));ax.axis('off')
    return fig,ax


def text(ax,x,y,s,color='ink',size=None,ha='left'):
    ax.text(x,y,s,fontsize=size or PX['caption'],color=C[color],ha=ha,va='center')


def line(ax,x1,y1,x2,y2,color='ink',dash=False):
    ax.plot([x1,x2],[y1,y2],color=C[color],lw=PX['stroke'],ls='--' if dash else '-')


def lobes(ax,x,y,vertical=True):
    for sign in [-1,1]:
        dx,dy=(0,sign*17) if vertical else (sign*17,0)
        ax.add_patch(Ellipse((x+dx,y+dy),20 if vertical else 32,32 if vertical else 20,
                             facecolor=C['nu'] if sign<0 else 'none',edgecolor=C['nu'],lw=PX['stroke']))


def components():
    fig,ax=canvas(550,290)
    for y in [55,235]:line(ax,130,y,230,y,'muted',True)
    for x in [155,205]:lobes(ax,x,55)
    text(ax,20,55,r'$\pi2$',size=PX['label']);text(ax,270,45,'two p orbitals; 2 electrons')
    text(ax,270,70,'one alkene component','muted')
    line(ax,167,145,193,145);text(ax,155,145,'C',ha='center',size=PX['label']);text(ax,205,145,'C',ha='center',size=PX['label'])
    text(ax,20,145,r'$\sigma2$',size=PX['label']);text(ax,270,135,'one occupied sigma bond')
    text(ax,270,160,'2 electrons','muted')
    lobes(ax,180,235);text(ax,20,235,r'$\omega2$',size=PX['label'])
    text(ax,270,225,'one p orbital; 2 electrons')
    text(ax,270,250,'carbanion; empty orbital = '+r'$\omega0$','muted')
    save(fig,OUT/'notation_components.svg')


def faces():
    fig,ax=canvas(530,300)
    for y,name,opposite in [(80,r'$\pi2\mathrm{s}$',False),(225,r'$\pi2\mathrm{a}$',True)]:
        text(ax,15,y,name,size=PX['label'])
        for x in [190,330]:lobes(ax,x,y)
        line(ax,175,y,345,y,'muted',True)
        line(ax,110,y-29,190,y-29,'good',True)
        line(ax,330,y+29 if opposite else y-29,410,y+29 if opposite else y-29,'good',True)
        text(ax,430,y-5,'opposite' if opposite else 'same','good')
        text(ax,430,y+18,'faces','good')
    text(ax,115,7,'new contacts at the two ends','muted',PX['small'])
    save(fig,OUT/'notation_pi_faces.svg')


def sigma():
    fig,ax=canvas(550,330)
    for y,states,token in [(85,('R','R'),r'$\sigma2\mathrm{s}$'),(235,('R','I'),r'$\sigma2\mathrm{a}$')]:
        line(ax,175,y,325,y,'muted',True)
        # Old sigma bond uses the large, inward-pointing lobes.
        for x,sign in [(175,1),(325,-1)]:
            ax.add_patch(Ellipse((x+sign*45,y),95,18,facecolor=C['nu'],edgecolor=C['nu'],lw=PX['stroke']))
            ax.add_patch(Ellipse((x-sign*9,y),18,12,facecolor='none',edgecolor=C['nu'],lw=PX['stroke']))
            ax.plot(x,y,'o',ms=3,color=C['ink'])
        for x,sign,state in [(175,1,states[0]),(325,-1,states[1])]:
            contact=x+sign*45 if state=='R' else x-sign*10
            line(ax,contact,y-45,contact,y-12,'good',True)
            text(ax,x,y+40,'retention' if state=='R' else 'inversion',ha='center',size=PX['small'])
        text(ax,20,y,token,size=PX['label']);text(ax,420,y,'same' if states[0]==states[1] else 'different','good')
    text(ax,110,8,'large lobe: R; small lobe: I','muted',PX['small'])
    text(ax,120,320,'I / I is also s; I / R is also a','muted',PX['small'])
    save(fig,OUT/'notation_sigma_faces.svg')


def main():
    numbered('claisen_aliphatic',14,'notation_33_numbering',
       [['A1',-.30,-2.25,'muted'],['A2',-.90,-.85,'muted'],['A3',-.95,.05,'muted'],
        ['B1',.30,-.85,'muted'],['B2',.30,.05,'muted'],['B3',-.30,.65,'muted']],
       [-1.26,.76,.12,1.47], 'Numbering [3,3], allyl vinyl ether; Clayden p.910',
       [['[3,3]',3,-1.7,'ink',10],['old: A1-B1',3,-.55,'el'],['new: A3-B3',3,.40,'good'],['O counts as A1',3,1.35,'muted']])
    numbered('wittig23_benzyl_allyl',12,'notation_23_numbering',
       [['A2',-.25,.15,'muted'],['A1',.30,1.30,'muted'],['B1',.35,-.40,'muted'],['B2',-.14,-.82,'muted'],['B3',-.84,-.20,'muted']],
       [-.79,.99,-1.21,-.35],'Numbering [2,3]-Wittig; Clayden p.917-918',
       [['[2,3]',3,-1.4,'ink',10],['old: A1-B1',3,-.25,'el'],['new: A2-B3',3,.70,'good'],['anion C is A2',3,1.65,'muted']], pairs=[[3,180,7]])
    numbered('h15_shift_cp',11,'notation_15_numbering',
       [['B1',-.20,-.95,'muted'],['B2',-.85,-.30,'muted'],['B3',-.65,.25,'muted'],
        ['B4',.20,.25,'muted'],['B5',.35,-.30,'muted'],['A1 = H',.30,-3.20,'muted']],
       [.76,-1.94,1.21,-.45],'Numbering [1,5]-H along the diene path; Clayden p.919',
       [['[1,5]-H',3,-1.7,'ink',10],['old: H-B1',3,-.55,'el'],['new: H-B5',3,.40,'good'],['count B1 to B5',3,1.35,'muted']])
    components();faces();sigma()
    # Matplotlib emits trailing spaces in SVG path data; normalize whitespace.
    for path in OUT.glob("notation_*.svg"):
        path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines())+"\n")

if __name__=='__main__':main()
