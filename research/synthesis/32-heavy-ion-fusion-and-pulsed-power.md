---
title: "Heavy Ion Fusion and Pulsed Power"
type: synthesis
doc: 32
part: 3
aliases:
  - "Heavy Ion Fusion and Pulsed Power"
tags:
  - fusion/synthesis
  - fusion/icf
created: 2026-08-25
updated: 2026-08-29
status: stable
confidence: high
related:
  - "[[05-inertial-confinement-fusion]]"
  - "[[21-the-graveyard]]"
  - "[[26-appendix-quantitative-data]]"
  - "[[33-safety-environment-decommissioning]]"
---
# 32 — Heavy Ion Fusion and Pulsed Power

*Project Lux · The inertial fusion driver that solved the power-plant problem, and was cancelled*

---

## 1. The omission this document corrects

[[05-inertial-confinement-fusion|Document 05]] treated inertial fusion as essentially a laser technology, with pulsed power as a magneto-inertial footnote. That reflects where the money and the headlines are, and it understates the history considerably.

**There is a third ICF driver class — accelerated heavy ion beams — which was pursued in the United States for thirty-five years, was widely regarded as the most credible route to an inertial fusion *power plant* as distinct from an inertial fusion *experiment*, and was cancelled in 2011/12.**

Its story is worth telling because it inverts the usual fusion narrative: this was not a concept that failed on physics. It was a concept whose physics was never seriously doubted, cancelled because the *target* physics it depended on had not yet been demonstrated — by lasers.

Then, in December 2022, lasers demonstrated it.

---

## 2. Heavy ion fusion

### The origin
**In 1976, Denis Keefe at Lawrence Berkeley Laboratory proposed heavy ion beams as inertial fusion drivers.** The proposal was quickly taken seriously, because accelerator technology is mature, industrial and well-understood in a way that high-energy lasers were not.

### Why accelerators are the *right* driver for a power plant

Compare against the IFE driver requirements table in [[05-inertial-confinement-fusion|Document 05]]:

| Power plant needs | Laser status | Accelerator status |
|---|---|---|
| **Wall-plug efficiency ~10%** | ~0.5% (NIF); ~10% aspirational for DPSSL | **25–40%, routinely, today** |
| **Repetition rate 10–20 Hz** | ~1 shot per several hours (NIF); 1–10 Hz in research | **Native. Accelerators run continuously at high rep rate; it is what they are for** |
| **Component lifetime over 10⁹ shots** | Final optics degrade; a known unsolved problem | **Final focusing magnets can stand off metres from the target and be shielded** |
| **Beam-to-target coupling** | Sensitive to laser-plasma instabilities | **Ions deposit by classical stopping power. No LPI, no hot-electron preheat** |

That last row is a physics advantage, not merely an engineering one. A laser's energy is deposited at a critical-density surface and must be transported inward, exposing it to stimulated Raman and Brillouin scattering and two-plasmon decay. **An ion beam deposits its energy volumetrically by well-understood stopping power, with a Bragg peak that can be positioned.** There is no equivalent of laser-plasma instability.

**Heavy ion fusion solves, by construction, the three engineering problems that make laser IFE hard.** That is why the community took it seriously for so long.

### The technology
Point designs for **recirculator drivers** — accelerators in which the beam circulates repeatedly through the same accelerating structure rather than traversing a single long linac — were developed in a **multi-year study by LLNL, LBNL and FM Technologies**. Induction linacs, which accelerate high-current beams with induction cores rather than RF cavities, were the mainstream approach.

The physics problem specific to the concept is **space charge**: a beam intense enough to drive a fusion target contains enough charge that it repels itself, defeating the focusing needed to hit a millimetre target. The solution is **space-charge neutralisation** — injecting plasma or electrons into the beam path to cancel the self-field during final focus. This has been studied experimentally at LBNL and theoretically at Princeton and in Japan.

### The cancellation
**The US programme was terminated in 2011/12.**

The reasoning was defensible at the time. NIF had just been completed and the National [[ignition|Ignition]] Campaign was underway; **nobody had demonstrated ignition**. Building a multi-billion-dollar accelerator driver for a target physics that had not been proven was hard to justify while the facility built to prove it was still trying.

The National Ignition Campaign then failed in September 2012.

### What survived
- The **Heavy Ion Fusion Science Virtual National Laboratory (HIFS-VNL)** — LLNL, LBNL and PPPL
- **NDCX-II** at LBNL, a compact induction accelerator producing a high-quality dense beam to rapidly deliver energy to a solid target. It studies **acceleration, compression and focusing of intense ion beams** in a regime relevant to a driver, and serves the broader warm dense matter community
- Continuing theoretical work on **direct-drive heavy ion beam ICF**, notably in Japan

### The case for revisiting it
The argument has changed since 2011 in exactly one respect, and it is the decisive one.

**Ignition has now been demonstrated eleven times.** The question is no longer *"can a target ignite?"* — it is *"can a driver deliver ignition-scale energy at 15 Hz, at 10% efficiency, for a decade?"*

That is precisely the question heavy ion fusion was designed to answer, and it is precisely the question lasers answer worst. The concept was cancelled for lacking a proof that now exists.

No major programme has restarted it. Given that DOE's IFE-STAR hubs are explicitly targeting *"high-efficiency lasers at high repetition rates"* as a named gap, the omission is at least worth noting.

---

## 3. Pulsed power

### The principle
Store electrical energy slowly, release it in nanoseconds. A capacitor bank charged over minutes can discharge tens of megajoules in under a hundred nanoseconds, producing terawatt-scale electrical power.

The classical architecture:
1. **Marx generator** — capacitors charged in parallel, then switched into series, multiplying the voltage
2. **Pulse-forming line** — usually water-dielectric, which sharpens the pulse and matches impedance
3. **Magnetically insulated transmission lines** — carry the pulse into the load without breaking down
4. **The load** — a wire array, a metal liner, or a plasma column

### Sandia's [[z-machine|Z Machine]]
The largest pulsed-power facility in the world. Roughly **20 megaamperes** delivered to the load in about 100 nanoseconds, from around 20 MJ of stored energy.

Z drives **MagLIF** — Magnetized Liner Inertial Fusion — in which the current implodes a metal liner onto pre-magnetised, laser-preheated D-T fuel. It appears as a distinct experimental line in the Wurzel-Hsu Lawson dataset ([[26-appendix-quantitative-data|Document 26]]), and it also generates the most intense laboratory X-ray source on Earth, used for **Z-pinch-driven hohlraums** and for stockpile stewardship.

### Linear Transformer Drivers
The modern architecture. An **LTD** stacks many small capacitor-and-switch bricks around a common induction cavity, so the voltage is added inductively along an axis rather than through a Marx and a pulse-forming line.

The advantages are directly the ones a power plant needs:
- **Far more compact** — no water lines
- **Higher repetition rate** — bricks recharge quickly
- **Modular** — build the machine from identical units, which is a manufacturing learning-curve argument rather than a construction one
- **Better efficiency** — fewer conversion stages

LTDs are what make a commercial pulsed-power fusion plant conceivable at all, and they are the technology underneath the current commercial entrant.

### [[pacific-fusion|Pacific Fusion]]
The clearest present-day pulsed-power fusion effort. Founded 2023; **over $1 billion committed** in a milestone-tranched Series A.

Its architecture uses **coordinated electromagnetic pulses rather than lasers** to drive [[inertial-confinement|inertial confinement]].

Demonstrated milestones:
- **June 2026: a scaled module prototype delivered more than 440 GW of peak output power at approximately 1.1 MV** in ultra-fast pulses — described as the performance required to ultimately drive fusion conditions
- **20 July 2026: LLNL and Pacific Fusion surpassed 3,000 successful Sirius pulsed-power prototype tests**

That second item is the more informative one. **Three thousand successful shots on a prototype module is a reliability statistic**, and reliability at high shot count is exactly what a pulsed plant needs and what no laser system has demonstrated.

### The efficiency argument
This is the strategic case for the whole category:

| Driver | Wall-plug efficiency |
|---|---|
| Flashlamp-pumped Nd:glass (NIF) | **~0.5%** |
| Diode-pumped solid-state laser | ~10% (aspirational) |
| Krypton fluoride excimer | ~7–10% |
| **Pulsed power** | **>50%** |
| **Heavy ion accelerator** | **25–40%** |

For a plant that must produce net electricity, driver efficiency enters the energy balance directly. A gain-50 target driven by a 10%-efficient laser and a gain-20 target driven by a 50%-efficient pulser deliver comparable plant performance — **and gain 20 is a great deal easier to achieve than gain 50.**

This is the single most important number in inertial fusion energy economics, and it is why the non-laser drivers persist despite lasers having the ignition record.

---

## 4. Why the laser approach dominates anyway

Three reasons, none of them technical superiority for power production:

**1. Ignition was demonstrated with a laser.** NIF exists, works, and produces data. A driver with a demonstrated ignition capability attracts capital regardless of its efficiency.

**2. Laser technology has an enormous adjacent industrial base.** Diode-pumped solid-state lasers benefit from telecom, materials processing and defence investment. Induction accelerators for heavy ion fusion have essentially no adjacent commercial market.

**3. Stockpile stewardship funds laser ICF.** NIF's primary mission is weapons physics; fusion energy is a secondary benefit. Heavy ion fusion has no comparable patron, which is precisely why its budget could be cut in 2011 without affecting a national security mission.

**The uncomfortable observation** is that the driver best suited to a power plant lost to the driver best suited to a weapons programme, for reasons that had little to do with power plants.

---

## 5. Assessment

**Heavy ion fusion is the most credible dormant concept in the field** — more so than the mirror was in 2015, because nothing about it was ever shown not to work. It solves efficiency, repetition rate and final-optics survival simultaneously and by construction. It was cancelled for the absence of a proof that now exists.

**Pulsed power is quietly the most operationally mature ICF driver.** Z has been running for decades; LTDs are modular and manufacturable; Pacific Fusion has 3,000 prototype shots and 440 GW at 1.1 MV. Its weakness is that pulsed-power-driven target physics is far less developed than laser-driven target physics, and it inherits the standoff problem — how to get an enormous current into a target chamber without destroying the transmission line every shot.

**The generalisable lesson** — consistent with [[21-the-graveyard|Document 21]] — is that fusion concepts are killed by budget cycles and by the state of *adjacent* technologies, not usually by their own physics. Heavy ion fusion was cancelled because NIF had not yet ignited. If ignition had come three years earlier, the US inertial fusion energy programme would look completely different today.


## Evidence in `raw/`

Primary sources held in this vault that evidence the claims above:

- [[toward-icf-energy-based-on-heavy-ion-beam]]

---

**Continue to:** [[33-safety-environment-decommissioning|33 — Safety, Environment and Decommissioning]] · [[05-inertial-confinement-fusion|05 — Inertial Confinement Fusion]] · [[21-the-graveyard|21 — The Graveyard]]
