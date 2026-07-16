---
id: VARIABLE-KUBE_CPU_RESERVED
type: variable
title: kube_cpu_reserved
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_cpu_reserved
tags:
  - kubelet
  - node
  - resource-reservation
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kubelet kube-reserved CPU; default 100m"
relations: []
---

# kube_cpu_reserved

## Summary
CPU reserved for Kubernetes system daemons (kubelet `kube-reserved`). Default: `100m`. The sample inventory shows commented example overrides of `100m` for nodes and `200m` for control-plane hosts (`kube_control_plane.yml`), but those are commented out and the effective default is `100m`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_cpu_reserved: "100m"`. Commented example values appear in `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` (`100m`) and `inventory/sample/group_vars/k8s_cluster/kube_control_plane.yml` (`200m`), both disabled by default. The role default `"100m"` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related: `kube_ephemeral_storage_reserved`, `kube_memory_reserved`.

## References
- roles/kubernetes/node/defaults/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
