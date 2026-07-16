---
id: VARIABLE-KUBE_VIP_BGPPEERS
type: variable
title: kube_vip_bgppeers
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_bgppeers
tags:
  - kube-vip
  - bgp
  - loadbalancer
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_vip_bgppeers with an empty (unset/null) default"
relations: []
---

# kube_vip_bgppeers

## Summary
Specifies additional BGP peers for kube-vip when BGP mode is used. It is defined with no value (null/unset) by default, meaning no extra BGP peers are configured beyond those derived from the other `kube_vip_bgp_*` variables.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_vip_bgppeers:` (an empty default, i.e. null). The value is unchanged across v2.29.0-v2.31.0. Only the line number shifts (line 82 in v2.29.0/v2.29.1, line 80 in v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when kube-vip is enabled with BGP (`kube_vip_bgp_enabled: true`). Related variables: `kube_vip_bgp_enabled`, `kube_vip_bgp_peeraddress`, `kube_vip_local_as`, `kube_vip_bgp_peeras`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
