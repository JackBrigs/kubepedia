---
id: VARIABLE-KUBE_VIP_BGP_ENABLED
type: variable
title: kube_vip_bgp_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_bgp_enabled
tags:
  - kube-vip
  - bgp
  - networking
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_vip_bgp_enabled with default false"
relations: []
---

# kube_vip_bgp_enabled

## Summary
Enables BGP mode for kube-vip. Default `false`. When `true`, kube-vip advertises the virtual IP via BGP and the BGP-related variables (peer address, AS, router id, etc.) are rendered into the manifest.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```
kube_vip_bgp_enabled: false
```

Value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Consumed in `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2` as a gate (`{% if kube_vip_bgp_enabled %}`) for the BGP block. In v2.31.0 it also gates an assertion in `roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml`.

## Compatibility
Kubespray v2.29.0 - v2.31.0. Related BGP variables: `kube_vip_bgp_routerid`, `kube_vip_bgp_peeraddress`, `kube_vip_bgp_peeras`, `kube_vip_bgp_peerpass`, `kube_vip_bgppeers`, and (v2.31.0+) `kube_vip_bgp_sourceip` / `kube_vip_bgp_sourceif`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
