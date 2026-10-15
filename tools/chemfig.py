#!/usr/bin/env python3
"""ReShiki 기반 반응/메커니즘 그림 생성기 (다크 모드 자동 대응 SVG).

사용법:
    export RESHIKI=/path/to/reshiki        # ReShiki 실행 파일
    python3 tools/chemfig.py figures/L01/*.json

스펙(JSON) 형식 두 가지:

1) "scheme": SMILES로 자동 배치하는 반응식
   {"scheme": {"reactions": [{"reactants": ["C=C", ...], "products": [...],
                              "conditions": "HBr", "title": "", "arrow": "forward"}],
               "molecules": [], "columns": 1, "width_pt": 540}}
   분자는 "SMILES" 문자열 또는 {"smiles": ..., "label": ...}.

2) 좌표를 직접 지정하는 메커니즘 그림 (결합 길이 1 단위, x 오른쪽, y 아래)
   "atoms":    [[원소, x, y, 전하, 수소수, 색], ...]   (뒤쪽 항목은 생략 가능)
   "bonds":    [[a, b, 차수, 표시, 색], ...]          표시: plain/wedge/hash/dashed/bold (점선 형성 결합은 차수 5와 함께: [a, b, 5, "dashed", 색])
   "arrows":   [[x1, y1, x2, y2, 종류], ...]          직선 화살표. 종류: forward(기본), resonance, equilibrium, retro
   "captions": [[텍스트, x, y, 색, 크기pt], ...]      (x, y)는 텍스트 왼쪽 위, 크기 기본 8pt
   "shapes":   [{"lobe": [...]}, {"line": [...]}]     p 오비탈 로브와 점선 (add_shapes 참고)
   "abbrev":   [[라벨, 기준 원자, [원자들]], ...]       예: ["CH3", 2, [2]]로 메틸을 CH3 라벨로 접기
   "lone_pairs": [[원자, 각도], ...]                  각도: 90 위, 0 오른쪽, 180 왼쪽, 270 아래
   "curved": [{"from": 끝점, "to": 끝점, "bend": 0.5, "color": "arrow", "kind": "curved"}]
      끝점: {"atom": i} | {"bond": [a, b]} | {"lp": [원자, 각도]} | {"pt": [x, y]}
      끝점에 "gap": 간격(pt, 기본 2), "offset": [dx, dy](결합 단위),
      "dir": 닿는 방향 각도(기본: 곡선이 다가오는 방향)를 더할 수 있다.
      kind: "curved"(전자쌍) | "fishhook"(전자 하나)
      bend: 곡률. 양수면 진행 방향의 왼쪽(화면 기준 반시계)으로 휜다.

색 이름: ink(기본), arrow(전자 이동), nu(친핵체), el(친전자체), good, muted.
출력 SVG는 prefers-color-scheme에 따라 라이트/다크 색이 자동으로 바뀐다.

원리: 좌표 그림은 ReShiki MCP의 compose로 기본 문서를 만든 뒤 .rsk(JSON)에
굽은 화살표(atom/bond/lone_pair에 부착), 비공유 전자쌍 마크, 색을 넣고
reshiki --cli convert로 SVG를 만든다.
"""
import json
import math
import os
import re
import subprocess
import sys
import tempfile

SCALE = 42.0  # ReShiki 기본 스타일에서 결합 길이 1 = 42 단위

# (라이트, 다크) 색상
PALETTE = {
    "ink": ("#1b1b1f", "#e6e6ea"),
    "arrow": ("#c2410c", "#ff9f5a"),
    "nu": ("#1d4ed8", "#8ab4ff"),
    "el": ("#b91c1c", "#ff8a8a"),
    "good": ("#15803d", "#6ee7a0"),
    "muted": ("#6b7280", "#9ca3af"),
}
# ReShiki 문서에 넣을 표식 RGB. 후처리에서 CSS 클래스로 바꾼다.
SENTINEL = {
    "ink": (0, 0, 0),
    "nu": (1, 2, 250),
    "el": (250, 2, 1),
    "good": (2, 250, 1),
    "arrow": (250, 120, 3),
    "muted": (120, 121, 122),
}


def reshiki_bin():
    path = os.environ.get("RESHIKI")
    if not path or not os.path.exists(path):
        sys.exit("RESHIKI 환경변수에 reshiki 실행 파일 경로를 지정하세요.")
    return path


class Mcp:
    """reshiki --mcp 에 붙는 최소 JSON-RPC 클라이언트."""

    def __init__(self, folder):
        self.p = subprocess.Popen(
            [reshiki_bin(), "--mcp", "--allow-read", folder, "--allow-write", folder],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        self.i = 0
        self._req("initialize", {"protocolVersion": "2024-11-05", "capabilities": {},
                                 "clientInfo": {"name": "chemfig", "version": "1"}})
        self._send({"jsonrpc": "2.0", "method": "notifications/initialized"})

    def _send(self, obj):
        self.p.stdin.write(json.dumps(obj) + "\n")
        self.p.stdin.flush()

    def _req(self, method, params):
        self.i += 1
        self._send({"jsonrpc": "2.0", "id": self.i, "method": method, "params": params})
        while True:
            line = self.p.stdout.readline()
            if not line:
                sys.exit("reshiki --mcp 가 응답 없이 종료되었습니다.")
            d = json.loads(line)
            if d.get("id") == self.i:
                return d

    def call(self, name, args):
        d = self._req("tools/call", {"name": name, "arguments": args})
        res = d.get("result", {})
        text = res.get("content", [{}])[0].get("text", "")
        if "error" in d or res.get("isError"):
            sys.exit(f"reshiki {name} 오류: {text or d.get('error')}")
        return json.loads(text)

    def close(self):
        self.p.stdin.close()
        self.p.wait(timeout=10)


# ---------------- 표기 정리(기본 적용) ----------------

_SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
_NOT_FORMULA = {"SN1", "SN2", "SE2", "E1", "E2", "E1cB", "L1", "L2", "L3"}
_FORMULA_TOKEN = re.compile(r"^[(\[]*(?:[A-Z][a-z]?|\(|\)|Et|Me|Ph|Bu|Pr|Ac|Ts|Ms)[A-Za-z0-9()\[\]⁺⁻+=]*$")


def subscript_formulas(text):
    """캡션·조건의 화학식 숫자를 아래첨자로: (COCl)2 → (COCl)₂, CH2Cl2 → CH₂Cl₂, Et3N → Et₃N.
    SN2·E2 같은 반응 이름, 단계 번호(1. 2.), 페이지(p.7), 온도·당량 숫자는 건드리지 않는다."""
    def tok(m):
        t = m.group(0)
        core = t.strip("()[],;:")
        if core in _NOT_FORMULA or re.match(r"^L\d", core) or not _FORMULA_TOKEN.match(t) or not re.search(r"[A-Za-z)\]]\d", t):
            return t
        return re.sub(r"(?<=[A-Za-z)\]])(\d+)", lambda d: d.group(1).translate(_SUB), t)
    return re.sub(r"[^\s,;/]+", tok, text)


# ReShiki는 약어 라벨 안의 '-'를 음전하 윗첨자로 바꾼다(t-Bu → t⁻Bu). 접두 이성질체 기호는 윗첨자 글자로.
_ISO_PREFIX = {"t-": "ᵗ", "i-": "ⁱ", "n-": "ⁿ", "s-": "ˢ", "tert-": "ᵗ", "sec-": "ˢ", "iso-": "ⁱ"}


def fix_abbrev_label(label):
    for k, v in _ISO_PREFIX.items():
        if label.startswith(k):
            return v + label[len(k):]
    return label


# ---------------- 스펙 -> ReShiki 제안(Proposal) ----------------

def mol_entry(m):
    if isinstance(m, str):
        m = {"smiles": m}
    return dict(smiles=m["smiles"], label=m.get("label", ""), coefficient=m.get("coefficient", 1),
                rotation=m.get("rotation", 0), compact=False)


def scheme_proposal(sc):
    comp = dict(arrangement=sc.get("arrangement", "rows"), columns=sc.get("columns", 1),
                width_pt=sc.get("width_pt", 540), preserve_details=True)
    reactions = [dict(reactants=[mol_entry(m) for m in r["reactants"]],
                      products=[mol_entry(m) for m in r["products"]],
                      conditions=subscript_formulas(r.get("conditions", "")), arrow=r.get("arrow", "forward"),
                      title=r.get("title", ""), role="main", direction=None)
                 for r in sc.get("reactions", [])]
    return dict(explanation="", replace_ids=[], composition=comp,
                molecules=[mol_entry(m) for m in sc.get("molecules", [])],
                reactions=reactions, sketch=None)


def sketch_proposal(spec):
    atoms = [dict(element=a[0], x=a[1], y=a[2], charge=a[3] if len(a) > 3 else 0, isotope=0,
                  hydrogens=a[4] if len(a) > 4 else 0, color=None, variable=None)
             for a in spec.get("atoms", [])]
    bonds = [dict(a=b[0], b=b[1], order=b[2] if len(b) > 2 else 1,
                  display=b[3] if len(b) > 3 else "plain", ring_arc=False)
             for b in spec.get("bonds", [])]
    arrows = [dict(start=dict(x=a[0], y=a[1]), end=dict(x=a[2], y=a[3])) for a in spec.get("arrows", [])]
    captions = [dict(text=subscript_formulas(c[0]), position=dict(x=c[1], y=c[2]), color=None) for c in spec.get("captions", [])]
    abbreviations = [dict(label=fix_abbrev_label(a[0]), anchor=a[1], atoms=a[2]) for a in spec.get("abbrev", [])]
    sketch = dict(atoms=atoms, bonds=bonds, shapes=[], tilts=[], centroids=[], arrows=arrows,
                  captions=captions, abbreviations=abbreviations, ligands=[])
    comp = dict(arrangement="rows", columns=1, width_pt=540, preserve_details=True)
    return dict(explanation="", replace_ids=[], composition=comp, molecules=[], reactions=[], sketch=sketch)


# ---------------- .rsk 문서 편집 ----------------

def rgb(name):
    return list(SENTINEL[name or "ink"])


def anchor(target, e, toward):
    """화살표를 원자/결합/전자쌍에 붙인다.
    direction은 화살표 끝이 대상에 닿는 쪽(대상에서 바깥을 향하는 단위 벡터)이다.
    기본값은 곡선의 제어점 쪽, 즉 곡선이 실제로 다가오는 방향이다.
    "dir": 각도(90 위, 0 오른쪽)로 직접 지정할 수 있다.
    gap은 대상과 화살표 끝 사이 간격(pt), offset은 부착점 이동(결합 단위)이다."""
    if "dir" in e:
        r = math.radians(e["dir"])
        dx, dy = math.cos(r), -math.sin(r)
    else:
        dx, dy = toward
    off = e.get("offset", [0, 0])
    return {"target": target, "offset": {"x": off[0] * SCALE, "y": off[1] * SCALE},
            "direction": {"x": dx, "y": dy}, "gap": e.get("gap", 2)}


def lp_offset(ang):
    """원자 중심에서 비공유 전자쌍까지의 변위.
    10 pt 라벨(29.2 단위) 한 글자 O/N 글리프의 반폭 ≈ 11.4, 반높이(cap) ≈ 10.6에
    점 반지름(1.2)과 작은 틈(~2)을 더해 점이 글리프에 바로 붙도록 한다.
    (이전 값 21/17은 글리프에서 약 9 단위 떨어져 보였다.)"""
    r = math.radians(ang)
    return LP_RX * math.cos(r), -LP_RY * math.sin(r)


LP_RX, LP_RY = 14.5, 14.0


def decorate(doc, spec):
    """compose가 만든 문서에 색, 비공유 전자쌍, 굽은 화살표를 넣는다."""
    atoms = doc["atoms"]  # compose는 스펙의 원자 순서대로 원자를 만든다
    if len(atoms) != len(spec.get("atoms", [])):
        sys.exit("원자 수가 스펙과 다릅니다. compose 결과를 확인하세요.")
    for a, s in zip(atoms, spec["atoms"]):
        want = (round(s[1] * SCALE, 3), round(s[2] * SCALE, 3))
        got = (round(a["position"]["x"], 3), round(a["position"]["y"], 3))
        if want != got:
            sys.exit(f"원자 좌표가 어긋났습니다: {want} != {got}")
        if len(s) > 5 and s[5]:
            a["text_style"]["color"] = rgb(s[5])
    ids = [a["id"] for a in atoms]
    by_pair = {}
    for b in doc["bonds"]:
        by_pair[frozenset((b["a"], b["b"]))] = b
    for s in spec.get("bonds", []):
        if len(s) > 4 and s[4]:
            by_pair[frozenset((ids[s[0]], ids[s[1]]))]["color"] = rgb(s[4])
    for ann, s in zip(doc.get("annotations", []), spec.get("captions", [])):
        if len(s) > 3 and s[3]:
            ann["format"]["style"]["color"] = rgb(s[3])
        # 캡션은 원자 라벨(10pt)보다 작게. 다섯 번째 항목으로 크기(pt)를 지정할 수 있다.
        ann["format"]["style"]["size_pt"] = float(s[4]) if len(s) > 4 else 8.0

    # 직선 화살표 종류: [x1, y1, x2, y2, "forward"|"resonance"|"equilibrium"|"retro"]
    for arr, sa in zip(doc.get("arrows", []), spec.get("arrows", [])):
        if len(sa) > 4:
            arr["kind"] = sa[4]

    next_id = max([x["id"] for k in ("atoms", "annotations", "arrows", "graphics", "groups")
                   for x in doc.get(k, [])] + [0]) + 1
    marks = {}  # (원자 인덱스, 각도) -> mark id

    def lone_pair(i, ang):
        nonlocal next_id
        key = (i, ang)
        if key in marks:
            return marks[key]
        r = math.radians(ang)
        ox, oy = lp_offset(ang)
        mark = {"id": next_id, "kind": "lone_pair", "angle": float((ang - 90) % 360),
                "offset": {"x": ox, "y": oy}, "size_pt": 4.0}
        atoms[i].setdefault("marks", []).append(mark)
        marks[key] = next_id
        next_id += 1
        return marks[key]

    for lp in spec.get("lone_pairs", []):
        lone_pair(lp[0], lp[1])

    def point_and_target(e):
        if "atom" in e:
            i = e["atom"]
            p = atoms[i]["position"]
            return (p["x"], p["y"]), {"kind": "atom", "atom": ids[i]}
        if "bond" in e:
            a, b = e["bond"]
            pa, pb = atoms[a]["position"], atoms[b]["position"]
            stored = by_pair.get(frozenset((ids[a], ids[b])))
            if stored is None:
                sys.exit(f"결합 {e['bond']}이 문서에 없습니다.")
            # ReShiki는 문서에 저장된 원자 순서로 결합을 찾는다
            return (((pa["x"] + pb["x"]) / 2, (pa["y"] + pb["y"]) / 2),
                    {"kind": "bond", "a": min(stored["a"], stored["b"]), "b": max(stored["a"], stored["b"]), "fraction": 0.5})
        if "lp" in e:
            i, ang = e["lp"]
            m = lone_pair(i, ang)
            p = atoms[i]["position"]
            ox, oy = lp_offset(ang)
            return ((p["x"] + ox, p["y"] + oy),
                    {"kind": "lone_pair", "atom": ids[i], "mark": m})
        return (e["pt"][0] * SCALE, e["pt"][1] * SCALE), None

    for c in spec.get("curved", []):
        (x0, y0), t0 = point_and_target(c["from"])
        (x1, y1), t1 = point_and_target(c["to"])
        bend = c.get("bend", 0.5)
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy) or 1.0
        # 화면 좌표(y 아래)에서 진행 방향의 왼쪽 법선은 (dy, -dx)
        nx, ny = dy / L, -dx / L
        ctrl = {"x": (x0 + x1) / 2 + nx * bend * L, "y": (y0 + y1) / 2 + ny * bend * L}
        arrow = {"id": next_id, "start": {"x": x0, "y": y0}, "end": {"x": x1, "y": y1},
                 "kind": c.get("kind", "curved"), "control": ctrl,
                 "style": {"color": rgb(c.get("color", "arrow"))}}
        def unit(px, py):
            vx, vy = ctrl["x"] - px, ctrl["y"] - py
            n = math.hypot(vx, vy) or 1.0
            return vx / n, vy / n
        if t0:
            arrow["start_anchor"] = anchor(t0, c["from"], unit(x0, y0))
        if t1:
            arrow["end_anchor"] = anchor(t1, c["to"], unit(x1, y1))
        doc["arrows"].append(arrow)
        next_id += 1
    return doc


# ---------------- 렌더링과 다크 모드 후처리 ----------------

def fix_font(txt):
    """기존 그림과 같은 글꼴(DejaVu Sans)로 고정한다. ReShiki nightly는 Arial을 Noto Sans CJK로 대체해 글자가 작고 가늘어 보인다."""
    return txt.replace('"family":"Arial"', '"family":"DejaVu Sans"').replace('"family": "Arial"', '"family": "DejaVu Sans"')


def convert_to_svg(src, out):
    r = subprocess.run([reshiki_bin(), "--cli", "convert", src, "-o", out, "--force"],
                       capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        sys.exit("reshiki convert 오류: " + r.stderr.strip())


# 배경 카드 (라이트, 다크). 옵시디언 기본 테마의 배경색과 같다.
# 뷰어의 테마와 운영체제의 다크/라이트 설정이 달라도 선과 글자가 항상 읽히게 한다.
CARD = ("#ffffff", "#1e1e1e")


def style_block():
    light = "".join(f".c-{k}.fill{{fill:{v[0]}}}.c-{k}.stroke{{stroke:{v[0]}}}" for k, v in PALETTE.items())
    dark = "".join(f".c-{k}.fill{{fill:{v[1]}}}.c-{k}.stroke{{stroke:{v[1]}}}" for k, v in PALETTE.items())
    light += f".card{{fill:{CARD[0]}}}"
    dark += f".card{{fill:{CARD[1]}}}"
    return f"<style>{light}@media (prefers-color-scheme: dark){{{dark}}}</style>"


def theme_svg(svg):
    """흰 배경을 없애고 표식 색을 라이트/다크 전환 CSS 클래스로 바꾼다."""
    svg = re.sub(r'<rect [^>]*fill="rgb\(255,255,255\)"/>\n?', "", svg, count=1)
    names = {f"rgb({r},{g},{b})": n for n, (r, g, b) in SENTINEL.items()}

    def tag(m):
        el = m.group(0)
        name, kinds = None, []
        for attr in ("fill", "stroke"):
            mm = re.search(attr + r'="(rgb\([0-9,]+\))"', el)
            if mm and mm.group(1) in names:
                name = name or names[mm.group(1)]
                kinds.append(attr)
                el = el.replace(mm.group(0), "")
        if name:
            el = el.replace("<" + m.group(1), f'<{m.group(1)} class="c-{name} {" ".join(kinds)}"', 1)
        return el

    svg = re.sub(r"<(line|path|text|circle|ellipse|polygon|polyline)\b[^>]*?/?>", tag, svg)
    # 한글이 섞인 캡션도 깨지지 않게 글꼴 대체 목록을 붙인다
    svg = re.sub(r'font-family="(DejaVu Sans|Noto Sans CJK JP)"',
                 'font-family="DejaVu Sans, Noto Sans CJK KR, Noto Sans CJK JP, sans-serif"', svg)
    # 표시 크기: 결합 하나가 화면에서 약 26px
    m = re.search(r'viewBox="([-0-9.e]+) ([-0-9.e]+) ([-0-9.e]+) ([-0-9.e]+)"', svg)
    x, y, w, h = map(float, m.groups())
    svg = re.sub(r'width="[^"]+" height="[^"]+"', f'width="{w * 0.62:.0f}" height="{h * 0.62:.0f}"', svg, count=1)
    card = f'<rect class="card" x="{x:.3f}" y="{y:.3f}" width="{w:.3f}" height="{h:.3f}" rx="14"/>'
    return svg.replace(">", ">" + style_block() + card, 1)


def add_shapes(svg, shapes):
    """ReShiki가 못 그리는 도형(p 오비탈 로브, 점선)을 같은 좌표계(결합 길이 1 = 42)로 덧붙인다.
    {"lobe": [x, y, 크기, 기울기(도, 시계 방향), 부호(+1 위 로브 채움 / -1), 색, 불투명도]}
    {"line": [x1, y1, x2, y2, 색, "dash"|"dot"|"solid"]}
    {"eq": [x1, y1, x2, y2, 색, 선굵기, 촉 길이, 촉 높이, 간격]}  평형 화살표 ⇌ (x1,y1 → x2,y2 방향이 정반응)
    """
    els, xs, ys = [], [], []
    sw = 1.7500001
    for sh in shapes:
        if "lobe" in sh:
            x, y, size, tilt, sign, *rest = sh["lobe"]
            col = rest[0] if rest else "nu"
            op = rest[1] if len(rest) > 1 else 1.0
            a = math.radians(tilt)
            ux, uy = math.sin(a), -math.cos(a)  # 화면에서 '위' 로브 방향
            rx, ry = 0.20 * size * SCALE, 0.40 * size * SCALE
            for k, sg in ((1, sign), (-1, -sign)):
                cx = (x + ux * k * 0.42 * size) * SCALE
                cy = (y + uy * k * 0.42 * size) * SCALE
                cls = f"c-{col} fill stroke" if sg > 0 else f"c-{col} stroke"
                fill = "" if sg > 0 else ' fill="none"'
                els.append(f'<ellipse class="{cls}"{fill} cx="{cx:.2f}" cy="{cy:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" '
                           f'transform="rotate({tilt} {cx:.2f} {cy:.2f})" stroke-width="{sw}" opacity="{op}"/>')
                r = max(rx, ry)
                xs += [cx - r, cx + r]; ys += [cy - r, cy + r]
        elif "line" in sh:
            x1, y1, x2, y2, col, kind = sh["line"]
            dash = {"dash": ' stroke-dasharray="7 5"', "dot": ' stroke-dasharray="2 4"', "solid": ""}[kind]
            els.append(f'<line class="c-{col} stroke" x1="{x1*SCALE:.2f}" y1="{y1*SCALE:.2f}" x2="{x2*SCALE:.2f}" '
                       f'y2="{y2*SCALE:.2f}" stroke-width="{sw}" stroke-linecap="round"{dash}/>')
            xs += [x1 * SCALE, x2 * SCALE]; ys += [y1 * SCALE, y2 * SCALE]
        elif "eq" in sh:
            # 평형 화살표 ⇌ (굵은 반화살촉 두 개): [x1, y1, x2, y2, 색, 선굵기, 촉 길이, 촉 높이, 두 선 사이 간격] (길이는 SVG 단위)
            x1, y1, x2, y2, *rest = sh["eq"]
            col = rest[0] if rest else "ink"
            w_, bl, bh, sep = (list(rest[1:5]) + [3.2, 21.0, 11.0, 11.0][len(rest[1:5]):])[:4]
            p1, p2 = (x1 * SCALE, y1 * SCALE), (x2 * SCALE, y2 * SCALE)
            ln = math.hypot(p2[0] - p1[0], p2[1] - p1[1]) or 1.0
            ux, uy = (p2[0] - p1[0]) / ln, (p2[1] - p1[1]) / ln
            nx, ny = uy, -ux  # 진행 방향의 왼쪽 법선(화면 좌표)
            for (a, b, side, d) in ((p1, p2, 1, 1), (p2, p1, -1, -1)):
                ox, oy = side * sep / 2 * nx, side * sep / 2 * ny
                ax, ay, bx, by = a[0] + ox, a[1] + oy, b[0] + ox, b[1] + oy
                els.append(f'<line class="c-{col} stroke" x1="{ax:.2f}" y1="{ay:.2f}" x2="{bx:.2f}" y2="{by:.2f}" '
                           f'stroke-width="{w_}" stroke-linecap="butt"/>')
                tx, ty = d * ux, d * uy
                pts = [(bx, by), (bx - bl * tx + side * bh * nx, by - bl * ty + side * bh * ny),
                       (bx - 0.7 * bl * tx, by - 0.7 * bl * ty)]
                els.append(f'<polygon class="c-{col} fill" points="' + " ".join(f"{px:.2f},{py:.2f}" for px, py in pts) + '"/>')
                xs += [bx, ax, pts[1][0]]; ys += [by, ay, pts[1][1]]
    m = re.search(r'viewBox="([-0-9.e]+) ([-0-9.e]+) ([-0-9.e]+) ([-0-9.e]+)"', svg)
    x, y, w, h = map(float, m.groups())
    pad = 11.666667
    nx, ny = min(x, min(xs) - pad), min(y, min(ys) - pad)
    nw, nh = max(x + w, max(xs) + pad) - nx, max(y + h, max(ys) + pad) - ny
    svg = svg.replace(m.group(0), f'viewBox="{nx:.3f} {ny:.3f} {nw:.3f} {nh:.3f}"', 1)
    svg = re.sub(r'width="[^"]+" height="[^"]+"', f'width="{nw * 0.62:.0f}" height="{nh * 0.62:.0f}"', svg, count=1)
    svg = re.sub(r'<rect class="card"[^>]*/>', f'<rect class="card" x="{nx:.3f}" y="{ny:.3f}" width="{nw:.3f}" height="{nh:.3f}" rx="14"/>', svg, count=1)
    # 도형은 카드 바로 뒤(구조보다 아래)에 깐다
    return re.sub(r'(<rect class="card"[^>]*/>)', lambda mm: mm.group(1) + "".join(els), svg, count=1)


def build(path, out=None):
    with open(path) as f:
        spec = json.load(f)
    out = out or os.path.splitext(path)[0] + ".svg"
    with tempfile.TemporaryDirectory(dir=os.path.dirname(os.path.abspath(out))) as td:
        raw = os.path.join(td, "raw.svg")
        if "scheme" in spec:
            pj = os.path.join(td, "p.json")
            with open(pj, "w") as f:
                json.dump(scheme_proposal(spec["scheme"]), f)
            mcp = Mcp(td)
            try:
                res = mcp.call("compose", {"proposal": scheme_proposal(spec["scheme"]), "style_document": None})
                rsk0 = os.path.join(td, "scheme.rsk")
                mcp.call("file_save", {"document": res["value"]["document"], "path": rsk0,
                                       "format": None, "overwrite": True, "pages": None})
            finally:
                mcp.close()
            with open(rsk0) as f:
                txt = f.read()
            fixed = os.path.join(td, "scheme_font.rsk")
            with open(fixed, "w") as f:
                f.write(fix_font(txt))
            convert_to_svg(fixed, raw)
        else:
            mcp = Mcp(td)
            try:
                res = mcp.call("compose", {"proposal": sketch_proposal(spec), "style_document": None})
                rsk = os.path.join(td, "base.rsk")
                mcp.call("file_save", {"document": res["value"]["document"], "path": rsk,
                                       "format": None, "overwrite": True, "pages": None})
            finally:
                mcp.close()
            with open(rsk) as f:
                doc = decorate(json.load(f), spec)
            final = os.path.join(td, "final.rsk")
            with open(final, "w") as f:
                f.write(fix_font(json.dumps(doc)))
            if spec.get("keep_rsk"):
                with open(os.path.splitext(out)[0] + ".rsk", "w") as f:
                    json.dump(doc, f, indent=1)
            convert_to_svg(final, raw)
        with open(raw) as f:
            svg = theme_svg(f.read())
        if spec.get("shapes"):
            svg = add_shapes(svg, spec["shapes"])
    with open(out, "w") as f:
        f.write(svg)
    print(out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for p in sys.argv[1:]:
        build(p)
