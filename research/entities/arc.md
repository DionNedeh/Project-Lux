---
title: "ARC"
type: entity
entity_type: machine
country: "United States"
status_detail: planned
operator: "[[commonwealth-fusion-systems]]"
net_electric_mwe: 400
site: "Chesterfield County, Virginia"
first_power_target: "early 2030s"
tags:
  - fusion/entity
  - fusion/machines
  - fusion/economics
status: stable
confidence: high
related:
  - "[[sparc]]"
  - "[[commonwealth-fusion-systems]]"
  - "[[lcoe-fusion]]"
  - "[[29-remote-handling-and-maintenance]]"
  - "[[30-power-plant-designs-compared]]"
created: 2026-08-26
updated: 2026-11-02
---
*Affordable, Robust, Compact.* The first grid-scale commercial fusion power plant, and the design that reorganised the field when published from MIT in 2015.

## The 2015 paper

R = **3.3 m**, B₀ = **9.2 T**, I_p ≈ 7.8 MA, **525 MW** fusion, ~200 MWe. Three architectural choices define it — **all three about maintenance and lifetime, not plasma physics**:

1. **Demountable toroidal field magnets** — joints allow the entire vacuum vessel to be removed and replaced as a unit. The most-irradiated component becomes a **consumable**
2. **FLiBe liquid immersion blanket** — moderator, tritium breeder, coolant and shield simultaneously
3. **[[rebco]] HTS** — the enabling technology

## The design philosophy

ARC *enforces significant margin to disruptive operational limits* — strict limits on edge [[safety-factor]], [[greenwald-density-limit]] fraction, and **normalised [[plasma-beta|beta]] kept below the no-wall limit**. It buys margin with magnetic field rather than with control systems. A genuinely different bet from the ARIES advanced-tokamak line.

## The commercial plant

**~400 MWe from ~1.1 GW fusion**, at the James River Industrial Center, Chesterfield County, Virginia — the *Fall Line Fusion Power Station*, 94 acres. Cost **>$2.5 bn** (≈ $6,250/kW, the field's first real cost datum — see [[lcoe-fusion]]).

- Conditional-use permit approved **unanimously**
- **First fusion company to apply to PJM Interconnection**
- **[[google]] holds a 200 MW PPA** — half the output — plus equity


## The best-modelled fuel cycle in the corpus

ARC-class is the reference case for two MIT-led fuel-cycle studies, which makes it the design whose
tritium behaviour this vault can characterise in most depth — though none of it is CFS's own work.

[[meschini-2023-tritium-fuel-cycle-arc-step|Meschini *et al.* 2023]] model a 2LiF + BeF₂ liquid
immersion blanket and find required [[tritium-breeding-ratio|TBR]] stays **below 1.2** if
[[tritium-burn-fraction|tritium burn efficiency]] reaches **0.5–1%** — conditional on
[[availability|availability]] above 70%, processing under 4 h and
[[direct-internal-recycling|DIR]].

[[meschini-2025-trapping-tritium-self-sufficiency|Meschini *et al.* 2025]] then add
[[tritium-retention|trapping]], and the picture worsens materially: first-wall and vacuum-vessel
inventory up a **factor of 10³–10⁴**, [[tritium-doubling-time|doubling time]] **+50%**,
[[tritium-start-up-inventory|start-up inventory]] **+30%**, required TBR **+2–5%**.

**These are academic models of an ARC-*class* plant, not statements about the Chesterfield
machine**, and no measurement exists for any of it.

## Evidence in `raw/`

Primary sources held in this vault that evidence the claims above:

- [[arc-compact-high-field-demonstration-power-plant]]
- [[meschini-2023-tritium-fuel-cycle-arc-step]]
- [[meschini-2025-trapping-tritium-self-sufficiency]]
