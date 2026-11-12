---
title: "REBCO High-Temperature Superconductor"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/magnets
  - fusion/supply-chain
status: stable
confidence: high
related:
  - "[[b4-scaling]]"
  - "[[quench]]"
  - "[[sparc]]"
  - "[[commonwealth-fusion-systems]]"
  - "[[18-superconductors-and-magnets]]"
  - "[[canis]]"
created: 2026-08-26
updated: 2026-09-02
---
**Rare-Earth Barium Copper Oxide** — the conductor that made the current fusion boom possible.

Not a wire but a **tape**: a ~1 μm superconducting layer on a buffered metal substrate, capped with silver and copper, typically 4 or 12 mm wide and ~0.1 mm thick.

Its decisive property is not the high transition temperature (~90 K) — fusion magnets run cold anyway. It is that **REBCO retains enormous current density in enormous magnetic fields**, well past where Nb₃Sn quenches at 12–13 T. Via [[b4-scaling]], that difference is everything.

## Manufacturing

The superconducting layer must be **biaxially textured** — grains aligned in all three axes, because REBCO carries almost no current across a misaligned grain boundary. Templates by **IBAD** or **RABiTS**; deposition by **PLD** or **MOCVD**.

## The three unretired risks

1. **Supply** — global capacity **~10,000 km/year**, with substantial Chinese manufacturing strength. A single high-field tokamak consumes thousands of kilometres
2. **Radiation lifetime** — **not established.** DOE's near-term milestone is literally *"conduct REBCO irradiation campaigns to define magnet performance and standards."* An industry is being built around a conductor whose in-service degradation is unknown
3. **[[quench]] protection** — normal-zone propagation is centimetres per second, so a hot spot can reach destructive temperature while remaining nearly invisible electrically

[[canis]] adds a different demonstrated point: nine soldered-metal-insulation REBCO shaping coils, made from tape supplied by three manufacturers, were integrated and operated at 20 K. The result supports repeatable planar-coil manufacture and static field control; planned quench and manufacturing-defect campaigns were not reported as completed. See [[prototyping-test-canis-hts-planar-coil-array]].

Operating at 20 K rather than 4.5 K also cuts the Carnot penalty by roughly 4–5×, which matters more than it is usually credited given the 2026 helium shortage.


## Evidence in `raw/`

Primary sources held in this vault that evidence the claims above:

- [[sparc-toroidal-field-model-coil-program]]
- [[prototyping-test-canis-hts-planar-coil-array]]
