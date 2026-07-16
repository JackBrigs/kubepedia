---
id: VARIABLE-NRI_ENABLED
type: variable
title: nri_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nri_enabled
tags:
  - cri
  - containerd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Enables the Node Resource Interface (NRI); computed from container_manager"
relations: []
---

# nri_enabled

## Summary
Enables the Node Resource Interface (NRI) plugin API in the container runtime. Defaults to true when the container runtime is containerd, otherwise false.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as the computed expression `nri_enabled: "{{ container_manager == 'containerd' }}"`. The expression is unchanged across v2.29.0-v2.31.0 (only the line number shifts: 328 in v2.29.0/v2.29.1, 329 in v2.30.0, 341 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Effective default depends on `container_manager`. Docs (`docs/CRI/containerd.md`, `docs/CRI/cri-o.md`) show setting `nri_enabled: true` explicitly. Related: `container_manager`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
