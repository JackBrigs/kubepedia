---
id: VARIABLE-CONTAINERD_MIN_VERSION_REQUIRED
type: variable
title: containerd_min_version_required
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_min_version_required
tags:
  - containerd
  - preflight
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/main.yml
    note: "Minimum containerd version enforced by preflight checks; default \"1.3.7\""
relations: []
---

# containerd_min_version_required

## Summary
Defines the minimum containerd version accepted by Kubespray preflight/validation. Default is `"1.3.7"`.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/main.yml`:

```yaml
containerd_min_version_required: "1.3.7"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. This is a vars-level constant (not a user-facing default), used to validate the effective containerd version.

## References
- roles/kubespray_defaults/vars/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
