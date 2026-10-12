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
   "bonds":    [[a, b, 차수, 표시, 색], ...]          표시: plain/wedge/hash/dashed/bold
   "arrows":   [[x1, y1, x2, y2, 종류], ...]          직선 화살표. 종류: forward(기본), resonance, equilibrium, retro
   "captions": [[텍스트, x, y, 색, 크기pt], ...]      (x, y)는 텍스트 왼쪽 위, 크기 기본 8pt
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
                      conditions=r.get("conditions", ""), arrow=r.get("arrow", "forward"),
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
    captions = [dict(text=c[0], position=dict(x=c[1], y=c[2]), color=None) for c in spec.get("captions", [])]
    abbreviations = [dict(label=a[0], anchor=a[1], atoms=a[2]) for a in spec.get("abbrev", [])]
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
    """원자 중심에서 비공유 전자쌍까지의 변위. 라벨은 가로가 넓어서 타원으로 잡는다."""
    r = math.radians(ang)
    return 21.0 * math.cos(r), -17.0 * math.sin(r)


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
    # 표시 크기: 결합 하나가 화면에서 약 26px
    m = re.search(r'viewBox="([-0-9.e]+) ([-0-9.e]+) ([-0-9.e]+) ([-0-9.e]+)"', svg)
    x, y, w, h = map(float, m.groups())
    svg = re.sub(r'width="[^"]+" height="[^"]+"', f'width="{w * 0.62:.0f}" height="{h * 0.62:.0f}"', svg, count=1)
    card = f'<rect class="card" x="{x:.3f}" y="{y:.3f}" width="{w:.3f}" height="{h:.3f}" rx="14"/>'
    return svg.replace(">", ">" + style_block() + card, 1)


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
            r = subprocess.run([reshiki_bin(), "--cli", "compose", pj, "-o", raw],
                               capture_output=True, text=True, timeout=120)
            if r.returncode != 0:
                sys.exit("reshiki compose 오류: " + r.stderr.strip())
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
                json.dump(doc, f)
            if spec.get("keep_rsk"):
                with open(os.path.splitext(out)[0] + ".rsk", "w") as f:
                    json.dump(doc, f, indent=1)
            convert_to_svg(final, raw)
        with open(raw) as f:
            svg = theme_svg(f.read())
    with open(out, "w") as f:
        f.write(svg)
    print(out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for p in sys.argv[1:]:
        build(p)
