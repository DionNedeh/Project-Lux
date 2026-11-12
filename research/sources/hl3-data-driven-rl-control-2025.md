---
title: "Data-driven Dynamics and Reinforcement-learning Control on HL-3"
type: source
source_type: article
file: "raw/articles/hl3-data-driven-rl-control-2025.html"
authors: "Wu, N. et al."
publisher: "Communications Physics 8, 393"
source_date: 2025
ingested: 2026-08-26
tags:
  - fusion/source
  - fusion/computation
  - fusion/operations
status: stable
confidence: high
related:
  - "[[40-ai-for-fusion-transferable-control]]"
  - "[[tokamak]]"
  - "[[plasma-beta]]"
  - "[[safety-factor]]"
created: 2026-08-26
updated: 2026-08-26
---
Wu and colleagues use historical HL-3 data to learn a high-fidelity dynamics model, then train a reinforcement-learning controller inside that learned simulator. On the physical machine, the controller produced a **400 ms trajectory at a 1 kHz control rate** and adapted plasma triangularity without retraining.

This is a practical answer to a core constraint in fusion control: exploratory reinforcement learning cannot safely or economically learn through unconstrained trial and error on an operating tokamak. A learned surrogate can provide many simulated rollouts between scarce machine sessions, while a live experiment tests whether the resulting policy survives the simulator-to-machine gap.

The result is demonstrated real-time control over a bounded duration and operating envelope. It is not evidence of autonomous full-discharge management, reactor-scale availability, protection against every off-normal event or safe learning outside the training distribution. “High-fidelity” is the authors’ model characterisation, not proof that every relevant plant state is represented.

Together with the TCV predict-first work, the paper shows two related pathways: learn a dynamics model from machine history; then use that model to search for actions before exposing the device. [[40-ai-for-fusion-transferable-control|Document 40]] treats the learned simulator as an engineering component that must itself be validated, monitored for distribution shift and subordinated to deterministic machine-protection systems. DOI: **10.1038/s42005-025-02302-y**.
