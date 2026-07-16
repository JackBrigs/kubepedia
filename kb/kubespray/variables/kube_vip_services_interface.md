---
id: VARIABLE-KUBE_VIP_SERVICES_INTERFACE
type: variable
title: kube_vip_services_interface
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_services_interface
tags:
  - kube-vip
  - loadbalancer
  - network
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Network interface for kube-vip service mode, empty default"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# kube_vip_services_interface

## Summary
The host network interface that kube-vip uses when running in service (LoadBalancer) mode. Defined with no value (null/unset) by default, so kube-vip falls back to its own interface detection unless the user sets it.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_vip_services_interface:` (an empty default, i.e. null). The value is unchanged across v2.29.0-v2.31.0; only the line number shifts (line 68 in v2.29.0/v2.29.1, line 66 in v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant when `kube_vip_services_enabled: true`. Related variables: `kube_vip_services_enabled`, `kube_vip_interface`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
