---
title: "Tungsten Plasma-Facing Components"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/materials
status: stable
confidence: high
sources:
  - "[[overview-of-the-helios-design]]"
related:
  - "[[divertor]]"
  - "[[helium-embrittlement]]"
  - "[[boronization]]"
  - "[[helios]]"
  - "[[rafm-steel]]"
  - "[[38-component-manufacturing]]"
  - "[[22-critical-materials-supply-chains]]"
created: 2026-08-26
updated: 2026-09-08
---
The consensus plasma-facing material: highest melting point of any metal (3,422 °C), lowest sputtering yield of any practical candidate, low tritium retention.

## Its own limits

- **Recrystallises above ~1300 °C**, losing strength permanently
- **DBTT around 400 °C**, pushed higher by irradiation — brittle when cold, weak when hot, with a narrow usable band
- **High-Z radiator** — core tungsten concentration must stay below roughly **10⁻⁵** or the plasma quenches
- **Transmutes to rhenium and osmium** under neutron flux, changing properties over life
- Helium implantation produces a nanostructured surface "fuzz" that degrades performance

## The supply exposure

**Over 80% of global tungsten supply is controlled by non-Western entities**, China dominant in both mining and processing. Fusion enters this market needing not commodity tungsten but precision-manufactured, actively cooled monoblocks in quantities nobody has produced. See [[38-component-manufacturing]].

## The alternative

**Liquid metal PFCs** — flowing lithium or tin. A liquid cannot be neutron-damaged, cannot recrystallise, and self-heals after erosion. If they work, both the tungsten supply problem and the tungsten materials problem disappear at once.

## Designing around the DBTT

[[helios|Helios]] shows how the narrow usable band above gets engineered around
([[overview-of-the-helios-design]]). Its [[divertor]] targets are **51,000 tessellated hexagonal
tungsten tiles, 2.5 cm across**, cooled by closed-loop helium impingement jets and mounted on a
vanadium-alloy support structure, under an assumed **10 MW/m²**. The coolant reaches them **already
pre-heated by the blanket to above tungsten's ductile-to-brittle transition temperature** — the cold
end of the band is removed by routing the coolant, not by choosing a different metal.

It also illustrates the manufacturing exposure concretely: 51,000 precision tiles per plant is the
kind of quantity the supply concern above is about. This is a preconceptual design; no such target
has been built.
