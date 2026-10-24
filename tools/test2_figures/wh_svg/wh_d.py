from orb import *
C=Canvas(1120,560)
C.text(24,30,"Why ketene can do π2s + π2a but a plain alkene cannot",size=20,anchor="start",weight="bold")
C.text(24,56,"Top view: alkene 1 (HOMO, blue) lies flat; its p orbitals point at you (+ lobes on top). Partner (LUMO, red) sits above it, crossed at 90°.",size=13,cls="mutedt",anchor="start")
def panel(cx,cy,ketene,title,sub):
    C.text(cx,96,title,size=15,weight="bold"); C.text(cx,116,sub,size=12,cls="mutedt")
    d=62
    L_,R_=(cx-d,cy),(cx+d,cy)
    C.line(L_,R_,"nus",3)
    for p in (L_,R_): C.raw(f'<circle class="nu" cx="{p[0]}" cy="{p[1]}" r="24" fill-opacity="0.8" stroke-width="1.6"/>'); C.text(p[0],p[1],"+",size=16,cls="bg",weight="bold")
    A,B=(cx,cy-d),(cx,cy+d)
    C.line(A,B,"els",3)
    def hl(p,side,filled):
        x=p[0]+side*30
        if filled: C.raw(f'<ellipse class="el" cx="{x}" cy="{p[1]}" rx="27" ry="11" fill-opacity="0.85" stroke-width="1.5"/>')
        else: C.raw(f'<ellipse class="els" cx="{x}" cy="{p[1]}" rx="27" ry="11" stroke-width="1.5"/>')
    hl(A,+1,True); hl(A,-1,False); hl(B,+1,False); hl(B,-1,True)
    for p in (A,B): C.raw(f'<circle class="ink" cx="{p[0]}" cy="{p[1]}" r="3.5"/>')
    # corner interactions
    def corner(p1,p2,ok):
        m=mid(p1,p2)
        if ok: C.line(p1,p2,"goods",2.6,"5,4")
        else: C.line(p1,p2,"els",2.6,"2,5"); C.text(m[0]+(10 if m[0]>cx else -10),m[1]+(-10 if m[1]<cy else 10),"×",size=18,cls="el")
    corner((A[0]+52,A[1]+8),(R_[0]-6,R_[1]-22),True)
    corner((A[0]-52,A[1]+8),(L_[0]+6,L_[1]-22),False)
    corner((B[0]+52,B[1]-8),(R_[0]-6,R_[1]+22),False)
    corner((B[0]-52,B[1]-8),(L_[0]+6,L_[1]+22),True)
    C.text(A[0],A[1]-30,"C(central)" if ketene else "C",size=12,cls="el",weight="bold")
    C.text(B[0],B[1]+32,"CR₂" if ketene else "C",size=12,cls="el",weight="bold")
    if ketene:
        C.raw(f'<circle class="good" cx="{A[0]}" cy="{A[1]}" r="17" fill-opacity="0.35" stroke-width="2"/>')
        C.text(A[0],A[1]-52,"=O  (C=O π* points down at alkene 1)",size=11.5,cls="mutedt")
        C.line((A[0]-14,A[1]+10),(L_[0]+18,L_[1]-14),"goods",2.6,"5,4"); C.line((A[0]+14,A[1]+10),(R_[0]-18,R_[1]-14),"goods",2.6,"5,4")
    return
panel(200,300,False,"(b) alkene + alkene, crossed","2 bonding vs 2 antibonding → no net gain")
panel(560,300,True,"(c) ketene + alkene, crossed","extra p orbital on the central C: 4 bonding vs 2 antibonding")
x0=790
lines=[("Why (b) fails","el",True),("• crossed approach: bonding at 2 corners,","ink",False),("  antibonding at the other 2","ink",False),("• poor overlap, substituents clash","ink",False),("• supra/supra is S+A → forbidden","ink",False),("",None,False),("Why (c) works","good",True),("• central C is sp: a second π (C=O)","ink",False),("  at 90° to the C=C","ink",False),("• that p orbital bonds to BOTH alkene","ink",False),("  carbons → net bonding","ink",False),("• low-lying LUMO (electrophilic C=O)","ink",False),("• central C carries no substituents","ink",False),("  → crossed approach is not blocked","ink",False)]
for i,(t,cls,b) in enumerate(lines):
    if t: C.text(x0,150+i*22,t,size=12.5 if not b else 14,cls=cls if cls!="ink" else "ink",anchor="start",weight="bold" if b else "normal")
C.raw('<g class="coloronly">'); C.text(24,505,"Green dashed: in-phase (bonding) overlap; red dotted ×: out-of-phase (antibonding). Green circle: ketene C=O π* lobe facing alkene 1.",size=12,cls="mutedt",anchor="start"); C.raw('</g>')
C.raw('<g class="monoonly">'); C.text(24,505,"Dashed: in-phase (bonding) overlap; dotted ×: out-of-phase (antibonding). Shaded circle: ketene C=O π* lobe facing alkene 1.",size=12,cls="mutedt",anchor="start"); C.raw('</g>')
C.text(24,530,"Sources: CM3121 L15 p.6–8 (cumulated double bonds; thermal [2+2]); Clayden 2e p.898–899 (crossed approach, extra p orbital).",size=11.5,cls="mutedt",anchor="start")
save(C,"WH4_ketene_crossed")
