# tools/test2_figures

`figures/Test2_figures/`의 개념 그림(SVG)과 오비탈 애니메이션(GIF)을 만든 Python 스크립트다. ReShiki(`tools/chemfig.py`)가 아니라 PIL과 cairosvg로 직접 그린다.

필요 패키지: `pip install pillow numpy scipy cairosvg`. 글꼴은 DejaVu Sans(`/usr/share/fonts/truetype/dejavu/`)를 쓴다.

## 실행 방법

각 스크립트는 **자기 폴더 안에서** 실행하며(공용 모듈 `common.py`, `orb.py`, `glyph.py`, `geom.py`를 같은 폴더에서 가져온다), 결과를 현재 폴더에 쓴다. SVG는 컬러판과 `_bw.svg` 흑백판이 함께 나오고, 확인용 PNG(`*.png`, `check*.png`, `c0.png` 등)도 같이 생긴다. 확인용 PNG는 저장소에 넣지 않는다.

```bash
cd tools/test2_figures/wh_svg && python3 wh1.py      # WH_counting_rule.svg, WH_counting_rule_bw.svg
cd tools/test2_figures/endo   && python3 endo_gif.py # endo_rule_3D.gif
```

만들어진 파일은 아래 표의 저장소 이름으로 바꿔 `figures/Test2_figures/`의 해당 폴더에 넣는다. SVG에 다른 도구가 붙인 메타데이터가 있으면 지우고 넣는다.

## 스크립트와 저장소 파일 대응

| 폴더 | 스크립트 | 출력 파일 | 저장소 파일 (`figures/Test2_figures/`) |
|---|---|---|---|
| `l11/` | `make.py` | `enamine_conjugate_addition_p19.svg` | `01_L11_conjugate_addition/L11_01_enamine_conjugate_addition_p19.svg` |
| `l11/` | `gen.py` | `enamine_conjugate_addition_general.svg` | `01_L11_conjugate_addition/L11_02_enamine_conjugate_addition_general.svg` |
| `l11/` | `cyc.py` | `iminium_catalysis_cycle.svg` | `01_L11_conjugate_addition/L11_03_iminium_catalysis_cycle.svg` |
| `wh_svg/` | `da_mech.py` | `DA_mechanism(_bw).svg` | `02_cycloaddition_L13-L15/CY_01_DA_mechanism(_bw).svg` |
| `wh_svg/` | `fmo.py` | `FMO_cycloaddition(_bw).svg` | `02_cycloaddition_L13-L15/CY_02_FMO_allowed_vs_forbidden(_bw).svg` |
| `gif_da_orbitals/` | `da.py` | `DA_orbitals.gif` | `02_cycloaddition_L13-L15/CY_03_DA_orbitals.gif` |
| `gif_ez_diene/` | `da3d.py` | `EZ_diene_DA_3D.gif` | `02_cycloaddition_L13-L15/CY_04_EZ_diene_DA_3D.gif` |
| `gif_ketene/` | `reach.py` | `antarafacial_reach.gif` | `02_cycloaddition_L13-L15/CY_05_antarafacial_reach_2plus2.gif` |
| `gif_ketene/` | `k22.py` | `ketene_vs_alkene_22.gif` | `02_cycloaddition_L13-L15/CY_06_ketene_vs_alkene_2plus2.gif` |
| `wh_svg/` | `wh_d.py` | `WH4_ketene_crossed(_bw).svg` | `02_cycloaddition_L13-L15/CY_07_ketene_crossed_topview(_bw).svg` |
| `endo/` | `endo_svg.py` | `endo_steps_1-3(_bw).svg` | `02_cycloaddition_L13-L15/CY_08_endo_steps_1-3(_bw).svg` |
| `endo/` | `endo_step4.py` | `endo_step4_products(_bw).svg` | `02_cycloaddition_L13-L15/CY_09_endo_step4_products(_bw).svg` |
| `endo/` | `endo_gif.py` | `endo_rule_3D.gif` | `02_cycloaddition_L13-L15/CY_10_endo_rule_3d.gif` |
| `endo/` | `sec_gif.py` | `endo_secondary_overlap.gif` | `02_cycloaddition_L13-L15/CY_11_endo_secondary_overlap.gif` |
| – | (스크립트 없음) | – | `02_cycloaddition_L13-L15/CY_12_endo_maleic_anhydride_products.gif` (예비본, 생성 스크립트가 남아 있지 않다) |
| `wh_svg/` | `wh_a.py` | `WH1_phase_basics(_bw).svg` | `03_woodward_hoffmann/WH_01_phase_basics(_bw).svg` |
| `wh_svg/` | `wh_b.py` | `WH2_MO_ladders(_bw).svg` | `03_woodward_hoffmann/WH_02_MO_ladders(_bw).svg` |
| `wh_svg/` | `wh_c.py` | `WH3_SA_matching(_bw).svg` | `03_woodward_hoffmann/WH_03_SA_matching(_bw).svg` |
| `wh_svg/` | `tab1.py` | `WH_notation_table(_bw).svg` | `03_woodward_hoffmann/WH_04_notation_table(_bw).svg` |
| `wh_svg/` | `wh1.py` | `WH_counting_rule(_bw).svg` | `03_woodward_hoffmann/WH_05_counting_rule(_bw).svg` |
| `wh_svg/` | `wh2.py` | `WH_counting_examples(_bw).svg` | `03_woodward_hoffmann/WH_06_counting_examples(_bw).svg` |
| `wh_svg/` | `tab2.py` | `WH_examples_table(_bw).svg` | `03_woodward_hoffmann/WH_07_examples_table(_bw).svg` |
| `wh_svg/` | `atoms_vs_e.py` | `WH_atoms_vs_electrons(_bw).svg` | `03_woodward_hoffmann/WH_08_atoms_vs_electrons(_bw).svg` |
| `gif_h17/` | `h17.py` | `H17_antarafacial.gif` | `04_sigmatropic_L16/SG_01_1-7H_shift_antarafacial.gif` |
| `wh_svg/` | `cheat.py` | `WH_cheatsheet_card(_bw).svg` | `05_cheatsheet/CS_01_WH_cheatsheet_card(_bw).svg` |

공용 모듈: `wh_svg/common.py`(SVG 캔버스, 색 클래스, 다크 모드 CSS, `save`), `wh_svg/orb.py`(p 오비탈 로브), `wh_svg/glyph.py`(기호), `endo/common.py`(wh_svg와 같은 캔버스), `endo/geom.py`(cyclopentadiene·dienophile 3D 좌표).

## 손본 내용

- `wh_svg/wh1.py`: 표 아래 "sum ODD → thermally allowed"와 "sum EVEN → thermally forbidden"이 한 줄에서 겹쳤던 것을 두 줄로 나눴다.
- `wh_svg/wh_c.py`: 맨 아래 hν 각주가 그림 폭을 넘어 잘리던 것을 두 줄로 나눴다.
- `l11/make.py`: 출력 경로를 현재 폴더 기준으로 바꿨다.

## 한계

- GIF는 3D 좌표를 결합 길이만 맞춘 도식이며, 로브 크기는 Hückel 계수를 반영한 것과 위상만 보인 것이 섞여 있다(각 그림 하단 설명 참고).
- `figures/STYLE.md`의 ReShiki 스펙 규칙(그림 하나 = JSON 하나)은 적용되지 않는다. 색 규칙(HOMO·nucleophile 파랑, LUMO·electrophile 빨강, 전자 이동 주황, 새 결합 초록)은 따른다.
