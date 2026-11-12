---
title: "Overview of the Helios Design: A Practical Planar Coil Stellarator Fusion Power Plant"
type: source
source_type: paper
file: "raw/papers/Overview-of-the-Helios-design.pdf"
authors: "Swanson, Kumar, Dudt et al. (42 authors, Thea Energy)"
publisher: "arXiv:2512.08027v3 (preprint); Fusion Engineering and Design (version of record)"
source_date: 2026-01-05
ingested: 2026-09-08
tags:
  - fusion/source
  - fusion/designs
  - fusion/engineering
status: stable
confidence: high
related:
  - "[[helios]]"
  - "[[thea-energy]]"
  - "[[eos]]"
  - "[[canis]]"
  - "[[balance-of-plant]]"
  - "[[recirculating-power]]"
  - "[[30-power-plant-designs-compared]]"
  - "[[09-engineering-challenges]]"
created: 2026-09-08
updated: 2026-09-12
---
The overview paper for [[thea-energy|Thea Energy]]'s **preconceptual design** of [[helios|Helios]], a planar-coil [[stellarator]] power plant, summarising a *Fusion Engineering and Design* special issue and referring detail to some twenty companion papers. Funded under the [[us-doe]] Milestone-Based Fusion Development Program.

**This is a design study, not a result.** Every figure below comes from simulation — DESC, BP3, OpenMC, TMAP8, COMSOL, Amesim. No Helios hardware exists; Thea's only hardware evidence remains [[canis]] ([[prototyping-test-canis-hts-planar-coil-array]]).

## The facility power balance

The vault's first end-to-end company-authored accounting ([[balance-of-plant]]), read from both the §4.4 text and the Figure 11 Sankey diagram:

| Stage | Value |
|---|---|
| D-T fusion power | 958 MW (80% neutrons) |
| Lithium-6 breeding exotherm | +135 MW |
| Total thermal | **1,094 MW** |
| Generated electric | 459.9 MWe |
| Coolant pumping | −21.8 → gross **438.1 MWe** |
| Auxiliary (maintenance 20.0, tritium 15.0, cryoplant 10.5, ECRH 2.5) | −48.0 MWe |
| **Net to grid** | **390.1 MWe** |

Lead-lithium and helium feed intermediate heat exchangers; steam superheated to **635 °C** drives three turbines. The diagram settles a question the prose leaves open — the 2.5 MW ECRH budget sits *inside* the 48 MW, not beside it.

> [!warning] Two efficiency conventions, one plant
> Rankine efficiency is reported as **~40.2%**, and as **~42.2%** if computed from total generated power, "as in some fusion power plant design studies". Never write either bare — this is the [[q-gain-definitions|error class of unqualified Q]].

Because Helios is designed **ignited**, no `Q_sci` is quoted. No cost or LCOE appears, so nothing here bears on [[lcoe-fusion]].

## Access limitations

Inspected in full: the **arXiv v3 preprint** (submitted 8 December 2025, v3 dated 5 January 2026), captured to `raw/` and cross-checked against Thea's author-hosted PDF of 10 December 2025 on seventeen key figures — all agreeing. The publisher version of record was unreachable; ScienceDirect serves a CAPTCHA.

**Not inspected:** the dedicated companion paper on this exact subject — Tang *et al.*, *Fusion Engineering and Design* **230**:115896, DOI 10.1016/j.fusengdes.2026.115896. It is CC BY 4.0, yet Unpaywall and OpenAlex record the publisher page as its only open-access location, and it is absent from arXiv, OSTI and Thea's own listing. Every power figure above is therefore the overview's *summary* of that paper.

## Internal tensions preserved

- **Tritium.** Table 1 gives startup inventory **1–2 kg** and idealised [[tritium-breeding-ratio|TBR]] **1.3**; the fuel-cycle section concludes **<1 kg** and TBR **<1.15** suffice. Design value versus analysis requirement.
- **Waste heat.** §4.4 states **681 MW**; Figure 11 labels the sink **703.0 MW**. The diagram total is consistent with also absorbing plasma-vessel coolant and auxiliary loads (1,094.1 − 390.1 = 704.0); the prose figure reconciles to no stated sum.

Neither affects the headline chain, on which text and diagram agree to within rounding.

> [!note] Where the decimal values live
> The itemised figures exist **only in the Figure 11 image**, not the PDF text layer — `raw/extracts/` will not contain them. Re-render page 15 to re-check.
