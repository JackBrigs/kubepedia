---
id: CONCEPT-CLUSTER_NETWORKING
type: concept
title: "Cluster networking model (CIDRs, CNI, node prefix, service IP)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cluster networking
  - pod cidr service cidr
  - kube_pods_subnet
  - kube_service_addresses
  - kube_network_node_prefix
  - kube_apiserver_ip
  - kube_network_plugin
tags:
  - networking
  - cni
  - cidr
  - architecture
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_network_plugin/pods_subnet/service_addresses/node_prefix/apiserver_ip (tag v2.31.0)"
relations:
  - type: see_also
    target: CONCEPT-KUBE_PROXY
  - type: see_also
    target: CONFIG-DUAL_STACK
  - type: see_also
    target: CONCEPT-CILIUM_DATAPATH
---

# Cluster networking model (CIDRs, CNI, node prefix, service IP)

## Summary

Kubespray's network model is a handful of CIDRs plus a CNI. **Pods** get IPs from
`kube_pods_subnet`, **Services** (ClusterIP) from `kube_service_addresses`, each node
carves a `/kube_network_node_prefix` slice of the pod CIDR, and the **API service IP** is
derived as the first usable address of the service CIDR. These are **install-time,
cluster-wide** choices — changing them later means re-networking the cluster.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Defaults:
  - `kube_network_plugin: calico` — Kubespray's **default** CNI. (This KB indexes
    **Cilium**; Calico is the default but deferred here — see the backlog.)
  - `kube_pods_subnet: 10.233.64.0/18` — pod IP pool.
  - `kube_service_addresses: 10.233.0.0/18` — Service (ClusterIP) pool.
  - `kube_network_node_prefix: 24` — per-node pod subnet size.
  - `kube_apiserver_ip:` = first usable IP of the service CIDR (`10.233.0.1`) — the
    `kubernetes.default` ClusterIP.
  - `dns_domain: cluster.local`; `kube_proxy_mode: ipvs` ([[CONCEPT-KUBE_PROXY]]).

## Implementation

**How the numbers relate (defaults):**

- Pod CIDR `/18` split into `/24` per node → **up to 64 nodes**, **~254 pods/node**. Raise
  the pod CIDR (e.g. `/16`) or shrink the node prefix for bigger clusters — size it before
  install.
- Service CIDR `/18` → ~16k Service ClusterIPs.
- Pod and Service CIDRs must **not overlap** each other, the node/LAN networks, or (for
  overlays) the underlay — a common cause of mysterious routing failures.
- `kube_apiserver_ip` (`10.233.0.1`) is what in-cluster clients reach as
  `kubernetes.default.svc`; it lives in the service CIDR.

**Where the CNI fits:**

- The CNI (`kube_network_plugin`) implements pod networking within these CIDRs — overlay
  (VXLAN) or native routing, plus NetworkPolicy. Cilium specifics:
  [[CONCEPT-CILIUM_DATAPATH]].
- `kube_proxy_mode` (or a CNI kube-proxy replacement) implements Service routing on top.

## Compatibility

- **Install-time decision:** pod/service CIDRs and node prefix are effectively immutable
  after install — plan for growth up front (node count × pods/node).
- **Dual-stack** adds IPv6 CIDRs alongside these ([[CONFIG-DUAL_STACK]]).
- The default CNI is **Calico**; set `kube_network_plugin: cilium` for the CNI this KB
  documents. Multus (`kube_network_plugin_multus`) layers multiple CNIs (off by default).
- CIDR overlaps with existing infrastructure are the classic post-install networking bug —
  verify against your LAN/VPC ranges before deploying.

## References

- `kube_network_plugin` / CIDR / node-prefix / `kube_apiserver_ip` at tag `v2.31.0`.
  kube-proxy: [[CONCEPT-KUBE_PROXY]]; Cilium datapath: [[CONCEPT-CILIUM_DATAPATH]];
  dual-stack: [[CONFIG-DUAL_STACK]].
