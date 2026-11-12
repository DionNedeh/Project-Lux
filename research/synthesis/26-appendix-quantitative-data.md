---
title: "Appendix: Quantitative Progress Data"
type: synthesis
doc: 26
part: 2
aliases:
  - "Appendix: Quantitative Progress Data"
tags:
  - fusion/synthesis
  - fusion/data
  - fusion/reference
created: 2026-08-25
updated: 2026-08-26
status: stable
confidence: high
related:
  - "[[01-fusion-physics-fundamentals]]"
  - "[[05-inertial-confinement-fusion]]"
  - "[[12-state-of-play-2026]]"
  - "[[21-the-graveyard]]"
  - "[[27-people-institutions-public-trust]]"
---
# 26 — Appendix: Quantitative Progress Data

*Project Lux · The actual numbers, machine by machine, from the primary dataset*

---

## Source and method

All data in this appendix is extracted from **Wurzel, S. E. & Hsu, S. C., *Continuing progress toward fusion energy breakeven and gain as measured against the [[lawson-criterion|Lawson criteria]]*, arXiv:2505.03834v6 (7 November 2025)** — held locally at `papers/Wurzel-Hsu-2025-Lawson-criterion-progress-update.pdf`. It updates their *Physics of Plasmas* 29, 062103 (2022) paper.

This is the field's canonical harmonised dataset. Its value is that it **applies consistent definitions across machines and decades**, correcting for the fact that different laboratories have historically defined confinement time, peak versus volume-averaged quantities, and gain in incompatible ways. Values inferred rather than directly measured are footnoted in the original.

The key quantity throughout is the **[[triple-product|triple product]]**:

```
n_i0 · T_i0 · τ_E     [keV · m⁻³ · s]
```

using **peak** ion density and ion temperature and the energy confinement time. [[ignition|Ignition]] for D-T requires roughly **3 × 10²¹** on this measure under idealised assumptions; real profiles and impurities push the requirement several times higher.

---

## Table A — Tokamaks and spherical tokamaks

| Machine | Year | Shot | T_i0 (keV) | n_i0 (m⁻³) | τ_E (s) | **Triple product** (keV m⁻³ s) |
|---|---|---|---|---|---|---|
| [[t-3|T-3]] | 1969 | 25 kOe, 85 kA | 0.3 | 2.25 × 10¹⁹ | 0.003 | **2.0 × 10¹⁶** |
| ST | 1971 | 10 cm limiter, 42 kA | 0.5 | 4 × 10¹⁹ | 0.0034 | 6.8 × 10¹⁶ |
| ST | 1972 | 12 cm limiter | 0.4 | 6 × 10¹⁹ | 0.01 | 2.4 × 10¹⁷ |
| TFR | 1974 | Mo limiter | 0.95 | 7.1 × 10¹⁹ | 0.019 | 1.3 × 10¹⁸ |
| PLT | 1976 | 22149-231 | 1.54 | 5.2 × 10¹⁹ | 0.04 | 3.2 × 10¹⁸ |
| **Alcator A** | 1978 | 8.7 T discharge | 0.8 | **1.5 × 10²¹** | 0.02 | 2.4 × 10¹⁹ |
| TFR | 1981 | Inconel limiter | 0.95 | 1.61 × 10²⁰ | 0.034 | 5.2 × 10¹⁸ |
| **Alcator C** | 1984 | Multiple [[pellet-injection|pellet injection]] | 1.5 | **1.5 × 10²¹** | 0.052 | 1.2 × 10²⁰ |
| ASDEX | 1988 | 23349-57 | 0.8 | 7.50 × 10¹⁹ | 0.12 | 7.2 × 10¹⁸ |
| **[[jet|JET]]** | 1991-11-02 | 26087 | 18.6 | 4.1 × 10¹⁹ | 0.8 | **6.1 × 10²⁰** |
| JET | 1991-11-04 | 26095 | 22.0 | 3.4 × 10¹⁹ | 0.8 | 6.0 × 10²⁰ |
| JET | 1991-11-09 | 26148 | 18.8 | 2.4 × 10¹⁹ | 0.6 | 2.7 × 10²⁰ |
| [[tftr|TFTR]] | 1992-10-29 | 68522 | 29.0 | 6.8 × 10¹⁹ | 0.18 | 3.5 × 10²⁰ |
| JT-60U | 1994 | 17110 | 37 | 4.2 × 10¹⁹ | 0.3 | 4.7 × 10²⁰ |
| TFTR | 1994-05-27 | 76778 | 44 | 6.3 × 10¹⁹ | 0.19 | 5.3 × 10²⁰ |
| TFTR | 1994-11-02 | 80539 | 36 | 6.7 × 10¹⁹ | 0.17 | 4.1 × 10²⁰ |
| **TFTR** | **1995-02-17** | **83546** | **43** | 6.6 × 10¹⁹ | 0.28 | **7.9 × 10²⁰** ← highest ever achieved |
| JT-60U | 1996 | E26939 | 45.0 | 4.35 × 10¹⁹ | 0.26 | 5.1 × 10²⁰ |
| JT-60U | 1996 | E26949 | 35.5 | 4.3 × 10¹⁹ | 0.28 | 4.3 × 10²⁰ |
| [[diii-d|DIII-D]] | 1997 | 87977 | 18.1 | 8.5 × 10¹⁹ | 0.24 | 3.7 × 10²⁰ |
| JET | 1997-10-31 | 42976 | 28 | 3.3 × 10¹⁹ | 0.51 | 4.7 × 10²⁰ |
| **JT-60U** | 1998 | E31872 | 16.8 | 4.8 × 10¹⁹ | 0.69 | **5.6 × 10²⁰** |
| START | 1998 | 35533 | 0.2 | 1.02 × 10²⁰ | 0.003 | 6.1 × 10¹⁶ |
| MAST | 2006 | 14626 | 3 | 3 × 10¹⁹ | 0.05 | 4.5 × 10¹⁸ |
| NSTX | 2009 | 129041 | 1.2 | 5 × 10¹⁹ | 0.08 | 4.8 × 10¹⁸ |
| [[east|EAST]] | 2015 | 56933 | 2.1 | 8.5 × 10¹⁹ | 0.054 | 9.6 × 10¹⁸ |
| [[kstar|KSTAR]] | 2014 | 7081 | 2 | 4.80 × 10¹⁹ | 0.1 | 9.6 × 10¹⁸ |
| **[[alcator-c-mod|Alcator C-Mod]]** | 2016 | 1160930033 | 2.5 | **5.5 × 10²⁰** | 0.054 | 7.4 × 10¹⁹ |
| Alcator C-Mod | 2016 | 1160930042 | 6 | 2 × 10²⁰ | 0.054 | 6.5 × 10¹⁹ |
| ASDEX-U | 2016 | 32305 | 8 | 5 × 10¹⁹ | 0.056 | 2.2 × 10¹⁹ |
| EAST | 2018 | 78723 | 1.94 | 5.58 × 10¹⁹ | 0.045 | 4.9 × 10¹⁸ |
| [[globus-m2|Globus-M2]] | 2019 | 37873 | 1.2 | 1.19 × 10²⁰ | 0.01 | 1.4 × 10¹⁸ |
| PI3 ([[general-fusion|General Fusion]]) | 2021 | 21 100 | 0.4 | 4 × 10¹⁹ | 0.012 | 1.9 × 10¹⁷ |
| JET (DTE2) | 2021-12-21 | 99972 | 11 | 8.5 × 10¹⁹ | 0.23 | 2.2 × 10²⁰ |
| [[st40|ST40]] ([[tokamak-energy|Tokamak Energy]]) | 2022 | 10009 | 9.6 | 5.5 × 10¹⁹ | 0.012 | 6.3 × 10¹⁸ |
| JET (DTE3) | 2023-10-09 | 104600 | 7 | 9 × 10¹⁹ | 0.23 | 1.4 × 10²⁰ |
| **[[sparc|SPARC]]** | **2027** | *projected* | **20** | **4 × 10²⁰** | **0.77** | **6.2 × 10²¹** |
| **[[iter|ITER]]** | **2039** | *projected* | **20** | **1 × 10²⁰** | **3.7** | **7.4 × 10²¹** |

---

## The single most striking thing in this table

**The highest triple product ever achieved in a tokamak was set by TFTR on 17 February 1995: 7.9 × 10²⁰ keV m⁻³ s.**

It has not been beaten in thirty-one years.

JT-60U came close in 1996–98 (5.1–5.6 × 10²⁰). JET's D-T campaigns in 2021 and 2023 reached 2.2 × 10²⁰ and 1.4 × 10²⁰ respectively — **substantially below the 1990s peak**.

This is not a sign that the field went backwards. Three things explain it, and each is informative:

1. **The 1990s D-T peaks were transient, hero-shot conditions** on machines pushed to their absolute limits for a second or two, at temperatures (36–44 keV) far above what a reactor would use.
2. **Modern campaigns optimise for different things** — pulse duration, integrated scenarios, ITER-relevant wall materials, exhaust compatibility. JET's 2021 and 2023 campaigns ran with a beryllium-tungsten ITER-like wall that is *harder* to get performance from than the carbon walls of the 1990s, deliberately, because ITER will have one.
3. **No larger tokamak was built.** TFTR shut down in 1997, JT-60U was rebuilt as [[jt-60sa|JT-60SA]], JET retired in 2023. Triple product scales strongly with machine size and current, and **between 1997 and the 2020s no machine capable of exceeding those values was constructed anywhere in the world.**

Point 3 is the quantitative demonstration of the "construction stall" argument in [[21-the-graveyard|Document 21]]. **Magnetic fusion's performance plateau from the late 1990s to the 2020s was not a physics stall. It was a procurement stall.** The field spent that period building ITER, and ITER was late.

**And the corollary matters:** SPARC's projected 6.2 × 10²¹ is roughly **eight times the best value ever achieved**, and ITER's 7.4 × 10²¹ about nine times. These are not incremental targets. They are the first genuine step forward in this metric since the Clinton administration.

---

## Table B — Other magnetic and lower-density magneto-inertial concepts

| Machine | Concept | Year | T_i0 (keV) | n_i0 (m⁻³) | **Triple product** |
|---|---|---|---|---|---|
| **[[zeta|ZETA]]** | Pinch | 1957 | 0.09 | 1 × 10²⁰ | **9.0 × 10¹⁴** |
| Model C | [[stellarator|Stellarator]] | 1969 | 0.2 | 5 × 10¹⁸ | 1.0 × 10¹⁴ |
| ETA-BETA I | RFP | 1977 | — | 1 × 10²¹ | 1.0 × 10¹³ |
| W7-A | Stellarator | 1980 | 0.01 | 9.6 × 10¹⁹ | 8.6 × 10¹⁷ |
| ETA-BETA II | RFP | 1984 | — | 3.5 × 10²⁰ | 3.2 × 10¹⁵ |
| TMX-U | Mirror | 1984-02-02 | 0.545 | 2 × 10¹⁸ | 3.0 × 10¹⁴ |
| ZT-40M | RFP | 1987 | 0.09 | 9.60 × 10¹⁹ | 2.2 × 10¹⁶ |
| CTX | Spheromak | 1990 | — | 4.50 × 10¹⁹ | 1.6 × 10¹⁵ |
| LSX | FRC | 1993 | 0.15 | 1.30 × 10²¹ | 7.1 × 10¹⁶ |
| MST | RFP | 2001 | 0.33 | 1.20 × 10¹⁹ | 3.0 × 10¹⁶ |
| **W7-AS** | Stellarator | 2002 | — | 1.10 × 10²⁰ | **1.5 × 10¹⁹** |
| FRX-L | FRC | 2003 | 0.18 | 4 × 10²² | 1.2 × 10¹⁶ |
| ZaP | Z-pinch | 2003 | — | 9 × 10²² | 3.3 × 10¹⁵ |
| FRX-L | FRC | 2005 | 0.547 | 4.81 × 10²² | 2.9 × 10¹⁶ |
| HSX | Stellarator (quasi-helical) | 2005 | — | 2.5 × 10¹⁸ | 6.8 × 10¹⁴ |
| TCS | FRC | 2005 | 0.396 | 6.50 × 10¹⁸ | 6.5 × 10¹² |
| SSPX | Spheromak | 2007 | 2.28 | 2.25 × 10²⁰ | 1.1 × 10¹⁷ |
| GOL-3 | Mirror | 2007 | — | 7 × 10²⁰ | 1.3 × 10¹⁸ |
| RFX-mod | RFP | 2008 | 0.09 | 3 × 10¹⁹ | 7.5 × 10¹⁶ |
| **LHD** | Stellarator | 2008 | 0.1 | 5 × 10²⁰ | **5.2 × 10¹⁹** |

### What this table shows

**ZETA at 9.0 × 10¹⁴ in 1957 is the field's baseline.** SPARC's projected 6.2 × 10²¹ is roughly **seven million times higher**.

**Stellarators climbed five orders of magnitude** from Model C (1.0 × 10¹⁴, 1969) through W7-A (8.6 × 10¹⁷, 1980) and W7-AS (1.5 × 10¹⁹, 2002) to LHD (5.2 × 10¹⁹, 2008) — and W7-X has since set the record for pulses over 10 seconds. That is what forty years of optimisation theory bought.

**HSX's 6.8 × 10¹⁴ (2005) looks unimpressive** and is not the point: HSX was a small university device built to demonstrate that **quasi-helical symmetry works**, which it did, and which underwrites the entire modern stellarator programme.

**The alternative concepts sit two to four orders of magnitude below the tokamaks.** That is the honest position, and it is why the tokamak remains the leading concept despite its disruptions and its pulsed operation. It is also why the alternative concepts' advantages — no disruptions, steady state, [[direct-energy-conversion|direct energy conversion]], simple maintenance — have to be very large to compensate.

---

## Table C — Scientific energy gain, Q_sci

Only experiments that produced enough fusion energy for Q_sci to be meaningful.

| Machine | Date | Shot | **Q_sci** | Note |
|---|---|---|---|---|
| JET | 1991-11-09 | 26148 | 0.12 | First controlled fusion power in a magnetic device |
| TFTR | 1995-02-17 | 83546 | 0.28 | |
| JET | 1997-10-31 | 42974/42976 | **0.27** | See note below on the "0.67" figure |
| NIF | 2013-11-19 | N131119 | 0.16 | |
| NIF | 2017-08-27 | N170827 | 0.62 | |
| NIF | 2019-10-07 | N191007 | 0.63 | |
| **NIF** | **2021-08-08** | **N210808** | **0.69** | [[burning-plasma|Burning plasma]]; threshold of ignition |
| JET (DTE2) | 2021-12-21 | 99971/99972 | 0.33 | 59 MJ |
| **JET (DTE3)** | **2023-10-03** | **104522** | **0.37** | **69 MJ — magnetic-confinement record** |
| **NIF** | **2022-12-05** | **N221204** | **1.51** | **First ignition. 3.15 MJ from 2.05 MJ** |
| NIF | 2023-07-30 | N230729 | **1.89** | 3.88 MJ |
| NIF | 2024 | — | 1.26 / 1.55 | |
| **NIF** | 2024-11-18 | N241117 | **2.36** | 5.2 MJ |
| OMEGA | 2021–2022 | various | 0.01–0.03 | Direct drive, at 1/70th of NIF's energy |

*(The April 2025 8.6 MJ shot at target gain 4.13 and the June 2026 11th ignition at ~3.8 postdate the dataset's cutoff; see [[05-inertial-confinement-fusion|Document 05]].)*

### An important definitional note on JET's famous "Q = 0.67"

The number usually quoted for JET's 1997 DTE1 result is **Q ≈ 0.67**, from 16.1 MW of fusion power. Wurzel and Hsu's harmonised analysis assigns shot 42976 a **Q_sci of 0.27**, from **P_fusion = 1.1 × 10⁷ W against P_in = 4.0 × 10⁷ W**.

Both are defensible; they measure different things. **0.67 is a transient peak** reached for a fraction of a second under conditions that could not be sustained. **0.27 is the harmonised value** under the paper's consistent definition.

This is not pedantry. It is the single best illustration of why [[01-fusion-physics-fundamentals|Document 01 §5]] insists on specifying *which* Q is being quoted, and it explains why headline fusion numbers from different eras cannot be compared without checking the definition underneath them.

---

## Summary: the whole history in one column

| Era | Best triple product achieved | Factor gained |
|---|---|---|
| 1957 (ZETA) | 9.0 × 10¹⁴ | — |
| 1969 (T-3) | 2.0 × 10¹⁶ | ×22 |
| 1978 (Alcator A) | 2.4 × 10¹⁹ | ×1,200 |
| 1984 (Alcator C) | 1.2 × 10²⁰ | ×5 |
| **1995 (TFTR)** | **7.9 × 10²⁰** | **×6.6** |
| 1995 → 2023 | *no improvement* | **×1** |
| **2027 (SPARC, projected)** | **6.2 × 10²¹** | **×7.8** |
| 2039 (ITER, projected) | 7.4 × 10²¹ | ×1.2 |

**From 1957 to 1995 the field gained nearly six orders of magnitude in thirty-eight years — a rate comparable to Moore's law.**

**From 1995 to 2023 it gained nothing on this metric**, because no machine capable of exceeding TFTR was built.

**SPARC, if it performs to projection, resumes the climb in 2027.**

That is the clearest quantitative statement of where fusion actually is, and it reframes the whole "always thirty years away" complaint. Fusion's performance curve did not flatten because the physics ran out. It flattened because, for a quarter of a century, nobody built the next machine.

---

**Continue to:** [[27-people-institutions-public-trust|27 — People, Institutions and Public Trust]] · [[01-fusion-physics-fundamentals|01 — Physics Fundamentals]] · [[12-state-of-play-2026|12 — State of Play 2026]]
