---
id: VARIABLE-KUBE_EPHEMERAL_STORAGE_RESERVED
type: variable
title: kube_ephemeral_storage_reserved
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_ephemeral_storage_reserved
tags:
  - kubelet
  - node
  - resource-reservation
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kubelet kube-reserved ephemeral-storage; default 500Mi"
relations: []
---

# kube_ephemeral_storage_reserved

## Summary
Ephemeral storage reserved for Kubernetes system daemons (kubelet `kube-reserved`). Default: `500Mi`. The sample inventory shows commented example overrides of `2Gi` for both nodes and control-plane hosts, but those are disabled and the effective default is `500Mi`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_ephemeral_storage_reserved: "500Mi"`. Commented example values of `2Gi` appear in `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` and `inventory/sample/group_vars/k8s_cluster/kube_control_plane.yml`, both disabled by default. The role default `"500Mi"` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related: `kube_cpu_reserved`, `kube_memory_reserved`.

## References
- roles/kubernetes/node/defaults/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
