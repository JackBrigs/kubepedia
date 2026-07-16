---
id: VARIABLE-KUBE_VIP_INTERFACE
type: variable
title: kube_vip_interface
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_interface
tags:
  - kube-vip
  - networking
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Network interface kube-vip binds the VIP to; default empty (unset)"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# kube_vip_interface

## Summary
Specifies the network interface on which kube-vip advertises/binds the virtual IP. Default is empty (no value set), so it must be provided by the user when needed.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_vip_interface:` with an empty (null) default. The default is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when `kube_vip_enabled: true`. Related to `kube_vip_services_interface` and the ARP/BGP options.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
