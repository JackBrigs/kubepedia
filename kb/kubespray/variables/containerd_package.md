---
id: VARIABLE-CONTAINERD_PACKAGE
type: variable
title: containerd_package
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - containerd_package
tags:
  - container-engine
  - containerd-common
  - variable
sources:
  - type: code
    path: roles/container-engine/containerd-common/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd-common/defaults/main.yml
    note: "default: containerd.io"
relations: []
---
<!-- generated: variable-stub -->

# containerd_package

## Summary

Kubespray variable `containerd_package` — default `containerd.io`. Defined in `roles/container-engine/containerd-common/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/container-engine/containerd-common/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
containerd_package: containerd.io
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/container-engine/containerd-common/defaults/main.yml` (Kubespray `v2.31.0`).
