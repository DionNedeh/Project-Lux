---
title: "Impact of trapping on tritium self-sufficiency and tritium inventories in fusion power plant fuel cycles"
type: source
source_type: paper
file: "raw/papers/Meschini-2025-trapping-tritium-self-sufficiency.pdf"
authors: "S. Meschini, R. Delaporte-Mathurin, G. R. Tynan (MIT PSFC / UC San Diego), S. E. Ferry (MIT PSFC)"
publisher: "Nuclear Fusion 65 036010 (16 pp), DOI 10.1088/1741-4326/adacfa, CC BY 4.0"
source_date: 2025-02-11
ingested: 2026-11-02
tags:
  - fusion/source
  - fusion/subsystems
  - fusion/materials
status: stable
confidence: high
related:
  - "[[arc]]"
  - "[[st-e1]]"
  - "[[meschini-2023-tritium-fuel-cycle-arc-step]]"
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
  - "[[tritium-retention]]"
  - "[[tritium-breeding-ratio]]"
  - "[[declared-tbr-values]]"
  - "[[tritium-start-up-inventory]]"
  - "[[tritium-doubling-time]]"
  - "[[tritium-accountancy]]"
  - "[[tungsten-pfc]]"
  - "[[displacements-per-atom]]"
  - "[[29-remote-handling-and-maintenance]]"
  - "[[28-vacuum-wall-conditioning-tritium-plant]]"
created: 2026-11-02
updated: 2026-11-02
---
The paper that puts a number on what every fuel-cycle model in this vault had left out.
Full text held; **CC BY 4.0**, version of record. Received 12 September 2024, accepted
22 January 2025.

## The omission it closes

[[meschini-2023-tritium-fuel-cycle-arc-step|Its own predecessor]] and
[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency|Abdou *et al.*]] both track tritium as it
*flows*. Neither tracks tritium that stops — held in first wall, divertors and breeding
blanket by [[tritium-retention|trapping]]. The authors state plainly that **no
state-of-the-art fuel-cycle model considers it**, and that two effects compound it: traps
created by irradiation damage, and the component replacements that carry trapped inventory out
of the plant.

The novelty claimed is integrating three things into one system-level model — a
physics-based trapping model, the evolution of damage-induced traps, and
[[29-remote-handling-and-maintenance|component replacement]].

## The result, for an ARC-class plant

> [!warning] Trapped inventory is not a rounding error
> Tritium inventory in the first wall and vacuum vessel rises by a **factor of 10³–10⁴** once
> trapping, damage-induced traps and replacement are accounted for.

Carried through the fuel cycle, that slows the whole system:

| Quantity | Change against a no-trapping scenario |
|---|---|
| [[tritium-doubling-time\|Doubling time]] | **+50%** |
| [[tritium-start-up-inventory\|Start-up inventory]] | **+30%** |
| Required [[tritium-breeding-ratio\|TBR]] | **+2–5%** |

## Why that uplift matters to this vault

A 2–5% uplift on *required* TBR is small in isolation and decisive in context. The declared
ST-E1 breeding values recorded in [[declared-tbr-values]] span **1.085–1.146**, and
[[meschini-2023-tritium-fuel-cycle-arc-step|the 2023 paper]] bounds maximum achievable TBR at
1.1–1.2. Applying this correction to a requirement already sitting inside that band moves the
requirement toward — or past — what the design achieves. **No source in this vault has done
that calculation for [[st-e1|ST-E1]], and this page does not do it either**: the uplift is
derived for an ARC-class plant with a FLiBe immersion blanket, not for a liquid-lithium
spherical tokamak, and transferring it would be inference, not evidence.

## What it does **not** establish

- **Nothing measured.** A modelling result for an unbuilt plant; no fuel cycle has operated.
- **ARC-class only.** The 10³–10⁴ figure and all three percentage changes are ARC-class.
- **No accountancy claim.** Trapped tritium is modelled, not *measured* — and
  [[tritium-accountancy]] records that no instrument exists for the blanket term at all.
