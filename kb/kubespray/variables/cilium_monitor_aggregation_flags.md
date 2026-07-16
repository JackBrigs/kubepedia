---
id: VARIABLE-CILIUM_MONITOR_AGGREGATION_FLAGS
type: variable
title: cilium_monitor_aggregation_flags
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_monitor_aggregation_flags
tags:
  - cilium
  - cni
  - monitoring
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Default cilium_monitor_aggregation_flags: \"all\""
relations: []
---

# cilium_monitor_aggregation_flags

## Summary
Sets the TCP flags that, on first observation, cause monitor notifications to be generated. Default `"all"`. Only effective when `cilium_monitor_aggregation` is set to "medium" or higher.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_monitor_aggregation_flags: "all"`. The default value `"all"` is unchanged across v2.29.0-v2.31.0 (line number shifts: 308 in v2.29.0/v2.29.1, 306 in v2.30.0, 291 in v2.31.0). Exposed to users (commented) in the sample inventory `k8s-net-cilium.yml`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variable: `cilium_monitor_aggregation` (this flag is only effective when aggregation is "medium" or higher).

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
