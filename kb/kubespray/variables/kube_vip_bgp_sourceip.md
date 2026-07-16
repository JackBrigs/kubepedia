---
id: VARIABLE-KUBE_VIP_BGP_SOURCEIP
type: variable
title: kube_vip_bgp_sourceip
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_bgp_sourceip
tags:
  - kube-vip
  - bgp
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Declares the BGP source IP for kube-vip with an empty (null) default; introduced in v2.31.0"
relations: []
---

# kube_vip_bgp_sourceip

## Summary
Source IP address used by kube-vip for BGP peering when BGP mode is enabled. It is declared with no value (empty/null default). It is mutually exclusive with `kube_vip_bgp_sourceif` — the role fails if both are set.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml:89` with an empty value:

```yaml
kube_vip_bgp_sourceip:
```

Normalized in `roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml` (`kube_vip_bgp_sourceip_normalized: "{{ kube_vip_bgp_sourceip | default('', true) | string | trim }}"`) and enforced mutually exclusive with `kube_vip_bgp_sourceif` (fail message: "kube-vip allows only one of kube_vip_bgp_sourceip or kube_vip_bgp_sourceif."). It is rendered into `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2` and documented in the sample inventory `inventory/sample/group_vars/k8s_cluster/addons.yml:202` (commented). This variable was introduced in v2.31.0 — it is absent from v2.29.0, v2.29.1, and v2.30.0.

## Compatibility
Kubespray `v2.31.0` only (not present in v2.29.0-v2.30.0). Effective only when `kube_vip_bgp_enabled` is true; mutually exclusive with `kube_vip_bgp_sourceif`.

## References
- roles/kubernetes/node/defaults/main.yml
- roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
