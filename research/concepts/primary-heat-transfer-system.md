---
title: "Primary Heat Transfer System (PHTS)"
type: concept
domain: engineering
symbol: "PHTS"
aliases:
  - "PHTS"
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/subsystems
status: draft
confidence: medium
sources:
  - "[[tokamak-cooling-systems-and-power-conversion-system-options]]"
  - "[[maturation-of-critical-technologies-demo-balance-of-plant]]"
related:
  - "[[balance-of-plant]]"
  - "[[eu-demo]]"
  - "[[helios]]"
  - "[[divertor]]"
  - "[[lithium-lead-eutectic]]"
  - "[[thermal-storage-pulsed-operation]]"
  - "[[recirculating-power]]"
  - "[[09-engineering-challenges]]"
  - "[[24-grid-integration-and-operations]]"
created: 2026-09-12
updated: 2026-09-12
---
The closed coolant loops that take heat out of in-vessel components and hand it to the power conversion system. The first link in [[balance-of-plant|balance of plant]], and the one that has to survive the neutron flux.

## Why there are so many of them

A fission plant has one primary circuit. A fusion plant has a **family**, because its heat sources have incompatible temperatures, materials and safety classifications. [[eu-demo|EU-DEMO]] carries four kinds — breeding zone, first wall, divertor (cassette bodies and plasma-facing components separately) and vacuum vessel — adding up to **8 separated primary coolant systems for the WCLL blanket and 14 for HCPB**, against **1** for a European Pressurized Reactor at nearly twice the thermal power ([[maturation-of-critical-technologies-demo-balance-of-plant]]).

The blanket loop is what differs between designs; **divertor and vacuum-vessel loops use essentially the same arrangement for either blanket concept**.

## Operating conditions vary by an order of magnitude

| Loop | Fluid | Pressure | In / out |
|---|---|---|---|
| HCPB blanket | helium | ~8 MPa | 300 / 520 °C |
| Vacuum vessel | water | ~1 MPa | 190 / 200 °C |

That spread is the design problem. The hot loops set cycle efficiency; the cold ones are too cool to make good steam, so **divertor and vacuum-vessel heat is demoted to feedwater preheating** rather than driving the turbine.

## It is also a confinement barrier

The divertor PHTS is not only a cooling system. Its ex-vessel portions provide **primary confinement** for coolant carrying tritium and activated corrosion products ([[tokamak-cooling-systems-and-power-conversion-system-options]]) — so a heat-transfer component is also a nuclear safety component, which is much of why fusion balance of plant is harder to license than its thermal duty suggests.

## The alternative arrangement

[[helios|Helios]] shows a leaner variant: [[lithium-lead-eutectic|lead-lithium]] and helium feed intermediate heat exchangers directly, with no pulsed-duty buffering, because a steady-state [[stellarator]] never enters dwell. Both remain design studies — no fusion PHTS has operated at power.
