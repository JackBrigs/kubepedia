---
id: VARIABLE-DOWNLOAD_ALWAYS_PULL
type: variable
title: download_always_pull
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - download_always_pull
tags:
  - download
  - images
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Default download_always_pull: false"
relations:
  - type: see_also
    target: TAG-DOWNLOAD
---

# download_always_pull

## Summary
Controls image pull behaviour during downloads. When set to `true`, container images are always pulled; otherwise Kubespray checks by the repository's tag/digest before pulling. Default: `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `download_always_pull: false`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the download role defaults; related to `download_container`, `download_force_cache`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
