---
title: "Open Problems and Risks"
type: synthesis
doc: 14
part: 1
aliases:
  - "Open Problems and Risks"
tags:
  - fusion/synthesis
  - fusion/risks
created: 2026-08-25
updated: 2026-10-19
status: stable
confidence: high
related:
  - "[[00-executive-summary]]"
  - "[[12-state-of-play-2026]]"
  - "[[15-references]]"
  - "[[tritium-burn-fraction]]"
  - "[[tritium-start-up-inventory]]"
  - "[[direct-internal-recycling]]"
  - "[[availability]]"
---
# 14 — Open Problems and Risks

*Project Lux · The honest list of what could stop this*

---

## Purpose

Every other document in this dossier describes what is being built and why it might work. This one describes what is unresolved and why it might not. It is deliberately adversarial.

Nothing here is a prediction of failure. It is the list of things that, if they resolve badly, mean fusion does not become an energy source in the timeframe the field currently projects.

---

## Tier 1: Problems that could prevent fusion from working as an energy source

### 1.1 [[helium-embrittlement|Helium embrittlement]] at power-plant doses

**The problem.** Fusion neutrons produce **10–15 appm helium per dpa** in structural steel, versus 0.1–1 in a fission spectrum. Helium is insoluble in metal, migrates to grain boundaries, and forms bubbles that cause intergranular fracture. At the doses a power plant reaches — **70–100 dpa over a component's life** — no one knows whether reduced-activation ferritic-martensitic steels retain usable ductility.

**Why it is Tier 1.** There is no material with an established fallback. If EUROFER-97 and F82H fail at 30 dpa, the alternatives — ODS steels, vanadium alloys, SiC/SiC composites — are all substantially less mature, and requalifying an entire structural material class is a decade-plus program on its own.

**Why we do not know.** **No fusion-spectrum neutron source exists anywhere in the world.** [[ifmif-dones|IFMIF-DONES]] is under construction; FPNS is a mid-term DOE roadmap item. Surrogates — fission reactors with helium implantation, spallation sources, ion beams — approximate the damage but not the simultaneous combination of dpa rate, He/dpa ratio and spectrum.

**Timing.** DOE's *mid-term* materials milestone is datasets to **~10 dpa**. A power plant needs 70–100. **Pilot plants will be built and operated before the data that would qualify them exists.**

**What would resolve it.** IFMIF-DONES phase 1 data (~20 dpa) in the 2030s; ODS or vanadium alloys proving robust; or an architecture that makes the problem moot — liquid first walls ([[general-fusion|General Fusion]]), FLiBe immersion with a replaceable vessel (CFS's [[arc|ARC]]), or aneutronic fuel.

---

### 1.2 Tritium breeding below self-sufficiency

**The problem.** Every D-T plant must breed more tritium than it burns. The design target is **TBR > 1.1**. Neutrons are lost to structure, ports, diagnostics and heating penetrations, and every port and every diagnostic reduces TBR. Real machines have many ports.

**Why it is Tier 1.** This is not an efficiency question. With a world inventory of **30–40 kg**, production under **0.13 kg/reactor-year** from CANDUs, a **12.3-year half-life**, and a consumption rate of **~56 kg per GW-year**, a plant that cannot breed its own fuel cannot operate. There is no market to buy from.

**The fleet problem is worse than the plant problem.** A single plant might be started from existing inventory. A fleet must bootstrap from breeding surplus, and the **doubling time** is set by how far TBR exceeds 1. TBR = 1.05 versus TBR = 1.15 is the difference between an industry that can grow and one that cannot.

**Why we do not know.** No integrated breeding blanket has ever operated. [[iter|ITER]]'s Test Blanket Modules are the first in-device test, from **2039**.

**Secondary exposure.** **Li-6 enrichment capacity is historically concentrated in Russia and China.** Blankets need 30–90% enrichment against a natural abundance of 7.5%.

**What would resolve it.** [[unity-3|UNITY-3]] (ORNL, standing up now) and [[librti|LIBRTI]] (UK, £220 m) producing integrated blanket data in the late 2020s; [[direct-internal-recycling|Direct Internal Recycling]] cutting inventory and holdup; domestic Li-6 enrichment capacity.

> [!warning] This risk is mis-titled, and the correction widens it
> Added 2026-10-19 from [[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency|Abdou *et al.* 2021]].
> Framing the Tier 1 risk as *breeding* understates it. The binding constraints are the plasma's
> [[tritium-burn-fraction|burn fraction × fuelling efficiency]] (ITER: **0.36%**; required:
> **>2%**), the fuel cycle's **processing time** (required: 1–4 h), and the plant's
> **[[availability]]** — self-sufficiency is *impossible* below 10% availability and only
> *possible* below 50%, whatever the blanket achieves.
>
> Three consequences for this document's risk register:
>
> 1. **The resolvers listed above are insufficient.** UNITY-3 and LIBRTI address breeding. They do
>    not address burn fraction, which no facility can test without a burning plasma.
> 2. **The low-availability near-term devices are compromised twice.** FNSF, VNS and CTF are
>    predicted below **30%** availability — so the very machines meant to demonstrate blankets may
>    be unable to close their own fuel cycle. This couples directly to the RAMI risk elsewhere in
>    this document.
> 3. **The paper's own verdict is negative.** Its authors state that the physics and technology
>    state-of-the-art **will not enable** DEMO and future power plants to meet these requirements.
>    That is the strongest sourced statement in this vault that a Tier 1 risk is currently unmet.
>
> The counterweight: **maximum achievable TBR is estimated at 1.15**, and calculated TBR has been
> shown to **overestimate** experiment by an average factor of **1.14** — so the margin is thinner
> than the TBR > 1.1 target implies. Nothing here softens the risk; it relocates and enlarges it.

---

### 1.3 Core-edge incompatibility

**The problem.** A reactor [[divertor]] must reduce heat flux from roughly 10× above material limits to **under 10 MW/m²**, with target plasma temperature in the **single-eV range**. The only known method is [[detachment]] — radiating the power away in the divertor volume with seeded impurities. But those impurities and that cold, dense edge must coexist with a **hot, clean, high-performance burning core** perhaps a metre away.

**Why it is Tier 1.** If a detached divertor cannot be maintained without degrading the core below the confinement required for Q > 10, then reactor-scale tokamaks have a hard power-density ceiling — which flows directly into plant size and therefore cost.

**Why we do not know.** Detachment works on present machines. None has a [[burning-plasma|burning plasma]]. The scrape-off layer also **narrows** with increasing size and field, so the problem is worst exactly where it matters most.

**What would resolve it.** Super-X (demonstrated on MAST-U, *Nature Energy* 2025), X-point radiator and quasi-continuous exhaust (both extended into D-T on [[jet|JET]]'s DTE3), [[negative-triangularity|negative triangularity]], or liquid-metal plasma-facing components.

---

### 1.4 Availability

**The problem.** A fusion plant is intensely radioactive after first operation and can never be entered. Every subsequent maintenance operation is remote, through ports, in a contaminated space. **Nobody has ever done this on an operating fusion plant.**

**Why it is Tier 1 economically.** LCOE is roughly inversely proportional to capacity factor. If blanket replacement takes six months every two years, availability caps at 75% before unplanned outages. At 50% availability, a plant's LCOE doubles. **This is the most likely reason a technically successful fusion plant is commercially useless.**

**What would resolve it.** Architectures that treat the irradiated volume as replaceable rather than repairable — ARC's demountable magnets and liftable vacuum vessel, General Fusion's liquid wall, the inherently serviceable linear geometries of mirrors and Z-pinches. Plus the DOE roadmap's RAMI handbook, qualified joining and cutting of irradiated materials, and validated mock-up maintenance workflows.

---

## Tier 2: Problems that could delay fusion by a decade or more

### 2.1 [[sparc|SPARC]] underperforms

The entire private magnetic-confinement thesis rests on one machine in 2027. SPARC's design goal is Q > 2 with a nominal projection of Q ≈ 11 — that gap exists because Q ≈ 11 assumes H98,y2 = 1, i.e. that confinement scaling extrapolates cleanly into a regime nobody has operated in.

If confinement degrades at high field, or if disruptions damage the machine, or if the divertor cannot handle 140 MW in a compact volume, the result is not just CFS's problem. DOE has aligned its roadmap to it as *Milestone 1*; the sector's valuations assume it; and a visible failure would be read by generalist capital as a verdict on fusion rather than on one machine.

### 2.2 First-of-a-kind cost overrun

FOAK capital cost estimates span **$1,400 to $43,000/kW**. Western nuclear FOAK projects — Vogtle, Hinkley Point C, Flamanville, Olkiluoto — routinely ran **2–4× over budget and a decade late**, and a fusion plant is more complex than any of them.

ARC at ">$2.5 bn for ~400 MWe" is the field's first real cost datum. If it lands at $6 bn, the economics of every subsequent plant are reassessed downward, and the offtake agreements that make project finance possible become much harder to sign.

### 2.3 The HTS supply chain

Global REBCO tape capacity is roughly **10,000 km/year**, with substantial concentration in China. A single high-field [[tokamak]] consumes thousands of kilometres. A fleet requires an order-of-magnitude expansion in a market with few suppliers and long capacity lead times.

Additionally: **REBCO's radiation tolerance is not established** for reactor lifetimes. DOE's near-term milestone is explicitly to "conduct REBCO irradiation campaigns to define magnet performance and standards" — i.e. the field is building machines around a conductor whose in-service degradation is not yet characterised. In a spherical tokamak's centre column, where shielding space barely exists, this is acute.

### 2.4 Funding discontinuity

The sector raised $4.48 bn in the year to July 2026, up 69%. It raised **$0.9 bn in 2024**. Fusion funding is volatile and correlated with general risk appetite.

The companies' own estimate of further capital required — average $2.7 bn each across 56 companies — implies **over $100 billion**. Cumulative funding to date is $14 bn. A two-year funding winter arriving before SPARC's result would be severe.

Public money is not a reliable backstop: the DOE roadmap disclaims funding commitments on nearly every page, and the facilities the private sector most needs (FPNS, blanket and fuel-cycle test beds) are precisely the ones requiring appropriations for infrastructure that will not operate for a decade.

### 2.5 Workforce

The sector employs ~5,600 directly and ~10,500 through the supply chain. Scaling to a construction industry requires cryogenic engineers, tritium chemists, remote-handling specialists, superconducting magnet engineers, and nuclear-qualified welders — populations that are small, ageing, and competed for by the fission renaissance and the AI data-centre buildout simultaneously.

**14 companies name skilled workforce a near-term challenge and 15 a long-term one.**

---

## Tier 3: Problems that are real but manageable

### 3.1 Disruptions

A tokamak [[disruption]] dumps full thermal and magnetic energy into the wall in milliseconds and can generate multi-megaampere runaway electron beams. On a reactor-scale machine, a single unmitigated event can cause serious damage.

*Why manageable:* AI-based prediction and avoidance is progressing rapidly and is now deployed in real-time control systems; mitigation by massive gas or shattered-pellet injection works; and stellarators, mirrors and FRCs avoid the failure mode entirely by construction.

### 3.2 Waste volume

Fusion will produce **more low- and intermediate-level waste by volume than fission**, because the machine itself becomes waste. It is far less radiotoxic and decays in 50–100 years rather than geological time, but "fusion has no waste" is false and should not be said.

*Why manageable:* reduced-activation materials, designed recyclability, and a decay horizon within institutional planning range.

### 3.3 Tritium as a regulated and dual-use material

A plant holding kilograms of tritium is materially a tritium production facility. Accountancy is genuinely hard because tritium permeates through hot metal.

*Why manageable:* the byproduct-material framework is designed for exactly this, and Agreement States already regulate substantial tritium inventories.

### 3.4 Fissile breeding potential

A 14.1 MeV neutron flux is an excellent transmutation tool. A blanket loaded with U-238 breeds Pu-239; with Th-232 it breeds U-233 — with no fissile material in the declared inventory.

*Why manageable:* safeguards and blanket design transparency; and any state capable of building a fusion plant has easier routes to fissile material. But the concern is technically valid.

### 3.5 Public disappointment

Repeated "breakthrough" headlines that never produce electricity erode credibility. The field's fifty-year record of missed timelines is a real reputational liability.

*Why manageable:* public-market listings impose quarterly reality checks, and milestone-gated funding punishes over-promising directly.

---

## The specific claims this dossier treats with scepticism

Stated plainly, because a survey that only reports what participants say is not a survey.

**1. "Fusion will be too cheap to meter."**
The best independent analysis (TU Berlin / DIW, arXiv:2606.26536, 56 references, Monte Carlo harmonised) puts mature LCOE at **$110–145/MWh** and explicitly urges *"caution when potential fusion developers refer to the potential economic competitiveness of fusion power plants."* Even a plant with a *free* fusion core has a balance-of-plant floor around **$7/MWh**.

**2. "NIF achieved net energy."**
NIF achieved **target gain 4.13** — 8.6 MJ out for 2.08 MJ delivered to the target. The laser drew roughly **300–400 MJ from the grid** to deliver that 2.08 MJ. On a wall-plug basis the record shot's gain was about **0.02**. The scientific milestone is genuine; the energy claim is not.

**3. [[aneutronic-fusion|Aneutronic fusion]] timelines.**
p-¹¹B requires roughly 3 billion K and must defeat bremsstrahlung losses scaling as Z_eff²n²√T with boron's Z = 5. TAE has reached ~75 million K for ~30 ms. HB11 reported a 10× alpha-yield improvement in May 2026 and remains many orders of magnitude from breakeven. **No facility has demonstrated sustained aneutronic fusion.** The endgame is genuinely attractive; the timelines quoted are not credible.

**4. "Fusion produces no radioactive waste."**
It produces no *long-lived* waste and no fission products or transuranics. It produces a **larger volume** of low- and intermediate-level activated material than fission.

**5. Any pilot-plant date that skips an intermediate machine.**
Fusion knowledge is embodied in hardware. A roadmap that goes from a bench experiment to a 200 MWe plant is missing a generation of learning that no simulation replaces.

**6. Temperature records without confinement time.**
Temperature alone is not a [[triple-product|triple product]], and beam-target neutrons are not thermonuclear neutrons. This is exactly the error that produced the [[zeta|ZETA]] fiasco in 1958, and it recurs in press releases regularly.

---

## What would most change this assessment

### Strong positive signals to watch for

1. **SPARC achieves Q > 5** — not just Q > 1. This would confirm confinement scaling holds into the burning regime and would validate the compact high-field pathway definitively.
2. **An integrated blanket demonstrates TBR > 1.1** at UNITY-3, LIBRTI or equivalent — the single most valuable result available this decade, and almost nobody outside the field is watching for it.
3. **A structural material shows acceptable ductility at 30+ dpa with fusion-relevant He/dpa** — even from a surrogate, this would materially de-risk every pilot plant.
4. **A plant demonstrates remote replacement of an activated in-vessel component on schedule** — this is the availability question, answered.
5. **ARC comes in at or near $2.5 bn.**

### Strong negative signals

1. **SPARC achieves Q < 1 with no clear physics explanation.**
2. **Helium embrittlement disqualifies RAFM steels below 30 dpa.**
3. **A well-funded company fails publicly on a technical rather than a financial basis.**
4. **REBCO irradiation campaigns show unacceptable critical-current degradation at reactor fluences.**
5. **A funding contraction of 2024's severity persisting more than eighteen months.**

---

## Final assessment

**The case for optimism** is that every problem in Tier 1 is an *engineering* problem with identified approaches, real money, and — for the first time — dedicated facilities being built to address it. Engineering problems with capital behind them have a much better historical resolution rate than open physics questions. The physics, which was the hard part for seventy years, is largely done.

**The case for caution** is that Tier 1 contains four problems, **not one of which has ever been demonstrated at any scale**, and that the facilities which would resolve two of them will not produce decisive data until the 2030s — after the pilot plants that depend on those answers have been designed and built.

**The most probable outcome, on the evidence in this dossier:**

- **Scientific net gain in magnetic confinement: 2027–2029.** High confidence. The hardware exists.
- **Some quantity of fusion-derived electricity on a grid: 2028–2033.** Moderate confidence. Most plausibly from a pulsed direct-conversion device, not a thermal-cycle tokamak.
- **A plant that breeds its own tritium and runs a full duty cycle: 2040s.** This is where the materials and blanket answers land.
- **Economically competitive fusion at scale: 2050s**, and contingent on a learning curve that has never been demonstrated for a technology of this complexity.

That is slower than the industry says and considerably faster than the field's seventy-year record would suggest. Both halves of that sentence matter.

The single most important thing to understand is that **fusion's risk has moved, not disappeared.** For seventy years the question was whether the physics permitted it. That question is answered. The question now is whether metallurgy, tritium chemistry and project finance can deliver on a comparable timescale — and there is, as yet, no evidence either way.

---

**Continue to:** [[15-references|15 — References]] · [[00-executive-summary|00 — Executive Summary]] · [[12-state-of-play-2026|12 — State of Play 2026]]
