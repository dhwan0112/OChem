from common import *
import numpy as np, math
from geom import D, dienophile, HD, unit
C=Canvas(1100,600)
def T(x,y,t,size=13,cls="ink",anchor="middle",weight="normal",style="normal"): C.text(x,y,t,size=size,cls=cls,anchor=anchor,weight=weight,style=style)
T(24,32,"4  Reading the product: where does the endo substituent end up?",size=19,anchor="start",weight="bold")
def rotx(p,ang,cen):
    p=p-cen; c,s=math.cos(ang),math.sin(ang); return cen+np.array([p[0],p[1]*c-p[2]*s,p[1]*s+p[2]*c])
def product(mode):
    P={k:v.copy() for k,v in D.items()}
    P['C2']=P['C2']+np.array([0,0.15,0]); P['C3']=P['C3']+np.array([0,0.15,0]); P['C5']=np.array([0,HD+0.75,-0.8])
    d=dienophile('endo'); cen=(d['Cb']+d['Ca'])/2
    if mode=='exo': d={k:rotx(v,math.pi,cen) for k,v in d.items()}
    shift=np.array([-0.78,HD-1.55,-0.55])-dienophile('endo')['Cb']
    for k in d: P[k]=d[k]+shift
    return P
def P2(p,ox,oy,s=60,az=math.radians(68),el=math.radians(14)):
    x=p[0]*math.cos(az)+p[2]*math.sin(az); z=-p[0]*math.sin(az)+p[2]*math.cos(az)
    y=p[1]*math.cos(el)+z*math.sin(el); return (ox+x*s, oy-(y-1.3)*s)
def draw_nb(ox,oy,mode):
    P=product(mode); q={k:P2(v,ox,oy) for k,v in P.items()}
    for a,b,o,cls in (("C1","C2",1,"inks"),("C2","C3",2,"nus"),("C3","C4",1,"inks"),("C4","C5",1,"inks"),("C5","C1",1,"inks"),("C1","Cb",1,"goods"),("C4","Ca",1,"goods"),("Cb","Ca",1,"inks"),("Ca","Cc",1,"els")):
        C.bond(q[a],q[b],cls,o,w=2.2 if cls!="inks" else 1.9)
    T(q["Cc"][0]+(10 if mode=="endo" else -10),q["Cc"][1]+14,"CHO",size=13,cls="el",weight="bold",anchor="start" if mode=="endo" else "end")
    T(q["C5"][0]-8,q["C5"][1]-14,"CH₂ bridge",size=12.5,cls="mutedt",weight="bold")
    T(max(q["C2"][0],q["C3"][0])+12,(q["C2"][1]+q["C3"][1])/2,"C=C",size=12.5,cls="nu",weight="bold",anchor="start")
    return q
y0=70
T(24,y0,"(a) cyclic diene → bicyclic product",size=15,anchor="start",weight="bold")
draw_nb(150,y0+175,"endo"); T(150,y0+250,"endo adduct (major)",size=14,weight="bold",cls="good")
T(150,y0+270,"CHO ANTI to the CH₂ bridge",size=12.5); T(150,y0+288,"= on the same side as the new C=C",size=12.5,cls="mutedt")
draw_nb(420,y0+175,"exo"); T(420,y0+250,"exo adduct (minor)",size=14,weight="bold",cls="el")
T(420,y0+270,"CHO SYN to the CH₂ bridge",size=12.5); T(420,y0+288,"= away from the C=C",size=12.5,cls="mutedt")
T(24,y0+322,"L13 p.21: “new double bond and C=O groups end up on same side of molecule: endo”.",size=12,anchor="start",cls="mutedt")
# (b) acyclic
xb=600
T(xb,y0,"(b) open-chain diene → cyclohexene",size=15,anchor="start",weight="bold")
def hexa(cx,cy,r=42):
    return [(cx+r*math.cos(math.radians(a)),cy+r*math.sin(math.radians(a))) for a in (-90,-30,30,90,150,210)]
def hashb(p,q):
    n=7; dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); nx,ny=-dy/L,dx/L
    for i in range(1,n+1):
        t=i/n; w=1+5*t; x,y=p[0]+dx*t,p[1]+dy*t
        C.line((x-nx*w,y-ny*w),(x+nx*w,y+ny*w),"inks",1.6)
def wedge(p,q):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); nx,ny=-dy/L,dx/L
    C.raw(f'<polygon class="ink" points="{p[0]:.1f},{p[1]:.1f} {q[0]+nx*5:.1f},{q[1]+ny*5:.1f} {q[0]-nx*5:.1f},{q[1]-ny*5:.1f}"/>')
def cyclohex(cx,cy,cho_wedge):
    v=hexa(cx,cy)
    # v0 top (C1, Me), v1 upper-right (Cα? CHO), v2 lower-right, v3 bottom (C4, Me), v4 lower-left, v5 upper-left ; double bond v4–v5
    for i in range(6): C.bond(v[i],v[(i+1)%6],"inks",2 if i==4 else 1,inner=(cx,cy) if i==4 else None)
    me1=(v[0][0],v[0][1]-34); me2=(v[3][0],v[3][1]+34); cho=(v[1][0]+30,v[1][1]-18)
    hashb(v[0],me1); hashb(v[3],me2)
    (wedge if cho_wedge else hashb)(v[1],cho)
    T(me1[0],me1[1]-10,"Me",size=12.5,weight="bold"); T(me2[0],me2[1]+12,"Me",size=12.5,weight="bold")
    T(cho[0]+6,cho[1]-2,"CHO",size=12.5,weight="bold",cls="el",anchor="start")
T(xb+10,y0+30,"(E,E)-hexa-2,4-diene + acrolein (L13 p.23–24)",size=12.5,anchor="start",cls="mutedt")
cyclohex(xb+110,y0+160,False); T(xb+120,y0+272,"endo (major): all cis",size=14,weight="bold",cls="good")
cyclohex(xb+340,y0+160,True); T(xb+350,y0+272,"exo: CHO trans to Me",size=14,weight="bold",cls="el")
T(xb+10,y0+300,"Rule: the endo EWG ends up CIS to the diene’s",size=12.5,anchor="start")
T(xb+10,y0+318,"OUT groups (and TRANS to its IN groups).",size=12.5,anchor="start")
T(xb+10,y0+338,"Both Me of (E,E)-diene are OUT → Me, CHO, Me all cis.",size=12,anchor="start",cls="mutedt")
C.line((20,y0+360),(1080,y0+360),"muted",0.8)
T(24,y0+388,"Three-step recipe for any DA stereo question (L14 p.16–19)",size=15,anchor="start",weight="bold")
for i,t in enumerate(["1. Regio: ortho/para rule decides which atoms bond (skip for symmetric partners).",
"2. Endo: put the EWG under the diene → in the product it sits on the same face as the diene’s OUT groups (or anti to the bridge).",
"3. Stereospecificity: substituents keep their cis/trans relationship from the dienophile (and in/out from the diene)."]):
    T(36,y0+414+i*24,t,size=13,anchor="start")
T(24,y0+506,"Sources: L13 p.21–24; L14 p.16–19. Structures schematic (bicyclic drawn from the same 3D model as endo_rule_3D.gif).",size=11,anchor="start",cls="mutedt")
save(C,"endo_step4_products")
