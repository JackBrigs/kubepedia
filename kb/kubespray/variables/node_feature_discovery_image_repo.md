---
id: VARIABLE-NODE_FEATURE_DISCOVERY_IMAGE_REPO
type: variable
title: node_feature_discovery_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - node_feature_discovery_image_repo
tags:
  - nfd
  - download
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image repository for the Node Feature Discovery container"
relations: []
---

# node_feature_discovery_image_repo

## Summary
Container image repository for Node Feature Discovery (NFD). Default: `{{ kube_image_repo }}/nfd/node-feature-discovery`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
node_feature_discovery_image_repo: "{{ kube_image_repo }}/nfd/node-feature-discovery"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray range: `>=v2.29.0 <=v2.31.0`. Depends on `kube_image_repo`. Paired with `node_feature_discovery_image_tag` and `node_feature_discovery_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
