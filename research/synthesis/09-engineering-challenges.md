---
title: "Engineering Challenges"
type: synthesis
doc: 09
part: 1
aliases:
  - "Engineering Challenges"
tags:
  - fusion/synthesis
  - fusion/engineering
created: 2026-08-25
updated: 2026-10-19
status: stable
confidence: high
related:
  - "[[10-economics-and-markets]]"
  - "[[11-policy-regulation-safety]]"
  - "[[14-open-problems-and-risks]]"
  - "[[tritium-breeding-ratio]]"
  - "[[tritium-burn-fraction]]"
  - "[[tritium-start-up-inventory]]"
  - "[[direct-internal-recycling]]"
  - "[[availability]]"
---
# 09 — Engineering Challenges

*Project Lux · The problems that will actually decide whether fusion becomes an energy source*

---

## Framing

The plasma physics community has spent seventy years answering one question: *can a plasma be made to release net fusion energy?* The answer, as of December 2022, is yes.

Everything in this document is the answer to a different question: *can a machine be built around such a plasma that survives, refuels itself, and pays for itself?* None of these problems is solved. Several have never been tested at any scale.

The fusion companies themselves agree. Asked to name their long-term challenges, the 44 respondents to the FIA's 2026 survey ranked **neutron-resilient materials (25 mentions)** and **tritium self-sufficiency (23)** at the top, with **plasma science at 7**. The industry has largely stopped worrying about plasmas and started worrying about metal.

---

## 1. The 14.1 MeV neutron — the root of most other problems

Every problem in this document descends from a single fact: **80% of D-T fusion energy leaves the plasma as a 14.1 MeV neutron**, and that neutron is unlike anything the nuclear industry has dealt with before.

Fission neutrons average about 2 MeV. A 14.1 MeV neutron is different in kind, not degree, for one reason: it is above the threshold for **(n,α) and (n,p) transmutation reactions** in structural metals, which sit around 3 MeV.

### Displacement damage

A fast neutron knocks an atom out of its lattice site, which knocks out others in a cascade. The cumulative measure is **[[displacements-per-atom|displacements per atom (dpa)]]**.

| Environment | dpa |
|---|---|
| [[iter|ITER]], entire operational life | **< 2 dpa** |
| Fusion power plant first wall | **~15 dpa per year** |
| Target for a 5-year component life | **~70–100 dpa** |
| [[ifmif-dones|IFMIF-DONES]] phase 1 / phase 2 | ~20 / ~50 dpa |

### Gas production — the part fission data cannot cover

The transmutation reactions produce **helium and hydrogen inside the metal**. Helium is insoluble; it migrates to grain boundaries and forms bubbles.

The critical ratio is **helium appm per dpa**:

- **Fission spectrum: ~0.1–1 appm He/dpa**
- **Fusion spectrum: ~10–15 appm He/dpa**

An order of magnitude more helium for the same displacement damage. The consequences are:

- **High-temperature [[helium-embrittlement|helium embrittlement]]** — grain-boundary bubbles cause intergranular fracture with essentially no ductility
- **Void swelling** — helium stabilises voids, causing dimensional change of several percent
- **Shift in ductile-to-brittle transition temperature (DBTT)** — steels that are ductile at room temperature become brittle, sometimes by hundreds of degrees

**This is why fission irradiation data cannot qualify fusion materials**, and why the field's most important missing facility is a fusion-spectrum neutron source.

### Activation

Neutron capture makes the entire structure radioactive. The mitigation is **elemental**: design alloys from elements whose [[activation-products|activation products]] are short-lived. This is the origin of **reduced-activation** materials — replacing molybdenum with tungsten, niobium with tantalum, and eliminating nickel, cobalt and copper wherever possible.

Done well, the result is a structure that decays to hands-on or recyclable levels in **50–100 years** rather than the geological timescales of fission waste. See [[11-policy-regulation-safety|Document 11]].

---

## 2. Structural materials

### The candidates

| Material | Operating window | Status |
|---|---|---|
| **RAFM steels** — EUROFER-97 (EU), F82H (Japan), CLAM (China) | ~350–550 °C | **The baseline.** Best-characterised. Reduced-activation ferritic-martensitic |
| **ODS steels** (oxide-dispersion-strengthened) | up to ~650 °C | Higher temperature = higher thermal efficiency. Nano-oxide dispersions also trap helium. Hard to manufacture and join |
| **Vanadium alloys** (V-4Cr-4Ti) | ~400–700 °C | Excellent thermal and low-activation properties; compatible with liquid lithium. Extremely oxygen-sensitive. **DOE targets 500 kg domestic heats** |
| **SiC/SiC composites** | >1000 °C | Very low activation, very high temperature. Immature; joining, hermeticity and irradiation stability unresolved |
| **Tungsten** | plasma-facing only | Not structural — see §4 |

The RAFM operating window is narrow and both ends are set by irradiation: below ~350 °C, irradiation hardening and embrittlement dominate; above ~550 °C, thermal creep and helium embrittlement take over. **Every degree of that window is worth money**, because thermal-cycle efficiency scales with coolant outlet temperature.

### What the roadmap actually asks for

The DOE roadmap's near-, mid- and long-term milestones for Challenge Area A are unusually concrete:

- **Near (2–3 yr):** accelerated qualification pathways for Fe- and V-alloys with full datasets within four years; a centralised AI/HPC materials data strategy; **domestic industrial heats of multi-tonne Fe-alloy and 500 kg V-alloy**; corrosion loops and a high-heat-flux facility
- **Mid (3–5 yr):** complete irradiation campaigns and post-irradiation examination to **~10 dpa**; **quantify helium-assisted embrittlement thresholds** and high-temperature creep-fatigue limits; integrated tritium retention and permeation datasets
- **Long (5–10 yr):** component-relevant performance under fusion-prototypic neutron, heat and tritium loads simultaneously; **codify fusion-specific requirements into ASME-based standards**; qualify domestic manufacture of thick sections and additive builds

Note the last item in the mid-term list and the first in the long-term list. **10 dpa is where the mid-term ends.** A power plant needs 70–100. The roadmap is candid that the near-term programme gets nowhere near power-plant conditions.

### The missing facility

There is **no operating fusion-spectrum neutron source anywhere in the world.**

- **IFMIF-DONES** (Granada, Spain) — a 40 MeV, 125 mA deuteron beam striking a flowing lithium jet, producing neutrons by Li(d,xn) stripping with a spectrum approximating D-T. Phase 1 targets ~20 dpa, phase 2 ~50 dpa. Under construction; the design has evolved from the original IFMIF via EVEDA.
- **FPNS** (US Fusion Prototypical Neutron Source) — placed in the DOE roadmap's **mid-term (3–5 year)** construction window, i.e. not operating before the early 2030s.
- **Surrogates in the interim** — spallation sources (SNS, ISIS), fission reactors (HFIR, BOR-60, ATR) with helium implantation to mimic the gas ratio, and ion-beam irradiation for rapid screening. All are approximations; none reproduces the combination of dpa rate, He/dpa ratio and spectrum.
- **Commercial neutron sources are emerging as a stopgap.** **[[astral-systems|Astral Systems]]** (Bristol) now sells continuous DD and DT irradiation services and has run hundreds of hours of commercial campaigns on tritium breeder materials including solid lithium, FLiBe and composite breeders. **[[avalanche-energy|Avalanche Energy]]** is building **FusionWERX** as a commercial fusion test facility. This is a genuinely useful market response to a public-infrastructure gap.

**The timing problem is stark.** Companies plan pilot plants for the early-to-mid 2030s. The facility that would qualify those plants' materials will begin producing meaningful data in roughly the same period. Every pilot plant will therefore be built on **extrapolated and surrogate data**, and will itself function as the materials experiment.

---

## 3. Tritium and the fuel cycle

### The arithmetic

For a plant producing **1 GW of fusion power**:

```
1 GW / 17.6 MeV per reaction = 3.55 × 10²⁰ reactions/second
→ tritium consumption ≈ 0.18 g/minute ≈ 152 g/day ≈ 55.6 kg/year
```

Against that:

- **Total world civilian tritium inventory: 30–40 kg** projected over the next decade
- **CANDU production: under 0.13 kg per reactor per year**; global supply a few kg/year
- **Market price: $30,000–35,000 per gram** — so a 5 kg start-up inventory costs **$150–175 million in fuel alone**
- **Half-life: 12.3 years** — the inventory decays at 5.5% per year whether used or not

**A single plant would consume more than the world's entire inventory in its first year.** There is no scenario in which fusion runs on purchased tritium. Breeding is not an optimisation; it is the precondition for the technology existing at all.

### Breeding

```
n + ⁶Li → T + ⁴He + 4.8 MeV      (exothermic; large cross-section at low neutron energy)
n + ⁷Li → T + ⁴He + n − 2.5 MeV  (endothermic; threshold ~2.5 MeV, but regenerates the neutron)
```

Every D-T neutron must, on average, produce **more than one** tritium atom to sustain the cycle — the **[[tritium-breeding-ratio|tritium breeding ratio (TBR)]]**. But each fusion reaction produces exactly one neutron, and neutrons are lost to structure, ports, diagnostics and heating penetrations. So breeding above unity requires **neutron multiplication**:

```
⁹Be + n → 2n + 2⁴He        or        ²⁰⁸Pb + n → 2n + ²⁰⁷Pb
```

Beryllium is the better multiplier and is toxic, scarce and itself becomes activated. Lead is abundant and less effective. Most blanket designs use one or the other.

**Required TBR:** physically above 1.0; in practice designs target **1.05–1.15** to cover losses, decay and the surplus needed to start the *next* plant. **DOE's roadmap sets TBR > 1.1**, both as a near-term FPP-scale target and as the long-term TRL-7 integrated demonstration.

That band is not merely a design convention. [[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency|Abdou *et al.* 2021]] — the primary source, added to the vault on 2026-10-19 — frames it as a confidence boundary: self-sufficiency is **unlikely** above 1.15, **possible** between 1.05 and 1.15, and **attained with high confidence** only at or below 1.05. The **maximum achievable** TBR for the most detailed blanket designs is estimated at **1.15**. Requirement and capability therefore occupy the same interval, and integral experiments found calculation **overestimates** tritium production by an average factor of **1.14** — a bias in the wrong direction, larger than the margin. See [[tritium-breeding-ratio]].

### Blanket concepts

| Concept | Breeder | Coolant | Multiplier | Champion |
|---|---|---|---|---|
| **HCPB** | Li₄SiO₄ / Li₂TiO₃ pebbles | Helium | Beryllium pebbles | EU (DEMO), KIT |
| **WCLL** | Liquid PbLi | Water | Lead (in PbLi) | EU (DEMO) |
| **HCLL** | Liquid PbLi | Helium | Lead | EU |
| **DCLL** | Liquid PbLi | PbLi + helium | Lead | US |
| **FLiBe molten salt** | LiF-BeF₂ | FLiBe itself | Beryllium | **CFS ([[arc|ARC]])**, [[type-one-energy|Type One Energy]] |
| **Liquid lithium** | Li | Li | — | Some mirror and [[stellarator]] designs |
| **Liquid PbLi cavity** | PbLi | PbLi | Lead | **[[general-fusion|General Fusion]]** (the liquid *is* the wall) |

**The liquid-breeder attraction.** A flowing liquid breeder is simultaneously breeder, coolant and — in the immersion designs — first wall shielding. Crucially, **a liquid cannot suffer displacement damage**: there is no lattice to displace. CFS's ARC and General Fusion's MTF both make this a central architectural bet.

**The liquid-breeder problem.** A conducting fluid flowing across a strong magnetic field experiences an enormous **MHD pressure drop** — the induced currents oppose the flow. Mitigations are flow-channel inserts and electrical insulators, both of which must survive the neutron flux they exist to enable. The DOE roadmap's mid-term milestones name "MHD mitigation, flow-channel inserts/insulators, and manifold/channel designs" explicitly.

### Closing the cycle — the part nobody discusses enough

Breeding tritium is necessary but not sufficient. The tritium must be **extracted, purified, isotopically separated, stored and re-injected**, continuously, at very low loss.

The reason this is hard is **[[tritium-burn-fraction|burn fraction]]**. Only about **1–3% of injected tritium fuses per pass** through the plasma. The other 97–99% is pumped out with [[helium-ash|helium ash]] and impurities and must be recycled. So a plant burning 56 kg/year **circulates on the order of 2–5 tonnes of tritium per year** through its fuel-cycle plant.

**The precise figures are worse than that range suggests, and are the binding constraint on the whole fuel cycle.** What matters is the product of burn fraction and fuelling efficiency, `η_f · f_b`. ITER's estimate at maximum fuelling is **0.36%** — well below the 1–3% band above, which corresponds to first-DEMO *expectations* rather than any demonstrated value. Self-sufficiency requires `η_f · f_b` **> 2%**, ideally approaching **5%**, with inner-cycle processing time of **1–4 h**. At ITER's burn fraction a 3 GW plant would need TBR **1.82** and **over 200 kg** of start-up tritium; at 5% it needs TBR 1.02 and under 5 kg ([[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]).

**No blanket improvement can rescue a plant whose burn fraction is too low** — which inverts the usual framing of tritium as a breeding problem.

Sub-problems, each unsolved at scale:

- **Tritium-compatible vacuum pumping** at plant throughput
- **Direct Internal Recycling (DIR)** — returning unburned D-T straight to the fuelling system without full isotope separation, drastically cutting inventory and processing load. A DOE mid-term milestone
- **Isotope separation** with high protium removal and low holdup
- **Permeation** — tritium diffuses through hot metal. It will migrate into coolant, into concrete, into the environment. Permeation barriers are essential and must survive irradiation
- **Retention** — tritium is absorbed by plasma-facing components and by dust. Retained inventory is both a fuel loss and a safety-case limit
- **Accountancy** — regulators require knowing where every gram is, to within a small tolerance, in a system where it permeates through walls

### Start-up inventory: the fleet problem

A new plant needs a [[tritium-start-up-inventory|start-up inventory]] before it can breed anything. Estimates range from a few kilograms to over ten, depending on design and on how efficiently DIR reduces holdup.

The dependence is quantified: **11 kg** for a 3 GW plant at `η_f · f_b` = 2% and 4 h processing, falling **below 5 kg** at 5% and 1 h, and scaling **linearly with fusion power** — about **1 kg** for a 100 MW facility. A **24 h reserve** inventory is found to give unacceptable requirements, so reserves must cover only a few hours, making this a **component-reliability** problem rather than a storage one ([[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]).

**[[availability]] is also a tritium parameter**, and this is the finding with the sharpest consequence for the facilities listed below: self-sufficiency is **impossible below 10% availability** for any burn fraction, possible above 30%, and reasonably confident only above 50%. FNSF, VNS and CTF are all predicted **below 30%** — the devices expected to demonstrate breeding may be unable to close their own fuel cycle while doing so.

- **One plant** can plausibly be started from the world's existing CANDU-derived inventory
- **A fleet** cannot. It must be bootstrapped from the surplus bred by earlier plants — which introduces a **doubling time**, set by how far TBR exceeds 1 and by tritium decay

This makes the difference between TBR = 1.05 and TBR = 1.15 the difference between a fusion industry that can double every few years and one that effectively cannot grow. **It is one of the most consequential and least discussed numbers in the field.**

### What is being built about it

- **[[unity-3|UNITY-3]]** (ORNL, 2026) — **the first facility generating 14 MeV neutrons to evaluate commercial breeding blanket designs and validate tritium production.** Complements UNITY-1 (Japan) and UNITY-2 (Canada, under development), both from [[kyoto-fusioneering|Kyoto Fusioneering]].
- **[[librti|LIBRTI]]** (UK, **£220 m** over 2025/26–2029/30) — a global first-of-a-kind lithium breeding tritium facility.
- **[[h3at|H3AT]]** (UKAEA with Eni) — tritium processing and handling at plant scale.
- **ITER's Test Blanket Module programme** — six TBM concepts in equatorial ports; the first in-device breeding test ever, from 2039.
- **BABY** and similar small-scale experiments (arXiv:2412.02721 in `papers/`) — direct measurement of tritium production in small breeder volumes, establishing the measurement techniques.
- **Li-6 enrichment**: natural lithium is only **7.5% Li-6**; blankets need **30–90%**. Historic capacity is concentrated in **Russia and China** — a sovereignty exposure flagged by both industry analysts and the DOE roadmap.

---

## 4. Plasma-facing components and exhaust

### The heat flux problem

Fusion power that does not leave as neutrons leaves as charged particles and radiation, and must be exhausted. For a **500 MW** fusion plasma, roughly **100 MW** must be handled — and in a [[tokamak]], the scrape-off layer channels it onto a strike region only **millimetres wide** at the [[divertor]] target.

| | Value |
|---|---|
| Material limit, steady-state | **5–20 MW/m²** |
| Tungsten divertor design target | **< 10 MW/m²** |
| Unmitigated reactor heat flux | **~10× above the limit** |
| Required target plasma temperature | **single-digit eV** (to stay below the sputtering threshold) |

The scrape-off layer width **narrows as machines get larger and fields get stronger** (Eich scaling: λ_q roughly inversely proportional to poloidal field), so the problem worsens exactly where it matters most.

### [[detachment|Detachment]] — the only known answer

**Detachment** deliberately radiates the exhaust power away in the divertor volume before it reaches a surface, by seeding impurities (nitrogen, neon, argon) and operating at high neutral density. Plasma-neutral interactions then remove power, momentum and particles simultaneously, and the ion flux to the target collapses.

The tension is structural: **the core must be hot and clean; the divertor must be cold and dirty**, separated by perhaps a metre. Whether a detached divertor is compatible with a high-performance burning core at reactor scale is genuinely unresolved, and it is on ITER's critical question list.

### Alternative configurations

- **[[super-x-divertor|Super-X divertor]]** — lengthens the field-line connection and increases the wetted area. **[[mast-upgrade|MAST-Upgrade]] demonstrated transient heat-load control** with it (*Nature Energy*, 2025) — one of the decade's more important exhaust results
- **X-point radiator (XPR)** — a stable, strongly radiating region near the X-point. **Extended into D-T on [[jet|JET]]'s DTE3**
- **Quasi-continuous exhaust (QCE)** — a naturally small-ELM regime, also demonstrated in D-T on JET
- **[[negative-triangularity|Negative triangularity]]** — reverses the plasma cross-section curvature, suppressing the edge instabilities that drive ELMs while retaining good confinement. Explored extensively on [[diii-d|DIII-D]] and [[tcv|TCV]]; the basis of the [[manta|MANTA]] pilot-plant design study
- **Liquid metal PFCs** — lithium or tin surfaces that are continuously replenished, so erosion is irrelevant and there is no lattice to damage. DOE's long-term milestone is to "operate continuous-flow liquid walls proving stability, impurity control, and tritium recovery." Attractive; MHD control and tritium retention in the liquid are the open questions

### Tungsten's own limits

Tungsten is the consensus plasma-facing material — highest melting point of any metal, low sputtering yield, low tritium retention. It also:

- **Recrystallises above ~1300 °C**, losing strength permanently
- Has a **DBTT around 400 °C** that irradiation pushes higher — so it is brittle when cold and weak when hot, with a narrow usable band
- Is a **high-Z radiator**: even trace tungsten in the core radiates catastrophically. Core tungsten concentration must stay below roughly 10⁻⁵
- **Transmutes to rhenium and osmium** under neutron irradiation, changing its properties over life

DOE's Challenge Area B milestones accordingly cover cyclic/transient/ELM-like loading databases, erosion-redeposition and cracking limits, W/Cu-alloy mockup fatigue and creep testing, and AI-guided screening of low-erosion, low-retention alternatives.

---

## 5. Magnets

### Why HTS changed everything

Fusion power density scales as **β²B⁴**. Nb₃Sn — ITER's conductor — saturates around 12–13 T on the conductor. **REBCO tape operates above 20 T.** That single materials substitution is the reason a machine the size of JET can attempt what ITER attempts at forty times the volume.

Demonstrated milestones:
- **CFS/MIT: 20 T** on a large-bore model coil (September 2021)
- **[[wham|WHAM]]/Realta: 17 T** on a confined plasma (July 2024)
- **[[tokamak-energy|Tokamak Energy]] Demo4: 11.8 T, 7 MA-turns** in a full tokamak-configuration magnet (2026)
- **[[hh70|HH70]] ([[energy-singularity|Energy Singularity]])**: the first fully HTS tokamak, built in about two years

### The open problems

**Supply chain.** Global HTS tape capacity is roughly **10,000 km/year**. The top pulsed-laser-deposition manufacturers produce over 3,000 km-12mm each, more than half of global output, and **China holds substantial manufacturing strength**. A single high-field tokamak consumes thousands of kilometres. Scaling to a fleet requires order-of-magnitude expansion.

Responses: **[[arpa-e|ARPA-E]] SCALEUP awarded [[thea-energy|Thea Energy]] $20 M (July 2026)** for the first US modular HTS magnet production line; **CFS is selling magnets as a merchant product**, beginning with Realta (April 2026), explicitly to create the demand that justifies tape-capacity investment.

**Radiation tolerance.** REBCO's critical current degrades under fast-neutron fluence, and the epoxies and insulation degrade sooner. In a compact high-field machine the magnet sits close to the plasma with limited shielding space — most acutely in a **spherical tokamak's centre column**, where there is barely room for the conductor let alone shielding. DOE's near-term milestone is explicit: **"Conduct REBCO irradiation campaigns to define magnet performance and standards."**

**[[quench|Quench]] protection.** HTS has a very slow normal-zone propagation velocity, so a local hot spot does not spread quickly enough to be detected by conventional means before it damages the conductor. **No-insulation winding** helps by letting current bypass a defect radially, but complicates ramp dynamics. In a magnet storing gigajoules, quench detection is a safety-critical system.

**Array manufacture and control.** [[canis]] demonstrated nine planar [[rebco]] shaping coils made from 45 double pancakes and tape from three suppliers, integrated and operated at 20 K. Two static field patterns matched prediction with 0.56% and 0.60% RMS error. This retires part of the repeatability and mutual-coupling risk for small planar arrays, not the integrated [[eos|Eos]] case: the test formed no closed flux surfaces or plasma, and several transient, quench and defect-robustness tests remained future work. See [[prototyping-test-canis-hts-planar-coil-array]].

**Cryogenic load.** Nuclear heating deposits power directly into a 4–20 K magnet, and every watt at 4 K costs several hundred watts of room-temperature electrical power. This feeds straight into the [[recirculating-power|recirculating power]] fraction and therefore into Q_eng. Cryoplant heat management appears in the FIA challenge list, if modestly.

---

## 6. Remote maintenance, availability, and the thing utilities actually care about

A fusion plant is **intensely radioactive after first operation** and can never be entered by a human again. Every subsequent maintenance operation — replacing a divertor cassette, changing a blanket module, repairing a diagnostic — must be done by remote handling, through ports, in a confined, activated, tritium-contaminated space.

This drives **RAMI** — Reliability, Availability, Maintainability, Inspectability — and it is the single most likely reason a technically successful fusion plant would be commercially useless.

The arithmetic is brutal: if replacing a full set of blanket modules takes six months and must happen every two years, the plant's availability is capped at 75% before any unplanned outage. Fission plants achieve 90%+; a plant with a $6,000/kW capital cost and 50% availability has an LCOE roughly double the same plant at 90%.

DOE's Challenge Area F milestones therefore include:
- An **initial RAMI handbook** with metrics, availability targets and design-for-maintainability guidance (near term)
- **Qualified joining and cutting methods for irradiated materials** to enable modular in-vessel replacement (mid term)
- Remote handling and sensing prototypes for activated blankets and PFCs in corrosive, hazardous environments
- Validated mock-up maintenance workflows with reliability data
- Automated controls and remote operation in steady-state and high-repetition-rate facilities (long term)

**Design responses.** CFS's ARC uses **demountable joints** in the toroidal-field magnets so the entire vacuum vessel can be lifted out and replaced rather than repaired in place — treating the most-irradiated component as a consumable. General Fusion's liquid wall sidesteps the problem by having no solid first wall to replace. Mirror and linear geometries are inherently easier to service than a torus threaded through a 3D coil set — which is one of the strongest practical arguments for Realta's and Zap's architectures, and one of the strongest against stellarators.

---

## 7. Balance of plant and the recirculating power trap

Fusion plants that use a thermal cycle face conventional thermodynamics: **35–45% conversion efficiency** from a Rankine or closed Brayton cycle, set by the coolant outlet temperature, which is set by the structural material's temperature limit, which is set by irradiation behaviour. The entire chain from neutron damage to electricity price runs through that one link.

See [[balance-of-plant]] for the subsystem itself, which is **30–40% of plant capital cost** and the least-discussed majority of the machine.

Against gross electrical output, the plant must subtract **recirculating power**:

- Cryoplant for the magnets
- Plasma heating and current drive (tens to >100 MW, at 30–50% wall-plug efficiency)
- Coolant pumping (particularly severe for helium, and for liquid metals against MHD drag)
- Tritium plant, vacuum systems, controls

For a tokamak, plausible recirculating fractions are **20–40% of gross output**. This is why **Q_eng > 1 typically requires Q_sci in the 10–30+ range**, and why scientific breakeven, while a genuine milestone, is a long way from a generator.

### A worked accounting

[[helios|Helios]] is the first design in this vault to publish the whole chain end to end ([[overview-of-the-helios-design]] — a **preconceptual design**, so these are projected, not measured):

| Stage | Value |
|---|---|
| D-T fusion power in plasma | 958 MW |
| Lithium-6 breeding exotherm | +135 MW |
| Total thermal | **1,094 MW** |
| Steam superheat / turbines | 635 °C, three stages |
| Generated electric | 459.9 MWe |
| Coolant pumping | −21.8 MWe (gross 438.1 MWe) |
| Maintenance, tritium plant, cryoplant, ECRH | −48.0 MWe |
| Waste heat | 681 MW in text, 703.0 MW in the Sankey diagram |
| **Net export** | **390.1 MWe** |

Pumping plus the four auxiliary loads is 69.8 MW — the "70 MW of auxiliary power" the paper quotes elsewhere, not an additional charge on top.

### And the same accounting for a pulsed machine

[[eu-demo|EU-DEMO]]'s published balance of plant makes the contrast structural rather than numerical ([[maturation-of-critical-technologies-demo-balance-of-plant]], [[tokamak-cooling-systems-and-power-conversion-system-options]]). It needs **8–14 separated [[primary-heat-transfer-system|primary heat transfer systems]]** where a fission plant of nearly twice the thermal power needs one, because blanket, first wall, divertor and vacuum vessel all demand different fluids, pressures and temperatures — helium at 8 MPa and 300/520 °C for an HCPB blanket, water at ~1 MPa and 190/200 °C for the vacuum vessel. The cold loops cannot make useful steam and are demoted to feedwater preheating.

It must also bridge a dwell: **2 hours of burn, then ~10 minutes at 1–2% of nominal power**. Neither paper states a net cycle efficiency, so none is quoted here. What they do state is that the once-through steam generator must hold stable operation at **1% of nominal** in dwell, against industrial practice of 5% and above — an open problem, in a pre-concept design, in the part of the plant usually assumed to be mature.

Two things are worth extracting. First, self-consumption is about **15% of generated power** rather than 20–40%, because an ignited [[stellarator]] carries no current-drive load — under 1 MW of heating once burning, against tens to >100 MW for a tokamak. Second, **the efficiency figure is convention-dependent**: 40.2% net of pumping, 42.2% on total generated power, from the same plant. Quote neither bare; see [[balance-of-plant]].

**The schemes that escape this.** [[direct-energy-conversion|Direct energy conversion]] — capturing charged-particle energy electrically without a thermal cycle — bypasses the Carnot limit entirely. It is only available to configurations with an open field line or a pulsed compression:

- **Realta demonstrated DEC on WHAM on 19 June 2026** — the first commercial fusion company to convert plasma energy directly to electricity
- **Helion's** entire architecture is built on inductive recovery from an expanding compressed FRC
- Aneutronic fuels (p-¹¹B) would make this dramatically more valuable, since nearly all the energy is in charged particles

This is the strongest single argument for the non-tokamak concepts, and it is why several of them target **industrial process heat or off-grid power first** — markets where the thermal-cycle penalty does not apply.

---

## 8. Systems integration — the challenge nobody can test in isolation

Every problem above has been listed separately. In a real plant they interact, and the interactions are where first-of-a-kind projects die:

- The blanket must breed tritium **and** remove heat **and** shield the magnets **and** be replaceable remotely — and optimising any one degrades the others
- Higher coolant temperature raises efficiency **and** worsens creep and helium embrittlement
- Thicker shielding protects the magnets **and** displaces breeder volume, reducing TBR
- Impurity seeding protects the divertor **and** dilutes and cools the core
- A compact machine costs less **and** narrows the scrape-off layer and concentrates neutron flux

DOE's Challenge Area F addresses this with a standards-based **FAIR data repository**, a common **verification, validation and uncertainty quantification** framework for whole-plant modelling, AI/HPC pipelines connected to DIII-D, NSTX-U and [[mpex|MPEX]], and **modular digital-twin platforms** coupling live data, simulation and predictive diagnostics for licensed plant design.

Thea Energy's stellarator digital twin with **NVIDIA, Synopsys, Argonne and Princeton** is the clearest private-sector instance of the same idea.

---

## 9. Ranked assessment

| Rank | Challenge | Why | Best case | Realistic |
|---|---|---|---|---|
| **1** | **Neutron-tolerant materials** | No qualification facility exists; 10 dpa is the mid-term target against a 70–100 dpa need | Surrogates + AI-accelerated qualification prove adequate | Pilot plants built on extrapolated data and become the experiment |
| **2** | **Tritium breeding and fuel cycle** | Never demonstrated; TBR > 1.1 required; Li-6 supply concentrated in Russia and China | UNITY-3 / LIBRTI validate blankets this decade | One plant fuellable; a *fleet* constrained by doubling time |
| **3** | **Divertor and exhaust** | 10× above material limits; core-edge compatibility unproven at scale | Detachment + Super-X/XPR scale; or liquid metals work | Solved case-by-case; caps machine power density |
| **4** | **Capital cost and FOAK risk** | $1,400–43,000/kW spread; nobody has built one | Modular, factory-built plants drive learning curves | First plants heavily subsidised or sold at premium to hyperscalers |
| **5** | **Availability and remote maintenance** | Determines whether a working plant is economic | Demountable / replaceable architectures work | The reason first plants underperform their business case |
| **6** | **HTS supply chain** | ~10,000 km/yr global; concentrated | Capacity scales like solar did | A cost and schedule constraint, not a blocker |
| **7** | **Plasma physics** | Largely conceded; Q > 1 imminent | [[sparc|SPARC]] exceeds Q = 1 comfortably in 2027 | Fine, with residual [[disruption]] and burn-control risk |

The ordering matters. **Fusion's remaining risk is concentrated in nuclear engineering and project economics, not in plasma physics** — and the field's public communication still, largely, has this backwards.


## Waste volume as an engineering consequence

The consumable-component problem has a disposal tail. Because first wall, divertor and breeding
blanket are replaced on a schedule, every replacement set becomes waste, and a fusion power core is
a large thin-walled structure to begin with. [[43-fusion-waste-classification-and-disposal]] sets out the consequence: fusion trades
waste *intensity* for waste *volume*, and the disposal class is fixed at procurement by impurity
control rather than being remediable later.

---

**Continue to:** [[10-economics-and-markets|10 — Economics and Markets]] · [[11-policy-regulation-safety|11 — Policy, Regulation and Safety]] · [[14-open-problems-and-risks|14 — Open Problems]]
