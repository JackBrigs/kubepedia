---
id: VARIABLE-CONTAINERD_STATIC_ARCHIVE_CHECKSUM
type: variable
title: containerd_static_archive_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_static_archive_checksum
tags:
  - containerd
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Looks up the static containerd archive checksum for arch and version"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_static_archive_checksum

## Summary
The checksum of the static containerd archive, looked up from the `containerd_static_archive_checksums` map by architecture and containerd version. Used when `containerd_static_binary` is true.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
containerd_static_archive_checksum: "{{ containerd_static_archive_checksums[image_arch][containerd_version] }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only line numbers shift).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related: `containerd_static_binary`, `containerd_checksum`, `containerd_version`, `image_arch`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
