---
title: "Beta"
type: concept
domain: physics
symbol: "β"
units: "dimensionless"
tags:
  - fusion/concept
  - fusion/physics
status: stable
confidence: high
related:
  - "[[tokamak]]"
  - "[[field-reversed-configuration]]"
  - "[[b4-scaling]]"
  - "[[01-fusion-physics-fundamentals]]"
  - "[[hl3-data-driven-rl-control-2025]]"
created: 2026-08-26
updated: 2026-08-26
---
The ratio of plasma pressure to magnetic pressure — the efficiency with which a magnetic field is being used to confine plasma.

```
β = 2μ₀p / B²
```

| Configuration | Typical β |
|---|---|
| Conventional [[tokamak]] | 1–5% |
| Spherical tokamak | 20–40% |
| [[stellarator]] | 4–5% |
| [[field-reversed-configuration]] | **≈ 1** |

Beta is limited by MHD stability. The empirical **Troyon limit** expresses this via normalised beta `β_N = β·a·B/I_p`, conventionally ≲ 3–4.

Because fusion power density goes as **β²B⁴** (see [[b4-scaling]]), beta and field are substitutable. High-beta configurations buy performance without high field — which is the entire argument for spherical tokamaks and FRCs, and why FRCs are the only geometry where [[aneutronic-fusion]] looks even remotely plausible.

[[arc]] deliberately operates **below the no-wall beta limit**, buying disruption margin with field instead of performance with beta.
