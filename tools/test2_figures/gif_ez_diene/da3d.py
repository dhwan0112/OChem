import numpy as np, math
from PIL import Image, ImageDraw, ImageFont
W,H=720,540; SS=2  # supersample
F=lambda s,b=False: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf"%("-Bold" if b else ""), s*SS)
# coordinates: x = left-right (u), y = up, z = depth (v: +z = back)
def P(u,y,v): return np.array([u,y,v],float)
R6=1.40
ang={ 'C1':180,'C2':120,'C3':60,'C4':0,'C5':-60,'C6':-120 }
def ring(name,y=0.0): a=math.radians(ang[name]); return P(R6*math.cos(a),y,R6*math.sin(a))
UP=np.array([0,1.0,0])
def unit(v): return v/np.linalg.norm(v)
# ----- reactant geometry -----
C={k:ring(k) for k in ['C1','C2','C3','C4']}
def sp2_dirs(c,n):  # two in-plane substituent dirs at 120° from bond c->n (in xz plane)
    d=unit(n-c); a=math.atan2(d[2],d[0])
    return [np.array([math.cos(a+s*2*math.pi/3),0,math.sin(a+s*2*math.pi/3)]) for s in (1,-1)]
def classify(c,n):
    ds=sp2_dirs(c,n); center=np.zeros(3)
    # inside = the one pointing more toward the ring centre / other terminus (toward -z front region)
    ds.sort(key=lambda d: np.dot(d,unit(center-c)))
    return ds[1],ds[0]  # inside, outside
in1,out1=classify(C['C1'],C['C2']); in4,out4=classify(C['C4'],C['C3'])
# product directions at sp3 termini: outward bisector +/- up
def sp3_dirs(c):
    b=unit(np.array([c[0],0,c[2]])); th=math.radians(52)
    return b*math.cos(th)+UP*math.sin(th), b*math.cos(th)-UP*math.sin(th)
up1,dn1=sp3_dirs(C['C1']); up4,dn4=sp3_dirs(C['C4'])
LR,LH,LE=1.45,1.0,1.5
dien_y0=-2.7
atoms={}  # name: (start,end,radius,color,label)
def add(n,s,e,r,col,lab=None): atoms[n]=(np.array(s,float),np.array(e,float),r,col,lab)
GR=(70,70,78); HC=(245,245,245); RBLUE=(29,78,216); RRED=(214,40,40); EST=(13,148,136)
for k in ['C1','C2','C3','C4']: add(k,C[k],C[k],0.30,GR)
# H on C2, C3 (in plane, outward)
for k in ['C2','C3']:
    d=unit(np.array([C[k][0],0,C[k][2]])); add('H'+k[1],C[k]+d*LH,C[k]+d*LH,0.20,HC,'H')
# C1: R outside (E), H inside ; C4: R inside (Z), H outside
add('R1',C['C1']+out1*LR,C['C1']+dn1*LR,0.36,RBLUE,'R')
add('H1',C['C1']+in1*LH,C['C1']+up1*LH,0.20,HC,'H')
add('R4',C['C4']+in4*LR,C['C4']+up4*LR,0.36,RRED,'R')
add('H4',C['C4']+out4*LH,C['C4']+dn4*LH,0.20,HC,'H')
# dienophile DMAD
C6e=ring('C6'); C5e=ring('C5')
C6s=P(-0.62,dien_y0,-0.55); C5s=P(0.62,dien_y0,-0.55)
add('C6',C6s,C6e,0.30,GR); add('C5',C5s,C5e,0.30,GR)
add('E6',C6s+np.array([-LE,0,0]),C6e+unit(np.array([C6e[0],0,C6e[2]]))*LE,0.34,EST,'E')
add('E5',C5s+np.array([LE,0,0]),C5e+unit(np.array([C5e[0],0,C5e[2]]))*LE,0.34,EST,'E')
bonds=[('C1','C2',(2,1)),('C2','C3',(1,2)),('C3','C4',(2,1)),('C5','C6',(3,2)),('C1','C6',(0,1)),('C4','C5',(0,1)),
       ('C2','H2',(1,1)),('C3','H3',(1,1)),('C1','R1',(1,1)),('C1','H1',(1,1)),('C4','R4',(1,1)),('C4','H4',(1,1)),('C6','E6',(1,1)),('C5','E5',(1,1))]
NEW={('C1','C6'),('C4','C5')}
def ease(t): return t*t*(3-2*t)
def pos(n,t):
    s,e,_,_,_=atoms[n]
    if n in ('R1','H1','R4','H4'):  # rotate substituent around carbon (keep length)
        c=C['C1'] if n[1]=='1' else C['C4']; ds=unit(s-c); de=unit(e-c); L=np.linalg.norm(s-c)
        d=unit(ds*(1-t)+de*t) if np.linalg.norm(ds*(1-t)+de*t)>1e-6 else de
        return c+d*L
    if n in ('E6','E5'):
        c=pos('C6' if n=='E6' else 'C5',t); ds=unit(s-atoms['C6' if n=='E6' else 'C5'][0]); de=unit(e-atoms['C6' if n=='E6' else 'C5'][1])
        return c+unit(ds*(1-t)+de*t)*LE
    return s*(1-t)+e*t
def project(p,az,el,scale=74,dist=14):
    ca,sa=math.cos(az),math.sin(az); x=p[0]*ca+p[2]*sa; z=-p[0]*sa+p[2]*ca
    ce,se=math.cos(el),math.sin(el); y=p[1]*ce+z*se; z2=-p[1]*se+z*ce
    f=dist/(dist+z2)
    return (W/2+x*scale*f)*SS,(H*0.47-y*scale*f)*SS,z2,f
def shade(col,k):
    return tuple(int(min(255,c*k)) for c in col)
def draw_atom(d,x,y,r,col,lab):
    for i in range(6,0,-1):
        rr=r*i/6; k=0.75+0.45*(1-i/6)
        off=(1-i/6)*r*0.35
        d.ellipse([x-rr-off,y-rr-off,x+rr-off,y+rr-off],fill=shade(col,k))
    d.ellipse([x-r,y-r,x+r,y+r],outline=(30,30,30),width=2*SS) if col==HC else None
    if lab:
        f=F(int(r/SS*0.9) if lab!='H' else int(r/SS*0.85),True)
        tc=(30,30,30) if col==HC else (255,255,255)
        d.text((x,y),lab,font=f,fill=tc,anchor="mm")
def draw_bond(d,p,q,order,partial,col=(60,60,66)):
    (x1,y1),(x2,y2)=p,q; dx,dy=x2-x1,y2-y1; L=math.hypot(dx,dy)+1e-9; nx,ny=-dy/L,dx/L
    w=int(5*SS)
    if partial:
        n=12
        for i in range(n):
            if i%2: continue
            a,b=i/n,(i+1)/n
            d.line([(x1+dx*a,y1+dy*a),(x1+dx*b,y1+dy*b)],fill=(21,128,61),width=w)
        return
    offs={1:[0],2:[-1,1],3:[-1.6,0,1.6]}[order]
    for o in offs:
        oo=o*4.2*SS
        d.line([(x1+nx*oo,y1+ny*oo),(x2+nx*oo,y2+ny*oo)],fill=col,width=w if order==1 else int(3.6*SS))
def render(t,az,el,caption,sub,plane_alpha=0.0,show_labels=False,annot=0.0):
    img=Image.new("RGB",(W*SS,H*SS),(255,255,255)); d=ImageDraw.Draw(img,"RGBA")
    P2={n:project(pos(n,t),az,el) for n in atoms}
    prims=[]
    for a,b,(o0,o1) in bonds:
        if (a,b) in NEW:
            if t<0.08: continue
            partial = t<0.85; order=1; col=(21,128,61)
        else:
            order = o0 if t<0.5 else o1; partial=False; col=(60,60,66)
        za=(P2[a][2]+P2[b][2])/2
        prims.append((za+0.01,'b',(a,b,order,partial,col)))
    for n,(s,e,r,colr,lab) in atoms.items():
        prims.append((P2[n][2]-0.02,'a',n))
    # plane layering: items below plane drawn first
    ypos={n:pos(n,t)[1] for n in atoms}
    def is_below(pr):
        if pr[1]=='a': return ypos[pr[2]]<-0.05
        a,b=pr[2][0],pr[2][1]; return (ypos[a]+ypos[b])/2<-0.05
    layers=[[p for p in prims if is_below(p)],[p for p in prims if not is_below(p)]] if plane_alpha>0 else [prims]
    for li,layer in enumerate(layers):
        if plane_alpha>0 and li==1:
            # translucent ring plane
            pts=[project(ring(k)*1.0*np.array([1.55,1,1.55]),az,el) for k in ['C1','C2','C3','C4','C5','C6']]
            d.polygon([(p[0],p[1]) for p in pts],fill=(148,163,184,int(150*plane_alpha)),outline=(100,116,139,int(255*plane_alpha)))
        for pr in sorted(layer,key=lambda z:-z[0]):
            if pr[1]=='b':
                a,b,order,partial,col=pr[2]; draw_bond(d,P2[a][:2],P2[b][:2],order,partial,col)
            else:
                n=pr[2]; s,e,r,colr,lab=atoms[n]; f=P2[n][3]
                draw_atom(d,P2[n][0],P2[n][1],r*74*f*SS,colr,lab)
    img=img.resize((W,H),Image.LANCZOS); d=ImageDraw.Draw(img)
    fb=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",19)
    fr=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",15)
    d.text((W/2,26),caption,font=fb,fill=(20,20,24),anchor="mm")
    d.text((W/2,52),sub,font=fr,fill=(90,90,100),anchor="mm")
    # legend
    if annot>0:
        fa=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",15)
        for n,txt,colr in [('R1','outside (E)',RBLUE),('R4','inside (Z)',RRED)]:
            x,y=P2[n][0]/SS,P2[n][1]/SS
            d.text((x,y-30),txt,font=fa,fill=colr,anchor="mm")
    lx,ly=18,H-58
    for i,(colr,txt) in enumerate([(RBLUE,"R on C1: outside (E)"),(RRED,"R on C4: inside (Z)"),(EST,"E = CO2Me (DMAD)"),((21,128,61),"new σ bond")]):
        x=lx+i*176
        d.ellipse([x,ly-7,x+14,ly+7],fill=colr); d.text((x+20,ly),txt,font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",13),fill=(40,40,48),anchor="lm")
    d.text((W/2,H-22),"Concerted, suprafacial: inside groups rotate up, outside groups rotate down (Clayden 2e p.885–886)",font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",12),fill=(110,110,120),anchor="mm")
    return img
frames=[];durs=[]
EL=math.radians(16)
# phase 1: reactants viewed from above-ish
for i in range(26):
    az=math.radians(-20+i*1.6)
    frames.append(render(0,az,math.radians(48),"(E,Z)-diene + DMAD (s-cis diene seen from above)","blue R points OUTSIDE (E), red R points INSIDE (Z); DMAD waits underneath",annot=1)); durs.append(90)
for i in range(6): frames.append(frames[-1]); durs.append(110)
# tilt camera down to side view
az0=math.radians(20)
for i in range(12):
    e=math.radians(48-36*ease(i/11))
    frames.append(render(0,az0,e,"Tilt to a side view","the diene plane is horizontal; DMAD approaches from below",annot=1)); durs.append(80)
# phase 2: reaction
for i in range(40):
    t=ease(i/39)
    frames.append(render(t,az0,math.radians(12),"Both new σ bonds form on the bottom face","termini rotate: inside R swings UP, outside R swings DOWN",annot=max(0,1-3*t))); durs.append(80)
for i in range(6): frames.append(frames[-1]); durs.append(120)
# phase 3
for i in range(10):
    frames.append(render(1,az0,math.radians(12),"Product: the two R groups are on opposite faces → trans","grey plane = the new six-membered ring",plane_alpha=(i+1)/10)); durs.append(80)
for i in range(60):
    az=az0+math.radians(6*i)
    frames.append(render(1,az,math.radians(14),"Product: the two R groups are on opposite faces → trans","red R (was inside) above the ring, blue R (was outside) below",plane_alpha=1)); durs.append(70)
for i in range(8): frames.append(frames[-1]); durs.append(150)
frames[0].save("EZ_diene_DA_3D.gif",save_all=True,append_images=frames[1:],duration=durs,loop=0,optimize=True)
for k,idx in enumerate([0,40,75,120]): frames[idx].save(f"check_{k}.png")
print(len(frames))
