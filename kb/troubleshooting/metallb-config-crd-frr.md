---
id: TROUBLE-METALLB_CONFIG_CRD_FRR
type: troubleshooting
title: "MetalLB: config ignored (ConfigMap→CRD) / FRR mode"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.13.0 <=0.16.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - metallb configmap ignored
  - metallb no ip assigned
  - metallb ipaddresspool crd
  - metallb frr mode
tags:
  - troubleshooting
  - metallb
  - networking
  - loadbalancer
  - upgrade
sources:
  - type: docs
    path: MetalLB configuration (CRDs)
    url: https://metallb.universe.tf/configuration/
    note: "ConfigMap config removed since 0.13; IPAddressPool/L2Advertisement/BGPAdvertisement CRs"
relations:
  - type: see_also
    target: COMPONENT-METALLB
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# MetalLB: config ignored (ConfigMap→CRD) / FRR mode

## Summary

A `LoadBalancer` Service gets **no external IP** and MetalLB seems to ignore your
configuration. On MetalLB **0.13+** the legacy **ConfigMap-based config was removed** — you
must use the CRDs (`IPAddressPool`, `L2Advertisement`, `BGPAdvertisement`). The base ships
**0.13.9**; the horizon is **0.16.1**.

## Problem

- `LoadBalancer` Services stay `<pending>` (no IP assigned).
- A `config` ConfigMap is present but has no effect.
- BGP sessions don't come up after choosing the FRR implementation.

## Context

- Applies to MetalLB **0.13.0–0.16.1** (base: 0.13.9 — [[COMPONENT-METALLB]]).

## Diagnostics

- **The ConfigMap config is gone (since 0.13):** define an **`IPAddressPool`** plus an
  **`L2Advertisement`** (layer2) or **`BGPAdvertisement`** (BGP) CR. A leftover `config`
  ConfigMap is silently ignored.
- No pool covering the Service's needs → no IP. Check the controller logs and that the pool's
  address range is valid and not exhausted.
- **FRR mode:** MetalLB offers an FRR-based BGP implementation (and the newer `FRR-K8s`
  mode) as an alternative to the native speaker — the deployment mode must match your CRs and
  is selected at install; a mismatch breaks BGP advertisement.

## Known Issues

- Across 0.13→0.16, validate the CR set and the chosen BGP mode after upgrade; confirm exact
  per-release changes against the MetalLB release notes for your target patch.

## References

- MetalLB configuration docs (above); component: [[COMPONENT-METALLB]]; horizon:
  [[CONCEPT-UPGRADE_HORIZON]].
