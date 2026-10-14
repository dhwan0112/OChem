#!/usr/bin/env python3
"""시각화 보강 2D 그림의 chemfig 스펙(JSON) 생성기: FMO 로브, con/dis 로브, anti 첨가 입체화학.
사용법: python3 tools/gen_visual_boost_2d.py && RESHIKI=... python3 tools/chemfig.py figures/L13/da_fmo_lobes.json ..."""
import json
def dump(p,d): json.dump(d,open(p,"w"),ensure_ascii=False,indent=1); print(p)

# ---- DA FMO
at=[];bd=[];sh=[];cap=[]
xs=[0,1.4,2.8,4.2]
for x in xs: at.append(["C",x,0,0,0])
for i in range(3): bd.append([i,i+1,1])
for x,s,c in zip(xs,[1,1,-1,-1],[1.0,0.72,0.72,1.0]): sh.append({"lobe":[x,0,1.5*c,0,s]})
at.append(["C",0,4.4,0,0]); at.append(["C",4.2,4.4,0,0])
bd.append([4,5,1])
for x,s in [(0,-1),(4.2,1)]: sh.append({"lobe":[x,4.4,1.5,0,s]})
for x in (0,4.2): sh.append({"line":[x,1.3,x,3.1,"good","dash"]})
cap=[["diene HOMO (ψ2)",5.0,-0.25],["dienophile LUMO (π*)",5.0,4.15],
     ["phases match at both ends",0.45,1.55,"good"],["→ suprafacial, allowed",0.45,2.3,"good"],
     ["filled lobe = + phase, open = − phase; end lobes are larger",-0.3,5.9,"muted"]]
dump("figures/L13/da_fmo_lobes.json",{"title":"Diels–Alder FMO: diene HOMO ψ2와 dienophile LUMO π*의 말단 위상 일치 (L13 p.)","atoms":at,"bonds":bd,"captions":cap,"shapes":sh})

# ---- con/dis
at=[];bd=[];sh=[];cap=[];cur=[]
def row(y,n,signs,mode,label):
    global at,bd
    b=len(at); xs=[i*1.3 for i in range(n)]
    for x in xs: at.append(["C",x,y,0,0])
    for i in range(n-1): bd.append([b+i,b+i+1,1])
    for i,(x,s) in enumerate(zip(xs,signs)):
        sh.append({"lobe":[x,y,1.4,0,s,"nu",1.0 if i in (0,n-1) else 0.35]})
    cap.append([label,-0.3,y-1.9])
    # 오른쪽: U자로 굽힌 사슬, 말단 둘이 위에서 만난다
    L=1.3*n+1.4; W=2.0
    if n==4: pts=[(L,y),(L-0.3,y+1.2),(L+W+0.3,y+1.2),(L+W,y)]
    else:    pts=[(L,y),(L-0.6,y+0.85),(L,y+1.7),(L+W,y+1.7),(L+W+0.6,y+0.85),(L+W,y)]
    b=len(at)
    for (x,yy) in pts: at.append(["C",x,yy,0,0])
    for i in range(len(pts)-1): bd.append([b+i,b+i+1,1])
    R=L+W
    sh.append({"lobe":[L,y,1.4,35,signs[0]]})
    sh.append({"lobe":[R,y,1.4,145 if mode=="conrotatory" else -35,signs[-1]]})
    sh.append({"line":[L+0.6,y-0.8,R-0.6,y-0.8,"good","dash"]})
    cur.append({"from":{"pt":[L-0.8,y+0.35]},"to":{"pt":[L-0.8,y-0.65]},"bend":0.6})
    if mode=="conrotatory": cur.append({"from":{"pt":[R+0.8,y-0.65]},"to":{"pt":[R+0.8,y+0.35]},"bend":0.6})
    else: cur.append({"from":{"pt":[R+0.8,y+0.35]},"to":{"pt":[R+0.8,y-0.65]},"bend":-0.6})
    cap.append([mode,L-0.2,y+(1.4 if n==4 else 2.1),"good"])
row(0,4,[1,1,-1,-1],"conrotatory","4π: butadiene HOMO ψ2 (thermal)")
row(5.0,6,[1,1,-1,-1,1,1],"disrotatory","6π: hexatriene HOMO ψ3 (thermal)")
cap.append(["the ends turn so that lobes of the SAME phase meet (new σ bond, green)",-0.3,8.2,"muted"])
dump("figures/L17/con_dis_homo_lobes.json",{"title":"열적 4π conrotatory / 6π disrotatory: HOMO 말단 로브 위상 (L17 p.)","atoms":at,"bonds":bd,"captions":cap,"shapes":sh,"curved":cur})

# ---- anti addition stereo
at=[];bd=[];cap=[];arr=[]
def alkene(x0,y0,E):
    global at,bd
    b=len(at)
    at += [["C",x0,y0,0,0],["C",x0+1,y0,0,0],
           ["C",x0-0.5,y0-0.87,0,3],["H",x0-0.5,y0+0.87,0,0],
           ["C",x0+1.5,y0+0.87 if E else y0-0.87,0,3],["H",x0+1.5,y0-0.87 if E else y0+0.87,0,0]]
    bd += [[b,b+1,2],[b,b+2,1],[b,b+3,1],[b+1,b+4,1],[b+1,b+5,1]]
def zig(x0,y0,br2,br3):
    """C1–C4 zigzag; C2 위로 Br/H, C3 아래로 Br/H. br2/br3: 'wedge'|'hash' (Br 표시)"""
    global at,bd
    b=len(at); o={"wedge":"hash","hash":"wedge"}
    at += [["C",x0,y0+0.5,0,3],["C",x0+0.87,y0,0,0],["C",x0+1.73,y0+0.5,0,0],["C",x0+2.6,y0,0,3],
           ["Br",x0+0.4,y0-0.95,0,0],["H",x0+1.35,y0-0.95,0,0],["Br",x0+1.25,y0+1.45,0,0],["H",x0+2.2,y0+1.45,0,0]]
    bd += [[b,b+1,1],[b+1,b+2,1],[b+2,b+3,1],[b+1,b+4,1,br2],[b+1,b+5,1,o[br2]],[b+2,b+6,1,br3],[b+2,b+7,1,o[br3]]]
alkene(0.5,0,True); arr.append([3.0,0,4.8,0]); cap.append(["Br₂ (anti)",3.1,-1.0,"muted"])
zig(5.7,-0.2,"wedge","hash"); cap += [["meso",6.5,1.9,"good"],["(E)-2-butene",0.15,1.35,"muted"]]
y=4.2
alkene(0.5,y,False); arr.append([3.0,y,4.8,y]); cap.append(["Br₂ (anti)",3.1,y-1.0,"muted"])
zig(5.7,y-0.2,"wedge","wedge"); cap.append(["+",9.6,y-0.15,"ink",10]); zig(10.9,y-0.2,"hash","hash")
cap += [["racemic (1 : 1 enantiomers)",8.0,y+1.9,"good"],["(Z)-2-butene",0.15,y+1.35,"muted"]]
def nbx(i):
    for b in bd:
        if i in b[:2]: return at[b[0] if b[1]==i else b[1]][1]
ab=[["H3C" if a[1]<nbx(i) else "CH3",i,[i]] for i,a in enumerate(at) if a[0]=="C" and len(a)>4 and a[4]==3]
for a in at:
    if len(a)>4: a[4]=0
dump("figures/L02/anti_addition_stereo.json",{"abbrev":ab,"title":"anti 첨가의 입체특이성: E-2-butene → meso, Z-2-butene → racemic (L2 p.)","atoms":at,"bonds":bd,"captions":cap,"arrows":arr})
