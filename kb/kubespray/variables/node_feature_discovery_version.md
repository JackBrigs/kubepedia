---
id: VARIABLE-NODE_FEATURE_DISCOVERY_VERSION
type: variable
title: node_feature_discovery_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - node_feature_discovery_version
tags:
  - nfd
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Version of the Node Feature Discovery component"
relations: []
---

# node_feature_discovery_version

## Summary
Version of the Node Feature Discovery (NFD) component deployed by Kubespray. Default: `0.16.4`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
node_feature_discovery_version: 0.16.4
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray range: `>=v2.29.0 <=v2.31.0`. Consumed by `node_feature_discovery_image_tag` (rendered as `v{{ node_feature_discovery_version }}`).

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
