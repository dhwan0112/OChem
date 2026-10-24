import math,re
L=36.0
els=[]; RED="#c0392b"; NEW="#1e8449"; GREY="#444"; BLUE="#2e6fb7"
def text(x,y,t,size=14,c="#111",anchor="middle",weight="normal",style="normal"):
    if "<tspan" in t and anchor=="middle":
        plain=re.sub(r"<[^>]+>","",t); w=sum(size*(0.33 if ch in " .,()" else 0.62 if ch.isupper() else 0.5) for ch in plain)
        x-=w/2; anchor="start"
    els.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="Helvetica, Arial, sans-serif" font-size="{size}" fill="{c}" text-anchor="{anchor}" dominant-baseline="central" font-weight="{weight}" font-style="{style}">{t}</text>')
def sub(a,n,b=""): return f'{a}<tspan dy="4" font-size="10">{n}</tspan><tspan dy="-4">{b}</tspan>'
def sup(a,n,b=""): return f'{a}<tspan dy="-6" font-size="10">{n}</tspan><tspan dy="6">{b}</tspan>'
def line(p,q,c="#111",w=1.7):
    els.append(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>')
class M:
    def __init__(s): s.a={}; s.b=[]
    def at(s,k,p,label=None,anchor="c",trim=10):
        s.a[k]=(p[0],p[1],label,anchor,trim if label else 0); return p
    def bd(s,i,j,o=1,c="#111",inner=None,kind=None): s.b.append((i,j,o,c,inner,kind))
    def p(s,k): return s.a[k][:2]
    def draw(s):
        for i,j,o,c,inner,kind in s.b:
            xi,yi,_,_,ti=s.a[i]; xj,yj,_,_,tj=s.a[j]
            d=math.hypot(xj-xi,yj-yi); ux,uy=(xj-xi)/d,(yj-yi)/d; nx,ny=-uy,ux
            p=(xi+ux*ti,yi+uy*ti); q=(xj-ux*tj,yj-uy*tj)
            if kind=="wedge":
                w=4.2; els.append(f'<polygon points="{p[0]:.1f},{p[1]:.1f} {q[0]+nx*w:.1f},{q[1]+ny*w:.1f} {q[0]-nx*w:.1f},{q[1]-ny*w:.1f}" fill="{c}"/>'); continue
            if o==1: line(p,q,c)
            elif inner is not None:
                line(p,q,c); cx,cy=inner; mx,my=(p[0]+q[0])/2,(p[1]+q[1])/2
                if (cx-mx)*nx+(cy-my)*ny<0: nx,ny=-nx,-ny
                line((p[0]+nx*5+ux*5,p[1]+ny*5+uy*5),(q[0]+nx*5-ux*5,q[1]+ny*5-uy*5),c)
            else:
                for t in (-2.6,2.6): line((p[0]+nx*t,p[1]+ny*t),(q[0]+nx*t,q[1]+ny*t),c)
        for k,(x,y,l,an,_) in s.a.items():
            if not l: continue
            if an=="s": text(x-5,y,l,anchor="start")
            elif an=="e": text(x+5,y,l,anchor="end")
            else: text(x,y,l)
def pol(c,r,ang): return (c[0]+r*math.cos(math.radians(ang)),c[1]+r*math.sin(math.radians(ang)))
def add(p,ang,l=L): return pol(p,l,ang)
R5=L/(2*math.sin(math.radians(36)))
def mid(a,b,dx=0,dy=0): return ((a[0]+b[0])/2+dx,(a[1]+b[1])/2+dy)
def carrow(p,q,bend=0.35,c=RED):
    (x1,y1),(x2,y2)=p,q; mx,my=(x1+x2)/2,(y1+y2)/2; d=math.hypot(x2-x1,y2-y1)
    nx,ny=-(y2-y1)/d,(x2-x1)/d; cx,cy=mx+nx*d*bend,my+ny*d*bend
    els.append(f'<path d="M{x1:.1f},{y1:.1f} Q{cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}" fill="none" stroke="{c}" stroke-width="1.6" marker-end="url(#ah)"/>')
def charge(p,s): els.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="6.5" fill="white" stroke="#111" stroke-width="1"/>'); text(p[0],p[1]+0.5,s,size=12)
def lp(p,ang,dist=12):
    c=pol(p,dist,ang); nx,ny=-math.sin(math.radians(ang)),math.cos(math.radians(ang))
    for t in (-3.4,3.4): els.append(f'<circle cx="{c[0]+nx*t:.1f}" cy="{c[1]+ny*t:.1f}" r="1.7" fill="#111"/>')
def catalyst(m,c,n1label="N",n1H=True):
    # pentagon, N1 at bottom (90°)
    angs={"N1":90,"C5":162,"C4":234,"N3":306,"C2":18}
    for k,a in angs.items():
        lab={"N1":"N","N3":"N"}.get(k)
        m.at(k,pol(c,R5,a),lab)
    for i,j in [("N1","C5"),("C5","C4"),("C4","N3"),("N3","C2"),("C2","N1")]: m.bd(i,j)
    m.at("O4",add(m.p("C4"),234),"O"); m.bd("C4","O4",2)
    m.at("Me3",add(m.p("N3"),306+0),"Me","s"); m.bd("N3","Me3")
    m.at("Me2a",add(m.p("C2"),-12),"Me","s"); m.at("Me2b",add(m.p("C2"),48),"Me","s"); m.bd("C2","Me2a"); m.bd("C2","Me2b")
    m.at("CH2",add(m.p("C5"),162+20)); m.bd("C5","CH2",kind="wedge")
    m.at("Ph",add(m.p("CH2"),120),"Ph"); m.bd("CH2","Ph")
    if n1H: m.at("H1",add(m.p("N1"),90,26),"H"); m.bd("N1","H1")
def pyrrole(m,pre,c,attach_ang,mode="arom"):
    # attach vertex at attach_ang; order going around: C2(attach),C3,C4,C5,N1
    ks=[pre+"C2",pre+"C3",pre+"C4",pre+"C5",pre+"N"]
    angs=[attach_ang+72*i for i in range(5)]
    for k,a in zip(ks,angs): m.at(k,pol(c,R5,a),"N" if k.endswith("N") else None)
    for i in range(5): m.bd(ks[i],ks[(i+1)%5],1)
    # set double bonds
    m.b=[b for b in m.b if not (b[0] in ks and b[1] in ks)]
    dbl={"arom":[(0,1),(2,3)],"pyrrolium":[(1,2),(3,4)]}[mode]
    for i in range(5):
        j=(i+1)%5
        m.bd(ks[i],ks[j],2 if (i,j) in dbl else 1,inner=c if (i,j) in dbl else None)
    nme=pol(c,R5+L,angs[4]); m.at(pre+"Me",nme,"Me"); m.bd(pre+"N",pre+"Me")
    return ks
def rarrow(p,q,label=None,label2=None,lab_side=(0,-14),c="#111",dashed=False):
    da=' stroke-dasharray="6,4"' if dashed else ""
    els.append(f'<line x1="{p[0]}" y1="{p[1]}" x2="{q[0]}" y2="{q[1]}" stroke="{c}" stroke-width="1.9" marker-end="url(#rh)"{da}/>')
def note(x,y,t,size=12.5,c=GREY,anchor="middle",style="normal",weight="normal"): text(x,y,t,size=size,c=c,anchor=anchor,style=style,weight=weight)

# ===== Station 1: catalyst (top-left) =====
c1=(150,170); A=M(); catalyst(A,c1); A.draw()
note(150,275,"chiral 2° amine catalyst (20 mol%)",weight="bold",c="#111")
note(150,293,"imidazolidinone",size=12)
lp(A.p("N1"),180,13)
# arrow 1 -> 2
rarrow((290,175),(445,175))
note(367,140,"+ crotonaldehyde",c="#111",size=13)
note(367,157,sub("(E-MeCH=CHCHO), −H","2","O"),size=12)
note(367,197,"1) condensation",c=BLUE,weight="bold",size=12.5)
note(367,214,"(“imine formation”)",size=12)

# ===== Station 2: iminium (top-right) =====
c2=(600,120); B=M(); catalyst(B,c2,n1H=False); 
n1=B.p("N1")
B.at("k1",add(n1,90)); B.bd("N1","k1",2)
B.at("Hk1",add(B.p("k1"),30,24),"H"); B.bd("k1","Hk1")
B.at("k2",add(B.p("k1"),150)); B.bd("k1","k2")
B.at("k3",add(B.p("k2"),90)); B.bd("k2","k3",2)
B.at("kMe",add(B.p("k3"),150),"Me"); B.bd("k3","kMe")
B.draw()
charge((n1[0]+15,n1[1]-3),"+")
note(B.p("k3")[0]+12,B.p("k3")[1]-14,"β",size=13,c=RED,style="italic")
note(B.p("k2")[0]+12,B.p("k2")[1]+4,"α",size=13,c=RED,style="italic")
# pyrrole attacking from left-bottom
pc=(B.p("k3")[0]+105,B.p("k3")[1]+30)
P=M(); pk=pyrrole(P,"p",pc,180)  # C2 points left toward k3
P.draw()
k3=B.p("k3"); k2=B.p("k2"); k1=B.p("k1")
pN=P.p("pN"); pC2=P.p("pC2"); pC3=P.p("pC3")
carrow(mid(pC2,pC3,-7,-2),(k3[0]+10,k3[1]+4),bend=0.35)
pC4=P.p("pC4"); pC5=P.p("pC5")
carrow(mid(pC4,pC5,-4,0),mid(pC3,pC4,0,7),bend=-0.6)
lp(pN,30,13)
carrow((pN[0]+15,pN[1]+2),mid(pN,pC5,4,6),bend=0.9)
carrow(mid(k3,k2,-7,0),mid(k2,k1,-7,-3),bend=-0.6)
carrow(mid(k1,n1,-7,2),(n1[0]-11,n1[1]+6),bend=0.7)
note(560,372,"iminium ion: more electrophilic than C=O",c="#111",size=12.5,weight="bold")
note(560,389,"(lower LUMO at the β-carbon)",size=12)
note(560,410,"pyrrole attacks the face opposite the benzyl group",size=12,c=NEW)
# arrow 2 -> 3
rarrow((1055,330),(1055,560))
note(1040,445,"2) conjugate addition",c=BLUE,weight="bold",anchor="end",size=12.5)
note(1040,462,"(face-selective)",anchor="end",size=12)

# ===== Station 3: enamine + pyrrolium (bottom-right) =====
c3=(600,560); C=M(); catalyst(C,c3,n1H=False)
n1c=C.p("N1")
C.at("e1",add(n1c,90)); C.bd("N1","e1")
C.at("He1",add(C.p("e1"),30,24),"H"); C.bd("e1","He1")
C.at("e2",add(C.p("e1"),150)); C.bd("e1","e2",2)
C.at("e3",add(C.p("e2"),90)); C.bd("e2","e3")
C.at("eMe",add(C.p("e3"),150),"Me"); C.bd("e3","eMe")
C.draw()
pc3=(C.p("e3")[0]+R5+L*0.95,C.p("e3")[1]+18)
Q=M(); qk=pyrrole(Q,"q",pc3,180+0,mode="pyrrolium")
# new bond e3 - qC2
Q.draw()
line(C.p("e3"),Q.p("qC2"),NEW,2.2)
charge((Q.p("qN")[0]+14,Q.p("qN")[1]+10),"+")
note(Q.p("qC2")[0]+2,Q.p("qC2")[1]-14,"H",size=12)
note(560,815,"enamine + pyrrolium (non-aromatic)",c="#111",size=12.5,weight="bold")
# arrow 3 -> 4
rarrow((470,700),(320,700))
note(395,663,"3) −H"+'<tspan dy="-6" font-size="10">+</tspan><tspan dy="6"> (pyrrole rearomatizes)</tspan>',c=BLUE,size=12.5,weight="bold")
note(395,722,"4) H"+'<tspan dy="4" font-size="10">2</tspan><tspan dy="-4">O: hydrolysis</tspan>',c=BLUE,size=12.5,weight="bold")
note(395,739,"(via the saturated iminium)",size=12)

# ===== Station 4: product (bottom-left) =====
c4=(110,660)
D=M(); dk=pyrrole(D,"d",c4,0)  # C2 points right
s=add(D.p("dC2"),0-30*0, L)  # stereocentre to the right
D.at("s",add(D.p("dC2"),-30)); D.bd("dC2","s",c=NEW)
D.at("sMe",add(D.p("s"),90),"Me"); D.bd("s","sMe",kind="wedge")
D.at("t1",add(D.p("s"),-30)); D.bd("s","t1")
D.at("t2",add(D.p("t1"),30)); D.bd("t1","t2")
D.at("tO",add(D.p("t2"),-30),"O"); D.bd("t2","tO",2)
D.draw()
note(D.p("s")[0]-2,D.p("s")[1]-16,"(R)",size=11.5,style="italic")
note(150,760,"product released",c="#111",size=12.5,weight="bold")
note(150,777,"68–90% yield, 87–97% ee",size=12)
# arrow 4 -> 1 (catalyst regenerated)
rarrow((40,600),(40,250))
note(52,430,"catalyst regenerated",anchor="start",size=12.5,c=BLUE,weight="bold")

W,H=1080,870
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker>
<marker id="rh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#111"/></marker>
</defs>
<rect width="{W}" height="{H}" fill="white"/>
<text x="20" y="32" font-family="Helvetica, Arial, sans-serif" font-size="20" font-weight="bold" fill="#111">Iminium ion catalysis — catalytic cycle (L11 p.21)</text>
{"".join(els)}
<text x="20" y="852" font-family="Helvetica, Arial, sans-serif" font-size="11.5" fill="#666">Source: CM3121 L11 p.21 (imidazolidinone 20 mol%; crotonaldehyde + N-methylpyrrole). Green: new C–C bond. Red arrows: electron-pair movement.</text>
</svg>'''
open("iminium_catalysis_cycle.svg","w").write(svg)
import cairosvg; cairosvg.svg2png(url="iminium_catalysis_cycle.svg",write_to="check3.png",output_width=1300)
