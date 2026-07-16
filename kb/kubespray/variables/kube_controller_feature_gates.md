---
id: VARIABLE-KUBE_CONTROLLER_FEATURE_GATES
type: variable
title: kube_controller_feature_gates
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_controller_feature_gates
tags:
  - controller-manager
  - feature-gates
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Feature gates passed to kube-controller-manager; default empty list"
relations: []
---

# kube_controller_feature_gates

## Summary
List of feature gates passed to kube-controller-manager. Default is an empty list `[]`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_controller_feature_gates: []
```

The default empty list `[]` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related to `kube_controller_manager_bind_address` and other controller-manager tuning variables.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
