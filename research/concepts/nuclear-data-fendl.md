---
title: "Nuclear Data and FENDL"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/data
  - fusion/risks
status: stable
confidence: high
related:
  - "[[tritium-breeding-ratio]]"
  - "[[iaea]]"
  - "[[19-simulation-codes-nuclear-data]]"
created: 2026-08-26
updated: 2026-11-02
---
The quiet weak link under every neutronics calculation in fusion.

**FENDL** — the Fusion Evaluated Nuclear Data Library, coordinated by the **[[iaea]]** Nuclear Data Section — is the community standard for cross-section data feeding tritium breeding, shielding, activation, nuclear heating and damage calculations.

## The state of it

- In **FENDL-3.1d**, neutron cross sections for **65 of 180 isotopes** are inherited from **ENDF/B-VII.1** — a general-purpose fission-oriented library
- Neutron fluxes computed with different libraries differ by as much as **+12% / −8%**
- **Five isotopes were found to have negative average heating numbers** — a physically impossible value, i.e. an outright data defect
- **Uncertainty propagation to gamma heating and shutdown dose rate has never been published** by any study

## Why it matters more than it sounds

**The [[tritium-breeding-ratio]] design target is 1.1 and the failure threshold is 1.0 — a 10% margin.** Nuclear data uncertainty on TBR is a few percent, and inter-library flux discrepancies run to 12%.

**The uncertainty in the calculation is a meaningful fraction of the entire design margin on the parameter that determines whether a fusion plant can operate at all.**

The corollary: a blanket design validated only computationally has not been validated. That is precisely why [[unity-3]] and [[librti]] matter more than their budgets suggest.

Transport codes: **MCNP** (export-controlled), **OpenMC** (open source, increasingly standard — and which had to fall back to ENDF/B-VIII.0 because of defects in converted FENDL-3.1d photon data).

## A second design that does not use FENDL

[[st-e1|ST-E1]]'s neutronics runs its in-house Geant4 application **G4Tokamak** on
**ENDF/B-VIII.0** with ParticleHP for transport, and **TENDL-2019** under FISPACT-II for
activation — **not FENDL** ([[st-e1-neutronics-crossref-metadata-2026]], full text read
2026-11-02, answering a question this page previously left open).

That makes two of the vault's recent neutronics lineages routing around FENDL-3.1d. It also gives
the first cross-code metric held here: against MCNP on a 20° sector, G4Tokamak's mean flux ratio
is **0.90** — a ~10% underestimate — while returning a **2% higher** TBR. No tolerance or
statistical test is stated, so this is a reported comparison, not a validation.
See [[19-simulation-codes-nuclear-data]].
