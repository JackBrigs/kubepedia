---
id: VARIABLE-GVISOR_RUNSC_BINARY_CHECKSUM
type: variable
title: gvisor_runsc_binary_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gvisor_runsc_binary_checksum
tags:
  - gvisor
  - checksum
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Selected checksum for the runsc binary of the active arch/version"
relations: []
---

# gvisor_runsc_binary_checksum

## Summary
Resolved checksum used to verify the downloaded gVisor `runsc` binary. It selects the entry matching the current architecture and gVisor version from the `gvisor_runsc_binary_checksums` map.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as a computed expression:

```yaml
gvisor_runsc_binary_checksum: "{{ gvisor_runsc_binary_checksums[image_arch][gvisor_version] }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `image_arch`, `gvisor_version`, and the `gvisor_runsc_binary_checksums` map; used only when `gvisor_enabled` is true.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
