---
title: "Maturation of Critical Technologies for the DEMO Balance of Plant Systems"
type: source
source_type: paper
file: "raw/papers/Maturation-of-critical-technologies-DEMO-balance-of-plant.pdf"
authors: "Barucca, Hering, Perez Martin et al. (34 authors)"
publisher: "Fusion Engineering and Design 179, article 113096"
source_date: 2022-06-01
ingested: 2026-09-12
tags:
  - fusion/source
  - fusion/engineering
  - fusion/subsystems
status: stable
confidence: high
related:
  - "[[balance-of-plant]]"
  - "[[primary-heat-transfer-system]]"
  - "[[eu-demo]]"
  - "[[thermal-storage-pulsed-operation]]"
  - "[[tokamak-cooling-systems-and-power-conversion-system-options]]"
  - "[[lithium-lead-eutectic]]"
  - "[[24-grid-integration-and-operations]]"
  - "[[09-engineering-challenges]]"
created: 2026-09-12
updated: 2026-09-12
---
The EUROfusion **Pre-Concept Design** of [[eu-demo|EU-DEMO]]'s [[balance-of-plant|balance of plant]], covering both candidate blankets — Water-Cooled Lithium Lead (WCLL) and Helium-Cooled Pebble Bed (HCPB) — plus an assessment of rejected variants. Thirty-four authors across Ansaldo Nucleare, KIT, ENEA, Palermo, Sapienza, UNED, UC3M, Consorzio RFX, VTT, Fortum and Politecnico di Torino.

**Version of record, CC BY 4.0**, obtained from the KIT institutional repository rather than the publisher, which is CAPTCHA-walled. This is a **design study at pre-concept maturity** — no hardware, no operating measurements.

## Why fusion balance of plant is not a solved problem

The paper's Table 1 sets DEMO against a European Pressurized Reactor, and the comparison is the most quotable thing in it:

| | WCLL BoP | HCPB BoP | EPR |
|---|---|---|---|
| Plant thermal power | 2260.4 MWth | 2366.2 MWth | 4300.0 MWth |
| Separated primary coolant systems | **8** | **14** | **1** (4 loops) |
| Primary heat exchangers / steam generators | **10** | **14** | **4** |
| Steam cycle | superheated Rankine | — | saturated Rankine |

**At roughly half the thermal power, DEMO needs eight to fourteen separate primary coolant systems where a fission plant needs one.** That is the concrete form of the claim that balance of plant dominates plant cost and complexity. Heat arrives from four [[primary-heat-transfer-system|PHTS]] families — breeding zone, first wall, divertor (cassettes and plasma-facing components) and vacuum vessel — each with its own conditions.

## The pulsed-operation problem, priced

Because DEMO pulses, something must keep the turbine turning through dwell. Two references emerged:

- **WCLL — direct coupling with a small energy store.** HITEC molten salt (**400 m³**, 41 MWe electrical heater) feeds a molten-salt steam generator delivering **about 10% of nominal steam load** in dwell, purely to hold generator synchronism with the grid.
- **HCPB — indirect coupling.** An intermediate loop plus store decouples the blanket PHTS from the power conversion system entirely, sized so the turbine sees **the same steam load in dwell as in pulse** — a power conversion system the authors can then call "not pulsed". Its technology is borrowed from **concentrated solar power** (~200 MWe, storage to 1 GWh_th), which is qualified industrially.

Auxiliary gas-fired boiler variants (250 MW for WCLL, ~200 MWth for HCPB) were assessed and judged unattractive on size. Divertor and vacuum-vessel PHTS heat is demoted to feedwater preheating, to lift cycle efficiency.

## What it does not establish

No net cycle efficiency is stated, so none is recorded here. The open problems are named rather than solved: the once-through steam generator must operate stably at **1% of nominal power in dwell**, against normal industrial practice of 5% and above, and steam-turbine rotor materials for very-low-load pulsating duty are an open R&D item. Availability findings are described as preliminary.
