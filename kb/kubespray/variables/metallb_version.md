---
id: VARIABLE-METALLB_VERSION
type: variable
title: metallb_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - metallb_version
tags:
  - metallb
  - version
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the MetalLB version (0.13.9)"
relations:
  - type: see_also
    target: COMPONENT-METALLB
---

# metallb_version

## Summary
Version of MetalLB deployed by Kubespray. Default is `0.13.9`. It feeds the shared image tag (`v{{ metallb_version }}`).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `metallb_version: 0.13.9`. The value is unchanged across v2.29.0–v2.31.0 (only line numbers shift: 383 → 385 → 386 → 368).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Consumed by `metallb_image_tag`. Related variables: `metallb_controller_image_repo`, `metallb_speaker_image_repo`, `metallb_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
