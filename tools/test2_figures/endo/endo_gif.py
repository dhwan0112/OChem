import numpy as np, math
from PIL import Image, ImageDraw, ImageFont
from scipy.spatial import ConvexHull
from geom import *
W,H=720,560; SS=2
FB=lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",s)
FR=lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",s)
X=np.array([1.,0,0])
GREEN=(21,128,61); ORANGE=(234,88,12); CB=(29,78,216); CR=(185,28,28); GR=(70,70,78); HC=(245,245,245); OX=(220,38,38)
def ease(t): t=min(max(t,0),1); return t*t*(3-2*t)
def lerp(a,b,t): return np.asarray(a,float)*(1-t)+np.asarray(b,float)*t
def rotx(p,ang,cen):
    p=p-cen; c,s=math.cos(ang),math.sin(ang); return cen+np.array([p[0],p[1]*c-p[2]*s,p[1]*s+p[2]*c])
DEN=dienophile('endo'); DEX=dienophile('exo')
# product targets (endo)
def prod_pos():
    P={}
    P['Cb']=np.array([-0.78,HD-1.55,-0.55]); P['Ca']=np.array([0.78,HD-1.55,-0.55])
    P['C5']=np.array([0,HD+0.75,-0.8])
    return P
def substituent_dirs():
    pass
def build(st):
    flip=st.get('flip',0.0)  # 0 = endo, 1 = exo (rotation about C=C axis)
    r=ease(st.get('react',0)); atoms=[];bonds=[];lobes=[];links=[]
    # diene
    P={k:v.copy() for k,v in D.items()}
    pp=prod_pos(); P['C5']=lerp(D['C5'],pp['C5'],r)
    for k in ('C2','C3'): P[k]=D[k]+Y*0.15*r
    # dienophile (rotated by flip*pi around x axis through the C=C midpoint, then raised by reaction)
    cen=(DEN['Cb']+DEN['Ca'])/2
    dd={k:rotx(v,math.pi*ease(flip),cen) for k,v in DEN.items()}
    # reaction: move dienophile up toward product (endo only)
    shift=lerp(np.zeros(3),pp['Cb']-DEN['Cb'],r)
    for k in dd: dd[k]=dd[k]+shift
    for k in ('C1','C2','C3','C4','C5'): atoms.append((k,P[k],0.30,GR,None))
    for k,v in dd.items():
        if k.startswith('H'): atoms.append((k,v,0.19,HC,'H'))
        elif k=='O': atoms.append((k,v,0.31,OX,'O'))
        else: atoms.append((k,v,0.30,GR,None))
    # H on diene
    for k in ('C1','C2','C3','C4'):
        out=unit(np.array([P[k][0],0,P[k][2]]))
        d0=out; d1=unit(out*0.8+Y*0.55) if k in ('C1','C4') else out
        h=P[k]+unit(lerp(d0,d1,r))*1.0; atoms.append(('h'+k,h,0.19,HC,'H')); bonds.append((P[k],h,1,(60,60,66)))
    for s in (1,-1):
        h=P['C5']+unit(np.array([0,0.8*s,-0.6]))*1.0; atoms.append(('h5'+str(s),h,0.19,HC,'H')); bonds.append((P['C5'],h,1,(60,60,66)))
    bonds+=[(P['C1'],P['C2'],2 if r<0.5 else 1,(60,60,66)),(P['C2'],P['C3'],1 if r<0.5 else 2,(60,60,66)),(P['C3'],P['C4'],2 if r<0.5 else 1,(60,60,66)),
            (P['C4'],P['C5'],1,(60,60,66)),(P['C5'],P['C1'],1,(60,60,66))]
    bonds+=[(dd['Cb'],dd['Ca'],2 if r<0.5 else 1,(60,60,66)),(dd['Ca'],dd['Cc'],1,(60,60,66)),(dd['Cc'],dd['O'],2,(60,60,66)),
            (dd['Cc'],dd['Hc'],1,(60,60,66)),(dd['Ca'],dd['Ha'],1,(60,60,66)),(dd['Cb'],dd['Hb1'],1,(60,60,66)),(dd['Cb'],dd['Hb2'],1,(60,60,66))]
    if r>0.05:
        o=1 if r>0.6 else 0
        bonds+=[(P['C1'],dd['Cb'],o,GREEN),(P['C4'],dd['Ca'],o,GREEN)]
    oa=max(0,1-r*1.7)*st.get('orb',1)
    flipping = 0.05<flip<0.95
    if oa>0:
        for k in ('C1','C2','C3','C4'): lobes.append((P[k],cDiene[k],CB,oa))
        if not flipping:
            sgn=1  # overall LUMO sign re-chosen after flip so primary overlaps stay in phase
            for k in ('Cb','Ca','Cc','O'): lobes.append((dd[k],cDph[k]*sgn,CR,oa))
        if st.get('links',0)>0 and not flipping:
            la=oa*st['links']
            links.append((P['C1'],cDiene['C1'],dd['Cb'],cDph['Cb'],la,GREEN))
            links.append((P['C4'],cDiene['C4'],dd['Ca'],cDph['Ca'],la,GREEN))
        if st.get('sec',0)>0 and flip<0.05:
            links.append((P['C3'],cDiene['C3'],dd['Cc'],cDph['Cc'],oa*st['sec'],ORANGE))
    return atoms,bonds,lobes,links,P,dd
def proj(p,az,el,scale=66,dist=13,cy=0.60):
    ca,sa=math.cos(az),math.sin(az); x=p[0]*ca+p[2]*sa; z=-p[0]*sa+p[2]*ca
    ce,se=math.cos(el),math.sin(el); y=p[1]*ce+z*se; z2=-p[1]*se+z*ce
    f=dist/(dist+z2); return np.array([(W/2+x*scale*f)*SS,(H*cy-(y-1.3)*scale*f)*SS]),z2,f
def lobe_len(c): return 0.38+0.55*abs(c)
def lobe_poly(P,nv,c,az,el):
    L=lobe_len(c); w=0.15+0.15*abs(c)
    a=unit(np.cross(nv,X)); b=np.cross(nv,a); pts=[]
    for i in range(9):
        tt=i/8*math.pi
        for j in range(12):
            pp=j/12*2*math.pi
            q=P+nv*(L*(1-math.cos(tt))/2*1.9)+(a*math.cos(pp)+b*math.sin(pp))*w*math.sin(tt)
            pts.append(proj(q,az,el)[0])
    pts=np.array(pts); hull=ConvexHull(pts); return [tuple(pts[v]) for v in hull.vertices]
def render(st,az,el,cap,sub,tags=None,tally=None):
    atoms,bonds,lobes,links,P,dd=build(st)
    img=Image.new("RGB",(W*SS,H*SS),(255,255,255)); d=ImageDraw.Draw(img,"RGBA")
    prims=[]
    for (p,q,o,col) in bonds:
        (a,za,_),(b,zb,_)=proj(p,az,el),proj(q,az,el); prims.append(((za+zb)/2+0.02,'b',(a,b,o,col)))
    for (nm,p,r,col,lab) in atoms:
        a,z,f=proj(p,az,el); prims.append((z,'a',(a,r*66*f*SS,col,lab)))
    for (Pp,c,col,al) in lobes:
        for sgn in (1,-1):
            nv=Y*sgn; filled=(c*sgn)>0
            prims.append((proj(Pp+nv*0.5,az,el)[1],'l',(lobe_poly(Pp,nv,c,az,el),filled,col,al)))
    for pr in sorted(prims,key=lambda x:-x[0]):
        k=pr[1]
        if k=='b':
            a,b,o,col=pr[2]; dx,dy=b-a; L=math.hypot(dx,dy)+1e-9; nx,ny=-dy/L,dx/L
            if o==0:
                for i in range(0,10,2):
                    p=a+(b-a)*i/10; q=a+(b-a)*(i+1)/10; d.line([tuple(p),tuple(q)],fill=col,width=int(4*SS))
                continue
            for oo in ([0] if o==1 else [-1,1]):
                d.line([(a[0]+nx*oo*4*SS,a[1]+ny*oo*4*SS),(b[0]+nx*oo*4*SS,b[1]+ny*oo*4*SS)],fill=col,width=int((5 if o==1 else 3.5)*SS))
        elif k=='a':
            a,r,col,lab=pr[2]
            for i in range(6,0,-1):
                rr=r*i/6; kk=0.75+0.45*(1-i/6); off=(1-i/6)*r*0.35
                d.ellipse([a[0]-rr-off,a[1]-rr-off,a[0]+rr-off,a[1]+rr-off],fill=tuple(int(min(255,c*kk)) for c in col))
            if col==HC: d.ellipse([a[0]-r,a[1]-r,a[0]+r,a[1]+r],outline=(40,40,40),width=2*SS)
            if lab: d.text((a[0],a[1]),lab,font=FB(int(r/SS*0.95)),fill=(30,30,30) if col==HC else (255,255,255),anchor="mm")
        else:
            poly,filled,col,al=pr[2]
            if filled: d.polygon(poly,fill=col+(int(190*al),),outline=col+(int(255*al),))
            else:
                d.polygon(poly,fill=(255,255,255,int(140*al)),outline=col+(int(255*al),)); d.line(poly+[poly[0]],fill=col+(int(255*al),),width=int(2.2*SS))
    for (pa,ca,pb,cb,al,col) in links:
        ta=pa-Y*lobe_len(ca)*0.95; tb=pb+Y*lobe_len(cb)*0.95
        A2=proj(ta,az,el)[0]; B2=proj(tb,az,el)[0]
        for i in range(0,14,2):
            p=A2+(B2-A2)*i/14; q=A2+(B2-A2)*(i+1)/14
            d.line([tuple(p),tuple(q)],fill=col+(int(255*al),),width=int((3.4 if col==GREEN else 4.2)*SS))
    img=img.resize((W,H),Image.LANCZOS); d=ImageDraw.Draw(img)
    if tags:
        for (key,txt,col,dx,dy) in tags:
            src={**P,**dd}
            if key in src:
                q=proj(src[key],az,el)[0]/SS; d.text((q[0]+dx,q[1]+dy),txt,font=FB(14),fill=col,anchor="mm")
    d.text((W/2,24),cap,font=FB(18),fill=(20,20,24),anchor="mm")
    d.text((W/2,48),sub,font=FR(14),fill=(90,90,100),anchor="mm")
    if tally:
        for i,(t,col) in enumerate(tally): d.text((16,78+i*20),t,font=FB(14),fill=col,anchor="lm")
    ly=H-16; x=14
    for col,txt,dash in [(CB,"diene HOMO ψ2",0),(CR,"acrolein LUMO",0),(GREEN,"primary overlap → σ bonds",1),(ORANGE,"secondary overlap (no bond)",1)]:
        if dash: d.line([(x,ly),(x+22,ly)],fill=col,width=3)
        else: d.ellipse([x+4,ly-7,x+16,ly+7],fill=col)
        d.text((x+28,ly),txt,font=FR(12),fill=(50,50,60),anchor="lm"); x+=28+FR(12).getlength(txt)+16
    return img
frames=[];durs=[]
def add(img,ms): frames.append(img); durs.append(ms)
EL=math.radians(13)
TAG_TS=[('C5',"CH₂ (front)",(90,90,100),0,-28),('C3',"C2=C3 (back)",(29,78,216),10,-34),('O',"C=O",(185,28,28),26,12)]
# step 1
for i in range(18):
    add(render(dict(flip=0,links=min(1,i/6)),math.radians(52+i*1.2),EL,"Step 1 · The TS: two parallel planes","side view: diene on top (CH₂ at the front, C2=C3 at the back), acrolein underneath",tags=TAG_TS),90)
# step 2 endo with secondary overlap
az=math.radians(73)
for i in range(30):
    t=min(1,i/8)
    add(render(dict(flip=0,links=1,sec=t),az+math.radians(1.2*i),EL,"Step 2 · ENDO: the C=O is tucked under the diene","its p orbital also overlaps in phase with C3 of the diene (orange)",tags=TAG_TS,tally=[("extra overlap → lower TS energy",ORANGE)]),90)
for i in range(6): add(frames[-1],120)
az2=az+math.radians(1.2*29)
# step 3 flip to exo
for i in range(22):
    t=i/21
    add(render(dict(flip=t,links=1),az2,EL,"Step 3 · EXO: flip the dienophile over","the C=O now points out, under the CH₂ instead of under the diene",tags=[('C5',"CH₂",(90,90,100),0,-24)]),85)
for i in range(22):
    add(render(dict(flip=1,links=1),az2+math.radians(-1.2*i),EL,"Step 3 · EXO: no secondary overlap","only the two primary overlaps: TS is higher → forms more slowly",tags=TAG_TS,tally=[("no extra overlap",(120,120,130))]),90)
for i in range(6): add(frames[-1],120)
az3=az2+math.radians(-1.2*21)
for i in range(16):
    t=i/15
    add(render(dict(flip=1-t,links=1),az3,EL,"Endo TS is lower → endo product forms faster","kinetic control (the exo product is often the more stable one)"),85)
# step 4 product
for i in range(30):
    t=ease(i/29)
    add(render(dict(flip=0,links=1,sec=1,react=t),az3,EL,"Step 4 · Bonds form: endo adduct","the CHO ends up on the side of the new C=C, away from the CH₂ bridge"),85)
TAG_P=[('C5',"CH₂ bridge",(90,90,100),0,-26),('O',"CHO (endo)",(185,28,28),36,14),('C2',"new C=C",(29,78,216),-20,-24)]
for i in range(40):
    add(render(dict(flip=0,react=1),az3+math.radians(9*i),math.radians(20),"Endo product: CHO anti to the CH₂ bridge","= syn to the new C=C (L13 p.21: “new C=C and C=O on the same side”)",tags=TAG_P),80)
for i in range(6): add(frames[-1],150)
frames[0].save("endo_rule_3D.gif",save_all=True,append_images=frames[1:],duration=durs,loop=0,optimize=True)
for k,idx in enumerate([10,35,75,170]): frames[idx].save(f"c{k}.png")
print(len(frames))
