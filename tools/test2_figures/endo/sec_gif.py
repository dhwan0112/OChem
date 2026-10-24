import numpy as np, math
from PIL import Image, ImageDraw, ImageFont
from scipy.spatial import ConvexHull
W,H=720,560; SS=2
FB=lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",s)
FR=lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",s)
def unit(v): v=np.asarray(v,float); return v/np.linalg.norm(v)
Y=np.array([0,1.,0]); X=np.array([1.,0,0])
GREEN=(21,128,61); ORANGE=(234,88,12); CB=(29,78,216); CR=(185,28,28); GR=(70,70,78); OX=(220,38,38)
def ease(t): t=min(max(t,0),1); return t*t*(3-2*t)
HD=2.5
def pent(a,r=1.2,y=HD): a=math.radians(a); return np.array([r*math.cos(a),y,r*math.sin(a)])
DIENE={'d1':pent(198),'d2':pent(126),'d3':pent(54),'d4':pent(342),'d5':pent(270)}  # d5 = CH2 (front)
cD={'d1':0.60,'d2':0.37,'d3':-0.37,'d4':-0.60}
# maleic anhydride (endo): ring extends to the back (+z), under d2=d3
MA0={'a3':np.array([-0.70,0,-0.30]),'a4':np.array([0.70,0,-0.30]),'a2':np.array([-1.13,0,1.03]),'a5':np.array([1.13,0,1.03]),'Or':np.array([0,0,1.85])}
MA0['O2']=MA0['a2']+unit(np.array([-0.95,0,0.3]))*1.2; MA0['O5']=MA0['a5']+unit(np.array([0.95,0,0.3]))*1.2
cM={'a3':-0.42,'a4':0.42,'a2':-0.25,'a5':0.25}
def rotx(p,ang,cen):
    p=p-cen; c,s=math.cos(ang),math.sin(ang); return cen+np.array([p[0],p[1]*c-p[2]*s,p[1]*s+p[2]*c])
def lobe_len(c): return 0.42+0.75*abs(c)
def build(st):
    flip=ease(st.get('flip',0)); cen=(MA0['a3']+MA0['a4'])/2
    M={k:rotx(v,math.pi*flip,cen) for k,v in MA0.items()}
    atoms=[];bonds=[];lobes=[];prim=[];sec=[]
    for k,p in DIENE.items(): atoms.append((k,p,0.28,GR,'CH₂' if k=='d5' else None))
    for k,p in M.items(): atoms.append((k,p,0.28 if k.startswith('a') else 0.30,OX if k.startswith('O') else GR,'O' if k.startswith('O') else None))
    g=(60,60,66)
    bonds+=[(DIENE['d1'],DIENE['d2'],2,g),(DIENE['d2'],DIENE['d3'],'dev',g),(DIENE['d3'],DIENE['d4'],2,g),(DIENE['d4'],DIENE['d5'],1,g),(DIENE['d5'],DIENE['d1'],1,g)]
    bonds+=[(M['a3'],M['a4'],2,g),(M['a3'],M['a2'],1,g),(M['a4'],M['a5'],1,g),(M['a2'],M['Or'],1,g),(M['a5'],M['Or'],1,g),(M['a2'],M['O2'],2,g),(M['a5'],M['O5'],2,g)]
    oa=st.get('orb',1)
    flipping=0.03<flip<0.97
    for k in ('d1','d2','d3','d4'): lobes.append((DIENE[k],cD[k],CB,oa))
    if not flipping:
        for k in ('a3','a4','a2','a5'): lobes.append((M[k],cM[k],CR,oa))
        prim=[('d1','a3'),('d4','a4')]
        if flip<0.03: sec=[('d2','a2'),('d3','a5')]
    return atoms,bonds,lobes,prim,sec,M
def mkproj(az,el,scale,focus):
    def proj(p):
        p=p-focus
        ca,sa=math.cos(az),math.sin(az); x=p[0]*ca+p[2]*sa; z=-p[0]*sa+p[2]*ca
        ce,se=math.cos(el),math.sin(el); y=p[1]*ce+z*se; z2=-p[1]*se+z*ce
        f=13/(13+z2); return np.array([(W/2+x*scale*f)*SS,(H*0.52-y*scale*f)*SS]),z2,f
    return proj
def lobe_poly(P,nv,c,proj):
    L=lobe_len(c); w=0.16+0.18*abs(c)
    a=unit(np.cross(nv,X)); b=np.cross(nv,a); pts=[]
    for i in range(9):
        tt=i/8*math.pi
        for j in range(12):
            pp=j/12*2*math.pi
            q=P+nv*(L*(1-math.cos(tt))/2)+(a*math.cos(pp)+b*math.sin(pp))*w*math.sin(tt)
            pts.append(proj(q)[0])
    pts=np.array(pts); hull=ConvexHull(pts); return [tuple(pts[v]) for v in hull.vertices]
def render(st,az,el,cap,sub,scale=70,focus=np.array([0,1.25,0.2]),glow=0.0,secal=1.0,tags=None,tally=None):
    proj=mkproj(az,el,scale,focus)
    atoms,bonds,lobes,prim,sec,M=build(st)
    P={**DIENE,**M}
    img=Image.new("RGB",(W*SS,H*SS),(255,255,255)); d=ImageDraw.Draw(img,"RGBA")
    prims=[]
    for (p,q,o,col) in bonds:
        (a,za,_),(b,zb,_)=proj(p),proj(q); prims.append(((za+zb)/2+0.02,'b',(a,b,o,col)))
    for (nm,p,r,col,lab) in atoms:
        a,z,f=proj(p); prims.append((z,'a',(a,r*scale*f*SS,col,lab)))
    for (Pp,c,col,al) in lobes:
        for sgn in (1,-1):
            nv=Y*sgn; filled=(c*sgn)>0
            prims.append((proj(Pp+nv*0.45)[1],'l',(lobe_poly(Pp,nv,c,proj),filled,col,al)))
    for pr in sorted(prims,key=lambda x:-x[0]):
        k=pr[1]
        if k=='b':
            a,b,o,col=pr[2]; dx,dy=b-a; L=math.hypot(dx,dy)+1e-9; nx,ny=-dy/L,dx/L
            if o=='dev':
                d.line([tuple(a),tuple(b)],fill=col,width=int(5*SS))
                for i in range(0,10,2):
                    p=a+(b-a)*i/10+np.array([nx,ny])*5*SS; q=a+(b-a)*(i+1)/10+np.array([nx,ny])*5*SS
                    d.line([tuple(p),tuple(q)],fill=CB,width=int(3*SS))
                continue
            for oo in ([0] if o==1 else [-1,1]):
                d.line([(a[0]+nx*oo*4*SS,a[1]+ny*oo*4*SS),(b[0]+nx*oo*4*SS,b[1]+ny*oo*4*SS)],fill=col,width=int((5 if o==1 else 3.5)*SS))
        elif k=='a':
            a,r,col,lab=pr[2]
            for i in range(6,0,-1):
                rr=r*i/6; kk=0.75+0.45*(1-i/6); off=(1-i/6)*r*0.35
                d.ellipse([a[0]-rr-off,a[1]-rr-off,a[0]+rr-off,a[1]+rr-off],fill=tuple(int(min(255,c*kk)) for c in col))
            if lab=='O': d.text((a[0],a[1]),lab,font=FB(int(r/SS*0.9)),fill=(255,255,255),anchor="mm")
        else:
            poly,filled,col,al=pr[2]
            if filled: d.polygon(poly,fill=col+(int(185*al),),outline=col+(int(255*al),))
            else:
                d.polygon(poly,fill=(255,255,255,int(140*al)),outline=col+(int(255*al),)); d.line(poly+[poly[0]],fill=col+(int(255*al),),width=int(2.2*SS))
    def tips(a,b):
        ta=P[a]-Y*lobe_len(cD[a])*0.9; tb=P[b]+Y*lobe_len(cM[b])*0.9
        return proj(ta)[0],proj(tb)[0]
    for a,b in prim:
        A2,B2=tips(a,b)
        for i in range(0,14,2):
            p=A2+(B2-A2)*i/14; q=A2+(B2-A2)*(i+1)/14; d.line([tuple(p),tuple(q)],fill=GREEN+(230,),width=int(3.4*SS))
    for a,b in (sec if secal>0.02 else []):
        A2,B2=tips(a,b); m=(A2+B2)/2; L=np.linalg.norm(B2-A2)
        if glow>0:
            for rr,al in ((1.0,40),(0.75,60),(0.5,90)):
                R=(L*0.55*rr+10*SS)*(0.9+0.25*glow); d.ellipse([m[0]-R*0.6,m[1]-R,m[0]+R*0.6,m[1]+R],fill=ORANGE+(int(al*secal*glow),))
        for i in range(0,14,2):
            p=A2+(B2-A2)*i/14; q=A2+(B2-A2)*(i+1)/14; d.line([tuple(p),tuple(q)],fill=ORANGE+(int(255*secal),),width=int(4.2*SS))
    img=img.resize((W,H),Image.LANCZOS); d=ImageDraw.Draw(img)
    if tags:
        for key,txt,col,dx,dy in tags:
            q=proj(P[key])[0]/SS; d.text((q[0]+dx,q[1]+dy),txt,font=FB(14),fill=col,anchor="mm")
    d.text((W/2,24),cap,font=FB(18),fill=(20,20,24),anchor="mm")
    d.text((W/2,48),sub,font=FR(14),fill=(90,90,100),anchor="mm")
    if tally:
        for i,(t,col) in enumerate(tally): d.text((16,78+i*20),t,font=FB(14),fill=col,anchor="lm")
    d.text((W-10,78),"filled = +, open = −",font=FR(12),fill=(90,90,100),anchor="rm")
    ly=H-16; x=14
    for col,txt,dash in [(CB,"diene HOMO",0),(CR,"dienophile LUMO",0),(GREEN,"primary → σ bonds",1),(ORANGE,"secondary (no bond)",1)]:
        if dash: d.line([(x,ly),(x+22,ly)],fill=col,width=3)
        else: d.ellipse([x+4,ly-7,x+16,ly+7],fill=col)
        d.text((x+28,ly),txt,font=FR(12),fill=(50,50,60),anchor="lm"); x+=28+FR(12).getlength(txt)+16
    return img
frames=[];durs=[]
def add(img,ms): frames.append(img); durs.append(ms)
EL=math.radians(16)
TAGS=[('d5',"CH₂ (front)",(90,90,100),0,-30),('d2',"C2",(29,78,216),-18,-30),('d3',"C3",(29,78,216),18,-30),('a2',"C=O",(185,28,28),-26,18),('a5',"C=O",(185,28,28),26,18)]
# 1 overview endo TS, only primary
for i in range(18):
    add(render(dict(flip=0),math.radians(40+i*1.0),EL,"Endo TS: cyclopentadiene + maleic anhydride","green: the two overlaps that become the new σ bonds",secal=0,tags=TAGS),90)
az=math.radians(58)
# 2 secondary overlaps pulse in
for i in range(36):
    g=0.5+0.5*math.sin(i/36*4*math.pi)
    add(render(dict(flip=0),az,EL,"Look at the BACK of the diene (C2, C3)","each C=O carbon sits under C2 / C3: same-sign lobes overlap (orange)",glow=min(1,i/8)*(0.6+0.4*g),secal=min(1,i/8),tags=TAGS,
               tally=[("C2 lobe (−) ··· C=O carbon (−)",ORANGE),("C3 lobe (+) ··· C=O carbon (+)",ORANGE),("→ in phase: TS stabilised",GREEN)]),85)
# 3 zoom in
for i in range(24):
    t=ease(i/23); sc=70+50*t; fz=np.array([0,1.25,0.2])*(1-t)+np.array([0,1.2,1.0])*t
    g=0.5+0.5*math.sin(i/24*4*math.pi)
    add(render(dict(flip=0),az+math.radians(10)*t,EL+math.radians(6)*t,"Zoom: the secondary overlap","it stabilises the TS but never becomes a bond (no C2–C=O bond in the product)",scale=sc,focus=fz,glow=0.6+0.4*g,tally=[("secondary overlap ×2",ORANGE)]),85)
for i in range(24):
    t=ease(i/23); sc=120-50*t; fz=np.array([0,1.2,1.0])*(1-t)+np.array([0,1.25,0.2])*t
    add(render(dict(flip=0),az+math.radians(10)*(1-t),EL+math.radians(6)*(1-t),"Meanwhile C2=C3 is becoming a π bond","the C=O groups interact with this ‘developing π bond at the back of the diene’ (Clayden)",scale=sc,focus=fz,glow=0.7,tags=TAGS),85)
# 4 flip to exo
for i in range(22):
    t=i/21
    add(render(dict(flip=t),az,EL,"Exo: flip the anhydride over","the C=O groups swing to the front, under the CH₂",glow=0.7*(1-t),secal=1-t,tags=TAGS[:1]),85)
for i in range(22):
    add(render(dict(flip=1),az+math.radians(-0.8*i),EL,"Exo TS: no secondary overlap","the C=O groups are far from C2/C3 → higher TS → slower",tags=[TAGS[0]],tally=[("secondary overlap: none",(120,120,130))]),90)
az2=az+math.radians(-0.8*21)
for i in range(18):
    t=i/17
    add(render(dict(flip=1-t),az2,EL,"Endo wins on speed (kinetic product)","exo is the more stable product, but endo forms faster",glow=0.7*t if t>0.95 else 0,tags=TAGS[:1]),85)
for i in range(24):
    g=0.5+0.5*math.sin(i/24*4*math.pi)
    add(render(dict(flip=0),az2+math.radians(1.2*i),EL,"Endo TS: 2 primary + 2 secondary overlaps","L13 p.21, 29 · Clayden 2e p.884",glow=0.6+0.4*g,tags=TAGS),90)
for i in range(4): add(frames[-1],150)
frames[0].save("endo_secondary_overlap.gif",save_all=True,append_images=frames[1:],duration=durs,loop=0,optimize=True)
for k,idx in enumerate([10,40,70,120]): frames[idx].save(f"s{k}.png")
print(len(frames))
