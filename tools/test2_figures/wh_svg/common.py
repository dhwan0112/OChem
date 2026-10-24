import math, re
FONT="DejaVu Sans, Helvetica, Arial, sans-serif"
STYLE_COLOR='''
.ink{stroke:#1b1b1f;fill:#1b1b1f}.inks{stroke:#1b1b1f;fill:none}
.nu{stroke:#1d4ed8;fill:#1d4ed8}.nus{stroke:#1d4ed8;fill:none}
.el{stroke:#b91c1c;fill:#b91c1c}.els{stroke:#b91c1c;fill:none}
.arr{stroke:#c2410c;fill:none}.arrh{fill:#c2410c;stroke:none}
.good{stroke:#15803d;fill:#15803d}.goods{stroke:#15803d;fill:none}
.muted{fill:#6b7280;stroke:#6b7280}.mutedt{fill:#6b7280;stroke:none}
.bg{fill:#ffffff}.monoonly{display:none}
text{stroke:none}
@media (prefers-color-scheme: dark){
.ink{stroke:#e6e6ea;fill:#e6e6ea}.inks{stroke:#e6e6ea}
.nu{stroke:#8ab4ff;fill:#8ab4ff}.nus{stroke:#8ab4ff}
.el{stroke:#ff8a8a;fill:#ff8a8a}.els{stroke:#ff8a8a}
.arr{stroke:#ff9f5a}.arrh{fill:#ff9f5a}
.good{stroke:#4ade80;fill:#4ade80}.goods{stroke:#4ade80}
.muted{fill:#a1a1aa;stroke:#a1a1aa}.mutedt{fill:#a1a1aa}
.bg{fill:#1e1e1e}}
text.ink,text.nu,text.el,text.good,text.muted,text.mutedt,text.inks{stroke:none}
'''
STYLE_MONO='''
.ink,.nu,.el,.good{stroke:#000;fill:#000}.inks,.nus,.els,.goods,.arr{stroke:#000;fill:none}
.arrh{fill:#000;stroke:none}.muted{fill:#444;stroke:#444}.mutedt{fill:#444;stroke:none}.bg{fill:#fff}.coloronly{display:none}
text{stroke:none}
text.ink,text.nu,text.el,text.good,text.muted,text.mutedt,text.inks{stroke:none}
'''
class Canvas:
    def __init__(s,W,H): s.W,s.H=W,H; s.e=[]
    def line(s,p,q,cls="inks",w=1.9,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        s.e.append(f'<line class="{cls}" x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke-width="{w}" stroke-linecap="round"{d}/>')
    def text(s,x,y,t,size=14,cls="ink",anchor="middle",weight="normal",style="normal"):
        if "<tspan" in t and anchor=="middle":
            plain=re.sub(r"<[^>]+>","",t); w=sum(size*(0.33 if ch in " .,()[]" else 0.66 if ch.isupper() else 0.55) for ch in plain)
            x-=w/2; anchor="start"
        s.e.append(f'<text class="{cls}" x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" text-anchor="{anchor}" dominant-baseline="central" font-weight="{weight}" font-style="{style}">{t}</text>')
    def bond(s,p,q,cls="inks",order=1,inner=None,trim=(0,0),dash=None,w=1.9):
        d=math.hypot(q[0]-p[0],q[1]-p[1]); ux,uy=(q[0]-p[0])/d,(q[1]-p[1])/d; nx,ny=-uy,ux
        p=(p[0]+ux*trim[0],p[1]+uy*trim[0]); q=(q[0]-ux*trim[1],q[1]-uy*trim[1])
        if order==1: s.line(p,q,cls,w,dash); return
        if inner:
            s.line(p,q,cls,w,dash); mx,my=(p[0]+q[0])/2,(p[1]+q[1])/2
            if (inner[0]-mx)*nx+(inner[1]-my)*ny<0: nx,ny=-nx,-ny
            s.line((p[0]+nx*6+ux*6,p[1]+ny*6+uy*6),(q[0]+nx*6-ux*6,q[1]+ny*6-uy*6),cls,w,dash)
        else:
            for t in (-3,3): s.line((p[0]+nx*t,p[1]+ny*t),(q[0]+nx*t,q[1]+ny*t),cls,w,dash)
    def carrow(s,p,q,bend=0.4):
        (x1,y1),(x2,y2)=p,q; mx,my=(x1+x2)/2,(y1+y2)/2; d=math.hypot(x2-x1,y2-y1)
        nx,ny=-(y2-y1)/d,(x2-x1)/d; cx,cy=mx+nx*d*bend,my+ny*d*bend
        s.e.append(f'<path class="arr" d="M{x1:.1f},{y1:.1f} Q{cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}" stroke-width="1.8" marker-end="url(#ah)"/>')
    def rarrow(s,p,q):
        s.e.append(f'<line class="inks" x1="{p[0]}" y1="{p[1]}" x2="{q[0]}" y2="{q[1]}" stroke-width="2" marker-end="url(#rh)"/>')
    def raw(s,x): s.e.append(x)
    def svg(s,mono=False):
        st=STYLE_MONO if mono else STYLE_COLOR
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s.W} {s.H}" width="{s.W}" height="{s.H}">
<style>{st}</style>
<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="arrh" d="M0,0 L10,5 L0,10 z"/></marker>
<marker id="rh" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path class="ink" d="M0,0 L10,5 L0,10 z"/></marker>
</defs>
<rect class="bg" width="{s.W}" height="{s.H}" rx="14"/>
{"".join(s.e)}
</svg>'''
def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)),c[1]+r*math.sin(math.radians(a)))
def mid(a,b,dx=0,dy=0): return ((a[0]+b[0])/2+dx,(a[1]+b[1])/2+dy)
def save(c,name):
    import cairosvg
    for mono in (False,True):
        fn=f"{name}{'_bw' if mono else ''}.svg"; open(fn,"w").write(c.svg(mono))
        cairosvg.svg2png(url=fn,write_to=fn.replace('.svg','.png'),output_width=int(c.W*1.4))
