---
id: VARIABLE-KUBE_PROXY_NODESELECTOR
type: variable
title: kube_proxy_nodeselector
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kube_proxy_nodeselector
tags:
  - win-nodes
  - kubernetes-patch
  - variable
sources:
  - type: code
    path: roles/win_nodes/kubernetes_patch/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/win_nodes/kubernetes_patch/defaults/main.yml
    note: "default: kubernetes.io/os"
relations: []
---
<!-- generated: variable-stub -->

# kube_proxy_nodeselector

## Summary

Kubespray variable `kube_proxy_nodeselector` — default `kubernetes.io/os`. Defined in `roles/win_nodes/kubernetes_patch/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/win_nodes/kubernetes_patch/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
kube_proxy_nodeselector: kubernetes.io/os
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/win_nodes/kubernetes_patch/defaults/main.yml` (Kubespray `v2.31.0`).
