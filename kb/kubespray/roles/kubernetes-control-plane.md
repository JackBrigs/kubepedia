---
id: ROLE-KUBERNETES_CONTROL_PLANE
type: role
title: kubernetes/control-plane
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubernetes/control-plane
tags:
  - role
sources:
  - type: code
    path: roles/kubernetes/control-plane
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/kubernetes/control-plane
    note: "kubernetes/control-plane role"
relations:
  - type: see_also
    target: TAG-CONTROL_PLANE
---

# kubernetes/control-plane

## Summary

Renders the kubeadm ClusterConfiguration (v1beta4) and runs kubeadm to bring up kube-apiserver, controller-manager and scheduler on the control plane.

## Implementation

Task files under `roles/kubernetes/control-plane/tasks/`. Invoked from the playbooks under the
corresponding run-tag (see [[TAG-CONTROL_PLANE]]).

## Configuration

Driven by variables in `roles/kubespray_defaults` (see [[ROLE-KUBESPRAY_DEFAULTS]]) and the role's own `defaults/`.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.

## References

- `roles/kubernetes/control-plane/` (tag `v2.31.0` `1c9add4`).
