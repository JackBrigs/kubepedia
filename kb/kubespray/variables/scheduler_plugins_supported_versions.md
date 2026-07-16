---
id: VARIABLE-SCHEDULER_PLUGINS_SUPPORTED_VERSIONS
type: variable
title: scheduler_plugins_supported_versions
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - scheduler_plugins_supported_versions
tags:
  - scheduler-plugins
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Maps Kubernetes major versions to scheduler-plugins versions"
relations: []
---

# scheduler_plugins_supported_versions

## Summary
Map of Kubernetes major version to the supported scheduler-plugins version. Used to resolve `scheduler_plugins_version` by `kube_major_version`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
scheduler_plugins_supported_versions:
  '1.31': 0
  '1.30': 0
  '1.29': 0
```

The map is unchanged across v2.29.0-v2.31.0 (line 135 in v2.29.0, 137 in v2.29.1/v2.30.0/v2.31.0). A preceding comment notes "Scheduler plugins doesn't build for K8s 1.29 yet".

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `scheduler_plugins_version` via `scheduler_plugins_supported_versions[kube_major_version]`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
