---
title: "UKAEA Vanadium Strategy (LIBRTI conference presentation)"
type: source
source_type: notes
file: "raw/papers/UKAEA-2026-vanadium-strategy-LIBRTI.pdf"
authors: "Davidson Sabu, Asma Ramzi, Paul Goodwin, Allan Harte — Manufacturing Technology and Equipment Qualification, Fusion Technology Division, UKAEA, Rotherham"
publisher: "UKAEA; conference poster hosted on indico.ukaea.uk, PDF created 28 January 2026"
source_date: 2026-01-28
ingested: 2026-11-02
tags:
  - fusion/source
  - fusion/materials
  - fusion/supply-chain
status: stable
confidence: medium
related:
  - "[[ukaea]]"
  - "[[librti]]"
  - "[[vanadium-alloys]]"
  - "[[rafm-steel]]"
  - "[[lithium-6]]"
  - "[[st-e1]]"
  - "[[step]]"
  - "[[arc]]"
  - "[[tokamak-energy]]"
  - "[[ornl]]"
  - "[[kyoto-fusioneering]]"
  - "[[spherical-tokamak]]"
  - "[[tritium-breeding-ratio]]"
  - "[[22-critical-materials-supply-chains]]"
  - "[[38-component-manufacturing]]"
created: 2026-11-02
updated: 2026-11-02
---
The first source in this vault to address the **vanadium alloy supply chain** — a dependency
[[22-critical-materials-supply-chains]] had never analysed, despite [[st-e1|ST-E1]] selecting
vanadium over [[rafm-steel|RAFM steel]].

> [!warning] A strategy poster, not a peer-reviewed study
> This is a **conference presentation** by UKAEA's manufacturing group, stating an
> organisation's intent and summarising others' published work. `source_type: notes`. Its
> claims about alloy behaviour are second-hand summaries of the five papers it cites; its
> claims about strategy are UKAEA's own. Nothing here is a measurement made for this document.

## The claim that evidences something this vault held as asserted

> The high thermal conductivity and favourable nuclear properties of V-4Cr-4Ti alloys *"also
> reduce the need for neutron multipliers or lithium-6 enrichment in liquid lithium breeder
> blanket systems."*

That is a **third party** — a national laboratory with no stake in ST-E1 — stating the
architectural logic that [[st-e1|ST-E1]]'s unenriched-lithium choice depends on. The vault
previously recorded that logic as asserted and unevidenced. It is now evidenced in outline,
though still not quantified: no TBR figure accompanies the statement. See [[lithium-6]].

## Manufacturing scale, which is the real constraint

| Heat | Scale | Route |
|---|---|---|
| Industrial heat (Johnson & Smith) | **1200 kg** | Aluminothermic-reduction V + high-purity Cr/Ti, EBM purification, double vacuum-arc melting |
| NIFS-HEAT-1 (Muroga *et al.*) | **30 kg** (200 kg planned) | EBM of V, Cr, Ti; vacuum arc remelting |
| SWIP-30 (Fu *et al.*) | **30 kg** | Double electron-beam melting in high vacuum |

**The largest heat ever made is 1200 kg.** Set against any power-plant-scale requirement, this
is the gap the poster exists to address: UKAEA names *"Investing in Domestic UK Vanadium
material & manufacturing supply chain"* as a long-term bet, and a *"White Paper on
Industrialisation of V-4Cr-4Ti"* as an intended output. The supply chain is presented as
something to be built, not something that exists.

## Liquid lithium: a second-order problem named plainly

- A **standard composition with impurity limits** does not yet exist and needs specifying.
- *"Purity of commercial Li today is lower than that in 80s/90s"* — commercial lithium has
  become **worse**, not better, for this application.
- Lithium strips oxygen from vanadium, preventing embrittlement; but carbon and nitrogen in the
  lithium diffuse **into** the alloy.
- MHD pressure drop requires insulator coatings, which are also wanted as tritium permeation
  barriers and for corrosion resistance.

## Open work, in UKAEA's own words

Radiation-accelerated corrosion and cracking, transmutation-produced helium effects on similar
and dissimilar joints, and high-temperature oxygen effects at higher dose all *"need to be
studied"*. Qualification is being attempted by a **novel digital route** — Bayesian
optimisation over literature and tensile data to 900 °C, producing a surrogate model, with
EPRI engaged for regulatory acceptance — funded by a £250k DSIT tactical fund, with
[[ornl|ORNL]], [[tokamak-energy|Tokamak Energy]], the University of Birmingham, ATI and digiLab
named as partners. The target asset is explicitly a **[[spherical-tokamak|spherical tokamak]]**
with a liquid-metal breeder blanket.

## What it does **not** establish

- **No tonnage requirement, and no production-capacity figure.** Neither global vanadium output
  nor fusion demand appears anywhere in this document.
- **No TBR number** for the enrichment claim above.
- **Its reference [1] is not held**: Muroga, Zheng & Yang, *Current Opinion in Solid State and
  Materials Science* 36 (2025) 101224 — see [[vanadium-alloys]] for that access failure.
