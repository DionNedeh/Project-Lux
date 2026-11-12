---
title: "Tritium Burn Fraction"
type: concept
domain: physics
symbol: "f_b"
units: "dimensionless (per cent)"
tags:
  - fusion/concept
  - fusion/physics
  - fusion/subsystems
status: stable
confidence: high
sources:
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
  - "[[st-e1-tritium-systems-crossref-metadata-2026]]"
  - "[[yang-2026-st-e1-tritium-tmap8-surrogate-models]]"
related:
  - "[[tritium-breeding-ratio]]"
  - "[[tritium-start-up-inventory]]"
  - "[[direct-internal-recycling]]"
  - "[[availability]]"
  - "[[pellet-injection]]"
  - "[[helium-ash]]"
  - "[[iter]]"
  - "[[09-engineering-challenges]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
created: 2026-10-19
updated: 2026-11-02
---
The fraction of tritium fuelled into the plasma that actually **fuses** before confinement is lost.
Formally, burning rate over fuelling rate
([[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency|Abdou *et al.* 2021]]).

**It is small, and that is the problem.** Nearly every atom injected returns unburnt for
re-processing — so burn fraction, not breeding, sets a plant's tritium inventory.

## Why it dominates the fuel cycle

Unburnt tritium still has to be *handled*, and time in the exhaust train, isotope separation and
storage is [[tritium-start-up-inventory|inventory]] — bought before startup, decaying while it
waits. So what matters is never `f_b` alone but its **product with fuelling efficiency**.

| `η_f · f_b` | Consequence (3 GW plant) |
|---|---|
| 0.36% — ITER's estimate at maximum fuelling | Required [[tritium-breeding-ratio\|TBR]] **1.82**, start-up inventory **>200 kg**: unacceptable |
| 2% | Start-up inventory **11 kg** at 4 h processing |
| 5% | Required TBR **1.02**, start-up inventory **<5 kg** at 1 h processing |

**Requirement: `η_f · f_b` > 2%, ideally 5%.** Below 1% it fails however good the blanket is.

> [!warning] Never write burn fraction bare
> `f_b` and `η_f · f_b` differ by about fourfold at reference fuelling efficiency. The
> [[yang-2026-st-e1-tritium-tmap8-surrogate-models|ST-E1 modelling paper]] tabulates a "tritium burn
> efficiency" of 0.02 and **never defines it** — the same class of defect as
> [[q-gain-definitions|unqualified Q]].

## The route to raising it

Fuelling efficiency `η_f` has a reference value of **25%**, with DEMO extrapolations *below* it. The
favoured route is **high-field-side [[pellet-injection|pellet injection]]**, projected at **25–50%**
— projections, not measurements, and ones Abdou *et al.* call *"highly uncertain"* at shallow
penetration. Detail on [[pellet-injection]].

The deeper obstacle: it cannot be measured where it matters. DEMO predictions are *"highly uncertain
because of lack of experiments with burning plasma"*. [[helium-ash]] dilution caps it further.

> [!note] Corroborated independently — and now with figures, 2026-11-02
> [[st-e1-tritium-systems-crossref-metadata-2026|ST-E1's fuel-cycle paper]] reports **extraction
> sensitivity and fuelling efficiency as the dominant drivers, *rather than marginal improvements
> in breeding ratio*** — Abdou's reframing, by a different method with no shared authorship. Its
> full text gives **f_b = 2.6%** at η_f **76%** (R = 0.1) or **2.9%** at **68%** (R = 0.2), for a
> burn efficiency of **2%**; it does not say which is the reference.
>
> That 2% clears [[meschini-2023-tritium-fuel-cycle-arc-step|Meschini *et al.* 2023]]'s
> **0.5–1%** requirement — but Meschini attach **availability > 70%**, processing **< 4 h** and
> [[direct-internal-recycling|DIR]], and ST-E1's figure assumes **100% availability**
> ([[availability]]). The margin is real; the operating point is not demonstrated.

## Status

**Never demonstrated at reactor-relevant values.** No device has operated a burning D-T plasma long
enough to establish `f_b` in a reactor regime, and the figures above are a mixture of ITER
projections and design requirements. See [[09-engineering-challenges]] and
[[14-open-problems-and-risks]].
