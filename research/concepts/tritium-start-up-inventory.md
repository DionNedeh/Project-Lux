---
title: "Tritium Start-up Inventory"
type: concept
domain: engineering
units: "kg"
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/economics
status: stable
confidence: high
sources:
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
  - "[[sindelar-2023-tritium-accountancy-control-challenges-fusion]]"
  - "[[st-e1-tritium-systems-crossref-metadata-2026]]"
  - "[[overview-of-the-helios-design]]"
related:
  - "[[tritium-breeding-ratio]]"
  - "[[tritium-burn-fraction]]"
  - "[[direct-internal-recycling]]"
  - "[[availability]]"
  - "[[tritium-accountancy]]"
  - "[[iter]]"
  - "[[helios]]"
  - "[[st-e1]]"
  - "[[eu-demo]]"
  - "[[09-engineering-challenges]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
  - "[[14-open-problems-and-risks]]"
created: 2026-10-19
updated: 2026-11-02
---
The tritium a D-T plant must **possess** on day one, before its blanket has bred anything — an
entry fee paid in its scarcest [[22-critical-materials-supply-chains|material]].

## The numbers

From [[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency|Abdou *et al.* 2021]]:

| Condition | Start-up inventory |
|---|---|
| `η_f · f_b` = 2%, processing time 4 h, 3 GW | **11 kg** |
| `η_f · f_b` = 5%, processing time 1 h, 3 GW | **<5 kg** |
| ITER's burn fraction (0.36%), 3 GW | **>200 kg** — stated as unacceptable |
| 100 MW facility | **~1 kg** |

**Inventory scales linearly with fusion power** — plants want to be large, and largeness makes the
entry fee unaffordable. Against a world civilian inventory of **30–40 kg**
([[tritium-breeding-ratio]]) at **$30,000–35,000/gram**, an 11 kg charge is a third of all that
exists; >200 kg exceeds world supply severalfold.

## What drives it down

1. **[[tritium-burn-fraction|Burn fraction and fuelling efficiency]]** — dominant; 2% to 5% more
   than halves the requirement.
2. **Processing time** — **1–4 h**, and the **isotope separation system dominates** it,
   which is why [[direct-internal-recycling]] reduces inventory directly.
3. **Reserve time** — a **24 h** reserve gives unacceptable inventories, so reserves must cover only
   **a few hours**, converting storage into a **reliability** problem.

> [!note] Two design claims, neither with a comparable figure
> [[helios|Helios]] gives **1–2 kg** against its own analysis concluding **under 1 kg**
> ([[overview-of-the-helios-design]]) — design value versus requirement, both far below Abdou's 3 GW
> figures and consistent with linear scaling from ~390 MWe.
> [[st-e1-tritium-systems-crossref-metadata-2026|ST-E1]] gives **1.58 kg** including a 20%
> commissioning contingency, 1.31 kg tritium-lean, with a [[tritium-doubling-time|doubling time]]
> of **152 days**. **CORRECTION 2026-11-02:** this page previously recorded ST-E1 as claiming *"low
> overall inventory"* with no figure attached — true of the abstract, not of the full text.

> [!warning] Trapping would raise every figure here by about a third
> [[meschini-2025-trapping-tritium-self-sufficiency|Meschini *et al.* 2025]] find start-up
> inventory **+30%** once [[tritium-retention|trapping]] is modelled, for an ARC-class plant.
> Nothing on this page includes it.

> [!warning] Not the same as *in-process* inventory
> A smaller quantity circulates at any moment: **[[iter|ITER]]'s is expected at ~1 kg**, commercial
> plants at several hundred grams to 1 kg
> ([[sindelar-2023-tritium-accountancy-control-challenges-fusion]]). That is the holdup the cycle
> minimises, **not** the charge a plant must own before starting. Same units, different quantities —
> see [[tritium-accountancy]].

## Who supplies the first charge

Nobody. Tritium comes mostly as a CANDU byproduct at **under 0.13 kg per reactor-year** and decays
at **5.5% per year**, so no stockpile can be built up in advance. Abdou *et al.*
name the institutional answer — a **fusion nuclear science facility** sized not for power but to
**accumulate surplus tritium for DEMO's start-up**, a brief no funded facility has. So this is a
*programme* question, not a plant one.
