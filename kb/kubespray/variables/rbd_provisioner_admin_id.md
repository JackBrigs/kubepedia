---
id: VARIABLE-RBD_PROVISIONER_ADMIN_ID
type: variable
title: rbd_provisioner_admin_id
status: active
kubespray_version: ">=v2.27.0 <=v2.27.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - rbd_provisioner_admin_id
tags:
  - kubernetes-apps
  - external-provisioner
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/external_provisioner/rbd_provisioner/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.27.1/roles/kubernetes-apps/external_provisioner/rbd_provisioner/defaults/main.yml
    note: "default: admin"
relations: []
---
<!-- generated: variable-stub -->

# rbd_provisioner_admin_id

## Summary

Kubespray variable `rbd_provisioner_admin_id` — default `admin`. Defined in `roles/kubernetes-apps/external_provisioner/rbd_provisioner/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.27.1` of the indexed range. **Removed after `v2.27.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/external_provisioner/rbd_provisioner/defaults/main.yml` (Kubespray `v2.27.1`):

```yaml
rbd_provisioner_admin_id: admin
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.27.1`. **Removed after `v2.27.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/external_provisioner/rbd_provisioner/defaults/main.yml` (Kubespray `v2.27.1`).
