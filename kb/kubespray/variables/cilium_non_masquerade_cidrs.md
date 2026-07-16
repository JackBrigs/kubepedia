---
id: VARIABLE-CILIUM_NON_MASQUERADE_CIDRS
type: variable
title: cilium_non_masquerade_cidrs
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_non_masquerade_cidrs
tags:
  - cilium
  - cni
  - masquerade
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "List of CIDRs excluded from masquerading"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_non_masquerade_cidrs

## Summary
List of CIDRs whose destination traffic is excluded from masquerading (SNAT). Packets from a pod to an IP outside this range are masqueraded. The default is a fixed list of private and special-use IPv4 ranges. Rendered into the Cilium Helm values as `nonMasqueradeCIDRs`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as a YAML list and consumed by `roles/network_plugin/cilium/templates/values.yaml.j2` as `nonMasqueradeCIDRs: {{ cilium_non_masquerade_cidrs }}`. The list is identical across v2.29.0-v2.31.0 (only line number shifts: 129 in v2.29.0/v2.29.1, 127 in v2.30.0, 112 in v2.31.0):

```yaml
cilium_non_masquerade_cidrs:
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16
  - 100.64.0.0/10
  - 192.0.0.0/24
  - 192.0.2.0/24
  - 192.88.99.0/24
  - 198.18.0.0/15
  - 198.51.100.0/24
  - 203.0.113.0/24
  - 240.0.0.0/4
```

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_masq_link_local`, `cilium_masq_link_local_ipv6`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
