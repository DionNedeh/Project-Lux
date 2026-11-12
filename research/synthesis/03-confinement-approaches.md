---
title: "Confinement Approaches"
type: synthesis
doc: 03
part: 1
aliases:
  - "Confinement Approaches"
tags:
  - fusion/synthesis
  - fusion/physics
  - fusion/machines
created: 2026-08-25
updated: 2026-08-29
status: stable
confidence: high
related:
  - "[[04-magnetic-confinement-devices]]"
  - "[[05-inertial-confinement-fusion]]"
  - "[[07-private-fusion-industry]]"
---
# 03 — Confinement Approaches: The Full Taxonomy

*Project Lux · Every way anyone is seriously trying to confine a fusion plasma*

---

## The fundamental problem

To fuse, a plasma must be held at 100–200 million K at sufficient density for sufficient time. No material container can touch it — any solid wall would both vaporise and, more importantly, [[quench]] the plasma instantly by radiating away its energy through impurity contamination.

There are exactly **three physical strategies** for holding a plasma without a wall, and they are distinguished by which term of the Lawson product they maximise:

| Strategy | Density | Confinement time | Mechanism |
|---|---|---|---|
| **Magnetic confinement (MCF)** | ~10²⁰ m⁻³ (a millionth of atmospheric) | seconds to continuous | Magnetic fields deflect charged particles |
| **[[inertial-confinement|Inertial confinement]] (ICF)** | ~10³¹ m⁻³ (1000× solid) | ~10⁻¹⁰ s | Fuel inertia — it burns before it can expand |
| **Magneto-inertial (MIF)** | ~10²⁴–10²⁸ m⁻³ | ~10⁻⁶ s | Compress a magnetised plasma; field insulates during compression |

Note that these span **eleven orders of magnitude in density** and a comparable range in time, while the product `nτ` must land in the same narrow band. This is why the engineering of the three routes has almost nothing in common — a laser fusion plant and a [[tokamak]] share the fuel and essentially nothing else.

The distribution of effort in the private sector as of 2026 (FIA survey, 56 companies):

- **Magnetic confinement — 26 companies (46%)**
- **Inertial confinement — 12 companies (21%)**
- **Magneto-inertial — 9 companies (16%)**
- **Hybrid electrostatic — 7 companies (13%)**
- **Muon-catalysed — 1 company**

---

## Part I: Magnetic Confinement

### The geometry problem

A charged particle in a magnetic field spirals along field lines — confined perpendicular to the field, free along it. So field lines must not end at a wall. The obvious solution is a torus: bend the field into a doughnut so the lines close on themselves.

But a purely toroidal field fails. The field is stronger on the inside of the torus than the outside, and this gradient plus the field-line curvature causes **charge-dependent vertical drift**: ions drift up, electrons drift down. The resulting vertical electric field drives an **E×B drift** that pushes the entire plasma outward into the wall in microseconds.

The fix is to give the field lines a **helical twist**, so that a particle following a line spends time both above and below the midplane, and the drifts cancel. This is the **rotational transform**, and how you generate it defines the machine:

- **Tokamak** — drive a large toroidal current through the plasma itself; its poloidal field twists the lines
- **[[stellarator|Stellarator]]** — twist the lines using complex, 3D external coils, requiring no plasma current
- **Reversed field pinch** — a tokamak-like device where the toroidal field reverses at the edge, with a much weaker external field
- **Spheromak / FRC** — let the plasma generate essentially all of its own field, in a self-organised state

---

### 1. The Tokamak

**Principle.** Strong toroidal field from external coils (typically 5–12 T), plus a poloidal field from a plasma current of several megamperes driven inductively by a central solenoid acting as a transformer primary.

**Strengths.**
- By far the best-understood confinement scheme. Sixty years and hundreds of machines of empirical scaling, validated theory, and mature diagnostics.
- Highest triple products ever achieved in magnetic confinement.
- Axisymmetric — good fast-alpha confinement, comparatively simple coils.
- [[h-mode|H-mode]] gives a factor-of-two confinement bonus for free.

**Weaknesses.**
- **Disruptions.** The plasma current is both the source of confinement and a stored energy reservoir. Losing it dumps the full thermal and magnetic energy into the wall in milliseconds and can generate multi-megaampere runaway electron beams. This is the tokamak's fundamental design vulnerability, and it worsens with size.
- **Pulsed by nature.** An inductive transformer cannot drive current forever. Steady-state operation requires non-inductive current drive (neutral beams, RF) which costs [[recirculating-power|recirculating power]], or high bootstrap fraction, or accepting pulsed operation with thermal storage.
- **Density limit.** Greenwald limit constrains operating space (though [[east|EAST]] reported a route past it in January 2026).

**Who is pursuing it.** [[iter|ITER]], [[sparc|SPARC]]/[[arc|ARC]] (CFS), [[jt-60sa|JT-60SA]], EAST/[[best-tokamak|BEST]]/[[cfetr|CFETR]], [[kstar|KSTAR]], [[diii-d|DIII-D]], [[west|WEST]], [[t-15md|T-15MD]], [[hh70|HH70]]/HH170 ([[energy-singularity|Energy Singularity]]), plus the spherical variants below. **5 companies** report conventional tokamaks and **3** spherical tokamaks in the FIA survey.

---

### 2. The Spherical Tokamak

**Principle.** Squash the tokamak's aspect ratio (R/a) from ~3 down to ~1.5. The plasma becomes a cored apple rather than a doughnut.

**Strengths.**
- **Much higher beta.** Spherical tokamaks routinely reach β of 20–40% versus a few percent conventionally. Since fusion power goes as β²B⁴, high beta partially substitutes for high field.
- Compact, potentially cheaper machines.
- Naturally higher [[bootstrap-current|bootstrap current]] fraction.

**Weaknesses.**
- **The centre column.** There is very little room on the inboard side for the central solenoid, the toroidal-field conductors, *and* neutron shielding. In a D-T reactor the centre column takes a brutal neutron dose with almost no space to shield it. This is the spherical tokamak's central unsolved engineering problem.
- Solenoid-free start-up is required, which is an active research area.
- Less confinement data than conventional tokamaks.

**Who.** UK **[[step|STEP]]** (the flagship national bet), **[[tokamak-energy|Tokamak Energy]]** ([[st40|ST40]] — which achieved 100 million K in 2022 — and the ST80-HTS successor), **ENN** in China, [[mast-upgrade|MAST-Upgrade]] and NSTX-U as research devices.

---

### 3. The Stellarator

**Principle.** Generate the entire confining field, including the rotational transform, from external coils. No plasma current is required.

**Strengths.**
- **No disruptions.** With no large plasma current, the tokamak's principal failure mode simply does not exist. This is a profound advantage for a power plant that must run at 90%+ availability.
- **Intrinsically steady-state.** No transformer, no current drive, no pulsing. A stellarator can in principle run continuously.
- **No density limit** of the Greenwald type; stellarators operate at high density comfortably.

**Weaknesses.**
- **Geometric complexity.** W7-X's 50 non-planar superconducting coils are shaped to roughly 1 mm tolerance. Manufacturing cost and schedule risk are severe, and maintenance access through a 3D coil set is genuinely difficult.
- **Neoclassical transport.** An unoptimised 3D field has catastrophic collisionless particle losses. This is why stellarators lost to tokamaks in 1969 — and why they came back once computers could optimise the field.
- **Fast-alpha confinement.** Good alpha confinement in 3D geometry is hard to arrange and is a live design constraint for reactor-scale stellarators.

**The optimisation revolution.** Modern stellarators are *designed*, not drawn. Two families of optimisation target:

- **Quasi-symmetry** — engineer the field *strength* to have a hidden symmetry (quasi-axisymmetric, quasi-helical, or quasi-poloidal) even though the geometry is fully 3D. A particle then behaves as if it were in a symmetric device, recovering good confinement. HSX (Wisconsin) demonstrated quasi-helical symmetry experimentally.
- **Quasi-isodynamicity** — arrange the field so that collisionless particle orbits close on themselves, eliminating neoclassical transport by a different route. W7-X is optimised this way.

Recent method advances (2026) include **quasi-single-stage optimisation**, which folds coil buildability directly into the plasma-boundary optimisation rather than solving the two problems sequentially, and generative models producing candidate configurations directly.

**Who.** **[[wendelstein-7-x|Wendelstein 7-X]]** (Germany — the world leader), **LHD** (Japan, retired 2025), **[[type-one-energy|Type One Energy]]** ([[infinity-two|Infinity Two]], TVA site in Tennessee), **[[thea-energy|Thea Energy]]** (Eos — using arrays of simple *planar* coils rather than complex 3D ones), **[[proxima-fusion|Proxima Fusion]]** (Stellaris, Munich), **[[renaissance-fusion|Renaissance Fusion]]**, **[[helical-fusion|Helical Fusion]]**, **[[gauss-fusion|Gauss Fusion]]**, **[[stellarex|Stellarex]]**. **8 companies** in the FIA survey — the largest single magnetic category, which would have been unimaginable in 2010.

---

### 4. The [[magnetic-mirror|Magnetic Mirror]]

**Principle.** A linear (not toroidal) field with strong magnetic "plugs" at each end. Particles moving along the axis are reflected by the magnetic gradient — the magnetic-moment invariant makes a converging field act as a mirror.

**Strengths.**
- **Simple, linear geometry.** Cylindrical vessel, simple coils, straightforward maintenance access, easy to segment for replacement.
- High beta.
- **[[direct-energy-conversion|Direct energy conversion]] is natural.** Charged particles escaping the ends can be decelerated against an electrostatic field, converting their kinetic energy directly to electricity without a steam cycle. Realta demonstrated exactly this in June 2026.

**Weaknesses.**
- **End losses.** Particles in the "loss cone" of velocity space escape immediately. This is intrinsic and is why the US cancelled the [[mftf-b|MFTF-B]] mirror program in 1986 on the day it was completed.
- Historically poor confinement relative to toroidal devices.

**Why it is back.** Two changes. First, HTS magnets allow far higher mirror ratios than were possible in the 1980s — [[wham|WHAM]] achieved **17 T** on the confined plasma. Higher mirror ratio directly shrinks the loss cone. Second, tandem mirror configurations and modern theory address the losses more effectively than 1980s designs.

**Who.** **[[realta-fusion|Realta Fusion]]** (WHAM at UW-Madison → Anvil → Hammir), **[[novatron|Novatron Fusion]]** (Sweden), plus gas dynamic trap and centrifugal mirror variants. Notably, CFS is supplying Realta's magnets — an early sign of a fusion *supply chain* rather than 56 vertically integrated companies.

---

### 5. [[field-reversed-configuration|Field-Reversed Configuration (FRC)]]

**Principle.** A self-organised, elongated plasmoid in which the plasma's own current reverses the applied field, creating closed field lines with **no toroidal field at all**. [[plasma-beta|Beta]] approaches 1 — the plasma pressure nearly equals the magnetic pressure.

**Strengths.**
- **β ≈ 1** is the highest of any configuration; magnetic field is used with maximum efficiency.
- Simple, linear geometry with a natural [[divertor]] at each end.
- The high beta makes **advanced aneutronic fuels** (p-¹¹B, D-³He) more plausible than in any other scheme, because those fuels need enormous pressure.
- Translatable — the plasmoid can be formed in one place and moved to another.

**Weaknesses.**
- Stability. FRCs are theoretically vulnerable to tilt and rotational modes; historically they were short-lived.
- Confinement scaling is far less established than tokamaks.

**Who.** **[[tae-technologies|TAE Technologies]]** (the largest FRC effort; C-2W/"Norm", targeting eventual p-¹¹B), **[[helion-energy|Helion Energy]]** (colliding, compressed FRCs with pulsed direct energy recovery), **NearStar Fusion**, **Princeton Fusion Systems**. **3 companies** report pure FRC; Helion's approach is usually classed as magneto-inertial.

---

### 6. Other magnetic schemes

- **Levitated dipole** — a superconducting ring levitated inside the vacuum chamber, mimicking a planetary magnetosphere. Remarkable stability and natural density peaking. **[[openstar-technologies|OpenStar Technologies]]** (New Zealand) achieved plasma in 2024. Recent work explores D-T levitated dipole plants (arXiv:2602.20564).
- **Reversed field pinch** — RFX-mod2 (Italy), MST (Wisconsin). Low external field requirement; self-organised states.
- **Z-pinch** — the oldest idea, revived. See magneto-inertial below.
- **Levitron, plectoneme, centrifugal mirror** — single-company approaches in the FIA survey.

---

## Part II: Inertial Confinement

### The principle

Deliver energy to the surface of a millimetre-scale fuel capsule fast enough that the surface blows off (ablates) and the reaction drives the remaining shell inward at 350–400 km/s. The fuel compresses to ~1,000× solid density and ~100 million K in a central hot spot, ignites, and a burn wave propagates outward through the cold dense fuel before the whole assembly disassembles — in about 100 picoseconds.

Confinement is provided by nothing but the fuel's own inertia.

### Drive approaches

**Indirect drive (NIF).** Lasers enter a small cylindrical **hohlraum** of gold or depleted uranium and heat its inner wall, which re-radiates a near-blackbody X-ray field at a few hundred eV. Those X-rays ablate the capsule.

- *Advantage*: the X-ray bath is highly uniform, which relaxes the beam-symmetry requirement enormously.
- *Disadvantage*: only ~10–15% of laser energy reaches the capsule. Terrible for a power plant.

**Direct drive (OMEGA, most startups).** Lasers illuminate the capsule directly.

- *Advantage*: several times more efficient coupling.
- *Disadvantage*: requires extraordinary beam-to-beam uniformity, and suffers **laser-plasma instabilities** — stimulated Raman and Brillouin scattering redirect laser light, and two-plasmon decay generates hot electrons that pre-heat the fuel and destroy compressibility.

**[[fast-ignition|Fast ignition]].** Compress the fuel with a nanosecond pulse, then ignite it separately with a picosecond petawatt pulse (or a laser-accelerated ion beam). Decoupling compression from heating relaxes the symmetry requirement and could raise gain substantially. Pursued by **[[focused-energy|Focused Energy]]** and **[[marvel-fusion|Marvel Fusion]]**; not yet demonstrated at ignition scale.

**Shock ignition, and "quantum-enhanced" schemes.** Variants that use a final strong shock to ignite, or nanostructured targets to enhance coupling. Marvel Fusion's approach uses nanostructured targets with ultrashort pulses.

### The gap between NIF and a power plant

NIF has demonstrated the physics. It is nothing like a power plant, and the gaps are all engineering:

| Parameter | NIF today | IFE power plant requires |
|---|---|---|
| Repetition rate | ~1 shot per several hours | **10–20 Hz** |
| Laser wall-plug efficiency | ~0.5% | **~10%** |
| Target gain | 4.13 | **50–100+** |
| Target cost | ~$100,000s, hand-made | **<$0.50**, mass-produced |
| Targets per year | ~hundreds | **~500 million** |
| Chamber survival | Replaceable optics, few shots | Must survive 10⁹ shots/yr |

Every one of those is a factor of 10³ to 10⁶. That is the honest scope of the IFE problem — and it is why the August 2026 announcement that **Inertia and LLNL cut cryogenic D-T fuel layering from days to 2–3 hours** matters far more than it sounds: target throughput is a first-order barrier.

DOE's **IFE-STAR** program ($42M across three hubs — Colorado State's RISE, University of Rochester, and LLNL's STARFIRE) targets exactly these gaps, with driver research at 1–10 Hz using krypton fluoride and diode-pumped solid-state lasers.

**Who.** LLNL/NIF and Rochester's LLE (public); **[[xcimer-energy|Xcimer Energy]]** (excimer laser driver, "Athena" plant architecture approved by DOE August 2026), **Focused Energy**, **Marvel Fusion**, **[[first-light-fusion|First Light Fusion]]**, **[[longview-fusion|Longview Fusion]]**, **[[ex-fusion|EX-Fusion]]**, **[[blue-laser-fusion|Blue Laser Fusion]]**, **LaserFusionX**, **[[inertia-enterprises|Inertia Enterprises]]**. **12 companies**.

---

## Part III: [[magneto-inertial-fusion|Magneto-Inertial Fusion (MIF)]]

### The principle

Sit between the two extremes. Embed a magnetic field in the fuel *before* compressing it. The field suppresses thermal conduction losses to the wall and traps charged fusion products, so the fuel does not need to reach ICF densities to burn — relaxing the compression requirement by orders of magnitude. But it is still compressed and pulsed, so it does not need MCF's long confinement times.

The appeal is that it targets the least-demanding corner of parameter space: **10²⁴–10²⁸ m⁻³ and microseconds**, instead of 10³¹/nanoseconds or 10²⁰/seconds.

### Variants

**Magnetized Liner Inertial Fusion (MagLIF).** Sandia's [[z-machine|Z Machine]] drives ~20 MA through a metal liner, imploding it onto pre-magnetised, laser-preheated D-T fuel. Has produced substantial neutron yields and appears in the Lawson-progress dataset as a distinct experimental line.

**Magnetized Target Fusion (MTF).** **[[general-fusion|General Fusion]]**'s approach: inject a magnetised plasma into a rotating cavity of liquid lead-lithium, then collapse the cavity with pneumatic or mechanical pistons. The liquid metal is elegant in principle — it *is* the first wall, *is* the breeding blanket, and *is* the coolant, and being liquid it cannot suffer neutron damage. **LM26 ([[lm26|Lawson Machine 26]])** has reached **0.72 keV** (~8.4 million °C) and is funded through end-2028.

**Pulsed-magnetic / pulser-driven ICF.** **[[pacific-fusion|Pacific Fusion]]** uses coordinated electromagnetic pulses rather than lasers. Its June 2026 milestone: a scaled module prototype delivering **>440 GW peak power at ~1.1 MV**. Pulsed power is enormously more efficient than lasers (>50% wall-plug vs ~10% aspiration), which is the strategic argument for the whole approach.

**Sheared-flow-stabilized Z-pinch.** **[[zap-energy|Zap Energy]]**'s FuZE and FuZE-Q. A classic Z-pinch is violently unstable to sausage and kink modes — this killed the concept in the 1950s. Zap's insight is that a sheared axial flow stabilises those modes, allowing a pinch with **no external magnetic coils at all**. Zap has reported electron temperatures above **1 keV** (>10 million °C). If it works, the machine is radically simpler and cheaper than anything else in fusion.

**Colliding/compressed FRC.** **Helion**: form two FRCs, accelerate them toward each other at over a million mph, collide and compress them magnetically. When the fused plasma expands against the magnetic field, it induces a current directly back into the coils — **direct electricity recovery, no steam cycle**. Helion also targets **D-³He**, breeding its own ³He from D-D side reactions.

**Who.** 9 companies: General Fusion, Zap Energy, Pacific Fusion, Helion (usually classed here), NearStar, Fuse, plus dense plasma focus and plasma-jet variants.

---

## Part IV: Electrostatic and other approaches

**7 companies** in the FIA survey pursue hybrid electrostatic schemes — magnetic-electrostatic confinement, electrostatic cusps, inertial-electrostatic lattice confinement, augmented beam-target.

The classic form is the **Farnsworth-Hirsch fusor**: accelerate ions electrostatically toward a central grid. Fusors work — they are a standard amateur science project — but a fundamental result (the Rider limit and related analyses) shows that any scheme relying on a non-Maxwellian ion distribution in a collisional plasma loses more energy to collisional thermalisation and bremsstrahlung than it gains from fusion. Getting around this requires either recirculating the lost energy at very high efficiency or operating in a regime where the standard analysis does not apply. Companies in this category argue for specific escapes from the theorem; none has demonstrated one.

**[[avalanche-energy|Avalanche Energy]]** pursues a compact magneto-electrostatic "Orbitron" targeting small (kilowatt-scale) modular units and near-term revenue from neutron/isotope applications rather than grid power — a business model worth noting as distinct.

**Muon-catalysed fusion** (1 company). Replace an electron with a muon; the 207× heavier muon orbits 207× closer, screening the nuclear charge so effectively that fusion occurs at room temperature. It genuinely works. The problem is the **alpha-sticking** limit: a muon catalyses roughly 100–150 fusions before sticking to a helium nucleus and being lost, while producing the muon costs far more energy than 150 D-T reactions release. Making this work requires a breakthrough in muon production efficiency of roughly an order of magnitude.

---

## Part V: How to compare them

There is no single figure of merit, but these axes separate the approaches usefully:

| | Tokamak | Stellarator | Mirror | FRC | Laser ICF | MIF |
|---|---|---|---|---|---|---|
| **Physics maturity** | Very high | High | Medium | Low-Medium | High (NIF) | Low-Medium |
| **[[disruption|Disruption]] risk** | **High** | None | None | Low | N/A | N/A |
| **Steady-state capable** | Hard | **Natural** | Natural | Pulsed | Pulsed | Pulsed |
| **Engineering complexity** | Medium | **Very high** | **Low** | Low | Very high | Medium |
| **Beta (field efficiency)** | 1–5% | 4–5% | High | **~1** | N/A | High |
| **Direct energy conversion** | No | No | **Yes** | **Yes** | No | Sometimes |
| **Maintenance access** | Hard | **Very hard** | **Easy** | Easy | Medium | Medium |
| **Aneutronic fuel plausible** | No | No | Maybe | **Yes** | No | Maybe |
| **Nearest net-energy demo** | **SPARC 2027** | 2030s | 2030s | Late 2020s | NIF (done) | Late 2020s |

### The honest assessment

**The tokamak is winning on physics and losing on engineering.** It has by far the strongest empirical basis, the highest achieved performance, and the only near-term credible path to Q>1 in magnetic confinement (SPARC, 2027). It also has disruptions, pulsed operation, and a first wall that must survive being 2 metres from a [[burning-plasma|burning plasma]].

**The stellarator is the best reactor concept and the worst construction project.** No disruptions and inherently continuous operation are exactly what a utility wants. Building the coils is exactly what a utility does not want to pay for. The whole question is whether design optimisation — planar-coil arrays like Thea's, or quasi-single-stage optimisation — can make them buildable at cost.

**Mirrors and FRCs are the high-variance bets with the best endgame.** Simple geometry, easy maintenance, direct energy conversion, and a plausible route to aneutronic fuels. Also the least data.

**ICF has the only demonstrated ignition and the largest engineering gap.** NIF proved the physics that Nuckolls proposed in 1972. Turning that into 20 shots per second with $0.25 targets is a manufacturing problem of a scale the field has never attempted.

**MIF is a genuine attempt to find an easier corner of parameter space**, and its leading exponents — General Fusion's liquid wall, Helion's direct recovery, Zap's coil-free pinch — each solve a *different* one of fusion's engineering problems by construction rather than by effort. If any of them works, it likely works cheaply.

The field's current state is best described not as a race between these but as **a portfolio**, deliberately maintained. The DOE roadmap explicitly funds "Advancing Confinement Approaches" as a challenge area covering tokamaks, stellarators and IFE simultaneously, and the FIA data shows no convergence: the market has emphatically **not** settled on a winner.


## Evidence in `raw/`

Primary sources held in this vault that evidence the claims above:

- [[novel-approach-proton-boron-11-fusion-2026]]

---

**Continue to:** [[04-magnetic-confinement-devices|04 — Magnetic Confinement Devices]] · [[05-inertial-confinement-fusion|05 — Inertial Confinement Fusion]] · [[07-private-fusion-industry|07 — The Private Fusion Industry]]
