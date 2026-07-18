---
id: VARIABLE-CEPHFS_PROVISIONER_NAMESPACE
type: variable
title: cephfs_provisioner_namespace
status: active
kubespray_version: ">=v2.27.0 <=v2.27.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - cephfs_provisioner_namespace
tags:
  - kubernetes-apps
  - external-provisioner
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/external_provisioner/cephfs_provisioner/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.27.1/roles/kubernetes-apps/external_provisioner/cephfs_provisioner/defaults/main.yml
    note: "default: cephfs-provisioner"
relations: []
---
<!-- generated: variable-stub -->

# cephfs_provisioner_namespace

## Summary

Kubespray variable `cephfs_provisioner_namespace` — default `cephfs-provisioner`. Defined in `roles/kubernetes-apps/external_provisioner/cephfs_provisioner/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.27.1` of the indexed range. **Removed after `v2.27.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/external_provisioner/cephfs_provisioner/defaults/main.yml` (Kubespray `v2.27.1`):

```yaml
cephfs_provisioner_namespace: cephfs-provisioner
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.27.1`. **Removed after `v2.27.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/external_provisioner/cephfs_provisioner/defaults/main.yml` (Kubespray `v2.27.1`).
