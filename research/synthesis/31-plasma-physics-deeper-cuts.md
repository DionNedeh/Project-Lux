---
title: "Plasma Physics: The Deeper Cuts"
type: synthesis
doc: 31
part: 3
aliases:
  - "Plasma Physics: The Deeper Cuts"
tags:
  - fusion/synthesis
  - fusion/physics
created: 2026-08-25
updated: 2026-08-26
status: stable
confidence: high
related:
  - "[[01-fusion-physics-fundamentals]]"
  - "[[03-confinement-approaches]]"
  - "[[04-magnetic-confinement-devices]]"
  - "[[17-diagnostics-control-disruption]]"
  - "[[19-simulation-codes-nuclear-data]]"
  - "[[32-heavy-ion-fusion-and-pulsed-power]]"
  - "[[fusionmae-crossref-metadata-2026]]"
  - "[[tokamak-agnostic-elm-crossref-metadata-2026]]"
  - "[[tcv-predict-first-rampdown-2025]]"
  - "[[hl3-data-driven-rl-control-2025]]"

---
# 31 — Plasma Physics: The Deeper Cuts

*Project Lux · The specific physics that decides whether [[iter|ITER]] works*

---

## Scope

[[01-fusion-physics-fundamentals|Document 01]] covered what fusion requires. This covers the physics that determines whether a specific machine achieves it — the phenomena that appear in reactor design margins, that ITER was built partly to resolve, and that would be the actual cause if a next-step machine underperformed.

Five topics: the **L-H transition**, the **[[pedestal]]**, **turbulence self-regulation**, **energetic particle physics**, and **[[burn-control|burn control]]**.

---

## 1. The L-H transition — and the threshold problem

### What it is

Above a threshold heating power, a [[tokamak]] plasma spontaneously reorganises into **[[h-mode|H-mode]]**, with roughly double the energy confinement time. Discovered on ASDEX in 1982; the baseline scenario for essentially every reactor design since.

The mechanism, as currently understood: at the plasma edge, **sheared E×B flow** tears apart the turbulent eddies responsible for transport. Turbulence generates the flow (through Reynolds stress); the flow suppresses the turbulence; the suppression steepens the pressure gradient; the steeper gradient sustains the flow. It is a **bifurcation in a self-regulating system**.

### Why the threshold is a genuine design risk

The empirical scaling used for design is the **ITPA Martin 2008** law:

```
P_L-H = 0.0488 · ⟨n_e,20⟩^0.717 · B_tor^0.803 · S^0.941 · (2/A_eff)
```

where S is plasma surface area and A_eff the effective isotope mass.

**The problem, stated in the literature:** experimental observations from multiple devices demonstrate *"significant departures from the current power threshold empirical scaling law from the 2008 ITPA Martin scaling, which undermines the confidence in the predicted power threshold for ITER."*

This matters concretely. ITER has a **finite installed heating power** — 33 MW of neutral beam plus 20 MW ICRH plus 20 MW ECRH. If its actual L-H threshold exceeds the Martin prediction by enough, **ITER may struggle to access H-mode in some of its planned scenarios**, and H-mode is the basis of the entire Q=10 case.

### The complications

**[[isotope-effect|The isotope effect]].** The threshold scales roughly **inversely with isotope mass** — hydrogen is worst, deuterium better, tritium better still. This is the `(2/A_eff)` term. It is bad news for ITER's early campaigns, which run hydrogen and deuterium precisely to avoid activation, and it means the first attempts at H-mode will be made under the hardest conditions.

**Grad-B drift direction.** Reversing the ion ∇B drift direction relative to the X-point changes the threshold by roughly a factor of two. This is a purely geometric choice with a first-order effect, and it is not fully explained.

**Hidden parameters.** Wall conditioning state, [[divertor]] geometry, neutral density, error fields, and rotation all move the threshold. Work on **reducing the L-H transition power threshold in ITER-similar-shape [[diii-d|DIII-D]] hydrogen plasmas** exists precisely because the community is trying to buy margin.

### The physics underneath

The transition dynamics are *"not fully understood."* What is observed is a **complex interaction between turbulence-driven E×B zonal flow oscillations and geodesic acoustic modes**. Below threshold, plasmas show **limit-cycle oscillations** — competition between turbulence level and zonal-flow shearing, cycling back and forth without locking into H-mode. Cross the threshold and the system locks.

This is one of the cleanest examples in plasma physics of a **predator-prey system**: turbulence feeds the flow, the flow eats the turbulence, and the transition is what happens when the predator wins permanently.

---

## 2. The pedestal

H-mode's confinement bonus lives in a narrow edge region — the **pedestal** — where the pressure gradient is steep and turbulence is suppressed. Because core profiles are roughly *stiff* (their gradients are pinned near a turbulence threshold), **the pedestal height sets the whole plasma's pressure**, and therefore its fusion power. A 20% improvement in pedestal pressure is worth roughly 40% in fusion power.

### EPED

The **EPED** model predicts pedestal height and width from two constraints acting together:
- **Peeling-ballooning MHD stability** — the limit at which the edge current and pressure gradient drive a large-scale instability (this is what an ELM is)
- **Kinetic ballooning mode** — a local turbulence constraint that sets the pedestal *width*

EPED has been notably successful, and it is one of the few genuinely predictive models in tokamak physics.

### Super H-mode

EPED predicts something unexpected: in **strongly shaped plasmas above a critical pedestal density, the pedestal pressure bifurcates** — there is a second, much higher stable branch. This is the **Super H-mode** regime, and it has been accessed experimentally on DIII-D.

If Super H-mode is achievable and sustainable at reactor scale, it is a large free performance gain. Whether it is compatible with a detached divertor and a reactor's density requirements is unresolved — and it is the same core-edge compatibility tension that appears throughout this dossier.

### ELMs, and the regimes that avoid them

The peeling-ballooning limit is not a soft boundary. When the pedestal reaches it, it **collapses** — an **[[elm|edge-localised mode]]** expelling several percent of the plasma's stored energy onto the divertor in under a millisecond. Uncontrolled Type-I ELMs would destroy a reactor divertor.

The escape routes, in rough order of maturity:
- **Resonant magnetic perturbations** — 3D fields that degrade the pedestal slightly and suppress ELMs entirely. Works; costs confinement
- **Pellet pacing** — trigger small ELMs deliberately before large ones can build
- **Quasi-continuous exhaust (QCE)** — a naturally small-ELM regime; **demonstrated in D-T on [[jet|JET]]'s DTE3**
- **X-point radiator (XPR)** — a stable strongly radiating region near the X-point; **also demonstrated in D-T on JET**
- **[[negative-triangularity|Negative triangularity]]** — reverse the plasma cross-section curvature. Access to good confinement **without an H-mode pedestal at all**, and therefore without ELMs. The basis of the [[manta|MANTA]] design
- **I-mode, EDA H-mode, QH-mode** — naturally ELM-free regimes with varying reactor relevance

That JET demonstrated **two** of these in actual deuterium-tritium plasmas in its final campaign is, in retrospect, one of the most valuable results it produced.

---

## 3. Turbulence self-regulation and the isotope effect

### Zonal flows
The organising concept in modern transport physics. Turbulence in a magnetised plasma **spontaneously generates its own large-scale sheared flows** (zonal flows), which then shear apart the turbulence that made them. Confinement is therefore not a fixed property but the equilibrium of a self-regulating loop, and small changes in the loop's parameters produce disproportionate changes in transport.

This is why confinement scaling laws are empirical rather than derived, and why gyrokinetic simulation is expensive: you cannot get the answer without resolving the loop.

### The isotope effect — an unsolved problem hiding in plain sight
Simple gyro-Bohm theory says confinement should **degrade** with increasing isotope mass. Experiments consistently show it **improves**: deuterium plasmas confine better than hydrogen, and D-T better still.

**This has never been fully explained.** It matters enormously, because every reactor projection is extrapolated from deuterium experiments to D-T operation, and the direction and magnitude of the isotope correction is a real uncertainty in those projections. JET's D-T campaigns were among the few opportunities to measure it directly.

### Turbulence spreading and non-locality
Turbulence generated in one region propagates into adjacent regions, so transport is not purely local to the gradient. This breaks the assumptions of the reduced transport models used inside design codes, and it is one of the reasons high-fidelity gyrokinetics remains necessary ([[19-simulation-codes-nuclear-data|Document 19]]).

---

## 4. Energetic particle physics

In a [[burning-plasma|burning plasma]], 3.5 MeV alphas constitute a population of **super-Alfvénic** particles — moving faster than the Alfvén speed — carrying a substantial fraction of the plasma's energy. This creates a physics regime that only ITER and [[sparc|SPARC]] will access.

### Alfvén eigenmodes
A population of fast ions with a spatial gradient can resonantly drive **Alfvén eigenmodes** — TAEs (toroidicity-induced), RSAEs (reversed-shear), EPMs (energetic particle modes). The modes then transport the fast ions outward.

The loop is self-defeating: alphas drive the mode, the mode expels the alphas, the alphas no longer heat the plasma — and on the way out they can strike the wall in localised spots.

**Whether this is benign or severe at reactor scale is not settled.** It is one of the specific things ITER exists to determine, and it cannot be resolved by scaling from present machines because present machines cannot make a comparable alpha population.

### Fast-ion confinement in 3D
For stellarators this is a **design constraint rather than a phenomenon**. Fast alphas in a 3D field follow complex orbits, and an unoptimised [[stellarator]] loses them promptly. [[quasi-symmetry|Quasi-symmetry and quasi-isodynamicity]] optimisation ([[04-magnetic-confinement-devices|Document 04]]) exist substantially to fix thermal transport, but **good fast-alpha confinement is a separate and harder objective**, and it is a live question for every stellarator power plant design.

### Alpha channelling
A speculative but serious idea: use waves to **extract energy from alphas and give it to fuel ions** before the alphas thermalise, simultaneously improving heating efficiency and removing [[helium-ash|helium ash]] faster. It appears in the p-¹¹B literature as one of the few routes that could make aneutronic fuels economic ([[03-confinement-approaches|Document 03]]). Not demonstrated.

---

## 5. Burn control — the thing nobody has ever done

A burning plasma is a **positive-feedback thermal system**:

```
Fusion power → alpha heating → temperature ↑ → reactivity ↑ → fusion power ↑
```

Over the operating range of roughly 10–20 keV, `⟨σv⟩` rises steeply with temperature, so the loop gain is greater than one. Left alone, a burning plasma does one of two things: it **runs away thermally** until a pressure or density limit ends the discharge — usually violently — or it **quenches**.

### The control problem
Actuators available: fuelling rate, auxiliary heating, impurity seeding (to increase radiation), and in principle plasma shaping. All of them act on **timescales of seconds**. The plasma's thermal response is faster.

There are further complications:
- **Helium ash accumulation** dilutes the fuel over time, which is a slow *negative* feedback that partially self-stabilises but degrades performance
- **Impurity accumulation** in the core can [[quench]] the burn abruptly
- **Sawteeth and other MHD** periodically redistribute the core, including the alpha population
- A **detached divertor** must be maintained simultaneously, using impurity seeding that also affects the core

**No machine has ever done this.** ITER's Q=10 scenario and SPARC's Q>1 attempt will be the first tests, and burn control instability is a plausible failure mode that would look, from outside, like the machine simply not reaching its target.

### Start-up
A related and under-discussed problem: **how do you get to a burning plasma from cold?** The sequence — breakdown, current ramp, L-mode, L-H transition, density ramp, entry into the burning regime — must be traversed without hitting a density limit, a beta limit, or an MHD instability, on a machine where the plasma's properties change qualitatively partway through.

ITER's specific version of this is harder than most, because its superconducting central solenoid cannot supply high loop voltage. Breakdown at **low toroidal inductive electric field** is consequently a research topic in its own right, and **[[jt-60sa|JT-60SA]]'s demonstration of first plasma at 0.15 V/m** was deliberately an ITER-relevant result ([[04-magnetic-confinement-devices|Document 04]]).

---

## 6. Why this matters for reading claims

Each item above is a place where a machine can quietly fail to meet projection **without anything dramatic happening**:

| Phenomenon | Failure mode | Would look like |
|---|---|---|
| L-H threshold higher than Martin scaling | Cannot access H-mode with installed power | "Confinement below expectation" |
| Pedestal lower than EPED predicts | Core pressure caps out | "Q below target" |
| Isotope effect smaller than assumed | D-T does not outperform D as projected | "Extrapolation was optimistic" |
| Alfvén eigenmodes expel alphas | Reduced self-heating | "Alpha heating anomaly" |
| Burn control unstable | Cannot sit at the operating point | "Discharge terminated early" |
| Helium ash accumulation | Progressive dilution | "Performance decays through the pulse" |

None of these would be a scandal. All of them are ordinary physics, well within the range of what the field considers possible, and **any of them could mean SPARC returns Q = 0.8 rather than Q = 2** — which would be reported as a failure and would in fact be a result.

Conversely, **Super H-mode, a favourable isotope effect, and benign alpha physics** would push in the other direction, and a machine designed with ARC-style margin might comfortably exceed its stated goal.

The honest position on SPARC and ITER is that the **error bars on the projections are wider than the projections' own stated targets**, and that this is normal for a first-of-a-kind experiment in an unexplored regime.

---

**Continue to:** [[32-heavy-ion-fusion-and-pulsed-power|32 — Heavy Ion Fusion and Pulsed Power]] · [[17-diagnostics-control-disruption|17 — Diagnostics, Control and Disruption]] · [[01-fusion-physics-fundamentals|01 — Physics Fundamentals]]
