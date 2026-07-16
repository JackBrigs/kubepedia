---
id: VARIABLE-KUBE_LOG_LEVEL
type: variable
title: kube_log_level
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_log_level
tags:
  - logging
  - control-plane
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Log verbosity level (-v) for Kubernetes components; default 2"
relations: []
---

# kube_log_level

## Summary
Log verbosity level (the `-v` flag) applied to Kubernetes components. Default: `2`.

## Implementation
Defined as the role default in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_log_level: 2
```

Also surfaced to users in the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` with the same value `2`. The role default takes precedence per project rules; both agree here. Unchanged across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0–v2.31.0. Higher values increase verbosity of component logs.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
