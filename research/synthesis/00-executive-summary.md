---
title: "Executive Summary"
type: synthesis
doc: 00
part: 1
aliases:
  - "Executive Summary"
tags:
  - fusion/synthesis
  - fusion/overview
created: 2026-08-25
updated: 2026-08-29
status: stable
confidence: high
related:
  - "[[01-fusion-physics-fundamentals]]"
  - "[[12-state-of-play-2026]]"
  - "[[14-open-problems-and-risks]]"
  - "[[17-diagnostics-control-disruption]]"
  - "[[19-simulation-codes-nuclear-data]]"
  - "[[22-critical-materials-supply-chains]]"
  - "[[26-appendix-quantitative-data]]"
  - "[[27-people-institutions-public-trust]]"
  - "[[29-remote-handling-and-maintenance]]"
  - "[[32-heavy-ion-fusion-and-pulsed-power]]"
  - "[[34-investment-mechanics]]"
  - "[[35-fusion-and-climate]]"
  - "[[38-component-manufacturing]]"
---
# 00 — Executive Summary

*Project Lux · compiled 25 August 2026*

---

## 1. The single most important thing to understand

Fusion energy has, in the last four years, undergone a change of *kind*, not just of degree.

Until December 2022, no laboratory on Earth had ever released more fusion energy from a plasma than was delivered into it. That threshold — **scientific breakeven** — had been the field's horizon for seventy years. It has now been crossed eleven times at a single facility, and a second, entirely different class of machine is being assembled to cross it a twelfth time by a completely different route.

The consequence is that the binding constraint on fusion has moved. For seventy years the question was *"can a plasma be made to burn?"* The answer is now yes. The question for the next fifteen years is *"can a machine be built around a [[burning-plasma|burning plasma]] that survives its own neutrons, breeds its own fuel, and sells electricity at a price anyone will pay?"*

That is an engineering and economics question. It is not obviously easier.

---

## 2. Where the numbers stand, August 2026

### Physics performance

| Metric | Best achieved | Where | When |
|---|---|---|---|
| Fusion energy from one shot | **8.6 MJ**, target gain **4.13** (2.08 MJ laser in) | NIF (LLNL) | 7 April 2025 |
| Most recent [[ignition]] | 7.9 ± 0.4 MJ, gain ~3.8 — 11th ignition | NIF | 20 June 2026 |
| Fusion energy, magnetic confinement | **69 MJ** over ~5 s from 0.2 mg fuel | [[jet|JET]] (DTE3) | 3 October 2023 |
| Fusion power, magnetic confinement | 16 MW (Q≈0.67, transient) | JET (DTE1) | 1997 |
| Steady-state [[h-mode|H-mode]] duration | **1,066 s** | [[east|EAST]] (China) | January 2025 |
| Long-pulse plasma, fully-HTS [[tokamak]] | **1,337 s** | [[hh70|HH70]] ([[energy-singularity|Energy Singularity]]) | 2026 |
| [[triple-product|Triple product]], pulses >10 s | World record | [[wendelstein-7-x|Wendelstein 7-X]] | 2025 campaign |
| Magnetic field on a confined plasma | **17 T** | [[wham|WHAM]] (UW-Madison / Realta) | 15 July 2024 |
| HTS tokamak-configuration magnet | 11.8 T, 7 MA-turns | Demo4 ([[tokamak-energy|Tokamak Energy]]) | 2026 |

### Money

- **$14.24 billion** total private + public investment in fusion companies since tracking began
- **$4.48 billion** raised in the 12 months to July 2026 — a record, up 69% year on year
- **$13.26 bn private / $0.98 bn public** split
- **56 companies** surveyed, up from 23 in 2021; **five have raised over $1 bn** (CFS, TAE, Helion, [[pacific-fusion|Pacific Fusion]], SHINE — all US)
- **~5,600 direct employees**, plus ~10,500 supply-chain jobs
- Companies estimate they each need a further **$2.7 bn on average** (median $1.2 bn) to reach a commercial plant

### Machines being built right now

| Machine | Owner | Purpose | Status |
|---|---|---|---|
| **[[sparc|SPARC]]** | [[commonwealth-fusion-systems|Commonwealth Fusion Systems]] | First net-energy tokamak (Q>1) | ~80% assembled; first plasma & breakeven targeted **2027** |
| **[[iter|ITER]]** | 35 nations | Burning plasma at 500 MW, Q≥10 | Sector modules installing; research ops **2034**, D-T **2039** |
| **Orion** | Helion | First fusion plant on a PPA ([[microsoft|Microsoft]]) | Under construction, Malaga WA; power targeted **2028** |
| **[[arc|ARC]]** | Commonwealth Fusion Systems | First grid-scale commercial plant, ~400 MWe | Permitted, site prep imminent, Chesterfield VA; early 2030s |
| **[[step|STEP]]** | UK (UKIFS) | Prototype fusion power plant | Site acquired 3.5 yrs early; £200M construction partner appointed |
| **[[best-tokamak|BEST]]** | China ([[asipp|ASIPP]]) | Burning plasma demonstration | Under construction, Hefei |
| **LM26** | [[general-fusion|General Fusion]] | Magnetized target fusion demo | Operating; 0.72 keV reached; funded through 2028 |
| **Anvil** | [[realta-fusion|Realta Fusion]] | Tandem mirror demo | Magnets contracted to CFS |
| **Eos** | [[thea-energy|Thea Energy]] | Planar-coil [[stellarator]] | Fast-tracked; magnet line funded by [[arpa-e|ARPA-E]] |

---

## 3. The four things that actually stand between here and a power plant

Ranked by how often they appear as a top concern in the FIA's survey of the companies themselves, and by how much of the DOE roadmap is devoted to them.

### 3.1 Neutron-tolerant materials — *the hardest problem*

A D-T fusion plant subjects its first wall to roughly **15 [[displacements-per-atom|displacements per atom]] per year**. ITER, over its entire operating life, will accumulate **less than 2 dpa**. There is, today, **no facility anywhere in the world** that can irradiate candidate materials with a fusion-spectrum neutron flux to the doses a power plant will experience.

The 14.1 MeV neutron is the problem. Above about 3 MeV, neutrons transmute nuclei in the structure, producing helium and hydrogen gas inside the metal lattice. The helium collects at grain boundaries and embrittles the steel in a way that fission-reactor data cannot predict, because fission neutrons are too soft to do it.

Two facilities are meant to close this gap: **[[ifmif-dones|IFMIF-DONES]]** in Granada, Spain (a 40 MeV, 125 mA deuteron beam on a lithium jet, targeting ~20 dpa in phase 1 and ~50 dpa in phase 2) and the US **Fusion Prototypical Neutron Source (FPNS)**, which the June 2026 DOE roadmap places in the *mid-term, 3–5 year* construction window. Neither is operating. Every pilot-plant schedule in the industry assumes materials qualification that no one can currently perform.

*29 of 44 companies named this a near-term challenge and 25 named it a long-term one — the highest long-term score of any issue.*

### 3.2 Tritium — *the fuel does not exist*

Deuterium is effectively free: it is 1 part in 6,400 of ordinary hydrogen and there is enough in the ocean to last indefinitely. Tritium is the opposite. It has a **12.3-year half-life**, does not occur naturally in useful quantities, and the entire world civilian inventory is projected at **30–40 kg** over the coming decade, produced mostly as a byproduct of CANDU heavy-water fission reactors at **less than 0.13 kg per reactor per year**. Market price has settled around **$30,000–35,000 per gram**.

A single 1 GW fusion plant would burn on the order of **55–60 kg of tritium per year**.

The arithmetic is therefore unforgiving: **no fusion plant can ever be fuelled from external supply.** Every plant must breed its own tritium, in a lithium blanket surrounding the plasma, via `n + ⁶Li → T + ⁴He`. It must achieve a **[[tritium-breeding-ratio|tritium breeding ratio (TBR)]] above 1** — the DOE roadmap sets the design target at **TBR > 1.1** — while simultaneously extracting, purifying, and re-injecting that tritium with low enough inventory and losses to close the loop.

This has never been demonstrated at any scale. ITER will be the first device to test breeding blanket modules at all, and it will do so from an externally supplied tritium inventory.

There is a second-order bottleneck: **[[lithium-6]]**. Natural lithium is only 7.5% Li-6, and blankets need 30–90% enrichment. Historic enrichment capacity is concentrated in Russia and China, which the DOE roadmap and industry commentary both flag as a sovereignty risk.

### 3.3 Plasma exhaust — *the [[divertor]] problem*

A 500 MW fusion plasma dumps roughly **100 MW** of power onto a strike region a few millimetres wide. Unmitigated, that is an order of magnitude beyond what any solid material can survive: tungsten, the best available choice, tolerates roughly **5–20 MW/m²** steady-state, and requires the plasma temperature at the target to fall into the single-electron-volt range to avoid sputtering the wall into the plasma.

The mitigation is **[[detachment]]** — deliberately radiating the power away in the divertor volume using seeded impurities (nitrogen, neon, argon) before it reaches the surface — while somehow not degrading the core plasma that is producing the fusion power in the first place. That tension between a hot core and a cold edge is unresolved at reactor scale.

Alternative geometries are being tested: the **[[super-x-divertor|Super-X divertor]]** on [[mast-upgrade|MAST-Upgrade]] demonstrated transient heat-load control (Nature Energy, 2025), the **X-point radiator** and **quasi-continuous exhaust** regimes were extended into D-T on JET's final campaign, and **[[negative-triangularity|negative triangularity]]** is under study as a way to avoid edge-localised modes entirely.

### 3.4 Cost — *the number nobody can pin down*

A 2026 analysis in *Nature Energy* compiled first-of-a-kind capital cost estimates and found a range of **$1,400 to $43,000 per kilowatt** — a thirty-fold spread. The US National Academies have set **$5 billion overnight cost** as the threshold for a viable pilot plant; design studies such as [[manta|MANTA]] claim $3.4 bn. Mature-technology LCOE projections cluster around **$110–145/MWh** depending on confinement scheme, which most analysts consider optimistic.

For context: CFS's first ARC plant is expected to cost **over $2.5 billion** for ~400 MWe, which is roughly $6,250/kW — inside the plausible band but far above gas or solar.

---

## 4. The thing that changed the funding picture: AI

The fusion investment surge is not primarily a climate story any more. The FIA's own foreword names it explicitly: *"the last year has added an important new driver: the energy demand of artificial intelligence."*

AI data-centre electricity demand is projected to rise from **460 TWh in 2024 to roughly 1,300 TWh by 2035**. A single hyperscale AI facility draws **300–500 MW** — comparable to a mid-sized city. As of May 2026, hyperscalers had committed to **over 9.8 GW across 13 nuclear projects**.

Fusion's profile — firm, high-capacity-factor, siteable near load, carbon-free, no fuel-price exposure — maps onto that demand almost perfectly. Hence:

- **Helion ↔ Microsoft**: the world's first fusion PPA (2023), ≥50 MW after a one-year ramp, targeted 2028
- **[[google|Google]] ↔ CFS**: 200 MW from the first ARC plant — half its output — plus a direct investment
- Five companies now hold PPAs or offtake commitments; six hold siting agreements

These agreements matter beyond their megawatts. They convert speculative technology risk into a bankable revenue line, which is what makes project finance for a first-of-a-kind plant possible at all.

---

## 5. The regulatory unlock

On **26 February 2026** the [[us-nrc|US Nuclear Regulatory Commission]] published a proposed rule, *Regulatory Framework for Fusion Machines*, that regulates commercial fusion under the **byproduct material framework (10 CFR Part 30)** rather than the reactor licensing framework (Part 50) used for fission.

This is a very large deal. It means fusion is regulated on the basis of the radioactive materials it handles — principally tritium and activation products — rather than as a reactor with accident scenarios involving criticality and decay heat. The framework is performance-based, technology-inclusive and risk-informed. Crucially, it means **39 Agreement States**, not the NRC, will license most fusion facilities, which is faster and cheaper.

Comments closed 27 May 2026; a final rule is targeted for **October 2026**, well ahead of the December 2027 deadline set by NEIMA.

The physical basis for this treatment is sound: a fusion plant contains no fissile material, cannot sustain a chain reaction, has no decay-heat meltdown pathway, and produces no transuranics or fission products. Its activated structures become handleable in **50–100 years** rather than the geological timescales of spent fission fuel.

---

## 6. Timelines: what the field says, and how to read it

From the FIA survey of 47 companies on when they will field a **first pilot plant**:

- Before 2030 — **4**
- 2030–2035 — **28**
- 2036–2040 — **11**
- 2040–2045 — **4**

And on **first commercial electricity** (45 responses): 3 say 2026–2030, 16 say 2031–2035, 13 say 2036–2040, 9 say 2041–2045.

Two observations are worth making about this distribution.

**First, it has been remarkably stable.** The FIA notes that across six annual reports the modal answer has stayed in the 2030s. Timelines in fusion have historically slipped a year per year; these have not, at least not yet.

**Second, it is a survey of survivors and optimists.** Companies that believed they were 25 years away would struggle to raise money, so they either do not exist or do not say so. The FIA's own CEO is blunt about what comes next: *"When we emerge into a fully commercial fusion industry, few expect there to be 56 companies in it."*

The public programs are more conservative and more explicit about it. ITER will not run D-T until **2039**. [[eurofusion|EUROfusion]] targets DEMO construction in the 2030s and **fusion electricity on the European grid by 2050**. The DOE roadmap targets **commercialization by the mid-2030s** but conditions every milestone on appropriations.

A reasonable synthesis: **scientific net gain on a magnetic device is likely within 1–3 years** (SPARC, 2027, is the leading candidate and has already built most of the hardware). **A machine that puts fusion-derived electricity onto a grid in any quantity is plausible in the late 2020s to early 2030s** (Helion's Orion is the earliest credible attempt). **A plant that generates electricity economically, breeds its own tritium, and survives a full-power year is a 2040s proposition** unless the materials problem resolves faster than currently looks likely.

---

## 7. The near-term calendar

| When | What to watch |
|---|---|
| **Late 2026** | NRC final fusion rule; [[jt-60sa|JT-60SA]] restart campaign (~6 months); ITER Central Solenoid stacking completes |
| **2027** | **SPARC first plasma and attempted scientific breakeven** — the single most consequential scheduled event in the field; HH170 construction completion (China) |
| **2028** | Helion Orion targets first power to Microsoft; General Fusion LM26 program milestones conclude |
| **Early 2030s** | CFS ARC first power to Virginia grid (Google PPA); [[type-one-energy|Type One Energy]] [[infinity-two|Infinity Two]] at TVA site; STEP construction |
| **2034** | ITER Start of Research Operation |
| **2039** | ITER Start of D-T Operation |
| **2050** | EUROfusion target for fusion electricity on the European grid |

---

## 8. What would change this picture

**Upside surprises that are genuinely possible:**
- SPARC exceeds Q=1 comfortably in 2027 and validates the high-field HTS pathway, compressing every compact-tokamak schedule behind it
- A breeding blanket demonstrates TBR > 1.1 in an integrated test at ORNL's [[unity-3|UNITY-3]] or equivalent, removing the deepest uncertainty in the fuel cycle
- HTS tape production scales past the ~10,000 km/yr global bottleneck, and magnet cost falls the way solar module cost did
- AI-driven plasma control (already demonstrated for magnetic control and tearing-mode avoidance on real tokamaks) removes [[disruption]] risk as a design constraint

**Downside risks that are equally real:**
- SPARC underperforms, or a magnet or divertor failure costs years
- [[helium-embrittlement|Helium embrittlement]] at 10–15 dpa turns out to disqualify the leading structural steels, and there is still no facility to find out until the 2030s
- Tritium start-up inventory proves unobtainable for a fleet — one plant may be fuellable, twenty may not
- First-of-a-kind capital cost lands at the top of the $1,400–43,000/kW range and fusion is simply outcompeted by fission plus storage
- The 56 companies consolidate hard in a funding downturn, taking supply-chain capacity with them

---

## 9. Bottom line

Fusion is no longer a physics bet. It is a **materials, fuel-cycle, and capital-cost bet**, being placed with real money by serious institutions on a 2030s timeline, against engineering problems that are well-characterised but genuinely unsolved.

The most honest summary of August 2026 is this: **the plasma physics community has largely delivered what it promised, and has handed the problem to the metallurgists, the tritium chemists, and the project financiers.** Whether those three groups can deliver on a comparable timescale is the open question, and nothing that has happened so far tells us the answer.

---

## 10. A note on what this summary leaves out

The nine sections above cover the field as it is usually described: physics, machines, money, timelines. A second pass through the dossier (**Documents 16–27**) covers the systems that account is built on top of, and several of them contain material that changes the picture:

- **[[17-diagnostics-control-disruption|17 — Disruption mitigation]]**: current modelling finds **no acceptable runaway-electron outcome for a full-current ITER D-T disruption**. This is an unsolved problem on the critical path of the world's largest fusion project, and it is far less discussed than tritium or materials.
- **[[19-simulation-codes-nuclear-data|19 — Nuclear data]]**: the cross-section libraries underpinning every tritium breeding calculation carry uncertainties **comparable to the entire TBR design margin**.
- **[[22-critical-materials-supply-chains|22 — Critical materials]]**: the **2026 helium crisis** removed roughly a third of global supply and was on nobody's fusion risk register in 2025.
- **[[26-appendix-quantitative-data|26 — Quantitative data]]**: the highest triple product ever achieved in a tokamak was set by **[[tftr|TFTR]] in 1995** and has not been beaten since — a quantitative demonstration that the field's long plateau was a construction stall, not a physics one.
- **[[27-people-institutions-public-trust|27 — Workforce]]**: PhD admissions contracted in 2024–25, forecasting a shortage of principal investigators and lead engineers **in the early 2030s**, precisely when pilot plants are scheduled.

A third pass (**Documents 28–39**) covers the plant systems, the design lineages, and the arguments:

- **[[35-fusion-and-climate|35 — Fusion and Climate]]**: integrated assessment models find that **cost-minimising scenarios do not build fusion before about 2070**, even when it is available from 2050. Fusion is a second-half-of-the-century technology, and the climate case usually made for it is not the one the models support.
- **[[32-heavy-ion-fusion-and-pulsed-power|32 — Heavy Ion Fusion]]**: an entire ICF driver class — more efficient, natively high-repetition-rate, with standoff final optics — was cancelled in 2011/12 for want of an ignition proof that now exists.
- **[[38-component-manufacturing|38 — Component Manufacturing]]**: tungsten monoblocks have survived **1,000 cycles at 20 MW/m²** in the ITER Divertor Test Facility — unirradiated. Meanwhile the US **cannot yet melt fusion-grade structural steel at industrial scale**.
- **[[34-investment-mechanics|34 — Investment Mechanics]]**: General Fusion's SPAC was announced with $230m of trust capital and delivered **$127m** after redemptions — fusion's first real public-market price signal, and a cautious one.
- **[[29-remote-handling-and-maintenance|29 — Remote Handling]]**: JET is the only tokamak ever maintained remotely. Replacing its first wall took **18 months of two-shift working**. That is the benchmark a commercial plant must beat annually.


**On the survivorship point above.** [[45-survivorship-failure-and-retrenchment]] develops it with primary sourcing for two 2025
cases, and records what the FIA data does and does not capture: exit is counted (3 dropouts against
6 new entrants in 2026) but never characterised, and a company that abandons power generation while
remaining in the survey — as [[first-light-fusion]] did — does not register as exit at all.

---

**Continue to:** [[01-fusion-physics-fundamentals|01 — Physics Fundamentals]] · [[12-state-of-play-2026|12 — State of Play 2026]] · [[14-open-problems-and-risks|14 — Open Problems]] · [[26-appendix-quantitative-data|26 — Quantitative Data]]
