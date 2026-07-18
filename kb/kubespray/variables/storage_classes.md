---
id: VARIABLE-STORAGE_CLASSES
type: variable
title: storage_classes
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - storage_classes
tags:
  - kubernetes-apps
  - persistent-volumes
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/persistent_volumes/cinder-csi/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/persistent_volumes/cinder-csi/defaults/main.yml
    note: "default: (structured / block value — see source)"
relations: []
---
<!-- generated: variable-stub -->

# storage_classes

## Summary

Kubespray variable `storage_classes` — default `(structured / block value — see source)`. Defined in `roles/kubernetes-apps/persistent_volumes/cinder-csi/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/persistent_volumes/cinder-csi/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
storage_classes: (structured / block value — see source)
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/persistent_volumes/cinder-csi/defaults/main.yml` (Kubespray `v2.31.0`).
