---
id: VARIABLE-SKOPEO_BINARY_CHECKSUM
type: variable
title: skopeo_binary_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - skopeo_binary_checksum
tags:
  - skopeo
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Selects the skopeo binary checksum for the current arch and version"
relations: []
---

# skopeo_binary_checksum

## Summary
Resolved checksum for the skopeo binary matching the current architecture and version. Computed as `"{{ skopeo_binary_checksums[image_arch][skopeo_version] }}"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
skopeo_binary_checksum: "{{ skopeo_binary_checksums[image_arch][skopeo_version] }}"
```

The expression is unchanged across v2.29.0-v2.31.0 (line 204 in v2.29.0, 206 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Indexes `skopeo_binary_checksums` by `image_arch` and `skopeo_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
