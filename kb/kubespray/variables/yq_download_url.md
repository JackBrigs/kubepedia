---
id: VARIABLE-YQ_DOWNLOAD_URL
type: variable
title: yq_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - yq_download_url
tags:
  - yq
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed download URL for the yq linux binary."
relations: []
---

# yq_download_url

## Summary
The URL from which the yq binary is downloaded. It is a computed default built from `github_url`, `yq_version`, and `image_arch`, pointing at the mikefarah/yq GitHub release asset for the Linux binary of the matching architecture.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

`yq_download_url: "{{ github_url }}/mikefarah/yq/releases/download/v{{ yq_version }}/yq_linux_{{ image_arch }}"`

The expression is unchanged across v2.29.0-v2.31.0 (line 176 in v2.29.0; line 178 in v2.29.1/v2.30.0/v2.31.0). The concrete URL varies only through the resolved `yq_version` and `image_arch`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `github_url`, `yq_version`, `image_arch`, `yq_binary_checksum`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
