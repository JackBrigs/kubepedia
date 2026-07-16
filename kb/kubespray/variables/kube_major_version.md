---
id: VARIABLE-KUBE_MAJOR_VERSION
type: variable
title: kube_major_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_major_version
tags:
  - versioning
  - internal
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/main.yml
    note: "Computed Kubernetes major.minor version derived from kube_version"
relations: []
---

# kube_major_version

## Summary
Internal computed variable holding the Kubernetes major.minor version derived from `kube_version` (e.g. `1.17.4` -> `1.17`). Used throughout version-dependent lookups.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/main.yml` (line 5) as a computed expression:

```yaml
kube_major_version: "{{ (kube_version | split('.'))[:-1] | join('.') }}"
```

It strips the patch component from `kube_version`. The expression is unchanged across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0–v2.31.0. Internal variable (in `vars/`, not `defaults/`) — not intended for user override. Related: `kube_major_next_version`, `kube_version`.

## References
- roles/kubespray_defaults/vars/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
