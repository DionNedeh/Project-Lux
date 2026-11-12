---
title: "Displacements per Atom (dpa)"
type: concept
domain: engineering
symbol: "dpa"
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/materials
  - fusion/risks
status: stable
confidence: high
related:
  - "[[helium-embrittlement]]"
  - "[[rafm-steel]]"
  - "[[ifmif-dones]]"
  - "[[fpns]]"
  - "[[09-engineering-challenges]]"
created: 2026-08-26
updated: 2026-11-02
---
The standard measure of neutron displacement damage: how many times, on average, each atom in a material has been knocked out of its lattice site.

| Environment | dpa |
|---|---|
| [[iter]], entire operational life | **< 2** |
| Fusion power plant first wall | **~15 per year** |
| Target for a 5-year component life | **70–100** |
| [[ifmif-dones]] phase 1 / phase 2 | ~20 / ~50 |
| DOE roadmap **mid-term** dataset target | **~10** |

Read the last two rows together. **The mid-term target is 10 dpa against a power-plant need of 70–100**, and the facility that would generate the data does not yet operate.

## A worked case: ST-E1's centre column

A [[spherical-tokamak|spherical tokamak]] concentrates its damage inboard, and
[[st-e1-neutronics-crossref-metadata-2026|ST-E1's neutronics]] puts numbers on it:

| Location | dpa per full-power year |
|---|---|
| Tungsten carbide block, thin part of centre-column midplane | **≈ 50** (±6%) |
| Centre-column shield front, midplane | ≈ 18 |
| Lower overhead shield | ≈ 1.3 |
| Vacuum vessel structure | < 0.05 |

The centre-column figure is **five times the quoted first-wall rate** and at the top of the
70–100 dpa component-life band within two years. It is a calculated value for an unbuilt machine,
on a material — [[vanadium-alloys|V-4Cr-4Ti]] structure around a WC block — with no irradiation
dataset at that dose.

Damage alone is not the whole problem — see [[helium-embrittlement]] for why fission irradiation data cannot substitute.
