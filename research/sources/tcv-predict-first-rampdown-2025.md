---
title: "Learning Plasma Dynamics and Robust Ramp-down Trajectories at TCV"
type: source
source_type: article
file: "raw/articles/tcv-predict-first-rampdown-2025.html"
authors: "Wang, A. M. et al."
publisher: "Nature Communications 16, 8877"
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
  - "[[tcv]]"
  - "[[disruption]]"
  - "[[availability]]"
created: 2026-08-26
updated: 2026-08-26
---
Wang and colleagues demonstrate a “predict-first” workflow for designing plasma-current ramp-down trajectories on [[tcv|TCV]]. A neural state-space dynamics model was trained on **311 prior pulses**, of which only **five** occupied the high-performance regime targeted by the experiments. Reinforcement learning searched that learned environment for trajectories intended to preserve operational margin while ending the discharge safely.

The work is unusually valuable because the policy was not left in simulation. The researchers executed the designed trajectories on TCV and reported statistically significant improvements in their ramp-down metrics, including a case that extrapolated plasma current **20% beyond the training data**. It is therefore live-machine evidence, not merely an offline replay.

The narrow evidence boundary remains important. This is controlled trajectory design for a short terminal phase on a research tokamak, supported by a limited dataset and a handful of high-performance examples. It does not demonstrate indefinite autonomous operation, fault-tolerant plant control, or transfer to a reactor-scale device. The model’s success also does not make extrapolation generically safe: the 20% result is one tested excursion inside one experimental workflow.

The paper nevertheless closes a crucial gap between simulator-trained control and physical validation. It shows how learned dynamics, optimisation and human-supervised experimental execution can form a testable loop. [[40-ai-for-fusion-transferable-control|Document 40]] treats this as one of the strongest current examples of AI moving a real plasma rather than only classifying its historical data. DOI: **10.1038/s41467-025-63917-x**.
