---
title: "Spherical Tokamak"
type: concept
domain: physics
symbol: "A = R₀ / a"
tags:
  - fusion/concept
  - fusion/machines
  - fusion/designs
status: draft
confidence: medium
sources:
  - "[[st-e1-neutronics-crossref-metadata-2026]]"
  - "[[willis-2026-st-e1-pre-concept-design-overview]]"
  - "[[ukaea-2026-vanadium-strategy]]"
related:
  - "[[tokamak]]"
  - "[[plasma-beta]]"
  - "[[st40]]"
  - "[[st-e1]]"
  - "[[step]]"
  - "[[mast-upgrade]]"
  - "[[globus-m2]]"
  - "[[tokamak-energy]]"
  - "[[ukaea]]"
  - "[[tritium-breeding-ratio]]"
  - "[[vanadium-alloys]]"
  - "[[rebco]]"
  - "[[04-magnetic-confinement-devices]]"
  - "[[30-power-plant-designs-compared]]"
created: 2026-11-02
updated: 2026-11-02
---
A [[tokamak]] squashed toward a cored apple: the major radius is pulled in until the aspect
ratio `A = R₀/a` approaches unity. The physics case is [[plasma-beta|beta]] — a low-aspect-ratio
plasma holds more pressure for a given field, and fusion power density scales as β²B⁴.

The vault's spherical machines are [[st40|ST40]], [[mast-upgrade|MAST-U]],
[[globus-m2|Globus-M2]], and the two power-plant designs [[step|STEP]] and [[st-e1|ST-E1]].

## What the geometry costs

Everything that has to fit around the plasma now has to fit through the **centre column**, and
that single constraint propagates through the whole design.
[[st-e1-neutronics-crossref-metadata-2026|ST-E1's neutronics paper]] is the clearest evidence
this vault holds for how hard it bites:

- **Inboard breeding is ruled out entirely** for lack of space, so all
  [[tritium-breeding-ratio|breeding]] is outboard — and the outboard vertical shield has to
  reflect neutrons back into the blanket to recover TBR.
- The centre column carries the machine's worst radiation damage: up to **≈ 50 dpa per full-power
  year** in the tungsten carbide shielding block at a thin part of the midplane.
- Shielding the [[rebco|HTS]] magnets *"is a major driver dictating tokamak size, plant
  lifetime, and balance of plant"* — a notable ordering, in which the magnets, not the plasma,
  size the machine.

> [!warning] The shielding problem is not solved in the design this vault holds best
> ST-E1's baseline exceeds its own HTS fast-flux limit by a factor of about 2.4, giving an
> estimated **13 full-power years** against a 30 fpy design intent. A larger 2400 MW variant at
> aspect ratio **2.31** recovers roughly 25 fpy. See [[st-e1]].

## Why it attracts private capital anyway

A compact machine is cheaper to build and faster to iterate, which is why
[[tokamak-energy|Tokamak Energy]] and the UK's [[step|STEP]] programme both took this route,
and why [[ukaea-2026-vanadium-strategy|UKAEA's materials strategy]] names the spherical tokamak
with a liquid-metal breeder blanket as its target asset. The trade is explicit: accept the
hardest possible inboard engineering problem in exchange for size.

Compare [[04-magnetic-confinement-devices]] for the conventional-aspect-ratio alternative, and
[[30-power-plant-designs-compared]] for how the designs line up.
