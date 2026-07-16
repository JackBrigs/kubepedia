---
id: VARIABLE-GVISOR_CONTAINERD_SHIM_BINARY_CHECKSUMS
type: variable
title: gvisor_containerd_shim_binary_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gvisor_containerd_shim_binary_checksums
tags:
  - gvisor
  - checksum
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Map of arch -> gvisor version -> sha512 checksum for the containerd-shim-runsc-v1 binary"
relations: []
---

# gvisor_containerd_shim_binary_checksums

## Summary
Lookup map of known SHA-512 checksums for the gVisor `containerd-shim-runsc-v1` binary, keyed by architecture (e.g. `arm64`, `amd64`) and then by gVisor release date-version (e.g. `20260323.0`). Feeds `gvisor_containerd_shim_binary_checksum`.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml`:

```yaml
gvisor_containerd_shim_binary_checksums:
  arm64:
    '20260323.0': sha512:b285a1ca...
    ...
  amd64:
    ...
```

The variable is present in all four tags. The map's content grows over time as new gVisor releases are added (the first key also determines `gvisor_version`), but the variable definition and structure are unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Consumed via `image_arch` and `gvisor_version` to derive `gvisor_containerd_shim_binary_checksum`; relevant only when `gvisor_enabled` is true.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
