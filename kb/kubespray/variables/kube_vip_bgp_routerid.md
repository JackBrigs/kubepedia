---
id: VARIABLE-KUBE_VIP_BGP_ROUTERID
type: variable
title: kube_vip_bgp_routerid
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_bgp_routerid
tags:
  - kube-vip
  - bgp
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Declares the BGP router ID for kube-vip with an empty (null) default"
relations: []
---

# kube_vip_bgp_routerid

## Summary
BGP router ID advertised by kube-vip when BGP mode is enabled. It is declared with no value (empty/null default), so no router ID is set unless the operator provides one. It is injected into the kube-vip manifest as the `bgp_routerid` environment value.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` with an empty value:

```yaml
kube_vip_bgp_routerid:
```

Consumed in `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2` as `value: {{ kube_vip_bgp_routerid | string | to_json }}`. The empty default and the path are unchanged across v2.29.0-v2.31.0 (only the line number shifts: 77 in v2.29.0/v2.29.1, 75 in v2.30.0/v2.31.0).

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Effective only when `kube_vip_bgp_enabled` is true; related to `kube_vip_bgp_peeras`, `kube_vip_bgp_peeraddress`, and `kube_vip_bgp_peerpass`.

## References
- roles/kubernetes/node/defaults/main.yml
- roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
