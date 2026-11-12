---
title: "Runaway Electrons"
type: concept
domain: physics
tags:
  - fusion/concept
  - fusion/physics
  - fusion/risks
status: stable
confidence: high
sources:
  - "[[runaway-electron-generation-iter-mitigated-disruptions-2026]]"
related:
  - "[[disruption]]"
  - "[[shattered-pellet-injection]]"
  - "[[iter]]"
  - "[[17-diagnostics-control-disruption]]"
created: 2026-08-26
updated: 2026-08-26
---
In a sufficiently hot plasma, drag on an electron *decreases* with energy above a threshold. An electron past that threshold accelerates freely — it runs away. Worse, a runaway can knock a thermal electron into the runaway population: **avalanche multiplication scaling exponentially with plasma current**.

A multi-megaampere, multi-MeV electron beam striking the first wall deposits its energy centimetres deep in a localised volume, melting and potentially perforating components.

> [!warning] The result that should be more widely known
> Current modelling with the **DREAM** framework finds **megaampere-scale runaway currents in 15 MA [[iter]] discharges even in non-activated scenarios**. With staggered [[shattered-pellet-injection]] outperforming single-stage injection, **no cases with acceptable runaway currents were found for a D-T plasma.**

The reason D-T is worse is intrinsic: **tritium beta decay and Compton scattering from activated structures continuously generate runaway seeds**. Unlike hot-tail seeds these cannot be removed by cooling the plasma faster — and every seed feeds the avalanche.

Approaches under investigation: post-thermal-quench SPI for seed depletion, passive 3D coils that deliberately destroy the flux surfaces the beam needs, and operating in regimes where disruptions are less likely.

**As of August 2026 ITER's disruption mitigation has no demonstrated solution for its full-current D-T scenario.** A concrete unsolved problem on the critical path of the world's largest fusion project.
