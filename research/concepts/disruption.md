---
title: "Disruption"
type: concept
domain: physics
tags:
  - fusion/concept
  - fusion/physics
  - fusion/risks
status: stable
confidence: high
related:
  - "[[runaway-electrons]]"
  - "[[shattered-pellet-injection]]"
  - "[[tokamak]]"
  - "[[stellarator]]"
  - "[[17-diagnostics-control-disruption]]"
  - "[[fusionmae-crossref-metadata-2026]]"
  - "[[tcv-predict-first-rampdown-2025]]"
  - "[[hl3-data-driven-rl-control-2025]]"
created: 2026-08-26
updated: 2026-08-26
---
The sudden, complete loss of plasma confinement in a [[tokamak]]. The tokamak's characteristic and structural design vulnerability.

## Sequence, in milliseconds

1. **Thermal quench** — the plasma's entire thermal energy (hundreds of MJ in [[iter]]) hits the wall in **under a millisecond**
2. **Current quench** — plasma current collapses; changing flux induces enormous eddy currents and electromagnetic forces. ITER's vessel is designed for tens of meganewtons
3. **[[runaway-electrons]]** — loop voltage accelerates electrons to tens of MeV, forming a beam carrying a large fraction of the original current

## Why it worsens with size

Runaway avalanche gain scales with plasma current. ITER at 15 MA is far more exposed than any existing machine.

## Related failure: vertical displacement events

Elongated plasmas are vertically unstable and held by active feedback. Losing control drives the column into the wall, generating **halo currents** through the structure — a primary structural design case.

**[[stellarator|Stellarators]], [[magnetic-mirror|mirrors]], [[field-reversed-configuration|FRCs]] and [[z-pinch|Z-pinches]] do not have this problem**, because they carry no large plasma current. That advantage is worth more than it is usually credited.
