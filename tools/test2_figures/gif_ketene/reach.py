import numpy as np, math
from PIL import Image, ImageDraw, ImageFont
W,H=680,520; SS=2
FB=lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",s)
FR=lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",s)
def unit(v): v=np.asarray(v,float); return v/np.linalg.norm(v)
Y=np.array([0,1.,0]); X=np.array([1.,0,0]); Z=np.array([0,0,1.])
A=0.67; HSEP=2.3; HALF=0.655
GREEN=(21,128,61); RED=(200,30,30); ORANGE=(234,88,12)
CB=(29,78,216); CR=(185,28,28); CO=(234,88,12)  # HOMO blue, LUMO red, extra p orange
def ease(t): t=min(max(t,0),1); return t*t*(3-2*t)
def lerp(a,b,t): return np.asarray(a)*(1-t)+np.asarray(b)*t
def overlap_sign(p1,n1,p2,n2):
    u=unit(p2-p1); Ssig,Spi=-1.0,0.35
    return float(np.dot(n1,n2)*Spi+np.dot(n1,u)*np.dot(n2,u)*(Ssig-Spi))
def build(st):
    """st: dict with theta, phi, ketene(0..1), react(0..1)"""
    th,ph,kt,rx=st['theta'],st['phi'],st['ket'],st['react']
    atoms=[];bonds=[];lobes=[];inter=[]
    T1=np.array([-A,0,0]); T2=np.array([A,0,0])
    d=np.array([math.sin(th),0,math.cos(th)]); ph_=np.array([-math.cos(th),0,math.sin(th)])
    n=math.cos(ph)*Y+math.sin(ph)*ph_
    cen=np.array([0,HSEP,0])
    K1=cen-HALF*d; K2=cen+HALF*d
    # product targets
    P_T1=np.array([-0.78,0,0]); P_T2=np.array([0.78,0,0]); P_K1=np.array([-0.78,1.56,0]); P_K2=np.array([0.78,1.56,0])
    r=ease(rx)
    T1p=lerp(T1,P_T1,r); T2p=lerp(T2,P_T2,r); K1p=lerp(K1,P_K1,r); K2p=lerp(K2,P_K2,r)
    m=unit(np.cross(d,n))
    if rx>0.02:
        bonds.append((T1p,K1p,1 if rx>0.55 else 0,GREEN)); bonds.append((T2p,K2p,1 if rx>0.55 else 0,GREEN))
    # bottom alkene
    atoms+= [('T1',T1p,0.30,(70,70,78),None),('T2',T2p,0.30,(70,70,78),None)]
    for nm,c,sx in (('T1',T1p,-1),('T2',T2p,1)):
        for sz in (-1,1):
            dir0=unit(np.array([sx*0.5,0,sz*0.866])); dir1=unit(np.array([sx*0.55,-0.55,sz*0.63]))
            p=c+unit(lerp(dir0,dir1,r))*1.0; atoms.append(('H'+nm+str(sz),p,0.19,(245,245,245),'H')); bonds.append((c,p,1,(60,60,66)))
    bonds.append((T1p,T2p,2 if r<0.5 else 1,(60,60,66)))
    # top component
    atoms+= [('K1',K1p,0.30,(70,70,78),None),('K2',K2p,0.30,(70,70,78),None)]
    if kt<1 or True:
        bonds.append((K1p,K2p,2 if r<0.5 else 1,(60,60,66)))
    # substituents on K1: H (alkene) -> R (ketene)
    for s in (-1,1):
        dir0=unit(-d*(0.5+0.35*kt)+m*(0.866-0.25*kt)*s); dir1=unit(np.array([-0.55,0.55,0.63*s]))
        p=K1p+unit(lerp(dir0,dir1,r))*(1.0+0.4*kt)
        col=tuple(int(a*(1-kt)+b*kt) for a,b in zip((245,245,245),(124,58,237)))
        atoms.append(('K1s'+str(s),p,0.19+0.13*kt,col,'R' if kt>0.5 else 'H')); bonds.append((K1p,p,1,(60,60,66)))
    # K2: H's (alkene, fade out) or O (ketene)
    if kt<1:
        for s in (-1,1):
            p=K2p+unit(d*0.5+m*0.866*s)*1.0*(1-kt)
            if 1-kt>0.15:
                atoms.append(('K2s'+str(s),p,0.19*(1-kt)+0.02,(245,245,245),'H' if kt<0.5 else None)); bonds.append((K2p,p,1,(60,60,66)))
    if kt>0:
        Odir=unit(lerp(d,np.array([0.6,0.8,0]),r)); Op=K2p+Odir*1.18*kt
        atoms.append(('O',Op,0.30*kt+0.02,(220,38,38),'O' if kt>0.5 else None)); bonds.append((K2p,Op,2,(60,60,66)))
    # orbitals (fade out as reaction proceeds)
    oa=max(0,1-r*1.6)
    if oa>0:
        for nm,P,c in (('T1',T1p,1),('T2',T2p,1)):
            lobes.append((P,Y,c,CB,oa))
        for nm,P,c in (('K1',K1p,1),('K2',K2p,-1)):
            lobes.append((P,n,c,CR,oa))
        if kt>0: lobes.append((K2p,Y,-1,CO,oa*kt))
        # interactions
        pairs=[('T1',T1p,Y,1,'K1',K1p,n,1),('T2',T2p,Y,1,'K2',K2p,n,-1),('T1',T1p,Y,1,'K2',K2p,n,-1),('T2',T2p,Y,1,'K1',K1p,n,1)]
        show_diag = False
        for i,(a,pa,na,ca,b,pb,nb,cb) in enumerate(pairs):
            if i>=2 and not show_diag: continue
            s=ca*cb*overlap_sign(pa,na,pb,nb)
            inter.append((pa,na,ca,pb,nb,cb,s>0,oa,(GREEN if s>0 else RED)))
        if kt>0.05:
            for pa in (T1p,T2p):
                s=1*(-1)*overlap_sign(pa,Y,K2p,Y)
                inter.append((pa,Y,1,K2p,Y,-1,s>0,oa*kt,ORANGE))
    return atoms,bonds,lobes,inter
def proj(p,az,el,scale=74,dist=13,cy=0.56):
    ca,sa=math.cos(az),math.sin(az); x=p[0]*ca+p[2]*sa; z=-p[0]*sa+p[2]*ca
    ce,se=math.cos(el),math.sin(el); y=p[1]*ce+z*se; z2=-p[1]*se+z*ce
    f=dist/(dist+z2); return np.array([(W/2+x*scale*f)*SS,(H*cy-(y-1.1)*scale*f)*SS]),z2,f
def lobe_poly(P,nvec,az,el,L=0.62,w=0.27):
    nvec=unit(nvec); a=np.cross(nvec,X if abs(nvec[0])<0.9 else Y); a=unit(a); b=np.cross(nvec,a)
    pts=[]
    for i in range(10):
        tt=i/9*math.pi
        for j in range(12):
            pp=j/12*2*math.pi
            q=P+nvec*(L*(1-math.cos(tt))/2*1.9)+ (a*math.cos(pp)+b*math.sin(pp))*w*math.sin(tt)
            pts.append(proj(q,az,el)[0])
    pts=np.array(pts)
    from scipy.spatial import ConvexHull
    hull=ConvexHull(pts); return [tuple(pts[v]) for v in hull.vertices]
def tip(P,nvec,toward,L=0.62):
    nvec=unit(nvec); sgn=1 if np.dot(toward-P,nvec)>0 else -1
    return P+nvec*sgn*L*0.95, sgn
def render(st,az,el,cap,sub,tally=None,note=None,clash=False,plane=0.0,reach=0.0,labels=None):
    atoms,bonds,lobes,inter=build(st)
    img=Image.new("RGB",(W*SS,H*SS),(255,255,255)); d=ImageDraw.Draw(img,"RGBA")
    prims=[]
    for (p,q,o,col) in bonds:
        (a,za,_),(b,zb,_)=proj(p,az,el),proj(q,az,el); prims.append(((za+zb)/2+0.02,'b',(a,b,o,col)))
    for (nm,p,r,col,lab) in atoms:
        a,z,f=proj(p,az,el); prims.append((z,'a',(a,r*74*f*SS,col,lab)))
    for (P,nv,c,col,al) in lobes:
        for sgn in (1,-1):
            nn=unit(nv)*sgn; filled=(c*sgn)>0
            C=P+nn*0.6; z=proj(C,az,el)[1]
            prims.append((z,'l',(lobe_poly(P,nn,az,el),filled,col,al)))
    if plane>0:
        th,ph=st['theta'],st['phi']
        dd=np.array([math.sin(th),0,math.cos(th)]); ph_=np.array([-math.cos(th),0,math.sin(th)])
        nn=math.cos(ph)*Y+math.sin(ph)*ph_; mm=unit(np.cross(dd,nn)); cen=np.array([0,HSEP,0])
        corners=[cen+dd*1.5*sx+mm*1.25*sy for sx,sy in ((-1,-1),(1,-1),(1,1),(-1,1))]
        poly=[tuple(proj(c,az,el)[0]) for c in corners]; zc=proj(cen,az,el)[1]
        prims.append((zc+0.3,'p',(poly,plane)))
    for pr in sorted(prims,key=lambda x:-x[0]):
        if pr[1]=='p':
            poly,al=pr[2]; d.polygon(poly,fill=(120,130,150,int(70*al)),outline=(90,100,120,int(200*al))); continue
        k=pr[1]
        if k=='b':
            a,b,o,col=pr[2]; dx,dy=b-a; L=math.hypot(dx,dy)+1e-9; nx,ny=-dy/L,dx/L
            if o==0:
                for i in range(10):
                    if i%2: continue
                    p=a+(b-a)*i/10; q=a+(b-a)*(i+1)/10
                    d.line([tuple(p),tuple(q)],fill=col,width=int(4*SS))
                continue
            offs=[0] if o==1 else [-1,1]
            for oo in offs:
                d.line([(a[0]+nx*oo*4*SS,a[1]+ny*oo*4*SS),(b[0]+nx*oo*4*SS,b[1]+ny*oo*4*SS)],fill=col,width=int((5 if o==1 else 3.5)*SS))
        elif k=='a':
            a,r,col,lab=pr[2]
            for i in range(6,0,-1):
                rr=r*i/6; kk=0.75+0.45*(1-i/6); off=(1-i/6)*r*0.35
                d.ellipse([a[0]-rr-off,a[1]-rr-off,a[0]+rr-off,a[1]+rr-off],fill=tuple(int(min(255,c*kk)) for c in col))
            if col==(245,245,245): d.ellipse([a[0]-r,a[1]-r,a[0]+r,a[1]+r],outline=(40,40,40),width=2*SS)
            if lab: d.text((a[0],a[1]),lab,font=FB(int(r/SS*0.95)),fill=(30,30,30) if col==(245,245,245) else (255,255,255),anchor="mm")
        else:
            poly,filled,col,al=pr[2]
            if filled: d.polygon(poly,fill=col+(int(200*al),),outline=col+(int(255*al),))
            else:
                d.polygon(poly,fill=(255,255,255,int(150*al)),outline=col+(int(255*al),))
                d.line(poly+[poly[0]],fill=col+(int(255*al),),width=int(2.2*SS))
    # interactions on top
    for (pa,na,ca,pb,nb,cb,ok,al,col) in inter:
        ta,_=tip(pa,na,pb); tb,_=tip(pb,nb,pa)
        A2=proj(ta,az,el)[0]; B2=proj(tb,az,el)[0]
        seg=14; L=np.linalg.norm(B2-A2)
        for i in range(seg):
            if (i%2): continue
            p=A2+(B2-A2)*i/seg; q=A2+(B2-A2)*(i+1)/seg
            d.line([tuple(p),tuple(q)],fill=col+(int(255*al),),width=int(3.2*SS))
        if not ok:
            m=(A2+B2)/2; s=9*SS
            d.line([(m[0]-s,m[1]-s),(m[0]+s,m[1]+s)],fill=col+(int(255*al),),width=int(3*SS)); d.line([(m[0]-s,m[1]+s),(m[0]+s,m[1]-s)],fill=col+(int(255*al),),width=int(3*SS))
    if reach>0:
        atoms_d={a[0]:a[1] for a in atoms}
        T1=atoms_d['T1']; K1=atoms_d['K1']
        start=T1+Y*0.62*0.95; end=K1+Y*0.62*0.95
        ctrl1=np.array([-2.3,HSEP-0.6,0.0]); ctrl2=np.array([-2.0,HSEP+1.3,0.0])
        pts=[]
        N=40
        for i in range(int(N*reach)+1):
            t=i/N; q=(1-t)**3*start+3*(1-t)**2*t*ctrl1+3*(1-t)*t**2*ctrl2+t**3*end
            pts.append(tuple(proj(q,az,el)[0]))
        for i in range(0,len(pts)-1,2):
            d.line([pts[i],pts[i+1]],fill=GREEN+(255,),width=int(3.4*SS))
        if reach>=1:
            e=pts[-1]; d.ellipse([e[0]-6*SS,e[1]-6*SS,e[0]+6*SS,e[1]+6*SS],fill=GREEN+(255,))
    if clash:
        for (nm,p,r,col,lab) in atoms:
            if nm.startswith('K1s') or nm.startswith('K2s'):
                if p[1]<HSEP-0.3:
                    a,_,f=proj(p,az,el); rr=r*74*f*SS*2.0
                    d.ellipse([a[0]-rr,a[1]-rr,a[0]+rr,a[1]+rr],outline=(200,30,30,220),width=int(3*SS))
    img=img.resize((W,H),Image.LANCZOS); d=ImageDraw.Draw(img)
    d.text((W/2,24),cap,font=FB(18),fill=(20,20,24),anchor="mm")
    d.text((W/2,48),sub,font=FR(14),fill=(90,90,100),anchor="mm")
    if tally:
        x0,y0=16,72
        for i,(txt,col) in enumerate(tally):
            d.text((x0,y0+i*20),txt,font=FB(14),fill=col,anchor="lm")
    if labels:
        for (txt,x,y,col) in labels: d.text((x,y),txt,font=FB(14),fill=col,anchor="mm")
    if note: d.text((W/2,H-44),note,font=FR(13),fill=(60,60,70),anchor="mm")
    ly=H-18; x=14
    for col,txt,dash in [(CB,"HOMO (π, bottom)",0),(CR,"LUMO (top)",0),((120,130,150),"nodal plane of LUMO",0),(GREEN,"bonding",1),(RED,"antibonding",1)]:
        if dash: d.line([(x,ly),(x+22,ly)],fill=col,width=3)
        else: d.ellipse([x+4,ly-7,x+16,ly+7],fill=col)
        d.text((x+28,ly),txt,font=FR(12),fill=(50,50,60),anchor="lm"); x+= 28+FR(12).getlength(txt)+14
    d.text((W-10,72),"filled = +, open = −",font=FR(12),fill=(90,90,100),anchor="rm")
    return img


frames=[];durs=[]
def add(img,ms): frames.append(img); durs.append(ms)
EL=math.radians(14)
az=math.radians(20)
st=dict(theta=math.radians(90),phi=0,ket=0,react=0)
L1=[("× node",205,300,RED),("head-to-head ✓",500,300,GREEN)]
for i in range(20):
    add(render(st,math.radians(5+i*0.8),EL,"Suprafacial on both: one end fails","HOMO (bottom) meets the LUMO's lower lobes only",plane=1,labels=L1 if i>4 else None),90)
for i in range(6): add(frames[-1],120)
azb=math.radians(21)
for i in range(26):
    t=i/25
    add(render(st,azb,EL,"Your idea: reach across the nodal plane at that end","left end: bond to the TOP lobe (+), on the other side of the grey plane",plane=1,reach=ease(t),labels=[("head-to-head ✓",500,300,GREEN)]),80)
for i in range(10): add(frames[-1],120)
for i in range(30):
    t=ease(i/29); st=dict(theta=math.radians(90)*(1-t),phi=math.radians(90)*t,ket=0,react=0)
    add(render(st,azb,EL,"How it happens: the LUMO component twists","the top lobe of the left carbon swings round to face the HOMO",plane=1),80)
st=dict(theta=0,phi=math.pi/2,ket=0,react=0)
L3=[("across the plane ✓",170,250,GREEN),("head-to-head ✓",530,250,GREEN)]
for i in range(8): add(render(st,azb,EL,"Both ends now in phase: π2s + π2a","the two bonds sit on opposite sides of the LUMO's nodal plane",plane=1,labels=L3),110)
for i in range(40):
    azz=azb+math.radians(4.5*i)
    add(render(st,azz,EL,"Both ends now in phase: π2s + π2a","HOMO: same face (s) · LUMO: opposite faces (a)",plane=1),80)
for i in range(6): add(frames[-1],140)
frames[0].save("antarafacial_reach.gif",save_all=True,append_images=frames[1:],duration=durs,loop=0,optimize=True)
for k,idx in enumerate([22,45,70,90]): frames[idx].save(f"r{k}.png")
print(len(frames))
