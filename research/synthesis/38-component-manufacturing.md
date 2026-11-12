---
title: "Component Manufacturing"
type: synthesis
doc: 38
part: 3
aliases:
  - "Component Manufacturing"
tags:
  - fusion/synthesis
  - fusion/engineering
  - fusion/manufacturing
created: 2026-08-25
updated: 2026-11-02
status: stable
confidence: high
related:
  - "[[05-inertial-confinement-fusion]]"
  - "[[09-engineering-challenges]]"
  - "[[10-economics-and-markets]]"
  - "[[18-superconductors-and-magnets]]"
  - "[[22-critical-materials-supply-chains]]"
  - "[[23-standards-codes-liability]]"
  - "[[25-failure-case-studies]]"
  - "[[39-the-discourse]]"
---
# 38 — Component Manufacturing

*Project Lux · How you actually build the parts, and why a fleet is a factory problem*

---

## 1. The problem statement

Every other document in this dossier treats components as things that exist: a [[divertor]], a blanket module, a magnet. This one asks how they are made, and the answer determines whether fusion can scale.

The gap between one machine and a fleet is a **manufacturing** gap. [[iter|ITER]] has **54 divertor cassettes** and **440 blanket modules**. A single divertor cassette carries **thousands of [[tungsten-pfc|tungsten]] monoblocks**. A fleet of a hundred plants, each replacing its divertor every year or two, implies **millions of precision-bonded, actively cooled, high-heat-flux components per decade** — produced to nuclear quality standards, from materials that are difficult to machine, joined by processes that are difficult to qualify.

Nobody makes these at that rate. Nobody has ever needed to.

---

## 2. The tungsten monoblock — fusion's defining component

The plasma-facing surface of a modern divertor is built from **monoblocks**: rectangular blocks of tungsten, roughly 25 mm across, each drilled through with a hole carrying a **copper-alloy cooling tube**, threaded onto that tube in a row like beads on a string.

Each monoblock must:
- Survive **10–20 MW/m²** of steady heat flux, plus transients
- Conduct that heat through a **tungsten-to-copper bond** across a large thermal-expansion mismatch
- Endure **thousands of thermal cycles** without the bond failing
- Do all of the above while being neutron-irradiated and eroded

**The bond is the hard part.** Tungsten and copper have very different thermal expansion coefficients, so every thermal cycle works the joint. A single failed bond creates a hot spot that melts, and one melted monoblock can contaminate an entire plasma.

---

## 3. The joining technologies

There is no single answer; several processes are in qualification simultaneously.

| Technique | How it works | Notes |
|---|---|---|
| **HIP** (Hot Isostatic Pressing) | Component held at high temperature under high isostatic gas pressure; diffusion bonds the interfaces and closes porosity | The workhorse. Also used to **close residual pores in additively manufactured parts** |
| **HRP** (Hot Radial Pressing) | **Pressurises only the internal cooling tube**, expanding it against the monoblock, while the joining zone is held in vacuum at bonding temperature | Elegant: radial diffusion bonding without pressurising the whole part. Used for DEMO divertor target mock-ups with advanced W-alloy monoblocks |
| **Brazing** | Filler metal melted at the interface — **Cu-Mn-based fillers** are common | Simpler and cheaper; lower temperature capability |
| **Functionally graded interlayers** | A **W/Cu functionally graded material** between the tungsten and the copper, so the thermal expansion mismatch is spread over a gradient rather than concentrated at a discontinuity | Attacks the root cause rather than the symptom |
| **Diffusion welding** | Solid-state joining under pressure and temperature | Under qualification |
| **Plasma spraying** | W-based coatings deposited directly onto a heat sink | Under qualification; avoids a discrete joint entirely |

### Additive manufacturing enters
The newest route: **tungsten monoblock components produced via Laser Powder Bed Fusion (LPBF), then post-processed by HIP** — the HIP step both closes residual porosity from the printing process *and* simulates the diffusion bond between heat sink and tungsten.

Additive manufacturing is attractive for fusion for reasons beyond geometry: it allows **internal cooling channel designs** that cannot be machined, it reduces the number of joints (each of which is a failure site), and it suits **low-volume, high-complexity** production. DEMO divertor work is exploring **fibre reinforcement combined with additive manufacturing** for the same reason.

Tungsten is, however, among the hardest materials to print — high melting point, high thermal conductivity, brittle, and prone to cracking on rapid solidification. That it works at all is recent.

---

## 4. The qualification result that matters

The most important published number in this area:

> Small-scale tungsten monoblock mock-ups manufactured by **different bonding technologies** were tested under high heat flux in the **ITER Divertor Test Facility**, and **all W monoblocks endured repetitive heat load at 20 MW/m² for 1,000 cycles without failure.**

Two things follow from this.

**First, the technology works.** 20 MW/m² is at the top of the material limit band ([[09-engineering-challenges|Document 09]]), and 1,000 cycles without failure across *multiple different bonding routes* is a genuinely strong result. The divertor's steady-state heat flux problem is, at the component level, solved.

**Second, note what the test did not include.** These were **unirradiated** mock-ups. Neutron irradiation embrittles tungsten, raises its ductile-to-brittle transition temperature, transmutes it to rhenium and osmium, and degrades the copper alloy heat sink. **A component that survives 1,000 cycles at 20 MW/m² fresh is not demonstrated to survive them at 30 dpa** — and, per [[09-engineering-challenges|Document 09]], there is no facility that can find out.

The DOE roadmap's Challenge Area B milestones say exactly this: mid-term, *"test tungsten and Cu-alloy mockups for fatigue, creep, and thermomechanical durability"*; long-term, *"validate tungsten-based and liquid-metal PFCs under fusion-prototypic neutron, heat, and plasma flux"* and *"demonstrate component-scale endurance: recrystallization resistance, crack thresholds, and transmutation effects."*

### Where this is being tested today
- **ITER Divertor Test Facility** — high heat flux qualification
- **[[west|WEST]]** (CEA Cadarache) — high heat flux testing of newly developed tungsten components in an actual [[tokamak]] with an actively cooled tungsten divertor
- **W7-X** — tungsten-based divertor development for a [[stellarator]] geometry
- **[[mpex|MPEX]]** (ORNL) — commissioning to deliver plasma exposure testing, a near-term DOE milestone

---

## 5. Beyond the divertor: the other manufacturing problems

### Blanket modules
Larger, more complex, and made from materials that are themselves not yet qualified. A breeding blanket module contains breeder material, a neutron multiplier, coolant channels, tritium purge paths, and structural steel — all in a component that must be neutronically transparent enough to breed, thick enough to shield, and strong enough to hold pressure.

DOE's near-term materials milestone is telling: **establish domestic industrial heat capability for multi-tonne Fe-alloy and 500 kg V-alloy heats.** A "heat" is a single melt of steel. The United States currently cannot melt fusion-grade reduced-activation steel at industrial scale. That is not a research problem; it is a foundry problem, and it is on the critical path.

### Thick-section welding
Vacuum vessels are made of thick stainless steel sections joined by long welds. [[25-failure-case-studies|Document 25]] documents what happens when this goes wrong: ITER's vessel sectors distorted beyond tolerance during segment welding, invalidating the automated field-joint assembly method for the entire machine.

DOE's long-term milestone — *"qualify domestic manufacturing of thick-section heats and additive builds"* — reflects that this is a capability, not a given.

### HTS magnets
Covered in [[18-superconductors-and-magnets|Document 18]]. The manufacturing summary: ~10,000 km/year of global REBCO tape capacity, cables (VIPER, CORC, HRP-bonded stacks) that must be wound into non-planar geometries, and **the first US modular HTS magnet production line only funded in July 2026** via [[arpa-e|ARPA-E]]'s $20 m to [[thea-energy|Thea Energy]].

### Targets, for inertial fusion
An entirely different manufacturing problem and arguably the largest one in the field. A laser IFE plant at 15 Hz consumes roughly **500 million targets per year**, each a near-perfect sphere with a cryogenic D-T layer, at a unit cost below **$0.50** ([[05-inertial-confinement-fusion|Document 05]]).

The August 2026 **Inertia / LLNL** result — cutting cryogenic D-T fuel layer formation from **days to 2–3 hours**, with a path below an hour, while maintaining ignition-proven tolerances — is a manufacturing result, not a physics one, and it is the most consequential IFE development of the year for exactly that reason.

---

## 6. The transition nobody has made

Fusion components today are made the way research hardware is made: **small batches, hand-finished, individually inspected, by a handful of specialist suppliers, at costs nobody optimises**.

A fleet requires the opposite: **high volume, automated, statistically controlled, multi-sourced, cost-driven** — the transition every technology makes on its way from prototype to product, and the one that generates the learning curve fusion's economics depend on ([[10-economics-and-markets|Document 10]]).

The obstacles are specific:

1. **No qualified materials** means no stable specification to manufacture against ([[23-standards-codes-liability|Document 23]])
2. **No codes** means every component requires bespoke justification, which cannot be automated
3. **No volume** means no supplier will invest in tooling — and no volume exists until plants are built
4. **Concentrated inputs** — tungsten, REBCO, beryllium, Li-6 — cap throughput regardless of demand ([[22-critical-materials-supply-chains|Document 22]])
5. **Nuclear quality assurance** adds documentation and traceability overhead to every part

That third item is the classic chicken-and-egg of first-of-a-kind industries, and it is what the DOE roadmap's **"Seed Fusion Supply Chains"** action and CFS's decision to sell magnets as a merchant product are both attempts to break.

---

## 7. Assessment

**At the component level, fusion's high-heat-flux problem is in better shape than the popular account suggests.** Tungsten monoblocks bonded by several independent routes have survived 1,000 cycles at 20 MW/m² in the ITER Divertor Test Facility. That is a real, qualified, multi-vendor result.

**At the system level, the same components have never been tested irradiated**, and the facility to do so does not exist. This is the same gap that appears in [[09-engineering-challenges|Document 09]], restated in manufacturing terms: *we can build the part, and we cannot yet certify it will survive a reactor.*

**The unglamorous milestones matter most.** A domestic melt capability for multi-tonne reduced-activation steel; a US HTS magnet production line; a cryogenic pellet extrusion system that runs at reactor rates; a target factory. None of these will make a headline, and each of them is a precondition for a fleet.

**The single clearest statement of fusion's real status** may be this: the United States, in 2026, funded its first production line for fusion magnets and does not yet have the industrial capacity to melt fusion-grade structural steel at scale. The physics is nearly ready. **The factories have not been built.**


## 8. Stellarator coils: from bespoke geometry to repeatable planar units

[[wendelstein-7-x]] demonstrates the traditional manufacturing problem: 50 individually complex non-planar superconducting coils held to roughly millimetre-scale geometry. [[thea-energy|Thea Energy]]'s answer is not to improve that production line but to replace it with many simple planar [[rebco]] shaping coils whose currents synthesise the three-dimensional field.

[[canis]] is the first local primary evidence for that manufacturing argument. The programme made **nine complete winding packs from 45 double pancakes**, using REBCO from **three suppliers** without tailoring the baseline process to each supplier. A dedicated line reached roughly **half a day takt time** and **no more than three days total production time per double pancake**. The coils were assembled as a 3 × 3 array and operated at **20 K**. Two static field patterns measured 25 cm from the array had RMS errors of **0.56% and 0.60%** against prediction ([[prototyping-test-canis-hts-planar-coil-array]]).

This closes the recorded gap only at prototype scale. Canis was flat; it did not create toroidal flux, closed flux surfaces, quasisymmetry or a plasma, and it did not reproduce the forces, currents or systems density of [[eos|Eos]]. Transient control, multiple quench scenarios, manufacturing-defect robustness and dense field-shaping-unit integration remained future work. The demonstrated claim is therefore narrower and more useful than “the planar-coil stellarator works”: **repeatable planar HTS coil manufacture and coupled static control have been shown; integrated stellarator performance has not.**

## 9. Vanadium alloy: a material with a process history but no production line

*Added 2026-11-02.*

[[vanadium-alloys|V-4Cr-4Ti]] is the clearest case in this document of a material whose
*metallurgy* is better understood than its *manufacture*.
[[ukaea-2026-vanadium-strategy|UKAEA's vanadium strategy]] compiles the documented heats:

| Heat | Scale | Route |
|---|---|---|
| Industrial (Johnson & Smith) | **1200 kg** | Aluminothermic-reduction V + high-purity Cr/Ti → EBM purification → double vacuum-arc melting → extrusion → warm/cold rolling → repeated vacuum anneal 1000–1050 °C |
| NIFS-HEAT-1 (Muroga *et al.*) | **30 kg**, 200 kg planned | EBM of V, Cr, Ti → vacuum arc remelting; no downstream forming |
| SWIP-30 (Fu *et al.*) | **30 kg** | Double EBM in high vacuum → hot forging → hot rolling (~85% deformation) → cold rolling → vacuum anneal 1273–1293 K |

Three heats, three continents, three decades — and a **1200 kg** ceiling. Tubing technology for
high-purity low-activation V-4Cr-4Ti exists (Nagasaka *et al.* 2003), and gas tungsten arc and
laser welding have been demonstrated with post-weld heat treatment optimised through precipitation
control. So forming and joining are not blank.

**What is blank is qualification and volume.** UKAEA is attempting qualification by a *novel
digital route* — Bayesian optimisation over literature and tensile data to 900 °C producing a
surrogate model, with EPRI engaged for regulatory acceptance — precisely because the
irradiation-and-test campaign the conventional route would demand does not exist and would take
decades. Impurity control is the binding constraint, and a standard composition with impurity
limits has **not yet been specified**.

> [!note] Compare Canis above
> Canis is the pattern this document rewards: a dedicated line, a measured takt time, repeatable
> output. Vanadium has none of those — no takt time, no line, no supplier base. The contrast is the
> point. A design can select a material in a paper far faster than an industry can learn to melt
> it, and [[st-e1|ST-E1]] has selected this one. See [[22-critical-materials-supply-chains]] §5.

---

**Continue to:** [[39-the-discourse|39 — The Discourse]] · [[22-critical-materials-supply-chains|22 — Critical Materials and Supply Chains]] · [[09-engineering-challenges|09 — Engineering Challenges]]
