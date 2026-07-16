---
id: VARIABLE-CILIUM_AGENT_HEALTH_PORT
type: variable
title: cilium_agent_health_port
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_agent_health_port
tags:
  - cilium
  - cni
  - health
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "TCP port for the cilium-agent health check endpoint; default \"9879\""
relations: []
---

# cilium_agent_health_port

## Summary
Sets the TCP port used by the cilium-agent health check endpoint. Defaults to `"9879"` (a quoted string).

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_agent_health_port: "9879"
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 17 in v2.29.0/v2.29.1, line 15 in v2.30.0/v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Cilium CNI only.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
