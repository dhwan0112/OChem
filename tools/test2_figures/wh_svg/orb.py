from common import *
import math
def porb(C,x,y,c,cls,scale=1.0,minr=0.0):
    a=abs(c); ry=(9+26*a)*scale; rx=(7+5*a)*scale
    if a<0.01:
        C.raw(f'<circle class="ink" cx="{x:.1f}" cy="{y:.1f}" r="2.6"/>'); return 0
    top_fill=c>0
    for dy,filled in ((-ry,top_fill),(ry,not top_fill)):
        if filled: C.raw(f'<ellipse class="{cls}" cx="{x:.1f}" cy="{y+dy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill-opacity="0.85" stroke-width="1.5"/>')
        else: C.raw(f'<ellipse class="{cls}s" cx="{x:.1f}" cy="{y+dy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" stroke-width="1.5"/>')
    C.raw(f'<circle class="ink" cx="{x:.1f}" cy="{y:.1f}" r="2.6"/>')
    return ry
def chain(C,x0,y,cs,cls,sp=44,scale=1.0):
    xs=[x0+i*sp for i in range(len(cs))]
    C.line((xs[0],y),(xs[-1],y),"inks",1.3)
    rys=[porb(C,x,y,c,cls,scale) for x,c in zip(xs,cs)]
    return xs,rys
def link(C,p,q,ok):
    if ok: C.line(p,q,"goods",2.4,"5,4")
    else:
        C.line(p,q,"els",2.4,"2,5"); m=mid(p,q); C.text(m[0]+13,m[1],"×",size=20,cls="el")
def huckel(n,j): return [math.sqrt(2/(n+1))*math.sin(j*k*math.pi/(n+1)) for k in range(1,n+1)]
