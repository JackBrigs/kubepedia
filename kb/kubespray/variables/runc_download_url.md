---
id: VARIABLE-RUNC_DOWNLOAD_URL
type: variable
title: runc_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - runc_download_url
tags:
  - runc
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Constructs the runc binary download URL"
relations: []
---

# runc_download_url

## Summary
The URL from which the runc binary is downloaded. Built from `github_url`, the runc version, and the target architecture.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:
`runc_download_url: "{{ github_url }}/opencontainers/runc/releases/download/v{{ runc_version }}/runc.{{ image_arch }}"`.
The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Present in Kubespray >=v2.29.0 <=v2.31.0. Depends on `github_url`, `runc_version`, and `image_arch`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
