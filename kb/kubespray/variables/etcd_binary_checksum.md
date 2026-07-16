---
id: VARIABLE-ETCD_BINARY_CHECKSUM
type: variable
title: etcd_binary_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_binary_checksum
tags:
  - etcd
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Selects the etcd binary checksum by arch and version from etcd_binary_checksums"
relations: []
---

# etcd_binary_checksum

## Summary
The checksum used to verify the downloaded etcd binary. It is computed by looking up the `etcd_binary_checksums` map by the target architecture and etcd version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:
```yaml
etcd_binary_checksum: "{{ etcd_binary_checksums[image_arch][etcd_version] }}"
```
The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 181 in v2.29.0, line 183 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `etcd_binary_checksums`, `image_arch`, and `etcd_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
