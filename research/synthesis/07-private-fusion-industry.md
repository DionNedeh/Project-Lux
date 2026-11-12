---
title: "The Private Fusion Industry"
type: synthesis
doc: 07
part: 1
aliases:
  - "The Private Fusion Industry"
tags:
  - fusion/synthesis
  - fusion/industry
  - fusion/companies
created: 2026-08-25
updated: 2026-09-02
status: stable
confidence: high
related:
  - "[[01-fusion-physics-fundamentals]]"
  - "[[04-magnetic-confinement-devices]]"
  - "[[08-national-programs]]"
  - "[[09-engineering-challenges]]"
  - "[[10-economics-and-markets]]"
  - "[[14-open-problems-and-risks]]"
---
# 07 — The Private Fusion Industry

*Project Lux · 56 companies, $14.24 billion, and how to tell signal from pitch deck*

> **Source note.** Funding figures in this document are the companies' own **declared totals** as reported to the [[fusion-industry-association|Fusion Industry Association]] for its *Global Fusion Industry Report 2026* (published 13 July 2026), extracted directly from the report PDF held in `papers/`. Where press reporting gives a different number, both are noted. Declared totals include committed but not necessarily drawn capital, and the FIA states plainly that "external accounts can give conflicting numbers."

---

## 1. The shape of the sector

### The headline numbers

| Metric | Value |
|---|---|
| **Total funding to date** | **$14,242,143,000** |
| **Raised in 12 months to July 2026** | **$4,476,143,000** (+69% YoY, a record) |
| Private / public split | $13.26 bn / $0.98 bn |
| Companies surveyed | **56** (up from 23 in 2021) |
| New entrants this year | 6 (3 dropped out) |
| Direct employees | **5,606** (an undercount — not all reported) |
| Supply-chain jobs supported | **10,497** |
| Further capital each company estimates needing | **average $2.7 bn, median $1.2 bn** |

### The funding curve

| Year | Cumulative | Raised that year |
|---|---|---|
| ≤2021 | $1.9 bn | — |
| 2022 | $4.8 bn | $2.9 bn |
| 2023 | $6.2 bn | $1.4 bn |
| 2024 | $7.1 bn | **$0.9 bn** ← the trough |
| 2025 | $9.8 bn | $2.6 bn |
| **2026** | **$14.2 bn** | **$4.5 bn** |

The 2024 trough is worth dwelling on. It reflected the general venture funding contraction, and at the time the FIA's own CEO warned that fusion "would not meet its goals of commercial fusion in the 2030s with increases of only $1 billion new funding per year." The recovery since has been driven substantially by **AI-related electricity demand** — an explicit finding in the 2026 report's foreword — rather than by any single technical breakthrough.

### Where the companies are

| Country | Companies |
|---|---|
| **United States** | **28** — including all five that have raised over $1 bn |
| UK | 4 |
| Germany | 4 |
| China | 4 *(incomplete — see below)* |
| Japan | 3 |
| India | 3 |
| Canada | 2 |
| France, Switzerland, Sweden, Hungary, Israel, New Zealand | 1 each |

US concentration: **California 10, Washington 3, Massachusetts 2, Colorado 2, New Mexico 2, Wisconsin 2, Maryland 2**, plus New Jersey, Virginia and Tennessee.

**The China caveat is important and the FIA states it openly.** Its report includes four Chinese companies, but notes that "press reports have indicated several more companies, backed by both government and private funding" which did not respond to the survey. **The visible picture of Chinese private fusion is materially incomplete**, and any comparison of national totals should be read with that in mind.

### How the sector splits technically

| Approach | Companies | Share |
|---|---|---|
| Magnetic confinement | 26 | 46% |
| [[inertial-confinement|Inertial confinement]] | 12 | 21% |
| Magneto-inertial | 9 | 16% |
| Hybrid electrostatic | 7 | 13% |
| Muon-catalysed | 1 | 2% |

Within magnetic confinement, **stellarators (8) now outnumber tokamaks (5)** — a complete inversion of the public-sector balance, and a direct consequence of the optimisation advances described in [[04-magnetic-confinement-devices|Document 04]].

**Fuel choice:** D-T 40, p-¹¹B 5, D-D 5, D-³He 2, multiple fuels 4.

---

## 2. The billion-dollar tier

Five companies have declared over $1 billion. All are American.

### [[commonwealth-fusion-systems|Commonwealth Fusion Systems]] — $3.0 bn
**Devens, Massachusetts · founded 2018 · ~1,000 employees · high-field [[tokamak]] · D-T**

The largest and, on most measures, the most credible. Spun out of MIT's Plasma Science and Fusion Center to commercialise REBCO high-temperature superconductors, on the thesis that fusion power density scales as B⁴ and therefore a stronger magnet beats a bigger machine.

**Why it is taken seriously:**
- It published its full physics basis openly — a seven-paper special issue of the *Journal of Plasma Physics* in 2020 — inviting exactly the scrutiny most startups avoid
- It de-risked its central technical claim first: the **20 tesla model coil test of September 2021** proved the magnet before the machine was designed around it
- Its collaborator list reads like the field itself: MIT, Brookhaven, Columbia, Max Planck IPP, NREL, NVIDIA, Dominion Energy

**Status August 2026:**
- **[[sparc|SPARC]] ~80% assembled**; TF1 installed; all 18 magnets due in place by summer's end; **first plasma and scientific breakeven targeted 2027**
- **[[arc|ARC]]**, ~400 MWe, permitted at Chesterfield County, Virginia; **>$2.5 bn expected cost**; first power early 2030s; first fusion company to apply to **PJM Interconnection**
- **$1 billion raised from pension funds** in July 2026 — the first time institutional retirement capital has treated fusion as infrastructure
- **$863 m** raised in the FIA survey year — the largest single-company raise in the sector
- Now **selling magnets to other fusion companies**, starting with [[realta-fusion|Realta Fusion]] (April 2026)

That last item is strategically the most interesting: CFS is attempting to become a supplier as well as a developer, which builds the HTS supply chain the whole industry needs and hedges its own single-machine risk.

### [[helion-energy|Helion Energy]] — $1.5 bn
**Everett, Washington · founded 2013 · pulsed FRC · D-³He**

The most aggressive schedule in fusion and the most polarising company in it.

Helion collides two field-reversed configurations at over a million miles per hour and compresses them magnetically. As the fused plasma expands against the field it induces current **directly back into the coils** — electricity without a steam cycle, at pulsed high efficiency. It targets **D-³He**, breeding its own helium-3 from D-D side reactions, which drastically reduces (but does not eliminate) the neutron load.

**Status:**
- **[[polaris|Polaris]]** reached **150 million °C** (February 2026) and became the **first privately funded machine to operate with D-T fuel**; it now runs nearly every day
- **Orion**, the commercial plant, is under construction at Malaga, Washington
- **World's first fusion PPA** ([[microsoft|Microsoft]], 2023): **≥50 MW after a one-year ramp, targeted 2028**
- Valuation **$15.5 bn**; raised **$465 m** in the survey year

**The debate.** Helion publishes far less peer-reviewed detail than CFS or Type One, and prominent plasma physicists have questioned whether its pulsed direct-recovery efficiency claims survive contact with real losses. Against that: it has a signed offtake agreement with a counterparty that performed technical diligence, it is operating a D-T machine daily, and it is building a plant. Both facts are real; this dossier does not adjudicate between them.

### [[tae-technologies|TAE Technologies]] — $1.5 bn
**Foothill Ranch, California · founded 1998 · FRC · targeting p-¹¹B**

The oldest company in the modern sector and the longest-running private fusion effort anywhere. Beam-driven [[field-reversed-configuration|field-reversed configuration]]: neutral beams both sustain the FRC against decay and heat it.

Machine lineage: C-2 → C-2U → **C-2W ("Norm")** → *Copernicus* → *Da Vinci*.

**2025-26:** TAE announced that Norm **outperformed expectations**, achieving FRC formation using neutral beams alone — a substantial simplification that it says removes a whole device from the roadmap. It stated it would **skip Copernicus** and move directly toward Da Vinci, its first commercial plant. *Reporting since has been inconsistent about whether Copernicus is cancelled or merely deferred; sources conflict and this is not resolved here.*

TAE has also built a genuine revenue business around spin-offs — **TAE Power Solutions** (power management and energy storage) and **TAE Life Sciences** (boron neutron capture therapy) — which is a materially different capital strategy from the rest of the sector.

**The honest gap:** p-¹¹B needs roughly 3 billion K. Norm has reached about 75 million K for ~30 ms. TAE does not dispute this; its argument is that an FRC's β ≈ 1 eventually makes the fuel accessible where no other geometry can.

### [[pacific-fusion|Pacific Fusion]] — $1.0 bn
**California · founded 2023 · pulser-driven inertial confinement**

The fastest-funded newcomer in the sector's history, founded by a team including former Meta CTO Mike Schroepfer and physicists from the NIF and Z-machine lineages. Uses **coordinated electromagnetic pulses** rather than lasers — pulsed power converts wall-plug electricity to load energy at over 50% efficiency, versus a laser's ~10% aspiration.

Pacific Fusion's distinguishing practice is a **milestone-gated funding structure**: capital is committed but released only on demonstrated technical milestones, published in advance.

**June 2026 milestone (second set achieved):** a scaled module prototype delivered **more than 440 GW of peak output power at approximately 1.1 MV** in ultra-fast pulses — described as the performance required to eventually drive fusion conditions.

### [[shine-technologies|SHINE Technologies]] — $1.1 bn
**Janesville, Wisconsin · founded 2010**

The outlier, and instructive because of it. SHINE is pursuing fusion through a **staged commercial ladder**: industrial neutron imaging first, then medical isotope production (notably molybdenum-99), then nuclear waste recycling, and only then fusion energy. It has **actual revenue today** from operating neutron sources.

Collaborators include [[arpa-e|ARPA-E]], GE-Hitachi, and the Department of Defense. It is the only company in the billion-dollar tier making money now, and its model — sell neutrons before you sell electricity — is being copied across the sector.

---

## 3. The $100 m–$1 bn tier

| Company | Declared | Location | Approach | Notes |
|---|---|---|---|---|
| **[[proxima-fusion|Proxima Fusion]]** | **$752 m** | Munich, Germany | Quasi-isodynamic [[stellarator]] | Spun from Max Planck IPP (W7-X lineage). **$518 m raised this year** — second-largest in the sector. Published the first fully integrated stellarator plant design optimised for physics *and* engineering simultaneously (*Stellaris*) |
| **ENN Science & Technology** | **$720 m** | Langfang, China | Spherical torus, p-¹¹B ambitions | The largest declared Chinese private effort. Press reporting has cited a lower $400 m figure |
| **[[focused-energy|Focused Energy]]** | **$500 m** | US / Darmstadt, Germany | Laser ICF, proton [[fast-ignition|fast ignition]] | **$240 m this year.** DOE Milestone awardee; $6.9 m research agreement with Rochester LLE (March 2026); German federal *and* state government partnerships to build plants |
| **[[general-fusion|General Fusion]]** | **~$500 m** | Richmond, BC, Canada | Magnetized target fusion | **First publicly listed fusion company (Nasdaq: GFUZ, July 2026).** LM26 reached 0.72 keV (~8.4 M °C); ~$150 m cash funds the program through end-2028 |
| **[[inertia-enterprises|Inertia Enterprises]]** | **$450 m** | US | ICF targets and fuel | **$450 m raised this year.** With LLNL, cut cryogenic D-T fuel layering from days to **2–3 hours** (August 2026) |
| **[[marvel-fusion|Marvel Fusion]]** | **$440 m** | Munich, Germany | Laser ICF, nanostructured targets | **$150 m demonstration facility with Colorado State University** |
| **[[zap-energy|Zap Energy]]** | **$338 m** | Everett, Washington | Sheared-flow-stabilized Z-pinch | >1 keV electron temperature demonstrated. **TIME Top GreenTech 2026 #16** — highest-ranked fusion company. DOE Milestone awardee |
| **[[tokamak-energy|Tokamak Energy]]** | **$335 m** | Oxfordshire, UK | Spherical tokamak + HTS magnets | Founded 2009, 300 staff. **Demo4 reached 11.8 T and 7 MA-turns.** Selected as **Magnet Systems Partner for UK [[step|STEP]] (£70 m / $95 m)**. Sells magnets as a business via TE Magnetics |
| **[[yan-fusion|YAN Fusion]]** | **$293 m** (phased) | Shanghai, China | — | New entrant; $293 m this year |
| **[[type-one-energy|Type One Energy]]** | **$200 m** | Knoxville, Tennessee | Optimised stellarator | **[[infinity-two|Infinity Two]], 350 MW, at a TVA former coal site**, mid-2030s. Published a complete physics basis including blanket and tritium fuel-cycle feasibility in *J. Plasma Physics*. Licensed ORNL cryogenic pellet fuelling (Aug 2026) |
| **[[xcimer-energy|Xcimer Energy]]** | **$178 m** | Colorado | KrF excimer laser ICF | **DOE approved its preconceptual design and technology roadmap for "Athena"** (August 2026). DOE Milestone awardee |
| **[[first-light-fusion|First Light Fusion]]** | **$156 m** | Oxford, UK | *Pivoted* — amplifier tech licensing | £25 m first close led by East X Ventures. **Abandoned its own plant ambitions** — see §6 |
| **[[kyoto-fusioneering|Kyoto Fusioneering]]** | **$144 m** | Kyoto, Japan | **Not a plant developer** — fusion plant technology | Gyrotrons, tritium systems, blankets. Building **UNITY-1** (Japan) and **UNITY-2** (Canada); relocating US HQ to Oak Ridge, TN alongside DOE's [[unity-3|UNITY-3]] |
| **[[startorus|Startorus Fusion]]** | ~$139 m | Xi'an, China | Spherical tokamak / MIF | $220 m raised this year per FIA's raise chart |
| **[[thea-energy|Thea Energy]]** | **$130 m** | Kearny, New Jersey | **Planar-coil** stellarator | [[canis]]: nine-coil HTS array manufactured and controlled within 1% of predicted static field; [[eos]] remains planned. **First DOE Milestone awardee to complete a full pilot plant design review.** $20 m ARPA-E SCALEUP for a US modular HTS magnet line |
| **[[energy-singularity|Energy Singularity]]** | **$112.5 m** | Shanghai, China | **Fully HTS tokamak** | **[[hh70|HH70]] — world's first fully HTS tokamak**, first plasma June 2024, built in ~2 years. **1,337 s** long-pulse. HH170 (Q≥10 target) construction due to finish end-2027 |
| **[[avalanche-energy|Avalanche Energy]]** | **$104 m** | Seattle, Washington | Magneto-electrostatic "Orbitron" | Deliberately tiny: **0.1 MWe** modular units for off-grid, marine and space. Reported 1 keV plasma temperature. Building **FusionWERX**, a commercial fusion test facility. Partners: DARPA, DIU, AFWERX |

---

## 4. The rest of the field

| Company | Declared | Location | Approach |
|---|---|---|---|
| [[helical-fusion|Helical Fusion]] | $65 m | Japan | Helical (stellarator) |
| Realta Fusion | $58.8 m | Madison, Wisconsin | HTS tandem [[magnetic-mirror|magnetic mirror]] |
| [[astral-systems|Astral Systems]] | $40 m | Bristol, UK | Inertial-electrostatic lattice — **selling neutron irradiation services today** |
| [[ex-fusion|EX-Fusion]] | $38 m | Osaka, Japan | DPSSL direct-drive laser |
| [[blue-laser-fusion|Blue Laser Fusion]] | $37.5 m | Goleta, California | Coherent-beam-combined fibre laser ICF (founded by Nobel laureate Shuji Nakamura) |
| [[nt-tao|nT-Tao]] | $34 m | Israel | Compact fusion |
| [[openstar-technologies|OpenStar Technologies]] | $29.4 m | Wellington, New Zealand | **Levitated dipole** — achieved plasma 2024 |
| Acceleron Fusion | $26.5 m | Cambridge, Massachusetts | **Muon-catalysed fusion** |
| [[longview-fusion|Longview Fusion Energy Systems]] | $12 m | California | NIF-derived laser plant design |
| GenF | $10.8 m | — | — |
| HelicitySpace | $10 m | California | Plasma-jet MIF for **space propulsion** |
| Pranos Fusion | $7.2 m | India | — |
| ASPL Fusion | $2 m | Gandhinagar, India | Gas dynamic magnetic trap; incubated at IPR/DAE. Phased plan via BNCT and neutron activation revenue |
| Terra Fusion Energy | $1.5 m | — | — |
| Anubal Fusion | $0.5 m | Hyderabad, India | Petawatt laser, p-¹¹B |

Plus: Crossfield Fusion, Deutelio, Fuse, [[gauss-fusion|Gauss Fusion]], Horne Technologies, LaserFusionX, Liberty Fusion, [[maritime-fusion|Maritime Fusion]], MIFTI, NearStar Fusion, [[neofusion|NeoFusion]], [[novatron|Novatron Fusion]], Princeton Satellite Systems, Pulsar Fusion, [[renaissance-fusion|Renaissance Fusion]], [[stellarex|Stellarex]], Tibbar Plasma, LPPFusion, EMC2.

---

## 5. What the companies say about themselves

From the FIA survey — these are self-reported and should be read as intentions, not forecasts.

**When will you achieve scientific net energy gain?** (31 responses)
Before 2030: **6** · 2030–2035: **24** · 2036–2040: 0 · 2040–2045: 1

**Engineering net gain?** (33 responses)
Before 2030: 3 · 2030–2035: **16** · 2036–2040: **11** · 2040–2045: 3

**First pilot plant?** (47 responses)
Before 2030: 4 · **2030–2035: 28** · 2036–2040: 11 · 2040–2045: 4

**First commercial electricity?** (45 responses)
2026–2030: 3 · **2031–2035: 16** · 2036–2040: 13 · 2041–2045: 9 · 2046–2050: 3 · after 2050: 1

**Commercially viable cost/Q?** (42 responses)
2026–2030: 2 · 2031–2035: 11 · **2036–2040: 14** · 2041–2045: 8 · 2046–2050: 5 · after 2050: 2

Note the internal tension in that last block: companies expect **electricity** before they expect **economic viability**. That is coherent — a first plant can be subsidised or sold at a premium to a hyperscaler — but it means the sector is not claiming cheap fusion power in the early 2030s. It is claiming *some* fusion power.

### What they say is hard

Ranked by near-term concern (44 responses; near-term / long-term counts):

| Challenge | Near | Long |
|---|---|---|
| Funding | **30** | 18 |
| Fusion power efficiency / high enough Q | **29** | 23 |
| **Neutron-resilient materials** | **29** | **25** ← highest long-term |
| Tritium self-sufficiency | 25 | 23 |
| Integrated systems engineering | 19 | 10 |
| Plasma science | 15 | 7 |
| Supply chain readiness | 15 | **20** |
| Skilled workforce | 14 | 15 |
| Pulse duration | 11 | 10 |
| Geopolitics | 11 | 12 |
| First-of-a-kind construction risk | 11 | 8 |
| Nuclear safety / regulatory | 10 | 11 |
| Full life-cycle (maintenance, waste, decommissioning) | 10 | **14** |
| Plasma exhaust | 9 | 7 |
| Siting and permitting | 5 | 7 |
| Cryoplants | 4 | 3 |
| PPAs and offtake | 2 | 6 |

**Read the long-term column.** Plasma science ranks *seventh* near-term and drops to 7 mentions long-term. **Materials and tritium sit at the top and stay there.** The industry's own assessment matches the assessment in this dossier's [[09-engineering-challenges|Document 09]]: the physics is largely conceded; the nuclear engineering is not.

---

## 6. How to read this sector critically

### Signals that a company is real

1. **Published, peer-reviewed physics basis.** CFS (JPP special issue, 2020), Type One Energy (JPP, including blanket and fuel-cycle feasibility), Proxima Fusion (Stellaris), Avalanche (papers in *Nature*, *Physics of Plasmas*, IEEE). This is costly, invites attack, and is therefore informative.
2. **A de-risking milestone completed before the big build.** CFS's 20 T magnet. Tokamak Energy's Demo4. Pacific Fusion's pulser module. Realta's 17 T and its direct-energy-conversion demo. Thea's [[canis]] array, which demonstrated nine planar [[rebco]] coils and static field control within 1% of prediction, with integrated-stellarator performance explicitly still untested ([[prototyping-test-canis-hts-planar-coil-array]]).
3. **Third-party technical validation with money attached.** DOE Milestone Program certification (Thea Energy's completed design review; DOE's approval of Xcimer's architecture). A signed PPA from a counterparty that ran diligence.
4. **Selling something now.** SHINE's isotopes. Astral's irradiation services. Kyoto Fusioneering's plant components. TAE's power-electronics and BNCT businesses. Tokamak Energy's magnets. Revenue is discipline.
5. **Becoming part of someone else's supply chain.** CFS→Realta magnets. ORNL→Type One pellet fuelling. This is what an industry looks like as distinct from 56 prototypes.

### Signals to discount

1. **A temperature record without a confinement time.** Temperature alone is not a [[triple-product|triple product]], and beam-target neutrons are not thermonuclear neutrons. This is precisely the error that produced the [[zeta|ZETA]] fiasco in 1958.
2. **Q quoted without saying which Q.** See [[01-fusion-physics-fundamentals|Document 01 §5]].
3. **A pilot plant date with no intermediate machine.** If the roadmap goes from a bench experiment to a power plant, an entire generation of hardware learning is missing.
4. **No public position on tritium breeding.** Any D-T company that has not said how it will achieve TBR > 1 has not confronted its hardest problem.
5. **Aneutronic claims without a bremsstrahlung answer.** p-¹¹B's difficulty is not temperature; it is radiative loss at Z=5.

### The consolidation everyone expects

The FIA's CEO says it directly in the 2026 report's conclusion: *"When we emerge into a fully commercial fusion industry, few expect there to be 56 companies in it. The race is on."*

Three companies dropped out of this year's survey. **First Light Fusion** is the most instructive case: a well-funded UK company with real technical achievements that concluded its own approach would not reach a plant and pivoted to licensing its shock-amplifier technology instead. That is a rational and honourable outcome, and it will not be the last.

Two structural changes will accelerate the sorting:

- **Public markets.** General Fusion now trades as GFUZ, with a second company in process. Quarterly disclosure and a live ticker impose a discipline the sector has never faced. The FIA notes this brings "a different type of scrutiny."
- **Milestone-gated capital.** Pacific Fusion's model, DOE's Milestone Program, and increasingly the private rounds themselves tie money to demonstrated results rather than narrative.

### What the funding does *not* prove

$14.24 billion sounds like a lot and is, in fusion's history, unprecedented. It is also:

- Less than the cost of a single large LNG terminal
- Roughly one-third of one year of global upstream oil and gas capital expenditure
- Below the *average* declared need of the companies themselves — 56 companies at an average $2.7 bn further requirement each implies well over **$100 billion** to carry the current field to commercial plants

Most of these companies will not raise their share. That is not a criticism of the sector; it is how every capital-intensive technology transition has worked. But it means the correct mental model is **a portfolio in which most positions go to zero and one or two return the whole fund** — and the interesting question is not whether fusion companies fail, but whether the two or three that survive are enough to build an industry.


## Failure modes, primary-sourced

[[45-survivorship-failure-and-retrenchment]] adds primary sourcing to the dropout arithmetic above. [[first-light-fusion]]'s own
March 2025 statement confirms it discontinued **Machine 4** and abandoned power-plant development
while remaining in the industry count — so company counts overstate the number of organisations
actually pursuing a plant. [[general-fusion]] laid off **at least 25% of staff** days after [[lm26]]
compressed plasma, then recovered to a Nasdaq listing fourteen months later: technical progress and
capital availability are only loosely coupled, in both directions.

---

**Continue to:** [[08-national-programs|08 — National Programs]] · [[10-economics-and-markets|10 — Economics and Markets]] · [[14-open-problems-and-risks|14 — Open Problems]]
