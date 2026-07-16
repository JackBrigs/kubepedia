---
id: VARIABLE-METALLB_SPEAKER_IMAGE_REPO
type: variable
title: metallb_speaker_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - metallb_speaker_image_repo
tags:
  - metallb
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the MetalLB speaker container image repository"
relations: []
---

# metallb_speaker_image_repo

## Summary
Container image repository for the MetalLB speaker component. Default is the computed expression `{{ quay_image_repo }}/metallb/speaker`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `metallb_speaker_image_repo: "{{ quay_image_repo }}/metallb/speaker"`. The expression is unchanged across v2.29.0–v2.31.0 (only line numbers shift: 381 → 383 → 384 → 366).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Derives from `quay_image_repo`. Related variables: `metallb_controller_image_repo`, `metallb_image_tag`, `metallb_speaker_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
