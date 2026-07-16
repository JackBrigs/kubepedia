---
id: VARIABLE-CRIO_ARCHIVE_CHECKSUM
type: variable
title: crio_archive_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crio_archive_checksum
tags:
  - download
  - cri-o
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "computed checksum looked up from crio_archive_checksums by arch and version"
relations: []
---

# crio_archive_checksum

## Summary

`crio_archive_checksum` is the expected checksum of the downloaded CRI-O archive.
It is not a literal value: it is looked up from the `crio_archive_checksums` map by
the current image architecture and the selected `crio_version`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
crio_archive_checksum: "{{ crio_archive_checksums[image_arch][crio_version] }}"
```

The expression is unchanged across v2.29.0-v2.31.0. The concrete checksum depends on
`image_arch` and on the resolved `crio_version`.

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: same computed expression.
- Related: `crio_archive_checksums`, `crio_version`, `image_arch`, `crio_download_url`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
