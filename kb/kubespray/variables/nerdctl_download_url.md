---
id: VARIABLE-NERDCTL_DOWNLOAD_URL
type: variable
title: nerdctl_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nerdctl_download_url
tags:
  - nerdctl
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed download URL for the nerdctl release archive"
relations: []
---

# nerdctl_download_url

## Summary
Computed URL from which the nerdctl release archive is downloaded, built from the GitHub base URL, nerdctl version, host OS, and CPU architecture.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

`nerdctl_download_url: "{{ github_url }}/containerd/nerdctl/releases/download/v{{ nerdctl_version }}/nerdctl-{{ nerdctl_version }}-{{ ansible_system | lower }}-{{ image_arch }}.tar.gz"`

The expression is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `github_url`, `nerdctl_version`, `ansible_system`, and `image_arch`; the downloaded archive is verified against `nerdctl_archive_checksum`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
