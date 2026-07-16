---
id: VARIABLE-KUBELET_RUNTIME_CGROUPS_CGROUPFS
type: variable
title: kubelet_runtime_cgroups_cgroupfs
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_runtime_cgroups_cgroupfs
tags:
  - kubelet
  - cgroups
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Runtime cgroup path used when the cgroupfs driver is selected; default /system.slice/{{ container_manager }}.service"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_runtime_cgroups_cgroupfs

## Summary
Sets the container-runtime cgroup path that kubelet uses when `cgroupfs` is the cgroup driver. Default is `"/system.slice/{{ container_manager }}.service"`, i.e. the systemd slice of the configured container runtime (containerd/crio/docker).

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kubelet_runtime_cgroups_cgroupfs: "/system.slice/{{ container_manager }}.service"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 21 in each tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when the cgroupfs driver is used (paired with `kubelet_kubelet_cgroups_cgroupfs`). Interpolates `container_manager`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
