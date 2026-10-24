import numpy as np, math
def unit(v): v=np.asarray(v,float); return v/np.linalg.norm(v)
Y=np.array([0,1.,0])
HD=2.6  # diene plane height (diene on TOP, dienophile below)
def pent(a,r=1.2,y=HD): a=math.radians(a); return np.array([r*math.cos(a),y,r*math.sin(a)])
D={'C1':pent(198),'C2':pent(126),'C3':pent(54),'C4':pent(342),'C5':pent(270)}   # C5 = CH2 (front, -z)
def dienophile(mode):
    """acrolein below the diene. mode 'endo': CHO points to the back (+z, under C2=C3); 'exo': to the front (-z, under CH2)"""
    Cb=np.array([-0.72,0.0,-0.30]); Ca=np.array([0.72,0.0,-0.30])
    s=1 if mode=='endo' else -1
    Cc=Ca+unit(np.array([-0.05,0,1.0*s]))*1.45
    O=Cc+unit(np.array([0.95,0,0.35*s]))*1.22
    Hc=Cc+unit(np.array([-0.85,0,0.55*s]))*1.0
    Ha=Ca+unit(np.array([0.55,0,-0.85*s]))*1.0
    Hb1=Cb+unit(np.array([-0.5,0,0.866]))*1.0; Hb2=Cb+unit(np.array([-0.5,0,-0.866]))*1.0
    return dict(Cb=Cb,Ca=Ca,Cc=Cc,O=O,Hc=Hc,Ha=Ha,Hb1=Hb1,Hb2=Hb2)
# frontier orbital coefficients (Hückel-type, signs chosen so primary overlaps are in phase)
cDiene={'C1':0.60,'C2':0.37,'C3':-0.37,'C4':-0.60}     # HOMO psi2
cDph={'Cb':-0.60,'Ca':0.37,'Cc':0.37,'O':-0.60}         # acrolein LUMO (psi3-like), overall sign flipped
