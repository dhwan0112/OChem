from glyph import *
C=Canvas(1080,945)
C.text(24,32,"Woodward–Hoffmann notation, read in three parts",size=21,anchor="start",weight="bold")
# big anatomy
x0,y0=60,118
C.text(x0,y0,"π",size=64,anchor="start",weight="bold")
C.text(x0+50,y0+16,"2",size=40,anchor="start",weight="bold",cls="nu")
C.text(x0+82,y0+16,"s",size=40,anchor="start",weight="bold",cls="good")
C.text(x0+150,y0+16,"+",size=36,anchor="start")
C.text(x0+200,y0,"π",size=64,anchor="start",weight="bold")
C.text(x0+250,y0+16,"2",size=40,anchor="start",weight="bold",cls="nu")
C.text(x0+282,y0+16,"a",size=40,anchor="start",weight="bold",cls="good")
cap=[(560,78,"① symbol = orbital type","ink","π: π bond / π system   σ: σ bond   ω: lone pair or empty p"),
     (560,128,"② subscript = number of ELECTRONS","nu","not atoms: allyl cation (3 atoms) = 2;  1,3-dipole (3 atoms) = 4"),
     (560,178,"③ letter = which faces the component uses","good","s = suprafacial (same face at both ends); a = antarafacial (opposite faces)")]
for x,y,t,cls,sub in cap:
    C.text(x,y,t,size=15,anchor="start",weight="bold",cls=cls); C.text(x,y+20,sub,size=12.5,anchor="start",cls="mutedt")
# s vs a pictures
yy=285
C.text(60,yy-50,"s vs a at a glance (green arrows = where the new bonds form)",size=14,anchor="start",weight="bold")
def G(x,y,kind,n,face,cls="nus",k=1.6):
    C.raw(f'<g transform="translate({x},{y}) scale({k})">'); comp_glyph(C,0,0,kind,n,face,cls,sp=16); C.raw('</g>')
G(90,yy,"pi",2,"s"); C.text(160,yy,"π2s",size=16,anchor="start",weight="bold"); C.text(210,yy,"both new bonds from the bottom face",size=12.5,anchor="start",cls="mutedt")
G(560,yy,"pi",2,"a"); C.text(630,yy,"π2a",size=16,anchor="start",weight="bold"); C.text(680,yy,"one bond from the bottom, one from the top",size=12.5,anchor="start",cls="mutedt")
G(84,yy+88,"sigma",2,"s",cls="els",k=1.5); C.text(160,yy+88,"σ2s",size=16,anchor="start",weight="bold"); C.text(210,yy+88,"σ bond (C–H, C–C, C–O) used on one side",size=12.5,anchor="start",cls="mutedt")
G(590,yy+88,"omega",1,"a",cls="els",k=1.5); C.text(630,yy+88,"ω2a / ω0a",size=16,anchor="start",weight="bold"); C.text(725,yy+88,"one centre: lone pair (2 e⁻) or empty p (0 e⁻)",size=12.5,anchor="start",cls="mutedt")
# classification table
ty=470
C.text(24,ty-14,"Step 1: classify each component by its electron count",size=16,anchor="start",weight="bold")
cols=[(24,"e⁻"),(84,"class"),(180,"q or r"),(270,"HOMO ends*"),(390,"typical components")]
rows=[("0","(4r)","r = 0","—","ω0: empty p orbital (cation centre)"),
      ("2","(4q+2)","q = 0","S","π2 alkene, C=O;  σ2 C–H, C–C, C–O;  ω2 lone pair;  allyl cation (3 atoms)"),
      ("4","(4r)","r = 1","A","π4 diene;  1,3-dipole (3 atoms);  allyl anion"),
      ("6","(4q+2)","q = 1","S","π6 triene (e.g. tropone, hexatriene)"),
      ("8","(4r)","r = 2","A","π8 tetraene"),
      ("10","(4q+2)","q = 2","S","rare")]
rh=34; y=ty+20
C.raw(f'<rect class="inks" x="20" y="{y-rh/2}" width="1040" height="{rh}" stroke-width="1"/>')
for x,t in cols: C.text(x+4,y,t,size=13.5,anchor="start",weight="bold")
for i,r in enumerate(rows):
    y=ty+20+(i+1)*rh
    shade="nu" if r[1]=="(4q+2)" else "el"
    C.raw(f'<rect class="{shade}" x="20" y="{y-rh/2}" width="1040" height="{rh}" fill-opacity="0.07" stroke-width="0"/>')
    C.line((20,y+rh/2),(1060,y+rh/2),"muted",0.6)
    C.text(28,y,r[0],size=14,anchor="start",weight="bold")
    C.text(88,y,r[1],size=14,anchor="start",weight="bold",cls=shade)
    C.text(184,y,r[2],size=13,anchor="start",cls="mutedt")
    C.text(300,y,r[3],size=14,anchor="start",weight="bold",cls="good" if r[3]=="S" else "el" if r[3]=="A" else "mutedt")
    C.text(394,y,r[4],size=12.5,anchor="start")
# counting matrix
my=ty+20+7*rh+40
C.text(24,my,"Step 2: count only these two kinds, then add",size=16,anchor="start",weight="bold")
bx,by,bw,bh=200,my+22,180,46
C.text(bx+bw/2,by-6+0,"",size=1)
C.text(bx+bw/2,by-2,"s",size=14,weight="bold"); C.text(bx+bw+bw/2,by-2,"a",size=14,weight="bold")
for r,lab in enumerate(["(4q+2)","(4r)"]):
    C.text(bx-12,by+16+bh/2+r*bh,lab,size=14,anchor="end",weight="bold")
    for c in range(2):
        cnt=(r==0 and c==0) or (r==1 and c==1)
        X=bx+c*bw; Yb=by+16+r*bh
        if cnt: C.raw(f'<rect class="good" x="{X}" y="{Yb}" width="{bw}" height="{bh}" fill-opacity="0.16" stroke-width="2"/>'); C.text(X+bw/2,Yb+bh/2,"+1",size=16,cls="good",weight="bold")
        else: C.raw(f'<rect class="inks" x="{X}" y="{Yb}" width="{bw}" height="{bh}" stroke-width="1" stroke-dasharray="4,4"/>'); C.text(X+bw/2,Yb+bh/2,"0",size=16,cls="mutedt")
C.text(620,my+40,"sum ODD  → thermally allowed",size=15,anchor="start",weight="bold",cls="good")
C.text(620,my+66,"sum EVEN → thermally forbidden",size=15,anchor="start",weight="bold",cls="el")
C.text(620,my+92,"hν: opposite (even → allowed)",size=13,anchor="start",cls="mutedt")
C.text(24,928,"*HOMO ends: S = same sign at both ends, A = opposite (explanatory label, not lecture notation). Sources: L14 p.4–6; L15 p.13; Clayden 2e p.886–888.",size=11.5,cls="mutedt",anchor="start")
save2(C,"WH_notation_table")
