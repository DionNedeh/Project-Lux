---
title: "Diagnostics, Control and Disruption Mitigation"
type: synthesis
doc: 17
part: 2
aliases:
  - "Diagnostics, Control and Disruption Mitigation"
tags:
  - fusion/synthesis
  - fusion/engineering
  - fusion/subsystems
created: 2026-08-25
updated: 2026-08-26
status: stable
confidence: high
related:
  - "[[16-heating-current-drive-fuelling]]"
  - "[[18-superconductors-and-magnets]]"
  - "[[19-simulation-codes-nuclear-data]]"
  - "[[fusionmae-crossref-metadata-2026]]"
  - "[[tokamak-agnostic-elm-crossref-metadata-2026]]"
  - "[[tcv-predict-first-rampdown-2025]]"
  - "[[hl3-data-driven-rl-control-2025]]"

---
# 17 — Diagnostics, Control and [[disruption|Disruption]] Mitigation

*Project Lux · How you measure something at 150 million degrees that destroys your instruments, and how you stop it killing your machine*

---

## 1. The problem nobody outside the field thinks about

You cannot put a thermometer in a fusion plasma. Every measurement must be made **remotely** — by intercepting light, particles or fields that escape — and every instrument that does the intercepting sits in an environment specifically designed to be hostile to matter.

This creates a paradox that gets worse as fusion gets better:

> **A [[burning-plasma|burning plasma]] is harder to measure than a non-burning one, precisely because it is burning.**

The neutron and gamma fluxes that signify success are the same fluxes that darken windows, degrade detectors, induce spurious voltages in magnetic coils, and heat components that must remain dimensionally stable to microns.

[[iter|ITER]] will carry roughly **40 individual measurement systems** spanning magnetics, neutron diagnostics, optical and spectroscopic systems, bolometry and microwave diagnostics. Getting them to survive is one of the least glamorous and most schedule-critical parts of the project.

---

## 2. The core diagnostic techniques

### Magnetics — the foundation
Pickup coils, flux loops, Rogowski coils and saddle loops measure the magnetic field around the plasma. From these, equilibrium reconstruction codes infer plasma position, shape, current and stored energy — in real time, every millisecond, feeding the control system.

**Everything else depends on this.** If magnetics fail, the plasma cannot be controlled at all.

**Why a burning plasma breaks them:** magnetic diagnostics integrate a voltage to get a flux. Over a 400- or 3,600-second pulse, any small offset — and **radiation-induced electromotive force** in the cabling produces exactly such an offset — integrates into a large, drifting error. Steady-state magnetic measurement is an unsolved-in-practice problem that ITER addresses with Hall sensors and steady-state magnetic sensors alongside conventional inductive ones.

### Thomson scattering — the gold standard
Fire a high-power laser through the plasma and collect the tiny fraction of light scattered by free electrons. The Doppler broadening of the scattered spectrum gives **electron temperature**; the total scattered intensity gives **electron density**. Spatially resolved, absolutely calibrated, and theoretically clean.

This is the technique the Culham team carried to Moscow in 1969 to verify [[t-3|T-3]] — the measurement that converted the world to tokamaks.

**Why a burning plasma breaks it:** it needs windows, mirrors and a clear optical path. See §3.

### Charge-exchange recombination spectroscopy (CXRS)
Inject a neutral beam; beam neutrals donate electrons to fully stripped impurity ions (typically carbon or helium), which then emit characteristic light. The Doppler width gives **ion temperature**, the shift gives **rotation velocity**, and the intensity gives **impurity density**.

Ion temperature is the quantity that actually determines fusion rate, so this is not optional. It requires both a neutral beam and clean optics.

### Motional Stark effect (MSE)
The Stark splitting of beam-emission lines, in the electric field the beam particles see as they move through the magnetic field, encodes the **local magnetic field pitch angle** — and hence the **current density profile**, which is otherwise almost unmeasurable and which determines MHD stability.

### Interferometry and reflectometry
Microwave or laser beams probe the plasma's refractive index to give **line-integrated density** (interferometry) or **density profiles and fluctuations** (reflectometry). Microwave systems are far more radiation-tolerant than optical ones, which is why reflectometry is expected to carry more of the load on reactor-class machines.

### Bolometry
Measure **total radiated power** and its spatial distribution — essential for [[divertor]] [[detachment]] control and for detecting impurity accumulation.

### Neutron diagnostics
The only direct measurement of **fusion power**. Neutron flux monitors, activation foils, and neutron cameras give yield, and neutron spectrometry gives ion temperature from Doppler broadening of the 14.1 MeV peak. On a burning plasma these become the primary performance diagnostic — and they are the one class of instrument that *benefits* from a high neutron flux.

---

## 3. Why burning-plasma diagnostics are genuinely hard

The environment: **high neutron and gamma fluxes, volumetric nuclear heating, particle bombardment, and radiation loads across the entire electromagnetic spectrum**. Specific failure mechanisms:

### First-mirror degradation — the canonical problem
Every optical diagnostic needs a mirror inside the vacuum vessel with a direct line of sight to the plasma. That mirror is simultaneously:
- **Eroded** by charge-exchange neutrals sputtering its surface
- **Coated** by material eroded from elsewhere and redeposited on it

Both change its reflectivity, and both change it *non-uniformly and unpredictably over time*. A diagnostic whose absolute calibration drifts is a diagnostic that cannot measure absolute quantities. Mitigations — plasma cleaning by RF discharge, shutters, careful duct geometry, single-crystal molybdenum or rhodium mirror materials — are all partial.

The IOP special issue chapter *"Diagnostics"* in **On the path to [[tokamak]] burning plasma operation** (Nucl. Fusion, 2025) is the current authoritative review, and its overall message is that **the hardest measurements are precisely those involving visible radiation** — Thomson scattering, CXRS and MSE. These are also, inconveniently, the measurements that give temperature, rotation and current profile.

### Window darkening
Fused silica and sapphire windows develop colour centres under neutron and gamma irradiation, absorbing exactly the light the diagnostic is trying to collect.

### Detector damage
Semiconductor detectors accumulate displacement damage and leakage current. Research on ultra-thin 3D silicon detectors and on radiation-hard alternatives (diamond, SiC) is active — and the **University of Arizona's July 2026 demonstration of graphene nanoribbons as radiation sensors for fusion plants** is one of the more interesting recent entries.

### Nuclear heating and dimensional stability
Diagnostic components absorb volumetric heating and move. A mirror that shifts by tens of microns has re-pointed the diagnostic.

### The port competition, again
Every diagnostic needs a line of sight. Every line of sight is a hole in the breeding blanket. **Diagnostics, heating systems and the [[tritium-breeding-ratio|tritium breeding ratio]] are all competing for the same wall area** — a constraint that recurs throughout this dossier and that no design has fully resolved.

---

## 4. Control: from feedback loops to reinforcement learning

### What must be controlled, simultaneously
- Plasma position and shape (millisecond timescale, or the plasma hits the wall)
- Plasma current and current profile
- Density (via fuelling)
- Temperature and stored energy (via heating)
- Divertor detachment state (via impurity seeding)
- MHD modes — NTMs, sawteeth, ELMs, resistive wall modes
- **[[burn-control|Burn control]]** — in a burning plasma, fusion power is a function of temperature and temperature is a function of fusion power

That last one is new and has never been done. A burning plasma is a **coupled nonlinear system with positive feedback**. Too much alpha heating and the plasma can run away thermally until a pressure limit ends it violently; too little and it quenches. Managing that with actuators that respond in seconds, against a plasma that responds in milliseconds, is one of ITER's genuine open questions.

### The AI transition

Fusion control has moved from hand-tuned PID loops toward learned controllers faster than almost any other physical-systems domain:

- **Magnetic control by deep reinforcement learning** (DeepMind + EPFL, *Nature* 2022): a single RL agent commanded all 19 shaping coils on [[tcv|TCV]] directly, achieving plasma configurations that would have required bespoke controller design.
- **Tearing-instability avoidance** (DeepMind + KFE + Princeton, *Nature* 2024): an RL controller on [[diii-d|DIII-D]] that steers the plasma *away* from tearing-unstable regions in real time — prevention rather than suppression.
- **Disruption prediction**: Fusion Recurrent Neural Network predictors, cross-machine **transfer learning** (training on small tokamaks and transferring to large ones), and the **DisruptionBench** benchmark (*J. Fusion Energy*, 2025) which finally gave the field a common evaluation standard.
- **Physics-informed deep learning to predict NIF [[ignition]]** (*Science*, 2024).
- **Latent-space surrogates for divertor detachment control** — replacing expensive edge simulations with fast learned models inside the control loop.

DOE's June 2026 roadmap institutionalises this: the **AI-Fusion Digital Convergence Platform** is one of only two Build-pillar key actions, and Challenge Area C's mid-term milestones include "deploy digital twins for scenario modeling and predictive control."

**The caveat worth stating.** A learned controller is only as good as its training distribution, and no machine has ever trained on burning-plasma data because none exists. The first burning plasmas will be controlled by systems extrapolating outside their experience — which is an argument for conservative operation early, and for the transfer-learning research now underway.

---

## 5. Disruptions

### What happens

A disruption is the sudden, complete loss of plasma confinement. It proceeds in stages, and the whole event takes milliseconds:

1. **Thermal [[quench]]** — the plasma's entire thermal energy (hundreds of megajoules in ITER) is deposited on the wall in **under a millisecond**
2. **Current quench** — the plasma current collapses, and the changing flux induces enormous **eddy currents and electromagnetic forces** in the vessel structure. ITER's vessel is designed for tens of meganewtons of disruption loading
3. **Runaway electron generation** — the loop voltage during the current quench can accelerate electrons to tens of MeV, forming a beam carrying a large fraction of the original plasma current

### Why [[runaway-electrons|runaway electrons]] are the serious problem

In a sufficiently hot, dense plasma, drag on an electron *decreases* with energy above a threshold. An electron above that threshold accelerates freely — it "runs away." Worse, a runaway can knock a thermal electron into the runaway population, producing **avalanche multiplication that scales exponentially with plasma current**.

A multi-megaampere, multi-MeV electron beam striking the first wall does not spread its energy: it deposits it in a localised volume centimetres deep, melting and potentially perforating components.

**And the problem gets worse with machine size**, because avalanche gain scales with current. ITER at 15 MA is far more exposed than any existing machine. This is the tokamak's characteristic design vulnerability, and it is the strongest single argument for stellarators, mirrors and FRCs.

### [[shattered-pellet-injection|Shattered Pellet Injection]] — the mitigation

**SPI**, first demonstrated at **DIII-D in 2010**, is ITER's disruption mitigation system.

The method: fire large cryogenic pellets — for ITER, a **neon-hydrogen mixture** — down a guide tube that ends in a bend plate. The pellet **shatters** into a spray of fragments before entering the plasma. The fragments ablate rapidly and distribute material far more effectively than an intact pellet, radiating the thermal energy away **isotropically** (protecting the divertor from a localised dump) and raising the plasma density enormously, which increases collisional drag on incipient runaways.

### The two-stage refinement

Recent modelling shows that a **staggered injection** — pure hydrogen first, then a mixed hydrogen-neon pellet — substantially improves fragment assimilation and suppresses the **hot-tail** runaway generation mechanism, in which the fastest electrons fail to cool during a rapid thermal quench and become the runaway seed.

Dividing the injection into two stages significantly enhances assimilation and reduces runaway generation compared to a single-stage injection.

### The result that should be more widely known

Here is the finding that deserves emphasis, from the current modelling literature using the **DREAM** framework:

> **Megaampere-scale runaway currents are found in 15 MA discharges even in non-activated scenarios. With staggered injection outperforming single-stage — including in cases with radioactive runaway sources — no cases with acceptable runaway electron currents were found for a D-T plasma.**

The reason a D-T plasma is worse is intrinsic. Tritium beta decay and Compton scattering of gamma rays from activated structures **continuously generate runaway seed electrons**, and unlike hot-tail seeds, these cannot be removed by cooling the plasma faster. Every seed then feeds the avalanche.

So as of 2026, **ITER's disruption mitigation strategy does not have a demonstrated solution for its full-current D-T scenario.** Approaches under investigation include post-thermal-quench SPI specifically for seed depletion, passive 3D coils that deliberately destroy the magnetic surfaces the runaway beam needs, and simply operating in regimes where disruptions are less likely. [[sparc|SPARC]] has its own published study of runaway generation under deuterium and noble-gas injection (arXiv:2502.19891).

This is not a reason to think tokamaks will not work. It is a concrete, currently-unsolved engineering problem on the critical path of the world's largest fusion project, and it is far less discussed than tritium breeding or materials.

### Vertical displacement events
A related failure: elongated plasmas are vertically unstable and held in place by active feedback. If control is lost, the plasma column moves vertically into the wall, driving **halo currents** through the structure that produce large mechanical forces. VDE loads are a primary structural design case for ITER's vessel and in-vessel components.

---

## 6. Round 4 evidence update: transfer and bounded live control

The 2025–26 record now separates four levels that the earlier “AI control” label compressed. [[fusionmae-crossref-metadata-2026|FusionMAE]] learns reusable representations from 2,445 HL-3 discharges but remains an offline evaluation. [[tokamak-agnostic-elm-crossref-metadata-2026|Cross-machine ELM forecasting]] transfers a DIII-D-trained model to KSTAR without weight retraining, but forecasts rather than suppresses the instability. [[tcv-predict-first-rampdown-2025|TCV predict-first experiments]] and [[hl3-data-driven-rl-control-2025|HL-3 data-driven control]] reach bounded live-machine actuation.

These results strengthen the claim that control is becoming data-driven while narrowing it: none demonstrates indefinite autonomous plant operation. The assurance boundary—training support, uncertainty, independent protection and authorised operating envelope—is now part of the control problem. See [[40-ai-for-fusion-transferable-control|Document 40]].

## 7. What this means

**Diagnostics are a hidden schedule risk.** They are usually the last systems specified, the first to be descoped under budget pressure, and the ones that determine whether an expensive campaign produces interpretable data. A machine that runs but cannot measure its own ion temperature profile has not answered the question it was built to answer.

**Control has become an AI problem faster than anyone expected**, and the field has genuine, published, machine-validated results — not aspirations. This is one of the areas where fusion is moving faster than its own roadmaps assumed.

**Disruptions remain the tokamak's structural weakness**, and the honest 2026 position is that mitigation for a full-current D-T disruption is not yet demonstrated even in simulation. Concepts without a large plasma current — stellarators, mirrors, FRCs, Z-pinches — do not have this problem at all, and that advantage is worth more than it is usually credited.

---

**Continue to:** [[18-superconductors-and-magnets|18 — Superconductors and Magnet Engineering]] · [[19-simulation-codes-nuclear-data|19 — Simulation, Codes and Nuclear Data]] · [[16-heating-current-drive-fuelling|16 — Heating, Current Drive and Fuelling]]
