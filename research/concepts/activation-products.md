---
title: "Activation Products"
type: concept
domain: physics
tags:
  - fusion/concept
  - fusion/materials
  - fusion/safety
status: stable
confidence: high
related:
  - "[[43-fusion-waste-classification-and-disposal]]"
  - "[[rafm-steel]]"
  - "[[33-safety-environment-decommissioning]]"
  - "[[22-critical-materials-supply-chains]]"
  - "[[gonzalez-de-vicente-2022-fusion-waste]]"
created: 2026-08-29
updated: 2026-08-29
---
What makes a fusion plant radioactive. Fusion produces no fission products and no actinides; the
14.1 MeV neutron flux instead transmutes the atoms of the surrounding structure, turning the machine
itself into the radioactive inventory.

This single fact shapes fusion's safety case, its waste classification and — unexpectedly — its
procurement specifications.

## Why it is a materials-selection problem

Activation is **elemental**, not structural. Which isotopes appear depends on which elements are
present, so the mitigation is to build alloys from elements whose activation products are
short-lived: replace molybdenum with tungsten, niobium with tantalum, and eliminate nickel, cobalt
and copper wherever possible. That principle is what [[rafm-steel|reduced-activation ferritic-
martensitic steels]] exist to satisfy.

Use conventional stainless steel, with its nickel, cobalt and niobium content, and long-lived
activation products appear that will not decay to a disposable level on any useful timescale.

## Impurities, not the specification

The awkward finding in [[gonzalez-de-vicente-2022-fusion-waste]] is that the troublesome isotopes
frequently come from elements nobody specified. **⁹⁴Nb** is produced from niobium present at
parts-per-million as a tramp element in commercial steel; potassium and cobalt arrive the same way.
After irradiation these "might preclude disposal in LLW repositories".

Activation therefore turns into a supply-chain requirement — dedicated melts and verified feedstock
across thousands of tonnes — as set out in [[43-fusion-waste-classification-and-disposal]] and
[[22-critical-materials-supply-chains]].

## Why it is still better than fission

Activation products are overwhelmingly **short-lived relative to actinides**, and there are no
transuranics. Radiotoxicity falls over decades rather than geological time, and the associated
[[decay-heat]] is low enough that passive cooling suffices — which is why the accident pathways in
[[33-safety-environment-decommissioning]] stay bounded in a way fission's do not.
