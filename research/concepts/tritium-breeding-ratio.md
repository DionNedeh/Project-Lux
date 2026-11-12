---
title: "Tritium Breeding Ratio (TBR)"
type: concept
domain: engineering
symbol: "TBR"
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/materials
status: stable
confidence: high
sources:
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
  - "[[doe-fusion-science-technology-roadmap-2026]]"
  - "[[baby-tritium-self-sufficiency-experiment]]"
related:
  - "[[declared-tbr-values]]"
  - "[[lithium-6]]"
  - "[[unity-3]]"
  - "[[librti]]"
  - "[[iter]]"
  - "[[tritium-burn-fraction]]"
  - "[[tritium-start-up-inventory]]"
  - "[[direct-internal-recycling]]"
  - "[[availability]]"
  - "[[tritium-accountancy]]"
  - "[[09-engineering-challenges]]"
  - "[[19-simulation-codes-nuclear-data]]"
created: 2026-08-26
updated: 2026-11-02
---
Tritium bred per tritium consumed. **The precondition for fusion existing as an energy source.**

## Why it is not optional

A 1 GW plant burns **~55.6 kg/year** against a world civilian inventory of **30–40 kg**, produced as
a CANDU byproduct at **under 0.13 kg per reactor-year**, at **$30,000–35,000/gram**, decaying 5.5%
annually. **One plant would consume more than the world holds in its first year**, and there is no
market to buy from.

## The reactions

```
n + ⁶Li → T + ⁴He + 4.8 MeV      (exothermic, large low-energy cross-section)
n + ⁷Li → T + ⁴He + n − 2.5 MeV  (endothermic, regenerates the neutron)
```

Each fusion yields one neutron, and neutrons are lost to structure, ports and diagnostics — so
TBR > 1 generally needs **neutron multiplication** by [[beryllium]] or lead. **Design target:
TBR > 1.1** (DOE roadmap); failure threshold 1.0. **A 10% margin.**

## The achievability bands

From [[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency|Abdou *et al.* 2021]], the primary source
for a band the vault previously carried on the DOE roadmap's authority alone:

| Required TBR | Self-sufficiency |
|---|---|
| > 1.15 | **Unlikely** |
| 1.05 – 1.15 | **Possible** |
| ≤ 1.05 | **Attained with high confidence** |

**Maximum achievable** for the most detailed blanket designs is estimated at **1.15**, with high
confidence only at **1.05** — so requirement and capability occupy the same interval. That is the
whole difficulty.

> [!warning] The uncertainty is comparable to the margin, and biased
> Nuclear data uncertainty runs to a few percent, with 12% flux discrepancies between cross-section
> libraries ([[19-simulation-codes-nuclear-data]]). Worse, it is **biased**: integral experiments
> found calculation **overestimated** tritium production by an **average factor of 1.14** — an error
> in the dangerous direction, larger than the margin it eats. Abdou *et al.* call it *"alarming"* and
> report a recommended safety factor of **>1.1 to 1.2**.

## What actually binds

Not this quantity. Breeding is downstream of the plasma: what binds is
**[[tritium-burn-fraction|`η_f · f_b`]]** with processing time, while **[[availability]]** sets a
floor below which no blanket suffices. **No blanket improvement rescues a plant whose burn fraction
is too low** ([[09-engineering-challenges]]). The surplus is also the only **divertible** tritium a
plant makes — [[tritium-accountancy]].

## Declared values, and their conflicts

| Design | TBR |
|---|---|
| DOE roadmap target | > 1.1 |
| [[helios\|Helios]] | 1.3 idealised; < 1.15 required |
| [[st-e1\|ST-E1]] | 1.146 full coverage, 1.085–1.14 with penetrations — **reconciled 2026-11-02** |
| [[st-e1\|ST-E1]] neutronics | 1.169 (MCNP) · 1.194 (G4Tokamak) — above its own fuel-cycle baseline |
| [[arc\|ARC]]- / [[step\|STEP]]-class *required* | < 1.2, if burn efficiency reaches 0.5–1% |

Every declared figure, the disagreements between and within them, and what could not be resolved:
**[[declared-tbr-values]]**.

> [!warning] The *required* value moves too, and upward
> Declared values are what designs claim to achieve. What they must achieve is a separate
> quantity, and [[meschini-2025-trapping-tritium-self-sufficiency|Meschini *et al.* 2025]] raise it
> **2–5%** once [[tritium-retention|trapping]] is modelled. Against an achievable ceiling Abdou
> puts at **1.15**, a requirement already near 1.1 has little room to absorb that.

**Never demonstrated.** [[iter]]'s Test Blanket Modules are first, from **2039**; [[unity-3]] and
[[librti]] answer it sooner.
