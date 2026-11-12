---
title: "Q — the Four Gain Definitions"
type: concept
domain: physics
symbol: "Q"
tags:
  - fusion/concept
  - fusion/physics
  - fusion/data
status: stable
confidence: high
sources:
  - "[[willis-2026-st-e1-pre-concept-design-overview]]"
related:
  - "[[ignition]]"
  - "[[recirculating-power]]"
  - "[[nif]]"
  - "[[jet]]"
  - "[[st-e1]]"
  - "[[tritium-burn-fraction]]"
  - "[[26-appendix-quantitative-data]]"
  - "[[39-the-discourse]]"
created: 2026-08-26
updated: 2026-10-19
---
Where most public confusion about fusion lives. **Never write "Q" unqualified.**

| Symbol | Definition | Measures |
|---|---|---|
| **Q_sci** | P_fusion / P_heating-into-plasma | The plasma alone. Ignores everything else |
| **Q_target** | Fusion yield / laser energy on target | [[nif]]'s headline number |
| **Q_wp** | Fusion energy / total grid electricity drawn | The honest engineering figure |
| **Q_eng** | Net electricity exported / consumed | Whether the plant is a generator or a load |

## The gap in practice

NIF's 7 April 2025 shot: **Q_target = 4.13** (8.6 MJ from 2.08 MJ on target). The laser draws roughly **300–400 MJ from the grid**, so **Q_wp ≈ 0.02**. Both figures are correct; only one was widely reported.

[[jet]]'s famous 1997 **0.67** is a *transient peak*. The harmonised value for the same shot is **0.27**. See [[26-appendix-quantitative-data]].

## Landmarks

- **Q = 1** — scientific breakeven
- **Q = 5** — alpha self-heating equals external heating
- **Q ≈ 10** — [[iter]]'s target; a genuine [[burning-plasma]]
- **Q = ∞** — [[ignition]]
- **Q_eng > 1** — typically needs Q_sci of **10–30+**, because of [[recirculating-power]]

## The error is not only journalistic

Added 2026-10-19. Peer-reviewed design papers do it too, which is why this page's rule applies to
primary sources and not just to press coverage.

**[[st-e1|ST-E1]]** is the clearest recent case: the reference design point in
[[willis-2026-st-e1-pre-concept-design-overview|Willis *et al.* 2026]] tabulates **"Q (–)" with no
subscript** — 20 for the pilot phase, 50–70 for the commercial phase — and the surrounding prose says
only *"fusion gain"*. Arithmetic on the paper's own rows resolves it: 1500 MW fusion over 75 MW
auxiliary is exactly 20, so the quantity is **Q_sci**. That subscript is a vault derivation; the
source never supplies it.

Why it matters here rather than being pedantry: a reader who took ST-E1's "Q = 20" for **Q_eng** or
**Q_wp** would conclude the plant exports twenty times its consumption. The same paper's own figures
show the pilot phase producing 300–500 MWe net from 1500 MW fusion — a different ratio entirely, and
the one that decides whether the plant is a generator or a load.

A related case, in a different quantity: the ST-E1 fuel-cycle modelling tabulates a "tritium burn
efficiency" of 0.02 and defines it nowhere, leaving it undecidable whether it means a burn fraction
or a burn-fraction-times-fuelling-efficiency product. See [[tritium-burn-fraction]]. **The failure
mode generalises beyond Q: a bare symbol in a table is a defect wherever a field uses one symbol for
several quantities.**
