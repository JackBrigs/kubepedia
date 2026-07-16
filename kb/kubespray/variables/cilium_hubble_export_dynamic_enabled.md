---
id: VARIABLE-CILIUM_HUBBLE_EXPORT_DYNAMIC_ENABLED
type: variable
title: cilium_hubble_export_dynamic_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_export_dynamic_enabled
tags:
  - cilium
  - hubble
  - flowlog
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Toggle for dynamic Hubble flow-log export"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_hubble_export_dynamic_enabled

## Summary
Boolean toggle that enables dynamic Hubble flow-log export. When true, the export uses the entries defined in `cilium_hubble_export_dynamic_config_content`. Default is `false`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_hubble_export_dynamic_enabled: false`. The default is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related to `cilium_hubble_export_dynamic_config_content`, `cilium_hubble_export_file_max_backups`, and `cilium_hubble_export_file_max_size_mb`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
