---
id: VARIABLE-DOWNLOAD_RETRIES
type: variable
title: download_retries
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - download_retries
tags:
  - download
  - retries
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Default download_retries: 4"
relations: []
---

# download_retries

## Summary
Number of download retry attempts for files and containers. Default: `4`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `download_retries: 4`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies to both file and container downloads.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
