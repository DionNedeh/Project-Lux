---
title: "FusionMAE: Self-supervised Pretraining for Fusion Diagnostics and Control"
type: source
source_type: article
file: "raw/articles/fusionmae-crossref-metadata-2026.json"
authors: "Yang, Z. et al."
publisher: "Communications Physics 9, 232"
source_date: 2026-05-01
ingested: 2026-08-26
tags:
  - fusion/source
  - fusion/computation
  - fusion/operations
status: stable
confidence: medium
related:
  - "[[40-ai-for-fusion-transferable-control]]"
  - "[[tokamak]]"
  - "[[disruption]]"
  - "[[burn-control]]"
created: 2026-08-26
updated: 2026-08-26
---
FusionMAE is a masked-autoencoder model intended to learn reusable representations from heterogeneous tokamak diagnostics rather than training one model for each downstream task. Yang and colleagues report pretraining on **2,445 HL-3 discharges from four campaigns spanning 2022–2025**. During pretraining, portions of diagnostic signals are hidden and the model learns to reconstruct them; the resulting representation is then evaluated on diagnostic and control-related tasks.

The contribution is architectural and evidential. Fusion datasets are expensive, irregular and device-specific, while many labelled events are scarce. Self-supervised reconstruction can exploit unlabelled operational history and can tolerate incomplete diagnostic channels. That makes the work relevant to missing-signal reconstruction, state estimation and models that share a common representation across tasks.

The demonstrated result is still **offline model evaluation on experimental data**, not autonomous reactor control. The paper does not establish safe closed-loop operation, transfer to another tokamak, calibrated uncertainty outside its training distribution or long-duration power-plant reliability. In [[40-ai-for-fusion-transferable-control|Document 40]], it therefore sits below live-machine control and above a purely conceptual foundation-model proposal.

> [!warning] Capture limitation
> The raw file is Crossref bibliographic metadata because the publisher blocked automated full-text capture. The dataset and result summary were checked against the named primary article page (DOI **10.1038/s42005-026-02626-3**), but the local raw record does not reproduce the article text. Confidence is therefore medium for detailed findings and high for identity, authorship, venue and DOI.
