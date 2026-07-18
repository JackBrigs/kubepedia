---
id: VARIABLE-VSPHERE_CSI_RESIZER_TAG
type: variable
title: vsphere_csi_resizer_tag
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - vsphere_csi_resizer_tag
tags:
  - kubernetes-apps
  - csi-driver
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml
    note: "default: v1.8.0"
relations: []
---
<!-- generated: variable-stub -->

# vsphere_csi_resizer_tag

## Summary

Kubespray variable `vsphere_csi_resizer_tag` — default `v1.8.0`. Defined in `roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
vsphere_csi_resizer_tag: v1.8.0
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml` (Kubespray `v2.31.0`).
