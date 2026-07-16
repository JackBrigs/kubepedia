---
id: VARIABLE-EVICTION_HARD_CONTROL_PLANE
type: variable
title: eviction_hard_control_plane
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - eviction_hard_control_plane
tags:
  - kubelet
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Kubelet hard eviction thresholds for control-plane nodes; default empty map {}"
relations: []
---

# eviction_hard_control_plane

## Summary
Kubelet hard eviction thresholds applied to control-plane nodes. Default is an empty map `{}`, meaning Kubespray sets no custom hard eviction thresholds on control-plane nodes.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `eviction_hard_control_plane: {}` (line 59). The value `{}` is unchanged across v2.29.0-v2.31.0 (same file and line in all four tags).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Companion to `eviction_hard`, which sets the equivalent thresholds for worker nodes.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
