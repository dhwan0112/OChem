from common import *
C=Canvas(1000,760)
def T(x,y,t,size=13,cls="ink",anchor="middle",weight="normal",style="normal"): C.text(x,y,t,size=size,cls=cls,anchor=anchor,weight=weight,style=style)
T(20,28,"Count ELECTRONS, not atoms: components where the numbers differ",size=19,anchor="start",weight="bold")
T(20,52,"Top: structure. Bottom: the p orbitals that react, with the electrons each one brings (dots). Grey = not part of the reacting component.",size=12.5,cls="mutedt",anchor="start")
def bond(p,q,o=1,cls="inks",inner=None): C.bond(p,q,cls,o,inner=inner,trim=(0,0))
def lab(p,t,size=14,cls="ink"):
    C.raw(f'<circle class="bg" cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{7+2*len(t)}"/>'); T(p[0],p[1],t,size=size,cls=cls,weight="bold")
def chg(p,s): C.raw(f'<circle class="bg" cx="{p[0]}" cy="{p[1]}" r="7"/><circle class="inks" cx="{p[0]}" cy="{p[1]}" r="7" stroke-width="1"/>'); T(p[0],p[1]+0.5,s,size=11)
def porb(x,y,ne,active=True,cls="nus"):
    c=cls if active else "muted"
    k="s" if not c.endswith("s") else ""
    cc=c if c.endswith("s") else c
    st=f'class="{cc}" fill="none"' if active else 'class="muted" fill="none" fill-opacity="0"'
    for dy in (-13,13): C.raw(f'<ellipse {st} cx="{x}" cy="{y+dy}" rx="7" ry="13" stroke-width="1.5" {"" if active else "stroke-dasharray=\'3,3\'"}/>')
    C.raw(f'<circle class="ink" cx="{x}" cy="{y}" r="2"/>')
    for i in range(ne): C.raw(f'<circle class="{"nu" if active else "muted"}" cx="{x+13}" cy="{y-5+10*i}" r="3.6"/>')
    T(x,y+40,str(ne) if active else "–",size=13,weight="bold",cls="nu" if active else "mutedt")
def summary(x,y,atoms,e,cls_txt,cls,use):
    T(x,y,atoms if isinstance(atoms,str) and "·" in atoms else f"{atoms} atoms · {e} e⁻",size=13.5,weight="bold"); T(x,y+20,cls_txt,size=14,weight="bold",cls=cls); T(x,y+40,use,size=11.5,cls="mutedt")
PW=245
def panel(i,j): return 10+PW*j+PW/2, 90+330*i
# 1 allyl cation
cx,cy=panel(0,0); T(cx,cy,"allyl cation",size=14,weight="bold")
a=(cx-40,cy+75); b=(cx,cy+52); c=(cx+40,cy+75)
bond(a,b,2); bond(b,c); chg((c[0]+12,c[1]-12),"+")
for x,n in ((cx-40,1),(cx,1),(cx+40,0)): porb(x,cy+150,n)
summary(cx,cy+225,3,2,"(4q+2)","nu","[4+3] cycloaddition: π2s (L14 p.22)")
# 2 oxyallyl (zinc) cation
cx,cy=panel(0,1); T(cx,cy,"zinc oxyallyl cation",size=14,weight="bold")
a=(cx-40,cy+82); b=(cx,cy+60); c=(cx+40,cy+82); o=(cx,cy+28)
bond(a,b,2); bond(b,c); bond(b,(o[0],o[1]+9)); lab(o,"O"); T(o[0]+30,o[1],"ZnBr",size=12,cls="mutedt",weight="bold"); chg((c[0]+12,c[1]-12),"+")
for x,n in ((cx-40,1),(cx,1),(cx+40,0)): porb(x,cy+150,n)
summary(cx,cy+225,3,2,"(4q+2)","nu","O–ZnBr not counted (L14 p.22)")
# 3 allyl anion
cx,cy=panel(0,2); T(cx,cy,"allyl anion",size=14,weight="bold")
a=(cx-40,cy+75); b=(cx,cy+52); c=(cx+40,cy+75)
bond(a,b,2); bond(b,c); chg((c[0]+12,c[1]-12),"−")
for x,n in ((cx-40,1),(cx,1),(cx+40,2)): porb(x,cy+150,n)
summary(cx,cy+225,3,4,"(4r)","el","same atoms as the cation, opposite class")
# 4 nitrone
cx,cy=panel(0,3); T(cx,cy,"nitrone (1,3-dipole)",size=14,weight="bold")
a=(cx-45,cy+75); n=(cx,cy+52); o=(cx+45,cy+75)
bond(a,(n[0]-8,n[1]+4),2); bond((n[0]+8,n[1]+4),(o[0]-8,o[1]-4)); lab(n,"N"); lab(o,"O"); bond((n[0],n[1]-9),(n[0],n[1]-30)); T(n[0],n[1]-38,"R",size=12,weight="bold")
chg((n[0]+15,n[1]-14),"+"); chg((o[0]+15,o[1]-12),"−"); T(a[0]-14,a[1],"R₂C",size=12,anchor="end",weight="bold")
for x,nn in ((cx-45,1),(cx,1),(cx+45,2)): porb(x,cy+150,nn)
summary(cx,cy+225,3,4,"(4r)","el","[3+2] dipole: π4s (L15 p.13–16)")
# 5 ozone
cx,cy=panel(1,0); T(cx,cy,"ozone (1,3-dipole)",size=14,weight="bold")
a=(cx-45,cy+75); m=(cx,cy+52); o=(cx+45,cy+75)
bond((a[0]+8,a[1]-4),(m[0]-8,m[1]+4),2); bond((m[0]+8,m[1]+4),(o[0]-8,o[1]-4)); lab(a,"O"); lab(m,"O"); lab(o,"O")
chg((m[0]+15,m[1]-14),"+"); chg((o[0]+15,o[1]-12),"−")
for x,nn in ((cx-45,1),(cx,1),(cx+45,2)): porb(x,cy+150,nn)
summary(cx,cy+225,3,4,"(4r)","el","ozonolysis [3+2]: π4s (L15 p.21–23)")
# 6 tropone
cx,cy=panel(1,1); T(cx,cy,"tropone",size=14,weight="bold")
R=30; pts=[(cx+R*math.cos(math.radians(-90+k*360/7)),cy+80+R*math.sin(math.radians(-90+k*360/7))) for k in range(7)]
cen=(cx,cy+80)
for k in range(7):
    o_=2 if k in (1,3,5) else 1
    bond(pts[k],pts[(k+1)%7],o_,inner=cen if o_==2 else None,cls="inks")
bond(pts[0],(pts[0][0],pts[0][1]-22),2); lab((pts[0][0],pts[0][1]-30),"O")
xs=[cx-90+i*30 for i in range(7)]
porb(xs[0],cy+150,0,active=False)
for x in xs[1:]: porb(x,cy+150,1)
T(xs[0],cy+122,"C=O",size=10,cls="mutedt")
summary(cx,cy+225,"7 ring",6,"(4q+2)","nu","[6+4]: reacts as π6s (L14 p.21)")
# 7 ketene
cx,cy=panel(1,2); T(cx,cy,"ketene",size=14,weight="bold")
c1=(cx-35,cy+72); c2=(cx+5,cy+72); o=(cx+45,cy+72)
bond(c1,(c2[0]-5,c2[1]),2); bond((c2[0]+5,c2[1]),(o[0]-9,o[1]),2); C.raw(f'<circle class="ink" cx="{c2[0]}" cy="{c2[1]}" r="3.5"/>'); T(c2[0],c2[1]+16,"C",size=12,weight="bold"); lab(o,"O"); T(c1[0]-12,c1[1],"R₂C",size=12,anchor="end",weight="bold")
porb(cx-35,cy+150,1); porb(cx+5,cy+150,1); porb(cx+45,cy+150,0,active=False)
T(cx+45,cy+122,"C=O π (90°)",size=10,cls="mutedt")
summary(cx,cy+225,"C=C=O: 3 atoms · 2 e⁻ react",2,"(4q+2)","nu","[2+2]: only the C=C, as π2a (L15 p.6–7)")
# 8 omega
cx,cy=panel(1,3); T(cx,cy,"single centre (ω)",size=14,weight="bold")
for dx,s,ne,name,clsn in ((-50,"+",0,"ω0 · (4r)","el"),(50,"−",2,"ω2 · (4q+2)","nu")):
    p=(cx+dx,cy+68)
    for ang in (150,30,270): bond(p,pol(p,22,ang))
    chg((p[0]+12,p[1]-12),s)
    porb(cx+dx,cy+150,ne)
    T(cx+dx,cy+222,name,size=13,weight="bold",cls=clsn)
T(cx,cy+246,"1 atom · 0 or 2 e⁻",size=12.5,weight="bold")
T(cx,cy+265,"[2,3] carbanion: ω2a (Clayden p.918)",size=11.5,cls="mutedt")
C.line((20,738),(980,738),"muted",0.8)
T(20,750,"Only neutral all-carbon polyenes have atoms = electrons (ethylene 2/2, butadiene 4/4, hexatriene 6/6). Sources as noted under each panel.",size=11,cls="mutedt",anchor="start")
save(C,"WH_atoms_vs_electrons")
