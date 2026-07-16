---
id: VARIABLE-CRICTL_DOWNLOAD_URL
type: variable
title: crictl_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crictl_download_url
tags:
  - crictl
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "URL of the crictl (cri-tools) release archive on GitHub"
relations: []
---

# crictl_download_url

## Summary
The URL from which Kubespray downloads the crictl (cri-tools) release archive.
Built from the configured `github_url` mirror, the crictl version, the OS
(`ansible_system`), and the target architecture.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as the same
computed expression across all four tags:

```yaml
crictl_download_url: "{{ github_url }}/kubernetes-sigs/cri-tools/releases/download/v{{ crictl_version }}/crictl-v{{ crictl_version }}-{{ ansible_system | lower }}-{{ image_arch }}.tar.gz"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `github_url`,
`crictl_version`, `ansible_system`, and `image_arch`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
