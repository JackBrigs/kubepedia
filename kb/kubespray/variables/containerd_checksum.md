---
id: VARIABLE-CONTAINERD_CHECKSUM
type: variable
title: containerd_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_checksum
tags:
  - containerd
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Selects the containerd archive checksum (static vs regular)"
relations: []
---

# containerd_checksum

## Summary
The checksum used to verify the downloaded containerd archive. It picks the static-archive checksum when a static binary is requested, otherwise the regular archive checksum.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
containerd_checksum: "{{ containerd_static_archive_checksum if containerd_static_binary else containerd_archive_checksum }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only line numbers shift).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related: `containerd_static_binary`, `containerd_static_archive_checksum`, `containerd_download_url`, `containerd_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
