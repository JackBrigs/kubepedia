---
id: VARIABLE-VSPHERE_CSI_NAMESPACE
type: variable
title: vsphere_csi_namespace
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - vsphere_csi_namespace
tags:
  - kubernetes-apps
  - csi-driver
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml
    note: "default: kube-system"
relations: []
---
<!-- generated: variable-stub -->

# vsphere_csi_namespace

## Summary

Kubespray variable `vsphere_csi_namespace` — default `kube-system`. Defined in `roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
vsphere_csi_namespace: kube-system
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml` (Kubespray `v2.31.0`).
