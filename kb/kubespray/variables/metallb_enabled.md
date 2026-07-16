---
id: VARIABLE-METALLB_ENABLED
type: variable
title: metallb_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - metallb_enabled
tags:
  - metallb
  - addons
sources:
  - type: code
    path: roles/kubernetes-apps/metallb/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/metallb/defaults/main.yml
    note: "Defines default metallb_enabled: false"
relations: []
---

# metallb_enabled

## Summary
Toggles deployment of the MetalLB load-balancer addon. Default is `false`, so MetalLB is not installed unless explicitly enabled.

## Implementation
Defined in `roles/kubernetes-apps/metallb/defaults/main.yml` (line 2) as `metallb_enabled: false`, and mirrored (also `false`) in `roles/kubespray_defaults/defaults/main/main.yml` and the sample inventory `inventory/sample/group_vars/k8s_cluster/addons.yml`. Value is unchanged across v2.29.0–v2.31.0 (line shifts: kubespray_defaults main.yml 462 → 463 → 470; addons.yml 147 → 110).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Drives `metallb_speaker_enabled` (defaults to `{{ metallb_enabled }}`). Related variables: `metallb_version`, `metallb_controller_image_repo`, `metallb_speaker_image_repo`.

## References
- roles/kubernetes-apps/metallb/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/addons.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
