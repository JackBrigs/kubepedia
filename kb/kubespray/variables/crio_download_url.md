---
id: VARIABLE-CRIO_DOWNLOAD_URL
type: variable
title: crio_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crio_download_url
tags:
  - download
  - cri-o
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "computed URL for the CRI-O release archive"
relations: []
---

# crio_download_url

## Summary

`crio_download_url` is the URL from which the CRI-O container-runtime archive is
downloaded. It is a computed template built from the storage base URL, the image
architecture, and the selected `crio_version`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
crio_download_url: "{{ storage_googleapis_url }}/cri-o/artifacts/cri-o.{{ image_arch }}.v{{ crio_version }}.tar.gz"
```

The expression is unchanged across v2.29.0-v2.31.0. The resulting URL depends on
`storage_googleapis_url`, `image_arch`, and the resolved `crio_version`.

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: same computed expression.
- Related: `storage_googleapis_url`, `image_arch`, `crio_version`, `crio_archive_checksum`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
