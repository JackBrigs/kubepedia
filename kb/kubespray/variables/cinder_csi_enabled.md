---
id: VARIABLE-CINDER_CSI_ENABLED
type: variable
title: cinder_csi_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cinder_csi_enabled
tags:
  - openstack
  - csi
  - storage
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "cinder_csi_enabled: false (default, unchanged v2.29.0-v2.31.0)"
relations: []
---

# cinder_csi_enabled

## Summary

`cinder_csi_enabled` toggles deployment of the OpenStack Cinder CSI driver for
persistent block storage. The default is `false` across `v2.29.0`-`v2.31.0`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` as
`cinder_csi_enabled: false`. The literal `false` is unchanged across all four
tags; only the line number shifts (450 in v2.29.0/v2.29.1, 451 in v2.30.0, 459 in
v2.31.0).

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: default `false`.
- Relevant only for OpenStack-backed clusters using Cinder for volumes.

## References

- `roles/kubespray_defaults/defaults/main/main.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
