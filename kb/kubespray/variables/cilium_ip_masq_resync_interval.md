---
id: VARIABLE-CILIUM_IP_MASQ_RESYNC_INTERVAL
type: variable
title: cilium_ip_masq_resync_interval
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_ip_masq_resync_interval
tags:
  - cilium
  - masquerade
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Resync interval for Cilium's ip-masq-agent; default 60s"
relations: []
---

# cilium_ip_masq_resync_interval

## Summary
Resync interval for Cilium's ip-masq-agent. Default: `60s`. Relevant only when `cilium_ip_masq_agent_enable` is true.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml`:

```yaml
cilium_ip_masq_resync_interval: 60s
```

In `roles/network_plugin/cilium/templates/values.yaml.j2` the variable appears as a comment marker (`# cilium_ip_masq_resync_interval`) within the ip-masq-agent block; it is also exposed (commented) in `inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml`. The default `60s` is unchanged across v2.29.0-v2.31.0 (only line numbers shift between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_ip_masq_agent_enable`, `cilium_masq_link_local`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- roles/network_plugin/cilium/templates/values.yaml.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
