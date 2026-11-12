---
title: "Burn Control"
type: concept
domain: physics
tags:
  - fusion/concept
  - fusion/physics
  - fusion/engineering
status: stable
confidence: high
related:
  - "[[burning-plasma]]"
  - "[[helium-ash]]"
  - "[[detachment]]"
  - "[[iter]]"
  - "[[31-plasma-physics-deeper-cuts]]"
  - "[[fusionmae-crossref-metadata-2026]]"
  - "[[hl3-data-driven-rl-control-2025]]"
created: 2026-08-26
updated: 2026-08-26
---
The unsolved control problem at the heart of a fusion power plant.

A [[burning-plasma]] is a **positive-feedback thermal system**:

```
fusion power → alpha heating → temperature ↑ → reactivity ↑ → fusion power ↑
```

Over 10–20 keV, `⟨σv⟩` rises steeply with temperature, so loop gain exceeds one. Unmanaged, the plasma either **runs away thermally** until a pressure limit ends the discharge violently, or **quenches**.

## Why it is hard

Available actuators — fuelling, auxiliary heating, impurity seeding — act on **timescales of seconds**. The plasma's thermal response is faster. Simultaneously:

- [[helium-ash]] accumulation dilutes fuel (a slow stabilising negative feedback, but a performance penalty)
- Core impurity accumulation can quench the burn abruptly
- Sawteeth periodically redistribute the core, including the alphas
- A detached divertor must be maintained at the same time, using seeding that also cools the core

**Never demonstrated.** ITER's Q = 10 scenario and [[sparc]]'s Q > 1 attempt are the first tests. Burn-control instability is a plausible failure mode that would present, from outside, simply as a machine not reaching its target.
