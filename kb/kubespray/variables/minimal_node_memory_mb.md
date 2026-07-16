---
id: VARIABLE-MINIMAL_NODE_MEMORY_MB
type: variable
title: minimal_node_memory_mb
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - minimal_node_memory_mb
tags:
  - preinstall
  - preflight
  - node
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Minimum RAM (MB) required on worker nodes for preflight check"
relations: []
---

# minimal_node_memory_mb

## Summary
Minimum amount of RAM (in MB) required on worker nodes, enforced by the preinstall preflight memory check. Default is `1024`.

## Implementation
Defined as a role default in `roles/kubernetes/preinstall/defaults/main.yml` with value `minimal_node_memory_mb: 1024`. The default is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `minimal_master_memory_mb`, which sets the equivalent threshold for control-plane nodes.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
