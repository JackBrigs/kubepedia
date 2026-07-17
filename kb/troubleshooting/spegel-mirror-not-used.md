---
id: TROUBLE-SPEGEL_MIRROR_NOT_USED
type: troubleshooting
title: "Spegel: image pulls not served by the mirror"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.0.1 <=0.7.4"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - spegel mirror not used
  - spegel images still pulled from registry
  - spegel certs.d containerd
  - spegel eks 1.34 transfer service
tags:
  - troubleshooting
  - spegel
  - registry
  - containerd
sources:
  - type: docs
    path: spegel getting-started
    url: https://spegel.dev/docs/getting-started/
    note: "containerd requirements: certs.d config_path, discard_unpacked_layers=false"
  - type: docs
    path: spegel issue #1272
    url: https://github.com/spegel-org/spegel/issues/1272
    note: "EKS 1.34 + containerd 2.1 transfer service bypasses hosts.toml"
relations:
  - type: see_also
    target: CONCEPT-ADDON_SPEGEL
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# Spegel: image pulls not served by the mirror

## Summary

Spegel is installed but nodes still pull every image from the upstream registry — the P2P
mirror isn't used. Almost always a **containerd configuration** gap, or (on newer setups) the
containerd **transfer service** bypassing `hosts.toml`.

## Problem

- Image pulls hit the external registry despite Spegel running; no P2P traffic between nodes.
- Registry-outage doesn't fall back to peers as expected.

## Context

- Applies across Spegel **0.0.1–0.7.4** (owner pins 0.0.1; current 0.7.4 —
  [[CONCEPT-ADDON_SPEGEL]]). Spegel gates on **containerd**, not the K8s version.

## Diagnostics

- containerd must have **`config_path = "/etc/containerd/certs.d"`** set and
  **`discard_unpacked_layers = false`** — Spegel does **not** write these; set them and
  **restart containerd**. On GKE, apply the containerd config manually.
- **Newer setups (e.g. EKS 1.34 + containerd 2.1):** the containerd **transfer service**
  bypasses `hosts.toml`, so mirrors are not consulted (#1272) — a known limitation.
- Current Spegel dropped containerd 1.7/2.0 support (needs **containerd 2.1+**); the pinned
  **0.0.1** targets older containerd, so verify the actual image against the node's containerd.

## Known Issues

- Huge version gap (0.0.1 → 0.7.4): upgrading brings the containerd-2.1 requirement and config
  changes — validate `certs.d` and `discard_unpacked_layers` after any bump.

## References

- spegel getting-started + issue #1272 (above); addon: [[CONCEPT-ADDON_SPEGEL]]; horizon:
  [[CONCEPT-UPGRADE_HORIZON]].
