---
id: VARIABLE-KUBE_VIP_BGP_PEERAS
type: variable
title: kube_vip_bgp_peeras
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_bgp_peeras
tags:
  - kube-vip
  - bgp
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines the default BGP peer AS number 65000 for kube-vip"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# kube_vip_bgp_peeras

## Summary
BGP peer autonomous-system (AS) number used by kube-vip when BGP mode is enabled. The default is `65000`. It is injected into the kube-vip manifest as the `bgp_peeras` environment value.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as:

```yaml
kube_vip_bgp_peeras: 65000
```

Consumed in `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2` as `value: {{ kube_vip_bgp_peeras | string | to_json }}`. The default value `65000` and the path are unchanged across v2.29.0-v2.31.0 (only the line number shifts: 81 in v2.29.0/v2.29.1, 79 in v2.30.0/v2.31.0).

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Effective only when `kube_vip_bgp_enabled` is true; related to `kube_vip_local_as`, `kube_vip_bgp_peeraddress`, `kube_vip_bgp_peerpass`, and `kube_vip_bgp_routerid`.

## References
- roles/kubernetes/node/defaults/main.yml
- roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
