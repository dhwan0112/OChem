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
import urllib.parse
import sys

from math_notation import inline_greek, plain_greek_label, PROTECTED

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
NOTES = os.path.join(ROOT, "notes")
CATEGORIES = ["반응", "시약", "개념"]
START = "<!-- wiki-links:start -->"
END = "<!-- wiki-links:end -->"


def parse_list(value):
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return [value] if value else []
    # 쉼표로 나누되, 큰따옴표 안의 쉼표와 숫자 사이 쉼표(1,3-쌍극자 등)는 나누지 않는다
    items, cur, quoted = [], "", False
    body = value[1:-1]
    for k, ch in enumerate(body):
        if ch == '"':
            quoted = not quoted
        if ch == "," and not quoted and not (body[k - 1:k].isdigit() and body[k + 1:k + 2].isdigit()):
            items.append(cur)
            cur = ""
        else:
            cur += ch
    items.append(cur)
    return [v.strip().strip('"') for v in items if v.strip()]


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



# ---------------- 태그 체계 ----------------
# 강의 번호 -> 단원 태그
UNIT = {1: "알켄-첨가", 2: "알켄-첨가", 3: "방향족-치환", 4: "방향족-치환", 5: "환원",
        6: "산화-알켄-합성", 7: "엔올레이트", 8: "엔올레이트", 9: "엔올레이트", 10: "엔올레이트",
        11: "공액-첨가", 12: "보호기", 13: "고리화-첨가", 14: "고리화-첨가", 15: "고리화-첨가",
        # L16–L17은 슬라이드 공개 전 교과서(Clayden 35장) 기반 예습 노트
        16: "시그마트로픽-전자고리화", 17: "시그마트로픽-전자고리화"}
UNIT_NAME = {"산화-알켄-합성": "산화·알켄 합성", "시그마트로픽-전자고리화": "시그마트로픽·전자고리화"}
# 시험 범위 (수정된 일정표: Test 1 = 1–5주차, Test 2 = 6–10주차, 라디칼 제외)
def exam_scope(n):
    return "Test1" if n <= 10 else "Test2"

NAMED = {
    "인명반응": ["프리델-크래프츠 알킬화", "프리델-크래프츠 아실화", "클레멘센 환원", "콜베-슈미트 반응",
              "에슈바일러-클라크 반응", "로젠문트 환원", "스원 산화", "피닉 산화", "존스 산화", "위티그 반응",
              "HWE 반응", "무카이야마 알돌 반응", "클라이젠 축합", "교차 클라이젠 축합", "디크만 축합",
              "스토크 엔아민 반응", "마이클 반응", "로빈슨 고리 형성", "딜스-알더 반응", "역 딜스-알더 반응",
              "스타우딩거 β-락탐 합성", "린들라 환원", "크뇌베나겔 축합", "헨리 반응", "스타우딩거 환원", "클라이젠 자리옮김", "코프 자리옮김", "나자로프 고리화"],
    "인명시약": ["린들라 촉매", "DMP", "존스 시약", "TPAP", "그리냐르 시약", "에반스 옥사졸리디논", "유기구리 시약", "대니셰프스키 다이엔"],
    "인명규칙": ["마르코프니코프 규칙", "우드워드-호프만 규칙", "endo 규칙"],
}

REACTION_TYPE = {
    "친전자성-첨가": ["할로젠 첨가", "할로하이드린 형성", "할로젠화수소 첨가", "산 촉매 수화", "수소붕소화-산화",
                 "다이엔의 친전자성 첨가", "에폭시화", "다이하이드록실화"],
    "친전자성-방향족-치환": ["친전자성 방향족 치환", "방향족 할로젠화", "나이트로화", "설폰화",
                       "프리델-크래프츠 알킬화", "프리델-크래프츠 아실화", "콜베-슈미트 반응"],
    "친핵성-치환": ["에폭사이드 고리 열기", "엔올레이트 알킬화", "아자이드·나이트릴을 거친 아민 합성",
                "친핵성 방향족 치환", "첨가-제거 반응", "아세토아세트산 에스터 합성", "말론산 에스터 합성",
                "스토크 엔아민 반응", "다이아조늄 염 반응", "SN2 반응"],
    "친핵성-첨가": ["환원성 아미노화", "알돌 반응", "교차 알돌 반응", "무카이야마 알돌 반응", "분자내 알돌 반응",
                "프롤린 촉매 알돌 반응", "위티그 반응", "HWE 반응", "공액 첨가", "마이클 반응", "아세탈 형성",
                "로빈슨 고리 형성", "크뇌베나겔 축합", "헨리 반응", "이미늄 촉매 공액 첨가"],
    "친핵성-아실-치환": ["클라이젠 축합", "교차 클라이젠 축합", "디크만 축합", "펩타이드 합성", "에스터 부분 환원",
                    "아마이드 환원", "친핵성 아실 치환", "에스터 가수분해", "할로폼 반응"],
    "산화": ["에폭시화", "다이하이드록실화", "과아이오딘산 절단", "오존 분해", "알코올 산화", "스원 산화",
           "피닉 산화", "존스 산화", "TEMPO 산화", "수소붕소화-산화"],
    "환원": ["촉매 수소화", "린들라 환원", "용해 금속 환원", "클레멘센 환원", "환원성 아미노화",
           "에슈바일러-클라크 반응", "아마이드 환원", "에스터 부분 환원", "로젠문트 환원",
           "아자이드·나이트릴을 거친 아민 합성", "스타우딩거 환원", "수소화분해"],
    "제거": ["탈카복실화", "역알돌 반응"],
    "C–C-결합-형성": ["프리델-크래프츠 알킬화", "프리델-크래프츠 아실화", "콜베-슈미트 반응", "엔올레이트 알킬화",
                   "아세토아세트산 에스터 합성", "말론산 에스터 합성", "알돌 반응", "교차 알돌 반응",
                   "무카이야마 알돌 반응", "분자내 알돌 반응", "프롤린 촉매 알돌 반응", "클라이젠 축합",
                   "교차 클라이젠 축합", "디크만 축합", "스토크 엔아민 반응", "마이클 반응", "공액 첨가",
                   "로빈슨 고리 형성", "위티그 반응", "HWE 반응", "딜스-알더 반응", "광화학 2+2 고리화 첨가",
                   "케텐 2+2 고리화 첨가", "4+3 고리화 첨가", "6+4 고리화 첨가", "1,3-쌍극자 고리화 첨가",
                   "나이트론 고리화 첨가", "나이트릴 옥사이드 고리화 첨가", "크뇌베나겔 축합", "헨리 반응", "역전자 요구 딜스-알더 반응", "클라이젠 자리옮김", "코프 자리옮김", "비대칭 딜스-알더 반응", "이미늄 촉매 공액 첨가"],
    "C–C-결합-절단": ["과아이오딘산 절단", "오존 분해", "역알돌 반응", "탈카복실화", "역 딜스-알더 반응", "할로폼 반응"],
    "페리고리": ["딜스-알더 반응", "역 딜스-알더 반응", "광화학 2+2 고리화 첨가", "케텐 2+2 고리화 첨가",
              "스타우딩거 β-락탐 합성", "4+3 고리화 첨가", "6+4 고리화 첨가", "1,3-쌍극자 고리화 첨가",
              "나이트론 고리화 첨가", "나이트릴 옥사이드 고리화 첨가", "클릭 반응", "오존 분해", "역전자 요구 딜스-알더 반응", "시그마트로픽 자리옮김", "2,3-시그마트로픽 자리옮김", "클라이젠 자리옮김", "코프 자리옮김", "1,5-수소 이동", "전자고리화 반응", "나자로프 고리화", "비대칭 딜스-알더 반응"],
    "고리-형성": ["분자내 알돌 반응", "디크만 축합", "로빈슨 고리 형성", "딜스-알더 반응",
               "광화학 2+2 고리화 첨가", "케텐 2+2 고리화 첨가", "스타우딩거 β-락탐 합성",
               "4+3 고리화 첨가", "6+4 고리화 첨가", "1,3-쌍극자 고리화 첨가", "나이트론 고리화 첨가",
               "나이트릴 옥사이드 고리화 첨가", "클릭 반응", "에폭시화", "역전자 요구 딜스-알더 반응", "전자고리화 반응", "나자로프 고리화", "비대칭 딜스-알더 반응"],
    "보호-탈보호": ["아세탈 형성", "펩타이드 합성", "수소화분해"],
    "토토머화": ["케토-엔올 토토머화", "α-할로젠화"],
}

REAGENT_TYPE = {
    "산화제": ["mCPBA", "OsO4", "NaIO4", "오존", "DMP", "TPAP", "MnO2", "TEMPO", "NaClO2", "존스 시약", "KMnO4", "SeO2", "NMO"],
    "환원제": ["NaBH4", "NaBH3CN", "LiAlH4", "LiBH4", "DIBAL-H", "Pd/C", "린들라 촉매", "PtO2"],
    "수소붕소화": ["보레인", "9-BBN"],
    "촉매": ["Pd/C", "린들라 촉매", "루이스 산 촉매", "TEMPO", "TPAP", "OsO4", "PtO2"],
    "염기": ["LDA", "알콕사이드 염기"],
    "산": ["TFA", "혼산"],
    "루이스-산": ["루이스 산 촉매", "TiCl4"],
    "탄소-친핵체": ["그리냐르 시약", "유기구리 시약", "인 일라이드", "실릴 엔올 에터"],
    "아민": ["피롤리딘"],
    "할로젠화제": ["NBS"],
    "보호기": ["Boc 보호기", "Cbz 보호기", "Fmoc 보호기", "실릴 에터 보호기", "벤질 에터 보호기", "THP 보호기"],
    "키랄-보조기": ["에반스 옥사졸리디논"],
    "커플링제": ["DCC"],
    "다이엔-시약": ["대니셰프스키 다이엔"],
}

CONCEPT_TYPE = {
    "중간체": ["브로모늄 이온", "탄소 양이온", "아레늄 이온", "아실륨 이온", "나이트로늄 이온", "이미늄 이온",
             "사면체 중간체", "알릴 양이온", "엔올과 엔올레이트", "엔아민", "케텐", "1,3-쌍극자", "이민", "옥사포스페테인", "마이젠하이머 착물", "이소시아네이트"],
    "선택성": ["마르코프니코프 규칙", "입체특이성과 입체선택성", "속도론적 지배와 열역학적 지배", "치환기 효과",
             "속도론적 엔올레이트와 열역학적 엔올레이트", "1,2-첨가와 1,4-첨가", "endo 규칙",
             "딜스-알더 위치선택성", "하드-소프트 산염기", "느슨한 SN2 전이 상태", "키랄 보조기",
             "금속 수소화물의 반응성", "직교 보호"],
    "오비탈": ["친전자체와 친핵체", "프런티어 분자 오비탈", "우드워드-호프만 규칙", "초면과 대면", "페리고리 반응",
             "방향족성", "콘로테이션과 디스로테이션"],
    "산염기": ["α-수소의 산도", "하드-소프트 산염기", "E1cB 제거"],
    "구조-형태": ["s-cis 형태", "방향족성", "큐베인"],
    "전략": ["보호기", "직교 보호", "키랄 보조기"],
    "자리옮김": ["탄소 양이온 자리옮김"],
    "개관": ["알켄의 친전자성 첨가 개관", "엔올레이트 화학 개관", "아민 합성 개관", "알켄의 입체선택적 합성"],
}

# 2025 Test 1에 출제된 주제 (practice/Test1_2025.md의 표 기준)
PAST_EXAM = {
    "Test1-2025": ["위티그 반응", "HWE 반응", "수소붕소화-산화", "보레인", "마르코프니코프 규칙", "DMP", "피닉 산화",
                   "NaClO2", "알코올 산화", "프리델-크래프츠 아실화", "프리델-크래프츠 알킬화", "클레멘센 환원",
                   "환원성 아미노화", "NaBH3CN", "NaBH4", "엔올레이트 알킬화", "LDA", "알돌 반응", "교차 알돌 반응",
                   "무카이야마 알돌 반응", "실릴 엔올 에터", "TiCl4", "속도론적 엔올레이트와 열역학적 엔올레이트",
                   "다이하이드록실화", "OsO4", "에폭시화", "mCPBA", "에폭사이드 고리 열기", "입체특이성과 입체선택성",
                   "할로하이드린 형성", "오존 분해", "오존", "아세토아세트산 에스터 합성", "탈카복실화", "DIBAL-H",
                   "에스터 부분 환원", "아자이드·나이트릴을 거친 아민 합성", "친전자성 방향족 치환", "아레늄 이온",
                   "치환기 효과", "루이스 산 촉매", "NMO", "옥사포스페테인", "에스터 가수분해"],
}


def slug(tag):
    """옵시디언 태그에는 공백을 쓸 수 없다."""
    # 태그에는 쉼표도 쓸 수 없다 (1,5-다이카보닐 → 1-5-다이카보닐)
    return re.sub(r"[\s,]+", "-", tag.strip().lstrip("#"))


def compute_tags(doc, extra):
    t = plain_greek_label(doc["title"])
    tags = [f"분류/{doc['category']}"]
    for n in doc["lectures"]:
        tags += [f"범위/{exam_scope(n)}", f"강의/L{n:02d}", f"단원/{UNIT[n]}"]
    for group, table in (("", NAMED), ("유형/", REACTION_TYPE), ("시약유형/", REAGENT_TYPE),
                         ("개념유형/", CONCEPT_TYPE), ("기출/", PAST_EXAM)):
        for key, titles in table.items():
            if t in titles:
                tags.append(group + key)
    # 작성자가 붙인 자유 태그는 "주제/" 아래로 모은다. 체계 안의 태그와 겹치면 뺀다.
    known = {"반응", "시약", "개념", *UNIT.values()}
    for table in (NAMED, REACTION_TYPE, REAGENT_TYPE, CONCEPT_TYPE):
        known |= set(table)
    for x in extra:
        x = slug(x)
        if x and "/" not in x and x not in known:
            tags.append(f"주제/{x}")
    order = ["분류/", "범위/", "기출/", "인명", "단원/", "강의/", "유형/", "시약유형/", "개념유형/", "주제/"]
    rank = lambda x: next((i for i, p in enumerate(order) if x.startswith(p)), len(order))
    return sorted(dict.fromkeys(tags), key=lambda x: (rank(x), x))


def apply_tags(docs):
    """머리말의 '태그'(작성자 태그)를 정해진 체계의 'tags'로 바꾼다. 여러 번 실행해도 결과가 같다."""
    changed = 0
    for d in docs:
        text = d["text"]
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            continue
        lines = m.group(1).splitlines()
        extra, kept = [], []
        for line in lines:
            key = line.split(":", 1)[0].strip()
            if key == "태그":
                extra = parse_list(line.split(":", 1)[1])
            elif key == "주제태그":
                extra = parse_list(line.split(":", 1)[1])
            elif key == "tags":
                continue
            else:
                kept.append(line)
        tags = compute_tags(d, extra)
        kept.append("주제태그: [" + ", ".join(slug(x) for x in extra) + "]")
        kept.append("tags: [" + ", ".join(tags) + "]")
        new = "---\n" + "\n".join(kept) + "\n---\n" + text[m.end():]
        if new != text:
            open(d["path"], "w", encoding="utf-8").write(new)
            d["text"] = new
            changed += 1
        d["tags"] = tags
    return changed


def load_docs():
    docs = []
    for cat in CATEGORIES:
        for p in sorted(glob.glob(os.path.join(WIKI, cat, "*.md"))):
            docs.append(read_doc(p))
    return docs


def short(summary, n=70):
    """표에 넣을 짧은 요약: 첫 문장, 링크는 글자만 남긴다."""
    s = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", summary)
    s = re.sub(r"\[\[([^\]]+)\]\]", r"\1", s)
    s = re.sub(r"\[((?:\\.|[^\]\\])+)\]\([^)]+\)", lambda m: m.group(1).replace(r"\[", "[").replace(r"\]", "]"), s)
    s = re.split(r"(?<!cat)(?<!eq)(?<!aq)\. ", s)[0]
    s = inline_greek(s)
    if len(s) <= n:
        return s
    end = n - 1
    # LaTeX 명령/구분자 중간에서 자르면 목록의 나머지까지 수식으로 삼킬 수 있다.
    for m in PROTECTED.finditer(s):
        if m.start() < end < m.end():
            end = m.start()
            break
    if end == 0:
        first = next(PROTECTED.finditer(s), None)
        if first and re.search(r"\\(?:xrightarrow|longrightarrow|rightleftharpoons)", first[0]):
            return "반응식은 본문 참고"
        return (first[0] if first else "") + "…"
    return s[:end].rstrip() + "…"


def url(path):
    """마크다운 링크 주소: GitHub와 옵시디언이 모두 읽도록 공백과 괄호만 인코딩한다."""
    return path.replace("%", "%25").replace(" ", "%20").replace("(", "%28").replace(")", "%29")


def mdlink(text, target, from_dir):
    """target(절대 경로)으로 가는 상대 경로 마크다운 링크. 글자 속 대괄호는 이스케이프한다."""
    rel = os.path.relpath(target, from_dir).replace(os.sep, "/")
    text = inline_greek(text)
    text = re.sub(r"(?<!\\)([\[\]])", lambda m: "\\" + m[1], text)
    return f"[{text}]({url(rel)})"


# 목록에 보일 영어 이름: 제목에 한글이 없으면 제목 그대로, 아래 표에 있으면 그것, 아니면 첫 영어 별칭
ENGLISH_NAME = {
    "엔올과 엔올레이트": "enol and enolate", "친전자체와 친핵체": "electrophile and nucleophile",
    "입체특이성과 입체선택성": "stereospecificity and stereoselectivity", "초면과 대면": "suprafacial and antarafacial",
    "콘로테이션과 디스로테이션": "conrotatory and disrotatory", "속도론적 지배와 열역학적 지배": "kinetic vs thermodynamic control",
    "속도론적 엔올레이트와 열역학적 엔올레이트": "kinetic vs thermodynamic enolate",
    "아자이드·나이트릴을 거친 아민 합성": "amine synthesis via azide and nitrile", "할로젠 첨가": "halogen addition",
    "다이아조늄 염 반응": "diazonium salt reactions", "아민 합성 개관": "amine synthesis (overview)",
    "알켄의 친전자성 첨가 개관": "electrophilic addition to alkenes (overview)", "엔올레이트 화학 개관": "enolate chemistry (overview)",
    "이미늄 촉매 공액 첨가": "iminium-catalysed conjugate addition", "하드-소프트 산염기": "hard and soft acids and bases (HSAB)",
    "SN2 반응": "SN2 reaction", "E1cB 제거": "E1cB elimination", "역 딜스-알더 반응": "retro-Diels–Alder reaction",
    "보호기": "protecting group", "Boc 보호기": "Boc protecting group", "Cbz 보호기": "Cbz protecting group",
    "Fmoc 보호기": "Fmoc protecting group", "THP 보호기": "THP protecting group", "벤질 에터 보호기": "benzyl ether protecting group",
    "실릴 에터 보호기": "silyl ether protecting group",
}


def english_name(doc):
    if not re.search(r"[가-힣]", doc["title"]):
        return doc["title"]
    if doc["title"] in ENGLISH_NAME:
        return ENGLISH_NAME[doc["title"]]
    for a in doc["aliases"]:
        if re.search(r"[A-Za-z]", a) and not re.search(r"[가-힣]", a):
            return a
    return doc["title"]


def link(doc, from_dir=None):
    """위키 문서로 가는 링크. 보이는 글자는 영어 이름(학습자 선호), 주소는 한국어 파일 이름."""
    return mdlink(english_name(doc), doc["path"], from_dir or WIKI)


def hub(name, from_dir=None):
    return mdlink(name, os.path.join(WIKI, name + ".md"), from_dir or WIKI)


def build_front_page(docs):
    lines = [
        "---",
        "aliases: [위키, 대문, 목차]",
        "---",
        "# 위키 대문",
        "",
        "> 이 노트의 **본문**이다. 강의 순서와 상관없이 **반응, 시약, 개념(원리)** 하나마다 문서 하나를 두고, "
        "여러 강의에 흩어진 설명을 그 문서에 모았다. 궁금한 항목 하나를 열어 읽고, 링크를 따라 옆 문서로 넘어가며 공부한다.",
        "",
        "강의 순서가 필요하면 [README](../README.md)의 강의 노트(뼈대)를 본다. 강의 노트는 슬라이드 순서와 쪽수, "
        "그리고 이 문서들로 가는 링크만 담고 있다.",
        "",
        f"**모아 보기**: {hub('Test 1 범위')} · {hub('Test 2 범위')} · {hub('인명반응 목록')}. "
        "태그 창에서 `범위/`, `단원/`, `유형/`, `시약유형/`, `개념유형/`, `기출/`, `인명반응` 태그로도 골라 볼 수 있다.",
        "",
        "이 문서는 `tools/build_wiki_index.py`가 자동으로 만든다. 직접 고치지 말고 스크립트를 다시 실행한다.",
        "",
    ]
    # 단원별 시작점: 개관 문서와, 다른 문서에서 가장 많이 링크되는 핵심 문서
    backlinks = {}
    for d in docs:
        for target in set(re.findall(r"\]\(([^)#]+\.md)\)", d.get("text", ""))):
            stem = os.path.splitext(os.path.basename(urllib.parse.unquote(target)))[0]
            backlinks[stem] = backlinks.get(stem, 0) + 1
    lines += ["## 단원별 시작점", "", "| 단원 | 개관 | 핵심 문서 |", "|---|---|---|"]
    for u in dict.fromkeys(UNIT.values()):
        lec = [n for n, v in UNIT.items() if v == u]
        unit_docs = [d for d in docs if d["lectures"] and d["lectures"][0] in lec]
        overview = [d for d in unit_docs if "개관" in d["title"] or "개념유형/개관" in d.get("tags", [])]
        core = sorted((d for d in unit_docs if d not in overview),
                      key=lambda d: (-backlinks.get(d["file"], 0), d["title"]))[:6]
        span = f"L{lec[0]}" + (f"–L{lec[-1]}" if len(lec) > 1 else "")
        lines.append(f"| {UNIT_NAME.get(u, u.replace('-', ' '))} ({span}) | "
                     f"{', '.join(link(d) for d in overview) or '–'} | {', '.join(link(d) for d in core)} |")
    lines.append("")
    for cat in CATEGORIES:
        items = [d for d in docs if d["category"] == cat]
        lines += [f"## {cat} ({len(items)})", "", "| 문서 | 한 줄 요약 | 강의 |", "|---|---|---|"]
        for d in sorted(items, key=lambda d: english_name(d).lower()):
            lec = ", ".join(f"L{n}" for n in d["lectures"])
            lines.append(f"| {link(d)} | {short(d['summary'])} | {lec} |")
        lines.append("")
    path = os.path.join(WIKI, "위키 대문.md")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return path



def write_page(name, lines):
    path = os.path.join(WIKI, name + ".md")
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    return name


def build_hub_pages(docs):
    """태그로 묶은 모음 문서: 시험 범위별, 인명반응."""
    made = []
    note = "이 문서는 `tools/build_wiki_index.py`가 태그를 바탕으로 자동으로 만든다."
    star = "★ 표시는 2025 Test 1에 출제된 주제다."
    units = list(dict.fromkeys(UNIT.values()))
    for scope, desc in (("Test1", "1–5주차, 강의 L1–L10"),
                        ("Test2", "6–10주차, 강의 L11–L15 (라디칼 화학 제외; 시그마트로픽·전자고리화 반응은 자료가 나오면 추가)")):
        lines = ["---", f"tags: [모음, 범위/{scope}]", "---", f"# {scope[:-1]} {scope[-1]} 범위",
                 "", f"> {desc}. {note} {star}".rstrip(), ""]
        for u in units:
            # 이 범위에 속한 강의의 단원으로만 묶는다 (예: L13에서 다시 쓰인 오존 분해는 고리화 첨가 아래)
            items = [d for d in docs
                     if any(exam_scope(n) == scope and UNIT.get(n) == u for n in d["lectures"])]
            if not items:
                continue
            lec = sorted(n for n, v in UNIT.items() if v == u)
            lines += [f"## {UNIT_NAME.get(u, u.replace('-', ' '))} (L{lec[0]}" + (f"–L{lec[-1]})" if len(lec) > 1 else ")"), ""]
            for cat in CATEGORIES:
                group = sorted((d for d in items if d["category"] == cat), key=lambda d: english_name(d).lower())
                if group:
                    entries = [link(d) + (" ★" if "기출/Test1-2025" in d.get("tags", []) else "") for d in group]
                    lines.append(f"- **{cat}**: " + ", ".join(entries))
            lines.append("")
        made.append(write_page(f"{scope[:-1]} {scope[-1]} 범위", lines))
    lines = ["---", "tags: [모음, 인명반응]", "---", "# 인명반응 목록", "",
             f"> 사람 이름이 붙은 반응, 시약, 규칙을 모았다. {note}", ""]
    for key, title in (("인명반응", "반응"), ("인명시약", "시약"), ("인명규칙", "규칙")):
        group = sorted((d for d in docs if key in d.get("tags", [])), key=lambda d: english_name(d).lower())
        if group:
            lines += [f"## {title} ({len(group)})", "", "| 문서 | 한 줄 요약 | 강의 |", "|---|---|---|"]
            for d in group:
                lines.append(f"| {link(d)} | {short(d['summary'])} | {', '.join(f'L{n}' for n in d['lectures'])} |")
            lines.append("")
    made.append(write_page("인명반응 목록", lines))
    return made

def update_lecture_notes(docs):
    changed = 0
    for path in sorted(glob.glob(os.path.join(NOTES, "L*.md"))):
        n = int(re.match(r"L(\d+)_", os.path.basename(path)).group(1))
        related = [d for d in docs if n in d["lectures"]]
        text = open(path, encoding="utf-8").read()
        block_lines = [START, "", f"> **관련 위키 문서** ({hub('위키 대문', NOTES)})"]
        for cat in CATEGORIES:
            items = sorted((d for d in related if d["category"] == cat), key=lambda d: english_name(d).lower())
            if items:
                block_lines.append(f"> - {cat}: " + ", ".join(link(d, NOTES) for d in items))
        block_lines += ["", END]
        block = "\n".join(block_lines)
        if START in text:
            new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
        else:
            # 제목(H1) 바로 아래에 넣는다
            new = re.sub(r"^(# .+\n)", lambda m: m.group(1) + "\n" + block + "\n", text, count=1, flags=re.M)
        if new != text:
            open(path, "w", encoding="utf-8").write(new)
            changed += 1
    return changed


def check_links(docs):
    """wiki, notes, practice, README의 상대 경로 링크가 실제 파일을 가리키는지, 옵시디언 전용 [[ ]]가 남지 않았는지 본다."""
    broken = []
    files = glob.glob(os.path.join(WIKI, "**", "*.md"), recursive=True) + glob.glob(os.path.join(NOTES, "**", "*.md"), recursive=True) \
        + glob.glob(os.path.join(ROOT, "practice", "*.md")) + [os.path.join(ROOT, "README.md")]
    for path in files:
        text = open(path, encoding="utf-8").read()
        text = re.sub(r"```.*?```|`[^`\n]*`", "", text, flags=re.S)  # 코드 안의 예시는 건너뛴다
        for target in re.findall(r"\[\[([^\]]+)\]\]", text):
            broken.append((os.path.relpath(path, ROOT), f"[[{target}]]"))
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if re.match(r"[a-z]+:", target) or target.startswith("#"):
                continue
            dest = os.path.normpath(os.path.join(os.path.dirname(path), urllib.parse.unquote(target.split("#")[0])))
            if not os.path.exists(dest):
                broken.append((os.path.relpath(path, ROOT), target))
    return broken


def main():
    docs = load_docs()
    if "--check" not in sys.argv:
        print("태그 정리:", apply_tags(docs))
        print("목록:", os.path.relpath(build_front_page(docs), ROOT))
        print("모음 문서:", ", ".join(build_hub_pages(docs)))
        print("강의 노트 갱신:", update_lecture_notes(docs))
    broken = check_links(docs)
    print(f"위키 문서 {len(docs)}개, 깨진 링크 {len(broken)}개")
    for path, target in broken:
        print(f"  {path}: {target}")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
