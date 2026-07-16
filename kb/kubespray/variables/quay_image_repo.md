---
id: VARIABLE-QUAY_IMAGE_REPO
type: variable
title: quay_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - quay_image_repo
tags:
  - download
  - registry
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Base registry host for quay.io-hosted container images"
relations: []
---

# quay_image_repo

## Summary
Hostname of the Quay container registry used as the source prefix for images that Kubespray pulls from quay.io. Defaults to `quay.io`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
quay_image_repo: "quay.io"
```

Unchanged across v2.29.0-v2.31.0 (line 97 in v2.29.0/v2.29.1, line 99 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Used as a prefix by numerous image-repo variables in the same download defaults file; override to point at a mirror of quay.io.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
