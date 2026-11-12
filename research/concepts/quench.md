---
title: "Quench"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/magnets
  - fusion/risks
status: stable
confidence: high
sources:
  - "[[overview-of-the-helios-design]]"
related:
  - "[[rebco]]"
  - "[[18-superconductors-and-magnets]]"
  - "[[commonwealth-fusion-systems]]"
  - "[[helios]]"
  - "[[thea-energy]]"
  - "[[01-fusion-physics-fundamentals]]"
created: 2026-08-26
updated: 2026-09-08
---
A local loss of superconductivity. The affected region becomes resistive, dissipates energy, heats, and the normal zone spreads. In a magnet storing **gigajoules** — [[iter]]'s system holds ~51 GJ — an undetected quench concentrates that energy in a small volume and destroys the conductor.

## HTS makes this harder, not easier

Low-temperature superconductors have a fast **normal zone propagation velocity** — metres per second — so a quench spreads quickly, distributes its energy, and announces itself as a voltage rise.

**[[rebco]]'s NZPV is of order centimetres per second.** A hot spot can reach destructive temperature while remaining electrically almost invisible.

## Detection approaches

- **Voltage taps** — conventional; too slow and too noisy for HTS alone
- **Fibre-optic sensing** — distributed temperature and strain. [[commonwealth-fusion-systems]]'s **PIT VIPER** gives every HTS tape stack its own fibre, allowing reaction in **under a second**
- **Current-distribution monitoring** — detects both quench *and* cumulative damage, which is the more useful capability for a decades-lived magnet
- **No-insulation winding** — CFS's **NINT**: adjacent turns in electrical contact, so current bypasses a defect radially. The magnet routes around damage rather than quenching. Proven in the 2021 20 T TFMC test

NINT suits **steady-state** magnets at unvarying current; PIT VIPER suits **pulsed** coils. Two architectures for two duty cycles.

## Splitting the strategy by coil role

[[helios|Helios]] applies two schemes within one machine, chosen by what each coil does
([[overview-of-the-helios-design]]). Its **12 plasma-encircling coils are insulated**, with currents
**actively dumped into external resistors** on detection — the conventional protected approach for
coils holding most of the stored energy. Its **324 field-shaping coils are partially insulated and
self-protecting**, relying on current sharing between turns in the manner of the no-insulation idea
above. Driving 324 individually controlled coils with hot-swappable, redundant DC/DC converters makes
per-coil self-protection the tractable choice; the encircling supplies instead run to 50 kA with
regenerative discharge.

The design also quantifies why the field ceiling is a quench question, not only a stress one: raising
maximum on-coil field from 20 T to 25 T would release **60% more quench energy** (and impose 60%
higher forces), which the paper gives as a reason to stay at 20 T despite the larger plant that 25 T
would allow.
