---
id: VARIABLE-KUBE_VERSION_MIN_REQUIRED
type: variable
title: kube_version_min_required
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_version_min_required
tags:
  - validation
  - kubernetes-version
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Computed minimum supported Kubernetes version, derived from kubelet_checksums"
relations: []
---

# kube_version_min_required

## Summary
Minimum Kubernetes version supported by the current Kubespray release. It is computed from the oldest entry in the `kubelet_checksums` map, and is used by inventory validation to reject a `kube_version` older than the supported floor.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a computed expression (not a literal):

```yaml
kube_version_min_required: "{{ (kubelet_checksums['amd64'] | dict2items)[-1].key }}"
```

It takes the last key of the amd64 `kubelet_checksums` dict (the lowest version present). It is consumed in `roles/validate_inventory/tasks/main.yml`, whose failure message reads: "The current release of Kubespray only support newer version of Kubernetes than {{ kube_version_min_required }} - You are trying to apply {{ kube_version }}". The expression and path are unchanged across v2.29.0-v2.31.0 (line 28 in v2.29.0/v2.29.1/v2.30.0, line 31 in v2.31.0).

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Derived from `kubelet_checksums`; consumed by the `validate_inventory` role to gate `kube_version`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/validate_inventory/tasks/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
