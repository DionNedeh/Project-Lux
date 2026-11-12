---
title: "Pellet Injection"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/subsystems
status: stable
confidence: high
sources:
  - "[[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency]]"
related:
  - "[[ornl]]"
  - "[[type-one-energy]]"
  - "[[wendelstein-7-x]]"
  - "[[shattered-pellet-injection]]"
  - "[[tritium-burn-fraction]]"
  - "[[tritium-start-up-inventory]]"
  - "[[16-heating-current-drive-fuelling]]"
created: 2026-08-26
updated: 2026-10-19
---
The only viable method for fuelling the **core** of a reactor plasma.

Gas puffing does not work: neutrals ionise within centimetres of the boundary and never reach the core. It fuels the edge and the divertor — useful for [[detachment]] control — but cannot sustain a core density profile.

Instead, freeze deuterium-tritium into a solid pellet a few millimetres across and fire it in at hundreds of metres per second. The pellet ablates as it penetrates.

## The high-field-side trick

On the **high-field side** of the torus, ablated material drifts *inward* rather than outward, through a curvature-driven ∇B drift effect. So high-field-side injection delivers fuel far deeper than mechanical penetration alone would suggest — which is why reactor designs route pellet guide tubes over the top of the machine and inject from the inboard side.

Pellets also do double duty as **[[elm]] pacing** and, shattered, as [[shattered-pellet-injection|disruption mitigation]].

## Who owns the technology

**[[ornl]]** has been the world centre for four decades. Two 2026 datapoints:

- **[[wendelstein-7-x]]'s record 43-second, world-record-[[triple-product]] discharge was fed by ~90 frozen hydrogen pellets from a one-of-a-kind injector built at ORNL in Tennessee**
- On **6 August 2026** ORNL licensed **four cryogenic pellet fuelling inventions to [[type-one-energy]]**, including an extrusion system producing pellets **at rates appropriate for reactor operation** — research injectors fire tens per discharge; a plant needs a continuous line running for months

## Why the fuel cycle depends on this

Pellet fuelling is the designated route to the **fuelling efficiency** `η_f` that
[[tritium-burn-fraction|tritium self-sufficiency]] requires, and the numbers are tight
([[abdou-2021-dt-fuel-cycle-tritium-self-sufficiency|Abdou *et al.* 2021]], whose authors include
ORNL's L.R. Baylor):

| Quantity | Value | Status |
|---|---|---|
| Reference `η_f` | **25%** | Assumed |
| DEMO extrapolation | **below 25%** | Projected |
| High-field-side pellets | **25–50%** | Projected |
| Pellet-only T fuelling with D edge control | `f_b` **1.8–3.6%** | Projected, not validated |

Two cautions the paper states itself: pellet fuelling efficiency at shallow penetration is
*"highly uncertain"* and possibly optimistic, depending on how much pellet mass an **[[elm]]** ejects
— so the ELM-pacing and fuelling roles of pellets are in partial tension. And sustained high-speed
pellet injection has so far been demonstrated **only at 1 Hz, short-pulse** capability, against the
continuous reactor duty the ORNL/Type One licensing is meant to address.

**This is the link that makes pellet injection a fuel-supply technology rather than a density-control
one.** A plant that cannot fuel efficiently must circulate more tritium for the same power, which
enlarges its [[tritium-start-up-inventory|start-up inventory]] and raises its required
[[tritium-breeding-ratio|TBR]].
