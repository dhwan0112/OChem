from orb import *
C=Canvas(1080,790)
C.text(24,30,"Step 2. π-MO ladders: look only at the two END lobes",size=20,anchor="start",weight="bold")
C.text(24,56,"S = ends have the same sign (on the same face);  A = ends have opposite signs.  ψ1, ψ3, ψ5 … are S;  ψ2, ψ4, ψ6 … are A.",size=13,cls="mutedt",anchor="start")
yc=420; k=150
cols=[(2,140,"ethylene (2π)",{1:"HOMO",2:"LUMO"},56),(3,360,"allyl (3 atoms)",{2:"cation: LUMO / anion: HOMO"},50),(4,600,"butadiene (4π)",{2:"HOMO",3:"LUMO"},44),(6,860,"hexatriene (6π)",{3:"HOMO",4:"LUMO"},30)]
for n,xc,name,tags,sp in cols:
    C.text(xc,96,name,size=15,weight="bold")
    for j in range(1,n+1):
        cs=huckel(n,j); y=yc+2*math.cos(j*math.pi/(n+1))*k
        x0=xc-sp*(n-1)/2
        C.line((x0-14,y),(x0+sp*(n-1)+14,y),"muted",0.8,"2,3")
        chain(C,x0,y,cs,"nu" if tags.get(j,"").startswith("HOMO") else "el" if "LUMO" in tags.get(j,"") else "ink",sp=sp,scale=0.5)
        sym="S" if cs[0]*cs[-1]>0 else "A"
        xr=x0+sp*(n-1)+22
        C.text(xr,y-7,f"ψ{j}",size=12.5,anchor="start",weight="bold")
        C.text(xr,y+9,sym,size=12.5,anchor="start",weight="bold",cls="good" if sym=="S" else "el")
        if j in tags:
            t=tags[j]; cls="nu" if t.startswith("HOMO") else "el"
            if n==3: cls="ink"
            C.text(x0-22,y,t if n!=3 else "",size=12,anchor="end",cls=cls,weight="bold")
    if n==3:
        y=yc; C.text(xc,y+34,"cation LUMO / radical SOMO / anion HOMO",size=11,cls="mutedt")
# energy axis
C.raw(f'<line class="inks" x1="40" y1="{yc+300}" x2="40" y2="{yc-300}" stroke-width="1.5" marker-end="url(#rh)"/>'); C.text(52,yc-292,"E",size=14,anchor="start",weight="bold")
C.text(24,736,"Rule of thumb: count nodes. Even number of nodes (ψ1, ψ3 …) → S; odd number (ψ2, ψ4 …) → A. The middle lobes never decide W–H; only the ends form bonds.",size=12,cls="mutedt",anchor="start")
C.text(24,758,"Hückel coefficients; lobe size ∝ |c|. Sources: CM3121 L13 p.27; L14 p.10, 23; L16 p.22–25; Clayden 2e p.886.",size=11.5,cls="mutedt",anchor="start")
save(C,"WH2_MO_ladders")
