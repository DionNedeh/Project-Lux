---
title: "Investigating the application of Kalman Filters for real-time accountancy in fusion fuel cycles"
type: source
source_type: paper
file: "raw/papers/Flynn-Larsen-2022-Kalman-filters-tritium-accountancy.pdf"
authors: "H. B. Flynn, George Larsen (Savannah River National Laboratory, Aiken, South Carolina)"
publisher: "Fusion Engineering and Design 176 (2022) 113037, DOI 10.1016/j.fusengdes.2022.113037; DOE accepted manuscript, OSTI 1856104, report SRNL-STI-2021-00621"
source_date: 2022-01-28
ingested: 2026-11-02
tags:
  - fusion/source
  - fusion/subsystems
  - fusion/computation
status: stable
confidence: high
related:
  - "[[tritium-accountancy]]"
  - "[[sindelar-2023-tritium-accountancy-control-challenges-fusion]]"
  - "[[srnl-2013-tritium-accountancy-in-fusion-systems]]"
  - "[[thalia-hera-ukaea-tritium-accountancy-2026]]"
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
  - "[[tritium-retention]]"
  - "[[tritium-start-up-inventory]]"
  - "[[us-doe]]"
  - "[[11-policy-regulation-safety]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
  - "[[19-simulation-codes-nuclear-data]]"
created: 2026-11-02
updated: 2026-11-02
---
The source that addresses the **continuous-flow problem** in
[[tritium-accountancy|tritium accountancy]] directly: conventional accountancy assumes static
batches in controlled conditions, and a fusion plant will run continuously.

> [!note] Accepted manuscript, not the version of record
> The capture is the **DOE accepted manuscript** released through OSTI PAGES, not Elsevier's
> published version. Content was not compared against the version of record. Authored under
> contract 89303321CEM000080 for the DOE Office of Environmental Management; the paper's
> acknowledgements also credit support from the Office of Fusion Energy Sciences.

## Method

A simple fuel-cycle concept is defined and each component's tritium inventory evolved in time
by Euler approximation of a series of differential equations in Python. Sensor measurements are
then *simulated* at specific points and passed through a **Kalman Filter** — a state-prediction
algorithm standard in radar, robotics and hydrology, which the authors state had **not**
previously been applied to tritium inventory accountancy.

## The result

| Stage | Percent error against the model's true value |
|---|---|
| Simulated raw sensor | **64.37%** |
| Kalman Filter, end of day 1 | **≈ 0.633%** |
| Kalman Filter, end of day 3 | **≈ 0.001%** |

The authors measure this against *"the accountancy standard of 1%"* — the filter crosses that
threshold within a day of simulated operation. A tenfold increase in sampling frequency tightens
the estimate further and reaches its optimum earlier.

## The limitation the authors state themselves

> [!warning] The filter fails on accumulating bias
> Given a measurement system with a bias accumulating over the three-day period, the Kalman
> Filter *"accurately predicts the mean of the sensor measurement but has an increasingly large
> spread from the true value"* — which is useless, because the true value is what accountancy
> needs. A **Bias-Aware Kalman Filter** is named as ongoing work, deferred to a follow-on paper.

This matters because the paper also names the conditions a real fuel-cycle sensor will face —
high vibration, ground-loop issues, radiofrequency-generating components — all of which
accumulate exactly the biases the implemented filter cannot handle.

## What it does **not** establish

- **No real sensor data.** Every measurement is simulated from the model it is then validated
  against, so the 0.001% figure measures self-consistency, not instrument performance.
- **A simple fuel cycle.** The authors note designs have grown more complex since Abdou's 1985
  paper, and that understanding plasma-vessel contributions and losses is required before this
  is usable commercially — the same unmeasurable terms recorded in [[tritium-accountancy]].
- **Not the 1% standard's provenance.** The paper cites the figure without deriving it.
- **Nishi *et al.* 2006 is this paper's reference [1]** — "Study on tritium accountancy in fusion
  DEMO plant at JAERI", *Fusion Engineering and Design* 81(1-7) 745–751. That citation is now
  confirmed from a held source, but the paper itself remains **not held**, so the instrument
  accuracies on [[tritium-accountancy]] still reach this vault at second hand.
