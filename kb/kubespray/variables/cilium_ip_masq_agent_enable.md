---
id: VARIABLE-CILIUM_IP_MASQ_AGENT_ENABLE
type: variable
title: cilium_ip_masq_agent_enable
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_ip_masq_agent_enable
tags:
  - cilium
  - masquerade
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Enables Cilium's built-in ip-masq-agent; default false"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_ip_masq_agent_enable

## Summary
Toggles Cilium's built-in ip-masq-agent (`ipMasqAgent.enabled`). Default: `false`. When enabled, additional masquerade sub-options (`masqLinkLocal`, resync interval) apply.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml`:

```yaml
cilium_ip_masq_agent_enable: false
```

Consumed in `roles/network_plugin/cilium/templates/values.yaml.j2` (`ipMasqAgent.enabled: {{ cilium_ip_masq_agent_enable | to_json }}`), and gates a `{% if cilium_ip_masq_agent_enable %}` block containing `masqLinkLocal`/`masqLinkLocalIPv6`. Also exposed (commented) in `inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml`. The default `false` is unchanged across v2.29.0-v2.31.0 (only line numbers shift between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_masq_link_local`, `cilium_masq_link_local_ipv6`, `cilium_ip_masq_resync_interval`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- roles/network_plugin/cilium/templates/values.yaml.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
