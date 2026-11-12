---
title: "Modeling and analysis of the tritium fuel cycle for ARC- and STEP-class D-T fusion power plants"
type: source
source_type: paper
file: "raw/papers/Meschini-2023-tritium-fuel-cycle-ARC-STEP.pdf"
authors: "S. Meschini (Politecnico di Torino), S. E. Ferry, R. Delaporte-Mathurin, D. G. Whyte (MIT Plasma Science and Fusion Center)"
publisher: "Nuclear Fusion 63 126005 (34 pp), DOI 10.1088/1741-4326/acf3fc, CC BY 4.0"
source_date: 2023-09-14
ingested: 2026-11-02
tags:
  - fusion/source
  - fusion/subsystems
  - fusion/designs
status: stable
confidence: high
related:
  - "[[arc]]"
  - "[[step]]"
  - "[[st-e1]]"
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
  - "[[meschini-2025-trapping-tritium-self-sufficiency]]"
  - "[[tritium-breeding-ratio]]"
  - "[[declared-tbr-values]]"
  - "[[tritium-burn-fraction]]"
  - "[[tritium-start-up-inventory]]"
  - "[[tritium-doubling-time]]"
  - "[[direct-internal-recycling]]"
  - "[[availability]]"
  - "[[spherical-tokamak]]"
  - "[[dennis-whyte]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
  - "[[30-power-plant-designs-compared]]"
created: 2026-11-02
updated: 2026-11-02
---
The first source in this vault to apply
[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency|Abdou *et al.*'s]] fuel-cycle method to
**named private-sector plant designs** rather than to a generic DEMO. Full text held;
**CC BY 4.0**, version of record.

> [!note] Citation year
> This paper cites its parent as *Abdou et al 2020 Nucl. Fusion 61 013001*. That is the
> **same paper** this vault holds as [[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]] —
> online 2020, issue-dated 2021. One work, two years in circulation.

## What it models

A time-dependent, system-level fuel cycle in Matlab Simulink, applied to three designs:
**[[arc|ARC]]-class**, breeding in a 2LiF + BeF₂ (FLiBe) liquid immersion blanket; and **two
[[step|STEP]]-class** variants, one with a liquid-lithium blanket, one with an encapsulated
breeding blanket of FLiBe pebbles, gas-cooled.

## The headline requirement

**Required [[tritium-breeding-ratio|TBR]] stays below 1.2 — but only if tritium burn
efficiency reaches 0.5–1%.** The paper calls that *"significant, but attainable"* improvement
over current ability. It is bounded against a maximum achievable TBR the authors put at
**1.1–1.2 depending on blanket design**, so the margin is thin by construction.

Three further conditions come attached, and all three are demanding:

| Requirement | Value |
|---|---|
| Plant availability | **> 70%** |
| Tritium processing time | **< 4 h** |
| [[direct-internal-recycling\|Direct internal recycling]] | **required** |

## Why burn fraction dominates, in one number

Run the model at ITER's expected achievable [[tritium-burn-fraction|burn fraction]] of
**f_b = 0.36%** — two pellet injectors, maximum fuelling 120 Pa m³ s⁻¹ — and the required TBR
for self-sufficiency in [[eu-demo|DEMO]] becomes **1.82**, which the authors note is far above
anything achievable. This is the paper's clearest statement of the reframing
[[tritium-burn-fraction|`η_f · f_b`]] carries: breeding cannot rescue a plant that burns
almost none of what it is fed.

**[[tritium-doubling-time|Doubling time]] buys relief.** At `t_d` = 1 year, self-sufficiency
is *"highly unlikely"* below 1% burn efficiency; at `t_d` = 5 years it becomes *"much easier
to achieve"*.

## What it does **not** establish

- **Nothing measured.** A system-level model of two unbuilt plant classes, benchmarked against
  no operating fuel cycle, because none exists.
- **Not ST-E1.** The STEP-class liquid-lithium case is the nearest analogue to
  [[st-e1|ST-E1]]'s architecture, but it is STEP, modelled independently of Tokamak Energy.
- **No trapping.** Tritium held in first wall, divertor and blanket is outside this model —
  the gap its own authors closed two years later in
  [[meschini-2025-trapping-tritium-self-sufficiency]].
