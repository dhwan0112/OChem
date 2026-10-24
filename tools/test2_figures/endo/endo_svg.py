from common import *
import numpy as np, math
from geom import D, dienophile, cDiene, cDph, HD, unit
Yv=np.array([0,1.,0])
C=Canvas(1100,1060)
def T(x,y,t,size=13,cls="ink",anchor="middle",weight="normal",style="normal"): C.text(x,y,t,size=size,cls=cls,anchor=anchor,weight=weight,style=style)
T(24,32,"The endo rule, step by step (Diels–Alder, L13 p.21–24, 29)",size=21,anchor="start",weight="bold")
T(24,58,"Side view used throughout: the diene lies on top, the dienophile underneath in a parallel plane; left = front (CH₂ of cyclopentadiene), right = back (C2=C3).",size=12.5,cls="mutedt",anchor="start")
def P2(p,ox,oy,s=50,az=math.radians(62),el=math.radians(20)):
    x=p[0]*math.cos(az)+p[2]*math.sin(az); z=-p[0]*math.sin(az)+p[2]*math.cos(az)
    y=p[1]*math.cos(el)+z*math.sin(el)
    return (ox+x*s, oy-y*s)
def draw_ts(ox,oy,mode,orbitals=False,sec=False):
    d=dienophile(mode); A={**D,**d}
    q={k:P2(v,ox,oy) for k,v in A.items()}
    for a,b,o in (("C1","C2",2),("C2","C3",1),("C3","C4",2),("C4","C5",1),("C5","C1",1)):
        C.bond(q[a],q[b],"nus",o if a!="C2" else 1)
    for a,b,o in (("Cb","Ca",2),("Ca","Cc",1),("Cc","O",2)):
        C.bond(q[a],q[b],"els",o)
    C.raw(f'<circle class="bg" cx="{q["O"][0]:.1f}" cy="{q["O"][1]:.1f}" r="8"/>'); T(q["O"][0],q["O"][1],"O",size=13,cls="el",weight="bold")
    for k in ("C1","C2","C3","C4","Cb","Ca","Cc"): C.raw(f'<circle class="ink" cx="{q[k][0]:.1f}" cy="{q[k][1]:.1f}" r="2.2"/>')
    T(q["C5"][0]-16,q["C5"][1]+4,"CH₂",size=11.5,cls="mutedt",weight="bold")
    for a,b in (("C1","Cb"),("C4","Ca")):
        C.line(q[a],q[b],"goods",2,"5,4")
    if orbitals:
        for k in ("C1","C2","C3","C4"):
            c=cDiene[k]; L=(0.38+0.55*abs(c))*52*0.95; x,y=q[k]
            for sgn in (1,-1):
                filled=(c*sgn)>0; cy=y-sgn*L/2*1.0
                C.raw(f'<ellipse class="{"nu" if filled else "nus"}" cx="{x:.1f}" cy="{cy:.1f}" rx="{5+5*abs(c):.1f}" ry="{L/2:.1f}" fill-opacity="{0.75 if filled else 0}" stroke-width="1.3"/>')
        for k in ("Cb","Ca","Cc"):
            c=cDph[k]; L=(0.38+0.55*abs(c))*52*0.95; x,y=q[k]
            for sgn in (1,-1):
                filled=(c*sgn)>0; cy=y-sgn*L/2
                C.raw(f'<ellipse class="{"el" if filled else "els"}" cx="{x:.1f}" cy="{cy:.1f}" rx="{5+5*abs(c):.1f}" ry="{L/2:.1f}" fill-opacity="{0.75 if filled else 0}" stroke-width="1.3"/>')
        if sec:
            a=q["C3"]; b=q["Cc"]; C.raw(f'<path class="arr" d="M{a[0]:.1f},{a[1]+30:.1f} L{b[0]:.1f},{b[1]-30:.1f}" stroke-width="3" stroke-dasharray="3,4"/>')
    return q
# ---------- Step 1 ----------
y0=95
T(24,y0,"1  Two ways to lay the dienophile under the diene",size=16,anchor="start",weight="bold")
q=draw_ts(170,y0+192,"endo"); T(170,y0+262,"ENDO: C=O tucked UNDER the diene",size=13.5,weight="bold",cls="good")
T(170,y0+280,"(points toward C2=C3)",size=12,cls="mutedt")
q=draw_ts(470,y0+192,"exo"); T(470,y0+262,"EXO: C=O points OUT",size=13.5,weight="bold",cls="el")
T(470,y0+280,"(points toward the CH₂, away from the π system)",size=12,cls="mutedt")
T(640,y0+120,"• Same two new σ bonds (green dashed) in both.",size=12.5,anchor="start")
T(640,y0+142,"• Only the position of the substituent differs.",size=12.5,anchor="start")
T(640,y0+164,"• endo = “inside”: under the diene’s π system.",size=12.5,anchor="start")
T(640,y0+186,"• exo = “outside”: away from it.",size=12.5,anchor="start")
T(640,y0+214,"L13 p.22: “The EWG is placed right below",size=12,anchor="start",cls="mutedt")
T(640,y0+230,"the diene (endo transition state).”",size=12,anchor="start",cls="mutedt")
# ---------- Step 2 ----------
y1=400
T(24,y1,"2  Why endo: secondary orbital overlap",size=16,anchor="start",weight="bold")
draw_ts(170,y1+200,"endo",orbitals=True,sec=True); T(170,y1+272,"endo: extra in-phase overlap",size=13.5,weight="bold",cls="good")
T(170,y1+290,"C3 of diene ··· C of C=O (orange)",size=12,cls="mutedt")
draw_ts(470,y1+200,"exo",orbitals=True); T(470,y1+272,"exo: C=O too far away",size=13.5,weight="bold",cls="el")
T(470,y1+290,"only the 2 primary overlaps",size=12,cls="mutedt")
for i,t in enumerate(["• Diene HOMO ψ2 (blue) has lobes at C2 and C3 too.","• The C=O carbon carries part of the dienophile LUMO.","• In endo, these meet IN PHASE → extra stabilisation","   of the TS → lower barrier → faster.","• This overlap forms NO bond in the product.","• Needs a π substituent (C=O, CN …) on the dienophile."]):
    T(640,y1+90+i*22,t,size=12.5,anchor="start")
T(640,y1+90+6*22+8,"L13 p.29 · Clayden 2e p.884",size=12,anchor="start",cls="mutedt")
# ---------- Step 3 ----------
y2=725
T(24,y2,"3  Kinetic, not thermodynamic",size=16,anchor="start",weight="bold")
ox,oy=60,y2+240
C.line((ox,oy),(ox,oy-200),"inks",1.5); C.line((ox,oy),(ox+430,oy),"inks",1.5)
T(ox-8,oy-200,"E",size=13,anchor="end",weight="bold"); T(ox+430,oy+16,"reaction coordinate",size=11.5,anchor="end",cls="mutedt")
def curve(pts,cls,dash=None):
    d="M"+" ".join(f"{x:.1f},{y:.1f}" for x,y in pts[:1])
    path=f"M{pts[0][0]},{pts[0][1]} C{pts[1][0]},{pts[1][1]} {pts[2][0]},{pts[2][1]} {pts[3][0]},{pts[3][1]} S{pts[4][0]},{pts[4][1]} {pts[5][0]},{pts[5][1]}"
    C.raw(f'<path class="{cls}" d="{path}" stroke-width="2.4" {"stroke-dasharray=\'6,4\'" if dash else ""}/>')
s0=(ox+20,oy-70)
curve([s0,(ox+90,oy-70),(ox+120,oy-170),(ox+200,oy-170),(ox+280,oy-40),(ox+400,oy-40)],"goods")
curve([s0,(ox+90,oy-70),(ox+120,oy-195),(ox+200,oy-195),(ox+280,oy-25),(ox+400,oy-25)],"els",dash=True)
T(ox+200,oy-150,"endo TS (lower)",size=12,cls="good",weight="bold"); T(ox+200,oy-205,"exo TS",size=12,cls="el",weight="bold")
T(ox+405,oy-40,"endo product",size=11.5,anchor="start",cls="good"); T(ox+405,oy-22,"exo product (often more stable)",size=11.5,anchor="start",cls="el")
T(ox+30,oy-82,"diene + dienophile",size=11.5,anchor="start",cls="mutedt")
for i,t in enumerate(["• Endo forms FASTER (lower TS) → main product","   under normal, irreversible conditions.","• Exo product is usually less crowded → more stable.","• If the DA is reversible (e.g. furan + maleic anhydride),","   the system can equilibrate → exo.","• L13 p.22: often a mixture; endo usually favoured."]):
    T(640,y2+50+i*22,t,size=12.5,anchor="start")
C.line((20,1030),(1080,1030),"muted",0.8)
T(24,1046,"Lobes: filled = +, open = −; sizes follow Hückel coefficients. Acrolein + cyclopentadiene used as the example. Sources: L13 p.21–24, 29; Clayden 2e p.884.",size=11,cls="mutedt",anchor="start")
save(C,"endo_steps_1-3")
