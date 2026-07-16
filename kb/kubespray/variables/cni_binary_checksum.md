---
id: VARIABLE-CNI_BINARY_CHECKSUM
type: variable
title: cni_binary_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cni_binary_checksum
tags:
  - cni
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Checksum of the CNI plugins archive, looked up by arch and version"
relations: []
---

# cni_binary_checksum

## Summary
Checksum of the CNI plugins archive to be downloaded. Looked up from the `cni_binary_checksums` map by architecture and CNI version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cni_binary_checksum: "{{ cni_binary_checksums[image_arch][cni_version] }}"
```

This computed expression is unchanged across v2.29.0-v2.31.0 (line 182 in v2.29.0, 184 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Depends on `cni_binary_checksums`, `image_arch`, and `cni_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
