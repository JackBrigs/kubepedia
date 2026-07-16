---
id: VARIABLE-CONTAINERD_DOWNLOAD_URL
type: variable
title: containerd_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_download_url
tags:
  - containerd
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computes the containerd release archive download URL"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_download_url

## Summary
The URL from which the containerd release archive is downloaded. It is composed from the GitHub mirror base, the containerd version, and the architecture, and inserts `static-` when a static binary is requested.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
containerd_download_url: "{{ github_url }}/containerd/containerd/releases/download/v{{ containerd_version }}/containerd-{{ 'static-' if containerd_static_binary }}{{ containerd_version }}-linux-{{ image_arch }}.tar.gz"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only line numbers shift).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related: `github_url`, `containerd_version`, `containerd_static_binary`, `image_arch`, `containerd_checksum`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
