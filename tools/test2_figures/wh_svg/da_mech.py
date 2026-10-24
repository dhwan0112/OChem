from common import *
L=44; C=Canvas(1080,440)
C.text(24,30,"Diels–Alder: a [4+2] cycloaddition",size=20,anchor="start",weight="bold")
C.text(24,56,"diene (4π, HOMO) + dienophile (2π, LUMO) → cyclohexene; one concerted step through a cyclic 6-electron TS",size=13,cls="mutedt",anchor="start")
def hexpts(c): return {k:pol(c,L,a) for k,a in zip(["C1","C6","C5","C4","C3","C2"],[-90,-30,30,90,150,210])}
# reactants
c0=(150,215); h=hexpts(c0); sh=26
d6=(h["C6"][0]+sh,h["C6"][1]); d5=(h["C5"][0]+sh,h["C5"][1])
C.bond(h["C1"],h["C2"],"nus",2); C.bond(h["C2"],h["C3"],"nus"); C.bond(h["C3"],h["C4"],"nus",2)
C.bond(d6,d5,"els",2)
for k,lab in [("C1","1"),("C2","2"),("C3","3"),("C4","4")]:
    p=h[k]; C.text(p[0]+(-14 if k in("C2","C3") else -12),p[1]+(-4 if k=="C1" else 4 if k=="C4" else 0),lab,size=11,cls="mutedt")
C.text(d6[0]+13,d6[1]-4,"6",size=11,cls="mutedt"); C.text(d5[0]+13,d5[1]+4,"5",size=11,cls="mutedt")
# arrows: C1=C2 -> C2-C3 ; C3=C4 -> C4...C5 ; C5=C6 -> C6...C1
C.carrow(mid(h["C1"],h["C2"],-7,-4),mid(h["C2"],h["C3"],-9,0),bend=0.55)
C.carrow(mid(h["C3"],h["C4"],-4,7),(d5[0]-8,d5[1]+9),bend=0.45)
C.carrow(mid(d6,d5,9,0),(h["C1"][0]+9,h["C1"][1]-9),bend=0.55)
C.text(c0[0],c0[1]+92,"s-cis diene",size=13,cls="nu"); C.text(d6[0]+10,c0[1]+92,"dienophile",size=13,cls="el",anchor="start")
C.rarrow((260,215),(330,215)); 
# TS
c1=(430,215); h=hexpts(c1)
C.bond(h["C1"],h["C2"],"nus",w=1.9); C.bond(h["C2"],h["C3"],"nus"); C.bond(h["C3"],h["C4"],"nus"); C.bond(h["C6"],h["C5"],"els")
C.bond(h["C1"],h["C6"],"goods",dash="5,5"); C.bond(h["C4"],h["C5"],"goods",dash="5,5")
C.raw(f'<circle class="inks" cx="{c1[0]}" cy="{c1[1]}" r="{L*0.55:.1f}" stroke-width="1.5" stroke-dasharray="4,4"/>')
C.text(c1[0]+66,c1[1]-58,"‡",size=22)
C.text(c1[0],c1[1]+92,"cyclic TS, 6 e⁻",size=13,cls="mutedt")
C.text(c1[0],c1[1]+110,"(“aromatic” 4n+2)",size=12,cls="mutedt")
C.rarrow((530,215),(600,215))
# product
c2=(700,215); h=hexpts(c2)
C.bond(h["C1"],h["C2"],"inks"); C.bond(h["C2"],h["C3"],"goods",2,inner=c2); C.bond(h["C3"],h["C4"],"inks"); C.bond(h["C5"],h["C6"],"inks")
C.bond(h["C1"],h["C6"],"goods",w=3); C.bond(h["C4"],h["C5"],"goods",w=3)
C.text(c2[0],c2[1]+92,"cyclohexene",size=13)
# legend / bullets
x0=815
for i,(t,cls) in enumerate([("2 new σ bonds (C1–C6, C4–C5)","good"),("new π bond (C2=C3)","good"),("3 π bonds → 1 π + 2 σ","ink"),("[π4s + π2s]: thermally allowed","ink"),("no intermediate → stereospecific","ink")]):
    C.text(x0-20,150+i*26,"•",size=14,cls=cls,anchor="start"); C.text(x0-8,150+i*26,t,size=12,cls=cls,anchor="start")
C.text(24,400,"Sources: CM3121 L13 p.10 (mechanism), p.19 (stereospecificity), p.33–35 (Woodward–Hoffmann).",size=11.5,cls="mutedt",anchor="start")
C.raw('<g class="coloronly">'); C.text(24,418,"Orange: electron flow; blue: diene; red: dienophile; green: bonds formed.",size=11.5,cls="mutedt",anchor="start"); C.raw('</g>')
C.raw('<g class="monoonly">'); C.text(24,418,"Curved arrows: electron flow; bold bonds: new σ bonds; dashed: partial bonds in the TS.",size=11.5,cls="mutedt",anchor="start"); C.raw('</g>')
save(C,"DA_mechanism")
