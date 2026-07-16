---
id: VARIABLE-CILIUM_HUBBLE_EXPORT_FILE_MAX_BACKUPS
type: variable
title: cilium_hubble_export_file_max_backups
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_export_file_max_backups
tags:
  - cilium
  - hubble
  - flowlog
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Maximum number of rotated Hubble export files to keep"
relations: []
---

# cilium_hubble_export_file_max_backups

## Summary
Sets the maximum number of rotated (backup) Hubble flow-log export files to retain. Default is `"5"` (a quoted string).

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_hubble_export_file_max_backups: "5"`. The default is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related to `cilium_hubble_export_file_max_size_mb` and the dynamic export variables.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
