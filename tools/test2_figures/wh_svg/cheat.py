from common import *
C=Canvas(1000,640)
def T(x,y,t,size=13,cls="ink",anchor="start",weight="normal",style="normal"): C.text(x,y,t,size=size,cls=cls,anchor=anchor,weight=weight,style=style)
T(20,26,"Woodward–Hoffmann: thermal pericyclic reactions",size=19,weight="bold")
T(20,52,"allowed ⇔  #(4q+2)s  +  #(4r)a  = ODD",size=15.5,weight="bold",cls="good")
T(430,52,"even → forbidden ·  hν: reverse (even → allowed)",size=13,cls="mutedt")
C.line((20,68),(980,68),"muted",0.8)
# left column
x=20; y=92
T(x,y,"1  Notation  π 2 s",size=14,weight="bold"); y+=20
for t in ["π / σ / ω = orbital type (ω = lone pair or empty p)","number = ELECTRONS in that component (not atoms)","s = same face at both ends · a = opposite faces (twist)"]:
    T(x+12,y,t,size=12.5); y+=19
y+=10; T(x,y,"2  Classify by electron count",size=14,weight="bold"); y+=22
T(x+12,y,"2, 6, 10 e⁻  →  (4q+2)",size=13,cls="nu",weight="bold"); T(x+215,y,"0, 4, 8 e⁻  →  (4r)",size=13,cls="el",weight="bold"); y+=19
T(x+12,y,"q, r values are never used — only the class",size=12.5,cls="mutedt"); y+=28
T(x,y,"3  Count only two kinds",size=14,weight="bold"); y+=24
gx=x+120
T(gx+50,y,"s",size=13,weight="bold",anchor="middle"); T(gx+150,y,"a",size=13,weight="bold",anchor="middle"); y+=8
C.line((gx,y),(gx+200,y),"muted",0.8); C.line((gx,y+56),(gx+200,y+56),"muted",0.8); C.line((gx+100,y),(gx+100,y+56),"muted",0.8); C.line((gx,y+28),(gx+200,y+28),"muted",0.8)
T(gx-8,y+14,"(4q+2)",size=12.5,anchor="end",weight="bold",cls="nu"); T(gx-8,y+42,"(4r)",size=12.5,anchor="end",weight="bold",cls="el")
T(gx+50,y+14,"+1",size=14,anchor="middle",weight="bold",cls="good"); T(gx+150,y+14,"0",size=13,anchor="middle",cls="mutedt")
T(gx+50,y+42,"0",size=13,anchor="middle",cls="mutedt"); T(gx+150,y+42,"+1",size=14,anchor="middle",weight="bold",cls="good")
y+=80
T(x,y,"Why odd: HOMO of one component must meet the LUMO of",size=12.5,cls="mutedt"); y+=18
T(x,y,"the other in phase at every new bond; a LUMO has the",size=12.5,cls="mutedt"); y+=18
T(x,y,"opposite end-symmetry to its own HOMO → exactly one",size=12.5,cls="mutedt"); y+=18
T(x,y,"counted component (or 3, 5 …).",size=12.5,cls="mutedt"); y+=28
T(x,y,"Electron-count traps",size=14,weight="bold",cls="el"); y+=20
traps=["allyl cation (3 atoms) = 2 e⁻ → (4q+2);  allyl anion = 4 e⁻","1,3-dipole (3 atoms) = 4 e⁻ → (4r);  oxyallyl cation = 2 e⁻",
"tropone reacts as π6 (the C=O π is not used)","ketene: the C=C reacts (π2a), not the whole C=C=O",
"σ C–H or C–C = 2 e⁻;  lone pair ω2;  empty p ω0","[i,j] in sigmatropic names = ATOMS, not electrons",
"atoms = electrons only for neutral all-C polyenes"]
for t in traps: T(x+12,y,"• "+t,size=12.2); y+=18
# right column
x=500; y=92
T(x,y,"Worked counts (thermal)",size=14,weight="bold"); y+=22
rows=[("DA [4+2]","π4s + π2s","1","✓"),("[4+4]","π4s + π4s","0","✗"),("alkene [2+2]","π2s + π2s","2","✗  hν ✓"),
("ketene [2+2]","π2s + π2a","1","✓"),("[6+4]","π6s + π4s","1","✓"),("[4+3] allyl⁺","π4s + π2s","1","✓"),("[3+2] dipolar","π4s + π2s","1","✓"),
("[1,5]-H","σ2s + π4s","1","✓ supra"),("[1,7]-H","σ2s + π6a","1","✓ antara"),("[1,3]-H","σ2s + π2s","2","✗ (antara: too short)"),
("[3,3] Claisen/Cope","σ2s + π2s + π2s","3","✓ chair"),("[2,3]","ω2a + σ2s + π2a","1","✓"),("4π electrocyclic","π4a","1","✓ conrotatory"),("6π electrocyclic","π6s","1","✓ disrotatory")]
T(x,y,"reaction",size=11.5,cls="mutedt"); T(x+150,y,"components",size=11.5,cls="mutedt"); T(x+300,y,"sum",size=11.5,cls="mutedt"); T(x+340,y,"verdict",size=11.5,cls="mutedt"); y+=6
C.line((x,y),(x+460,y),"muted",0.8); y+=16
for r in rows:
    ok=int(r[2])%2==1
    T(x,y,r[0],size=12.5,weight="bold"); T(x+150,y,r[1],size=12.5); T(x+305,y,r[2],size=13,weight="bold",cls="good" if ok else "el",anchor="middle"); T(x+340,y,r[3],size=12,cls="good" if ok else "el",weight="bold")
    y+=21
y+=10
T(x,y,"Allowed ≠ happens: the twist (a) must be feasible",size=13.5,weight="bold"); y+=20
for t in ["ketene: sp C, no substituent + orthogonal C=O π* → works","simple alkene crossed: 2 bonding vs 2 antibonding, H clash → no","[1,7]-H: long chain coils (helix) → works;  [1,3]-H: too short → no"]:
    T(x+12,y,"• "+t,size=12.2); y+=18
C.line((20,612),(980,612),"muted",0.8)
T(20,628,"Sources: CM3121 L13 p.33–35; L14 p.4–7, 21–26; L15 p.6–8, 13; L16 p.6, 21–24; Clayden 2e p.886–888, 898–899, 918, 922–924.",size=10.5,cls="mutedt")
save(C,"WH_cheatsheet_card")
