---
id: VARIABLE-FIRST_KUBE_CONTROL_PLANE
type: variable
title: first_kube_control_plane
status: active
kubespray_version: ">=v2.30.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - first_kube_control_plane
tags:
  - control-plane
  - inventory
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Computed name of the first host in the kube_control_plane group"
relations: []
---

# first_kube_control_plane

## Summary
Computed variable holding the inventory hostname of the first node in the `kube_control_plane` group. Value: `{{ groups['kube_control_plane'] | first }}`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
first_kube_control_plane: "{{ groups['kube_control_plane'] | first }}"
```

This variable is NOT present in v2.29.0 or v2.29.1; it was introduced in v2.30.0. The value is identical in v2.30.0 (line 637) and v2.31.0 (line 656).

## Compatibility
Kubespray v2.30.0–v2.31.0 (not defined in v2.29.0/v2.29.1). Related: `first_kube_control_plane_address`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
