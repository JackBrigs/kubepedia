---
id: VARIABLE-CILIUM_HUBBLE_EXPORT_FILE_MAX_SIZE_MB
type: variable
title: cilium_hubble_export_file_max_size_mb
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_export_file_max_size_mb
tags:
  - cilium
  - hubble
  - flowlog
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Maximum size in MB of a Hubble export file before rotation"
relations: []
---

# cilium_hubble_export_file_max_size_mb

## Summary
Sets the maximum size in megabytes of a Hubble flow-log export file before it is rotated. Default is `"10"` (a quoted string).

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_hubble_export_file_max_size_mb: "10"`. The default is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related to `cilium_hubble_export_file_max_backups` and the dynamic export variables.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
