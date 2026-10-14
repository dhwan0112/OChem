#!/usr/bin/env python3
"""xyz 구조를 공-막대(ball-and-stick) 그림으로 그린다 (정사영, 깊이 순서).

구조 파일은 figures/xyz/*.xyz (GFN2-xTB로 최적화; 전이 상태는 형성/절단 결합 길이를
고정한 근사 구조). 그림은 tools/visual_boost.py가 이 모듈로 만든다.
"""
import numpy as np
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


ANG2PX = 34.0  # px/Å. 3D 투영은 결합이 짧아 보이므로 chemfig(26 px/결합)보다 크게 잡는다


def draw(ax, S, X, partial=(), dotted=(), views=(), offset=(0, 0), labels=None, dlabel=True, skip=(),
         charges=None, colors=None, nolabel=()):
    """chemfig 그림과 같은 선 그림 양식으로 그린다.
    - 결합: ink 1.085 px, 화면 뒤쪽 절반은 muted 색으로 깊이를 나타낸다.
    - 원자: C는 꼭짓점(라벨 없음), 나머지는 원소 기호(18 px DejaVu Sans), 배경색 바탕으로 결합을 끊는다.
    - 형성/절단 결합: good 색 점선, 수소결합: muted 점선. 길이 라벨은 12.7 px.
    좌표 단위는 px (Å × ANG2PX).
    """
    from mplfig import PX
    for axis, deg in views:
        X = X @ rot(axis, deg).T
    X = X * ANG2PX + np.array([offset[0], offset[1], 0])
    part = {tuple(sorted(p)) for p in partial}; dot = {tuple(sorted(p)) for p in dotted}
    zmid = np.median(X[:, 2])
    n = len(S)
    for i in range(n):
        for j in range(i + 1, n):
            d = np.linalg.norm(X[i] - X[j]) / ANG2PX; key = (i, j)
            p, q = X[i, :2], X[j, :2]
            if key in part or key in dot:
                isdot = key in dot
                ax.plot(*zip(p, q), color=C["muted"] if isdot else C["good"], lw=PX["stroke"] * 1.4,
                        ls=(0, (1.5, 3)) if isdot else (0, (4, 3)), zorder=2)
                if dlabel and key not in {tuple(sorted(k)) for k in nolabel}:
                    m = (p + q) / 2
                    ax.text(m[0] + 4, m[1], f"{d:.2f} Å", fontsize=PX["small"], va="center",
                            color=C["muted"] if isdot else C["good"], zorder=5)
            elif d < 1.15 * (COV[S[i]] + COV[S[j]]) and key not in skip:
                back = (X[i, 2] + X[j, 2]) / 2 < zmid
                ax.plot(*zip(p, q), color=C["muted"] if back else C["ink"], lw=PX["stroke"] * (1.0 if back else 1.6),
                        solid_capstyle="round", zorder=1 if back else 3)
    for i in range(n):
        if S[i] == "C":
            continue
        txt = S[i] + ((charges or {}).get(i, ""))
        ax.text(X[i, 0], X[i, 1], txt, fontsize=PX["label"], ha="center", va="center", color=C[(colors or {}).get(i, "ink")], zorder=6,
                bbox=dict(boxstyle="circle,pad=0.08", fc=C["card"], ec="none"))
    if labels:
        for i, (txt, dx, dy) in labels.items():
            ax.text(X[i, 0] + dx * ANG2PX, X[i, 1] + dy * ANG2PX, txt, fontsize=PX["small"], color=C["muted"],
                    zorder=7, ha="center")
    return X


def fit(fig, ax, margin=10):
    """데이터 범위에 맞춰 1 데이터 단위 = 1 px가 되도록 그림 크기를 정한다."""
    ax.relim(); ax.autoscale_view()
    fig.canvas.draw()
    bb = ax.dataLim
    x0, x1, y0, y1 = bb.x0 - margin, bb.x1 + margin, bb.y0 - margin, bb.y1 + margin
    ax.set_xlim(x0, x1); ax.set_ylim(y0, y1)
    ax.set_position([0, 0, 1, 1])
    fig.set_size_inches((x1 - x0) / 72, (y1 - y0) / 72)
