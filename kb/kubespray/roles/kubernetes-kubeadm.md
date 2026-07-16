---
id: ROLE-KUBERNETES_KUBEADM
type: role
title: kubernetes/kubeadm
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubernetes/kubeadm
tags:
  - role
sources:
  - type: code
    path: roles/kubernetes/kubeadm
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/kubernetes/kubeadm
    note: "kubernetes/kubeadm role"
relations:
  - type: see_also
    target: TAG-KUBEADM
---

# kubernetes/kubeadm

## Summary

Performs the node-side kubeadm step: bootstraps each node into the cluster (kubeadm join / kubelet bootstrap) so API server, kubelet and CNI can come up.

## Implementation

Task files under `roles/kubernetes/kubeadm/tasks/`. Invoked from the playbooks under the
corresponding run-tag (see [[TAG-KUBEADM]]).

## Configuration

Driven by variables in `roles/kubespray_defaults` (see [[ROLE-KUBESPRAY_DEFAULTS]]) and the role's own `defaults/`.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.

## References

- `roles/kubernetes/kubeadm/` (tag `v2.31.0` `1c9add4`).
