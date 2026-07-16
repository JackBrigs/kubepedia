---
id: VARIABLE-GVISOR_RUNSC_BINARY_CHECKSUMS
type: variable
title: gvisor_runsc_binary_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gvisor_runsc_binary_checksums
tags:
  - gvisor
  - checksum
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Map of arch -> gvisor version -> sha512 checksum for the runsc binary"
relations: []
---

# gvisor_runsc_binary_checksums

## Summary
Lookup map of known SHA-512 checksums for the gVisor `runsc` binary, keyed by architecture (e.g. `arm64`, `amd64`) and then by gVisor release date-version (e.g. `20260323.0`). Feeds `gvisor_runsc_binary_checksum`, and its first key defines `gvisor_version`.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml`:

```yaml
gvisor_runsc_binary_checksums:
  arm64:
    '20260323.0': sha512:2aacb4de...
    ...
  amd64:
    ...
```

The variable is present in all four tags. The map's content grows over time as new gVisor releases are added, but the variable definition and structure are unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. `gvisor_version` is derived from the first key of its `amd64` entry; consumed via `image_arch` and `gvisor_version` to derive `gvisor_runsc_binary_checksum`. Relevant only when `gvisor_enabled` is true.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
