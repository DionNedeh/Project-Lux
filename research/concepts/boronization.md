---
title: "Boronization and Wall Conditioning"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/subsystems
status: stable
confidence: high
related:
  - "[[iter]]"
  - "[[tungsten-pfc]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
  - "[[globus-m2]]"
  - "[[15-references]]"
created: 2026-08-26
updated: 2026-08-29
---
Depositing a thin boron film on vessel walls to reduce impurity content — principally **oxygen** — in the vacuum.

Boron is low-Z (so any entering the plasma radiates weakly), **getters oxygen** chemically, suppresses metallic impurity influx by forming a protective coating, and reduces carbon contamination.

**Method:** chemical vapour deposition of elemental boron by **glow discharge** in helium containing boron hydrides — diborane (B₂H₆), trimethylboron, decaborane, or carborane vapour.

**Inter-Shot Boronization (ISB)** injects carborane *between* discharges for continuous in-situ conditioning, requires only basic vacuum hardware, and outperforms conventional glow-discharge boronization. Demonstrated on Globus-M2.

## ITER's system — a case study in second-order consequences

**In 2023 ITER changed its armour tiles from [[beryllium]] to [[tungsten-pfc|tungsten]].** Beryllium gettered oxygen naturally; tungsten does not. Removing beryllium removed ITER's built-in oxygen control, creating a requirement the original design did not have:

| | |
|---|---|
| Boron layer | **10–100 nm** across all plasma-facing surfaces |
| Precursor | **Diborane, 5% in helium** |
| Injection lines | **>1 km** in the Tokamak Building; **~400 m** inside the vessel |
| Injection points | **21** |
| Anodes | 4 additional, for even distribution |
| Effective life | **2.5–12.5 weeks**; planned interval **every 2 weeks** |
| Diborane destruction | 700 °C thermal breakdown, or chemical trapping — **in the Tritium Building** |
| Installation begins | **2028** |

A materials decision made for divertor lifetime produced a kilometre of gas lines, 21 vessel penetrations, a toxic-gas plant, and a fortnightly procedure — **on a machine that has not yet made a plasma.**
