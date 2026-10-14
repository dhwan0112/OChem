#!/usr/bin/env python3
"""xyz 구조를 공-막대(ball-and-stick) 그림으로 그린다 (정사영, 깊이 순서).

구조 파일은 figures/xyz/*.xyz (GFN2-xTB로 최적화; 전이 상태는 형성/절단 결합 길이를
고정한 근사 구조). 그림은 tools/visual_boost.py가 이 모듈로 만든다.
"""
import numpy as np
from matplotlib.patches import Circle
from mplfig import C

COL = {"H": "#f2f2f2", "C": "#7d7f86", "O": "#e0453a", "Br": "#a0522d", "N": "#3b6fe0"}
RAD = {"H": 0.22, "C": 0.34, "O": 0.33, "Br": 0.45, "N": 0.33}
COV = {"H": 0.32, "C": 0.76, "O": 0.66, "Br": 1.20, "N": 0.71}


def read_xyz(p):
    L = open(p).read().split("\n")
    n = int(L[0]); S, X = [], []
    for l in L[2:2 + n]:
        t = l.split(); S.append(t[0]); X.append([float(v) for v in t[1:4]])
    return S, np.array(X)


def rot(ax, deg):
    a = np.radians(deg); c, s = np.cos(a), np.sin(a)
    return {"x": np.array([[1, 0, 0], [0, c, -s], [0, s, c]]),
            "y": np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]]),
            "z": np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])}[ax]


def orient(X, a, b, c):
    """원자 a→b를 x축으로, 원자 c가 xy 평면 위쪽(+y)에 오게 돌린다."""
    X = X - X[[a, b]].mean(0)
    ex = X[b] - X[a]; ex /= np.linalg.norm(ex)
    v = X[c] - X[a]; ey = v - ex * (v @ ex); ey /= np.linalg.norm(ey)
    ez = np.cross(ex, ey)
    return X @ np.array([ex, ey, ez]).T


def draw(ax, S, X, partial=(), dotted=(), views=(), offset=(0, 0), labels=None, dlabel=True, skip=()):
    for axis, deg in views:
        X = X @ rot(axis, deg).T
    X = X + np.array([offset[0], offset[1], 0])
    part = {tuple(sorted(p)) for p in partial}; dot = {tuple(sorted(p)) for p in dotted}
    items = []
    n = len(S)
    for i in range(n):
        for j in range(i + 1, n):
            d = np.linalg.norm(X[i] - X[j]); key = (i, j)
            if key in part or key in dot:
                items.append(((X[i, 2] + X[j, 2]) / 2 - 0.01, "pb", i, j, d))
            elif d < 1.15 * (COV[S[i]] + COV[S[j]]) and key not in skip:
                items.append(((X[i, 2] + X[j, 2]) / 2 - 0.01, "b", i, j, d))
        items.append((X[i, 2], "a", i, None, None))
    for z, kind, i, j, d in sorted(items, key=lambda t: t[0]):
        if kind == "a":
            r = RAD[S[i]]
            ax.add_patch(Circle(X[i, :2], r, fc=COL[S[i]], ec=C["ink"], lw=0.8, zorder=10 + z))
            ax.add_patch(Circle(X[i, :2] + np.array([-0.3, 0.3]) * r, 0.28 * r, fc="white", ec="none", alpha=0.45, zorder=10 + z))
        else:
            p, q = X[i, :2], X[j, :2]
            if kind == "b":
                ax.plot(*zip(p, q), color=C["ink"], lw=2.6, solid_capstyle="round", zorder=10 + z)
            else:
                isdot = (i, j) in dot
                ax.plot(*zip(p, q), color=C["muted"] if isdot else C["good"], lw=2.0,
                        ls=(0, (1, 2)) if isdot else (0, (3, 2)), zorder=10 + z)
                if dlabel:
                    m = (p + q) / 2
                    ax.text(m[0] + 0.12, m[1] + 0.05, f"{d:.2f} Å", fontsize=7,
                            color=C["muted"] if isdot else C["good"], zorder=100)
    if labels:
        for i, (txt, dx, dy) in labels.items():
            ax.text(X[i, 0] + dx, X[i, 1] + dy, txt, fontsize=8, color=C["ink"], zorder=100, ha="center")
    return X
