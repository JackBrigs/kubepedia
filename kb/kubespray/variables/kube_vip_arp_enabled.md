---
id: VARIABLE-KUBE_VIP_ARP_ENABLED
type: variable
title: kube_vip_arp_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_arp_enabled
tags:
  - kube-vip
  - arp
  - networking
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_vip_arp_enabled with default false"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# kube_vip_arp_enabled

## Summary
Enables ARP (layer 2) mode for kube-vip. Default `false`. When `true`, kube-vip advertises the virtual IP via gratuitous ARP; it also drives leader election (`kube_vip_leader_election_enabled` defaults to this value).

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```
kube_vip_arp_enabled: false
```

Value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Consumed by the manifest template (`roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2`, `value: {{ kube_vip_arp_enabled | string | to_json }}`) and asserted as boolean in `roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml`.

## Compatibility
Kubespray v2.29.0 - v2.31.0. Related: `kube_vip_leader_election_enabled` (defaults to `{{ kube_vip_arp_enabled }}`), `kube_vip_bgp_enabled` (alternative mode).

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
