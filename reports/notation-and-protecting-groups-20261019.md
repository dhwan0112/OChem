# L16 notation 그림 및 L12 protecting group 표 (2026-10-19)

## 반영 범위

- L16 통독 1.4절: [3,3], [2,3], [1,5]H의 번호 매기기 그림 3개와 경로 설명.
- L16 통독 4.5–4.6절: pi/sigma/omega, 전자 수, s/a 및 retention/inversion 그림 3개; H의 1s orbital 설명; 여섯 가지 열적 판정 예시.
- sigmatropic rearrangement 개념 문서에 같은 설명과 그림 반영. 연결 문서에 남아 있던 inline aligned 문장, 강조 표시, 각주 수식도 정리.
- L12 통독 4번 항목과 protecting group 개념 문서: 기존 9종의 항목을 보호 대상·구조·안정성 표(4열)와 도입·제거 조건 표(3열)로 재구성. 각 표는 제목행 외에 데이터 9행이며, 기존 구조·조건을 유지.

## 그림과 근거

| 그림 | 내용 | 교재 인쇄 쪽수 |
|---|---|---|
| `notation_33_numbering.svg` | O를 포함하는 두 경로와 A3–B3 새 결합 | Clayden 910 |
| `notation_23_numbering.svg` | O(A1), carbanion(A2), allyl 말단(B3) | Clayden 917–918 |
| `notation_15_numbering.svg` | H 하나와 diene 경로의 탄소 다섯 개 | Clayden 919 |
| `notation_components.svg` | orbital 수와 전자 수의 구분 | Clayden 912,918 |
| `notation_pi_faces.svg` | pi 성분 양 끝에서 같은 면/반대 면 접촉 | Clayden 913 |
| `notation_sigma_faces.svg` | R/R·I/I와 R/I·I/R의 구분 | Clayden 913 |

앞의 세 구조 그림은 기존 ReShiki 구조의 원자·결합 좌표와 명시된 H를 유지하고 번호 및 형성 결합을 추가했다. 뒤의 세 orbital 도식은 기존 `tools/mplfig.py`의 규격을 사용했다. A/B는 교육용 경로 라벨이며 공식 반응명 표기의 일부가 아님을 본문에 밝혔다. 점선은 연결 관계 또는 새 접촉이며 전자 이동 화살표나 계산된 TS가 아니다.

재생성:

```bash
/home/kim/opt/miniforge3/envs/chem/bin/python tools/gen_sigmatropic_notation.py
RESHIKI=/home/kim/opt/reshiki/0.11.0-nightly.20261013/reshiki python3 tools/chemfig.py figures/L16/notation_33_numbering.json figures/L16/notation_23_numbering.json figures/L16/notation_15_numbering.json
```

L12 표는 공식 강의 PDF p.5의 9개 행과 대조했다. silyl group별 안정성은 p.7, 대표 제거 조건은 p.6,8과 함께 확인했다. 박스로 강조한 다섯 항목을 표에서도 강조했다. benzyl ether의 “almost everything”은 모든 조건에서 안정하다는 뜻으로 일반화하지 않았다.

## 검증

- 새 그림 6개를 dark/light, 3배 렌더링하여 검수. 번호가 결합선과 겹치거나 carbanion의 음전하·비공유 전자쌍을 가리던 초기 배치를 수정한 뒤 재검수.
- 기존 native 그림과 같은 결합 좌표·배율, 원자 글자 크기 유지. 번호는 7 pt, native 설명은 8 pt. Orbital 그림은 공통 규격의 18.1 px 기호·14.5 px 설명·1.085 px 선과 테마별 배경 카드 사용.
- 수정한 본문 4문서의 정적 검사 및 실제 GitHub Markdown API 검사: 수식 432개 인식, 남은 수식·강조 문법 0건.
- GitHub 반환 HTML의 수식 요소를 로컬 MathJax로 렌더링한 dark/light 8개 구성: 수식 오류 0, 이미지 로딩 실패 0, 820 CSS px를 넘는 수식 0.
- L12 표는 dark/light에서 각각 10행(제목 포함)으로 확인. 4열 표는 820 px, 3열 표는 약 716 px.
- 위키 인덱스 재생성: 깨진 링크 0.

GitHub 파서 출력에서 로컬 렌더링을 위해 이미지 경로와 수식 wrapper를 변환했다. GitHub의 wrapper에 남은 inline-block 스타일은 제거하여 로컬 MathJax가 inline baseline을 계산하도록 했다. 실제 GitHub 웹 UI, Obsidian 앱, 모바일 화면을 검사했다는 뜻은 아니다.
