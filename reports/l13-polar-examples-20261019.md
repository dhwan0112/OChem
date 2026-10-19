# L13 §2 극성 고리 형성 그림 — 2026-10-19

- 강의 PDF p.6을 렌더링하여 구조·조건·수율을 대조했다.
- `tools/chemfig.py`와 ReShiki 0.11.0-nightly.20261013으로 4개 SVG를 생성했다. 대응하는 `figures/L13/polar_*.json`이 최종 좌표 스펙이다. `figures/defs/L13_polar_examples.json`은 초기 구조/배치용 SMILES 정의이며, 최종 수소 위치와 여백 조정은 좌표 스펙에 저장했다.
- Robinson annulation을 Michael addition과 고리화/탈수 두 그림으로, nitro-Michael/SN2를 열린 사슬 중간체와 고리화 두 그림으로 나누었다.
- L13 통독 §2, Diels–Alder wiki에 4개, Robinson annulation wiki에 해당 2개를 삽입했다.
- 원본에 없는 stereochemistry를 부여하지 않았다. 순변환 화살표와 단일 elementary step을 구분하는 설명을 추가했다. 65%는 전체 반응 수율이다.
- 원자 약 18 px, 캡션 약 14.5 px, 기존 0.62 표시 배율을 유지했다. 반응 중심 수소를 명시하고 겹치는 H/O 및 H/전하 라벨을 재배치했다.
- 신규 SVG 4개를 XML 파싱하고 dark/light 3배 렌더링 8개를 시각 검토했다. 전자쌍 이동 곡선이 아닌 단계별 순변환 구조 그림이므로 lone-pair 점과 곡선 화살표는 사용하지 않았다.
- `python3 tools/build_wiki_index.py`: wiki 181개, 깨진 링크 0개. `git diff --check` 통과.
- 검수 범위는 신규 그림과 삽입 문맥이다. 실제 Obsidian 앱의 화면 검수 및 L13 전체 수식 재검수는 수행하지 않았다.

로컬 검수 자료: `/home/kim/Documents/OChem-work/ochem-l13-polar-20261019/`.
