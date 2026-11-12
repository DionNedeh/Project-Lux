---
title: "Fusion Waste: Classification, Clearance and Disposal"
type: synthesis
doc: 43
part: 5
aliases:
  - "Fusion Waste"
  - "Radioactive Waste Classification"
tags:
  - fusion/synthesis
  - fusion/safety
  - fusion/materials
created: 2026-08-29
updated: 2026-08-29
status: stable
confidence: high
related:
  - "[[33-safety-environment-decommissioning]]"
  - "[[22-critical-materials-supply-chains]]"
  - "[[09-engineering-challenges]]"
  - "[[41-fusion-regulation-beyond-the-united-states]]"
  - "[[gonzalez-de-vicente-2022-fusion-waste]]"
---

# Fusion Waste: Classification, Clearance and Disposal

Fusion's most repeated public claim is that it produces no long-lived radioactive waste. The claim
is true in a narrow and important sense, and misleading in a broader one. Fusion avoids the
*category* of waste that dominates fission's political difficulty — high-level waste and
transuranics — while generating a **larger physical volume** of lower-activity material than the
fission plants it is compared against. That trade is real, it is well characterised in the
literature, and until now this corpus had not stated it.

The evidence base here is [[gonzalez-de-vicente-2022-fusion-waste|an IAEA-convened review]]
published in *Nuclear Fusion* in 2022, covering [[iter]], demonstration machines and power plants.

## 1. What fusion waste actually is

Fusion produces no fission products and no actinides. There is no spent fuel. What there is instead
is **activated structure**: the 14.1 MeV neutron flux transmutes the atoms of the vessel, blanket,
divertor and magnets that surround the plasma, turning the machine itself into the waste.

The inventory is therefore dominated by **structural steels** — reduced-activation
ferritic-martensitic grades such as EUROFER97 and F82H, plus AISI 316L, bainitic steels and JK2LB
(see [[rafm-steel]]). Add beryllium, [[tungsten-pfc|tungsten]], copper, and the lithium-bearing breeder materials
discussed under [[tritium-breeding-ratio]].

Two consequences follow immediately. Decay heat is far lower than for spent fission fuel, so passive
cooling suffices and the accident pathways in [[33-safety-environment-decommissioning]] stay bounded.
And the radiotoxicity falls rapidly rather than over geological time. The IAEA review states plainly
that fusion "should be able to avoid creating high-level waste".

That is the strong form of the claim, and it survives scrutiny.

## 2. The volume problem

Here is the part the public framing omits.

[[eu-demo]] could generate **as much as 10,000 tonnes of solid waste from in-vessel components
alone**. The comparison offered is the European sodium-cooled fast reactor: roughly **2,000 t** of
activated structure plus an estimated **300 t** of spent fuel over its lifetime — about **2,500 t**
in total of intermediate- and high-level waste.

Fusion's figure is roughly **four times larger**, and the review is careful to say the burden is
significant "both in terms of pure volume and volume per unit of electricity produced" — so this is
not an artefact of comparing a demonstration machine against a commercial one.

The reason is geometric. A fusion power core is a large, thin-walled, neutron-soaked structure with
an enormous surface area facing the plasma, and its most irradiated components — first wall,
divertor, breeding blanket — are **consumable**. They are replaced on a schedule, as
[[09-engineering-challenges]] sets out, and every replacement set becomes waste. A fission core is
compact, and its waste is concentrated in a small mass of fuel.

So the honest summary is: **fusion trades waste intensity for waste volume.** Whether that is a good
trade depends entirely on disposal cost per cubic metre and on whether the material can be cleared
or recycled rather than buried — which is why the next two sections matter more than they appear to.

## 3. Impurities decide the disposal route

The most operationally significant finding in the review is that what forces fusion waste into a
higher disposal class is usually **not** the designed alloy at all.

Long-lived isotopes arise from alloying elements — niobium, molybdenum, nickel, carbon, nitrogen,
copper, aluminium — and, critically, from **uncontrolled impurities** of those same elements plus
potassium and cobalt. After irradiation, the review states, these isotopes "might preclude disposal
in LLW repositories".

The isotope that recurs is **⁹⁴Nb**, produced from niobium present at parts-per-million levels as a
tramp element in commercial steel. Nobody specifies niobium into a fusion steel; it arrives with the
feedstock.

This turns a waste problem into a **supply-chain problem**, and connects directly to
[[22-critical-materials-supply-chains]]. Meeting a disposal class requires controlling the impurity
content of thousands of tonnes of steel — which means dedicated melts, verified feedstock, and a
qualified supplier base that does not currently exist at that scale. An ORNL steel formulation is
cited as mitigating most identified vacuum-vessel problems and meeting LLW disposal requirements,
demonstrating that the lever works. It is a metallurgy and procurement lever, not a physics one.

## 4. Classification is jurisdictional, not physical

There is no international definition of what fusion waste *is*. Classification is national, and the
boundaries differ.

The UK scheme runs Very Low Level Waste, Low Level Waste, Intermediate Level Waste and High Level
Waste, with LLW bounded near 4×10⁶ Bq/kg alpha and 12×10⁶ Bq/kg beta/gamma, and ILW routed to deep
disposal. France operates a LILW-SL class with an alpha limit cited at **4 MBq/kg** and, separately,
**nuclide-specific** limits.

The review's sharpest observation follows from that structure: ⁹⁴Nb activity in a given component
"could exceed the nuclide-specific limit under France's LLW" while satisfying UK repository criteria.

**The same physical object is two different waste classes in two countries.** A blanket module that
is disposable in one jurisdiction requires geological disposal in another — with an order-of-
magnitude cost difference and a different regulator.

This compounds the regulatory divergence documented in
[[41-fusion-regulation-beyond-the-united-states]]. A fusion industry expecting to sell a
standardised plant across borders inherits a **non-standardised waste liability**, and that
liability lands on the operator's balance sheet, not the vendor's. It belongs in the cost analysis
of [[10-economics-and-markets]] and in the liability discussion of
[[23-standards-codes-liability]], where it is currently absent.

## 5. Recycling and clearance are load-bearing

Given the volumes, disposal alone does not close. The review treats recycling and **clearance** —
the release of material from regulatory control once activity falls below a threshold — as
"essential to support fusion deployment". Not preferable. Essential.

The mechanism is decay during interim storage. Much of the inventory is dominated by
relatively short-lived activation products, so a storage period lets material fall through a
classification boundary; a storage building suffices for LLW awaiting clearance, which is a modest
facility by nuclear standards. Tritium is the awkward exception — under UK classification, tritium
activity has been reported to remain above LLW limits for around 80 years, which sets a storage
horizon measured in human careers.

The strategic implication is that **a fusion plant's waste outcome is fixed at the procurement
stage**, decades before decommissioning. Choose the steel and control the impurities, and most of
the inventory clears after storage. Fail to, and thousands of tonnes require deep disposal. There is
no remediation available later; you cannot un-activate a component.

## 5a. Tritium sets the storage horizon

Tritium is the awkward exception to the rapid-decay story, and it deserves separating out.

Everything else in the inventory is activation product: irradiate steel, wait, and the activity
falls. Tritium is different because it is **fuel**, it is mobile, and it permeates the structures it
touches. It has a 12.3-year half-life, which sounds short, but the starting inventories in a power
plant are large and the regulatory limits are low. Under UK classification, tritium activity in
fusion waste has been reported to remain above LLW limits for **around 80 years**.

That number sets a planning horizon nothing else in the fuel cycle does. An operator cannot dispose
of tritiated components on decommissioning; it must hold them, in monitored storage, for a period
longer than the operating life of the plant that produced them. The storage facility itself is
modest — a building, not a repository — but the **institutional** requirement is not: it needs an
organisation that still exists, and still holds a licence, three generations after shutdown.

This is the same institutional-continuity problem that fission decommissioning has repeatedly run
into, and [[33-safety-environment-decommissioning]] should read it alongside the liability
discussion. It is not a technical obstacle. It is a question about who is still there.

## 5b. What recycling and clearance actually require

If clearance is essential rather than optional, it is worth being precise about what it demands.

Clearance is a **regulatory release**: material falls below a threshold and leaves the controlled
regime entirely, becoming ordinary scrap. Recycling is different — material stays inside the
radiological boundary and is re-manufactured into new fusion components, never entering public
commerce. The two have very different requirements, and conflating them overstates how easy the
strategy is.

Recycling inside the boundary means remote handling at industrial scale. The review's estimates for
ARIES-ACT2 components use a conservative remote-handling dose limit in the range of
10³–10⁴, and at those levels components cannot be handled directly by people at any point in the
re-manufacturing chain. That implies a shielded, remotely operated re-manufacturing facility — an
industrial plant of a kind that does not exist anywhere for fusion, and whose cost appears in no
LCOE estimate in this corpus. [[29-remote-handling-and-maintenance]] describes the difficulty of
doing remote handling for *maintenance*; doing it for *materials processing* is a larger ask.

Clearance, by contrast, requires only patience and measurement — but it requires the impurity
control of §3 to have been done correctly at procurement, decades earlier. If it was not, no amount
of storage brings ⁹⁴Nb below a nuclide-specific limit on any useful timescale.

There is also a materials-recovery argument that the review makes and that this corpus should
record: recycling reclaims beryllium, tungsten and lithium-6, all of which
[[22-critical-materials-supply-chains]] identifies as constrained. **300–400 t of beryllium** in a
single plant is a significant fraction of world supply, and the **600 m³** of flowing PbLi in ARIES
designs carries both lithium-6 and a ²¹⁰Po hazard. Treating that as waste rather than as feedstock
would be a supply-chain decision as much as a waste one.

## 6. What this changes

Three things, for this corpus.

**The public claim needs qualifying.** "No long-lived waste" should read: *no high-level waste and
no transuranics, but a substantially larger volume of low- and intermediate-level waste, whose
disposal class depends on impurity control and on which country you are in.* That is still a
favourable comparison. It is not the absence of a waste problem, and [[39-the-discourse]] should
treat the unqualified version as an instance of the pattern it documents.

**Waste is a materials and procurement problem.** It resolves into the same binding constraint this
corpus reaches elsewhere: the qualified supply of well-characterised structural material. It sits
alongside [[helium-embrittlement]] and tritium breeding as a metallurgy problem, not a plasma
physics one.

**It is unquantified for real machines.** Every tonnage here is a design-stage estimate for a
conceptual plant. No fusion power plant has been decommissioned; [[jet]]'s decommissioning and
repurposing programme is the only large-scale exercise underway, and it is the one place where these
numbers will first meet reality.

> [!warning] Confidence
> The classification schemes and the mechanism are well established. The **tonnages are conceptual
> design estimates**, not measured inventories, and the 10,000 t figure is a stated upper bound
> ("as much as"), not a central case. Treat the ratio against fission as indicative of direction,
> not as a precise multiple.
