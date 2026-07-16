---
id: VARIABLE-SCHEDULER_PLUGINS_VERSION
type: variable
title: scheduler_plugins_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - scheduler_plugins_version
tags:
  - scheduler-plugins
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Resolves the scheduler-plugins version for the current Kubernetes major version"
relations: []
---

# scheduler_plugins_version

## Summary
The scheduler-plugins version selected for the cluster's Kubernetes major version. Computed as `"{{ scheduler_plugins_supported_versions[kube_major_version] }}"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
scheduler_plugins_version: "{{ scheduler_plugins_supported_versions[kube_major_version] }}"
```

The expression is unchanged across v2.29.0-v2.31.0 (line 139 in v2.29.0, 141 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Looks up `scheduler_plugins_supported_versions` by `kube_major_version`; feeds `scheduler_plugins_scheduler_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
