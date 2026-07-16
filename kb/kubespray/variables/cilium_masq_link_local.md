---
id: VARIABLE-CILIUM_MASQ_LINK_LOCAL
type: variable
title: cilium_masq_link_local
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_masq_link_local
tags:
  - cilium
  - masquerade
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Whether ip-masq-agent masquerades link-local (IPv4) traffic; default false"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_masq_link_local

## Summary
Controls whether Cilium's ip-masq-agent masquerades IPv4 link-local traffic (`ipMasqAgent.config.masqLinkLocal`). Default: `false`. Applied only when `cilium_ip_masq_agent_enable` is true.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml`:

```yaml
cilium_masq_link_local: false
```

Consumed in `roles/network_plugin/cilium/templates/values.yaml.j2` inside the `{% if cilium_ip_masq_agent_enable %}` block (`masqLinkLocal: {{ cilium_masq_link_local | to_json }}`); the paired IPv6 setting is `cilium_masq_link_local_ipv6`. Exposed (commented) in `inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml`. The default `false` is unchanged across v2.29.0-v2.31.0 (only line numbers shift between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_ip_masq_agent_enable`, `cilium_masq_link_local_ipv6`, `cilium_ip_masq_resync_interval`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- roles/network_plugin/cilium/templates/values.yaml.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
