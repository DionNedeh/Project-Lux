---
title: "L-H Transition and Power Threshold"
type: concept
domain: physics
symbol: "P_L-H"
tags:
  - fusion/concept
  - fusion/physics
  - fusion/risks
status: stable
confidence: high
related:
  - "[[h-mode]]"
  - "[[iter]]"
  - "[[isotope-effect]]"
  - "[[31-plasma-physics-deeper-cuts]]"
created: 2026-08-26
updated: 2026-08-26
---
The bifurcation into [[h-mode]], and a genuine unretired design risk for [[iter]].

## The scaling used for design

The ITPA **Martin 2008** law:

```
P_L-H = 0.0488 · ⟨n_e,20⟩^0.717 · B_tor^0.803 · S^0.941 · (2/A_eff)
```

S is plasma surface area, A_eff effective isotope mass.

## The problem

Experimental observations from multiple devices show **significant departures from Martin08**, which the literature states plainly *undermines confidence in the predicted power threshold for ITER*.

This matters concretely. ITER's installed heating is finite — 33 MW [[neutral-beam-injection|NBI]] plus 20 MW ICRH plus 20 MW ECRH. If the real threshold exceeds prediction sufficiently, **ITER may struggle to access H-mode in some planned scenarios** — and H-mode underpins the entire Q = 10 case.

## Complications

- **[[isotope-effect]]** — threshold scales roughly inversely with isotope mass, so hydrogen is worst. ITER's early campaigns run H and D precisely to avoid activation.
- **Grad-B drift direction** relative to the X-point changes the threshold by roughly a factor of two, for reasons not fully explained.
- Hidden parameters: wall conditioning state, divertor geometry, neutral density, error fields, rotation.

Below threshold, plasmas show **limit-cycle oscillations** — turbulence and zonal-flow shearing competing without locking.
