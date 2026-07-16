---
id: VARIABLE-KUBELET_PROTECT_KERNEL_DEFAULTS
type: variable
title: kubelet_protect_kernel_defaults
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_protect_kernel_defaults
tags:
  - kubelet
  - hardening
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Controls kubelet protectKernelDefaults; defaults to true"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_protect_kernel_defaults

## Summary
Controls kubelet `protectKernelDefaults`. When true, kubelet errors out rather than modifying kernel sysctl values that differ from its expected defaults. Defaults to `true`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kubelet_protect_kernel_defaults: true
```

The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 591 in v2.29.0, line 611 in v2.31.0). It is also referenced by the hardening docs and hardening CI inventory, both consistent with the `true` default.

## Compatibility
Kubespray v2.29.0 through v2.31.0.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
