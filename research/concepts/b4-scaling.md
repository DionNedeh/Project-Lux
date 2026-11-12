---
title: "The B⁴ Scaling"
type: concept
domain: physics
tags:
  - fusion/concept
  - fusion/physics
  - fusion/magnets
status: stable
confidence: high
related:
  - "[[plasma-beta]]"
  - "[[rebco]]"
  - "[[sparc]]"
  - "[[18-superconductors-and-magnets]]"
created: 2026-08-26
updated: 2026-08-26
---
The single most consequential design insight in modern fusion.

Fusion power density is `P/V = ¼n²⟨σv⟩E_fus`. Since `p = 2nT` and `⟨σv⟩/T² ≈ constant` over 8–25 keV, this becomes `P/V ∝ p²`. And since `p = βB²/2μ₀`:

```
P_fus / V  ∝  β² B⁴
```

**Fusion power density scales as the fourth power of magnetic field.** Doubling B at fixed [[plasma-beta|beta]] gives 16× the power density — or the same power from a far smaller machine.

## Why it reorganised the field

Conventional low-temperature superconductors (Nb₃Sn, as in [[iter]]) saturate around **12–13 T**. [[rebco]] high-temperature superconducting tape operates **above 20 T**.

That materials substitution is why [[sparc]] attempts what ITER attempts in roughly **1/40th the plasma volume**, and why the entire private tokamak sector reorganised around HTS after about 2018.

**The counterweight:** the same power in a smaller volume means higher neutron wall loading and a narrower [[divertor]] strike point. Compact designs are most likely to break at the divertor, not at confinement.
