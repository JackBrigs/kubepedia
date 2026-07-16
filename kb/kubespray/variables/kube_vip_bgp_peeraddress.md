---
id: VARIABLE-KUBE_VIP_BGP_PEERADDRESS
type: variable
title: kube_vip_bgp_peeraddress
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_bgp_peeraddress
tags:
  - kube-vip
  - bgp
  - networking
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_vip_bgp_peeraddress with empty default"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# kube_vip_bgp_peeraddress

## Summary
Address of the BGP peer that kube-vip connects to when BGP mode is enabled. Default is empty (unset). Rendered into the kube-vip manifest as the `bgp_peeraddress` value.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` with no value:

```
kube_vip_bgp_peeraddress:
```

Value is unchanged (empty) across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Consumed in `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2` (`value: {{ kube_vip_bgp_peeraddress | to_json }}`) within the `kube_vip_bgp_enabled` block.

## Compatibility
Kubespray v2.29.0 - v2.31.0. Effective only when `kube_vip_bgp_enabled: true`. Related: `kube_vip_bgp_peeras`, `kube_vip_bgp_peerpass`, `kube_vip_bgppeers`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
