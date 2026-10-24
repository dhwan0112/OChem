from orb import *
C=Canvas(1080,880)
C.text(24,30,"Step 3. Read S/A at the ends → supra or antara",size=20,anchor="start",weight="bold")
C.text(24,56,"Match the HOMO of one partner with the LUMO of the other (an MO's overall sign is arbitrary, so the first end can always be made to match).",size=12.5,cls="mutedt",anchor="start"); C.text(24,75,"Same symmetry (S+S or A+A) → the second end matches too: suprafacial. Mixed (S+A) → the second end must be reached from the other face: antarafacial.",size=12.5,cls="mutedt",anchor="start")
SC=0.55
def lobe_tip(x,y,c,up):  # returns tip point and sign of that lobe
    ry=(9+26*abs(c))*SC; sgn=(1 if c>0 else -1)*(1 if up else -1)
    return ((x,y-2*ry-2) if up else (x,y+2*ry+2)), sgn
def title(x0,y,t,sub): C.text(x0+170,y,t,size=14.5,weight="bold"); C.text(x0+170,y+19,sub,size=12,cls="mutedt")
def verdict(x0,y,t1,t2,ok):
    C.text(x0+170,y,t1,size=13,weight="bold",cls="good" if ok else "el"); C.text(x0+170,y+19,t2,size=12,cls="mutedt")
def cyclo(x0,Y,nT,jT,nB,jB,title_,sub,v1,v2,ok,antara_fix=False):
    title(x0,Y,title_,sub)
    sp=44; csT=huckel(nT,jT); csB=huckel(nB,jB)
    if (-1 if csT[0]>0 else 1)!=(1 if csB[0]>0 else -1): csB=[-c for c in csB]  # overall phase is arbitrary: fix left end
    xsT=[x0+170-sp*(nT-1)/2+i*sp for i in range(nT)]; yT=Y+105; yB=Y+225
    chain(C,xsT[0],yT,csT,"nu",sp=sp,scale=SC)
    xsB=[xsT[0],xsT[-1]]; C.line((xsB[0],yB),(xsB[1],yB),"inks",1.3)
    porb(C,xsB[0],yB,csB[0],"el",SC); porb(C,xsB[1],yB,csB[-1],"el",SC)
    C.text(xsT[-1]+26,yT,f"HOMO ψ{jT} ({'S' if csT[0]*csT[-1]>0 else 'A'})",size=12,cls="nu",anchor="start",weight="bold")
    C.text(xsB[-1]+26,yB,f"LUMO ({'S' if csB[0]*csB[-1]>0 else 'A'})",size=12,cls="el",anchor="start",weight="bold")
    for i,(xt,ct,xb,cb) in enumerate([(xsT[0],csT[0],xsB[0],csB[0]),(xsT[-1],csT[-1],xsB[1],csB[-1])]):
        pT,sT=lobe_tip(xt,yT,ct,False); pB,sB=lobe_tip(xb,yB,cb,True)
        if sT==sB: link(C,pT,pB,True)
        elif antara_fix and i==1:
            pB2,_=lobe_tip(xb,yB,cb,False)
            C.raw(f'<path class="goods" d="M{pT[0]:.1f},{pT[1]:.1f} Q{xb+75:.1f},{yB-5:.1f} {pB2[0]+4:.1f},{pB2[1]:.1f}" stroke-width="2.4" stroke-dasharray="5,4"/>')
        else: link(C,pT,pB,False)
    verdict(x0,Y+300,v1,v2,ok)
def hshift(x0,Y,n,j,title_,sub,v1,v2,ok,label):
    title(x0,Y,title_,sub)
    sp=36 if n>2 else 46; cs=huckel(n,j)
    yc=Y+185; xs=[x0+175-sp*(n-1)/2+i*sp for i in range(n)]
    chain(C,xs[0],yc,cs,"el",sp=sp,scale=SC)
    xm=xs[0]-sp  # migrating-from carbon
    C.line((xm,yc),(xs[0],yc),"inks",1.3)
    C.raw(f'<ellipse class="nu" cx="{xm}" cy="{yc-17}" rx="7" ry="15" fill-opacity="0.85" stroke-width="1.5"/>'); C.raw(f'<circle class="ink" cx="{xm}" cy="{yc}" r="2.6"/>')
    hx,hy=(xm+xs[-1])/2,yc-105
    C.raw(f'<circle class="nu" cx="{hx}" cy="{hy}" r="11" fill-opacity="0.85" stroke-width="1.5"/>'); C.text(hx,hy,"H",size=11,cls="bg")
    C.line((xm,yc-34),(hx-9,hy+7),"muted",2,"2,4")
    C.text(hx+16,hy-16,"σ C–H (HOMO, +/+)",size=12,cls="nu",anchor="start",weight="bold")
    # near end: C sp3 lobe (+) with near-end top lobe (+ always)
    pN,_=lobe_tip(xs[0],yc,cs[0],True); link(C,(xm+5,yc-30),pN,True)
    far_up_sign=1 if cs[-1]>0 else -1
    if far_up_sign>0: pF,_=lobe_tip(xs[-1],yc,cs[-1],True); link(C,(hx+10,hy+6),pF,True)
    else:
        pF,_=lobe_tip(xs[-1],yc,cs[-1],False)
        C.raw(f'<path class="goods" d="M{hx+10:.1f},{hy+6:.1f} Q{xs[-1]+105:.1f},{yc-50:.1f} {pF[0]+4:.1f},{pF[1]:.1f}" stroke-width="2.4" stroke-dasharray="5,4"/>')
    C.text((xs[0]+xs[-1])/2,yc+52,label,size=12,cls="el",weight="bold")
    verdict(x0,Y+300,v1,v2,ok)
Y1,Y2=105,505
cyclo(10,Y1,4,2,2,2,"(a) Diels–Alder [4+2]","L13 p.27; L14 p.6","A + A → both ends match","suprafacial/suprafacial: allowed",True)
cyclo(365,Y1,2,1,2,2,"(b) [2+2] alkene + alkene","L14 p.24–25","S + A → one end mismatches","supra/supra forbidden (thermal)",False)
cyclo(720,Y1,2,1,2,2,"(c) ketene [2+2]: π2s + π2a","L15 p.6–8","S + A, reached antarafacially","→ both ends match: allowed",True,antara_fix=True)
hshift(10,Y2,4,3,"(d) thermal [1,5]-H shift","L16 p.21–22","S + S → H stays on top","suprafacial: easy",True,"diene LUMO ψ3 (S)")
hshift(365,Y2,6,4,"(e) thermal [1,7]-H shift","L16 p.23","S + A → H must cross to the bottom","antarafacial: possible (long chain)",True,"triene LUMO ψ4 (A)")
hshift(720,Y2,2,2,"(f) thermal [1,3]-H shift","L16 p.24","S + A → antarafacial needed","3 atoms too short → does not occur",False,"alkene LUMO π* (A)")
C.text(24,856,"hν: an electron is promoted, so the frontier orbital changes symmetry and the answer flips",size=11.5,cls="mutedt",anchor="start")
C.text(24,871,"(photochemical [1,7]-H is suprafacial; photochemical [2+2] is allowed) — L14 p.26; L16 p.25.",size=11.5,cls="mutedt",anchor="start")
save(C,"WH3_SA_matching")
