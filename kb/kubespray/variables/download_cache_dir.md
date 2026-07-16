---
id: VARIABLE-DOWNLOAD_CACHE_DIR
type: variable
title: download_cache_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - download_cache_dir
tags:
  - download
  - cache
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Default download_cache_dir: /tmp/kubespray_cache"
relations:
  - type: see_also
    target: TAG-DOWNLOAD
---

# download_cache_dir

## Summary
Filesystem path used as the local cache directory for downloaded files and images. Default: `/tmp/kubespray_cache`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `download_cache_dir: /tmp/kubespray_cache`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `local_release_dir`, `download_keep_remote_cache`, `download_force_cache`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
