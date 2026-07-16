---
id: VARIABLE-GCR_IMAGE_REPO
type: variable
title: gcr_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gcr_image_repo
tags:
  - images
  - registry
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Base hostname of the Google Container Registry used to build image references; default gcr.io"
relations: []
---

# gcr_image_repo

## Summary
Base registry hostname for images pulled from Google Container Registry. Used as a building block when composing full image references. Default value is `gcr.io`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
gcr_image_repo: "gcr.io"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Override it (typically together with the other `*_image_repo` variables) to redirect image pulls to a mirror or private registry.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
