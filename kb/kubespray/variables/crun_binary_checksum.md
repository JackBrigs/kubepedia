---
id: VARIABLE-CRUN_BINARY_CHECKSUM
type: variable
title: crun_binary_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crun_binary_checksum
tags:
  - download
  - crun
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "computed checksum looked up from crun_checksums by arch and version"
relations: []
---

# crun_binary_checksum

## Summary

`crun_binary_checksum` is the expected checksum of the downloaded crun binary. It is
not a literal value: it is looked up from the `crun_checksums` map by the current
image architecture and the selected `crun_version`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
crun_binary_checksum: "{{ crun_checksums[image_arch][crun_version] }}"
```

The expression is unchanged across v2.29.0-v2.31.0. The concrete checksum depends on
`image_arch` and on the resolved `crun_version`.

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: same computed expression.
- Related: `crun_checksums`, `crun_version`, `image_arch`, `crun_download_url`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
