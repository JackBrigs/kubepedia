---
id: VARIABLE-KUBECTL_BINARY_CHECKSUM
type: variable
title: kubectl_binary_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubectl_binary_checksum
tags:
  - kubectl
  - checksum
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Resolves the kubectl checksum for the current arch and kube_version"
relations: []
---

# kubectl_binary_checksum

## Summary
The expected checksum for the downloaded `kubectl` binary, looked up from the
`kubectl_checksums` map by architecture and Kubernetes version. Default:
`{{ kubectl_checksums[image_arch][kube_version] }}`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:
`kubectl_binary_checksum: "{{ kubectl_checksums[image_arch][kube_version] }}"`.
The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line
number 184 in v2.29.0, 185 in v2.29.1/v2.30.0/v2.31.0, 186 in v2.30.0/v2.31.0 area).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `kubectl_checksums`, `image_arch`,
and `kube_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
