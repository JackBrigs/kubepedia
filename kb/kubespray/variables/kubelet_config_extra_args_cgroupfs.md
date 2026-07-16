---
id: VARIABLE-KUBELET_CONFIG_EXTRA_ARGS_CGROUPFS
type: variable
title: kubelet_config_extra_args_cgroupfs
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_config_extra_args_cgroupfs
tags:
  - kubelet
  - cgroups
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Extra kubelet config settings applied when cgroupfs is the cgroup driver; default systemCgroups: /system.slice, cgroupRoot: /"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_config_extra_args_cgroupfs

## Summary
Additional kubelet configuration parameters that are applied when the cgroupfs cgroup driver is used. Its default is a two-key mapping: `systemCgroups: /system.slice` and `cgroupRoot: /`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as a mapping:

```yaml
kubelet_config_extra_args_cgroupfs:
  systemCgroups: /system.slice
  cgroupRoot: /
```

This default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts: 125 in v2.29.0/v2.29.1, 122 in v2.30.0, 124 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to the cgroupfs vs systemd cgroup driver selection and to `kubelet_kubelet_cgroups` / `kubelet_runtime_cgroups`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
