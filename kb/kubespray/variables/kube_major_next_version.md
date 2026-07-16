---
id: VARIABLE-KUBE_MAJOR_NEXT_VERSION
type: variable
title: kube_major_next_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_major_next_version
tags:
  - versioning
  - internal
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/main.yml
    note: "Computed next Kubernetes minor version string; 1.{{ kube_next }}"
relations: []
---

# kube_major_next_version

## Summary
Internal computed variable holding the next Kubernetes minor version string (e.g. for `kube_version` 1.31.x it yields `1.32`). Used by version-manipulation tooling during upgrades.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/main.yml` (line 7) as a computed expression:

```yaml
kube_next: "{{ ((kube_version | split('.'))[1] | int) + 1 }}"
kube_major_next_version: "1.{{ kube_next }}"
```

It depends on `kube_version` and the helper `kube_next`. The expression is unchanged across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0–v2.31.0. Internal variable (in `vars/`, not `defaults/`) — not intended for user override. Related: `kube_major_version`, `kube_version`.

## References
- roles/kubespray_defaults/vars/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
