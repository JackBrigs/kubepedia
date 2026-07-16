---
id: VARIABLE-CILIUM_ROLLING_RESTART_WAIT_RETRIES_COUNT
type: variable
title: cilium_rolling_restart_wait_retries_count
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_rolling_restart_wait_retries_count
tags:
  - cilium
  - rollout
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_rolling_restart_wait_retries_count, default 30"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_rolling_restart_wait_retries_count

## Summary
Number of retries Kubespray performs when waiting for the Cilium DaemonSet rolling restart to complete. Default is `30`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_rolling_restart_wait_retries_count: 30
```

The default value `30` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when `kube_network_plugin: cilium`. Paired with `cilium_rolling_restart_wait_retries_delay_seconds`; total wait ≈ count × delay.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
