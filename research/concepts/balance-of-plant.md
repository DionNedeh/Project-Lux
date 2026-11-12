---
title: "Balance of Plant"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/subsystems
status: draft
confidence: medium
sources:
  - "[[overview-of-the-helios-design]]"
  - "[[maturation-of-critical-technologies-demo-balance-of-plant]]"
  - "[[tokamak-cooling-systems-and-power-conversion-system-options]]"
  - "[[doe-fusion-science-technology-roadmap-2026]]"
related:
  - "[[recirculating-power]]"
  - "[[thermal-storage-pulsed-operation]]"
  - "[[availability]]"
  - "[[lcoe-fusion]]"
  - "[[direct-energy-conversion]]"
  - "[[rafm-steel]]"
  - "[[helios]]"
  - "[[eu-demo]]"
  - "[[primary-heat-transfer-system]]"
  - "[[09-engineering-challenges]]"
  - "[[10-economics-and-markets]]"
  - "[[24-grid-integration-and-operations]]"
  - "[[30-power-plant-designs-compared]]"
created: 2026-09-08
updated: 2026-09-12
---
Everything between the blanket and the grid: the **primary heat transfer system** (PHTS), the intermediate heat exchangers, the thermodynamic cycle, the turbine-generator, and the electrical systems that both feed the plant and export from it.

**It is the majority of the plant and a minority of the discussion.** Balance of plant is **30–40% of capital cost** ([[30-power-plant-designs-compared|Document 30]]), capping how much core innovation can reduce total cost.

## The chain that sets efficiency

Conversion efficiency is **35–45%** for a Rankine or closed Brayton cycle, and is not a free parameter: it follows from coolant outlet temperature, which follows from the structural material's temperature limit, which follows from irradiation behaviour — the whole path from neutron damage to electricity price running through [[rafm-steel|one materials link]]. What the plant consumes to run itself is then subtracted as [[recirculating-power|recirculating power]].

> [!warning] Say which efficiency
> Cycle efficiency can be quoted against gross generated power or net of coolant pumping, and the two differ by around two percentage points on the same design. [[helios|Helios]] reports **~40.2%** net of pumping and **~42.2%** on total generated power, explicitly noting the second convention is used "in some fusion power plant design studies". An unqualified cycle efficiency is as ambiguous as an unqualified [[q-gain-definitions|Q]].

## A worked design case

[[helios|Helios]] is the vault's only end-to-end company-authored accounting ([[overview-of-the-helios-design]], a **design study**, not a measurement). Lead-lithium and helium carry heat to intermediate heat exchangers; steam superheated to **635 °C** drives three turbines. Of **1,094 MW** thermal, **459.9 MWe** is generated and **69.8 MW** of that runs the plant, leaving **390.1 MWe** net — itemised in [[recirculating-power]].

## Two architectures, and why they differ

Set that against [[eu-demo|EU-DEMO]], whose pre-concept balance of plant is the public-programme counterpart ([[maturation-of-critical-technologies-demo-balance-of-plant]]):

| | Helios | EU-DEMO |
|---|---|---|
| Operation | steady-state | 2 h pulse, ~10 min dwell |
| Energy storage | none | molten salt, required |
| Primary coolant systems | — | **8** (WCLL) to **14** (HCPB) |

**A fission EPR has one primary circuit at 4,300 MWth.** DEMO needs eight to fourteen at roughly half that — the sharpest available statement of why fusion balance of plant is not borrowed technology. The loops themselves are [[primary-heat-transfer-system|primary heat transfer systems]]; the buffering problem is [[thermal-storage-pulsed-operation|thermal storage]], which a [[stellarator]] avoids entirely.
