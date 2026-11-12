---
title: "Economics and Markets"
type: synthesis
doc: 10
part: 1
aliases:
  - "Economics and Markets"
tags:
  - fusion/synthesis
  - fusion/economics
created: 2026-08-25
updated: 2026-08-29
status: stable
confidence: high
related:
  - "[[09-engineering-challenges]]"
  - "[[11-policy-regulation-safety]]"
  - "[[13-roadmap-to-2040]]"
  - "[[14-open-problems-and-risks]]"
  - "[[public-acceptability-scoping-review-2026]]"
  - "[[fusion-fission-twin-conjoint-public-support-2026]]"

---
# 10 — Economics and Markets

*Project Lux · What fusion might cost, who would buy it, and why the customer changed*

---

## 1. The honest starting position

**Nobody knows what fusion electricity will cost, and the range of credible estimates spans more than an order of magnitude.**

A 2026 analysis in *Nature Energy* compiled first-of-a-kind capital cost estimates from experts and the literature and found a range of **$1,400 to $43,000 per kilowatt** — a **thirty-fold spread**. That is not a forecast; it is an admission that the technology is too immature for the question to be answerable.

For calibration, the same metric for technologies that exist:

| Technology | Overnight cost ($/kW) |
|---|---|
| Combined-cycle gas | ~$1,000–1,500 |
| Onshore wind | ~$1,500–2,000 |
| Utility solar | ~$1,000–1,400 |
| Offshore wind | ~$3,000–5,000 |
| Nuclear fission (Western FOAK) | ~$7,000–15,000 |
| **Fusion (estimated FOAK)** | **$1,400–43,000** |

Where fusion lands in that range determines whether it becomes an energy source or a very expensive science project. **CFS's [[arc|ARC]] — ~400 MWe for "over $2.5 billion" — implies roughly $6,250/kW**, which sits inside the plausible band and is comparable to Western fission FOAK. That is a real number attached to a real permitted project, and it is currently the best single data point in existence.

---

## 2. What the cost studies say

### The most rigorous recent analysis

Böhnlein, Böse, von Hirschhausen, Kemfert and Wimmers (TU Berlin / DIW Berlin, arXiv:2606.26536, in `papers/`) conducted a stochastic Monte Carlo harmonisation of **56 references** across the three technology lines. Their results for **mature** technology:

| Technology line | Mean LCOE (mature) |
|---|---|
| **Magnetic confinement** | **$114.6 / MWh** |
| **[[inertial-confinement|Inertial confinement]]** | **$110.3 / MWh** |
| **Magneto-inertial** | **$143.9 / MWh** |

Their conclusion is pointed and worth quoting directly, because it is the most careful independent assessment available:

> *"We find that these projected values are rather optimistic when compared to other literature or comparable technologies like fission. We therefore urge policymakers to caution when potential fusion developers refer to the potential economic competitiveness of fusion power plants."*

Their highlights add two important qualifications: reaching those LCOEs **implies learning rates above 30%**, which is very aggressive by historical standards for large capital plant, and **"initial actual cost expected to be much higher"** than the mature figures.

### Other reference points

- **NASEM threshold**: a viable pilot plant must achieve **overnight cost below $5 billion**
- **[[manta|MANTA]]** (a negative-triangularity NASEM-compliant pilot plant design study): **$3.4 bn overnight** — inside the threshold, on paper
- **[[first-light-fusion|First Light Fusion]]** claimed ICF could reach **$25/MWh** at maturity (pre-pivot; treat as advocacy)
- **A p-¹¹B plant at 2 GWe**, 95% availability, 3% cost of capital, 3-year construction, 50-year life, has a **balance-of-plant floor of $7.1/MWh** — i.e. even if the fusion core were *free*, the steam turbines, buildings and grid connection cost that much
- **CATF's Fusion Cost Model** provides an open framework for these calculations

That last item is the most useful sanity check in fusion economics. **The floor is not zero.** A fusion plant is a large thermal power station with an exotic heat source; most of its cost is conventional.

### Where the money goes

For a magnetic confinement plant, the rough breakdown:

| Component | Share of capital |
|---|---|
| Magnets and structure | 20–30% |
| Blanket, first wall, [[divertor]] | 10–20% |
| Balance of plant (turbine, buildings, electrical) | 30–40% |
| Heating, current drive, fuel cycle, cryogenics | 10–20% |
| Contingency, engineering, owner's costs | 15–25% |

Two implications follow. First, **the fusion-specific parts are a minority of the cost**, which caps how much innovation in the core can reduce the total. Second, the **replaceable components** — blanket and divertor — are both capital and a recurring operating cost, because they must be replaced through the plant's life.

---

## 3. The variables that actually swing the answer

### Availability — the most underrated number

LCOE is roughly inversely proportional to capacity factor. A plant at **50% availability costs twice as much per MWh** as the same plant at 100%.

Fission achieves 90%+. Fusion's availability is bounded by **remote replacement of activated in-vessel components**, and no one has ever done it. If blanket replacement takes six months every two years, availability caps at 75% before any unplanned outage — and every additional day of outage is directly a cost.

This is why [[09-engineering-challenges|Document 09 §6]] argues that RAMI is the most likely reason a technically successful plant is commercially useless, and why DOE's roadmap makes a RAMI handbook a near-term deliverable.

### Cost of capital

Fusion plants are capital-heavy and fuel-light — the opposite of gas. That makes the **discount rate dominant**. At a 3% cost of capital a plant is competitive; at 10% the same plant is not. This is precisely why **power purchase agreements matter more than their megawatts suggest** (see §5): a signed, creditworthy offtake converts merchant risk into contracted revenue and can move the financing rate by several hundred basis points.

### Learning rate

The TU Berlin analysis notes that the sector's LCOE projections **imply learning rates above 30%** — meaning cost falls 30% for every doubling of cumulative capacity. Solar PV achieved roughly 20–25%. Large nuclear plants in the West achieved **negative** learning: they got more expensive with experience, because each was bespoke and regulatory requirements ratcheted.

Which precedent fusion follows depends almost entirely on **whether plants are built repeatedly to the same design**. Modular, factory-built architectures (Helion's pulsed units, Avalanche's 0.1 MWe modules, Thea's planar-coil arrays) are explicitly designed to get onto a manufacturing learning curve rather than a construction one.

### Fuel

Effectively free at scale — deuterium from seawater, lithium from brine — **once breeding works**. Before breeding works, tritium at **$30,000–35,000/g** makes fuel the dominant cost, which is another way of saying that a plant without a working blanket is not a power plant at any price.

---

## 4. The demand side changed: AI

This is the single most important market development of the current period, and it is why the funding curve turned upward in 2025–26 rather than in 2023.

### The numbers

- AI data-centre electricity demand: **460 TWh in 2024 → ~1,300 TWh by 2035**
- A single hyperscale AI facility draws **300–500 MW** — comparable to a mid-sized city
- As of May 2026, hyperscalers had committed to **over 9.8 GW across 13 nuclear projects**: Meta up to 6.6 GW, Amazon 960 MW, [[microsoft|Microsoft]] 835 MW (plus fusion), [[google|Google]] 500 MW

The FIA's 2026 foreword names this explicitly as the change: *"the last year has added an important new driver: the energy demand of artificial intelligence."*

### Why fusion fits this demand unusually well

| Buyer requirement | Fusion characteristic |
|---|---|
| Firm, 24/7 baseload | High capacity factor, no intermittency |
| Very high power density on a small footprint | Compact plants, siteable near load |
| Carbon-free, for corporate commitments | No CO₂ |
| Long-term price certainty | Negligible fuel cost exposure |
| Sited near load, avoiding transmission queues | No fuel logistics; no resource siting constraint |
| Politically easier than fission | No fissile material, no meltdown pathway, byproduct-material licensing |

That last row deserves emphasis. A hyperscaler siting a plant next to a data centre faces a very different local-politics problem with fusion than with fission, and the NRC's byproduct-material framework makes the difference regulatory as well as perceptual.

### The counterargument

Hyperscalers need power **now**, and fusion will not deliver in this decade at scale. Carnegie's June 2026 analysis of hyperscaler nuclear commitments against US energy realities makes exactly this point about the whole nuclear category. The fusion PPAs are therefore best understood not as procurement but as **option purchases and strategic signalling** — cheap relative to the buyers' balance sheets, valuable if they work, and useful for corporate positioning regardless.

That does not make them unimportant. Even as options, they do the financing work described below.

---

## 5. Offtake and commercial structures

### The agreements that exist

| Deal | Capacity | Timing | Significance |
|---|---|---|---|
| **Helion ↔ Microsoft** (2023) | **≥50 MW** after a 1-year ramp | Target **2028** | **The world's first fusion PPA.** Established that a creditworthy counterparty would sign |
| **Google ↔ CFS** | **200 MW** — half of ARC's output | Early 2030s | Largest fusion offtake; paired with direct equity investment |
| **Google ↔ TAE** | — | — | Equity investment |
| **Type One ↔ TVA** | 350 MW site agreement | Mid-2030s | A **public utility** siting fusion at a retired coal plant |
| **Eni ↔ UKAEA ([[h3at|H3AT]])** | — | — | An oil major funding tritium infrastructure |

Across the sector (FIA 2026): **6 companies have siting agreements**, 4 are evaluating sites; **5 have PPAs or offtake commitments**, 2 are in discussions.

### Why these agreements matter more than their megawatts

A first-of-a-kind plant is unfinanceable on merchant terms — no lender will underwrite construction risk plus technology risk plus price risk simultaneously. A long-term PPA with an investment-grade counterparty removes the third and mitigates the first two, which is what makes project debt possible.

The FIA's framing: these agreements *"provide the baseline for financing a fusion power plant, reducing market risk by ensuring that there will be buyers as soon as fusion has power to sell."*

CFS's application to **PJM Interconnection** — the first ever by a fusion company — is the corresponding step on the other side: getting into the interconnection queue for the largest US wholesale market, years ahead of having anything to connect.

### Non-electricity markets — the underrated part of the story

From the FIA survey, primary and secondary target markets:

| Market | Primary | Secondary |
|---|---|---|
| Electricity generation | **45** | 1 |
| **Industrial heat** | 13 | **14** |
| Off-grid energy | 10 | 7 |
| Medical | 5 | 7 |
| **Space propulsion** | 3 | **10** |
| Marine propulsion | 4 | 3 |
| Hydrogen and clean fuels | 3 | 7 |
| Components (HTS, magnets) | 0 | 3 |

Plus named others: **nuclear waste transmutation, tritium and other fusion fuels**.

**Industrial heat is the sleeper.** It avoids the thermal-cycle efficiency penalty entirely — you sell the heat rather than converting it — and industrial process heat is a large, hard-to-decarbonise market with high willingness to pay. **Realta explicitly targets industrial heat before grid electricity** for exactly this reason.

### The revenue-before-fusion strategy

A growing group of companies is generating income today from fusion-adjacent products, which is both a discipline and a survival mechanism:

- **[[shine-technologies|SHINE Technologies]]** ($1.1 bn) — neutron imaging, then medical isotopes (Mo-99), then waste recycling, then energy. **Has revenue now.**
- **[[astral-systems|Astral Systems]]** ($40 m) — sells continuous DD and DT irradiation services; has run hundreds of hours of commercial campaigns on breeder materials, and validated production of **Cu-64, Cu-67, I-131, Tb-161, Sc-44, Sc-47**
- **[[kyoto-fusioneering|Kyoto Fusioneering]]** ($144 m) — sells gyrotrons, tritium systems and blanket technology to the rest of the industry
- **[[tokamak-energy|Tokamak Energy]]** — sells HTS magnets via TE Magnetics; won the **£70 m [[step|STEP]] magnet contract**
- **CFS** — began selling magnets as a merchant product in April 2026
- **TAE** — TAE Power Solutions (power electronics, energy storage) and TAE Life Sciences (boron neutron capture therapy)
- **ASPL Fusion** (India) — planning BNCT and neutron activation analysis revenue before any fusion plant
- **[[avalanche-energy|Avalanche Energy]]** — building FusionWERX as a commercial fusion test facility

This is how a supply chain forms, and it is a considerably healthier sign than another billion-dollar round.

---

## 6. Capital: how much, from whom, and how much more is needed

### Where it stands

- **$14.24 billion** cumulative; **$4.48 bn** in the year to July 2026
- **$13.26 bn private / $0.98 bn public** — the private sector now dominates by more than 13:1
- Investor mix has broadened dramatically: alongside the venture names (Founders Fund, Lightspeed, Lowercarbon, Prime Movers Lab, Google Ventures, Bessemer), the 2026 list includes **pension funds** (HostPlus), **sovereign and strategic capital** (Al Mirqab, BPI France, SPRIND, IQT), **utilities and energy majors** (RWE, JERA, Kansai Electric), **industrial conglomerates** (Mitsubishi, Mitsui, Sumitomo Mitsui, Fujikura, NTT), and **traditional asset managers** (Fidelity, Morgan Stanley Counterpoint Global, Brevan Howard, Deerfield, Stanley Druckenmiller)

**CFS raising $1 billion from pension funds in July 2026** is the clearest marker of the shift: pension capital buys infrastructure, not science experiments.

### How much more is needed

Companies were asked how much further funding they require to deliver a commercial plant:

- **Average: $2.7 billion. Median: $1.2 billion.** (Up from $2.6 bn / $694 m in 2025 — the median nearly doubled)

56 companies at an average $2.7 bn implies well over **$100 billion** to carry the current field to commercial plants. Cumulative funding to date is $14 bn.

**Most of these companies will not raise their share.** That is not a criticism; it is the arithmetic of every capital-intensive technology transition. The FIA's CEO states the implication plainly: *"few expect there to be 56 companies"* in a commercial fusion industry.

### Public markets

- **[[general-fusion|General Fusion]] listed on Nasdaq as GFUZ in July 2026** — the first publicly traded fusion company — via merger with Spring Valley Acquisition Corp. III
- A second company was in process at the time of the FIA report

The FIA's assessment is that public markets bring capital *and* discipline: *"the day-to-day financial progress of companies able to be tracked simply on a minute-to-minute ticker symbol."* For a sector that has historically communicated through press releases, a quarterly reporting obligation is a structural change.

---

## 7. Competitive position: what fusion has to beat

Fusion will not arrive into a vacuum. By the mid-2030s it competes against:

| Competitor | Likely LCOE | Fusion's advantage | Fusion's disadvantage |
|---|---|---|---|
| Solar + 4h storage | $40–70/MWh | Firm, dispatchable, land-light | Far more expensive |
| Onshore wind + storage | $50–80/MWh | Firm; siteable anywhere | Far more expensive |
| Gas with CCS | $70–110/MWh | No CO₂ at all, no fuel price risk | Unproven |
| Advanced fission / SMR | $80–140/MWh | No meltdown path, no long-lived waste, easier siting | Fission will be commercially proven first |
| Geothermal (next-gen) | $60–100/MWh | Siteable anywhere | Geothermal is closer |

**Fusion's realistic mature LCOE of ~$110–145/MWh sits at or above the top of that table.** It does not win on price against solar and wind, and it should not be marketed as though it will.

Where it wins is on the attributes price does not capture: **firmness without fuel, siting flexibility without resource dependence, energy density without emissions, and no long-lived waste or proliferation pathway**. Those attributes are worth a premium in exactly the markets — hyperscale computing, industrial heat, island and off-grid systems, marine propulsion — where several companies are already targeting their first sales.

The strategically honest position is therefore not that fusion will be "too cheap to meter", but that it will be **a premium firm-power product** that gets cheaper with volume, and whose value is highest where land, transmission or fuel logistics are the binding constraint.

---

## 8. The bottom line

1. **The cost range is genuinely unknown** — $1,400 to $43,000/kW — and anyone quoting a single number is projecting confidence they do not have.
2. **The best independent analysis puts mature LCOE at $110–145/MWh** and explicitly warns policymakers that even this is optimistic.
3. **CFS's ARC at ~$6,250/kW is the field's first real cost data point.** Whether it comes in on that number is one of the most informative things that will happen this decade.
4. **Availability, not physics, is the most likely economic failure mode.**
5. **AI demand has given fusion a customer with the balance sheet and the urgency to pay a premium**, and that — not any technical result — is what turned the funding curve.
6. **Non-electricity revenue is where the sector is actually earning money today**, and it is building the supply chain that grid-scale fusion will need.
7. **Over $100 billion of further capital is implied** by the companies' own estimates. The sector has raised $14 bn. Consolidation is not a risk; it is the plan.


## Disposal cost is jurisdiction-dependent

Decommissioning and waste costs assume a disposal route. [[43-fusion-waste-classification-and-disposal]] shows that route is set
nationally: identical components can fall either side of a classification boundary in different
countries, with an order-of-magnitude cost difference between surface and deep geological disposal.
No LCOE figure in this corpus prices that variance.


## Evidence in `raw/`

Primary sources held in this vault that evidence the claims above:

- [[nuclear-fusion-for-ai-data-centers-2026]]

---

**Continue to:** [[11-policy-regulation-safety|11 — Policy, Regulation and Safety]] · [[13-roadmap-to-2040|13 — Roadmap to 2040]] · [[14-open-problems-and-risks|14 — Open Problems]]
