---
id: VARIABLE-KUBELET_KUBELET_CGROUPS_CGROUPFS
type: variable
title: kubelet_kubelet_cgroups_cgroupfs
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_kubelet_cgroups_cgroupfs
tags:
  - kubelet
  - cgroups
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines the kubelet cgroup path used when the cgroupfs cgroup driver is selected; default /system.slice/kubelet.service"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_kubelet_cgroups_cgroupfs

## Summary
Sets the cgroup that the kubelet process itself is placed into when the `cgroupfs` cgroup driver is used. Default is `/system.slice/kubelet.service`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` (line 22):

```yaml
kubelet_kubelet_cgroups_cgroupfs: "/system.slice/kubelet.service"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Companion of `kubelet_runtime_cgroups_cgroupfs` (cgroupfs variant) and `kubelet_runtime_cgroups`; applies only when the cgroupfs driver is active.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
