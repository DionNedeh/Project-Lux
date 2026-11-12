---
title: "Quasi-symmetry and Quasi-isodynamicity"
type: concept
domain: physics
tags:
  - fusion/concept
  - fusion/physics
status: stable
confidence: high
related:
  - "[[stellarator]]"
  - "[[wendelstein-7-x]]"
  - "[[proxima-fusion]]"
  - "[[type-one-energy]]"
  - "[[04-magnetic-confinement-devices]]"
created: 2026-08-26
updated: 2026-08-29
---
The optimisation principles that resurrected the [[stellarator]].

**The problem.** A 3D magnetic field has no continuous symmetry, so particle orbits do not close and collisionless (neoclassical) transport is catastrophic. This is what killed the stellarator in 1969.

**Quasi-symmetry.** Engineer the field *strength* |B| to possess a hidden symmetry — quasi-axisymmetric, quasi-helical or quasi-poloidal — even though the geometry is fully three-dimensional. A particle then behaves as though it were in a symmetric device, recovering good confinement. **HSX** (Wisconsin) demonstrated quasi-helical symmetry experimentally in 2005.

**Quasi-isodynamicity.** A different route: arrange the field so collisionless particle orbits close on themselves, eliminating neoclassical transport directly. **[[wendelstein-7-x]] is optimised this way**, as is [[proxima-fusion]]'s *Stellaris*.

## Recent method advances

- **Quasi-single-stage optimisation** — folds coil buildability into the plasma-boundary optimisation rather than solving the two sequentially, giving smoother boundaries and reduced coil complexity
- **Generative models** — latent diffusion models now produce candidate ultra-compact quasi-isodynamic configurations directly

**The remaining hard problem** is fast-alpha confinement in 3D, which is a separate and harder objective than thermal transport, and a live constraint on every stellarator power plant design.


## Evidence in `raw/`

Primary sources held in this vault that evidence the claims above:

- [[quasi-single-stage-stellarator-optimization-2026]]
