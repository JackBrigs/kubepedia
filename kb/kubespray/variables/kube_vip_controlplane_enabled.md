---
id: VARIABLE-KUBE_VIP_CONTROLPLANE_ENABLED
type: variable
title: kube_vip_controlplane_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_controlplane_enabled
tags:
  - kube-vip
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Enables kube-vip control-plane VIP; default false"
relations: []
---

# kube_vip_controlplane_enabled

## Summary
Enables the kube-vip control-plane virtual IP function (VIP for the Kubernetes API server). Default is `false`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_vip_controlplane_enabled: false`. The value is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Takes effect only when `kube_vip_enabled: true`. Related to `kube_vip_lb_enable`, `kube_vip_arp_enabled`, and `kube_vip_bgp_enabled`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
