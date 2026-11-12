---
title: "Superconductors and Magnet Engineering"
type: synthesis
doc: 18
part: 2
aliases:
  - "Superconductors and Magnet Engineering"
tags:
  - fusion/synthesis
  - fusion/engineering
  - fusion/magnets
created: 2026-08-25
updated: 2026-11-02
status: stable
confidence: high
related:
  - "[[09-engineering-challenges]]"
  - "[[19-simulation-codes-nuclear-data]]"
  - "[[22-critical-materials-supply-chains]]"
---
# 18 — Superconductors and Magnet Engineering

*Project Lux · The component that changed fusion's economics, and what it takes to build one*

---

## 1. Why the magnet is the machine

For a magnetically confined reactor, fusion power density scales as **β²B⁴**. [[plasma-beta|Beta]] is bounded by MHD stability at a few percent for tokamaks. So **the magnet sets the machine.**

Everything downstream follows from the field strength you can generate: the plasma volume you need, the building you need to put it in, the amount of steel and concrete, the construction schedule, and therefore the capital cost. A machine that can run at twice the field can, in principle, do the same job at one-sixteenth the plasma volume.

This is why the single most consequential event in fusion between 2010 and 2022 was not a plasma result. It was a **magnet test**: CFS and MIT reaching **20 tesla** on a large-bore REBCO model coil on 5 September 2021.

---

## 2. The three conductor generations

| Generation | Material | Practical field limit | Operating temperature | Where used |
|---|---|---|---|---|
| **Copper** (resistive) | Cu, or Cu with Bitter plates | ~20 T, pulsed only | Room temp / water-cooled | [[diii-d|DIII-D]], [[alcator-c-mod|Alcator C-Mod]], [[jet|JET]], [[st40|ST40]] |
| **LTS** (low-temperature superconductor) | NbTi, Nb₃Sn | **~12–13 T** on conductor | **4.5 K** | [[iter|ITER]], W7-X, [[jt-60sa|JT-60SA]], [[east|EAST]], [[kstar|KSTAR]] |
| **HTS** (high-temperature superconductor) | **REBCO** tape | **>20 T** demonstrated | 4–20 K (usable at 77 K at low field) | [[sparc|SPARC]]/[[arc|ARC]], [[wham|WHAM]], Demo4, [[hh70|HH70]], Thea, Type One |

### Copper
Simple and cheap, and it dissipates ohmic power continuously — megawatts to hundreds of megawatts. Fine for a pulsed research device; impossible for a power plant, because the magnets would consume more power than the plasma produces. Every copper-magnet [[tokamak]] is, by construction, a physics experiment rather than a reactor prototype.

### LTS: NbTi and Nb₃Sn
**NbTi** is ductile, cheap and well understood, usable to about 9 T. **Nb₃Sn** reaches 12–13 T but is **brittle** — it must be wound in a ductile precursor state and then *reacted* by heat treatment at ~650 °C for days, after which the coil cannot be bent without cracking the superconductor. This "wind-and-react" constraint dictates the entire manufacturing sequence of an ITER-class magnet.

ITER consumed roughly **100,000 km of Nb₃Sn strand** — enough to circle the Earth 2.5 times — and building it **increased world Nb₃Sn production capacity by roughly an order of magnitude**. That industrial legacy now benefits the private sector directly, and it is arguably ITER's most durable contribution.

### HTS: REBCO
**Rare-Earth Barium Copper Oxide** (typically YBCO or GdBCO). Not a wire but a **tape**: a ~1 μm superconducting layer deposited on a buffered metal substrate, capped with silver and copper, typically 4 or 12 mm wide and ~0.1 mm thick.

Its critical property is not the high transition temperature (~90 K) — fusion magnets run cold anyway. It is that **REBCO retains enormous current density in enormous magnetic fields**, well past where Nb₃Sn quenches. Operating at 20 K rather than 4.5 K is a secondary but real benefit: the specific heat of materials is orders of magnitude higher at 20 K, which gives a magnet far more thermal margin against a local disturbance.

---

## 3. How REBCO tape is actually made — and why supply is tight

The superconducting layer must be **biaxially textured**: its crystal grains aligned in all three axes, because REBCO carries almost no current across a misaligned grain boundary. Achieving that on a flexible metal tape is the whole manufacturing problem.

Two routes to the textured template:

- **IBAD** (Ion Beam Assisted Deposition) — an ion beam sputters a buffer layer at a grazing angle, preferentially destroying misaligned grains
- **RABiTS** (Rolling Assisted Biaxially Textured Substrates) — texture the metal substrate itself by rolling and annealing, then epitaxially grow buffers on it

Two main routes to depositing the REBCO layer itself:

- **PLD** (Pulsed Laser Deposition) — a laser ablates a REBCO target onto the moving tape. High quality, and the dominant route among top-tier producers
- **MOCVD** (Metal-Organic Chemical Vapour Deposition) — higher throughput, chemically finicky

The result is a multi-layer vapour-deposition process running on a continuously moving substrate, requiring uniformity along kilometres of tape, with performance quoted as critical current per centimetre-width at a given field and temperature.

**Global capacity is around 10,000 km/year.** The top PLD-based manufacturers each produce over 3,000 km-of-12mm annually, together exceeding half of world output, and **China holds substantial manufacturing strength**. A single high-field tokamak consumes thousands of kilometres. This is the sector's tightest physical bottleneck.

**The 2026 responses:**
- **[[arpa-e|ARPA-E]] SCALEUP awarded [[thea-energy|Thea Energy]] $20 million (July 2026)** to establish **the first US production line for modular HTS magnets**
- **CFS began selling magnets as a merchant product in April 2026**, starting with [[realta-fusion|Realta Fusion]] — explicitly to create the aggregate demand that justifies tape-capacity investment
- **[[tokamak-energy|Tokamak Energy]]** sells magnets through its **TE Magnetics** division and won the **£70 m [[step|STEP]] magnet systems contract**

---

## 4. From tape to cable: the architectures

A single tape carries a few hundred amperes. A fusion magnet needs tens of kiloamperes. So tapes must be assembled into cables — and because REBCO is a flat, anisotropic tape rather than a round wire, this is genuinely hard. The cable must handle enormous Lorentz forces, allow helium cooling, permit current sharing between tapes, and tolerate bending during winding.

| Architecture | Description | Used by |
|---|---|---|
| **VIPER** | Stacks of HTS tape in channels within a copper former, soldered and VPI-impregnated, with a central cooling channel | **CFS / MIT PSFC** |
| **PIT VIPER** | VIPER with **internal electrical insulation partitioning each tape stack**, and a **fibre-optic sensor per stack** | **CFS** — for pulsed magnets |
| **CORC** | *Conductor On Round Core* — tapes helically wound around a round former. High engineering current density; good tolerance to transverse compression and bending | Various; attractive for fusion |
| **Twisted stacked-tape cable** | Stacks twisted along the cable axis to equalise flux linkage | Research |
| **Roebel** | Tapes punched and interleaved in a transposed pattern | Accelerator and fusion research |
| **STARS** | Simple-stacked, non-insulated conductor | **[[helical-fusion|Helical Fusion]]** (Japan) |

**VIPER's published specification: 45.6 kA at 10 K and 10.9 T.**

A notable milestone: the **first non-planar REBCO [[stellarator]] coil** was built using VIPER cable — demonstrating that HTS can be wound into the 3D geometries that stellarators require, which had been a serious open question for the private stellarator sector.

The alternative is to avoid non-planar winding. [[canis]] used **nine planar REBCO shaping coils assembled from 45 double pancakes**, with tape from three suppliers. At 20 K, closed-loop control reproduced two static field patterns with 0.56% and 0.60% RMS error. This is a manufacturing and magnet-control proof of concept, not a stellarator-plasma result; see [[prototyping-test-canis-hts-planar-coil-array]].

---

## 5. Insulation, or the deliberate absence of it

This is the most conceptually interesting choice in HTS magnet design.

### The no-insulation idea
In a conventional magnet, turns are electrically insulated so current follows the winding path. In a **no-insulation (NI)** coil, adjacent turns are in electrical contact. Current normally follows the spiral path (lowest impedance), but if a local defect or hot spot appears, **current simply bypasses it radially through the neighbouring turns**.

The result is a magnet that is **self-protecting**: it routes around damage rather than quenching catastrophically. For a device storing gigajoules, this is a profound advantage.

**CFS's NINT** — *no-insulation, no-twist* — was proven in the **2021 TFMC 20 T test**. It suits **steady-state** magnets operating at unvarying current, such as a tokamak's toroidal field coils.

### The cost, and PIT VIPER
NI's weakness is the mirror of its strength: because current can move radially, the coil has slow, complex charging dynamics and does not respond cleanly to rapid current changes. That makes it unsuitable for **pulsed** magnets — central solenoids and poloidal field coils, which must ramp on second timescales.

CFS's answer, announced as its "second breakthrough superconducting technology," is **PIT VIPER**: partition each stack of HTS tape with internal electrical insulation, restoring predictable pulsed behaviour, and then solve the protection problem a different way — **give every stack its own fibre-optic cable**. Light travelling through the fibre reveals a forming hot spot, and the machine can react **in under a second**.

That pairing — NINT for the steady-state TF coils, PIT VIPER for the pulsed coils — is the current state of the art in fusion magnet design, and it is a good illustration of how the field solves problems: not with one universal answer but with two architectures matched to two duty cycles.

---

## 6. [[quench|Quench]]: the failure mode

A **quench** is a local loss of superconductivity. The affected region becomes resistive, dissipates energy, heats, and the normal zone spreads. In a magnet storing gigajoules, an undetected quench concentrates that energy in a small volume and destroys the conductor.

**HTS makes this harder, not easier.** LTS magnets have a fast **normal zone propagation velocity** — metres per second — so a quench spreads quickly, distributes its energy, and is easy to detect by the voltage rise. REBCO's NZPV is of order **centimetres per second**. A hot spot can therefore reach destructive temperature while remaining electrically almost invisible.

Detection approaches:
- **Voltage taps** — the conventional method; too slow and too noisy for HTS alone
- **Fibre-optic sensing** — distributed temperature and strain along the conductor. This is CFS's PIT VIPER approach
- **Acoustic emission** — listening for the mechanical signature of a quench
- **Current-distribution monitoring** — measuring how current redistributes among tapes. Demonstrated (*Scientific Reports*, 2022) to detect both quench **and cumulative damage**, which is the more useful capability for a magnet expected to last decades
- **No-insulation self-protection**, as above

DOE's roadmap makes this a formal deliverable: Challenge Area C's mid-term milestone includes *"qualify HTS magnet cables/coils and radiation-hard diagnostics."*

---

## 7. Radiation — the unretired risk

Superconductors are crystalline materials, and neutron irradiation creates defects. In REBCO, the picture is not monotonic:

- Modest irradiation can **improve** performance, because defects act as flux-pinning centres that stop vortex motion
- Beyond a threshold fluence, the superconducting layer degrades and critical current falls irreversibly
- **The organic components fail first.** Epoxy impregnation, insulation and solder joints degrade at fluences well below the superconductor's own limit

For a compact high-field machine, the magnet sits close to the plasma with limited shielding space. In a **[[spherical-tokamak|spherical tokamak]]'s centre column**, there is barely room for the conductor, let alone shielding — which is the concept's central unsolved engineering problem.

> [!warning] A worked instance, and the design does not currently clear its own limit
> [[st-e1-neutronics-crossref-metadata-2026|ST-E1's neutronics paper]] — full text read
> 2026-11-02 — sets a fast-flux limit to the [[rebco|HTS]] of **< 4 × 10⁹ cm⁻² s⁻¹** for 30
> full-power years, and reports a **peak of 9.5 × 10⁹**, about **2.4× over**, for an estimated
> **13 fpy**. A larger 2400 MW variant using tungsten boride at aspect ratio 2.31 reaches
> ≈ 5.6 × 10⁹ and roughly **25 fpy**.
>
> Two things follow. First, this is the vault's only numerical magnet-lifetime shortfall
> published by a design team against its own criterion — evidence that the problem above is live,
> not rhetorical. Second, the abstract of the same paper describes the design as demonstrating
> feasibility of a 30-year life, so **the shortfall is visible only in the full text**. See
> [[st-e1]].
>
> The cryogenic side is tight too: **18.5 kW** of nuclear heating at 20 K against a **20 kW**
> budget — a 7.5% margin, of which the error-field correction coils alone take 9.8 kW.

The DOE roadmap's near-term milestone is blunt about the state of knowledge: **"Conduct REBCO irradiation campaigns to define magnet performance and standards."**

Put plainly: **an industry is being built around a conductor whose in-service radiation lifetime has not been established.** Lawrence Berkeley's work on gas production in REBCO-based magnets under irradiation is part of closing that gap. This belongs on any honest risk list.

---

## 8. Cryogenics — the system nobody mentions

Superconducting magnets need to be cold, and keeping something cold in a machine designed to be extremely hot is a large industrial plant in its own right.

**ITER's cryoplant, by the numbers:**

| | |
|---|---|
| Facility area | **5,400 m²** |
| Equipment mass | **~5,500 tonnes** |
| Helium inventory | **~25 tonnes** |
| Distribution network | **~5 km** of pipes, pumps and valves |
| Refrigerators | **Three identical helium refrigerators in parallel** |
| Total cooling capacity | **75 kW at 4.5 K** (−269 °C) |
| Mass cooled | **10,000 tonnes of superconducting magnets**, plus thermal shields, cryopumps and diagnostics |

**This is one of the largest cryogenic installations in the world**, and it exists purely as a support system.

### Why it matters economically
Removing heat at 4.5 K costs roughly **250–1,000 W of room-temperature electrical power per watt removed** (the Carnot penalty plus real inefficiency). So every watt of nuclear heating deposited in a cold magnet is amplified by two to three orders of magnitude in the plant's [[recirculating-power|recirculating power]] budget.

This is a direct argument for HTS beyond field strength: **operating at 20 K instead of 4.5 K reduces the Carnot penalty by roughly a factor of four or five.** It is one of the least-advertised advantages of the HTS transition and one of the more important ones for Q_eng.

### Vacuum
ITER's vacuum system is comparably extreme — the cryostat is the largest stainless steel vacuum chamber ever built (30 m × 30 m, ~3,850 t), and pumping is done by **cryopumps**: large cryoadsorption panels cooled by supercritical helium at 4 K, which freeze gas onto their surfaces. **Six torus cryopumps** sit around the vacuum vessel, with **two more on the cryostat**, and they consume **15% of the cryogenic power** on their own.

Cryopumps must periodically be regenerated — warmed to release trapped gas — which in a D-T machine means releasing a tritium-bearing gas load into the fuel cycle. Pumping, fuelling and tritium processing are one coupled system, not three.

---

## 9. Where magnet technology stands, August 2026

| Achievement | Value | Who | When |
|---|---|---|---|
| Highest field on a confined fusion plasma | **17 T** | WHAM (UW-Madison / Realta) | Jul 2024 |
| HTS model coil field | **20 T** | CFS / MIT (TFMC) | Sep 2021 |
| Full tokamak-configuration HTS magnet | **11.8 T, 7 MA-turns** | Tokamak Energy (Demo4) | 2026 |
| First fully HTS tokamak | Complete machine, built in ~2 years | [[energy-singularity|Energy Singularity]] (HH70) | 2024 |
| VIPER cable rating | **45.6 kA at 10 K, 10.9 T** | CFS / MIT | — |
| Largest LTS magnet system | **51 GJ stored, ~10,000 t** | ITER | Complete 2026 |
| Largest superconducting magnet component tested | **582-tonne magnet** for [[best-tokamak|BEST]] | China ([[asipp|ASIPP]]) | 4 Aug 2026 |
| First non-planar REBCO stellarator coil | — | VIPER-based | — |
| Planar HTS shaping-coil array | **9 coils; 45 double pancakes; 20 K** | [[canis]] / [[thea-energy]] | 2025 |

### The strategic read

**HTS is the technology that made the current fusion boom possible.** Every compact private tokamak, every private stellarator, and the mirror revival all depend on it. Without REBCO, the sector would look like it did in 2015.

**Three risks remain unretired**, and they are the ones to watch:
1. **Supply.** ~10,000 km/year globally, concentrated, against a fleet requirement orders of magnitude larger
2. **Radiation lifetime.** Not established. If REBCO or its insulation degrades faster than assumed, compact high-field machines need more shielding, which means bigger machines, which erases much of the advantage
3. **Quench protection at scale.** Demonstrated on model coils; not yet demonstrated on a full magnet system in a machine that has run for years

The magnet is no longer the reason fusion cannot work. It is now one of the reasons it might be expensive.


## Evidence in `raw/`

Primary sources held in this vault that evidence the claims above:

- [[sparc-toroidal-field-model-coil-program]]

---

**Continue to:** [[19-simulation-codes-nuclear-data|19 — Simulation, Codes and Nuclear Data]] · [[22-critical-materials-supply-chains|22 — Critical Materials and Supply Chains]] · [[09-engineering-challenges|09 — Engineering Challenges]]
