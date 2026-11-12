---
title: "Heating, Current Drive and Fuelling"
type: synthesis
doc: 16
part: 2
aliases:
  - "Heating, Current Drive and Fuelling"
tags:
  - fusion/synthesis
  - fusion/engineering
  - fusion/subsystems
created: 2026-08-25
updated: 2026-08-26
status: stable
confidence: high
related:
  - "[[01-fusion-physics-fundamentals]]"
  - "[[09-engineering-challenges]]"
  - "[[17-diagnostics-control-disruption]]"
  - "[[18-superconductors-and-magnets]]"
  - "[[24-grid-integration-and-operations]]"
---
# 16 — Heating, Current Drive and Fuelling

*Project Lux · How you actually get a plasma to 150 million degrees, keep current flowing in it, and feed it*

---

## Why this is a document of its own

A [[tokamak]] is often described as if the magnets were the machine. They are not. The magnets *hold* the plasma; something else has to **heat it, drive current in it, and refuel it** — continuously, from outside a vacuum vessel, through ports that also want to be occupied by breeding blanket.

These auxiliary systems are, collectively, among the largest cost items in a fusion plant, the dominant contributors to [[recirculating-power|recirculating power]], and the systems that most constrain where the blanket can go. [[iter|ITER]]'s heating systems alone represent a multi-billion-euro procurement across three technologies, each of which required its own dedicated test facility.

They also set a hard limit on plant economics. Every megawatt of heating power is a megawatt drawn from the plant's own output at 30–50% wall-plug efficiency, which is why Q_eng and Q_sci diverge so sharply ([[01-fusion-physics-fundamentals|Document 01 §5]]).

---

## 1. Ohmic heating — and why it runs out

A tokamak's plasma current is driven inductively: the central solenoid acts as a transformer primary, the plasma as a single-turn secondary. That current dissipates resistively and heats the plasma. Free, simple, and the only heating the earliest tokamaks had.

It fails for a specific and elegant reason. **Plasma resistivity scales as T⁻³/²** (Spitzer resistivity). The hotter the plasma gets, the better a conductor it becomes, and the less the same current heats it. Ohmic heating saturates around **1–2 keV** — roughly 10–20 million K.

D-T fusion needs 10–20 keV. So every fusion-relevant device needs **auxiliary heating**, and the search for it defined 1970s fusion engineering. PLT's achievement of 60 million K in 1978 using neutral beams was the moment this was settled.

---

## 2. [[neutral-beam-injection|Neutral Beam Injection (NBI)]]

### The principle

Accelerate ions electrostatically to high energy, **neutralise them** so they can cross the magnetic field, inject them into the plasma, where they re-ionise and thermalise by collisions — depositing energy and momentum.

NBI is unique among heating methods in that it does four things at once:
- **Heats** the plasma
- **Drives current** (the beam carries directional momentum)
- **Fuels** the plasma (the beam particles are fuel)
- **Drives rotation** (which stabilises certain MHD modes)

That combination is why it remains the workhorse despite being the most mechanically complex option.

### The negative-ion problem

Here is the engineering fork that defines modern NBI.

To penetrate to the centre of a large, dense plasma, beam particles must be energetic — for ITER, around **1 MeV per nucleon-equivalent**. But the neutralisation efficiency of **positive** ions collapses above roughly 100 keV/amu: a fast D⁺ simply will not pick up an electron from a gas target.

**Negative ions (D⁻) neutralise efficiently at any energy** — you are stripping a loosely bound extra electron rather than capturing one. So every high-energy fusion beamline must be built around negative ions.

That decision cascades into difficulty:
- D⁻ is fragile. Its binding energy is under 1 eV, so it is destroyed by collisions with background gas, by stray electric fields, and by photons.
- Producing D⁻ in quantity requires a **caesiated surface** — caesium evaporated onto the plasma grid lowers the work function so that atoms bouncing off it pick up an electron. Caesium then migrates, contaminates, and must be continuously managed.
- Co-extracted electrons must be dumped before the acceleration stage or they consume the entire power supply.
- The whole accelerator sits at −1 MV inside an SF₆-insulated vessel, and voltage holding at that level across large-area grids is itself a research problem.

### ITER's system

| | |
|---|---|
| Total NBI heating power | **33 MW** |
| Beam energy | **~1 MeV** |
| Negative deuterium ion current | **40 A per injector** |
| Power delivered per injector | **~16.5 MW** |
| Pulse length | **one hour** |

### The test facilities that had to be built first

ITER's beams were considered too risky to build without a full-scale prototype, so a dedicated facility — **PRIMA / [[nbtf-spider-mitica|NBTF]]**, at Consorzio RFX in Padua, Italy — was constructed to house two test stands:

- **SPIDER** — *Source for the Production of Ions of Deuterium Extracted from Rf plasma*. A full ITER-scale negative ion source, operating since **2018**, developing caesium injection strategies, beam uniformity and co-extracted electron control.
- **MITICA** — the complete **1 MV** injector: source, electrostatic accelerator, neutraliser, residual ion dump, and calorimeter. In advanced construction.

The existence of these facilities is itself informative: **a heating system for ITER required a research programme comparable in scale to a mid-sized tokamak**. Any company claiming a compact machine with substantial NBI power inherits that problem.

### The private-sector twist

Some concepts use beams not as auxiliary heating but as the **primary physics mechanism**:

- **[[tae-technologies|TAE Technologies]]** drives its [[field-reversed-configuration|field-reversed configuration]] entirely with neutral beams — the beams sustain the FRC against decay, provide a stabilising fast-ion population, and heat. TAE's 2025-26 announcement that "Norm" achieved plasma formation with **neutral beams alone** was a simplification of exactly this kind.
- Beam-driven fast-ion populations are also central to several mirror concepts.

---

## 3. Electron Cyclotron Resonance Heating (ECRH) and gyrotrons

### The principle

Launch microwaves at the **electron cyclotron frequency** — the frequency at which electrons gyrate around the magnetic field lines, `f_ce = eB / 2πm_e` ≈ **28 GHz per tesla**. At the resonant surface, electrons absorb the wave energy directly.

ECRH has properties no other heating method has:

- **Extreme localisation.** Because the resonance depends on local B, and B varies across the plasma, you can deposit power at a chosen radius by choosing a frequency — or by steering a mirror. Deposition widths of a few centimetres in a metres-wide plasma are routine.
- **No coupling structure inside the vessel.** The wave propagates in vacuum; the launcher can sit behind a port. Nothing has to touch the plasma.
- **Polarisation-selectable current drive** (ECCD).

That localisation is what makes ECRH the primary tool for **MHD control** (see §6) rather than merely bulk heating.

### The gyrotron

Generating megawatts of continuous millimetre-wave power required a device class of its own. A **gyrotron** is a fast-wave vacuum electron tube: an electron beam spirals in a strong superconducting magnet, and the electrons bunch in gyration phase, radiating coherently at the cyclotron frequency into a high-order cavity mode.

**ITER requires 24 gyrotrons at 170 GHz, 1 MW each, for 3,600-second pulses.**

That specification — megawatt, continuous, at a wavelength of 1.8 mm — is at the edge of what vacuum electronics can do. The engineering problems are the collector (dumping a megawatt of spent beam), the output window (a synthetic-diamond disc, the only material that is both transparent at 170 GHz and able to conduct the heat away), and mode purity.

### The 2026 milestone

The first **170 GHz, 1 MW gyrotron for the [[dtt|DTT]] ECRH system** completed acceptance testing at the **FALCON facility in Lausanne** (EPFL Swiss Plasma Center):

- **1 MW of RF power at 170 GHz for 100-second pulses**, delivered into an RF load as a 3 cm-diameter Gaussian beam
- Pre-series tube manufactured by **THALES**: **1.02 MW**, RF power stability **<5%**, **efficiency 40%**, five consecutive 100 s pulses with no parasitic modes
- **95% reliability — 19 successful pulses out of 20 attempts**

This is a **joint F4E and DTT procurement**, supplying both ITER and DTT — a rare instance of two major programmes sharing a component line, which is precisely how a supply chain is supposed to work.

The ITER tubes use a high-order **TE₃₁,₁₁** cavity mode. Development spans 14 GHz to sub-THz, and **megawatt-class sub-THz gyrotrons** are already proposed for future high-field devices — because resonance frequency scales with B, a 12 T machine like [[sparc|SPARC]] needs roughly twice ITER's frequency for the same resonance position.

---

## 4. Ion Cyclotron Resonance Heating (ICRH)

Same idea, ions instead of electrons: `f_ci ≈ 15 MHz per tesla` for deuterium. Tens of megahertz — radio frequencies, not microwaves.

**Advantages:** heats ions directly (which is what fuses); the RF sources are conventional, efficient and comparatively cheap; it can heat the plasma core; and minority-species schemes (a few percent of hydrogen or ³He in a deuterium plasma) give strong, well-localised absorption.

**Disadvantages, and they are serious:** ICRH requires an **antenna inside the vacuum vessel**, close to the plasma. That antenna:
- Occupies wall area that the breeding blanket wants
- Is exposed to the plasma edge, so it sputters impurities into the plasma
- Suffers from poor and variable coupling that depends sensitively on the edge density profile
- Generates RF sheaths that accelerate ions into nearby surfaces

ICRH's reputation is that it works well when it works and is temperamental. It remains in ITER's suite (**20 MW**) because heating ions directly is too valuable to abandon.

---

## 5. Current drive — the steady-state problem

A tokamak's plasma current cannot be sustained inductively forever: the central solenoid is a transformer, and transformers have a finite volt-second budget. When it runs out, the pulse ends.

There are three ways out, and every tokamak power plant design is some combination of them:

### 5.1 Accept pulsed operation
Run for hundreds or thousands of seconds, then pause to re-charge the solenoid. This is ITER's approach and the [[eu-demo|EU DEMO]] baseline. It works, but it makes the plant a pulsed heat source — with consequences covered in [[24-grid-integration-and-operations|Document 24]].

### 5.2 Non-inductive current drive
Drive current directly with waves or beams:

| Method | Efficiency | Notes |
|---|---|---|
| **NBI current drive** | Best current-drive efficiency of the RF/beam methods | But large, complex, and blanket-hostile |
| **ECCD** (electron cyclotron) | Lower efficiency | Superbly localised — the tool of choice for *targeted* current drive at a specific surface |
| **LHCD** (lower hybrid) | Highest efficiency of the RF methods | But deposits off-axis and couples poorly at reactor-relevant densities |
| **ICRF fast wave** | Moderate | Antenna problems as above |

All of them cost recirculating power. A plant driving 100% of its current non-inductively would likely be a net energy consumer.

### 5.3 [[bootstrap-current|Bootstrap current]] — the way out
A toroidal plasma with a pressure gradient **drives its own current** through trapped-particle dynamics. This is free current, and the bootstrap fraction rises with plasma pressure (specifically with poloidal beta).

**Advanced tokamak scenarios** target bootstrap fractions of **70–90%**, driving only the remainder externally. This is the only credible route to a steady-state tokamak power plant, and it is why "advanced scenario" development is a permanent line item in every fusion programme.

The catch: high bootstrap fraction requires broad, hollow current profiles that are more MHD-unstable, and reaching them requires **internal transport barriers** that are themselves delicate. The steady-state tokamak is a genuinely harder physics problem than the pulsed one.

**Stellarators avoid the entire question**, because their confining field is generated externally. This is the single strongest argument for the concept, and it is why the private [[stellarator]] sector exists.

---

## 6. Using heating for control, not just heat

Modern practice treats heating systems as **actuators in a control loop**, not just power supplies. This is where ECRH's localisation earns its cost.

### Neoclassical tearing modes (NTMs)
An NTM is a magnetic island that grows at a rational surface (typically q = 2 or q = 3/2) because the island flattens the pressure profile inside itself, removing the local bootstrap current, which makes the island grow further. It is self-reinforcing.

NTMs **degrade confinement significantly and can trigger disruptions**. The fix is precise: deposit **electron cyclotron current drive exactly inside the island**, replacing the missing bootstrap current. This requires real-time island detection, real-time mirror steering, and modulation synchronised to the island's rotation. It works, and it is standard practice on [[asdex-upgrade|ASDEX Upgrade]], [[diii-d|DIII-D]] and [[tcv|TCV]].

### Sawteeth
The plasma core periodically reorganises when q falls below 1, in a rapid internal reconnection called a **sawtooth crash**. Sawteeth are not intrinsically harmful — they expel [[helium-ash|helium ash]] from the core, which is useful — but **large sawtooth crashes seed NTMs**. So the goal is sawtooth *pacing*: keeping crashes small and frequent rather than rare and violent, again using localised ECCD or ICRH near the q = 1 surface.

A related and elegant phenomenon: in **hybrid scenarios**, off-axis current drive raises the core q above 1, shrinking or eliminating the q = 1 surface. The result is a **sawtooth-free regime with a broad, shear-free core current profile, a large non-inductive current fraction and improved confinement** — one of the more promising reactor scenarios. ASDEX Upgrade work on "flux pumping" explores how the plasma self-organises to maintain this state.

### ELM control
Edge-localised modes are handled by **resonant magnetic perturbation coils**, **pellet pacing** (deliberately triggering small ELMs before large ones can build), or by operating in naturally ELM-free regimes: **quasi-continuous exhaust**, **[[negative-triangularity|negative triangularity]]**, or the **X-point radiator**.

### Internal transport barriers
Long central heating — usually NBI — can establish an **internal transport barrier**: a region of suppressed turbulence in the plasma core producing peaked density and pressure profiles. ITBs raise performance substantially and are central to advanced scenarios, but they are fragile and prone to triggering MHD when the pressure gradient gets too steep.

---

## 7. Fuelling

A [[burning-plasma|burning plasma]] consumes fuel and must be refilled, continuously, from outside.

### Gas puffing
Simply admit neutral gas at the edge. Cheap, simple, and **it does not work well for a reactor**: neutrals ionise within centimetres of the plasma boundary and never reach the core. Gas puffing fuels the edge and the [[divertor]], which is useful for [[detachment]] control, but it cannot sustain a core density profile.

### [[pellet-injection|Pellet injection]] — the only viable core fuelling method

Freeze deuterium-tritium into a solid pellet a few millimetres across and fire it into the plasma at hundreds of metres per second. The pellet ablates as it penetrates, depositing fuel deep inside.

The physics has a useful quirk: on the **high-field side** of the torus, ablated material drifts *inward* rather than outward (a curvature-driven ∇B drift effect). So **high-field-side injection** delivers fuel much deeper than the pellet's mechanical penetration alone would suggest — which is why reactor designs route pellet guide tubes over the top of the machine and inject from the inboard side.

Pellet injection also does double duty as **ELM pacing** and, in shattered form, as the **[[disruption]] mitigation system** ([[17-diagnostics-control-disruption|Document 17]]).

### The engineering, and who owns it

Cryogenic pellet injection is a specialised discipline with a small number of world experts, and **[[ornl|Oak Ridge National Laboratory]] has been its centre for four decades**. Two 2026 developments make the point:

- **[[wendelstein-7-x|Wendelstein 7-X]]'s record 43-second, world-record-triple-product discharge was fed by roughly 90 frozen hydrogen pellets from a one-of-a-kind injector built at ORNL in Tennessee.** The best confinement result in stellarator history depended on an American fuelling system.
- **On 6 August 2026, ORNL licensed four cryogenic pellet fuelling inventions to [[type-one-energy|Type One Energy]]**, including a **novel extrusion system capable of producing pellets at rates appropriate for reactor operation**. That last clause is the important one: research injectors fire tens of pellets per discharge; a power plant needs a continuous extrusion line running for months.

### Why fuelling connects to the tritium problem

Only **1–3% of injected tritium fuses per pass**. Everything else is pumped out and recycled. Fuelling throughput therefore sets the **tritium inventory held up in the fuelling system**, which is a first-order term in a plant's total tritium inventory — and tritium inventory is both a cost (at $30,000–35,000/g) and a safety-case limit.

This is why **Direct Internal Recycling** — routing pumped exhaust back to the fuelling system without full isotope separation — appears as a DOE roadmap mid-term milestone. It is a fuelling-system innovation with fuel-cycle consequences.

---

## 8. What this means for plant design

Three conclusions follow from the whole chapter, and they are not obvious from the outside.

**1. Heating systems compete with the blanket for wall area.** Every port occupied by a beamline, an ICRH antenna or an ECRH launcher is a hole in the breeding blanket, and each hole reduces the [[tritium-breeding-ratio|tritium breeding ratio]]. **The heating system and the fuel cycle are in direct geometric conflict**, and that conflict is one of the least-discussed constraints in reactor design. ECRH is favoured partly because it needs the smallest aperture.

**2. Heating power is the dominant recirculating load.** At 30–50% wall-plug efficiency, 100 MW of injected heating costs 200–330 MW of plant output. This is why the difference between Q_sci = 10 and Q_sci = 30 matters so much economically.

**3. These systems are as immature as the reactor.** ITER's beams needed their own dedicated multi-decade test facility. Gyrotrons at ITER specification were only demonstrated at 100-second pulses in 2026 — against a 3,600-second requirement. Reactor-rate pellet extrusion was licensed to industry for the first time in August 2026. **The auxiliary systems are on the same development timeline as the machines they serve, and they are rarely counted in fusion timelines.**

---

**Continue to:** [[17-diagnostics-control-disruption|17 — Diagnostics, Control and Disruption Mitigation]] · [[18-superconductors-and-magnets|18 — Superconductors and Magnet Engineering]] · [[09-engineering-challenges|09 — Engineering Challenges]]
