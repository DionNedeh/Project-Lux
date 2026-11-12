---
title: "Tritium Doubling Time"
type: concept
domain: engineering
symbol: "t_d"
units: "days or years"
tags:
  - fusion/concept
  - fusion/subsystems
  - fusion/economics
status: draft
confidence: medium
sources:
  - "[[meschini-2023-tritium-fuel-cycle-arc-step]]"
  - "[[meschini-2025-trapping-tritium-self-sufficiency]]"
  - "[[st-e1-tritium-systems-crossref-metadata-2026]]"
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
related:
  - "[[tritium-start-up-inventory]]"
  - "[[tritium-breeding-ratio]]"
  - "[[tritium-burn-fraction]]"
  - "[[tritium-retention]]"
  - "[[declared-tbr-values]]"
  - "[[availability]]"
  - "[[direct-internal-recycling]]"
  - "[[arc]]"
  - "[[st-e1]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
  - "[[13-roadmap-to-2040]]"
created: 2026-11-02
updated: 2026-11-02
---
The time a plant takes to breed enough surplus tritium to **double its stored inventory** — and
so to supply the [[tritium-start-up-inventory|start-up charge]] of the next plant. It is the
quantity that converts a single working reactor into a fleet, which makes it an industry-scaling
parameter rather than a plant one.

## Why it is a design requirement and not an outcome

With no external tritium supply worth relying on, plant *n+1* is fuelled by plant *n*. A long
doubling time therefore caps the deployment rate of an entire industry, independently of how
well any single machine performs — the link to [[13-roadmap-to-2040|build-out timelines]].

[[meschini-2023-tritium-fuel-cycle-arc-step|Meschini *et al.* 2023]] show the requirement trades
directly against [[tritium-burn-fraction|burn efficiency]]:

| Target `t_d` | Verdict |
|---|---|
| 1 year | Self-sufficiency *"highly unlikely"* below 1% tritium burn efficiency |
| 5 years | *"Much easier to achieve"* |

So a short doubling time is bought with burn efficiency, [[availability|plant availability]]
above 70%, processing times under 4 hours and
[[direct-internal-recycling|direct internal recycling]] — not with
[[tritium-breeding-ratio|breeding ratio]] alone.

## Declared values

| Design | `t_d` | Source |
|---|---|---|
| [[st-e1\|ST-E1]] | **152 days** | [[st-e1-tritium-systems-crossref-metadata-2026\|086004]] |
| Generic reference | 5 years | [[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency\|Abdou *et al.*]] |

ST-E1's 152 days is **strikingly short** against Abdou's five-year reference, and it is a
designed figure, not a measured one. It is also computed under a **100% availability**
assumption — see [[availability]] — which is the most optimistic input available and sits above
the >70% that Meschini *et al.* require.

> [!warning] Trapping stretches it by half again
> [[meschini-2025-trapping-tritium-self-sufficiency|Meschini *et al.* 2025]] find doubling time
> rises **+50%** once [[tritium-retention|trapping]], damage-induced traps and component
> replacement are modelled, for an ARC-class plant. No source applies that correction to ST-E1,
> and this vault does not apply it either.

No doubling time has ever been measured. Every figure here is the output of a system-level model
of a plant that does not exist.
