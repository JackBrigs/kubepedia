---
id: VARIABLE-METALLB_SPEAKER_ENABLED
type: variable
title: metallb_speaker_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - metallb_speaker_enabled
tags:
  - metallb
  - addons
sources:
  - type: code
    path: roles/kubernetes-apps/metallb/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/metallb/defaults/main.yml
    note: "Defines metallb_speaker_enabled default (mirrors metallb_enabled)"
relations: []
---

# metallb_speaker_enabled

## Summary
Toggles deployment of the MetalLB speaker component (used for L2/BGP address advertisement). Default is the computed expression `{{ metallb_enabled }}`, so the speaker follows whether MetalLB itself is enabled.

## Implementation
Defined in `roles/kubernetes-apps/metallb/defaults/main.yml` as `metallb_speaker_enabled: "{{ metallb_enabled }}"`, and mirrored identically in `roles/kubespray_defaults/defaults/main/main.yml` and the sample inventory `inventory/sample/group_vars/k8s_cluster/addons.yml`. Expression unchanged across v2.29.0–v2.31.0 (role default line 6 in v2.29.x, line 7 in v2.30.0/v2.31.0; kubespray_defaults main.yml 463 → 464 → 471; addons.yml 148 → 111).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Derives from `metallb_enabled`. Related variables: `metallb_speaker_image_repo`, `metallb_version`.

## References
- roles/kubernetes-apps/metallb/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/addons.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
