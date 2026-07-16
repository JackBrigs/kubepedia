---
id: VARIABLE-KUBE_RESERVED_CGROUPS_FOR_SERVICE_SLICE
type: variable
title: kube_reserved_cgroups_for_service_slice
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_reserved_cgroups_for_service_slice
tags:
  - kubelet
  - cgroups
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kube_reserved_cgroups_for_service_slice with default kube.slice"
relations: []
---

# kube_reserved_cgroups_for_service_slice

## Summary
Name of the systemd slice used for kube resource reservation cgroups. Default is `kube.slice`. Feeds the `kube_reserved_cgroups` path and kubelet cgroup pre-start directories.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_reserved_cgroups_for_service_slice: kube.slice
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 45 in v2.29.0-v2.30.0, line 44 in v2.31.0). Consumed in `roles/kubernetes/node/templates/kubelet.service.j2` (cgroup mkdir ExecStartPre lines) and by `kube_reserved_cgroups`. The sample inventory carries a commented `# kube_reserved_cgroups_for_service_slice: kube.slice` example.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related to `kube_reserved` and `kube_reserved_cgroups`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
