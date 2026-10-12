#!/usr/bin/env python3
"""위키 목록 문서와 강의 노트의 '관련 위키 문서' 블록을 만들고, 위키링크를 검사한다.

사용법:
    python3 tools/build_wiki_index.py          # 목록 생성 + 강의 노트 블록 갱신 + 링크 검사
    python3 tools/build_wiki_index.py --check  # 링크 검사만

위키 문서의 머리말(frontmatter)에서 aliases, 분류, 태그, 강의를 읽고,
본문의 첫 '>' 줄을 한 줄 요약으로 쓴다.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
NOTES = os.path.join(ROOT, "notes")
CATEGORIES = ["반응", "시약", "개념"]
START = "<!-- wiki-links:start -->"
END = "<!-- wiki-links:end -->"


def parse_list(value):
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        return [v.strip().strip("'\"") for v in value[1:-1].split(",") if v.strip()]
    return [value] if value else []


def read_doc(path):
    text = open(path, encoding="utf-8").read()
    meta = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    title = os.path.splitext(os.path.basename(path))[0]
    h1 = re.search(r"^# (.+)$", text, re.M)
    summary = ""
    s = re.search(r"^> (.+)$", text, re.M)
    if s:
        summary = s.group(1).strip()
    lectures = []
    for item in parse_list(meta.get("강의", "")):
        lectures += re.findall(r"L(\d+)", item)
    return {
        "path": path,
        "file": title,
        "title": h1.group(1).strip() if h1 else title,
        "aliases": parse_list(meta.get("aliases", "")),
        "category": meta.get("분류", os.path.basename(os.path.dirname(path))),
        "lectures": sorted({int(x) for x in lectures}),
        "summary": summary,
        "text": text,
    }


def load_docs():
    docs = []
    for cat in CATEGORIES:
        for p in sorted(glob.glob(os.path.join(WIKI, cat, "*.md"))):
            docs.append(read_doc(p))
    return docs


def short(summary, n=70):
    """표에 넣을 짧은 요약: 첫 문장, 위키링크는 글자만 남긴다."""
    s = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", summary)
    s = re.sub(r"\[\[([^\]]+)\]\]", r"\1", s)
    s = s.split(". ")[0]
    return s if len(s) <= n else s[: n - 1] + "…"


def link(doc):
    # 파일 이름과 제목이 다르면(예: Pd/C → Pd-C) 별칭 링크를 쓴다
    if doc["file"] == doc["title"]:
        return f"[[{doc['file']}]]"
    return f"[[{doc['file']}|{doc['title']}]]"


def build_front_page(docs):
    lines = [
        "---",
        "aliases: [위키, 대문, 목차]",
        "---",
        "# 위키 대문",
        "",
        "> 강의 순서와 상관없이 **반응, 시약, 개념(원리)** 단위로 잘게 나눈 문서 모음이다. "
        "궁금한 항목 하나만 열어 읽고, 링크를 따라 옆 문서로 넘어가며 공부하도록 만들었다.",
        "",
        "강의 순서대로 정리한 긴 문서는 [README](../README.md)의 강의 노트 목록에서 볼 수 있다. "
        "각 강의 노트 맨 위에도 그 강의와 관련된 위키 문서 목록이 있다.",
        "",
        "이 문서는 `tools/build_wiki_index.py`가 자동으로 만든다. 직접 고치지 말고 스크립트를 다시 실행한다.",
        "",
    ]
    for cat in CATEGORIES:
        items = [d for d in docs if d["category"] == cat]
        lines += [f"## {cat} ({len(items)})", "", "| 문서 | 한 줄 요약 | 강의 |", "|---|---|---|"]
        for d in sorted(items, key=lambda d: d["title"]):
            lec = ", ".join(f"L{n}" for n in d["lectures"])
            lines.append(f"| {link(d)} | {short(d['summary'])} | {lec} |")
        lines.append("")
    path = os.path.join(WIKI, "위키 대문.md")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return path


def update_lecture_notes(docs):
    changed = 0
    for path in sorted(glob.glob(os.path.join(NOTES, "L*.md"))):
        n = int(re.match(r"L(\d+)_", os.path.basename(path)).group(1))
        related = [d for d in docs if n in d["lectures"]]
        text = open(path, encoding="utf-8").read()
        block_lines = [START, "", "> **관련 위키 문서** ([[위키 대문]])"]
        for cat in CATEGORIES:
            items = sorted((d for d in related if d["category"] == cat), key=lambda d: d["title"])
            if items:
                block_lines.append(f"> - {cat}: " + ", ".join(link(d) for d in items))
        block_lines += ["", END]
        block = "\n".join(block_lines)
        if START in text:
            new = re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.S)
        else:
            # 제목(H1) 바로 아래에 넣는다
            new = re.sub(r"^(# .+\n)", lambda m: m.group(1) + "\n" + block + "\n", text, count=1, flags=re.M)
        if new != text:
            open(path, "w", encoding="utf-8").write(new)
            changed += 1
    return changed


def check_links(docs):
    names = set()
    for d in docs:
        names |= {d["file"], d["title"], *d["aliases"]}
    names.add("위키 대문")
    broken = []
    files = [d["path"] for d in docs] + glob.glob(os.path.join(NOTES, "*.md"))
    front = os.path.join(WIKI, "위키 대문.md")
    if os.path.exists(front):
        files.append(front)
    for path in files:
        text = open(path, encoding="utf-8").read()
        for target in re.findall(r"\[\[([^\]|#]+)", text):
            if target.strip() not in names:
                broken.append((os.path.relpath(path, ROOT), target))
    return broken


def main():
    docs = load_docs()
    if "--check" not in sys.argv:
        print("목록:", os.path.relpath(build_front_page(docs), ROOT))
        print("강의 노트 갱신:", update_lecture_notes(docs))
    broken = check_links(docs)
    print(f"위키 문서 {len(docs)}개, 깨진 위키링크 {len(broken)}개")
    for path, target in broken:
        print(f"  {path}: [[{target}]]")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
