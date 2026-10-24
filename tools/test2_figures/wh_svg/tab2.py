from glyph import *
rows=[
("Diels–Alder [4+2]",[("pi",4,"s","nus"),("pi",2,"s","els")],"π4s + π2s","1","0","1","allowed","L14 p.6"),
("[4+4] (two dienes)",[("pi",4,"s","nus"),("pi",4,"s","els")],"π4s + π4s","0","0","0","forbidden","L14 p.7"),
("alkene + alkene [2+2]",[("pi",2,"s","nus"),("pi",2,"s","els")],"π2s + π2s","2","0","2","forbidden (hν: allowed)","L14 p.24–26"),
("ketene + alkene [2+2]",[("pi",2,"s","nus"),("pi",2,"a","els")],"π2s + π2a","1","0","1","allowed","L15 p.6–8"),
("tropone + diene [6+4]",[("pi",6,"s","nus"),("pi",4,"s","els")],"π6s + π4s","1","0","1","allowed","L14 p.21"),
("allyl cation + diene [4+3]",[("pi",4,"s","nus"),("pi",3,"s","els")],"π4s + π2s","1","0","1","allowed","L14 p.22"),
("1,3-dipolar [3+2]",[("pi",3,"s","nus"),("pi",2,"s","els")],"π4s + π2s","1","0","1","allowed","L15 p.13"),
("[1,5]-H shift",[("sigma",2,"s","els"),("pi",4,"s","nus")],"σ2s + π4s","1","0","1","allowed (supra)","L16 p.21–22"),
("[1,7]-H shift",[("sigma",2,"s","els"),("pi",6,"a","nus")],"σ2s + π6a","1","0","1","allowed (antara)","L16 p.23"),
("[1,3]-H shift",[("sigma",2,"s","els"),("pi",2,"s","nus")],"σ2s + π2s","2","0","2","forbidden; π2a version: allowed but impossible","L16 p.24"),
("[3,3] Claisen / Cope",[("sigma",2,"s","els"),("pi",2,"s","nus"),("pi",2,"s","nus")],"σ2s + π2s + π2s","3","0","3","allowed (chair TS)","L16 p.6"),
("[2,3] (C⁻, S, Se)",[("omega",1,"a","els"),("sigma",2,"s","els"),("pi",2,"a","nus")],"ω2a + σ2s + π2a","1","0","1","allowed","Clayden p.918"),
("4π electrocyclic (Δ)",[("pi",4,"a","nus")],"π4a","0","1","1","allowed: conrotatory","Clayden p.922–924"),
("6π electrocyclic (Δ)",[("pi",6,"s","nus")],"π6s","1","0","1","allowed: disrotatory","Clayden p.922–924"),
]
rh=72; top=122
C=Canvas(1180,top+rh*(len(rows)+1)+60)
C.text(24,32,"Woodward–Hoffmann counting: worked examples (thermal)",size=21,anchor="start",weight="bold")
C.text(24,58,"Pictures: blue/red = components; green arrows = faces where the new bonds form (both down = s, one up + one down = a).",size=12.5,cls="mutedt",anchor="start")
C.text(24,77,"Count (4q+2)s components and (4r)a components; an odd total means thermally allowed.",size=12.5,cls="mutedt",anchor="start")
X=[24,250,520,700,790,870,940,1110]
heads=["reaction","picture","notation","(4q+2)s","(4r)a","sum","thermal verdict",""]
y=top
C.raw(f'<rect class="inks" x="16" y="{y-20}" width="1150" height="40" stroke-width="1"/>')
for x,h in zip(X,heads): C.text(x+4,y,h,size=13.5,anchor="start",weight="bold")
for i,(name,comps,nota,a,b,s,v,src) in enumerate(rows):
    y=top+(i+1)*rh
    ok = int(s)%2==1
    C.raw(f'<rect class="{"good" if ok else "el"}" x="16" y="{y-rh/2+6}" width="1150" height="{rh}" fill-opacity="0.06" stroke-width="0"/>')
    C.line((16,y+rh/2+6),(1166,y+rh/2+6),"muted",0.6)
    C.text(X[0]+4,y-7,name,size=13,anchor="start",weight="bold"); C.text(X[0]+4,y+12,src,size=11,anchor="start",cls="mutedt")
    glyph_row(C,X[1]+10,y,comps)
    C.text(X[2]+4,y,nota,size=14,anchor="start",weight="bold")
    for xx,val in ((X[3],a),(X[4],b)): C.text(xx+30,y,val,size=15,weight="bold",cls="good" if val!="0" else "mutedt")
    C.text(X[5]+18,y,s,size=16,weight="bold",cls="good" if ok else "el")
    vt=v.split("; ")
    if len(vt)==1: C.text(X[6],y,v,size=12.5,anchor="start",weight="bold",cls="good" if ok else "el")
    else:
        C.text(X[6],y-8,vt[0],size=12.5,anchor="start",weight="bold",cls="el"); C.text(X[6],y+10,vt[1],size=11,anchor="start",cls="mutedt")
C.text(24,C.H-24,"Electron counts, not atom counts: allyl cation and 1,3-dipole are 3-atom components with 2 and 4 electrons. Electrocyclic rows (L17) show a (4r)a count.",size=11.5,cls="mutedt",anchor="start")
save2(C,"WH_examples_table")
