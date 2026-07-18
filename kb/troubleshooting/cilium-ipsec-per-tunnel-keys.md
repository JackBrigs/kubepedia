---
id: TROUBLE-CILIUM_IPSEC_PER_TUNNEL_KEYS
type: troubleshooting
title: "Cilium IPsec breaks on upgrade — single-key removed, per-tunnel keys mandatory (1.16 dep., 1.17 removed)"
status: active
kubespray_version: ">=v2.28.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.17.3 <=1.19.3"
verified_at: "2026-07-18"
confidence: confirmed
aliases:
  - cilium ipsec single key removed
  - cilium ipsec per-tunnel keys
  - ipsec secret plus sign cilium
  - cilium ipsec upgrade drops
  - cilium 1.17 ipsec key
tags:
  - cilium
  - troubleshooting
  - ipsec
  - upgrade
sources:
  - type: docs
    path: Documentation/operations/upgrade.rst
    url: https://github.com/cilium/cilium/blob/v1.17.3/Documentation/operations/upgrade.rst
    note: "1.16 makes per-tunnel keys mandatory (require + in secret); 1.17 removes single-key support entirely"
relations:
  - type: see_also
    target: CONCEPT-CILIUM_ENCRYPTION
  - type: see_also
    target: UPGRADE-CILIUM_1_15_TO_1_19
  - type: see_also
    target: TROUBLE-CILIUM_IPSEC_HOST_ROUTING_CVE
---

# Cilium IPsec breaks on upgrade — single-key removed, per-tunnel keys mandatory (1.16 dep., 1.17 removed)

## Summary

Cilium tightened IPsec key handling across the range: **per-tunnel keys became mandatory in 1.16**
(the IPsec secret must contain a `+` so keys are derived per node pair), and **single-key support was
removed entirely in 1.17**. A cluster whose `cilium-ipsec-keys` secret was created for single-key mode
loses encrypted connectivity when Kubespray moves Cilium to **1.17.3 (v2.28.0)** unless the secret is
in the per-tunnel format.

## Problem

- After the Kubespray v2.27.0 → v2.28.0 upgrade (Cilium 1.15→1.17), IPsec-encrypted pod traffic
  **drops** / nodes can't establish encrypted tunnels.
- The `cilium-ipsec-keys` secret is in the old single-key format (no `+`), which 1.17 no longer accepts.

## Context

- Applies to Cilium **1.16+** (mandatory) / **1.17+** (single-key removed) → Kubespray **v2.28.0+**
  ([[CONCEPT-CILIUM_ENCRYPTION]], [[UPGRADE-CILIUM_1_15_TO_1_19]]). Because Kubespray v2.27.0→v2.28.0
  crosses **both** 1.16 and 1.17, the deprecation and removal land in one jump.
- Per-tunnel keys derive a distinct key per node pair (better security/rotation); the secret format
  encodes this with the `+` marker in the key spec (`upgrade.rst`@v1.16.19/@v1.17.3).

## Diagnostics

- Inspect the secret: `kubectl -n kube-system get secret cilium-ipsec-keys -o jsonpath='{.data.keys}' | base64 -d`
  — a single-key entry without `+` is the old format.
- `cilium encrypt status` / agent logs show IPsec state and key errors.
- Hubble/`cilium monitor` shows encrypted-path drops after the upgrade.

## Known Issues

- **Fix:** recreate the `cilium-ipsec-keys` secret in the **per-tunnel** format (include the `+` so
  keys are per node pair) **before** the v2.27.0 → v2.28.0 upgrade, following the current IPsec key
  format ([[CONCEPT-CILIUM_ENCRYPTION]]). Rotate keys via the documented IPsec key-rotation procedure.
- **Also note (1.17→1.18):** the IPsec upgrade needs special attention and, on GKE, firewall rules must
  allow **ESP** — plan IPsec upgrades carefully across the whole range.
- **1.19 kernel caveat:** IPsec + KPR + BPF masquerade auto-enables eBPF host routing needing a kernel
  fix — [[TROUBLE-CILIUM_IPSEC_HOST_ROUTING_CVE]].

## References

- Cilium `Documentation/operations/upgrade.rst`@v1.16.19 / @v1.17.3 (per-tunnel keys mandatory /
  single-key removed). Encryption [[CONCEPT-CILIUM_ENCRYPTION]]; full jump
  [[UPGRADE-CILIUM_1_15_TO_1_19]]; 1.19 host-routing CVE [[TROUBLE-CILIUM_IPSEC_HOST_ROUTING_CVE]].
