---
id: VARIABLE-KUBEADM_USE_FILE_DISCOVERY
type: variable
title: kubeadm_use_file_discovery
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_use_file_discovery
tags:
  - kubeadm
  - discovery
  - security
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines kubeadm_use_file_discovery defaulting to remove_anonymous_access"
relations: []
---

# kubeadm_use_file_discovery

## Summary
Enables kubeadm file-based discovery when node joins, used when anonymous access has been removed. Defaults to the value of `remove_anonymous_access`.

## Implementation
Defined identically in two files:

```yaml
kubeadm_use_file_discovery: "{{ remove_anonymous_access }}"
```

- `roles/kubernetes/control-plane/defaults/main/main.yml` (line 252 in v2.29.0/v2.29.1, line 259 in v2.30.0/v2.31.0)
- `roles/kubernetes/kubeadm/defaults/main.yml` (line 8 in all four tags)

Both definitions are unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. `remove_anonymous_access` defaults to `false`.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related variable: `remove_anonymous_access`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- roles/kubernetes/kubeadm/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
