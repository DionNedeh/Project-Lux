---
title: "Simulation, Codes and Nuclear Data"
type: synthesis
doc: 19
part: 2
aliases:
  - "Simulation, Codes and Nuclear Data"
tags:
  - fusion/synthesis
  - fusion/computation
created: 2026-08-25
updated: 2026-11-02
status: stable
confidence: high
related:
  - "[[09-engineering-challenges]]"
  - "[[17-diagnostics-control-disruption]]"
  - "[[20-fusion-beyond-electricity]]"
  - "[[26-appendix-quantitative-data]]"
  - "[[fusionmae-crossref-metadata-2026]]"
  - "[[tokamak-agnostic-elm-crossref-metadata-2026]]"
  - "[[tcv-predict-first-rampdown-2025]]"
  - "[[hl3-data-driven-rl-control-2025]]"

---
# 19 — Simulation, Codes and Nuclear Data

*Project Lux · The computational infrastructure fusion runs on, and the data gaps underneath it*

---

## 1. Why fusion is a computational science

Fusion has an unusual relationship with simulation. In most engineering fields, you build prototypes and iterate. In fusion, a prototype costs a billion dollars and takes a decade, so **the design must be substantially correct before construction begins** — and that means it must be simulated.

Three specific pressures make this acute:

1. **Extrapolation.** No machine has ever operated in the burning-plasma regime. Every reactor design extrapolates from devices that are smaller, colder, and running the wrong fuel.
2. **Coupled multiphysics.** Plasma turbulence, MHD stability, neutron transport, thermal-hydraulics, structural mechanics and tritium chemistry are all coupled, on timescales spanning microseconds to years.
3. **Irreducible cost of the underlying physics.** A first-principles turbulence simulation of a single confinement time in a reactor-scale plasma is an exascale problem.

The DOE roadmap treats this as infrastructure on a par with hardware: the **AI-Fusion Digital Convergence Platform** is one of only two Build-pillar key actions, and **HPC, advanced manufacturing and AI** is one of the eight Infrastructure Streams.

---

## 2. The plasma physics code ecosystem

### Gyrokinetics — turbulent transport

The dominant loss channel in a magnetically confined plasma is **microturbulence** driven by the gradients confinement creates. Simulating it from first principles requires solving a 5-dimensional kinetic equation (three space, two velocity) after averaging out the fast gyration — the **gyrokinetic** approximation.

| Code | Type | Notes |
|---|---|---|
| **GENE** | Eulerian (continuum) | Open source, used worldwide, developed at IPP Garching. The European workhorse |
| **CGYRO** | Eulerian | General Atomics. Used for the **[[sparc|SPARC]] first-campaign performance predictions** (arXiv:2403.15633) |
| **GYRO / TGLF** | Eulerian / reduced model | TGLF is a fast quasilinear surrogate used inside design loops |
| **XGC** | Particle-in-cell, gyrokinetic | Optimised for the **edge** — the open-field-line region conventional codes cannot handle |
| **GTC / GEM / ORB5** | Particle-in-cell | Global core turbulence |
| **STELLA / GENE-3D** | — | [[stellarator|Stellarator]] geometry |

**The core-edge coupling problem.** Core codes assume closed flux surfaces; edge codes must handle open field lines, neutrals and wall interaction. Real plasmas do not respect the boundary. The **WDMApp** project built **EFFIS 2.0**, an integration framework coupling **XGC** (edge) to **GENE** or **GEM** (core) in a single running simulation — one of the significant computational achievements of the last decade, and a prerequisite for predicting whether a detached [[divertor]] is compatible with a high-performance core.

### MHD — large-scale stability

- **M3D-C1, NIMROD, JOREK** — nonlinear extended MHD; used for disruptions, ELMs, vertical displacement events, and [[shattered-pellet-injection|shattered pellet injection]] modelling
- **DREAM** — the runaway electron fluid/kinetic framework behind the [[iter|ITER]] [[disruption]] results in [[17-diagnostics-control-disruption|Document 17]]
- **MARS, MISHKA, ELITE** — linear stability and [[pedestal]] analysis

### Equilibrium and design

- **EFIT** — real-time equilibrium reconstruction from magnetic measurements. Runs on essentially every [[tokamak]] in the world
- **VMEC, DESC, SPEC** — 3D equilibrium for stellarators
- **SIMSOPT, STELLOPT** — stellarator optimisation frameworks
- **FreeGS, CHEASE, TRANSP** — free-boundary equilibrium and integrated transport analysis

### Edge and divertor

- **SOLPS-ITER** — the standard for divertor design; couples plasma fluid transport to kinetic neutrals. Notoriously expensive to run, which is why **latent-space surrogate models for [[detachment]] control** (arXiv:2502.19654) matter: they put a fast learned approximation inside a real-time control loop.

---

## 3. Integrated modelling and IMAS

Individual physics codes are not enough; a plant design needs them to talk to each other, consistently, with a shared description of the machine.

**IMAS** — the **ITER Integrated Modelling & Analysis Suite** — is the field's answer. Its core contribution is not a solver but a **standardised data model**: the *Interface Data Structures* (IDS), a common schema for describing plasma equilibria, profiles, machine geometry and diagnostic data.

This sounds bureaucratic and is, in practice, transformative. Before IMAS, coupling two codes meant writing a bespoke translator, and every pairing was a separate project. With a shared schema, codes become composable. IMAS has been progressively open-sourced and adopted well beyond ITER.

Other integrated frameworks: **OMFIT** (a widely used workflow and analysis integration environment), **FACIT/JINTRAC/ETS** in Europe, and **TRANSP** at PPPL.

DOE's Challenge Area F milestones include launching **"a centralized, standards-based data repository implementing FAIR principles"** and publishing **"a common VV/UQ framework enabling interoperable, traceable whole-plant modeling."** The **FEDER** FIRE Collaborative (Fusion Energy Data Ecosystem and Repository) is the vehicle.

---

## 4. Nuclear data — the quiet weak link

This is the part of the computational stack that almost nobody discusses, and it directly threatens the field's second-hardest problem.

### What nuclear data is

Every neutronics calculation — [[tritium-breeding-ratio|tritium breeding ratio]], shielding, activation, nuclear heating, damage rates, shutdown dose — is only as good as the **evaluated cross-section libraries** it uses. These are curated compilations of how each isotope responds to neutrons at each energy, built from measurement, nuclear theory and evaluation.

**FENDL** — the **Fusion Evaluated Nuclear Data Library**, coordinated by the **IAEA Nuclear Data Section** — is the fusion community's standard, with sub-libraries for incident neutrons, protons and deuterons, covering both transport and inventory calculations.

### The state of it

The published assessment is not reassuring:

- In **FENDL-3.1d**, neutron cross sections for **65 of 180 isotopes** are simply inherited from **ENDF/B-VII.1** — a general-purpose fission-oriented library, not a fusion evaluation
- **Neutron fluxes computed with different libraries differ by as much as +12% / −8%** against reference libraries
- **Five isotopes were found to have negative average heating numbers** — a physically impossible value, i.e. an outright data defect
- **Uncertainty propagation to gamma heating and shutdown dose rate has never been published** by any study. Most published uncertainty work has propagated only to tritium production rate and TBR

### Why this matters more than it sounds

The **tritium breeding ratio design target is 1.1, and the failure threshold is 1.0.** That is a **10% margin**.

Nuclear data uncertainty on TBR is of order a few percent, and the flux discrepancies between libraries are up to 12%. **The uncertainty in the calculation is a meaningful fraction of the entire design margin on the parameter that determines whether a fusion plant can operate at all.**

The corollary: a blanket design validated only computationally has not been validated. This is precisely why **[[unity-3|UNITY-3]]** (ORNL, 2026 — the first facility generating 14 MeV neutrons to evaluate commercial breeding blanket designs) and the UK's **£220 m [[librti|LIBRTI]]** exist, and why they matter more than their budgets suggest.

DOE's Challenge Area E milestone states it directly: **"Close neutronics data gaps for activation, shielding and tritium breeding; integrate into multiscale models."**

### The transport codes

- **MCNP** — the long-standing Monte Carlo standard, export-controlled, developed at Los Alamos
- **OpenMC** — open source, MIT-origin, increasingly the community choice. Notably, OpenMC benchmarking had to fall back to ENDF/B-VIII.0 **because of problems in the converted FENDL-3.1d photon data** — a small but telling detail
- **Serpent, Geant4, ADVANTG/FW-CADIS** for variance reduction
- Emerging **deterministic discontinuous-Galerkin** approaches for fusion neutronics
- **Paramak / OpenMC-DAGMC** — CAD-to-neutronics workflows, which matter because fusion geometry is far more complex than a fission core
- **G4Tokamak** — an in-house **[[tokamak-energy|Tokamak Energy]]** application for plant-scale neutronics, built on the **Geant4** toolkit and *"verified through benchmarking against MCNP"*, credited with faster design iteration on [[st-e1|ST-E1]] ([[st-e1-neutronics-crossref-metadata-2026]]). Added 2026-10-19

> [!note] A third lineage, and a company-built one
> G4Tokamak is worth flagging for two reasons. **Geant4 is a high-energy-physics toolkit**, not a
> reactor-physics code — so this is a third genealogy alongside MCNP's weapons-lab lineage and
> OpenMC's academic one, imported from particle physics into fusion plant design. And it is
> **built and maintained by a private company for its own design loop**, which is the pattern this
> document notes elsewhere for proprietary tooling: the benchmarking claim cannot be independently
> assessed from outside.
>
> **This vault holds only the abstract**, which asserts MCNP agreement without an agreement metric,
> and does not name the nuclear data library used — a material omission given the FENDL-3.1d photon
> data problem recorded on [[nuclear-data-fendl]]. The full text is behind a publisher CAPTCHA.

---

### Company-built codes enter the record

*Added 2026-11-02.* Until now this document's neutronics coverage was MCNP and OpenMC, both
community tools. The [[st-e1|ST-E1]] Focus Collection introduces two in-house alternatives, and
they matter as a trend as much as individually: **a design team that builds its own solver owns
its own verification burden.**

**G4Tokamak** — [[tokamak-energy|Tokamak Energy]]'s plant-scale neutronics application built on
**Geant4**, running **ENDF/B-VIII.0** with ParticleHP for transport and **FISPACT-II with
TENDL-2019** for activation ([[st-e1-neutronics-crossref-metadata-2026]]). Against MCNP on a 20°
sector its mean flux ratio is **0.90** — a ~10% underestimate — while returning a **2% higher**
[[tritium-breeding-ratio|TBR]] (1.194 against 1.169). Largest discrepancies: vacuum-vessel outer
wall, its insulation, and the solenoid former.

> [!note] "Verified through benchmarking" is a claim with a number but not a criterion
> No tolerance, acceptance threshold or statistical test accompanies the 0.90 ratio. A code that
> underestimates flux while overestimating breeding is biased in the *optimistic* direction on both
> counts — shielding looks better and breeding looks better. The paper does not discuss this.
> See [[nuclear-data-fendl]].

**PyFuel** — Tokamak Energy's fuel-cycle code, used for the ST-E1 inventory modelling, including a
concentration-dependent tritium-extraction efficiency curve
([[st-e1-tritium-systems-crossref-metadata-2026]]). Alongside **TMAP8**, which INL maintains and which
reproduces [[meschini-2023-tritium-fuel-cycle-arc-step|Meschini *et al.* 2023]] as a benchmark
case, and the Matlab Simulink model that paper itself uses, the vault now holds **three distinct
fuel-cycle code lineages** — none validated against an operating fuel cycle, because none exists.

## 5. Exascale and digital twins

### The compute

Fusion has been a driver application for every generation of leadership computing. Exascale machines — Frontier, Aurora, El Capitan, LUMI, JUPITER — run gyrokinetic and MHD simulations at scales that were impossible five years ago.

The stated ambition has shifted from *simulating isolated aspects* to *integrated simulation*: **combining plasma physics, materials science and engineering into a comprehensive virtual replica of a fusion device** — a digital twin.

### The digital twin, defined properly

A digital twin is not just a simulation. It is a model **coupled to live data from the physical machine**, updated continuously, used for prediction, diagnosis and control. The distinction matters: a simulation tells you what should happen; a twin tells you what is happening in the parts of the machine you cannot see.

Recent milestones:
- *Towards digital twins of fusion systems*, **Nucl. Fusion (2026)** — the current review
- *Summary report from the mini-conference on Digital Twins for Fusion Research*, **Phys. Plasmas 32, 050601 (2025)** — the community's consolidated position
- **[[thea-energy|Thea Energy]]'s stellarator digital twin** with **NVIDIA, Synopsys, Argonne and Princeton** — the clearest private-sector instance, and notably it includes an EDA company (Synopsys), which signals a chip-industry approach to design verification
- **DOE's Genesis Mission** selected its first projects in July 2026, several fusion-focused

The 2026 literature converges on a specific formulation: **validated tools leveraging high-fidelity exascale computing combined with multi-fidelity models, including AI-based surrogates.** You cannot run a gyrokinetic simulation inside a control loop; you can run a neural surrogate trained on one.

---

## 6. Where AI actually sits in the stack

Distinguishing the four genuinely different uses is worth doing, because they are often conflated:

| Use | What it does | Status |
|---|---|---|
| **Surrogate modelling** | Learned approximations replacing expensive solvers inside design and control loops | **Working, widely deployed.** TGLF-like reduced models, latent-space detachment models, NIF [[ignition]] prediction (*Science*, 2024) |
| **Real-time control** | RL agents commanding actuators directly | **Demonstrated on real machines.** [[tcv|TCV]] magnetic control (*Nature*, 2022); [[diii-d|DIII-D]] tearing avoidance (*Nature*, 2024) |
| **Design optimisation** | Searching high-dimensional design spaces | **Working.** Stellarator optimisation; latent diffusion models generating quasi-isodynamic configurations (arXiv:2608.16938) |
| **Data curation and interpretation** | Making decades of heterogeneous experimental data usable | **Underinvested.** DOE's FAIR repository and FEDER address exactly this |

That last row is where the least glamorous and possibly highest-return work is. Fusion has seventy years of experimental data in inconsistent formats across dozens of machines, and the empirical scaling laws that reactor designs depend on — IPB98(y,2) and its successors — are regressions over exactly that data.

---

## 7. The honest limitations

**Turbulence simulations still cannot span a discharge.** A first-principles gyrokinetic run covers milliseconds of a plasma that lives for seconds to minutes. Reactor predictions rely on reduced models calibrated against short high-fidelity runs, and on empirical scaling laws fitted to machines an order of magnitude smaller than the one being designed.

**Nobody has simulated a [[burning-plasma|burning plasma]] with validated confidence**, because there is no burning plasma to validate against. Every prediction for SPARC and ITER is an extrapolation, and the codes agree with each other more than they have been tested against reality.

**Nuclear data uncertainty is comparable to the TBR design margin**, as above.

**Integrated whole-plant modelling barely exists.** Coupling plasma to blanket to fuel cycle to structural response with quantified uncertainty is a DOE **long-term** milestone — 5 to 10 years out — meaning first-generation pilot plants will be designed without it.

**Validation and uncertainty quantification is the weakest link.** A code that reproduces existing experiments has been *calibrated*, not necessarily *validated*, and the difference only becomes apparent when you extrapolate. This is why DOE's roadmap calls for a **common VV/UQ framework** as a near-term deliverable — it is an admission that the field does not currently have one.

---

## 8. Why this belongs in a fusion dossier

It is tempting to treat computation as support infrastructure. It is not. Three concrete dependencies:

- **SPARC's performance prediction — the basis for a multi-billion-dollar machine and the DOE's national Milestone 1 — is a nonlinear CGYRO calculation.** If the turbulence model is wrong, the machine underperforms and there is no cheap way to find out first.
- **Every tritium breeding ratio is a neutronics calculation** resting on a library where a third of the isotopes are inherited from a fission evaluation and five have physically impossible heating numbers.
- **Every stellarator now being commercialised was designed by an optimiser**, not drawn by an engineer. Proxima's Stellaris, Thea's planar-coil array and Type One's [[infinity-two|Infinity Two]] exist because the objective function could be evaluated cheaply enough to search.

Fusion's computational stack is load-bearing. Its weakest members are **nuclear data** and **validated whole-plant integration** — and neither gets a fraction of the attention that magnets or plasma records receive.


## Evidence in `raw/`

Primary sources held in this vault that evidence the claims above:

- [[sparc-first-campaign-cgyro-predictions]]

---

**Continue to:** [[20-fusion-beyond-electricity|20 — Fusion Beyond Electricity]] · [[26-appendix-quantitative-data|26 — Appendix: Quantitative Progress Data]] · [[09-engineering-challenges|09 — Engineering Challenges]]
