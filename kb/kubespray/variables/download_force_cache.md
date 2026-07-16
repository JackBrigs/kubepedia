---
id: VARIABLE-DOWNLOAD_FORCE_CACHE
type: variable
title: download_force_cache
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - download_force_cache
tags:
  - download
  - cache
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Default download_force_cache: false"
relations:
  - type: see_also
    target: TAG-DOWNLOAD
---

# download_force_cache

## Summary
Only useful when `download_run_once` is false: locally cached files and images are uploaded to Kubernetes nodes, and images downloaded on those nodes are copied back to the Ansible runner's cache if not already present. Default: `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `download_force_cache: false`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `download_run_once`, `download_cache_dir`, `download_keep_remote_cache`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
