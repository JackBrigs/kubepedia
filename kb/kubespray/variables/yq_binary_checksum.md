---
id: VARIABLE-YQ_BINARY_CHECKSUM
type: variable
title: yq_binary_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - yq_binary_checksum
tags:
  - yq
  - checksum
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Selects the sha256 checksum for the yq binary by arch and version."
relations: []
---

# yq_binary_checksum

## Summary
The expected checksum of the downloaded yq binary, used to verify download integrity. It is a computed default that looks up the value in the `yq_checksums` map by the node's image architecture and the resolved yq version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

`yq_binary_checksum: "{{ yq_checksums[image_arch][yq_version] }}"`

The expression is unchanged across v2.29.0-v2.31.0 (line 186 in v2.29.0; line 188 in v2.29.1/v2.30.0/v2.31.0). The concrete checksum value is resolved from `yq_checksums`, keyed by `image_arch` and `yq_version`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `yq_checksums`, `yq_version`, `image_arch`, `yq_download_url`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
