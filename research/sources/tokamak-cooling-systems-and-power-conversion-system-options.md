---
title: "Tokamak Cooling Systems and Power Conversion System Options"
type: source
source_type: paper
file: "raw/papers/Tokamak-cooling-systems-and-power-conversion-system-options.pdf"
authors: "Moscato, Barucca, Bubelis et al. (20 authors)"
publisher: "Fusion Engineering and Design 178, article 113093"
source_date: 2022-05-01
ingested: 2026-09-12
tags:
  - fusion/source
  - fusion/engineering
  - fusion/operations
status: stable
confidence: high
related:
  - "[[primary-heat-transfer-system]]"
  - "[[balance-of-plant]]"
  - "[[eu-demo]]"
  - "[[maturation-of-critical-technologies-demo-balance-of-plant]]"
  - "[[thermal-storage-pulsed-operation]]"
  - "[[iter]]"
  - "[[24-grid-integration-and-operations]]"
  - "[[09-engineering-challenges]]"
created: 2026-09-12
updated: 2026-09-12
---
The companion study to [[maturation-of-critical-technologies-demo-balance-of-plant]], covering [[eu-demo|EU-DEMO]]'s tokamak cooling systems and power conversion options as addressed under Key Design Integration Issue 5 of the **Pre-Concept Design** phase. Twenty authors, EUROfusion and partner institutes.

**Access:** the **author postprint** from the IRIS Sapienza repository. The article is CC BY 4.0 in *Fusion Engineering and Design* 178, but the publisher version of record was unreachable and **was not compared against this copy**.

## The duty cycle, in numbers

The vault has long described fusion's pulsed-operation problem qualitatively. This source dates and quantifies it for DEMO:

| Phase | Duration | Power |
|---|---|---|
| Pulse (burn) | **2 hours** | nominal |
| Ramp-up / ramp-down | **100–200 s** each | transitional |
| Dwell | **~10 minutes** | **1–2% of nominal**, from residual heat in tokamak structures |

That residual 1–2% is the whole difficulty: it is not zero, so the plant never fully rests, and it is nowhere near enough to hold a turbine. See [[thermal-storage-pulsed-operation]].

## The comparison that frames the problem

> ITER dumps its heat to the environment **without any energy conversion at all**.

DEMO is therefore the first tokamak that must solve balance of plant as a nuclear-licensable system rather than a heat-rejection exercise — and the paper is explicit that an analogy with a fission plant "is not so trivial", because the primary heat source is intermittent.

## PHTS architecture

Heat is collected by several [[primary-heat-transfer-system|primary heat transfer systems]] and handed to the power conversion system through heat exchangers. HCPB and WCLL differ in **blanket** PHTS layout, while **divertor and vacuum-vessel PHTS use essentially the same arrangement for both** blanket concepts. Reported conditions include the HCPB blanket PHTS running pressurised helium at about **8 MPa, 300/520 °C**, and a vacuum-vessel PHTS at roughly **1 MPa, 190/200 °C**.

The divertor PHTS carries a safety function beyond heat removal: its ex-vessel portions provide **primary confinement** for coolant bearing tritium and activated particles.

## What it does not establish

Pre-concept design only — no built system, no operating data. The paper's encouraging findings, that the architectures can restore nominal conditions after transients and that balance-of-plant availability could meet DEMO's top-level requirements, are explicitly **preliminary assessments**, and it names criticalities still requiring design improvement. No net cycle efficiency figure is given.
