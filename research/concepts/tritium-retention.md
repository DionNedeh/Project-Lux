---
title: "Tritium Retention"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/subsystems
  - fusion/materials
status: draft
confidence: medium
sources:
  - "[[meschini-2025-trapping-tritium-self-sufficiency]]"
  - "[[sindelar-2023-tritium-accountancy-control-challenges-fusion]]"
  - "[[st-e1-tritium-systems-crossref-metadata-2026]]"
related:
  - "[[tritium-accountancy]]"
  - "[[tritium-breeding-ratio]]"
  - "[[tritium-start-up-inventory]]"
  - "[[tritium-doubling-time]]"
  - "[[tungsten-pfc]]"
  - "[[displacements-per-atom]]"
  - "[[boronization]]"
  - "[[divertor]]"
  - "[[arc]]"
  - "[[st-e1]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
  - "[[09-engineering-challenges]]"
created: 2026-11-02
updated: 2026-11-02
---
Tritium that enters plant structures and **stops** — trapped in the first wall, divertors and
breeding blanket rather than circulating through the fuel cycle. It is the term every
fuel-cycle model in this vault omitted until
[[meschini-2025-trapping-tritium-self-sufficiency|Meschini *et al.* 2025]].

## Why omitting it was not conservative

Trapping does not merely park inventory; it **slows the whole cycle**, because trapped tritium
is unavailable to breed the next plant's start-up charge. For an [[arc|ARC]]-class plant,
accounting for trapping, irradiation-induced traps and component replacement raises first-wall
and vacuum-vessel inventory by a **factor of 10³–10⁴**, and carries through as:

| Quantity | Change |
|---|---|
| [[tritium-doubling-time\|Doubling time]] | +50% |
| [[tritium-start-up-inventory\|Start-up inventory]] | +30% |
| Required [[tritium-breeding-ratio\|TBR]] | +2–5% |

Two effects compound it. Neutron damage **creates** new traps as the plant runs
([[displacements-per-atom|dpa]] accumulating in [[tungsten-pfc|tungsten]] and structure), and
scheduled component replacement physically **removes** trapped inventory from the plant.

> [!warning] It enters accountancy as a residual, not a measurement
> [[tritium-accountancy]] records that no instrument exists to measure tritium production in
> the blanket or consumption in the plasma. Retention is therefore inferred from what the
> balance fails to close — so the term with the largest modelled uncertainty is the one
> measured least directly. [[sindelar-2023-tritium-accountancy-control-challenges-fusion|Sindelar
> 2023]] states such methods *"would need to be developed"*.

## What is not known

The 10³–10⁴ figure is **ARC-class with a FLiBe immersion blanket**. No source in this vault
models retention for a liquid-lithium [[st-e1|spherical tokamak]], and
[[st-e1-tritium-systems-crossref-metadata-2026|ST-E1's fuel-cycle paper]] assigns its first wall
and divertor only 0.012–0.024 kg — three orders below the ARC-class trapped figure, on a
different model with no trapping physics. The two are not comparable, and this vault does not
transfer one onto the other.

No measurement exists for any of it: no D-T fusion power plant has operated, so every retention
figure here is modelled.
