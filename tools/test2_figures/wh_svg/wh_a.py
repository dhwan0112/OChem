from orb import *
C=Canvas(1080,505)
C.text(24,30,"Step 1. Phase, not direction: why lobes must match",size=20,anchor="start",weight="bold")
C.text(24,56,"Filled lobe = + phase, open lobe = − phase. A new bond forms only where two lobes of the SAME phase overlap.",size=13,cls="mutedt",anchor="start")
# panel A: one p orbital
x=90; y=210
porb(C,x,y,0.71,"nu"); C.text(x+30,y-38,"+",size=18,anchor="start",weight="bold"); C.text(x+30,y+38,"−",size=18,anchor="start",weight="bold")
C.text(x,y+95,"one p orbital:",size=13,weight="bold"); C.text(x,y+114,"top and bottom lobes",size=12.5,cls="mutedt"); C.text(x,y+131,"have opposite signs",size=12.5,cls="mutedt")
# panel B: overlap in phase / out of phase
x0=260
C.text(x0+70,100,"same phase → bonding",size=14,cls="good",weight="bold")
porb(C,x0+40,y,0.71,"nu"); porb(C,x0+100,y,0.71,"el")
C.raw(f'<path class="goods" d="M{x0+48},{y-50} Q{x0+70},{y-72} {x0+92},{y-50}" stroke-width="2.4" stroke-dasharray="5,4"/>')
C.text(x0+70,y+95,"top meets top:",size=13,weight="bold"); C.text(x0+70,y+114,"+ with + → bond",size=12.5,cls="mutedt")
x1=470
C.text(x1+70,100,"opposite phase → node",size=14,cls="el",weight="bold")
porb(C,x1+40,y,0.71,"nu"); porb(C,x1+100,y,-0.71,"el")
C.raw(f'<path class="els" d="M{x1+48},{y-50} Q{x1+70},{y-72} {x1+92},{y-50}" stroke-width="2.4" stroke-dasharray="2,5"/>'); C.text(x1+70,y-80,"×",size=20,cls="el")
C.text(x1+70,y+95,"top meets top:",size=13,weight="bold"); C.text(x1+70,y+114,"+ with − → no bond",size=12.5,cls="mutedt")
# panel C: supra vs antara on the same pi*
x2=700
C.text(x2+175,100,"the same π* used two ways",size=14,weight="bold")
# reference component (HOMO of partner, both ends + on bottom) drawn below
def comp_pair(xc,antara,title):
    xs=[xc-30,xc+30]; yt=y-25; yb=y+95
    porb(C,xs[0],yt,0.71,"nu"); porb(C,xs[1],yt,0.71,"nu"); C.line((xs[0],yt),(xs[1],yt),"inks",1.3)
    porb(C,xs[0],yb,-0.71,"el"); porb(C,xs[1],yb,0.71,"el"); C.line((xs[0],yb),(xs[1],yb),"inks",1.3)
    # left end: bottom lobe of top comp (−) with top lobe of bottom comp (−) => in phase
    link(C,(xs[0],yt+37),(xs[0],yb-37),True)
    if not antara:
        link(C,(xs[1],yt+37),(xs[1],yb-37),False)
    else:
        C.raw(f'<path class="goods" d="M{xs[1]},{yt+37} Q{xs[1]+80},{yb-10} {xs[1]+8},{yb+64}" stroke-width="2.4" stroke-dasharray="5,4"/>')
    C.text(xc,yb+92,title,size=12.5,weight="bold",cls="good" if antara else "el")
comp_pair(x2+75,False,"suprafacial: mismatch")
comp_pair(x2+265,True,"antarafacial: match")
C.text(x2+175,y+218,"antarafacial = reach the far lobe at one end",size=12,cls="mutedt")
C.text(x2+175,y+235,"= flip the sign at that end",size=12,cls="mutedt")
C.text(24,482,"Top: alkene HOMO (π). Bottom: alkene LUMO (π*). Sources: CM3121 L13 p.27–29; L14 p.5, 24–25; Clayden 2e p.886, 898–899.",size=11.5,cls="mutedt",anchor="start")
save(C,"WH1_phase_basics")
