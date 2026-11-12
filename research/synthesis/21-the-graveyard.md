---
title: "The Graveyard"
type: synthesis
doc: 21
part: 2
aliases:
  - "The Graveyard"
tags:
  - fusion/synthesis
  - fusion/history
  - fusion/machines
created: 2026-08-25
updated: 2026-08-29
status: stable
confidence: high
related:
  - "[[02-history-1920-2026]]"
  - "[[22-critical-materials-supply-chains]]"
  - "[[25-failure-case-studies]]"
---
# 21 — The Graveyard: Failed, Cancelled and Dormant Concepts

*Project Lux · What did not work, what was killed, and which corpses are still twitching*

---

## Why a dossier needs this chapter

A survey that lists only surviving approaches produces survivorship bias. Fusion's history contains a large number of concepts and projects that were funded, pursued seriously by competent people, and did not work — and the reasons they failed are more informative than most success stories.

There are three distinct categories, and conflating them is a common error:

- **Physically dead** — the concept was tested and the physics does not permit net energy
- **Killed** — the concept was never disproved; the money stopped
- **Dormant** — abandoned for a reason that a later technology removed

That third category is the one that should make anyone cautious about writing off an approach. **The [[stellarator]] was dead in 1969 and holds the long-pulse triple-product record in 2026. The [[magnetic-mirror|magnetic mirror]] was cancelled in 1986 and set the field record in 2024.** Nothing in fusion stays buried if an enabling technology arrives.

---

## Part I: Physically dead — or close to it

### The classic Z-pinch (1950s)

**The idea.** Run a current through a plasma column; its own magnetic field pinches it. Elegant, requires no external field coils at all.

**Why it failed.** The pinch is violently unstable to **sausage (m=0)** and **kink (m=1)** modes. Any small constriction increases the local field, which increases the pinch, which increases the constriction — collapse in microseconds. The instabilities also accelerate ions to high energy, producing **beam-target neutrons that look thermonuclear but are not** — the error that destroyed [[zeta|ZETA]]'s 1958 claim.

**The twitch.** **[[zap-energy|Zap Energy]]** ($338 m) argues that **sheared axial flow** stabilises exactly these modes, and has demonstrated electron temperatures above 1 keV in FuZE. If sheared-flow stabilisation holds at reactor-relevant currents, the resulting machine is radically simpler and cheaper than anything else in fusion — no external coils at all. That is a large "if" against seventy years of contrary evidence, which is precisely why it is interesting.

### The Farnsworth-Hirsch fusor and inertial electrostatic confinement

**The idea.** Accelerate ions electrostatically toward a central grid or virtual cathode; they fuse at the focus.

**Why it does not scale.** Fusors work — they are a standard amateur physics project and a legitimate commercial neutron source. As power plants they run into a fundamental result. Any scheme relying on a **non-thermal ion distribution in a collisional plasma** loses energy to collisional thermalisation and bremsstrahlung faster than it gains it from fusion. The **Rider analysis** (1995) formalised this for a broad class of non-equilibrium schemes, and grid losses compound it — ions that hit the grid are gone, and the grid erodes.

**The twitch.** Seven companies in the FIA survey pursue hybrid electrostatic approaches, each arguing a specific escape from the theorem — a virtual cathode, magnetic shielding of the grid, or operation in a regime the analysis does not cover. **[[avalanche-energy|Avalanche Energy]]'s Orbitron** is the best-funded ($104 m); it combines magnetic and electrostatic confinement and deliberately targets small modular units rather than grid power, which sidesteps the scaling problem by not attempting it. **[[astral-systems|Astral Systems]]** sells the neutrons rather than the electricity.

### Muon-catalysed fusion

**The idea.** Replace an electron in a hydrogen molecule with a muon, 207 times heavier. The muonic molecule is 207 times smaller, the nuclei sit close enough to tunnel, and **fusion proceeds at room temperature.** This genuinely works and was verified decades ago.

**Why it fails.** Two hard numbers:
- **Alpha sticking.** After each fusion, the muon has roughly a 1% chance of sticking to the resulting helium nucleus and being removed from the cycle. So one muon catalyses about **100–150 fusions** before it is lost.
- **Muon production cost.** Producing a muon costs several GeV. 150 D-T fusions release about 2.6 GeV. The energy balance is negative before any inefficiency is counted.

Closing the gap needs roughly an **order of magnitude improvement in muon production efficiency**, or a solution to alpha sticking, and neither has a credible route.

**The twitch.** **Acceleron Fusion** (Cambridge, MA, $26.5 m, founded 2023) pursues **"active-target muon production and high-density fusion cell"** — attacking both terms simultaneously. It is one company in fifty-six, appropriately sized to the odds.

---

## Part II: Killed — the concept was never disproved

### [[mftf-b|MFTF-B]] — the canonical cautionary tale

**The Mirror Fusion Test Facility** at Lawrence Livermore was a tandem mirror, the culmination of a decade of US mirror research.

- Cost **$372 million** — at the time, **the most expensive project in LLNL history**
- **Construction completed in 1986**
- Its operational budget was cancelled in the same year, amid Reagan-era energy research cuts
- **Formally cancelled in 1987 and disassembled without ever operating**

Read that sequence again. A $372 million machine was completed and then dismantled without a single plasma shot. It remains the reference case for what happens when a fusion programme's political support evaporates faster than its construction schedule, and it effectively ended US mirror research for thirty years.

**The resurrection.** In July 2024, the **Wisconsin HTS Axisymmetric Mirror ([[wham|WHAM]])** confined a plasma at **17 tesla** — the highest field ever applied to a fusion plasma. **[[realta-fusion|Realta Fusion]]** ($58.8 m) is commercialising it, and in June 2026 became **the first commercial fusion company to demonstrate [[direct-energy-conversion|direct energy conversion]]**. CFS is supplying its magnets.

What changed was not the physics of end losses. It was **HTS magnets**, which allow mirror ratios that were unattainable in the 1980s — and a higher mirror ratio directly shrinks the velocity-space loss cone that killed the concept. The mirror was dormant, not dead, and it was waiting for a conductor.

### The stellarator, 1969–2015

Abandoned worldwide within two years of the [[t-3|T-3]] results, because an unoptimised 3D magnetic field has catastrophic **neoclassical transport** — collisionless particle orbits that simply do not stay confined.

What changed was **computation**. Once it became possible to numerically optimise a 3D field for **quasi-symmetry** or **quasi-isodynamicity**, the transport problem became tractable by design. W7-X now holds the triple-product record for pulses over 10 seconds, and **stellarators (8) outnumber tokamaks (5) among private fusion companies.**

### Dense Plasma Focus

Developed as a fusion power device from the **early 1960s**. Scaling studies showed it would not reach commercially useful conditions, and **since the 1980s it has been used primarily as a teaching system and as a neutron and X-ray source** — a real and continuing application.

**The twitch.** **LPPFusion** pursues "Focus Fusion" — DPF aimed at **p-¹¹B**, using the plasmoid's very high density and the possibility of non-thermal ion distributions. It is one of the field's longest-running small efforts.

### Other cancelled machines

| Project | Country | Fate |
|---|---|---|
| **TPX** ([[tokamak|Tokamak]] Physics Experiment) | US | Cancelled 1995 before construction |
| **CIT / BPX** (Compact [[ignition|Ignition]] Tokamak / [[burning-plasma|Burning Plasma]] Experiment) | US | Cancelled at design stage, 1980s–90s |
| **FIRE** | US | Never funded |
| **IGNITOR** | Italy/Russia | Perennially proposed, never built |
| **NET** (Next European Torus) | EU | Superseded by [[iter|ITER]] |
| **INTOR** | International | ITER's conceptual predecessor |
| **US ITER participation** | US | Withdrawn 1998, rejoined 2003 |

The pattern is stark. **Between [[tftr|TFTR]]'s shutdown in 1997 and [[sparc|SPARC]]'s assembly in the 2020s, the United States did not build a single new large fusion device.** The intermediate machines that would have continued the triple-product climb were all cancelled or never funded, and the field's performance plateau from roughly 1997 to 2021 is a direct consequence. It was not a physics stall; it was a construction stall.

---

## Part III: Cold fusion and LENR

This requires care, because two different things share a name.

### The 1989 episode
Martin Fleischmann and Stanley Pons announced at a press conference — before peer review — that electrolysis of heavy water with a palladium cathode produced excess heat of nuclear origin. Replication attempts overwhelmingly failed. Panels convened by the DOE in 1989 and again in 2004 found the evidence unpersuasive. The episode did lasting reputational damage to the whole field of fusion, and it is why mainstream fusion is now conspicuously careful about announcing results before publication.

### The 2015–2026 reassessment
What has changed is not the evidence but the seriousness of the search:

- **[[google|Google]] funded a multi-year, multi-institution effort** to test the underlying claims with modern instrumentation. It published its results in *Nature* (2019). **It did not obtain reliable evidence for cold fusion** — but it did produce useful materials science and, importantly, established a set of state-of-the-art capabilities and methodologies for testing such claims.
- **[[arpa-e|ARPA-E]] announced $10 million across eight projects in February 2023** under its LENR programme, explicitly framed as an attempt to **"break the stalemate"** and determine whether low-energy nuclear reactions hold merit — building in part on the Google-sponsored methodological work.
- The field remains **largely experimental and early stage**. **ICCF-27**, the 27th International Conference on Condensed Matter Nuclear Science, is scheduled for **31 August – 4 September 2026** in Niagara Falls, Canada.

### How to hold this
The defensible position is neither dismissal nor credulity. **No reproducible, mechanistically understood excess-energy effect has been demonstrated**, and the theoretical objections — the Coulomb barrier, the absence of commensurate nuclear products — remain unanswered. But the cost of a properly instrumented programme is small relative to fusion budgets, and a definitive null result has value in itself. ARPA-E's framing — prove or debunk — is the right one.

**It is unrelated to the thermonuclear fusion described in the rest of this dossier**, and conflating them is the single most common error in public discussion of fusion energy.

### Adjacent claims that did not survive
**Sonofusion / bubble fusion** — claims of fusion in acoustically collapsed bubbles (Taleyarkhan, 2002) that failed replication and ended in a research-misconduct finding. **Polywell** — Robert Bussard's 1985 magnetic-cusp electrostatic concept, funded by the US Navy for years through **EMC2** (still listed in the FIA survey, founded 1985), with no published net-energy pathway.

---

## Part IV: The company graveyard begins

The FIA's 2026 report notes **three companies dropped out** of this year's survey. That number will grow. The clearest case so far is instructive:

### [[first-light-fusion|First Light Fusion]] — a well-executed retreat
**Oxford, UK · $156 m raised over five rounds**

First Light spent years developing projectile-driven inertial fusion: fire a hypervelocity projectile at a target containing an "amplifier" structure that focuses the resulting shock. It achieved real technical results, including validated fusion neutrons.

In 2025 it **pivoted away from being a fusion plant developer**, refocusing on **licensing its shock-amplifier technology** for other applications. It has continued to raise money — a **£25 m first close led by East X Ventures** through its Starmaker One fusion fund in 2026 — but no longer claims it will build a power station.

This is the healthy version of failure: a competent team concluded its own approach would not reach a plant on a credible timeline, and redirected to what its technology was actually good for. The FIA's CEO frames the general expectation directly: *"When we emerge into a fully commercial fusion industry, few expect there to be 56 companies in it."*

---

## What the graveyard teaches

**1. Distinguish "the physics forbids it" from "the money stopped."** Only the first is permanent. MFTF-B and the stellarator were killed and dormant respectively; both are back. The classic Z-pinch and muon catalysis have specific physical obstacles, and those obstacles have not moved.

**2. Enabling technologies resurrect concepts.** Computation resurrected the stellarator. HTS resurrected the mirror. Pulsed-power and sheared-flow theory are being applied to the Z-pinch now. When evaluating a "failed" concept, the question is not whether it failed but **what would have to change for it to stop failing** — and whether that thing has changed.

**3. Beam-target neutrons are the field's recurring trap.** ZETA in 1958, and every subsequent claim that reports neutrons without reporting a confinement time. This is why the [[triple-product|triple product]], not temperature or neutron count, is the metric that matters.

**4. Publishing before peer review is expensive.** Cold fusion's lasting damage was inflicted by a press conference. The modern sector's most credible companies — CFS, Type One, Proxima, Avalanche — all publish physics bases in peer-reviewed journals, and that is not a coincidence.

**5. A construction stall is indistinguishable from a physics stall, from the outside.** The 1997–2021 plateau in magnetic fusion performance looked like the technology running out of road. It was actually a generation of cancelled machines. That distinction matters enormously for how one reads the current period — which is, above all, **a period in which machines are finally being built again.**


## Failed companies, as distinct from failed concepts

This document catalogues concepts that did not work. [[45-survivorship-failure-and-retrenchment]] covers organisations that
stopped, narrowed or nearly failed — a different subject, because a company can abandon fusion
energy while its concept remains viable and while it remains in the industry's headline count.

---

**Continue to:** [[22-critical-materials-supply-chains|22 — Critical Materials and Supply Chains]] · [[25-failure-case-studies|25 — Failure Case Studies]] · [[02-history-1920-2026|02 — History 1920–2026]]
