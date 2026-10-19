# L16 Woodward–Hoffmann 보강 및 검수 — 2026-10-19

## 반영 범위

- 통독 L16 §4.7–4.10, §9.3, §10.1–10.2 및 기존 sigmatropic wiki에 설명과 SVG 10개를 추가했다.
- 같은 면/반대 면의 네 가지 접촉, face와 phase의 구별, sigma 성분의 R/R·I/I·R/I·I/R, [3,3]의 일관된 성분 재표현을 설명했다.
- [1,3]H·[1,5]H·[1,7]H의 성분 판정, diene/triene LUMO 비교, thermal/photochemical 선택 규칙을 보강했다.
- 형식상 symmetry-allowed라는 판정과 실제 conformation의 접근 가능성을 구분했다.

## 그림 및 출처

`tools/gen_l16_wh_examples.py`로 기존 `tools/mplfig.py` 스타일을 사용해 생성했다. Orbital 및 component teaching diagrams이며 최적화된 TS나 실제 H 이동 궤적이 아니다. 본문에 이 범위를 명시했다. 영어 라벨, 기존 PX 글자 크기, SVG 벡터 및 자동 light/dark 스타일을 유지했다.

| SVG (`figures/L16/`) | 내용 |
|---|---|
| wh_faces_four.svg | 위/위, 아래/아래, 위/아래, 아래/위 |
| wh_phase_not_face.svg | 같은 face와 같은 phase의 구별 |
| wh_sigma_four.svg | 네 가지 retention/inversion 조합 |
| wh_h13_components.svg | [1,3]H: 허용 판정과 기하 제약 |
| wh_h15_components.svg | [1,5]H: pi4s + sigma2s |
| wh_h17_components.svg | [1,7]H: pi6a + sigma2s |
| wh_h15_fmo.svg | Diene LUMO의 위상과 node |
| wh_h17_fmo.svg | Triene LUMO의 위상과 node |
| wh_33_count.svg | [3,3]의 두 일관된 성분 표시 |
| wh_hshift_photo.svg | Thermal/photochemical 비교 |

Clayden 인쇄 p.913과 p.921을 이미지로 확인했고 p.920–921의 텍스트도 대조했다. 본문에는 관련 교재 페이지를 개별 표기했다. FMO lobe 크기는 정성적 도식이며 orbital coefficient 크기를 정량적으로 나타내지 않는다.

## 실행한 검수

- 신규 SVG 10개 XML 파싱 성공; 각 그림을 dark/light로 렌더링한 20개 PNG를 시각 검토했다.
- 검토 중 [1,7]H 접촉선과 R 라벨 간섭, FMO의 탄소 라벨과 접촉점 간섭을 수정하고 재렌더링했다.
- 실제 GitHub Markdown API로 두 문서를 파싱: 인식된 수식 밖에 남은 LaTeX 후보 0개.
- 로컬 Chromium/MathJax로 두 문서를 dark/light 각각 확인: L16 243개, wiki 67개 수식. 네 화면 모두 MathJax 오류 0, 깨진 이미지 0, 본문 폭 820px 초과 수식 0.
- L16 정적 Markdown 검사 findings 0.
- `python3 tools/build_wiki_index.py`: wiki 181개, broken links 0.
- `git diff --check` 통과.

실제 Obsidian 앱 안의 렌더링은 이번 검수에 포함하지 않았다. 기존 전체 그림의 재검수가 아니라 신규 10개 그림과 변경한 두 문서의 검수다.

로컬 검수 자료: `/home/kim/Documents/OChem-work/ochem-l16-wh-20261019/`.
