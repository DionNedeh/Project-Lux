---
title: "Reduced-Activation Steels"
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
  - "[[willis-2026-st-e1-pre-concept-design-overview]]"
  - "[[st-e1-neutronics-crossref-metadata-2026]]"
related:
  - "[[helium-embrittlement]]"
  - "[[st-e1]]"
  - "[[displacements-per-atom]]"
  - "[[helios]]"
  - "[[balance-of-plant]]"
  - "[[38-component-manufacturing]]"
  - "[[33-safety-environment-decommissioning]]"
  - "[[09-engineering-challenges]]"
created: 2026-08-26
updated: 2026-11-02
---
**Reduced-Activation Ferritic-Martensitic** steels — EUROFER-97 (EU), F82H (Japan), CLAM (China). The baseline structural material for a fusion power plant.

## The design principle

Build alloys from elements whose [[activation-products|activation products]] are **short-lived**: tungsten for molybdenum, tantalum for niobium, and eliminate nickel, cobalt and copper where possible.

Done well, the structure decays to hands-on or recyclable levels in **50–100 years** rather than fission's geological timescales. **Reduced-activation design is a waste-management requirement, not an optimisation.**

## The operating window, and why it is narrow

**~350–550 °C**, both ends set by irradiation: below ~350 °C, hardening and embrittlement dominate; above ~550 °C, thermal creep and [[helium-embrittlement]] take over. Every degree is worth money, because cycle efficiency scales with coolant outlet temperature.

## Alternatives, all less mature

**ODS steels** (to ~650 °C, nano-oxide dispersions that trap helium), **[[vanadium-alloys|vanadium]]** (~400–700 °C, oxygen-sensitive), **SiC/SiC** (>1000 °C, immature).

> [!note] The industrial gap
> DOE's near-term milestone is to *establish domestic industrial heat capability for multi-tonne Fe-alloy and 500 kg V-alloy heats*. **The US cannot yet melt fusion-grade structural steel at scale.**

### Two designs that decline RAFM, and what it costs them

**[[helios|Helios]]** keeps EUROFER-97 for the blanket but takes **V-4Cr-4Ti ("V44") for the first
wall**, citing higher operating temperature, no ferromagnetism and damage tolerance for a **15
full-power-year** first-wall life against *"less than half that"* for RAFM
([[overview-of-the-helios-design]]). **[[st-e1|ST-E1]]** takes
[[vanadium-alloys|V-4Cr-4Ti]] for the **centre-column shield box** and as baseline for the
centre-column helium manifold — but **does not abandon RAFM**: its neutronics specifies **F82H**
for the lower overhead horizontal shield at 350–550 °C, and 316L(N)-IG for the vacuum vessel
([[st-e1-neutronics-crossref-metadata-2026]], read in full 2026-11-02). The earlier record here —
vanadium "outright" — was the overview read alone.

Both pay for it. V44 has a high affinity for hydrogenic species, swells under irradiation, and has an
**immature supply chain**: the largest heat ever produced is **1200 kg**
([[ukaea-2026-vanadium-strategy]]), against the DOE 500 kg milestone above. Nor does vanadium escape
activation: ST-E1's own neutronics reports *non*-reduced-activation steels and PFCs as its
**highest-activating** components. **Design-study selections, not qualified material.**


**Waste classification.** RAFM steels are the dominant fusion waste stream by mass, and their
disposal class is set less by designed composition than by **uncontrolled impurities** — niobium,
cobalt, potassium — arriving with commercial feedstock. An ORNL formulation meeting LLW requirements
shows composition control is an effective lever
([[gonzalez-de-vicente-2022-fusion-waste]], [[43-fusion-waste-classification-and-disposal]]).
