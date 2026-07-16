---
id: VARIABLE-CILIUM_MONITOR_AGGREGATION
type: variable
title: cilium_monitor_aggregation
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_monitor_aggregation
tags:
  - cilium
  - cni
  - monitoring
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Default cilium_monitor_aggregation: medium"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_monitor_aggregation

## Summary
Sets the Cilium monitor aggregation level (none/low/medium/maximum), which controls how much datapath monitoring notification traffic is generated. Default `medium`. Rendered into the Cilium Helm values as `monitorAggregation`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_monitor_aggregation: medium`. Consumed by `roles/network_plugin/cilium/templates/values.yaml.j2` as `monitorAggregation: {{ cilium_monitor_aggregation }}`. The default value `medium` is unchanged across v2.29.0-v2.31.0 (line number shifts: 60 in v2.29.0/v2.29.1, 58 in v2.30.0, 43 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variable: `cilium_monitor_aggregation_flags` (effective only when this is "medium" or higher).

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
