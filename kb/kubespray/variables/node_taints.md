---
id: VARIABLE-NODE_TAINTS
type: variable
title: node_taints
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - node_taints
tags:
  - kubernetes
  - node-taint
  - variable
sources:
  - type: code
    path: roles/kubernetes/node-taint/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node-taint/defaults/main.yml
    note: "default: []"
relations: []
---
<!-- generated: variable-stub -->

# node_taints

## Summary

Kubespray variable `node_taints` — default `[]`. Defined in `roles/kubernetes/node-taint/defaults/main.yml`. Present in Kubespray
`v2.31.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes/node-taint/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
node_taints: []
```

## Compatibility

Present in the Kubespray tags `v2.31.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes/node-taint/defaults/main.yml` (Kubespray `v2.31.0`).
