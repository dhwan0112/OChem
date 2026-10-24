import math
L=40.0
els=[]
def P(x,y): return (round(x,1),round(y,1))
class Mol:
    def __init__(s): s.a={}; s.b=[]
    def atom(s,k,x,y,label=None,color="#111"): s.a[k]=(x,y,label,color)
    def bond(s,i,j,order=1,inner=None,color="#111"): s.b.append((i,j,order,inner,color))
def shorten(p,q,lp,lq):
    (x1,y1),(x2,y2)=p,q; d=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/d,(y2-y1)/d
    s1=11 if lp else 0; s2=11 if lq else 0
    return (x1+ux*s1,y1+uy*s1),(x2-ux*s2,y2-uy*s2)
def line(p,q,c="#111",w=1.8):
    els.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>')
def text(x,y,t,size=15,c="#111",anchor="middle",weight="normal",style="normal"):
    els.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="Helvetica, Arial, sans-serif" font-size="{size}" fill="{c}" text-anchor="{anchor}" dominant-baseline="central" font-weight="{weight}" font-style="{style}">{t}</text>')
def draw(m):
    for i,j,o,inner,c in m.b:
        xi,yi,li,_=m.a[i]; xj,yj,lj,_=m.a[j]
        p,q=shorten((xi,yi),(xj,yj),li,lj)
        if o==1: line(p,q,c)
        elif inner is not None:
            line(p,q,c)
            cx,cy=inner; mx,my=(p[0]+q[0])/2,(p[1]+q[1])/2
            d=math.hypot(q[0]-p[0],q[1]-p[1]); ux,uy=(q[0]-p[0])/d,(q[1]-p[1])/d
            nx,ny=-uy,ux
            if (cx-mx)*nx+(cy-my)*ny<0: nx,ny=-nx,-ny
            off=5.5; sh=6
            line((p[0]+nx*off+ux*sh,p[1]+ny*off+uy*sh),(q[0]+nx*off-ux*sh,q[1]+ny*off-uy*sh),c)
        else:
            d=math.hypot(q[0]-p[0],q[1]-p[1]); ux,uy=(q[0]-p[0])/d,(q[1]-p[1])/d; nx,ny=-uy,ux
            for s in (-2.8,2.8): line((p[0]+nx*s,p[1]+ny*s),(q[0]+nx*s,q[1]+ny*s),c)
    for k,(x,y,l,c) in m.a.items():
        if l and len(l)>1: text(x-5.5,y,l,c=c,anchor="start")
        elif l: text(x,y,l,c=c)
def hexring(m,pre,cx,cy):
    pts=[]
    for k,ang in enumerate([-90,-30,30,90,150,210]):
        r=math.radians(ang); m.atom(f"{pre}{k}",cx+L*math.cos(r),cy+L*math.sin(r)); pts.append(f"{pre}{k}")
    return pts
def pyrrolidine(m,pre,nx,ny,Nlabel="N",Ncolor="#111"):
    R=L/(2*math.sin(math.radians(36))); cx,cy=nx,ny-R
    keys=[]
    for k in range(5):
        ang=math.radians(90+72*k)  # k=0 is N at bottom (svg y down)
        x,y=cx+R*math.cos(ang),cy+R*math.sin(ang)
        m.atom(f"{pre}p{k}",x,y,Nlabel if k==0 else None,Ncolor if k==0 else "#111"); keys.append(f"{pre}p{k}")
    for k in range(5): m.bond(keys[k],keys[(k+1)%5])
    return keys
def carrow(p,q,bend=0.35,c="#c0392b"):
    (x1,y1),(x2,y2)=p,q; mx,my=(x1+x2)/2,(y1+y2)/2; d=math.hypot(x2-x1,y2-y1)
    nx,ny=-(y2-y1)/d,(x2-x1)/d; cx,cy=mx+nx*d*bend,my+ny*d*bend
    els.append(f'<path d="M{x1:.1f},{y1:.1f} Q{cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}" fill="none" stroke="{c}" stroke-width="1.6" marker-end="url(#ah)"/>')
def rarrow(x1,x2,y,above=None,below=None,below2=None):
    els.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#111" stroke-width="1.8" marker-end="url(#rh)"/>')
    if above: text((x1+x2)/2,y-14,above,size=14)
    if below: text((x1+x2)/2,y+15,below,size=12.5,c="#444")
    if below2: text((x1+x2)/2,y+31,below2,size=12.5,c="#444")
def charge(x,y,s):
    els.append(f'<circle cx="{x}" cy="{y}" r="6.5" fill="white" stroke="#111" stroke-width="1"/>')
    text(x,y+0.5,s,size=12)
NEW="#1e8449"; RED="#c0392b"
# ---------------- Row 1 ----------------
Y=250
A=Mol(); r=hexring(A,"a",95,Y)
for k in range(6): A.bond(r[k],r[(k+1)%6],2 if k==0 else 1,inner=(95,Y) if k==0 else None)
ax,ay,_,_=A.a["a0"]; pk=pyrrolidine(A,"a",ax,ay-L); A.bond("ap0","a0")
draw(A)
nx,ny=A.a["ap0"][0],A.a["ap0"][1]
for dy in (-3.5,3.5): els.append(f'<circle cx="{nx+12:.1f}" cy="{ny+dy:.1f}" r="1.7" fill="#111"/>')
text(ax+40,ay-L-58,"pyrrolidine enamine",size=12,c="#444",anchor="start")
# acceptor
B=Mol(); bx=230
B.atom("cb",bx,Y-20); B.atom("ca",bx+34.6,Y); B.atom("co",bx+69.3,Y-20)
B.atom("O",bx+69.3,Y-60,"O"); B.atom("OMe",bx+103.9,Y,"OMe"); B.atom("S",bx+34.6,Y+40,"SMe")
B.bond("cb","ca",2); B.bond("ca","co"); B.bond("co","O",2); B.bond("co","OMe"); B.bond("ca","S")
draw(B)
text(bx+4,Y-38,"β",size=13,c=RED,style="italic"); text(bx+44,Y+14,"α",size=13,c=RED,style="italic")
text(178,Y+2,"+",size=20)
# curved arrows step 1
a0=A.a["a0"]; a1=A.a["a1"]
carrow((nx+15,ny+6),((nx+a0[0])/2+4,(ny+a0[1])/2+2),bend=-0.9)
m01=((a0[0]+a1[0])/2,(a0[1]+a1[1])/2)
carrow((m01[0]+2,m01[1]-6),(bx-9,Y-24),bend=-0.35)
cb=B.a["cb"]; ca=B.a["ca"]; co=B.a["co"]; O=B.a["O"]
carrow(((cb[0]+ca[0])/2+2,(cb[1]+ca[1])/2-4),((ca[0]+co[0])/2-2,(ca[1]+co[1])/2-5),bend=-0.55)
carrow(((co[0]+O[0])/2+6,(co[1]+O[1])/2+6),(O[0]+12,O[1]-2),bend=0.45)
rarrow(372,452,Y,above="MeCN",below="conjugate (1,4)",below2="addition")
# zwitterion
off=470
C=Mol(); r=hexring(C,"c",off+95-50,Y)
cxr=off+45
for k in range(6): C.bond(r[k],r[(k+1)%6])
c0=C.a["c0"]; pk=pyrrolidine(C,"c",c0[0],c0[1]-L,Nlabel="N")
C.bond("cp0","c0",2)
c1=C.a["c1"]
C.atom("n1",c1[0]+34.6,c1[1]-20); C.atom("n2",c1[0]+69.3,c1[1]); C.atom("n3",c1[0]+103.9,c1[1]-20)
C.atom("nO",c1[0]+103.9,c1[1]-60,"O"); C.atom("nOMe",c1[0]+138.6,c1[1],"OMe"); C.atom("nS",c1[0]+69.3,c1[1]+40,"SMe")
C.bond("c1","n1",color=NEW); C.bond("n1","n2"); C.bond("n2","n3",2); C.bond("n3","nO"); C.bond("n3","nOMe"); C.bond("n2","nS")
draw(C)
cn=C.a["cp0"]; charge(cn[0]+15,cn[1]-9,"+")
nO=C.a["nO"]; charge(nO[0]+15,nO[1]-9,"−")
text(off+120,Y+92,"iminium / ester enolate (zwitterion)",size=12,c="#444")
# ---------------- Row 2 ----------------
Y2=530
rarrow(40,200,Y2,above="H<tspan dy='4' font-size='10'>2</tspan><tspan dy='-4'>O</tspan>",below="proton transfer,",below2="iminium hydrolysis")
D=Mol(); r=hexring(D,"d",300,Y2)
for k in range(6): D.bond(r[k],r[(k+1)%6])
d0=D.a["d0"]; D.atom("dO",d0[0],d0[1]-L,"O"); D.bond("d0","dO",2)
d1=D.a["d1"]
D.atom("m1",d1[0]+34.6,d1[1]-20); D.atom("m2",d1[0]+69.3,d1[1]); D.atom("m3",d1[0]+103.9,d1[1]-20)
D.atom("mO",d1[0]+103.9,d1[1]-60,"O"); D.atom("mOMe",d1[0]+138.6,d1[1],"OMe"); D.atom("mS",d1[0]+69.3,d1[1]+40,"SMe")
D.bond("d1","m1",color=NEW); D.bond("m1","m2"); D.bond("m2","m3"); D.bond("m3","mO",2); D.bond("m3","mOMe"); D.bond("m2","mS")
draw(D)
text(d1[0]+60,Y2+88,"1,5-dicarbonyl  (95%)",size=13,c="#111",weight="bold")
text(d1[0]+60,Y2+106,"C=O ··· C=O : carbonyl C are 1,5",size=11.5,c="#444")
text(600,Y2+2,"+",size=20)
E=Mol(); pk=pyrrolidine(E,"e",680,Y2+18,Nlabel="NH")
draw(E); text(680,Y2+44,"pyrrolidine",size=12,c="#444")
# legend / title
title='Conjugate addition of an enamine (L11 p.19)'
head=f'<text x="30" y="34" font-family="Helvetica, Arial, sans-serif" font-size="19" font-weight="bold" fill="#111">{title}</text>'
leg=[]
leg.append(f'<text x="30" y="58" font-family="Helvetica, Arial, sans-serif" font-size="12.5" fill="#444">Enamine = neutral, soft C-nucleophile. Its β-carbon attacks the β-carbon of the acceptor; water returns the ketone.</text>')
legend_y=660
leg.append(f'<line x1="30" y1="{legend_y}" x2="58" y2="{legend_y}" stroke="{NEW}" stroke-width="2.4"/>')
leg.append(f'<text x="66" y="{legend_y}" dominant-baseline="central" font-family="Helvetica, Arial, sans-serif" font-size="12.5" fill="#444">new C–C bond</text>')
leg.append(f'<path d="M180,{legend_y+6} Q194,{legend_y-10} 208,{legend_y}" fill="none" stroke="{RED}" stroke-width="1.6" marker-end="url(#ah)"/>')
leg.append(f'<text x="218" y="{legend_y}" dominant-baseline="central" font-family="Helvetica, Arial, sans-serif" font-size="12.5" fill="#444">electron-pair movement</text>')
leg.append(f'<text x="30" y="{legend_y+26}" text-anchor="start" dominant-baseline="central" font-family="Helvetica, Arial, sans-serif" font-size="11.5" fill="#666">Source: CM3121 L11 p.19 (MeCN, then H<tspan dy="3" font-size="9">2</tspan><tspan dy="-3">O</tspan>, 95%); mechanism: Clayden 2e p.608</text>')
W,H=800,710
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>
<marker id="rh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#111"/></marker>
</defs>
<rect width="{W}" height="{H}" fill="white"/>
{head}
{"".join(leg)}
{"".join(els)}
</svg>'''
open("enamine_conjugate_addition_p19.svg","w").write(svg)
import cairosvg; cairosvg.svg2png(url="enamine_conjugate_addition_p19.svg",write_to="check1.png",output_width=1200)
