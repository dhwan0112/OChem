from common import *
C=Canvas(1080,500)
C.text(24,30,"Woodward–Hoffmann counting: which components count?",size=20,anchor="start",weight="bold")
C.text(24,56,"Thermal pericyclic reaction is allowed when (number of (4q+2)s components) + (number of (4r)a components) is ODD.",size=13,cls="mutedt",anchor="start")
# steps on the left
steps=["1. Split the reaction into components","   (π bonds, σ bonds, lone pair / empty p = ω)",
"2. Count electrons in each component","   2, 6, 10 → (4q+2)    0, 4, 8 → (4r)",
"3. Decide s or a for each component","   (same face at both ends = s; opposite = a)",
"4. Count only the shaded cells, then add"]
for i,t in enumerate(steps):
    C.text(30,100+i*24,t,size=13.5 if not t.startswith("   ") else 12.5,cls="ink" if not t.startswith("   ") else "mutedt",anchor="start",weight="bold" if not t.startswith("   ") else "normal")
# matrix
x0,y0,cw,ch=520,135,230,92
hx=x0-130
def cell(x,y,count):
    if count: C.raw(f'<rect class="good" x="{x}" y="{y}" width="{cw}" height="{ch}" fill-opacity="0.16" stroke-width="2"/>')
    else: C.raw(f'<rect class="inks" x="{x}" y="{y}" width="{cw}" height="{ch}" stroke-width="1.2" stroke-dasharray="4,4"/>')
for r in range(2):
    for c in range(2):
        cnt=(r==0 and c==0) or (r==1 and c==1); cell(x0+c*cw,y0+r*ch,cnt)
        cx,cy=x0+c*cw+cw/2,y0+r*ch+ch/2
        if cnt: C.text(cx,cy-12,"COUNT (+1 each)",size=15,cls="good",weight="bold"); C.text(cx,cy+14,["(4q+2)s","","","(4r)a"][r*2+c],size=13,cls="good")
        else: C.text(cx,cy-12,"ignore (0)",size=15,cls="mutedt"); C.text(cx,cy+14,["","(4q+2)a","(4r)s",""][r*2+c],size=13,cls="mutedt")
C.text(x0+cw/2,y0-38,"s (suprafacial)",size=14,weight="bold"); C.text(x0+cw+cw/2,y0-38,"a (antarafacial)",size=14,weight="bold")
C.text(x0+cw/2,y0-18,"bonds on the same face",size=11.5,cls="mutedt"); C.text(x0+cw+cw/2,y0-18,"bonds on opposite faces",size=11.5,cls="mutedt")
C.text(hx+60,y0+ch/2-10,"(4q+2)",size=15,weight="bold"); C.text(hx+60,y0+ch/2+12,"2, 6, 10 e⁻",size=12.5,cls="mutedt")
C.text(hx+60,y0+ch+ch/2-10,"(4r)",size=15,weight="bold"); C.text(hx+60,y0+ch+ch/2+12,"0, 4, 8 e⁻",size=12.5,cls="mutedt")
# mini orbital icons for s and a
def lobe(x,y,up,filled=True,cls="ink"):
    dy=-13 if up else 13
    if filled: C.raw(f'<ellipse class="{cls}" cx="{x}" cy="{y+dy}" rx="6" ry="12" fill-opacity="0.35" stroke-width="1.3"/>')
    else: C.raw(f'<ellipse class="{cls}s" cx="{x}" cy="{y+dy}" rx="6" ry="12" stroke-width="1.3"/>')
# results line
yb=y0+2*ch+42
C.text(x0+cw,yb-9,"sum ODD → thermally allowed",size=14.5,weight="bold",cls="good"); C.text(x0+cw,yb+12,"sum EVEN → thermally forbidden",size=14.5,weight="bold",cls="el")
C.text(x0+cw,yb+35,"photochemical (hν): the opposite parity (even → allowed)",size=13,cls="mutedt")
# q, r note
C.text(30,300,"q and r are just whole numbers (0, 1, 2 …).",size=13,anchor="start",weight="bold")
C.text(30,322,"You never need their values — only whether a component",size=12.5,cls="mutedt",anchor="start")
C.text(30,342,"holds 2/6/10 electrons (4q+2) or 0/4/8 electrons (4r).",size=12.5,cls="mutedt",anchor="start")
C.text(30,374,"Electron count per component, not atom count:",size=13,anchor="start",weight="bold")
C.text(30,396,"allyl cation = 3 atoms, 2 e⁻ → (4q+2);  diene = 4 e⁻ → (4r)",size=12.5,cls="mutedt",anchor="start")
C.text(30,418,"σ C–H bond = 2 e⁻ → (4q+2);  empty p orbital (ω0) = 0 e⁻ → (4r)",size=12.5,cls="mutedt",anchor="start")
C.text(24,478,"Sources: CM3121 L13 p.33–34; L14 p.4–6; L16 p.25 (photochemical reactions follow the opposite rules).",size=11.5,cls="mutedt",anchor="start")
save(C,"WH_counting_rule")
