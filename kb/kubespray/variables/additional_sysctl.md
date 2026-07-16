---
id: VARIABLE-ADDITIONAL_SYSCTL
type: variable
title: additional_sysctl
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - additional_sysctl
tags:
  - kernel
  - sysctl
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines additional_sysctl: [] (list of extra sysctl name/value pairs)"
relations: []
---

# additional_sysctl

## Summary
List of additional Linux kernel sysctl parameters to apply to cluster nodes. Default is an empty list `[]`, meaning no extra sysctl tunables are set. Each entry is a `{ name: ..., value: ... }` mapping.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `additional_sysctl: []`. A commented example above the definition shows the expected structure:
```yaml
# additional_sysctl:
#  - { name: kernel.pid_max, value: 131072 }
```
The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `kubelet_protect_kernel_defaults` (kernel tunable handling).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
