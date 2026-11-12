---
title: "Safety Factor q"
type: concept
domain: physics
symbol: "q"
tags:
  - fusion/concept
  - fusion/physics
status: stable
confidence: high
related:
  - "[[tokamak]]"
  - "[[disruption]]"
  - "[[bootstrap-current]]"
  - "[[arc]]"
  - "[[hl3-data-driven-rl-control-2025]]"
created: 2026-08-26
updated: 2026-08-26
---
The number of toroidal transits a magnetic field line makes per poloidal transit:

```
q ≈ a·B_t / (R·B_p)
```

It measures the helical pitch of the field, and it governs MHD stability. **q₉₅** — the value at the flux surface enclosing 95% of the poloidal flux — is the standard design figure. Values below ~2 invite kink instabilities and [[disruption]].

Where q passes through rational values (q = 1, 3/2, 2) the plasma is vulnerable to **magnetic islands**: the q = 1 surface hosts sawteeth, and q = 2 and 3/2 host [[neoclassical-tearing-mode|neoclassical tearing modes]].

Raising core q above 1 by off-axis current drive produces the **sawtooth-free hybrid scenario**, with a broad shear-free core, high non-inductive current fraction and improved confinement — one of the more promising reactor scenarios.

[[arc]] enforces a strict edge safety factor limit as part of buying disruption margin with field.
