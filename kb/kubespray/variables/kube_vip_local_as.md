---
id: VARIABLE-KUBE_VIP_LOCAL_AS
type: variable
title: kube_vip_local_as
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_local_as
tags:
  - kube-vip
  - bgp
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_vip_local_as with default value 65000"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# kube_vip_local_as

## Summary
Local BGP autonomous system number used by kube-vip in BGP mode. Default is `65000`. Rendered into the kube-vip manifest as the `bgp_as` env var.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_vip_local_as: 65000`. Consumed by `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2` (`value: {{ kube_vip_local_as | string | to_json }}`). The default value `65000` is unchanged across v2.29.0-v2.31.0 (line moved from 78 to 76).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Effective only when kube-vip BGP mode is enabled. Related: `kube_vip_bgp_enabled`, `kube_vip_bgp_peeraddress`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
