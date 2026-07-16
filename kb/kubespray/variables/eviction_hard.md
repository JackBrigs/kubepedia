---
id: VARIABLE-EVICTION_HARD
type: variable
title: eviction_hard
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - eviction_hard
tags:
  - kubelet
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Kubelet hard eviction thresholds for worker nodes; default empty map {}"
relations: []
---

# eviction_hard

## Summary
Kubelet hard eviction thresholds applied to (non control-plane) nodes. Default is an empty map `{}`, meaning no custom hard eviction thresholds are set by Kubespray.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `eviction_hard: {}` (line 58). The value `{}` is unchanged across v2.29.0-v2.31.0 (same file and line in all four tags).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related to `eviction_hard_control_plane`, which sets the equivalent thresholds for control-plane nodes.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
