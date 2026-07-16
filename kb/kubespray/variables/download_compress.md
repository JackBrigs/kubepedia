---
id: VARIABLE-DOWNLOAD_COMPRESS
type: variable
title: download_compress
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - download_compress
tags:
  - download
  - compression
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Default download_compress: 1"
relations:
  - type: see_also
    target: TAG-DOWNLOAD
---

# download_compress

## Summary
Compression level used when caching/transferring downloaded artifacts in `download_run_once` mode. Default compress level is `1` (fastest).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `download_compress: 1`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant with `download_run_once`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
