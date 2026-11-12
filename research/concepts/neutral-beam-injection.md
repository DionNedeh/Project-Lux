---
title: "Neutral Beam Injection (NBI)"
type: concept
domain: engineering
tags:
  - fusion/concept
  - fusion/engineering
  - fusion/subsystems
status: stable
confidence: high
related:
  - "[[nbtf-spider-mitica]]"
  - "[[iter]]"
  - "[[tae-technologies]]"
  - "[[16-heating-current-drive-fuelling]]"
created: 2026-08-26
updated: 2026-08-26
---
Accelerate ions electrostatically, **neutralise them** so they can cross the magnetic field, inject them into the plasma where they re-ionise and thermalise.

Unique in doing four things at once: **heats**, **drives current**, **fuels**, and **drives rotation** (which stabilises certain MHD modes). That combination is why it remains the workhorse despite being the most mechanically complex option.

## The negative-ion fork

To penetrate to the centre of a large dense plasma, beam particles must reach ~**1 MeV**. But neutralisation efficiency of **positive** ions collapses above ~100 keV/amu. **Negative ions (D⁻) neutralise efficiently at any energy**, because you are stripping a loosely bound extra electron rather than capturing one.

That decision cascades into difficulty. D⁻ has binding energy under 1 eV, so it is destroyed by collisions, stray fields and photons. Producing it in quantity requires a **caesiated surface** — caesium evaporated onto the plasma grid to lower the work function — which then migrates and contaminates. Co-extracted electrons must be dumped before acceleration. The whole accelerator sits at −1 MV inside an SF₆-insulated vessel.

## ITER

**33 MW total**, ~1 MeV, **40 A of negative deuterium ions per injector**, ~16.5 MW delivered, **for one hour**. Prototyped at [[nbtf-spider-mitica]] in Padua — a heating system that required a research programme comparable in scale to a mid-sized tokamak.

**[[tae-technologies]]** uses beams not as auxiliary heating but as the primary physics mechanism, sustaining its [[field-reversed-configuration]].
