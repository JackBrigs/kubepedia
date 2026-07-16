---
id: VARIABLE-FIRST_KUBE_CONTROL_PLANE_ADDRESS
type: variable
title: first_kube_control_plane_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - first_kube_control_plane_address
tags:
  - control-plane
  - inventory
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Computed access IP of the first host in the kube_control_plane group"
relations: []
---

# first_kube_control_plane_address

## Summary
Computed variable holding the access IP address of the first node in the `kube_control_plane` group. Value: `{{ hostvars[groups['kube_control_plane'][0]]['main_access_ip'] }}`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
first_kube_control_plane_address: "{{ hostvars[groups['kube_control_plane'][0]]['main_access_ip'] }}"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line numbers 639, 639, 642, 661 respectively).

## Compatibility
Kubespray v2.29.0–v2.31.0. Related: `first_kube_control_plane` (introduced in v2.30.0), `main_access_ip`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
