---
id: VARIABLE-UPCLOUD_CSI_SNAPSHOT_VALIDATION_WEBHOOK_IMAGE_TAG
type: variable
title: upcloud_csi_snapshot_validation_webhook_image_tag
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - upcloud_csi_snapshot_validation_webhook_image_tag
tags:
  - kubernetes-apps
  - csi-driver
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/csi_driver/upcloud/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/csi_driver/upcloud/defaults/main.yml
    note: "default: v4.2.1"
relations: []
---
<!-- generated: variable-stub -->

# upcloud_csi_snapshot_validation_webhook_image_tag

## Summary

Kubespray variable `upcloud_csi_snapshot_validation_webhook_image_tag` — default `v4.2.1`. Defined in `roles/kubernetes-apps/csi_driver/upcloud/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/csi_driver/upcloud/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
upcloud_csi_snapshot_validation_webhook_image_tag: v4.2.1
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/csi_driver/upcloud/defaults/main.yml` (Kubespray `v2.31.0`).
