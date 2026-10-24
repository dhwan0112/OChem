from common import *
C=Canvas(1080,565)
C.text(24,30,"Frontier orbitals decide whether a cycloaddition is allowed",size=20,anchor="start",weight="bold")
C.text(24,56,"Both new σ bonds must form from in-phase overlap of the HOMO of one component and the LUMO of the other (suprafacial on both).",size=13,cls="mutedt",anchor="start")
SP=48
def porb(x,y,c,cls):
    ry=10+26*abs(c); rx=9+5*abs(c)
    top_fill = c>0
    for dy,filled in ((-ry,top_fill),(ry,not top_fill)):
        if filled: C.raw(f'<ellipse class="{cls}" cx="{x:.1f}" cy="{y+dy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill-opacity="0.85" stroke-width="1.6"/>')
        else: C.raw(f'<ellipse class="{cls}s" cx="{x:.1f}" cy="{y+dy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" stroke-width="1.6"/>')
    C.raw(f'<circle class="ink" cx="{x:.1f}" cy="{y:.1f}" r="2.6"/>')
    return ry
def mo(xs,y,cs,cls,label,lab_cls):
    C.line((xs[0],y),(xs[-1],y),"inks",1.4)
    rys=[porb(x,y,c,cls) for x,c in zip(xs,cs)]
    C.text((xs[0]+xs[-1])/2,y-86 if y<300 else y+86,label,size=12.5,cls=lab_cls)
    return rys
def link(p,q,ok):
    if ok: C.line(p,q,"goods",2.2,"5,4")
    else:
        C.line(p,q,"els",2.2,"2,5"); m=mid(p,q); C.text(m[0]+12,m[1],"×",size=20,cls="el")
def panel(x0,title,sub,top,bot,verdict,ok_all,vcls):
    C.text(x0+150,100,title,size=15,weight="bold"); C.text(x0+150,120,sub,size=12,cls="mutedt")
    yT,yB=240,390
    xsT=[x0+150-SP*(len(top[0])-1)/2+SP*i for i in range(len(top[0]))]
    ryT=mo(xsT,yT,top[0],top[1],top[2],top[3])
    xsB=[xsT[0],xsT[-1]] if len(top[0])==4 else xsT
    ryB=mo(xsB,yB,bot[0],bot[1],bot[2],bot[3])
    # ends: bottom lobe of top vs top lobe of bottom
    for (xt,ct,rt),(xb,cb,rb) in [((xsT[0],top[0][0],ryT[0]),(xsB[0],bot[0][0],ryB[0])),((xsT[-1],top[0][-1],ryT[-1]),(xsB[-1],bot[0][-1],ryB[-1]))]:
        top_bottom_lobe_pos = not (ct>0); bot_top_lobe_pos = cb>0
        link((xt,yT+2*rt+2),(xb,yB-2*rb-2),top_bottom_lobe_pos==bot_top_lobe_pos)
    C.text(x0+150,505,verdict,size=14,cls=vcls,weight="bold")
psi2=[0.60,0.37,-0.37,-0.60]; pi=[0.71,0.71]; pistar=[0.71,-0.71]; pistar_b=[-0.71,0.71]
panel(30,"thermal [4+2] (Diels–Alder)","6 electrons",(psi2,"nu","diene HOMO (ψ2)","nu"),(pistar_b,"el","dienophile LUMO (π*)","el"),"both ends in phase → allowed",True,"good")
panel(390,"thermal [2+2]","4 electrons",(pi,"nu","alkene HOMO (π)","nu"),(pistar_b,"el","alkene LUMO (π*)","el"),"one end out of phase → forbidden",False,"el")
panel(750,"photochemical [2+2]","hν promotes one electron: π → π*",(pistar,"nu","excited alkene: HOMO = π*","nu"),(pistar_b,"el","ground-state LUMO (π*)","el"),"both ends in phase → allowed",True,"good")
# legend
ly=540
C.raw(f'<ellipse class="ink" cx="40" cy="{ly}" rx="7" ry="11" fill-opacity="0.85"/>'); C.text(54,ly,"+ phase",size=12,anchor="start")
C.raw(f'<ellipse class="inks" cx="130" cy="{ly}" rx="7" ry="11" stroke-width="1.6"/>'); C.text(144,ly,"− phase",size=12,anchor="start")
C.line((220,ly),(255,ly),"goods",2.2,"5,4"); C.text(262,ly,"bonding overlap",size=12,anchor="start")
C.line((400,ly),(435,ly),"els",2.2,"2,5"); C.text(442,ly,"antibonding (no bond)",size=12,anchor="start")
C.text(1056,ly,"Sources: CM3121 L13 p.27–30, 33–35; L14 p.24–26. Lobe size ∝ coefficient.",size=11.5,cls="mutedt",anchor="end")
save(C,"FMO_cycloaddition")
