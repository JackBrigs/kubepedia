---
id: VARIABLE-RUNC_BINARY_CHECKSUM
type: variable
title: runc_binary_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - runc_binary_checksum
tags:
  - runc
  - checksum
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computes runc binary checksum by arch and version"
relations: []
---

# runc_binary_checksum

## Summary
The expected SHA checksum of the downloaded runc binary, looked up by architecture and runc version. Used to verify the integrity of the runc download.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `runc_binary_checksum: "{{ runc_checksums[image_arch][runc_version] }}"`. It indexes the `runc_checksums` map by `image_arch` and `runc_version`. The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Present in Kubespray >=v2.29.0 <=v2.31.0. Depends on `runc_checksums`, `image_arch`, and `runc_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
