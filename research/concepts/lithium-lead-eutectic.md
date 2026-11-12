---
title: "Lithium-Lead Eutectic (PbLi)"
type: concept
domain: engineering
symbol: "Pb-16Li"
aliases:
  - "PbLi"
  - "Lithium-lead"
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/materials
status: stable
confidence: high
sources:
  - "[[overview-of-the-helios-design]]"
related:
  - "[[tritium-breeding-ratio]]"
  - "[[lithium-6]]"
  - "[[eu-demo]]"
  - "[[helios]]"
  - "[[balance-of-plant]]"
  - "[[30-power-plant-designs-compared]]"
  - "[[43-fusion-waste-classification-and-disposal]]"
created: 2026-08-29
updated: 2026-09-12
---
The liquid breeder that does two jobs at once: a molten lead–lithium eutectic carrying [[lithium-6]]
for tritium breeding while the lead acts as the neutron multiplier. It is the reason a large family
of blanket designs exists.

## Why it dominates blanket design

Lead is **abundant, cheap and comparatively non-toxic** — the direct contrast with
[[beryllium]], the alternative multiplier. Putting the multiplier and the breeder in the same
flowing liquid removes a whole class of solid-component problems: no pebble beds to crack, no
swelling, and a breeder that can be processed outside the vessel.

Three of the main blanket concepts in [[30-power-plant-designs-compared]] are PbLi variants:

- **WCLL** — water-cooled lithium-lead, an [[eu-demo]] baseline candidate
- **HCLL** — helium-cooled lithium-lead
- **DCLL** — dual-coolant lithium-lead

The competing family is helium-cooled pebble bed (**HCPB**), which uses solid ceramic breeder with a
[[beryllium]] multiplier.

## What it costs

**Polonium-210.** Neutron capture on the bismuth impurity in lead breeds ²¹⁰Po, an intensely
radiotoxic alpha emitter, into the circulating loop. The IAEA review underpinning
[[43-fusion-waste-classification-and-disposal]] tracks ²⁰⁹Bi and ²¹⁰Po inventories in the
**600 m³** of flowing PbLi in an ARIES-class plant, alongside ²⁰³Hg. This is a coolant that becomes
a mobile radiological hazard in its own right, quite separate from the activated structure around it.

**MHD pressure drop.** Driving an electrically conducting liquid metal across a strong magnetic
field induces currents that oppose the flow. The pumping penalty feeds directly into
[[recirculating-power]], and it is the principal engineering objection to liquid-metal blankets.

**Tritium extraction.** Tritium must be recovered from the liquid at low concentration and high
throughput — part of the fuel-cycle problem in [[28-vacuum-wall-conditioning-tritium-plant]].

## A specified instance

[[helios|Helios]] gives the vault its first fully parameterised PbLi blanket from a company design
([[overview-of-the-helios-design]], a preconceptual design — nothing built). It is a **uniform 50 cm
layer** completely surrounding plasma and first wall, **65% enriched in [[lithium-6]]**, with
EUROFER-97 structure and helium cooling, and the liquid flowing at **6.6 cm/s** before passing
through a heat exchanger and the tritium extraction system. **Silicon carbide inserts** form the
non-conductive break between flowing metal and structure — the named mitigation for the MHD
pressure drop above. Idealised [[tritium-breeding-ratio|TBR]] is 1.3.

> [!note] Which eutectic
> This page uses **Pb-16Li**; the Helios paper writes **Pb-17Li**. The composition is quoted variously
> as Pb-15.7Li through Pb-17Li — nomenclature, not disagreement.
