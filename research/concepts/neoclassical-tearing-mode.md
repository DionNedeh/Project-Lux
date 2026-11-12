---
title: "Neoclassical Tearing Mode (NTM)"
type: concept
domain: physics
tags:
  - fusion/concept
  - fusion/physics
status: stable
confidence: high
related:
  - "[[safety-factor]]"
  - "[[bootstrap-current]]"
  - "[[gyrotron]]"
  - "[[16-heating-current-drive-fuelling]]"
created: 2026-08-26
updated: 2026-08-26
---
A self-reinforcing magnetic island at a rational [[safety-factor|q]] surface — typically q = 2 or 3/2.

**The loop:** an island flattens the pressure profile inside itself → the local [[bootstrap-current]] disappears → the missing current makes the island grow → the island flattens more pressure.

NTMs **degrade confinement significantly and can trigger [[disruption|disruptions]]**.

## The fix, and why ECRH earns its cost

Deposit **electron cyclotron current drive precisely inside the island**, replacing the missing bootstrap current. This requires real-time island detection, real-time steerable mirrors, and modulation synchronised to island rotation.

It works, and it is standard practice on [[asdex-upgrade]], [[diii-d]] and [[tcv]]. It is also the clearest demonstration of why [[gyrotron|ECRH]]'s extreme spatial localisation — deposition widths of a few centimetres in a metres-wide plasma — is worth the expense of megawatt millimetre-wave sources.

**Sawtooth crashes seed NTMs**, which is why sawtooth *pacing* (keeping crashes small and frequent) matters more than sawtooth suppression.
