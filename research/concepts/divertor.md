---
title: "Divertor"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/physics
status: stable
confidence: high
sources:
  - "[[overview-of-the-helios-design]]"
related:
  - "[[detachment]]"
  - "[[super-x-divertor]]"
  - "[[elm]]"
  - "[[tungsten-pfc]]"
  - "[[helios]]"
  - "[[stellarator]]"
  - "[[wendelstein-7-x]]"
  - "[[09-engineering-challenges]]"
created: 2026-08-26
updated: 2026-09-08
---
The component that handles plasma exhaust — and the binding physics constraint on fusion power density.

## The numbers

A **500 MW** fusion plasma must exhaust roughly **100 MW**, channelled onto a strike region only **millimetres wide**.

| | Value |
|---|---|
| Material limit, steady-state | **5–20 MW/m²** |
| [[tungsten-pfc\|Tungsten]] design target | **< 10 MW/m²** |
| Unmitigated reactor heat flux | **~10× above the limit** |
| Required target plasma temperature | **single-digit eV** (below the sputtering threshold) |

**The problem worsens with machine quality.** The scrape-off layer width narrows as machines get larger and fields stronger (Eich scaling, λ_q roughly inversely proportional to poloidal field) — so compact high-field designs face it most acutely. See [[b4-scaling]].

The only known answer is [[detachment]]. Alternative geometries — [[super-x-divertor]], X-point radiator, [[negative-triangularity]] — and liquid-metal surfaces are the active research fronts.

**Every design study for thirty years has identified heat exhaust, not confinement, as the limit on power density.** See [[30-power-plant-designs-compared]].

## The stellarator's separate divertor problem

[[stellarator|Stellarators]] cannot simply inherit the tokamak poloidal divertor, and their own options
have not clearly scaled. The experimentally proven frontrunner is the **island divertor** used on
[[wendelstein-7-x|W7-X]] — but its proponents accept it does not scale directly to a power plant,
because neutral compression at the target is insufficient for a practical vacuum pumping scheme.

[[helios|Helios]] claims a route around this: a **toroidally continuous, non-resonant X-point divertor**,
tokamak-like, which its authors state is the first time a stellarator equilibrium has been explicitly
designed to contain one, and the first pairing of such a divertor with a power-plant-relevant
equilibrium at finite beta and bootstrap current ([[overview-of-the-helios-design]]). The higher
neutral compression is what lets the design use **turbomolecular rather than cryosorption pumps** —
better at pumping helium and needing no regeneration, at the cost of long ducts to keep the pumps
magnetically shielded.

Assumed target heat flux is **10 MW/m²**, at the [[tungsten-pfc|tungsten]] design target above rather
than below it. This is a design study: the divertor exists in simulation only.
