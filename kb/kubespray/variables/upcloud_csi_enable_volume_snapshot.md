---
id: VARIABLE-UPCLOUD_CSI_ENABLE_VOLUME_SNAPSHOT
type: variable
title: upcloud_csi_enable_volume_snapshot
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - upcloud_csi_enable_volume_snapshot
tags:
  - kubernetes-apps
  - csi-driver
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/csi_driver/upcloud/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/csi_driver/upcloud/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# upcloud_csi_enable_volume_snapshot

## Summary

Kubespray variable `upcloud_csi_enable_volume_snapshot` — default `false`. Defined in `roles/kubernetes-apps/csi_driver/upcloud/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/csi_driver/upcloud/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
upcloud_csi_enable_volume_snapshot: false
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/csi_driver/upcloud/defaults/main.yml` (Kubespray `v2.31.0`).
