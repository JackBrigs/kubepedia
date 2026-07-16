---
id: VARIABLE-SKOPEO_BINARY_CHECKSUMS
type: variable
title: skopeo_binary_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - skopeo_binary_checksums
tags:
  - skopeo
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Nested map of skopeo binary checksums by architecture and version"
relations: []
---

# skopeo_binary_checksums

## Summary
Nested map of skopeo binary SHA256 checksums keyed by architecture (`arm64`, `amd64`, ...) then by skopeo version. Used to resolve `skopeo_binary_checksum` and `skopeo_version`.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml`. Example first entries:

```yaml
skopeo_binary_checksums:
  arm64:
    1.16.1: sha256:3272f15f469af843d325134ff8a77a069d647c5f247766715c098b8f0622b627
    ...
  amd64:
    1.16.1: sha256:8813fb7fcd7a723196ac287683dd929d280f6fe7f0782eace452fe1e3ff2b7eb
    ...
```

The top of the map (first version `1.16.1` for both `arm64` and `amd64`, including the quoted checksums above) is unchanged across v2.29.0-v2.31.0. The block's starting line differs (1533 in v2.29.0, 1679 in v2.29.1, 1327 in v2.30.0, 1441 in v2.31.0) because surrounding checksum blocks shift.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `skopeo_version` (first `amd64` key) and `skopeo_binary_checksum`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
