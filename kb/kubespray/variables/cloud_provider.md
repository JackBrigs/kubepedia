---
id: VARIABLE-CLOUD_PROVIDER
type: variable
title: cloud_provider
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cloud_provider
tags:
  - cloud-provider
  - kubelet
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Cloud provider selector, empty string by default"
relations: []
---

# cloud_provider

## Summary
Selects the Kubernetes cloud provider integration. Defaults to an empty string (`""`), meaning no cloud provider is configured.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
cloud_provider: ""
```

The empty-string default is unchanged across v2.29.0-v2.31.0 (line 313 in v2.29.0/v2.29.1, 314 in v2.30.0, 326 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. When left empty, no external/in-tree cloud provider integration is enabled.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
