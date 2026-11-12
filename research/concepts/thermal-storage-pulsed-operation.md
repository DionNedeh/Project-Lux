---
title: "Pulsed Operation and Thermal Storage"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/economics
status: stable
confidence: high
sources:
  - "[[tokamak-cooling-systems-and-power-conversion-system-options]]"
  - "[[maturation-of-critical-technologies-demo-balance-of-plant]]"
related:
  - "[[bootstrap-current]]"
  - "[[stellarator]]"
  - "[[helion-energy]]"
  - "[[balance-of-plant]]"
  - "[[primary-heat-transfer-system]]"
  - "[[24-grid-integration-and-operations]]"
  - "[[eu-demo]]"
created: 2026-08-26
updated: 2026-09-12
---
A [[tokamak]] driven inductively runs in pulses — [[iter]] at 500 MW for 400 seconds; most power plant designs at hours followed by a dwell of minutes.

## The DEMO duty cycle

| Phase | Duration | Power |
|---|---|---|
| Pulse (burn) | **2 hours** | nominal |
| Ramp-up / ramp-down | **100–200 s** each | transitional |
| Dwell | **~10 minutes** | **1–2% of nominal** (residual heat) |

The residual 1–2% is the crux: not zero, so nothing fully settles, yet far too little to hold a turbine ([[tokamak-cooling-systems-and-power-conversion-system-options]]).

The problem is not primarily grid stability. **It is turbine life.** Thermally cycling a several-hundred-megawatt steam turbine causes differential expansion, rotor stress and creep-fatigue in exactly the components most expensive to replace.

## The three ways out

1. **Thermal storage** — a molten-salt buffer between core and power conversion, so the turbine sees continuous steam. The EU DEMO baseline. Large, expensive, lossy, and **rarely included in published LCOE figures**. Recent work proposes hybrid thermal-plus-electrochemical storage
2. **Steady state** — 70–90% [[bootstrap-current]] fraction. Harder physics
3. **Pulse far faster than any thermal timescale** — [[helion-energy]] at ~1 Hz with [[direct-energy-conversion]]; inertial fusion at 10–20 Hz. The pulsation disappears entirely

## How DEMO actually does it

Two references, one per blanket ([[maturation-of-critical-technologies-demo-balance-of-plant]]):

- **WCLL — direct coupling, small store.** HITEC molten salt (**400 m³**) sustains about **10% of nominal steam load** through dwell — sized not to keep producing power but to **stop the generator losing grid synchronism**. The turbine still cycles.
- **HCPB — indirect coupling, full store.** An intermediate loop decouples the blanket loops entirely, so the turbine sees **the same load in dwell as in pulse** — a power conversion system the authors can call "not pulsed" — borrowing qualified **concentrated solar power** practice.

> [!warning] The turbine still has to tolerate the trough
> Either way the once-through steam generator must run stably at **1% of nominal** in dwell, against industrial practice of 5% and above; rotor materials for that duty remain open R&D.

**[[stellarator|Stellarators]] never have the problem** — no plasma current, no transformer, no dwell. That removes a multi-hundred-million-dollar storage system and a turbine lifetime penalty. [[helios|Helios]] is the worked example: no store at all, because output never pulses.

**The awkward case is the middle one** — pulses of minutes to hours — which is where the leading concept sits.
