---
id: VARIABLE-GVISOR_CONTAINERD_SHIM_RUNSC_DOWNLOAD_URL
type: variable
title: gvisor_containerd_shim_runsc_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gvisor_containerd_shim_runsc_download_url
tags:
  - gvisor
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed download URL for the gVisor containerd-shim-runsc-v1 binary"
relations: []
---

# gvisor_containerd_shim_runsc_download_url

## Summary
Download URL for the gVisor `containerd-shim-runsc-v1` binary, computed from the Google Storage base URL, the gVisor version, and the node architecture.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as a computed expression:

```yaml
gvisor_containerd_shim_runsc_download_url: "{{ storage_googleapis_url }}/gvisor/releases/release/{{ gvisor_version }}/{{ ansible_architecture }}/containerd-shim-runsc-v1"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `storage_googleapis_url`, `gvisor_version`, and `ansible_architecture`; used only when `gvisor_enabled` is true.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
