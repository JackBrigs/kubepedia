---
id: VARIABLE-SKOPEO_DOWNLOAD_URL
type: variable
title: skopeo_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - skopeo_download_url
tags:
  - skopeo
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Constructs the download URL for the skopeo binary"
relations: []
---

# skopeo_download_url

## Summary
Download URL for the skopeo binary, built from the skopeo version and target architecture. Default `"{{ github_url }}/lework/skopeo-binary/releases/download/v{{ skopeo_version }}/skopeo-linux-{{ image_arch }}"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
skopeo_download_url: "{{ github_url }}/lework/skopeo-binary/releases/download/v{{ skopeo_version }}/skopeo-linux-{{ image_arch }}"
```

The expression is unchanged across v2.29.0-v2.31.0 (line 175 in v2.29.0, 177 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Interpolates `github_url`, `skopeo_version`, and `image_arch`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
