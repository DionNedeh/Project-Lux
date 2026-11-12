---
title: "Physics Fundamentals"
type: synthesis
doc: 01
part: 1
aliases:
  - "Physics Fundamentals"
tags:
  - fusion/synthesis
  - fusion/physics
created: 2026-08-25
updated: 2026-08-26
status: stable
confidence: high
related:
  - "[[02-history-1920-2026]]"
  - "[[03-confinement-approaches]]"
  - "[[04-magnetic-confinement-devices]]"
  - "[[09-engineering-challenges]]"
  - "[[fusionmae-crossref-metadata-2026]]"
  - "[[tokamak-agnostic-elm-crossref-metadata-2026]]"
  - "[[tcv-predict-first-rampdown-2025]]"
  - "[[hl3-data-driven-rl-control-2025]]"

---
# 01 — Physics Fundamentals

*Project Lux · What fusion actually requires, and why it is hard*

---

## 1. Why fusion releases energy

The binding energy per nucleon curve peaks at iron-56 (~8.8 MeV/nucleon). Everything lighter than iron releases energy when fused; everything heavier releases energy when split. Fusion sits on the steep left-hand side of that curve, which is why it is so energetically favourable: helium-4 is an unusually tightly bound nucleus, and forming it from lighter nuclei liberates a large fraction of the available mass-energy.

For deuterium-tritium fusion, the mass defect corresponds to **17.59 MeV per reaction**. Per unit mass of fuel this is roughly:

- **4× more** energy per kilogram than uranium fission
- **~10 million×** more than burning coal or methane

One gram of D-T fuel, fully burned, releases about **340 GJ** — approximately the energy in 11 tonnes of coal.

---

## 2. The Coulomb barrier and why stars are needed

Two positively charged nuclei repel. To fuse, they must approach within the range of the strong nuclear force (~1 femtometre), against a Coulomb potential of order:

```
V_c = Z₁Z₂e² / (4πε₀ r)  ≈ 1.4 MeV·fm × Z₁Z₂ / r[fm]
```

For D-T (Z₁=Z₂=1) at r = 1 fm, that is roughly **1.4 MeV** — far above any temperature achievable in a laboratory or, for that matter, in the core of the Sun (~1.3 keV).

Fusion happens anyway for two reasons:

1. **Quantum tunnelling.** Nuclei do not need to surmount the barrier; they can tunnel through it. The probability is governed by the Gamow factor, `exp(-√(E_G/E))`, which is exponentially sensitive to energy.
2. **The Maxwellian tail.** In a thermal plasma most particles sit near the mean energy, but the exponential tail contains particles at many times that energy. Because the tunnelling probability rises steeply with energy while the number of available particles falls steeply, the product peaks at a characteristic energy well above the mean — the **Gamow peak**.

The practical consequence: fusion in a thermal plasma is dominated by a small, energetic minority of the ion population, and the reaction rate is extremely sensitive to temperature.

---

## 3. The candidate reactions

| Reaction | Products | Energy release | Neutron fraction | Notes |
|---|---|---|---|---|
| **D + T → ⁴He + n** | α (3.52 MeV) + n (14.07 MeV) | **17.59 MeV** | **80%** | Highest cross-section at lowest temperature. The only realistic near-term fuel. |
| **D + D → T + p** (~50%) | T (1.01) + p (3.02) | 4.03 MeV | 0% | |
| **D + D → ³He + n** (~50%) | ³He (0.82) + n (2.45) | 3.27 MeV | ~66% of this branch | D-D combined needs ~10× the [[triple-product|triple product]] of D-T |
| **D + ³He → ⁴He + p** | α (3.6) + p (14.7) | **18.35 MeV** | ~0% direct | But D-D side reactions still make neutrons. ³He is scarce. |
| **T + T → ⁴He + 2n** | α + 2n | 11.3 MeV | high | Parasitic |
| **p + ¹¹B → 3 ⁴He** | 3 α (8.68 MeV total) | **8.68 MeV** | **~0%** | Aneutronic. Requires ~10× the temperature and defeats bremsstrahlung losses only marginally. |

### Why D-T wins by default

The D-T cross-section peaks at about **5 barns near 64 keV** in the centre-of-mass frame — roughly **100× larger** than D-D at the same energy, and it peaks at a much lower energy than any alternative. In the temperature range where machines actually operate (**10–25 keV**), D-T's Maxwellian-averaged reactivity `⟨σv⟩` is approximately:

```
⟨σv⟩_DT ≈ 1.1 × 10⁻²⁴ · T²  m³/s     (T in keV, valid ~8–25 keV)
```

peaking at about **8.7 × 10⁻²² m³/s near 64 keV**.

This quadratic dependence is why the triple product formulation works, and it is why **every machine that has ever produced significant fusion energy has used D-T** — and why every machine that uses D-T inherits the 14.1 MeV neutron problem described in [[09-engineering-challenges|Document 09]].

### The aneutronic temptation

p-¹¹B is seductive: no neutrons, no tritium, no breeding blanket, no activation, and the possibility of **[[direct-energy-conversion|direct energy conversion]]** from charged alphas to electricity without a steam cycle. Five of the 56 companies in the FIA survey are pursuing it.

The physics is punishing. The Coulomb barrier is five times higher (Z=1×5), the reactivity peaks near **600 keV**, and — critically — **bremsstrahlung radiation losses scale as Z_eff² n² √T**. With boron's Z=5 in the plasma, radiated power tends to exceed fusion power across most of the operating space. Achieving net energy requires either non-Maxwellian ion distributions, alpha-channeling to recycle energy, or operating far from thermal equilibrium — all unproven at scale.

**Status, August 2026**: [[hb11-energy|HB11 Energy]] reported a ~10× increase in measured alpha yield at ELI Beamlines (Czechia) in May 2026 using a chirped-pulse petawatt driver on a boron-hydride target. [[tae-technologies|TAE Technologies]] has reached ~75 million K for ~30 ms — still 5–10× below what p-¹¹B requires. **No facility has demonstrated sustained [[aneutronic-fusion|aneutronic fusion]], let alone breakeven.**

---

## 4. The [[lawson-criterion|Lawson criteria]]

### 4.1 The energy balance

John Lawson's 1955 analysis (declassified 1957) asked a simple question: under what conditions does a fusion plasma produce more energy than it costs to sustain?

Define the **energy confinement time** τ_E as the ratio of stored plasma energy to the power required to maintain it:

```
τ_E = W / P_loss     where  W = 3nT (for a two-species plasma at equal temperature)
```

Power balance for a self-heating plasma requires that the fusion power deposited in charged products exceeds all losses:

```
P_α  ≥  P_conduction + P_bremsstrahlung
```

For D-T, the alpha carries **20%** of the reaction energy (3.52 of 17.59 MeV); the neutron's 80% escapes the plasma immediately and cannot heat it.

### 4.2 The results

Working the balance through gives two commonly quoted forms:

**Lawson parameter ([[ignition]], D-T):**
```
n τ_E  ≳  1.5 × 10²⁰  m⁻³·s        (minimum near T ≈ 25 keV)
```

**Triple product (ignition, D-T):**
```
n T τ_E  ≳  3 × 10²¹  m⁻³·keV·s     (minimum near T ≈ 14 keV)
```

Equivalently, in pressure terms, `p τ_E ≳ 8–10 atm·s`. Real plasmas with peaked profiles and impurities require **roughly 3–5× more** than these idealised figures.

### 4.3 A caution on terminology

Wurzel and Hsu (arXiv:2505.03834) make a point worth repeating: it should be **"Lawson criteria"**, plural. There are two separate requirements — a condition on `nτ_E` *and* a condition on temperature — and "the Lawson criterion" is often used loosely to mean the ignition condition specifically, when Lawson himself was describing criteria for *a useful reactor*, which he took to mean an energy gain of about 2.

---

## 5. Q: the definitions, and how they are abused

This is where most public confusion about fusion lives. There are at least four distinct quantities called "gain".

| Symbol | Definition | What it measures |
|---|---|---|
| **Q_sci** (scientific) | P_fusion / P_heating-into-plasma | The plasma's own performance. **Ignores everything else.** |
| **Q_target** (ICF) | Fusion yield / laser energy delivered to target | NIF's headline number |
| **Q_wp** (wall-plug) | Fusion energy out / total electrical energy drawn from the grid | The honest engineering number |
| **Q_eng** (engineering) | Net electricity exported / total electricity consumed by the plant | What determines whether a plant is a generator or a load |

### The gap between them

NIF's 8.6 MJ shot on 7 April 2025 had **Q_target = 4.13**. But NIF's laser system draws roughly **300–400 MJ from the grid** to deliver 2.08 MJ to the target — a wall-plug efficiency near 0.5%. On a Q_wp basis, that shot was around **0.02**. This is not a criticism of NIF, which was built as a weapons-physics facility and was never designed for efficiency; it is a caution about headlines.

Similarly, [[jet|JET]]'s 69 MJ record (DTE3, 3 October 2023) corresponded to **Q_sci ≈ 0.33**, achieved on a machine consuming hundreds of megawatts of grid power during a pulse.

### Useful landmarks on the Q scale

- **Q = 1** — scientific breakeven. The plasma returns as much as was put into it.
- **Q = 5** — alpha self-heating equals external heating. The plasma is now substantially heating itself.
- **Q ≈ 10** — [[iter|ITER]]'s design target. A genuine **[[burning-plasma|burning plasma]]**: alpha heating is the dominant heat source.
- **Q = ∞** — ignition. External heating can be switched off entirely and the burn sustains itself.
- **Q_eng > 1** — the plant exports power. For a thermal-cycle plant with ~35–40% conversion efficiency and realistic [[recirculating-power|recirculating power]], this typically requires **Q_sci in the range 10–30+**.

That last row is the one that matters commercially, and it is why "breakeven" achieved at Q_sci = 1 is a scientific milestone rather than an economic one.

---

## 6. Magnetic confinement: the governing parameters

### 6.1 [[plasma-beta|Beta]] — the efficiency of magnetic confinement

```
β = plasma pressure / magnetic pressure = 2μ₀ p / B²
```

Typical [[tokamak]] values are **1–5%**. Spherical tokamaks reach higher (20–40%); stellarators typically 4–5%; field-reversed configurations approach β ≈ 1 by construction. Beta is limited by magnetohydrodynamic (MHD) instability. The empirical **Troyon limit** expresses this via normalised beta:

```
β_N = β · a·B / I_p        with β_N ≲ 3–4  (%·m·T/MA) conventionally
```

### 6.2 [[b4-scaling|The B⁴ scaling]] — the single most important design insight

Fusion power density goes as:

```
P_fus/V = ¼ n² ⟨σv⟩ E_fus
```

Since `p = 2nT`, and `⟨σv⟩/T² ≈ constant` over 8–25 keV, this becomes `P_fus/V ∝ p²`. And since `p = β B²/2μ₀`:

```
P_fus / V  ∝  β² B⁴
```

**Fusion power density scales as the fourth power of magnetic field.** Doubling B at fixed beta gives 16× the power density — or allows the same power from a machine of far smaller volume.

This is the entire thesis behind high-field compact tokamaks. Conventional low-temperature superconductors (Nb₃Sn, as used in ITER) top out around 12–13 T on the conductor. **REBCO high-temperature superconducting tape** can operate above 20 T. That difference is why [[sparc|SPARC]] aims to achieve what ITER achieves in roughly **1/40th the plasma volume**, and why the entire private tokamak sector reorganised around HTS after about 2018.

### 6.3 Confinement scaling

Empirical multi-machine regression gives the ITER Physics Basis scaling for [[h-mode|H-mode]] energy confinement, **IPB98(y,2)**:

```
τ_E = 0.0562 · I_p^0.93 · B^0.15 · P^-0.69 · n^0.41 · M^0.19 · R^1.97 · ε^0.58 · κ^0.78
```

Note the exponents: confinement improves strongly with **plasma current** and **major radius**, weakly with field, and *degrades* with heating power (P^-0.69). That last term is why simply adding heating power does not straightforwardly buy performance — a phenomenon called power degradation.

Extrapolating this scaling from present machines to reactor scale is one of the field's persistent uncertainties, and it is a principal reason ITER is as large as it is.

### 6.4 Operational limits

- **[[greenwald-density-limit|Greenwald density limit]]**: `n_G [10²⁰ m⁻³] = I_p[MA] / (π a²[m²])`. Exceeding it historically triggers disruptions. *In January 2026 [[east|EAST]] reported confirming a "density-free region" — a route to operating past this limit — which if it generalises is significant for reactor design.*
- **[[safety-factor|Safety factor q]]**: `q ≈ a B_t / (R B_p)`. Values of q₉₅ below ~2 invite kink instabilities.
- **Disruptions**: a sudden, complete loss of confinement dumping the full plasma thermal and magnetic energy into the wall in milliseconds, plus runaway electron beams. On a reactor-scale machine a single unmitigated [[disruption]] can cause serious damage. Prediction and avoidance is now an active machine-learning problem (see §8).

### 6.5 H-mode, the [[pedestal]], and ELMs

In 1982 on ASDEX, above a threshold heating power, plasmas were observed to spontaneously transition into a **high-confinement mode (H-mode)** with roughly double the energy confinement time. The mechanism is the formation of an **edge transport barrier** — a narrow "pedestal" region of steep pressure gradient at the plasma boundary where turbulence is suppressed by sheared flow.

H-mode is the baseline operating scenario for ITER and essentially every reactor design. It comes with a defect: the steep pedestal periodically collapses in **edge-localised modes (ELMs)**, expelling several percent of the plasma energy onto the [[divertor]] in under a millisecond. Uncontrolled ELMs would destroy a reactor divertor. Mitigation strategies include resonant magnetic perturbations, pellet pacing, and naturally ELM-free regimes such as **quasi-continuous exhaust (QCE)** and **[[negative-triangularity|negative triangularity]]** operation.

### 6.6 Transport

Classical (collisional) transport across field lines would give confinement times of hours. Real plasmas do far worse because of **microturbulence** — drift-wave instabilities driven by the very gradients that confinement creates:

- **ITG** (ion temperature gradient) modes — dominant ion heat transport
- **TEM** (trapped electron modes)
- **ETG** (electron temperature gradient) modes
- **Micro-tearing modes** — increasingly important at high beta

Gyrokinetic codes (GENE, CGYRO, GYRO, XGC) simulate these from first principles at enormous computational cost. The SPARC first-campaign predictions in `papers/SPARC-first-campaign-CGYRO-predictions.pdf` are an example of nonlinear CGYRO being used to forecast a machine's performance before it exists.

**Neoclassical transport** — the collisional transport corrected for toroidal geometry and trapped-particle orbits — sets a floor. In stellarators it is not a floor but a design problem: an unoptimised [[stellarator]] has catastrophic neoclassical losses, which is why **quasi-symmetry** and **quasi-isodynamicity** optimisation exists (see [[04-magnetic-confinement-devices|Document 04]]).

### 6.7 The [[bootstrap-current|bootstrap current]]

A toroidal plasma with a pressure gradient spontaneously drives its own toroidal current — the **bootstrap current** — via trapped-particle dynamics. In a tokamak this is enormously useful: it reduces the external current drive needed for steady-state operation, and advanced scenarios aim for bootstrap fractions above 70%. In a stellarator it is usually a nuisance to be minimised, since the confining field is generated externally by design.

---

## 7. [[inertial-confinement|Inertial confinement]]: a different set of parameters

ICF replaces magnetic confinement with **inertia**: compress fuel so violently that it burns before it can fly apart. Confinement time is set by the disassembly time, of order `R/c_s` — nanoseconds.

The Lawson criteria still apply, but they are reformulated in terms of **[[areal-density|areal density]]**:

```
ρR  [g/cm²]
```

### Key thresholds

- **ρR ≥ 0.3 g/cm²** in the hot spot — the range of a 3.5 MeV alpha in DT at 10 keV. Below this, alphas escape and cannot bootstrap the burn.
- **ρR ≈ 1–3 g/cm²** total fuel — required for high burn fraction
- **Burn fraction**: `f ≈ ρR / (ρR + H_B)` with `H_B ≈ 7 g/cm²`. So even ρR = 3 g/cm² burns only ~30% of the fuel.

### The implosion

- Peak fuel density must reach **~1,000× solid density** (several hundred g/cm³)
- **Implosion velocity** 350–400 km/s
- **Convergence ratio** (initial radius / final hot-spot radius) of **25–40**

That convergence ratio is the crux of ICF's difficulty. Compressing a shell by a factor of 30 in radius while keeping it spherical to within a few percent means suppressing **Rayleigh-Taylor instability** at both the ablation front and the hot-spot interface. Any capsule imperfection — a fill tube, a surface roughness, a dust mote — seeds a spike that can penetrate and [[quench]] the hot spot. This is why the April 2025 record shot's enabling factor was reported as *a higher-quality high-density-carbon (diamond) capsule*, not a change in the laser.

### Drive schemes

- **Indirect drive** (NIF): lasers heat the interior of a gold or depleted-uranium **hohlraum**, which re-radiates a near-Planckian X-ray bath that ablates the capsule. Symmetry is excellent; efficiency is poor (~10–15% of laser energy reaches the capsule).
- **Direct drive** (OMEGA, and most laser-fusion startups): lasers illuminate the capsule directly. Much more efficient, much harder to keep symmetric, and vulnerable to **laser-plasma instabilities** (stimulated Raman and Brillouin scattering, two-plasmon decay) that scatter light and pre-heat the fuel with hot electrons.
- **[[fast-ignition|Fast ignition]]** ([[focused-energy|Focused Energy]], [[marvel-fusion|Marvel Fusion]]): compress the fuel with one pulse, then ignite it with a separate ultra-short petawatt pulse. Decouples compression from ignition, potentially raising gain substantially. Unproven.
- **Magneto-inertial / pulsed magnetic** (Sandia's Z, [[pacific-fusion|Pacific Fusion]]): compress a magnetised fuel column with a pulsed-power-driven liner. Relaxes the density requirement because the embedded magnetic field insulates the fuel and traps alphas.

---

## 8. Alpha physics and the burning-plasma regime

A **burning plasma** is one in which alpha self-heating dominates. This is qualitatively different from anything achieved in magnetic confinement to date, and it is what ITER and SPARC are built to study.

Two new problem classes appear:

1. **Fast-ion confinement.** 3.5 MeV alphas have gyroradii and orbits much larger than thermal ions. If the field has ripple, resonances, or 3D error fields, alphas are lost before they thermalise — losing both the heating and, on the way out, potentially damaging the wall. This is a first-order design constraint for stellarators, whose 3D fields make good fast-ion confinement genuinely hard to arrange.

2. **Alpha-driven instabilities.** A population of super-Alfvénic alphas can resonantly excite **Alfvén eigenmodes** (TAEs, RSAEs, EPMs), which in turn transport the alphas outward — a self-defeating loop. Whether this is benign or severe at reactor scale is not settled, and it is one of the specific things ITER is designed to answer.

Alpha heating also means the plasma becomes a **coupled, self-regulating, nonlinear system**: fusion power depends on temperature, temperature depends on alpha heating, alpha heating depends on fusion power. Control of such a system — avoiding thermal runaway in one direction and quench in the other — has never been demonstrated.

---

## 9. Where AI enters the physics

Machine learning has moved from a peripheral tool to a load-bearing one:

- **Magnetic control.** DeepMind and EPFL demonstrated deep reinforcement learning controlling the full plasma shape and position on the [[tcv|TCV]] tokamak (*Nature*, 2022) — the controller learned to command 19 coils directly, replacing hand-tuned control laws.
- **Instability avoidance.** DeepMind with Korea's KFE and Princeton demonstrated RL that *avoids* tearing instabilities on [[diii-d|DIII-D]] by steering the plasma away from unstable regions in real time (*Nature*, 2024).
- **Disruption prediction.** Fusion Recurrent Neural Network (FRNN) predictors, cross-machine transfer learning, and the DisruptionBench benchmark (2025) are converging on predictors deployable in real-time plasma control systems.
- **Surrogate modelling.** Physics-informed deep learning is being used to predict NIF ignition (*Science*, 2024) and to replace expensive gyrokinetic runs inside design loops.
- **Design optimisation.** Stellarator optimisation has been transformed: quasi-single-stage frameworks fold coil feasibility directly into plasma-boundary optimisation, and latent diffusion models are now generating candidate quasi-isodynamic configurations (arXiv:2608.16938, 2026).

The DOE's June 2026 roadmap treats this as structural, not incidental — it makes an **"AI-Fusion Digital Convergence Platform"** one of only two Build-pillar key actions, alongside physical infrastructure.

---

## 10. A summary table of what must be achieved

| Requirement | D-T value | Status |
|---|---|---|
| Ion temperature | 10–20 keV (100–200 million K) | **Routinely achieved** since the 1990s |
| Triple product for ignition | ~3 × 10²¹ m⁻³·keV·s (ideal) | **Achieved at NIF**; approached in tokamaks |
| Q_sci > 1 | — | **Achieved (ICF only)**, 11 times at NIF |
| Q_sci ≈ 10 (burning plasma) | — | **Never achieved.** ITER 2039; SPARC targeting Q>1 in 2027 |
| Steady-state operation | Hours to continuous | 1,066 s (EAST); 1,337 s ([[hh70|HH70]]) — but not in D-T, not burning |
| Tritium breeding, TBR > 1.1 | — | **Never demonstrated** |
| Materials to 15 dpa/yr | — | **No test facility exists** |
| Divertor heat flux < 10 MW/m² | — | Demonstrated in mitigation experiments; not integrated with a burning core |
| Q_eng > 1 | — | **Never achieved by anyone, anywhere** |

The pattern is clear. The plasma-physics rows are largely green. The engineering rows are largely empty. That asymmetry is the subject of the rest of this dossier.

---

**Continue to:** [[02-history-1920-2026|02 — History 1920–2026]] · [[03-confinement-approaches|03 — Confinement Approaches]] · [[09-engineering-challenges|09 — Engineering Challenges]]
