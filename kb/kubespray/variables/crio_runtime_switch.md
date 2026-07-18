---
id: VARIABLE-CRIO_RUNTIME_SWITCH
type: variable
title: crio_runtime_switch
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - crio_runtime_switch
tags:
  - container-engine
  - cri-o
  - variable
sources:
  - type: code
    path: roles/container-engine/cri-o/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/cri-o/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# crio_runtime_switch

## Summary

Kubespray variable `crio_runtime_switch` — default `false`. Defined in `roles/container-engine/cri-o/defaults/main.yml`. Present in Kubespray
`v2.29.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/container-engine/cri-o/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
crio_runtime_switch: false
```

## Compatibility

Present in the Kubespray tags `v2.29.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/container-engine/cri-o/defaults/main.yml` (Kubespray `v2.31.0`).
