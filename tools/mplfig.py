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
SENT = {"card": "#fefefd", "ink": "#010101", "arrow": "#fe7f00", "nu": "#0000fe", "el": "#fe0000", "good": "#00fe00", "muted": "#7f7f7e"}
C = SENT
# chemfig 그림을 화면에 띄운 크기(px) 기준 규격 (결합 길이 42 SVG 단위 × 0.62 = 26 px)
PX = {"bond_len": 26.0, "stroke": 1.085, "label": 18.1, "caption": 14.5, "small": 12.7, "arrow": 1.6, "pad": 7.0, "rx": 8.7}  # 그림 코드에서 C["nu"]처럼 쓴다
CARD = ("#ffffff", "#1e1e1e")
plt.rcParams.update({"svg.fonttype": "none", "font.family": "DejaVu Sans", "font.size": 14.5, "lines.linewidth": 1.085,
                     "text.color": SENT["ink"], "axes.edgecolor": SENT["ink"], "axes.labelcolor": SENT["ink"],
                     "xtick.color": SENT["ink"], "ytick.color": SENT["ink"]})


def save(fig, path):
    buf = io.StringIO()
    fig.savefig(buf, format="svg", transparent=True, bbox_inches="tight", pad_inches=PX["pad"] / 72)
    plt.close(fig)
    svg = buf.getvalue()
    for k, v in SENT.items():
        svg = re.sub(v, f"var(--{k})", svg, flags=re.I)
    # matplotlib은 pt 단위로 크기를 쓴다. 72 dpi에서 1 pt = 1 px가 되도록 단위 없는 px로 바꾼다.
    svg = re.sub(r'width="([0-9.]+)pt" height="([0-9.]+)pt"', r'width="\1" height="\2"', svg, count=1)
    light = ";".join(f"--{k}:{v[0]}" for k, v in PALETTE.items() if k != 'card') + f";--card:{CARD[0]}"
    dark = ";".join(f"--{k}:{v[1]}" for k, v in PALETTE.items()) + f";--card:{CARD[1]}"
    style = f"<style>svg{{{light}}}@media (prefers-color-scheme: dark){{svg{{{dark}}}}}</style>"
    svg = re.sub(r"<metadata>.*?</metadata>", "", svg, flags=re.S)
    m = re.search(r'viewBox="([-0-9.]+) ([-0-9.]+) ([-0-9.]+) ([-0-9.]+)"', svg)
    x, y, w, h = map(float, m.groups())
    card = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{PX['rx']}" style="fill:var(--card)"/>'
    svg = re.sub(r"(<svg[^>]*>)", lambda mm: mm.group(1) + style + card, svg, count=1)
    with open(path, "w") as f:
        f.write(svg)
    print(path)
