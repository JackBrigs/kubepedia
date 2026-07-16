---
id: VARIABLE-NODE_FEATURE_DISCOVERY_IMAGE_TAG
type: variable
title: node_feature_discovery_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - node_feature_discovery_image_tag
tags:
  - nfd
  - download
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag for the Node Feature Discovery container, derived from the version variable"
relations: []
---

# node_feature_discovery_image_tag

## Summary
Container image tag for Node Feature Discovery (NFD). It is derived from `node_feature_discovery_version`, prefixed with `v`. Default expression: `v{{ node_feature_discovery_version }}`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
node_feature_discovery_image_tag: "v{{ node_feature_discovery_version }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Since `node_feature_discovery_version` is `0.16.4` in all four tags, the resolved tag is `v0.16.4`.

## Compatibility
Kubespray range: `>=v2.29.0 <=v2.31.0`. Depends on `node_feature_discovery_version`. Paired with `node_feature_discovery_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
