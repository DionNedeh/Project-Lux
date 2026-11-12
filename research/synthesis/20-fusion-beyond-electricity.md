---
title: "Fusion Beyond Electricity"
type: synthesis
doc: 20
part: 2
aliases:
  - "Fusion Beyond Electricity"
tags:
  - fusion/synthesis
  - fusion/markets
  - fusion/applications
created: 2026-08-25
updated: 2026-08-26
status: stable
confidence: high
related:
  - "[[09-engineering-challenges]]"
  - "[[10-economics-and-markets]]"
  - "[[11-policy-regulation-safety]]"
  - "[[21-the-graveyard]]"
  - "[[22-critical-materials-supply-chains]]"
---
# 20 — Fusion Beyond Electricity

*Project Lux · Space propulsion, medical isotopes, waste transmutation, process heat — and the revenue that arrives before the grid does*

---

## Why this matters more than it looks

The FIA's 2026 survey asked companies for both primary and secondary markets. The secondary column is the interesting one:

| Market | Primary | **Secondary** |
|---|---|---|
| Electricity generation | 45 | 1 |
| Industrial heat | 13 | **14** |
| **Space propulsion** | 3 | **10** |
| Off-grid energy | 10 | 7 |
| Medical | 5 | 7 |
| Hydrogen and clean fuels | 3 | 7 |
| Marine propulsion | 4 | 3 |
| Components (HTS, magnets) | 0 | 3 |

Also named: **nuclear waste transmutation, tritium and other fusion fuels**.

Two observations. **Space propulsion is the single largest secondary market** — larger than medical, hydrogen or marine. And **industrial heat is nearly as common a secondary market as electricity is a primary one.**

The strategic point is that these are not consolation prizes. A fusion neutron source is a *product* long before a fusion power plant is, and neutrons sell at prices that electricity never will. Several companies are already earning revenue this way, which is both a survival mechanism and a discipline that a purely pre-revenue sector lacks.

---

## 1. Neutrons as a product

A device that produces neutrons but nowhere near breakeven is useless as a power plant and potentially valuable as an irradiation service. Neutrons are used for materials testing, isotope production, non-destructive examination, and semiconductor testing, and there is a genuine shortage of high-flux 14 MeV sources.

### [[astral-systems|Astral Systems]] — the clearest example
**Bristol, UK · $40 m declared · inertial-electrostatic lattice confinement ("Multi-State Fusion")**

Astral sells irradiation, not electricity, **today**:

- Offering **large-volume, continuously operated DD and DT irradiation services** to commercial customers
- Completed **hundreds of hours of commercial irradiation campaigns** supporting research on **tritium breeder blanket materials including solid lithium, FLiBe and composite breeders** — i.e. it is directly serving the fusion sector's hardest problem
- Validated production of multiple medically relevant isotopes: **Cu-64, Cu-67, I-131, Tb-161, Sc-44, Sc-47**
- Built a **150-tonne shielded vault** to operate its high-flux DT volumetric neutron source; campaigns bookable directly
- **Berkeley, UK high-flux DT irradiation facility opening Q4 2026**; additional sites under consideration in Brazil, Canada, Sweden, USA and Germany
- Partners: UKAEA, University of Bristol, Bangor, McMaster, TU Munich, King's College London, IPEN

That list of isotopes is worth pausing on. **Tb-161 and Sc-47** are emerging therapeutic radionuclides with real clinical demand and constrained supply; **Cu-67** likewise. This is a functioning business.

### [[avalanche-energy|Avalanche Energy]] — FusionWERX
**Seattle · $104 m · magneto-electrostatic "Orbitron"**

Avalanche is building **FusionWERX**, a commercial test facility for developing and qualifying fusion technologies and hardware, including tritium handling equipment and superconducting magnets for future fusion neutron test stands. Its declared products already include spin-outs — **high-voltage feedthroughs, alphavoltaics, high-entropy alloys** — and it targets **0.1 MWe modular units** rather than grid plants. Partners: DARPA, DIU, AFWERX, Washington State.

### Why this matters to the whole field
[[09-engineering-challenges|Document 09]] identified the absence of a fusion-spectrum neutron source as the field's hardest problem, with [[ifmif-dones|IFMIF-DONES]] and FPNS both years away. **Commercial DT neutron services are a partial, imperfect, immediately available substitute** — not for 50 dpa qualification, but for breeder material screening, tritium release measurement, and detector development. A market response to a public infrastructure gap is a genuinely good outcome.

---

## 2. Medical isotopes

### The Mo-99 story
**Molybdenum-99** decays to **technetium-99m**, used in roughly 40 million diagnostic procedures a year — the workhorse of nuclear medicine. Historically it was produced in a handful of ageing research reactors using highly enriched uranium, a supply chain that is both fragile and a proliferation concern.

**[[shine-technologies|SHINE Technologies]]** ($1.1 bn, Janesville, Wisconsin) is building a non-reactor route: accelerator-driven fusion neutron sources irradiating a low-enriched uranium solution.

- **NNSA selected SHINE for $32 million** to complete its Mo-99 production facility, which is **approximately 75% complete**
- A proposed **Medicare rule includes a $10 add-on payment for radiopharmaceuticals derived from domestically produced Mo-99 from 1 January 2026** — a direct policy subsidy for exactly this supply chain

SHINE's model — **neutron imaging → medical isotopes → waste recycling → fusion energy**, in that order — is the most explicit "revenue ladder" in the industry, and it is why SHINE sits in the billion-dollar tier despite not pursuing a near-term power plant.

### Boron Neutron Capture Therapy (BNCT)

BNCT is a cell-level cancer radiotherapy. A boron-10-bearing drug concentrates in tumour cells; thermal neutrons are then absorbed by the B-10, triggering a reaction that releases short-range high-LET particles which kill the cell they were born in and spare its neighbour. It is particularly suited to **infiltrating tumours such as glioblastoma**, where conventional radiotherapy cannot achieve comparable selectivity.

Historically BNCT required a nuclear reactor, which confined it to a handful of sites. Since 2014, **accelerator-based epithermal neutron sources sitable inside hospitals** have been manufactured by **Sumitomo Heavy Industries, Hitachi and Mitsubishi** in Japan, and **Neutron Therapeutics** in the US.

Fusion-adjacent entrants:
- **TAE Life Sciences** — a [[tae-technologies|TAE Technologies]] spin-out, applying its accelerator and beam expertise to BNCT
- **ASPL Fusion** (India) — its phased roadmap begins with **PRABHA-BNCT**, an accelerator-based clinical BNCT facility with a shared non-destructive-examination vault, explicitly as a near-term revenue stream before any fusion plant

---

## 3. Fusion-fission hybrids

A concept with a long history, a bad reputation, and a genuinely strong technical argument.

### The idea
Surround a fusion neutron source with a **subcritical** fission blanket. The fusion device does not need to reach breakeven, because the fission blanket multiplies its energy by a large factor. The blanket does not need to be critical, because the fusion source supplies the neutrons — so it cannot run away, and it can burn fuel compositions a critical reactor cannot sustain.

### Why the technical case is strong

The published analyses are more favourable than the concept's reputation:

- A fusion-driven transmutation system combining a **subcritical fusion-fission hybrid** — uniquely able to burn the worst thermally non-fissile transuranic isotopes — **with a fuel cycle that uses cheaper light water reactors for most of the transmutation**
- **The number of hybrids needed to destroy a given amount of waste is an order of magnitude below the number of critical fast-spectrum reactors required**, because fast reactors cannot fully exploit that fuel cycle
- **Time for 99% transuranic waste destruction falls from centuries (with fast reactors) to decades**

Recent work includes coupling a **Reversed Field Pinch** to a **molten-salt subcritical test bed** with coexisting fast and thermal zones — allowing tritium breeding and actinide transmutation studies simultaneously — and neutronics studies of reflector choice in the **Fusion-Driven Subcritical Spent Fuel Burner (FDS-SFB)** model.

### Why it is unpopular anyway

The hybrid inherits **all of fission's political problems** — fissile material, proliferation sensitivity, spent fuel, criticality safety — while giving up fusion's cleanest selling point. The regulatory treatment would revert from byproduct material to full reactor licensing, discarding the advantage described in [[11-policy-regulation-safety|Document 11]]. And it requires *both* technologies to work.

### Who is doing it anyway

- **ASPL Fusion** (India) — **PRABHA-HYBRID**, a sub-critical fusion-fission hybrid producing **35 MW**, as step three of a four-step roadmap
- **Astral Systems** — "fission-fusion hybrid" is its stated energy capture approach; **2027 target for fusion-fission hybrid validation testing**
- Chinese programmes have historically shown interest in hybrid concepts as a bridge

**Assessment:** hybrids are the fastest route to *useful energy* from a fusion device, and the slowest route to *fusion's political advantages*. They are most likely to appear in countries with large existing fission fleets and spent-fuel inventories, and least likely where fusion is being marketed as fission's clean successor.

---

## 4. Space propulsion — the largest secondary market

### The physics case
Chemical rockets have specific impulse (I_sp) of 300–450 seconds — set by chemical bond energies. Fission-thermal reaches ~900 s. **Fusion propulsion concepts project 10,000–100,000+ s**, because the exhaust is plasma at fusion temperatures rather than combustion products.

For a spacecraft, that converts directly into either far more payload or far shorter trips. Mission studies for the outer planets that take a decade chemically fall to one to two years.

Fusion also has a specific advantage in space that it lacks on Earth: **it does not need to compete with solar and wind.** Beyond Jupiter, sunlight is too weak for photovoltaics, and the alternative is a radioisotope generator producing a few hundred watts. There is no cheap incumbent.

And a fusion device in space **does not need a steam cycle** — the plasma exhaust *is* the product, and [[direct-energy-conversion|direct energy conversion]] supplies onboard electrical power.

### Direct Fusion Drive (DFD)

The leading concept, developed at **PPPL since about 2001**, based on the **Princeton [[field-reversed-configuration|Field-Reversed Configuration]] (PFRC)**. A small FRC heated by odd-parity rotating magnetic fields, with a fraction of the plasma allowed to escape along open field lines as thrust while the rest of the fusion energy is recovered as electricity.

DFD leans toward **D-³He**, which minimises neutron production — critical in space, where shielding mass is prohibitive and there is no ground to bury activated components in.

- **Princeton Satellite Systems** is commercialising it; published mission studies include **a Titan mission using DFD** (arXiv:2009.12621)
- **Pulsar Fusion** (UK, founded 2011) is developing a compact DFD engine targeted operational by **2027**, and announced **"first plasma" in its Sunbird exhaust test system** — the first physical architecture of a fusion exhaust system for space travel. It has a research partnership with Princeton Satellite Systems applying **machine learning to PFRC-2 data**
- **Helicity Space** (founded 2018, $10 m declared) uses a **magneto-inertial plasma-jet** approach

### The honest assessment
None of these devices is close to fusion breakeven, and a propulsion system does not strictly need breakeven — it needs thrust and power at acceptable mass. That is a genuinely easier bar than a power plant, which is the strongest argument for the category.

It is also a market with one customer type (governments and a handful of space companies), long procurement cycles, and no revenue until a flight demonstration. Ten companies list it as a secondary market precisely because it is a plausible *option* rather than a plan.

---

## 5. Industrial heat, hydrogen, desalination

### Why heat before electricity is a serious argument

A fusion plant that sells **heat** avoids the thermal-cycle conversion penalty entirely. Instead of 400 MW of thermal output becoming 140 MW of saleable electricity at 35% efficiency, it becomes 400 MW of saleable heat. If the customer values heat at anything like the price of the gas they currently burn to make it, the economics change materially.

Industrial process heat is:
- A **large** market — roughly a quarter of global final energy demand
- **Genuinely hard to decarbonise** — electrification is inefficient for high-temperature processes; hydrogen is expensive; CCS is unpopular
- Willing to pay a **premium for firm, on-site, carbon-free heat**
- Located at industrial sites that already have permits, grid connections, cooling water and a workforce

**13 companies name industrial heat as a primary market and 14 as a secondary one.** **[[realta-fusion|Realta Fusion]] explicitly targets industrial process heat before grid electricity** — a rational sequencing given that its tandem mirror produces heat and direct-converted electricity in a compact, siteable package.

### Temperature tiers
The applications sort by required temperature:
- **Low grade** — district heating, **desalination** (steam distillation or powering reverse osmosis)
- **Mid grade** — chemical processing, food, paper
- **High grade** — **hydrogen production** (high-temperature steam electrolysis or thermochemical cycles), cement, steel

### Hydrogen and desalination
Fusion can supply hydrogen production either as electricity for electrolysis or, more efficiently, as high-temperature heat for **solid oxide electrolysis**, where some of the energy input comes as heat rather than electricity.

For desalination, the relevant feature is that **fusion plants provide the cheap, steady, round-the-clock power that desalination requires to run at high utilisation** — desalination plants are capital-heavy and uneconomic when run intermittently, which is why pairing them with renewables is awkward.

**Cogeneration** is the likeliest real configuration: a plant selling electricity as its primary product and adding revenue through desalination, direct air capture or district heating from waste heat.

### The counterweight
Analysts examining cost requirements for fusion-generated electricity, process heat and hydrogen conclude that **process heat and hydrogen will be tough early markets for fusion, but may open up as markets evolve.** The reason is straightforward: heat is currently cheap, because natural gas is cheap. Fusion's advantage in these markets depends on carbon pricing, on gas prices, or on customers with corporate decarbonisation commitments — the same logic that produced the hyperscaler PPAs.

---

## 6. Tritium and fuel as products

An underrated category. **"Tritium and other fusion fuels"** appears as a named market in the FIA survey, and the logic is sound: if fusion plants need tritium and [[lithium-6]] and the supply is constrained, then supplying them is a business.

- **[[kyoto-fusioneering|Kyoto Fusioneering]]** ($144 m) does not build reactors at all. It sells **gyrotrons, tritium systems and blanket technology** to everyone else, and is building **UNITY-1** (Japan) and **UNITY-2** (Canada), and now **[[unity-3|UNITY-3]] with ORNL** at Oak Ridge
- **Fusion Fuel Cycles (FFC)** appears as an Avalanche Energy partner
- **TAE Technologies and [[black-moon-energy|Black Moon Energy]]** announced a **helium-3 supply partnership on 5 August 2026** — see [[22-critical-materials-supply-chains|Document 22]]
- **CFS** selling magnets, **[[tokamak-energy|Tokamak Energy]]** selling magnets via TE Magnetics, **ORNL** licensing pellet fuelling to Type One

**This is the most important structural development in the sector**, and it is easy to miss because none of it makes headlines. An industry is not 56 companies each building everything; it is a supply chain. In 2026, for the first time, fusion has one.

---

## 7. Assessment

**The realistic sequence for fusion revenue is not "power plant, then everything else."** It is:

1. **Neutron irradiation services** — already selling (Astral, SHINE, Avalanche's FusionWERX)
2. **Medical isotopes** — already selling or near (SHINE, TAE Life Sciences)
3. **Components to other fusion companies** — began in earnest in 2026 (CFS, Tokamak Energy, Kyoto Fusioneering, ORNL)
4. **Industrial process heat** — targeted for first plants by several companies (Realta explicitly)
5. **Grid electricity** — 2028 at the earliest, 2030s realistically
6. **Space propulsion** — a genuine option, dependent on a flight demonstration nobody has funded
7. **Waste transmutation** — technically strong, politically encumbered, unlikely in the West

**For an investor or analyst, the useful screen is whether a company has a revenue path that does not require fusion breakeven.** For the field as a whole, these markets do something more valuable than generate cash: they build the tritium-handling expertise, the neutron-source capability, the magnet supply chain and the regulatory precedent that grid-scale fusion will need — and they do it a decade before the first plant needs them.

---

**Continue to:** [[21-the-graveyard|21 — The Graveyard]] · [[22-critical-materials-supply-chains|22 — Critical Materials and Supply Chains]] · [[10-economics-and-markets|10 — Economics and Markets]]
