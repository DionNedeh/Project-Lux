---
title: "Vanadium Alloys"
type: concept
domain: engineering
symbol: "V-4Cr-4Ti"
tags:
  - fusion/concept
  - fusion/materials
  - fusion/supply-chain
status: draft
confidence: medium
sources:
  - "[[ukaea-2026-vanadium-strategy]]"
  - "[[st-e1-neutronics-crossref-metadata-2026]]"
  - "[[willis-2026-st-e1-pre-concept-design-overview]]"
related:
  - "[[rafm-steel]]"
  - "[[lithium-6]]"
  - "[[st-e1]]"
  - "[[tokamak-energy]]"
  - "[[ukaea]]"
  - "[[spherical-tokamak]]"
  - "[[tritium-breeding-ratio]]"
  - "[[activation-products]]"
  - "[[displacements-per-atom]]"
  - "[[22-critical-materials-supply-chains]]"
  - "[[38-component-manufacturing]]"
  - "[[43-fusion-waste-classification-and-disposal]]"
created: 2026-11-02
updated: 2026-11-02
---
**V-4Cr-4Ti** — "V44" — is the reference fusion structural alloy for liquid-metal breeder
blankets, and the main alternative to [[rafm-steel|RAFM steel]]. Per
[[ukaea-2026-vanadium-strategy|UKAEA's vanadium strategy]] it offers high-temperature creep
resistance, high thermal strength, strong resistance to irradiation swelling, and low
activation.

## Why a blanket designer wants it

High thermal conductivity and favourable nuclear properties *"reduce the need for neutron
multipliers or [[lithium-6|lithium-6]] enrichment in liquid lithium breeder blanket systems"*
([[ukaea-2026-vanadium-strategy|UKAEA]]). That is the architectural argument behind
[[st-e1|ST-E1]]'s choice of pure, unenriched lithium — and it routes around the Li-6
enrichment chokepoint recorded in [[22-critical-materials-supply-chains]].

[[st-e1-neutronics-crossref-metadata-2026|ST-E1's neutronics paper]] selects V-4Cr-4Ti as the
structural material for the centre-column shield box, and as the baseline for the centre-column
helium manifold with 316L(N)-IG as an alternative.

## The constraint is production, not physics

> [!warning] The largest heat ever made is 1200 kg
> Documented V-4Cr-4Ti production runs to a **1200 kg** industrial heat, with NIFS-HEAT-1 at
> **30 kg** (200 kg planned) and SWIP-30 at **30 kg**
> ([[ukaea-2026-vanadium-strategy|UKAEA]], citing Johnson & Smith, Muroga *et al.* and Fu
> *et al.*). There is no standing commercial production line, and UKAEA names building a
> domestic supply chain and industrialising the alloy as *long-term bets*.

Chemistry bounds it too: impurity control is the limiting factor, and commercial lithium purity
is reported as **lower today than in the 1980s–90s**.

> [!note] Escaping one chokepoint is not escaping activation
> [[st-e1-neutronics-crossref-metadata-2026|ST-E1's own neutronics team]] reports that
> non-reduced-activation ferritic martensitic steels and plasma-facing components show the
> highest activation in the machine. A vanadium centre column does not make the plant
> low-activation overall. See [[43-fusion-waste-classification-and-disposal]].

## Demand figures, and whose they are

The trade association **Vanitec** (post of 3 June 2026, author Dr Yu Li) puts a commercial
fusion reactor at **500–1,500 t** of V-4Cr-4Ti — roughly 460–1,380 t contained vanadium —
against global production of *"approximately 120,000 tonnes per year"*, and scales that to
46,000–138,000 t for a 100-reactor fleet. **These are Vanitec's illustrative scenarios.** The
review they accompany — Muroga, Zheng & Yang, *Current Opinion in Solid State and Materials
Science* **36** (2025) 101224 — **is not held**: ScienceDirect returned HTTP 403 on
2 November 2026, and no OSTI deposit was found despite an ORNL co-author. Whether the tonnages
are the review's or Vanitec's arithmetic **could not be determined**.
