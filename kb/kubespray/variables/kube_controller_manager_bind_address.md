---
id: VARIABLE-KUBE_CONTROLLER_MANAGER_BIND_ADDRESS
type: variable
title: kube_controller_manager_bind_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_controller_manager_bind_address
tags:
  - controller-manager
  - networking
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Bind address for kube-controller-manager; default \"::\""
relations: []
---

# kube_controller_manager_bind_address

## Summary
Sets the bind address for kube-controller-manager. Default is `"::"` (all IPv6/IPv4 interfaces).

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kube_controller_manager_bind_address: "::"
```

The value `"::"` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related to `kube_controller_feature_gates`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
