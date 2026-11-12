---
title: "Gyrotron and ECRH"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/subsystems
status: stable
confidence: high
related:
  - "[[neoclassical-tearing-mode]]"
  - "[[iter]]"
  - "[[dtt]]"
  - "[[16-heating-current-drive-fuelling]]"
  - "[[recirculating-power]]"
created: 2026-08-26
updated: 2026-08-26
---
The megawatt millimetre-wave source that makes **electron cyclotron resonance heating** possible.

## Why ECRH is special

Launch microwaves at the electron cyclotron frequency, `f_ce ≈ 28 GHz per tesla`. At the resonant surface, electrons absorb the wave directly. Three properties no other heating method has:

- **Extreme localisation** — because resonance depends on local B, deposition can be steered to a chosen radius. Widths of a few centimetres in a metres-wide plasma
- **No in-vessel coupling structure** — the wave propagates in vacuum; the launcher sits behind a port. Nothing touches the plasma, and the aperture is small, which matters because every port is a hole in the breeding blanket
- **Polarisation-selectable current drive** (ECCD)

That localisation is why ECRH is the primary tool for **MHD control** — see [[neoclassical-tearing-mode]] — rather than merely bulk heating.

## The device

A fast-wave vacuum electron tube: an electron beam spirals in a strong superconducting magnet, bunches in gyration phase, and radiates coherently into a high-order cavity mode. The output window is a **synthetic diamond disc** — the only material both transparent at 170 GHz and able to conduct away the heat.

**[[iter]] requires 24 gyrotrons at 170 GHz, 1 MW each, for 3,600-second pulses.**

## The 2026 milestone

The first 170 GHz / 1 MW gyrotron for **[[dtt]]** passed acceptance at the **FALCON** facility in Lausanne: 1 MW for **100-second pulses**, pre-series tube from THALES at **1.02 MW, 40% efficiency, 95% reliability** (19 of 20 pulses). A joint F4E–DTT procurement serving both ITER and DTT.

Note the gap: **100 seconds demonstrated against a 3,600-second requirement.**
