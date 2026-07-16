---
id: VARIABLE-KATA_CONTAINERS_BINARY_CHECKSUM
type: variable
title: kata_containers_binary_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kata_containers_binary_checksum
tags:
  - kata
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Resolves the Kata Containers static tarball checksum for the current arch and version"
relations: []
---

# kata_containers_binary_checksum

## Summary
Holds the checksum used to verify the downloaded Kata Containers static binary tarball. It is a computed lookup into `kata_containers_binary_checksums`, keyed by the host architecture and the selected Kata version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
kata_containers_binary_checksum: "{{ kata_containers_binary_checksums[image_arch][kata_containers_version] }}"
```

The expression is unchanged across v2.29.0-v2.31.0 (line 197 in v2.29.0; line 199 in v2.29.1, v2.30.0 and v2.31.0). The resolved value depends on `image_arch` and `kata_containers_version`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `kata_containers_binary_checksums` (the checksum map) and `kata_containers_version` (which entry is selected). Only relevant when `kata_containers_enabled: true`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
