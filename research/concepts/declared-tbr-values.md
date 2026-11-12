---
title: "Declared TBR Values and Their Conflicts"
type: concept
domain: engineering
symbol: "TBR"
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/designs
status: stable
confidence: high
sources:
  - "[[overview-of-the-helios-design]]"
  - "[[willis-2026-st-e1-pre-concept-design-overview]]"
  - "[[yang-2026-st-e1-tritium-tmap8-surrogate-models]]"
  - "[[st-e1-tritium-systems-crossref-metadata-2026]]"
  - "[[st-e1-neutronics-crossref-metadata-2026]]"
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
  - "[[meschini-2023-tritium-fuel-cycle-arc-step]]"
  - "[[meschini-2025-trapping-tritium-self-sufficiency]]"
  - "[[ukaea-2026-vanadium-strategy]]"
related:
  - "[[tritium-breeding-ratio]]"
  - "[[tritium-burn-fraction]]"
  - "[[tritium-retention]]"
  - "[[vanadium-alloys]]"
  - "[[helios]]"
  - "[[st-e1]]"
  - "[[lithium-6]]"
  - "[[lithium-lead-eutectic]]"
  - "[[30-power-plant-designs-compared]]"
created: 2026-10-19
updated: 2026-11-02
---
What designs claim for [[tritium-breeding-ratio|TBR]], and where those claims disagree — with each
other and, in two cases, **internally**.

Judged against [[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency|Abdou's]] bands: *unlikely* above
1.15, *possible* 1.05–1.15, maximum achievable ~1.15.

## Helios — 1.3 and <1.15, in one paper

[[helios|Helios]] quotes an **idealised TBR of 1.3** from a [[lithium-lead-eutectic|PbLi]] blanket
enriched to 65% [[lithium-6]], while its own sensitivity analysis concludes **TBR under 1.15**
suffices ([[overview-of-the-helios-design]]).

> [!note] A conflict of kind, not of fact
> The 1.3 sits outside Abdou's achievable range; the <1.15 agrees with him almost exactly. But 1.3 is
> a **neutronics figure of merit** and 1.15 a **system requirement net of ports, penetrations and
> diagnostics**. Helios's two numbers *bracket* Abdou's boundary rather than contradicting it.
> **Both stand.**

## ST-E1 — RESOLVED 2026-11-02

Three figures stood recorded as irreconcilable. Read in full,
[[st-e1-tritium-systems-crossref-metadata-2026|086004]] shows they are **one quantity at three
penetration assumptions** — rows of, or ranges from, its Table 2 sensitivity study:

| Figure | What it actually is |
|---|---|
| **1.146** | Table 2 baseline, full breeding coverage — the overview's "> 1.14" |
| **1.113** | Table 2's *100% Pipes + Stiffening Plates* row (−2.8%), and exactly [[yang-2026-st-e1-tritium-tmap8-surrogate-models\|Yang's]] model input |
| **1.085** | Table 2's *100% ICRH* row (−8.2%), floor of the quoted 1.085–1.14 range |
| **~1.1** | The overview's §3.2 prose — that same post-insertion range |
| **1.20** | An *"initial design target … for rough scoping studies"*, never a prediction |

> [!note] CORRECTION 2026-11-02 — Yang's 1.113 was not a third estimate
> This page previously recorded 1.113 as an independent model input disagreeing with the
> overview. It is **a row of ST-E1's own sensitivity table**. That conflict was a provenance
> artefact and is now closed.

**A genuine tension remains.** [[st-e1-neutronics-crossref-metadata-2026|086003]]'s neutronics
gives **1.169** (MCNP) and **1.194** (G4Tokamak) — both *above* 086004's full-coverage 1.146 and
above Abdou's achievable ceiling. Same plant, same Focus Collection, different codes and geometry
revisions. **No source reconciles the two papers.**

**ST-E1 breeds without ⁶Li enrichment, and that is now evidenced.** 086004 selects natural liquid
lithium; [[ukaea-2026-vanadium-strategy|UKAEA]] states independently that
[[vanadium-alloys|V-4Cr-4Ti]] reduces the need for enrichment or
[[beryllium|beryllium]] multiplication in liquid-lithium blankets. Previously asserted — see
[[lithium-6]].

## Why the arithmetic may matter less than it looks

ST-E1's own fuel-cycle team reports **extraction sensitivity and fuelling efficiency as the dominant
drivers of inventory performance, *rather than marginal improvements in breeding ratio***
([[st-e1-tritium-systems-crossref-metadata-2026]]) — Abdou's reframing reached independently by a
company with every incentive to foreground its breeding instead.

So the gap between 1.1 and 1.14 matters less than that between a 0.36% and a 2%
[[tritium-burn-fraction|burn fraction]] — and the ST-E1 spread proved to be exactly that, a
provenance defect rather than a design risk.

> [!warning] What would move these numbers is in none of them
> [[meschini-2025-trapping-tritium-self-sufficiency|Meschini *et al.* 2025]] raise *required* TBR
> by **2–5%** once [[tritium-retention|trapping]] is modelled — and **no figure on this page
> includes it.**
