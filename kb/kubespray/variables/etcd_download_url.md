---
id: VARIABLE-ETCD_DOWNLOAD_URL
type: variable
title: etcd_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_download_url
tags:
  - etcd
  - download
  - url
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Download URL template for the etcd release tarball"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_download_url

## Summary
URL template for downloading the etcd release tarball from GitHub, parameterized by `github_url`, `etcd_version`, and `image_arch`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `etcd_download_url: "{{ github_url }}/etcd-io/etcd/releases/download/v{{ etcd_version }}/etcd-v{{ etcd_version }}-linux-{{ image_arch }}.tar.gz"` (line 157 in v2.29.0, line 159 in v2.29.1/v2.30.0/v2.31.0). The expression is **unchanged across v2.29.0-v2.31.0**; only the line number shifted.

## Compatibility
Kubespray v2.29.0-v2.31.0. Uses `github_url`, `etcd_version`, `image_arch`. Related: `etcd_binary_checksums` (verifies the downloaded tarball), `etcd_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
