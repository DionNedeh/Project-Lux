---
title: "Magnetic Confinement Devices"
type: synthesis
doc: 04
part: 1
aliases:
  - "Magnetic Confinement Devices"
tags:
  - fusion/synthesis
  - fusion/machines
created: 2026-08-25
updated: 2026-09-08
status: stable
confidence: high
related:
  - "[[05-inertial-confinement-fusion]]"
  - "[[06-iter-program]]"
  - "[[09-engineering-challenges]]"
---
# 04 — Magnetic Confinement Devices, Machine by Machine

*Project Lux · Every significant magnetic fusion device, past and present, with parameters*

---

## How to read a [[tokamak]]'s specification

Six numbers determine most of what a tokamak can do:

- **R** — major radius (metres), the distance from the machine's axis to the plasma centre
- **a** — minor radius (metres), the plasma's own half-width. **R/a** is the *aspect ratio*
- **B₀** — toroidal field on axis (tesla). Fusion power density goes as **B⁴**
- **I_p** — plasma current (megamperes). Confinement time goes roughly as **I_p**
- **V** — plasma volume (m³). Total fusion power goes as **B⁴ × V**
- **κ** — elongation, how vertically stretched the cross-section is. Higher κ allows higher current

The strategic tension in tokamak design is between **R** and **B**. [[iter|ITER]] chose to be large at modest field (5.3 T, 840 m³). [[sparc|SPARC]] chose to be small at very high field (12.2 T, ~20 m³). Both reach similar fusion performance, because 12.2/5.3 to the fourth power is about 28, which roughly compensates for being 40× smaller.

---

## Part I: Currently operating tokamaks

### [[east|EAST]] — Experimental Advanced Superconducting Tokamak
**China | [[asipp|ASIPP]], Hefei | since 2006**

| | |
|---|---|
| R / a | 1.85 m / 0.45 m |
| B₀ | 3.5 T |
| I_p | ~1 MA |
| Superconductor | NbTi (fully superconducting) |

The world's long-pulse leader. EAST's mission is **duration**, not power — it runs deuterium only, produces negligible fusion energy, and exists to answer the question of whether a plasma can be held in high-confinement mode for the timescales a power plant needs.

**Records:**
- **1,066 seconds** of steady-state [[h-mode|H-mode]] (January 2025) — beating its own 403 s from 2023
- **403 s** H-mode (2023)
- **1,056 s** of long-pulse plasma (2021)

**January 2026 result:** EAST reported experimental confirmation of a **"density-free region"** — evidence for a route past the [[greenwald-density-limit|Greenwald density limit]]. If this generalises, it relaxes one of the tokamak's fundamental operational constraints and matters directly for reactor design, since reactors want high density.

---

### [[jt-60sa|JT-60SA]]
**Japan / EU | QST, Naka | first plasma October 2023**

| | |
|---|---|
| R / a | 2.96 m / 1.18 m |
| B₀ | 2.25 T |
| I_p | 5.5 MA |
| Plasma volume | 135 m³ |
| Superconductor | NbTi + Nb₃Sn |

**The largest superconducting tokamak in operation.** Built jointly under the EU-Japan Broader Approach agreement — part of the compensation package for Japan losing the ITER site bid — its purpose is to explore ITER-relevant and DEMO-relevant scenarios ahead of ITER, particularly high-beta steady-state operation.

**Status August 2026:** Upgraded since 2024 with a **new carbon-armoured first wall and [[divertor]]** plus **in-vessel plasma control coils**. Commissioning of new equipment began 27 February 2026. The next experimental campaign starts at the end of 2026 and runs roughly six months.

**Notable result:** achieved first plasma under a **low toroidal inductive electric field of 0.15 V/m** — deliberately ITER-relevant, because ITER's superconducting central solenoid cannot supply the high loop voltages that copper-coil tokamaks use for breakdown.

---

### [[kstar|KSTAR]] — Korea Superconducting Tokamak Advanced Research
**South Korea | KFE, Daejeon | since 2008**

| | |
|---|---|
| R / a | 1.8 m / 0.5 m |
| B₀ | 3.5 T |
| Superconductor | Nb₃Sn + NbTi |

The first tokamak built entirely with Nb₃Sn superconductors, and a long-pulse and high-temperature research workhorse. KSTAR has held ion temperatures above 100 million K for tens of seconds, and installed a **tungsten divertor** in 2023-24, making it directly relevant to ITER's tungsten-wall strategy.

KSTAR is also where a substantial amount of the AI plasma-control work has been done, in collaboration with Princeton and DeepMind.

---

### [[diii-d|DIII-D]]
**USA | General Atomics, San Diego | since 1986**

| | |
|---|---|
| R / a | 1.66 m / 0.67 m |
| B₀ | 2.2 T |
| I_p | 2 MA |

The **US flagship** and the most flexible tokamak in the world. Copper coils (so pulsed, seconds not minutes), but with extraordinarily comprehensive diagnostics and shaping control. DIII-D's value is that you can ask it almost any physics question and get an answer quickly.

It is where **[[negative-triangularity|negative triangularity]]** operation has been most thoroughly explored, where DeepMind's **tearing-instability-avoidance reinforcement learning** was demonstrated (*Nature*, 2024), and where a very large fraction of the world's transport, [[pedestal]] and ELM-control database originates. The DOE roadmap explicitly names DIII-D as a facility to be sustained and connected to AI/HPC pipelines.

---

### [[west|WEST]] — Tungsten (W) Environment in Steady-state Tokamak
**France | CEA Cadarache | since 2016 (rebuilt from Tore Supra)**

Actively cooled tungsten divertor, superconducting coils, designed specifically to test **ITER-like plasma-facing components under long pulses**. WEST holds long-duration records in the tens of minutes for plasma with an actively cooled tungsten wall — a different and complementary record to EAST's.

---

### [[asdex-upgrade|ASDEX Upgrade]]
**Germany | IPP Garching | since 1991**

Medium-sized, all-tungsten wall, and the direct descendant of the machine where **H-mode was discovered in 1982**. AUG remains one of the most scientifically productive tokamaks in the world, and much of the current understanding of [[tungsten-pfc|tungsten plasma-facing components]], ELM control by magnetic perturbations, and [[detachment]] physics comes from it.

---

### [[tcv|TCV — Tokamak à Configuration Variable]]
**Switzerland | EPFL Lausanne | since 1992**

Extreme shaping flexibility — TCV can produce plasma cross-sections that no other machine can. This is where **DeepMind demonstrated deep-reinforcement-learning magnetic control** (*Nature*, 2022), commanding all 19 shaping coils directly.

---

### Spherical tokamaks: MAST-U, NSTX-U, [[st40|ST40]]

**[[mast-upgrade|MAST-Upgrade]]** (UKAEA Culham, R ≈ 0.85 m) is the world's leading testbed for the **[[super-x-divertor|Super-X divertor]]** — an alternative geometry that extends the field line length to the target and increases the wetted area. The 2025 *Nature Energy* result demonstrating transient heat-load control with Super-X is one of the more consequential exhaust results of the decade.

**NSTX-U** (PPPL) is the US spherical tokamak, undergoing extended repair and recovery.

**ST40** ([[tokamak-energy|Tokamak Energy]], Oxfordshire, R ≈ 0.4 m, B up to ~3 T) achieved **100 million K ion temperature in 2022** — the first privately funded device to do so, and remarkable for a machine that small. Its data appears in the Wurzel-Hsu Lawson dataset.

---

### Other operating machines

| Machine | Country | Note |
|---|---|---|
| **HL-3** (HL-2M) | China (SWIP, Chengdu) | Achieved 1 MA H-mode; China's advanced-divertor testbed |
| **[[t-15md|T-15MD]]** | Russia (Kurchatov) | Test-launched May 2021, first hot plasma March 2023 |
| **[[globus-m2|Globus-M2]]** | Russia (Ioffe) | Spherical tokamak |
| **[[hh70|HH70]]** | China ([[energy-singularity|Energy Singularity]]) | **World's first fully HTS tokamak**; first plasma June 2024; **1,337 s** long-pulse |
| **[[sst-1|SST-1]]** | India (IPR) | Steady-state superconducting tokamak |
| **[[jet|JET]]** | UK | **Retired December 2023** — see below |

---

## Part II: The machines being built

### SPARC — the most important machine in fusion right now
**USA | [[commonwealth-fusion-systems|Commonwealth Fusion Systems]] + MIT PSFC | Devens, Massachusetts**

| | |
|---|---|
| R / a | **1.85 m / 0.57 m** |
| B₀ | **12.2 T** |
| I_p | 8.7 MA |
| Superconductor | **REBCO HTS** |
| Fuel | **D-T** |
| Design goal | **Q > 2** |
| Nominal projection | **Q ≈ 11, ~140 MW fusion power** (at H98,y2 = 1) |

SPARC is a compact, high-field, D-T tokamak whose sole purpose is to be **the first magnetically confined plasma to produce net fusion energy**. Its design philosophy is the direct application of [[b4-scaling|the B⁴ scaling]]: rather than build something ITER-sized, build something JET-sized with more than twice the field.

The enabling technology is REBCO tape, validated by the **20 T model coil test of September 2021**. The design basis is published openly — a seven-paper special issue of the *Journal of Plasma Physics* (2020) laid out the physics case in public, which is unusual for a private company and has allowed independent scrutiny.

**Status, August 2026:**
- Approximately **80% assembled** as of 30 July 2026
- **TF1**, the first of 18 toroidal field magnets, installed in the Tokamak Hall
- All 18 magnets expected in place by **end of summer 2026**
- **First plasma and scientific breakeven targeted for 2027** (slipped from 2026)
- CFS raised **$1 billion from pension funds** in July 2026 — an industry first, and a signal that institutional capital now treats fusion as infrastructure rather than venture

**Why it matters beyond CFS.** If SPARC achieves Q > 1, it validates the entire high-field HTS thesis and compresses the schedule of every compact-tokamak program behind it. If it fails or badly underperforms, the credibility damage extends across the private sector. The DOE roadmap names *"Milestone 1: Q > 1, first demonstration in a U.S. fusion device"* as a headline national objective — which is, in practice, SPARC.

---

### [[arc|ARC]] — the first commercial plant
**USA | CFS | Chesterfield County, Virginia — "Fall Line Fusion Power Station"**

| | |
|---|---|
| Output | **~400 MWe** (from ~1.1 GW fusion power) |
| Site | James River Industrial Center, 94 acres |
| Cost | **>$2.5 billion** expected |
| Timeline | First power **early 2030s** |

**Status:** Chesterfield County Board of Supervisors approved the conditional-use permit unanimously. CFS became the **first fusion company to apply to PJM Interconnection**, the largest US wholesale electricity market, in early 2026. Design well advanced; site preparation imminent as of August 2026.

**Offtake:** [[google|Google]] has a **200 MW PPA** — half the plant's output — plus a direct equity investment.

ARC's key design feature is the **demountable magnet** concept and a **FLiBe (lithium fluoride-beryllium fluoride) liquid immersion blanket**, which serves simultaneously as neutron moderator, tritium breeder, and coolant, and allows the vacuum vessel to be replaced rather than repaired — a direct answer to the neutron-damage lifetime problem.

---

### ITER
See [[06-iter-program|Document 06]] for full treatment.

| | |
|---|---|
| R / a | 6.2 m / 2.0 m |
| B₀ | 5.3 T |
| I_p | 15 MA |
| Plasma volume | **840 m³** |
| Design goal | **500 MW for 400 s at Q = 10** |
| Start of Research Operation | **2034** |
| Start of D-T Operation | **2039** |

---

### [[best-tokamak|BEST]] and [[cfetr|CFETR]]
**China | ASIPP, Hefei**

**BEST** ([[burning-plasma|Burning plasma]] Experimental Superconducting Tokamak) is under construction in Hefei, intended to demonstrate burning plasma and, per Chinese statements, fusion power generation on a timeline aggressive relative to ITER. **CFETR** (China Fusion Engineering Test Reactor) is the planned follow-on, designed for several hundred MW fusion power with tritium breeding — effectively China's DEMO.

The supporting infrastructure — **CRAFT** (Comprehensive Research Facility for Fusion Technology) in Hefei — is a large technology test complex for magnets, divertors, and blankets. China's approach is characterised by building the *technology* facilities in parallel with the plasma facilities, rather than sequentially.

**Assessment:** China's public program is the best-resourced in the world in terms of construction throughput, and the FIA report notes explicitly that its coverage of Chinese private companies is incomplete because several declined to respond. The visible picture almost certainly understates Chinese activity.

---

### [[step|STEP]] — Spherical Tokamak for Energy Production
**UK | UKIFS | West Burton, Nottinghamshire**

The UK's flagship — a prototype **fusion power plant**, not an experiment, targeting net electricity to the grid around 2040.

**Status, 2026:**
- First land parcel transferred from EDF **23 March 2026 — three and a half years ahead of schedule**
- **£200 million** Construction Partner contract awarded to the **ILIOS consortium** (Kier-NUVIA joint venture)
- **Tokamak Energy** won a **£70M ($95M)** contract to supply HTS magnets
- Site capacity tripled to ~120 professionals; demolition and ash extraction of the former coal station ongoing
- UKIFS published its first Annual Report; first public consultation ran 14 January to 11 March 2026

---

## Part III: Stellarators

### [[wendelstein-7-x|Wendelstein 7-X]] — the world's leading [[stellarator]]
**Germany | IPP Greifswald | first plasma 10 December 2015**

| | |
|---|---|
| R / a | 5.5 m / 0.53 m |
| B₀ | 2.5 T |
| Plasma volume | 30 m³ |
| Coils | **50 non-planar + 20 planar superconducting** |
| Optimisation | **Quasi-isodynamic** |

W7-X is the vindication of forty years of stellarator optimisation theory. Its coils are shaped to roughly **1 mm tolerance** and were among the most complex engineered objects ever built; construction took over a decade and famously required rebuilding coils that failed acceptance testing.

**Records (2025 campaign, ended 22 May):**
- **World record [[triple-product|triple product]] for plasma durations above 10 seconds**, sustained across a **43-second** discharge
- Beats JET's long-pulse triple-product record despite **3× smaller plasma volume** and **5× less heating power**
- Peak triple product held stable for **1.9 s**
- Demonstrated **stable peaked density profiles** at tokamak-level performance (*Phys. Rev. E*, 2026)

That a stellarator now leads a tokamak on any confinement figure of merit is a genuine reversal of the 1969 verdict, and it is the single most important reason the private stellarator sector exists.

**What W7-X has not done:** it has no tritium, produces no fusion power, and is not designed to. It is a confinement-physics machine. Its purpose is to prove that an optimised stellarator can confine as well as a tokamak in steady state — which it has now largely done.

---

### LHD — [[lhd|Large Helical Device]]
**Japan | NIFS, Toki | 1998 – 25 December 2025**

The world's second-largest superconducting stellarator (heliotron configuration, R = 3.9 m, B = 3 T) and the first large fusion device built with superconducting coils. **Operations concluded on 25 December 2025** after 27 years and **200,000 plasma shots**, with 40% of experimental proposals in the final campaign coming from outside Japan.

LHD's legacy is a vast steady-state and high-density stellarator database, including ion temperatures above 100 million K and long-duration discharges, and it established much of what is known about impurity transport and divertor behaviour in helical devices.

---

### Private stellarators

**[[type-one-energy|Type One Energy]]** — *[[infinity-two|Infinity Two]]*
Optimised stellarator, targeting a **350 MW** plant at a former **Tennessee Valley Authority** coal site in Tennessee by the mid-2030s. Total funding past **$160M** (including an $87M convertible note). Has published a full physics basis in the *Journal of Plasma Physics*, including breeder blanket and tritium fuel-cycle feasibility — an unusually complete public design for a private company. Licensed **cryogenic pellet fuelling technology from ORNL** in August 2026.

**[[thea-energy|Thea Energy]]** — [[canis|Canis]] → [[eos|Eos]] → [[helios|Helios]] (preconceptual design published; see [[overview-of-the-helios-design]])
HQ Kearny, New Jersey. Distinctive approach: rather than complex 3D coils, Thea uses **arrays of simple planar coils** whose individually controlled currents synthesise the required 3D field. Canis physically demonstrated nine-coil manufacture and static closed-loop field control within 1% of prediction at 20 K. It was a flat magnet array, not a plasma device; Eos remains the planned integrated test. See [[prototyping-test-canis-hts-planar-coil-array]].

- **First DOE Milestone Program awardee to complete a full fusion pilot plant design review** — a genuine first for the sector
- **$20M [[arpa-e|ARPA-E]] SCALEUP award** (9 July 2026) for the **first US modular HTS magnet production line**
- Series B extension in August 2026 on top of a $100M Series B led by Thomas Tull's US Innovative Technology Fund
- Stellarator **digital twin** partnership with NVIDIA, Synopsys, Argonne and Princeton

**[[proxima-fusion|Proxima Fusion]]** — *Stellaris*
Munich, spun out of the Max Planck IPP (i.e. the W7-X lineage). Raised **€130M Series A** (May 2025) and **$518M** in the year to July 2026 — the second-largest raise in the industry that year. Published the first fully integrated, quasi-isodynamic stellarator power-plant design optimised simultaneously for physics *and* engineering.

**Others:** [[renaissance-fusion|Renaissance Fusion]] (France, HTS + liquid metal walls), [[helical-fusion|Helical Fusion]] (Japan), [[gauss-fusion|Gauss Fusion]] (Germany), [[stellarex|Stellarex]] (US).

---

## Part IV: Mirrors, FRCs, and pinches

### [[wham|WHAM]] / [[realta-fusion|Realta Fusion]]
**USA | UW-Madison → Realta**

- **17 tesla** on a confined plasma, 15 July 2024 — **the highest magnetic field ever applied to a fusion plasma**
- **19 June 2026: first commercial fusion company to demonstrate [[direct-energy-conversion|direct energy conversion]]** of plasma energy to electricity
- April 2026: strategic partnership with **CFS** for HTS magnets covering the **Anvil** demonstration device and its commercial successor **Hammir**
- Targeting first-of-a-kind plants mid-2030s, initially for **industrial process heat** rather than grid electricity

The Realta-CFS magnet deal is structurally significant: it is the first clear instance of one fusion company becoming a *supplier* to another, which is how an industry rather than a set of competing prototypes is formed.

### [[tae-technologies|TAE Technologies]]
**USA | Foothill Ranch, California | founded 1998**

The oldest and one of the largest private efforts (>$1.2 bn raised). [[field-reversed-configuration|Field-reversed configuration]] with **[[neutral-beam-injection|neutral beam injection]]** to sustain and heat the plasma — the beams both fuel and stabilise the FRC.

Machine lineage: C-2 → C-2U → C-2W ("Norm") → *Copernicus* → *Da Vinci*.

**2025-26 development:** TAE announced that **Norm outperformed expectations**, achieving plasma formation with neutral beams alone (a substantial simplification), and that it would **skip the planned Copernicus device** and move directly toward Da Vinci, its first commercial plant. Reporting since has been inconsistent on whether Copernicus is fully cancelled or deferred — sources conflict, and this dossier does not resolve it.

TAE's long-term target is **p-¹¹B**, which requires roughly 3 billion K. Norm has reached ~75 million K for ~30 ms. The gap is real and TAE does not dispute it; the argument is that FRC beta near 1 makes the fuel accessible eventually.

### [[helion-energy|Helion Energy]]
**USA | Everett, Washington**

Pulsed, colliding FRCs compressed magnetically, with **direct electricity recovery** — as the fused plasma expands against the field, it induces current back into the coils. No steam cycle. Targets **D-³He**, breeding its own ³He from D-D reactions.

- **[[polaris|Polaris]]**: reached **150 million °C** (announced February 2026); **first privately funded machine to operate with D-T fuel**; running near-daily to validate electricity recovery
- **Orion**: the commercial plant under construction at Malaga, Washington, to supply [[microsoft|Microsoft]] under the world's first fusion PPA. **≥50 MW after a one-year ramp; target 2028**
- Valuation **$15.5 bn**; raised **$465M** in the year to July 2026

Helion is the most aggressive timeline in the industry and the most polarising. It publishes less peer-reviewed detail than CFS or Type One, which draws consistent criticism; it also has a signed PPA with a counterparty that has done technical diligence, which is a form of validation the field has not previously had.

### [[zap-energy|Zap Energy]]
**USA | Everett, Washington**

**Sheared-flow-stabilized Z-pinch** — a plasma column carrying its own current, stabilised against sausage and kink modes by an axial velocity shear, with **no external magnetic coils at all**. Devices: FuZE, FuZE-Q, Century.

- Electron temperatures above **1 keV** (>10 million °C) demonstrated in a sheared-flow Z-pinch
- Named **#16 on TIME's Top GreenTech Companies 2026** — the highest-ranked fusion company
- DOE Milestone Program awardee

If the sheared-flow stabilisation holds at reactor-relevant currents, Zap's machine would be by far the cheapest and simplest fusion device ever built. That is a large "if" against a concept with a seventy-year history of instability.

### [[general-fusion|General Fusion]]
**Canada | Richmond, BC | founded 2002**

**Magnetized Target Fusion**: inject a magnetised plasma into a rotating cavity of liquid lead-lithium, then collapse the cavity mechanically. The liquid metal is simultaneously first wall, breeding blanket and coolant — and being liquid, it cannot be damaged by neutrons.

- **LM26 ([[lm26|Lawson Machine 26]])** reached **0.72 keV** (~8.4 million °C) plasma heating
- **Listed on Nasdaq as GFUZ, July 2026 — the first publicly traded fusion company**, via merger with Spring Valley Acquisition Corp. III (completed 10 July 2026)
- ~$150M cash funds the LM26 program through **end of 2028**

General Fusion went public after a difficult funding period, and its transition to public markets means its progress is now visible on a quarterly basis — which the FIA report notes will bring "a different type of scrutiny" to the whole sector.

---

## Part V: The retired machines that made all this possible

### JET — Joint European Torus
**UK | Culham | 25 June 1983 – December 2023**

| | |
|---|---|
| R / a | 2.96 m / 1.25 m |
| B₀ | 3.45 T |
| I_p | 4.8 MA |

The most important fusion device ever built. JET is the only machine to have run three separate D-T campaigns, and it holds the record for total fusion energy in a magnetic device.

- **1991 (PTE)**: 1.7 MW — first controlled fusion power in a magnetic device
- **1997 (DTE1)**: **16.1 MW peak, 22 MJ, Q = 0.67** — a record that stood 25 years
- **2021 (DTE2)**: 59 MJ over 5 s, with the new ITER-like beryllium/tungsten wall
- **3 October 2023 (DTE3)**: **69 MJ over ~5 s from 0.2 mg of fuel**

DTE3's real value was not the record. It was the demonstration, in an actual D-T plasma, of the **quasi-continuous exhaust** and **X-point radiator** regimes — advanced divertor scenarios that avoid the damaging transient heat loads of conventional ELMy H-mode. These are directly what ITER needs.

96 research papers were submitted within a year of the campaign's end. JET's **Decommissioning and Repurposing programme** — itself the world's first dismantling of a tritium-contaminated tokamak, and a source of irreplaceable data for every future plant's end-of-life planning — runs to roughly 2040.

### [[tftr|TFTR]]
**USA | PPPL | 1982–1997.** First extensive 50/50 D-T campaign. **10.7 MW** fusion power (1994), **1,500 MJ** total. Nuclear Historic Landmark, 2020.

### [[alcator-c-mod|Alcator C-Mod]]
**USA | MIT | 1991–2016.** The high-field, compact ancestor of SPARC. Set the record for **plasma pressure in a magnetically confined plasma (2.05 atmospheres)** on its final day of operation in September 2016. C-Mod's entire research program was an argument that high field beats large size — an argument that CFS was founded to prove.

### Others
**TFR** (France), **PLT** (Princeton — 60 million K in 1978), **ASDEX** (where H-mode was found), **[[t-3|T-3]]** (the machine that converted the world to tokamaks), **T-10**, **JT-60U** (which held the equivalent-Q record of 1.25 in D-D-scaled terms), **[[mftf-b|MFTF-B]]** (the $372M mirror cancelled in 1986 on the day it was completed), **[[zeta|ZETA]]**.

---

## Summary: the state of magnetic confinement, August 2026

**What has been proven:** plasmas can be confined at fusion temperatures for over 1,000 seconds (EAST, HH70); optimised stellarators confine as well as tokamaks at long pulse (W7-X); HTS magnets work at 17–20 T (WHAM, CFS, Tokamak Energy); D-T operation produces tens of megajoules (JET); advanced exhaust regimes function in D-T (JET DTE3); direct energy conversion works (Realta).

**What has never been proven:** Q > 1 in *any* magnetic device; a burning plasma in *any* device; tritium self-sufficiency in *any* device; a magnetic device operating with a burning plasma for a full duty cycle.

**The gap closes — or does not — in 2027, at Devens, Massachusetts.**

---

**Continue to:** [[05-inertial-confinement-fusion|05 — Inertial Confinement Fusion]] · [[06-iter-program|06 — The ITER Program]] · [[09-engineering-challenges|09 — Engineering Challenges]]
