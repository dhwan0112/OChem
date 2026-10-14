#!/usr/bin/env python3
"""시각화 보강 그림 중 ReShiki(chemfig.py)로 그릴 수 없는 것: 3D 구조/TS와 정성적 에너지 도표.

사용법: <numpy+matplotlib python> tools/visual_boost.py [그림이름 ...]
2D 그림(σ complex 공명, anti 첨가 입체화학, FMO 로브, con/dis 로브)은 figures/L##/*.json → chemfig.py로 만든다.
양식은 chemfig 그림에 맞춘다 (tools/mplfig.py의 PX 규격, figures/STYLE.md 7절).
3D 구조: figures/xyz/*.xyz (GFN2-xTB, ORCA의 otool_xtb 6.7.1 + ASE BFGS).
TS 표시 구조는 형성/절단 결합 길이를 고정해 최적화한 근사 구조다(진짜 안장점 아님).
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mplfig import C, PX, save
import mol3dfig as M

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = lambda p: os.path.join(ROOT, "figures", p)
XYZ = lambda n: M.read_xyz(F(f"xyz/{n}.xyz"))


def canvas():
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_aspect("equal"); ax.axis("off")
    return fig, ax


def arrow(ax, p, q, color="arrow", rad=0.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=11, lw=PX["arrow"],
                                 color=C[color], connectionstyle=f"arc3,rad={rad}", zorder=8))


def cap(ax, x, y, t, color="muted", size="caption", **kw):
    ax.text(x, y, t, fontsize=PX[size], color=C[color], **kw)


# ---------------------------------------------------------------- 3D
def bromonium_3d():
    S, X = XYZ("bromonium")
    X = M.orient(X, 0, 1, 2)
    fig, ax = canvas()
    Y = M.draw(ax, S, X, views=[("x", -25)], charges={2: "⁺"}, colors={2: "el"})
    d = Y[1] - Y[2]; d /= np.linalg.norm(d)
    tip = Y[1, :2] + d[:2] * 16; tail = Y[1, :2] + d[:2] * 60
    arrow(ax, tail, tip, "nu")
    cap(ax, tail[0] + 6, tail[1], "Br⁻ attacks anti to Br⁺", "nu", va="center")
    M.fit(fig, ax)
    cap(ax, Y[:, 0].min() - 10, tail[1] - 22, "C–C 1.47 Å, C–Br 1.98 Å (GFN2-xTB)", va="top")
    save(fig, F("L01/bromonium_3d.svg"))


def butterfly_3d():
    S, X = XYZ("butterfly")
    X = M.orient(X, 0, 1, 6)
    fig, ax = canvas()
    Y = M.draw(ax, S, X, partial=[(0, 6), (1, 6), (6, 7)], dotted=[(9, 10)], skip={(6, 10)},
               views=[("y", 40), ("x", -15)], colors={6: "el"}, nolabel=[(1, 6)])
    M.fit(fig, ax)
    y0 = Y[:, 1].min() - 22
    cap(ax, Y[:, 0].min() - 20, y0, "green dashed: C···O forming, O···O breaking", "good", va="top")
    cap(ax, Y[:, 0].min() - 20, y0 - 18, "grey dotted: O–H···O=C (H moves to C=O)", va="top")
    cap(ax, Y[:, 0].min() - 20, y0 - 36, "C2H4 + HCO3H, GFN2-xTB, approx. TS", va="top")
    save(fig, F("L01/mcpba_butterfly_ts_3d.svg"))


def pair_3d(a, b, partial, views, orient_args, out, notes, gap=170):
    fig, ax = canvas()
    ys = []
    for k, (n, lab) in enumerate([a, b]):
        S, X = XYZ(n)
        X = M.orient(X, *orient_args)
        Y = M.draw(ax, S, X, partial=partial, views=views, offset=(k * gap, 0), dlabel=(k == 0))
        ys.append((k * gap, Y[:, 1].min(), lab))
    M.fit(fig, ax)
    ylab = min(y for _, y, _ in ys) - 22
    for x, _, lab in ys:
        cap(ax, x, ylab, lab, "ink", ha="center", va="top")
    for i, t in enumerate(notes):
        cap(ax, -90, ylab - 26 - 17 * i, t, size="small", va="top")
    save(fig, F(out))


def cope_3d():
    pair_3d(("cope_chair", "chair TS (favored)"), ("cope_boat", "boat TS"), [(0, 5), (2, 3)],
            [("x", -45), ("y", 20)], (2, 0, 3), "L16/cope_chair_boat_ts_3d.svg",
            ["hexa-1,5-diene, GFN2-xTB, C···C fixed at 2.00 Å (approx. TS)",
             "xTB: boat ~8 kcal/mol higher (experiment ~6 kcal/mol)"], gap=230)


def da_3d():
    pair_3d(("da_endo", "endo TS (favored)"), ("da_exo", "exo TS"), [(5, 10), (6, 7)],
            [("x", -65), ("y", 15)], (7, 10, 11), "L13/da_endo_exo_ts_3d.svg",
            ["endo: anhydride C=O groups sit under the diene π system",
             "GFN2-xTB, C···C fixed at 2.25 Å (approx. TS); endo ~2 kcal/mol lower"], gap=250)


# ---------------------------------------------------------------- 에너지 도표
U = 26.0  # 도표 1 단위 = 26 px (결합 길이 하나)


def profile(ax, xs, ys, color, ls="-"):
    px, py = [], []
    for (x0, y0), (x1, y1) in zip(zip(xs, ys), zip(xs[1:], ys[1:])):
        t = np.linspace(0, 1, 40); s = (1 - np.cos(np.pi * t)) / 2
        px += list(x0 + (x1 - x0) * t); py += list(y0 + (y1 - y0) * s)
    ax.plot(np.array(px) * U, np.array(py) * U, color=C[color], lw=PX["arrow"], ls=ls, solid_capstyle="round")


def energy_canvas(xmax, ymin, ymax):
    fig, ax = canvas()
    ax.annotate("", xy=(-0.9 * U, ymax * U), xytext=(-0.9 * U, ymin * U),
                arrowprops=dict(arrowstyle="-|>", lw=PX["stroke"], color=C["ink"], mutation_scale=10))
    cap(ax, -1.25 * U, (ymin + ymax) / 2 * U, "energy", rotation=90, ha="center", va="center")
    cap(ax, xmax / 2 * U, (ymin - 0.4) * U, "reaction coordinate (qualitative)", ha="center", va="top")
    return fig, ax


def T(ax, x, y, t, color="ink", size="caption", **kw):
    cap(ax, x * U, y * U, t, color, size, **kw)


def hbr_profile():
    fig, ax = energy_canvas(8, -4.2, 7.2)
    profile(ax, [0, 1.8, 3.6, 5.4, 7.2], [0, 6.0, 3.8, 4.6, -3], "muted", ls="--")
    profile(ax, [0, 1.8, 3.6, 5.4, 7.2], [0, 3.6, 1.2, 2.0, -3.5], "good")
    T(ax, 0, -0.5, "isobutene + HBr", ha="center", va="top")
    T(ax, 3.6, 0.8, "3° cation", "good", ha="center", va="top")
    T(ax, 3.6, 3.0, "1° cation", "muted", ha="center", va="top")
    T(ax, 1.8, 6.4, "higher TS", "muted", "small", ha="center")
    T(ax, 7.4, -3.4, "t-BuBr (Markovnikov)", "good", va="center")
    fit_save(fig, ax, "L01/hbr_energy_profile.svg")


def sear_profile():
    fig, ax = energy_canvas(7, -1.6, 7.4)
    profile(ax, [0, 1.8, 3.6, 5.2, 7.0], [0, 6, 4.0, 4.8, -0.8], "good")
    profile(ax, [3.6, 5.2, 7.0], [4.0, 6.2, 2.8], "el", ls="--")
    T(ax, 0, -0.5, "benzene + E⁺", ha="center", va="top")
    T(ax, 1.8, 6.4, "slow: aromaticity lost", "ink", "small", ha="center")
    T(ax, 3.6, 3.5, "σ complex", ha="center", va="top")
    T(ax, 7.2, -0.8, "substitution (aromatic)", "good", va="center")
    T(ax, 7.2, 2.8, "addition (not aromatic)", "el", va="center")
    T(ax, 5.2, 4.25, "−H⁺ (fast)", "good", "small", ha="center", va="top")
    T(ax, 5.2, 6.5, "+Nu⁻", "el", "small", ha="center")
    fit_save(fig, ax, "L03/sear_energy_profile.svg")


def enolate_profile():
    fig, ax = energy_canvas(7, -1.0, 7.0)
    profile(ax, [3.5, 1.75, 0], [0, 4.0, 1.6], "nu")
    profile(ax, [3.5, 5.25, 7], [0, 5.5, 0.6], "el")
    T(ax, 3.5, -0.4, "2-methylcyclohexanone", ha="center", va="top")
    T(ax, 0, 1.1, "kinetic enolate", "nu", ha="center", va="top")
    T(ax, 7, 0.1, "thermodynamic enolate", "el", ha="center", va="top")
    T(ax, 1.75, 4.3, "lower TS (C6–H)", "nu", "small", ha="center")
    T(ax, 5.25, 5.8, "higher TS (C2–H)", "el", "small", ha="center")
    T(ax, 3.5, 7.0, "LDA, −78 °C → kinetic   |   equilibrating → thermodynamic", "muted", "small", ha="center")
    fit_save(fig, ax, "L07/enolate_kinetic_thermo_energy.svg")


def fit_save(fig, ax, out):
    M.fit(fig, ax, margin=6)
    save(fig, F(out))


ALL = {f.__name__: f for f in [bromonium_3d, butterfly_3d, cope_3d, da_3d, hbr_profile, sear_profile,
                              enolate_profile]}
if __name__ == "__main__":
    for n in (sys.argv[1:] or ALL):
        ALL[n]()
