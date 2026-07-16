---
id: VARIABLE-METALLB_IMAGE_TAG
type: variable
title: metallb_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - metallb_image_tag
tags:
  - metallb
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the MetalLB container image tag"
relations:
  - type: see_also
    target: COMPONENT-METALLB
---

# metallb_image_tag

## Summary
Container image tag shared by the MetalLB controller and speaker components. Default is the computed expression `v{{ metallb_version }}`, which resolves to `v0.13.9`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `metallb_image_tag: "v{{ metallb_version }}"`. The expression is unchanged across v2.29.0–v2.31.0 (only line numbers shift: 384 → 386 → 387 → 369). Since `metallb_version` is `0.13.9` in all four tags, it resolves to `v0.13.9`.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Derives from `metallb_version`. Related variables: `metallb_controller_image_repo`, `metallb_speaker_image_repo`, `metallb_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
