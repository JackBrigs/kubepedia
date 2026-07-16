---
id: VARIABLE-VSPHERE_CSI_ENABLED
type: variable
title: vsphere_csi_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - vsphere_csi_enabled
tags:
  - vsphere
  - csi
  - storage
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles deployment of the vSphere CSI driver; default false."
relations: []
---

# vsphere_csi_enabled

## Summary
Boolean toggle that controls whether the vSphere CSI (Container Storage Interface) driver is deployed. The default is `false`, so the vSphere CSI driver is not installed unless explicitly enabled. When set to `true` (typically alongside the vSphere external cloud provider), Kubespray deploys the CSI components for vSphere-backed persistent volumes.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

`vsphere_csi_enabled: false`

The default is unchanged across v2.29.0-v2.31.0 (line number shifts: 454 in v2.29.0/v2.29.1, 455 in v2.30.0, 463 in v2.31.0). The vSphere documentation (`docs/cloud_controllers/vsphere.md`) shows it set to `true` as a usage example, but the role default remains `false`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant when using the vSphere cloud provider. Related variables: `external_vsphere_*`, `cloud_provider`, `vsphere_csi_controller_replicas`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
