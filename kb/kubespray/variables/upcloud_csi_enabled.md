---
id: VARIABLE-UPCLOUD_CSI_ENABLED
type: variable
title: upcloud_csi_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - upcloud_csi_enabled
tags:
  - csi
  - upcloud
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles the UpCloud CSI driver: false"
relations: []
---

# upcloud_csi_enabled

## Summary
Boolean toggle that enables deployment of the UpCloud CSI storage driver. Default is `false` (disabled).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `upcloud_csi_enabled: false`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0; only its line number shifts (455 in v2.29.0/v2.29.1, 456 in v2.30.0, 464 in v2.31.0). The sample inventory `inventory/sample/group_vars/all/upcloud.yml` shows a commented `upcloud_csi_enabled: true`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only for the UpCloud cloud provider.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
