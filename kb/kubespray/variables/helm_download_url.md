---
id: VARIABLE-HELM_DOWNLOAD_URL
type: variable
title: helm_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - helm_download_url
tags:
  - helm
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Full URL of the Helm archive to download"
relations: []
---

# helm_download_url

## Summary
The full download URL for the Helm release archive. It is composed from the `get_helm_url` base, `helm_version`, and the active `image_arch`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
helm_download_url: "{{ get_helm_url }}/helm-v{{ helm_version }}-linux-{{ image_arch }}.tar.gz"
```

The computed expression is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `get_helm_url`, `helm_version`, `image_arch`, `helm_archive_checksum`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
