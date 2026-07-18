---
id: VARIABLE-CINDER_CSI_SNAPSHOTTER_IMAGE_TAG
type: variable
title: cinder_csi_snapshotter_image_tag
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - cinder_csi_snapshotter_image_tag
tags:
  - kubernetes-apps
  - csi-driver
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml
    note: "default: v6.3.2"
relations: []
---
<!-- generated: variable-stub -->

# cinder_csi_snapshotter_image_tag

## Summary

Kubespray variable `cinder_csi_snapshotter_image_tag` — default `v6.3.2`. Defined in `roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
cinder_csi_snapshotter_image_tag: v6.3.2
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml` (Kubespray `v2.31.0`).
