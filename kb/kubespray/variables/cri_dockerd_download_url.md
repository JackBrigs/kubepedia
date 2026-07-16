---
id: VARIABLE-CRI_DOCKERD_DOWNLOAD_URL
type: variable
title: cri_dockerd_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cri_dockerd_download_url
tags:
  - cri-dockerd
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "URL of the cri-dockerd release archive on GitHub"
relations: []
---

# cri_dockerd_download_url

## Summary
The URL from which Kubespray downloads the cri-dockerd release archive
(Mirantis/cri-dockerd). Built from the configured `github_url` mirror, the
cri-dockerd version, and the target architecture.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as the same
computed expression across all four tags:

```yaml
cri_dockerd_download_url: "{{ github_url }}/Mirantis/cri-dockerd/releases/download/v{{ cri_dockerd_version }}/cri-dockerd-{{ cri_dockerd_version }}.{{ image_arch }}.tgz"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `github_url`,
`cri_dockerd_version`, and `image_arch`. Relevant when `container_manager` is
`docker` (cri-dockerd).

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
