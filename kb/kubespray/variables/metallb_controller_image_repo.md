---
id: VARIABLE-METALLB_CONTROLLER_IMAGE_REPO
type: variable
title: metallb_controller_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - metallb_controller_image_repo
tags:
  - metallb
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the MetalLB controller container image repository"
relations:
  - type: see_also
    target: COMPONENT-METALLB
---

# metallb_controller_image_repo

## Summary
Container image repository for the MetalLB controller component. Default is the computed expression `{{ quay_image_repo }}/metallb/controller`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `metallb_controller_image_repo: "{{ quay_image_repo }}/metallb/controller"`. The expression is unchanged across v2.29.0–v2.31.0 (only line numbers shift: 382 → 384 → 385 → 367).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Derives from `quay_image_repo`. Related variables: `metallb_speaker_image_repo`, `metallb_image_tag`, `metallb_version`, `metallb_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
