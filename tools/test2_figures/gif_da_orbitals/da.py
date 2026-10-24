import numpy as np, math
from PIL import Image, ImageDraw, ImageFont
from scipy.spatial import ConvexHull
W,H=700,540; SS=2
FB=lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",s)
FR=lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",s)
def unit(v): v=np.asarray(v,float); return v/np.linalg.norm(v)
Y=np.array([0,1.,0]); X=np.array([1.,0,0])
GREEN=(21,128,61); RED=(200,30,30); CB=(29,78,216); CR=(185,28,28); GR=(70,70,78); HC=(245,245,245)
def ease(t): t=min(max(t,0),1); return t*t*(3-2*t)
def lerp(a,b,t): return np.asarray(a,float)*(1-t)+np.asarray(b,float)*t
R6=1.40; HSEP=2.9
def ring(a,y=0.0): a=math.radians(a); return np.array([R6*math.cos(a),y,R6*math.sin(a)])
# diene (bottom, HOMO psi2) ; dienophile (top, LUMO pi*)
C1,C2,C3,C4=ring(180),ring(120),ring(60),ring(0)
D6s=np.array([-0.9,HSEP,-0.35]); D5s=np.array([0.9,HSEP,-0.35])
D6e=ring(-120,0.55); D5e=ring(-60,0.55)
cD={'C1':0.60,'C2':0.37,'C3':-0.37,'C4':-0.60}; cP={'D6':-1.0,'D5':1.0}
def sp2_in_out(c,n):
    d=unit(n-c); a=math.atan2(d[2],d[0])
    ds=[np.array([math.cos(a+s*2*math.pi/3),0,math.sin(a+s*2*math.pi/3)]) for s in (1,-1)]
    ds.sort(key=lambda v: np.dot(v,unit(-c*np.array([1,0,1]))))
    return ds[1],ds[0]
in1,out1=sp2_in_out(C1,C2); in4,out4=sp2_in_out(C4,C3)
def sp3(c,up):
    b=unit(np.array([c[0],0,c[2]])); th=math.radians(50); return b*math.cos(th)+Y*math.sin(th)*(1 if up else -1)
def build(st):
    r=ease(st['react']); atoms=[];bonds=[];lobes=[];links=[]
    D6=lerp(D6s,D6e,r); D5=lerp(D5s,D5e,r)
    P={'C1':C1,'C2':C2,'C3':C3,'C4':C4,'D6':D6,'D5':D5}
    for k,p in P.items(): atoms.append((k,p,0.30,GR,None))
    # diene H
    for k in ('C2','C3'):
        d=unit(np.array([P[k][0],0,P[k][2]])); h=P[k]+d*1.0; atoms.append(('H'+k,h,0.19,HC,'H')); bonds.append((P[k],h,1,(60,60,66)))
    for c,ii,oo in ((C1,in1,out1),(C4,in4,out4)):
        for dd,up in ((ii,False),(oo,True)):  # dienophile from TOP: inside -> down, outside -> up
            h=c+unit(lerp(dd,sp3(c,up),r))*1.0; atoms.append(('h',h,0.19,HC,'H')); bonds.append((c,h,1,(60,60,66)))
    # dienophile H (ethylene in horizontal plane, along x)
    for k,sx in (('D6',-1),('D5',1)):
        for sz in (-1,1):
            d0=unit(np.array([sx*0.5,0,sz*0.866]))
            b=unit(np.array([P[k][0],0,P[k][2]]))
            d1=unit(b*0.55+Y*0.75+np.array([0,0,sz*0.45])) if sz>0 else unit(b*0.9+Y*0.25)
            h=P[k]+unit(lerp(d0,d1,r))*1.0; atoms.append(('h',h,0.19,HC,'H')); bonds.append((P[k],h,1,(60,60,66)))
    ob=lambda a,b: 0  # placeholder
    bonds.append((C1,C2,2 if r<0.5 else 1,(60,60,66))); bonds.append((C2,C3,1 if r<0.5 else 2,(60,60,66))); bonds.append((C3,C4,2 if r<0.5 else 1,(60,60,66)))
    bonds.append((D6,D5,2 if r<0.5 else 1,(60,60,66)))
    if r>0.05:
        o=1 if r>0.6 else 0
        bonds.append((C1,D6,o,GREEN)); bonds.append((C4,D5,o,GREEN))
    oa=max(0,1-r*1.7)
    if oa>0:
        for k in ('C1','C2','C3','C4'): lobes.append((P[k],cD[k],CB,oa))
        for k in ('D6','D5'): lobes.append((P[k],cP[k],CR,oa))
        if st.get('links',0)>0:
            la=oa*st['links']
            for a,b in (('C1','D6'),('C4','D5')):
                links.append((P[a],cD[a],P[b],cP[b],la))
    planes=[]
    if st.get('planes',0)>0 and oa>0:
        planes.append((np.array([0,0,0.1]),2.4,1.9,(37,99,235),st['planes']*oa))
        planes.append((np.array([0,P['D6'][1],-0.35]),1.9,1.1,(220,38,38),st['planes']*oa))
    return atoms,bonds,lobes,links,planes
def proj(p,az,el,scale=64,dist=13,cy=0.62):
    ca,sa=math.cos(az),math.sin(az); x=p[0]*ca+p[2]*sa; z=-p[0]*sa+p[2]*ca
    ce,se=math.cos(el),math.sin(el); y=p[1]*ce+z*se; z2=-p[1]*se+z*ce
    f=dist/(dist+z2); return np.array([(W/2+x*scale*f)*SS,(H*cy-(y-1.1)*scale*f)*SS]),z2,f
def lobe_len(c): return 0.40+0.55*abs(c)
def lobe_poly(P,nv,c,az,el):
    L=lobe_len(c); w=0.16+0.16*abs(c)
    a=unit(np.cross(nv,X)); b=np.cross(nv,a); pts=[]
    for i in range(9):
        tt=i/8*math.pi
        for j in range(12):
            pp=j/12*2*math.pi
            q=P+nv*(L*(1-math.cos(tt))/2*1.9)+(a*math.cos(pp)+b*math.sin(pp))*w*math.sin(tt)
            pts.append(proj(q,az,el)[0])
    pts=np.array(pts); hull=ConvexHull(pts); return [tuple(pts[v]) for v in hull.vertices]
def render(st,az,el,cap,sub,labels=None,tally=None):
    atoms,bonds,lobes,links,planes=build(st)
    img=Image.new("RGB",(W*SS,H*SS),(255,255,255)); d=ImageDraw.Draw(img,"RGBA")
    prims=[]
    for (cen,hx,hz,col,al) in planes:
        cs=[cen+np.array([sx*hx,0,sz*hz]) for sx,sz in ((-1,-1),(1,-1),(1,1),(-1,1))]
        prims.append((proj(cen,az,el)[1]+0.6,'p',([tuple(proj(c,az,el)[0]) for c in cs],col,al)))
    for (p,q,o,col) in bonds:
        (a,za,_),(b,zb,_)=proj(p,az,el),proj(q,az,el); prims.append(((za+zb)/2+0.02,'b',(a,b,o,col)))
    for (nm,p,r,col,lab) in atoms:
        a,z,f=proj(p,az,el); prims.append((z,'a',(a,r*64*f*SS,col,lab)))
    for (P,c,col,al) in lobes:
        for sgn in (1,-1):
            nv=Y*sgn; filled=(c*sgn)>0
            prims.append((proj(P+nv*0.5,az,el)[1],'l',(lobe_poly(P,nv,c,az,el),filled,col,al)))
    for pr in sorted(prims,key=lambda x:-x[0]):
        k=pr[1]
        if k=='p':
            poly,col,al=pr[2]; d.polygon(poly,fill=col+(int(40*al),),outline=col+(int(150*al),))
        elif k=='b':
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
            if lab: d.text((a[0],a[1]),lab,font=FB(int(r/SS*0.95)),fill=(30,30,30),anchor="mm")
        else:
            poly,filled,col,al=pr[2]
            if filled: d.polygon(poly,fill=col+(int(200*al),),outline=col+(int(255*al),))
            else:
                d.polygon(poly,fill=(255,255,255,int(150*al)),outline=col+(int(255*al),)); d.line(poly+[poly[0]],fill=col+(int(255*al),),width=int(2.2*SS))
    for (pa,ca,pb,cb,al) in links:
        ta=pa+Y*lobe_len(ca)*0.95; tb=pb-Y*lobe_len(cb)*0.95
        A2=proj(ta,az,el)[0]; B2=proj(tb,az,el)[0]
        for i in range(0,14,2):
            p=A2+(B2-A2)*i/14; q=A2+(B2-A2)*(i+1)/14
            d.line([tuple(p),tuple(q)],fill=GREEN+(int(255*al),),width=int(3.4*SS))
    mids=[]
    for (pa,ca,pb,cb,al) in links:
        ta=pa+Y*lobe_len(ca)*0.95; tb=pb-Y*lobe_len(cb)*0.95
        m=(proj(ta,az,el)[0]+proj(tb,az,el)[0])/2/SS; mids.append((m,al))
    img=img.resize((W,H),Image.LANCZOS); d=ImageDraw.Draw(img)
    if st.get('checks'):
        for (m,al),dx in zip(mids,(-26,26)):
            if al>0.5: d.text((m[0]+dx,m[1]),"✓",font=FB(22),fill=GREEN,anchor="mm")
    d.text((W/2,24),cap,font=FB(18),fill=(20,20,24),anchor="mm")
    d.text((W/2,48),sub,font=FR(14),fill=(90,90,100),anchor="mm")
    if tally:
        for i,(t,col) in enumerate(tally): d.text((16,76+i*20),t,font=FB(14),fill=col,anchor="lm")
    if labels:
        for (t,x,y,col) in labels: d.text((x,y),t,font=FB(14),fill=col,anchor="mm")
    d.text((W-10,76),"filled = +, open = −",font=FR(12),fill=(90,90,100),anchor="rm")
    ly=H-18; x=14
    for col,txt,dash in [(CB,"diene HOMO ψ2",0),(CR,"dienophile LUMO π*",0),(GREEN,"in-phase overlap / new σ",1),((120,130,150),"molecular (nodal) planes",0)]:
        if dash: d.line([(x,ly),(x+22,ly)],fill=col,width=3)
        else: d.ellipse([x+4,ly-7,x+16,ly+7],fill=col)
        d.text((x+28,ly),txt,font=FR(12),fill=(50,50,60),anchor="lm"); x+=28+FR(12).getlength(txt)+16
    return img

frames=[];durs=[]
def add(img,ms): frames.append(img); durs.append(ms)
EL0=math.radians(7); EL1=math.radians(26)
TA=[("diene HOMO ψ2: ends + / −  (A)",CB),("dienophile LUMO π*: ends − / +  (A)",CR)]
TC=[("π2s (dienophile) → (4q+2)s: +1",GREEN),("π4s (diene) → (4r)s: 0",(90,90,100)),("sum = 1 → thermally allowed",GREEN)]
for i in range(20):
    add(render(dict(react=0,links=0,planes=0),math.radians(-12+i*0.6),EL0,"Diels–Alder: diene HOMO (bottom) + dienophile LUMO (top)","front view: the four diene p orbitals in a row; look only at the END lobes",tally=TA),90)
az=0.0
for i in range(14):
    t=ease(i/13)
    add(render(dict(react=0,links=t,planes=0,checks=t>0.6),az,EL0,"Both ends in phase: A meets A","left: + with +   ·   right: − with −   (head-to-head at BOTH ends)",tally=TA),90)
for i in range(8): add(frames[-1],120)
for i in range(34):
    t=ease(i/33)
    add(render(dict(react=0,links=1,planes=min(1,i/8),checks=True),az+math.radians(-40*t),EL0+(EL1-EL0)*t,"No twist needed: π4s + π2s","diene uses its TOP face at both ends; dienophile its BOTTOM face at both ends",tally=TC),85)
for i in range(6): add(frames[-1],120)
az2=math.radians(-40)
for i in range(32):
    t=ease(i/31)
    add(render(dict(react=t,links=1,planes=1),az2,EL1,"Concerted: both σ bonds form in one step","3 π bonds → 1 π + 2 σ; the new C=C appears between C2 and C3",tally=TC),80)
for i in range(40):
    add(render(dict(react=1),az2+math.radians(9*i),EL1,"Product: cyclohexene","green = the two new σ bonds (L13 p.10)"),75)
for i in range(6): add(frames[-1],150)
frames[0].save("DA_orbitals.gif",save_all=True,append_images=frames[1:],duration=durs,loop=0,optimize=True)
for k,idx in enumerate([5,30,50,110]): frames[idx].save(f"c{k}.png")
print(len(frames))
