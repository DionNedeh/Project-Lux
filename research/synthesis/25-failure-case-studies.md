---
title: "Failure Case Studies"
type: synthesis
doc: 25
part: 2
aliases:
  - "Failure Case Studies"
tags:
  - fusion/synthesis
  - fusion/risks
  - fusion/history
created: 2026-08-25
updated: 2026-09-02
status: stable
confidence: high
related:
  - "[[02-history-1920-2026]]"
  - "[[07-private-fusion-industry]]"
  - "[[14-open-problems-and-risks]]"
  - "[[21-the-graveyard]]"
  - "[[26-appendix-quantitative-data]]"
  - "[[tcv-predict-first-rampdown-2025]]"

---
# 25 — Failure Case Studies

*Project Lux · What has actually gone wrong, why, and what each failure cost*

---

## Why case studies rather than a risk list

[[14-open-problems-and-risks|Document 14]] lists risks in the abstract. This document examines what has **actually** failed on real fusion projects, with root causes where they are published.

The value is in the pattern. Fusion's high-profile failures have very rarely been failures of plasma physics. They have been **welds, chlorides, mirrors, capsule defects, and budget votes** — which is exactly what the field's own risk ranking now says ([[07-private-fusion-industry|Document 07 §5]]): materials and integration, not plasma science.

---

## Case 1 — [[iter|ITER]]'s vacuum vessel sectors: welding distortion

**When:** discovered 2022 · **Consequence:** a principal driver of the 2024 rebaseline

### What happened

ITER's vacuum vessel is built as nine 40-degree sectors, each fabricated from four individual segments welded together. Each finished sector weighs about 440 tonnes.

**Welding the four segments together caused dimensional deviations larger than the specified limits, in multiple locations, on the outer shell surfaces.** The distortion altered the geometry at the **field joints** — the surfaces where one sector is welded to the next inside the assembly pit.

### Why that mattered so much

The field joints are not welded by hand. They are welded by **automated tools that must fit into a defined geometry and traverse a defined path.** A sector whose joint surfaces are out of tolerance is a sector those tools cannot access or operate on correctly.

So a manufacturing deviation of millimetres, on a component already delivered and already installed in the pit, invalidated the assembly method for the entire machine.

### The repair

Components had to be **removed and disassembled from the assembly pit**, with options ranging from on-site repair to re-manufacture in external facilities. The Director-General's public assessment of the schedule and cost consequences was that they would be **"not insignificant."**

### The lesson

**Tolerance stack-up on very large, first-of-a-kind welded structures is a first-order project risk.** Nothing here is exotic physics — it is the interaction between a distributed in-kind manufacturing model, welding distortion in thick sections, and an assembly sequence with essentially no float. It is precisely the class of problem that every fusion company planning a large vacuum vessel will meet.

---

## Case 2 — ITER's thermal shield: chloride stress corrosion cracking

**When:** leaks detected November 2021 · **Consequence:** 23 km of pipe replaced

### What happened

In November 2021, **helium leak testing detected leaks in a vacuum vessel thermal shield element that had been delivered eighteen months earlier.** Unexpected leaks were found in **three panels out of nearly five hundred**.

### Root cause

Published plainly by ITER:

> Stress caused by the **bending and welding of the cooling fluid pipes** to the thermal shield panels, compounded by a slow chemical reaction due to the presence of **chlorine residues** in small areas near the pipe welds.

The combination produced **stress corrosion cracking**, and over roughly eighteen months of storage, **cracks up to 2.2 millimetres deep** developed in the pipes.

### The response

Because the mechanism was time-dependent and the contamination could not be reliably located or excluded panel-by-panel, the decision was taken to **remove and replace all 23 kilometres of cooling pipes** across the panels — and to eliminate the mechanism by design:

- A **more corrosion-resistant grade of stainless steel** for the pipes
- **Abandoning the silver-plating process** used in the welded construction, which was the likely source of the residual chlorides
- Concurrent new manufacture of two 40-degree thermal shield sectors to protect the assembly schedule

### The lesson

This is the most instructive failure in modern fusion, and it has nothing to do with fusion.

**Three panels in five hundred had a manufacturing contaminant. The cracks grew slowly, in storage, with nothing operating.** The defect was invisible until a leak test eighteen months after delivery. And the only defensible response was to replace *everything*, because you cannot prove a negative about contamination you cannot locate.

For a fusion plant, the generalisation is uncomfortable: **components will be manufactured years before use, stored, and installed in places no human will ever re-enter.** A slow-acting manufacturing defect that surfaces after activation cannot be fixed the way this one was.

---

## Case 3 — The National [[ignition|Ignition]] Campaign: 3D reality

**When:** 2010–September 2012 · **Consequence:** ignition delayed ten years

### What happened

NIF was completed in 2009 and the National Ignition Campaign ran to a Congressionally-noted deadline of September 2012. **It ended without ignition.** Yields were roughly an **order of magnitude below** integrated design predictions.

### Root cause

The one-dimensional physics of ICF, as published by Nuckolls and colleagues in *Nature* in 1972, was essentially correct. The problem was that **ICF is not one-dimensional**.

At a convergence ratio of 25–40, any asymmetry is amplified enormously by **Rayleigh-Taylor instability** at both the ablation front and the deceleration interface. The seeds were mundane:

- **The capsule fill tube** — a few-micron hole in a perfect sphere, injecting a jet of ablator material into the hot spot
- **Surface roughness and voids** in the ablator, growing by factors of hundreds
- **Hohlraum drive asymmetry** and laser power imbalance
- **Laser-plasma instabilities** scattering light and pre-heating the fuel with hot electrons

A cold, high-Z spike penetrating the hot spot radiates its energy away and quenches the burn.

### The fix, and how long it took

Ten years of: thicker and more robust capsules, the HYBRID-E hohlraum redesign, far better capsule metrology and selection, and the switch from plastic to **high-density carbon (diamond)** ablators.

**Ignition came on 5 December 2022** — 3.15 MJ from 2.05 MJ. And the enabling factor for the April 2025 record of 8.6 MJ was reported as **a higher-quality custom diamond capsule, not any change to the laser.**

### The lesson

**Fusion's limiting variable is often manufacturing precision, not physics.** Ten years and a great deal of money were spent learning that the target, not the driver, was the constraint — and that remains the constraint today, which is why the August 2026 Inertia/LLNL result on cryogenic fuel layering matters so much for inertial fusion energy.

---

## Case 4 — [[wendelstein-7-x|Wendelstein 7-X]]: coils, leaks and a decade of construction

**When:** construction 1996–2014 · **Consequence:** roughly a decade of delay

### What happened

W7-X's 50 non-planar superconducting coils are shaped to about 1 mm tolerance and were, when built, among the most geometrically complex engineered objects in existence. Construction ran far longer than planned. Published accounts of the technical challenges include:

- Difficulty **fabricating the cable-in-conduit conductor**
- **Accuracy of the coil cases after welding and machining** — the same class of problem ITER met on its vessel sectors
- Development of **electrical joints**
- **Leaks in the cooling system caused by stress corrosion cracking** — the same failure mechanism as ITER's thermal shield
- High-voltage testing revealing that **insulation had to be reinforced and [[quench]] detection wires exchanged**
- Coils failing acceptance testing and requiring rework

### The outcome

First plasma on 10 December 2015. And in 2025, **W7-X set the world triple-product record for pulses over 10 seconds**, sustained across a 43-second discharge, beating [[jet|JET]]'s long-pulse record with a plasma three times smaller and five times less heating power.

### The lesson

Two, in tension.

**First:** [[stellarator]] construction is genuinely, structurally hard, and the private stellarator sector's central bet is that optimisation can make coils buildable at cost. [[thea-energy|Thea Energy]]'s planar-coil approach and quasi-single-stage optimisation are direct responses to exactly the problems in the list above. [[canis]] now supplies component-level evidence: nine planar coils were manufactured and controlled as an array within 1% of predicted static field. Because it was flat and produced no plasma or closed surfaces, it does not yet answer the integrated-machine failure modes ([[prototyping-test-canis-hts-planar-coil-array]]).

**Second, and more important:** **W7-X worked.** The machine that took a decade too long to build is now the best-performing stellarator in history and holds a record no [[tokamak]] has matched at that pulse length. A painful construction is not a failed programme.

---

## Case 5 — [[mftf-b|MFTF-B]]: cancelled the year it was completed

**When:** completed 1986, cancelled 1987 · **Consequence:** $372 million, zero plasmas

Covered in [[21-the-graveyard|Document 21]], but it belongs on this list because it is the only case where the failure was **entirely political**.

- **$372 million** — the most expensive project in Lawrence Livermore's history at the time
- **Construction completed in 1986**; operational budget cancelled the same year
- **Formally cancelled 1987 and disassembled without ever operating**

The physics was never tested. US mirror research effectively ended for thirty years — until **[[wham|WHAM]] achieved 17 tesla on a confined plasma in July 2024** and Realta began commercialising it.

**The lesson:** a fusion programme's schedule risk includes the political cycle. A machine that takes twelve years to build must survive three or four changes of government, and the ones that do are usually the ones with an international treaty behind them — which is, in its unglamorous way, an argument for ITER's existence.

---

## Case 6 — [[zeta|ZETA]], 1958: measuring the wrong thing

**When:** announced 24 January 1958, retracted May 1958

Covered in [[02-history-1920-2026|Document 02]]. The technical point deserves restating here because the error recurs.

ZETA produced neutrons. The team announced them as thermonuclear. Within four months it was established that they were **beam-target neutrons**, produced by plasma instabilities accelerating a small population of ions into the background gas — not by a thermal plasma at fusion temperature.

**Why it keeps happening:** neutron count is easy to measure and temperature is hard. A non-thermal ion population produces neutrons at a rate that looks impressive and scales in a way that goes nowhere. This is precisely why the **[[triple-product|triple product]]**, which requires an independent confinement time measurement, is the metric that matters — and why any modern announcement of a temperature or a neutron yield without a confinement time should be read carefully.

The one genuinely good consequence: the "ZETA fiasco" made it obvious that fusion claims could not be verified in secrecy, and it led directly to comprehensive declassification at the second Geneva conference in September 1958.

---

## Case 7 — [[first-light-fusion|First Light Fusion]]: a company concluding its own approach would not work

**When:** pivot announced 2025 · **Consequence:** $156 m redirected

First Light spent years on projectile-driven inertial fusion with a shock "amplifier" target. It produced real results, including validated fusion neutrons.

In 2025 it **stopped claiming it would build a power plant** and refocused on **licensing its amplifier technology**. It has since raised further money — a £25 m first close led by East X Ventures — but as a technology company, not a fusion developer.

**The lesson:** this is the healthy version of failure. A competent team assessed its own approach against a credible timeline and redirected rather than continuing to raise against a thesis it no longer believed. The FIA notes three companies dropped out of the 2026 survey; more will follow, and how they exit matters for the sector's credibility.

---

## The pattern

Sorting the seven cases by root cause:

| Case | Root cause category |
|---|---|
| ITER vacuum vessel | **Manufacturing tolerance** |
| ITER thermal shield | **Manufacturing contamination** |
| National Ignition Campaign | **Manufacturing precision** (targets) |
| Wendelstein 7-X | **Manufacturing complexity** + the same corrosion mechanism |
| MFTF-B | **Political** |
| ZETA | **Measurement / diagnosis** |
| First Light Fusion | **Strategic reassessment** |

**Not one of these was a failure of plasma physics.** Four were manufacturing. One was politics. One was diagnostics. One was a business decision.

Three specific mechanisms recur and are worth internalising:

1. **Welding distortion in large thick-section structures** — ITER's vessel and W7-X's coil cases
2. **Stress corrosion cracking from residual contamination** — ITER's thermal shield and W7-X's cooling system, independently, on two different continents
3. **Micron-scale imperfections amplified by convergence** — every ICF programme

And one meta-lesson that the field has largely learned: **the failures were all eventually diagnosed and fixed.** ZETA's neutrons were explained. NIF's capsules were improved and ignited. ITER's pipes were replaced. W7-X now holds a world record. The projects that died — MFTF-B — died of funding, not of physics.

That is a genuinely encouraging record for a technology whose critics usually argue it is impossible. It is also a cautionary one for anyone projecting first-of-a-kind schedules, because **every one of those diagnoses and fixes took years.**

---

**Continue to:** [[26-appendix-quantitative-data|26 — Appendix: Quantitative Progress Data]] · [[14-open-problems-and-risks|14 — Open Problems and Risks]] · [[21-the-graveyard|21 — The Graveyard]]
