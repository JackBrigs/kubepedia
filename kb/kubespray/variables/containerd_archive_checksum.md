---
id: VARIABLE-CONTAINERD_ARCHIVE_CHECKSUM
type: variable
title: containerd_archive_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_archive_checksum
tags:
  - containerd
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Checksum of the containerd archive, looked up by arch and version"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_archive_checksum

## Summary
Checksum of the containerd release archive to download. Looked up from the `containerd_archive_checksums` map by architecture and containerd version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
containerd_archive_checksum: "{{ containerd_archive_checksums[image_arch][containerd_version] }}"
```

This computed expression is unchanged across v2.29.0-v2.31.0 (line 201 in v2.29.0, 203 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Depends on `containerd_archive_checksums`, `image_arch`, and `containerd_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
