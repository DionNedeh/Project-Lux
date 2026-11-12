---
title: "Helios"
type: entity
entity_type: machine
country: "United States"
status_detail: planned
operator: "[[thea-energy]]"
tags:
  - fusion/entity
  - fusion/machines
  - fusion/designs
status: stable
confidence: medium
sources:
  - "[[overview-of-the-helios-design]]"
  - "[[prototyping-test-canis-hts-planar-coil-array]]"
related:
  - "[[thea-energy]]"
  - "[[eos]]"
  - "[[canis]]"
  - "[[stellarator]]"
  - "[[rebco]]"
  - "[[balance-of-plant]]"
  - "[[primary-heat-transfer-system]]"
  - "[[eu-demo]]"
  - "[[recirculating-power]]"
  - "[[lithium-lead-eutectic]]"
  - "[[quasi-symmetry]]"
  - "[[30-power-plant-designs-compared]]"
  - "[[04-magnetic-confinement-devices]]"
created: 2026-09-08
updated: 2026-09-12
---
[[thea-energy|Thea Energy]]'s **deuterium-tritium planar-coil [[stellarator]] power plant**, existing as a **preconceptual design only**. It follows [[canis]] (a magnet-array prototype, built) and [[eos]] (a planned demonstrator). Evidence: [[overview-of-the-helios-design]].

## Design point

A two-field-period **quasi-axisymmetric** equilibrium ([[quasi-symmetry]]) with aspect ratio 4.5, major radius 8 m, minor radius 1.8 m, 6 T on axis and 500 m³ of plasma. It is designed to run **ignited and steady-state** — 10 MW of ECRH to start up, under 1 MW thereafter, with a roughly two-hour startup.

| Quantity | Value |
|---|---|
| Fusion power | 958 MW |
| Total thermal power | 1,094 MW |
| Net electric power | ~390 MWe |
| Magnet operating temperature | 20 K |
| Maximum field on coil | 20 T |
| Idealised [[tritium-breeding-ratio\|TBR]] | 1.3 |
| Capacity factor | 88% |

The coil set is **12 large plasma-encircling coils plus 324 smaller field-shaping coils**, all planar and convex, all [[rebco|HTS]]. Individually controlling the shaping coils is what buys relaxed manufacturing tolerance and bootstrap-current control. Encircling coils are insulated with active [[quench]] dumping to external resistors; shaping coils are partially insulated and self-protecting. The 20 T cap is set against achieved practice — 20.1 T in existing large-bore HTS magnets.

## Architecture choices worth noting

- A **toroidally continuous non-resonant X-point [[divertor]]**, tokamak-like, which the authors state is the first time a stellarator equilibrium has been explicitly designed to include one. Targets are 51,000 tessellated hexagonal [[tungsten-pfc|tungsten]] tiles under an assumed 10 MW/m² heat flux, helium-jet cooled.
- A **[[lithium-lead-eutectic|Pb-17Li]]** breeding blanket, 65% enriched in [[lithium-6]], in a uniform 50 cm layer with EUROFER97 structure and helium cooling.
- A **V-4Cr-4Ti first wall** with tungsten armour, chosen over [[rafm-steel|RAFM steel]] for a 15-full-power-year life — with an immature supply chain acknowledged as a contraindication.
- Maintenance removes **entire toroidal sectors** from between the encircling coils, on one 84-day outage every two years.

## The boundary

Nothing about Helios is demonstrated. Confinement rests on ISS04 scaling with an enhancement factor of 1.4 — a value achieved in [[wendelstein-7-x|W7-X]] but not in this geometry — and beta is capped at 2.7% for conservatism. Set against pulsed [[eu-demo|EU-DEMO]], which needs 8–14 [[primary-heat-transfer-system|primary coolant systems]] and a molten-salt store, Helios needs neither — the architectural dividend of steady state. See [[balance-of-plant]] and [[overview-of-the-helios-design]] for what the source does and does not establish.
