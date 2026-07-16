---
id: VARIABLE-KUBE_RESERVED_CGROUPS
type: variable
title: kube_reserved_cgroups
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_reserved_cgroups
tags:
  - kubelet
  - cgroups
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_reserved_cgroups, computed from kube_reserved_cgroups_for_service_slice"
relations: []
---

# kube_reserved_cgroups

## Summary
Absolute cgroup path used for kube resource reservation. Computed default is `/{{ kube_reserved_cgroups_for_service_slice }}`, i.e. `/kube.slice` given the default slice.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` at line 41:

```yaml
kube_reserved_cgroups: "/{{ kube_reserved_cgroups_for_service_slice }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. It derives from `kube_reserved_cgroups_for_service_slice` (default `kube.slice`).

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Depends on `kube_reserved_cgroups_for_service_slice`; related to `kube_reserved`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
