---
id: VARIABLE-KUBE_VIP_ADDRESS
type: variable
title: kube_vip_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_address
tags:
  - kube-vip
  - loadbalancer
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kube_vip_address with an empty (null) default"
relations: []
---

# kube_vip_address

## Summary
Virtual IP address served by kube-vip for the control plane. Default is empty (unset), so it must be provided by the user to enable kube-vip. It is injected into the kube-vip manifest and added to the apiserver certificate SANs.

## Implementation
Default value is empty (the key is declared with no value, i.e. `kube_vip_address:`).

The defining path changed between tags (value unchanged in both locations):

| Tag | Defining path |
|-----|---------------|
| v2.29.0, v2.29.1 | `roles/kubernetes/node/defaults/main.yml` (`kube_vip_address:`) |
| v2.30.0, v2.31.0 | `roles/kubespray_defaults/defaults/main/main.yml` (`kube_vip_address:`) |

Consumed in `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2` (`value: {{ kube_vip_address | to_json }}`) and added to apiserver SANs in `roles/kubernetes/control-plane/tasks/kubeadm-setup.yml` (via `sans_kube_vip_address` in v2.29.x; as `- "{{ kube_vip_address }}"` in v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 - v2.31.0. Related: `kube_vip_enabled`, `kube_vip_controlplane_enabled`, `kube_vip_cidr`, `kube_vip_arp_enabled`.

## References
- roles/kubespray_defaults/defaults/main/main.yml (v2.30.0, v2.31.0); roles/kubernetes/node/defaults/main.yml (v2.29.0, v2.29.1)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
