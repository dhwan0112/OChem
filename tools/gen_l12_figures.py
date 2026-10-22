#!/usr/bin/env python3
"""L12 그림 생성기 (2026-10-21): practice 공식 풀이(Q1–Q3) 메커니즘·생성물과,
슬라이드에는 있으나 통독본에 없던 반응(p.3 PhMgBr 직접 첨가, p.3 impossible Grignard,
p.8 chloroformate carbamate 형성, p.9 peptide coupling)과 THP 보호(보충, Clayden p.550–551).
출력: figures/L12/*.json → RESHIKI=... python3 tools/chemfig.py figures/L12/prac_*.json ...
좌표: 결합 길이 1, x 오른쪽, y 아래. 각도는 수학 좌표(90 위, 0 오른쪽).
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures/L12"


def P(x, y, ang, d=1.0):
    r = math.radians(ang)
    return (x + d * math.cos(r), y - d * math.sin(r))


class Fig:
    def __init__(self, title):
        self.s = dict(title=title, atoms=[], bonds=[], abbrev=[], lone_pairs=[], curved=[], arrows=[], captions=[])

    def atom(self, el, x, y, charge=0, h=0, color=None, label=None):
        a = [el, round(x, 4), round(y, 4), charge, h]
        if color:
            a.append(color)
        self.s["atoms"].append(a)
        i = len(self.s["atoms"]) - 1
        if label:
            self.s["abbrev"].append([label, i, [i]])
        return i

    def bond(self, a, b, order=1, disp="plain", color=None):
        e = [a, b, order, disp]
        if color:
            e.append(color)
        self.s["bonds"].append(e)

    def pos(self, i):
        return tuple(self.s["atoms"][i][1:3])

    def sub(self, parent, ang, el="C", d=1.0, charge=0, h=0, color=None, label=None, order=1, disp="plain", bcolor=None):
        x, y = P(*self.pos(parent), ang, d)
        i = self.atom(el, x, y, charge, h, color, label)
        self.bond(parent, i, order, disp, bcolor)
        return i

    def H(self, parent, ang, color=None, bcolor=None):
        return self.sub(parent, ang, "H", color=color, bcolor=bcolor)

    def ring(self, n, cx, cy, start, orders=None, els=None):
        """정 n각형. 꼭짓점 k는 각도 start + k*360/n (반시계). 결합 k는 꼭짓점 k–k+1."""
        R = 1 / (2 * math.sin(math.pi / n))
        idx = []
        for k in range(n):
            x, y = P(cx, cy, start + k * 360 / n, R)
            el = (els or {}).get(k, "C")
            idx.append(self.atom(el, x, y))
        for k in range(n):
            self.bond(idx[k], idx[(k + 1) % n], orders[k] if orders else 1)
        return idx

    def cap(self, text, x, y, color="muted", size=None):
        c = [text, round(x, 3), round(y, 3), color]
        if size:
            c.append(size)
        self.s["captions"].append(c)

    def arrow(self, x1, y1, x2, y2, kind="forward"):
        self.s["arrows"].append([x1, y1, x2, y2, kind])

    def lp(self, i, ang, pad=None):
        self.s["lone_pairs"].append([i, ang] + ([pad] if pad is not None else []))

    def curved(self, frm, to, bend=0.5):
        self.s["curved"].append({"from": frm, "to": to, "bend": bend})

    def save(self, name):
        (OUT / f"{name}.json").write_text(json.dumps(self.s, ensure_ascii=False, indent=1) + "\n")
        print(OUT / f"{name}.json")


# ---------------- 공통 조각 ----------------

def dione_ring(f, cx, cy):
    """2-methylcyclohexane-1,3-dione 고리(pointy-top). 반환: dict(C1..C6, O1, O3)."""
    k = f.ring(6, cx, cy, 90)  # k0 top(90), k1 150, k2 210, k3 270, k4 330, k5 30
    C6, C5, C4, C3, C2, C1 = k
    O1 = f.sub(C1, 30, "O", order=2)
    O3 = f.sub(C3, 270, "O", order=2)
    return dict(C1=C1, C2=C2, C3=C3, C4=C4, C5=C5, C6=C6, O1=O1, O3=O3)


def heptenone(f, cx, cy, enolate=False, methyl=False):
    """cyclohept-2-en-1-one (또는 3-methyl enolate). start 90: k0=C1(top), k6=C2, k5=C3."""
    orders = [1] * 7
    if enolate:
        orders[6] = 2  # C1=C2
    else:
        orders[5] = 2  # C2=C3
    k = f.ring(7, cx, cy, 90, orders)
    C1, C2, C3, C4 = k[0], k[6], k[5], k[4]
    O = f.sub(C1, 90, "O", charge=-1 if enolate else 0, order=1 if enolate else 2,
              color="nu" if enolate else None)
    return dict(C1=C1, C2=C2, C3=C3, C4=C4, O=O, ring=k)


def amino_acid(f, X, Y, kind, nprot=None, cprot="OH", ncolor=None, ccolor=None):
    """Cα (X,Y); CO 오른쪽 위(30°), N 아래(270°). kind: 'Phe'(N wedge) | 'Ala'(CH3 wedge)."""
    Ca = f.atom("C", X, Y)
    Cco = f.sub(Ca, 30, color=ccolor)
    O = f.sub(Cco, 90, "O", order=2)
    if cprot == "OH":
        OX = f.sub(Cco, 330, "O", h=1)
    else:
        OX = f.sub(Cco, 330, "O", label=cprot)
    if kind == "Phe":
        N = f.sub(Ca, 270, "N", h=1 if nprot else 2, disp="wedge", color=ncolor)
        CH2 = f.sub(Ca, 150)
        f.sub(CH2, 90, label="Ph")
    else:
        N = f.sub(Ca, 270, "N", h=1 if nprot else 2, color=ncolor)
        f.sub(Ca, 150, disp="wedge")
    if nprot == "Boc":
        boc(f, N)
    return dict(Ca=Ca, Cco=Cco, O=O, OX=OX, N=N)


def boc(f, N, color=None):
    Cb = f.sub(N, 210, color=color, bcolor=color)
    f.sub(Cb, 270, "O", order=2)
    Ob = f.sub(Cb, 150, "O")
    f.sub(Ob, 210, label="tBu")
    return Cb


def dipeptide(f, X, Y, nprot=None, cprot="OH", ncolor=None, amide_color=None):
    """Phe–Ala. Phe Cα (X,Y); amide N at (X+1.732, Y); Ala Cα (X+2.598, Y-0.5)."""
    Ca = f.atom("C", X, Y)
    Cco = f.sub(Ca, 30)
    f.sub(Cco, 90, "O", order=2)
    Nam = f.sub(Cco, 330, "N", h=1, color=amide_color, bcolor=amide_color)
    N = f.sub(Ca, 270, "N", h=1 if nprot else 2, disp="wedge", color=ncolor)
    CH2 = f.sub(Ca, 150)
    f.sub(CH2, 90, label="Ph")
    CaA = f.sub(Nam, 30)
    f.sub(CaA, 90, disp="wedge")
    CcoA = f.sub(CaA, 330)
    f.sub(CcoA, 270, "O", order=2)
    if cprot == "OH":
        OX = f.sub(CcoA, 30, "O", h=1)
    else:
        OX = f.sub(CcoA, 30, "O", label=cprot)
    if nprot == "Boc":
        boc(f, N, color=ncolor)
    return dict(Ca=Ca, Cco=Cco, Nam=Nam, N=N, CaA=CaA, CcoA=CcoA, OX=OX)


def piperidine(f, N, ang_center):
    """N을 꼭짓점으로 하는 piperidine 고리. ang_center: N에서 고리 중심 방향."""
    cx, cy = P(*f.pos(N), ang_center, 1.0)
    pts = []
    for k in range(1, 6):
        x, y = P(cx, cy, ang_center + 180 + k * 60, 1.0)
        pts.append(f.atom("C", x, y))
    chain = [N] + pts + [N]
    for a, b in zip(chain, chain[1:]):
        f.bond(a, b)
    return pts


# ---------------- Practice Q1 ----------------

def q1_michael():
    f = Fig("Practice Q1 (1/3): 2-methylcyclohexane-1,3-dione enolate + MVK → Michael adduct (A) (L12_Practice_solutions p.1)")
    r = dione_ring(f, 0, 0)
    f.sub(r["C2"], 300, label="CH3")
    f.s["atoms"][r["C2"]][3] = -1
    f.s["atoms"][r["C2"]].append("nu")
    f.lp(r["C2"], 0)
    # MVK
    Cb = f.atom("C", 3.6, 0.5, color="el")
    f.H(Cb, 90)
    f.H(Cb, 210)
    Ca = f.sub(Cb, 330, order=2)
    f.H(Ca, 90)
    Cc = f.sub(Ca, 30)
    O = f.sub(Cc, 270, "O", order=2)
    f.sub(Cc, 30, label="CH3")
    f.curved({"lp": [r["C2"], 0]}, {"atom": Cb, "gap": 6, "dir": 180}, bend=0.35)
    f.curved({"bond": [Cb, Ca]}, {"bond": [Ca, Cc], "gap": 2}, bend=-0.8)
    f.curved({"bond": [Cc, O]}, {"atom": O, "gap": 3, "dir": 0}, bend=-0.9)
    f.cap("enolate (C2 carbanion)", -1.9, 2.5)
    f.cap("MVK", 3.9, 2.0)
    f.arrow(7.7, 0.3, 9.7, 0.3)
    f.cap("10% NaOH", 7.3, -0.75, "ink")
    f.cap("then H2O", 7.5, 0.45)
    # product (A)
    X = 12.1
    p = dione_ring(f, X, 0)
    f.sub(p["C2"], 300, label="CH3")
    Ca2 = f.sub(p["C2"], 0, bcolor="good")
    Cb2 = f.sub(Ca2, 60)
    Cc2 = f.sub(Cb2, 0)
    f.sub(Cc2, 60, "O", order=2)
    f.sub(Cc2, 300, label="CH3")
    f.cap("(A) 1,5-dicarbonyl", X - 1.6, 2.6)
    f.save("prac_q1_michael")


def q1_enamine_cyclization():
    f = Fig("Practice Q1 (2/3): piperidine enamine of (A) attacks the ring ketone (intramolecular aldol-type) (L12_Practice_solutions p.1)")
    r = dione_ring(f, 0, 0)
    f.s["atoms"][r["C3"]].append("el")
    f.sub(r["C2"], 300, label="CH3")
    Ca = f.sub(r["C2"], 0)
    Cb = f.sub(Ca, 300)
    Cc = f.sub(Cb, 300)
    Cd = f.sub(Cc, 240, order=2, label="H2C", color="nu", bcolor="nu")
    N = f.sub(Cc, 0, "N", color="nu")
    piperidine(f, N, 0)
    f.lp(N, 90)
    f.curved({"bond": [Cc, Cd]}, {"atom": r["C3"], "gap": 6, "dir": 330}, bend=0.35)
    f.curved({"bond": [r["C3"], r["O3"]]}, {"atom": r["O3"], "gap": 3, "dir": 180}, bend=-0.9)
    Ccx, Ccy = f.pos(Cc)
    f.curved({"lp": [N, 90]}, {"pt": [Ccx + 0.4, Ccy - 0.5]}, bend=-0.5)
    f.cap("enamine of (A) (from piperidine, – H2O)", -1.9, 3.8, size=7)
    f.arrow(6.7, 0.8, 8.1, 0.8)
    # product: bicyclic hydroxy iminium
    X = 10.6
    p = dione_ring(f, X, 0)
    # remove O3 (C3 now bears OH): rebuild ring B manually
    f.s["atoms"][p["O3"]][0] = "O"
    f.s["atoms"][p["O3"]][4] = 1  # OH
    # move OH to 210 direction
    ox, oy = P(*f.pos(p["C3"]), 210)
    f.s["atoms"][p["O3"]][1:3] = [round(ox, 4), round(oy, 4)]
    for b in f.s["bonds"]:
        if {b[0], b[1]} == {p["C3"], p["O3"]}:
            b[2] = 1
    f.sub(p["C2"], 30, label="CH3")
    bx, by = f.pos(p["C2"])
    cx, cy = bx, by + 1.0  # ring B center (0.866, 1.5) relative
    Ca2 = f.atom("C", *P(cx, cy, 30))
    Cb2 = f.atom("C", *P(cx, cy, 330))
    Cc2 = f.atom("C", *P(cx, cy, 270))
    Cd2 = f.atom("C", *P(cx, cy, 210))
    f.bond(p["C2"], Ca2)
    f.bond(Ca2, Cb2)
    f.bond(Cb2, Cc2)
    f.bond(Cc2, Cd2)
    f.bond(Cd2, p["C3"], color="good")
    N2 = f.sub(Cc2, 270, "N", charge=1, order=2, color="nu")
    piperidine(f, N2, 270)
    f.cap("bicyclic iminium (after proton transfer, O⁻ → OH)", X - 2.6, -2.3, size=7)
    f.save("prac_q1_enamine_cyclization")


def wmk(f, X, Y):
    """Wieland–Miescher ketone (B)."""
    p = dione_ring(f, X, Y)
    # C3=O3 → C3=Cd; remove O3 by turning it into Cd position? simpler: rebuild
    f.s["atoms"].pop(p["O3"])
    f.s["bonds"] = [b for b in f.s["bonds"] if p["O3"] not in b[:2]]
    f.sub(p["C2"], 30, label="CH3")
    bx, by = f.pos(p["C2"])
    cx, cy = bx, by + 1.0
    Ca2 = f.atom("C", *P(cx, cy, 30))
    Cb2 = f.atom("C", *P(cx, cy, 330))
    Cc2 = f.atom("C", *P(cx, cy, 270))
    Cd2 = f.atom("C", *P(cx, cy, 210))
    f.bond(p["C2"], Ca2)
    f.bond(Ca2, Cb2)
    f.bond(Cb2, Cc2)
    f.bond(Cc2, Cd2)
    f.bond(Cd2, p["C3"], 2, color="good")
    f.sub(Cc2, 270, "O", order=2)
    return p


def q1_dehydration():
    f = Fig("Practice Q1 (3/3): dehydration and piperidine release give the Wieland–Miescher ketone (B) (L12_Practice_solutions p.1)")
    p = dione_ring(f, 0, 0)
    f.s["atoms"][p["O3"]][4] = 1
    ox, oy = P(*f.pos(p["C3"]), 210)
    f.s["atoms"][p["O3"]][1:3] = [round(ox, 4), round(oy, 4)]
    f.s["atoms"][p["O3"]].append("el")
    for b in f.s["bonds"]:
        if {b[0], b[1]} == {p["C3"], p["O3"]}:
            b[2] = 1
            b.append("el")
    f.sub(p["C2"], 30, label="CH3")
    bx, by = f.pos(p["C2"])
    cx, cy = bx, by + 1.0
    Ca2 = f.atom("C", *P(cx, cy, 30))
    Cb2 = f.atom("C", *P(cx, cy, 330))
    Cc2 = f.atom("C", *P(cx, cy, 270))
    Cd2 = f.atom("C", *P(cx, cy, 210))
    f.bond(p["C2"], Ca2)
    f.bond(Ca2, Cb2)
    f.bond(Cb2, Cc2)
    f.bond(Cc2, Cd2)
    f.bond(Cd2, p["C3"])
    f.H(Cd2, 210, color="el", bcolor="el")
    N2 = f.sub(Cc2, 270, "N", charge=1, order=2)
    piperidine(f, N2, 270)
    f.arrow(4.4, 1.0, 6.2, 1.0)
    f.cap("heat, – H2O", 4.1, 0.0, "ink")
    f.cap("then H2O", 4.55, 1.15)
    X = 9.0
    wmk(f, X, 0)
    f.cap("+", X + 2.4, 1.1, "ink", 10)
    # piperidine
    N3 = f.atom("N", X + 4.4, 0.6, h=1)
    piperidine(f, N3, 270)
    f.cap("(B) Wieland–Miescher ketone", X - 1.9, 4.6)
    f.cap("piperidine", X + 3.5, -1.9)
    f.save("prac_q1_dehydration")


# ---------------- Practice Q2 ----------------

def enolate_A(f, X, Y):
    e = heptenone(f, X, Y, enolate=True)
    f.H(e["C2"], 38.6)
    f.sub(e["C3"], 317, label="CH3")
    f.H(e["C3"], 17)
    for b in f.s["bonds"]:
        if {b[0], b[1]} == {e["C1"], e["C2"]}:
            b.append("good")
    return e


def q2_cuprate():
    f = Fig("Practice Q2 (1/2): MeLi/CuCl (cat.) — conjugate addition of 'MeCu' to cyclohept-2-en-1-one gives the enolate (A) (L12_Practice_solutions p.2)")
    e = heptenone(f, 0, 0)
    f.H(e["C2"], 38.6)
    f.H(e["C3"], 347)
    f.s["atoms"][e["C3"]].append("el")
    Me = f.atom("C", 2.0, 1.7, color="nu", label="H3C")
    Cu = f.sub(Me, 0, "Cu", bcolor="nu")
    f.curved({"bond": [Me, Cu]}, {"atom": e["C3"], "gap": 6, "dir": 260}, bend=0.3)
    f.curved({"bond": [e["C2"], e["C3"]]}, {"bond": [e["C1"], e["C2"]], "gap": 2}, bend=0.8)
    f.curved({"bond": [e["C1"], e["O"]]}, {"atom": e["O"], "gap": 3, "dir": 180}, bend=0.9)
    f.cap("'MeCu' (soft)", 1.3, 2.4, size=7)
    f.arrow(4.9, 0.0, 7.3, 0.0)
    f.cap("MeLi, CuCl (cat.)", 4.3, -1.0, "ink")
    f.cap("no H2O/H⁺ quench", 4.4, 0.2, size=7)
    X = 10.0
    a = enolate_A(f, X, 0)
    f.cap("Li⁺", X + 0.8, -2.5, "muted")
    f.cap("(A) enolate, C1=C2", X - 1.9, 2.0)
    f.save("prac_q2_cuprate")


def q2_aldol():
    f = Fig("Practice Q2 (2/2): enolate (A) + 3-phenylpropanal (aldol), then NH4Cl quench → (B) (L12_Practice_solutions p.2)")
    a = enolate_A(f, 0, 0)
    # aldehyde
    Cal = f.atom("C", 3.3, -2.6, color="el")
    Oal = f.sub(Cal, 150, "O", order=2)
    f.H(Cal, 270)
    C2 = f.sub(Cal, 30)
    C3 = f.sub(C2, 330)
    f.sub(C3, 30, label="Ph")
    f.curved({"bond": [a["C1"], a["C2"]]}, {"atom": Cal, "gap": 6, "dir": 210}, bend=0.3)
    f.curved({"bond": [Cal, Oal]}, {"atom": Oal, "gap": 3, "dir": 180}, bend=0.9)
    f.cap("(A)", -1.6, 2.0)
    f.cap("3-phenylpropanal", 3.3, -4.1)
    f.arrow(6.4, -0.5, 8.0, -0.5)
    f.cap("then NH4Cl", 6.3, -1.5, "ink")
    X = 10.0
    e = heptenone(f, X, 0)
    # make saturated 3-methyl ketone with C2 substituent
    for b in f.s["bonds"]:
        if {b[0], b[1]} == {e["C2"], e["C3"]}:
            b[2] = 1
    f.H(e["C2"], 68.6)
    Cx = f.sub(e["C2"], 8.6, bcolor="good")
    f.sub(Cx, 68.6, "O", h=1)
    Cy = f.sub(Cx, 308.6)
    Cz = f.sub(Cy, 8.6)
    f.sub(Cz, 308.6, label="Ph")
    f.sub(e["C3"], 317, label="CH3")
    f.H(e["C3"], 17)
    f.cap("(B) β-hydroxy ketone", X - 1.9, 2.0)
    f.save("prac_q2_aldol")


# ---------------- Practice Q3 ----------------

def q3_protection():
    f = Fig("Practice Q3 (1/3): Phe → Boc-Phe-OH (Boc2O); Ala → H-Ala-OMe (H⁺, MeOH) (L12_Practice_solutions p.3)")
    amino_acid(f, 2.6, 0, "Phe", ncolor="nu")
    f.cap("L-phenylalanine", 0.9, 2.2)
    f.arrow(5.6, 0.0, 8.6, 0.0)
    f.cap("Boc2O", 6.5, -1.0, "ink")
    f.cap("(base)", 6.55, 0.2)
    a = amino_acid(f, 12.2, 0, "Phe", nprot="Boc", ncolor="good")
    f.cap("Boc-Phe-OH", 11.4, 2.9)
    Y = 5.8
    amino_acid(f, 2.6, Y, "Ala", ccolor="el")
    f.cap("L-alanine", 1.5, Y + 2.4)
    f.arrow(5.6, Y, 8.6, Y)
    f.cap("H⁺, MeOH", 6.2, Y - 1.0, "ink")
    f.cap("(Fischer esterification)", 5.4, Y + 0.2, size=7)
    b = amino_acid(f, 12.2, Y, "Ala", cprot="OMe", ccolor="good")
    f.cap("H-Ala-OMe", 11.3, Y + 2.4)
    f.save("prac_q3_protection")


def q3_coupling():
    f = Fig("Practice Q3 (2/3): Boc-Phe-OH + H-Ala-OMe —DCC→ Boc-Phe-Ala-OMe (L12_Practice_solutions p.3)")
    a = amino_acid(f, 3.0, 0, "Phe", nprot="Boc", ccolor="el")
    f.cap("Boc-Phe-OH", 1.3, 2.9)
    f.cap("+", 6.0, -0.4, "ink", 10)
    b = amino_acid(f, 8.6, 0, "Ala", cprot="OMe", ncolor="nu")
    f.cap("H-Ala-OMe", 7.8, 2.4)
    Y = 5.2
    f.arrow(0.8, Y, 3.6, Y)
    f.cap("DCC", 1.8, Y - 1.0, "ink")
    f.cap("(– DCU)", 1.55, Y + 0.2)
    dipeptide(f, 6.8, Y, nprot="Boc", cprot="OMe", amide_color="good")
    f.cap("Boc-Phe-Ala-OMe", 5.6, Y + 3.0)
    f.save("prac_q3_coupling")


def q3_deprotection():
    f = Fig("Practice Q3 (3/3): Boc-Phe-Ala-OMe —TFA→ H-Phe-Ala-OMe —NaOH, H2O→ Phe-Ala (L12_Practice_solutions p.3)")
    dipeptide(f, 3.0, 0, nprot="Boc", cprot="OMe", ncolor="el")
    f.cap("Boc-Phe-Ala-OMe", 1.4, 3.0)
    f.arrow(9.0, 0.0, 11.8, 0.0)
    f.cap("TFA", 9.9, -1.0, "ink")
    d = dipeptide(f, 13.6, 0, cprot="OMe", ncolor="good")
    f.s["atoms"][d["OX"]].append("el")
    f.cap("H-Phe-Ala-OMe", 12.4, 3.0)
    Y = 6.2
    f.arrow(9.0, Y, 11.8, Y)
    f.cap("NaOH, H2O", 8.9, Y - 1.0, "ink")
    e = dipeptide(f, 13.6, Y)
    f.s["atoms"][e["OX"]].append("good")
    f.cap("L-phenylalanyl-L-alanine (Phe-Ala)", 10.7, Y + 3.0)
    f.save("prac_q3_deprotection")


# ---------------- 통독본 보강 ----------------

def phmgbr_ketone():
    f = Fig("PhMgBr attacks the more electrophilic ketone of ethyl acetoacetate (52%), not the ester (L12 p.3)")
    Me = f.atom("C", 0, 0, label="H3C")
    C2 = f.sub(Me, 30, color="el")
    O = f.sub(C2, 90, "O", order=2)
    CH2 = f.sub(C2, 330)
    Ce = f.sub(CH2, 30)
    f.sub(Ce, 90, "O", order=2)
    f.sub(Ce, 330, "O", label="OEt")
    Ph = f.atom("C", 0.45, 1.8, color="nu", label="Ph")
    Mg = f.sub(Ph, 0, "Mg", bcolor="nu")
    f.sub(Mg, 0, "Br")
    f.curved({"bond": [Ph, Mg]}, {"atom": C2, "gap": 6, "dir": 270}, bend=0.25)
    f.curved({"bond": [C2, O]}, {"atom": O, "gap": 3, "dir": 180}, bend=0.9)
    f.cap("ketone: more electrophilic", -0.2, -2.4, "el", 7)
    f.cap("ester: less electrophilic", 2.6, 0.9, "muted", 7)
    f.arrow(5.8, 0.0, 7.8, 0.0)
    f.cap("PhMgBr", 6.0, -1.0, "ink")
    f.cap("then H3O⁺", 5.8, 0.2)
    X = 9.4
    Me2 = f.atom("C", X, 0, label="H3C")
    C2b = f.sub(Me2, 30)
    f.sub(C2b, 90, "O", h=1)
    f.sub(C2b, 270, label="Ph", bcolor="good")
    CH2b = f.sub(C2b, 330)
    Ceb = f.sub(CH2b, 30)
    f.sub(Ceb, 90, "O", order=2)
    f.sub(Ceb, 330, "O", label="OEt")
    f.cap("52%: ketone adduct, ester untouched", X - 0.4, 2.0)
    f.save("phmgbr_ketone_p3")


def grignard_mol(f, X, Y, ccolor=None, kcolor=None):
    Br = f.atom("Br", X, Y)
    Mg = f.sub(Br, 0, "Mg")
    C1 = f.sub(Mg, 330, color=ccolor, bcolor=ccolor)
    C2 = f.sub(C1, 30)
    C3 = f.sub(C2, 330)
    C4 = f.sub(C3, 30, color=kcolor)
    O = f.sub(C4, 90, "O", order=2)
    f.sub(C4, 330, label="CH3")
    return dict(Mg=Mg, C1=C1, C4=C4, O=O)


def impossible_grignard():
    f = Fig("'Impossible Grignard reagent': the C–MgBr of one molecule attacks the ketone of another (L12 p.3)")
    A = grignard_mol(f, 0, 0, ccolor="nu")
    B = grignard_mol(f, -1.9, 3.4, kcolor="el")
    # B's ketone O below so the attack comes from above
    ox, oy = P(*f.pos(B["C4"]), 270)
    f.s["atoms"][B["O"]][1:3] = [round(ox, 4), round(oy, 4)]
    f.curved({"bond": [A["Mg"], A["C1"]]}, {"atom": B["C4"], "gap": 6, "dir": 90}, bend=0.25)
    f.curved({"bond": [B["C4"], B["O"]]}, {"atom": B["O"], "gap": 3, "dir": 180}, bend=0.9)
    f.cap("nucleophile", 0.6, -1.3, "nu", 7)
    f.cap("electrophile", 2.4, 4.7, "el", 7)
    f.arrow(7.0, 1.7, 9.6, 1.7)
    f.cap("self-reaction", 6.9, 1.9)
    X = 11.0
    # product: CH3C(=O)(CH2)3–C(O⁻)(CH3)–(CH2)3–MgBr (new C–C bond green)
    Br = f.atom("Br", X, 1.2)
    Mg = f.sub(Br, 0, "Mg")
    c1 = f.sub(Mg, 330)
    c2 = f.sub(c1, 30)
    c3 = f.sub(c2, 330)
    c4 = f.sub(c3, 30)
    O4 = f.sub(c4, 90, "O", charge=-1)
    m4 = f.sub(c4, 270, label="CH3")
    c5 = f.sub(c4, 330, bcolor="good")
    c6 = f.sub(c5, 30)
    c7 = f.sub(c6, 330)
    c8 = f.sub(c7, 30)
    f.sub(c8, 90, "O", order=2)
    f.sub(c8, 330, label="CH3")
    f.cap("dimer alkoxide; still a Grignard → oligomerizes", X - 0.3, 3.3, size=7)
    f.save("impossible_grignard_p3")


def amine(f, X, Y):
    N = f.atom("N", X, Y, color="nu")
    f.sub(N, 210, label="R")
    f.sub(N, 330, label="R'")
    f.H(N, 270)
    return N


def chloroformate_carbamate():
    f = Fig("Carbamate formation: RR'NH + Cl–CO–OR'' (base) → RR'N–CO–OR'' via a tetrahedral intermediate (L12 p.8)")
    C = f.atom("C", 2.6, 0, color="el")
    O = f.sub(C, 90, "O", order=2)
    Cl = f.sub(C, 330, "Cl")
    Oe = f.sub(C, 210, "O")
    f.sub(Oe, 150, label="R''")
    N = amine(f, 2.6, 2.1)
    f.lp(N, 90)
    f.curved({"lp": [N, 90]}, {"atom": C, "gap": 6, "dir": 270}, bend=0.3)
    f.curved({"bond": [C, O]}, {"atom": O, "gap": 3, "dir": 180}, bend=0.9)
    f.cap("chloroformate", 1.2, -2.2)
    f.arrow(4.6, 0.5, 6.0, 0.5)
    X = 8.4
    C2 = f.atom("C", X, 0)
    O2 = f.sub(C2, 90, "O", charge=-1, color="nu")
    Cl2 = f.sub(C2, 330, "Cl", color="el", bcolor="el")
    Oe2 = f.sub(C2, 210, "O")
    f.sub(Oe2, 150, label="R''")
    N2 = f.sub(C2, 270, "N", charge=1, bcolor="good")
    f.sub(N2, 210, label="R")
    f.sub(N2, 330, label="R'")
    f.H(N2, 270)
    f.lp(O2, 180)
    f.curved({"lp": [O2, 180]}, {"pt": [X - 0.3, -0.45]}, bend=0.6)
    f.curved({"bond": [C2, Cl2]}, {"atom": Cl2, "gap": 3, "dir": 60}, bend=-0.9)
    f.cap("tetrahedral intermediate", X - 1.6, -2.2)
    f.arrow(10.6, 0.5, 12.4, 0.5)
    f.cap("base", 11.1, -0.5, "ink")
    f.cap("– HCl", 10.95, 0.7)
    X = 15.2
    C3 = f.atom("C", X, 0)
    f.sub(C3, 90, "O", order=2)
    Oe3 = f.sub(C3, 210, "O")
    f.sub(Oe3, 150, label="R''")
    N3 = f.sub(C3, 330, "N", color="good", bcolor="good")
    f.sub(N3, 30, label="R")
    f.sub(N3, 270, label="R'")
    f.cap("carbamate", X - 0.6, 2.6)
    f.cap("R'' = CH2Ph: Cbz-Cl;  R'' = 9-fluorenylmethyl: Fmoc-Cl", 6.0, 3.6, size=7)
    f.save("carbamate_chloroformate_p8")


def leu(f, X, Y, pg="PG1"):
    Ca = f.atom("C", X, Y)
    N = f.sub(Ca, 270, "N", h=1, disp="wedge")
    f.sub(N, 210, label=pg)
    CH2 = f.sub(Ca, 150)
    CH = f.sub(CH2, 90)
    f.sub(CH, 150)
    f.sub(CH, 30)
    Cco = f.sub(Ca, 30)
    O = f.sub(Cco, 90, "O", order=2)
    return dict(Ca=Ca, N=N, Cco=Cco, O=O)


def peptide_coupling():
    f = Fig("Peptide coupling: Gly NH2 (nucleophile) attacks the activated Leu C(=O)X (electrophile) (L12 p.9)")
    L = leu(f, 0, 0)
    f.s["atoms"][L["Cco"]].append("el")
    X = f.sub(L["Cco"], 330, label="X")
    # Gly
    N = f.atom("N", 3.3, 1.4, h=2, color="nu")
    Ca = f.sub(N, 330)
    Cc = f.sub(Ca, 30)
    f.sub(Cc, 90, "O", order=2)
    Og = f.sub(Cc, 330, "O")
    f.sub(Og, 30, label="PG2")
    f.lp(N, 90)
    f.curved({"lp": [N, 90]}, {"atom": L["Cco"], "gap": 6, "dir": 270}, bend=0.35)
    f.curved({"bond": [L["Cco"], L["O"]]}, {"atom": L["O"], "gap": 3, "dir": 180}, bend=0.9)
    f.cap("Leu (N-protected)", -2.2, 2.2)
    f.cap("Gly (C-protected)", 3.6, 2.9)
    f.arrow(7.8, 0.4, 9.3, 0.4)
    f.cap("– HX", 8.1, -0.55, "ink")
    X2 = 12.0
    L2 = leu(f, X2, 0)
    Nam = f.sub(L2["Cco"], 330, "N", h=1, color="good", bcolor="good")
    Ca2 = f.sub(Nam, 30)
    Cc2 = f.sub(Ca2, 330)
    f.sub(Cc2, 270, "O", order=2)
    Og2 = f.sub(Cc2, 30, "O")
    f.sub(Og2, 330, label="PG2")
    f.cap("protected dipeptide Leu-Gly", X2 - 0.5, 2.2)
    f.save("peptide_coupling_p9")


def thp_protection():
    f = Fig("THP protection of an alcohol: dihydropyran + H⁺ → oxocarbenium, then ROH adds (supplement, Clayden p.550–551; L12 p.5 table)")
    # panel 1: DHP, start 90: k0 top=C6, k1 150=O1, k2 210=C2, k3 270=C3, k4 330=C4, k5 30=C5
    k = f.ring(6, 0, 0, 90, orders=[1, 1, 1, 1, 1, 2], els={1: "O"})
    C6, O1, C5 = k[0], k[1], k[5]
    f.s["atoms"][C6].append("nu")
    f.s["atoms"][C5].append("nu")
    f.H(C6, 90)
    f.H(C5, 30)
    Hp = f.atom("H", 2.5, -0.1, charge=1, color="el")
    f.curved({"bond": [C6, C5]}, {"atom": Hp, "gap": 3, "dir": 180}, bend=-0.4)
    f.cap("dihydropyran", -1.3, 2.0)
    f.cap("H⁺ (cat.)", 2.4, 0.35, size=7)
    f.arrow(3.4, -0.6, 5.0, -0.6)
    # panel 2: oxocarbenium
    X = 6.8
    k2 = f.ring(6, X, 0, 90, orders=[2, 1, 1, 1, 1, 1], els={1: "O"})
    C6b, O1b, C5b = k2[0], k2[1], k2[5]
    f.s["atoms"][O1b][3] = 1
    f.s["atoms"][C6b].append("el")
    f.H(C6b, 90)
    f.H(C5b, 30)
    f.H(C5b, 330)
    Oa = f.atom("O", X + 1.9, -2.5, h=1, color="nu")
    f.sub(Oa, 60, label="R")
    f.lp(Oa, 270)
    f.curved({"lp": [Oa, 270]}, {"atom": C6b, "gap": 6, "dir": 30}, bend=-0.35)
    f.cap("oxocarbenium ion", X - 1.5, 2.0)
    f.arrow(10.4, -0.6, 12.0, -0.6)
    f.cap("– H⁺", 10.7, -1.5, "ink")
    # panel 3: THP ether
    X = 13.8
    k3 = f.ring(6, X, 0, 90, els={1: "O"})
    C6c, O1c = k3[0], k3[1]
    Oc = f.sub(C6c, 60, "O", bcolor="good", color="good")
    f.sub(Oc, 0, label="R")
    f.H(C6c, 120)
    f.cap("RO–THP (an acetal: O–C–O)", X - 1.6, 2.0)
    f.cap("deprotection: H⁺, H2O (reverse)", X - 1.7, 2.5, size=7)
    f.save("thp_protection")


if __name__ == "__main__":
    q1_michael()
    q1_enamine_cyclization()
    q1_dehydration()
    q2_cuprate()
    q2_aldol()
    q3_protection()
    q3_coupling()
    q3_deprotection()
    phmgbr_ketone()
    impossible_grignard()
    chloroformate_carbamate()
    peptide_coupling()
    thp_protection()
