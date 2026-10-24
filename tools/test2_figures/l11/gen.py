import math
L=40.0; DX=34.64; DY=20
els=[]; RED="#c0392b"; NEW="#1e8449"; GREY="#444"
def sub(t,n): return f'{t}<tspan dy="4" font-size="11">{n}</tspan><tspan dy="-4"> </tspan>'
def text(x,y,t,size=15,c="#111",anchor="middle",weight="normal",style="normal"):
    if "<tspan" in t and anchor=="middle":
        import re
        plain=re.sub(r"<[^>]+>","",t); w=0
        for ch in plain: w+= size*(0.33 if ch in " .,()" else 0.62 if ch.isupper() else 0.5)
        x-=w/2; anchor="start"
    els.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="Helvetica, Arial, sans-serif" font-size="{size}" fill="{c}" text-anchor="{anchor}" dominant-baseline="central" font-weight="{weight}" font-style="{style}">{t}</text>')
def line(p,q,c="#111",w=1.8):
    els.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>')
class Mol:
    def __init__(s): s.a={}; s.b=[]
    def atom(s,k,x,y,label=None,anchor="c",trim=11):
        s.a[k]=(x,y,label,anchor,trim if label else 0)
    def bond(s,i,j,o=1,c="#111"): s.b.append((i,j,o,c))
    def draw(s):
        for i,j,o,c in s.b:
            xi,yi,_,_,ti=s.a[i]; xj,yj,_,_,tj=s.a[j]
            d=math.hypot(xj-xi,yj-yi); ux,uy=(xj-xi)/d,(yj-yi)/d
            p=(xi+ux*ti,yi+uy*ti); q=(xj-ux*tj,yj-uy*tj)
            if o==1: line(p,q,c)
            else:
                nx,ny=-uy,ux
                for t in (-2.8,2.8): line((p[0]+nx*t,p[1]+ny*t),(q[0]+nx*t,q[1]+ny*t),c)
        for k,(x,y,l,an,_) in s.a.items():
            if not l: continue
            if an=="s": text(x-5.5,y,l,anchor="start")
            elif an=="e": text(x+5.5,y,l,anchor="end")
            else: text(x,y,l)
    def p(s,k): return s.a[k][:2]
def mid(a,b,dx=0,dy=0): return ((a[0]+b[0])/2+dx,(a[1]+b[1])/2+dy)
def carrow(p,q,bend=0.35):
    (x1,y1),(x2,y2)=p,q; mx,my=(x1+x2)/2,(y1+y2)/2; d=math.hypot(x2-x1,y2-y1)
    nx,ny=-(y2-y1)/d,(x2-x1)/d; cx,cy=mx+nx*d*bend,my+ny*d*bend
    els.append(f'<path d="M{x1:.1f},{y1:.1f} Q{cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}" fill="none" stroke="{RED}" stroke-width="1.6" marker-end="url(#ah)"/>')
def rarrow(x1,x2,y,above=None,below=None,below2=None):
    els.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#111" stroke-width="1.8" marker-end="url(#rh)"/>')
    if above: text((x1+x2)/2,y-14,above,size=14)
    if below: text((x1+x2)/2,y+15,below,size=12.5,c=GREY)
    if below2: text((x1+x2)/2,y+31,below2,size=12.5,c=GREY)
def charge(x,y,s):
    els.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6.5" fill="white" stroke="#111" stroke-width="1"/>'); text(x,y+0.5,s,size=12)
def greek(x,y,t): text(x,y,t,size=13,c=RED,style="italic")
def rowlabel(y,t): text(30,y,t,size=13,c=GREY,anchor="start",weight="bold")
R1,R2,R3="R¹","R²","R³"; NR2=sub("NR","2"); NR2p=NR2
# ---------- Row 1: enamine formation ----------
Y=165; rowlabel(Y-75,"1. enamine formation (L11 p.18)")
x=70
K=Mol(); K.atom("r1",x,Y,R1,"e"); K.atom("c1",x+DX,Y-DY); K.atom("o",x+DX,Y-DY-L,"O"); K.atom("c2",x+2*DX,Y); K.atom("r2",x+3*DX,Y-DY,R2,"s")
K.bond("r1","c1"); K.bond("c1","o",2); K.bond("c1","c2"); K.bond("c2","r2"); K.draw()
greek(x+2*DX,Y+15,"α")
text(x+3*DX+48,Y-8,"+",size=20); text(x+3*DX+95,Y-8,"R"+'<tspan dy="4" font-size="11">2</tspan><tspan dy="-4">NH</tspan>')
text(x+3*DX+95,Y+14,"(2° amine)",size=11.5,c=GREY)
rarrow(370,520,Y-8,above="H"+'<tspan dy="-5" font-size="10">+</tspan><tspan dy="5"> (cat.)</tspan>',below="−H₂O".replace("₂",'<tspan dy="3" font-size="10">2</tspan><tspan dy="-3">O</tspan>').replace("<tspan dy=\"-3\">O</tspan>O","<tspan dy=\"-3\">O</tspan>"),below2="via iminium, then loss of H"+'<tspan dy="-5" font-size="10">+</tspan><tspan dy="5"> from the α-C</tspan>')
x=575
E=Mol(); E.atom("r1",x,Y,R1,"e"); E.atom("c1",x+DX,Y-DY); E.atom("n",x+DX,Y-DY-L,NR2,"s"); E.atom("c2",x+2*DX,Y); E.atom("r2",x+3*DX,Y-DY,R2,"s")
E.bond("r1","c1"); E.bond("c1","n"); E.bond("c1","c2",2); E.bond("c2","r2"); E.draw()
greek(x+2*DX,Y+15,"α"); text(x+3*DX+60,Y+2,"enamine",size=12.5,c=GREY,anchor="start")
# ---------- Row 2: conjugate addition ----------
Y=370; rowlabel(Y-95,"2. conjugate (1,4) addition (L11 p.19)")
x=70
E2=Mol(); E2.atom("r1",x,Y,R1,"e"); E2.atom("c1",x+DX,Y-DY); E2.atom("n",x+DX,Y-DY-L,NR2,"s"); E2.atom("c2",x+2*DX,Y); E2.atom("r2",x+2*DX,Y+L,R2,"c")
E2.bond("r1","c1"); E2.bond("c1","n"); E2.bond("c1","c2",2); E2.bond("c2","r2"); E2.draw()
n=E2.p("n")
for dy in (-3.5,3.5): els.append(f'<circle cx="{n[0]-12:.1f}" cy="{n[1]+dy:.1f}" r="1.7" fill="#111"/>')
greek(x+2*DX+14,Y+8,"α")
bx=x+2*DX+95
A=Mol(); A.atom("r3",bx,Y,R3,"e"); A.atom("cb",bx+DX,Y-DY); A.atom("ca",bx+2*DX,Y); A.atom("cc",bx+3*DX,Y-DY); A.atom("o",bx+3*DX,Y-DY-L,"O"); A.atom("z",bx+4*DX,Y,"Z","s")
A.bond("r3","cb"); A.bond("cb","ca",2); A.bond("ca","cc"); A.bond("cc","o",2); A.bond("cc","z"); A.draw()
greek(bx+DX,Y-36,"β"); greek(bx+2*DX,Y+15,"α")
text(bx-42,Y-4,"+",size=20)
c1,c2=E2.p("c1"),E2.p("c2")
carrow((n[0]-15,n[1]+6),mid(n,c1,-5,2),bend=0.9)
carrow(mid(c1,c2,3,-6),(A.p("cb")[0]-8,A.p("cb")[1]-6),bend=-0.4)
cb,ca,cc,o=A.p("cb"),A.p("ca"),A.p("cc"),A.p("o")
carrow(mid(cb,ca,2,-4),mid(ca,cc,-2,-5),bend=-0.55)
carrow(mid(cc,o,6,6),(o[0]+12,o[1]-2),bend=0.45)
rarrow(440,520,Y-5)
x=560
Zw=Mol(); Zw.atom("r1",x,Y,R1,"e"); Zw.atom("c1",x+DX,Y-DY); Zw.atom("n",x+DX,Y-DY-L,NR2,"s"); Zw.atom("c2",x+2*DX,Y); Zw.atom("r2",x+2*DX,Y+L,R2)
Zw.atom("c3",x+3*DX,Y-DY); Zw.atom("r3",x+3*DX,Y-DY-L,R3); Zw.atom("c4",x+4*DX,Y); Zw.atom("c5",x+5*DX,Y-DY); Zw.atom("o",x+5*DX,Y-DY-L,"O"); Zw.atom("z",x+6*DX,Y,"Z","s")
Zw.bond("r1","c1"); Zw.bond("c1","n",2); Zw.bond("c1","c2"); Zw.bond("c2","r2"); Zw.bond("c2","c3",c=NEW); Zw.bond("c3","r3"); Zw.bond("c3","c4"); Zw.bond("c4","c5",2); Zw.bond("c5","o"); Zw.bond("c5","z"); Zw.draw()
nn=Zw.p("n"); charge(nn[0]-14,nn[1]-12,"+"); oo=Zw.p("o"); charge(oo[0]+14,oo[1]-10,"−")
text(x+3*DX,Y+68,"iminium / enolate (zwitterion)",size=12,c=GREY)
# ---------- Row 3: hydrolysis ----------
Y=585; rowlabel(Y-95,"3. aqueous work-up (L11 p.19: “then H₂O”)".replace("H₂O","H<tspan dy='3' font-size='10'>2</tspan><tspan dy='-3'>O</tspan>"))
rarrow(60,215,Y-5,above="H"+'<tspan dy="4" font-size="10">2</tspan><tspan dy="-4">O</tspan>',below="proton transfer,",below2="iminium hydrolysis")
x=290
P=Mol(); P.atom("r1",x,Y,R1,"e"); P.atom("c1",x+DX,Y-DY); P.atom("o1",x+DX,Y-DY-L,"O"); P.atom("c2",x+2*DX,Y); P.atom("r2",x+2*DX,Y+L,R2)
P.atom("c3",x+3*DX,Y-DY); P.atom("r3",x+3*DX,Y-DY-L,R3); P.atom("c4",x+4*DX,Y); P.atom("c5",x+5*DX,Y-DY); P.atom("o5",x+5*DX,Y-DY-L,"O"); P.atom("z",x+6*DX,Y,"Z","s")
P.bond("r1","c1"); P.bond("c1","o1",2); P.bond("c1","c2"); P.bond("c2","r2"); P.bond("c2","c3",c=NEW); P.bond("c3","r3"); P.bond("c3","c4"); P.bond("c4","c5"); P.bond("c5","o5",2); P.bond("c5","z"); P.draw()
for i,k in enumerate(["c1","c2","c3","c4","c5"],1):
    px,py=P.p(k); text(px,py+(-15 if i in (2,4) else 15),str(i),size=11,c="#2e6fb7",weight="bold")
text(x+3*DX,Y+72,"1,5-dicarbonyl compound",size=13.5,weight="bold")
text(640,Y-5,"+",size=20); text(700,Y-5,"R"+'<tspan dy="4" font-size="11">2</tspan><tspan dy="-4">NH</tspan>')
text(700,Y+17,"(recovered)",size=11.5,c=GREY)
# legend
ly=715
leg=[f'<line x1="30" y1="{ly}" x2="58" y2="{ly}" stroke="{NEW}" stroke-width="2.4"/>',
f'<text x="66" y="{ly}" dominant-baseline="central" font-family="Helvetica, Arial, sans-serif" font-size="12.5" fill="{GREY}">new C–C bond</text>',
f'<path d="M180,{ly+6} Q194,{ly-10} 208,{ly}" fill="none" stroke="{RED}" stroke-width="1.6" marker-end="url(#ah)"/>',
f'<text x="218" y="{ly}" dominant-baseline="central" font-family="Helvetica, Arial, sans-serif" font-size="12.5" fill="{GREY}">electron-pair movement</text>',
f'<text x="400" y="{ly}" dominant-baseline="central" font-family="Helvetica, Arial, sans-serif" font-size="12.5" fill="#2e6fb7">1–5: carbonyl C to carbonyl C</text>',
f'<text x="30" y="{ly+28}" dominant-baseline="central" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="{GREY}">Z = H, R, OR (aldehyde, ketone, ester acceptor); R¹ and R² may be joined in a ring (e.g. cyclohexanone enamine); typical 2° amines: pyrrolidine, morpholine.</text>',
f'<text x="30" y="{ly+50}" dominant-baseline="central" font-family="Helvetica, Arial, sans-serif" font-size="11.5" fill="#666">Sources: CM3121 L11 p.14, 18–19; curved-arrow mechanism: Clayden 2e p.608 (supplement).</text>']
W,H=900,790
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>
<marker id="rh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#111"/></marker>
</defs>
<rect width="{W}" height="{H}" fill="white"/>
<text x="30" y="36" font-family="Helvetica, Arial, sans-serif" font-size="20" font-weight="bold" fill="#111">Conjugate addition of enamines — general scheme</text>
<text x="30" y="60" font-family="Helvetica, Arial, sans-serif" font-size="12.5" fill="{GREY}">The enamine α-carbon (neutral, soft C-nucleophile) attacks the β-carbon of an α,β-unsaturated carbonyl; water then restores both C=O groups.</text>
{"".join(leg)}
{"".join(els)}
</svg>'''
open("enamine_conjugate_addition_general.svg","w").write(svg)
import cairosvg; cairosvg.svg2png(url="enamine_conjugate_addition_general.svg",write_to="check2.png",output_width=1300)
