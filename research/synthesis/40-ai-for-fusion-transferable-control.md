---
title: "AI for Fusion: From Device-Specific Models to Transferable Control"
type: synthesis
doc: 40
part: 4
aliases:
  - "AI for Fusion"
  - "Transferable Fusion Control"
tags:
  - fusion/synthesis
  - fusion/computation
  - fusion/operations
created: 2026-08-26
updated: 2026-08-26
status: stable
confidence: high
related:
  - "[[01-fusion-physics-fundamentals]]"
  - "[[17-diagnostics-control-disruption]]"
  - "[[19-simulation-codes-nuclear-data]]"
  - "[[31-plasma-physics-deeper-cuts]]"
  - "[[fusionmae-crossref-metadata-2026]]"
  - "[[tokamak-agnostic-elm-crossref-metadata-2026]]"
  - "[[tcv-predict-first-rampdown-2025]]"
  - "[[hl3-data-driven-rl-control-2025]]"
---
# 40 — AI for Fusion: From Device-Specific Models to Transferable Control

*Project Lux · What machine learning has demonstrated, what still belongs to simulation, and what a reactor-grade assurance case would require*

---

## 1. The change is not “AI arrives in fusion”

Machine learning was already present in disruption prediction, equilibrium reconstruction, diagnostic interpretation, surrogate modelling and control before the 2025–26 results reviewed here. The meaningful change is narrower and more important: researchers are trying to escape the **one machine, one diagnostic, one task** pattern.

Four recent demonstrations map that transition. [[fusionmae-crossref-metadata-2026|FusionMAE]] learns a reusable representation from 2,445 HL-3 discharges. [[tokamak-agnostic-elm-crossref-metadata-2026|Tokamak-agnostic ELM forecasting]] transfers a DIII-D-trained predictor to KSTAR without retraining its weights. [[tcv-predict-first-rampdown-2025|TCV predict-first control]] uses learned dynamics and reinforcement learning to design trajectories that were then executed on the machine. [[hl3-data-driven-rl-control-2025|HL-3 data-driven control]] trains in a learned simulator and runs a 1 kHz controller on an experiment.

None is an autonomous fusion power plant. Together, however, they reveal a credible engineering stack: self-supervised representation learning, physics-aware transfer, learned simulation, constrained optimisation and live experimental validation. The question is no longer whether neural models can fit fusion data. It is whether their useful behaviour can survive changes of campaign, diagnostic, machine and operating regime without outrunning the evidence.

## 2. An evidence ladder for fusion AI

“AI controlled a plasma” compresses distinct claims. A useful ladder is:

1. **Offline description:** reconstruct a state, classify an event or fit archived data.
2. **Offline prediction:** forecast an event on held-out discharges from the same machine.
3. **Cross-campaign prediction:** remain accurate after hardware, calibration or regime changes.
4. **Cross-machine transfer:** preserve useful performance on another device.
5. **Simulator-trained policy:** choose actions in a physics-based or learned environment.
6. **Live advisory use:** recommend actions while operators retain execution authority.
7. **Bounded live control:** issue commands inside a defined envelope with independent protection.
8. **Integrated plant control:** coordinate plasma, magnets, fuel cycle, heat removal and protection over reactor-relevant missions.

The four new sources occupy different rungs. FusionMAE is principally offline representation learning. The ELM work demonstrates cross-machine forecasting for one source–target pair. TCV and HL-3 reach bounded live control. No source reaches integrated plant control, and no reported value of [[q-gain-definitions|Q]]—whether (Q_{sci}), (Q_{target}), (Q_{wp}) or (Q_{eng})—is altered by these control results.

This ladder prevents two symmetrical errors. The first is dismissing every neural result because it is not a power plant. The second is treating any actuator command as autonomy. A bounded experiment can be an important technical result without proving the operational assurance needed for a commercial machine.

## 3. From labels to representations

Fusion datasets are simultaneously abundant and scarce. A large tokamak can produce dense time series from many diagnostics, but labelled examples of the events that matter most—rare disruptions, unusual transitions, component faults—may be few. Campaign changes alter calibrations and operating space. Different devices measure related physics with different instruments and sampling conventions.

FusionMAE addresses the labelling problem through masked reconstruction. Portions of diagnostic sequences are hidden and the model learns to infer them from the remaining context. According to [[fusionmae-crossref-metadata-2026]], the pretraining corpus contains **2,445 HL-3 discharges across four campaigns from 2022 to 2025**. The number is reported by Yang and colleagues; it is not a count independently reconstructed by Project Lux.

The promise is a common representation that downstream tools can reuse for missing-signal recovery, state estimation and control-related tasks. That resembles a foundation-model strategy, but the analogy should be held tightly. A language model’s transferable units are not equivalent to plasma variables, and a representation trained on one facility may encode its diagnostic layout as readily as its physics. The decisive tests are ablations across campaigns, missing sensors, regime boundaries and other devices—not parameter count or the word “pretrained”.

## 4. Transfer must be physical, not merely statistical

The ELM study provides a sharper transfer test. A network learned from megahertz turbulence measurements on [[diii-d|DIII-D]] forecasts Type-I [[elm|ELM]] onset on [[kstar|KSTAR]] with zero-shot weight transfer after physics-consistent preprocessing. The authors compare salient model features with independently calculated growth rates, stability boundaries and [[pedestal|pedestal]] evolution.

This matters because ordinary cross-validation can reward the wrong invariances. A model may recognise a diagnostic artefact, a campaign timestamp or a controller signature rather than an instability precursor. Applying it to another tokamak removes some shortcuts. Checking saliency against physics removes others.

Yet “tokamak-agnostic” remains bounded by the experiment. Two machines are not the entire tokamak class. DIII-D and KSTAR share important operating concepts; a spherical tokamak, stellarator or burning-plasma device presents different geometry, actuation and distributions. The demonstrated claim is **one zero-shot source–target transfer for ELM forecasting**, not universal portability and not ELM suppression.

For reactor programmes, the practical lesson is to build transfer tests into procurement and validation. A vendor should specify which changes a model tolerates: new campaign, recalibrated sensor, missing channel, new plasma shape, new wall material or new machine. “Generalises” without that axis is not an engineering requirement.

## 5. Learned simulators change how control is developed

Reinforcement learning usually improves through exploration. A tokamak cannot safely supply arbitrary exploratory actions, and machine time is too scarce to use as a training loop. Learned dynamics models offer a bridge: train a surrogate from experimental history, search for a policy inside it, then validate under bounded conditions.

The HL-3 work reports a **400 ms trajectory at 1 kHz** on the physical machine and adaptation of triangularity without retraining, according to [[hl3-data-driven-rl-control-2025]]. TCV’s predict-first workflow trained on **311 pulses**, with only **five high-performance examples**, then executed optimised ramp-downs on the machine. Wang and colleagues report statistically significant metric improvements and a tested plasma-current extrapolation of **20% beyond the training data**.

These are demonstrations, not designs or announcements. Their limits are equally concrete. Four hundred milliseconds is not a plant duty cycle. Five high-performance pulses are a sparse basis for rare-state assurance. A 20% extrapolation that succeeded once is not evidence that extrapolation is generally safe. The learned simulator is a component with its own failure modes: biased historical data, unobserved state, actuator lag, non-stationary walls and confident predictions outside its training support.

The correct architecture therefore does not replace physics models, transport codes or deterministic protection with one neural policy. It combines them. A learned surrogate can generate candidate actions; reduced physics models can reject impossible states; uncertainty estimates can shrink the permitted envelope; and an independent machine-protection system can always veto commands.

## 6. Control is larger than the plasma

A power plant must coordinate plasma shape, current and density with magnets, cryogenics, fuelling, impurity control, exhaust, tritium accountancy, thermal storage and turbine constraints. A plasma-optimal action can be plant-suboptimal. For example, preserving confinement while increasing transient load on the [[divertor]] may improve a short experimental objective and reduce component life.

That makes objective design a safety issue. Reward functions must encode hard constraints, not merely average performance. The controller should expose which constraints are active and what uncertainty accompanies its forecast. Operators need a degraded mode when diagnostics disappear, and investigators need reproducible logs linking each command to model version, input state and protection decision. [[31-plasma-physics-deeper-cuts|Document 31]]’s validation requirements apply directly: a model that cannot be traced through data, software, test and configuration history is not certifiable plant equipment.

Data governance is also physical governance. Training data should record calibration, machine configuration, wall condition and intervention history. Otherwise similar-looking signals can describe different systems. FAIR access and common schemas help research, but reactor operators will also need cybersecurity boundaries and controls on model updates. Continuous online learning is scientifically attractive and operationally dangerous if an unreviewed update can change safety-significant behaviour.

## 7. The assurance case

A reactor-grade AI control function would need evidence in at least six dimensions:

- **Envelope:** explicit states, machines and failure modes for which the model is authorised.
- **Uncertainty:** calibrated warnings that rise under distribution shift rather than remaining confidently wrong.
- **Independence:** deterministic protection and shutdown channels outside the learned controller.
- **Traceability:** immutable data, model and configuration provenance for every deployed version.
- **Adversarial testing:** sensor loss, bias, latency, actuator saturation and physically plausible rare events.
- **Progressive authority:** offline replay, shadow mode, advisory operation and bounded control before wider actuation.

Performance should be compared with conventional baselines, not with doing nothing. A neural controller earns authority only where it improves a declared metric without weakening protection, maintainability or interpretability. Where a simple controller is adequate, complexity is a liability.

## 8. What is now defensible

As of 26 August 2026, the evidence supports four conclusions.

First, machine learning has moved beyond retrospective classification into **bounded live control** on experimental tokamaks. Second, self-supervised learning can exploit thousands of unlabelled discharges and multiple campaigns, although device transfer remains unproven for FusionMAE. Third, one ELM study demonstrates meaningful zero-shot transfer from DIII-D to KSTAR, but not universal tokamak independence. Fourth, learned simulators can reduce the amount of dangerous or expensive exploration performed on the real machine, but their uncertainty must be part of the controller rather than an afterthought.

The radical improvement is not to install a general-purpose “fusion AI”. It is to build an assurance architecture in which transferable representations, physics constraints, learned simulators, independent protection and experimental evidence accumulate separately. That is slower to describe than autonomy, but much closer to how control becomes dependable.
