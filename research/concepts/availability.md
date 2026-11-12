---
title: "Availability and RAMI"
type: concept
domain: engineering
symbol: "capacity factor"
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/economics
  - fusion/risks
status: stable
confidence: high
sources:
  - "[[overview-of-the-helios-design]]"
  - "[[tokamak-cooling-systems-and-power-conversion-system-options]]"
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
  - "[[willis-2026-st-e1-pre-concept-design-overview]]"
related:
  - "[[29-remote-handling-and-maintenance]]"
  - "[[10-economics-and-markets]]"
  - "[[24-grid-integration-and-operations]]"
  - "[[arc]]"
  - "[[helios]]"
  - "[[st-e1]]"
  - "[[balance-of-plant]]"
  - "[[tritium-breeding-ratio]]"
  - "[[tritium-burn-fraction]]"
  - "[[tritium-start-up-inventory]]"
  - "[[tcv-predict-first-rampdown-2025]]"
created: 2026-08-26
updated: 2026-11-02
---
**Fusion's most economically decisive and least-analysed parameter.**

LCOE is inversely proportional to capacity factor: **a plant at 50% availability costs twice as much per MWh as the same plant at 100%.** Fission achieves 90%+.

## Where fusion availability goes

| Cause | Frequency | Duration |
|---|---|---|
| Divertor replacement | Every 1–2 full-power years | Months |
| Blanket module replacement | Every 2–5 years | Months |
| Planned remote inspection | Annual | Weeks |
| [[disruption]] recovery | Unplanned | Days to months |
| [[quench]] | Rare | Weeks to years |

Fission achieves this with **direct human access during outage** and forty years of practice; fusion has neither ([[29-remote-handling-and-maintenance]]). For calibration: [[jet]]'s first-wall replacement took **18 months of two-shift working**, entirely remotely.

## The state of the discipline

DOE's roadmap asks, as a **near-term** deliverable, to *"establish an initial RAMI handbook with metrics, availability targets, and design-for-maintainability guidance."*

**The industry has no agreed availability metrics**, let alone data. Design studies routinely assume 75–85% for machines whose remote maintenance has never been demonstrated — one assumption that can move LCOE twofold.

[[helios|Helios]] assumes **88%** on **one 84-day outage every two years** ([[overview-of-the-helios-design]]), via sector-based maintenance: whole toroidal sectors withdrawn from between encircling coils that stay in place. A coherent answer to the rows above, and **an assumption, not a demonstrated cycle time** — no device has performed a sector exchange.

[[eu-demo|EU-DEMO]]'s pre-concept work reports balance-of-plant availability **could** meet programme requirements ([[tokamak-cooling-systems-and-power-conversion-system-options]]) — called **preliminary** by its own authors. That is the state of the evidence: targets and models, not operating records.

This is the likeliest reason a technically successful plant turns out commercially useless.

## It also gates tritium self-sufficiency

| Availability factor | Tritium self-sufficiency |
|---|---|
| **< 10%** | **Impossible** for any `η_f · f_b` |
| **> 30%**, 1% ≤ `η_f · f_b` ≤ 2% | Possible |
| **> 50%**, `η_f · f_b` > 2% | Reasonable confidence |

A plant spends downtime **not breeding** while its inventory decays, so low availability raises
required [[tritium-breeding-ratio|TBR]] and [[tritium-start-up-inventory|start-up inventory]]
together. **FNSF, VNS and CTF are predicted below 30%**, so the devices meant to demonstrate
breeding blankets may not close their own fuel cycle. **RAMI is not only an economics problem; it is
a fuel-supply problem.**

[[meschini-2023-tritium-fuel-cycle-arc-step|Meschini *et al.* 2023]] put a sharper number on it:
self-sufficiency in [[arc|ARC]]- and [[step|STEP]]-class plants requires availability **above
70%**, alongside processing under 4 h and [[direct-internal-recycling|DIR]]. Their model's best
achievable availability, on optimistic processing times, is **94%**.

> [!warning] ST-E1 now spans 37.5% to 100% across three sources
> | Figure | Where |
> |---|---|
> | **100%** | [[st-e1-tritium-systems-crossref-metadata-2026\|086004]], stated as a simplification offset by a 20% contingency |
> | **> 80%** | the design mission ([[willis-2026-st-e1-pre-concept-design-overview]]) |
> | **37.5%** | [[yang-2026-st-e1-tritium-tmap8-surrogate-models\|Yang 2026]]'s fuel-cycle modelling |
>
> The **152-day [[tritium-doubling-time|doubling time]]** 086004 reports is computed at the top of
> that range. Recorded 2026-11-02; no source reconciles the three.
