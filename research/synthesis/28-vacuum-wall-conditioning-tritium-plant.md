---
title: "Vacuum, Wall Conditioning and the Tritium Plant"
type: synthesis
doc: 28
part: 3
aliases:
  - "Vacuum, Wall Conditioning and the Tritium Plant"
tags:
  - fusion/synthesis
  - fusion/engineering
  - fusion/subsystems
created: 2026-08-25
updated: 2026-11-02
status: stable
confidence: high
related:
  - "[[09-engineering-challenges]]"
  - "[[25-failure-case-studies]]"
  - "[[29-remote-handling-and-maintenance]]"
  - "[[30-power-plant-designs-compared]]"
  - "[[direct-internal-recycling]]"
  - "[[tritium-accountancy]]"
  - "[[tritium-start-up-inventory]]"
  - "[[tritium-burn-fraction]]"
  - "[[st-e1]]"
---
# 28 — Vacuum, Wall Conditioning and the Tritium Plant

*Project Lux · The plumbing. Nothing works without it and nobody writes about it.*

---

## 1. Why the wall is a component of the plasma

A fusion plasma is not an isolated system. It sits inside a metal box, and that box is in continuous chemical and physical exchange with it: adsorbing fuel, releasing impurities, eroding, redepositing. A [[tokamak]]'s performance on any given day depends substantially on **what the wall did last week**.

The numbers make the sensitivity clear. **A core tungsten concentration above roughly 10⁻⁵ radiates enough power to [[quench]] the plasma.** Oxygen at the parts-per-thousand level in the residual gas can prevent breakdown entirely. So a machine whose vessel is nominally clean can still be unusable.

Managing that is **wall conditioning**, and it is one of the least-documented and most operationally decisive disciplines in fusion.

---

## 2. Vacuum

### The requirement
A tokamak torus operates at a base pressure around **10⁻⁶ Pa** — roughly a hundred-billionth of atmospheric — inside a vessel with an enormous internal surface area, hundreds of penetrations, and metres of weld seam. [[iter|ITER]]'s cryostat, the outer vacuum boundary, is **the largest stainless steel vacuum chamber ever built** at 30 m × 30 m and about 3,850 tonnes.

### Why this is hard at scale
- **Outgassing.** Every internal surface releases adsorbed water, hydrocarbons and gases continuously. Surface area, not volume, sets the pumping requirement — and a tokamak's interior is a labyrinth of tiles, gaps and diagnostic ducts, all of which are surface.
- **Leak detection.** Finding a leak of order 10⁻¹⁰ Pa·m³/s somewhere in a structure the size of a building is a specialised art. ITER's helium leak testing found the thermal shield cracks described in [[25-failure-case-studies|Document 25]] — three panels out of nearly five hundred.
- **Materials selection.** Everything inside must be vacuum-compatible: no organics, no cadmium or zinc plating, no trapped volumes. This constrains every design choice, including fastener selection.
- **Baking.** The vessel is heated — ITER to 200 °C, higher for in-vessel components — to accelerate desorption. Baking a 5,000-tonne structure uniformly is an engineering problem in itself.

### Pumping
Turbomolecular pumps handle rough vacuum. High vacuum and — critically — **high throughput during a pulse** is handled by **cryopumps**: cryoadsorption panels at 4 K that freeze gas onto their surfaces. ITER has **six torus cryopumps plus two on the cryostat**, and they consume **15% of the cryogenic power** on their own.

Cryopumps must be **regenerated** — warmed to release trapped gas. In a D-T machine that gas is tritium-bearing, so regeneration is not a vacuum operation but a **fuel-cycle operation**. Pumping, fuelling and tritium processing are one coupled system, and the design of a reactor's pumping determines the size of its tritium inventory.

**Compound cryopumps** — combining condensation for most species with adsorption on charcoal for helium, which will not freeze at 4 K — are the reactor-relevant technology, and helium is precisely what must be pumped (see §5).

---

## 3. Wall conditioning

### The toolkit

**Baking** removes weakly bound water and hydrocarbons.

**Glow discharge cleaning (GDC)** — strike a low-density DC glow discharge in helium or hydrogen at ~1 Pa, using the vessel as the cathode. Ions bombard the entire wall at modest energy, sputtering off contaminants. Standard practice on every tokamak; unusable while superconducting magnets are energised, because the field constrains the discharge.

**Ion cyclotron wall conditioning (ICWC)** — an RF-driven discharge that *does* work with the magnetic field on, which is why it matters for superconducting machines that cannot de-energise between shots.

**Lithium conditioning** — evaporating or dropping lithium onto plasma-facing surfaces. Lithium getters oxygen aggressively and dramatically reduces recycling. Used extensively on NSTX and LTX.

### Boronization

The workhorse. **Deposit a thin film of boron on the vessel walls** to reduce impurity content — principally oxygen — in the vacuum.

**Mechanism:** boron is low-Z, so any that enters the plasma radiates weakly. It **getters oxygen** chemically, **suppresses metallic impurity influx** by forming a protective coating, and **reduces carbon contamination** by mitigating chemical erosion.

**Method:** chemical vapour deposition of elemental boron by **glow discharge in a helium atmosphere containing boron hydrides**. Common precursors: **diborane (B₂H₆), trimethylboron, decaborane (B₁₀H₁₄)**, and vapours of **carborane (C₂B₁₀H₁₂)**.

**A recent variant worth noting: Inter-Shot Boronization (ISB).** Requiring only basic vacuum hardware, ISB injects carborane **between plasma discharges** for continuous in-situ conditioning. Results on **[[globus-m2|Globus-M2]]** show it outperforming conventional glow discharge boronization and permitting longer experimental sessions — an operationally significant result for machines that cannot afford to stop for conditioning.

Related techniques: **siliconization** (demonstrated on HL-2A) and other low-Z coatings.

---

## 4. ITER's boronization system — a case study in second-order consequences

This is worth setting out in full, because it is a clean illustration of how one design decision propagates through an entire plant.

### The cause
**In 2023, ITER changed the plasma chamber's armour tiles from [[beryllium]] to tungsten.**

Beryllium is low-Z and getters oxygen naturally — it was, in effect, a permanently self-conditioning wall. Tungsten is high-Z, does not getter, and radiates catastrophically if it enters the core. **Removing beryllium removed ITER's built-in oxygen control**, which increased impurities and created a requirement for a conditioning system that the original design did not have.

### The system
| | |
|---|---|
| Boron layer thickness | **10–100 nanometres** across all plasma-facing surfaces |
| Precursor | **Diborane at 5% concentration in a helium carrier** |
| Injection lines in the Tokamak Building | **over 1 kilometre** |
| Injection lines inside the vessel | **approximately 400 metres** |
| Gas injection points | **21**, optimised and integrated into the vacuum vessel |
| Deposition method | **Glow-discharge-assisted** — a current between the wall (cathode) and "glow anodes" creates a cold plasma that accelerates ions against the wall |
| Anodes | **Four additional anodes** added to achieve even boron distribution, after modelling and international tokamak testing |
| Effective lifetime | **2.5 to 12.5 weeks** per application |
| Planned interval | **maximum every two weeks** |
| Installation begins | **2028** |

### The diborane problem
Diborane is toxic, pyrophoric, and expensive. Non-decomposed diborane must be **destroyed safely**, by either:
- **Thermal breakdown at 700 °C** — tested at [[west|WEST]] and [[diii-d|DIII-D]]
- **Chemical trapping** — proven at [[asdex-upgrade|ASDEX Upgrade]]

The treatment infrastructure will occupy space **in the Tritium Building**, which is itself a constrained and expensive volume.

### The stated challenges
- Testing ITER's high-energy anode design, which delivers **ten times more energy than current tokamaks**, for compatibility with frequent boronization cycles
- Determining optimal anode placement for even coverage
- Measuring the **oxygen absorption capacity** of boronized surfaces
- **Operating in a tritiated environment at unprecedented scale**

### Why it belongs in a dossier
A materials decision made for [[divertor]] lifetime reasons in 2023 produced, by 2026, a requirement for a kilometre of new gas lines, 21 vessel penetrations, a toxic-gas destruction plant in the Tritium Building, and a fortnightly operational procedure — **on a machine that has not yet made a plasma.**

That is what "systems integration" means in practice, and it is why [[09-engineering-challenges|Document 09]] ranks integration as a first-class challenge. No component decision in a fusion plant is local.

---

## 5. [[helium-ash|Helium ash]] — the exhaust nobody plans for

The D-T reaction produces helium. That helium thermalises in the plasma and, unlike the neutron, **stays there**.

### Why it matters
Helium is not a contaminant in the ordinary sense — it is chemically inert and low-Z, so it radiates little. Its problem is **dilution**: every helium nucleus displaces fuel. Since fusion power scales as the square of fuel density, a few percent helium is a direct multiplicative penalty on power output.

The published framing is unambiguous: control of helium ash is *"one of the key issues affecting the performance and achievable burn time of a fusion reactor"*, and *"it will be mandatory to keep the concentration of helium ash within tolerable values, in order to avoid fuel dilution and achieve stationary burning."*

There is a second-order consequence that connects directly to the tritium problem: **the helium fraction limits the maximum achievable tritium burn efficiency**, because ash dilution in the core caps fusion performance per unit of fuel circulated. Poor ash removal means more tritium circulating for the same power, which means larger tritium inventory, which means higher cost and a tighter safety case.

### How it is removed
**The only significant pathway for thermalised helium to leave the vessel is pumping at the divertor.** Helium must diffuse from the core to the edge, cross the separatrix, travel down the scrape-off layer to the divertor, and be captured by the cryopumps before it recycles back into the plasma.

That chain has several weak links, and helium is a difficult gas to pump — it does not condense at 4 K, requiring **charcoal adsorption panels** in compound cryopumps.

Approaches under study: **selective helium pumping** (exploiting differences in pumping speed between helium and hydrogen isotopes), divertor geometry optimised for helium compression, and **pellet-based impurity capture** — injecting small pellets through the plasma edge to capture and carry out helium and other impurities.

[[jet|JET]] performed dedicated helium exhaust experiments with Type-I ELMs in [[h-mode|H-mode]], and SOLPS-ITER modelling of helium transport, recycling and pumping has been carried out for ASDEX Upgrade. **It remains an open reactor-design question**, and it is one of the "critical physics areas" the ARIES studies list alongside MHD stability and heat exhaust.

---

## 6. The tritium plant

The fuel cycle described conceptually in [[09-engineering-challenges|Document 09]] is, physically, a chemical plant. Here is what it actually contains.

### The loop
```
Torus exhaust (D, T, He, impurities, tritiated water and methane)
   → Tritium Exhaust Processing (recover all hydrogen isotopes, destroy tritiated compounds)
      → Isotope Separation System (separate H / D / T)
         → Storage and Delivery (metal hydride getter beds)
            → Fuelling (gas puff, pellet injection)
               → back to the torus
```
With side streams: **water detritiation**, **atmosphere detritiation**, **breeder blanket tritium extraction**, and **[[tritium-accountancy|accountancy]]** at every node.

> [!warning] "Accountancy at every node" was the thinnest phrase in this document
> It is now a page. Added 2026-10-19: accountancy is a **measurement discipline** built on material
> balance areas, key measurement points and an inventory-difference uncertainty budget — and fusion
> breaks it three ways. **A power plant cannot stop for a physical inventory**, and continuous-flow
> measurement uncertainty grows as **√t** until it dominates the balance. **Retained tritium is a
> residual rather than a measurement**, so every error elsewhere lands on it. And **the two
> fusion-specific terms — burn-up in the plasma and breeding in the blanket — have no measurement
> method at all**, which the source literature says *"would need to be developed"*.
>
> See [[tritium-accountancy]], [[srnl-2013-tritium-accountancy-in-fusion-systems]] and
> [[sindelar-2023-tritium-accountancy-control-challenges-fusion]].

### The key technologies

**PERMCAT** — the process chosen for the **final clean-up stage of ITER's Tritium Exhaust Processing**. It directly combines a **palladium/silver membrane with a catalyst bed**, detritiating gas mixtures that contain both molecular tritium *and* chemically bound tritium — tritiated water and tritiated methane, which are the hard cases. The catalyst cracks the compound; the Pd/Ag membrane, which is permeable to hydrogen isotopes and essentially nothing else, extracts the released tritium.

**Palladium membranes** appear throughout: permeation, membrane reaction, and catalytic-reaction-plus-permeation are all listed among ITER tritium plant subsystem technologies, alongside electrolysis and decomposition reactions.

**Cryogenic distillation (CD)** — the isotope separation workhorse. Hydrogen isotopologues (H₂, HD, D₂, HT, DT, T₂) have slightly different boiling points near 20 K, so a cryogenic distillation cascade separates them. It is *"currently the only readily deployable technology at this scale."*

**Water detritiation** — the standard configuration is **LPCE + CD**: liquid-phase catalytic exchange transfers tritium from water to elemental hydrogen, then cryogenic distillation separates the isotopes. All current large-scale systems use this front-end-then-cascade architecture.

**Blanket tritium extraction** — a distinct problem, because tritium bred in a lithium blanket is dilute, distributed and hot. **Zeolite membranes and palladium membrane reactors** have been proposed for extraction from ITER and DEMO breeder blankets.

**Storage** — metal hydride getter beds (uranium or ZrCo), which absorb tritium reversibly and hold it as a solid rather than a pressurised gas.

### Where the research frontier is
Not throughput — **inventory**. The next generation of work targets **low-tritium-inventory isotope separation technologies for future power plants**.

The reason is that every gram of tritium sitting in a distillation column, a getter bed or a pipe run is a gram that is not in the plasma, that costs $30,000–35,000, that decays at 5.5% per year, and that appears in the plant's safety case as a potential release. **Reducing holdup is worth more than increasing throughput**, and it is why **[[direct-internal-recycling|Direct Internal Recycling]]** — bypassing full isotope separation for the bulk of the exhaust — is a DOE roadmap milestone.

### The quantities, added 2026-10-19

[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency|Abdou *et al.* 2021]] puts numbers on everything this section describes qualitatively:

- **Processing time is a hard requirement, not a performance metric.** The inner fuel cycle must turn exhaust around in **1–4 h**. Longer makes self-sufficiency impossible below 1% `η_f · f_b`, and **the isotope separation system dominates that time** — which is precisely why DIR, which skips it, buys so much.
- **DIR's effect is quantified.** At `η_f · f_b` = 1%, recycling **80%** of exhaust directly lowers required [[tritium-breeding-ratio|TBR]] from **1.120 to 1.075**.
- **Batch-to-continuous is the named R&D direction** for cutting processing time.
- **Reserve inventory is a reliability problem.** A 24 h reserve gives unacceptable inventories; reserves must cover **only a few hours**, which means every component in the fuel cycle needs high reliability and fast maintainability. §8's claim that these systems are "where operating cost and availability actually live" is strengthened: they are also where *fuel supply* lives.

> [!warning] The loss assumptions under all of this are weakly grounded
> Both fuel-cycle models in the vault assume very low environmental tritium losses, and neither
> validates the assumption. Abdou *et al.* set losses to **10⁻⁴** — stating in the paper that the
> value is chosen *arbitrarily* — and assign **zero** direct environmental loss to the blanket,
> plasma-facing components, storage and fuelling, on the grounds that they sit inside the vacuum
> vessel. The [[yang-2026-st-e1-tritium-tmap8-surrogate-models|ST-E1 modelling]] uses per-component
> fractions of **10⁻⁸ to 10⁻⁷** with zero for the rest, taken from
> [[tokamak-energy|Tokamak Energy]].
>
> Given that §6 opens by noting tritium *permeates through hot metal, into coolant, into concrete*,
> the gap between that physical picture and a 10⁻⁴ arbitrary loss term is the single least-tested
> assumption in fusion fuel-cycle modelling. The vault records it as an open assumption, not as an
> error — no operating plant exists to measure against.

### Retention and recovery: one modelled case

The [[st-e1|ST-E1]] study is the vault's only component-level tritium retention modelling. On its own conservative assumptions, **bake-out works**: heating an 8 mm tungsten-armour divertor to 873 K released **over 95% of retained tritium in about 33 h**. Component inventories reached quasi-steady state after roughly 10,000 s.

Both figures are from an **unreviewed preprint** that excludes re-emission and irradiation damage and models a single trap per material in 1D — so they indicate feasibility of the *approach*, not a recovery guarantee. Bake-out as a tritium-recovery operation, rather than a vacuum one, is the point worth carrying forward: it is the same coupling §2 identifies for cryopump regeneration.

---

### A second fully quantified fuel cycle, added 2026-11-02

Reading [[st-e1-tritium-systems-crossref-metadata-2026|ST-E1's fuel-cycle paper]] in full gives
this document its second end-to-end set of plant fuel-cycle numbers after Helios:

| Quantity | ST-E1 |
|---|---|
| [[tritium-start-up-inventory\|Start-up inventory]] | **1.58 kg** (incl. 20% commissioning contingency); 1.31 kg tritium-lean |
| [[tritium-doubling-time\|Doubling time]] | **152 days** |
| Operational inventory | 2.4 kg, reached in 85 days; 24 h reserve |
| Total inventory excl. storage | **1.39 kg** at 2% burn efficiency; 2.42 kg at 1% |
| Largest single holdup | Isotope separation, **0.41 kg**; blanket **0.31 kg** |
| [[direct-internal-recycling\|DIR]] | fraction 0.7; protium 1 at% in / 0.8 at% out |
| Extraction | TES, 1% efficient below ~100 ppb rising to 80% above ~1 ppm; 20% bleed |
| Cryogenic distillation | 5 cm per stage, max 70 stages, 3.5 m; 12 stages suffice at 50% DIR |

Two details are worth keeping. The **extraction efficiency is concentration-dependent** by two
orders of magnitude, which makes blanket tritium concentration a design variable rather than a
consequence — and it is the quantity nobody can measure (§7). And the blanket loop is
**360,000 kg of lithium flowing at 296 kg s⁻¹**, so a 0.31 kg blanket inventory is a sub-ppm
concentration in a very large mass.

> [!warning] Every figure above omits trapping
> [[meschini-2025-trapping-tritium-self-sufficiency|Meschini *et al.* 2025]] raise doubling time
> **+50%**, start-up inventory **+30%** and required [[tritium-breeding-ratio|TBR]] **+2–5%** once
> [[tritium-retention|trapping]] is modelled — and put first-wall and vacuum-vessel inventory up a
> factor of **10³–10⁴** for an ARC-class plant. ST-E1 assigns its first wall and divertor
> 0.012–0.024 kg. The two models are not comparable and **no source reconciles them**; the
> discrepancy is the largest open quantitative question in this section.

## 7. Accountancy — the measurement discipline

Relocated here 2026-10-19 from [[tritium-accountancy]], which holds the framework; this section
holds the detail that a concept page cannot carry at schema length.

### What can actually be measured

Practical accuracies, compiled in 2023 **from Nishi *et al.*, *Fusion Engineering and Design* 81
(2006) 745–751** — and therefore twenty-year-old instrument figures, reaching this vault at second
hand ([[sindelar-2023-tritium-accountancy-control-challenges-fusion]]):

| Method | Practical accuracy |
|---|---|
| Laser Raman spectrometry (concentration) | **< 0.5%** — the best listed |
| Calorimetry, integrated | ~1% |
| Static PVTC (pressure, volume, temperature, concentration) | 1–5% integrated |
| — pressure · volume · temperature | 0.2–0.9% · < 0.5% · 0.1 °C |
| Dynamic PVTC — accountancy with mass flowing | a few % integrated |
| Mass spectrometry (concentration) | 0.5–5% |
| Gas chromatograph · Bremsstrahlung X-ray | few to 5% · a few % |
| Ionisation chamber (concentration) | few to 10% |
| **Releases to the environment** | **~10%** |

Static inventories live in **metal hydride beds**, **molecular sieve beds** and **sealed confinement
vessels**; losses are detected by **inventory-difference control limits** and **statistical sampling
plans**.

> [!warning] The two measurements fusion most needs do not exist
> The table's own note: methods *"using neutron flux for tritium consumption by the fusion reaction
> and for tritium production in the blanket **would need to be developed**."*
>
> Everything above measures tritium **in a pipe or a bed**. Nothing measures tritium being *made* in
> a blanket or *consumed* in a plasma — which are precisely the two terms the fusion-modified balance
> adds. See [[tritium-accountancy]].

### Who is building the missing instruments

One programme, at [[ukaea|UKAEA]]'s Tritium Fuel Cycle division with [[librti|LIBRTI]]
([[thalia-hera-ukaea-tritium-accountancy-2026]]):

- **HERA** — real-time analysis of **gas streams** by mass spectrometry and Raman, quantifying
  H₂, D₂ and T₂ from the limit of detection to 100%, with a **palladium catalyst** for
  semi-quantification of HD, HT and DT, and a glovebox generating its own calibration standards by
  PVTc. This attacks the continuous-flow problem directly, using the table's two best methods.
- **THALIA** — accountancy for tritium **trapped in liquid breeders**: FLiBe first, then liquid
  lithium and [[lithium-lead-eutectic|LiPb]]. Sub-projects **ERATO** (liquid scintillation counting
  of tritiated lithium salts) and **CLIO** (ICP-MS, *"not been developed for small atoms such as
  hydrogen"*).

**Both are at low technology readiness level**, principally because getting a tritiated lithium
matrix into an analysable state is hard, and because **tritium speciation in the breeder is
unknown**. [[st-e1|ST-E1]] breeds in liquid lithium — THALIA's *third* target material.

Underneath all spectroscopic methods sits reference data, and that too is thin: experimentally
verified tritium material properties are *"sparse"*, which is the gap
[[marsteller-2025-t2apir-first-results|T2ApIR]] at Tritium Laboratory Karlsruhe exists to close — a
cryogenic cell below 10 K with infrared, Raman and polariscope access, currently in commissioning
with no property data published.

### Scale, and a distinction worth keeping

[[iter|ITER]]'s total **in-process** inventory is expected at approximately **1 kg**, with commercial
plants put at several hundred grams to 1 kg each across *"hundreds to thousands"* of plants at global
scale (2023 estimates). **In-process inventory is not
[[tritium-start-up-inventory|start-up inventory]]** — the same units, different quantities.

Steady state is not reached until permeation and hold-up losses have saturated, which is
plant-specific: **early-life accountancy measures a system still filling its own walls.**

---

## 8. Assessment

**This document covers the systems that determine whether a fusion machine can be *operated*, as distinct from whether it can be *built*.** They share three characteristics:

1. **They are invisible in fusion communications.** No press release has ever led with a boronization system.
2. **They are coupled to everything.** ITER's tungsten decision created a boronization requirement that consumes space in the Tritium Building. Cryopump regeneration is a fuel-cycle operation. Helium ash removal sets tritium inventory.
3. **They are where operating cost and availability actually live.** A fortnightly boronization is a fortnightly outage window. Poor helium exhaust is a permanent power penalty. Tritium holdup is a permanent capital charge.

The most useful generalisation: **fusion's plasma physics is a science problem, its materials are a research problem, and its vacuum, conditioning and fuel handling are an operations problem** — and operations problems are the ones that determine whether a plant runs 90% of the year or 50%.

---

**Continue to:** [[29-remote-handling-and-maintenance|29 — Remote Handling and Maintenance]] · [[30-power-plant-designs-compared|30 — Power Plant Designs Compared]] · [[09-engineering-challenges|09 — Engineering Challenges]]
