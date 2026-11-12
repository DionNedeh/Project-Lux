---
title: "Military, Dual-Use and Security"
type: synthesis
doc: 37
part: 3
aliases:
  - "Military, Dual-Use and Security"
tags:
  - fusion/synthesis
  - fusion/policy
  - fusion/security
created: 2026-08-25
updated: 2026-10-19
status: stable
confidence: high
related:
  - "[[tritium-accountancy]]"
  - "[[08-national-programs]]"
  - "[[11-policy-regulation-safety]]"
  - "[[22-critical-materials-supply-chains]]"
  - "[[32-heavy-ion-fusion-and-pulsed-power]]"
  - "[[38-component-manufacturing]]"
  - "[[39-the-discourse]]"
  - "[[china-fusion-device-radiation-safety-2025]]"

---
# 37 — Military, Dual-Use and Security

*Project Lux · The defence money in fusion, and the parts of the field that were never really civilian*

---

## 1. The uncomfortable foundation

Fusion energy research has a defence origin that is usually elided and occasionally denied. Stating it plainly is not a criticism; it is context that explains funding patterns, publication norms and facility priorities that otherwise look arbitrary.

- **The first release of fusion energy on Earth was a hydrogen bomb** — Ivy Mike, 1 November 1952
- **The US, UK and Soviet fusion programmes were all classified** until the second Geneva conference in September 1958
- **The [[nif|National Ignition Facility]]'s primary mission is stockpile stewardship** — validating thermonuclear weapons physics without nuclear testing. Fusion energy is a secondary benefit of a weapons-physics facility, and NIF's design priorities (single-shot, high-precision, diagnostically rich, efficiency-indifferent) reflect that
- **Sandia's [[z-machine|Z Machine]]** likewise serves stockpile stewardship alongside its MagLIF fusion programme

This is why [[32-heavy-ion-fusion-and-pulsed-power|Document 32]] reaches the conclusion it does: the ICF driver best suited to a power plant (heavy ion accelerators) lost funding to the driver best suited to a weapons programme (lasers), because the weapons programme had a patron.

**Magnetic confinement is the genuinely civilian half of fusion.** Tokamaks and stellarators have essentially no weapons application — the plasma conditions, timescales and physics are wrong — which is precisely why they could be declassified in 1958 while ICF remained sensitive for decades longer.

---

## 2. Where defence money is actually going now

The modern picture is narrower than the history and is concentrated in **space power and propulsion**, not in weapons.

### The Defense Innovation Unit
**DIU has awarded contracts for two nuclear technologies — compact fusion and radioisotope heat — for spacecraft that could carry a high-power payload and freely manoeuvre in cislunar space.**

The requirement is specific and it is not about fusion energy. A spacecraft operating between Earth and lunar orbit, carrying a power-hungry payload, and needing to change orbit repeatedly, cannot do it on solar panels and chemical propellant. Fission is the incumbent answer and carries launch-approval and public-perception costs. **Compact fusion is being funded as a possible alternative to a fission reactor in space**, which is a much narrower proposition than grid power.

### AFWERX and the Air Force
**AFWERX** is the innovation arm of the Department of the Air Force, powered by the Air Force Research Laboratory, with four arms: **AFVentures, Spark, Prime and SpaceWERX**. AFVentures runs the DAF SBIR/STTR programme, including an **Open Topic** mechanism that solicits dual-use technology without a predetermined end-user.

That Open Topic structure is how a fusion startup gets defence money without being a defence contractor — and it is why several fusion companies list AFWERX among their partners.

### DARPA
Present across the fusion-adjacent portfolio, and named as a partner by **[[avalanche-energy|Avalanche Energy]]**, whose partner list is **DARPA, DIU, AFWERX and Washington State** — three defence innovation organisations and one state government.

### Why Avalanche is the archetype
Avalanche Energy's targeting is instructive. It develops **modular 100 kWe to 5 MWe compact fusion machines** based on the Orbitron scheme, and names its markets as *"electricity generation, space propulsion, marine propulsion, off-grid energy"* with an explicit pitch to **"dual-use, mobile and distributed power applications across air, land, sea, and space"** — islanded microgrids in austere or remote environments, electric vehicle recharging, and spacecraft power and propulsion.

*Austere environments* and *islanded microgrids* are defence procurement language. A 100 kWe fusion unit is not a power plant; it is a forward operating base generator that does not need a fuel convoy — and fuel convoys are, historically, where a large share of casualties in expeditionary operations occur.

**This is the honest shape of defence interest in fusion in 2026:** not weapons, but **energy logistics and space power**.

---

## 3. Maritime propulsion — dual-use by nature

Nuclear marine propulsion is mature and entirely fission-based: naval submarines and carriers, plus a small number of civilian vessels. Fusion entrants are targeting the civilian side, but the technology is inherently dual-use, and any compact fusion reactor suitable for a container ship is suitable for a naval auxiliary.

### [[maritime-fusion|Maritime Fusion]]
Founded **2024** in San Francisco **by SpaceX and Tesla engineers** (Y Combinator W25). Developing a **complete ship-based propulsion system** — [[tokamak]], shielding, cryogenic plant, magnet power supplies, tritium handling, heat conversion — on the argument that the assembly is **far smaller than the fuel tanks required for an ammonia- or hydrogen-powered vessel**. **First deployment targeted 2032.**

### FusPoB — the Fusion Power Barge
A Joint Industry Project of **[[nt-tao|nT-Tao]]** (Israel), **ABS** (ship classification society), **Siemens Energy**, **P&P Marine Consultants** and **TEMISTh**, conducting an engineering and safety study for a **containerised fusion reactor generating up to 20 MWe** in a **71.4 m barge**, driving **two 8,000 kWe steam generators**, with **battery backup giving six hours of autonomy at eight knots**. Commercial prototype around **2032**.

The presence of **ABS** matters: a classification society is the body that would have to certify such a vessel, and its participation from the design stage is the maritime analogue of early regulator engagement.

### Why shipping is a genuinely good fusion market
- Ships carry roughly **90% of world trade** and burn among the dirtiest fuels in use
- **Volumetric energy density is worth money** — every cubic metre of fuel tank is a cubic metre not carrying cargo
- The sector **already operates nuclear vessels** and has the regulatory precedent
- Fuel is bought at bunker prices, not grid prices, so the LCOE comparison is far more favourable than against wholesale electricity
- Refuelling logistics dominate operating patterns, and a reactor that runs for years changes them

**Assessment:** early, and both target 2032, which on this dossier's evidence should be read as the 2030s at best. But the market logic is stronger than for grid electricity, and it is a case where fusion's disadvantages (capital cost, complexity) matter less and its advantages (energy density, no fuel logistics) matter more.

---

## 4. The security dimensions

### Export control and the HTS question
[[22-critical-materials-supply-chains|Document 22]] established that REBCO tape production is concentrated, with substantial Chinese manufacturing strength, against roughly 10,000 km/year of global capacity.

HTS tape is a genuine dual-use technology — it enables high-field magnets for fusion, for accelerators, and for other applications — and it is the input over which the most plausible export-control friction exists. The US response so far has been to build domestic capacity (**[[arpa-e|ARPA-E]]'s $20 m to [[thea-energy|Thea Energy]]** for the first US modular HTS magnet line) rather than to restrict trade, which is the constructive direction.

### The three proliferation concerns
Covered in [[11-policy-regulation-safety|Document 11 §5]] and not repeated here, but restated for completeness: **tritium is a weapons-boosting material**; **a fusion neutron source could breed fissile material in a modified blanket, with no fissile material in the declared inventory**; and **ICF research is directly relevant to thermonuclear weapons design**. The first two require safeguards; the third is a permanent constraint on what inertial fusion research can be published openly.

> [!warning] The first concern has a specific quantity attached to it, and it is not optional
> Added 2026-10-19 from [[sindelar-2023-tritium-accountancy-control-challenges-fusion]], presented to
> the **INMM & ESARDA** joint meeting and funded by **DOE NNSA's Office of Defense Nuclear
> Nonproliferation** — the safeguards community assessing fusion on its own terms.
>
> Self-sustaining operation requires breeding **10–20% more tritium than the plant burns**. That
> surplus *"is where any diverted tritium would have to come from, otherwise, the fusion process will
> not be sustainable."*
>
> So the diversion vector is not a design flaw to be engineered out — **it is the breeding margin
> that makes fusion work at all** ([[tritium-breeding-ratio]]). A plant with no surplus cannot fuel
> its successor; a plant with a surplus has a divertible stock. The two cannot be separated.
>
> Three things make it harder than the sentence above implies. **Tritium sits outside IAEA
> safeguards** — it is not a special nuclear material to the IAEA or the [[us-nrc|NRC]], so no
> international accountancy requirement exists for it. **The measurements needed do not exist**:
> there is no method for quantifying tritium bred in a blanket or burnt in a plasma, which are
> precisely the terms a diversion calculation needs ([[tritium-accountancy]]). And the panel that
> assessed this observed that the **international inspection staff required "would be
> substantial"**.
>
> This does not overturn §5's conclusion that fusion is a large proliferation improvement over
> fission. It identifies where the residual risk actually lives, and shows it is currently
> unmeasurable rather than merely unmeasured.

### Energy security as the actual driver
The most consequential "security" dimension in 2026 is not weapons-related at all. The FIA's framing:

> *The first nations to commercialize fusion could gain profound leverage over global energy markets and an early push to develop the global supply chains and jobs that follow... the combination of technological leadership required and the energy availability fusion will provide means that the country that leads will have a leg-up in securing long-term influence and economic prosperity.*

Every national strategy documented in [[08-national-programs|Document 08]] is written in this register — Germany's "world's first fusion power plant", China's Five-Year Plan promising "extraordinary measures", Korea naming fusion one of seven strategic technologies, the DOE roadmap's "Grow" pillar. **Fusion has been reclassified from a science programme to a strategic industry**, and that reclassification is what unlocked the money.

The 2026 helium crisis ([[22-critical-materials-supply-chains|Document 22]]) — where strikes on Qatari infrastructure and the closure of a shipping strait removed roughly a third of global helium supply — is a live demonstration that energy-technology supply chains are now a security question in the ordinary sense.

---

## 5. The tension nobody has resolved

Fusion's openness has been one of its structural advantages since 1958. The 1969 Culham expedition to Moscow, the [[iter|ITER]] agreement surviving the post-2022 rupture, the IAEA's coordinating role, the open publication of [[sparc|SPARC]]'s physics basis — these are not incidental. **Fusion progressed faster because it was open.**

The 2026 picture is more mixed:

- Chinese companies **declining to report** to the FIA's industry survey
- National strategies framed around **leadership rather than collaboration**
- HTS tape becoming an **export-control question**
- **ICF's permanent weapons-physics sensitivity** limiting what can be published
- Defence agencies as **early customers**, with the confidentiality that implies

None of this is dramatic and none of it is unreasonable. But the direction of travel is away from the openness that made the field work, and the field has not had the conversation about what it is trading away.

The counterexample remains ITER: 35 nations, including Russia, still cooperating on the largest scientific project in history, with Russia manufacturing 25 distinct systems for it throughout a period of otherwise total scientific rupture. That is worth more than its schedule slippage costs, and it is the strongest available argument that fusion's collaborative model is not naive.

---

## 6. Assessment

**Defence funding in fusion is real, modest, and narrowly targeted** — space power and propulsion for cislunar operations, and compact modular units for austere-environment energy logistics. It is not weapons work. DIU, AFWERX and DARPA are acting as early-stage customers for a capability that has no civilian buyer yet, which is the classic role of defence procurement in technology development.

**[[inertial-confinement|Inertial confinement]] fusion is genuinely dual-use and always has been.** NIF's ignition was a stockpile stewardship result that happened to be a fusion energy result. That relationship funds the facility and constrains its publication, and both effects are permanent.

**Maritime is the most credible near-term dual-use market**, and the presence of a classification society in the FusPoB consortium suggests at least one group is taking certification seriously from the outset.

**The real security story is energy security, not weapons.** Fusion has been reclassified as strategic industrial policy in every major economy simultaneously, and that is what changed the funding. The associated cost — a slow drift away from the openness that has served the field since 1958 — is being paid without much discussion.

---

**Continue to:** [[38-component-manufacturing|38 — Component Manufacturing]] · [[39-the-discourse|39 — The Discourse]] · [[11-policy-regulation-safety|11 — Policy, Regulation and Safety]]
