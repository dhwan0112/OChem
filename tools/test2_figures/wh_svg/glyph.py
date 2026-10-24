from common import *
def mini_p(C,x,y,rx=4.2,ry=8.5,cls="inks"):
    C.raw(f'<ellipse class="{cls}" cx="{x:.1f}" cy="{y-ry:.1f}" rx="{rx}" ry="{ry}" stroke-width="1.3"/>')
    C.raw(f'<ellipse class="{cls}" cx="{x:.1f}" cy="{y+ry:.1f}" rx="{rx}" ry="{ry}" stroke-width="1.3"/>')
    C.raw(f'<circle class="ink" cx="{x:.1f}" cy="{y:.1f}" r="1.8"/>')
def arrow_v(C,x,y,down=True,L=13):
    y1=y+(18 if down else -18); y2=y1+(L if down else -L)
    C.raw(f'<line class="goods" x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{y2:.1f}" stroke-width="2.2" marker-end="url(#gh)"/>')
def comp_glyph(C,x,y,kind,n,face,cls="nus",sp=15):
    """draw a component; returns width"""
    if kind=="pi":
        xs=[x+i*sp for i in range(n)]
        C.line((xs[0],y),(xs[-1],y),"inks",1.2)
        for xx in xs: mini_p(C,xx,y,cls=cls)
        arrow_v(C,xs[0],y,True); arrow_v(C,xs[-1],y,face=="s")
        return sp*(n-1)
    if kind=="sigma":
        C.line((x,y),(x+20,y),"inks",2.2)
        C.raw(f'<circle class="ink" cx="{x}" cy="{y}" r="3"/>'); C.raw(f'<circle class="{cls}" cx="{x+20}" cy="{y}" r="6" stroke-width="1.4"/>')
        C.text(x+20,y,"H",size=7.5,cls="ink")
        arrow_v(C,x,y-8,True); arrow_v(C,x+20,y-8,face=="s")
        return 20
    if kind=="omega":
        mini_p(C,x,y,cls=cls)
        if face=="s":
            C.raw(f'<line class="goods" x1="{x-3:.1f}" y1="{y+17:.1f}" x2="{x-8:.1f}" y2="{y+30:.1f}" stroke-width="2.2" marker-end="url(#gh)"/>')
            C.raw(f'<line class="goods" x1="{x+3:.1f}" y1="{y+17:.1f}" x2="{x+8:.1f}" y2="{y+30:.1f}" stroke-width="2.2" marker-end="url(#gh)"/>')
        else: arrow_v(C,x,y,True); arrow_v(C,x,y,False)
        return 0
def glyph_row(C,x,y,comps):
    cx=x
    for i,(kind,n,face,cls) in enumerate(comps):
        if i: C.text(cx+10,y,"+",size=14); cx+=22
        w=comp_glyph(C,cx,y,kind,n,face,cls); cx+=w+12
    return cx
GH='<marker id="gh" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="good" d="M0,0 L10,5 L0,10 z"/></marker>'
def save2(c,name):
    import cairosvg
    for mono in (False,True):
        sv=c.svg(mono).replace("</defs>",GH+"</defs>")
        fn=f"{name}{'_bw' if mono else ''}.svg"; open(fn,"w").write(sv)
        cairosvg.svg2png(url=fn,write_to=fn.replace('.svg','.png'),output_width=int(c.W*1.4))
