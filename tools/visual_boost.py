#!/usr/bin/env python3
"""시각화 보강 그림 생성 (3D 구조/TS, 에너지 도표, 오비탈 도식, Newman 투영).

사용법: <numpy+matplotlib python> tools/visual_boost.py [그림이름 ...]
3D 구조: figures/xyz/*.xyz (GFN2-xTB, ORCA의 otool_xtb 6.7.1 + ASE BFGS).
TS 표시 구조는 형성/절단 결합 길이를 고정해 최적화한 근사 구조다(진짜 안장점 아님).
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch, Circle
from mplfig import C, save
import mol3dfig as M

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = lambda p: os.path.join(ROOT, "figures", p)
XYZ = lambda n: M.read_xyz(F(f"xyz/{n}.xyz"))
HA2KCAL = 627.509


def canvas(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_aspect("equal"); ax.axis("off")
    return fig, ax


def arrow(ax, p, q, color="arrow", rad=0.0, lw=1.6, style="-|>"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=12, lw=lw,
                                 color=C[color], connectionstyle=f"arc3,rad={rad}", zorder=200))


# ---------------------------------------------------------------- 3D
def bromonium_3d():
    S, X = XYZ("bromonium")
    X = M.orient(X, 0, 1, 2)
    fig, ax = canvas(4.2, 3.6)
    Y = M.draw(ax, S, X, views=[("x", -25)], labels={2: ("Br+", 0, 0.62)})
    d = Y[1] - Y[2]; d /= np.linalg.norm(d)
    tip = Y[1, :2] + d[:2] * 0.5; tail = Y[1, :2] + d[:2] * 2.0
    arrow(ax, tail, tip, "nu")
    ax.text(*(tail + np.array([0.05, -0.3])), "Br−  (backside, anti to Br+)", color=C["nu"], fontsize=8)
    ax.text(-2.2, -2.45, "C–C 1.47 Å,  C–Br 1.98 Å", color=C["muted"], fontsize=7)
    ax.text(-2.2, 2.6, "bromonium ion (ethylene + Br+), GFN2-xTB", color=C["muted"], fontsize=7)
    ax.autoscale_view(); ax.set_xlim(-2.4, 3.6); ax.set_ylim(-2.6, 2.9)
    save(fig, F("L01/bromonium_3d.svg"))


def butterfly_3d():
    S, X = XYZ("butterfly")
    X = M.orient(X, 0, 1, 6)
    fig, ax = canvas(4.6, 4.6)
    M.draw(ax, S, X, partial=[(0, 6), (1, 6), (6, 7)], dotted=[(9, 10)], skip={(6, 10), (7, 10)} - set(),
           views=[("y", 40), ("x", -15)], labels={6: ("O", -0.45, 0.1), 7: ("O", 0.45, 0.0), 9: ("O=C", 0.55, 0.0)})
    ax.text(-2.4, -1.7, "green dashed: bonds forming/breaking (C···O, O···O)", color=C["good"], fontsize=7)
    ax.text(-2.4, -2.0, "dotted: O–H···O=C hydrogen bond (H moves to C=O)", color=C["muted"], fontsize=7)
    ax.text(-2.4, -2.3, "model: C2H4 + HCO3H, GFN2-xTB, distances fixed (approx. TS)", color=C["muted"], fontsize=7)
    ax.autoscale_view(); ax.set_xlim(-2.5, 3.2); ax.set_ylim(-2.45, 5.6)
    save(fig, F("L01/mcpba_butterfly_ts_3d.svg"))


def pair_3d(name, a, b, partial, title, views, orient_args, out, notes):
    fig, ax = canvas(7.6, 3.8)
    for k, (n, lab) in enumerate([a, b]):
        S, X = XYZ(n)
        X = M.orient(X, *orient_args)
        M.draw(ax, S, X, partial=partial, views=views, offset=(k * 6.0, 0), dlabel=(k == 0))
        ax.text(k * 6.0, -3.6, lab, ha="center", fontsize=9, color=C["ink"])
    for i, t in enumerate(notes):
        ax.text(-2.8, -4.1 - 0.35 * i, t, fontsize=7, color=C["muted"])
    ax.text(-2.8, 3.2, title, fontsize=8, color=C["ink"])
    ax.autoscale_view()
    save(fig, F(out))


def cope_3d():
    pair_3d("cope", ("cope_chair", "chair TS (favored)"), ("cope_boat", "boat TS"), [(0, 5), (2, 3)],
            "[3,3] Cope TS of hexa-1,5-diene: chair vs boat", [("x", -45), ("y", 20)], (2, 0, 3),
            "L16/cope_chair_boat_ts_3d.svg",
            ["GFN2-xTB, forming/breaking C···C fixed at 2.00 Å (approx. TS)",
             "xTB: boat ~8 kcal/mol higher (experiment ~6 kcal/mol)"])


def da_3d():
    pair_3d("da", ("da_endo", "endo TS (favored)"), ("da_exo", "exo TS"), [(5, 10), (6, 7)],
            "cyclopentadiene + maleic anhydride: endo vs exo", [("x", -65), ("y", 15)], (7, 10, 11),
            "L13/da_endo_exo_ts_3d.svg",
            ["endo: C=O groups of the anhydride lie under the diene π system",
             "GFN2-xTB, forming C···C fixed at 2.25 Å (approx. TS); xTB: endo ~2 kcal/mol lower"])


# ---------------------------------------------------------------- 에너지 도표
def profile(ax, xs, ys, color, lw=2.0, ls="-"):
    """(x, y) 점들을 부드러운 곡선으로 잇는다 (코사인 보간)."""
    px, py = [], []
    for (x0, y0), (x1, y1) in zip(zip(xs, ys), zip(xs[1:], ys[1:])):
        t = np.linspace(0, 1, 40); s = (1 - np.cos(np.pi * t)) / 2
        px += list(x0 + (x1 - x0) * t); py += list(y0 + (y1 - y0) * s)
    ax.plot(px, py, color=C[color], lw=lw, ls=ls)


def energy_axes(w=5.6, h=3.6):
    fig, ax = plt.subplots(figsize=(w, h))
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("reaction coordinate"); ax.set_ylabel("energy (qualitative)")
    return fig, ax


def hbr_profile():
    fig, ax = energy_axes()
    profile(ax, [0, 1.5, 3, 4.5, 6], [0, 6.0, 3.8, 4.6, -3], "muted", ls="--")
    profile(ax, [0, 1.5, 3, 4.5, 6], [0, 3.6, 1.2, 2.0, -3.5], "good")
    ax.text(0, 0.35, "isobutene + HBr", fontsize=8, ha="center")
    ax.text(3, 0.55, "3° cation\n(CH3)3C+", fontsize=8, ha="center", color=C["good"], va="top")
    ax.text(3, 4.2, "1° cation (CH3)2CHCH2+", fontsize=8, ha="center", color=C["muted"])
    ax.text(1.5, 6.3, "TS1 (higher)", fontsize=7, ha="center", color=C["muted"])
    ax.text(1.5, 2.9, "TS1", fontsize=7, ha="center", color=C["good"])
    ax.text(6, -2.6, "t-BuBr\n(Markovnikov)", fontsize=8, ha="center", color=C["good"])
    ax.text(6.0, -4.6, "rate-determining step = protonation;\nlower TS → more stable cation wins", fontsize=7, ha="center", color=C["muted"])
    ax.set_xlim(-0.8, 7); ax.set_ylim(-5.2, 7)
    save(fig, F("L01/hbr_energy_profile.svg"))


def sear_profile():
    fig, ax = energy_axes(6.0, 3.8)
    profile(ax, [0, 1.6, 3.2, 4.6, 6.2], [0, 6, 4.0, 4.8, -0.8], "good")
    profile(ax, [3.2, 4.6, 6.2], [4.0, 6.2, 2.8], "el", ls="--")
    ax.text(-0.1, 0.45, "benzene + E+", ha="right", fontsize=8)
    ax.text(1.6, 6.35, "TS1 (slow:\naromaticity lost)", ha="center", fontsize=7)
    ax.text(3.0, 3.0, "σ complex\n(arenium ion)", ha="center", fontsize=8)
    ax.text(6.3, -0.4, "substitution\nproduct\n(aromatic again)", ha="left", fontsize=8, color=C["good"])
    ax.text(6.3, 3.0, "addition product\n(not aromatic)", ha="left", fontsize=8, color=C["el"])
    ax.text(4.6, 5.35, "−H+ (fast)", ha="center", fontsize=7, color=C["good"])
    ax.text(4.6, 6.4, "+Nu−", ha="center", fontsize=7, color=C["el"])
    ax.set_xlim(-0.8, 8.4); ax.set_ylim(-1.5, 7.6)
    save(fig, F("L03/sear_energy_profile.svg"))


def enolate_profile():
    fig, ax = energy_axes(6.0, 3.8)
    profile(ax, [3, 1.5, 0], [0, 4.0, 1.6], "nu")       # kinetic: 왼쪽
    profile(ax, [3, 4.5, 6], [0, 5.5, 0.6], "el")       # thermodynamic: 오른쪽
    ax.text(3, -0.6, "2-methylcyclohexanone + base", ha="center", fontsize=8)
    ax.text(0, 2.0, "kinetic enolate\n(less substituted C=C)", ha="center", fontsize=8, color=C["nu"])
    ax.text(6, 1.0, "thermodynamic enolate\n(more substituted C=C)", ha="center", fontsize=8, color=C["el"])
    ax.text(1.5, 4.25, "lower TS: C6–H\n(less hindered)", ha="center", fontsize=7, color=C["nu"])
    ax.text(4.5, 5.75, "higher TS: C2–H", ha="center", fontsize=7, color=C["el"])
    ax.text(3, 6.6, "LDA, −78 °C (irreversible) → left    |    weaker base, rt, equilibrium → right",
            ha="center", fontsize=7, color=C["muted"])
    ax.set_xlim(-1.2, 7.4); ax.set_ylim(-1.2, 7.0)
    save(fig, F("L07/enolate_kinetic_thermo_energy.svg"))


# ---------------------------------------------------------------- 오비탈
def p_orb(ax, x, y, sign, size=0.55, alpha=1.0, angle=0):
    """p 오비탈 하나: 위 로브 부호 sign(+1 채움 / −1 빈), 아래는 반대."""
    up = np.array([-np.sin(np.radians(angle)), np.cos(np.radians(angle))])
    for k, s in ((1, sign), (-1, -sign)):
        cx, cy = np.array([x, y]) + up * k * size * 0.55
        ax.add_patch(Ellipse((cx, cy), size * 0.62, size * 1.1, angle=angle,
                             fc=C["nu"] if s > 0 else "none", ec=C["nu"], lw=1.3, alpha=alpha, zorder=5))
    ax.add_patch(Circle((x, y), 0.05, fc=C["ink"], zorder=6))


def da_fmo():
    fig, ax = canvas(5.4, 4.2)
    dx = [0, 1.2, 2.4, 3.6]
    for x, s, c in zip(dx, [1, 1, -1, -1], [1.0, 0.75, 0.75, 1.0]):
        p_orb(ax, x, 1.6, s, size=0.55 * c + 0.2)
    ax.plot(dx, [1.6] * 4, color=C["ink"], lw=1.0)
    ax.text(4.3, 1.6, "diene HOMO (ψ2)", va="center", fontsize=8)
    for x, s in zip([0, 3.6], [-1, 1]):
        p_orb(ax, x, -1.6, s, size=0.75)
    ax.plot([0, 3.6], [-1.6, -1.6], color=C["ink"], lw=1.0, ls=(0, (1, 2)))
    ax.text(4.3, -1.6, "dienophile LUMO (π*)", va="center", fontsize=8)
    for x in (0, 3.6):
        ax.plot([x, x], [1.0, -1.0], color=C["good"], lw=1.6, ls=(0, (3, 2)))
    ax.text(1.8, 0.05, "phases match\nat BOTH ends\n→ both σ bonds form together\n(suprafacial, thermally allowed)",
            ha="center", va="center", fontsize=7, color=C["good"])
    ax.text(-0.6, 2.9, "filled lobe = + phase, open lobe = − phase; end lobes larger (bigger coefficient)", fontsize=7, color=C["muted"])
    ax.set_xlim(-0.8, 6.6); ax.set_ylim(-2.8, 3.2)
    save(fig, F("L13/da_fmo_lobes.svg"))


def con_dis():
    fig, ax = canvas(7.4, 4.6)
    rows = [(1.8, "4π: butadiene HOMO ψ2 (thermal)", [1, 1, -1, -1], "conrotatory", (1, -1)),
            (-1.8, "6π: hexatriene HOMO ψ3 (thermal)", [1, 1, -1, -1, 1, 1], "disrotatory", (1, 1))]
    for y, lab, signs, mode, rot in rows:
        n = len(signs); xs = np.linspace(0, 3.0, n)
        for x, s in zip(xs, signs):
            p_orb(ax, x, y, s, size=0.5, alpha=1 if x in (xs[0], xs[-1]) else 0.35)
        ax.plot(xs, [y] * n, color=C["ink"], lw=1.0)
        ax.text(-0.3, y + 1.0, lab, fontsize=8)
        # 오른쪽: 말단 두 개만, 회전 후 위 로브끼리 만남
        L, R = 5.0, 6.6
        # 왼쪽 말단은 시계 방향으로 돌아 + 로브가 안쪽 위로 온다.
        # 오른쪽 말단: 4π는 아래쪽 + 로브가 올라오도록 같은 방향(시계), 6π는 반대 방향(반시계)
        p_orb(ax, L, y, signs[0], size=0.6, angle=-35)
        p_orb(ax, R, y, signs[-1], size=0.6, angle=(35 if mode == "disrotatory" else -145))
        arrow(ax, (L - 0.55, y - 0.6), (L - 0.55, y + 0.6), "arrow", rad=-0.6)
        if mode == "conrotatory":
            arrow(ax, (R + 0.55, y + 0.6), (R + 0.55, y - 0.6), "arrow", rad=-0.6)
        else:
            arrow(ax, (R + 0.55, y - 0.6), (R + 0.55, y + 0.6), "arrow", rad=0.6)
        ax.plot([L + 0.25, R - 0.25], [y + 0.45, y + 0.45], color=C["good"], lw=1.6, ls=(0, (3, 2)))
        ax.text((L + R) / 2, y - 1.05, mode, ha="center", fontsize=9, color=C["good"])
    ax.text(-0.3, -3.6, "ends must turn so that lobes of the SAME phase meet to make the new σ bond",
            fontsize=7, color=C["muted"])
    ax.set_xlim(-0.6, 7.6); ax.set_ylim(-3.9, 3.2)
    save(fig, F("L17/con_dis_homo_lobes.svg"))


# ---------------------------------------------------------------- Newman
def newman(ax, cx, cy, front, back, title, color_br="el"):
    """front/back: {각도(deg): 라벨}. 앞 탄소 결합은 중심에서, 뒤 탄소 결합은 원 밖에서."""
    R = 0.8
    ax.add_patch(Circle((cx, cy), R, fc="none", ec=C["ink"], lw=1.5))
    for ang, lab in front.items():
        v = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
        ax.plot([cx, cx + v[0] * 1.45], [cy, cy + v[1] * 1.45], color=C["ink"], lw=1.6)
        ax.text(cx + v[0] * 1.8, cy + v[1] * 1.8, lab, ha="center", va="center", fontsize=9,
                color=C[color_br] if lab == "Br" else C["ink"])
    for ang, lab in back.items():
        v = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
        ax.plot([cx + v[0] * R, cx + v[0] * 1.45], [cy + v[1] * R, cy + v[1] * 1.45], color=C["ink"], lw=1.6)
        ax.text(cx + v[0] * 1.8, cy + v[1] * 1.8, lab, ha="center", va="center", fontsize=9,
                color=C[color_br] if lab == "Br" else C["ink"])
    ax.text(cx, cy - 2.55, title, ha="center", fontsize=8)


def anti_newman():
    fig, ax = canvas(7.6, 3.6)
    fr = {90: "Br", 210: "CH3", 330: "H"}
    newman(ax, 0, 0, fr, {270: "Br", 30: "CH3", 150: "H"}, "from (E)-2-butene:\nmeso (2R,3S)")
    newman(ax, 5.2, 0, fr, {270: "Br", 150: "CH3", 30: "H"}, "from (Z)-2-butene:\n(2R,3R) + (2S,3S) racemic")
    ax.text(-2.3, 2.6, "Br2 adds anti: the two Br end up 180° apart (Newman, C2 in front)", fontsize=8, color=C["muted"])
    ax.text(1.4, -3.65, "same front carbon; only the back carbon differs → meso vs chiral pair", fontsize=7, color=C["muted"])
    ax.set_xlim(-2.6, 7.6); ax.set_ylim(-3.8, 2.9)
    save(fig, F("L02/anti_addition_newman.svg"))


ALL = {f.__name__: f for f in [bromonium_3d, butterfly_3d, cope_3d, da_3d, hbr_profile, sear_profile,
                              enolate_profile, da_fmo, con_dis, anti_newman]}
if __name__ == "__main__":
    for n in (sys.argv[1:] or ALL):
        ALL[n]()
