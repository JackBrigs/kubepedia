---
id: VARIABLE-CONTAINERD_STATIC_BINARY
type: variable
title: containerd_static_binary
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_static_binary
tags:
  - containerd
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggle to install the static containerd archive; default false"
relations: []
---

# containerd_static_binary

## Summary
Boolean toggle that selects the statically linked containerd archive instead of the regular one. When true, the download URL inserts `static-` and the static-archive checksum is used. Default: `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
containerd_static_binary: false
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only line numbers shift). Several CI files under `tests/files/` override it to `true`, but the shipped default is `false`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related: `containerd_download_url`, `containerd_checksum`, `containerd_static_archive_checksum`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
