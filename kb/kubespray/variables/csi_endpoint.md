---
id: VARIABLE-CSI_ENDPOINT
type: variable
title: csi_endpoint
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - csi_endpoint
tags:
  - kubernetes-apps
  - csi-driver
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml
    note: "default: {% if external_vsphere_version >= '7.0u1' %}/csi{% else %}/var/lib/…"
relations: []
---
<!-- generated: variable-stub -->

# csi_endpoint

## Summary

Kubespray variable `csi_endpoint` — default `{% if external_vsphere_version >= '7.0u1' %}/csi{% else %}/var/lib/…`. Defined in `roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
csi_endpoint: {% if external_vsphere_version >= '7.0u1' %}/csi{% else %}/var/lib/…
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml` (Kubespray `v2.31.0`).
