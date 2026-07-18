---
id: VARIABLE-ENABLE_DUAL_STACK_NETWORKS
type: variable
title: enable_dual_stack_networks
status: active
kubespray_version: ">=v2.27.0 <=v2.27.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - enable_dual_stack_networks
tags:
  - kubespray-defaults
  - variable
sources:
  - type: code
    path: roles/kubespray-defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.27.1/roles/kubespray-defaults/defaults/main/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# enable_dual_stack_networks

## Summary

Kubespray variable `enable_dual_stack_networks` — default `false`. Defined in `roles/kubespray-defaults/defaults/main/main.yml`. Present in Kubespray
`v2.27.0`–`v2.27.1` of the indexed range. **Removed after `v2.27.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubespray-defaults/defaults/main/main.yml` (Kubespray `v2.27.1`):

```yaml
enable_dual_stack_networks: false
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.27.1`. **Removed after `v2.27.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubespray-defaults/defaults/main/main.yml` (Kubespray `v2.27.1`).
