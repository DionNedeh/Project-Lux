---
title: "Critical Materials and Supply Chains"
type: synthesis
doc: 22
part: 2
aliases:
  - "Critical Materials and Supply Chains"
tags:
  - fusion/synthesis
  - fusion/materials
  - fusion/supply-chain
created: 2026-08-25
updated: 2026-11-02
status: stable
confidence: high
related:
  - "[[09-engineering-challenges]]"
  - "[[helios]]"
  - "[[rafm-steel]]"
  - "[[18-superconductors-and-magnets]]"
  - "[[23-standards-codes-liability]]"
  - "[[24-grid-integration-and-operations]]"
---
# 22 — Critical Materials and Supply Chains

*Project Lux · The physical inputs fusion cannot substitute, and the 2026 helium crisis nobody saw coming*

---

## The materials a fusion plant cannot do without

Beyond structural steel, a fusion plant depends on a short list of elements for which there is **no functional substitute**:

| Material | Function | Why it cannot be swapped |
|---|---|---|
| **[[lithium-6|Lithium-6]]** | Tritium breeding | The only practical breeding reaction |
| **[[beryllium]]** or **lead** | Neutron multiplication | TBR > 1 is impossible without one of them |
| **[[tungsten-pfc|Tungsten]]** | Plasma-facing components | Highest melting point of any metal; lowest sputtering yield |
| **Helium-4** | Cryogenics, and coolant in gas-cooled blankets | Nothing else is liquid at 4 K |
| **REBCO (rare earths, barium, copper)** | HTS magnets | The whole high-field thesis |
| **Niobium, tin, titanium** | LTS magnets | ITER-class systems |
| **Tantalum** | Functional additions to reduced-activation steel | Low-activation substitute for niobium in structure |
| **Helium-3** | D-³He fuel cycles | Aneutronic-leaning fuel; essentially unobtainable terrestrially |

Lithium-6 and REBCO tape were covered in [[09-engineering-challenges|Document 09]] and [[18-superconductors-and-magnets|Document 18]]. This document covers what those did not: **helium, beryllium, tungsten, and helium-3** — and the acute supply shock that hit in 2026.

---

## 1. The 2026 helium crisis

This is the most immediately consequential supply-chain event in the period this dossier covers, and it arrived from an entirely unanticipated direction.

### What happened

In **late February and early March 2026**, missile and drone strikes on **Qatar's Ras Laffan Industrial City** took roughly **a third of global helium supply offline**. The **near-simultaneous closure of the Strait of Hormuz** to commercial shipping blocked much of what remained from reaching international markets.

**Ras Laffan alone accounts for 30–38% of global helium output.**

### The consequences

- **Spot prices doubled** immediately
- Asian semiconductor fabrication inventories — estimated at roughly a **six-month supply** — began drawing down, with analysts warning the constraint becomes severe as those are exhausted
- Seagate and Western Digital reported **full 2026 production allocations with 20–30% price increases** from March. Every hard drive of 10 TB and above uses helium as a sealed internal gas, **with no substitute**

### Why fusion is exposed

Helium is not a fusion input in the sense that lithium is. It is worse than that: **it is the working fluid of the entire cryogenic system**, and no superconducting magnet operates without it.

The scale, from [[iter|ITER]]:

| | |
|---|---|
| Helium inventory | **~25 tonnes** |
| Distribution network | ~5 km of pipes, pumps and valves |
| Cooling capacity | 75 kW at 4.5 K |
| Mass cooled | 10,000 tonnes of magnets, plus shields, cryopumps, diagnostics |

Helium is also used as the **coolant in helium-cooled blanket designs** (HCPB, HCLL), as a purge gas in solid breeder blankets, and it is the **product** of the fusion reaction itself — [[helium-ash|helium ash]] that must be pumped out of the plasma.

Helium's fundamental problem is that it is **irrecoverable**. Released to atmosphere, it escapes Earth's gravity. It is produced by alpha decay in the crust over geological time and captured only where natural gas geology traps it. **There is no synthetic route.** A fusion industry that scales into a constrained helium market is competing with semiconductor fabs, MRI scanners and party balloons for a non-renewable resource.

### Mitigations
- **Closed-loop recovery.** Modern cryoplants recover and re-liquefy helium rather than venting it. ITER's system is designed for storage and recovery of the full inventory in warm and cold gaseous tanks.
- **HTS at 20 K.** Operating magnets at 20 K rather than 4.5 K reduces both the Carnot penalty and the helium requirement, and opens the possibility of **conduction cooling with cryocoolers** rather than a liquid helium bath. This is a genuine, under-discussed strategic advantage of the HTS transition.
- **Diversified supply** — new capacity in Russia (Amur), Algeria, Tanzania and the US. All are years from filling a 30% gap.

**Assessment:** the helium crisis is unlikely to stop fusion, but it raises operating costs, lengthens procurement, and adds a geopolitical exposure that nobody had on their risk register in 2025. It also strengthens the case for HTS on grounds that have nothing to do with magnetic field.

---

## 2. Beryllium

**Function:** the best neutron multiplier available. `⁹Be + n → 2n + 2⁴He` is what allows a blanket to breed more than one tritium per fusion neutron. Beryllium was also ITER's original first-wall material (later revised toward tungsten).

**Why it is a problem:**

- **Toxicity.** Beryllium dust causes **chronic beryllium disease**, an irreversible granulomatous lung condition, at very low exposures. Handling requires stringent containment and medical surveillance, which raises costs across manufacturing, installation and — critically — **remote maintenance and decommissioning**, where activated beryllium dust is both a radiological and a chemical hazard.
- **Scarcity and concentration.** Global production is small and concentrated in a handful of operations, dominated by the United States and Kazakhstan.
- **Activation.** Beryllium transmutes under neutron irradiation, including to long-lived isotopes, which complicates the "fusion waste decays in 50–100 years" claim.
- **Swelling.** Helium generation inside beryllium causes dimensional change under irradiation.

**The alternative:** **lead**, via `²⁰⁸Pb + n → 2n + ²⁰⁷Pb`. Abundant, cheap, non-toxic by comparison, and already present as the carrier in **lithium-lead (PbLi)** liquid breeders — which is a substantial part of why PbLi blanket designs (WCLL, HCLL, DCLL) are so widely pursued. Lead is a less effective multiplier, so lead-based designs need more careful neutronics to reach TBR > 1.1.

**The trend is clearly away from beryllium**, and the toxicity and waste arguments are as important as the neutronics.

---

## 3. Tungsten

**Function:** plasma-facing components, principally the [[divertor]]. Highest melting point of any metal (3,422 °C), lowest sputtering yield of any practical candidate, low tritium retention.

**The supply problem:** **over 80% of global tungsten supply is controlled by non-Western entities**, with China overwhelmingly dominant in both mining and processing. The semiconductor industry — which uses tungsten for contact plugs in 3D transistors — has already absorbed a **"geopolitical premium" estimated to add a 25% cost floor** to advanced logic.

Fusion enters this market as a new and demanding customer, needing not commodity tungsten but **precision-manufactured, monoblock, actively cooled tungsten-copper components** in quantities no one has previously produced.

For a sense of that quantity from an actual design: [[helios|Helios]]'s divertor targets are **51,000 tessellated hexagonal tungsten tiles, 2.5 cm across**, per plant ([[overview-of-the-helios-design]]). That is one subsystem of one machine, and the tiles are precision components under 10 MW/m² with helium-jet cooling — not stock material.

**The material problems** (covered in [[09-engineering-challenges|Document 09]]) compound the supply one: recrystallisation above ~1300 °C, a ductile-to-brittle transition around 400 °C that irradiation pushes higher, and transmutation to rhenium and osmium under neutron flux. Helium implantation in tungsten also produces the "fuzz" nanostructure that degrades surfaces — an active research area in its own right.

**The alternative:** **liquid metal plasma-facing components** — flowing lithium or tin. A liquid cannot be damaged by neutrons, cannot recrystallise, and self-heals after erosion. DOE's long-term Challenge Area B milestone is to *"operate continuous-flow liquid walls proving stability, impurity control, and tritium recovery for power-plant readiness."* If liquid walls work, both the tungsten supply problem and the tungsten materials problem disappear at once, which is why the concept attracts disproportionate attention relative to its maturity.

---

## 4. Helium-3 — and the lunar question

### Why anyone wants it

The **D-³He** reaction produces 18.35 MeV entirely in charged particles: `D + ³He → ⁴He (3.6 MeV) + p (14.7 MeV)`. No primary neutron. That means:

- **Little to no activation** of the structure
- **No tritium breeding blanket required**
- **[[direct-energy-conversion|Direct energy conversion]]** of charged products, bypassing the Carnot limit
- Radically simpler maintenance and waste

The catch is that D-D side reactions still produce neutrons, so it is *neutron-lean* rather than aneutronic — and D-³He requires substantially higher temperatures than D-T.

### Why it is essentially unobtainable

Helium-3 is produced terrestrially almost exclusively as a **tritium decay product** — tritium beta-decays to ³He with a 12.3-year half-life. So the world's helium-3 comes from the same nuclear-weapons and CANDU tritium inventories that constrain fusion fuel in the first place. Annual supply is measured in **tens of kilograms**, most of it committed to neutron detection for homeland security and to cryogenics.

**[[helion-energy|Helion Energy]]'s approach is the elegant workaround**: breed its own ³He *in situ* from D-D reactions, then burn it. This makes the fuel cycle self-contained and is one of the more clever architectural decisions in the sector.

### The lunar proposition

The solar wind has implanted helium-3 in lunar regolith over billions of years, unshielded by any magnetosphere. This has been discussed since the 1980s and was, until recently, firmly in the category of speculative futurism.

**It stopped being speculative in 2026:**

- **[[black-moon-energy|Black Moon Energy]]** unveiled a **robotic lunar mission** to collect data and de-risk future helium-3 production, partnered with **NASA's Jet Propulsion Laboratory and Caltech**, who will oversee robotic systems, instrumentation, data collection and mission operations
- Black Moon holds **$500 million in helium-3 contracts** to supply the **Department of Energy and fusion reactor companies**
- It targets **2029** for a reconnaissance rover to assess feasibility
- On **5 August 2026, [[tae-technologies|TAE Technologies]] and Black Moon Energy announced a strategic helium-3 supply partnership**

### The arithmetic problem

Helium-3 concentrations in lunar regolith are on the order of **parts per billion**. Historical estimates run to roughly **100 million tonnes of regolith processed per tonne of helium-3** recovered.

That is a mining operation of a scale never attempted on Earth, conducted on the Moon, requiring the regolith to be heated to several hundred degrees to release the implanted gas, powered by something, with the product returned to Earth.

**Assessment.** The contracts and the JPL partnership are real, and $500 million of committed offtake is not nothing. But the physical arithmetic has not changed since the 1980s, and the concentration is the problem — not the launch cost, not the robotics. The most defensible reading is that lunar helium-3 is a **long-dated option** whose near-term value is partly in the terrestrial supply agreements and partly in the attention it brings, and that any fusion company whose fuel plan *depends* on it has a fuel plan that will not survive contact with a mining engineer.

Helion's in-situ breeding remains the only ³He supply route that does not require a new extraterrestrial industry.

---

## 5. Vanadium — the dependency a ⁶Li-free design moves onto

*Added 2026-11-02. This document previously tracked four chokepoints and did not include this one.*

The four above are the chokepoints of a **particular** blanket architecture. A design that breeds
on natural lithium escapes the ⁶Li enrichment concentration — and lands on
[[vanadium-alloys|V-4Cr-4Ti]] instead.

[[st-e1|ST-E1]] makes exactly that trade: natural, unenriched liquid lithium, with V-4Cr-4Ti as the
centre-column shield structural material
([[st-e1-tritium-systems-crossref-metadata-2026]], [[st-e1-neutronics-crossref-metadata-2026]]).
[[ukaea-2026-vanadium-strategy|UKAEA]] states the enabling physics plainly: V-4Cr-4Ti's thermal
conductivity and nuclear properties *"reduce the need for neutron multipliers or lithium-6
enrichment in liquid lithium breeder blanket systems."*

### Why it is a chokepoint and not a solution

| Fact | Figure |
|---|---|
| Largest documented V-4Cr-4Ti heat | **1200 kg** (industrial, Johnson & Smith) |
| NIFS-HEAT-1 | 30 kg, 200 kg planned |
| SWIP-30 | 30 kg |
| DOE near-term milestone | domestic **500 kg** V-alloy heat capability |

There is **no standing commercial production line** for fusion-grade vanadium alloy anywhere.
UKAEA lists building a domestic supply chain and industrialising the alloy as *long-term bets*, and
a white paper on industrialisation as a future output — which is to say the supply chain is a plan,
not an asset. Impurity control is the binding technical constraint, and commercial **lithium**
purity is reported as *lower today than in the 1980s–90s*.

> [!warning] The tonnage figures in circulation are a trade association's, not a journal's
> **Vanitec** (3 June 2026, Dr Yu Li) puts a commercial reactor at **500–1,500 t** of V-4Cr-4Ti
> against global vanadium production of *"approximately 120,000 tonnes per year"*, scaling to
> 46,000–138,000 t for 100 reactors. These are described as *illustrative deployment scenarios*.
> The peer-reviewed review they accompany — **Muroga, Zheng & Yang**, *Current Opinion in Solid
> State and Materials Science* **36** (2025) 101224 — **is not held in this vault**: ScienceDirect
> returned HTTP 403 on 2 November 2026 and no OSTI deposit was found despite an ORNL co-author.
> **Whether the tonnages are the review's or Vanitec's own arithmetic could not be determined**,
> and they should not be cited as a published finding until the review is read.

So the honest position is narrower than the Li-6 entry above: the **concentration risk is unknown**
because no capacity analysis has been read, while the **production-scale risk is documented and
large** — a 1200 kg historical maximum against a plant needing, on the only estimate available,
three orders of magnitude more.

## 6. The supply chain as a whole

### What the industry itself says

From the FIA 2026 survey, **supply chain readiness for specialised components** is named by **15 companies as a near-term challenge and 20 as a long-term one** — and it is one of only three issues whose long-term score is *higher* than its near-term score. The industry expects this to get worse, not better.

The other two rising concerns are **full life-cycle issues** (10 → 14) and **PPAs and offtake** (2 → 6).

### The concentration map

| Input | Where the capacity is | Exposure |
|---|---|---|
| **Helium** | Qatar (30–38%), US, Algeria, Russia | **Acute — 2026 crisis ongoing** |
| **Lithium-6 enrichment** | Historically Russia and China | High — no Western capacity at scale, **though design-dependent: see below** |
| **Tungsten** | China (>80% with other non-Western producers) | High |
| **REBCO tape** | ~10,000 km/yr globally; significant Chinese strength | High |
| **Beryllium** | US, Kazakhstan | Moderate, but toxicity-limited |
| **Tritium** | CANDU reactors: Canada, South Korea, Romania | Structural — 30–40 kg world inventory |
| **Nb₃Sn** | Expanded ~10× by ITER procurement | **Low — a genuine ITER legacy** |
| **Vanadium alloy (V-4Cr-4Ti)** | No fusion-grade capacity at scale | Emerging — see below |

**Vanadium is the newest entry on this map.** It appears here because a company design now depends on it: [[helios|Helios]] selects V-4Cr-4Ti over [[rafm-steel|RAFM steel]] for its first wall, and the paper itself lists an **immature supply chain** among the contraindications ([[overview-of-the-helios-design]]). DOE's near-term milestone asks only for **500 kg** of V-alloy industrial heat capability — a figure that indicates how far from plant quantities the current base is.

That last row is the encouraging one and worth noting: **ITER's most durable contribution may prove to be industrial rather than scientific.** It built a global Nb₃Sn supply chain, large-scale cryogenics capability, and precision manufacturing capacity that did not previously exist, and all of it now serves companies that will reach a plant before ITER reaches D-T.

### What is being done

- **[[arpa-e|ARPA-E]] SCALEUP: $20 m to [[thea-energy|Thea Energy]]** (July 2026) for the first US modular HTS magnet production line
- **CFS selling magnets as a merchant product** from April 2026 — creating aggregate demand to justify tape capacity investment
- **DOE roadmap: "Seed Fusion Supply Chains"** as an explicit Grow-pillar key action
- **DOE materials milestones**: establish domestic industrial heat capability for **multi-tonne Fe-alloy and 500 kg V-alloy** heats — i.e. the ability to melt fusion-grade steel domestically at industrial scale, which currently does not exist
- **UK [[librti|LIBRTI]] (£220 m)** addressing lithium and tritium directly

> [!note] One chokepoint can be designed around, which is worth stating precisely
> Added 2026-10-19. **[[st-e1|ST-E1]] breeds on pure, unenriched lithium**, selected explicitly to
> reach a high *volumetric* [[tritium-breeding-ratio|TBR]] without ⁶Li enrichment and without
> extensive [[beryllium|beryllium]] multiplication ([[willis-2026-st-e1-pre-concept-design-overview]]).
>
> This is the only such route in the corpus, and it does not dissolve the exposure recorded above —
> most designs in this vault do need 30–90% enrichment, and the enrichment capacity concentration is
> real. What it establishes is that **⁶Li enrichment is a chokepoint for a class of blanket
> architectures, not an unavoidable input to D-T fusion.** A low-aspect-ratio machine can trade
> blanket volume and coverage for isotopic enrichment.
>
> The same design also substitutes **vanadium alloys for [[rafm-steel|RAFM steel]]**, which moves
> rather than removes a materials dependency — vanadium is not among the four chokepoints this
> document tracks, and the corpus holds no supply analysis for it. **That is a gap, not a
> reassurance.**
>
> The claim is asserted in a pre-concept overview whose supporting neutronics papers are not held,
> and no breeding blanket has operated in any device. Treat it as a design route, not a solved
> supply problem.
- **[[kyoto-fusioneering|Kyoto Fusioneering]]** operating as a merchant supplier of gyrotrons, tritium systems and blanket technology across the industry

### The honest assessment

**No single material on this list is a hard blocker.** Every one has a substitution, a recovery path, or an expansion route. But every one is a **cost and schedule multiplier**, several are concentrated in jurisdictions that Western programmes treat as strategic competitors, and the 2026 helium crisis demonstrated that the binding constraint can arrive from a direction nobody modelled.

The strategic conclusion is the one the DOE roadmap and the FIA both reach: **fusion's supply chain is currently sized for a research programme, not an industry**, and closing that gap requires industrial policy rather than technology. It is one of the few problems in this dossier that money alone can actually solve — but it takes about a decade of it, starting before the plants exist.


## Impurity control as a waste requirement

[[gonzalez-de-vicente-2022-fusion-waste]] establishes that what forces fusion components into a higher disposal class is usually
not the designed alloy but **uncontrolled impurities** — niobium, cobalt and potassium arriving as
tramp elements in commercial steel. ⁹⁴Nb from parts-per-million niobium can preclude LLW disposal.
This makes disposal class a **procurement specification**: dedicated melts and verified feedstock
across thousands of tonnes of steel, from a qualified supplier base that does not yet exist at
scale. See [[43-fusion-waste-classification-and-disposal]].

---

**Continue to:** [[23-standards-codes-liability|23 — Standards, Codes and Liability]] · [[24-grid-integration-and-operations|24 — Grid Integration and Plant Operations]] · [[18-superconductors-and-magnets|18 — Superconductors and Magnets]]
