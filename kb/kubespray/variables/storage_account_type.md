---
id: VARIABLE-STORAGE_ACCOUNT_TYPE
type: variable
title: storage_account_type
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - storage_account_type
tags:
  - kubernetes-apps
  - persistent-volumes
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/persistent_volumes/azuredisk-csi/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/persistent_volumes/azuredisk-csi/defaults/main.yml
    note: "default: StandardSSD_LRS"
relations: []
---
<!-- generated: variable-stub -->

# storage_account_type

## Summary

Kubespray variable `storage_account_type` — default `StandardSSD_LRS`. Defined in `roles/kubernetes-apps/persistent_volumes/azuredisk-csi/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/persistent_volumes/azuredisk-csi/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
storage_account_type: StandardSSD_LRS
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/persistent_volumes/azuredisk-csi/defaults/main.yml` (Kubespray `v2.31.0`).
