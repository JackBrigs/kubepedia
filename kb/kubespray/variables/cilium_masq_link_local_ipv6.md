---
id: VARIABLE-CILIUM_MASQ_LINK_LOCAL_IPV6
type: variable
title: cilium_masq_link_local_ipv6
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_masq_link_local_ipv6
tags:
  - cilium
  - cni
  - masquerade
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Default cilium_masq_link_local_ipv6: false"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_masq_link_local_ipv6

## Summary
Controls whether Cilium masquerades traffic to the IPv6 link-local prefix. Default `false`. When false, the IPv6 link-local range is appended to the non-masquerade CIDRs list. The value is rendered into the Cilium Helm values as `masqLinkLocalIPv6`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_masq_link_local_ipv6: false`. Consumed by `roles/network_plugin/cilium/templates/values.yaml.j2` as `masqLinkLocalIPv6: {{ cilium_masq_link_local_ipv6 | to_json }}`. The default value is unchanged across v2.29.0-v2.31.0 (only the line number within the defaults file shifts: 144 in v2.29.0/v2.29.1, 142 in v2.30.0, 127 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variable: `cilium_masq_link_local` (IPv4 counterpart), `cilium_non_masquerade_cidrs`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
