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
Rr=1.85; SPAN=math.radians(262); RISE=1.85
coef=[-0.52,0.23,0.42,-0.42,-0.23,0.52]   # C1..C6, triene LUMO psi4 (overall sign chosen so C6 top = +)
def chain(tau):
    P={}
    for k in range(1,8):
        f=(7-k)/6
        a=math.radians(-90-131)+SPAN*f   # C7 at front-left, C1 at front-right (gap faces -z)
        P['C%d'%k]=np.array([Rr*math.cos(a),tau*RISE*f ,Rr*math.sin(a)])
    return P
def build(st):
    tau=ease(st['tau']); m=ease(st['mig']); P=chain(tau)
    atoms=[];bonds=[];lobes=[];links=[]
    for k,p in P.items(): atoms.append((k,p,0.30,GR,None))
    gapdir=unit(P['C1']-P['C7'])*np.array([1,0,1]); gapdir=unit(gapdir)
    Hs=P['C7']+Y*0.85+gapdir*0.55
    He=P['C1']-Y*0.85-gapdir*0.55
    Hp=lerp(Hs,He,m)
    atoms.append(('H',Hp,0.24,(147,197,253),'H'))
    bonds.append((P['C7'],Hp,1 if m<0.5 else 0,(120,120,130)) if m<0.95 else None)
    if m>0.05: bonds.append((P['C1'],Hp,1 if m>0.5 else 0,GREEN))
    # other C7 H (bottom) and C1 H's omitted for clarity
    dbl0={(1,2),(3,4),(5,6)}; dbl1={(2,3),(4,5),(6,7)}
    for k in range(1,7):
        o=2 if ((k,k+1) in (dbl0 if m<0.5 else dbl1)) else 1
        bonds.append((P['C%d'%k],P['C%d'%(k+1)],o,(60,60,66)))
    oa=max(0,1-m*1.8)
    if oa>0:
        for k in range(1,7): lobes.append((P['C%d'%k],coef[k-1],CR,oa*(1 if k in (1,6) else 0.35)))
        lobes.append((P['C7'],0.55,CB,oa,'up_only'))
        if st.get('links',0)>0:
            la=oa*st['links']
            links.append((P['C7']+Y*0.85,P['C6']+Y*0.85,True,la))
            c1top=P['C1']+Y*0.85; c1bot=P['C1']-Y*0.85
            reach_bottom = tau>0.6
            links.append((Hp,c1bot if reach_bottom else c1top,reach_bottom,la))
    bonds=[b for b in bonds if b is not None]
    return atoms,bonds,lobes,links
def proj(p,az,el,scale=78,dist=13,cy=0.55):
    ca,sa=math.cos(az),math.sin(az); x=p[0]*ca+p[2]*sa; z=-p[0]*sa+p[2]*ca
    ce,se=math.cos(el),math.sin(el); y=p[1]*ce+z*se; z2=-p[1]*se+z*ce
    f=dist/(dist+z2); return np.array([(W/2+x*scale*f)*SS,(H*cy-(y-1.0)*scale*f)*SS]),z2,f
def lobe_len(c): return 0.40+0.55*abs(c)
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
def render(st,az,el,cap,sub,tally=None,note=None):
    atoms,bonds,lobes,links=build(st)
    img=Image.new("RGB",(W*SS,H*SS),(255,255,255)); d=ImageDraw.Draw(img,"RGBA")
    prims=[]
    for (p,q,o,col) in bonds:
        (a,za,_),(b,zb,_)=proj(p,az,el),proj(q,az,el); prims.append(((za+zb)/2+0.02,'b',(a,b,o,col)))
    for (nm,p,r,col,lab) in atoms:
        a,z,f=proj(p,az,el); prims.append((z,'a',(a,r*78*f*SS,col,lab)))
    for lb in lobes:
        P,c,col,al=lb[:4]; only=len(lb)>4
        for sgn in ((1,) if only else (1,-1)):
            nv=Y*sgn; filled=(c*sgn)>0
            prims.append((proj(P+nv*0.5,az,el)[1],'l',(lobe_poly(P,nv,c,az,el),filled,col,al)))
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
            if lab: d.text((a[0],a[1]),lab,font=FB(int(r/SS*0.9)),fill=(20,20,40),anchor="mm")
        else:
            poly,filled,col,al=pr[2]
            if filled: d.polygon(poly,fill=col+(int(190*al),),outline=col+(int(255*al),))
            else:
                d.polygon(poly,fill=(255,255,255,int(140*al)),outline=col+(int(255*al),)); d.line(poly+[poly[0]],fill=col+(int(255*al),),width=int(2.2*SS))
    marks=[]
    for (p,q,ok,al) in links:
        A2=proj(p,az,el)[0]; B2=proj(q,az,el)[0]; col=GREEN if ok else RED
        for i in range(0,14,2):
            a=A2+(B2-A2)*i/14; b=A2+(B2-A2)*(i+1)/14; d.line([tuple(a),tuple(b)],fill=col+(int(255*al),),width=int(3.4*SS))
        marks.append(((A2+B2)/2/SS,ok,al))
    labs={}
    for nm,p,r,col,lab in atoms:
        if nm in ('C1','C7','C6'):
            out=unit(p*np.array([1,0,1])); labs[nm]=proj(p+out*0.55-Y*0.15,az,el)[0]/SS
    img=img.resize((W,H),Image.LANCZOS); d=ImageDraw.Draw(img)
    for (m,ok,al) in marks:
        if al>0.5: d.text((m[0]+18,m[1]),"✓" if ok else "×",font=FB(22),fill=GREEN if ok else RED,anchor="mm")
    for nm,q in labs.items(): d.text((q[0],q[1]),nm,font=FB(14),fill=(60,60,70),anchor="mm")
    d.text((W/2,24),cap,font=FB(18),fill=(20,20,24),anchor="mm")
    d.text((W/2,48),sub,font=FR(14),fill=(90,90,100),anchor="mm")
    if tally:
        for i,(t,col) in enumerate(tally): d.text((16,76+i*20),t,font=FB(14),fill=col,anchor="lm")
    if note: d.text((W/2,H-42),note,font=FR(13),fill=(60,60,70),anchor="mm")
    d.text((W-10,76),"filled = +, open = −",font=FR(12),fill=(90,90,100),anchor="rm")
    ly=H-16; x=14
    for col,txt,dash in [(CB,"σ C–H (HOMO, S)",0),(CR,"triene LUMO ψ4 (A)",0),(GREEN,"in phase",1),(RED,"out of phase",1)]:
        if dash: d.line([(x,ly),(x+22,ly)],fill=col,width=3)
        else: d.ellipse([x+4,ly-7,x+16,ly+7],fill=col)
        d.text((x+28,ly),txt,font=FR(12),fill=(50,50,60),anchor="lm"); x+=28+FR(12).getlength(txt)+16
    return img
frames=[];durs=[]
def add(img,ms): frames.append(img); durs.append(ms)
EL=math.radians(16)
T=[("σ C–H: S   ·   triene LUMO ψ4: A",(40,40,48)),("→ ends do not match on one face",RED)]
TB=[("σ2s + π6a",(40,40,48)),("(4q+2)s: σ2s → +1",GREEN),("(4q+2)a: π6a → 0",(90,90,100)),("sum = 1 → thermally allowed",GREEN)]
for i in range(22):
    add(render(dict(tau=0,mig=0,links=min(1,i/6)),math.radians(-20+i*0.9),EL,"Thermal [1,7]-H shift: flat chain","C7 end: + meets + ✓   ·   but the H meets the TOP lobe of C1 (−) ×",tally=T),90)
for i in range(6): add(frames[-1],120)
az=math.radians(0)
for i in range(32):
    t=i/31
    add(render(dict(tau=t,mig=0,links=1),az,EL,"Twist: the triene coils into a helix (antarafacial)","C1 rises above the H, so the H now meets C1's BOTTOM lobe (+)",tally=T if t<0.6 else TB),85)
for i in range(8): add(frames[-1],120)
for i in range(34):
    add(render(dict(tau=1,mig=0,links=1),az+math.radians(-2.2*i),EL,"H leaves the TOP face of C7, arrives on the BOTTOM face of C1","the H stays on one face of the σ bond (s); the triene uses both faces (a)",tally=TB),85)
az2=az+math.radians(-2.2*33)
for i in range(30):
    t=ease(i/29)
    add(render(dict(tau=1,mig=t,links=1),az2,EL,"Concerted H shift","double bonds move: C1=C2, C3=C4, C5=C6 → C2=C3, C4=C5, C6=C7",tally=TB),85)
for i in range(30):
    add(render(dict(tau=1,mig=1,links=0),az2+math.radians(6*i),math.radians(30),"Product: H now on C1 (other H atoms omitted)","example: previtamin D → vitamin D by a thermal antarafacial [1,7]-H shift (L16 p.23)",note="[1,3]-H: a 3-carbon chain cannot twist like this → no reaction (L16 p.24)"),80)
for i in range(6): add(frames[-1],150)
frames[0].save("H17_antarafacial.gif",save_all=True,append_images=frames[1:],duration=durs,loop=0,optimize=True)
for k,idx in enumerate([12,55,80,150]): frames[idx].save(f"c{k}.png")
print(len(frames))
