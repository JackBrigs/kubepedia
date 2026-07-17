---
id: COMPONENT-FLANNEL
type: component
title: Flannel (CNI)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "0.28.4"
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - flannel
  - flannel cni
  - kube_network_plugin flannel
tags:
  - cni
  - networking
  - flannel
sources:
  - type: code
    path: roles/network_plugin/flannel/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/flannel/defaults/main.yml
    note: "flannel_backend_type: vxlan"
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "flannel_version 0.28.4, flannel_cni_version 1.7.1-flannel1"
relations:
  - type: depends_on
    target: VARIABLE-KUBE_NETWORK_PLUGIN
  - type: see_also
    target: COMPONENT-CALICO
  - type: see_also
    target: CONFIG-CNI_MTU
---

# Flannel (CNI)

## Summary

Flannel is the **simplest** Kubespray CNI option (`kube_network_plugin: flannel`) — a plain L3
overlay with **no NetworkPolicy**. At v2.31.0 it ships **flannel 0.28.4** (flannel-cni
`1.7.1-flannel1`). Default backend is **VXLAN**.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`. Choose it via [[VARIABLE-KUBE_NETWORK_PLUGIN]]; it's the
  minimal alternative to Calico ([[COMPONENT-CALICO]]) / Cilium ([[COMPONENT-CILIUM]]).
- **No NetworkPolicy enforcement** — if you need policy, use Calico/Cilium (or add a policy
  controller).

## Implementation

- Deploys `kube-flannel` as a DaemonSet (Flannel agent + CNI). It gives each node a pod subnet
  and routes pod traffic over the chosen backend.
- Images/version track `flannel_version` (0.28.4) and `flannel_cni_version`.

## Configuration

- **`flannel_backend_type: vxlan`** (default) — encapsulates over UDP 8472; `host-gw` (native
  routing, same L2, no encapsulation) and `wireguard` are alternatives.
- **`flannel_interface`** — pin the host interface on multi-NIC nodes (wrong autodetect breaks
  cross-node traffic).
- MTU follows the backend overhead ([[CONFIG-CNI_MTU]]).

## Compatibility

- **Kubernetes:** flannel 0.28.x supports the base's 1.31–1.35 window.
- **Switching CNI** on a live cluster is disruptive — pick at install; don't flip
  `kube_network_plugin`.
- **No policy / limited features** vs Calico/Cilium — a deliberate simplicity trade-off.

## References

- flannel defaults + download vars (v2.31.0, above); selection:
  [[VARIABLE-KUBE_NETWORK_PLUGIN]]; MTU: [[CONFIG-CNI_MTU]].
