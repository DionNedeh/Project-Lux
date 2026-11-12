---
title: "Standards, Codes and Liability"
type: synthesis
doc: 23
part: 2
aliases:
  - "Standards, Codes and Liability"
tags:
  - fusion/synthesis
  - fusion/policy
  - fusion/standards
created: 2026-08-25
updated: 2026-08-29
status: stable
confidence: high
related:
  - "[[09-engineering-challenges]]"
  - "[[10-economics-and-markets]]"
  - "[[11-policy-regulation-safety]]"
  - "[[24-grid-integration-and-operations]]"
  - "[[27-people-institutions-public-trust]]"
  - "[[china-fusion-device-radiation-safety-2025]]"
  - "[[uk-fusion-strategy-2026]]"

---
# 23 — Standards, Codes and Liability

*Project Lux · The engineering rulebook that does not yet exist, and who pays when something goes wrong*

---

## 1. Why codes and standards decide schedules

[[11-policy-regulation-safety|Document 11]] covered *regulation* — whether a government permits you to operate. This document covers something different and, for a project engineer, more immediately binding: **the codes and standards that determine whether a component can legally be built, welded, inspected and accepted.**

The distinction matters because a licence tells you what safety outcome you must achieve, while a code tells you **how to demonstrate that a pressure vessel is fit for service**. Without an applicable code, a manufacturer cannot certify a part, an insurer cannot underwrite it, and a regulator has no basis to accept it. Projects do not usually fail because of physics; they fail because a weld cannot be qualified.

Fusion's problem is that **the two available codes were written for other machines.**

---

## 2. The two candidate codes

Internationally, two standards govern the mechanical components of a fusion reactor:

### ASME Boiler & Pressure Vessel Code (BPVC)
The American standard, and the global default for pressure-retaining equipment. Section III covers nuclear components; Division 5 covers high-temperature reactors.

**Strengths:** enormous depth, universal recognition, a mature qualification and stamping infrastructure, and a supply chain of certified manufacturers.

**Weaknesses for fusion:** it was written for light water reactors and extended toward high-temperature fission. It has limited treatment of **irradiation effects on candidate fusion materials**, limited coverage of the specific fusion alloys (RAFM steels, vanadium alloys, tungsten), and limited support for the **advanced manufacturing techniques** — additive manufacturing, hot isostatic pressing, complex internal cooling channels — that fusion components require.

### AFCEN RCC-MRx
The French code, from the *Association Française pour les règles de Conception, de construction et de surveillance en exploitation des matériels des Chaudières Électro-Nucléaires*.

RCC-MRx is explicitly written **for components operating at high temperature, for components operating under significant irradiation, and for specific components dedicated to fusion reactors.**

That third clause is the point. RCC-MRx offers material advantages over ASME BPVC for fusion-specific components — the **breeding blanket** above all — through:
- More comprehensive treatment of **high-temperature behaviour** (creep, creep-fatigue interaction, relaxation)
- Explicit treatment of **irradiation effects on candidate materials**
- Support for **advanced manufacturing techniques**

It is the code [[iter|ITER]] has largely worked to, and it is where fusion-specific design rules have progressed furthest.

### The practical position
Most fusion projects end up using RCC-MRx where it fits, ASME where the supply chain demands it, and bespoke justification for everything else. That "everything else" is large, and it is where schedule risk lives.

---

## 3. What is actually missing

The gaps are specific and well-catalogued in the literature (*The Need for Codes and Standards in Nuclear Fusion Energy*, J. Fusion Energy, 2023; the FESAC white paper on fusion construction codes; and the **IAEA Technical Meeting on Experience in Codes and Standards for Fusion Technology**, November 2025):

**1. No qualified fusion structural materials.** RAFM steels — EUROFER-97, F82H — are not code-qualified for nuclear service anywhere. Vanadium alloys and SiC/SiC composites are further behind. Qualification requires irradiated mechanical property datasets that, as [[09-engineering-challenges|Document 09]] explains, **cannot currently be generated because no fusion-spectrum neutron source exists.**

**2. Small-specimen test methods are not codified.** Irradiation volume in any test reactor is tiny and expensive, so fusion materials data comes from **miniaturised specimens**. Codes were written around full-size specimens. Establishing that a sub-size test predicts full-size behaviour — especially for fracture toughness and ductile-to-brittle transition — is itself a standards problem. DOE's long-term milestone is explicit: *"Codify fusion-specific functional requirements into ASME-based standards using validated small-specimen methods."*

**3. No rules for the components fusion actually has.** A breeding blanket is not a pressure vessel, a heat exchanger or a fuel assembly. It is a neutron-multiplying, tritium-generating, magnetohydrodynamically-loaded, remotely-replaceable structure with internal coolant channels. There is no code section for it.

**4. Joining and cutting of irradiated materials.** A remotely-replaced in-vessel component must be cut out and a new one welded in, **in situ, remotely, on material that has been irradiated**. Irradiated material welds differently — helium in the lattice causes weld cracking. DOE's mid-term milestone is to *"qualify joining and cutting methods for irradiated materials to enable modular in-vessel replacement."* No code covers this today.

**5. Superconducting magnet standards.** There is no equivalent of the BPVC for a gigajoule-class superconducting magnet. DOE's Challenge Area C milestone — *"conduct REBCO irradiation campaigns to define magnet performance and standards"* — is a statement that these standards must be created from scratch.

---

## 4. Why this is on the critical path

The sequence is unforgiving:

```
Irradiation facility → irradiated property data → small-specimen validation
   → code case → qualified material → certified component → licensed plant
```

Each arrow takes years. The first box does not exist: **[[ifmif-dones|IFMIF-DONES]] is under construction and FPNS is a mid-term (3–5 year) DOE roadmap item.**

The DOE roadmap places codification in its **long-term (5–10 year)** bucket — i.e. **2031–2036**. Multiple companies plan pilot plants for the **early-to-mid 2030s**.

**Those two timelines overlap, which means first-generation pilot plants will be built before the codes governing their components exist.** In practice this is handled through case-by-case regulatory justification, extensive analysis in place of qualification, and conservative design margins — all of which cost money and, more importantly, cannot be repeated cheaply for a second plant. The learning curve that fusion economics depends on ([[10-economics-and-markets|Document 10]]) requires standardisation, and standardisation requires standards.

---

## 5. Liability and insurance

### The fission framework

The **Price-Anderson Act** became law on **2 September 1957** to cover public liability claims for personal injury and property damage from a commercial nuclear power plant accident. It works in layers: owners of nuclear plants currently carry **$500 million in private insurance for offsite liability per reactor site** (per *site*, not per reactor), backed by a retrospective industry-wide pool, with the federal government above that.

Internationally, the equivalent instruments are the **Paris Convention**, the **Vienna Convention** and the **Convention on Supplementary Compensation for Nuclear Damage**.

### Does any of it apply to fusion?

**Probably not, and that is mostly good.** Price-Anderson is tied to licences issued under the Atomic Energy Act for utilisation and production facilities involving special nuclear material. A fusion machine regulated as a **byproduct material facility under 10 CFR Part 30** — the framework the NRC proposed on 26 February 2026 — falls outside that structure.

The consequences cut both ways:

**Favourable:** no mandatory nuclear liability insurance premium, no retrospective pool contribution, and no channelling of liability that discourages suppliers. Fusion developers can insure in the conventional commercial market, which is far cheaper.

**Unfavourable, and underappreciated:** **channelling of liability** in the nuclear conventions exists to protect *suppliers*. Under Price-Anderson, a company that sells a valve to a nuclear plant is not exposed to accident liability — the operator is. Without that channelling, a supplier of, say, a tritium pump to a fusion plant carries ordinary product liability for whatever that pump does.

For a nascent industry trying to attract conventional industrial suppliers who have no nuclear experience and no appetite for radiological liability, **this is a real barrier to supply chain formation**, and it is one of the least-discussed consequences of the byproduct-material decision.

### The insurance market

Fusion's insurable risks are, in practice, industrial rather than nuclear:
- Tritium release — the dominant radiological exposure
- Magnet [[quench]] and the destruction of a gigajoule-class magnet system
- Cryogenic and vacuum failures
- Beryllium and lithium chemical hazards
- Conventional construction and business-interruption risk on a first-of-a-kind plant

The last item is likely the largest. **Business interruption on a $2.5 billion first-of-a-kind plant with an unproven availability profile** is an underwriting problem with no actuarial base, and it will be priced accordingly — feeding straight into the cost of capital that [[10-economics-and-markets|Document 10]] identifies as a dominant LCOE term.

---

## 6. The international coordination problem

Codes and standards are national or regional; fusion's supply chain is global. A blanket module designed in Europe to RCC-MRx, manufactured in Japan, installed in the United States and licensed by a US Agreement State crosses three regulatory philosophies.

The **IAEA** has taken the convening role — its **Technical Meeting on Experience in Codes and Standards for Fusion Technology** (18–21 November 2025) is the field's main forum — but it has no authority to impose harmonisation.

The risk is genuine: **divergent national standards would fragment a supply chain that is already too small.** If a European gyrotron cannot be accepted into a US plant without requalification, the cost of every component rises and the learning curve flattens. Conversely, early harmonisation is one of the cheapest possible interventions, and it is available now, before the plants exist.

This is, quietly, one of the highest-leverage and lowest-cost policy actions available to the field — and it is receiving a fraction of the attention given to licensing frameworks.

---

## 7. Assessment

**Regulation has moved much faster than codification.** The US has a proposed fusion rule with a final rule targeted for October 2026; the UK has statutorily excluded fusion from nuclear site licensing; Germany and France are adapting. But **no jurisdiction has a complete set of design and construction codes for fusion components**, and the materials data that would underpin them cannot yet be generated.

**The practical consequence** is that first-generation plants will be built on bespoke justification rather than codified rules — expensive, slow, non-repeatable, and impossible to scale. The second generation is where standardisation pays off, and whether it exists by then depends on decisions being made now about irradiation facilities and small-specimen methodology.

**The liability picture is favourable but incomplete.** Escaping Price-Anderson lowers the operator's cost and also removes the supplier protection that made the fission supply chain possible. Nobody has yet worked out what replaces it.

**The most useful thing a government could do for fusion in 2026** is not another funding announcement. It is to fund the irradiation facilities that generate qualification data, and to push the IAEA process toward harmonised international fusion codes before national divergence sets. Both are cheap. Neither is glamorous. Both are on the critical path.


## Waste classification is not standardised across borders

[[43-fusion-waste-classification-and-disposal]] records a liability this document does not currently capture: waste classification is
**jurisdictional**. An alpha limit of 4 MBq/kg applies in France's LILW-SL class, and ⁹⁴Nb activity
may exceed France's nuclide-specific limit while satisfying UK repository criteria. The same
physical component can be two different waste classes in two countries, so a vendor selling a
standardised plant across borders exports a **non-standardised waste liability** that lands on the
operator.

---

**Continue to:** [[24-grid-integration-and-operations|24 — Grid Integration and Plant Operations]] · [[27-people-institutions-public-trust|27 — People, Institutions and Public Trust]] · [[11-policy-regulation-safety|11 — Policy, Regulation and Safety]]
