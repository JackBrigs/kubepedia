---
id: VARIABLE-KUBE_NEXT
type: variable
title: kube_next
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_next
tags:
  - kubernetes
  - versioning
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/main.yml
    note: "Computes the next Kubernetes minor version number from kube_version"
relations: []
---

# kube_next

## Summary
Internal computed variable equal to the next Kubernetes minor version number (the current minor plus one). It is derived from `kube_version` and used internally for version-comparison logic. Not intended to be set by users.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/main.yml` (a `vars/` file, so it is a computed constant rather than an overridable default):

```yaml
kube_next: "{{ ((kube_version | split('.'))[1] | int) + 1 }}"
```

It takes the second dotted component of `kube_version` (the minor version), converts it to an integer, and adds one. The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `kube_version`. Being in `vars/` it takes precedence over role defaults and is not meant to be overridden.

## References
- roles/kubespray_defaults/vars/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
