---
title: "Tritium Production and Processing Systems for ST-E1"
type: source
source_type: paper
file: "raw/articles/st-e1-tritium-systems-crossref-metadata-2026.json"
authors: "Yildirim, Naish, Trueba, Levine, Kumar, Gohani et al. (20 authors, Tokamak Energy Ltd)"
publisher: "Nuclear Fusion 66 086004, DOI 10.1088/1741-4326/ae773a, CC BY 4.0"
source_date: 2026
ingested: 2026-10-19
tags:
  - fusion/source
  - fusion/engineering
  - fusion/subsystems
status: stable
confidence: high
related:
  - "[[st-e1]]"
  - "[[tokamak-energy]]"
  - "[[tritium-breeding-ratio]]"
  - "[[declared-tbr-values]]"
  - "[[tritium-burn-fraction]]"
  - "[[tritium-start-up-inventory]]"
  - "[[tritium-doubling-time]]"
  - "[[tritium-retention]]"
  - "[[direct-internal-recycling]]"
  - "[[availability]]"
  - "[[lithium-6]]"
  - "[[vanadium-alloys]]"
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
  - "[[yang-2026-st-e1-tritium-tmap8-surrogate-models]]"
  - "[[st-e1-neutronics-crossref-metadata-2026]]"
  - "[[willis-2026-st-e1-pre-concept-design-overview]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
created: 2026-10-19
updated: 2026-11-02
---
The [[st-e1|ST-E1]] Focus Collection's fuel-cycle paper — and, read in full, the resolution of
the vault's longest-standing ST-E1 conflict.

> [!note] Full text reached 2026-11-02. The page basename is historical
> Captured 19 October 2026 as Crossref metadata only. The IOP block has lifted and the full text
> was read on **2 November 2026**. **No local capture was possible** — a plain request still
> returns a 302 into bot validation — so `file:` still points at the JSON and the basename
> keeps its original name. See *Access limitations*.

## RESOLVED — the three conflicting TBR figures were one table all along

The vault recorded three irreconcilable ST-E1 breeding values. **Table 2 is a sensitivity
table, and two of the three are rows in it:**

| Case | TBR | Δ |
|---|---|---|
| **Baseline, full breeding coverage** | **1.146** | 0.0% |
| 33% Limiters | 1.142 | −0.4% |
| 33% ECRH | 1.135 | −0.9% |
| 33% ECRH + 33% Limiters | 1.135 | −1.0% |
| 33% ICRH | 1.131 | −1.3% |
| 100% ECRH | 1.122 | −2.1% |
| **100% Pipes + Stiffening Plates** | **1.113** | −2.8% |
| 100% Limiters | 1.107 | −3.4% |
| **100% ICRH** | **1.085** | −8.2% |

> [!warning] CORRECTION 2026-11-02 — Yang's 1.113 was never an independent third estimate
> [[yang-2026-st-e1-tritium-tmap8-surrogate-models|Yang 2026]]'s modelled 1.113 is **exactly this
> table's "100% Pipes + Stiffening Plates" row**. The overview's ">1.14" is the full-coverage
> 1.146; its prose "~1.1" is the post-insertion range. One quantity, three penetration assumptions
> — not three disagreeing measurements. The **1.20** is an *"initial design target … for rough
> scoping studies"*, never a prediction. See [[declared-tbr-values]].

## EVIDENCED — the unenriched lithium claim

*"Only solid breeders and natural lithium achieve the target TBR in excess of 1.20."* The paper
selects **natural, unenriched liquid lithium**. The claim this vault carried as asserted since
19 October is now evidenced from the design paper itself, and independently in outline by
[[ukaea-2026-vanadium-strategy|UKAEA]] via [[vanadium-alloys]]. See [[lithium-6]].

## The fuel cycle, quantified

| Quantity | Value |
|---|---|
| [[tritium-start-up-inventory\|Start-up inventory]] | **1.58 kg** (incl. 20% commissioning contingency); 1.31 kg tritium-lean |
| [[tritium-doubling-time\|Doubling time]] | **152 days** |
| Operational inventory `I_op` | 2.4 kg, reached in 85 days |
| Total inventory excl. storage | **1.39 kg** at TBE 2%; 2.42 kg at TBE 1% |
| [[tritium-burn-fraction\|Burn fraction]] | 2.6% at η_fuel 76% (R = 0.1); 2.9% at 68% (R = 0.2) |
| [[direct-internal-recycling\|DIR]] fraction | 0.7, protium 1 at% in / 0.8 at% out |
| Blanket inventory | 0.31 kg, in a 360,000 kg loop flowing 296 kg s⁻¹ |

**Extraction** is a concentration-dependent TES: 1% efficient below an onset concentration
(100 ppb worked example), rising to 80% above ~1 ppm, with a 20% bleed and per-segment lithium
loops. Lithium tritide electrolysis is *"a potential method"*; no final selection appears in the
text retrieved. Full fuel-cycle table: [[28-vacuum-wall-conditioning-tritium-plant|Document 28 §6]].

> [!warning] NEW CONFLICT — availability, now with a third figure
> This paper assumes **100% availability**, noting it as a simplification offset by a 20%
> contingency. The design mission targets **> 80%**; Yang 2026 models **37.5%**. The design
> paper's own fuel-cycle analysis uses the most optimistic of the three. See [[availability]].

## What it does not establish

- **Table 1's breeder-to-value mapping could not be determined** from the retrieved text: five
  breeders (Li₁₇Pb₈₃, Li, FLiBe, Li₄SiO₄, Li₂TiO₃) against TBR cells 1.04, 1.26, 0.92, 1.27,
  one cell missing. Which breeders clear 1.20 is therefore **not recorded here**.
- **No trapping physics.** First wall and divertor are assigned 0.012–0.024 kg; see
  [[tritium-retention]] for why that is not comparable with trapping-inclusive models.
- **Nothing measured.** No liquid-lithium breeder blanket has operated in any fusion device.

## Access limitations

Read 2 November 2026 via the harness's fetch of the IOP landing page, two passes over a
177,150-character page. **Coverage is partial** — §3.4 onward recovered only in part; licence and
affiliations absent from the retrieved text. **CC BY 4.0** per Crossref. The raw capture remains
the Crossref JSON; `raw/` is append-only.
