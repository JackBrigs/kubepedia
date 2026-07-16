---
id: VARIABLE-CNI_DOWNLOAD_URL
type: variable
title: cni_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cni_download_url
tags:
  - cni
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Download URL for the CNI plugins archive"
relations:
  - type: see_also
    target: COMPONENT-CNI_PLUGINS
---

# cni_download_url

## Summary
Full download URL for the CNI plugins archive (`cni-plugins-linux-<arch>-v<version>.tgz`), built from the GitHub URL base, architecture, and CNI version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cni_download_url: "{{ github_url }}/containernetworking/plugins/releases/download/v{{ cni_version }}/cni-plugins-linux-{{ image_arch }}-v{{ cni_version }}.tgz"
```

This computed expression is unchanged across v2.29.0-v2.31.0 (line 158 in v2.29.0, 160 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Depends on `github_url`, `cni_version`, and `image_arch`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
