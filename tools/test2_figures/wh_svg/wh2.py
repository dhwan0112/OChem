from common import *
C=Canvas(1080,860)
C.text(24,30,"Worked examples: classify each component, then count",size=20,anchor="start",weight="bold")
C.text(24,56,"Lobes show only the faces used to form bonds (phases omitted). Green dashed: bond forming; grey: bond breaking.",size=13,cls="mutedt",anchor="start")
RY=15; RX=7; SP=44
def atom(x,y,cls="ink"):
    for dy in (-RY,RY): C.raw(f'<ellipse class="{cls}s" cx="{x:.1f}" cy="{y+dy:.1f}" rx="{RX}" ry="{RY}" stroke-width="1.4"/>')
    C.raw(f'<circle class="ink" cx="{x:.1f}" cy="{y:.1f}" r="2.4"/>')
def comp(xs,y,cls,label=None,lx=None,ly=None):
    C.line((xs[0],y),(xs[-1],y),"inks",1.3)
    for x in xs: atom(x,y,cls)
    if label: C.text(lx if lx else (xs[0]+xs[-1])/2, ly if ly else y, label, size=12.5, cls=cls, anchor="middle")
def tip(x,y,up): return (x,y-2*RY-1) if up else (x,y+2*RY+1)
def form(p,q): C.line(p,q,"goods",2.2,"5,4")
def formcurve(p,q,c):
    C.raw(f'<path class="goods" d="M{p[0]:.1f},{p[1]:.1f} Q{c[0]:.1f},{c[1]:.1f} {q[0]:.1f},{q[1]:.1f}" stroke-width="2.2" stroke-dasharray="5,4"/>')
def brk(p,q): C.line(p,q,"muted",2.2,"2,4")
def tally(x0,y,rows,total,verdict,ok):
    for i,(sym,klass,cnt) in enumerate(rows):
        C.text(x0+18,y+i*20,sym,size=12.5,anchor="start",weight="bold")
        C.text(x0+98,y+i*20,klass,size=12,cls="mutedt",anchor="start")
        C.text(x0+300,y+i*20,cnt,size=12.5,cls="good" if cnt=="+1" else "mutedt",anchor="end",weight="bold")
    yy=y+len(rows)*20+4; C.line((x0+18,yy-8),(x0+300,yy-8),"inks",1)
    C.text(x0+18,yy+6,f"sum = {total}",size=13,anchor="start",weight="bold")
    C.text(x0+300,yy+6,verdict,size=13,anchor="end",weight="bold",cls="good" if ok else "el")
def title(x0,y,t,sub): C.text(x0+160,y,t,size=14.5,weight="bold"); C.text(x0+160,y+19,sub,size=12,cls="mutedt")
# ---------- Row 1 ----------
Y1=95
# (a) Diels-Alder
x0=20; title(x0,Y1,"(a) Diels–Alder [4+2]","L14 p.6")
xs=[x0+160-1.5*SP+i*SP for i in range(4)]; yt=Y1+80; yb=Y1+190
comp(xs,yt,"nu"); comp([xs[0],xs[3]],yb,"el")
form(tip(xs[0],yt,False),tip(xs[0],yb,True)); form(tip(xs[3],yt,False),tip(xs[3],yb,True))
C.text(xs[3]+30,yt,"π4s",size=13,cls="nu",anchor="start",weight="bold"); C.text(xs[3]+30,yb,"π2s",size=13,cls="el",anchor="start",weight="bold")
tally(x0,Y1+250,[("π4s","4 e⁻ = (4r), s","0"),("π2s","2 e⁻ = (4q+2), s","+1")],1,"odd → allowed",True)
# (b) [2+2] supra-supra
x0=380; title(x0,Y1,"(b) thermal [2+2], supra/supra","L14 p.24–25")
xs=[x0+160-SP*0.75,x0+160+SP*0.75]
comp(xs,yt,"nu"); comp(xs,yb,"el")
form(tip(xs[0],yt,False),tip(xs[0],yb,True)); form(tip(xs[1],yt,False),tip(xs[1],yb,True))
C.text(xs[1]+30,yt,"π2s",size=13,cls="nu",anchor="start",weight="bold"); C.text(xs[1]+30,yb,"π2s",size=13,cls="el",anchor="start",weight="bold")
tally(x0,Y1+250,[("π2s","2 e⁻ = (4q+2), s","+1"),("π2s","2 e⁻ = (4q+2), s","+1")],2,"even → forbidden",False)
# (c) ketene [2+2]
x0=740; title(x0,Y1,"(c) ketene [2+2]: π2s + π2a","L15 p.6–8, 32")
xs=[x0+160-SP*0.75,x0+160+SP*0.75]
comp(xs,yt,"nu"); comp(xs,yb,"el")
form(tip(xs[0],yt,False),tip(xs[0],yb,True))
# antarafacial: right atom of bottom component bonds through its BOTTOM lobe
formcurve(tip(xs[1],yt,False),tip(xs[1],yb,False),(xs[1]+95,yb-10))
C.text(xs[0]-25,yt,"π2s (alkene)",size=13,cls="nu",anchor="end",weight="bold"); C.text(xs[0]-25,yb,"π2a (ketene C=C)",size=13,cls="el",anchor="end",weight="bold")
C.text(xs[1]+30,yb-62,"opposite face",size=11,cls="good",anchor="start")
tally(x0,Y1+250,[("π2s","2 e⁻ = (4q+2), s","+1"),("π2a","2 e⁻ = (4q+2), a","0")],1,"odd → allowed",True)
# ---------- Row 2 ----------
Y2=470
# (d) [1,5]-H shift
x0=20; title(x0,Y2,"(d) [1,5]-H shift, suprafacial","L16 p.21–22")
xs=[x0+160-2*SP+i*SP for i in range(5)]; yc=Y2+150
comp(xs[1:],yc,"nu")
atom(xs[0],yc,"ink"); C.line((xs[0],yc),(xs[1],yc),"inks",1.3)
hx,hy=(xs[0]+xs[4])/2,yc-95
C.raw(f'<circle class="els" cx="{hx}" cy="{hy}" r="9" stroke-width="1.6"/>'); C.text(hx,hy,"H",size=11)
brk((hx-8,hy+5),tip(xs[0],yc,True)); form((hx+8,hy+5),tip(xs[4],yc,True))
C.text(xs[0],yc+48,"C1",size=11,cls="mutedt"); C.text(xs[4],yc+48,"C5",size=11,cls="mutedt")
C.text(hx+16,hy-14,"σ2s (C1–H)",size=13,cls="el",anchor="start",weight="bold"); C.text((xs[1]+xs[4])/2,yc+68,"π4s (diene)",size=13,cls="nu",weight="bold")
tally(x0,Y2+250,[("σ2s","2 e⁻ = (4q+2), s","+1"),("π4s","4 e⁻ = (4r), s","0")],1,"odd → allowed",True)
# (e) [1,3]-H shift
x0=380; title(x0,Y2,"(e) [1,3]-H shift","L16 p.24")
xs=[x0+160-SP+i*SP for i in range(3)]
comp(xs[1:],yc,"nu"); atom(xs[0],yc,"ink"); C.line((xs[0],yc),(xs[1],yc),"inks",1.3)
hx,hy=xs[1],yc-90
C.raw(f'<circle class="els" cx="{hx}" cy="{hy}" r="9" stroke-width="1.6"/>'); C.text(hx,hy,"H",size=11)
brk((hx-7,hy+6),tip(xs[0],yc,True))
formcurve((hx+8,hy+5),tip(xs[2],yc,False),(xs[2]+110,yc-40))
C.text(xs[2]+40,yc+40,"H must reach the",size=11,cls="good",anchor="start"); C.text(xs[2]+40,yc+55,"opposite face: too far",size=11,cls="good",anchor="start")
C.text(hx+16,hy-14,"σ2s",size=13,cls="el",anchor="start",weight="bold"); C.text((xs[1]+xs[2])/2,yc+68,"π2",size=13,cls="nu",weight="bold")
yy=Y2+250
C.text(x0+18,yy,"π2s + σ2s",size=12.5,anchor="start",weight="bold"); C.text(x0+150,yy,"1 + 1",size=12,cls="mutedt",anchor="start"); C.text(x0+300,yy,"2 → forbidden",size=12.5,cls="el",anchor="end",weight="bold")
C.text(x0+18,yy+20,"π2a + σ2s",size=12.5,anchor="start",weight="bold"); C.text(x0+150,yy+20,"0 + 1",size=12,cls="mutedt",anchor="start"); C.text(x0+300,yy+20,"1 → allowed*",size=12.5,cls="good",anchor="end",weight="bold")
C.line((x0+18,yy+32),(x0+300,yy+32),"inks",1)
C.text(x0+18,yy+46,"*but geometrically impossible → no [1,3]-H shift",size=12,cls="el",anchor="start")
# (f) [3,3] Claisen / Cope
x0=740; title(x0,Y2,"(f) [3,3] (Claisen, Cope), chair TS","L16 p.6")
xs=[x0+160-SP+i*SP for i in range(3)]; yt2=yc-50; yb2=yc+50
comp(xs[1:],yt2,"nu"); comp(xs[1:],yb2,"nu")
atom(xs[0],yt2,"ink"); atom(xs[0],yb2,"ink"); C.line((xs[0],yt2),(xs[1],yt2),"inks",1.3); C.line((xs[0],yb2),(xs[1],yb2),"inks",1.3)
brk(tip(xs[0],yt2,False),tip(xs[0],yb2,True)); form(tip(xs[2],yt2,False),tip(xs[2],yb2,True))
C.text(xs[0]-14,yc,"σ2s",size=13,cls="el",anchor="end",weight="bold")
C.text(xs[2]+28,yt2,"π2s",size=13,cls="nu",anchor="start",weight="bold"); C.text(xs[2]+28,yb2,"π2s",size=13,cls="nu",anchor="start",weight="bold")
tally(x0,Y2+250,[("σ2s","2 e⁻ = (4q+2), s","+1"),("π2s","2 e⁻ = (4q+2), s","+1"),("π2s","2 e⁻ = (4q+2), s","+1")],3,"odd → allowed",True)
C.text(24,845,"Sources: CM3121 L14 p.4–7, 24–25; L15 p.6–8, 32; L16 p.6, 21–24. Ketene (c): the C=C reacts antarafacially, helped by the orthogonal C=O π (Clayden p.898–899).",size=11.5,cls="mutedt",anchor="start")
save(C,"WH_counting_examples")
