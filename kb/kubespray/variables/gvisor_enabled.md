---
id: VARIABLE-GVISOR_ENABLED
type: variable
title: gvisor_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gvisor_enabled
tags:
  - gvisor
  - runtime
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggle for installing/configuring the gVisor (runsc) container runtime; default false"
relations: []
---

# gvisor_enabled

## Summary
Boolean toggle controlling whether the gVisor (runsc) sandboxed container runtime is installed and configured. Default value is `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
gvisor_enabled: false
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0. (Molecule test scenarios under `roles/container-engine/gvisor/molecule/` set it to `true`, but that is test-only override, not the shipped default.)

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. When set to true it activates the gVisor download/checksum variables (`gvisor_version`, `gvisor_runsc_*`, `gvisor_containerd_shim_*`).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
