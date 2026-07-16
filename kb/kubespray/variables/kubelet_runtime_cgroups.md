---
id: VARIABLE-KUBELET_RUNTIME_CGROUPS
type: variable
title: kubelet_runtime_cgroups
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_runtime_cgroups
tags:
  - kubelet
  - cgroups
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Cgroup for the container runtime service under the systemd cgroup driver"
relations: []
---

# kubelet_runtime_cgroups

## Summary
The cgroup kubelet assigns to the container runtime, used when systemd is the cgroup driver (the default). Computed as `/<kube_service_cgroups>/<container_manager>.service`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` (line 17):

```yaml
kubelet_runtime_cgroups: "/{{ kube_service_cgroups }}/{{ container_manager }}.service"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. When the cgroup driver is `cgroupfs`, `roles/kubernetes/node/tasks/facts.yml` overrides it with `kubelet_runtime_cgroups_cgroupfs`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `kube_service_cgroups` and `container_manager`. Related: `kubelet_runtime_cgroups_cgroupfs`, `kubelet_kubelet_cgroups`.

## References
- roles/kubernetes/node/defaults/main.yml
- roles/kubernetes/node/tasks/facts.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
