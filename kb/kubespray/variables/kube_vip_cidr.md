---
id: VARIABLE-KUBE_VIP_CIDR
type: variable
title: kube_vip_cidr
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_cidr
tags:
  - kube-vip
  - networking
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "CIDR prefix length for the kube-vip VIP; default 32"
relations: []
---

# kube_vip_cidr

## Summary
Sets the CIDR prefix length used by kube-vip for the advertised virtual IP address. Default is `32` (a single host address).

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_vip_cidr: 32`. The value is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when `kube_vip_enabled: true`. Related to `kube_vip_interface`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
