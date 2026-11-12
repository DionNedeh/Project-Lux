---
title: "Beryllium"
type: concept
domain: engineering
symbol: "Be"
tags:
  - fusion/concept
  - fusion/materials
  - fusion/supply-chain
  - fusion/safety
status: stable
confidence: high
related:
  - "[[22-critical-materials-supply-chains]]"
  - "[[tritium-breeding-ratio]]"
  - "[[43-fusion-waste-classification-and-disposal]]"
  - "[[boronization]]"
  - "[[iter]]"
created: 2026-08-29
updated: 2026-08-29
---
The neutron multiplier the field is quietly walking away from. Beryllium was [[iter]]'s original
first-wall material and remains a candidate multiplier in solid breeding blankets, but its toxicity,
its activation behaviour and its supply constraints have pushed several designs toward lead instead.

## Why it was chosen

Beryllium multiplies neutrons via `(n,2n)`, raising the [[tritium-breeding-ratio]] above what
lithium alone can achieve. It is also low-Z, so the [[tungsten-pfc|plasma-facing]] penalty for
sputtered beryllium entering the plasma is far smaller than for a high-Z metal — a core beryllium
influx costs little radiated power, where tungsten above roughly 10⁻⁵ concentration will
[[quench]] the discharge.

It had a second, unplanned virtue: **beryllium getters oxygen**. That kept [[iter]]'s impurity levels
down without a dedicated system.

## Why it is being abandoned

- **Chronic beryllium disease.** Beryllium dust causes an irreversible granulomatous lung condition
  at very low exposures. Handling demands stringent containment and medical surveillance, which
  raises cost across manufacturing, installation and — critically —
  [[29-remote-handling-and-maintenance|remote maintenance]] and decommissioning, where activated
  beryllium dust is simultaneously a radiological and a chemical hazard.
- **It activates to long-lived isotopes.** This complicates the claim that fusion waste decays in
  50–100 years, and it is one of the impurity-driven problems described in
  [[43-fusion-waste-classification-and-disposal]]. A single plant may hold **300–400 t**.
- **Supply.** Beryllium is among the constrained materials examined in
  [[22-critical-materials-supply-chains]].

Several designs therefore prefer lead as the multiplier — see [[lithium-lead-eutectic]], which is
abundant, cheap and comparatively non-toxic.

## The consequence ITER did not plan for

ITER's 2023 change of first-wall armour from beryllium to tungsten **removed its built-in oxygen
control**. Impurities rose, and a wall-conditioning requirement appeared that the original design
never had — which is why ITER now needs the [[boronization]] system described there. Removing a
material removed a function nobody had listed as a requirement.
