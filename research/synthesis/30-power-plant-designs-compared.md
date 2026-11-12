---
title: "Power Plant Designs Compared"
type: synthesis
doc: 30
part: 3
aliases:
  - "Power Plant Designs Compared"
tags:
  - fusion/synthesis
  - fusion/designs
created: 2026-08-25
updated: 2026-10-19
status: stable
confidence: high
related:
  - "[[03-confinement-approaches]]"
  - "[[09-engineering-challenges]]"
  - "[[helios]]"
  - "[[st-e1]]"
  - "[[balance-of-plant]]"
  - "[[10-economics-and-markets]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
  - "[[29-remote-handling-and-maintenance]]"
  - "[[31-plasma-physics-deeper-cuts]]"
  - "[[33-safety-environment-decommissioning]]"
---
# 30 — Fusion Power Plant Designs Compared

*Project Lux · Sixty years of paper reactors, and what the design choices reveal*

---

## 1. Why paper reactors matter

No fusion power plant exists. But dozens have been designed in detail — some over multi-year programmes with substantial budgets — and those design studies are the field's accumulated answer to the question *"what would this actually look like?"*

They are worth studying for a specific reason: **a power plant design study is where all the constraints in this dossier meet.** Confinement physics, magnet technology, tritium breeding, heat exhaust, materials limits, remote maintenance and cost all have to close simultaneously in a single self-consistent point design. When they cannot be made to close, the study tells you which constraint broke — and that is more informative than any individual result.

### The systems codes

Design studies are produced by **systems codes**: integrated models that solve the plasma physics, engineering and cost equations together and search for a feasible optimum. The ones in use:

| Code | Used for |
|---|---|
| **PROCESS** | UK / EU; used in [[cfetr|CFETR]] assessment |
| **SYCOMORE** | EU-DEMO |
| **GASC** | CFETR assessment |
| **ARIES systems code** | The US ARIES series |
| **TPC** | Japanese DEMO |
| **BLUEPRINT**, **FUSE** | Newer open frameworks |

These codes encode the field's assumptions. When two of them disagree about whether a machine closes, the disagreement is usually about a scaling law or a materials limit — which is why *Developing Integrated Cost Models for Fusion Power Plants* (J. Fusion Energy, 2025) matters as much as any physics paper.

---

## 2. The design studies, by lineage

### The ARIES series (US, 1990s–2010s)

The most systematic body of fusion power plant design work ever undertaken. **Five ARIES designs corresponding to five different [[tokamak]] operating modes**, compared using physics figures of merit that quantify major parameters in a common operating space.

The critical physics areas the ARIES studies identified as design-limiting are worth listing, because they have not changed:
- **MHD stability**
- **Current drive**
- **Heat exhaust**
- **Energy confinement**
- **[[helium-ash|Helium ash]] removal**

That fifth item appears in almost no popular account of fusion and in every serious design study ([[28-vacuum-wall-conditioning-tritium-plant|Document 28 §5]]).

**ARIES-AT** — the advanced tokamak endpoint — was the series' most optimistic and most influential design: roughly 1,000 MWe, high bootstrap fraction, SiC/SiC composite structure with a lithium-lead breeder, and a claimed cost of electricity competitive with fission. It became, for two decades, the reference for "what fusion could be" — and its assumptions about SiC/SiC maturity and advanced-tokamak physics have not been validated since.

**ARIES-CS** was the compact [[stellarator]] variant, and it established the scale of the stellarator's engineering penalty in a directly comparable framework.

### [[eu-demo|EU DEMO]] (2010s–present)

The most conservative major design, deliberately.

The European strategy has been to let [[iter|ITER]] retire the physics risk and then build a machine that **requires no new physics**. DEMO is consequently large (major radius around 9 metres), operates in conventional ELMy [[h-mode|H-mode]], uses a **pulsed** inductive scenario with thermal storage rather than betting on steady-state advanced scenarios, and targets roughly **2 GW of fusion power for around 500 MWe net**.

Its distinguishing features are that it must **breed its own tritium**, demonstrate **net electricity to the grid**, and achieve the **availability a utility requires** — none of which ITER does. Two blanket concepts have been carried in parallel for most of its history: **HCPB** (helium-cooled pebble bed, with beryllium multiplier) and **WCLL** (water-cooled lithium-lead).

**The critique:** DEMO's conservatism makes it large, and large makes it expensive. Its existence has also been a moving target — the design has been re-baselined repeatedly, and construction start has slipped with ITER's schedule.

**And conservatism on physics has not bought simplicity on plant.** DEMO's published [[balance-of-plant|balance of plant]] needs **8 separated primary coolant systems under WCLL and 14 under HCPB**, with 10 and 14 primary heat exchangers or steam generators — against **one** primary circuit and four steam generators in a European Pressurized Reactor running at 4,300 MWth to DEMO's ~2,300 ([[maturation-of-critical-technologies-demo-balance-of-plant]]). It is the clearest measurement anywhere in this document of how much of a fusion plant is *not* the fusion part.

### [[arc|ARC]] and the compact high-field line (2015–present)

**ARC** — *Affordable, Robust, Compact* — was published from MIT in 2015 and is the design that reorganised the field. The original paper's parameters: major radius **3.3 m**, on-axis field **9.2 T**, plasma current about **7.8 MA**, **525 MW** of fusion power, roughly **200 MWe** net.

Three architectural choices define it, and all three are about **maintenance and lifetime rather than plasma physics**:

1. **Demountable toroidal field magnets** — joints in the TF coils allow the entire vacuum vessel to be removed and replaced as a unit
2. **FLiBe liquid immersion blanket** — molten lithium fluoride-beryllium fluoride surrounds the vessel, acting as neutron moderator, tritium breeder, coolant and shield simultaneously
3. **REBCO high-temperature superconductors** — the enabling technology for the field strength that makes the compactness possible

**The design philosophy is explicitly conservative on plasma physics.** ARC *"enforces significant margin to disruptive operational limits"* — strict limits on edge safety factor, Greenwald density fraction, and **normalised beta kept below the no-wall limit** — on the logic that a high-field design can afford to operate well inside every stability boundary and should, because disruptions are the thing that destroys machines.

That is a genuinely different bet from the ARIES advanced-tokamak line, which sought performance by operating **near** limits with active stabilisation. ARC buys margin with magnetic field instead of with control systems.

**The commercial ARC** now being built at Chesterfield County, Virginia is larger than the 2015 paper: approximately **400 MWe from roughly 1.1 GW of fusion power**, at an expected cost **above $2.5 billion**.

**[[manta|MANTA]]** — *Modular, Adjustable, Negative-Triangularity ARC* — is the notable derivative: a high-field compact pilot plant using **[[negative-triangularity|negative triangularity]]** to avoid ELMs entirely, NASEM-compliant, with a claimed overnight cost of **$3.4 billion**.

### CFETR (China)

Explicitly designed to **bridge the gap between ITER and DEMO** — a step the Western programmes do not have.

**Phase I targets are precise and modest:** fusion power **50–200 MW**, **Q_plasma = 1–5**, **TBR > 1.0**, and neutron irradiation to about **10 dpa**. Phase II scales toward gigawatt-class fusion power.

Two things stand out. First, the **10 dpa** target — CFETR is designed partly as a materials irradiation facility, addressing in-machine what [[ifmif-dones|IFMIF-DONES]] and FPNS address ex-machine. Second, **TBR > 1.0 is a Phase I requirement**, meaning China intends to demonstrate tritium self-sufficiency in an operating machine rather than in test modules.

### [[step|STEP]] (UK)

A **spherical tokamak** prototype power plant targeting net electricity around 2040. Its distinguishing bet is that the spherical configuration's high beta compensates for the lower achievable field, giving a smaller and cheaper machine — at the cost of the centre-column problem ([[03-confinement-approaches|Document 03]]), which STEP must solve.

### K-DEMO (Korea) and JA DEMO (Japan)

Both conventional large tokamaks in the DEMO lineage, developed with strong national industrial participation. K-DEMO has been developed with US collaboration and targets a larger field than EU DEMO; JA DEMO is assessed with the TPC systems code and is coupled to Japan's revised 2030s ambition.

### The stellarator power plants (new)

- **[[infinity-two|Infinity Two]]** ([[type-one-energy|Type One Energy]]) — **350 MW**, sited with the Tennessee Valley Authority. Notable for having published a complete physics basis **including breeder blanket and tritium fuel-cycle feasibility** in the *Journal of Plasma Physics* — a level of public design detail rare for a private company
- **Stellaris** ([[proxima-fusion|Proxima Fusion]]) — the first fully integrated quasi-isodynamic stellarator power plant design optimised simultaneously for **physics and engineering feasibility**, which is the specific gap between W7-X and a plant
- **[[helios|Helios]]** ([[thea-energy|Thea Energy]]) — the planar-coil architecture scaled to a plant, and since the December 2025 preconceptual design release the **most completely specified of the three** ([[overview-of-the-helios-design]]). A two-field-period quasi-axisymmetric equilibrium, 8 m major radius, 6 T on axis, **958 MW fusion / 1,094 MW thermal / ~390 MWe net**, with 12 encircling plus **324 individually controlled planar shaping coils** at 20 T maximum on-coil. It is the only design here to publish a full [[balance-of-plant|balance-of-plant]] accounting and a tokamak-like X-point [[divertor]] in a stellarator. [[canis]] has demonstrated a nine-coil planar [[rebco]] array and static field control within 1% of prediction; [[eos]] is the planned integrated step between that component proof and Helios. Neither Canis nor the evidence in [[prototyping-test-canis-hts-planar-coil-array]] demonstrates a stellarator plasma, and Helios itself is simulation only

### The inertial fusion plant designs

Less numerous but instructive. **HYLIFE-II** was the reference US IFE plant concept, using **thick liquid jets** of molten salt to protect the chamber wall from each shot — the IFE equivalent of [[general-fusion|General Fusion]]'s liquid wall, and for the same reason. Its accident consequence analysis remains one of the few published IFE safety studies. **Xcimer's "Athena"**, whose preconceptual design DOE approved in August 2026, is the current commercial descendant.

---

## 3. The comparison that matters: design philosophy

Stripping away parameters, there are essentially **four strategies** for making a fusion plant close, and every design picks one.

| Strategy | Buy performance with... | Cost | Exemplars |
|---|---|---|---|
| **Size** | A large plasma volume at modest field | Capital cost, construction time, long schedules | ITER, EU DEMO, K-DEMO, JA DEMO |
| **Field** | B⁴ scaling via HTS magnets | HTS supply chain, magnet radiation lifetime, high heat flux in a small volume | [[sparc|SPARC]], ARC, MANTA, HH170, [[tokamak-energy|Tokamak Energy]] |
| **[[plasma-beta|Beta]]** | High plasma pressure per unit field | Centre-column shielding (spherical tokamaks); stability margin | STEP, [[st40|ST40]], ENN, FRCs, mirrors |
| **Physics performance** | Advanced scenarios, high bootstrap, active stabilisation | Control complexity, operating near limits, [[disruption]] exposure | ARIES-AT, the advanced tokamak line |

**The historical shift is from the first and fourth strategies to the second and third.** ITER and ARIES-AT represent the 1990s consensus: build big, or operate cleverly. The 2015-onward consensus is: build small and strong, and operate conservatively.

> [!note] A fifth strategy has appeared, and it is financial rather than physical
> Added 2026-10-19. **[[st-e1|ST-E1]]** buys performance with **phasing**: build a plant whose
> permanent assets — magnet cage, vacuum vessel, cryostat, civil works — are specified for the
> commercial phase from the outset, run it first as a pilot at **300–500 MWe**, then upgrade the
> replaceable in-vessel systems to reach **800–1000 MWe**
> ([[willis-2026-st-e1-pre-concept-design-overview]]).
>
> The cost is paid in **design commitment under uncertainty**: the permanent structures must be
> right for a machine whose commercial operating point (`Q_sci` 50–70, steady-state, fully
> non-inductive, neutron wall loading 2.1–2.6 MW m⁻²) depends on physics the pilot phase has not yet
> demonstrated. The stated motivation is explicitly the financing problem — limited lifetime energy
> output against high upfront cost — rather than a plasma-physics argument, which makes it the first
> design in this document whose organising principle is commercial.
>
> ST-E1 still sits in the **beta** row above as a spherical tokamak, and the §3 taxonomy holds for
> its core; the phasing is a layer over it rather than a replacement.

Whether that is right depends entirely on whether **B⁴ compactness survives contact with heat exhaust**. A machine with the same power in a smaller volume has a higher neutron wall loading and a narrower [[divertor]] strike point — which is why divertor physics ([[09-engineering-challenges|Document 09]]) is the specific place compact designs are most likely to break.

---

## 4. What every design study agrees on

Read across sixty years of design studies and a small number of conclusions recur regardless of concept or era:

1. **Tritium breeding closes, but barely.** Every design achieves TBR above 1 on paper, and every design achieves it with modest margin, sensitive to port fraction and shielding thickness. Nobody has demonstrated it.
2. **Heat exhaust is the binding physics constraint on power density.** Not confinement. Every attempt to make a machine smaller runs into the divertor before it runs into anything else.
3. **The blanket and divertor are consumables.** No design assumes plant-lifetime in-vessel components. All assume periodic remote replacement, and therefore all depend on capabilities that do not yet exist ([[29-remote-handling-and-maintenance|Document 29]]).
4. **[[recirculating-power|Recirculating power]] is 20–40% of gross output**, dominated by heating and current drive, cryogenics and coolant pumping. *The one published exception is an ignited stellarator: [[helios|Helios]] projects ~15%, because there is no current drive to pay for.*
5. **[[balance-of-plant|Balance of plant]] is 30–40% of capital cost.** The fusion-specific parts are a minority of the plant, which caps how much innovation in the core can reduce total cost ([[10-economics-and-markets|Document 10]]).
6. **Helium ash removal is always in the top five design-limiting issues** and is almost never discussed outside the studies.

---

## 5. What the design studies have historically got wrong

Worth stating, because these are the systematic biases to correct for when reading any current design:

**Materials optimism.** ARIES-AT assumed SiC/SiC composite structures that remain immature twenty-five years later. Many designs assume operating temperatures at the top of a material's window, which is where irradiation effects are worst.

**Availability optimism.** Design studies routinely assume 75–85% availability for machines whose remote maintenance has never been demonstrated. This single assumption can move LCOE by a factor of two.

**Confinement extrapolation.** Every design relies on scaling laws fitted to machines an order of magnitude smaller, extrapolated into a burning-plasma regime nobody has operated in.

**Cost.** [[10-economics-and-markets|Document 10]] documents the $1,400–43,000/kW spread in first-of-a-kind estimates. Design study costs cluster near the optimistic end, and the independent stochastic analysis (TU Berlin / DIW, arXiv:2606.26536) concludes that even mature-technology LCOE projections are *"rather optimistic when compared to other literature or comparable technologies like fission."*

**The gap from DEMO to commercial.** *Technological features of a commercial fusion power plant, and the gap from DEMO* (Fusion Eng. Des., 2023) makes the point that even a successful DEMO is not a commercial plant — it demonstrates feasibility, not economics, and the step from one to the other has its own unretired risks.

---

## 6. Assessment

**The design studies are the field's most under-read literature.** They contain the honest, integrated, quantified version of every claim made in a press release, and they have consistently identified the same binding constraints — heat exhaust, tritium margin, availability, recirculating power — for thirty years.

**The most significant change in the last decade is philosophical, not technical.** The field has moved from *buy performance with size or with clever physics* to *buy margin with magnetic field and operate conservatively*. ARC's explicit choice to sit below the no-wall beta limit, inside the Greenwald fraction, and above the safety-factor limit is a bet that **the thing that kills a fusion plant is not insufficient performance but a disruption, an unavailable divertor, or a failed weld.**

On the evidence in this dossier — where every documented major failure has been manufacturing, politics or diagnostics, and none has been insufficient plasma performance — that appears to be the right bet.


## Evidence in `raw/`

Primary sources held in this vault that evidence the claims above:

- [[arc-compact-high-field-demonstration-power-plant]]
- [[overview-of-the-helios-design]]

---

**Continue to:** [[31-plasma-physics-deeper-cuts|31 — Plasma Physics: The Deeper Cuts]] · [[33-safety-environment-decommissioning|33 — Safety, Environment and Decommissioning]] · [[10-economics-and-markets|10 — Economics and Markets]]
