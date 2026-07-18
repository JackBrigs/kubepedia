---
id: VARIABLE-EXTERNAL_VSPHERE_VERSION
type: variable
title: external_vsphere_version
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - external_vsphere_version
tags:
  - kubernetes-apps
  - csi-driver
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml
    note: "default: 7.0u1"
relations: []
---
<!-- generated: variable-stub -->

# external_vsphere_version

## Summary

Kubespray variable `external_vsphere_version` — default `7.0u1`. Defined in `roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
external_vsphere_version: 7.0u1
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml` (Kubespray `v2.31.0`).
