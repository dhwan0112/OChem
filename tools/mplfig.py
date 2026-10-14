#!/usr/bin/env python3
"""matplotlib 기반 그림(3D 구조/전이 상태, 에너지 도표, 오비탈 도식)용 공통 테마.

chemfig.py와 같은 색 규칙(figures/STYLE.md)을 쓴다. 표식 색으로 그린 뒤 SVG에서
CSS 변수로 바꿔, prefers-color-scheme에 따라 라이트/다크가 자동 전환된다.
필요: numpy, matplotlib (예: conda env "chem").
"""
import io, re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PALETTE = {"ink": ("#1b1b1f", "#e6e6ea"), "arrow": ("#c2410c", "#ff9f5a"), "nu": ("#1d4ed8", "#8ab4ff"),
           "el": ("#b91c1c", "#ff8a8a"), "good": ("#15803d", "#6ee7a0"), "muted": ("#6b7280", "#9ca3af")}
SENT = {"ink": "#010101", "arrow": "#fe7f00", "nu": "#0000fe", "el": "#fe0000", "good": "#00fe00", "muted": "#7f7f7e"}
C = SENT  # 그림 코드에서 C["nu"]처럼 쓴다
CARD = ("#ffffff", "#1e1e1e")
plt.rcParams.update({"svg.fonttype": "none", "font.family": "DejaVu Sans", "font.size": 9,
                     "text.color": SENT["ink"], "axes.edgecolor": SENT["ink"], "axes.labelcolor": SENT["ink"],
                     "xtick.color": SENT["ink"], "ytick.color": SENT["ink"]})


def save(fig, path):
    buf = io.StringIO()
    fig.savefig(buf, format="svg", transparent=True, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    svg = buf.getvalue()
    for k, v in SENT.items():
        svg = re.sub(v, f"var(--{k})", svg, flags=re.I)
    light = ";".join(f"--{k}:{v[0]}" for k, v in PALETTE.items()) + f";--card:{CARD[0]}"
    dark = ";".join(f"--{k}:{v[1]}" for k, v in PALETTE.items()) + f";--card:{CARD[1]}"
    style = f"<style>svg{{{light}}}@media (prefers-color-scheme: dark){{svg{{{dark}}}}}</style>"
    svg = re.sub(r"<metadata>.*?</metadata>", "", svg, flags=re.S)
    m = re.search(r'viewBox="([-0-9.]+) ([-0-9.]+) ([-0-9.]+) ([-0-9.]+)"', svg)
    x, y, w, h = map(float, m.groups())
    card = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" style="fill:var(--card)"/>'
    svg = re.sub(r"(<svg[^>]*>)", lambda mm: mm.group(1) + style + card, svg, count=1)
    with open(path, "w") as f:
        f.write(svg)
    print(path)
