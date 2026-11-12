---
title: "Why Fission Data Cannot Qualify Fusion Materials"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/materials
  - fusion/risks
status: stable
confidence: high
related:
  - "[[helium-embrittlement]]"
  - "[[displacements-per-atom]]"
  - "[[ifmif-dones]]"
  - "[[fpns]]"
  - "[[astral-systems]]"
created: 2026-08-26
updated: 2026-08-26
---
A frequent question: fission reactors irradiate materials, so why not use that data?

**Because the spectrum is wrong, and the wrongness is exactly where the damage is.**

| | Fission | Fusion |
|---|---|---|
| Mean neutron energy | ~2 MeV | **14.1 MeV** |
| Above (n,α) threshold (~3 MeV) | Largely no | **Yes** |
| Helium production | ~0.1–1 appm He/[[displacements-per-atom\|dpa]] | **~10–15 appm He/dpa** |

The same displacement damage, with **an order of magnitude more helium** — and helium at grain boundaries is what causes [[helium-embrittlement]], swelling and weld cracking.

## The surrogates, and their limits

- **Fission reactors with helium implantation** (HFIR, BOR-60, ATR) — approximates the ratio, not the simultaneity
- **Spallation sources** (SNS, ISIS) — wrong spectrum shape
- **Ion beams** — fast screening, no bulk
- **Commercial DT neutron services** — [[astral-systems]] now sells continuous DD and DT irradiation, and has run hundreds of hours on breeder materials. A genuine market response to a public infrastructure gap

None reproduces the combination of dpa rate, He/dpa ratio and spectrum.

**[[ifmif-dones]]** and **[[fpns]]** exist to close this. Neither operates. Every pilot plant of the 2030s will be built on extrapolated data and will itself function as the materials experiment.
