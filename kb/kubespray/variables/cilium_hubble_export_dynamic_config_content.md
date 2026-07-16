---
id: VARIABLE-CILIUM_HUBBLE_EXPORT_DYNAMIC_CONFIG_CONTENT
type: variable
title: cilium_hubble_export_dynamic_config_content
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_export_dynamic_config_content
tags:
  - cilium
  - hubble
  - flowlog
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Dynamic Hubble flow-log export configuration content"
relations: []
---

# cilium_hubble_export_dynamic_config_content

## Summary
Defines the dynamic Hubble flow-log export configuration used when `cilium_hubble_export_dynamic_enabled` is true. It is a list of flow-log entries with name, field mask, include/exclude filters, and target file path.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml`. The default value is unchanged across v2.29.0-v2.31.0:

```yaml
cilium_hubble_export_dynamic_config_content:
  - name: all
    fieldMask: []
    includeFilters: []
    excludeFilters: []
    filePath: "/var/run/cilium/hubble/events.log"
```

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Consumed together with `cilium_hubble_export_dynamic_enabled`, `cilium_hubble_export_file_max_backups`, and `cilium_hubble_export_file_max_size_mb`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
