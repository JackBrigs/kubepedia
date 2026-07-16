---
id: VARIABLE-CRUN_DOWNLOAD_URL
type: variable
title: crun_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crun_download_url
tags:
  - download
  - crun
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "computed URL for the crun release binary from GitHub"
relations: []
---

# crun_download_url

## Summary

`crun_download_url` is the URL from which the crun runtime binary is downloaded. It
is a computed template built from the GitHub base URL, the selected `crun_version`,
and the image architecture.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
crun_download_url: "{{ github_url }}/containers/crun/releases/download/{{ crun_version }}/crun-{{ crun_version }}-linux-{{ image_arch }}"
```

The expression is unchanged across v2.29.0-v2.31.0. The resulting URL depends on
`github_url`, the resolved `crun_version`, and `image_arch`.

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: same computed expression.
- Related: `github_url`, `crun_version`, `image_arch`, `crun_binary_checksum`, `crun_enabled`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
