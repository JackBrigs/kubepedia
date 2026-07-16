---
id: VARIABLE-DOWNLOAD_KEEP_REMOTE_CACHE
type: variable
title: download_keep_remote_cache
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - download_keep_remote_cache
tags:
  - download
  - cache
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Default download_keep_remote_cache: false"
relations:
  - type: see_also
    target: TAG-DOWNLOAD
---

# download_keep_remote_cache

## Summary
When `false` (default), remote cache files are deleted after use. Setting it to `true` keeps them, which per the code comment is only really useful when developing Kubespray.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `download_keep_remote_cache: false`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `download_cache_dir`, `download_force_cache`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
