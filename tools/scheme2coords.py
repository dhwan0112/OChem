#!/usr/bin/env python3
"""SMILES 반응식(scheme) → 좌표 스펙(atoms/bonds) 변환기. 역할 색을 넣은 단계 그림용.

사용법: RESHIKI=... python3 tools/scheme2coords.py 정의.json
정의.json: {"out": "figures/L01/이름.json", "title": "... (L1 p.N)",
           "reactants": ["SMILES", ...], "products": [...], "conditions": "...", "below": "..."}
SMILES 원자 맵 번호로 역할 색을 준다: :1 nu(파랑), :2 el(빨강), :3 good(초록).
두 원자가 같은 역할이면 그 사이 결합도 같은 색이 된다. 맵 번호는 그림에 남지 않는다.
배치는 기존 단계 그림(L01/e2_2_bromobutane 등)과 같다: 분자 세로 중심 y=0,
'+' 10pt, 화살표 길이 2.8, 조건 글자는 화살표 위.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chemfig as cf

ROLE = {1: "nu", 2: "el", 3: "good"}


def compose_mol(smiles, td):
    sc = {"reactions": [], "molecules": [smiles]}
    m = cf.Mcp(td)
    try:
        r = m.call("compose", {"proposal": cf.scheme_proposal(sc), "style_document": None})
        p = os.path.join(td, "m.rsk")
        m.call("file_save", {"document": r["value"]["document"], "path": p, "format": None,
                             "overwrite": True, "pages": None})
    finally:
        m.close()
    return json.load(open(p))


def tw(t, size=8):  # 대략적인 글자 폭(결합 단위)
    return len(t) * size * 0.042


def build(defn, td):
    atoms, bonds, caps, arrows, abbrev = [], [], [], [], []
    x = 0.0
    def place(smi):
        nonlocal x
        d = compose_mol(smi, td)
        A = d["atoms"]
        xs = [a["position"]["x"] / 42 for a in A]; ys = [a["position"]["y"] / 42 for a in A]
        x0, cy = min(xs), (min(ys) + max(ys)) / 2
        lab = [a for a in A if a["element"] != "C"]
        ll = [a for a in lab if abs(a["position"]["x"] / 42 - x0) < 0.05]
        pad = (0.5 + 0.3 * max(a.get("label_h", 0) for a in ll)) if ll else 0.0
        idx = {}
        for a in A:
            role = ROLE.get(a.get("map_num", 0))
            e = [a["element"], round(a["position"]["x"] / 42 - x0 + x + pad, 3),
                 round(a["position"]["y"] / 42 - cy, 3), a["charge"], a.get("explicit_h", 0) or (a.get("label_h", 0) if a["element"] != "C" else 0)]
            if role: e.append(role)
            idx[a["id"]] = len(atoms); atoms.append(e)
            if a["element"] == "H" and a.get("isotope") == 2: abbrev.append(["D", len(atoms) - 1, [len(atoms) - 1]])
        for b in d["bonds"]:
            i, j = idx[b["a"]], idx[b["b"]]
            ri = atoms[i][5] if len(atoms[i]) > 5 else None
            rj = atoms[j][5] if len(atoms[j]) > 5 else None
            disp = {"wedge": "wedge", "hash": "hash"}.get((b.get("stereo") or {}).get("kind") if isinstance(b.get("stereo"), dict) else b.get("display"), "plain")
            e = [i, j, b["order"], disp]
            if ri and ri == rj: e.append(ri)
            bonds.append(e)
        right = max(xs) - x0 + x + pad
        rlab = any(abs(a["position"]["x"] / 42 - max(xs)) < 0.05 for a in lab)
        x = right + (0.5 + 0.3 * max([a.get("label_h", 0) for a in lab if abs(a["position"]["x"] / 42 - max(xs)) < 0.05] + [0]) if rlab else 0.0)
    def plus():
        nonlocal x
        caps.append(["+", x + 0.75, -0.4, "ink", 10]); x += 1.9
    for k, s in enumerate(defn["reactants"]):
        if k: plus()
        place(s)
    L = max(2.8, tw(defn.get("conditions", "")) + 0.8, tw(defn.get("below", "")) + 0.8)
    a0 = x + 0.5
    arrows.append([a0, 0.0, a0 + L, 0.0, defn.get("arrow", "forward")])
    if defn.get("conditions"):
        caps.append([defn["conditions"], a0 + (L - tw(defn["conditions"])) / 2, -0.95, "ink"])
    if defn.get("below"):
        caps.append([defn["below"], a0 + (L - tw(defn["below"])) / 2, 0.25, "muted"])
    x = a0 + L + 0.5
    for k, s in enumerate(defn["products"]):
        if k: plus()
        place(s)
    for c in defn.get("captions", []):
        caps.append(c)
    return {"title": defn.get("title", ""), "atoms": atoms, "bonds": bonds, "arrows": arrows, "captions": caps, **({"abbrev": abbrev} if abbrev else {})}


if __name__ == "__main__":
    import tempfile
    for p in sys.argv[1:]:
        defs = json.load(open(p))
        for d in (defs if isinstance(defs, list) else [defs]):
            with tempfile.TemporaryDirectory() as td:
                spec = build(d, td)
            json.dump(spec, open(d["out"], "w"), ensure_ascii=False)
            print(d["out"])
