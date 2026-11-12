---
title: "Explainable Tokamak-agnostic ELM Forecasting"
type: source
source_type: article
file: "raw/articles/tokamak-agnostic-elm-crossref-metadata-2026.json"
authors: "Joung, S. et al."
publisher: "Communications Physics"
source_date: 2026-06-01
ingested: 2026-08-26
tags:
  - fusion/source
  - fusion/computation
  - fusion/physics
status: stable
confidence: medium
related:
  - "[[40-ai-for-fusion-transferable-control]]"
  - "[[diii-d]]"
  - "[[kstar]]"
  - "[[elm]]"
created: 2026-08-26
updated: 2026-08-26
---
This study tests whether an instability forecaster learned on one tokamak can remain useful on another. Joung and colleagues trained a neural network on megahertz turbulent-fluctuation measurements from [[diii-d|DIII-D]], then applied its weights to [[kstar|KSTAR]] after physics-consistent preprocessing. The reported zero-shot result forecasts Type-I [[elm|edge-localised-mode]] onset without retraining the network on KSTAR labels.

The important distinction is between **portability of a forecasting representation** and universal machine independence. The authors also compare saliency features with independently calculated instability growth rates, stability limits and pedestal evolution. That explainability check matters because a model can otherwise appear transferable while exploiting machine- or diagnostic-specific artefacts.

The demonstration covers one source–target pair, one instability family and a common measurement class. It is not closed-loop ELM suppression, does not prove portability to every tokamak, and does not remove the need for device-specific calibration and safety validation. “Tokamak-agnostic” is therefore the paper’s tested framing, not a licence to describe the model as universally device-independent.

For Project Lux, this is stronger evidence for cross-device generalisation than the earlier device-specific disruption and control examples, but it remains at the **forecasting** rung of the control-evidence ladder in [[40-ai-for-fusion-transferable-control|Document 40]].

> [!warning] Capture limitation
> The raw file is Crossref bibliographic metadata because the publisher blocked automated full-text capture. Findings were checked on the named primary article page (DOI **10.1038/s42005-026-02689-2**); detailed-result confidence is medium, while bibliographic confidence is high.
