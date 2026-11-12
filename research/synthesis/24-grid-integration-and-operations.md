---
title: "Grid Integration and Plant Operations"
type: synthesis
doc: 24
part: 2
aliases:
  - "Grid Integration and Plant Operations"
tags:
  - fusion/synthesis
  - fusion/operations
  - fusion/economics
created: 2026-08-25
updated: 2026-09-12
status: stable
confidence: high
related:
  - "[[05-inertial-confinement-fusion]]"
  - "[[09-engineering-challenges]]"
  - "[[helios]]"
  - "[[balance-of-plant]]"
  - "[[10-economics-and-markets]]"
  - "[[16-heating-current-drive-fuelling]]"
  - "[[25-failure-case-studies]]"
  - "[[27-people-institutions-public-trust]]"
  - "[[fusion-fission-twin-conjoint-public-support-2026]]"

---
# 24 — Grid Integration and Plant Operations

*Project Lux · A fusion plant is a pulsed heat source pretending to be a power station*

---

## 1. The problem the physics creates for the grid

A [[tokamak]]'s plasma current is driven inductively by a central solenoid acting as a transformer primary. A transformer has a finite volt-second budget. When it is exhausted, the pulse ends and the solenoid must be re-charged.

**[[iter|ITER]]'s design point is 500 MW for 400-second pulses.** [[eu-demo|EU DEMO]]'s baseline is pulsed. Most tokamak power plant designs assume pulses of **hours** followed by a **dwell** of minutes.

This is a real problem, and it is not primarily a grid-stability problem — it is a **turbine problem**.

> Because the tokamak operates in long-pulse mode, the electric power output from the plant exhibits significant pulsation, which **adversely affects steam turbine lifetime and power grid stability.**

Thermal cycling a several-hundred-megawatt steam turbine is the issue. Turbines are designed for continuous operation; thermal transients cause differential expansion, rotor stress and creep-fatigue damage in exactly the components that are most expensive to replace. A turbine cycled every few hours for thirty years is a different — and much shorter-lived — machine than one that runs continuously.

---

## 2. The three ways out

### 2.1 Thermal energy storage — the mainstream answer

Insert a **thermal buffer** between the fusion core and the power conversion system. During the burn, store surplus heat; during the dwell, discharge it. The turbine sees a smooth, continuous steam supply and never knows the plasma stopped.

This is the standard approach in European DEMO studies and it works, at a price:
- A molten-salt or similar store sized for a full dwell period is **large and expensive**
- Round-trip losses reduce net efficiency
- It adds a large, high-temperature, safety-relevant system to a plant that already has too many

#### What DEMO actually specified

The pre-concept design phase settled a reference per blanket, and the pair shows the trade in the open ([[maturation-of-critical-technologies-demo-balance-of-plant]]):

| | WCLL — direct coupling | HCPB — indirect coupling |
|---|---|---|
| Store | HITEC molten salt, **400 m³** | intermediate loop + larger store |
| Steam load in dwell | **~10% of nominal** | **same as pulse** |
| What it buys | generator stays synchronised | power conversion system is "not pulsed" |
| Turbine | still cycles | does not |

The small store is **not an energy system** — it is a synchronisation device, sized to stop the generator dropping off the grid rather than to keep selling power. Only the indirect variant actually removes the turbine-life penalty, and it pays for that with a whole intermediate heat transport system. The technology is borrowed from **concentrated solar power**, which is the one industry that has already qualified molten-salt storage at this scale (~200 MWe, up to 1 GWh_th).

The duty cycle it must cover is **2 hours of burn, ramps of 100–200 seconds, and about 10 minutes of dwell at 1–2% of nominal power** ([[tokamak-cooling-systems-and-power-conversion-system-options]]). Note the unsolved piece: the once-through steam generator has to run stably at **1% of nominal** in dwell, where industrial practice is 5% and above, and steam-turbine rotor materials for that duty remain open R&D.

Recent Chinese work (*Fusion Engineering and Design*, 2024; *Journal of Energy Storage*, 2026) proposes **hybrid thermal-plus-electrochemical storage**: thermal storage smooths the bulk output while a battery handles fast transients. The battery is small relative to the thermal store and considerably cheaper than sizing the thermal system for the worst case.

### 2.2 Steady-state operation — the physics answer

Drive the current non-inductively and never stop. As [[16-heating-current-drive-fuelling|Document 16 §5]] explains, this requires **[[bootstrap-current|bootstrap current]] fractions of 70–90%** in an advanced tokamak scenario, with the remainder driven by beams or RF at a recirculating-power cost.

Advanced scenarios are harder to control, more MHD-sensitive, and rely on internal transport barriers that are delicate. Steady-state is a genuinely harder physics problem than pulsed operation, which is why ITER and DEMO chose pulsed baselines and treat steady-state as an upgrade path.

**Stellarators simply do not have this problem.** No plasma current means no transformer, no dwell, no thermal cycling, and no storage system. Combined with the absence of disruptions, this is the strongest practical argument for the concept, and it is what "inherently steady-state" actually buys in plant terms — not a physics elegance point but the removal of a multi-hundred-million-dollar storage system and a turbine lifetime penalty.

#### What that looks like in a design

[[helios|Helios]] is the first plant design in this vault to publish its grid interface in detail ([[overview-of-the-helios-design]] — preconceptual, so projected). It has **no thermal store at all**, because it never stops: three steam turbines run continuously on 635 °C steam for **~390 MWe** net export, with an **88% capacity factor** limited by maintenance rather than by dwell ([[availability]]).

Its electrical architecture is nonetheless not simple:

- **Twin 300 MVA transformers** export from the turbine-generator at **345 kV**
- A **34.5 kV** medium-voltage backbone, fed by a station-service transformer, supplies six internal groups: primary heat transfer, ECRH and magnet power supplies, cryogenics, controls and computing, utilities, and tritium systems
- A **200–300 Mvar STATCOM or SVC**, harmonic filters and a **battery energy storage system** stabilise transients
- Steady-state auxiliary demand is **70 MW**, with ramp-rate-limited power-up sequencing through controls, cryogenics, fuelling and ECRH

So the storage system that §2.1 exists to avoid does not vanish entirely — it reappears, far smaller, as a battery sized for power-quality transients rather than for a full dwell period. That is the honest version of the steady-state advantage: a different and much cheaper storage problem, not none.

### 2.3 Embrace pulsing entirely — the Helion answer

**Helion** operates at the opposite extreme: pulse repetition on the order of **once per second or faster**, with **direct inductive energy recovery** rather than a thermal cycle. At that rate the pulsation is far above any grid or turbine timescale, and power electronics smooth it trivially. There is no steam cycle to thermally cycle because there is no steam cycle.

**Inertial fusion energy is similar.** A plant firing at **10–20 Hz** is, from the grid's perspective, continuous. The pulsation problem disappears entirely; it is replaced by target manufacture and chamber survival ([[05-inertial-confinement-fusion|Document 05]]).

**This is a genuine and underappreciated architectural advantage of the pulsed-and-fast concepts.** The problematic regime is precisely the middle one — pulses of minutes to hours — which is where the tokamak sits.

---

## 3. The other pulsed load: the machine's own power supplies

Before a fusion plant can put power on the grid, it draws enormous **pulsed power** from it. Ramping a multi-megaampere plasma current, energising poloidal field coils, and running heating systems means transient loads of hundreds of megawatts on second timescales.

Drawing that directly from the grid causes voltage flicker and, at ITER's scale, would be unacceptable to any transmission operator.

**The standard solution is flywheel energy storage.** Large flywheel generator sets store energy over minutes and release it over seconds, decoupling the machine from the grid:

- **[[asdex-upgrade|ASDEX Upgrade]]** runs on **three large flywheel generators** feeding its pulsed power supply system — high current for magnetic confinement, high voltage for additional heating
- [[jet|JET]] operated two flywheel generators of 775 MVA combined
- ITER has both steady-state and pulsed power distribution networks, drawing up to hundreds of megawatts during a pulse

Flywheel generator sets are used because of their large capacity and short working time — a good match to a tokamak's duty cycle, and a mature technology borrowed from the accelerator world.

---

## 4. Plant operations: the things that determine whether it earns money

### Availability, and where it goes

[[10-economics-and-markets|Document 10]] established that LCOE is roughly inversely proportional to capacity factor. Here is what actually consumes availability in a fusion plant:

| Cause | Frequency | Duration | Notes |
|---|---|---|---|
| **[[divertor|Divertor]] replacement** | Every 1–2 full-power years | Months | The most-loaded component |
| **Blanket module replacement** | Every 2–5 years | Months | Remote handling of activated, tritium-bearing modules |
| **Planned inspection** | Annual | Weeks | Remote inspection of an interior no human enters |
| **[[disruption|Disruption]] recovery** | Unplanned | Days to months | Damage-dependent; tokamaks only |
| **Magnet [[quench]]** | Rare | Weeks to years | Potentially catastrophic |
| **Tritium plant maintenance** | Continuous concern | — | Cannot be shut down independently |
| **Conventional plant** | As any thermal station | — | Turbine, generator, cooling |

Fission plants achieve 90%+ availability with **direct human access during outage**, fuel changes that take weeks, and forty years of accumulated operational practice. Fusion has none of those advantages.

DOE's roadmap treats this as a first-class problem: near-term, establish an **initial RAMI handbook with metrics, availability targets and design-for-maintainability guidance**; mid-term, **validate mock-up maintenance workflows and collect reliability data for predictive maintenance models**; and expand **RAMI analysis to top failure-mode studies and pilot-relevant reliability targets**.

That phrasing — *establish an initial handbook* — is worth noting. **The industry does not yet have agreed availability metrics for fusion plants**, let alone data.

### Operational planning is now a research topic

Recent work applies **mixed-integer programming unit-commitment models** — the standard tool for scheduling conventional generation fleets — to magnetic confinement fusion power plants (*Fusion Engineering and Design*, 2025). That such a paper needed writing tells you something: **nobody has yet worked out how a fusion plant bids into an electricity market.**

The open questions are practical and unglamorous:
- Can a fusion plant provide **frequency response** or **spinning reserve**? A tokamak cannot ramp quickly; a thermal store might
- What is its **forced outage rate** for capacity-market accreditation?
- Can it **black start**? Almost certainly not — a fusion plant needs substantial grid power to start
- How does a pulsed plant participate in a market that settles in five-minute intervals?

### Startup, shutdown and the tritium constraint

A fusion plant cannot be started from cold quickly. Cooling 10,000 tonnes of magnet to 4.5 K takes **weeks**. Conditioning the vacuum vessel takes days. This makes a fusion plant a **baseload machine by construction**, unsuited to load-following, and it means an unplanned trip is expensive in ways a gas turbine's is not.

There is also a fuel-cycle constraint with no analogue in fission: **tritium decays at 5.5% per year whether the plant runs or not.** An idle fusion plant is losing its fuel inventory continuously. Extended outages are therefore doubly costly — lost revenue plus lost tritium — and this feeds back into the fleet doubling-time argument in [[09-engineering-challenges|Document 09]].

---

## 5. Siting

A pattern has emerged across three continents, and it is deliberate:

| Project | Site | Former use |
|---|---|---|
| **CFS [[arc|ARC]]** | Chesterfield County, Virginia | James River Industrial Center |
| **UK [[step|STEP]]** | West Burton, Nottinghamshire | **Coal-fired power station** |
| **Type One [[infinity-two|Infinity Two]]** | Tennessee | **TVA former coal facility** |
| **Helion Orion** | Malaga, Washington | Industrial site near hydro generation |
| **Realta** | Madison, Wisconsin | **Former Oscar Mayer plant** |

**Retired industrial and coal sites are close to an ideal siting profile for fusion:**
- Existing high-capacity **grid connection and switchyard** — the interconnection queue is a multi-year obstacle for greenfield generation
- Existing **cooling water** rights and infrastructure
- Existing **industrial zoning** and environmental baseline
- A local workforce with **energy-industry skills** and a community that wants the jobs back
- Local politics that is **favourable rather than merely tolerant**

CFS's application to **PJM Interconnection** in early 2026 — the first ever by a fusion company — is the corresponding move on the grid side, and the fact that it happened years before there is anything to connect reflects how long interconnection takes.

---

## 6. What this means

**The pulsed tokamak is the awkward case, and it is also the leading concept.** Pulses of minutes to hours are precisely the timescale that damages turbines and requires expensive thermal storage. Faster-pulsed concepts (Helion, IFE) and continuous concepts (stellarators) both avoid it, from opposite directions.

**Thermal storage is a real cost that rarely appears in cost estimates.** A store sized for a DEMO-class dwell period is a significant capital item, and most published fusion LCOE figures do not obviously include it.

**Availability is the least-analysed and most economically decisive parameter in fusion**, and the industry is only now writing down how to measure it.

**Siting has quietly gone well.** Unanimous local approval in Virginia, a UK site transferred three and a half years early, and a US public utility hosting a [[stellarator]] are not the outcomes a technology with fusion's public-communication history might have expected. The coal-site strategy is working.

---

**Continue to:** [[25-failure-case-studies|25 — Failure Case Studies]] · [[27-people-institutions-public-trust|27 — People, Institutions and Public Trust]] · [[10-economics-and-markets|10 — Economics and Markets]]
